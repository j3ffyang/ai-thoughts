# Choosing a Model for OpenCode via OpenRouter: Privacy, Price, and Performance

## Overview
A decision guide for picking a model and serving provider on OpenRouter: separate the model's origin from the host's jurisdiction, tier the privacy risk, compare prices, then lock in a default with OpenRouter's ZDR, no-training, and provider controls.

## Learning Objectives
The viewer will understand:
1. The model vs service distinction, and that the data risk is jurisdictional.
2. The four privacy tiers and the price leaders across six families.
3. The balanced default and the config to enforce data controls.

---

## Section 1: Model ≠ Service

**Key Concept**: An open-weight model carries no inherent data risk; the risk lives in the serving provider's jurisdiction.

**Content**:
- "The distinction that matters throughout this note is between the **model** and the **serving provider**."
- An open-weight model (DeepSeek, Qwen, Kimi, GLM) is a set of downloadable files; it carries no inherent data risk.
- "The risk lives in the **service that hosts it and the law that governs that service**."
- "A Chinese *model* is not the same as a Chinese *service*. The open weights can run anywhere."

**Visual Element**:
- Type: two-panel conceptual diagram
- Subject: left = "model" (a file/box, neutral); right = "service/endpoint" (a server with a flag/jurisdiction)
- Treatment: split panel, arrow showing weights can run anywhere

**Text Labels**:
- Headline: "MODEL ≠ SERVICE"
- Left: "open weights — no inherent risk"
- Right: "the endpoint — jurisdiction is the risk"

---

## Section 2: The Privacy Ladder

**Key Concept**: Data exposure falls from China-jurisdiction endpoints down to self-hosting.

**Content**:
- Highest: China-jurisdiction API endpoint (DeepSeek direct, Alibaba, Moonshot, `.cn`) receiving your code or secrets — compulsory-disclosure law.
- Medium: non-China aggregator routing to a China endpoint without retention/training controls.
- Lower: non-China host (Together, Fireworks, DeepInfra, Baseten, GMI) running the same open weights under no-retention terms — contractual, not state compulsion.
- Lowest: self-host (Ollama, llama.cpp, vLLM) or BYOC — no third-party exposure.
- "This is a **jurisdiction and compulsion** risk, not a claim that any vendor abuses data."

**Visual Element**:
- Type: four-step ladder / stacked tiers, descending
- Subject: exposure decreasing from top to bottom
- Treatment: color-graded stacked bars; top red-ish, bottom green-ish

**Text Labels**:
- Headline: "THE PRIVACY LADDER"
- T1: "HIGHEST — China-jurisdiction endpoint"
- T2: "MEDIUM — aggregator → China endpoint"
- T3: "LOWER — non-China host, no-retention"
- T4: "LOWEST — self-host / BYOC"

---

## Section 3: The Price Landscape

**Key Concept**: Open-weight families are far cheaper on output; Kimi and the Western frontier sit at the top.

**Content**:
- Cheapest capable → frontier flagship, input/output per M (2026-09-27): DeepSeek V4 Flash \$0.047/\$0.094 → V4 Pro \$0.348/\$0.696; Qwen3.8 Flash \$0.15/\$0.47 → Qwen3.8 Max Prime \$4/\$12; GLM-5.3 Flash \$0.04/\$0.50 → GLM-5.3 \$0.24/\$0.75; Kimi K2.5 \$0.45/\$2.25 → K3 \$3/\$15; Gemini 2.5 Flash-Lite \$0.10/\$0.40 → 3.1 Pro Preview \$2/\$12; gpt-5.1-codex-mini \$0.25/\$2 → GPT-5.2 \$1.75/\$14.
- "**Price winners: DeepSeek, with Qwen and GLM close.** … **Kimi is not a price leader.**"
- "Model prices change frequently."

**Visual Element**:
- Type: comparison matrix / table with a bar accent
- Subject: six families × cheapest vs flagship
- Treatment: rows per family, numbers in monospace, cheap rows highlighted

**Text Labels**:
- Headline: "THE PRICE LANDSCAPE"
- Note: "input / output per million tokens — 2026-09-27"
- Callout: "open-weight families win on output; frontier costs ~20× more"

---

## Section 4: The Decision

**Key Concept**: Match the model+routing to the data's sensitivity.

**Content**:
- Proprietary or contains secrets → self-host open weights, or a non-China host with Zero Data Retention via OpenRouter, or a Western frontier model. Avoid China-jurisdiction endpoints.
- Open-source / non-sensitive → DeepSeek V4 Flash or Qwen3.8 Flash via OpenRouter — best price/performance for coding.
- Balanced default → DeepSeek V4 Pro on a non-China host, with a cheap small model for routine steps.

**Visual Element**:
- Type: decision flow / three-branch fork
- Subject: "is the data sensitive?" → three routes
- Treatment: left-to-right flow with three outcome cards

**Text Labels**:
- Headline: "WHAT SHOULD YOU USE?"
- A: "SECRETS → self-host / ZDR / Western frontier"
- B: "OPEN-SOURCE → V4 Flash or Qwen3.8 Flash"
- C: "BALANCED → V4 Pro on a non-China host"

---

## Section 5: Lock It In (config)

**Key Concept**: Enforce the choice in OpenCode + OpenRouter.

**Content**:
- OpenCode config: `"model": "openrouter/deepseek/deepseek-v4-pro"`, `"small_model": "openrouter/deepseek/deepseek-v4-flash"`.
- OpenRouter controls: **enforce Zero Data Retention**, **opt out of training**, and pin or exclude providers by jurisdiction.
- For agentic tool-calling reliability, prefer the `:exacto` routing variant; avoid `:floor` (often routes to fp4 and can degrade tool calls).

**Visual Element**:
- Type: config card + toggle/control icons
- Subject: a JSON snippet beside three control toggles
- Treatment: monospace code block, minimal chrome

**Text Labels**:
- Headline: "LOCK IT IN"
- Labels: "model: deepseek-v4-pro", "small_model: deepseek-v4-flash"
- Controls: "enforce ZDR", "no training", "pin / exclude by jurisdiction"
- Warning: "avoid :floor (fp4)"

---

## Data Points (Verbatim)

### Statistics
- "DeepSeek V4 Flash \$0.047 / \$0.094"
- "DeepSeek V4 Pro \$0.348 / \$0.696"
- "GLM-5.3 Flash \$0.04 / \$0.50"
- "Kimi K3 \$3 / \$15"
- "GPT-5.2 \$1.75 / \$14"

### Quotes
- "A Chinese *model* is not the same as a Chinese *service*."
- "The risk lives in the **service that hosts it and the law that governs that service**."
- "Price winners: DeepSeek, with Qwen and GLM close."

### Key Terms
- **model vs serving provider**: the weights vs the endpoint that runs them.
- **ZDR**: Zero Data Retention — no storing of prompts/outputs.
- **`:floor` / `:exacto`**: OpenRouter routing variants (cheapest-quant vs exact-provider).

---

## Design Instructions

### Style Preferences
- None specified; infer technical, careful, privacy-conscious.

### Layout Preferences
- None specified; four combinations recommended in `analysis.md`.

### Other Requirements
- Language: English.
- Final image path: `imgs/260927-<slug>.png` (article prefix `260927`).
- Text must be exact and minimal — favor fewer labels over garbled text.