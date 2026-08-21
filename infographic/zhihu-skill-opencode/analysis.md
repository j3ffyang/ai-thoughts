---
title: "知乎 技能 + CLI —— 在 OpenCode 中的安装与配置"
topic: "technical/tutorial"
data_type: "process"
complexity: "moderate"
point_count: 6
source_language: "zh"
user_language: "zh"
---

## Main Topic
如何在 OpenCode 中安装并配置知乎官方 `zhihu` 技能与 `zhihu-cli`，重点是无头环境下用环境变量完成认证的路径。

## Learning Objectives
After viewing this infographic, the viewer should understand:
1. 知乎 `zhihu` 技能是什么、它能做什么（搜索、热榜、直答、本人内容）
2. 官方 CLI 如何安全安装（清单校验、无 sudo、不修改 PATH）以及无头环境下如何用 `ZHIHU_ACCESS_SECRET` 完成认证
3. 如何验证初始化成功，以及 Access Secret 的安全使用边界

## Target Audience
- **Knowledge Level**: 中级（熟悉终端与 CLI，但可能不了解无头环境与密钥链）
- **Context**: 想在 OpenCode 中使用知乎开放平台能力的开发者/Agent 用户
- **Expectations**: 得到一份可照做的安装→认证→验证→安全清单

## Content Type Analysis
- **Data Structure**: 线性流程——技能是什么 → 安装 CLI → 认证 → 验证 → 安全说明
- **Key Relationships**: 无头环境缺失 D-Bus → 密钥链不可用 → 回退到 `ZHIHU_ACCESS_SECRET` 环境变量
- **Visual Opportunities**: 命令、状态码、错误码可作高亮标签；流程步骤用箭头串联；无头 vs 桌面环境可用左右对比

## Key Data Points (Verbatim)
- "zhihu-cli 0.3.0"
- "linux-amd64"
- "installed: true" 与 "compatible: true"
- "最低要求 0.1.0"
- "KEYCHAIN_UNAVAILABLE"
- "source: environment"
- "脱敏值 (masked) f8af...657d"
- "keychain: unavailable"
- "verification: valid"
- "Code 0, success"
- "不需要 sudo，也不修改 PATH"
- 安装路径 "~/.local/share/zhihu-cli/current/zhihu-cli"

## Layout × Style Signals
- Content type: process/tutorial → suggests linear-progression、winding-roadmap
- Tone: technical → suggests technical-schematic、ikea-manual
- Audience: 中文技术用户 → suggests technical-schematic、hand-drawn-edu
- Complexity: moderate → 中等密度布局，分节清晰

## Design Instructions (from user input)
无（用户未指定额外设计偏好）

## Recommended Combinations
1. **linear-progression + technical-schematic** (Recommended): 安装→认证→验证的线性流程，蓝图为底的工程风格贴合 CLI 主题
2. **winding-roadmap + ikea-manual**: 把配置过程当作一段旅程，极简线条手册风
3. **bento-grid + craft-handmade**: 分块总览五个环节，手作风降低技术门槛
