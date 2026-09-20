---
name: pptx-extract
description: >
  Extract a PowerPoint deck into full-data, page-delimited Markdown — every
  text run, table, speaker note, and image — with unextractable data (vector
  metafiles, charts, OLE embeds) skipped but visibly noted on its slide, then
  prove losslessness with a 5-point machine audit. Use when the user asks to
  extract/convert a PPTX to Markdown, add a new deck to an extraction project,
  or regenerate a stale extraction. Related terms: PPT, PowerPoint, PPTX,
  slide extraction, 提取.
---

# PPTX → Markdown extraction

Turn a PowerPoint deck into one full-data Markdown file, and prove that nothing was lost. This skill is **self-contained**: it bundles the two tools it needs under `scripts/`, so it runs from anywhere and requires only a target project with a `source/` folder.

## What it needs

- A **target project** with a `source/` folder holding the `.pptx` decks (read-only); outputs land in `<project>/extracted/`.
- A **Python 3 with `python-pptx`** (the system `python3` may not have it).
- This skill's **bundled scripts**: `scripts/extract_pptx.py` and `scripts/audit_pptx.py`.

Set three variables and use them in every command below:

```bash
SKILL_DIR=.opencode/skills/pptx-extract   # this skill's folder (its base directory)
PROJECT=/path/to/extraction-project       # folder holding source/ and receiving extracted/
PY=/path/to/venv/bin/python               # any Python 3 with python-pptx
```

The tools take `--project` and anchor to it, so they run from **any** working directory. A bare deck stem is resolved inside `$PROJECT/source/`, and output always lands in `$PROJECT/extracted/`.

## Format contract

- One Markdown file per deck: `<project>/extracted/<stem>.md`; images at `<project>/extracted/assets/<stem>/sNN-MM.<ext>` (`NN` = slide number, `MM` = picture index within the slide, document order).
- **Page delimiter:** `<!-- slide: NN -->` (zero-padded, deck order); each slide is headed `## Slide NN`.
- Deck header on line 1: `<!-- deck: <file> | slides: N | tool: extract_pptx.py -->`.
- Text: every run in document order, never summarized. Bullets nest by the paragraph indent level; emphasis is preserved; hyperlinks are carried from the slide relationships.
- Tables: real Markdown tables, multi-paragraph cells keep their line breaks via `<br>`.
- Speaker notes: verbatim under `Notes:` after the slide content.
- **Exclusions, never silent:** layout/master chrome (backgrounds, logos, inherited placeholder text) is excluded by design; vector metafiles (`.emf`/`.wmf`) and charts/OLE embeds are skipped rather than embedded, but each is disclosed in a visible note on that slide (`> Unextractable data on this slide: ...`).

## Inputs

- `target` — a deck stem or a `.pptx` path. A bare stem is resolved inside `$PROJECT/source/`; if ambiguous, list `$PROJECT/source/*.pptx` and ask.

## Outputs

- `$PROJECT/extracted/<stem>.md` — one file per deck, split at `<!-- slide: NN -->` markers
- `$PROJECT/extracted/assets/<stem>/sNN-MM.<ext>` — every extractable image, in slide order

## Procedure

1. **Preflight** — report what the deck contains before touching it:

   ```bash
   unzip -l "$PROJECT/source/<stem>.pptx" | grep -c -E 'ppt/slides/slide[0-9]+\.xml$'
   unzip -l "$PROJECT/source/<stem>.pptx" | grep -c 'ppt/media/'
   unzip -l "$PROJECT/source/<stem>.pptx" | grep -c -E 'ppt/(charts/chart[0-9]+|diagrams/data[0-9]+|embeddings/)'
   unzip -l "$PROJECT/source/<stem>.pptx" | grep -c -E 'ppt/notesSlides/notesSlide[0-9]+\.xml$'
   ```

   Slides / media / charts+smartart+embeds / notes. Any non-zero charts+embeds → tell the user up front: those become visible "unextractable" notes, not data.

2. **Extract** — run this skill's bundled extractor:

   ```bash
   "$PY" "$SKILL_DIR/scripts/extract_pptx.py" --project "$PROJECT" "<stem>"
   ```

   Output always lands in `$PROJECT/extracted/`, regardless of the current directory.

3. **Audit** — run this skill's bundled 5-point losslessness proof (exit 1 on any hard failure):

   ```bash
   "$PY" "$SKILL_DIR/scripts/audit_pptx.py" --project "$PROJECT" "<stem>"
   ```

   The first four checks are hard gates: slide markers == slide count, unexplained media blobs == 0, unresolvable image references == 0, missing `<a:t>` strings == 0. The fifth is reported for review (the count of visible "unextractable" notes). On `FAIL`, investigate before declaring success — never report a partial extraction as done.

4. **Spot-check** — read the 2–3 densest slides in the `.md` (bullets nested, tables real, `Notes:` verbatim) and confirm the first line is the deck header.

5. **Report** — slide count, images, tables, notes, and every exclusion with its reason (chrome / metafile / OLE / chart). If any exclusion is unexpected for this deck, surface it to the user.

## Verification

- `audit_pptx.py` exits 0 (all checks OK).
- The "unexplained: 0" check is the strongest guarantee: no media file can vanish without a named reason.
- The `.md` opens cleanly in a Markdown viewer with no broken images or garbled content.

## Error handling

- **Legacy binary `.ppt`** (pre-2007): `python-pptx` cannot read it. Convert first with `soffice --headless --convert-to pptx` into a temp directory, then extract the converted file; the `.md`/`assets/` still land in `$PROJECT/extracted/` under the original stem.
- **`notes: 0` but notesSlides exist in the zip:** legitimate — check the notes XML; a slide-number placeholder is not real content. Only flag it if the notes carry actual text.
- **All-image slide (architecture screenshot):** legitimate — the data lives in the pixels, not the XML. Note it in the report; do not try to "fix" it (OCR is out of scope unless the user asks).
- **Missing blob that is a master/layout background:** expected and unremarkable — chrome is excluded by design, the audit explains it.
- **A blob the audit cannot explain:** stop. Unzip it, identify what references it, and report to the user before re-running.
- **Never write into `$PROJECT/source/`.** If a source must be converted or altered, work on a copy in a temp directory and leave the original untouched.