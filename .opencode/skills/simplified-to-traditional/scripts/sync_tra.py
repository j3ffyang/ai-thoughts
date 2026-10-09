#!/usr/bin/env python3
"""Sync a Simplified-Chinese ai-thoughts article to its Traditional-Chinese twin.

Source of truth : docs/<YYMMDD-slug>-zh-hans.md   (bare .md here is English; -chn.md is legacy)
Generated twin  : docs/<YYMMDD-slug>-zh-hant.md

What it does:
  * injects / refreshes the permanent cross-link under the H1 in BOTH files
  * converts the body with OpenCC (s2twp)
  * writes the -zh-hant twin

Usage:
    python3 sync_tra.py docs/<slug>-zh-hans.md            # write / update the twin
    python3 sync_tra.py docs/<slug>-zh-hans.md --check    # exit 1 if the pair is stale
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

GITHUB = "https://github.com/j3ffyang/ai-thoughts/blob/main/docs/"
LINK_RE = re.compile(r"^>\s*(?:繁體版|簡體版|繁体版|简体版)\s*[：:]")
H1_RE = re.compile(r"^#\s+(\S.*\S|\S)\s*$")
OPENCC = ["opencc", "-c", "s2twp.json"]

# Post-OpenCC pins: OpenCC's phrase dictionary renders some terms inconsistently
# between occurrences. Each (from, to) pair is applied in order to the converted
# Traditional text. Keep this list small and specific; it survives every re-sync.
OVERRIDES = [
    ("作者自雲", "作者自云"),  # 云 = "says" (作者自云), not 雲 "cloud"
    ("幹血之症", "乾血之症"),  # 乾 = dry (干血 = dry blood, a TCM condition); OpenCC picked 幹
]

# One-Simplified-to-many-Traditional forms where OpenCC can pick the wrong
# variant for a rare/literary/technical term (e.g. 云→雲, 干→幹). We never
# auto-fix these; after each sync we print every occurrence so a reviewer can
# verify it against the cited edition (or the intended meaning) and, if wrong,
# pin a fix in OVERRIDES. Kept to forms whose wrong pick is plausible and
# costly; common correct forms (與/後/裡/為/著…) are deliberately excluded so
# the lint stays low-noise.
HOT_LIST = "雲幹髮複隻係繫錶製鬥穀餘鬆瀋鍾劃衝儘麵臺噁鬱鹹纖兇僕"


def lint_traditional(text: str) -> list[str]:
    """Return one warning per risky Traditional form found, with context."""
    warnings: list[str] = []
    for i, line in enumerate(text.split("\n"), 1):
        for j, ch in enumerate(line):
            if ch in HOT_LIST:
                lo, hi = max(0, j - 6), min(len(line), j + 7)
                warnings.append(f"line {i}: {ch}  …{line[lo:hi]}…")
    return warnings


def apply_overrides(text: str) -> str:
    for src, dst in OVERRIDES:
        text = text.replace(src, dst)
    return text


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def h1_title(text: str) -> str:
    for line in text.split("\n"):
        m = H1_RE.match(line)
        if m:
            return m.group(1).strip()
    return ""


def strip_link_lines(text: str) -> str:
    return "\n".join(ln for ln in text.split("\n") if not LINK_RE.match(ln))


def with_link(text: str, link: str) -> str:
    """Remove any existing cross-link lines, then put `link` directly under the H1."""
    lines = strip_link_lines(text).split("\n")
    out: list[str] = []
    inserted = False
    for line in lines:
        out.append(line)
        if not inserted and H1_RE.match(line):
            out.append("")
            out.append(link)
            inserted = True
    if not inserted:
        out = [link, ""] + out
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.rstrip("\n") + "\n"


def to_traditional(text: str) -> str:
    proc = subprocess.run(
        OPENCC, input=text.encode("utf-8"), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if proc.returncode != 0:
        sys.exit(f"opencc failed: {proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8")


def twin_path(src: Path) -> Path:
    name = src.name
    if name.endswith("-zh-hans.md"):
        return src.with_name(name[: -len("-zh-hans.md")] + "-zh-hant.md")
    sys.exit(f"unrecognized source filename: {name} (expected <YYMMDD-slug>-zh-hans.md)")


def build(src: Path) -> tuple[str, str, Path, str]:
    """Return (src_text, src_with_link, twin_path, twin_text)."""
    src_text = read(src)
    twin = twin_path(src)

    src_title = h1_title(src_text)
    src_link = f"> 繁体版：[{src_title}]({GITHUB}{twin.name})"
    src_out = with_link(src_text, src_link)

    body = strip_link_lines(src_text)
    tra_body = apply_overrides(to_traditional(body))
    tra_title = h1_title(tra_body)
    tra_link = f"> 簡體版：[{tra_title}]({GITHUB}{src.name})"
    twin_out = with_link(tra_body, tra_link)

    return src_text, src_out, twin, twin_out


def report_lint(warnings: list[str]) -> None:
    if not warnings:
        return
    print(f"⚠ {len(warnings)} ambiguous form(s) to verify — pin a fix in OVERRIDES if wrong:")
    for w in warnings:
        print("  -", w)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="path to the <YYMMDD-slug>-zh-hans.md Simplified article")
    ap.add_argument("--check", action="store_true", help="report drift; do not write")
    args = ap.parse_args()

    src = Path(args.source)
    if not src.is_file():
        sys.exit(f"source not found: {src}")

    src_text, src_out, twin, twin_out = build(src)
    lint = lint_traditional(twin_out)

    if args.check:
        problems: list[str] = []
        if read(src) != src_out:
            problems.append(f"{src.name}: cross-link missing, stale, or needs normalizing")
        if not twin.is_file():
            problems.append(f"{twin.name}: missing")
        elif read(twin) != twin_out:
            problems.append(f"{twin.name}: out of sync with {src.name}")
        if problems:
            print("FAIL: not in sync")
            for p in problems:
                print("  -", p)
            report_lint(lint)
            return 1
        print(f"OK: {src.name} and {twin.name} are in sync")
        report_lint(lint)
        return 0

    wrote: list[str] = []
    if read(src) != src_out:
        src.write_text(src_out, encoding="utf-8")
        wrote.append(src.name)
    twin.write_text(twin_out, encoding="utf-8")
    wrote.append(twin.name)
    print("wrote:", ", ".join(wrote))
    report_lint(lint)
    return 0


if __name__ == "__main__":
    sys.exit(main())
