#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = ["mcp", "tradingview-screener"]
# ///
"""TradingView MCP — quotes, technical ratings, and screens.

TradingView publishes no official API. This drives the same scanner endpoint
its own web app uses, through the `tradingview-screener` client: read-only,
no login, no cookies. It is personal-use tooling — the data is TradingView's,
and the endpoints can change without notice.

Three tools:

  tv_quote(symbols, market)   price, change, volume, market cap, rating
  tv_rating(symbol, interval) technical rating split into MA and oscillators
  tv_screen(filters, ...)     market-wide queries with typed filters
"""

from __future__ import annotations

import json
import operator
from typing import Any

from mcp.server.mcpserver import MCPServer
from tradingview_screener import Column, Query
from tradingview_screener import screeners

mcp = MCPServer("tradingview")

# Interval suffix used by the scanner's field names. "" is the daily default.
INTERVALS = {
    "1m": "|1", "5m": "|5", "15m": "|15", "30m": "|30",
    "1h": "|60", "2h": "|120", "4h": "|240",
    "1D": "", "1W": "|1W", "1M": "|1M",
}

# Fields the model may filter on. Deliberately short: every name here is one
# the scanner actually serves, so a typo fails loudly instead of returning junk.
FIELDS = {
    "close": "last price",
    "change": "percent change today",
    "volume": "volume today",
    "market_cap_basic": "market capitalisation",
    "RSI": "relative strength index (14)",
    "Recommend.All": "technical rating, -1 sell … +1 buy",
    "Recommend.MA": "rating from moving averages",
    "Recommend.Other": "rating from oscillators",
    "price_earnings_ttm": "trailing P/E",
    "average_volume_10d_calc": "10-day average volume",
    "sector": "sector name",
    "typespecs": "instrument kinds, e.g. ['common'] — use op \"has\"",
}

OPS = {
    "<": operator.lt, "<=": operator.le, ">": operator.gt,
    ">=": operator.ge, "==": operator.eq, "!=": operator.ne,
}
LIST_OPS = {"has": "has", "not_has": "has_none_of"}


STOCK_EXCHANGES = ("NASDAQ", "NYSE", "AMEX")
CRYPTO_EXCHANGES = ("BINANCE", "COINBASE")


def _candidates(symbol: str, market: str) -> list[str]:
    """Expand a bare symbol into EXCHANGE:TICKER candidates, in preference order.

    The scanner only speaks qualified tickers, so "AAPL" resolves to
    NASDAQ:AAPL by trying the exchanges in order in one request. A ticker that
    already carries a colon is left alone.
    """
    s = symbol.strip().upper()
    if not s:
        return []
    if ":" in s:
        return [s]
    if market == "crypto":
        pair = s if s.endswith(("USDT", "USD", "USDC")) else s + "USDT"
        out = [f"BINANCE:{pair}"]
        if pair.endswith("USDT"):
            out.append(f"COINBASE:{pair[:-1]}")   # BTCUSDT -> COINBASE:BTCUSD
        return out
    return [f"{ex}:{s}" for ex in STOCK_EXCHANGES]


def _base(market: str) -> Query:
    return screeners.crypto() if market == "crypto" else Query()


def _field(name: str, interval: str = "1D") -> Column:
    if name not in FIELDS:
        raise ValueError(f"unknown field {name!r}; allowed: {', '.join(sorted(FIELDS))}")
    suffix = INTERVALS.get(interval)
    if suffix is None:
        raise ValueError(f"unknown interval {interval!r}; allowed: {', '.join(INTERVALS)}")
    # Only the rating fields are timeframe-specific.
    if name.startswith("Recommend."):
        return Column(name + suffix)
    return Column(name)


def _human(n: float) -> str:
    for unit, div in (("T", 1e12), ("B", 1e9), ("M", 1e6), ("K", 1e3)):
        if abs(n) >= div:
            return f"{n / div:.2f}{unit}"
    return f"{n:.0f}"


