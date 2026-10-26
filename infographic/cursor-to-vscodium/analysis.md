---
title: "Replace Cursor with a Minimal VSCodium AppImage"
topic: "technical/personal guide"
data_type: "comparison + setup guide + metrics"
complexity: "moderate"
point_count: 6
source_language: "en"
user_language: "en"
---

## Main Topic

A guide to replacing Cursor with a minimal, self-contained VSCodium AppImage on Arch — no forced agent, no telemetry, no account. Three Open VSX extensions (Vim, Markdown Preview Enhanced, Markdown PDF) cover three functions; Mermaid is built in and PlantUML renders locally.

## Learning Objectives

After viewing this infographic, the viewer should understand:

1. Why leave Cursor — the forced agent and the editor-as-data-path.
2. The three functions the editor must do, and which minimal tools cover each.
3. How it is installed self-contained (AppImage + checksum) and removed cleanly — VSCodium and Cursor separately.

## Target Audience

- **Knowledge Level**: Intermediate — Linux/Arch developers, privacy-minded.
- **Context**: choosing or migrating a code editor away from an AI-first product.
- **Expectations**: the tradeoffs (privacy, ergonomics, footprint) and the concrete recipe.

## Content Type Analysis

- **Data Structure**: an A/B comparison (Cursor vs VSCodium), a 3-item spec, and a setup guide with a small metrics table.
- **Key Relationships**: grievances → VSCodium behaviour → the three functions → install → footprint → rollback.
- **Visual Opportunities**: split Cursor/VSCodium columns; a "where your code goes" flow; three function chips; an extensions table; footprint bar sizes; checksum-verified install.

## Key Data Points (Verbatim)

- "No agent; you launch OpenCode yourself in the terminal"
- "**No login** to launch, edit, or install extensions"
- "`update.mode: none`; the AppImage updates only when **you** replace the file"
- "An account authentication occurs only when an extension is asking for it."
- "Even if you use your API key, your requests will still go through our backend! That's where we do our final prompt building."
- "we may use and store codebase data, prompts, editor actions, code snippets … to improve our AI features and train our models."
- "your data may be stored for investigation."
- The three functions: "a file tree with git status tags", "view/edit source with Vim keys", "render Markdown with Mermaid + PlantUML diagrams"
- Extensions: `vscodevim.vim` 1.32.4, `shd101wyy.markdown-preview-enhanced` 0.8.40, `yzane.markdown-pdf` 2.2.0
- "Open VSX" — the Eclipse Foundation's vendor-neutral registry
- Footprint: Cursor AppImage 280.6 MiB; VSCodium AppImage 184.5 MiB; VSCodium extracted 795.2 MiB; Cursor config left behind ≈ 825 MiB; VSCodium AppImage "only ~34% smaller than Cursor's"
- "self-contained and delete-and-go"
- Version `1.140.06880`

## Layout × Style Signals

- Content type: A/B comparison + guide → suggests `binary-comparison`, `comparison-matrix`, or `dense-modules`.
- Tone: technical, honest, minimal → suggests `technical-schematic`, `pop-laboratory`, `ui-wireframe`, or `corporate-memphis`.
- Audience: developers choosing an editor → clean, technical, readable.
- Complexity: moderate (comparison + spec + metrics + steps) → organized, not overloaded.

## Design Instructions (from user input)

None specified. Defaults apply: `bento-grid` + `craft-handmade` if no choice is made.

## Recommended Combinations

1. **binary-comparison + corporate-memphis** (Recommended): a clean Cursor-vs-VSCodium split — the grievance rows on the left, VSCodium's answer on the right, with the "where your code goes" net-effect strip below.
2. **dense-modules + pop-laboratory**: high-density technical reference — the three functions, the extensions table, the install command, and the footprint numbers as modules.
3. **bento-grid + technical-schematic**: modular cells (why leave, the 3 functions, the extensions, footprint, install/rollback) with a blueprint feel.
4. **iceberg + ui-wireframe**: the editor you see on the surface vs the hidden data path beneath — Cursor's backend routing made visible.
