# Replace Cursor with VSCodium

## Overview

A visual summary of replacing Cursor with a minimal, self-contained VSCodium AppImage on Arch: why to leave Cursor, the three functions the editor must do, the three Open VSX extensions that cover them, where your code goes, the footprint, and the checksum-verified install.

## Learning Objectives

The viewer will understand:

1. Why leave Cursor — a forced agent and an editor that is a data path by design.
2. The three functions and the minimal tools that cover them.
3. How it is installed and removed cleanly.

---

## Section 1: Why leave Cursor

**Key Concept**: Cursor vs VSCodium, point by point.

**Content**:
- Forced agent on launch: chat/agent pane opens itself → no agent; you launch OpenCode yourself.
- Account / sign-in gate: account wall → no login to launch, edit, or install extensions.
- Update nagging: frequent, forced upgrade prompts → `update.mode: none`.
- Feature bloat: accounts, AI, telemetry, tip popups → strip to editor + tree + preview.

**Visual Element**: split two-column comparison, Cursor left, VSCodium right, four rows.

**Text Labels**:
- Headline: "Why leave Cursor"
- Columns: "Cursor", "VSCodium"
- Rows: "Agent boots itself", "Account wall", "Forced updates", "AI + telemetry"
- Rows: "No agent", "No login", "update.mode: none", "Editor only"

---

## Section 2: The 3 functions

**Key Concept**: Everything else is deliberately out of scope.

**Content**:
- a file tree with git status tags
- view/edit source with Vim keys
- render Markdown with Mermaid + PlantUML diagrams

**Visual Element**: three function chips with small icons (file tree, keyboard, diagram).

**Text Labels**:
- Headline: "Exactly 3 functions"
- "git status tags", "Vim keys", "Mermaid + PlantUML"

---

## Section 3: Three Open VSX extensions

**Key Concept**: Nothing the built-in core already does is re-added.

**Content**:
- `vscodevim.vim` 1.32.4 — Vim keys
- `shd101wyy.markdown-preview-enhanced` 0.8.40 — Markdown preview + local PlantUML
- `yzane.markdown-pdf` 2.2.0 — Markdown → PDF (optional add-on)

**Visual Element**: three small extension cards, Open VSX registry ("no Microsoft account").

**Text Labels**:
- Headline: "Three extensions"
- "Vim", "Markdown Preview Enhanced", "Markdown PDF"
- "Open VSX"

---

## Section 4: Where your code goes

**Key Concept**: The structural difference — Cursor's editor *is* a data path; VSCodium's is not.

**Content**:
- Cursor: all traffic routes through its backend by design.
- "Even if you use your API key, your requests will still go through our backend!"
- VSCodium: the editor is inert; the only egress is OpenCode, which you invoke deliberately.

**Visual Element**: two flows — a code icon routed to a server (Cursor), a code icon held on-machine (VSCodium).

**Text Labels**:
- Headline: "Where your code goes"
- "Routes through its backend", "Stays on the machine"

---

## Section 5: Footprint

**Key Concept**: Still Electron — the win is behaviour, not size.

**Content**:
- Cursor AppImage: 280.6 MiB
- VSCodium AppImage: 184.5 MiB (~34% smaller)
- VSCodium extracted on disk: 795.2 MiB
- Cursor config left behind ≈ 825 MiB

**Visual Element**: four size bars, VSCodium vs Cursor compared.

**Text Labels**:
- Headline: "Footprint"
- "Cursor AppImage", "280.6 MiB", "VSCodium AppImage", "184.5 MiB", "Extracted", "795.2 MiB", "Cursor config left behind", "≈ 825 MiB"

---

## Section 6: Install in one step

**Key Concept**: Non-root, no pacman — self-contained and delete-and-go.

**Content**:
- Download the AppImage + `.sha256`, verify with `sha256sum -c`.
- `chmod +x`, symlink `VSCodium.AppImage`.
- Rollback: remove the AppImage, config dirs, launcher; Cursor is purged separately.

**Visual Element**: a terminal window with the install command; a separate trash/removal arrow for Cursor.

**Text Labels**:
- Headline: "Install & remove"
- "sha256sum -c", "chmod +x", "delete-and-go"

---

## Data Points — REFERENCE ONLY (never copy into the prompt)

> Verification only. Do not include in the assembled prompt.

- "No agent; you launch OpenCode yourself in the terminal"
- "No login to launch, edit, or install extensions"
- "update.mode: none"; "the AppImage updates only when you replace the file"
- "An account authentication occurs only when an extension is asking for it."
- "Even if you use your API key, your requests will still go through our backend! That's where we do our final prompt building."
- "we may use and store codebase data, prompts, editor actions, code snippets … to improve our AI features and train our models."
- "your data may be stored for investigation."
- Extensions: `vscodevim.vim` 1.32.4, `shd101wyy.markdown-preview-enhanced` 0.8.40, `yzane.markdown-pdf` 2.2.0
- "Open VSX" — the Eclipse Foundation's vendor-neutral registry
- Footprint: Cursor AppImage 280.6 MiB; VSCodium AppImage 184.5 MiB; VSCodium extracted 795.2 MiB; Cursor config ≈ 825 MiB; "~34% smaller"
- "self-contained and delete-and-go"
- Version `1.140.06880`

---

## Design Instructions

Extracted from the user's steering prompt:

### Style Preferences
- To be chosen in Step 4 (default if unspecified: craft-handmade).

### Layout Preferences
- To be chosen in Step 4 (default if unspecified: bento-grid).

### Other Requirements
- Language: English. Text accuracy over visual density.
