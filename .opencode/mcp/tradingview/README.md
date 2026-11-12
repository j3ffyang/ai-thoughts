# tradingview MCP

Quotes, technical ratings and market screens from TradingView's scanner, exposed as three MCP tools. Read-only, no login, no cookies.

TradingView publishes **no official API**. This drives the same scanner endpoint its web app uses, through the [`tradingview-screener`](https://pypi.org/project/tradingview-screener/) client. Personal-use tooling: the data is TradingView's, the endpoints can change without notice, and nothing here should be redistributed.

## Tools

| Tool | Arguments | Returns |
|---|---|---|
| `tv_quote` | `symbols` (comma or space separated), `market` (`stock` / `crypto`) | price, change, volume, market cap, technical rating |
| `tv_rating` | `symbol`, `interval` (`1m`…`1M`, default `1D`), `market` | overall rating, split into moving averages and oscillators |
| `tv_screen` | `filters` (JSON), `market`, `limit` (≤100), `sort_by`, `desc` | matching rows, sorted |

A rating runs −1 (sell) to +1 (buy). The three columns rarely agree, and the disagreement is usually the point.

### Filters

```json
[
  {"field": "RSI", "op": "<", "value": 25},
  {"field": "market_cap_basic", "op": ">", "value": 10000000000}
]
```

Ops: `<`, `<=`, `>`, `>=`, `==`, `!=`, `between` (value `[low, high]`), and `has` / `not_has` for `typespecs`.

Fields: `close`, `change`, `volume`, `market_cap_basic`, `RSI`, `Recommend.All`, `Recommend.MA`, `Recommend.Other`, `price_earnings_ttm`, `average_volume_10d_calc`, `sector`, `typespecs`.

Stock screens add `typespecs has 'common'` unless you filter on `typespecs` yourself — without it the results fill with preferred shares (`BAC/PE`) that look like ordinary tickers.

## Examples

Bare tickers resolve: `AAPL` → `NASDAQ:AAPL`, `BTC` → `BINANCE:BTCUSDT`. The scanner itself only speaks qualified tickers, so the tool tries NASDAQ, NYSE and AMEX in one request and keeps the hit; a ticker that already has a colon is used as given.

```
tv_quote("NASDAQ:AAPL, NASDAQ:NVDA")
tv_rating("NASDAQ:NVDA", "4h")
tv_screen('[{"field":"RSI","op":"<","value":25}]', limit=10)
tv_quote("BINANCE:BTCUSDT", market="crypto")
```

## Registration

```jsonc
"mcp": {
  "servers": {
    "tradingview": {
      "type": "local",
      "command": [
        "uv", "run",
        "/home/jeff/pool/git/negtivSpace/ai-thoughts/.opencode/mcp/tradingview/server.py"
      ],
      "enabled": true
    }
  }
}
```

`server.py` declares its dependencies inline (PEP 723), so `uv run` fetches `mcp` and `tradingview-screener` per launch — nothing is installed, no venv is created. MCP servers load at client startup, so restart the client after adding the entry.

`opencode mcp list` reads only the global config; a project-level entry is used by sessions but not listed there.

## What it does not do

- No chart data. OHLCV history belongs to a different endpoint and a different library; this tool answers "what is it doing now", not "draw me a candle chart".
- No watchlists, alerts or ideas. Those need a logged-in session, and cookies in a config file are a different risk class.
- No writing anything. Every tool is a read.

## Verified

Against `tradingview-screener` 3.2.2, 2026-11-11: quotes for US equities and `BINANCE:` crypto pairs, ratings across `1h` and `1W` (the scanner takes a
timeframe suffix, `Recommend.All|60`), multi-condition screens, and the
common-stock default that removes preferred shares.
