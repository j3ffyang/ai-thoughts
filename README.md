# ai_thoughts

[中文版](README_zh.md)

A bilingual (English · 中文) collection of articles and essays spanning three domains: **technology** (hands-on experience with OpenClaw 🦞 and Hermes Agent ⚕, privacy, knowledge management), **history**, and **culture & philosophy** (motorcycle culture, how different cultures face death, the "unknown unknowns" of knowledge). This page indexes the English articles; Chinese-language articles (including most culture posts) are listed in the [中文版](README_zh.md).

Images for each article live in the [`imgs/`](imgs/) subdirectory and follow the same `YYMMDD-slug` naming convention as the articles themselves.

Custom OpenCode skills developed here auto-publish to [ClawHub](https://clawhub.ai/j3ffyang) — the Published Skills table below lists each one.

---

## Contents

### I. Personal Tech, Privacy & Gaming

| Article | Description |
|---|---|
| [play-rdr2-with-opencode](docs/260921-play-rdr2-with-opencode.md) | Playing Red Dead Redemption 2 with an AI agent — documenting a playthrough in OpenCode with a custom skill and an AGENTS.md, on Arch Linux via Steam/Proton |
| [rdr2-ch2-playthrough-notes](docs/260921-rdr2-ch2-playthrough.md) | Working reference: RDR2 Chapter 2 playthrough notes — gold bars, legendary animals, trinkets, robberies, and challenges, maintained with the rdr2-playthrough skill |
| [lossless-pptx-extraction](docs/260919-lossless-pptx-extraction.md) | Engineering deep-dive: extracting PowerPoint decks into full-data Markdown — OOXML shape walking, content vs layout chrome vs unrenderable objects, a 5-point losslessness audit, and why the pipeline stays local instead of running in CI |
| [happy-birthday-linux](docs/260828-happy-birthday-linux-from-aix-to-arch.md) | A 35-year Linux journey in one personal story — AIX at IBM, getting hacked and the security habit it forged, the distro years ending at Arch, and every machine now Arch Linux; with a visual summary infographic |
| [arch-hyprland-gpd-win4-egpu](docs/260807-gpd-dual-amd-gpu.md) | Dual AMD GPUs on a handheld — iGPU + eGPU (RX 7600M XT via OCuLink) rendering offload, verification commands, and stable DRM symlinks |
| [brave-browser-privacy](docs/260706-brave-post.md) | Deep dive into why I switched to Brave: local keychain, Shields, WebRTC control, Tor integration, and real-world privacy difference |
| [immutable-os-strategy](docs/260622-immutable-os.md) | Personal strategy on "immutable" OS choices — why a quarter-century Linux power user sticks with native Arch Linux and Debian LTS over Bazzite/Silverblue |
| [dcs-joystick-tuning](docs/260620-dcs-joystick-tuning.md) | Beginner's guide to DCS World with a VKB Gladiator NXT EVO joystick and a no-numpad keyboard — game-mode flying, keybindings, and axis tuning |

### II. Cross-Platform & Comparative

| Article | Description |
|---|---|
| [opencode-create-skill-onfly](docs/260906-opencode-create-skill-onfly.md) | Create SKILL.md, AGENTS.md, and PERSONA.md on the fly instead of hunting others' skills — three levels of customization, real benefits from daily use, and OpenCode as the daily agent |
| [agents-md-not-a-persona](docs/260821-agents-md-not-a-persona.md) | AGENTS.md is not a persona but a constitution written in scars — every rule traced to a real incident (a self-cloned repo, lying docs, a prompt flood), agent-agnostic lessons for any AI coding agent |
| [zhihu-skill-opencode](docs/260815-zhihu-config-in-opencode.md) | Installing the zhihu skill + official zhihu-cli in OpenCode — including the headless-environment auth path via ZHIHU_ACCESS_SECRET when the OS keychain is unavailable |
| [agents-opencode-config](docs/260811-agents-opencode-config.md) | OpenCode AGENTS.md + opencode.jsonc — architecture, precedence and workflow: how the two surfaces load, resolve conflicts, evaluate permissions, and isolate across submodule context walls; verified against anomalyco/opencode source HEAD e11dbd0. |
| [port-skill-to-opencode](docs/260811-port-skill-to-opencode.md) | How to port an existing Hermes Agent skill to OpenCode — copy the folder, rewrite frontmatter, fix paths, and test the router |
| [opencode-git-underrated](docs/260809-opencode-git-underrated.md) | How a 15-year git user produced more automation in two days with OpenCode than in most of those years — the 9-step thought-flow loop, division of labor, and the compounding architecture |
| [ai-agent-collaboration](docs/260808-ai-agent-collaboration.md) | What three repos of auto-published ClawHub skills taught me about AGENTS.md, SKILL.md, project boundaries, and the architecture of working with an AI agent |
| [opencode-is-best](docs/260802-opencode-is-best.md) | Vendor freedom, the big-pickle model, enforced conventions, and unified billing via OpenRouter — why this setup wins for me |
| [ai-combination](docs/260701-ai-combination2.md) | Optimizing AI usage: from Doubao user to power user — combine OpenRouter, OpenCode, and Hermes/OpenClaw SKILL.md workflows |
| [choose-between-opencode-and-claude-code](docs/260513-choose-cc-opencode.md) | Comparison of OpenCode vs Claude Code for running Claude Opus and other models |
| [engageOpenClaw](docs/260420-engage-openclaw.md) | Reflections after 3 months with OpenClaw and Hermes: orchestrating multi-step AI tasks and per-section image generation workflows |

### III. History, Culture & Philosophy

| Article | Description |
|---|---|
| [terminal-is-an-art](docs/260811-terminal-is-an-art.md) | Almost 30 years on Unix/Linux distilled into why the command line is an art — simple, direct, honest, powerful, universal, and still growing as AI agents' natural interface |
| [unknown-unknowns](docs/260722-unknown-unknowns2.md) | Personal essay on the four types of knowledge — known knowns, known unknowns, unknown knowns, and the unknown unknowns that shape our lives |

### IV. Hermes Agent ⚕

| Article | Description |
|---|---|
| [hermes-cleanup](docs/260731-hermes-cleanup.md) | List enabled skills, opt out of bundled skills, and revert anytime — debloat your agent |
| [hermes-backup](docs/260528-hermes-backup.md) | Guide to backing up Hermes Agent data using the built-in CLI — full snapshots, quick backups, and restore procedures |
| [hermes-perftips](docs/260518-hermes-perftips.md) | Hermes Agent Tips & Best Practices Summary |
| [hermes-persona-soul](docs/260513-hermes-persona-soul.md) | Practical guide to configuring Hermes Agent's SOUL.md for personality customization |
| [hermes-connect-models](docs/260506-hermes-connect-models.md) | Treasure hunt: Hermes Agent ⚕ Connects to Free Models |
| [hermes-SOUL-annotated](docs/260505-hermes-soul.md) | Annotated takeaways from Tony Simons' viral 170-line SOUL.md post — why SOUL.md makes Hermes feel like a teammate |
| [hermes-github](docs/260504-hermes-github.md) | Hermes Agent: 10 GitHub Repos to Stress-Test It |
| [hermes-custom-skill-install](docs/260429-custom-skill-hermes.md) | Tested end-to-end workflow: install a custom Hermes SKILL.md from GitHub, with verified commands, examples, and a live installation walkthrough |
| [hermes-update-err](docs/260423-hermes-update-err.md) | Debugging the Hermes TUI build failure caused by a malformed root package.json |
| [hermes-connect-nvidiamodel-openrouter](docs/260421-hermes-connect-nvidiamodel-openrouter.md) | Guide to connecting Hermes to Nvidia Nemotron free model via OpenRouter, with primary and fallback model configuration |
| [hermes-openrouter-elephant-alpha](docs/260414-hermes-elephant-alpha.md) | Practical guide to setting up Hermes with OpenRouter's free Elephant-Alpha model as an alternative to OpenClaw, including WhatsApp integration and multi-user configuration |

### V. Second Brain & Knowledge Management

| Article | Description |
|---|---|
| [obsidian-karpathy-llm](docs/260721-obsidian-karpathy-llm.md) | Query your personal vault with a local LLM — no cloud, no API keys |
| [ollama-gpu](docs/260716-ollama-gpu.md) | Running Ollama on Arch Linux with AMD GPUs (GPD Win 4) — diagnosing low GPU utilization and switching to the ROCm build |
| [2nd-brain-design](docs/260710-2nd-brain-design.md) | Design doc for an AI-powered bilingual knowledge assistant ("2nd Brain") on Obsidian — architecture, milestones, and tech stack |

### VI. Solo Business & Personal Writing

| Article | Description |
|---|---|
| [raindrop-bookmark-manager](docs/260606-raindrop.md) | Notes on Raindrop.io as a bookmark manager — privacy, security, and open-source clients |
| [tech-conversation](docs/260521-tech-interview.md) | Tech Q&A conversation (not a job interview) on day-to-day AI agent workflows — mindset, environment, skills, prompts, work style, quality, and security |
| [engage-ai](docs/260420-engage-ai.md) | Notes and links on Claude tooling and AI productivity tips for developers |
| [the-timeless-allure-of-motorcycle-riding](docs/260323-the-timeless-allure-of-motorcycle-riding.md) | English article on motorcycle culture, history, and riding styles |

### VII. OpenClaw Platform 🦞

| Article | Description |
|---|---|
| [openclaw-update](docs/260525-openclaw-update.md) | Recent updates and developments in OpenClaw platform |
| [openclaw-custom-skills](docs/260406-openclaw-custom-skills.md) | Step-by-step tutorial for building, validating, testing, and publishing custom skills on ClawHub |
| [openclaw-security](docs/260327-openclaw-security-eng.md) | Security audit of OpenClaw: real incidents, known vulnerabilities, and a tiered hardening checklist for self-hosters |
| [openclawActivity2](docs/260320-openclaw-activity2.md) | What I've been up to in OpenClaw lately: setup, configuration, and recent activity log |

### VIII. Published Skills on ClawHub

Developed in this repo and auto-published to [ClawHub](https://clawhub.ai/j3ffyang) on every push.

| Skill | Description |
|---|---|
| [astro-sync](https://clawhub.ai/j3ffyang/skills/astro-sync) | Convert and polish a Markdown article into AstroPaper-compatible post format for the astro_journal blog (everbox.io). Use when the user wants to publish or sync an article (e.g. from ai-thoughts/docs/ or history/docs/) to the Astro blog, convert Markdown to Astro format, add AstroPaper frontmatter, or move images into src/assets/images/. |
| [rdr2-playthrough](https://clawhub.ai/j3ffyang/skills/rdr2-playthrough) | Use when maintaining RDR2 (Red Dead Redemption 2) playthrough notes — logging an acquisition ("acquired X", "got N gold bars", "finished X"), answering in-game location/crafting questions, or reviewing the notes for duplicate or stale info. Triggers on RDR2, Red Dead Redemption, playthrough, legendary animal, talisman, trinket, valerian root, gold bar, horse, weapon, berry. |
| [pptx-extract](https://clawhub.ai/j3ffyang/skills/pptx-extract) | Extract a PowerPoint deck into full-data, page-delimited Markdown — every text run, table, speaker note, and image — with unextractable data (vector metafiles, charts, OLE embeds) skipped but visibly noted on its slide, then prove losslessness with a 5-point machine audit. Use when the user asks to extract/convert a PPTX to Markdown, add a new deck to an extraction project, or regenerate a stale extraction. Related terms: PPT, PowerPoint, PPTX, slide extraction, 提取. |
| [normalize-whitespace](https://clawhub.ai/j3ffyang/skills/normalize-whitespace) | Normalize indentation of a large reference text document (e.g. README.md) to a consistent TAB style while keeping content byte-identical. Use when asked to fix inconsistent leading spaces, align command blocks, or clean indentation spread across hundreds of lines in a prose-heavy, single-fence document. Built from the 2026-09 instguid README.md normalization session. |
| [sync-config-with-sample](https://clawhub.ai/j3ffyang/skills/sync-config-with-sample) | Sync a production config file (e.g. hyprland.lua.gpd) against the latest upstream sample (e.g. hyprland.lua.260917) by copying only reference info/URL comments while preserving the user's actual configuration. Use when the user drops a freshly downloaded sample alongside a live config, mentions keeping the newest sample as the diff baseline, or wants only real config differences to remain visible in diff. |
| [publish-skills](https://clawhub.ai/j3ffyang/skills/publish-skills) | Publish SKILL.md files to ClawHub (clawhub.ai) and diagnose publish failures across the three skill repos (history, ai-custom-skills, ai-thoughts). Use when the user wants to publish skills to ClawHub, manually trigger a publish, check why a publish failed or was skipped, or understand the ClawHub skill sync pipeline. |
| [bold-highlights](https://clawhub.ai/j3ffyang/skills/bold-highlights) | Add sparse, deliberate bold highlights to a few key concepts so readers can scan and capture the article's core points. Use when polishing an article in ai-thoughts/docs/ or when the user asks to make an article more scannable or add highlights. |
| [arch-sign-off](https://clawhub.ai/j3ffyang/skills/arch-sign-off) | Append the Arch Linux sign-off line `btw, i use arch` to the very bottom of an article in ai-thoughts/docs/ (EN or ZH). This is a standing default for every article: apply it unless the user explicitly says not to. Use when writing or finishing any new article, or when the user asks to add it. |
| [translate-to-chn](https://clawhub.ai/j3ffyang/skills/translate-to-chn) | Translate a specific article from ai-thoughts/docs/ into Simplified Chinese, writing the output to an exactly-same-filename "-chn.md" file. Use when the user names a specific article and asks to translate it (e.g. "translate 260803-ollama-to-llamacpp", "翻译 xxx", "make a -chn.md version"). Never runs automatically; only acts on an explicitly chosen article. |
| [custom-infographic](https://clawhub.ai/j3ffyang/skills/custom-infographic) | Generate a professional infographic from an article, document, URL, or topic, using the baoyu layout x style system (21 layouts x 21 styles). Original author 宝玉 (JimLiu); ported & customized by j3ffyang. Use when the user asks to create an infographic, 信息图, visual summary, 可视化, or a high-density information image, or wants an article turned into a visual poster. |
| [resize-for-banner](https://clawhub.ai/j3ffyang/skills/resize-for-banner) | Rescale an image into social banner versions using ImageMagick. The image is resized to fit and the leftover space is padded black — never cropped. Use when the user wants a banner, cover photo, or resized version for a social profile or article header. Never overwrites the original — creates new files beside it. Defaults to Twitter/X (5:2, 1500x600); other platforms available on request. |
| [zhihu-for-opencode](https://clawhub.ai/j3ffyang/skills/zhihu-for-opencode) | 使用知乎开放平台搜索知乎和全网内容、获取热榜、调用知乎直答，或读取当前用户自己的知乎创作、关注与收藏。用户提到知乎搜索、社区观点、真实经验、热点、热榜、知乎直答、我的知乎内容、我的关注、我的收藏、开放平台、API、MCP、Access Secret，或要求查看、安装和配置知乎 Skill 时使用。深度研究优先返回搜索原始来源；本人数据只读取完成任务所需的最小范围。 |
| [read-image](https://clawhub.ai/j3ffyang/skills/read-image) | Generate textual descriptions of one or more images when the current session model (e.g. opencode/big-pickle) has no image input, by delegating to a vision-capable model on OpenRouter via `opencode run` with --file. Use when the user drops photos into imgs/, asks "can you read/describe these images", or an image needs a description for an article, portfolio, infographic, or video pipeline. Related terms: 看图, 描述图片, image description, vision model, glm-4.6v, --file. |
| [story-telling](https://clawhub.ai/j3ffyang/skills/story-telling) | Generate a narration script (voiceover + shot list + per-clip visual prompts + music cues) for a personal travel-story video or essay, from a thought-flow master skill and the author's own photos. Use when the user wants "a script", "旁白脚本", a storytelling/故事化 script for a video, or asks to turn a personal travel story (e.g. the death-in-Mexico project) into a narrated video or essay. Output is Simplified Chinese first-person storytelling, engine-agnostic in voiceover and timing, engine-specific in clip prompts. Never runs automatically; acts only when the user asks for a script. |
| [video-gen](https://clawhub.ai/j3ffyang/skills/video-gen) | Generate a video from a story-telling narration script plus the author's photos, using Seedance 2.0 image-to-video via OpenRouter's asynchronous video API: pre-render gates (face-scan, narrative order, risk-POC), then per-clip submit -> poll -> download, then ffmpeg assembly. Multi-clip projects default to silent clips plus one continuous soundtrack (synthesized or royalty-free/PD); subtitle voiceover is the fallback (no OpenRouter TTS). Verified working 2026-08-15 (POC: 4s 480p clip, $0.28, ~3 min). Use when the user asks to render a narration script into a video, generate a 视频, or run the death-in-Mexico project's video pipeline. Related terms: Seedance, 视频生成, OpenRouter, image-to-video. |
| [thought-flow](https://clawhub.ai/j3ffyang/skills/thought-flow) | The 8-stage collaboration loop for working with the user: INTENT, CONSTRAINTS, PROPOSE, PRESS, PRACTICE, INVESTIGATE, CODIFY, BOUNDARY-CHECK. Use when starting a new task (state intent and constraints up front), when proposing a plan (include options + a recommendation), when the user pushes back on a proposal, when something fails or looks broken and needs investigation, or when deciding whether to codify knowledge into an AGENTS.md rule or a SKILL.md procedure. |

### IX. Drafts & Working Notes

Earlier versions of articles are kept alongside their final versions so each piece shows the evolution from brainstorming doc to finished post. These are the drafts that became (or are becoming) the articles above.

| Draft | Notes |
|---|---|
| [opencode-openrouter-model-selection](docs/260922-opencode-openrouter-model-selection.md) | Picking a model and provider for OpenCode via OpenRouter — separating model origin from serving jurisdiction, tiering data-privacy risk, comparing DeepSeek/Qwen/GLM/Kimi/Gemini/OpenAI prices, and reproducing live rates with curl and Python |
| [ground-truth-and-growth](docs/260825-ground-truth-and-growth.md) | Reflections on growing with AI agents — choosing OpenCode, learning the pace of AI collaboration, discovering Git automation, and finding meditative honesty in terminal-based computing |
| [death-thought-flow](docs/260817-death-thought-flow.md) | Personal thought-flow master for the death-in-Mexico project — seven thinking points, six content sections, verified facts, and cultural guardrails; use with the story-telling skill to generate a narration script or essay |
| [ai-video-pipeline](docs/260816-ai-video-pipeline.md) | How a 60-second AI video trailer was built from eight photos with five OpenCode skills, an 8-stage thought-flow loop, and two content-policy failures that became codified gates |
| [ai-video-recommendations](docs/260816-ai-video-recommendations.md) | Ten rules for making AI videos with image-to-video engines — story-first scripting, delegated vision, audio decoupling, and a resumable pipeline that turns failures into codified skills |
| [ollama-to-llamacpp](docs/260803-ollama-to-llamacpp.md) | Pushing the limit of a local LLM on Arch Linux (GPD): switching from Ollama to llama.cpp for finer VRAM control, higher efficiency, and better output quality with qwen2.5:14b |
| [ai-combination (full v1.1)](docs/260701-ai-combination.md) · [template](docs/260701-ai-combination-template.md) | Full-length version and seed template behind the condensed ai-combination article |
| [web-search newsletter](docs/260425-web-search.md) | Notes on building a newsletter skill with web_search (OpenClaw/Hermes) |
| [openclaw-custom-skills (early drafts)](docs/260406-writing-your-own-custom-skill-in-openclaw.md) | Earlier iterations of the OpenClaw custom-skills tutorial |

---

> **Maintaining this index:** edit [`articles.yaml`](articles.yaml), then run `python scripts/gen_readmes.py` to regenerate `README.md` and [`README_zh.md`](README_zh.md).
> The Published Skills table is auto-derived from each `.opencode/skills/*/SKILL.md` frontmatter, linking to its ClawHub page. Article sections are ordered by newest post; drafts stay last.

