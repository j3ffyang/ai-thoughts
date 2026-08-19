---
name: skill-publish
description: >
  Publish SKILL.md files to ClawHub (clawhub.ai) and diagnose publish failures
  across the three skill repos (history, ai-custom-skills, ai-thoughts). Use
  when the user wants to publish skills to ClawHub, manually trigger a publish,
  check why a publish failed or was skipped, or understand the ClawHub skill
  sync pipeline.
---

# ClawHub Skill Publish

Publish and maintain the ClawHub skill registry. All skills are published to a single ClawHub account (`j3ffyang`) through GitHub Actions; skills are never published manually.

## Scope

Skills come from three repos under the `negtivSpace` superproject. Each repo has its own `.github/workflows/clawhub-skill-sync.yml` that publishes its skills to ClawHub:

- `history/` — publishes only `.opencode/skills/chinese-history-literature-culture` (via a `skill_path` entry). The `astro-sync` skill in `history/.opencode/skills/` is **local-only**: it stays in the repo for opencode to load, but is not published to ClawHub.
- `ai-thoughts/.opencode/skills/` — `astro-sync`, `custom-infographic`, `skill-publish`, `resize-for-banner`, `translate-to-chn`. All are published via a glob over `.opencode/skills/*/SKILL.md`, so `skill-publish` self-publishes like any other skill.
- `ai-custom-skills/` — roots `openclaw/`, `hermes/`, `claude-code/`, plus the nested `claude-code/perplexity-downloader/perplexity-downloader` handled via a matrix `skill_path` entry. Data folders without a `SKILL.md` (e.g. `openclaw/twitter-bookmarks-exporter`) are skipped automatically.

## Single-source rule — read before anything else

- **Only the `j3ffyang/*` copies of these repos publish.** The `negtivspace/*` copies keep the same workflow file (mirrors stay in sync) but are a no-op: every job is guarded with `github.repository_owner == 'j3ffyang'`.
- Both copies are pushed on every change, so both repos run the workflow on push. Without the owner guard they would both publish to the *same* ClawHub account and race, producing `Version X already exists` collisions.
- Never create or run a manual publish path that could double-publish to ClawHub. If a skill edit is needed, edit it in the working repo, push to both remotes, and let the workflow publish once.
- `clawhub_token` (the `j3ffyang` ClawHub token) is set as a repo secret in all six repo copies; only the `j3ffyang` ones ever use it.

## Pipeline

- Workflow per repo: `clawhub-skill-sync.yml` with a `dry-run` job (pull requests only) and a `publish` job (pushes / workflow_dispatch), both calling the reusable workflow `openclaw/clawhub/.github/workflows/skill-publish.yml` pinned to tag `v0.23.3` (no `@v1` tag exists).
- Both jobs need `permissions: {contents: read, id-token: write}`; callers of the reusable workflow fail with `startup_failure` (`id-token: none`) if the job-level permission is missing.
- Publishing uses the caller repo's checkout; a new or changed skill is detected by fingerprint. Unchanged skills are skipped (`alreadySynced`).

## Status & version semantics

- `unchanged` / `alreadySynced` — fingerprint matches ClawHub; nothing to do.
- New skill — first publish is version `1.0.0`.
- Changed skill — next patch version of the latest published version.
- `Error: Version X.Y.Z already exists. Increment the version number...` — the skill is already on ClawHub at that version (usually from a prior publish or a dual-remote race). Do not re-publish; the workflow will report it `alreadySynced` on the next run.
- `Invalid publish output: 'pending-publication'` — a false alarm. The publish actually succeeded; the upstream workflow's status map (v0.23.3) does not recognize the `pending-publication` status string and reports it as failed. Verify with the skills API before assuming a problem.

## Procedure

1. **Add or edit a skill**: create/update the `SKILL.md` (and sibling files) in the correct root of the correct repo. Respect that repo's conventions (e.g. `history/AGENTS.md` filename rules). Do not rename or convert skills; publish them as-is.
2. **Push to both remotes** of the submodule (`j3ffyang` and `negtivspace`). The push to `j3ffyang/*` triggers the publish; the `negtivspace/*` run is a no-op by design.
3. **Wait for the `j3ffyang/*` workflow run** to finish; check the publish summary for the affected slug.
4. **Manually trigger a publish** (e.g. after a failed run) via `workflow_dispatch` on the `j3ffyang/*` repo.
5. **Verify on ClawHub** (read-only, API): `curl -s -H "Authorization: Bearer $CLH_TOKEN" https://clawhub.ai/api/v1/skills/<slug>` — the `latestVersion` and `owner.handle` fields confirm what is live.

## Error Handling

- **`Version X.Y.Z already exists`** — confirm the skill already exists (skills API) and let the next run mark it `alreadySynced`; if the local content is genuinely newer, the workflow's next-patch bump handles it on its own.
- **`pending-publication` reported as failure** — treat as success; verify via the skills API.
- **`startup_failure` / `id-token: none`** — the caller job is missing `permissions: {contents: read, id-token: write}`; add it.
- **Nested skill not found** — the matrix `skill_path` must point at the folder containing the `SKILL.md` (double-nested folders need the full path).
- **Slug collision** — `astro-sync` exists in both `history` and `ai-thoughts` with different content. `ai-thoughts` publishes it (canonical); `history`'s copy is local-only, kept out of ClawHub via `skill_path`. Never publish the same slug from two repos to the same owner.
- **Token missing** — publish fails without `clawhub_token`; it must be set as a secret on the `j3ffyang/*` repo.

## Verification

- All three workflow files carry `github.repository_owner == 'j3ffyang'` guards on both jobs.
- `actionlint` passes on every `clawhub-skill-sync.yml`.
- Every expected slug appears in the `j3ffyang/*` run's publish summary as `alreadySynced` or `published`.
- Skills API returns `owner.handle == 'j3ffyang'` and the expected `latestVersion` for every published skill.
