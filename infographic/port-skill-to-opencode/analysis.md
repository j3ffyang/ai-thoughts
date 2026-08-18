---
title: "How to Port a Skill from Hermes Agent to OpenCode"
topic: "technical tutorial"
data_type: "process"
complexity: "moderate"
point_count: 4
source_language: "en"
user_language: "en"
---

## Main Topic
A practical 4-step guide for porting an existing Hermes Agent skill to OpenCode, preserving tested logic while adjusting frontmatter, paths, and dependencies.

## Learning Objectives
After viewing this infographic, the viewer should understand:
1. Hermes and OpenCode skills share the same structure — porting is mostly frontmatter changes
2. The 4-step porting workflow: understand formats → copy & rewrite → fix paths → test
3. Key pitfalls: description rewriting for the skill router, worktree boundary, dependencies, licensing

## Target Audience
- **Knowledge Level**: Intermediate — familiar with AI agent skills, has used Hermes Agent or similar
- **Context**: Wants to reuse existing Hermes skills in OpenCode without rewriting from scratch
- **Expectations**: Clear, actionable steps with minimal fluff

## Content Type Analysis
- **Data Structure**: Sequential process with 4 distinct steps, each with sub-actions
- **Key Relationships**: Step 1 (understand) → Step 2 (copy/rewrite) → Step 3 (fix paths) → Step 4 (test)
- **Visual Opportunities**: Side-by-side frontmatter comparison (Hermes vs OpenCode), numbered step flow, warning callouts for pitfalls

## Key Data Points (Verbatim)
- "structurally the same thing: a `SKILL.md` with frontmatter, plus optional `references/` and `scripts/` folders"
- "OpenCode uses the same `name`, `description`, and `license` fields. Two optional additions: `metadata` and `compatibility`"
- "The `name` field in frontmatter follows the folder name"
- "The router matches this text, not the filename — a vague description means the skill never gets picked up"
- "OpenCode only loads skills from inside the project worktree — if the original skill references paths outside the repo (e.g. `~/.hermes/...`), those references will break"
- "skills are loaded at session start, not hot-reloaded"
- "porting an MIT-licensed skill is fine as long as you preserve the original license and author attribution"
- "republishing without attribution creates confusion even if the license allows it"

## Layout × Style Signals
- Content type: process/tutorial → suggests linear-progression
- Tone: practical, direct → suggests ikea-manual
- Audience: developers/technical → suggests technical-schematic or ikea-manual
- Complexity: moderate (4 steps) → balanced linear flow

## Design Instructions (from user input)
None specified — using defaults.

## Recommended Combinations
1. **linear-progression + ikea-manual** (Recommended): Clean step-by-step flow with minimal line art, perfect for a 4-step technical tutorial
2. **linear-progression + craft-handmade**: Hand-drawn feel adds warmth to a technical topic
3. **linear-progression + technical-schematic**: Blueprint aesthetic for a developer audience
