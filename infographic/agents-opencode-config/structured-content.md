# OpenCode Configuration Architecture: AGENTS.md & opencode.jsonc

## Overview
OpenCode is configured by two complementary surfaces: Markdown AGENTS.md files feeding instructions into model context, and machine-parsed JSONC configuration gating tool execution permissions.

## Learning Objectives
The viewer will understand:
1. The dual-surface model separating behavioral judgment (`AGENTS.md`) from tool access permissions (`opencode.jsonc`).
2. The exact file loading sequence, directory traversal rules, and precedence mechanics for instructions and configs.
3. The permission decision pipeline (built-in allow catch-all, wildcard matching, last-matching rule wins, ask/deny effects).
4. The context wall behavior of nested `.git` repositories and single-source-of-truth management via symlinks.

---

## Section 1: Dual Configuration Surfaces

**Key Concept**: Instructions shape how the agent judges; the config gates what it may do.

**Content**:
- AGENTS.md: Feeds Markdown instructions straight into the model's system context. Shapes behavior, reasoning, and judgment.
- opencode.jsonc: Machine-parsed JSONC settings (permissions, agents, providers, plugins). Gates tool access and execution.
- Neither surface can fully replace the other — put rules about behavior in AGENTS.md, rules about tool access in the config.
- Both `.json` and `.jsonc` formats accepted with comments and trailing commas.

**Visual Element**:
- Type: Dual-pillar comparative layout
- Left Pillar: "AGENTS.md (Context & Behavior)" with markdown icon, brain/judgment icon.
- Right Pillar: "opencode.jsonc (Gating & Permissions)" with gear/shield icon, JSON key-value icon.
- Treatment: Highlighting complementary non-overlapping domains.

**Text Labels**:
- Headline: "Two Complementary Configuration Surfaces"
- Subhead: "Judgment vs Execution Gating"
- Left Label: "AGENTS.md → Model Context (Behavior)"
- Right Label: "opencode.jsonc → Tool Gating (Permissions)"

---

## Section 2: AGENTS.md Loading & Precedence

**Key Concept**: Concatenative upward loading where all discovered files load into context and none override another.

**Content**:
- The loader reads the global file plus every AGENTS.md walking up from cwd to project root.
- Render order into system prompt:
  1. `~/.config/opencode/AGENTS.md` (Global rules, always first)
  2. `<cwd>/AGENTS.md` (Nearest project file)
  3. `<parent>/AGENTS.md` (Walking upward)
  4. ... (One file per directory)
  5. `<project root>/AGENTS.md` (Farthest, rendered last)
- No override: Because all files load into prompt at once, conflicts are not settled by precedence — the model sees all of them. Keep layers non-contradictory.
- Setting `OPENCODE_DISABLE_PROJECT_CONFIG=1` skips project-file discovery.

**Visual Element**:
- Type: Upward vertical sequence ladder / stack diagram
- Flow: Step 1 (Global at top) -> Step 2 (CWD) -> Step 3 (Parent) -> Step 5 (Root at bottom)
- Treatment: Visual stack with curly bracket indicating "All concatenated into System Prompt".

**Text Labels**:
- Headline: "AGENTS.md Upward Concatenation"
- Subhead: "All Load • None Override"
- Labels: "1. Global (`~/.config/opencode/`)", "2. `<cwd>/AGENTS.md`", "3. `<parent>/AGENTS.md`", "4. `<project root>/AGENTS.md`", "Result: Concatenated into Context"

---

## Section 3: opencode.jsonc Priority & Ruleset Appending

**Key Concept**: Config documents resolve low-to-high priority (later wins on key), while permission rulesets are appended.

**Content**:
- Priority order (lowest to highest, later wins on key):
  1. `~/.config/opencode/opencode.jsonc` (Global)
  2. `<project root>/opencode.jsonc` (Project root)
  3. `<intermediate dirs>/opencode.jsonc`
  4. `<cwd>/opencode.jsonc`
  5. `<project root>/.opencode/opencode.jsonc`
  6. `<cwd>/.opencode/opencode.jsonc` (Local, highest priority)
- Ruleset Appending: Permission rulesets are appended rather than replaced — global rules and local rules all stay live.
- Verification command: `opencode debug config` inspects resolved output.

**Visual Element**:
- Type: Layered priority pyramid / ladder with append indicator
- Flow: Global (Base / lowest) -> Project Root -> CWD -> `.opencode/` Local (Peak / highest)
- Treatment: Side callout badge: "Keys: Later Wins | Permission Rules: Appended".

**Text Labels**:
- Headline: "opencode.jsonc Priority Ladder"
- Subhead: "Layered Keys + Appended Permission Rules"
- Labels: "Global (Lowest)", "Project Root", "CWD", "Local .opencode/ (Highest Priority)", "Inspect: opencode debug config"

---

## Section 4: Permission Decision Pipeline & Evaluation

**Key Concept**: "Last matching wildcard rule wins" over evaluated tool calls with built-in default allow.

