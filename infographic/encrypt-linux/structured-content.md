# Encrypting Linux

## Overview
From a hack 20+ years ago to a working setup: LUKS for the OS, Veracrypt for USB disks, and an rsync backup — plus the honest limits.

## Learning Objectives
The viewer will understand:
1. How a break-in led from detecting tampering to preventing it.
2. What LUKS and Veracrypt each cover, and the key gotchas.
3. That encryption protects data at rest only — and is not a backup.

---

## Section 1: The Hack

**Key Concept**: A break-in long ago turned security into a habit.

**Content**:
- hacked installing over a modem about 20+ years ago
- the tell: `ls` did not match the files that should be there
- `tripwire` baselined hashes of binaries to catch replaced ones

**Visual Element**:
- Type: story caption + small terminal icon
- Subject: a listing that betrays replaced binaries, and a hash baseline
- Treatment: compact, narrative

**Text Labels**:
- Headline: "The Hack That Started It"
- Labels: "hack", "ls lied", "tripwire", "hash baseline"

---

## Section 2: Detect to Prevent

**Key Concept**: Encryption defends data at rest, not a running machine.

**Content**:
- protects: a powered-off or stolen disk
- does not protect: a running, unlocked machine

**Visual Element**:
- Type: two-state diagram (shielded vs open)
- Subject: a disk safe when off, exposed when running
- Treatment: high contrast

**Text Labels**:
- Headline: "Detect to Prevent"
- Labels: "at rest: safe", "unlocked: exposed"

---

## Section 3: LUKS

**Key Concept**: LUKS encrypts the whole OS except `/boot`.

**Content**:
- `/boot` stays cleartext so firmware and bootloader can read it
- the UEFI ESP is FAT32 by specification
- back up the LUKS header, or lose the data; key slots hold several passphrases

**Visual Element**:
- Type: partitioned disk diagram
- Subject: one tiny cleartext boot partition, one large encrypted root
- Treatment: bicolor split

**Text Labels**:
- Headline: "LUKS: the Whole OS"
- Labels: "except /boot", "ESP = FAT32", "header backup", "key slots"

---

## Section 4: cryptsetup

**Key Concept**: The commands that build and protect the encrypted root.

**Content**:
- `luksFormat` builds it; `open` unlocks it; `luksHeaderBackup` saves the header
- `luksFormat` destroys the target partition

**Visual Element**:
- Type: command chip row with a caution badge
- Subject: three monospace chips
- Treatment: caution in the alert color

**Text Labels**:
- Headline: "cryptsetup"
- Labels: "luksFormat", "open", "luksHeaderBackup"

---

## Section 5: Overhead

**Key Concept**: With hardware AES, the cost is negligible.

**Content**:
- `aes-xts` 512b benches at ~6.2 GiB/s
- expect near-zero lag on sequential I/O

**Visual Element**:
- Type: big-number callout
- Subject: one large throughput figure
- Treatment: numeral dominant

**Text Labels**:
- Headline: "Overhead"
- Labels: "~6.2 GiB/s", "near-zero lag", "AES-NI"

---

## Section 6: Veracrypt

**Key Concept**: Veracrypt encrypts partitions and USB disks, applied any time.

**Content**:
- encrypts a partition; used for all USB disks
- `veracrypt -c` creates a volume interactively
- cross-platform containers and hidden volumes

**Visual Element**:
- Type: device + command chip
- Subject: a USB stick beside a create command
- Treatment: compact

**Text Labels**:
- Headline: "Veracrypt: USB & Partitions"
- Labels: "USB disks", "veracrypt -c", "cross-platform"

---

## Section 7: rsync Backup

**Key Concept**: Mirror the LUKS home onto the Veracrypt USB — encryption is not backup.

**Content**:
- daily mirror from the LUKS disk to the Veracrypt USB
- a failed disk or a lost header means total loss

**Visual Element**:
- Type: flow arrow between two disk icons
- Subject: encrypted disk → encrypted USB
- Treatment: one directional arrow

**Text Labels**:
- Headline: "rsync Backup"
- Labels: "rsync -aAXH --delete", "LUKS to Veracrypt USB", "encryption is not backup"

---

## Data Points — REFERENCE ONLY (never copy into the prompt)

### Statistics
- "aes-xts 512b at ~6.2 GiB/s"
- "about 20+ years ago"
- "without AES acceleration the cost jumps to 2–3× or more"

### Key Terms
- **LUKS**: Linux Unified Key Setup.
- **ESP**: EFI System Partition (FAT32).
- **evil-maid**: attacker with brief physical access tampering with boot.

---

## Design Instructions
### Style Preferences
- Technical, precise, slightly cautionary.
### Layout Preferences
- Dense modules; one module per concept.
### Other Requirements
- English; landscape.