def _fmt(col: str, v: Any) -> str:
    """Numbers are rounded at the edge: a scanner returns 15 digits, a reader
    needs two."""
    if v is None:
        return "-"
    if isinstance(v, str):
        return v
    try:
        f = float(v)
    except (TypeError, ValueError):
        return str(v)
    if f != f:  # NaN
        return "-"
    if col == "market_cap_basic":
        return _human(f)
    if col == "volume":
        return f"{int(f):,}"
    return f"{f:.2f}"


def _table(df: Any) -> str:
    """Render a DataFrame as a compact fixed-width table."""
    if df is None or len(df) == 0:
        return "no rows"
    head = list(df.columns)
    rows = [[_fmt(c, v) for c, v in zip(head, r)] for r in df.itertuples(index=False)]
    widths = [max(len(str(h)), *(len(r[i]) for r in rows)) for i, h in enumerate(head)]
    line = "  ".join(str(h).ljust(widths[i]) for i, h in enumerate(head))
    out = [line, "  ".join("-" * w for w in widths)]
    for r in rows:
        out.append("  ".join(v.ljust(widths[i]) for i, v in enumerate(r)))
    return "\n".join(out)


@mcp.tool()
def tv_quote(symbols: str, market: str = "stock") -> str:
    """Price, change, volume, market cap and technical rating for one or more symbols.

    symbols: comma- or space-separated, e.g. "NASDAQ:AAPL, NASDAQ:NVDA".
    market: "stock" (default) or "crypto" (e.g. BINANCE:BTCUSDT).
    Bare tickers work: "AAPL" resolves to NASDAQ:AAPL, "BTC" to BINANCE:BTCUSDT.
    """
    if market not in ("stock", "crypto"):
        return f"unknown market {market!r}; use 'stock' or 'crypto'"
    wanted = [t.strip() for t in symbols.replace(",", " ").split() if t.strip()]
    if not wanted:
        return "give at least one symbol"

    flat: list[str] = []
    for w in wanted:
        flat.extend(_candidates(w, market))
    q = (_base(market)
         .set_tickers(*flat[:60])
         .select("name", "close", "change", "volume", "market_cap_basic", "Recommend.All"))
    _, df = q.get_scanner_data()
    if df is None or len(df) == 0:
        return f"no data for {', '.join(wanted)}"

    # One row per requested symbol, in the order asked, using the first
    # candidate that exists (NASDAQ before NYSE, BINANCE before COINBASE).
    rows = []
    for w in wanted:
        bare = w.split(":")[-1].upper()
        for pref in _candidates(w, market):
            hit = df[df["ticker"] == pref]
            if len(hit):
                rows.append(hit.iloc[0])
                break
        else:
            match = df[df["name"].str.upper() == bare]
            if len(match):
                rows.append(match.iloc[0])
    if not rows:
        return f"no data for {', '.join(wanted)}"
    return _table(__import__("pandas").DataFrame(rows).reset_index(drop=True))


@mcp.tool()
def tv_rating(symbol: str, interval: str = "1D", market: str = "stock") -> str:
    """Technical rating for one symbol: overall, moving averages, oscillators.

    interval: 1m, 5m, 15m, 30m, 1h, 2h, 4h, 1D (default), 1W, 1M.
    A rating runs -1 (sell) to +1 (buy); the three columns rarely agree, and
    that disagreement is usually the interesting part.
    """
    if interval not in INTERVALS:
        return f"unknown interval {interval!r}; use one of {', '.join(INTERVALS)}"
    cands = _candidates(symbol, market)
    q = (_base(market)
         .set_tickers(*cands)
         .select("name", "close", "Recommend.All", "Recommend.MA", "Recommend.Other"))
    _, df = q.get_scanner_data()
    if df is None or len(df) == 0:
        return f"no data for {symbol!r}"
    order = {c: i for i, c in enumerate(cands)}
    df = df.sort_values("ticker", key=lambda s: s.map(lambda x: order.get(x, 99)))

    def verdict(v: float) -> str:
        if v is None:
            return "n/a"
        if v >= 0.5:
            return "strong buy"
        if v >= 0.1:
            return "buy"
        if v <= -0.5:
            return "strong sell"
        if v <= -0.1:
            return "sell"
        return "neutral"

    row = df.iloc[0]
    overall = float(row["Recommend.All"])
    return (
        f"{symbol}  close {row['close']}  interval {interval}\n"
        f"  overall       {overall:+.3f}  ({verdict(overall)})\n"
        f"  moving avgs   {float(row['Recommend.MA']):+.3f}\n"
        f"  oscillators   {float(row['Recommend.Other']):+.3f}"
    )