**Content**:
- Evaluated chain: `[built-in defaults ... config rules ... saved per-session approvals]`
- Built-in default starts with `{action: "*", resource: "*", effect: "allow"}`.
- Unmatched commands run silently under default allow.
- Wildcard resolution: `*` matches any characters, `?` exactly one.
- Aggregation rules:
  - Any deny blocks → BLOCKED (hard pre-check, no override).
  - Any ask prompts → PROMPT (once / always / reject).
  - Otherwise → RUNS (allow).
- Warning: An ask/deny written AFTER an allow with the same prefix shadows it. Keep prefixes disjoint.

**Visual Element**:
- Type: Decision tree / logic flowchart
- Nodes:
  - Input: Tool Call `(action, resource)`
  - Step 1: Match against `[Defaults + Config Rules + Session Approvals]`
  - Decision Branch:
    - `Deny` match → ❌ BLOCKED (Hard block)
    - `Ask` match → ⚠️ PROMPT (Once / Always / Reject)
    - No match / `Allow` → ✅ RUNS (Catch-all Allow)

**Text Labels**:
- Headline: "Permission Evaluation Pipeline"
- Subhead: "Last Matching Rule Wins • Default Catch-All Allow"
- Labels: "Tool Call (action, resource)", "Rule Chain Evaluation", "Deny → Blocked", "Ask → Prompt User", "Allow / No Match → Silent Allow"

---

## Section 5: Repository Context Walls & Submodule Topology

**Key Concept**: Nested `.git` directories act as context walls preventing instruction leakage.

**Content**:
- The loader stops walking upward at each project root (nearest `.git`).
- Submodule isolation: Sessions inside `ai-thoughts/` or `history/` get global + that repo's AGENTS.md.
- Meta-repo hub file (`negtivSpace/AGENTS.md`) is a sibling, not a middle layer — instructions cannot leak down into submodules.
- Placement rule: Put universal rules in global (`~/.config/opencode/`), hub-only workflows in meta-repo, and repo-specific rules in sub-repo.

**Visual Element**:
- Type: Architectural boundary diagram / container box schematic
- Diagram:
  - Outer Box: Meta-repo (`negtivSpace`) with `negtivSpace/AGENTS.md`
  - Context Wall: Heavy brick/shield border marked `.git boundary (Stop Walk)`
  - Inner Box 1: `ai-thoughts/` with its own `.git` and `AGENTS.md`
  - Inner Box 2: `history/` with its own `.git` and `AGENTS.md`
  - Arrow: Global `~/.config/opencode/` injects into all boxes universally.

**Text Labels**:
- Headline: "Repository Context Walls (.git Isolation)"
- Subhead: "No Upward Instruction Leakage Across Submodules"
- Labels: "Global (~/.config/opencode/)", "Meta-Repo (Hub)", "Context Wall (.git)", "Sub-Repo A (ai-thoughts)", "Sub-Repo B (history)"

---

## Section 6: Workflow & Centralized Source of Truth

**Key Concept**: Centralized single source of truth versioned via git, with symlinks wiring into OpenCode.

**Content**:
- Global configuration files are git-managed symlinks into `negtivSpace/opencode/`:
  - `~/.config/opencode/opencode.jsonc` → `negtivSpace/opencode/opencode.jsonc`
  - `~/.config/opencode/AGENTS.md` → `negtivSpace/opencode/AGENTS.md`
- Workflow steps:
  1. Edit config in repository (single source of truth).
  2. Restart opencode session.
  3. Verify with `opencode debug config`.
- Centralization Trade-off: Centralizing `AGENTS.md`, `opencode.jsonc`, and skills in one managed place provides simple, unified git sync across machines.

**Visual Element**:
- Type: Workflow loop & symlink mapping diagram
- Flow: Git Repo Source → Symlink Mapping (`~/.config/opencode/`) → OpenCode Runtime Engine → Restart & Verify Loop

**Text Labels**:
- Headline: "Centralized Management & Symlink Workflow"
- Subhead: "Single Source of Truth • Git-Managed • Symlinked"
- Labels: "1. Edit Repo Config", "2. Symlink Distribution", "3. Restart Session", "4. Verify with debug config"

---

## Data Points (Verbatim)

### Key Rules & Facts
- "AGENTS.md files feed Markdown instructions straight into the model's context; opencode.json / opencode.jsonc files hold machine-parsed settings."
- "Instructions shape how the agent judges; the config gates what it may do."
- "All load, none override: Concatenated into the system prompt."
- "The built-in default agent rule list begins with a catch-all {action: "*", resource: "*", effect: "allow"}."
- "For a tool call, the matching rule is the last rule whose wildcard pattern matches the action and resource."
- "Aggregation across resources: any deny blocks, otherwise any ask prompts, otherwise allow."
- "Each nested .git acts as a context wall: parent instructions cannot leak down into a sub-repo session."

---

## Design Instructions

### Style Preferences
- **Palette**: Clean blueprint & laboratory tones (deep navy/slate background, cyan/teal accent lines, crisp white labels, warning amber for ask, crimson for deny, emerald green for allow).
- **Aesthetic**: Modern technical schematic / pop laboratory engineering poster.
- **Structure**: High-density 6-card modular arrangement with clear section containers, flow arrows, and visual hierarchy.
