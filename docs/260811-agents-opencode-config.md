# OpenCode AGENTS.md + opencode.jsonc — architecture, precedence and workflow

A summary of how this machine's OpenCode is configured, how the pieces load, and how the precedence rules actually work. Facts were verified against the opencode source tree (anomalyco/opencode) and the official docs on 2026-08-11, not from memory.

## Overview: two configuration surfaces

OpenCode is configured by two complementary surfaces. AGENTS.md files feed Markdown instructions straight into the model's context; opencode.json / opencode.jsonc files hold machine-parsed settings (permissions, agents, providers, plugins). Instructions shape how the agent judges; the config gates what it may do. Neither can fully replace the other — put rules about behavior in AGENTS.md, rules about tool access in the config.

The config files support JSONC (comments and trailing commas) everywhere, and either filename is accepted in every location.

## File inventory (as of 2026-08-11)

- `~/.config/opencode/opencode.jsonc` — global config, a symlink to `negtivSpace/opencode/opencode.jsonc` (committed in that repo, so versioned). This is the single source of truth for permission rules.
- `~/.config/opencode/AGENTS.md` — global rules; a symlink to `negtivSpace/opencode/AGENTS.md` (git-managed, same pattern as the config), loaded in every session.
- `<repo>/AGENTS.md` — project rules, versioned, loaded when working in that repo (e.g. `ai-thoughts/AGENTS.md`).
- `<repo>/opencode.json` / `<repo>/opencode.jsonc` — project config at the repo root.
- `<repo>/.opencode/opencode.json` / `.jsonc` — local config, the highest-priority config layer; currently absent in ai-thoughts, so sessions there run on the global config plus defaults.
- `<repo>/.opencode/skills/<name>/SKILL.md` — skills, auto-discovered.

## AGENTS.md loading and precedence

The loader (source: `packages/core/src/instruction-context.ts`) reads the global file plus every AGENTS.md it finds walking up from the directory opencode was opened in to the project root (for a git repo, the repo root). Every file loads; none overrides another. They are concatenated into the system prompt in this order.

```
rendered into the model's context, in this order (all load, none override):

  1. ~/.config/opencode/AGENTS.md        global rules (always, first)
  2. <cwd>/AGENTS.md                     nearest project file
  3. <parent>/AGENTS.md                  walking upward
  4. ...                                 one file per directory
  5. <project root>/AGENTS.md            farthest, rendered last

  Fallback per category, only where no AGENTS.md exists:
     CLAUDE.md / ~/.claude/CLAUDE.md     Claude Code compatibility

  Because every file is in the prompt at once, conflicts are not settled by
  precedence — the model sees all of them and is expected to follow all of
  them. Keep the layers non-contradictory.
```

This is visible in every session: the system prompt lists "Instructions from: /home/jeff/.config/opencode/AGENTS.md" followed by "Instructions from: .../ai-thoughts/AGENTS.md".

## opencode.jsonc loading and precedence

The config loader (source: `packages/core/src/config.ts`) reads config documents from low to high priority and applies them in that order — later files win on the same key. Permission rulesets are appended rather than replaced, so global rules and local rules all stay live.

```
config documents, from lowest to highest priority (later wins):

  1. ~/.config/opencode/opencode.json / .jsonc         global
  2. <project root>/opencode.json / .jsonc             project root
  3. <intermediate dirs>/opencode.json / .jsonc        walking down toward cwd
  4. <cwd>/opencode.json / .jsonc                      nearest direct file
  5. <project root>/.opencode/opencode.json / .jsonc
  6. <intermediate dirs>/.opencode/.../.opencode/...
  7. <cwd>/.opencode/opencode.json / .jsonc            local, highest priority

  Rules (permissions) are appended, not replaced:
  within one rule list, "last matching rule wins".
  Inspect the resolved result with:  opencode debug config
```

## Permission model and decision flow

Permission effects are allow, ask and deny; `opencode --auto` auto-approves ask results (deny still enforced). The built-in default agent rule list begins with a catch-all `{action: "*", resource: "*", effect: "allow"}` (source: `packages/core/src/plugin/agent.ts`), and the config's `permission` rules are appended after those defaults for every agent (source: `packages/core/src/config/plugin/agent.ts`). The practical consequence: anything the config does not mention runs without prompting — which is exactly why a `"*": "ask"` catch-all in the old config caused the prompt flood, and why removing it made unmatched commands run silently.

For a tool call, the matching rule is the last rule whose wildcard pattern matches the action and resource (source: `packages/core/src/permission.ts`). Bash rules match the parsed command string (e.g. `git status --porcelain`); `*` matches any characters, `?` exactly one. Aggregation across resources: any deny blocks, otherwise any ask prompts, otherwise allow. A config `deny` is a hard pre-check that a per-session "always" approval cannot override; a config `ask` can be approved per-session. Per-session approvals chosen in the ask prompt (once / always / reject) are stored per project and appended after config rules.

