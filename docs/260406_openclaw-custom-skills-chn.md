
![customSkill](../imgs/2604061410_openclaw-custom-skills.png)

## 入门

我最近花时间帮一位经营多家便利店的朋友，琢磨如何用 AI 提升效率。那次对话催生了一个想法：与其依赖现成的 Skill，不如在 OpenClaw 里自己写？事实证明，完全可行。

本指南会带你走完完整流程——从定义你想构建什么，到编写 Skill、测试，再到 ClawHub 上部署。

## 先配置好你的模型

在写 Skill 之前，确保语言模型和图像模型已正确配置。多数情况下，OpenClaw 使用能同时处理文本和图像的多模态模型。但若需要高质量生成图像，应显式设置 `imageGenerationModel`。

先列出当前模型：

```sh
openclaw models list
```

你可能会看到类似输出：

```sh
🦞 OpenClaw 2026.4.5 (3e72c03)
   Your task has been queued; your dignity has been deprecated.

Model                                      Input      Ctx      Local Auth  Tags
anthropic/claude-haiku-4-5-20251001        text+image 195k     no    yes   default,configured
openai/gpt-5.1-codex                       text+image 391k     no    yes   configured,alias:GPT
openai/gpt-5-mini                          text+image 391k     no    yes   configured
google/gemini-3-flash-preview              text       195k     no    yes   configured,alias:gemini-flash
moonshot/kimi-k2.5                         text+image 250k     no    yes   configured,alias:Kimi
```

在我的环境中，`openai/gpt-image-1` 被定义为 `agents.defaults.imageGenerationModel`。API 密钥存放在 `~/.openclaw/.env`—— 需要像保管信用卡一样妥善保管该文件。

```json
openclaw config get agents.defaults.imageGenerationModel

🦞 OpenClaw 2026.4.5 (3e72c03)
   I don't sleep, I just enter low-power mode and dream of clean diffs.

{
  "primary": "openai/gpt-image-1",
  "fallbacks": [
    "google/gemini-3-pro-image-preview",
    "fal/fal-ai/flux/dev"
  ]
}
```

## 动手之前先想清楚

写任何代码之前，最重要的一步是：坐下来用一份 Markdown 文档，把 Skill 要做什么写清楚。

假设你要做一个润色技术博客的 Skill，可以这样记录：

- **输入：** 关于技术主题的原始 Markdown 草稿（例如 Linux 文件同步工作流）
- **处理：** 将草稿改写为 1,000–1,200 字的精炼 en-US 英文，分为 4–5 个逻辑章节
- **保留：** 所有技术术语、代码块、文件路径和命令示例保持原样
- **输出：** 整理后的 Markdown 文件，以及一张概括全文的头图
- **风格：** 使用一致的视觉语言（例如「简洁扁平矢量插画，极简等距风格」）
- **分辨率：** 以 16:9 比例生成图像，适合作为博客头图

写清楚之后，用任意 AI 工具分析一遍（我个人偏好 Perplexity），你就有了蓝图。

## 创建你的 SKILL.md

接下来编写实际的 Skill 定义，在这里定义输入、输出和工作流。

典型的 SKILL.md 包含两部分：YAML frontmatter 和 Markdown 文档。下面是一个真实示例：

