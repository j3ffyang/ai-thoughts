# Extracting PowerPoint to Markdown Without Losing a Byte

## Overview
A local, single-folder pipeline that turns PowerPoint decks into full-data, page-delimited Markdown — built on `python-pptx`, guarded by a five-point audit, and deliberately kept off CI.

## Learning Objectives
The viewer will understand:
1. Why "all data, no summary" makes the audit, not the converter, the hard part.
2. How deck contents split into content / chrome / unrenderable — and why exclusions must be visible.
3. Why deterministic output and confidential binaries keep the work local.

---

## Section 1: The Requirement

**Key Concept**: "All data, no summary" is the hard requirement that shaped everything.

**Content**:
- The easy half is the text; the hard half is everything "data" hides: tables, speaker notes, hyperlinks, embedded images, objects with no Markdown equivalent.
- The first real question is not "how do I convert?" but "how will I prove I didn't lose anything?"

**Visual Element**:
- Type: headline block with a magnifier over a document
- Subject: a slide deck with hidden items being revealed (notes, table, link, image)
- Treatment: bold headline, small icons for the hidden data types

**Text Labels**:
- Headline: "ALL DATA, NO SUMMARY"
- Subhead: "The hard part is proving nothing was lost"
- Labels: "notes", "tables", "hyperlinks", "images"

---

## Section 2: Under the Hood

**Key Concept**: A `.pptx` is a zip of XML parts, and `python-pptx` does the parsing.

**Content**:
- "A modern `.pptx` is not a binary blob; it is a zip archive of XML parts."
- `python-pptx` turns those parts into Python objects — shapes, tables, notes, pictures, hyperlinks.
- The project adds the layer above: what counts as content, the exclusion policy, a deterministic format, and the audit.

**Visual Element**:
- Type: layered diagram
- Subject: zip archive → XML parts → python-pptx objects → project layer
- Treatment: three stacked layers with an arrow upward

**Text Labels**:
- Headline: "A .PPTX IS A ZIP OF XML"
- Layer 1: "XML parts"
- Layer 2: "python-pptx"
- Layer 3: "the project's guarantees"

---

## Section 3: Three Classes of Content

**Key Concept**: Knowing what to keep, drop, and disclose is the real engineering.

**Content**:
- **Content** — text, tables, notes, content images: extracted.
- **Chrome** — layout backgrounds, logos, inherited placeholder text: excluded by design.
- **Unrenderable** — things Markdown cannot represent: skipped, not embedded, always disclosed in a visible note.

**Visual Element**:
- Type: three-column taxonomy
- Subject: content kept / chrome excluded / unrenderable disclosed
- Treatment: three equal panels, each with a representative icon

**Text Labels**:
- Headline: "THREE CLASSES"
- Col 1: "CONTENT — extracted"
- Col 2: "CHROME — excluded"
- Col 3: "UNRENDERABLE — disclosed"
- Note: "A silent exclusion is indistinguishable from data that never existed"

---

## Section 4: One Folder, One Skill

**Key Concept**: The project is a single self-contained folder; regeneration is the normal path.

**Content**:
- `source/` holds the decks and is never modified; `extracted/` holds the generated Markdown and images; `tools/` holds the scripts.
- Output is deterministic: "the same input produces byte-identical results."
- A skill, `pptx-extract`, codifies the whole procedure and travels with the folder.

**Visual Element**:
- Type: file-tree diagram
- Subject: `source/`, `extracted/`, `tools/`, skill, docs
- Treatment: monospace tree, one highlighted branch for the skill

**Text Labels**:
- Headline: "ONE FOLDER, ONE SKILL"
- Folder labels: "source/", "extracted/", "tools/"
- Skill label: "pptx-extract"
- Note: "regeneration is the normal path"

---

## Section 5: The Audit Is the Product

**Key Concept**: A five-point audit machine-proves losslessness; the first four are hard gates.

**Content**:
- "The number of slide markers in the Markdown equals the slide count in the source."
- "Every media blob in the source is explained — either extracted, identified as layout chrome, or identified as a metafile."
- "Every image reference in the Markdown resolves to a real file on disk."
- "Every text string in the slide and notes XML appears in the Markdown."
- "Every 'unextractable' note is accounted for." (the fifth is reported, not a gate)
- "No image can vanish without a named reason."

**Visual Element**:
- Type: numbered checklist / verification dashboard
- Subject: five checks with pass marks
- Treatment: checklist with 4 solid gates + 1 report badge

**Text Labels**:
- Headline: "THE AUDIT IS THE PRODUCT"
- Check 1: "slide count"
- Check 2: "media explained"
- Check 3: "links resolve"
- Check 4: "text complete"
- Check 5: "exclusions reported"
- Callout: "no image can vanish without a named reason"

---

## Section 6: Five Bugs Only Review Caught

**Key Concept**: The output looked plausible while four defects stayed latent.

**Content**:
- Image links were missing the `assets/` prefix.
- The deck header carried today's date, breaking determinism.
- The Windows-metafile signature in the audit was wrong.
- The text-completeness check is substring-based (a known limitation).
- A chart/embedded-object branch could crash on a chart-first slide.

**Visual Element**:
- Type: numbered callout cards
- Subject: five small defect cards with a magnifying glass
- Treatment: compact cards, one line each

**Text Labels**:
- Headline: "FIVE BUGS ONLY REVIEW CAUGHT"
- Labels: "1 broken links", "2 volatile date", "3 wrong signature", "4 substring check", "5 latent crash"
- Note: "Review the tool, not just its output"

---

## Section 7: Why It Stays Local

**Key Concept**: CI would force large confidential binaries into git; local is enough — with backup.

**Content**:
- "CI only sees what git sees, and the sources are roughly 80 MB of confidential binaries."
- The automation is local: a runner, a `--check` diff mode, and an optional pre-commit hook.
- "The honest cost of no remote is backup."
- "Where knowledge lives determines whether it is useful and how much it costs to maintain."

**Visual Element**:
- Type: fork / decision diagram
- Subject: GitHub Actions crossed out → local runner chosen
- Treatment: split path, cloud rejected, laptop accepted; a backup shield icon

**Text Labels**:
- Headline: "WHY IT STAYS LOCAL"
- Rejected: "GitHub Actions"
- Chosen: "local runner"
- Labels: "80 MB confidential binaries", "backup is the cost", "deterministic"

---

## Data Points (Verbatim)

### Statistics
- "13.2 MB vector diagram"
- "roughly 80 MB of confidential binaries"
- "five-point audit"

### Quotes
- "all data, no summary"
- "no image can vanish without a named reason"
- "the same input produces byte-identical results"
- "btw, i use arch"

### Key Terms
- **python-pptx**: the library that turns OOXML parts into Python objects.
- **chrome**: master and layout backgrounds, logos, inherited placeholder text — shared design, excluded.
- **unrenderable**: things Markdown cannot represent, skipped but always disclosed.

---

## Design Instructions

### Style Preferences
- None specified by the user; infer technical, honest, precise. Clean and uncluttered.

### Layout Preferences
- None specified; three combinations recommended in `analysis.md`.

### Other Requirements
- Language: English.
- Final image path follows the repo convention: `imgs/260919-<slug>.png`.
- Text must be exact and minimal — favor fewer labels over garbled text.