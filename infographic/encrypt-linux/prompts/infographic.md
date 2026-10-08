Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: dense-modules
- **Style**: pop-laboratory
- **Aspect Ratio**: 16:9
- **Language**: English

## CRITICAL: Text Accuracy

The list below is the **complete and only** text that may appear in the image. Each string appears **exactly once** — no repeated labels, no echoed headings, no duplicated cells, no mirrored imagery. Do not render any word from the sections below this one.

Main title: `Encrypting Linux`
Subtitle: `From a hack 20+ years ago to LUKS + Veracrypt`

Module 1 headline: `The Hack That Started It`
Module 1 labels: `hack` · `ls lied` · `tripwire` · `hash baseline`

Module 2 headline: `Detect to Prevent`
Module 2 labels: `at rest: safe` · `unlocked: exposed`

Module 3 headline: `LUKS: the Whole OS`
Module 3 labels: `except /boot` · `ESP = FAT32` · `header backup` · `key slots`

Module 4 headline: `cryptsetup`
Module 4 labels: `luksFormat` · `open` · `luksHeaderBackup`

Module 5 headline: `Overhead`
Module 5 labels: `~6.2 GiB/s` · `near-zero lag` · `AES-NI`

Module 6 headline: `Veracrypt: USB & Partitions`
Module 6 labels: `USB disks` · `veracrypt -c` · `cross-platform`

Module 7 headline: `rsync Backup`
Module 7 labels: `rsync -aAXH --delete` · `LUKS to Veracrypt USB` · `encryption is not backup`

## Core Principles

- Follow the layout structure precisely for information architecture
- Apply style aesthetics consistently throughout
- Keep information concise, highlight keywords and core concepts
- Use compact spacing; this layout prioritizes information density
- Maintain clear visual hierarchy

## Text Requirements

- All text must match the specified style treatment
- Main title should be prominent and readable
- Key numbers should be visually emphasized with accent color, slightly larger
- Labels should be clear and appropriately sized
- Render every string in the list exactly once; if two modules seem to need the same word, rephrase one instead of repeating it
- Do not render any hash value, terminal output line, filename, arrow caption, state caption, or any other word that is not in the list
- The large throughput figure appears exactly once, in its own module only
- The three command chips in the cryptsetup module each show their command exactly once — no truncated copies, no captions, no extra badges or warning words

## Layout Guidelines

High-density modular layout with seven typed information modules packed with concrete data. Each module serves one function and contains real data points, not generic description. Minimal whitespace, compact spacing, smaller text acceptable to maximize density. Each module sits in its own clearly bounded cell with a small badge-style header. Use big highlighted numerals for counts and the throughput figure. Reading order runs left to right, top to bottom across the modules. No decorative-only empty space; every region carries information.

## Style Guidelines

Lab-manual precision meets pop-art color impact: coordinate systems, technical diagrams, and fluorescent accents on a faint blueprint grid. Palette: background professional grayish-white with a faint blueprint grid; primary muted teal/sage green for functional blocks and data zones; a single vibrant fluorescent pink reserved strictly for warnings and the most critical figure; vivid translucent lemon-yellow highlighter over keywords; ultra-fine charcoal-brown hairlines for grids and rules. Typography: bold brutalist headers with high impact, crisp technical sans-serif body, large highlighted numerals. Include fine grid lines, ruler ticks, cross-hair targets, and directional arrows as pure graphics. Maintain tension between massive bold headers and small precise annotations. Avoid cute doodles, soft pastels, and flat stock icons. Render no footer, margin text, or caption strip anywhere in the image.

---

Generate the infographic using exactly the strings in the "CRITICAL: Text Accuracy" list, each appearing once, and nothing else.

Everything below is guidance for imagery, composition and meaning only — do **not** render any word from it as text:

Module at top left: a broken-list icon beside a small shield motif — the illustration itself contains no text.

Module at top center: a two-state icon pair — a closed padlock over a disk, and an open padlock over a screen.

Module at top right: a disk graphic split into a tiny unlocked segment and a large locked segment.

Module at mid left: a row of exactly three monospace command chips, each holding one command, with no other text.

Module at mid center: a single large numeric callout with a speedometer motif.

Module at mid right: a USB stick beside one command chip, with small cross-platform icons.

Module along the bottom, spanning full width: a clean two-icon flow — a disk icon on the left and a USB icon on the right, joined by one bold straight arrow pointing left to right. Keep this band simple, with generous space around the two icons.
