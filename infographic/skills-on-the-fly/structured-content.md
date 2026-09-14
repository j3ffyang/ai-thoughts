# Create SKILL.md, AGENTS.md, and PERSONA.md on the fly

## Overview
Why hunt through skill marketplaces when you can write the skill you need while you work? Real experience of the three customization levels — SKILL.md, AGENTS.md, PERSONA.md — and the 5-step loop that keeps them growing.

## Learning Objectives
The viewer will understand:
1. That creating your own skill/config files beats finding one that only half-fits.
2. The three levels of agent customization and when each is used.
3. The on-the-fly loop and the benefits of owning every line.

---

## Section 1: Objective

**Key Concept**: Write the skill you need while you work — it does exactly what you want because you wrote it.

**Content**:
- Instead of hunting through skill marketplaces and community hubs for a skill that only half-fits, you write the one you need while you work.
- "it does exactly what you want, because you wrote it"
- Real, authentic experience from working with AI over the past few years.

**Visual Element**:
- Type: icon scenes
- Subject: a person choosing between a big market shelf (half-fitting puzzle piece) and writing their own puzzle piece on the spot
- Treatment: hand-drawn doodle, small comparison

**Text Labels**:
- Headline: "Write it yourself"
- Label: "exactly what you want"
- Label: "because you wrote it"

---

## Section 2: The Approach — three levels

**Key Concept**: Customization comes in three file types, from procedure to rules to personality.

**Content**:
- The examples come from OpenCode but work the same on Claude Code, Gemini CLI, OpenClaw, Hermes.
- "I don't see much difference among them"
- Three levels: create a custom SKILL.md while working; define requirements in AGENTS.md; add personality in PERSONA.md.

**Visual Element**:
- Type: three stacked cards / three columns
- Subject: one card per file: SKILL.md «procedure», AGENTS.md «rules», PERSONA.md «personality»
- Treatment: tidy, labeled, color-coded

**Text Labels**:
- Headline: "Three levels of customization"
- Card 1: "SKILL.md — procedure"
- Card 2: "AGENTS.md — rules"
- Card 3: "PERSONA.md — personality"

---

## Section 3: The 5-step loop

**Key Concept**: You never start intending to write a skill — a clear loop shows up while working, and that is the moment to create it.

**Content**:
- "While working, you discover some task that needs to be done over and over again in a clear loop"
- "The loop, in practice, is always the same:"
- Step 1: Spot the loop — a task that keeps showing up while you work.
- Step 2: Write the file — a SKILL.md (or an AGENTS.md rule, or a PERSONA.md voice) describing it precisely.
- Step 3: Use it the next time it appears — the agent matches the description and takes over.
- Step 4: Tighten it on the fly — add stricter conditions, handle edge cases, check duplicates.
- Step 5: Own it — every line is yours, so it's exact and safe.

**Visual Element**:
- Type: circular flow diagram
- Subject: 5 numbered nodes on a circle with arrows, returning to "spot the loop" (endless cycle)
- Treatment: big clear numbers, arrows to show the repeat

**Text Labels**:
- Headline: "The loop, in practice, is always the same"
- Nodes: "1 Spot", "2 Write", "3 Use", "4 Tighten", "5 Own"
- Tagline at center: "on the fly"

---

## Section 4: Custom SKILL.md

**Key Concept**: A SKILL.md is a markdown file that describes one task — it loads only when it matches, staying out of the way otherwise.

**Content**:
- Located at `.opencode/skills/<skill-name>/SKILL.md`
- States what the skill does, when to use it, and how to do the work.
- "The agent loads it only when it matches its description, so it stays out of the way the rest of the time."
- Example: everbox.io blog sync — "The whole workflow is 100% automated without human touch."
- Example: automatically publish skills to clawhub.ai/j3ffyang/skills/publish-skills
- Example: bold-highlights skill — "All highlights are automatically generated"
- Example: add "btw, i use arch" at the end of each blog post.
- "Whenever I find a good point or a stricter condition, I modify or optimize my custom SKILL.md on the fly, while checking for duplicate entries if applicable."

**Visual Element**:
- Type: file card + mini-workflow strip
- Subject: a SKILL.md document with a small pipeline (markdown → npm test → git push → live) and three example chips
- Treatment: doodle document with an automation arrow showing "on the fly"

**Text Labels**:
- Headline: "SKILL.md — one task, one file"
- Chip examples: "blog sync", "publish-skills", "bold-highlights"
- Sign-off chip: "btw, i use arch"

