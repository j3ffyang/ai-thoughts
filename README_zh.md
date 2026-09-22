# ai_thoughts

[English](README.md)

中英双语（English · 中文）文章与随笔合集，涵盖三大领域：**技术**（OpenClaw 🦞 与 Hermes Agent ⚕ 的实战体验、隐私、知识管理）、**历史**、以及**文化与哲思**（摩托车文化、不同文化如何面对死亡、"未知的未知"）。内容涵盖实操指南（自定义技能开发、自托管部署加固），以及更具个人色彩的写作（个人创业、骑行文化）。

每篇文章的配图存放于 [`imgs/`](imgs/) 子目录，沿用与文章相同的 `YYMMDD-slug` 命名规范。

本仓库自研的 OpenCode 技能会在每次推送时自动发布到 [ClawHub](https://clawhub.ai/j3ffyang)——下方"已发布技能"表格逐项列出。

---

## 目录

### 一、个人技术、隐私与游戏

| 文章 | 简介 |
|---|---|
| [play-rdr2-with-opencode](docs/260921-play-rdr2-with-opencode.md) | 用 AI 智能体玩《荒野大镖客 2》——在 OpenCode 中用自定义技能与 AGENTS.md 记录一次通关，运行于 Arch Linux + Steam/Proton |
| [rdr2-ch2-playthrough-notes](docs/260921-rdr2-ch2-playthrough.md) | 工作参考：《荒野大镖客 2》第二章通关笔记——金条、传奇动物、饰品、抢劫与挑战，由 rdr2-playthrough 技能维护 |
| [lossless-pptx-extraction](docs/260919-lossless-pptx-extraction.md) · [无损提取 PPTX](docs/260919-lossless-pptx-extraction-chn.md) | 工程深潜：把 PowerPoint 演示文稿完整提取为 Markdown——OOXML 形状遍历、内容与版式装饰及不可渲染对象的区分、五点无损审计，以及为何这条流水线选择本地运行而非 CI |
| [happy-birthday-linux](docs/260828-happy-birthday-linux-from-aix-to-arch.md) · [生日快乐，Linux](docs/260828-happy-birthday-linux-from-aix-to-arch-chn.md) | 三十五年的 Linux 个人旅程——从 IBM 的 AIX 起步、被入侵后养成安全习惯、兜兜转转的发行版岁月最终停在 Arch，如今每一台机器都是 Arch Linux；附视觉总结信息图 |
| [arch-hyprland-gpd-win4-egpu](docs/260807-gpd-dual-amd-gpu.md) · [arch-hyprland-gpd-win4-egpu_chn](docs/260807-gpd-dual-amd-gpu-chn.md) | 掌机上的双 AMD GPU（iGPU + eGPU，OCuLink 连接 RX 7600M XT）渲染卸载指南——验证命令、稳定 DRM 符号链接与调整日志 |
| [brave-browser-privacy](docs/260706-brave-post.md) | 为什么我选择Brave的深度分析：本地密钥管理、Shields隐私防护、WebRTC控制与Tor集成（英文） |
| [brave-browser-privacy](docs/260706-brave-post-chn.md) | 為什麼我開始使用Brave的深度分析：本地密鑰管理、隱私防護、WebRTC控制及Tor整合（繁體中文） |
| [immutable-os-strategy](docs/260622-immutable-os.md) | "不可变操作系统"选型策略——为何一位使用Linux四分之一世纪的老用户坚持原生Arch与Debian LTS，而非Bazzite/Silverblue |
| [dcs-joystick-tuning](docs/260620-dcs-joystick-tuning.md) | DCS World新手入门指南：VKB Gladiator NXT EVO摇杆 + 无数字键盘的键位映射、游戏模式飞行与摇杆轴调校 |

### 二、跨平台与比较

| 文章 | 简介 |
|---|---|
| [opencode-create-skill-onfly](docs/260906-opencode-create-skill-onfly.md) · [opencode-create-skill-onfly](docs/260906-opencode-create-skill-onfly-chn.md) | 随手创建 SKILL.md、AGENTS.md 和 PERSONA.md，而不是去淘别人的技能——三个自定义层次、日复一日使用得来的真实好处，以及作为日常智能体的 OpenCode |
| [agents-md-not-a-persona](docs/260821-agents-md-not-a-persona.md) · [AGENTS.md 不是人格设定](docs/260821-agents-md-not-a-persona-chn.md) | AGENTS.md 不是人格设定——它是一部用伤疤写成的宪章：每条规则追溯到真实事故（自克隆仓库、撒谎的文档、提示洪水），不绑定特定工具的通用法则 |
| [zhihu-skill-opencode](docs/260815-zhihu-config-in-opencode.md) · [zhihu-skill-opencode_chn](docs/260815-zhihu-config-in-opencode-chn.md) | 在 OpenCode 中安装 zhihu 技能与官方 zhihu-cli 的全程记录——包括无头环境下密钥链不可用时通过 ZHIHU_ACCESS_SECRET 完成认证的路径 |
| [AGENTS + opencode.jsonc 架构](docs/260811-agents-opencode-config.md) · [AGENTS + opencode.jsonc 架构（中文）](docs/260811-agents-opencode-config-chn.md) | OpenCode AGENTS.md 与 opencode.jsonc 架构、优先级与工作流：双配置表面如何加载、消解冲突、评估权限并在子模块上下文隔离墙间运作；对照 anomalyco/opencode 源码 HEAD e11dbd0 严格复核。 |
| [port-skill-to-opencode](docs/260811-port-skill-to-opencode.md) · [port-skill-to-opencode](docs/260811-port-skill-to-opencode-chn.md) | 将现有 Hermes Agent 技能移植到 OpenCode——复制文件夹、重写 frontmatter、修正路径并测试路由器 |
| [opencode-git-underrated](docs/260809-opencode-git-underrated.md) | 一位用了十五年 git 的用户，如何在两天内用 OpenCode 产出比过去多数年份更多的自动化——9 步思维流循环、分工与复利架构 |
| [opencode-git-underrated_chn](docs/260809-opencode-git-underrated-chn.md) | OpenCode + Git：被低估的组合——十五年 git 老手两天内构建的自动化系统与思维流循环（简体中文） |
| [ai-agent-collaboration](docs/260808-ai-agent-collaboration.md) · [ai-agent-collaboration_chn](docs/260808-ai-agent-collaboration-chn.md) | 跨三个仓库自动发布技能到 ClawHub 的真实实践——关于 AGENTS.md、SKILL.md、项目边界与 AI 协作架构的启发 |
| [opencode-is-best](docs/260802-opencode-is-best.md) · [opencode-is-best_chn](docs/260802-opencode-is-best-chn.md) | 免供应商锁定、big-pickle 模型、可执行的规范约定与 OpenRouter 统一计费——为什么这套方案最合我意 |
| [ai-combination](docs/260701-ai-combination2.md) | 优化AI使用方式：从豆包用户到进阶用户——组合 OpenRouter、OpenCode 与 Hermes/OpenClaw 的 SKILL.md 工作流 |
| [ai-combination_chn](docs/260701-ai-combination2-chn.md) | 豆包用户到 AI 进阶用户：OpenRouter + OpenCode + AI Agent 组合策略（简体中文） |
| [opencode-vs-claude-code](docs/260513-choose-cc-opencode.md) | OpenCode与Claude Code的比较：用于运行Claude Opus和其他模型（中英双语） |
| [opencode-vs-claude-code_chn](docs/260513-choose-cc-opencode-chn.md) | OpenCode 与 Claude Code 对比（简体中文） |
| [engageOpenClaw](docs/260420-engage-openclaw.md) | 使用OpenClaw与Hermes三个月后的复盘：多步骤AI任务编排与章节配图生成工作流 |

### 三、历史、文化与哲思

| 文章 | 简介 |
|---|---|
| [terminal-is-an-art](docs/260811-terminal-is-an-art.md) · [terminal-is-an-art](docs/260811-terminal-is-an-art-chn.md) | 近30年Unix/Linux经验凝练：命令行为何是艺术——简单、直接、诚实、强大、通用，且作为AI智能体的原生界面仍在进化 |
| [unknown-unknowns](docs/260722-unknown-unknowns2.md) | 关于知识四种类型的个人随笔——已知的已知、已知的未知、未知的已知，以及塑造我们人生的"未知的未知" |
| [unknown-unknowns](docs/260722-unknown-unknowns2-chn.md) | 不知道自己不知道的事——知识的四种类型（简体中文） |

### 四、Hermes Agent ⚕

| 文章 | 简介 |
|---|---|
| [hermes-cleanup](docs/260731-hermes-cleanup.md) · [hermes-cleanup_chn](docs/260731-hermes-cleanup-chn.md) | 查看已启用技能、退出内置技能、随时可回退——给 Hermes Agent 减负 |
| [hermes-backup](docs/260528-hermes-backup.md) | 使用Hermes内置CLI备份数据的操作指南——全量快照、快速备份与恢复流程 |
| [hermes-backup_chn](docs/260528-hermes-backup-chn.md) | 备份 Hermes Agent 的中文指南，涵盖全量快照、快速备份与恢复步骤（简体中文） |
| [hermes-perftips](docs/260518-hermes-perftips.md) | Hermes Agent Tips & Best Practices Summary |
| [hermes-perftips_chn](docs/260518-hermes-perftips-chn.md) | Hermes 使用技巧与最佳实践（简体中文） |
| [hermes-persona-soul](docs/260513-hermes-persona-soul.md) | 关于配置Hermes Agent的SOUL.md以定义代理身份、语气和边界的实用指南 |
| [hermes-persona-soul_chn](docs/260513-hermes-persona-soul-chn.md) | Hermes Agent SOUL.md 人格配置实战指南（简体中文） |
| [hermes-connect-models](docs/260506-hermes-connect-models.md) | 寻宝：Hermes Agent ⚕ 连接免费模型 |
| [hermes-connect-models_chn](docs/260506-hermes-connect-models-chn.md) | 探索 Hermes Agent 连接免费模型的寻宝之旅（简体中文） |
| [hermes-SOUL-annotated](docs/260505-hermes-soul.md) | Tony Simons 爆火的 170 行 SOUL.md 深度解读——为何 SOUL.md 让 Hermes 更像一个队友 |
| [hermes-SOUL-annotated_chn](docs/260505-hermes-soul-chn.md) | Hermes 的 170 行 SOUL.md 深度解读（简体中文） |
| [hermes-github](docs/260504-hermes-github.md) | Hermes Agent: 10 GitHub Repos to Stress-Test It |
| [hermes-custom-skill-install](docs/260429-custom-skill-hermes.md) | 从GitHub安装自定义Hermes SKILL.md的端到端验证流程，含实测命令、示例与现场安装演练 |
| [hermes-custom-skill-install_chn](docs/260429-custom-skill-hermes-chn.md) | 从 GitHub 安装自定义 Hermes SKILL.md 的完整实操流程（简体中文） |
| [hermes-update-err](docs/260423-hermes-update-err.md) | 排查Hermes TUI构建失败问题：根因为根目录package.json格式错误 |
| [hermes-connect-nvidiamodel-openrouter](docs/260421-hermes-connect-nvidiamodel-openrouter.md) | 将Hermes接入OpenRouter上的Nvidia Nemotron免费模型，含主备模型配置 |
| [hermes-openrouter-elephant-alpha](docs/260414-hermes-elephant-alpha.md) | 将Hermes接入OpenRouter免费Elephant-Alpha模型的实操指南（作为OpenClaw的替代方案），含WhatsApp集成与多用户配置 |
| [hermes-openrouter-elephant-alpha_chn](docs/260414-hermes-elephant-alpha-chn.md) | 使用 Hermes 连接 OpenRouter 免费 Elephant-Alpha 模型的配置指南（简体中文） |

### 五、第二大脑与知识管理

| 文章 | 简介 |
|---|---|
| [obsidian-karpathy-llm](docs/260721-obsidian-karpathy-llm.md) | 让个人笔记可被本地大模型检索问答——全程本地，无需云端与 API 密钥 |
| [obsidian-karpathy-llm](docs/260721-obsidian-karpathy-llm-chn.md) | 用 Obsidian + Karpathy LLM Wiki + Ollama 打造本地 AI 知识库（简体中文） |
| [ollama-gpu](docs/260716-ollama-gpu.md) | 在Arch Linux上以AMD GPU（GPD Win 4）运行Ollama——排查GPU利用率过低并切换到ROCm版本 |
| [2nd-brain-design](docs/260710-2nd-brain-design.md) | 基于Obsidian的中英双语AI知识助手（"第二大脑"）设计文档——架构、里程碑与技术栈 |

### 六、一人企业与个人随笔

| 文章 | 简介 |
|---|---|
| [raindrop-bookmark-manager](docs/260606-raindrop.md) | Raindrop.io 书签管理工具的使用笔记——隐私、安全与开源客户端 |
| [raindrop-bookmark-manager](docs/260606-raindrop-chn.md) | 书签管理器 Raindrop.io 的隐私、安全与开源客户端使用笔记（简体中文） |
| [tech-conversation](docs/260521-tech-interview.md) | 技术问答对话（非面试）：AI Agent 日常工作流——思维模式、环境准备、技能、提示词、工作方式与安全 |
| [tech-conversation](docs/260521-tech-interview-chn.md) | 技术问答对话（非面试）：AI Agent 日常工作流（简体中文） |
| [engage-ai](docs/260420-engage-ai.md) | Claude工具使用笔记与面向开发者的AI效率提升技巧 |
| [the-timeless-allure-of-motorcycle-riding](docs/260323-the-timeless-allure-of-motorcycle-riding.md) | 摩托车文化、历史与骑行风格英文文章 |
| [timeless-allure-motorcycle-riding](docs/260323-timeless-allure-motorcycle-riding-chn.md) | 摩托车骑行主题文章中文重写版，附各章节配图 |
| [一人公司](docs/260317-illustrated.md) | 借助AI创办一人企业的图文指南——六个步骤、推荐技术栈与90天路线图（中文） |

### 七、OpenClaw 🦞 平台

| 文章 | 简介 |
|---|---|
| [openclaw-update](docs/260525-openclaw-update.md) | OpenClaw平台最近的更新和发展 |
| [openclaw-custom-skills_chn](docs/260407-openclaw-custom-skills-chn.md) | OpenClaw 自定义技能从构建到发布 ClawHub 的完整教程（简体中文） |
| [openclaw-custom-skills](docs/260406-openclaw-custom-skills.md) | 在ClawHub上构建、校验、测试与发布自定义技能的完整教程 |
| [openclaw-security](docs/260327-openclaw-security.md) | OpenClaw安全审计：真实事件、已知漏洞及面向自托管用户的分级加固清单（中文） |
| [openclaw-security_eng](docs/260327-openclaw-security-eng.md) | OpenClaw安全审计英文版：真实事件、已知漏洞及自托管用户加固清单 |
| [openclawActivity2](docs/260320-openclaw-activity2.md) | 近期OpenClaw使用记录：安装配置与日常活动日志 |
| [openclaw-thoughts](docs/260313-openclaw-thoughts.md) | 将OpenClaw作为本地AI代理平台运行的个人笔记：可组合性、技能与实战心得（中文） |

### 八、已发布技能（ClawHub）

在本仓库中开发，每次推送时自动发布到 [ClawHub](https://clawhub.ai/j3ffyang) 上。

| 技能 | 简介 |
|---|---|
| [rdr2-playthrough](https://clawhub.ai/j3ffyang/skills/rdr2-playthrough) | Use when maintaining RDR2 (Red Dead Redemption 2) playthrough notes — logging an acquisition ("acquired X", "got N gold bars", "finished X"), answering in-game location/crafting questions, or reviewing the notes for duplicate or stale info. Triggers on RDR2, Red Dead Redemption, playthrough, legendary animal, talisman, trinket, valerian root, gold bar, horse, weapon, berry. |
| [astro-sync](https://clawhub.ai/j3ffyang/skills/astro-sync) | Convert and polish a Markdown article into AstroPaper-compatible post format for the astro_journal blog (everbox.io). Use when the user wants to publish or sync an article (e.g. from ai-thoughts/docs/ or history/docs/) to the Astro blog, convert Markdown to Astro format, add AstroPaper frontmatter, or move images into src/assets/images/. |
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

### 九、草稿与工作笔记

旧版文章与其最终版并存，是为了让每一篇都展示从头脑风暴文档到成稿的演变过程。以下是促成（或正在促成）上述文章的草稿。

| 草稿 | 说明 |
|---|---|
| [opencode-openrouter-model-selection](docs/260922-opencode-openrouter-model-selection.md) | 通过 OpenRouter 为 OpenCode 选择模型与供应商——区分模型来源与推理服务所在地、数据隐私风险分级、DeepSeek/Qwen/GLM/Kimi/Gemini/OpenAI 价格对比，并附可复现的 curl/Python 取价脚本 |
| [ground-truth-and-growth](docs/260825-ground-truth-and-growth.md) · [真相与成长](docs/260825-ground-truth-and-growth-chn.md) | 与 AI 智能体共同成长的反思——选择 OpenCode、学习 AI 协作的节奏、发现 Git 自动化，在终端计算中找到冥想般的诚实 |
| [death-thought-flow](docs/260817-death-thought-flow.md) | Personal thought-flow master for the death-in-Mexico project — seven thinking points, six content sections, verified facts, and cultural guardrails; use with the story-telling skill to generate a narration script or essay |
| [ai-video-pipeline](docs/260816-ai-video-pipeline.md) | How a 60-second AI video trailer was built from eight photos with five OpenCode skills, an 8-stage thought-flow loop, and two content-policy failures that became codified gates |
| [ai-video-recommendations](docs/260816-ai-video-recommendations.md) | Ten rules for making AI videos with image-to-video engines — story-first scripting, delegated vision, audio decoupling, and a resumable pipeline that turns failures into codified skills |
| [ollama-to-llamacpp](docs/260803-ollama-to-llamacpp.md) · [从Ollama切换到llama.cpp](docs/260803-ollama-to-llamacpp-chn.md) | 在Arch Linux（GPD）上把本地LLM推到极限：从Ollama切换到llama.cpp，精细控制VRAM、提升效率与输出质量（qwen2.5:14b） |
| [ai-combination（完整 v1.1）](docs/260701-ai-combination.md) · [模板](docs/260701-ai-combination-template.md) | 精炼版 ai-combination 文章背后的完整版与种子模板 |
| [web-search 简报](docs/260425-web-search.md) | 基于 web_search 构建简报技能的笔记（OpenClaw/Hermes） |
| [openclaw-custom-skills（早期草稿）](docs/260406-writing-your-own-custom-skill-in-openclaw.md) | OpenClaw 自定义技能教程的早期迭代版本 |

---

> **维护说明：** 编辑 [`articles.yaml`](articles.yaml)，然后运行 `python scripts/gen_readmes.py` 重新生成 `README.md` 与 [`README_zh.md`](README.md)。
> "已发布技能"表格根据各 `.opencode/skills/*/SKILL.md` 的 frontmatter 自动生成，并链接到对应 ClawHub 页面。文章分区按最新文章排序，草稿固定在末尾。

