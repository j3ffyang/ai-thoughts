# J3ffyang's Portfolio

Building **AI-powered automation skills**, **productivity tools**, and **knowledge systems** for individual developers and AI-native workflows.

---

## 🎯 What I Do

I create **production-ready automation skills** across multiple AI platforms (OpenCode, Hermes, OpenClaw, Claude), focusing on:

- **Skill-based AI orchestration** — turning workflows into reusable, composable skills
- **Multilingual content automation** — English ↔ Chinese/Traditional Chinese
- **Developer productivity tools** — Chrome extensions, CLI utilities, API integrations
- **AI platform experimentation** — deeply hands-on with OpenCode, Hermes, OpenClaw, Claude, and OpenRouter

All code prioritizes **clarity over cleverness**: simple, readable, portable, and easy to fork.

---

## 📦 Main Repositories

### AI Skills (by platform)

**⚡ OpenCode — the growing collection, auto-published to ClawHub**

My OpenCode skills live in `ai-thoughts/.opencode/skills/` and publish to [ClawHub](https://clawhub.ai/j3ffyang) automatically on every push — no local installs, one owner account. The collection is growing fastest here:

- **`astro-sync`** — convert & polish an article into an AstroPaper post for the astro_journal blog (everbox.io), images included
- **`resize-for-banner`** — 16:9 (LinkedIn) / 5:2 (X) social banners, padded black, never cropped, never overwrites the source
- **`translate-to-chn`** — translate an article into Simplified Chinese as a `-chn.md` twin

| Platform | Repo | Purpose | Latest | Status |
|----------|------|---------|--------|--------|
| **OpenCode** ⚡ | **[ai-thoughts/.opencode/skills](https://github.com/negtivspace/ai-thoughts/tree/main/.opencode/skills)** | [`astro-sync`](https://clawhub.ai/j3ffyang) (article → AstroPaper post for everbox.io, images included), [`resize-for-banner`](https://clawhub.ai/j3ffyang) (16:9 / 5:2 social banners, padded never cropped), [`translate-to-chn`](https://clawhub.ai/j3ffyang) (article → Simplified Chinese `-chn.md` twin). Auto-published to ClawHub on every push. | `add auto-wrap tool` (Aug 2026) | 🔄 Active |
| **Hermes** ⚕ | **[hermes-custom-skills](https://github.com/negtivspace/hermes-custom-skills)** | Specialized skills for [Hermes Agent](https://hermes.ai) — autonomous workflows, content generation, task orchestration. | `docs: add README and CONTRIBUTING` (Jul 2026) | 🔄 Active |
| **OpenClaw** 🦞 | **[openclaw-custom-skills](https://github.com/negtivspace/openclaw-custom-skills)** | Production skills for [OpenClaw](https://openclaw.ai) published to ClawHub. Multilingual blog publishing, media generation. | `add chinese edition` (Jul 2026) | 🔄 Active |
| **Claude Code** | **[claude-custom-skills](https://github.com/negtivspace/claude-custom-skills)** | Automation skills for [Claude Code](https://claude.ai) — productivity hacks, data export, content workflows. | `add i18n support to README` (Jul 2026) | ✨ Stable |
| **Multi-platform** | **[ai-custom-skills](https://github.com/negtivspace/ai-custom-skills)** | Production-ready skills across platforms (Claude Code, Hermes, OpenClaw) — content creation, data export, workflow automation. | `add new skill and tidy up the repo` (Jul 2026) | 🔄 Active |

### Writing & Documentation

| Repo | Purpose | Articles | Latest |
|------|---------|----------|--------|
| **[ai-thoughts](https://github.com/negtivspace/ai-thoughts)** | Articles & essays: AI platforms (OpenClaw, Hermes), solo entrepreneurship, privacy, technical deep-dives. Bilingual: English + Simplified/Traditional Chinese | 36 articles | `docs: register port-skill-to-opencode article, add sign-off insertion rule to AGENTS.md` (Aug 2026) |

### Tools & Extensions

| Repo | Purpose | Type | Latest |
|------|---------|------|--------|
| **[chrome-extensions](https://github.com/negtivspace/chrome-extensions)** | Monorepo of Chrome extensions: [`sum2chn`](https://github.com/negtivspace/chrome-extensions/tree/main/sum2chn) (translate & summarize web pages → Simplified Chinese MD), [`twitter2md`](https://github.com/negtivspace/chrome-extensions/tree/main/twitter2md) (X post → Markdown, ext + Node CLI), [`twitter-bookmark-summarizer`](https://github.com/negtivspace/chrome-extensions/tree/main/twitter-bookmark-summarizer) (summarize tweets via GPT-4o) | Chrome Ext + CLI | `docs: add top-level README and MIT license` (Aug 2026) |

---

## 🔍 Code Highlights

### Example: Generate the Portfolio with Python
**Repo:** `ai-thoughts` | **Language:** Python | **Purpose:** Render PORTFOLIO.md from a template + `articles.yaml` + git log

```python
def render(data: dict) -> str:
    out = TEMPLATE.read_text(encoding="utf-8")
    values = {
        "ARTICLE_COUNT": str(article_count()),
        "LATEST_COMMIT": latest_commit(),
        "LATEST_ARTICLES": latest_articles(data),
        "LAST_UPDATED": last_updated(),
    }
    for key, value in values.items():
        out = out.replace("{{" + key + "}}", value)
    leftover = sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", out)))
    if leftover:
        print(f"error: unfilled placeholders: {leftover}", file=sys.stderr)
        sys.exit(1)
    return out
```

**Why it matters:** Turns `articles.yaml` + git log into a fresh PORTFOLIO.md with zero hand-editing, and `--check` mode keeps the committed file honest in CI.

---

### Example: Auto-Wrap Markdown Prose with Python
**Repo:** `ai-thoughts` | **Language:** Python | **Purpose:** Join hard-wrapped paragraphs into single-line paragraphs while preserving code fences, tables, and lists

```python
def glue(a: str, b: str) -> str:
    a_end, b_start = a[-1:], b[:1]
    if CJK.match(a_end) and CJK.match(b_start):
        return ""          # 中文之间不加空格
    return " "
```

**Why it matters:** Article and skill prose is stored one-paragraph-per-line (auto-wrapped); this tool restores that convention across `docs/` and `.opencode/skills/` without touching structure — and `--check` flags any file that drifts.

---

### Example: Auto-Publish Skills to ClawHub with GitHub Actions
**Repo:** `ai-thoughts` | **Language:** YAML + Python | **Purpose:** Publish `.opencode/skills/` to ClawHub on every push — no local CLI

```yaml
name: ClawHub Skill Sync
on:
  push:
    branches: [main]
    paths:
      - ".opencode/skills/**"
      - ".github/workflows/clawhub-skill-sync.yml"
  workflow_dispatch:

jobs:
  publish:
    if: github.event_name != 'pull_request' && github.repository_owner == 'j3ffyang'
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v7.0.1
      - uses: oven-sh/setup-bun@<sha>
        with:
          bun-version: 1.3.10
      - name: Checkout ClawHub CLI
        uses: actions/checkout@v7.0.1
        with:
          repository: openclaw/clawhub
          ref: v0.23.3
          path: clawhub-source
      - name: Install ClawHub CLI dependencies
        working-directory: clawhub-source
        run: bun install --frozen-lockfile
      - name: Publish skills to ClawHub
        env:
          CLAWHUB_TOKEN: ${{ secrets.clawhub_token }}
        run: python3 scripts/clawhub_publish.py
```

**Why it matters:** Publishing runs the ClawHub CLI directly instead of the reusable workflow, so the five real statuses the CLI can return — `unchanged`, `would-publish`, `submitted`, `published`, `pending-publication` — are all treated as success. (The upstream reusable workflow only maps three of them, so a successful async publish showed up as a red ✗.) The `repository_owner` guard still stops the two remotes from double-publishing to one ClawHub account.

---

### Example: Verify a Published Skill with a Shell One-Liner
**Repo:** `skill-publish` skill | **Language:** Shell | **Purpose:** Confirm what's live on ClawHub via the read-only skills API

```bash
# What's actually live? Check latestVersion + owner.handle
curl -s -H "Authorization: Bearer $CLH_TOKEN" \
  https://clawhub.ai/api/v1/skills/<slug>
```

**Why it matters:** Turns "the workflow failed" into a verified fact — the API call proves a skill published even when the upstream workflow's status mapping reports a false failure.

---

## 📈 Activity Timeline

*Timeline is editorial — edit it directly in `scripts/portfolio_template.md`, then regenerate.*

### Q3 2026 (Current)
- **Aug 8:** Added `scripts/unwrap_md.py` — auto-wraps article and skill prose to one-paragraph-per-line, preserving code fences, tables, and list nesting
- **Aug 8:** Published the AI agent collaboration playbook — what a real multi-repo ClawHub auto-publish project taught about AGENTS.md, SKILL.md, and project boundaries
- **Aug 7:** Published AMD iGPU + eGPU setup guide for GPD Win4 (bilingual EN/ZH) with verification commands and stable DRM symlinks
- **Aug 4:** Merged the three Chrome extensions (`sum2chn`, `twitter2md`, `twitter-bookmark-summarizer`) into a single `chrome-extensions` monorepo
- **Early Aug:** Published "Why OpenCode is the best AI agent setup for me" essay and the Ollama → llama.cpp local-LLM deep-dive (draft)
- **Jul 31:** Published the Hermes Agent skills/plugins cleanup guide (bilingual)
- **Jul 21-22:** Published Obsidian + Karpathy LLM Wiki local search guide and the "unknown unknowns" essay (bilingual)
- **Jul 14:** Added Brave browser privacy analysis (bilingual) to `ai-thoughts`
- **Jul 14:** Polished and committed two blog posts with bilingual README updates
- **Early Jul:** Releasing v1 of `sum2chn` Chrome extension (translation + summarization)

### Q2 2026
- **Jun:** Completed `twitter2md` Chrome extension and Node.js CLI tool
- **Jun:** Refactored `twitterBookmarkSum` to use popup-triggered summarization
- **May:** Released `twitter2md` for X post extraction as Markdown

### Q1 2026
- **Apr:** Published first Hermes Agent articles and tutorials in `ai-thoughts`
- **Mar:** Established `openclaw-custom-skills` repo on ClawHub
- **Feb:** Began deep-dive experimentation with OpenClaw and Hermes platforms

---

## 🛠️ Tech Stack

**Languages:** Python, JavaScript, TypeScript, Bash

**AI Platforms:** 
- [OpenClaw](https://openclaw.ai) — local agent orchestration
- [Hermes Agent](https://hermes.ai) — autonomous workflow automation
- [Claude Code](https://claude.ai/code) — AI-native coding
- [OpenRouter](https://openrouter.ai) — unified LLM gateway

**APIs & Services:**
- Anthropic Claude (Sonnet, Opus)
- OpenRouter (100+ model access)
- Chrome Extension APIs
- Twitter/X API v2
- Web scraping & DOM manipulation

**Tools:**
- Git + GitHub
- Node.js + npm
- Python 3.10+
- Markdown-first documentation

---

## 💡 Design Philosophy

1. **Skills > Projects** — I think in workflows. Every tool becomes a reusable skill.
2. **Multilingual by default** — English + Chinese (Simplified + Traditional)
3. **Code clarity wins** — Readable Python/JS beats clever one-liners. Always.
4. **Composition over bloat** — Small, focused repos that work well together.
5. **Learn in public** — Detailed articles about what works (and what doesn't).

---

## 🔗 Quick Links

- **GitHub:** [@negtivspace](https://github.com/negtivspace)
- **Blog:** [ai-thoughts](https://github.com/negtivspace/ai-thoughts) — 36 articles on AI, privacy, and entrepreneurship
- **Gists & Experiments:** [Personal gists](https://gist.github.com/j3ffyang)

---

## 📝 Latest Articles

From `ai-thoughts` (most recent published articles):

1. **"zhihu skill + CLI — install and configuration in OpenCode"** (Aug 2026) — Installing the zhihu skill + official zhihu-cli in OpenCode — including the headless-environment auth path via ZHIHU_ACCESS_SECRET when the OS keychain is unavailable
2. **"The Terminal Is an Art"** (Aug 2026) — Almost 30 years on Unix/Linux distilled into why the command line is an art — simple, direct, honest, powerful, universal, and standard for 50 years
3. **"OpenCode + Git: The Underrated Duo"** (Aug 2026) — How a 15-year git user produced more automation in two days with OpenCode than in most of those years — the 9-step thought-flow loop, division of labor, and the compounding architecture
4. **"AI Agent Collaboration: An OpenCode Playbook Built on AGENTS.md and SKILL.md"** (Aug 2026) — What three repos of auto-published ClawHub skills taught me about AGENTS.md, SKILL.md, project boundaries, and the architecture of working with an AI agent
5. **"Arch Linux + Hyprland on GPD Win4 with iGPU + eGPU"** (Aug 2026) — Dual AMD GPUs on a handheld — iGPU + eGPU (RX 7600M XT via OCuLink) rendering offload, verification commands, and stable DRM symlinks
6. **"OpenCode is Best for Me"** (Aug 2026) — Vendor freedom, the big-pickle model, enforced conventions, and unified billing via OpenRouter — why this setup wins for me

👉 See all 36 articles at **[ai-thoughts/docs](https://github.com/negtivspace/ai-thoughts/tree/main/docs)**

---

## 🚀 Getting Started

### Clone a Skill Repo
```bash
git clone https://github.com/negtivspace/ai-custom-skills
cd ai-custom-skills
# Follow README for your specific platform (Claude Code / Hermes / OpenClaw)
```

### Try a Tool
```bash
# Chrome extensions monorepo (twitter2md, sum2chn, twitter-bookmark-summarizer)
git clone https://github.com/negtivspace/chrome-extensions
cd chrome-extensions/twitter2md
npm install
npm run build  # or load the extension manually in Chrome
```

### Read Articles
```bash
git clone https://github.com/negtivspace/ai-thoughts
cd docs
# 36 articles: AI platforms, privacy, solo entrepreneurship, technical deep-dives
```

---

## 📄 License

Most repos are **MIT License** — see individual repos for details.

---

**Last Updated:** August 17, 2026 | Tracking: 6 active repos, 36 published articles, 10+ published skills
