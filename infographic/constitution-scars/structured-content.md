# AGENTS.md Is Not a Persona — It's a Constitution Written in Scars

## Overview
An infographic tracing how real-world failures in AI agent configuration produce durable operational rules — the "scars" that form a constitution more valuable than any persona prompt.

## Learning Objectives
The viewer will understand:
1. Why persona instructions ("You are a senior dev") are less valuable than operational rules earned through failure
2. Three major failure modes (and five brief ones) that produce lasting config rules
3. The four traits that make a rule survive: traceable to incident, single owner, verifiable, cheap to obey

---

## Section 1: The Thesis — Persona vs Constitution

**Key Concept**: A persona claims what an agent is; a constitution constrains what it may do. The second is case law.

**Content**:
- "A persona claims what an agent is. A constitution constrains what it may do. The first is a wish; the second is case law."
- "Rules that were not imagined but *earned*, each one traceable to a specific incident where something went wrong and never should again."

**Visual Element**:
- Type: binary comparison / split panel
- Left: persona — a mask or costume icon, soft/dreamy
- Right: constitution — a scarred document or case law book, worn/real
- Treatment: stark contrast between wishful and earned

**Text Labels**:
- Headline: "Persona vs Constitution"
- Left label: "A wish"
- Right label: "Case law"
- Subhead: "The valuable content is operational law"

---

## Section 2: Scar I — A Repo That Cloned Itself

**Key Concept**: An agent silently poisoned a managed repo with a nested clone, and the author didn't notice for four days.

**Content**:
- Date: August 17th
- Agent ran `git clone` into a managed workspace tree
- Shell history was empty (agents run non-interactive shells)
- Session database recorded everything: command, timestamp, triggering message
- Rule: "never poison a working tree with scratch artifacts"
- At scale: poisons `git status`, breaks project-root detection, trains you to ignore warnings

**Visual Element**:
- Type: detective / forensic scene
- Subject: a workspace directory tree with a foreign repo nested inside, marked with a warning
- Treatment: evidence-board feel — fingerprints, timeline, the clone as the "crime"

**Text Labels**:
- Headline: "Scar I: A Repo That Cloned Itself"
- Rule: "never poison a working tree with scratch artifacts"
- Detail: "Shell history: empty. Session database: everything."
- Detail: "Left behind like a cigarette butt"

---

## Section 3: Scar II — The Documentation That Lied

**Key Concept**: Two surfaces describing the same fact will drift, and drift toward false confidence.

**Content**:
- Permission setup described in two places: AGENTS.md and config file comments
- A sentence claimed unmatched shell commands were "silently denied"
- Truth: unmatched commands run silently *allowed* under a permissive default
- Wrong sentence sat for weeks asserting the security posture the author wished they had
- Fix: one file is the human-facing truth, the other quotes it; deduplicate until each fact has one home

**Visual Element**:
- Type: two documents side by side with diverging arrows
- Subject: two config surfaces drifting apart, one labeled "truth" and one labeled "wish"
- Treatment: the drift shown as a growing gap between them

**Text Labels**:
- Headline: "Scar II: The Documentation That Lied"
- Key line: "toward more confidence, less truth"
- Fix: "One source of truth per fact"

---

## Section 4: Scar III — The Prompt Flood

**Key Concept**: Security theater gets deleted under pressure — calibrate interruptions to only when they matter.

**Content**:
- Earlier config: catch-all requiring approval for everything
- Author reflexively approved things unread — worse than not being asked
- Replaced with allow-driven design: read-only runs silently, destructive commands prompt
- Durable insight: "security theater gets deleted under pressure, and when it goes, it takes the real protections down with it"
- "Rules that survive contact with daily work are rules calibrated to interrupt only when interruption matters"

**Visual Element**:
- Type: funnel or flow diagram
- Subject: all commands → approval gate (old) vs filtered: destructive commands → prompt, read-only → silent (new)
- Treatment: the old path clogged with prompts, the new path clean

**Text Labels**:
- Headline: "Scar III: The Prompt Flood"
- Old: "Everything requires approval"
- New: "Allow-driven by design"
- Insight: "Security theater gets deleted under pressure"

---

## Section 5: Further Scars (Compressed)

**Key Concept**: Five quick lessons — concatenate, verify source, deduplicate, distinguish drift from error, scope approvals.

**Content**:
- "Instruction files concatenate — they are a pile, not a cascade"
- "When docs and behavior disagree, the behavior ships and the docs apologize later"
- "Symlinked config… fails in ways that look like continued success"
- "Hygiene signals and errors are different species"
- "Session-scoped approvals die with the session, and permanent rules belong in versioned config"

**Visual Element**:
- Type: five compact modules / tiles
- Subject: each scar as a small icon + one-line rule
- Treatment: quick-scan, grid layout within the section

**Text Labels**:
- Headline: "Further Scars"
- Tile 1: "Pile, not cascade"
- Tile 2: "Verify against source"
- Tile 3: "Infrastructure lies gracefully"
- Tile 4: "Drift ≠ Error"
- Tile 5: "Session vs Permanent"

---

## Section 6: The Constitution Outlives the Model

**Key Concept**: The instruction file persists across model swaps — institutional memory written in failure.

**Content**:
- Four traits of durable rules: traces to incident, single owner, verifiable, cheap to obey
- "The agent that cloned that repo will be swapped for a better one, probably soon"
- "The instruction file and the permission config are the parts that persist — institutional memory written in failure, readable by whatever model comes next"
- "A persona is addressed to today's model; a constitution is addressed to their successors"
- "Write down what went wrong, name the date, state the rule, and make the next inhabitant of your terminal inherit the scar instead of reopening the wound"

**Visual Element**:
- Type: timeline or succession diagram
- Subject: model versions fading out, the config file remaining constant
- Treatment: the file as a scarred but enduring document, passed between generations

**Text Labels**:
- Headline: "The Constitution Outlives the Model"
- Subhead: "Institutional memory written in failure"
- Closing: "Inherit the scar instead of reopening the wound"

---

## Data Points (Verbatim)

### Quotes
- "A persona claims what an agent is. A constitution constrains what it may do. The first is a wish; the second is case law."
- "never poison a working tree with scratch artifacts"
- "toward more confidence, less truth"
- "security theater gets deleted under pressure, and when it goes, it takes the real protections down with it"
- "inherit the scar instead of reopening the wound"
- "institutional memory written in failure, readable by whatever model comes next"

### Key Terms
- **AGENTS.md**: Markdown instruction file shaping how an agent judges
- **Persona prompt**: Instructions claiming what an agent is ("You are a senior dev")
- **Constitution**: Operational rules constraining what an agent may do, earned through failure
- **Scar**: A rule traceable to a specific incident where something went wrong

---

## Design Instructions

### Style Preferences
- None specified — default to recommended combination

### Layout Preferences
- None specified — default to recommended combination

### Other Requirements
- None specified
