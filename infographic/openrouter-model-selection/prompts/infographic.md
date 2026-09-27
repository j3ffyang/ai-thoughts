Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: comparison-matrix (multi-factor grid)
- **Style**: technical-schematic (engineering blueprint)
- **Aspect Ratio**: 16:9
- **Language**: English

## CRITICAL: Text Accuracy

Render EXACTLY these strings, spelled correctly, no duplicates, no extra words:

- Title: `CHOOSING A MODEL FOR OPENCODE VIA OPENROUTER`
- Subtitle: `Privacy · price · performance · 2026-09-27`
- `MODEL ≠ SERVICE`
- `open weights — no inherent risk` / `the endpoint — jurisdiction is the risk`
- Privacy ladder: `HIGHEST — China-jurisdiction endpoint` / `MEDIUM — aggregator → China endpoint` / `LOWER — non-China host, no-retention` / `LOWEST — self-host / BYOC`
- Matrix header: `FAMILY` / `CHEAPEST (in/out per M)` / `FLAGSHIP (in/out per M)`
- Rows:
  - `DeepSeek` `$0.047 / $0.094` `$0.348 / $0.696`
  - `Qwen` `$0.15 / $0.47` `$4 / $12`
  - `GLM` `$0.04 / $0.50` `$0.24 / $0.75`
  - `Kimi` `$0.45 / $2.25` `$3 / $15`
  - `Gemini` `$0.10 / $0.40` `$2 / $12`
  - `OpenAI` `$0.25 / $2` `$1.75 / $14`
- Decision: `SECRETS → self-host / ZDR` / `OPEN-SOURCE → V4 Flash or Qwen3.8 Flash` / `BALANCED → V4 Pro on a non-China host`
- Config: `model: deepseek-v4-pro` / `small_model: deepseek-v4-flash`
- Controls: `enforce ZDR` / `no training` / `pin / exclude by jurisdiction`
- Warning: `avoid :floor (fp4)`
- Footer note: `Prices change frequently`

Pitfalls to avoid:
- Do NOT double words or repeat a label.
- Decimal prices must be exact: `$0.047`, `$0.094`, `$0.348`, `$0.696`, `$0.04`, `$3`, `$15`, `$1.75`, `$14`.
- `≠` must be the not-equal sign; `→` the arrow.
- Prefer FEWER labels over shrinking text into illegibility. If space runs short, drop the least important label rather than misspelling any number.

## Core Principles

- Follow the layout structure precisely; apply the blueprint style consistently.
- Keep information concise; highlight keywords; ample whitespace; clear hierarchy.

## Layout Guidelines (comparison-matrix)

- A clear grid: first column = item names, header row = criteria.
- Cells hold short values (prices), with color coding; highlight the recommended row (DeepSeek).
- Leave a header band for the title/subtitle, and a side band for the privacy ladder.
- A legend/footer for the note.

## Style Guidelines (technical-schematic — blueprint)

- Deep blue background (#1E3A5F) with white/light-gray linework and grid; primary blue (#2563EB); amber (#F59E0B) accents; cyan callouts.
- Clean geometry, consistent stroke weights, technical annotations.
- All-caps sans-serif labels.
- Regions:
  - Top: title band (`CHOOSING A MODEL FOR OPENCODE VIA OPENROUTER`) + subtitle.
  - Upper-left: `MODEL ≠ SERVICE` with the two-panel note.
  - Left column: `THE PRIVACY LADDER` — four stacked tiers (HIGHEST → LOWEST), color-graded.
  - Center/right: the `THE PRICE LANDSCAPE` matrix (6 families × cheapest/flagship), DeepSeek row highlighted.
  - Bottom-left: `WHAT SHOULD YOU USE?` — three outcome cards.
  - Bottom-right: `LOCK IT IN` config card + controls, with `avoid :floor (fp4)`.
  - Footer: `Prices change frequently`.

---

Generate the infographic based on the content below:

## The core distinction
An open-weight model is just files — no inherent data risk. The risk is the serving endpoint's jurisdiction. `MODEL ≠ SERVICE`.

## Privacy ladder (highest exposure → lowest)
HIGHEST — China-jurisdiction endpoint (receiving your code/secrets). MEDIUM — non-China aggregator routing to a China endpoint. LOWER — non-China host under no-retention terms. LOWEST — self-host (Ollama, llama.cpp, vLLM) or BYOC.

## Price landscape (input/output per million tokens, 2026-09-27)
DeepSeek (cheapest $0.047/$0.094 → flagship V4 Pro $0.348/$0.696); Qwen ($0.15/$0.47 → $4/$12); GLM ($0.04/$0.50 → $0.24/$0.75); Kimi ($0.45/$2.25 → $3/$15); Gemini ($0.10/$0.40 → $2/$12); OpenAI ($0.25/$2 → $1.75/$14). Price winners: DeepSeek, with Qwen and GLM close; Kimi is not a price leader.

## Decision
Secrets → self-host / ZDR / Western frontier. Open-source → DeepSeek V4 Flash or Qwen3.8 Flash. Balanced default → DeepSeek V4 Pro on a non-China host.

## Lock it in
OpenCode config: model `deepseek-v4-pro`, small_model `deepseek-v4-flash`. OpenRouter controls: enforce Zero Data Retention, opt out of training, pin/exclude providers by jurisdiction. For tool-calling, prefer `:exacto`; avoid `:floor` (fp4).

Text labels (in English):
CHOOSING A MODEL FOR OPENCODE VIA OPENROUTER · Privacy · price · performance · 2026-09-27 · MODEL ≠ SERVICE · open weights — no inherent risk · the endpoint — jurisdiction is the risk · THE PRIVACY LADDER · HIGHEST — China-jurisdiction endpoint · MEDIUM — aggregator → China endpoint · LOWER — non-China host, no-retention · LOWEST — self-host / BYOC · THE PRICE LANDSCAPE · FAMILY · CHEAPEST (in/out per M) · FLAGSHIP (in/out per M) · DeepSeek · $0.047 / $0.094 · $0.348 / $0.696 · Qwen · $0.15 / $0.47 · $4 / $12 · GLM · $0.04 / $0.50 · $0.24 / $0.75 · Kimi · $0.45 / $2.25 · $3 / $15 · Gemini · $0.10 / $0.40 · $2 / $12 · OpenAI · $0.25 / $2 · $1.75 / $14 · WHAT SHOULD YOU USE? · SECRETS → self-host / ZDR · OPEN-SOURCE → V4 Flash or Qwen3.8 Flash · BALANCED → V4 Pro on a non-China host · LOCK IT IN · model: deepseek-v4-pro · small_model: deepseek-v4-flash · enforce ZDR · no training · pin / exclude by jurisdiction · avoid :floor (fp4) · Prices change frequently