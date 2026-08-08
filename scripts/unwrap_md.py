#!/usr/bin/env python3
"""Unwrap hard-wrapped Markdown prose into single-line paragraphs (auto-wrap).

Usage:
    python scripts/unwrap_md.py [path ...]    # unwrap given .md files (default: docs/ + .opencode/skills)
    python scripts/unwrap_md.py --check       # exit 1 if any scanned file still needs unwrapping

Structural elements are preserved verbatim: fenced code blocks, tables,
headings, horizontal rules, blockquotes, list items, and YAML frontmatter.
Paragraph prose and wrapped list-item continuations are joined into one line;
CJK-to-CJK joins use no space, everything else a single space.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\S")
HEADING = re.compile(r"^#{1,6}\s")
HR = re.compile(r"^(?:---|\*\*\*|___)\s*$")
FENCE = re.compile(r"^\s*(?:```|~~~)")
CLOSE_FENCE = re.compile(r"^\s*(?:```|~~~)\s*$")
TABLE = re.compile(r"^\s*\|")
PIPE = re.compile(r"\|")


def glue(a: str, b: str) -> str:
    a_end = a[-1:]
    b_start = b[:1]
    if CJK.match(a_end) and CJK.match(b_start):
        return ""
    return " "


def join_prose(run: list[str]) -> list[str]:
    out: list[str] = []
    acc = ""
    for ln in run:
        if ln.startswith("    "):
            if acc:
                out.append(acc)
            out.append(ln)
            acc = ""
            continue
        if not acc:
            lead = ln[: len(ln) - len(ln.lstrip())]
            acc = lead + ln.strip()
        else:
            s = ln.strip()
            acc += glue(acc, s) + s
    if acc:
        out.append(acc)
    return out


def join_list_run(run: list[str]) -> list[str]:
    out: list[str] = []
    cur: str | None = None
    for ln in run:
        if ln.startswith("    "):
            if cur is not None:
                out.append(cur)
            out.append(ln)
            cur = None
            continue
        if LIST_ITEM.match(ln):
            if cur is not None:
                out.append(cur)
            cur = ln.rstrip()
        elif cur is not None:
            s = ln.strip()
            cur += glue(cur, s) + s
        else:
            out.extend(join_prose([ln]))
    if cur is not None:
        out.append(cur)
    return out


def unwrap(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i, n = 0, len(lines)

    if lines and lines[0].strip() == "---":
        out.append(lines[0])
        i = 1
        while i < n and lines[i].strip() != "---":
            out.append(lines[i])
            i += 1
        if i < n:
            out.append(lines[i])
            i += 1

    in_fence = False
    while i < n:
        ln = lines[i]
        s = ln.strip()
        if in_fence:
            out.append(ln)
            if CLOSE_FENCE.match(ln):
                in_fence = False
            i += 1
            continue
        if FENCE.match(s):
            in_fence = True
            out.append(ln)
            i += 1
            continue
        if not s:
            out.append(ln)
            i += 1
            continue
        if HEADING.match(s) or HR.match(s) or TABLE.match(s) or PIPE.search(s) or s.startswith("<!--") or s.startswith("!["):
            out.append(ln)
            i += 1
            continue
        if s.startswith(">"):
            out.append(ln)
            i += 1
            continue
        run = []
        while i < n:
            li = lines[i]
            si = li.strip()
            if (
                not si
                or HEADING.match(si)
                or HR.match(si)
                or TABLE.match(si)
                or PIPE.search(si)
                or FENCE.match(si)
                or si.startswith(">")
                or si.startswith("<!--")
                or si.startswith("![")
            ):
                break
            run.append(li)
            i += 1
        if any(LIST_ITEM.match(l) for l in run):
            out.extend(join_list_run(run))
        else:
            out.extend(join_prose(run))
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def scan() -> list[Path]:
    paths = [*(ROOT / "docs").glob("*.md"), *(ROOT / ".opencode" / "skills").glob("*/SKILL.md")]
    return [p for p in paths if unwrap(p.read_text(encoding="utf-8")) != p.read_text(encoding="utf-8")]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="*", help="files to unwrap (default: all docs/ and .opencode/skills)")
    ap.add_argument("--check", action="store_true", help="exit 1 if any scanned file still needs unwrapping")
    args = ap.parse_args()

    targets = [ROOT / p for p in args.paths] if args.paths else scan_source()
    changed = [p for p in targets if p.exists() and unwrap(p.read_text(encoding="utf-8")) != p.read_text(encoding="utf-8")]

    if args.check:
        if changed:
            for p in changed:
                print(f"wrapped: {p.relative_to(ROOT)}")
            return 1
        return 0

    for p in changed:
        p.write_text(unwrap(p.read_text(encoding="utf-8")), encoding="utf-8")
        rel = p.relative_to(ROOT) if ROOT in p.parents else p
        print(f"unwrapped {rel}")
    print(f"{len(changed)} file(s) updated")
    return 0


def scan_source() -> list[Path]:
    return [*(ROOT / "docs").glob("*.md"), *(ROOT / ".opencode" / "skills").glob("*/SKILL.md")]


if __name__ == "__main__":
    sys.exit(main())
