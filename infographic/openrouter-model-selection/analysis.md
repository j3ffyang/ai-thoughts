---
title: "Choosing a Model for OpenCode via OpenRouter: Privacy, Price, and Performance"
topic: "technical / decision guide"
data_type: "comparison + decision"
complexity: "moderate"
point_count: 6
source_language: "en"
user_language: "en"
---

## Main Topic
A practical guide to picking a model and serving provider when driving OpenCode through OpenRouter — separating a model's *origin* from the *jurisdiction of the service that hosts it*, tiering the privacy risk, comparing prices across six families, and giving a balanced default plus the OpenCode/OpenRouter config to enforce it.

## Learning Objectives
After viewing this infographic, the viewer should understand:
1. Why an open-weight *model* is not the same as a *service*: the data risk lives in the endpoint's jurisdiction and compulsion, not the weights.
2. How the price landscape splits: open-weight families (DeepSeek, Qwen, GLM) are far cheaper on output; Kimi and the Western frontier sit at the top.
3. How to choose — self-host/non-China ZDR for secrets, cheap open-weight for non-sensitive work, DeepSeek V4 Pro as a balanced default — and enforce it with OpenRouter's ZDR, no-training, and provider pin/exclude controls.

## Target Audience
- **Knowledge Level**: Intermediate — developers driving OpenCode/agents through OpenRouter.
- **Context**: Choosing a default model + provider with an eye on privacy and cost.
- **Expectations**: A clear map of the privacy tiers, the price leaders, and the config to lock in.

## Content Type Analysis
- **Data Structure**: A comparison matrix (families × cheapest/flagship price), a tiered risk ladder (highest → lowest exposure), and a decision table (data sensitivity → what to use).
- **Key Relationships**: Model vs serving provider; jurisdiction → compulsion risk; price floor vs quantization.
- **Visual Opportunities**: A four-tier exposure ladder; a price-leader bar/table; a decision flow (is the data sensitive? → self-host/ZDR vs cheap open-weight); the config snippet.

## Key Data Points (Verbatim)
- "A Chinese *model* is not the same as a Chinese *service*."
- "The risk lives in the **service that hosts it and the law that governs that service**."
- Privacy tiers: "Highest → China-jurisdiction API endpoint"; "Medium → Non-China aggregator routing to a China endpoint without retention or training controls"; "Lower → Non-China host … under no-retention terms"; "Lowest → Self-host (Ollama, llama.cpp, vLLM) or BYOC".
- "This is a **jurisdiction and compulsion** risk, not a claim that any vendor abuses data."
- Prices (input / output per M, 2026-09-27): DeepSeek V4 Flash \$0.047 / \$0.094; DeepSeek V4 Pro \$0.348 / \$0.696; Qwen3.8 Flash \$0.15 / \$0.47; Qwen3.8 Max Prime \$4 / \$12; GLM-5.3 Flash \$0.04 / \$0.50; GLM-5.3 \$0.24 / \$0.75; Kimi K2.5 \$0.45 / \$2.25; Kimi K3 \$3 / \$15; Gemini 2.5 Flash-Lite \$0.10 / \$0.40; Gemini 3.1 Pro Preview \$2 / \$12; gpt-5.1-codex-mini \$0.25 / \$2; GPT-5.2 \$1.75 / \$14.
- "**Price winners: DeepSeek, with Qwen and GLM close.**"
- Controls: "enforce Zero Data Retention", "opt out of training", "pin or exclude providers by jurisdiction", "prefer the `:exacto` routing variant; avoid `:floor`, which often routes to **fp4**".
- Config: `"model": "openrouter/deepseek/deepseek-v4-pro"`, `"small_model": "openrouter/deepseek/deepseek-v4-flash"`.
- "Model prices change frequently."

## Layout × Style Signals
- Content type: comparison + decision → suggests `comparison-matrix`, `binary-comparison`, `bento-grid`, `dashboard`.
- Tone: careful, technical, privacy-conscious → suggests `technical-schematic`, `corporate-memphis`, `ui-wireframe`.
- Audience: developers → clean and precise.
- Complexity: moderate (6 points) → balanced layout with clear sections.

## Design Instructions (from user input)
No explicit style/aspect given; the user just invoked the skill. Infer from content. Output follows the repo's `imgs/<YYMMDD>-<slug>.png` convention (article prefix `260927`).

## Recommended Combinations
1. **`comparison-matrix` + `technical-schematic`** (Recommended): the families (DeepSeek/Qwen/GLM/Kimi/Gemini/OpenAI) × price as a precise matrix, with the privacy tiers as a side ladder.
2. **`bento-grid` + `corporate-memphis`**: overview modules — model vs provider, the four risk tiers, the price leaders, and the config — in a clean grid.
3. **`binary-comparison` + `technical-schematic`**: open-weight vs Western frontier, and privacy vs price, as split panels.
4. **`dashboard` + `corporate-memphis`**: the price table rendered as a metrics dashboard.