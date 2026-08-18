# 如何将 Hermes Agent 技能 (skill) 移植到 OpenCode

**原文：** [260811-port-skill-to-opencode.md](260811-port-skill-to-opencode.md)

![将技能从 Hermes Agent 移植到 OpenCode — 视觉摘要](../imgs/260818-port-skill-to-opencode.png)

除了从头编写技能 (skill)，你也可以移植现有的。移植复用经过测试、久经考验的逻辑——保留主体，只调整 OpenCode 需要的部分。本仓库中的 `custom-infographic` 技能（`.opencode/skills/custom-infographic/`，前身为 `baoyu-infographic`）就是一个移植实例，来自 [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) v1.56.1，通过 Hermes Agent ⚕ 完成。

## 1. 理解两种格式

Hermes Agent ⚕ 技能和 OpenCode 技能在结构上完全相同：一个 `SKILL.md` 加上前置元数据 (frontmatter)，以及可选的 `references/` 和 `scripts/` 文件夹。布局完全一致，因此移植主要是修改前置元数据加上快速测试。

不同之处在于前置元数据。Hermes ⚕ 技能通常包含：

```yaml
---
name: some-skill
description: What it does
license: MIT
---
```

OpenCode 使用相同的 `name`、`description` 和 `license` 字段。额外可选两个字段：`metadata`（标注原作者，用于发布）和 `compatibility`（仅信息用途——OpenCode 的加载器 (loader) 会忽略它，但它记录了技能的目标平台）：

```yaml
---
name: some-skill
description: A trigger-friendly description with keywords like "信息图", "visual summary", or "generate a poster"
license: MIT
compatibility: opencode
metadata:
  author: Original Author
  upstream: https://github.com/author/some-skill
  version: 1.0.0
---
```

## 2. 复制技能并重写前置元数据

1. 将技能文件夹复制到 `.opencode/skills/`（项目级）或 `~/.config/opencode/skills/`（用户全局）：`cp -r ~/.hermes/skills/some-skill .opencode/skills/`
2. 重命名技能文件夹以避免与原始版本混淆——例如 `baoyu-infographic` 改为 `custom-infographic`。前置元数据中的 `name` 字段跟随文件夹名称。在 `metadata` 块中保留原作者姓名以示尊重。
3. 保留原始的 `description` 和 `license`。
4. 添加 `compatibility: opencode`（可选，仅信息用途——OpenCode 忽略它，但它记录了技能的目标平台）。
5. 重写 `description`，使 OpenCode 的技能路由器 (skill router) 能匹配到它：包含用户会输入的动作动词和关键词，英文和中文都加上。路由器匹配的是这段文本，而不是文件名——描述太模糊意味着技能永远不会被触发。
6. 添加 `metadata` 块，标注原作者和上游仓库——这是良好的归属 (attribution) 实践。OpenCode 的加载器会忽略它，但它对浏览技能文件夹的人以及发布到 ClawHub 很有用。

## 3. 修复路径和依赖

技能主体很少需要改动；需要关注的是路径和环境。

- `references/` 和 `scripts/` 与 `SKILL.md` 同级——只要复制整个文件夹（而不是只复制文件），相对路径引用（如 `references/layouts/bento-grid.md`）就能继续工作。注意 OpenCode 只从项目工作树 (worktree) 内部加载技能——如果原始技能引用了仓库外部的路径（如 `~/.hermes/...`），那些引用会失效。
- 检查硬编码路径：Hermes ⚕ 技能可能假设 `~/.hermes/...` 或自己的技能目录；OpenCode 技能从项目目录运行，因此优先使用相对路径或环境变量。
- 检查外部依赖：命令（`which python3`）、Python 包或 API 密钥。`custom-infographic` 移植版需要 `OPENROUTER_API_KEY` 用于图像生成——在环境中设置或在 SKILL.md 中说明。
- 对捆绑的脚本执行 `chmod +x`。

## 4. 在 OpenCode 中测试

1. 启动新的 OpenCode 会话 (session)，让它加载新技能（技能在会话启动时加载，不会热重载）。
2. 用触发词请求该技能的功能（例如 "make an infographic about X"）。
3. 如果没有被触发，优化 `description`——路由器匹配的是文本。
4. 端到端运行一次技能的完整工作流，修复错误输出揭示的问题。

就是这样——移植比从头编写更快，并且保留了原作者经过测试的行为。`custom-infographic` 移植版已经过多次测试，持续稳定工作，`imgs/` 中有输出证明——一个经过实战检验的移植技能比从头编写的新技能更可靠。

关于许可 (license) 的说明：移植 MIT 许可的技能没有问题，只要保留原始许可和作者归属。如果你计划将移植版发布到 ClawHub，请在 `metadata` 块中保留原作者姓名——即使许可允许，重新发布时不注明归属也会造成混乱。

btw, i use arch 
