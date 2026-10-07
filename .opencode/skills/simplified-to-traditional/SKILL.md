---
name: simplified-to-traditional
description: >
  Convert a Simplified-Chinese article in ai-thoughts/docs/ into its Traditional-Chinese
  twin, and keep the two in sync. The Simplified article is the source of truth and
  lives as <YYMMDD-slug>-zh-hans.md; the Traditional twin is generated to
  <YYMMDD-slug>-zh-hant.md with OpenCC (s2twp) plus a permanent cross-link. Use when
  the user asks to make, sync, or update the Traditional (繁體) version of a Chinese
  article — "convert to traditional", "做繁體版", "同步繁简", "zh-hant", "繁體". Never
  runs automatically; acts only on an explicitly named article. Future articles only
  — do NOT backfill existing files unless the user explicitly orders it.
---

# Simplified → Traditional (zh-hans → zh-hant)

Convert one Simplified-Chinese article into Traditional Chinese, and keep the pair in sync.

## Approval gate — read before anything else

- **Never convert or write without explicit user approval.** This skill converts on demand only; it does not run automatically and does not pick articles on its own.
- **Wait for the user to name the article.** If they don't, do nothing but ask which one.
- Before writing, confirm the plan: the source file, the exact output path, and whether an existing `-zh-hant.md` should be overwritten. **Never overwrite silently.**
- **Scope: future articles only.** In this repo a bare `docs/<YYMMDD-slug>.md` is the **English** article and the legacy `-chn.md` files are the existing Simplified-Chinese articles — neither is a source here unless the user explicitly orders it.

## Conventions

- **Filenames.** Simplified article = `docs/<YYMMDD-slug>-zh-hans.md`; Traditional twin = `docs/<YYMMDD-slug>-zh-hant.md`. (In ai-thoughts a bare `.md` is English and the legacy `-chn.md` files are out of scope.)
- **Source of truth = the Simplified file.** The Traditional file is derived from it.
- **Traditional variant.** OpenCC `s2twp` (Taiwan, phrase-aware) — the best default for these literary articles.
- **Cross-link.** Exactly one line, directly under the H1 and above the infographic; Chinese label; a permanent absolute URL on the `j3ffyang` account:
  - In the Simplified file: `> 繁体版：[<simplified title>](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/<slug>-zh-hant.md)`
  - In the Traditional file: `> 簡體版：[<traditional title>](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/<slug>-zh-hans.md)`
  - The label is written in the file's own script (Simplified file → `繁体版`; Traditional file → `簡體版`) so neither file mixes scripts.
- **Infographic stays Simplified** and is shared by both files (same `../imgs/...` path). The README lists the Simplified article only.

## Procedure

1. **Wait for the user to name the article**, then locate `docs/<YYMMDD-slug>-zh-hans.md` (in this repo the source must be `-zh-hans.md` — a bare `.md` is English).
2. **Confirm the plan**: source path, output path (`-zh-hant.md`), and overwrite permission if the output already exists.
3. **If an existing `-zh-hant.md` is present**, stop and ask before overwriting — unless the user asked to update it.
4. **Run the sync script:**
   ```bash
   python3 .opencode/skills/simplified-to-traditional/scripts/sync_tra.py docs/<slug>-zh-hans.md
   ```
   It (a) injects/updates the Simplified file's `繁體版` cross-link, (b) converts the body with `opencc -c s2twp`, (c) injects the Traditional file's `简体版` cross-link, and (d) writes `docs/<slug>-zh-hant.md`.
5. **Review** the generated Traditional against the Simplified. OpenCC can miss proper nouns, rare characters, or archaic terms. Surface anything suspicious to the user; do not silently hand-fix — a hand-edit is drift and will fail the next `--check`.
6. **Verify** the pair is in sync:
   ```bash
   python3 .opencode/skills/simplified-to-traditional/scripts/sync_tra.py docs/<slug>-zh-hans.md --check
   ```
   Exit 0 = in sync; exit 1 lists what is stale.
7. **Report**: source, output, and any review notes.

## Keeping the two in sync

- After editing the **Simplified** article, re-run the sync to refresh its Traditional twin.
- `--check` regenerates the Traditional in memory and diffs it against the file (ignoring the cross-link lines); non-zero exit means out of sync.
- **Do not treat the Traditional file as an editable primary.** Edit the Simplified and re-sync. If a term is genuinely mis-converted by OpenCC, tell the user and decide together, then pin it as a `(from, to)` pair in `scripts/sync_tra.py` → `OVERRIDES` — it is applied after OpenCC on every re-sync, so it survives (a hand-edit would not).

## Verification checklist

- [ ] Traditional file exists at `docs/<slug>-zh-hant.md`.
- [ ] Both files carry the correct cross-link line directly under the H1 (Chinese label, `j3ffyang` URL, pointing at the other file).
- [ ] `sync_tra.py <source> --check` exits 0.
- [ ] The infographic reference points at the shared (Simplified) image; no broken `../imgs/`.
- [ ] The Simplified file's body is otherwise unchanged (only the cross-link line added).
- [ ] Nothing committed (commit only on explicit approval).

## Error handling

- **Source not found**: list `docs/*-zh-hans.md` and ask which to use; do not substitute a bare (English) or `-chn.md` file.
- **Output already exists**: stop and ask before overwriting.
- **`opencc` missing or wrong dict**: report and stop; do not guess a conversion.
- **Ambiguous source name** (neither `-zh-hans.md` nor an explicitly ordered `-chn.md`): ask.
