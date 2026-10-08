---
title: "Encrypting Linux: LUKS + Veracrypt"
topic: "technical / personal narrative"
data_type: "process (story) + system/structure + data/metrics"
complexity: "moderate"
point_count: 7
source_language: "en"
user_language: "en"
---

## Main Topic
A personal account of how a hack 20+ years ago pushed the author from detecting tampering to preventing it — and the practical setup that resulted: LUKS for the OS, Veracrypt for USB disks, and an rsync backup routine.

## Learning Objectives
After viewing this infographic, the viewer should understand:
1. The journey from detection (tripwire) to prevention (disk encryption).
2. What LUKS and Veracrypt each protect, where they differ, and the key gotchas (header backup, `/boot` cleartext).
3. That encryption protects data at rest only, and is not a backup.

## Target Audience
- **Knowledge Level**: Intermediate — Linux users curious about disk encryption.
- **Context**: Considering encrypting their own disk; wants the shape of a real setup, not a tutorial.
- **Expectations**: The tool choice split, the commands involved, the honest limits.

## Content Type Analysis
- **Data Structure**: A narrative arc (hack → prevention) wrapping a two-tool system (LUKS + Veracrypt) plus a backup routine.
- **Key Relationships**: detection → prevention; LUKS ↔ fixed disk; Veracrypt ↔ removable media; both ↔ "at rest"; rsync ↔ durability.
- **Visual Opportunities**: a timeline/story band, a two-column tool split, big numbers (6.2 GiB/s), command chips, a caution badge.

## Key Data Points (Verbatim)
- "My experience with Linux dates from about 20+ years ago."
- "hacked several times. The tell was `ls` — the listing did not match the files I knew surely were there"
- "LUKS encrypts the entire operating system **except `/boot`**"
- "`aes-xts` 512b at ~6.2 GiB/s"
- "Expect **near-zero** lag on sequential I/O"
- "without AES acceleration the cost jumps to 2–3× or more"
- "`veracrypt -c` walks through volume type (partition vs container file), size, and algorithm"
- "Encryption is not backup: a failed disk or a lost header means total loss."
- "back up the LUKS header — lose it and the data is unrecoverable"

## Layout × Style Signals
- Content type: personal journey + technical system → suggests linear-progression or dense-modules
- Tone: technical but personal, some caution → suggests technical-schematic or pop-laboratory
- Audience: intermediate Linux users → legible, precise, not cute
- Complexity: moderate (7 points) → balanced density

## Design Instructions (from user input)
None specified — skill invoked with the article only.

## Recommended Combinations
1. **dense-modules + pop-laboratory** (Recommended): packs the story, tool split, commands, and numbers into a precise lab-style board.
2. **linear-progression + technical-schematic**: foregrounds the 20-year story arc, engineering blueprint style.
3. **bento-grid + technical-schematic**: clean overview grid of hack → threat model → LUKS → Veracrypt → backup.
4. **binary-comparison + corporate-memphis**: LUKS vs Veracrypt side-by-side (fixed disk vs removable media).
