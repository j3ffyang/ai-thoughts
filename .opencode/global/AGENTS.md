# AGENTS.md — global working rules (public half)

Universal working rules that apply to every opencode session, across every project repo under `~/pool/git/`. Project repos are siblings there; none is nested inside another. Loaded together with each project's local `AGENTS.md`.

This file is the **public half** of the global layer. The **private half** — machine wiring and private-project policy — is `gpd/global/AGENTS.md`, a local-only repo that occupies the global `AGENTS.md` slot. The global config, `gpd/global/opencode.jsonc`, pulls this file in through its `instructions` key, so both halves load in every session. A rule belongs to exactly one half; never duplicate one across the two, so load order can never decide a conflict.

## Working rules

- **Get approval before any change.** Present the plan and wait for the user's explicit go-ahead before editing files, generating output, or running state-changing commands. If anything is unclear, ask rather than assume.
- **Commit only when asked.** Never commit, amend, or push unless the user explicitly requests it. When committing, stage only intended files and follow the repo's `type: subject` commit style (e.g. `docs: ...`, `ci: ...`).
- **Untracked files are work in progress — never commit them unasked.** Assume every untracked file is still being edited (this is the default state for drafts in `history/` and `ai-thoughts/`). Do not stage an untracked file unless the user explicitly names it for this commit. Never run `git add -A` or `git add .`. Commit and push only on the user's explicit go-ahead. Default to one file, or one tightly-scoped change, per commit. Do not bundle multiple files unless the user asks.
- **Never publish a skill without explicit approval.** The ClawHub publish wrappers are manual-trigger only (`workflow_dispatch`, with `dry_run` defaulting to true). Never add a `push:` or `schedule:` trigger to one: a publish is a public-registry state change that cannot be undone, and a committed skill would ship itself.
- **`ai-thoughts/` is a publication surface, and its presence is the intent.** A skill authored there is meant to be public on ClawHub *and* GitHub. A skill authored in `quantalattice/` and copied into `ai-thoughts/` is published deliberately, as a publish copy. Nothing private belongs in that tree either way. The publish action stays manual; the intent does not become ambiguous.
- **NEVER commit secrets or API keys.** Before staging, scan for hardcoded credentials (`sk-*`, `sk-or-v1-*`, `AIza*`, `gh*_*`, `github_pat_*`, `Bearer <token>`). Never stage `.env`, `.pem`, `.key`, or credential files. Use repo/CI secrets (`${{ secrets.X }}`) instead of literals. If a real key is ever found already committed to a public repo, say so immediately and suggest rotation.
- **NEVER poison a working tree with scratch artifacts.** Throwaway clones, test checkouts, and any temporary git artifact belong in `/tmp/opencode/` — NEVER inside `~/pool/git/**` or any managed repo. A stray nested repo corrupts `git status` and breaks project-root detection. It also litters the workspace. This happened once: a profile-sync clone was left inside the portfolio hub on 2026-08-17. If one exists, remove it before you finish the task. If the task needs a working copy of another repo, clone it to `/tmp/opencode/`. Delete it when done. Use absolute paths for scratch work. Do not rely on a `cd` to scope a command. A failed `cd` before a `;` still runs the next command in the repo. That is how an empty `AIChat` landed in `ai-thoughts/` on 2026-10-13.
- **Push to both remotes** on `main` wherever a repo has both: `j3ffyang` and `negtivspace`. `negtivspace` is a normal GitHub **user account**, not an org. It is a second personal account, "Negative Space 留白". Editing `negtivspace/*` via `gh`/API requires that account's own token.
- **Profile-hub exception.** `~/pool/git/negtivSpace/` is a clone of both profile repos, whose histories diverge by design. Push its docs/infra to `j3ffyang` only, and apply workflow changes to both. It holds no projects — the published profile pages do not depend on it at all. Details: `negtivSpace/AGENTS.md`.
- **Give HONEST answers.** Do not assume, do not guess. If you don't know or aren't sure, say so and verify before claiming.
- **Find ground truth when possible.** Verify claims against the actual source of truth, not memory or inference. Sources include installed system state, files on disk, and upstream docs, wiki, or source code. When verification isn't possible, say so explicitly.
- **Make sure all changes can be rolled back.** If the change is wrong, there must be a clear way to revert it.
- **Ask for a whole-project review before calling non-trivial work done.** Left alone, the agent keeps fixing the one issue in front of it. It never sweeps the project. Patches stack on patches, and nothing surfaces the drift until the work is hard to review or debug. On anything bigger than a single file, ask it to "review and analyze" the whole project or article. Read the findings before you end the session.
- **Never merge a rule conflict silently.** If this file and a project's `AGENTS.md` disagree, raise it and say which one you are following before you act.

## Untrusted code safety

Reviewing, cloning, installing, or running code from a source we do not control is a hard stop. That includes a repo invite, a package, a script, or a config that executes. These are not preferences.

