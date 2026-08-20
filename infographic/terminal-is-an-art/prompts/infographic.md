Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: bento-grid
- **Style**: craft-handmade
- **Aspect Ratio**: 16:9
- **Language**: en

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
- Use English for all text content

## Layout Guidelines

Modular grid layout with varied cell sizes, like a bento box.

Structure:
- Grid of rectangular cells
- Mixed cell sizes (1x1, 2x1, 1x2, 2x2)
- No strict symmetry required
- Hero cell for main point
- Supporting cells around it

Best for: Multiple topic overview, feature highlights, dashboard summaries

Visual Elements:
- Clear cell boundaries
- Varied cell backgrounds
- Icons or illustrations per cell
- Consistent padding/margins
- Visual hierarchy through size

Text Placement:
- Main title at top
- Cell titles within each cell
- Brief content per cell
- Minimal text, maximum visual
- CTA or summary in prominent cell

## Style Guidelines

Hand-drawn and paper craft aesthetic with warm, organic feel.

Color Palette:
- Primary: Warm pastels, soft saturated colors, craft paper tones
- Background: Light cream (#FFF8F0), textured paper (#F5F0E6)
- Accents: Bold highlights, construction paper colors

Visual Elements:
- Hand-drawn or cut-paper quality
- Organic, slightly imperfect shapes
- Layered depth with shadows (paper variant)
- Simple cartoon elements and icons
- Character illustrations (people, personalities in cartoon form)
- Ample whitespace, clean composition
- Keywords and core concepts highlighted
- Strictly hand-drawn — no realistic or photographic elements

Style Enforcement:
- All imagery must maintain cartoon/illustrated aesthetic
- Replace real photos or realistic figures with hand-drawn equivalents
- Maintain consistent line weight and illustration style throughout

Typography:
- Hand-drawn or casual font style
- Clear, readable labels
- Keywords emphasized with larger/bolder text
- Cut-out letter style for paper variant

---

Generate the infographic based on the content below:

# The Terminal Is an Art — Structured Content

## Overview
A visual summary of a personal essay arguing the terminal is computing's closest thing to an art form — nine sections covering simplicity, directness, honesty, power, workflow, universality, AI agents, understanding, and aesthetic beauty.

## Learning Objectives
The viewer will understand:
1. The nine qualities that make the terminal enduringly powerful
2. Why the terminal outperforms GUIs in speed, transparency, and self-sufficiency
3. How the terminal has evolved to host AI agents without losing its essence

---

## Section 1: Simple

**Key Concept**: The terminal is the simplest interface — a prompt, a cursor, one line of input.

**Content**:
- A prompt, a blinking cursor, and one line of input
- No windows, no panels, no ribbons, no onboarding tour
- Starts from almost nothing and grows only with what you add
- Runs anywhere, on anything — even a fifteen-year-old laptop
- "No setup, no configuration, no tutorial needed"

**Visual Element**:
- Type: Terminal window illustration
- Subject: Minimal terminal with prompt and blinking cursor
- Treatment: Clean, empty terminal — negative space as design

**Text Labels**:
- Headline: "Simple"
- Subhead: "Starts from almost nothing"
- Labels: "echo hello", "date", "whoami"

---

## Section 2: Direct

**Key Concept**: Command in, result out — the gap between wanting and doing is one keystroke.

**Content**:
- `ls`, `cp`, `git commit -m "..."` — command in, result out
- `ssh user@host` — connect to a server
- `chmod 755 script.sh` — change permissions
- `mkdir -p path/to/dir` — create directories with parents
- "No menus to navigate, no settings to hunt for"

**Visual Element**:
- Type: Command → result flow diagram
- Subject: Arrow from command input to output
- Treatment: Simple directional flow

**Text Labels**:
- Headline: "Direct"
- Subhead: "One keystroke from intent to action"
- Labels: "command in, result out"

---

## Section 3: Honest & Transparent

**Key Concept**: Errors straight in your face — no polite wrapper, no vague apology.

**Content**:
- `command not found`, `No such file or directory`, `Permission denied`
- "It tells you exactly what went wrong — no polite wrapper, no vague apology"
- `dmesg` — kernel's own log
- `strace` — traces every system call
- `journalctl -e` — what systemd did and when
- "No GUI offers that level of honesty"

**Visual Element**:
- Type: Terminal error message box
- Subject: Error messages displayed raw
- Treatment: Red/warning colored text on dark terminal

**Text Labels**:
- Headline: "Honest & Transparent"
- Subhead: "Raw truth, no filter"
- Labels: "command not found", "Permission denied"

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
- Chain `cat`, `sort`, `uniq -c`, `head` — an analytics tool no vendor ships

**Visual Element**:
- Type: Pipeline diagram
- Subject: Pipe chain flowing left to right
- Treatment: Connected boxes showing data flow through commands

**Text Labels**:
- Headline: "Powerful"
- Subhead: "Compose your own tools"
- Labels: "grep | sort | uniq -c | head"

---

## Section 5: Workflow

**Key Concept**: Every step is visible, re-runnable, and scriptable — a terminal workflow lives in a file and lasts forever.

**Content**:
- `make`, `test`, `deploy` — the whole pipeline in plain text
- `crontab -e` — schedule a task for 3 AM
- `systemctl status` — whether your service is alive
- `make -j4` — build in parallel
- "A shell script: one file, one command, the entire pipeline runs"
- "A GUI workflow lives in your muscle memory; a terminal workflow lives in a file"

**Visual Element**:
- Type: Pipeline flow (make → test → deploy)
- Subject: Sequential steps with arrows
- Treatment: Linear progression with checkpoints

**Text Labels**:
- Headline: "Workflow"
- Subhead: "Visible, scriptable, lasting"
- Labels: "make → test → deploy"

---

## Section 6: Universal

**Key Concept**: Same commands across every distro, shell, and fifty years — plus the terminal needs almost nothing around it.

**Content**:
- Arch, Debian, bash, zsh, fish — the commands are the same
- `ls`, `cd`, `grep`, `cat` — since Unix was born, fifty years ago
- "A command I type today would work on a system from 1975"
- SSH — distance and hardware disappear
- `iwctl` during Arch install — skill investment pays back
- "No VPN client, no middle-man app, no Tailscale tunnel — the terminal *is* the network layer"
- "I live in vim — no VS Code, no Cursor, no Electron wrapper eating four gigs of RAM"

**Visual Element**:
- Type: Circular diagram showing distros/shells orbiting a central terminal
- Subject: Multiple environments, one set of commands
- Treatment: Hub with spokes to distro/shell names

**Text Labels**:
- Headline: "Universal"
- Subhead: "50 years, same commands"
- Labels: "Arch", "Debian", "bash", "zsh", "fish", "SSH", "vim"

---

## Section 7: The Terminal and the Agent

**Key Concept**: The terminal is the natural interface for AI agents — full access, full control, no walled garden.

**Content**:
- "An agent needs to read output, run commands, see results, and iterate — that's the shell"
- "Two minds, one prompt, taking turns"
- Browser agent: sandboxed, limited to web pages and APIs someone else designed
- Desktop app: proprietary interface you can't inspect or extend
- Terminal agent: full access to filesystem, shell, commands — "your environment, not a walled garden"
- Modern terminal emulators accept images dragged right into the window
- "The terminal didn't need a redesign to host AI. The prompt was already the perfect interface."

**Visual Element**:
- Type: Comparison diagram — terminal agent vs. browser/GUI agent
- Subject: Left side: terminal with agent prompt; Right side: browser sandbox / desktop app wrapper
- Treatment: Split comparison, terminal side open and expansive, browser/GUI side boxed and constrained

**Text Labels**:
- Headline: "The Terminal and the Agent"
- Subhead: "Two minds, one prompt"
- Labels: "terminal agent", "browser agent", "desktop agent", "full access", "sandboxed"

---

## Section 8: Understanding

**Key Concept**: The terminal demystified the computer — the machine stopped being a black box.

**Content**:
- "Files, processes, pipes, permissions — I learned them by looking, not by clicking through menus"
- "When a GUI broke, I was lost; when the terminal broke, I could read the error and fix it"
- instguid — shell tips documented since 2000, started on AIX, grew to cover Linux
- "I understand my systems in a way GUI usage alone never teaches"

**Visual Element**:
- Type: Open terminal revealing internal system components
- Subject: Terminal as window into files, processes, permissions
- Treatment: Transparent/layered view showing what's underneath

**Text Labels**:
- Headline: "Understanding"
- Subhead: "The machine stops being a black box"
- Labels: "files", "processes", "pipes", "permissions", "instguid (since 2000)"

---

## Section 9: Art & Aesthetic

**Key Concept**: Beauty of negative space — craft, ritual, and the Unix philosophy as aesthetic principle.

**Content**:
- "Decoration isn't art"
- "Beauty of negative space — monospace fonts, blank lines that breathe, a cursor that waits"
- Unix philosophy: "do one thing and do it well" — not just engineering, aesthetic
- Pipe chain `cat log | grep error | sort | uniq -c` — "a small composition"
- Ritual: mechanical keyboard, `cd ~/projects && git pull`, green-on-black glow at 2 AM
- "Simple, direct, honest, powerful, universal, and still growing"
- "I still think of the command line not as a tool but as a craft"

**Visual Element**:
- Type: Laptop with terminal showing pipe chain, mechanical keyboard nearby
- Subject: The aesthetic experience of using a terminal
- Treatment: Warm, atmospheric — 2 AM glow, craft feel

**Text Labels**:
- Headline: "Art & Aesthetic"
- Subhead: "Craft made visible"
- Labels: "cat | grep | sort | uniq -c", "cd ~/projects && git pull", "2 AM"

---

## Data Points (Verbatim)

### Statistics
- "almost thirty years" of using Unix/Linux
- "fifty years" since Unix was born
- "a command I type today would work on a system from 1975"
- "four gigs of RAM" (Electron overhead)
- "instguid" — notes since 2000

### Key Quotes
- "The closest thing to an art form this industry ever produced"
- "The gap between wanting and doing is one keystroke"
- "The terminal hands you the raw truth and trusts you to read it"
- "The terminal scales with your imagination, not with the version number"
- "A GUI workflow lives in your muscle memory and dies with your patience; a terminal workflow lives in a file and lasts forever"
- "Two minds, one prompt, taking turns"
- "The terminal didn't need a redesign to host AI. The prompt was already the perfect interface."
- "Simple, direct, honest, powerful, universal, and still growing"

### Key Terms
- **pipe**: Chains commands together — cat | grep | sort | uniq -c
- **SSH**: Secure Shell — connects to remote machines, replaces VPN/Tailscale
- **TUI**: Text User Interface — terminal-based interface
- **bloatware**: Unwanted pre-installed software

---

Text labels (in en):
- Main Title: "The Terminal Is an Art"
- Section 1: "Simple" / "Starts from almost nothing"
- Section 2: "Direct" / "One keystroke from intent to action"
- Section 3: "Honest & Transparent" / "Raw truth, no filter"
- Section 4: "Powerful" / "Compose your own tools"
- Section 5: "Workflow" / "Visible, scriptable, lasting"
- Section 6: "Universal" / "50 years, same commands"
- Section 7: "The Terminal and the Agent" / "Two minds, one prompt"
- Section 8: "Understanding" / "The machine stops being a black box"
- Section 9: "Art & Aesthetic" / "Craft made visible"
- Footer: "btw, i use arch "
- Author note: "almost thirty years on Unix/Linux"
