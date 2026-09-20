#!/usr/bin/env python3
"""audit_pptx.py — 5-point losslessness audit for an extraction.

Compares the generated extracted/<stem>.md + extracted/assets/<stem>/ against the
source source/<stem>.pptx. Exit code 1 if any hard check fails.

Usage:
    "$PY" tools/audit_pptx.py [--project DIR] <file.pptx | stem>

Checks:
    1. slide markers in the .md == slide count in the source
    2. every media blob in the source is explained (extracted, layout chrome,
       or a vector metafile) — "unexplained" must be 0
    3. every image reference in the .md resolves on disk
    4. every <a:t> string in slide + notes XML appears in the .md (text completeness)
    5. visible "unextractable" notes are reported (metafile/chart/OLE count)
"""

import argparse
import html
import re
import sys
from pathlib import Path
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_pptx import resolve_source  # noqa: E402

WORK_DIR = Path(__file__).resolve().parent.parent


def is_metafile(blob):
    """Windows metafile signatures: EMF (01 00 00 00), placeable WMF (D7 CD C6 9A),
    and standard WMF (01|02 00 09 00)."""
    return blob[:4] in (
        b"\x01\x00\x00\x00",  # EMF
        b"\xd7\xcd\xc6\x9a",  # placeable WMF (0x9AC6CDD7 LE)
        b"\x01\x00\x09\x00",  # standard WMF, memory
        b"\x02\x00\x09\x00",  # standard WMF, disk
    )


def main():
    parser = argparse.ArgumentParser(description="5-point losslessness audit for an extraction")
    parser.add_argument("target", help="a .pptx path or a bare stem")
    parser.add_argument("--project", default=None, help="project root containing source/ and extracted/ (default: this tool's own project)")
    args = parser.parse_args()

    work_dir = Path(args.project).resolve() if args.project else WORK_DIR
    source_dir = work_dir / "source"
    out_dir = work_dir / "extracted"
    pptx = resolve_source(args.target, source_dir)
    stem = pptx.stem
    md_path = out_dir / f"{stem}.md"
    asset_dir = out_dir / "assets" / stem
    if not md_path.is_file():
        sys.exit(f"missing output: {md_path} (run extract_pptx.py first)")

    md = md_path.read_text(encoding="utf-8")
    z = ZipFile(pptx)
    names = z.namelist()
    slides = [n for n in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)]
    notes = [n for n in names if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", n)]
    media = {n: z.read(n) for n in names if n.startswith("ppt/media/")}
    assets = {p.read_bytes() for p in asset_dir.iterdir() if p.is_file()} if asset_dir.is_dir() else set()

    failures = 0

    marks = len(re.findall(r"^<!-- slide: \d+ -->", md, re.M))
    ok1 = marks == len(slides)
    failures += not ok1
    print(f"1. slide markers: {marks} (expect {len(slides)}) {'OK' if ok1 else 'FAIL'}")

    missing = {n: b for n, b in media.items() if b not in assets}
    chrome = set()
    for rel in names:
        if re.fullmatch(r"ppt/(slideLayouts|slideMasters|notesMasters|notesSlides)/_rels/[^/]+\.xml\.rels", rel):
            chrome |= set(re.findall(r'Target="\.\./media/([^"]+)"', z.read(rel).decode()))
    unexplained = {n for n in missing if n.rsplit("/", 1)[-1] not in chrome and not is_metafile(missing[n])}
    failures += bool(unexplained)
    print(f"2. missing media blobs: {len(missing)} (chrome={sum(1 for n in missing if n.rsplit('/', 1)[-1] in chrome)}, "
          f"metafile={sum(1 for n in missing if is_metafile(missing[n]))}) | unexplained: {len(unexplained)} "
          f"{sorted(unexplained) or ''} {'OK' if not unexplained else 'FAIL'}")

    refs = re.findall(r"!\[[^\]]+\]\(([^)]+)\)", md)
    bad = [r for r in refs if not (md_path.parent / r).is_file()]
    failures += bool(bad)
    print(f"3. image refs: {len(refs)} | unresolvable: {len(bad)} {bad[:5] or ''} {'OK' if not bad else 'FAIL'}")

    stripped = re.sub(r"[*_~`]|\\", "", md)
    missing_text = []
    for xml in slides + notes:
        for m in re.findall(r"<a:t>(.*?)</a:t>", z.read(xml).decode("utf-8"), re.S):
            s = html.unescape(m).strip()
            if s and s not in stripped:
                missing_text.append((xml, s))
    failures += bool(missing_text)
    print(f"4. <a:t> strings missing from md: {len(missing_text)} {'OK' if not missing_text else 'FAIL'}")
    for xml, s in missing_text[:10]:
        print(f"   MISSING from {xml}: {s[:60]!r}")

    n_notes = len(re.findall(r"^> Unextractable data", md, re.M))
    n_meta = sum(1 for b in media.values() if is_metafile(b))
    print(f"5. visible unextractable notes: {n_notes} (metafile blobs in source: {n_meta})"
          + (" — note: metafiles present but no visible note" if n_meta and not n_notes else ""))

    print("RESULT:", "PASS" if not failures else f"FAIL ({failures} check(s))")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()