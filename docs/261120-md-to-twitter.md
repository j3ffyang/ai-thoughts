# Markdown Into X: An OpenCode Skill, Threads and Long Posts

*2026-11-20*

**Thesis:** X renders no rich text and cannot carry an image in a paste, so the third converter cannot produce the "paste payload" the other two do. It produces a thread script, and the honest question is which shape fits which account.

**Status:** working. The converter, the weighted counting, the splitting and the dry run are tested. The API path is written and has never run against the live service, because no X credentials exist on this machine.

**The skill:** [md-to-twitter](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/md-to-twitter/SKILL.md) — a custom `SKILL.md` written for **OpenCode**: two files in the repo, no service, no plugin, nothing to install.

## Why this exists

My articles are Markdown files in a git repo. That is the source of truth, and publishing anywhere else is a rendering step. Two targets already have a converter: [LinkedIn](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261111-md-to-linkedin.md) takes an HTML fragment, and Medium takes one too, as long as its images are hosted at a public URL. Both produce a single file you paste once.

X takes neither. It is the least file-friendly of the three, and the reason is not the converter — it is the platform. There is no rich-text paste and no way to put an image inside text. So "one file that carries the pictures" is impossible on X by design, and the equivalent has to be something else.

## What X cannot hold

No bold, no italics, no headings, no tables, no code blocks. An image reaches X only by upload; a paste never carries one. That is not a limitation to work around. It is the shape of the target, and the converter's job is to know it and say so.

The policy is the same as the sibling skills: **degrade the formatting, keep the words.** Markers are stripped, links survive as text plus URL, and each image becomes an attachment on the post that mentions it.

## What the file actually is

`docs/<article>-twitter.txt` is a numbered script, not a payload. For the [skill-versus-MCP article](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261111-skill-vs-mcp.md) it is 66 posts, each separated by `---`, with the image listed under the post that carries it:

```
[1/66]
A Skill or an MCP Server? Two Ways to Give an Agent a Trick

2026-11-11

Thesis: they are not two answers to one question. …
```

You read from it. You do not upload it. That is the whole difference from the LinkedIn and Medium files, and it is the part that took a while to accept.

## Two shapes, one article

X gives a free account 280 characters per post, and a paid account 25,000 in one long post. The same article has two honest renderings:

| | free account | paid account |
| --- | --- | --- |
| shape | thread | one long post |
| posts | 66 at 280 characters | 1 at 13,609 characters |
| flag | *(default)* | `--limit 25000` |
| images | 1 upload, on post 4 | 1 upload, on the post |
| effort | 66 copy-pastes, or `--post` | 1 copy-paste, or `--post` |

The paid path is the closest thing to the LinkedIn and Medium experience: one paste, one image, done. The free path is arithmetically a wall, and the file says so rather than pretending otherwise.

## Code, quotes, tables

X's long post has no code frame and no table. The converter's default keeps the words: code stays text and stays copyable, tables flatten to `a | b | c` rows, quotes keep their `>` prefix. For this article the tables are the comparison grids, so `--tables image` screenshots them and attaches the PNGs — three images in one long post, code still text.

Code as an image is a worse trade. It looks right and cannot be copied, which is the opposite of what code is for. The native code frame lives in X Articles, not in a long post: its Insert menu has Code and Table, each an atomic block. That is a different target, and a different skill.

## The number that decides

13,609 characters divided by 280 is 66. That is arithmetic, not a bug. A 66-post thread is rarely read end to end, so the choice is deliberate:

- **Paid** — `--limit 25000`, one post. The only way a 2,300-word article arrives as one piece.
- **Free** — accept the long thread, or cut the opening posts by hand and append the article URL.
- **Neither** — the thread file is still a scaffold: keep the first few posts and link the rest.

The script does not summarise. Condensing 13,609 characters into a readable thread is an editorial decision, and a converter that quietly dropped paragraphs would be worse than one that reports 66.

## Posting it, one post at a time

The manual route is the file and the composer. Copy post 1, paste, post. Each next post is a reply to the one before. On post 4, attach the image by hand. For the paid shape there is nothing to chain: copy the one long post, attach its images, post.

The API route is `--post`. It uploads each image, posts the thread in order, and chains each post as a reply to the one before. `--at N` sends exactly one post and prints the command for the next:

```sh
.opencode/skills/md-to-twitter/scripts/md2twitter.py docs/<article>.md --at 1 --post
# posted 1/66: https://x.com/i/status/…
# next: --at 2 --post --reply-to 1234567890
```

Nothing is remembered between runs — the tweet id is the state, which is why it is printed rather than stored. Credentials are OAuth 1.0a, from the environment or `~/.config/md-to-twitter/keys.json`.

## What it enforces

| limit | value |
| --- | --- |
| characters per post | 280 weighted (274 when `--number` reserves room) |
| images per post | 4 |
| image size | 5 MB |
| image types | png, jpeg, webp, gif |

Counting follows X's rules: most characters cost 1, CJK and emoji cost 2, and every URL costs 23 however long it is. A Chinese article therefore produces roughly twice as many posts as the same article in English.

## The files

The skill is two files: a `SKILL.md` that says when to use it and what X can hold, and `md2twitter.py`, which does the conversion, the counting, the splitting and the posting.

- ClawHub: [md-to-twitter](https://clawhub.ai/j3ffyang/skills/md-to-twitter)
- GitHub: [SKILL.md](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/md-to-twitter/SKILL.md)

The lesson is not about X specifically. Every target has a shape it can hold, and the honest part of a converter is admitting which constructs it cannot — and, when the target cannot take a file at all, producing the script a person or an API can follow instead.

btw, i use arch
