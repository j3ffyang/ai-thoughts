---
name: custom-infographic
description: Generate a professional infographic from an article, document, URL, or topic, using the baoyu layout x style system (21 layouts x 21 styles). Original author 宝玉 (JimLiu); ported & customized by j3ffyang. Use when the user asks to create an infographic, 信息图, visual summary, 可视化, or a high-density information image, or wants an article turned into a visual poster.
license: MIT
compatibility: opencode
metadata:
  author: 宝玉 (JimLiu)
  upstream: https://github.com/JimLiu/baoyu-skills#baoyu-infographic
  version: 1.56.1
---

# Infographic Generator

Adapted from [baoyu-infographic](https://github.com/JimLiu/baoyu-skills) v1.56.1 (ported via Hermes Agent) for opencode, then customized by j3ffyang to comply with the opencode standard and this repo's `imgs/` convention. Image generation uses OpenRouter image models through the bundled `scripts/generate_image.py`, which requires `OPENROUTER_API_KEY` in the environment.

Two dimensions: **layout** (information structure) × **style** (visual aesthetics). Freely combine any layout with any style.

## When to Use

Trigger this skill when the user asks to create an infographic, visual summary, information graphic, or uses terms like "信息图", "可视化", or "高密度信息大图". The user provides content (text, file path, URL, or topic) and optionally specifies layout, style, aspect ratio, or language.

*Note*: Image generation needs `OPENROUTER_API_KEY` set and an image-capable model (default `google/gemini-3.1-flash-image`). If the key is missing or the call fails, still produce `analysis.md`, `structured-content.md`, and `prompts/infographic.md` for external use — see `references/workflow-example.md`.

## Options

| Option | Values |
|--------|--------|
| Layout | 21 options (see Layout Gallery), default: bento-grid |
| Style | 21 options (see Style Gallery), default: craft-handmade |
| Aspect | Named: landscape (16:9), portrait (9:16), square (1:1). Custom: any W:H ratio (e.g., 3:4, 4:3, 2.35:1) |
| Language | en, zh, ja, etc. |

## Layout Gallery

| Layout | Best For |
|--------|----------|
| `linear-progression` | Timelines, processes, tutorials |
| `binary-comparison` | A vs B, before-after, pros-cons |
| `comparison-matrix` | Multi-factor comparisons |
| `hierarchical-layers` | Pyramids, priority levels |
| `tree-branching` | Categories, taxonomies |
| `hub-spoke` | Central concept with related items |
| `structural-breakdown` | Exploded views, cross-sections |
| `bento-grid` | Multiple topics, overview (default) |
| `iceberg` | Surface vs hidden aspects |
| `bridge` | Problem-solution |
| `funnel` | Conversion, filtering |
| `isometric-map` | Spatial relationships |
| `dashboard` | Metrics, KPIs |
| `periodic-table` | Categorized collections |
| `comic-strip` | Narratives, sequences |
| `story-mountain` | Plot structure, tension arcs |
| `jigsaw` | Interconnected parts |
| `venn-diagram` | Overlapping concepts |
| `winding-roadmap` | Journey, milestones |
| `circular-flow` | Cycles, recurring processes |
| `dense-modules` | High-density modules, data-rich guides |

Full definitions: `references/layouts/<layout>.md`

## Style Gallery

| Style | Description |
|-------|-------------|
| `craft-handmade` | Hand-drawn, paper craft (default) |
| `claymation` | 3D clay figures, stop-motion |
| `kawaii` | Japanese cute, pastels |
| `storybook-watercolor` | Soft painted, whimsical |
| `chalkboard` | Chalk on black board |
| `cyberpunk-neon` | Neon glow, futuristic |
| `bold-graphic` | Comic style, halftone |
| `aged-academia` | Vintage science, sepia |
| `corporate-memphis` | Flat vector, vibrant |
| `technical-schematic` | Blueprint, engineering |
| `origami` | Folded paper, geometric |
| `pixel-art` | Retro 8-bit |
| `ui-wireframe` | Grayscale interface mockup |
| `subway-map` | Transit diagram |
| `ikea-manual` | Minimal line art |
| `knolling` | Organized flat-lay |
| `lego-brick` | Toy brick construction |
| `pop-laboratory` | Blueprint grid, coordinate markers, lab precision |
| `morandi-journal` | Hand-drawn doodle, warm Morandi tones |
| `retro-pop-grid` | 1970s retro pop art, Swiss grid, thick outlines |
| `hand-drawn-edu` | Macaron pastels, hand-drawn wobble, stick figures |

Full definitions: `references/styles/<style>.md`

## Recommended Combinations

| Content Type | Layout + Style |
|--------------|----------------|
| Timeline/History | `linear-progression` + `craft-handmade` |
| Step-by-step | `linear-progression` + `ikea-manual` |
| A vs B | `binary-comparison` + `corporate-memphis` |
| Hierarchy | `hierarchical-layers` + `craft-handmade` |
| Overlap | `venn-diagram` + `craft-handmade` |
| Conversion | `funnel` + `corporate-memphis` |
| Cycles | `circular-flow` + `craft-handmade` |
| Technical | `structural-breakdown` + `technical-schematic` |
| Metrics | `dashboard` + `corporate-memphis` |
| Educational | `bento-grid` + `chalkboard` |
| Journey | `winding-roadmap` + `storybook-watercolor` |
| Categories | `periodic-table` + `bold-graphic` |
| Product Guide | `dense-modules` + `morandi-journal` |
| Technical Guide | `dense-modules` + `pop-laboratory` |
| Trendy Guide | `dense-modules` + `retro-pop-grid` |
| Educational Diagram | `hub-spoke` + `hand-drawn-edu` |
| Process Tutorial | `linear-progression` + `hand-drawn-edu` |

Default: `bento-grid` + `craft-handmade`

## Keyword Shortcuts

When user input contains these keywords, **auto-select** the associated layout and offer associated styles as top recommendations in Step 3. Skip content-based layout inference for matched keywords.

If a shortcut has **Prompt Notes**, append them to the generated prompt (Step 5) as additional style instructions.

| User Keyword | Layout | Recommended Styles | Default Aspect | Prompt Notes |
|--------------|--------|--------------------|----------------|--------------|
| 高密度信息大图 / high-density-info | `dense-modules` | `morandi-journal`, `pop-laboratory`, `retro-pop-grid` | portrait | — |
| 信息图 / infographic | `bento-grid` | `craft-handmade` | landscape | Minimalist: clean canvas, ample whitespace, no complex background textures. Simple cartoon elements and icons only. |

## Output Structure

```
infographic/{topic-slug}/
├── source-{slug}.{ext}
├── analysis.md
├── structured-content.md
└── prompts/infographic.md

final image → imgs/<YYMMDD>-<slug>.png
```

Working files live in `infographic/{topic-slug}/`; the final image always lands in `imgs/` following this repo's `YYMMDD-slug` filename convention (see `ai-thoughts/AGENTS.md`).

- `{topic-slug}`: 2-4 words kebab-case from topic. Conflict: append `-YYYYMMDD-HHMMSS`.
- Final image name: `imgs/<YYMMDD>-<slug>.png` where `<slug>` is a 2-4 word kebab-case name and `<YYMMDD>` is the current date — or, when the source is an ai-thoughts article, the article's own `YYMMDD` prefix so the image shares it.

## Core Principles

- Preserve source data faithfully — no summarization or rephrasing (but **strip any credentials, API keys, tokens, or secrets** before including in outputs)
- Define learning objectives before structuring content
- Structure for visual communication (headlines, labels, visual elements)
- Communicate concisely with the user — provide actionable updates rather than verbose explanations unless asked for details

## Workflow

### Step 1: Setup & Analyze

**Load references**: Read `references/analysis-framework.md` from this skill.

1. Save source content (file path or paste → `source.md` using `write`)
   - **Backup rule**: If `source.md` exists, rename to `source-backup-YYYYMMDD-HHMMSS.md`
2. Analyze: topic, data type, complexity, tone, audience
3. Detect source language and user language
4. Extract design instructions from user input
5. Save analysis to `analysis.md`
   - **Backup rule**: If `analysis.md` exists, rename to `analysis-backup-YYYYMMDD-HHMMSS.md`

See `references/analysis-framework.md` for detailed format.

### Step 2: Generate Structured Content → `structured-content.md`

Transform content into infographic structure:
1. Title and learning objectives
2. Sections with: key concept, content (verbatim), visual element, text labels
3. Data points (all statistics/quotes copied exactly)
4. Design instructions from user

**Rules**: Markdown only. No new information. Preserve data faithfully. Strip any credentials or secrets from output.

See `references/structured-content-template.md` for detailed format.

### Step 3: Recommend Combinations

**3.1 Check Keyword Shortcuts first**: If user input matches a keyword from the **Keyword Shortcuts** table, auto-select the associated layout and prioritize associated styles as top recommendations. Skip content-based layout inference.

**3.2 Otherwise**, recommend 3-5 layout×style combinations based on:
- Data structure → matching layout
- Content tone → matching style
- Audience expectations
- User design instructions

### Step 4: Confirm Options

Use the `question` tool to confirm options with the user. Ask all three questions in one call:

**Q1 — Combination**: Present 3+ layout×style combos with rationale. Ask user to pick one.

**Q2 — Aspect**: Ask for aspect ratio preference (landscape/portrait/square or custom W:H).

**Q3 — Language** (only if source ≠ user language): Ask which language the text content should use.

If the user already specified all options, skip Step 4.

### Step 5: Generate Prompt → `prompts/infographic.md`

**Backup rule**: If `prompts/infographic.md` exists, rename to `prompts/infographic-backup-YYYYMMDD-HHMMSS.md`

**Load references**: Read the selected layout from `references/layouts/<layout>.md` and style from `references/styles/<style>.md`.

Combine:
1. Layout definition from `references/layouts/<layout>.md`
2. Style definition from `references/styles/<style>.md`
3. Base template from `references/base-prompt.md`
4. Structured content from Step 2
5. All text in confirmed language
6. **Text accuracy block**: After assembling all content, add a "CRITICAL: Text Accuracy" section at the top of the prompt. List every exact text string that must appear in the image, spell out known pitfalls, and instruct the model to favor fewer labels over garbled text. This block is mandatory — skip it and the image will garble text.

**Aspect ratio resolution** for `{{ASPECT_RATIO}}`:
- Named presets → ratio string: landscape→`16:9`, portrait→`9:16`, square→`1:1`
- Custom W:H ratios → use as-is (e.g., `3:4`, `4:3`, `2.35:1`)

Save the assembled prompt to `prompts/infographic.md` using `write`.

### Step 6: Generate Image

Run the bundled generator with the prompt from Step 5, writing the final image directly to `imgs/` with the repo-convention filename:

```bash
python .opencode/skills/custom-infographic/scripts/generate_image.py \
  --prompt infographic/{topic-slug}/prompts/infographic.md \
  --output imgs/{YYMMDD}-{slug}.png \
  --aspect 16:9
```

- The final image goes to `imgs/<YYMMDD>-<slug>.png` (repo convention, see Output Structure) — never to `infographic/{topic-slug}/`.
- Map aspect ratio to the `--aspect` value: landscape→`16:9`, portrait→`9:16`, square→`1:1`, custom ratios passed as-is (Gemini supports `3:4`, `4:3`, `21:9`, `1:4`, `4:1`, `1:8`, `8:1`; map anything else to the nearest named preset)
- Requires `OPENROUTER_API_KEY` to be set; the default model is `google/gemini-3.1-flash-image`, override with `--model`
- On failure, auto-retry once, then report the error to the user
- **Backup rule**: If the target `imgs/<YYMMDD>-<slug>.png` already exists, rename it to `imgs/<YYMMDD>-<slug>-backup-YYYYMMDD-HHMMSS.png` before writing. Never overwrite silently.

### Step 7: Output Summary

Report: topic, layout, style, aspect, language, output path (`imgs/<YYMMDD>-<slug>.png`), files created.

## References

- `references/analysis-framework.md` — Analysis methodology
- `references/structured-content-template.md` — Content format
- `references/base-prompt.md` — Prompt template
- `references/layouts/<layout>.md` — 21 layout definitions
- `references/styles/<style>.md` — 21 style definitions
- `references/workflow-example.md` — Example workflow when image generation is unavailable

## Pitfalls

1. **Data integrity is paramount** — never summarize, paraphrase, or alter source statistics. "73% increase" must stay "73% increase", not "significant increase".
2. **Strip secrets** — always scan source content for API keys, tokens, or credentials before including in any output file.
3. **One message per section** — each infographic section should convey one clear concept. Overloading sections reduces readability.
4. **Style consistency** — the style definition from the references file must be applied consistently across the entire infographic. Don't mix styles.
5. **Aspect ratio support** — `image_config` aspect ratios are limited to what the selected model supports (Gemini: `16:9`, `9:16`, `1:1`, `3:4`, `4:3`, `21:9`, plus extended `1:4`, `4:1`, `1:8`, `8:1`); map custom ratios outside that set to the nearest named preset.
6. **API availability** — generation fails without `OPENROUTER_API_KEY` or when the model cannot output images. Verify the key is set before starting; if generation is impossible, deliver the prompt-only outputs (`analysis.md`, `structured-content.md`, `prompts/infographic.md`) and tell the user.
7. **Text accuracy in image generation** — AI image models frequently garble, misspell, or double text. Every prompt MUST include an explicit "CRITICAL: Text Accuracy" block that (a) lists every exact text string the image must render, (b) spells out common pitfalls to avoid (doubled words, garbled section titles, similar-looking words), and (c) instructs the model to prioritize text accuracy over visual density — shrink the number of labels rather than shrinking font size or misspelling words. After generation, verify all text with a vision model (e.g. `opencode run` with `--model openrouter/z-ai/glm-4.6v --file`) against the expected text list before delivering to the user.

## Credits

- **Original author**: 宝玉 (JimLiu) — the baoyu layout × style system, [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) v1.56.1.
- **Ported & customized by**: j3ffyang — OpenCode adaptation and this repo's `imgs/` output convention.
