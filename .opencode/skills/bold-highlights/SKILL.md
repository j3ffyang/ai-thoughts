---
name: bold-highlights
description: >
  Add sparse, deliberate bold highlights to a few key concepts so readers can
  scan and capture the article's core points. Use when polishing an article in
  ai-thoughts/docs/ or when the user asks to make an article more scannable
  or add highlights.
---

# Bold Highlights — Scannable Prose

Add bold highlights sparingly — a few key words that carry the article's arc. Bolding in most paragraphs defeats the purpose; a reader should notice a handful of highlights, not a shower.

## Inputs

- `target` — path to the article in `ai-thoughts/docs/` (optional). If omitted, apply to the article currently being worked on.

## Outputs

- The article file with bold highlights applied.

## Procedure

1. Read the article and identify its overall arc (the story it tells from start to finish).
2. Pick a handful of key arc moments — roughly 5-10 highlights for a full-length article. Good candidates: the opening thesis, one concept per major section, and the payoff or tip the author cares most about.
3. Bold the single most essential concept at each chosen moment. Leave most paragraphs un-bolded, and never bold list items.
4. Verify: scan only the bolded words from top to bottom. Does a sparse mini-story still hold? If not, move highlights to better moments.
5. Regenerate READMEs if the article is registered in `articles.yaml`.

## Constraints

- **Max 1 bold highlight per paragraph.** Most paragraphs should have none.
- **Target roughly 5-10 highlights per article.** A handful the reader can count — fewer is always better. When in doubt, remove one.
- **Space them out.** Don't bold in two adjacent paragraphs — the highlights should feel deliberate, not rhythmic.
- **Keep bolded phrases short.** 1-3 words max. A single word is ideal.
- **Don't bold proper nouns, tool names, or obvious context.** Bold the *concept*, not the *thing*. Example: bold "ground truth" (the idea), not "OpenCode" (already obvious from context).
- **Never bold list items.** Bullets are already scannable; bolding each one is noise.
- **Don't bold the title or sign-off.**

## Verification

- Roughly 5-10 bold highlights across the whole article; never more than one per paragraph.
- Scanning only the bold words tells a coherent, sparse mini-story.
- No bold in two adjacent paragraphs; no bold inside any list.
- Article reads naturally — the highlights are meant to be scarce.

## Error Handling

- **User says no**: skip bolding; leave the article as-is.
- **Article already has bold highlights**: verify they follow the constraints; thin them out if they're too frequent, don't add more.
- **User asks for a single highlight** (e.g. "highlight one thing"): honor that literally — bold just that concept and nothing else.
- **Not an article**: never apply to READMEs, `articles.yaml`, or files outside `ai-thoughts/docs/`.