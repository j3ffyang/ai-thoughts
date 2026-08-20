# ai_thoughts

[中文版](README_zh.md)

A bilingual (English · 中文) collection of articles and essays spanning three domains: **technology** (hands-on experience with OpenClaw 🦞 and Hermes Agent ⚕, privacy, knowledge management), **history**, and **culture & philosophy** (motorcycle culture, how different cultures face death, the "unknown unknowns" of knowledge). This page indexes the English articles; Chinese-language articles (including most culture posts) are listed in the [中文版](README_zh.md).

Images for each article live in the [`imgs/`](imgs/) subdirectory and follow the same `YYMMDD-slug` naming convention as the articles themselves.

---

## Contents

### I. Solo Business & Personal Writing

| Article | Description |
|---|---|
| [the-timeless-allure-of-motorcycle-riding](docs/260323-the-timeless-allure-of-motorcycle-riding.md) | English article on motorcycle culture, history, and riding styles |
| [engage-ai](docs/260420-engage-ai.md) | Notes and links on Claude tooling and AI productivity tips for developers |
| [tech-conversation](docs/260521-tech-interview.md) | Tech Q&A conversation (not a job interview) on day-to-day AI agent workflows — mindset, environment, skills, prompts, work style, quality, and security |
| [raindrop-bookmark-manager](docs/260606-raindrop.md) | Notes on Raindrop.io as a bookmark manager — privacy, security, and open-source clients |

### II. History, Culture & Philosophy

| Article | Description |
|---|---|
| [unknown-unknowns](docs/260722-unknown-unknowns2.md) | Personal essay on the four types of knowledge — known knowns, known unknowns, unknown knowns, and the unknown unknowns that shape our lives |
| [terminal-is-an-art](docs/260811-terminal-is-an-art.md) | Almost 30 years on Unix/Linux distilled into why the command line is an art — simple, direct, honest, powerful, universal, and still growing as AI agents' natural interface |

### III. Second Brain & Knowledge Management

| Article | Description |
|---|---|
| [2nd-brain-design](docs/260710-2nd-brain-design.md) | Design doc for an AI-powered bilingual knowledge assistant ("2nd Brain") on Obsidian — architecture, milestones, and tech stack |
| [obsidian-karpathy-llm](docs/260721-obsidian-karpathy-llm.md) | Query your personal vault with a local LLM — no cloud, no API keys |
| [ollama-gpu](docs/260716-ollama-gpu.md) | Running Ollama on Arch Linux with AMD GPUs (GPD Win 4) — diagnosing low GPU utilization and switching to the ROCm build |

### IV. Personal Tech, Privacy & Gaming

| Article | Description |
|---|---|
| [immutable-os-strategy](docs/260622-immutable-os.md) | Personal strategy on "immutable" OS choices — why a quarter-century Linux power user sticks with native Arch Linux and Debian LTS over Bazzite/Silverblue |
| [brave-browser-privacy](docs/260706-brave-post.md) | Deep dive into why I switched to Brave: local keychain, Shields, WebRTC control, Tor integration, and real-world privacy difference |
| [dcs-joystick-tuning](docs/260620-dcs-joystick-tuning.md) | Beginner's guide to DCS World with a VKB Gladiator NXT EVO joystick and a no-numpad keyboard — game-mode flying, keybindings, and axis tuning |
| [arch-hyprland-gpd-win4-egpu](docs/260807-amd.md) | Dual AMD GPUs on a handheld — iGPU + eGPU (RX 7600M XT via OCuLink) rendering offload, verification commands, and stable DRM symlinks |

### V. OpenClaw Platform 🦞

| Article | Description |
|---|---|
| [openclaw-security](docs/260327-openclaw-security-eng.md) | Security audit of OpenClaw: real incidents, known vulnerabilities, and a tiered hardening checklist for self-hosters |
| [openclaw-custom-skills](docs/260406-openclaw-custom-skills.md) | Step-by-step tutorial for building, validating, testing, and publishing custom skills on ClawHub |
| [openclawActivity2](docs/260320-openclaw-activity2.md) | What I've been up to in OpenClaw lately: setup, configuration, and recent activity log |
| [openclaw-update](docs/260525-openclaw-update.md) | Recent updates and developments in OpenClaw platform |

### VI. Hermes Agent ⚕

