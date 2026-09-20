#!/usr/bin/env python3
"""extract_pptx.py — PPTX -> full-data Markdown extractor.

Source of truth is the .pptx in source/ (read-only); .md + assets/ are
generated under extracted/. Re-run any time;
rollback = delete extracted/<stem>.md + extracted/assets/<stem>/ and re-run.

Usage:
    "$PY" tools/extract_pptx.py [--project DIR] <file.pptx | stem>
    (a bare stem is resolved inside <project>/source/; --project defaults to
     the folder that contains this tool's source/ and extracted/)

Output:
    <project>/extracted/<stem>.md                  all data, page-delimited (one deck per file)
    <project>/extracted/assets/<stem>/sNN-MM.ext   every picture-shape image, in slide order

Guarantees (the "all data" contract):
    - every text run in document order, with bold/italic/strike preserved
    - every table rendered as a real markdown table (no cell content lost)
    - every speaker note, verbatim
    - every picture-shape image saved + referenced
    - hyperlinks carried from the slide .rels
    - unextractable data (charts, OLE embeds, Windows vector metafiles .emf/.wmf)
      is skipped, never embedded, but ALWAYS mentioned in a visible note on the
      slide, so readers know unsupported data was there

Excluded by design (documented in AGENTS.md): slide layout/master
chrome (backgrounds, logos) and placeholder text inherited from layouts —
shared design furniture, not slide content.
"""

import argparse
import sys
from pathlib import Path

from pptx import Presentation
from pptx.oxml.ns import qn
from pptx.shapes.group import GroupShape
from pptx.shapes.picture import Picture

WORK_DIR = Path(__file__).resolve().parent.parent          # default project root
SOURCE_DIR = WORK_DIR / "source"                          # default inputs
OUT_DIR = WORK_DIR / "extracted"                          # default output dir


def resolve_source(arg, source_dir=None):
    """Resolve a pptx path: explicit path first, then <source_dir>/<arg>[.pptx]."""
    source_dir = source_dir or SOURCE_DIR
    p = Path(arg)
    if p.is_file():
        return p.resolve()
    for cand in (source_dir / arg, source_dir / f"{arg}.pptx"):
        if cand.is_file():
            return cand.resolve()
    matches = list(source_dir.glob(f"*{arg}*.pptx"))
    if len(matches) == 1:
        return matches[0].resolve()
    sys.exit(f"cannot resolve source deck: {arg!r} (looked in {source_dir})")


def is_ole(shape):
    """Embedded OLE objects (e.g. embedded Excel workbooks) carry an oleObj element."""
    return "oleObj" in shape._element.xml


def is_strike(run):
    """Strike-through is not a python-pptx Font property; read a:rPr@strike."""
    rPr = run._r.find(qn("a:rPr"))
    return rPr is not None and rPr.get("strike") == "sngStrike"


def fmt_run(run):
    """Render one run: text + emphasis markers + hyperlink."""
    text = run.text
    if not text:
        return ""
    if run.font.bold:
        text = f"**{text}**"
    if run.font.italic:
        text = f"*{text}*"
    if is_strike(run):
        text = f"~~{text}~~"
    url = run.hyperlink.address
    if url:
        text = f"[{text}]({url})"
    return text


def shape_text(shape):
    """All paragraphs of a shape's text frame, bullets nested by indent level."""
    out = []
    for p in shape.text_frame.paragraphs:
        runs = "".join(fmt_run(r) for r in p.runs)
        if not runs.strip():
            out.append("")
        else:
            out.append("  " * p.level + "- " + runs)
    return out


def shape_table(shape):
    """Real markdown table from a graphic-frame table; pipes escaped,
    multi-paragraph cells keep their line breaks via <br>."""
    tbl = shape.table
    lines = []
    rows = []
    for row in tbl.rows:
        cells = []
        for cell in row.cells:
            cell_text = "<br>".join(c for c in cell.text.strip().splitlines() if c)
            cells.append(cell_text.replace("|", "\\|"))
        rows.append(cells)
    width = max(len(r) for r in rows)
    for i, r in enumerate(rows):
        r = r + [""] * (width - len(r))
        lines.append("| " + " | ".join(r) + " |")
        if i == 0:
            lines.append("|" + "---|" * width)
    return lines


