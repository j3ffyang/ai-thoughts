Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: linear-progression
- **Style**: technical-schematic
- **Aspect Ratio**: 16:9
- **Language**: zh

## CRITICAL: Text Accuracy

The list below is the **complete and only** text that may appear in the image. Each string appears **exactly once** — no repeated labels, no echoed headings, no duplicated cells, no mirrored imagery. No word outside this block may be rendered as text. Do not render any word from the sections below this one.

- **Title**: `知乎 技能 + CLI —— 在 OpenCode 中的安装与配置`
- **Step 1 — title**: `技能是什么`
- **Step 1 — capability labels**: `search zhihu`, `search global`, `hot`, `answer`, `me ...`
- **Step 2 — title**: `安装 CLI`
- **Step 2 — labels**: `0.3.0`, `installed: true`, `compatible: true`, `无 sudo`, `PATH 不变`
- **Step 3 — title**: `无头环境下的认证`
- **Step 3 — left label**: `桌面 · Secret Service/D-Bus`
- **Step 3 — right label**: `无头 · ZHIHU_ACCESS_SECRET`
- **Step 3 — labels**: `KEYCHAIN_UNAVAILABLE`, `source: environment`
- **Step 4 — title**: `验证`
- **Step 4 — labels**: `verification: valid`, `Code 0, success`
- **Step 5 — title**: `安全说明`
- **Step 5 — labels**: `stdin`, `ZHIHU_ACCESS_SECRET`, `不落盘`, `不提交`

Each string above appears exactly once, and every card/element appears exactly once. If space is tight, prefer fewer labels over smaller or illegible text.

CJK glyph caution: this is Simplified Chinese content; render every character exactly and do not translate. Watch for rare or look-alike substitutions — 技 not 枝, 装 not 妆, 证 not 征, 验 not 检, 说 not 悦, 盘 not 磐 or 盆, 安 not 按, 境 not 镜, 环 not 还, 认 not 让, 落 not 洛, 提 not 题, 交 not 文, 头 not 买. Every string and every card appears exactly once.

## Core Principles

- Follow the layout structure precisely for information architecture
- Apply style aesthetics consistently throughout
- If content involves sensitive or copyrighted figures, create stylistically similar alternatives
- Keep information concise, highlight keywords and core concepts
- Use ample whitespace for visual clarity
- Maintain clear visual hierarchy

## Text Requirements

- All text must match the specified style treatment
- Main titles should be prominent and readable
- Key concepts should be visually emphasized
- Labels should be clear and appropriately sized
- Use the specified language for all text content
- No duplication: every string in the "CRITICAL: Text Accuracy" list appears once. If two cells seem to need the same word, rephrase one or drop it — never repeat it.

## Layout Guidelines (linear-progression)

linear-progression: sequential progression showing steps, timeline, or chronological events.

Structure:
- Linear arrangement (horizontal)
- Nodes/markers at key points (numbered step nodes 1-5)
- Connecting line or path between nodes
- Clear start and end points
- Directional flow indicators (arrows)

Process variant: action steps, numbered sequence, step numbers, action icons.

Text placement: the main title sits at the top, and each step node carries its step title, a brief description beneath it, and a clearly visible step number.

## Style Guidelines (technical-schematic)

technical-schematic: technical diagrams with engineering precision and clean geometry.

Color palette:
- Primary: Blues (#2563EB), teals, grays, white lines
- Background: Deep blue (#1E3A5F) blueprint with grid
- Accents: Amber highlights (#F59E0B), cyan callouts

Blueprint variant: white on blue, measurements, grid pattern.

Visual elements: geometric precision, grid pattern, dimension lines, technical symbols and annotations, clean vector shapes, consistent stroke weights.

Typography: technical stencil or clean sans-serif, all-caps labels, measurement annotations.

## Visual and content notes (imagery only — do NOT render any word from this section)

- Step 1: a central hub icon radiates to five surrounding capability nodes, each drawn with a small glyph — community answers, whole-web search, a trending list, a direct-answer assistant, and the signed-in user's own content.
- Step 2: numbered nodes chained left-to-right by arrows trace download, then verification (domain, file size, checksum, archive layout, self-reported version), then installation into an XDG user-data path, then a status check showing installed and compatible flags, with no elevated privileges and no change to the shell lookup path.
- Step 3: a left/right comparison — a desktop session whose OS keychain works versus a headless machine whose keychain is unavailable — with a central fallback arrow leading to a process-level environment variable injected by the host, plus a masked credential and an environment source indicator.
- Step 4: a checklist with two ticked commands, each consuming an API quota call — one verifies the signed-in identity against the user's own content, the other lists a single item and returns success with an empty list treated as passing.
- Step 5: an icon list of four prohibitions — never repeat the secret in a reply, never write it to disk, never store it in a dotenv file, never commit it — with the secret entering only via standard input or an injected environment variable.

Generate a single 16:9 infographic using exactly the strings in the CRITICAL: Text Accuracy list, each appearing once, and nothing else.
