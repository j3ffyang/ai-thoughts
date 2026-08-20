Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: bento-grid
- **Style**: morandi-journal
- **Aspect Ratio**: 16:9
- **Language**: English

## Core Principles

- Follow the layout structure precisely for information architecture
- Apply style aesthetics consistently throughout
- If content involves sensitive or copyrighted figures, create stylistically similar alternatives
- Keep information concise, highlight keywords and core concepts
- Use ample whitespace for visual clarity
- Maintain clear visual hierarchy

## Text Requirements

- All text must match the specified style treatment
- Main titles should be prominent and readable
- Key concepts should be visually emphasized
- Labels should be clear and appropriately sized
- Use the specified language for all text content

## Layout Guidelines (bento-grid)

Modular grid layout with varied cell sizes, like a bento box.
- Grid of rectangular cells
- Mixed cell sizes (1x1, 2x1, 1x2, 2x2)
- No strict symmetry required
- Hero cell for main point
- Supporting cells around it
- Clear cell boundaries
- Varied cell backgrounds
- Icons or illustrations per cell
- Consistent padding/margins
- Visual hierarchy through size
- Main title at top
- Cell titles within each cell
- Brief content per cell
- Minimal text, maximum visual

## Style Guidelines (morandi-journal)

Hand-drawn doodle illustration with warm Morandi color tones and cozy bullet journal aesthetic.

