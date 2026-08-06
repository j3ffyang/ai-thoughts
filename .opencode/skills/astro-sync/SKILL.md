---
name: astro-sync
description: >
  Convert and polish a Markdown article into AstroPaper-compatible post format
  for the astro_journal blog (everbox.io). Use when the user wants to publish
  or sync an article (e.g. from ai-thoughts/docs/) to the Astro blog, convert
  Markdown to Astro format, add AstroPaper frontmatter, or move images into
  src/assets/images/.
---

# Astro Sync

Convert a polished Markdown draft into a ready-to-publish AstroPaper post in
the `astro_journal` repo (`/home/jeff/pool/git/astro_journal`), copying and
rewriting image references to match the blog's conventions.

## Approval gate — read before anything else

- **Never sync, write, or publish anything without explicit user approval.**
  This skill converts on demand only; it does not run automatically.
- The **user decides which article** is ready to sync and publish from
  `ai-thoughts` to `astro_journal` and **points it out explicitly**. Do not
  guess, propose candidates, or sync articles on your own.
- When the user names an article, still confirm the plan (target category,
  draft/featured, tags) before writing to the blog repo.
- **Never commit or push without explicit user approval.** After writing the
  post, ask for go-ahead first; only then stage the post + new images, commit,
  and push. The blog repo (`astro_journal`) has a single remote `origin`.

## Blog conventions (source of truth: astro_journal/AGENTS.md)

- Posts live in `src/data/blog/<category>/` — categories: `tech`, `travel`,
  `photo`, `philosophy`. **Not** `src/content/`.
- Filenames: `yymmdd-lowercase-slug.md` — 6-digit date prefix, lowercase,
  hyphens only. No underscores, camelCase, or 10-digit timestamps.
- URLs derive from the filename; never hardcode `/posts/...` links.
- Frontmatter follows the AstroPaper schema (see below).
- Images live in `src/assets/images/`, referenced by literal relative path
  `../../../assets/images/<file>` from a post in `src/data/blog/<category>/`.
- Renaming a **published** post requires adding a redirect (old URL → new URL)
  to `postRedirects` in `astro.config.ts`.
- `.orig` files anywhere in the repo are intentional references — never modify
  or delete them.

## Inputs

- `source` — Path to the source Markdown article (e.g.
  `ai-thoughts/docs/260803-ollama-to-llamacpp.md`). Required. If the user only
  names an article, locate it in `ai-thoughts/docs/` by slug or date.
- `category` — Blog category: `tech`, `travel`, `photo`, or `philosophy`.
  Optional. Default `tech`.
- `draft` — `true`/`false`. Optional. Default `false` (published).
- `featured` — `true`/`false`. Optional. Default `false`.
  - `true`: homepage-worthy — a signature/opinion essay, deep dive, or
    milestone post that defines the blog's voice. Use sparingly (aim ≤ 20%
    of posts) so the homepage stays curated.
  - `false`: everything else — how-tos, quick notes, release/changelog
    posts, and `*-chn.md` translations of an already-published post.
  - When the user doesn't specify, ask which it is (per Procedure step 2);
    never auto-pick `true`.
- `tags` — List of lowercase hyphen-separated tags. Optional. Default derived
  from the article topic.

## Outputs

- `postPath` — Path to the created post, e.g.
  `src/data/blog/tech/260803-ollama-to-llamacpp.md`.
- `imagesCopied` — List of image files copied into `src/assets/images/`.

## Procedure

1. **Wait for the user to point out the article** to sync. Do not start until
   they name it explicitly.
2. **Confirm the plan** with the user: target category, `draft`/`featured`,
   and tags. Get their go-ahead before writing anything to `astro_journal`.
3. **Locate the blog**: confirm `astro_journal` is checked out at
   `/home/jeff/pool/git/astro_journal`.
4. **Read the source** article from `source`. If it has no frontmatter, infer
   the title from the first `#`/`##` heading and the date from the filename
   (or today if none).
5. **Determine the filename**: `yymmdd-lowercase-slug.md`. Normalize the slug:
   lowercase, hyphens only, strip underscores/camelCase and any existing date
   prefix/timestamp. Keep the 6-digit `yymmdd` date prefix.
6. **Polish** (light): fix grammar/spelling/clarity in English; preserve code
   blocks, inline code, and technical terms verbatim. Do not rewrite substance.
7. **Copy images**: for every `../imgs/<file>` reference in the source, copy
   the image from `ai-thoughts/imgs/` into `src/assets/images/`, normalizing
   the filename to lowercase-hyphens with a 6-digit `yymmdd` prefix. Rewrite
   the reference in the post to `../../../assets/images/<file>`.
8. **Write frontmatter** (AstroPaper schema):

   ```yaml
   ---
   author: Jeff Yang
   pubDatetime: <ISO-8601 datetime, e.g. 2026-08-03T12:00:00.000Z>
   title: <Post title>
   tags:
     - <tag1>
     - <tag2>
   description: <One-line summary>
   featured: false
   draft: false
   ---
   ```

   `pubDatetime` comes from the source date if present, otherwise now.
   `modDatetime` is optional and only set when updating an existing post.
9. **Write the post** to `src/data/blog/<category>/<filename>` with the
   frontmatter followed by the polished body.
 10. **Report** `postPath` and `imagesCopied` to the user.
 11. **Commit & push (only after approval):** ask the user explicitly whether
     to commit. On approval, stage the post and any new images in
     `astro_journal`, commit with a concise message, and push to `origin`.
     Without approval, leave the changes uncommitted and say so.

## Verification

- File is in `src/data/blog/<category>/` and named `yymmdd-lowercase-slug.md`
  (lowercase, hyphens only, 6-digit date prefix).
- Frontmatter contains at least `author`, `pubDatetime`, `title`, `tags`,
  `description`; `draft`/`featured` present when applicable.
- Every image reference in the post points to an existing file in
  `src/assets/images/` (verify with a glob/ls).
- No `../imgs/` references remain in the post.
- No hardcoded `/posts/...` links were introduced.
- If committed: the post and new images are staged together, and `origin/main`
  is up to date.
- Optional: run `pnpm run astro -- check` in the blog repo to confirm no
  content/config errors.

## Error Handling

- **Source not found**: list candidate files in `ai-thoughts/docs/` and ask
  which to use.
- **Image missing**: skip it, note it in `imagesCopied` as missing, and tell
  the user the reference will be broken.
- **Category invalid**: list `tech`, `travel`, `photo`, `philosophy` and ask.
- **Filename collision**: if a post already exists at the target path, stop and
  ask whether to overwrite, use `modDatetime`, or pick a new slug.
