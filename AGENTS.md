# AGENTS.md

## Project

Personal repository of AI/tech articles and bilingual (Chinese / English) essays — including OpenClaw/Hermes notes, history, culture, and second-brain write-ups — with a YAML-driven README index.

## Working rules

The universal working rules (approval before changes, commit only when asked, honesty, ground truth, rollback, brand conventions) are defined in the global `~/.config/opencode/AGENTS.md` and apply here too. This file adds only what is specific to this repo.

- **Rollback defaults.** Git-tracked files → `git restore` / `git revert`; generated output (`README.md`, `README_zh.md`, `PORTFOLIO.md`) → regenerate from its source of truth (`articles.yaml` / the portfolio template).

## Writing conventions

- **No hard-wrap.** Avoid hard-wrap at all, including `docs/`, `.opencode/skills/`, and agents — prose is one paragraph per line. Verify with `python scripts/unwrap_md.py --check`, or run `python scripts/unwrap_md.py` to unwrap.
- **Chinese files are translations of the English original.** Every Chinese markdown file is translated from, and identical in content to, its English counterpart — only the language differs. Don't search the Chinese file as a reference, unless otherwise specified.
- **Arch sign-off.** Every article in `docs/` ends with the line `btw, i use arch ` as its final paragraph, unless the user explicitly says otherwise. It stays verbatim English in both EN and ZH versions; don't duplicate it if already present, and never add it to READMEs or `articles.yaml`.

## Filename conventions

Every file in `docs/` and `imgs/` follows a `YYMMDD-slug` pattern: a 6-digit date (`YYMMDD`, no `HHMM`, no `YYYY-MM-DD`), a hyphen, then a lowercase slug. No spaces.

- **Articles** — `docs/<YYMMDD>-<slug>.md`, e.g. `260313-openclaw-thoughts.md`.
- **Images** — `imgs/<YYMMDD>-<slug>.<ext>`, e.g. `260313-main.png`; images for an article share the article's `YYMMDD` prefix.
- **Screenshots / captures with no meaningful name** — keep the capture time as the slug, e.g. `260506-180248.png` (from `2026-05-06-180248_hyprshot.png`).
- **Renaming** — when a file is renamed, update every `../imgs/<file>` and doc link that referenced the old name.

## README index workflow

`README.md` and `README_zh.md` are **generated output** — never edit them by hand. They are produced from the single source of truth `articles.yaml`:

```bash
python scripts/gen_readmes.py              # regenerate both READMEs
python scripts/gen_readmes.py --check      # CI/verification: exit 1 if a README is stale
```

To add or update an article:

1. Drop the file into `docs/` (follow the rules in "Filename conventions").
2. Add/update a row in `articles.yaml`:
   - English article → link with `lang: en` (+ `desc_en`; no `desc_zh` until a `-chn.md` exists)
   - Chinese article → link with `lang: zh` (+ `desc_zh`)
   - Draft/working note → set `section: drafts` (lands in the Drafts & Working Notes section). Keep `status: draft` too — `status` is metadata only (`draft` or `published`) and never affects placement; the generator routes rows by `section`.
   - Optional `label_zh` on a link gives the Chinese display name in `README_zh.md` (Chinese articles usually get one).
3. Run the generator, confirm the diff shows only the intended row, and commit `articles.yaml` + both regenerated READMEs together.

**Note:** `gen_readmes.py` prints a warning for every `docs/*.md` not listed in `articles.yaml` (e.g. unregistered drafts). That's expected until the row is added — it's a reminder, not an error.

The generator also **fails hard** on invalid manifests: unknown `section`, missing `desc_zh` on any row where the English article's `-chn.md` counterpart exists in `docs/` (or the row carries a `lang: zh` link), missing `desc_en` on any row with a `lang: en` link, or a `path` that points to a missing file. Fix those before committing. An EN-only row (no `-chn.md` file yet) may omit `desc_zh` — `README_zh.md` then falls back to its `desc_en`. The trigger for adding `desc_zh` is the `-chn.md` file existing in the same folder; add `desc_zh` together with that `-chn.md` version.

### EN / ZH routing rule

- `README.md` keeps a row only if it has at least one `lang: en` link, and renders just those English links.
- `README_zh.md` shows **all** rows (EN + ZH) with Chinese descriptions; Chinese display labels come from `label_zh` where set, English slugs otherwise.

## PORTFOLIO.md workflow

`PORTFOLIO.md` is **generated output** too — never edit it by hand. It is rendered from the static template `scripts/portfolio_template.md` with `{{...}}` placeholders filled from `articles.yaml`, `docs/`, and git log:

```bash
python scripts/gen_portfolio.py              # regenerate PORTFOLIO.md
python scripts/gen_portfolio.py --check      # CI/verification: exit 1 if stale
```

Filled automatically: article count (unique published articles by YYMMDD from `articles.yaml`), the ai-thoughts repo row's latest commit, the "Latest Articles" list (top N published articles by date, deduped by YYMMDD), and the "Last Updated" date. Editorial content (the Activity Timeline, repo tables, tech stack, etc.) lives in the template — edit the template, then regenerate.

## Repo conventions

- Docs-only repository: no build/lint/test pipeline; only the README generator and its `--check` validation mode.
- Two remotes on `main`: `negtivspace` and `j3ffyang` — push to both. `negtivspace` is a **normal GitHub user account** (a second personal account, "Negative Space 留白"), **not** an org. Editing `negtivspace/ai-thoughts` via `gh`/API (e.g. setting the About description/homepage) requires the `negtivspace` account's own token — the `j3ffyang` token gets 404 on that account's repos.
