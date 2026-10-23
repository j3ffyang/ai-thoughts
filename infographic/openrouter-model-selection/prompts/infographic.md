Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: comparison-matrix (multi-factor grid)
- **Style**: technical-schematic (engineering blueprint)
- **Aspect Ratio**: 16:9
- **Language**: English

## CRITICAL: Text Accuracy

The list below is the complete and only text that may appear in the image, organized by region. Each string appears exactly once — no repeated labels, no echoed headings, no duplicated cells, no mirrored imagery. No word outside this list may be rendered as text. Spell the model-id strings and the floor-variant routing token exactly as written, and keep the not-equal sign and the arrows exact. Prefer fewer labels over shrinking text into illegibility: if space runs short, drop a non-essential label rather than misspelling any number.

- Title band: title `CHOOSING A MODEL FOR OPENCODE VIA OPENROUTER`; subtitle `Privacy · price · performance · 2026-09-27`
- Model-vs-service panel: headline `MODEL ≠ SERVICE`; left note `open weights — no inherent risk`; right note `the endpoint — jurisdiction is the risk`
- Privacy ladder: headline `THE PRIVACY LADDER`; tiers `HIGHEST — China-jurisdiction endpoint`, `MEDIUM — aggregator → China endpoint`, `LOWER — non-China host, no-retention`, `LOWEST — self-host / BYOC`
- Price matrix: headline `THE PRICE LANDSCAPE`; note `input / output per million tokens — 2026-09-27`; callout `open-weight families win on output; frontier costs ~20× more`; column headers `FAMILY`, `CHEAPEST (in/out per M)`, `FLAGSHIP (in/out per M)`
- Matrix rows (name, cheapest, flagship):
  - `DeepSeek` and `$0.047 / $0.094` and `$0.348 / $0.696`
  - `Qwen` and `$0.15 / $0.47` and `$4 / $12`
  - `GLM` and `$0.04 / $0.50` and `$0.24 / $0.75`
  - `Kimi` and `$0.45 / $2.25` and `$3 / $15`
  - `Gemini` and `$0.10 / $0.40` and `$2 / $12`
  - `OpenAI` and `$0.25 / $2` and `$1.75 / $14`
- Decision fork: headline `WHAT SHOULD YOU USE?`; branches `SECRETS → self-host / ZDR / Western frontier`, `OPEN-SOURCE → V4 Flash or Qwen3.8 Flash`, `BALANCED → V4 Pro on a non-China host`
- Config card: headline `LOCK IT IN`; fields `model: deepseek-v4-pro`, `small_model: deepseek-v4-flash`; controls `enforce ZDR`, `no training`, `pin / exclude by jurisdiction`; warning `avoid :floor (fp4)`
- Footer: `Prices change frequently`

## Core Principles

- Follow the layout structure precisely; apply the blueprint style consistently.
- Keep information concise; highlight keywords; ample whitespace; clear hierarchy.

## Layout Guidelines (comparison-matrix)

- A clear grid: first column = item names, header row = criteria.
- Cells hold short values (prices), with color coding; highlight the recommended row (the cheapest open-weight family).
- Leave a header band for the title/subtitle, and a side band for the privacy ladder.
- A legend/footer for the note.

## Style Guidelines (technical-schematic — blueprint)

- Deep blue background (#1E3A5F) with white/light-gray linework and grid; primary blue (#2563EB); amber (#F59E0B) accents; cyan callouts.
- Clean geometry, consistent stroke weights, technical annotations.
- All-caps sans-serif labels.
- Regions:
  - Top: a wide banner for the headline and subtitle.
  - Upper-left: a two-panel conceptual note.
  - Left column: a four-tier descending ladder, color-graded.
  - Center/right: the six-row comparison matrix, with the recommended row highlighted.
  - Bottom-left: three outcome cards.
  - Bottom-right: a config card with controls and a caution marker.
  - Bottom: a thin footer rule.

## Visual and content notes (imagery only — do NOT render any word from this section)

- Core distinction: a split two-panel diagram. The left panel shows an abstract stack of downloadable file blocks, drawn inert and neutral; the right panel shows a server rack with a jurisdiction flag and a warning glow. A long arrow crosses the panels to show the files can be moved anywhere. Convey that the files themselves carry no exposure and that the risk comes from where they are hosted and which law governs the host.
- Privacy ladder: a four-tier staircase descending, exposure decreasing from top to bottom. Color-grade the top tier red and the bottom tier green; each tier is a stacked bar with a small chip for its label.
- Price landscape: a six-row comparison grid. The first column holds family names, the next two columns hold the cheapest-tier and flagship-tier input/output figures, set in monospace. Highlight the row whose output price is lowest, and add a bar accent showing the flagship end sitting far above the cheap end.
- Decision: a single question node on the left forks into three routes, each ending in an outcome card on the right.
- Lock it in: a config card with a monospace code block beside three control toggles, with a small caution marker on the routing token.
- Footer: a thin rule carrying the note.

---

Generate a single 16:9 infographic using exactly the strings in the CRITICAL: Text Accuracy list, each appearing once, and nothing else.
