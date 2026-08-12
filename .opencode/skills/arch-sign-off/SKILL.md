---
name: arch-sign-off
description: >
  Append the Arch Linux sign-off line `btw, i use arch ` to the very bottom of
  an article in ai-thoughts/docs/ (EN or ZH). This is a standing default for
  every article: apply it unless the user explicitly says not to. Use when
  writing or finishing any new article, or when the user asks to add it.
---

# Arch Sign-off

Append the Arch Linux sign-off line to the bottom of an article in `ai-thoughts/docs/`.

## Default rule — read before anything else

- **Every article in `ai-thoughts/docs/` ends with the sign-off line, unless the user explicitly says otherwise.** "Unless I say no" means: if the user has not told you to skip it, append it.
- The sign-off is one line at the very bottom of the file, as its own paragraph:

```
btw, i use arch 
```

- The sign-off stays **verbatim English** in both the EN and the ZH (`-chn.md`) versions. Do not translate it. Keep the  glyph (U+F303, `nf-linux-archlinux`) as-is.
- If the sign-off is already present, do not duplicate it.

## Inputs

- `target` — path to the article in `ai-thoughts/docs/` (optional). If omitted, apply to the article currently being written.

## Outputs

- The article file with the sign-off line at the end (or unchanged if already present).

## Procedure

1. Check the bottom of the target article.
2. If the last line is already `btw, i use arch `, stop — nothing to do.
3. Otherwise append the sign-off as the final line, separated by one blank line from the preceding paragraph.
4. When the article has a `-chn.md` counterpart, apply the same line to it (verbatim English).
5. Keep one paragraph per line (no hard-wrap); the sign-off is a single short line.

## Verification

- The file ends with `btw, i use arch ` plus a trailing newline.
- No duplicate sign-off lines.
- The `-chn.md` version (if any) carries the identical line.
- The  glyph (U+F303) is preserved.

## Error Handling

- **User says no**: do not append; leave the article as-is.
- **Not an article**: never append to READMEs, `articles.yaml`, or files outside `ai-thoughts/docs/`.
