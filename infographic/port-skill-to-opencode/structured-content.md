# Porting a Skill from Hermes Agent to OpenCode

## Overview
A practical 4-step guide to port existing Hermes Agent skills to OpenCode — reuse tested logic, only adjust what OpenCode needs.

## Learning Objectives
The viewer will understand:
1. Hermes and OpenCode skills share the same structure — porting is mostly frontmatter changes
2. The 4-step porting workflow: understand formats → copy & rewrite → fix paths → test
3. Key pitfalls: description rewriting for the skill router, worktree boundary, licensing

---

## Section 1: Understand the Two Formats

**Key Concept**: Hermes and OpenCode skills are structurally identical — both are a `SKILL.md` with frontmatter, plus optional `references/` and `scripts/` folders.

**Content**:
- Hermes skill frontmatter: `name`, `description`, `license`
- OpenCode adds two optional fields: `metadata` (credits original author, useful for publishing) and `compatibility` (informational — OpenCode's loader ignores it, but it documents the skill's target platform)
- The layout is identical — porting is mostly frontmatter + a quick test

**Visual Element**:
- Type: side-by-side comparison
- Left: Hermes frontmatter block (3 fields)
- Right: OpenCode frontmatter block (5 fields, 2 highlighted as optional)
- Treatment: split screen with highlighted differences

**Text Labels**:
- Headline: "Same Structure, Different Frontmatter"
- Left label: "Hermes Agent Skill"
- Right label: "OpenCode Skill"
- Highlight: "2 optional fields added"
- Note: "compatibility is informational only — loader ignores it"

---

## Section 2: Copy & Rewrite the Frontmatter

**Key Concept**: Copy the skill folder, rename it, and rewrite the `description` so the skill router can find it.

**Content**:
- Copy folder: `cp -r ~/.hermes/skills/some-skill .opencode/skills/`
- Rename the folder (e.g. `baoyu-infographic` → `custom-infographic`)
- The `name` field follows the folder name
- Keep original `description` and `license`
- Add `compatibility: opencode` (optional, informational)
- Rewrite `description` with trigger keywords (English + Chinese if relevant)
- Add `metadata` block crediting the original author and upstream repo

**Visual Element**:
- Type: numbered steps with icons
- Subject: folder copy → rename → edit frontmatter
- Treatment: left-to-right flow with arrows

**Text Labels**:
- Headline: "Copy, Rename, Rewrite"
- Step 1: "Copy the folder"
- Step 2: "Rename to avoid confusion"
- Step 3: "Rewrite `description` for the router"
- Step 4: "Add `metadata` for attribution"
- Key callout: "Router matches description text, not filename"

---

## Section 3: Fix Paths & Dependencies

**Key Concept**: The skill body rarely changes — but paths and environment dependencies need attention. OpenCode only loads from inside the project worktree.

**Content**:
- `references/` and `scripts/` live beside `SKILL.md` — relative references keep working if you copy the whole folder
- Worktree boundary: OpenCode only loads skills from inside the project worktree — references to `~/.hermes/...` or paths outside the repo will break
- Check hard-coded paths: Hermes may assume `~/.hermes/...`; OpenCode runs from the project
- Check external dependencies: commands, Python packages, API keys
- `chmod +x` any bundled scripts

**Visual Element**:
- Type: checklist with warning icons
- Subject: path symbols, dependency icons (terminal, package, key), warning triangle for worktree
- Treatment: caution-style with highlights for pitfalls

**Text Labels**:
- Headline: "Watch for Paths & Dependencies"
- Item 1: "Relative paths stay working"
- Item 2: "Worktree boundary: paths outside repo break"
- Item 3: "Check commands, packages, API keys"
- Item 4: "`chmod +x` bundled scripts"

---

## Section 4: Test in OpenCode

**Key Concept**: Start a new session, trigger, and run end-to-end to catch issues early. Skills are loaded at session start, not hot-reloaded.

**Content**:
- Start a new OpenCode session (skills are loaded at session start, not hot-reloaded)
- Ask for the skill's job using its trigger words (e.g. "make an infographic about X")
- If not triggered, tighten the `description` — the router matches that text
- Run the skill's own workflow end to end once

**Visual Element**:
- Type: numbered steps with play/test icons
- Subject: session start → trigger → test → success
- Treatment: clean flow with success indicator

**Text Labels**:
- Headline: "Test End-to-End"
- Step 1: "Start a new session"
- Step 2: "Trigger with keywords"
- Step 3: "Fix description if not picked up"
- Step 4: "Run full workflow once"
- Closing: "A ported skill that's been battle-tested is more reliable than a new one written from scratch"

---

## Section 5: Licensing Note

**Key Concept**: Porting MIT-licensed skills is fine — preserve the license and author attribution, especially when publishing to ClawHub.

**Content**:
- Porting an MIT-licensed skill is fine as long as you preserve the original license and author attribution
- If you plan to publish the port to ClawHub, keep the original author's name in the `metadata` block
- Republishing without attribution creates confusion even if the license allows it

**Visual Element**:
- Type: callout / info box
- Subject: license icon, attribution symbol
- Treatment: subtle sidebar or footer note

**Text Labels**:
- Headline: "Licensing: Preserve Attribution"
- Body: "Keep original license + author name in `metadata`"
- Warning: "Republishing without attribution creates confusion"

---

## Data Points (Verbatim)

### Key Facts
- "structurally the same thing: a `SKILL.md` with frontmatter, plus optional `references/` and `scripts/` folders"
- "The router matches this text, not the filename — a vague description means the skill never gets picked up"
- "OpenCode only loads skills from inside the project worktree — if the original skill references paths outside the repo (e.g. `~/.hermes/...`), those references will break"
- "skills are loaded at session start, not hot-reloaded"
- "porting an MIT-licensed skill is fine as long as you preserve the original license and author attribution"
- "republishing without attribution creates confusion even if the license allows it"

---

## Design Instructions

### Style Preferences
- Clean, minimal line art (ikea-manual style)
- No complex background textures
- Simple icons and diagrams

### Layout Preferences
- Linear left-to-right or top-to-bottom flow
- 5 distinct sections (4 steps + licensing note)
- Side-by-side comparison in Section 1

### Other Requirements
- Include the frontmatter comparison as a visual anchor
- Keep text concise — labels, not paragraphs
- Warning callout for worktree boundary pitfall