```
per tool call -> evaluate (action, resource) against
   [built-in defaults ... config rules ... saved per-session approvals]

   find last matching wildcard rule
   |- config denies any resource?        -> BLOCKED (hard, no override)
   |- any matched rule says deny?        -> BLOCKED
   |- any matched rule says ask?         -> PROMPT (once / always / reject)
   `- otherwise (no config rule matched) -> RUNS (default catch-all allow)

note: an ask/deny pattern written AFTER an allow with the same prefix shadows
it (last matching rule wins) — keep the prefixes of asks disjoint from allows.
```

`edit` covers edit, write and patch. `~` and `$HOME` expand only in path-action patterns (read, edit, external_directory), not in bash patterns.

## Workflow: changing permissions

1. Edit `negtivSpace/opencode/opencode.jsonc` — the single source of truth. `negtivSpace/` here is the local clone of the `negtivSpace/negtivSpace` GitHub repo (the folder and the repo share the same name), sitting outside any individual project tree. Two symlinks wire it into OpenCode: `~/.config/opencode/opencode.jsonc → …/negtivSpace/opencode/opencode.jsonc` and `~/.config/opencode/AGENTS.md → …/negtivSpace/opencode/AGENTS.md`. Edits to the repo propagate to both symlinks immediately; git history and rollback come for free.
2. Restart opencode — the config is read once when a location opens, so changes need a restart.
3. Verify with `opencode debug config` before trusting the new rules.
4. For one-off tweaks, use the ask prompt's once / always ("Accept always") / reject; "always" lasts only the current session, so permanent rules go in the config.

## Conflict, confusion and duplication review

Duplication between global and repo AGENTS.md: eight rules used to appear almost verbatim in both `~/.config/opencode/AGENTS.md` and `ai-thoughts/AGENTS.md`, plus two in `history/AGENTS.md`. On 2026-08-11 the repos were deduplicated: universal rules now live only in the global file (symlinked into `negtivSpace/opencode/`), and each repo's AGENTS.md keeps project-specific rules plus a one-line delegation to global. The tradeoff: a public clone of a repo read by other tooling no longer carries the universal rules, but on this machine every session gets them from the global file, and there is a single owner per rule so drift is impossible. The `negtivSpace/AGENTS.md` pattern (delegate to global) is the model the repo files now follow.

The two global files are now symmetric: both are git-managed symlinks into `negtivSpace/opencode/` (the config was already a symlink; on 2026-08-11 AGENTS.md joined it). History, rollback and machine-switch survival all come from the repo. The setup on a new machine is: clone `negtivSpace` and create the two `~/.config/opencode/` symlinks.

Doc drift already bit once: the AGENTS.md permission paragraph and the config comments both describe the permission behavior, and one edit claimed unmatched commands were "silently denied" when the truth is that they run under the default allow. Keep those two descriptions in sync — the AGENTS.md paragraph is the human-facing truth, the config comment the inline truth.

The main pitfall to avoid: a local `.opencode/opencode.jsonc` overrides the global config for that repo, so reintroducing a `"*": "ask"` catch-all there (the old style) silently restores the prompt flood in just that repo. Keep any future local config allow-driven, matching the global style.

No genuine conflicts between the surfaces: AGENTS.md instructs behavior, the config gates tools, and they never fight because they operate on different things. The "commit only when asked" rule and the "push to both remotes" convention are complementary (commit is user-initiated, push follows the repo convention), and the config's read-only git allow list backs both. The read-only git/gh allow prefixes and the destructive ask prefixes were checked to be disjoint — the only near-misses (`git stash list`, `git tag -l`, `git config --get`, and friends) stay allowed because the ask patterns use explicit subcommands instead of a broad `git stash*` / `git tag*` catch-all.

Prose wrapping is deliberately per-repo, not global. `ai-thoughts/AGENTS.md` mandates no hard-wrap (one paragraph per line, verified by `scripts/unwrap_md.py --check`), `history/AGENTS.md` auto-wraps, and the global `opencode/AGENTS.md` delegates to each repo — never assume a global wrapping rule. Reviewed on 2026-08-11: keep the rule. It's cheap (one line, no pipeline to maintain) and high-value — hard-wrapped prose turns a one-word edit into a 20-line diff and muddies CJK word boundaries. `unwrap_md.py` is insurance, not a gate: with no CI pipeline, `--check` is a manual hygiene check, and escalating it to a hook or CI gate isn't worth building.

## References

- Source — config load order: `packages/core/src/config.ts`; AGENTS.md loading: `packages/core/src/instruction-context.ts`; permission evaluation and defaults: `packages/core/src/permission.ts`; built-in default agent rules: `packages/core/src/plugin/agent.ts`; config rules appended to agents: `packages/core/src/config/plugin/agent.ts`.
- Docs — opencode.ai/docs/rules, opencode.ai/docs/config, opencode.ai/docs/permissions.
- Local — `~/.config/opencode/opencode.jsonc` (symlink to `negtivSpace/opencode/opencode.jsonc`) and `~/.config/opencode/AGENTS.md` (symlink to `negtivSpace/opencode/AGENTS.md`).

btw, i use arch 
