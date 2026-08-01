# AGENTS.md

## Project

Personal repository of AI/tech articles and bilingual (Chinese / English)
essays — including OpenClaw/Hermes notes, history, culture, and second-brain
write-ups — with a YAML-driven README index.

## Working rules

- **Get approval before any change.** Present the plan and wait for the
  user's explicit go-ahead before editing files, generating output, or
  running state-changing commands. If anything is unclear, ask rather than
  assume.
- **Commit only when asked.** Never commit, amend, or push unless the user
  explicitly requests it. When committing, stage only intended files.

## README index workflow

`README.md` and `README_zh.md` are **generated output** — never edit them by
hand. They are produced from the single source of truth `articles.yaml`:

```bash
python scripts/gen_readmes.py
```

To add or update an article:

1. Drop the file into `docs/` (follow the `YYMMDD-slug` naming).
2. Add/update a row in `articles.yaml`:
   - English article → link with `lang: en` (+ `desc_en`)
   - Chinese article → link with `lang: zh` (+ `desc_zh`)
   - Draft/working note → `status: draft` (lands in the drafts section)
   - Optional `label_zh` on a link gives the Chinese display name in
     `README_zh.md` (Chinese articles usually get one).
3. Run the generator, confirm the diff shows only the intended row, and
   commit `articles.yaml` + both regenerated READMEs together.

### EN / ZH routing rule

- `README.md` keeps a row only if it has at least one `lang: en` link, and
  renders just those English links.
- `README_zh.md` shows **all** rows (EN + ZH) with Chinese descriptions;
  Chinese display labels come from `label_zh` where set, English slugs
  otherwise.

## Repo conventions

- Docs-only repository: no build, lint, or test steps.
- Two remotes on `main`: `negtivspace` and `j3ffyang` — push to both.