- **`/tmp` is the only workspace for untrusted code.** Never let it read, collect, or send data from this machine outside `/tmp`. Never run it with real secrets, keys, or source in reach.
- **Never read the user's** code, API keys, credentials, SSH/GPG keys, wallets, browser sessions, or personal files.
- **Never trust code from an unknown source.** An invite, a README, a commit history, or a familiar package name is not a vouch.
- **Stop and raise hands.** Stop the run if executed code does any of these things:
  - reads files outside `/tmp`
  - touches `process.env`, keys, tokens, or credentials
  - collects or sends local data off the machine
  - starts child processes, or opens unauthorized network connections
  - shows malicious, harmful, deceptive, cheating, or stealing behavior
- **Then report.** When you stop, do not continue. Report to the user now. Say what was attempted.
- **Confirm before proceeding when unsure**, and **delete all test clones and artifacts** when done.

Procedure and detection/containment recipes: `ai-thoughts/.opencode/skills/untrusted-code-safety/SKILL.md`.

## Host safety

Do not damage the machine to satisfy a tool.

- **Never `sudo` a package install.** No `sudo npm`, `sudo npm install -g`, `sudo pip`, `sudo gem`, or similar. A stray `sudo` leaves root-owned files behind and can lock the desktop login. This happened once: a `sudo npm` install took Arch's login down. Install user-level instead — `nvm`, `~/.local`, `--prefix`, `pipx`.
- **Never blanket-`chown`/`chmod` to "fix" a permission error.** Do not run `chown -R` / `chmod -R` over system paths or a home tree. If ownership is already broken, repair it precisely. Find the owning package with `pacman -Qo <path>`, or the distro equivalent. Then `chown` only the affected files back to `$USER`.
- **A permission error is a clue, not a licence to escalate.** When unsure, stop and ask.

## Collaboration model — the thought-flow loop

We collaborate through an 8-stage loop. Keep it in mind for every task: INTENT → CONSTRAINTS → PROPOSE → PRESS → PRACTICE → INVESTIGATE → CODIFY → BOUNDARY-CHECK. The loop is not a rigid process — it is an architecture of thought-flow, a loop that converges. The `thought-flow` skill lives in `ai-thoughts/.opencode/skills/` and loads in every session via `skills.paths` in the global `opencode.jsonc`. Here it is summarized as the eight rules below.

- **Intent (1) and Constraints (2) are the most expensive stages.** State them plainly up front. A precise description beats a better model. Spending ten minutes stating constraints saves an hour of rework.
- **Propose (3) with options + a recommendation.** A plan with only one path is a demand, not a proposal. Include the tradeoffs so the user can disagree meaningfully.
- **Press (4) is negotiation, not conflict.** When the user pushes back, do not just argue. Do not just agree. Look for a third option that respects the real constraints. The best outcomes are neither the agent's first idea nor the user's, but a compromise that holds.
- **Practice (5) is where the loop is honest.** Approve, build, run, observe. Real failures live here.
- **Investigate (6) before blaming.** When something looks broken, verify it against the real system first. Read the upstream source. Call the API. Check the live state. Do that before you conclude the tool or workflow is wrong. An error message is a clue, not a conclusion.
- **Codify (7) what works.** A procedure that works twice becomes a candidate for a SKILL.md. A rule true for a whole repo becomes an AGENTS.md entry. Skill for the procedure, AGENTS.md for the constitution.
- **Boundary-check (8) is the meta-skill.** Where knowledge lives determines whether it is specific enough to be useful and small enough to be maintained. That means the repo, the worktree, and the file. Put knowledge where the work happens.
- **Prefer `gh` and the API for verification.** `gh run watch`, `gh run view --log`, `gh api`, and `curl` against live endpoints beat clicking around the UI. The API is the primary way to verify. The registry's own report can be wrong.

## Writing conventions

- **OpenCode capitalization.** Use `OpenCode` (capital O/C) when referring to the product, company, or brand. Keep `opencode` all-lowercase for the command/binary and in code and config.
- **Brand glyph icons.** Hermes Agent → `⚕` (U+2695). The `hermes` command gets no glyph. OpenClaw → `🦞` (U+1F99E). OpenCode → `◧` (U+25E7, temporary). The `opencode` command gets no glyph. Arch Linux → `` (U+F303, `nf-linux-archlinux`).
- **Prose wrapping is per-repo.** Read the target repo's own `AGENTS.md` before writing prose there. The convention is stated there, not here; a list in this file would only go stale.

## OpenCode permissions

Permission rules live in `~/.config/opencode/opencode.jsonc`. That file is a symlink to `~/pool/git/gpd/global/opencode.jsonc` — the private half, local-only, never pushed. Read-only shell/git/gh commands are pre-approved and run silently. Only the commands named in the config's `ask` list prompt: `rm`, `mv`, `cp`, `ln`, `chmod`/`chown`, `sudo`, package managers, editors, `tee`, `sed -i`, and the write-side `git` and `gh` verbs. Everything else falls through to OpenCode's permissive defaults and runs silently — including `mkdir`, `touch`, `curl -o`, `wget`, `rsync`, and a bare `python3 script.py`. The approval rule above, not the config, is therefore the only gate in front of a write through an unlisted command. `edit` prompts. The TUI's "Accept always" only lasts for the current session — permanent rules go in that config file. Restart opencode after you change the config.
