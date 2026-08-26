---
name: bold-highlights
description: >
  Add bold highlights to key concepts in each paragraph so readers can scan
  and capture the article's core points. Use when polishing an article in
  ai-thoughts/docs/ or when the user asks to make an article more scannable
  or add highlights.
---

# Bold Highlights — Scannable Prose

Bold 1-2 words per paragraph to carry the paragraph's core concept. When read
alone, the bolded words should tell the article's arc.

## Inputs

- `target` — path to the article in `ai-thoughts/docs/` (optional). If omitted,
  apply to the article currently being worked on.

## Outputs

- The article file with bold highlights applied.

## Procedure

1. Read the article and identify its overall arc (the story it tells from start
   to finish).
2. For each body paragraph (skip the title, sign-off, and image captions):
   - Identify the 1-2 most essential concepts — the words that carry the
     paragraph's core meaning.
   - Bold them using `**word**` syntax.
3. Verify: scan only the bolded words from top to bottom. Does the article's
   story hold? If not, adjust which words are bolded.
4. Regenerate READMEs if the article is registered in `articles.yaml`.

## Constraints

- **Max 2 bold highlights per paragraph.** Fewer is better. Three or more
  defeats the purpose.
- **No adjacent-paragraph repeats.** Don't bold the same word in two consecutive
  paragraphs — it dilutes the signal.
- **Keep bolded phrases short.** 1-3 words max. A single word is ideal.
- **Don't bold proper nouns, tool names, or obvious context.** Bold the
  *concept*, not the *thing*. Example: bold "ground truth" (the idea), not
  "OpenCode" (already obvious from context).
- **Don't bold the title or sign-off.**

## Verification

- Each body paragraph has 1-2 bold highlights (no more).
- Scanning only the bold words tells a coherent mini-story.
- No bold word appears in two adjacent paragraphs.
- Article still reads naturally — highlights are additive, not disruptive.

## Error Handling

- **User says no**: skip bolding; leave the article as-is.
- **Article already has bold highlights**: verify they follow the constraints;
  adjust if needed, don't add more.
- **Not an article**: never apply to READMEs, `articles.yaml`, or files outside
  `ai-thoughts/docs/`.