```yaml
---
name: blog-polish-eng-single-image
description: Polish a technical blog draft into a 1000–1200 word, 4–5 section en-US article, preserve technical terms/code, and generate one consistent hero image prompt.
author: Jeff Yang
version: 1.0.5
tags: [openclaw, clawhub, blog, polish, translate, markdown, images, prompts]
triggers: ["polish blog", "technical blog images", "blog draft images"]
metadata:
  openclaw:
    requires: []
    platforms: ["linux", "darwin"]
    env: []
inputSchema:
  type: object
  properties:
    draftPath:
      type: string
      description: Path to the draft markdown. Defaults to ~/.openclaw/workspace/contentDraft/latestDraft.md
    outputDir:
      type: string
      description: Directory to save outputs. Defaults to ~/.openclaw/workspace/contentPolished/
    subject:
      type: string
      description: Short subject slug used in output filename (e.g. openclaw-skills). If omitted, infer from the draft title.
    style:
      type: string
      description: Visual style phrase reused for the hero image (e.g. "clean flat vector illustration, minimal isometric").
    background:
      type: string
      description: Background phrase reused for the hero image (e.g. "white background with subtle grid").
    aspectRatioHero:
      type: string
      description: Aspect ratio for hero image (e.g. "16:9 horizontal").
  required: []
outputSchema:
  type: object
  properties:
    polishedPath:
      type: string
      description: Path to the final polished markdown file.
    imagePath:
      type: string
      description: Path of the generated hero image, or intended filename if only a prompt was produced.
    imagePrompt:
      type: string
      description: Single-line prompt for the hero image.
---

# Blog Polish Skill

This skill rewrites a technical blog draft into a polished English article and generates exactly one hero image as a PNG, using one matching hero prompt. It is intended for drafts that already contain technical content, code, commands, or product details that should be preserved while improving clarity, structure, and reading flow.

## Purpose

Use this skill when you want to turn a rough technical draft into a publishable article without losing domain-specific detail. The output should read naturally in en-US English, stay faithful to the original meaning, and keep technical terms, identifiers, code blocks, file paths, and command examples intact unless a correction is clearly needed.

This skill generates one hero image only. It does not create per-section images. The single hero image should summarize the whole article visually at a high level and should be consistent with the article’s subject and tone.

## When to use

Use this skill when the source draft is one of the following:

- A technical blog post that needs editing for clarity and flow.
- A translated draft that should be rewritten into natural en-US English.
- A markdown article that needs a better structure and cleaner sectioning.
- A post that should include one matching hero image prompt for later image generation.

Do not use this skill for short notes, changelogs, marketing copy, or posts that do not need technical preservation.

## Editing behavior

The rewrite should preserve the author’s intent while improving readability. Prefer shorter paragraphs, clearer transitions, and section headings that guide the reader through the main idea.

Rewrite the article in spoken, unofficial English that feels natural, clear, and conversational, while still preserving technical accuracy.

The skill should:

- Keep technical terms, product names, API names, file names, and command syntax accurate.
- Preserve code blocks, inline code, quoted commands, and URLs unless they are obviously wrong.
- Improve grammar, sentence flow, and article structure.
- Expand thin or fragmented notes into a coherent article when the source material supports it.
- Avoid inventing facts, results, benchmarks, or claims that are not present in the draft.

The skill should not:

- Rewrite code into prose.
- Remove essential technical details.
- Add unnecessary marketing language.
- Split the article into section images or multiple image prompts.

## Input fields

`draftPath` points to the source markdown draft. If omitted, the skill reads the default latest draft file from the workspace. This should contain the original article text, headings, and any code samples that need preservation.

`outputDir` sets where the polished markdown file and image filename should be saved. If omitted, the skill uses the default polished-content directory.

`subject` is used to build the output filename. If not provided, the skill should infer a short slug from the article title.

`style` defines the visual language for the hero image. Use one style phrase consistently so the image matches the article’s mood.

`background` defines the backdrop for the hero image. Keep it simple and reusable across posts for consistency.

`aspectRatioHero` controls the hero image shape. Typical values are `16:9 horizontal` or similar wide formats suitable for blog headers.

## Output

The skill produces one polished markdown file and one hero image prompt.

The polished file should contain:

- A cleaned-up title.
- A strong introduction.
- 3 to 5 content sections, depending on the source material.
- A concise closing section if appropriate.
- Preserved technical content where relevant.

The image output should contain:

- The image file must be written in the same directory as the markdown file and must use the same basename with a .png extension.
- One hero image filename or intended image path.
- One single-line hero prompt.
- A high-level visual summary of the article, not a section-by-section breakdown.

## Image policy

This skill intentionally generates one image only.

The image should be:

- A hero image for the whole article.
- Visually aligned with the topic and style.
- Broad enough to represent the subject without depending on individual section contents.
- Consistent with the same visual style and background settings used across posts.

The image should not be:

- A separate illustration for each section.
- A collage of unrelated concepts.
- Overly literal if the topic is abstract.
- Packed with too many technical labels or small details.

## Workflow

1. Resolve the draft and output paths.
2. Read the markdown draft.
3. Extract the title and basic structure.
4. Rewrite the article into polished en-US prose.
5. Save the polished markdown file.
6. Create one hero image prompt only.
7. Return the final file path, hero image path, and image prompt.

## Constraints

Maintain the meaning of the original draft. If the source contains code snippets, commands, paths, or configuration examples, keep them intact and formatted correctly. If the draft is sparse, improve clarity and organization, but do not fabricate missing technical content.

Keep the article focused and practical. Prefer specific explanations over generic filler. If the article has a narrow technical subject, the hero image should stay broad and conceptual rather than trying to depict every detail.

## Example usage

A draft about a Linux file synchronization workflow might be polished into a clear article with headings such as introduction, setup, common pitfalls, and conclusion. The hero image prompt could describe a clean technical illustration showing a laptop, file paths, and subtle sync arrows, but only as one overall image for the post.

## Implementation notes

The workflow should emit a single structured output object with these fields:

- `polishedPath`
- `imagePath`
- `imagePrompt`

The image must be written as a PNG file. It must use the same basename as the markdown file and be saved in the same directory as the markdown file. The skill should not emit arrays of images or prompts. It should not reference per-section image generation in the description, schema, or workflow.

Generate the image using OpenClaw’s default image model (`agents.defaults.imageGenerationModel`) unless an explicit image generation model is provided by the environment.
```