def iter_shapes(shapes):
    """Depth-first, document order; groups transparent."""
    for shape in shapes:
        if isinstance(shape, GroupShape):
            yield from iter_shapes(shape.shapes)
        else:
            yield shape


def extract_slide_md(slide, index, asset_dir, stats):
    lines = []
    n_images = 0
    n_other = 0
    for shape in iter_shapes(slide.shapes):
        if isinstance(shape, Picture):
            img = shape.image
            n_images += 1
            tag = f"s{index:02d}-{n_images:02d}"
            if img.ext.lower() in ("emf", "wmf"):
                # Windows vector metafile: unrenderable in markdown; excluded by design,
                # but always mentioned visibly so readers know data was skipped.
                lines.append(f"> Unextractable data on this slide: Windows vector metafile ({tag}, .{img.ext}, {len(img.blob) / 1048576:.1f} MB) — not embedded; original kept in source .pptx only.")
            else:
                fname = f"{tag}.{img.ext}"
                (asset_dir / fname).write_bytes(img.blob)
                lines.append(f"![{tag}](assets/{asset_dir.name}/{fname})")
            continue
        if shape.has_table:
            lines.append("")
            lines.extend(shape_table(shape))
            lines.append("")
            stats["tables"] += 1
            continue
        if shape.has_chart:
            n_other += 1
            lines.append(f"> Unextractable data on this slide: chart (s{index:02d}-x{n_other:02d}) — not embedded; original kept in source .pptx only.")
            stats["charts"] += 1
            continue
        if is_ole(shape):
            n_other += 1
            lines.append(f"> Unextractable data on this slide: embedded OLE object (s{index:02d}-x{n_other:02d}) — not embedded; original kept in source .pptx only.")
            stats["embeds"] += 1
            continue
        if shape.has_text_frame:
            paras = shape_text(shape)
            if any(x.strip() for x in paras):
                lines.append("")
                lines.extend(paras)
                lines.append("")
    # speaker notes (verbatim)
    if slide.has_notes_slide:
        ntf = slide.notes_slide.notes_text_frame
        if ntf:
            notes = [p.text for p in ntf.paragraphs if p.text.strip()]
            if notes:
                stats["notes"] += 1
                lines.append("Notes:")
                lines.extend(f"> {p}" for p in notes)
                lines.append("")
    if not any(x.strip() for x in lines):
        lines.append("(no text content)")
    return lines, n_images


def main():
    parser = argparse.ArgumentParser(description="PPTX -> full-data Markdown extractor")
    parser.add_argument("target", help="a .pptx path or a bare stem")
    parser.add_argument("--project", default=None, help="project root containing source/ and extracted/ (default: this tool's own project)")
    args = parser.parse_args()

    work_dir = Path(args.project).resolve() if args.project else WORK_DIR
    source_dir = work_dir / "source"
    out_dir = work_dir / "extracted"
    pptx_path = resolve_source(args.target, source_dir)
    stem = pptx_path.stem
    out_md = out_dir / f"{stem}.md"
    asset_dir = out_dir / "assets" / stem
    asset_dir.mkdir(parents=True, exist_ok=True)

    prs = Presentation(str(pptx_path))
    slides = list(prs.slides)
    stats = {"tables": 0, "notes": 0, "charts": 0, "embeds": 0}

    md = [
        f"<!-- deck: {pptx_path.name} | slides: {len(slides)} | tool: extract_pptx.py -->",
        "",
    ]
    for i, slide in enumerate(slides, start=1):
        md.append(f"<!-- slide: {i:02d} -->")
        md.append("")
        md.append(f"## Slide {i:02d}")
        md.append("")
        lines, n_img = extract_slide_md(slide, i, asset_dir, stats)
        md.extend(lines)
        md.append("")

    out_md.write_text("\n".join(md) + "\n", encoding="utf-8")

    n_img_total = len(list(asset_dir.iterdir()))
    print(f"source      : {pptx_path}")
    print(f"slides      : {len(slides)}")
    print(f"images      : {n_img_total} -> {asset_dir}")
    print(f"tables      : {stats['tables']}")
    print(f"notes       : {stats['notes']}")
    if stats["charts"] or stats["embeds"]:
        print(f"charts/embeds: {stats['charts']}/{stats['embeds']} (visible notes emitted)")
    print(f"markdown    : {out_md}")


if __name__ == "__main__":
    main()