**Color Palette**:
- Background: Warm cream/beige with subtle paper texture (#F5F0E6)
- Primary: Muted teal/sage green (#7BA3A8) for headers and frames
- Secondary: Warm terracotta/orange (#D4956A) for highlights and numbers
- Line art: Dark charcoal brown (#4A4540)
- Soft highlights: Pale yellow (#F5E6C8)

**Visual Elements**:
- Hand-drawn doodle illustrations with organic, slightly imperfect ink lines
- Washi tape strip decorations (diagonal stripes pattern, beige and brown)
- Rounded card containers for brand/option items
- Hand-drawn rulers, scales, and progress bars with emoji quality indicators
- Dotted line frames around sections
- Connecting arrows and dotted lines between modules
- Corner decorations: tiny houses, stars, sparkles, clouds
- Wavy line dividers between sections
- Callout bubbles for tips

**Typography**:
- Main title: Bold hand-lettered calligraphy style with decorative flourishes
- Module headers: Clean handwritten text in white on dark teal rounded badge (#6B9080)
- Body text: Neat handwritten print style, easy to read
- Numbers: Highlighted in terracotta (#D4956A), slightly larger than body

**Style Enforcement**:
- All imagery must maintain hand-drawn/doodle aesthetic—no digital precision
- Organic, slightly imperfect shapes throughout
- Sketch-like quality with visible line weight variations
- Warm and cozy journal feel, not clinical or corporate

**Avoid**:
- Flat vector icons or emoji
- Clean geometric shapes
- Stock illustration style
- Strict grid layout
- Pure white background
- Digital/corporate look

---

Generate the infographic based on the content below:

# The Terminal Is an Art

## Overview
A personal essay arguing that the Unix/Linux terminal is the closest thing to an art form in computing — built on simplicity, directness, honesty, power, workflow, universality, and the deep understanding it provides.

## Learning Objectives
The viewer will understand:
1. The seven core qualities that make the terminal exceptional
2. Why the terminal's 50-year design philosophy rewards long-term investment
3. How simple commands compose into powerful tools through transparency

---

## Section 1: Simple

**Key Concept**: The terminal has no bloat by definition — there's nothing there to bloat.

**Content**:
- A prompt, a blinking cursor, and one line of input
- No windows, no panels, no ribbons, no onboarding tour
- Runs anywhere, on anything — even a fifteen-year-old laptop
- "Type `echo hello`, `date`, `whoami` — and the computer answers"

**Visual Element**:
- Type: illustration
- Subject: minimal terminal window with blinking cursor, no chrome
- Treatment: clean, white space, single focal point

**Text Labels**:
- Headline: "Simple"
- Subhead: "No bloat by definition"
- Commands: `echo`, `date`, `whoami`

---

## Section 2: Direct

**Key Concept**: The gap between wanting and doing is one keystroke.

**Content**:
- `ls`, `cp`, `git commit -m "..."` — command in, result out
- `ssh user@host` — connect to a server
- `chmod 755 script.sh` — change permissions
- `mkdir -p path/to/dir` — create directories

**Visual Element**:
- Type: icon set
- Subject: command → result arrow
- Treatment: one-directional flow, immediate

**Text Labels**:
- Headline: "Direct"
- Subhead: "One keystroke from intent to action"
- Commands: `ls`, `cp`, `git`, `ssh`, `chmod`, `mkdir -p`

---

## Section 3: Honest and Transparent

**Key Concept**: The terminal never hides the truth — errors and output are unfiltered.

**Content**:
- `command not found` / `No such file or directory` / `Permission denied`
- No middle-man handling output and logs
- `dmesg` — kernel's own log
- `strace` — traces every system call
- `journalctl -e` — what systemd did and when

**Visual Element**:
- Type: illustration
- Subject: terminal showing raw error output
- Treatment: direct, unpolished, real

**Text Labels**:
- Headline: "Honest & Transparent"
- Subhead: "Raw truth, no filter"
- Commands: `dmesg`, `strace`, `journalctl -e`

---

## Section 4: Powerful

**Key Concept**: One line replaces a whole application — the pipe is the real superpower.

**Content**:
- `grep` a million-line log
- `rsync` a directory across the network
- `ffmpeg` transcode a video
- `awk` reshapes columns of data
- `sed` transforms text in place
- `find . -name "*.md" | xargs wc -l` — counts every line

**Visual Element**:
- Type: pipe chain diagram
- Subject: multiple commands flowing through pipes
- Treatment: compositional, building momentum

**Text Labels**:
- Headline: "Powerful"
- Subhead: "Compose your own tools"
- Commands: `grep`, `rsync`, `ffmpeg`, `awk`, `sed`, `find`, `xargs`

---

## Section 5: Workflow

**Key Concept**: Every step is visible, re-runnable, and scriptable.

**Content**:
- `make`, `test`, `deploy` — the whole pipeline in plain text
- `crontab -e` — schedule a task for 3 AM
- `systemctl status` — whether your service is alive
- `make -j4` — build in parallel
- A shell script: one file, one command, the entire pipeline runs

**Visual Element**:
- Type: flowchart
- Subject: make → test → deploy pipeline
- Treatment: linear, visible steps, scriptable

**Text Labels**:
- Headline: "Workflow"
- Subhead: "Visible, scriptable, lasting"
- Commands: `make`, `test`, `deploy`, `crontab`, `systemctl`

---

## Section 6: Universal

**Key Concept**: Same commands, same architecture, across every distro, shell, and fifty years of stability.

**Content**:
- Arch, Debian, bash, zsh, fish — the commands are the same
- Debian's design philosophy: free, community-built, available to everyone
- SSH — distance and hardware disappear
- `ls`, `cd`, `grep`, `cat` — since Unix was born, fifty years ago
- `iwctl` in a text UI during Arch install — skill investment pays back

**Visual Element**:
- Type: icon set / world
- Subject: multiple distros/shells radiating from shared terminal core
- Treatment: universal, connected, timeless

**Text Labels**:
- Headline: "Universal"
- Subhead: "50 years, same commands"
- Commands: `ls`, `cd`, `grep`, `cat`, `iwctl`

---

## Section 7: Understanding

**Key Concept**: The terminal demystified the computer — files, processes, pipes, permissions learned by looking.

**Content**:
- "When a GUI broke, I was lost; when the terminal broke, I could read the error and fix it"
- "The machine stopped being a black box"
- instguid — shell tips documented since 2000, started on AIX, grew to cover Linux
- "Commands learned twenty-five years ago still work today"

**Visual Element**:
- Type: illustration
- Subject: person at terminal, computer becoming transparent
- Treatment: revelatory, deepening

**Text Labels**:
- Headline: "Understanding"
- Subhead: "The machine stops being a black box"
- Reference: instguid (2000–present)

---

## Section 8: Art and Aesthetic

**Key Concept**: The terminal's beauty is negative space and craft — do one thing and do it well is an aesthetic principle.

**Content**:
- Monospace fonts, blank lines that breathe, a cursor that waits
- Unix philosophy as aesthetic: `cat log | grep error | sort | uniq -c`
- The ritual: mechanical keyboard, `cd ~/projects && git pull`, green-on-black glow at 2 AM
- "Simple, direct, honest, powerful, and universal — built once, fifty years ago"

**Visual Element**:
- Type: atmospheric illustration
- Subject: terminal at 2 AM, green-on-black glow
- Treatment: ritualistic, almost musical

**Text Labels**:
- Headline: "Art & Aesthetic"
- Subhead: "Craft made visible"
- Pipe example: `cat | grep | sort | uniq -c`

---

## Data Points (Verbatim)

### Key Facts
- "almost thirty years" — author's experience
- "fifty years" — Unix's age
- "2000" — instguid documentation start
- "twenty-five years" — commands learned timeline
- "almost three decades" — career span

### Commands Referenced
- Getting started: `echo`, `date`, `whoami`
- File & directory: `ls`, `cp`, `mv`, `mkdir -p`, `chmod`, `touch`
- Search & text: `grep`, `awk`, `sed`, `find`, `xargs`, `sort`, `uniq`, `cut`, `head`, `wc`
- Networking: `ssh`, `wget`, `rsync`, `iwctl`
- System: `dmesg`, `strace`, `journalctl`, `systemctl`, `crontab`, `make`, `ps`
- Media: `ffmpeg`
- Version control: `git`

### Quotes
- "The terminal is the one tool that never gets in the way, never hides the truth, never adds what you didn't ask for."
- "The most reliable interface in computing is also the oldest."
- "After almost three decades, I still think of the command line not as a tool but as a craft — and that's the closest thing to art I know."

---

## Design Instructions

### Style Preferences
- Warm, personal tone — not corporate or clinical
- Hand-drawn or journal-like aesthetic
- Green-on-black terminal color accent

### Layout Preferences
- Bento grid for 8 sections
- Each section clearly separated
- Command examples as small, readable text

### Other Requirements
- Include Arch sign-off: "btw, i use arch" with glyph
- Include instguid reference

Text labels (in English):
- Title: "The Terminal Is an Art"
- Section headlines: "Simple", "Direct", "Honest & Transparent", "Powerful", "Workflow", "Universal", "Understanding", "Art & Aesthetic"
- Closing: "btw, i use arch"
