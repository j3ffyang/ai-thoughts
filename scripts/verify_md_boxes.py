#!/usr/bin/env python3
"""Verify ASCII/box diagrams inside fenced Markdown code blocks are square.

Usage:
    python scripts/verify_md_boxes.py [path ...]   # check given .md files/dirs
    python scripts/verify_md_boxes.py --check      # exit 1 if any box is misaligned

Default scan: `docs/*.md` and `.opencode/skills/*/SKILL.md` (same set as
`scripts/unwrap_md.py`).

A box is a line inside a fenced code block that draws part of a box:
  * a border row  — contains a corner (┌ ┐ └ ┘)
  * a content row — contains two or more walls (│)

For a single-width block (all corners share one span), every content row's
walls must line up with that span. Rows with a single │ (arrow connectors) are
ignored, and blocks with nested / mixed-width boxes are out of scope. A block
whose opening fence carries the token `no-box-check` is skipped.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FENCE = ("```", "~~~")
HORIZ = set("┌┐└┘─┬┴├┤┼")
CORNERS = set("┌┐└┘")
WALL = "│"


def span(line: str) -> tuple[int, int]:
    cols = [i for i, c in enumerate(line) if c in HORIZ or c == WALL]
    return min(cols), max(cols)


def check_block(block: list[str], offset: int) -> list[tuple[int, int, int, int, int]]:
    if not any("┌" in ln and "┐" in ln for ln in block):
        return []
    corner_spans = {span(ln) for ln in block if any(c in ln for c in CORNERS)}
    if len(corner_spans) != 1:
        return []  # nested / mixed-width diagrams are out of scope (use no-box-check)
    want = next(iter(corner_spans))
    problems: list[tuple[int, int, int, int, int]] = []
    for i, ln in enumerate(block):
        if any(c in ln for c in CORNERS) or ln.count(WALL) >= 2:
            a, b = span(ln)
            if (a, b) != want:
                problems.append((offset + i + 1, a, b, want[0], want[1]))
    return problems


def check_file(path: Path) -> list[tuple[int, int, int, int, int]]:
    problems: list[tuple[int, int, int, int, int]] = []
    lines = path.read_text(encoding="utf-8").split("\n")
    in_fence = False
    fence_info = ""
    block: list[str] = []
    block_start = 0
    for i, ln in enumerate(lines):
        s = ln.strip()
        if in_fence:
            if s.startswith(FENCE):
                if "no-box-check" not in fence_info:
                    problems += check_block(block, block_start)
                in_fence = False
                block = []
            else:
                block.append(ln)
            continue
        if s.startswith(FENCE):
            in_fence = True
            fence_info = s
            block = []
            block_start = i + 1
    return problems


def scan() -> list[Path]:
    return [*(ROOT / "docs").glob("*.md"), *(ROOT / ".opencode" / "skills").glob("*/SKILL.md")]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="*", help="files/dirs to check (default: docs/ and .opencode/skills)")
    ap.add_argument("--check", action="store_true", help="exit 1 if any box diagram is misaligned")
    args = ap.parse_args()

    if args.paths:
        targets: list[Path] = []
        for p in args.paths:
            q = Path(p) if Path(p).is_absolute() else ROOT / p
            if q.is_dir():
                targets += sorted(q.rglob("*.md"))
            elif q.exists():
                targets.append(q)
    else:
        targets = scan()

    found = False
    for path in targets:
        for lineno, a, b, wl, wr in check_file(path):
            found = True
            rel = path.relative_to(ROOT) if ROOT in path.parents else path
            print(f"misaligned box: {rel}:{lineno} (cols {a}-{b}, expected {wl}-{wr})")

    if args.check:
        return 1 if found else 0
    if not found:
        print(f"all box diagrams aligned ({len(targets)} file(s) checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