---

## Section 5: AGENTS.md

**Key Concept**: The constitution of a repository — standing rules that apply every session.

**Content**:
- Defines the standing rules that apply every session:
  - get approval before any change
  - commit only when asked
  - never commit secrets
  - give honest answers
  - always make sure a change can be rolled back
- Also holds writing conventions such as filename patterns and the no-hard-wrap rule.
- "Use specific, explicit words when you talk to your agent. I found that when I use the term ground truth, the agent seriously cross-checks the source."
- "The agent reads AGENTS.md at the start of every session, so it knows the rules before it does anything."

**Visual Element**:
- Type: constitution / rule-list panel
- Subject: a document styled like a constitution with 5 short rule chips and a highlighted "ground truth" chip
- Treatment: authoritative but hand-drawn friendly

**Text Labels**:
- Headline: "AGENTS.md — the repo's constitution"
- Rules: "approval first", "commit when asked", "never commit secrets", "honest answers", "rollback always"
- Highlight: "ground truth"

---

## Section 6: PERSONA.md

**Key Concept**: An optional file that gives the agent a consistent personality and voice.

**Content**:
- Optional; some platforms use a config setting instead.
- Gives the agent "a consistent personality and voice".
- "Honestly, I don't use it much in practice — but when you work on content (writing, translations, blog posts) and want the output to always sound like you rather than like a generic assistant, it earns its keep."
- Remember: a restart may be needed for any new file to be picked up — "Don't assume your new file or rule is live the moment you save it."

**Visual Element**:
- Type: speech-bubble / mirror card
- Subject: a mirror with the agent's "voice" versus a generic assistant
- Treatment: warm doodles, quote bubbles

**Text Labels**:
- Headline: "PERSONA.md — a voice that sounds like you"
- Labels: "consistent personality", "restart to pick up"

---

## Section 7: Benefit

**Key Concept**: Every benefit is ground truth from daily use — not marketing copy.

**Content**:
- simple
- secure — you wrote every line, so you know exactly what it does
- independent — you use your own, not someone else's
- some community skills are simply not good enough, and they don't fit your exact requirements
- accurate — the workflow can be very accurate and precise, without you having to re-explain it every time
- smarter — writing it forces you to understand the workflow's logic precisely

**Visual Element**:
- Type: benefit chip row
- Subject: six short chips with a small icon each
- Treatment: bold labels, simple icons

**Text Labels**:
- Chips: "simple", "secure", "independent", "accurate", "smarter", "not good enough (others)"

---

## Section 8: Reason to Use OpenCode + the push

**Key Concept**: No provider lock-in, terminal-native, and this is the fastest way to make the agent yours.

**Content**:
- "OpenCode keeps me free from any AI provider lock-in while I can switch between hundreds of models on demand."
- "It runs in the terminal — the lowest dependency footprint I know."
- "Next time you catch yourself repeating a task, don't go hunting in a marketplace — write your own SKILL.md, AGENTS.md, or PERSONA.md on the fly. It's the fastest way to make the agent truly yours."

**Visual Element**:
- Type: terminal + CTA banner
- Subject: a small terminal window with a final call-to-action line
- Treatment: clear banner, one bold sentence

**Text Labels**:
- Headline: "Make the agent truly yours"
- CTA: "Write your own — on the fly"
- Sign-off: "btw, i use arch"

---

## Data Points (Verbatim)

### Key Phrases
- "create your own" / "exactly what you want, because you wrote it"
- "clear loop"
- "The loop, in practice, is always the same"
- "100% automated without human touch"
- "the agent seriously cross-checks the source"
- "consistent personality"
- "btw, i use arch"

### Key Terms
- **SKILL.md**: a procedure for a specific task — what it does, when to use it, how to do the work
- **AGENTS.md**: the constitution of a repository — standing rules for every session
- **PERSONA.md**: an optional file giving the agent a consistent personality and voice
- **ground truth**: using this exact word makes the agent seriously cross-check the source

---

## Design Instructions

### Style Preferences
- None provided by user. Content-driven defaults only.

### Layout Preferences
- None provided. Candidate layouts: circular-flow, linear-progression, hub-spoke (see analysis.md recommendations).

### Other Requirements
- Language: English. Final image goes to `imgs/260906-skills-on-the-fly.png` (article's YYMMDD prefix, repo convention).