结构很直观：名称、描述、版本、输入参数和输出结构。把 Skill 做什么写清楚、写具体即可。

完整 SKILL.md 见：https://clawhub.ai/j3ffyang/blog-polish-eng-single-image

## 校验与迭代

发布前，用 Perplexity 或 Claude 等 AI 工具，对照 OpenClaw 与 ClawHub 标准审阅你的 SKILL.md。可使用如下提示词：

```
Review this SKILL.md for compliance with OpenClaw and ClawHub standards.
Check the JSON schema, descriptions, and workflow logic.
Suggest any improvements to clarity or structure.
```

多迭代几轮，直到你对 Skill 有信心。现在修好 schema 里的小问题，能省下日后大量调试时间。

## 本地安装与测试

对 SKILL.md 满意后，在本地安装：

```sh
cd ~/.openclaw/workspace/skills
clawhub install your-skill-name
```

列出已安装的 Skill 以确认：

```sh
clawhub list
```

输出中应能看到你的 Skill。接着在你配置的渠道（Discord、WhatsApp、Telegram 等）中测试：

```
trigger "your-skill-name"
```

在工作区目录查看输出，确认润色后的 Markdown 和生成的图像是否出现在预期位置。

## 部署到 ClawHub

确认 Skill 运行正常后，上传到 ClawHub：

```sh
clawhub publish ~/.openclaw/workspace/skills/your-skill-name
```

ClawHub 会校验 SKILL.md 并向社区开放。若将 shell 脚本标记为「可疑」，通常只是警告——只要信任自己的代码，即可放心。

发布后，任何人都可以用以下命令安装你的 Skill：

```sh
clawhub install your-username/your-skill-name
```

## 结语

掌握流程后，在 OpenClaw 中构建自定义 Skill 并不复杂：想清楚目标、写出符合标准的 SKILL.md、校验、本地测试，满意后再发布。从想法到社区可用工具，整个过程通常不到一小时。

你的 Skill 会成为个人效率工具箱的一部分——若做得好，也会成为社区工具箱的一部分。

---

tag: #openclaw #ai #opensource #linux #clawhub #skill
