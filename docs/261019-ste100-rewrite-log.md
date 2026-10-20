# ASD-STE100 rewrite log — two rule files

**Status:** working record, 2026-10-19. This is not an article.

**Scope:** `opencode/AGENTS.md` and `ai-thoughts/AGENTS.md`, one pass each, measured before and after with the [`asd-ste100`](https://github.com/j3ffyang/ai-thoughts/tree/main/.opencode/skills/asd-ste100) skill.

## Why keep this

The article argues that the STE rules make agent instructions checkable. This file is the evidence: the actual changes to the two rule files, with the diffs, the measurements, and the decisions.

## Result

### `opencode/AGENTS.md`

| Measure | Before | After |
|---|---:|---:|
| Sentences | 98 | 147 |
| Over 20 words | 21 (21%) | **0** |
| Over 25 words | 11 | **0** |
| Semicolons | 7 | **0** |
| Linter errors | 18 | **0** |
| Linter warnings | 18 | 5 |
| Words | 1,444 | 1,437 |

### `ai-thoughts/AGENTS.md`

| Measure | Before | After |
|---|---:|---:|
| Sentences | 77 | 116 |
| Over 20 words | 17 (22%) | **0** |
| Over 25 words | 6 | **0** |
| Semicolons | 9 | **0** |
| Linter errors | 15 | **0** |
| Linter warnings | 25 | 14 |
| Words | 1,307 | 1,312 |

The remaining 19 warnings across both files are passive voice in descriptions: "being edited", "be rolled back", "was attempted", "is summarized", "be maintained", and similar. Rule 3.6 permits passive in descriptions when the agent is unknown, so they stay.

Both files ended close to their original length: `opencode` lost 7 words, `ai-thoughts` gained 5. The `STOP` rewrite itself grew from 59 to 62 words. Splitting usually adds words; here other trims offset it. STE trades brevity for checkability, not the other way around.

## Method

Run from the `ai-thoughts` repo root:

```bash
python3 .opencode/skills/asd-ste100/scripts/ste_lint.py --stats ../opencode/AGENTS.md AGENTS.md
```

`--stats` prints one row per file: sentences, over 20 words, over 25 words, semicolons, errors, and warnings. These rows were re-measured against the committed pre-state (`b229c82^` for `opencode/AGENTS.md`, `8dc597d^` for `ai-thoughts/AGENTS.md`). An earlier run reported 94 sentences, 12 over 25 words, 19 errors, and 17 warnings for `opencode/AGENTS.md`; those figures do not reproduce from the committed files, so the table above replaces them.

The linter strips bold markers, excludes code fences, headings, and table rows, counts a code span as one word, and reports sentences over 25 words as errors, over 20 as warnings, plus semicolons and non-approved words.

## Patterns applied

1. **Condition first.** The `STOP and RAISE HANDS` rule put three commands before a ten-item trigger; the trigger now comes first, as a list.
2. **One action per sentence.** Commit/push, whole-project review, investigate, and press each became two or three sentences.
3. **Semicolons split.** Seven in `opencode` and nine in `ai-thoughts` became sentence breaks: retry paths, skill loading, intent, verification, glyphs, permissions, naming, and the registry caveat.
4. **Bracketed asides promoted to sentences.** Parentheticals about the account type, the source of truth, and the login incident are now their own sentences.
5. **Non-approved words replaced.** `Ensure` became `Make sure`; `require an opencode restart` became `Restart opencode after you change the config`.
6. **A false mechanism removed.** The Boundary-check bullet claimed skills load only up to the worktree root, which the corrected line and `opencode.jsonc` contradict. The lesson stays; the wrong mechanism is gone.

## The actual diff

### `opencode/AGENTS.md`

````diff
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
````

### `ai-thoughts/AGENTS.md`

````diff
diff --git a/AGENTS.md b/AGENTS.md
index a7473e8..96456dd 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -2,46 +2,46 @@
 
 ## Project
 
-Personal repository of AI/tech articles and bilingual (Chinese / English) essays — including OpenClaw/Hermes notes, history, culture, and second-brain write-ups — with a YAML-driven README index.
+Personal repository of AI/tech articles and bilingual (Chinese / English) essays. Topics include OpenClaw/Hermes notes, history, culture, and second-brain write-ups. A YAML-driven README index lists them.
 
 ## Working rules
 
-The universal working rules (approval before changes, commit only when asked, honesty, ground truth, rollback, brand conventions) are defined in the global `~/.config/opencode/AGENTS.md` and apply here too. This file adds only what is specific to this repo.
+The universal working rules are defined in the global `~/.config/opencode/AGENTS.md` and apply here too. They cover approval, commits, honesty, ground truth, rollback, and brand conventions. This file adds only what is specific to this repo.
 
-- **Rollback defaults.** Git-tracked files → `git restore` / `git revert`; generated output (`README.md`, `README_zh.md`, `PORTFOLIO.md`) → regenerate from its source of truth (`articles.yaml` / the portfolio template).
+- **Rollback defaults.** Git-tracked files → `git restore` / `git revert`. Generated output (`README.md`, `README_zh.md`, `PORTFOLIO.md`) → regenerate from its source of truth (`articles.yaml` / the portfolio template).
 
 ## Host safety (whole machine, not just this repo)
 
 Do not damage the machine to satisfy a tool.
 
-- **Never `sudo` a package install.** No `sudo npm`, `sudo npm install -g`, `sudo pip`, `sudo gem`, or similar. A stray `sudo` leaves root-owned files behind and can lock the desktop login (this happened once: a `sudo npm` install took Arch's login down). Install user-level instead — `nvm`, `~/.local`, `--prefix`, `pipx`.
-- **Never blanket-`chown`/`chmod` to "fix" a permission error.** Do not run `chown -R` / `chmod -R` over system paths or a home tree. If ownership is already broken, repair it precisely: find the owning package with `pacman -Qo <path>` (or the distro equivalent), then `chown` only the affected files back to `$USER`.
+- **Never `sudo` a package install.** No `sudo npm`, `sudo npm install -g`, `sudo pip`, `sudo gem`, or similar. A stray `sudo` leaves root-owned files behind and can lock the desktop login. This happened once: a `sudo npm` install took Arch's login down. Install user-level instead — `nvm`, `~/.local`, `--prefix`, `pipx`.
+- **Never blanket-`chown`/`chmod` to "fix" a permission error.** Do not run `chown -R` / `chmod -R` over system paths or a home tree. If ownership is already broken, repair it precisely. Find the owning package with `pacman -Qo <path>`, or the distro equivalent. Then `chown` only the affected files back to `$USER`.
 - **A permission error is a clue, not a licence to escalate.** When unsure, stop and ask.
 
 ## Writing conventions
 
 - **No hard-wrap.** Avoid hard-wrap at all, including `docs/`, `.opencode/skills/`, and agents — prose is one paragraph per line. Verify with `python scripts/unwrap_md.py --check`, or run `python scripts/unwrap_md.py` to unwrap.
 - **Chinese files are translations of the English original.** Every Chinese markdown file is translated from, and identical in content to, its English counterpart — only the language differs. Don't search the Chinese file as a reference, unless otherwise specified.
-- **Arch sign-off.** Every article in `docs/` ends with the line `btw, i use arch` as its final paragraph, unless the user explicitly says otherwise. It stays verbatim English in both EN and ZH versions; don't duplicate it if already present, and never add it to READMEs or `articles.yaml`. See the `arch-sign-off` skill for the exact command.
-- **Box diagrams.** A fenced code block that draws a box (`┌ ┐ └ ┘ │ ─`) must be square: every content row's walls line up with the corners, and arrow connectors line up with the `┬` marks. Never hand-count a box — generate it programmatically, then verify with `python scripts/verify_md_boxes.py <file>` (add `--check` for CI). Blocks with genuinely nested / mixed-width boxes are out of scope for the check.
+- **Arch sign-off.** Every article in `docs/` ends with the line `btw, i use arch` as its final paragraph, unless the user explicitly says otherwise. It stays verbatim English in both EN and ZH versions. Do not duplicate it if already present, and never add it to READMEs or `articles.yaml`. See the `arch-sign-off` skill for the exact command.
+- **Box diagrams.** A fenced code block that draws a box (`┌ ┐ └ ┘ │ ─`) must be square. Every content row's walls line up with the corners. Arrow connectors line up with the `┬` marks. Never hand-count a box — generate it programmatically, then verify with `python scripts/verify_md_boxes.py <file>` (add `--check` for CI). Blocks with genuinely nested / mixed-width boxes are out of scope for the check.
 
 ## Filename conventions
 
-Every file in `docs/` and `imgs/` follows a `YYMMDD-slug` pattern: a 6-digit date (`YYMMDD`, no `HHMM`, no `YYYY-MM-DD`), a hyphen, then a lowercase slug. No spaces.
+Every file in `docs/` and `imgs/` follows a `YYMMDD-slug` pattern. The date is 6 digits (`YYMMDD`, no `HHMM`, no `YYYY-MM-DD`). A hyphen follows, then a lowercase slug. No spaces.
 
 - **Articles** — `docs/<YYMMDD>-<slug>.md`, e.g. `260313-openclaw-thoughts.md`.
-- **Chinese translations** — Simplified: `docs/<YYMMDD>-<slug>-zh-hans.md`; its Traditional twin (generated by the `simplified-to-traditional` skill): `docs/<YYMMDD>-<slug>-zh-hant.md`. The legacy `-chn.md` suffix predates this rule — existing files keep it until the user explicitly migrates them, but new translations always use `-zh-hans.md`.
-- **Images** — `imgs/<YYMMDD>-<slug>.<ext>`, e.g. `260313-main.png`; images for an article share the article's `YYMMDD` prefix.
+- **Chinese translations** — Simplified: `docs/<YYMMDD>-<slug>-zh-hans.md`. Its Traditional twin, generated by the `simplified-to-traditional` skill: `docs/<YYMMDD>-<slug>-zh-hant.md`. The legacy `-chn.md` suffix predates this rule. Existing files keep it until the user explicitly migrates them. New translations always use `-zh-hans.md`.
+- **Images** — `imgs/<YYMMDD>-<slug>.<ext>`, e.g. `260313-main.png`. Images for an article share the article's `YYMMDD` prefix.
 - **Screenshots / captures with no meaningful name** — keep the capture time as the slug, e.g. `260506-180248.png` (from `2026-05-06-180248_hyprshot.png`).
 - **Renaming** — when a file is renamed, update every `../imgs/<file>` and doc link that referenced the old name.
 
 ## Image housekeeping
 
-`imgs/` holds assets that are not always referenced from a file in this repo — treat "unreferenced" as a question, never a delete signal on its own.
+`imgs/` holds assets that a file in this repo does not always reference. Treat "unreferenced" as a question, never as a delete signal.
 
-- **Social banner assets are consumed outside the repo.** Files like `imgs/*-banner-twitter.png` (and `*-xbanner`, `*-1500x600`, `*-5x2`) are generated by the `resize-for-banner` skill and uploaded manually (e.g. to twitter.com) when publishing an article. Nothing in the repo links them, so a reference-based "unreferenced images" sweep must **never** flag them as deletable.
-- **Auto-generated backups are disposable.** `imgs/*-backup-*` and `infographic/**/*-backup-*` are byproducts of regenerating an asset; they are gitignored and can be deleted freely.
-- **Before deleting any image, confirm it is genuinely unused** — check in-repo references *and* account for externally-consumed assets like the banners above.
+- **Social banner assets are consumed outside the repo.** Files like `imgs/*-banner-twitter.png` (and `*-xbanner`, `*-1500x600`, `*-5x2`) come from the `resize-for-banner` skill. They are uploaded manually, e.g. to twitter.com, when publishing an article. Nothing in the repo links them, so a reference-based "unreferenced images" sweep must **never** flag them as deletable.
+- **Auto-generated backups are disposable.** `imgs/*-backup-*` and `infographic/**/*-backup-*` are byproducts of regenerating an asset. They are gitignored and can be deleted freely.
+- **Before deleting any image, confirm it is genuinely unused.** Check in-repo references, and account for externally consumed assets like the banners above.
 
 ## README index workflow
 
@@ -52,26 +52,26 @@ python scripts/gen_readmes.py              # regenerate both READMEs
 python scripts/gen_readmes.py --check      # CI/verification: exit 1 if a README is stale
 ```
 
-**Ordering is automatic — don't hand-order.** Article sections are sorted by their newest post (most recently updated first), rows are newest-first within each section, and drafts are pinned last. The `Published Skills on ClawHub` block is derived from `.opencode/skills/*/SKILL.md` frontmatter (no `articles.yaml` entry is needed for a skill) and sits between the articles and the drafts section. Section order drifting over time is intended — it's how the most active topics stay on top.
+**Ordering is automatic — don't hand-order.** The generator sorts article sections by their newest post, most recently updated first. Rows are newest-first within each section. Drafts are pinned last. The `Published Skills on ClawHub` block comes from `.opencode/skills/*/SKILL.md` frontmatter. No `articles.yaml` entry is needed for a skill. That block sits between the articles and the drafts section. Section order drifting over time is intended — it's how the most active topics stay on top.
 
 To add or update an article:
 
 1. Drop the file into `docs/` (follow the rules in "Filename conventions").
 2. Add/update a row in `articles.yaml`:
-   - English article → link with `lang: en` (+ `desc_en`; no `desc_zh` until a `-zh-hans.md` — or a legacy `-chn.md` — exists)
+   - English article → link with `lang: en` (+ `desc_en`). Do not add `desc_zh` until a `-zh-hans.md`, or a legacy `-chn.md`, exists.
    - Chinese article → link with `lang: zh` (+ `desc_zh`)
-   - Draft/working note → set `section: drafts` (lands in the Drafts & Working Notes section). Keep `status: draft` too — `status` is metadata only (`draft` or `published`) and never affects placement; the generator routes rows by `section`.
+   - Draft/working note → set `section: drafts` (lands in the Drafts & Working Notes section). Keep `status: draft` too. `status` is metadata only (`draft` or `published`) and never affects placement. The generator routes rows by `section`.
    - Optional `label_zh` on a link gives the Chinese display name in `README_zh.md` (Chinese articles usually get one).
 3. Run the generator, confirm the diff shows only the intended row, and commit `articles.yaml` + both regenerated READMEs together.
 
 **Note:** `gen_readmes.py` prints a warning for every `docs/*.md` not listed in `articles.yaml` (e.g. unregistered drafts). That's expected until the row is added — it's a reminder, not an error.
 
-The generator also **fails hard** on invalid manifests: unknown `section`, missing `desc_zh` on any row where the English article's `-zh-hans.md` counterpart exists in `docs/` (or a legacy `-chn.md` counterpart, or the row carries a `lang: zh` link), missing `desc_en` on any row with a `lang: en` link, or a `path` that points to a missing file. Fix those before committing. An EN-only row (no Chinese counterpart yet) may omit `desc_zh` — `README_zh.md` then falls back to its `desc_en`. The trigger for adding `desc_zh` is the `-zh-hans.md` (or legacy `-chn.md`) file existing in the same folder; add `desc_zh` together with that Chinese version.
+The generator also **fails hard** on invalid manifests. It rejects an unknown `section`. It rejects a missing `desc_zh` when the English article has a `-zh-hans.md` or legacy `-chn.md` counterpart. It also rejects a `lang: zh` link without `desc_zh`. It rejects a missing `desc_en` on any row with a `lang: en` link. It rejects a `path` that points to a missing file. Fix those before you commit. An EN-only row may omit `desc_zh`, and `README_zh.md` then falls back to `desc_en`. Add `desc_zh` only when the `-zh-hans.md`, or legacy `-chn.md`, file exists in the same folder.
 
 ### EN / ZH routing rule
 
 - `README.md` keeps a row only if it has at least one `lang: en` link, and renders just those English links.
-- `README_zh.md` shows **all** rows (EN + ZH) with Chinese descriptions; Chinese display labels come from `label_zh` where set, English slugs otherwise.
+- `README_zh.md` shows **all** rows (EN + ZH) with Chinese descriptions. Chinese display labels come from `label_zh` where set, and English slugs otherwise.
 
 ## PORTFOLIO.md workflow
 
@@ -82,9 +82,9 @@ python scripts/gen_portfolio.py              # regenerate PORTFOLIO.md
 python scripts/gen_portfolio.py --check      # CI/verification: exit 1 if stale
 ```
 
-Filled automatically: article count (unique published articles by YYMMDD from `articles.yaml`), the ai-thoughts repo row's latest commit, the "Latest Articles" list (top N published articles by date, deduped by YYMMDD), and the "Last Updated" date. Editorial content (the Activity Timeline, repo tables, tech stack, etc.) lives in the template — edit the template, then regenerate.
+The generator fills four things automatically. It fills the article count, which is the unique published articles by YYMMDD from `articles.yaml`. It fills the ai-thoughts repo row's latest commit. It fills the "Latest Articles" list: the top N published articles by date, deduped by YYMMDD. It fills the "Last Updated" date. Editorial content (the Activity Timeline, repo tables, tech stack, etc.) lives in the template — edit the template, then regenerate.
 
 ## Repo conventions
 
 - Docs-only repository: no build or test pipeline. Scripts are utilities, and several expose `--check` for CI (`gen_readmes.py`, `gen_portfolio.py`, `unwrap_md.py`, `verify_md_boxes.py`). Skills ship their own scripts too.
-- Two remotes on `main`: `negtivspace` and `j3ffyang` — push to both. `negtivspace` is a **normal GitHub user account** (a second personal account, "Negative Space 留白"), **not** an org. Editing `negtivspace/ai-thoughts` via `gh`/API (e.g. setting the About description/homepage) requires the `negtivspace` account's own token — the `j3ffyang` token gets 404 on that account's repos.
+- Two remotes on `main`: `negtivspace` and `j3ffyang` — push to both. `negtivspace` is a **normal GitHub user account** (a second personal account, "Negative Space 留白"), **not** an org. Editing `negtivspace/ai-thoughts` via `gh`/API requires the `negtivspace` account's own token. This includes setting the About description or homepage. The `j3ffyang` token gets 404 on that account's repos.
````

## What did not change

- No rule was removed. Every condition, exception, and path survived in both files.
- The passive-voice warnings were left in place: 5 in `opencode`, 14 in `ai-thoughts`. They describe states or unknown agents.
- Both files are within 12 words of their original length. The `STOP` rewrite itself grew from 59 to 62.
- Nothing outside the two rule files was rewritten in this pass. The article, the skill, and the portfolio edits are separate changes.

## Reproduce

```bash
cd /home/jeff/pool/git/negtivSpace
git show HEAD^:opencode/AGENTS.md > /tmp/opencode/before-global.md
git -C ai-thoughts show HEAD^:AGENTS.md > /tmp/opencode/before-ai.md
python3 ai-thoughts/.opencode/skills/asd-ste100/scripts/ste_lint.py /tmp/opencode/before-global.md
python3 ai-thoughts/.opencode/skills/asd-ste100/scripts/ste_lint.py /tmp/opencode/before-ai.md
python3 ai-thoughts/.opencode/skills/asd-ste100/scripts/ste_lint.py opencode/AGENTS.md
python3 ai-thoughts/.opencode/skills/asd-ste100/scripts/ste_lint.py ai-thoughts/AGENTS.md
```

`HEAD^` is the commit before each rewrite. The first two runs report the "before" columns; the last two report zero errors.

## Provenance

- Skill: [`asd-ste100`](https://github.com/j3ffyang/ai-thoughts/tree/main/.opencode/skills/asd-ste100)
- Article: [`261019-ste100-agent-instructions.md`](261019-ste100-agent-instructions.md)
- Commits: `git log -- opencode/AGENTS.md` in `negtivSpace`, and `git log -- AGENTS.md` in `ai-thoughts`.

btw, i use arch