@mcp.tool()
def tv_screen(filters: str = "", market: str = "stock", limit: int = 20,
              sort_by: str = "", desc: bool = True) -> str:
    """Screen the market with typed filters.

    filters: JSON list, each {"field": ..., "op": ..., "value": ...}.
      ops: <, <=, >, >=, ==, !=  — or "between" with value [low, high]
      fields: close, change, volume, market_cap_basic, RSI, Recommend.All,
              Recommend.MA, Recommend.Other, price_earnings_ttm,
              average_volume_10d_calc, sector, typespecs
      list ops: "has" / "not_has" for typespecs
    Example: [{"field":"RSI","op":"<","value":30},
              {"field":"market_cap_basic","op":">","value":10000000000}]
    limit: rows to return (max 100).
    sort_by: a field name; defaults to market cap for stocks, volume for crypto.
    """
    if market not in ("stock", "crypto"):
        return f"unknown market {market!r}; use 'stock' or 'crypto'"

    parsed: list[dict] = []
    if filters.strip():
        try:
            parsed = json.loads(filters)
        except json.JSONDecodeError as exc:
            return f"filters is not valid JSON: {exc}"
        if not isinstance(parsed, list):
            return "filters must be a JSON list"

    # Each condition is collected, then passed to where() once: a second
    # where() call replaces the filter rather than adding to it, so chaining
    # silently keeps only the last condition.
    conds: list[Any] = []
    for f in parsed:
        if not isinstance(f, dict) or "field" not in f or "op" not in f:
            return 'each filter needs "field" and "op" (and usually "value")'
        try:
            col = _field(f["field"])
        except ValueError as exc:
            return str(exc)
        op, value = f["op"], f.get("value")
        try:
            if op == "between":
                low, high = value
                conds.append(col.between(low, high))
            elif op in LIST_OPS:
                conds.append(getattr(col, LIST_OPS[op])(value))
            elif op in OPS:
                conds.append(OPS[op](col, value))
            else:
                return f"unknown op {op!r}; use one of {', '.join(OPS)} or 'between'"
        except (TypeError, ValueError) as exc:
            return f"bad value for {f['field']}: {exc}"

    # A stock screen without this returns preferred shares and ETFs, which look
    # like common stock until the ticker suffix gives them away.
    implicit = []
    if market == "stock" and not any(f.get("field") == "typespecs" for f in parsed):
        implicit.append(Column("typespecs").has("common"))

    q = _base(market)
    if conds or implicit:
        q = q.where(*conds, *implicit)

    sort_field = sort_by or ("volume" if market == "crypto" else "market_cap_basic")
    try:
        sort_col = _field(sort_field)
    except ValueError as exc:
        return str(exc)

    n = max(1, min(int(limit), 100))
    q = q.select("name", "close", "change", "volume", "RSI", "Recommend.All")
    q = q.order_by(sort_col, ascending=not desc).limit(n)
    _, df = q.get_scanner_data()
    out = _table(df)
    if implicit:
        out += "\n\n(common stock only; add a typespecs filter to widen it)"
    return out


if __name__ == "__main__":
    mcp.run()
