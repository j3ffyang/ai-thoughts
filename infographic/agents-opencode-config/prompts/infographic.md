Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: dense-modules
- **Style**: pop-laboratory
- **Aspect Ratio**: 16:9
- **Language**: English

## Core Principles

- Follow the layout structure precisely for information architecture
- Apply style aesthetics consistently throughout
- Keep information concise, highlight keywords and core concepts
- Maintain high-density structured layout with laboratory coordinate markers, blueprint grids, and sharp visual hierarchy
- No empty filler space: use coordinate badges, technical flow nodes, and precise parameter callouts

## Layout Guidelines (dense-modules)

- High-density modular layout organized into 6 distinct technical modules across a landscape 16:9 canvas
- Coordinate-labeled modules: each card has an alphanumeric technical coordinate (MOD-01, MOD-02, MOD-03, MOD-04, MOD-05, MOD-06)
- Module Archetypes:
  1. MOD-01 (Top-Left): Dual-Pillar Comparison (AGENTS.md vs opencode.jsonc)
  2. MOD-02 (Top-Center): Upward Concatenation Stack (AGENTS.md Loading Flow)
  3. MOD-03 (Top-Right): Priority Ladder & Append Stack (opencode.jsonc Precedence)
  4. MOD-04 (Bottom-Left): Decision Logic Tree (Permission Evaluation Pipeline)
  5. MOD-05 (Bottom-Center): Context Isolation Diagram (.git Submodule Boundaries)
  6. MOD-06 (Bottom-Right): Centralized Symlink Workflow (Single Source of Truth)
- Header zone across top with bold title, system parameters, and coordinate axes
- Hairline borders, precise alignment, and high informational density

## Style Guidelines (pop-laboratory)

- Background: Professional grayish-white with faint blueprint grid texture (#F2F2F2)
- Primary palette: Muted teal/sage green (#B8D8BE) for major functional blocks, charcoal brown/navy (#2D2926) for technical line art
- High-alert accent: Vibrant fluorescent pink / crimson (#E91E63) for Deny / Hard Block highlights and warning markers
- Marker highlights: Vivid lemon yellow (#FFF200) as translucent highlighter effect for key terms
- Visual elements: Coordinate labels on every module (SEC-01, MOD-A, etc.), cross-hair targets, flow arrows, rulers, micro-annotations
- Typography: Bold brutalist headline titles paired with ultra-crisp technical sans-serif annotations

---

Generate the infographic based on the content below:

### Infographic Title & Header
- **Main Title**: OPENCODE CONFIGURATION ARCHITECTURE & PRECEDENCE
- **Subtitle**: AGENTS.md Markdown Context vs opencode.jsonc Gating • Execution & Loading Pipeline Blueprint
- **Metadata**: REV: 2026.08.21 • SPEC: anomalyco/opencode `e11dbd0`

---

### Module 01 [SEC-01 / DUAL-SURFACES]: Two Complementary Configuration Surfaces
- **Concept**: Instructions shape how the agent judges; config gates what it may do.
- **Pillar A (Context)**: `AGENTS.md` → Injected directly into LLM system prompt; guides reasoning & behavior.
- **Pillar B (Gating)**: `opencode.jsonc` → Machine-parsed JSONC settings; gates tool access & execution permissions.
- **Rule**: Neither replaces the other. Format supports JSONC comments & trailing commas.

### Module 02 [SEC-02 / INSTRUCTION-FLOW]: AGENTS.md Upward Loading & Concatenation
- **Concept**: Upward directory traversal where all discovered files load into context and none override another.
- **Loading Stack**:
  1. `~/.config/opencode/AGENTS.md` (Global rules, always first)
  2. `<cwd>/AGENTS.md` (Nearest project file)
  3. `<parent>/AGENTS.md` (Walking upward)
  4. `<project root>/AGENTS.md` (Farthest, rendered last)
- **Rule**: All load, none override. All concatenated into prompt. `OPENCODE_DISABLE_PROJECT_CONFIG=1` skips project files.

### Module 03 [SEC-03 / CONFIG-LADDER]: opencode.jsonc Priority & Appending
- **Concept**: Config keys resolve low-to-high priority (later wins on key); permission rulesets are appended.
- **Priority Ladder (Later Wins)**:
  1. `~/.config/opencode/opencode.jsonc` (Global)
  2. `<project root>/opencode.jsonc` (Project root)
  3. `<cwd>/opencode.jsonc` (Direct file)
  4. `<project root>/.opencode/opencode.jsonc`
  5. `<cwd>/.opencode/opencode.jsonc` (Local - Highest Priority)
- **Key Inspection**: `opencode debug config`

### Module 04 [SEC-04 / PERMISSION-PIPELINE]: Permission Decision Flow & Resolution
- **Concept**: Last matching wildcard rule wins over tool calls, defaulting to silent allow.
- **Evaluation Chain**: `[Built-in Defaults ... Config Rules ... Session Approvals]`
- **Decision Logic**:
  - `Deny` match → [❌ BLOCKED] Hard block (cannot be overridden by session "always").
  - `Ask` match → [⚠️ PROMPT] User choice: once / always / reject.
  - No match / `Allow` → [✅ RUNS] Default catch-all `{action: "*", resource: "*", effect: "allow"}`.
- **Alert**: Ask/Deny after Allow with same prefix shadows it. Keep prefixes disjoint.

### Module 05 [SEC-05 / CONTEXT-WALLS]: Repository Boundaries & Submodule Isolation
- **Concept**: Nested `.git` directories act as context walls preventing instruction leakage.
- **Isolation Topology**:
  - Meta-Repo (`negtivSpace/`): Hub file covers root & space between repos.
  - Context Wall (`.git`): Stop-walk barrier blocks hub rules from leaking down into submodules.
  - Sub-Repos (`ai-thoughts/`, `history/`): Session loads `Global + Sub-repo AGENTS.md`.

### Module 06 [SEC-06 / CENTRAL-WORKFLOW]: Single Source of Truth & Symlink Sync
- **Concept**: Centralized git-versioned config linked to system paths.
- **Symlink Setup**:
  - `~/.config/opencode/opencode.jsonc` → `negtivSpace/opencode/opencode.jsonc`
  - `~/.config/opencode/AGENTS.md` → `negtivSpace/opencode/AGENTS.md`
- **Workflow**: Edit in git repo → Symlink updates instantly → Restart OpenCode → Verify with `opencode debug config`.
- **Trade-off Note**: Centralizing all config & skills in one repository provides simple, unified git sync.

---

Text labels (in English):
- "OPENCODE CONFIGURATION ARCHITECTURE & PRECEDENCE"
- "Dual Configuration Surfaces: Context vs Gating"
- "AGENTS.md Upward Concatenation (All Load • None Override)"
- "opencode.jsonc Priority Ladder (Later Wins • Rules Appended)"
- "Permission Evaluation Pipeline (Last Matching Rule Wins)"
- "Context Walls & Submodule Isolation (.git Boundary)"
- "Single Source of Truth & Symlink Sync"
- "Default Catch-All Allow: {action: '*', resource: '*', effect: 'allow'}"
- "Inspect: opencode debug config"
