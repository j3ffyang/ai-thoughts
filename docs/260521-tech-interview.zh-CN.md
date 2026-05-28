# 从 Prompt 到 Output：AI Agent 日常用法

## 1. 心法
- 输出不对劲？先翻 **prompt** — 需求没讲明白，八成是你这边的问题，别急着怪 agent
- 其实就是把故事讲清楚，比如，曹雪芹的红楼梦。一个章节一个章节地讲述

## 2. 环境（前置）
- 没有的话，更新 `~/.openclaw/SOUL.md` 和 `~/.hermes/SOUL.md`，让 agent 更贴合你的场景
- 会看 markdown
- **Linux** 最好；**macOS** 也行。尽量别在 **Windows** 上跑 agent：
  - 管理员权限太大，容易动到整个系统
  - PowerShell 对系统可选，但 agent 经常要用，多一层麻烦
- 学点 Unix/Linux，用 **非 root** 用户操作
- Python 会一点更好
- **结果文件命名**（OpenClaw 和 Hermes）：`YYMMDD` + 时间 + 主题 + 子主题，例如 `2605211430-report-summary.md`
  - 文件名别带空格
  - 知道输出存哪。默认路径：`~/.openclaw`、`~/.hermes`（配置、skills、状态，含对话历史和输出文件）

## 3. Skills（个人看法）
- 大多时候自己写
- 使用别人的可以去 https://clawhub.ai、https://www.skills.sh、https://hermes-agent.nousresearch.com/docs/skills 
- 装了的 Skill 到底干啥，搞明白再用
- skills 和 plugins **按需装** — 性能和安全的考虑。**Skills**：AI 自己决定啥时候用。**Plugins**：自动挂钩（比如邮件），不用 AI 选
- **特别长的 Skill 文件** 多留个心眼；难审，也更容易藏你不想要的东西

## 4. Prompt 和语言
- 要写得准，个人感觉 **prompt 用英文** 往往比中文或其他语言省事
- 措辞要准；拿不准可以用 Gemini、Perplexity 等对一下
- **prompt** 短而准 — 省 token，也少出错
- 工作 **从大拆到小**（目标 → 步骤 → 单个小任务）
- 同一会话里别重复发一样，或者相对矛盾的消息，比如，你说7点约会吃放。然后，又改为6点。容易混淆
- **新任务 → 新会话** — 无关的历史会话会被当 prompt 上下文塞进来
- 别在老 prompt 上一直改来改去，agent 会懵。干脆开新的

## 5. 工作方式
- **架构思维**：先整体后细节，一步一步来（比如盖房：规划 → 买料 → 地基 → 水电、布线、贴砖、刷漆 → 收尾）
- 能独立的活儿 **并行** 干（比如水电、布线、贴砖可以同时搞）
- 一次搞不完的，拆成小步；从小处着手
- **护栏**：说清楚什么不能做（比如「全部用 Python，别碰 Java」）

## 6. 质量和测试
- 上线前让 AI 帮你过一遍 `SKILL.md`
- 开 verbose，盯着测试跑
- **SKILL.md**：标准 skill markdown — YAML frontmatter + 用人类自然语言写的声明式说明

## 7. 安全
- 只信 **官方文档和仓库**（比如 Nous、https://clawhub.ai）
- 平时多长个心眼
- Skill 文件特别长的话，信任度放低 — 装之前先搞清楚

## 8. 收尾
- AI 和 agent 变得快 — 保持好奇，持续学习
