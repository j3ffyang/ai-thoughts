---
title: "OpenCode Configuration Architecture: AGENTS.md & opencode.jsonc"
topic: "technical"
data_type: "structural-breakdown"
complexity: "complex"
point_count: 8
source_language: "en"
user_language: "en"
---

## Main Topic
A comprehensive architectural blueprint explaining how OpenCode's dual configuration surfaces (`AGENTS.md` instruction context and `opencode.jsonc` machine config) load, interact, resolve precedence, and evaluate permissions across repository boundaries.

## Learning Objectives
After viewing this infographic, the viewer should understand:
1. The dual-surface model: `AGENTS.md` governs model judgment (behavior) while `opencode.jsonc` gates tool execution (permissions).
2. The loading order and precedence mechanisms: upward concatenation for instructions vs. layered override with rule appending for JSONC configs.
3. The permission decision tree: built-in default allow catch-all, wildcard pattern matching, last-matching-rule-wins resolution, and context boundary insulation across submodules.

## Target Audience
- **Knowledge Level**: Intermediate to Advanced developers and AI CLI agent users.
- **Context**: Configuring OpenCode safely across multi-repo, mono-repo, or submodule architectures.
- **Expectations**: Clear visual mental model of how configuration files load, how permissions are evaluated, and how to avoid configuration drift or permission floods.

## Content Type Analysis
- **Data Structure**: Multi-layer system architecture with sequential loading pipelines and decision flows.
- **Key Relationships**: Instructions vs permissions; global symlinks vs project/local configs; parent meta-repo vs child submodule `.git` context walls.
- **Visual Opportunities**:
  - Two parallel pillars for the dual configuration surfaces.
  - Upward/downward directory loading order diagrams.
  - Decision flow / logic tree for permission checks (Allow / Ask / Deny).
  - Context boundary isolation diagram (showing `.git` walls between repos).

## Key Data Points (Verbatim)
- "AGENTS.md files feed Markdown instructions straight into the model's context; opencode.json / opencode.jsonc files hold machine-parsed settings"
- "Instructions shape how the agent judges; the config gates what it may do."
- "AGENTS.md loader reads the global file plus every AGENTS.md it finds walking up from cwd to project root. All load, none override."
- "opencode.jsonc loader reads from low to high priority (global -> project root -> intermediate -> cwd -> .opencode/); later files win on same key, permission rulesets are appended."
- "The built-in default agent rule list begins with a catch-all {action: "*", resource: "*", effect: "allow"}."
- "For a tool call, the matching rule is the last rule whose wildcard pattern matches the action and resource."
- "Aggregation: any deny blocks, otherwise any ask prompts, otherwise allow."
- "Each nested .git acts as a context wall: parent instructions cannot leak down into a sub-repo session."

## Layout × Style Signals
- Content type: System structure, multi-section technical breakdown → suggests `dense-modules` or `bento-grid` or `structural-breakdown`
- Tone: Highly precise, engineering, architectural → suggests `pop-laboratory`, `technical-schematic`, or `retro-pop-grid`
- Audience: Engineers seeking clarity on execution mechanics → suggests clean blueprint/schematic visuals with structured containers
- Complexity: Complex (8 main architectural components) → suggests modular card layout with high visual density

## Recommended Combinations
1. **dense-modules + pop-laboratory** (Recommended): Crisp blueprint grid, coordinate accents, high-density modular cards detailing dual surfaces, loading pipelines, permission evaluation tree, and repository boundary walls.
2. **bento-grid + technical-schematic**: Clean blueprint schematic with dark/light engineering styling, side-by-side comparative pillars, and flowchart nodes.
3. **structural-breakdown + retro-pop-grid**: High-contrast Swiss-grid aesthetic with structured exploded component views and bold visual hierarchy.
