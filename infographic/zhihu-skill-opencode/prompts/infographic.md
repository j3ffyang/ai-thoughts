Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: linear-progression
- **Style**: technical-schematic
- **Aspect Ratio**: 16:9
- **Language**: zh

## Core Principles

- Follow the layout structure precisely for information architecture
- Apply style aesthetics consistently throughout
- If content involves sensitive or copyrighted figures, create stylistically similar alternatives
- Keep information concise, highlight keywords and core concepts
- Use ample whitespace for visual clarity
- Maintain clear visual hierarchy

## Text Requirements

- All text must match the specified style treatment
- Main titles should be prominent and readable
- Key concepts should be visually emphasized
- Labels should be clear and appropriately sized
- Use the specified language for all text content

## Layout Guidelines

linear-progression: sequential progression showing steps, timeline, or chronological events.

Structure:
- Linear arrangement (horizontal)
- Nodes/markers at key points (numbered step nodes 1-5)
- Connecting line or path between nodes
- Clear start and end points
- Directional flow indicators (arrows)

Process variant: action steps, numbered sequence, step numbers, action icons.

Text placement: title at top, step titles at each node, brief descriptions below nodes, step numbers clearly visible.

## Style Guidelines

technical-schematic: technical diagrams with engineering precision and clean geometry.

Color palette:
- Primary: Blues (#2563EB), teals, grays, white lines
- Background: Deep blue (#1E3A5F) blueprint with grid
- Accents: Amber highlights (#F59E0B), cyan callouts

Blueprint variant: white on blue, measurements, grid pattern.

Visual elements: geometric precision, grid pattern, dimension lines, technical symbols and annotations, clean vector shapes, consistent stroke weights.

Typography: technical stencil or clean sans-serif, all-caps labels, measurement annotations.

---

Generate the infographic based on the content below:

# 知乎 技能 + CLI —— 在 OpenCode 中的安装与配置

## Overview
在 OpenCode 中安装并配置知乎官方 `zhihu` 技能与 `zhihu-cli`：技能能做什么、CLI 如何安全安装、无头环境如何用 `ZHIHU_ACCESS_SECRET` 完成认证、如何验证与安全使用。

## Section 1: 技能是什么

`zhihu` 技能通过官方 CLI（`zhihu-cli`）接入知乎开放平台。

- 位置：`.opencode/skills/zhihu/`，会话启动时自动发现
- `search zhihu` —— 社区回答
- `search global` —— 全网搜索
- `hot` —— 热榜
- `answer` —— 知乎直答
- `me ...` —— 当前用户自己的内容
- 原始 HTTP API、OAuth 与 MCP 文档只在开发接入场景才读取

## Section 2: 安装 CLI

技能包不携带二进制，由 `scripts/setup.sh` 从官方清单安全下载安装。

- 下载 `zhihu-cli 0.3.0`（`linux-amd64`）
- 校验：域名、文件大小、SHA-256、归档结构、二进制自报版本
- 安装到 `~/.local/share/zhihu-cli/current/zhihu-cli`（XDG 用户数据目录）
- 不需要 sudo，也不修改 PATH
- 状态检查：`installed: true` 与 `compatible: true`（最低要求 0.1.0，无可用更新）

## Section 3: 无头 (headless) 环境下的认证

无头环境没有桌面会话 D-Bus，密钥链不可用，改用 `ZHIHU_ACCESS_SECRET` 环境变量完成认证。

- 无头环境：没有图形界面，只能通过命令行或 SSH 交互（远程服务器、CI 构建机、容器）
- `auth set --secret-stdin` 通常写入操作系统密钥链（Linux 为 Secret Service/D-Bus，如 GNOME Keyring）
- 本机无可用会话 D-Bus → 返回 `KEYCHAIN_UNAVAILABLE`；CLI 不把凭证降级保存为普通文件
- 回退方案：进程级环境变量 `ZHIHU_ACCESS_SECRET`，由宿主注入
- 业务命令优先读取环境变量、其次读密钥链；环境变量存在但无效时不静默回退
- `auth status` 确认：`source: environment`，脱敏值 `f8af...657d`，`keychain: unavailable`

## Section 4: 验证

初始化用两次联网调用验证（都会消耗接口额度）。

- `auth status --verify` → `verification: valid`（发起一次本人内容请求）
- `me contents --type all --limit 1` → `Code 0, success`，内容列表为空（空列表同样视为通过）
- 技能现已可用于搜索、热榜、知乎直答以及读取用户本人的内容

## Section 5: 安全说明

Access Secret 只通过标准输入或环境变量传入，绝不落盘、绝不提交。

- 只通过 stdin（`auth set --secret-stdin`）或 `ZHIHU_ACCESS_SECRET` 环境变量传入
- 绝不在回复中复述
- 绝不写入技能目录、项目目录或 `.env` 文件
- 也绝不提交
- `.opencode/skills/zhihu/` 目录目前尚未被 git 跟踪，提交仍待处理

## Data Points (Verbatim)

- "zhihu-cli 0.3.0"（linux-amd64）
- "最低要求 0.1.0"
- "installed: true"
- "compatible: true"
- "KEYCHAIN_UNAVAILABLE"
- "source: environment"
- "脱敏值 (masked) f8af...657d"
- "keychain: unavailable"
- "verification: valid"
- "Code 0, success"
- 安装路径 "~/.local/share/zhihu-cli/current/zhihu-cli"
- 无头 (headless) 环境: 没有图形界面的机器，只能通过命令行或 SSH 交互
- 密钥链 (keychain): Linux 桌面为 Secret Service/D-Bus（如 GNOME Keyring）

Text labels (in zh):
- Title: "知乎 技能 + CLI —— 在 OpenCode 中的安装与配置"
- Step 1: "技能是什么" / "search zhihu" / "search global" / "hot" / "answer" / "me ..."
- Step 2: "安装 CLI" / "zhihu-cli 0.3.0" / "installed: true" / "compatible: true" / "无 sudo" / "PATH 不变"
- Step 3: "无头环境下的认证" / "KEYCHAIN_UNAVAILABLE" / "ZHIHU_ACCESS_SECRET" / "source: environment"
- Step 4: "验证" / "verification: valid" / "Code 0, success"
- Step 5: "安全说明" / "stdin" / "不落盘" / "不提交"
