# CRITICAL: Text Accuracy

Render these exact strings correctly in the image — every one must appear spelled exactly as written. Misspelled, doubled, or garbled text is a failure. Prefer fewer labels over tiny, wrong text:

- Title: "Happy Birthday Linux — From AIX to Arch" (note: "Linux", "AIX"; the em dash "—" between "Linux" and "From")
- Hook: "35 years. I was there for most of them."
- "AIX"
- "1998" (milestone year, not "1999")
- "IBM Toronto"
- "2000"
- "got hacked"
- "security became a habit"
- "distro hopping" or "the distro years"
- "Manjaro" … "Arch"
- "VMs, Cloud, Kubernetes"
- "Proton"
- "all Arch Linux"
- "btw, i use arch"

Pitfalls to avoid:
- "AIX" must not become "AI", "AXI", or "A1X"
- "Arch" must not become "Archi", "Aach", or "March"
- "Proton" must not become "Protonn" or "Proton?"
- The em dash in the title must render — not a hyphen, not a slash
- No doubled words anywhere ("the the", "Linux Linux")
- Prefer dropping a non-essential label over shrinking font size until it garbles

---

Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: winding-roadmap
- **Style**: storybook-watercolor
- **Aspect Ratio**: 16:9
- **Language**: English

## Core Principles

- Follow the layout structure precisely for information architecture
- Apply style aesthetics consistently throughout
- Keep information concise, highlight keywords and core concepts
- Use ample whitespace for visual clarity
- Maintain clear visual hierarchy
- This is a warm personal memoir tribute, not a corporate chart — keep it nostalgic and joyful

## Text Requirements

- All text must match the specified style treatment
- Main title should be prominent and readable (hand-lettered style)
- Key concepts should be visually emphasized
- Milestone labels should be clear and appropriately sized
- Use the English language for all text content
- Exact strings in the Text Accuracy block are non-negotiable

## Layout Guidelines

Winding-roadmap:
- An S-curve or winding path spanning the canvas left-to-right (landscape)
- Milestone markers/flags along the path, each with a short label and year
- Start point on the left, destination landmark on the right
- Small scene elements beside the path (icons: a server/terminal, a lock for security, a game controller, a container, a text editor)
- Progress indicators connecting the milestones
- Title at the top; hook line as a subtitle; destination description at the end
- 7-9 milestone stops; the road travels from "AIX" toward "Arch"

## Style Guidelines

storybook-watercolor:
- Soft hand-painted illustration with whimsical charm
- Muted blues, greens, warm earth tones; watercolor washes
- Background: cream watercolor-paper texture
- Visible brushstrokes, soft color bleeds, gentle splatter accents
- Delicate line work over washes; organic shapes
- Elegant hand-lettering for titles; flowing letterforms
- Dreamy, atmospheric, warm and nostalgic quality

---

Generate the infographic based on the content below:

## Narrative Arc

- **Start (early 90s)**: IBM — "first learned that AIX existed"
- **1998**: Met Linux — a teammate off "to try Linux for fun"
- **2000**: IBM Toronto — "I got hacked while installing over modem in 2000, several times"; then encryption (`veracrypt`, `luks`), `openssh`, firewalls (`ipchains` kernel 2.2 → `iptables` kernel 2.4+)
- **Security habit**: "From then on, security became a habit" — encryption, no remote session without ssh; paid off later in cloud computing
- **The Distro Years**: Fedora → Ubuntu → Debian → Manjaro → CachyOS → Arch; "SteamOS lasted only 1 day"
- **The Stack**: minimal desktop; "`terminator` for almost 20 years", now `kitty`; `pacman` + `yay`
- **VMs → Cloud → Kubernetes**: VMware, Xen, KVM/OpenStack; "almost everything runs on Linux"
- **Games on Linux**: "In 2024 … I tried Steam on Linux" — "Proton, the emulator, works perfectly on Linux with Arch"
- **Destination — All Arch Linux**: 4 machines, "they're all Arch Linux" — "btw, i use arch"

## Milestone Stops (label text)

1. "AIX" (IBM, early 90s)
2. "met Linux" (1998)
3. "got hacked" (2000)
4. "security became a habit"
5. "the distro years" (Fedora → Arch)
6. "the stack" (terminal + pacman)
7. "VMs, Cloud, Kubernetes"
8. "Proton" (games, 2024)
9. "all Arch Linux" (destination)