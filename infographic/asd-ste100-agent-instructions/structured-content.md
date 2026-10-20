# The Rules, Not the Words: ASD-STE100 for Agent Instructions

## Overview

ASD-STE100 is a controlled language for aircraft maintenance manuals: 53 writing rules and an 875-word dictionary. Agent instructions need the rules, not the words. Take the four that carry most of the work, measure the result with a linter, and leave the dictionary out.

## Learning Objectives

The viewer will understand:
1. What ASD-STE100 is, and why only the rules transfer to agent instructions.
2. What the four load-bearing rules change in a real prompt.
3. How the rewrite measured out, where the rule belongs, and what it cannot fix.

---

## Section 1: What It Is

**Key Concept**: Two parts — 53 writing rules and a controlled dictionary — built so non-native readers of maintenance manuals cannot misread a step.

**Content**:
- "ASD-STE100 is a controlled language for aircraft maintenance manuals."
- Part 1: 53 writing rules
- Part 2: 875 approved words and 1,274 non-approved words with replacements
- Issue 9, January 2025; the first guide came in 1986

**Visual Element**:
- Type: two-part split panel
- Subject: a rules block and a dictionary block side by side, the rules block emphasised
- Treatment: flat schematic panel, numbered part labels

**Text Labels**:
- Headline: "Two Parts"
- Part 1: "53 writing rules"
- Part 2: "875 approved words"
- Note: "1,274 non-approved words"

---

## Section 2: The Four Rules

**Key Concept**: The rules that carry most of the work for agent instructions.

**Content**:
- "one action per sentence, imperative mood, condition first, and one name for one thing"
- Rule 5.2 — one instruction per sentence
- Rule 5.3 — write instructions in the imperative
- Rule 5.4 — put the condition first
- Rule 1.11 — one name for one item

**Visual Element**:
- Type: four equal rule chips in a row
- Subject: each chip carries a rule number and a one-line rule
- Treatment: uniform rectangles, numbered corner tags

**Text Labels**:
- Headline: "The Four Rules"
- Chips: "Rule 5.2", "Rule 5.3", "Rule 5.4", "Rule 1.11"

---

## Section 3: Before and After

**Key Concept**: One compound prompt becomes two checkable steps.

**Content**:
- "Review the diff and fix the failing test."
- "1. Review the diff. 2. Fix the failing test."
- "Two steps an agent can mark done. The compound version has one checkbox and two jobs."

**Visual Element**:
- Type: before/after pair
- Subject: two stacked terminal-like panels, the left one struck through
- Treatment: left panel muted, right panel clean with numbered steps

**Text Labels**:
- Headline: "Split the Compound Step"
- Before: "Review the diff and fix the failing test."
- After: "1. Review the diff."
- After: "2. Fix the failing test."

---

## Section 4: The Measurement

**Key Concept**: Two rule files, measured before and after the rewrite with the skill's linter.

**Content**:
- Global: 98 sentences, 21 over 20 words (21%), 11 over 25, 7 semicolons, 18 errors → 147, 0, 0, 0, 0
- Project: 77 sentences, 17 over 20 words (22%), 6 over 25, 9 semicolons, 15 errors → 116, 0, 0, 0, 0
- Safety rule: 59 → 62 words

**Visual Element**:
- Type: compact metrics table with before/after columns
- Subject: four rows, two rule files and two counts
- Treatment: monospace numerals, zero cells emphasised

**Text Labels**:
- Headline: "Before and After the Pass"
- Rows: "Global", "Project", "18 errors", "15 errors", "0", "59 → 62 words"

---

## Section 5: Where the Rule Lives

**Key Concept**: A short rule in the always-loaded file, the procedure in a skill, and a linter to settle arguments.

**Content**:
- Short scope rule in the always-loaded rules file
- Full rule set and rewrite procedure in a skill folder
- Deterministic check: `scripts/ste_lint.py`
- The linter checks length, semicolons, banned words, passive voice, phrasal verbs — not meaning

**Visual Element**:
- Type: two-lane diagram
- Subject: an always-on lane and an on-demand lane, joined by a check icon
- Treatment: flat schematic lanes, right-pointing connectors

**Text Labels**:
- Headline: "Rule, Skill, Linter"
- Lane: "Always loaded"
- Lane: "On demand"
- Check: "scripts/ste_lint.py"

---

## Section 6: What It Does Not Buy

**Key Concept**: The standard fixes form, not truth, not policy, not voice.

**Content**:
- "It does not fix correctness."
- "Policy is not procedure."
- "The dictionary is not a reliable control."
- "Voice loss."

**Visual Element**:
- Type: warning band of four notices
- Subject: four outline boxes with warning marks
- Treatment: muted hazard tint, no illustrations

**Text Labels**:
- Headline: "What It Does Not Buy"
- Notices: "Does not fix correctness", "Policy is not procedure", "The dictionary is not a reliable control", "Voice loss in essays"

---

## Data Points — REFERENCE ONLY (never copy into the prompt)

> **Do not include this section in the assembled prompt, and never treat it as a second render list.** Every renderable string already lives in the per-section **Text Labels** above, and is enumerated once in the prompt's `CRITICAL: Text Accuracy` block. This section exists for data-integrity verification only.

### Statistics
- "53 writing rules"; "875 approved words"; "1,274 non-approved words"
- "98", "21 (21%)", "11", "7", "18"; "147", "0", "0", "0", "0"
- "77", "17 (22%)", "6", "9", "15"; "116", "0", "0", "0", "0"
- "59 → 62 words"

### Quotes
- "one action per sentence, imperative mood, condition first, and one name for one thing" — the article's thesis
- "Two steps an agent can mark done. The compound version has one checkbox and two jobs." — the article
- "copy it, run the linter on your rules, and fix your longest rule first" — the takeaway

### Key Terms
- **ASD-STE100**: a controlled language for aircraft maintenance manuals.
- **Rule 5.2**: one instruction per sentence.
- **Rule 5.3**: write instructions in the imperative.
- **Rule 5.4**: put the condition first.
- **Rule 1.11**: one name for one item.
- **Linter**: `scripts/ste_lint.py`, measures form only.

---

## Design Instructions

Extracted from user's steering prompt:

### Style Preferences
- None specified; the skill's recommended combinations apply.

### Layout Preferences
- None specified.

### Other Requirements
- Renderable text stays in English (source and user language both English).
- The image is a summary of `docs/261019-ste100-agent-instructions.md`, not a replacement for it.