| Article | Description |
|---|---|
| [hermes-openrouter-elephant-alpha](docs/260414-hermes-elephant-alpha.md) | Practical guide to setting up Hermes with OpenRouter's free Elephant-Alpha model as an alternative to OpenClaw, including WhatsApp integration and multi-user configuration |
| [hermes-connect-nvidiamodel-openrouter](docs/260421-hermes-connect-nvidiamodel-openrouter.md) | Guide to connecting Hermes to Nvidia Nemotron free model via OpenRouter, with primary and fallback model configuration |
| [hermes-update-err](docs/260423-hermes-update-err.md) | Debugging the Hermes TUI build failure caused by a malformed root package.json |
| [hermes-custom-skill-install](docs/260429-custom-skill-hermes.md) | Tested end-to-end workflow: install a custom Hermes SKILL.md from GitHub, with verified commands, examples, and a live installation walkthrough |
| [hermes-github](docs/260504-hermes-github.md) | Hermes Agent: 10 GitHub Repos to Stress-Test It |
| [hermes-SOUL-annotated](docs/260505-hermes-soul.md) | Annotated takeaways from Tony Simons' viral 170-line SOUL.md post — why SOUL.md makes Hermes feel like a teammate |
| [hermes-connect-models](docs/260506-hermes-connect-models.md) | Treasure hunt: Hermes Agent ⚕ Connects to Free Models |
| [hermes-persona-soul](docs/260513-hermes-persona-soul.md) | Practical guide to configuring Hermes Agent's SOUL.md for personality customization |
| [hermes-perftips](docs/260518-hermes-perftips.md) | Hermes Agent Tips & Best Practices Summary |
| [hermes-backup](docs/260528-hermes-backup.md) | Guide to backing up Hermes Agent data using the built-in CLI — full snapshots, quick backups, and restore procedures |
| [hermes-cleanup](docs/260731-hermes-cleanup.md) | List enabled skills, opt out of bundled skills, and revert anytime — debloat your agent |

### VII. Cross-Platform & Comparative

| Article | Description |
|---|---|
| [engageOpenClaw](docs/260420-engage-openclaw.md) | Reflections after 3 months with OpenClaw and Hermes: orchestrating multi-step AI tasks and per-section image generation workflows |
| [choose-between-opencode-and-claude-code](docs/260513-choose-cc-opencode.md) | Comparison of OpenCode vs Claude Code for running Claude Opus and other models |
| [ai-combination](docs/260701-ai-combination2.md) | Optimizing AI usage: from Doubao user to power user — combine OpenRouter, OpenCode, and Hermes/OpenClaw SKILL.md workflows |
| [opencode-is-best](docs/260802-opencode-is-best.md) | Vendor freedom, the big-pickle model, enforced conventions, and unified billing via OpenRouter — why this setup wins for me |
| [ai-agent-collaboration](docs/260808-ai-agent-collaboration.md) | What three repos of auto-published ClawHub skills taught me about AGENTS.md, SKILL.md, project boundaries, and the architecture of working with an AI agent |
| [opencode-git-underrated](docs/260809-opencode-git-underrated.md) | How a 15-year git user produced more automation in two days with OpenCode than in most of those years — the 9-step thought-flow loop, division of labor, and the compounding architecture |

### VIII. Skills

| Article | Description |
|---|---|
| [custom-infographic](.opencode/skills/custom-infographic/SKILL.md) | custom-infographic — professional infographic generator (21 layouts × 21 styles); original author 宝玉 (JimLiu), ported & customized by j3ffyang as an **opencode** skill (needs OPENROUTER_API_KEY) |
| [zhihu-skill-opencode](docs/260815-zhihu-config-in-opencode.md) | Installing the zhihu skill + official zhihu-cli in OpenCode — including the headless-environment auth path via ZHIHU_ACCESS_SECRET when the OS keychain is unavailable |
| [port-skill-to-opencode](docs/260811-port-skill-to-opencode.md) | How to port an existing Hermes Agent skill to OpenCode — copy the folder, rewrite frontmatter, fix paths, and test the router |

### IX. Drafts & Working Notes

Earlier versions of articles are kept alongside their final versions so each piece shows the evolution from brainstorming doc to finished post. These are the drafts that became (or are becoming) the articles above.

| Draft | Notes |
|---|---|
| [ollama-to-llamacpp](docs/260803-ollama-to-llamacpp.md) | Pushing the limit of a local LLM on Arch Linux (GPD): switching from Ollama to llama.cpp for finer VRAM control, higher efficiency, and better output quality with qwen2.5:14b |
| [openclaw-custom-skills (early drafts)](docs/260406-writing-your-own-custom-skill-in-openclaw.md) | Earlier iterations of the OpenClaw custom-skills tutorial |
| [ai-combination (full v1.1)](docs/260701-ai-combination.md) · [template](docs/260701-ai-combination-template.md) | Full-length version and seed template behind the condensed ai-combination article |
| [web-search newsletter](docs/260425-web-search.md) | Notes on building a newsletter skill with web_search (OpenClaw/Hermes) |
| [agents-opencode-config](docs/260811-agents-opencode-config.md) | Summary note on the OpenCode setup: how AGENTS.md and opencode.jsonc load, their precedence flows, the permission decision model, and a conflict/duplicate review |
| [ai-video-pipeline](docs/260816-ai-video-pipeline.md) | How a 60-second AI video trailer was built from eight photos with five OpenCode skills, an 8-stage thought-flow loop, and two content-policy failures that became codified gates |
| [ai-video-recommendations](docs/260816-ai-video-recommendations.md) | Ten rules for making AI videos with image-to-video engines — story-first scripting, delegated vision, audio decoupling, and a resumable pipeline that turns failures into codified skills |
| [death-thought-flow](docs/260817-death-thought-flow.md) | Personal thought-flow master for the death-in-Mexico project — seven thinking points, six content sections, verified facts, and cultural guardrails; use with the story-telling skill to generate a narration script or essay |

---

> **Maintaining this index:** edit [`articles.yaml`](articles.yaml), then run `python scripts/gen_readmes.py` to regenerate `README.md` and [`README_zh.md`](README_zh.md).

