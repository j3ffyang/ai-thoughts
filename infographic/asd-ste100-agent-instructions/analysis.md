---
title: "The Rules, Not the Words: ASD-STE100 for Agent Instructions"
topic: "technical / writing standard"
data_type: "overview + comparison + metrics"
complexity: "complex"
point_count: 9
source_language: "en"
user_language: "en"
---

## Main Topic

ASD-STE100 is an aircraft-maintenance writing standard with 53 rules and a controlled dictionary. For agent work, the value is the rules — one action per sentence, imperative mood, condition first, one name per item — not the word list. Applying them to `AGENTS.md`, `SKILL.md`, and prompts turns compound instructions into steps an agent can check.

## Learning Objectives

After viewing this infographic, the viewer should understand:
1. What ASD-STE100 is, and why the rules transfer to agent instructions while the dictionary does not.
2. What the four load-bearing rules look like before and after, on a real prompt.
3. What the measured effect was, where the rule should live, and what the standard cannot buy.

## Target Audience

- **Knowledge Level**: Intermediate — developers who write `AGENTS.md`, `SKILL.md`, or long prompts.
- **Context**: Arriving from a Karpathy thread about asking models to write in ASD-STE100; wants a practical translation to agent instructions.
- **Expectations**: The rules, a worked before/after, numbers, and an honest list of limits.

## Content Type Analysis

- **Data Structure**: A standard (what it is) → four rules (how it reads) → before/after examples → measured effect → placement (rule vs skill) → limits.
- **Key Relationships**: rules ↔ dictionary; compound sentence ↔ checkable step; rule file ↔ loaded-every-session; linter ↔ form only.
- **Visual Opportunities**: a two-part split (53 rules / controlled dictionary), four rule chips, a before/after prompt pair, a small metrics table, a two-lane placement diagram (rule + skill), a warning band of limits.

## Key Data Points (Verbatim)

- "53 writing rules" (Part 1); "875 approved words" and "1,274 non-approved words" (Part 2); the FAQ rounds it to "about 900"
- Issue 9, January 2025; the first guide came in 1986; late 1970s AECMA project
- Rules cited: 5.1 (20 words procedures), 6.3 (25 words descriptions), 5.2 (one instruction per sentence), 5.3 (imperative), 5.4 (condition first), 1.11 (one name per item), 8.1 (no semicolons), 4.5 (articles, new in Issue 9), 3.6 (active voice)
- Preservation-oil example: 25 words → "10 words" + "16 words"
- One-off prompt: "Review the diff and fix the failing test." → "1. Review the diff. 2. Fix the failing test."
- Safety rule: 59 → 62 words; "the file went from 18 linter errors to zero"
- Measurement, Global: before 98 / 21 (21%) / 11 / 7 / 18 → after 147 / 0 / 0 / 0 / 0
- Measurement, Project: before 77 / 17 (22%) / 6 / 9 / 15 → after 116 / 0 / 0 / 0 / 0
- Karpathy's softening: "80% of the way to ASD-STE100"
- "one action per sentence, imperative mood, condition first, and one name for one thing"
- Takeaway: "copy it, run the linter on your rules, and fix your longest rule first"

## Layout × Style Signals

- Content type: overview with a comparison and a small metrics block → suggests `dense-modules` or `bento-grid`
- Tone: technical, instructional, honest about limits → suggests `technical-schematic` or `pop-laboratory`
- Audience: developers who read specifications → tolerant of density, expects precision markers
- Complexity: complex (9 points) → dense layout with clear section separation

## Design Instructions (from user input)

The user invoked the skill on the article with no style, colour, layout, aspect, or language instruction. Defaults apply unless overridden at confirmation.

## Recommended Combinations

1. **dense-modules + technical-schematic** (Recommended): a specification-sheet treatment, fitting for an engineering standard; carries the rules, the numbers, and the limits without decoration.
2. **bento-grid + pop-laboratory**: modular panels with a lab-precision grid; good when the four rules and the metrics should each read as a separate instrument.
3. **binary-comparison + ikea-manual**: a minimal line-art before/after; best if the piece should teach one transformation only.
4. **dashboard + corporate-memphis**: the measurement table as the centrepiece, with the rules as supporting cards.
