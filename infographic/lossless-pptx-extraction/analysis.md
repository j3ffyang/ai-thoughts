---
title: "Extracting PowerPoint to Markdown Without Losing a Byte"
topic: "technical / engineering"
data_type: "process + system-structure"
complexity: "moderate"
point_count: 7
source_language: "en"
user_language: "en"
---

## Main Topic
A local pipeline that converts PowerPoint decks into full-data, page-delimited Markdown. It is built on `python-pptx`, and its centrepiece is a five-point audit that machine-proves nothing was lost — plus the decision to keep the whole thing local instead of running it in CI.

## Learning Objectives
After viewing this infographic, the viewer should understand:
1. Why "all data, no summary" moves the hard problem from converting to *proving* — the audit, not the converter, is the product.
2. How a deck's contents split into three classes (content / chrome / unrenderable), and why every exclusion must be disclosed in a visible note.
3. The operational judgment behind the project: deterministic output, one documented exception, and why large confidential binaries keep the work local rather than in CI.

## Target Audience
- **Knowledge Level**: Intermediate — engineers and knowledge-workers who care about document pipelines and build-vs-buy calls.
- **Context**: Readers of the blog who want the engineering story behind the article.
- **Expectations**: A clear, honest visual map of the pipeline, the audit, and the key decisions.

## Content Type Analysis
- **Data Structure**: A system with a flow (source → extract → audit) plus a taxonomy (three content classes) and a decision fork (CI vs local).
- **Key Relationships**: The requirement drives the design and the acceptance test; the parse layer (python-pptx) is routine, the guarantees layer is the work.
- **Visual Opportunities**: Pipeline flow with arrows; a folder tree; a three-column taxonomy; a numbered checklist for the audit; a forked decision (CI vs local); war-story callouts for the five bugs.

## Key Data Points (Verbatim)
- "all data, no summary" (or "all data, not a summary")
- "a modern `.pptx` is not a binary blob; it is a zip archive of XML parts"
- "13.2 MB vector diagram, a Windows metafile that no Markdown viewer can render"
- "the first four are hard gates and any failure exits non-zero"
- "the fifth check is not a gate"
- "no image can vanish without a named reason"
- "Output is deterministic: the same input produces byte-identical results"
- "roughly 80 MB of confidential binaries"
- "a skill, `pptx-extract`"
- "btw, i use arch"

## Layout × Style Signals
- Content type: process + system → suggests `structural-breakdown`, `linear-progression`, `bento-grid`
- Tone: honest engineering, practical, anti-hype → suggests `technical-schematic`, `pop-laboratory`, `ui-wireframe`
- Audience: engineers → technical aesthetics, clean and precise
- Complexity: moderate (7 points) → balanced layout with clear sections

## Design Instructions (from user input)
No explicit style or aspect instructions were given; the user simply said "execute custom-infographic" against this article. Infer from content. Output must follow the repo's `imgs/<YYMMDD>-<slug>.png` convention (article prefix `260919`).

## Recommended Combinations
1. **`structural-breakdown` + `technical-schematic`** (Recommended): the project as a system — sources → extract → audit → outputs, with the folder tree — rendered as a precise blueprint.
2. **`bento-grid` + `pop-laboratory`**: overview modules for requirement, taxonomy, audit, bugs, and the local decision, in a lab-notebook grid.
3. **`linear-progression` + `ikea-manual`**: the pipeline as clean, minimal numbered steps (preflight → extract → audit → report).
4. **`bridge` + `corporate-memphis`**: problem (silent data loss) → solution (a visible, machine-checked audit), flat and clean.