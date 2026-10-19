# ASD-STE100 rewrite log — `opencode/AGENTS.md`

**Status:** working record, 2026-10-19. This is not an article.

**Scope:** one file, one pass, measured before and after with the [`asd-ste100`](https://github.com/j3ffyang/ai-thoughts/tree/main/.opencode/skills/asd-ste100) skill.

## Why keep this

The article argues that the STE rules make agent instructions checkable. This file is the evidence: the actual change to the global rules, with the diff, the measurements, and the decisions.

## Result

| Measure | Before | After |
|---|---:|---:|
| Sentences | 94 | 147 |
| Over 20 words | 21 (22%) | **0** |
| Over 25 words | 12 | **0** |
| Semicolons | 7 | **0** |
| Linter errors | 19 | **0** |
| Linter warnings | 17 | 5 |
| Words | 1,444 | 1,437 |

The five remaining warnings are passive voice in descriptions: "being edited", "be rolled back", "was attempted", "is summarized", "be maintained". Rule 3.6 permits passive in descriptions when the agent is unknown, so they stay.

The file ended seven words shorter overall, but the `STOP` rewrite itself grew from 59 to 62 words. Splitting usually adds words; here other trims offset it. STE trades brevity for checkability, not the other way around.

## Method

Run from the `ai-thoughts` repo root:

```bash
python3 .opencode/skills/asd-ste100/scripts/ste_lint.py ../opencode/AGENTS.md
```

The linter strips bold markers, excludes code fences, headings, and table rows, counts a code span as one word, and reports sentences over 25 words as errors, over 20 as warnings, plus semicolons and non-approved words.

## Patterns applied

1. **Condition first.** The `STOP and RAISE HANDS` rule put three commands before a ten-item trigger; the trigger now comes first, as a list.
2. **One action per sentence.** Commit/push, whole-project review, investigate, and press each became two or three sentences.
3. **Semicolons split.** Seven semicolons became sentence breaks: retry paths, skill loading, intent, verification, glyphs, permissions, and the registry caveat.
4. **Bracketed asides promoted to sentences.** Parentheticals about the account type, the source of truth, and the login incident are now their own sentences.
5. **Non-approved words replaced.** `Ensure` became `Make sure`; `require an opencode restart` became `Restart opencode after you change the config`.
6. **A false mechanism removed.** The Boundary-check bullet claimed skills load only up to the worktree root, which the corrected line and `opencode.jsonc` contradict. The lesson stays; the wrong mechanism is gone.

## The actual diff

```diff
diff --git a/opencode/AGENTS.md b/opencode/AGENTS.md
index 75311d7..c8d33dd 100644
--- a/opencode/AGENTS.md
+++ b/opencode/AGENTS.md
@@ -6,24 +6,30 @@ Universal working rules that apply to every opencode session, across all `negtiv
 
 - **Get approval before any change.** Present the plan and wait for the user's explicit go-ahead before editing files, generating output, or running state-changing commands. If anything is unclear, ask rather than assume.
 - **Commit only when asked.** Never commit, amend, or push unless the user explicitly requests it. When committing, stage only intended files and follow the repo's `type: subject` commit style (e.g. `docs: ...`, `ci: ...`).
-- **Untracked files are work in progress — never commit them unasked.** Assume every untracked file is still being edited (this is the default state for drafts in `history/` and `ai-thoughts/`). Do not stage an untracked file, and never run `git add -A` / `git add .`, unless the user explicitly names that file for this commit. Commit and push only on the user's explicit go-ahead, and default to one file (or one tightly-scoped change) per commit — do not bundle multiple files unless the user asks.
-- **NEVER commit secrets or API keys.** Before staging, scan for hardcoded credentials (`sk-*`, `sk-or-v1-*`, `AIza*`, `gh*_*`, `github_pat_*`, `Bearer <token>`) and never stage `.env`, `.pem`, `.key`, or credential files. Use repo/CI secrets (`${{ secrets.X }}`) instead of literals. If a real key is ever found already committed to a public repo, say so immediately and suggest rotation.
-- **NEVER poison a working tree with scratch artifacts.** Throwaway clones, test checkouts, and any temporary git artifact belong in `/tmp/opencode/` — NEVER inside `~/pool/git/**` or any managed repo. A stray nested repo corrupts `git status`, breaks project-root detection, and litters the workspace (this already happened once: a profile-sync clone left behind in `negtivSpace/` on 2026-08-17). If one exists, remove it before finishing the task; if the task needs a working copy of another repo, clone it to `/tmp/opencode/` and delete it when done.
-- **Push to both remotes** on `main` for repos under `negtivSpace`: `j3ffyang` and `negtivspace`. `negtivspace` is a normal GitHub **user account** (a second personal account, "Negative Space 留白"), not an org — editing `negtivspace/*` via `gh`/API requires that account's own token.
+- **Untracked files are work in progress — never commit them unasked.** Assume every untracked file is still being edited (this is the default state for drafts in `history/` and `ai-thoughts/`). Do not stage an untracked file unless the user explicitly names it for this commit. Never run `git add -A` or `git add .`. Commit and push only on the user's explicit go-ahead. Default to one file, or one tightly-scoped change, per commit. Do not bundle multiple files unless the user asks.
+- **NEVER commit secrets or API keys.** Before staging, scan for hardcoded credentials (`sk-*`, `sk-or-v1-*`, `AIza*`, `gh*_*`, `github_pat_*`, `Bearer <token>`). Never stage `.env`, `.pem`, `.key`, or credential files. Use repo/CI secrets (`${{ secrets.X }}`) instead of literals. If a real key is ever found already committed to a public repo, say so immediately and suggest rotation.
+- **NEVER poison a working tree with scratch artifacts.** Throwaway clones, test checkouts, and any temporary git artifact belong in `/tmp/opencode/` — NEVER inside `~/pool/git/**` or any managed repo. A stray nested repo corrupts `git status` and breaks project-root detection. It also litters the workspace. This happened once: a profile-sync clone was left in `negtivSpace/` on 2026-08-17. If one exists, remove it before you finish the task. If the task needs a working copy of another repo, clone it to `/tmp/opencode/`. Delete it when done.
+- **Push to both remotes** on `main` for repos under `negtivSpace`: `j3ffyang` and `negtivspace`. `negtivspace` is a normal GitHub **user account**, not an org. It is a second personal account, "Negative Space 留白". Editing `negtivspace/*` via `gh`/API requires that account's own token.
 - **Profile-hub exception.** The `negtivSpace` root repo mirrors the two profile repos, whose histories diverge by design. Push its docs/infra to `j3ffyang` only, and apply workflow changes to both. Details: `negtivSpace/AGENTS.md`.
 - **Give HONEST answers.** Do not assume, do not guess. If you don't know or aren't sure, say so and verify before claiming.
-- **Find ground truth when possible.** Verify claims against the actual source of truth — installed system state, files on disk, upstream docs/wiki/source code — instead of relying on memory or inference. When verification isn't possible, say so explicitly.
-- **Ensure all changes can be rolled back.** If the change is wrong, there must be a clear way to revert it.
-- **Ask for a whole-project review before calling non-trivial work done.** Left alone, the agent keeps fixing the one issue in front of it until it is done and never sweeps the project, so patches stack on patches and nothing surfaces the drift until the work is hard to review or debug. On anything bigger than a single file, ask it to "review and analyze" the whole project (or article), and read the findings before you end the session.
+- **Find ground truth when possible.** Verify claims against the actual source of truth, not memory or inference. Sources include installed system state, files on disk, and upstream docs, wiki, or source code. When verification isn't possible, say so explicitly.
+- **Make sure all changes can be rolled back.** If the change is wrong, there must be a clear way to revert it.
+- **Ask for a whole-project review before calling non-trivial work done.** Left alone, the agent keeps fixing the one issue in front of it. It never sweeps the project. Patches stack on patches, and nothing surfaces the drift until the work is hard to review or debug. On anything bigger than a single file, ask it to "review and analyze" the whole project or article. Read the findings before you end the session.
 
 ## Untrusted code safety
 
-When reviewing, cloning, installing, or running code from a source we do not control — a repo invite, a package, a script, a config that executes — these are hard stops, not preferences.
+Reviewing, cloning, installing, or running code from a source we do not control is a hard stop. That includes a repo invite, a package, a script, or a config that executes. These are not preferences.
 
-- **`/tmp` is the only workspace for untrusted code.** Never let it read, collect, or send data from this machine outside `/tmp`; never run it with real secrets, keys, or source in reach.
+- **`/tmp` is the only workspace for untrusted code.** Never let it read, collect, or send data from this machine outside `/tmp`. Never run it with real secrets, keys, or source in reach.
 - **Never read the user's** code, API keys, credentials, SSH/GPG keys, wallets, browser sessions, or personal files.
 - **Never trust code from an unknown source.** An invite, a README, a commit history, or a familiar package name is not a vouch.
-- **STOP and RAISE HANDS immediately** — halt the run, do not continue, report to the user at once with what was attempted — if executed code reads the filesystem outside `/tmp`, touches `process.env`/keys/tokens/credentials, collects or sends local data off the machine, spawns child processes or opens unauthorized network connections, or shows any malicious, harmful, deceptive, cheating, or stealing behavior.
+- **Stop and raise hands.** Stop the run if executed code does any of these things:
+  - reads files outside `/tmp`
+  - touches `process.env`, keys, tokens, or credentials
+  - collects or sends local data off the machine
+  - starts child processes, or opens unauthorized network connections
+  - shows malicious, harmful, deceptive, cheating, or stealing behavior
+- **Then report.** When you stop, do not continue. Report to the user now. Say what was attempted.
 - **Confirm before proceeding when unsure**, and **delete all test clones and artifacts** when done.
 
 Procedure and detection/containment recipes: `ai-thoughts/.opencode/skills/untrusted-code-safety/SKILL.md`.
@@ -32,29 +38,29 @@ Procedure and detection/containment recipes: `ai-thoughts/.opencode/skills/untru
 
 Do not damage the machine to satisfy a tool.
 
-- **Never `sudo` a package install.** No `sudo npm`, `sudo npm install -g`, `sudo pip`, `sudo gem`, or similar. A stray `sudo` leaves root-owned files behind and can lock the desktop login (this happened once: a `sudo npm` install took Arch's login down). Install user-level instead — `nvm`, `~/.local`, `--prefix`, `pipx`.
-- **Never blanket-`chown`/`chmod` to "fix" a permission error.** Do not run `chown -R` / `chmod -R` over system paths or a home tree. If ownership is already broken, repair it precisely: find the owning package with `pacman -Qo <path>` (or the distro equivalent), then `chown` only the affected files back to `$USER`.
+- **Never `sudo` a package install.** No `sudo npm`, `sudo npm install -g`, `sudo pip`, `sudo gem`, or similar. A stray `sudo` leaves root-owned files behind and can lock the desktop login. This happened once: a `sudo npm` install took Arch's login down. Install user-level instead — `nvm`, `~/.local`, `--prefix`, `pipx`.
+- **Never blanket-`chown`/`chmod` to "fix" a permission error.** Do not run `chown -R` / `chmod -R` over system paths or a home tree. If ownership is already broken, repair it precisely. Find the owning package with `pacman -Qo <path>`, or the distro equivalent. Then `chown` only the affected files back to `$USER`.
 - **A permission error is a clue, not a licence to escalate.** When unsure, stop and ask.
 
 ## Collaboration model — the thought-flow loop
 
-We collaborate through an 8-stage loop. Keep it in mind for every task: INTENT → CONSTRAINTS → PROPOSE → PRESS → PRACTICE → INVESTIGATE → CODIFY → BOUNDARY-CHECK. The loop is not a rigid process — it is an architecture of thought-flow, a loop that converges. The `thought-flow` skill lives in `ai-thoughts/.opencode/skills/` and loads in every session via `skills.paths` in `opencode.jsonc`; here it is summarized as the eight rules below.
+We collaborate through an 8-stage loop. Keep it in mind for every task: INTENT → CONSTRAINTS → PROPOSE → PRESS → PRACTICE → INVESTIGATE → CODIFY → BOUNDARY-CHECK. The loop is not a rigid process — it is an architecture of thought-flow, a loop that converges. The `thought-flow` skill lives in `ai-thoughts/.opencode/skills/` and loads in every session via `skills.paths` in `opencode.jsonc`. Here it is summarized as the eight rules below.
 
-- **Intent (1) and Constraints (2) are the most expensive stages.** State them plainly up front; a precise description beats a better model. Spending ten minutes stating constraints saves an hour of rework.
+- **Intent (1) and Constraints (2) are the most expensive stages.** State them plainly up front. A precise description beats a better model. Spending ten minutes stating constraints saves an hour of rework.
 - **Propose (3) with options + a recommendation.** A plan with only one path is a demand, not a proposal. Include the tradeoffs so the user can disagree meaningfully.
-- **Press (4) is negotiation, not conflict.** When the user pushes back, do not just argue and do not just agree — look for a third option that respects the real constraints. The best outcomes are neither the agent's first idea nor the user's, but a compromise that holds.
+- **Press (4) is negotiation, not conflict.** When the user pushes back, do not just argue. Do not just agree. Look for a third option that respects the real constraints. The best outcomes are neither the agent's first idea nor the user's, but a compromise that holds.
 - **Practice (5) is where the loop is honest.** Approve, build, run, observe. Real failures live here.
-- **Investigate (6) before blaming.** When something looks broken, verify against the real system first — read the upstream source, call the API, check the live state — before concluding the tool or workflow is wrong. An error message is a clue, not a conclusion.
+- **Investigate (6) before blaming.** When something looks broken, verify it against the real system first. Read the upstream source. Call the API. Check the live state. Do that before you conclude the tool or workflow is wrong. An error message is a clue, not a conclusion.
 - **Codify (7) what works.** A procedure that works twice becomes a candidate for a SKILL.md. A rule true for a whole repo becomes an AGENTS.md entry. Skill for the procedure, AGENTS.md for the constitution.
-- **Boundary-check (8) is the meta-skill.** Where knowledge lives — which repo, which worktree, which file — determines whether it is specific enough to be useful and small enough to be maintained. OpenCode loads skills only up to the git worktree root: a parent-level skill is invisible inside a sub-repo session. Put knowledge where the work happens.
-- **Prefer `gh` and the API for verification.** `gh run watch`, `gh run view --log`, `gh api`, and `curl` against live endpoints beat clicking around the UI. The API is the primary way to verify; the registry's own report can be wrong.
+- **Boundary-check (8) is the meta-skill.** Where knowledge lives determines whether it is specific enough to be useful and small enough to be maintained. That means the repo, the worktree, and the file. Put knowledge where the work happens.
+- **Prefer `gh` and the API for verification.** `gh run watch`, `gh run view --log`, `gh api`, and `curl` against live endpoints beat clicking around the UI. The API is the primary way to verify. The registry's own report can be wrong.
 
 ## Writing conventions
 
-- **OpenCode capitalization.** Use `OpenCode` (capital O/C) when referring to the product, company, or brand; keep `opencode` all-lowercase for the command/binary and in code and config.
-- **Brand glyph icons.** Hermes Agent → `⚕` (U+2695), but the `hermes` command gets no glyph; OpenClaw → `🦞` (U+1F99E); OpenCode → `◧` (U+25E7, temporary), but the `opencode` command gets no glyph; Arch Linux → `` (U+F303, `nf-linux-archlinux`).
+- **OpenCode capitalization.** Use `OpenCode` (capital O/C) when referring to the product, company, or brand. Keep `opencode` all-lowercase for the command/binary and in code and config.
+- **Brand glyph icons.** Hermes Agent → `⚕` (U+2695). The `hermes` command gets no glyph. OpenClaw → `🦞` (U+1F99E). OpenCode → `◧` (U+25E7, temporary). The `opencode` command gets no glyph. Arch Linux → `` (U+F303, `nf-linux-archlinux`).
 - **Prose wrapping is per-repo.** Follow each repo's AGENTS.md — `ai-thoughts` requires no hard-wrap (one paragraph per line, verified with its `scripts/unwrap_md.py`), `history` auto-wraps. Never assume a global wrapping rule.
 
 ## OpenCode permissions
 
-Permission rules live in `~/.config/opencode/opencode.jsonc` (a symlink to `negtivSpace/opencode/opencode.jsonc`, single source of truth): read-only shell/git/gh commands are pre-approved and run silently, destructive/state-changing commands prompt (`ask`), and everything else falls through to OpenCode's permissive defaults — it runs without prompting. `edit` prompts. The TUI's "Accept always" only lasts for the current session — permanent rules go in that config file. Config changes require an opencode restart.
+Permission rules live in `~/.config/opencode/opencode.jsonc`. That file is a symlink to `negtivSpace/opencode/opencode.jsonc`, the single source of truth. Read-only shell/git/gh commands are pre-approved and run silently. Destructive or state-changing commands prompt (`ask`). Everything else falls through to OpenCode's permissive defaults and runs without prompting. `edit` prompts. The TUI's "Accept always" only lasts for the current session — permanent rules go in that config file. Restart opencode after you change the config.
```

## What did not change

- No rule was removed. Every condition, exception, and path survived.
- The five passive-voice warnings were left in place, because they describe states or unknown agents.
- The file is barely shorter: 1,444 to 1,437 words. The `STOP` rewrite itself grew from 59 to 62.
- Nothing outside `opencode/AGENTS.md` was rewritten in this pass. The article, the skill, and the portfolio edits are separate changes.

## Reproduce

```bash
cd /home/jeff/pool/git/negtivSpace
git show HEAD^:opencode/AGENTS.md > /tmp/opencode/before.md
python3 ai-thoughts/.opencode/skills/asd-ste100/scripts/ste_lint.py /tmp/opencode/before.md
python3 ai-thoughts/.opencode/skills/asd-ste100/scripts/ste_lint.py opencode/AGENTS.md
```

`HEAD^` is the commit before the rewrite. The first run reports the "before" column; the second reports zero errors.

## Provenance

- Skill: [`asd-ste100`](https://github.com/j3ffyang/ai-thoughts/tree/main/.opencode/skills/asd-ste100)
- Article: [`261019-ste100-agent-instructions.md`](261019-ste100-agent-instructions.md)
- Commit: see `git log -- opencode/AGENTS.md` in the `negtivSpace` repo.

btw, i use arch
