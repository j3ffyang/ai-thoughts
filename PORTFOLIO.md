# J3ffyang's Portfolio

Building **AI-powered automation skills**, **productivity tools**, and **knowledge systems** for individual developers and AI-native workflows.

---

## 🎯 What I Do

I create **production-ready automation skills** across multiple AI platforms (OpenClaw, Hermes, Claude Code), focusing on:

- **Skill-based AI orchestration** — turning workflows into reusable, composable skills
- **Multilingual content automation** — English ↔ Chinese/Traditional Chinese
- **Developer productivity tools** — Chrome extensions, CLI utilities, API integrations
- **AI platform experimentation** — deeply hands-on with OpenClaw, Hermes, Claude, and OpenRouter

All code prioritizes **clarity over cleverness**: simple, readable, portable, and easy to fork.

---

## 📦 Main Repositories

### Core AI Skills & Automation

| Repo | Purpose | Latest | Status |
|------|---------|--------|--------|
| **[ai-custom-skills](https://github.com/negtivspace/ai-custom-skills)** | Production-ready skills for multiple platforms (Claude Code, Hermes, OpenClaw). Covers content creation, data export, workflow automation. | `add new skill and tidy up the repo` (Jul 2026) | 🔄 Active |
| **[hermes-custom-skills](https://github.com/negtivspace/hermes-custom-skills)** | Specialized skills for [Hermes Agent](https://hermes.ai) — autonomous workflows, content generation, task orchestration. | `docs: add README and CONTRIBUTING` (Jul 2026) | 🔄 Active |
| **[openclaw-custom-skills](https://github.com/negtivspace/openclaw-custom-skills)** | Production skills for [OpenClaw](https://openclaw.ai) published to ClawHub. Multilingual blog publishing, media generation. | `add chinese edition` (Jul 2026) | 🔄 Active |
| **[claude-custom-skills](https://github.com/negtivspace/claude-custom-skills)** | Automation skills for [Claude Code](https://claude.ai) — productivity hacks, data export, content workflows. | `add i18n support to README` (Jul 2026) | ✨ Stable |

### Tools & Extensions

| Repo | Purpose | Type | Latest |
|------|---------|------|--------|
| **[chrome-extensions](https://github.com/negtivspace/chrome-extensions)** | Monorepo of Chrome extensions: [`sum2chn`](https://github.com/negtivspace/chrome-extensions/tree/main/sum2chn) (translate & summarize web pages → Simplified Chinese MD), [`twitter2md`](https://github.com/negtivspace/chrome-extensions/tree/main/twitter2md) (X post → Markdown, ext + Node CLI), [`twitter-bookmark-summarizer`](https://github.com/negtivspace/chrome-extensions/tree/main/twitter-bookmark-summarizer) (summarize tweets via GPT-4o) | Chrome Ext + CLI | `docs: add top-level README and MIT license` (Aug 2026) |

### Writing & Documentation

| Repo | Purpose | Articles | Latest |
|------|---------|----------|--------|
| **[ai-thoughts](https://github.com/negtivspace/ai-thoughts)** | Articles & essays: AI platforms (OpenClaw, Hermes), solo entrepreneurship, privacy, technical deep-dives. Bilingual: English + Traditional Chinese | 59 docs | `docs: add Brave browser privacy analysis` (Jul 2026) |

---

## 🔍 Code Highlights

### Example: Twitter Bookmarks to Markdown Exporter
**Repo:** `ai-custom-skills` | **Language:** Python | **Purpose:** Parse Twitter bookmarks → individual Markdown files

```python
#!/usr/bin/env python3
"""
Twitter Bookmarks to Markdown Exporter
Parses bookmarks.json (X GraphQL or legacy v1 format) into individual .md files.
"""

import json
import re
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent.parent  # project root
OUT_DIR = SCRIPT_DIR / "output" / "bookmarks"
BOOKMARKS_FILE = SCRIPT_DIR / "bookmarks.json"
```

**Why it matters:** Demonstrates ability to parse complex data structures, handle multiple input formats, and produce clean, organized output.

---

### Example: Claude API Integration for Translation
**Repo:** `chrome-extensions/sum2chn` | **Language:** JavaScript | **Purpose:** Translate & summarize web pages using Claude Sonnet

```javascript
const CLAUDE_API_URL = 'https://api.anthropic.com/v1/messages';
const CLAUDE_MODEL = 'claude-sonnet-4-6';

const TRANSLATION_SYSTEM_PROMPT = `You are a professional translator and technical writer specializing in Simplified Chinese (简体中文).

Process the provided English web page content and produce a high-quality Chinese document by following these steps:

1. TRANSLATION: Translate all English content faithfully and accurately into Simplified Chinese.
2. GRAMMAR & STYLE: Improve the Chinese text for natural fluency.
3. REORGANIZATION: Improve readability and logical flow.
4. SUMMARIZATION: Condense repetitive content without losing key information.
5. MARKDOWN FORMAT: Output in standard Markdown format with proper headings and code blocks.
```

**Why it matters:** Shows hands-on experience with Claude API, prompt engineering, and production-level system prompts.

---

## 📈 Activity Timeline

### Q3 2026 (Current)
- **Aug 4:** Merged the three Chrome extensions (`sum2chn`, `twitter2md`, `twitter-bookmark-summarizer`) into a single `chrome-extensions` monorepo
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
- **Blog:** [ai-thoughts](https://github.com/negtivspace/ai-thoughts) — 59 articles on AI, privacy, and entrepreneurship
- **Gists & Experiments:** [Personal gists](https://gist.github.com/j3ffyang)

---

## 📝 Latest Articles

From `ai-thoughts` (recent posts):

1. **"Why I Switched to Brave"** (Jul 2026) — Deep analysis of Brave vs Firefox: local keychain, WebRTC control, Tor integration
2. **"Brave Browser Privacy Analysis"** (Jul 2026) — Bilingual breakdown of privacy features + real-world tracking prevention
3. **"AI Usage & Combination: From Doubao User to AI Power User"** (Jul 2026) — Complete guide to OpenRouter + OpenCode + Skills for multi-provider AI workflows
4. **"OpenClaw Security Audit"** — Real incidents, vulnerabilities, hardening checklist for self-hosters
5. **"Hermes Agent Setup Guides"** — Connect to free models, backup data, configure personality (SOUL.md)

👉 See all 59 articles at **[ai-thoughts/docs](https://github.com/negtivspace/ai-thoughts/tree/main/docs)**

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
# 59 articles: AI platforms, privacy, solo entrepreneurship, technical deep-dives
```

---

## 📄 License

Most repos are **MIT License** — see individual repos for details.

---

**Last Updated:** August 4, 2026 | Tracking: 6 active repos, 59 articles, 10+ published skills
