#!/usr/bin/env python3
"""Regenerate PORTFOLIO.md from a template, articles.yaml, and git log.

Usage:
    python scripts/gen_portfolio.py           # write PORTFOLIO.md
    python scripts/gen_portfolio.py --check   # verify PORTFOLIO.md is up to date (exit 1 if stale)

Template: scripts/portfolio_template.md. PORTFOLIO.md is generated output —
never edit it by hand. Placeholders filled by this script:

    {{ARTICLE_COUNT}}   number of unique published articles (by YYMMDD in articles.yaml)
    {{LATEST_COMMIT}}   subject + month of the latest commit on HEAD
    {{LATEST_ARTICLES}} top N published articles (title, month, description)
    {{LAST_UPDATED}}    today's date
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime, date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "articles.yaml"
TEMPLATE = ROOT / "scripts" / "portfolio_template.md"
PORTFOLIO = ROOT / "PORTFOLIO.md"
LATEST_N = 6

DATE_RE = re.compile(r"(\d{6})-")


def load_manifest() -> dict:
    with MANIFEST.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def article_count(data: dict) -> int:
    dates = set()
    for row in data["rows"]:
        if row.get("status") != "published":
            continue
        for ln in row["links"]:
            m = DATE_RE.match(ln["path"].rsplit("/", 1)[-1])
            if m:
                dates.add(m.group(1))
    return len(dates)


def latest_commit() -> str:
    out = subprocess.run(
        ["git", "log", "-1", "--date=format:%b %Y", "--format=%s|%ad"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    subject, _, stamp = out.partition("|")
    return f"`{subject}` ({stamp})"


def doc_title(path: Path, fallback: str) -> str:
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except OSError:
        pass
    return fallback


def latest_articles(data: dict, n: int = LATEST_N) -> str:
    cands = []
    seen_dates = set()
    for row in data["rows"]:
        if row.get("status") != "published":
            continue
        en = next((ln for ln in row["links"] if ln.get("lang") == "en"), None)
        ln = en or row["links"][0]
        m = DATE_RE.match(ln["path"].rsplit("/", 1)[-1])
        if not m:
            continue
        date_key = m.group(1)
        if date_key in seen_dates:
            continue
        seen_dates.add(date_key)
        d = datetime.strptime(date_key, "%y%m%d")
        title = doc_title(ROOT / ln["path"], ln["label"])
        desc = row.get("desc_en") or row.get("desc_zh") or ""
        cands.append((d, title, desc))
    cands.sort(key=lambda c: c[0], reverse=True)
    return "\n".join(
        f'{i}. **"{title}"** ({d.strftime("%b %Y")}) — {desc}'
        for i, (d, title, desc) in enumerate(cands[:n], start=1)
    )


def last_updated() -> str:
    today = date.today()
    return f"{today:%B} {today.day}, {today.year}"


def render(data: dict) -> str:
    out = TEMPLATE.read_text(encoding="utf-8")
    values = {
        "ARTICLE_COUNT": str(article_count(data)),
        "LATEST_COMMIT": latest_commit(),
        "LATEST_ARTICLES": latest_articles(data),
        "LAST_UPDATED": last_updated(),
    }
    for key, value in values.items():
        out = out.replace("{{" + key + "}}", value)
    leftover = sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", out)))
    if leftover:
        print(f"error: unfilled placeholders: {leftover}", file=sys.stderr)
        sys.exit(1)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="verify PORTFOLIO.md is up to date")
    args = ap.parse_args()

    data = load_manifest()
    generated = render(data)

    if args.check:
        current = PORTFOLIO.read_text(encoding="utf-8") if PORTFOLIO.exists() else None
        if current != generated:
            print("stale: PORTFOLIO.md is out of date — run python scripts/gen_portfolio.py")
            return 1
        return 0

    PORTFOLIO.write_text(generated, encoding="utf-8")
    print(f"wrote PORTFOLIO.md ({len(generated.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
