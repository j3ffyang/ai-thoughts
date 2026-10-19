# The Rules, Not the Words: ASD-STE100 for Agent Instructions

**Source:** Andrej Karpathy, X thread, 1 October 2026 — [x.com/karpathy/status/2105819303471976479](https://x.com/karpathy/status/2105819303471976479)

**Thesis:** ASD-STE100 is a controlled language originally built for aircraft maintenance. Its value for AI work is not the ~900-word dictionary. It is the writing rules: one action per sentence, imperative mood, condition first, and one name for one thing. Those rules attack the exact failure mode of agent instructions — a compound sentence that cannot be checked off.

**Verdict:** take the rules and a few high-value substitutions, skip the full 900-word dictionary, and apply it to instructions only. Do not apply it to essays. Treat Karpathy's tip as a starting point, not a standard: he himself asks for "80% of the way to ASD-STE100".

## Where the tip came from

The thread is about reading model output, not about prompting tricks in general. Karpathy's first suggestion is to ask the model to explain something in ASD-STE100 — "a controlled language specification", originally developed for aircraft maintenance manuals. He reports that models know the standard well, and that its "heavy constraints on clean writing style" produce text he finds "a lot more readable". He also admits the spec is "quite stringent", and that he sometimes softens the request to "80% of the way to ASD-STE100".

The rest of the thread moves away from writing: diagrams, then HTML pages, then 3Blue1Brown-style explainer videos, each described as "even better". So the post is really about output formats that are easier to verify. The STE tip is the cheapest of the four, and the only one that is a language constraint.

One leap is worth naming. Karpathy asks a model to write *for a human*; this article asks a human to write *for an agent*. The two directions are not symmetric. A human who hits an ambiguous sentence can ask a follow-up question. An agent that loads `AGENTS.md` at 2am cannot: it will pick a reading, and it will act on it. That asymmetry is why the rules transfer while the evidence does not. The failure mode below is visible in the text itself.

Two things to keep honest. First, this is an anecdote ("I've had success"), not a benchmark. Second, our own implementation ([asd-ste100](https://github.com/j3ffyang/ai-thoughts/tree/main/.opencode/skills/asd-ste100)) does not include the standard's dictionary, because ASD restricts reproduction to authorized organizations. Most people are actually running the rules, not the controlled vocabulary.

## What ASD-STE100 actually is

ASD traces the work to the late 1970s: an AECMA project for European airlines, with the US AIA invited. The first guide came in 1986. The current edition, Issue 9, arrived in January 2025, when the document became an international standard. It is free to read: start at [asd-ste100.org](https://www.asd-ste100.org/), where the [Issue 9 PDF](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) is the source for every rule and example below.

The reason for its existence is narrow and useful: maintenance documentation read by non-native English speakers, where a misread instruction can kill someone. That origin explains both its strength and its limit. It is excellent at procedures with one correct action. It is not a general prose style.

The scope is two parts, and only one of them is a word list:

- **Part 1 — 53 writing rules.** Grammar, sentence length, verb forms, safety instructions, writing practices.
- **Part 2 — a controlled dictionary.** Issue 9 lists **875 approved words** and **1,274 non-approved words** with replacements. The FAQ rounds this to "about 900". For scale, `ensure (v)` is not approved; the replacement is `MAKE SURE (v)`. The non-approved list is this kind of substitution: the least interesting part of the standard, and the part people overestimate.

The dictionary is not a hard wall. Technical nouns and verbs are open by design (the standard's Rules 1.5–1.13): a company, industry, or subject field can add its own terms. What the rules forbid is using those terms loosely — as verbs, as different names for the same item, or as jargon.

The items worth stealing first, each with a small example. These are the smallest wins; the next section takes three structural rules in full.

- `make sure` — "Make sure that the valve is closed." Not "verify" or "ensure".
- `remove`, `install`, `set` — one verb per action: "Remove the four bolts." "Install the new O-ring." "Set the switch to ON."
- `do` — the generic action verb: "Do the pressure test." Not "perform" or "conduct".
- Condition first — "When the light comes on, set the switch to NORMAL."
- No semicolons — write two sentences: "Examine the removed parts for damage. Replace the damaged parts."

## Three examples from the standard

### 1. One instruction per sentence (Rule 5.2)

> Non-STE: `Set the TEST switch to the middle position and release the SHORT-CIRCUIT TEST switch.`
>
> STE: `A. Set the TEST switch to the middle position.` / `B. Release the SHORT-CIRCUIT TEST switch.`

The rule allows an exception: two actions that happen at the same time stay in one sentence ("Remove and discard the seal."). Sequential actions become separate steps. This is the rule that matters most for prompts, because a numbered step can be checked, and a compound sentence cannot. The same applies to a one-off prompt: "review the diff and fix the failing test" is two actions, and only one of them is checkable.

### 2. Short sentences split, they do not trim (Rule 5.1)

> Non-STE (25 words): `Put preservation oil into the unit through the vent hole until the oil level is approximately 6 mm below the surface of the flange cover.`
>
> STE: `Put preservation oil into the unit through the vent hole.` (10 words) `Continue until the oil level is approximately 6 mm below the surface of the flange cover.` (16 words)

Procedures cap at 20 words per sentence. Descriptions cap at 25. The standard is explicit that you divide the sentence; you do not delete the condition to fit the limit. That distinction matters: most "keep it short" advice produces telegraphic text, which STE rejects.

### 3. One name for one thing (Rule 1.11)

> Non-STE: `1. Make sure that the servo control unit is in the open position. 2. Do the operational test of the actuator. 3. Disconnect the control unit from the test rig.`
>
> STE: `1. Make sure that the actuator is in the open position. 2. Do the operational test of the actuator. 3. Disconnect the actuator from the test rig.`

Synonyms read as variety in prose and as ambiguity in procedures. The reader — or the agent — cannot tell whether "control unit" and "actuator" are the same object.

## What it means for prompts and AGENTS.md

### The measurement

Sentence length in my own rule files, paths relative to the `negtivSpace` repo, measured with the skill's linter (`ai-thoughts/.opencode/skills/asd-ste100/scripts/ste_lint.py`, run from the `ai-thoughts` repo root). It strips bold markers, excludes code fences, headings, and table rows, and counts a code span as one word:

| File | Sentences | Over 20 words | Over 25 words |
|---|---|---|---|
| `opencode/AGENTS.md` (before) | 94 | **21 (22%)** | 12 |
| `opencode/AGENTS.md` (after) | 147 | **0** | 0 |
| `ai-thoughts/AGENTS.md` | 77 | **17 (22%)** | 6 |
| `negtivSpace/AGENTS.md` | 130 | 1 (1%) | 1 |

Before the pilot, about a fifth of the sentences in the two working-rule files broke the 20-word limit. The pilot took `opencode/AGENTS.md` to zero: no sentence over 20 words, and no semicolons. `ai-thoughts/AGENTS.md` is unchanged at 17 (22%). The root file was already nearly clean, because it is written as short bullets.

### The worst offender

The safety rule in `opencode/AGENTS.md` ran almost 60 words before the pilot, with the trigger buried after three imperatives:

> "**STOP and RAISE HANDS immediately** — halt the run, do not continue, report to the user at once with what was attempted — if executed code reads the filesystem outside `/tmp`…"

The sentence continued with four more triggers: credentials, data exfiltration, child processes or network connections, and deceptive behavior. I applied Rule 5.4 (condition first) and Rule 5.2 (one action per sentence):

```
If executed code does any of these things, stop:
- reads files outside /tmp
- touches process.env, keys, tokens, or credentials
- collects or sends local data off the machine
- starts child processes, or opens unauthorized network connections
- shows malicious, harmful, deceptive, cheating, or stealing behavior
Do not continue the run. Report to the user now. Say what was attempted.
```

Same policy, no dropped condition, four checkable actions, five flat triggers. The rewrite is not shorter than the original. STE trades brevity for checkability, and the pilot confirms it: the file went from 19 linter errors to zero.

### What the constraint buys

- **Checkability.** One action per sentence means each rule can be marked done or not done.
- **Policy vs description.** Rule 5.3 (imperative) forces "Run the linter." over "the linter should be run" — the second is advice, not a rule.
- **Condition-first ordering.** Rule 5.4 maps directly onto permission and safety rules, where the trigger must be read before the action.
- **No synonym drift.** Rule 1.11 is the discipline already enforced by hand: `OpenCode` (product) versus `opencode` (binary).
- **Fewer silent ambiguities.** Keeping articles and using active voice (Rules 3.6, 4.2) prevent the telegraphic style that makes short rules unparseable.

### What it does not buy

**It does not fix correctness.** One public experiment with the STE prompt ([Mysore, Oct 2026](https://medium.com/@visrow/karpathy-says-make-your-llm-write-like-an-aircraft-manual-i-built-a-browser-tool-to-measure-it-17f0aaeb86b4)) found that the formatted answer still dropped a safety-critical detail: it said "connect cables to both battery terminals" without saying which cable goes where. Form constraints do not make facts true. Any article claiming otherwise is overselling.

**Policy is not procedure.** `AGENTS.md` carries priorities, exceptions, and rationale: *prefer X unless Y; ask if unsure*. STE was designed for procedures with exactly one correct action, and it has no vocabulary for tradeoffs. Flattening conditional policy into imperatives can make an agent more literal and less correct. Rewrite the actions; leave the reasoning as descriptive text under the 25-word limit.

**The dictionary is not a reliable control.** Model familiarity with STE is plausible but unmeasured, and the 875-word list cannot simply be bundled, because ASD restricts reproduction. If determinism matters, a linter plus your own short banned-words list is the only honest route, not a prompt that names the standard.

**Word counts break on identifiers.** `opencode.jsonc`, a path, or an API name is one word for a human and several for a counter. Any lint must exclude code spans and identifiers, or every technical rule fails.

**Voice loss.** The articles in `docs/` are essays. Applying STE there would flatten the register that makes them readable. The constraint belongs to instructions, not prose. This article is itself an essay, so it keeps its long sentences; judging it by Rule 5.1 would be a category error.

## AGENTS.md rule or SKILL.md?

The two options are not exclusive, and the repository already has a precedent for splitting them. `thought-flow` is a short summary in the global `AGENTS.md` plus a full skill. `arch-sign-off` is a short rule in `AGENTS.md` plus a skill that holds the exact command.

| Piece | Where | Why |
|---|---|---|
| Short scope rule | `opencode/AGENTS.md` → Writing conventions | Always loaded; small enough to obey |
| Full rule set and rewrite procedure | `ai-thoughts/.opencode/skills/asd-ste100/` | On demand; 53 rules must not sit in always-on context |
| Deterministic check | `scripts/ste_lint.py` inside the skill | A model judging its own sentence length is unreliable |

A rule alone would be too vague to act on. A skill alone may not load during ordinary edits. The rule states the scope; the skill carries the detail; the script settles arguments.

Boundary check: `opencode.jsonc` already points `skills.paths` at `ai-thoughts/.opencode/skills`, scanned recursively, so a skill placed there loads in every session regardless of the working directory. No new global directory is needed, and no per-repo copy is needed either.

A candidate `AGENTS.md` rule, kept short enough to obey itself:

```md
**Instruction writing (STE-lite).** Applies to prompts, AGENTS.md, SKILL.md, and checklists — never to articles, essays, or translations.
- Write one action per sentence. Split compound steps.
- Write instructions in the imperative: "Run the linter." Not "the linter should be run".
- Put the condition first, then a comma: "If the check fails, read the log."
- Use one name for one thing. Do not rotate synonyms for a file, command, or concept.
- Keep instructions to 20 words and descriptions to 25. Do not count code spans or identifiers.
- Keep the reason for a rule as description. Do not delete a condition or exception to meet the limit.
- Keep technical names verbatim: paths, commands, identifiers.
For the full standard, load the `asd-ste100` skill.
```

The skill now lives at `ai-thoughts/.opencode/skills/asd-ste100/`:

```
asd-ste100/
  SKILL.md               # when to use, the 10 core rules, rewrite procedure, exclusions
  references/rules.md    # condensed 53 rules by section
  scripts/ste_lint.py    # length, semicolons, banned words, passive, phrasal verbs
```

The linter is the part that makes this more than a style preference. Useful checks: sentence length over 20 or 25 words, semicolons outside code, banned words (`ensure`, `utilize`, `leverage`, `facilitate`, `commence`, `prior to`, `in order to`), passive voice (`be` plus a past participle), and phrasal verbs. It does not check meaning, one action per sentence, or synonym drift.

## How to apply it

1. **Pilot on one file.** Rewrite `opencode/AGENTS.md` only, and measure before and after. Do not touch `ai-thoughts/AGENTS.md` until the numbers justify it; much of it instructs the human, not the agent.
2. **Rewrite rules, not rationale.** Keep the "why" sentences as descriptions under the 25-word limit. Deleting reasoning to meet a word count is a net loss.
3. **Start with `STOP and RAISE HANDS`.** It is the highest-stakes rule and the longest sentence. The pilot started there and ended at zero errors.
4. **Use the skill.** It lives at `ai-thoughts/.opencode/skills/asd-ste100/` and loads in every session. Publish it only after it has proved itself twice.
5. **Leave the articles alone.** If STE helps an article, it helps by removing ambiguity in technical steps, not by flattening the voice.

## What is still not done

The pilot edited `opencode/AGENTS.md`. All 19 linter errors are gone, and every rule, condition, and exception survived. The [`asd-ste100`](https://github.com/j3ffyang/ai-thoughts/tree/main/.opencode/skills/asd-ste100) skill summarizes the rules and omits the dictionary; it is not the standard. `ai-thoughts/AGENTS.md` is unchanged at 17 sentences over 20 words. The open question is no longer whether the limits survive real rules. It is whether the rewritten file reads as clearly to a human as it does to the linter.

The next step is to use the rewritten rules for a week, then wire the linter into review. A rule that cannot be checked will drift back to its original shape within a month.

btw, i use arch
