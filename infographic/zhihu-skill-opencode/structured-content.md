# 知乎 技能 + CLI —— 在 OpenCode 中的安装与配置

## Overview
在 OpenCode 中安装并配置知乎官方 `zhihu` 技能与 `zhihu-cli`：技能能做什么、CLI 如何安全安装、无头环境如何用 `ZHIHU_ACCESS_SECRET` 完成认证、如何验证与安全使用。

## Learning Objectives
The viewer will understand:
1. 知乎 `zhihu` 技能是什么，以及它能提供哪些能力
2. 官方 CLI 如何被安全安装（校验、无 sudo、不修改 PATH）
3. 无头环境下密钥链不可用时，如何用 `ZHIHU_ACCESS_SECRET` 环境变量完成认证
4. 如何验证初始化成功，以及 Access Secret 的安全使用边界

---

## Section 1: 技能是什么

**Key Concept**: `zhihu` 技能通过官方 CLI（`zhihu-cli`）接入知乎开放平台。

**Content**:
- 位置：`.opencode/skills/zhihu/`，会话启动时自动发现
- `search zhihu` —— 社区回答
- `search global` —— 全网搜索
- `hot` —— 热榜
- `answer` —— 知乎直答
- `me ...` —— 当前用户自己的内容
- 原始 HTTP API、OAuth 与 MCP 文档只在开发接入场景才读取

**Visual Element**:
- Type: 中心辐射图标图
- Subject: CLI 图标居中，五种能力向外辐射
- Treatment: 每个能力配一个图标 + 命令名

**Text Labels**:
- Headline: "技能是什么"
- Labels: "search zhihu", "search global", "hot", "answer", "me ..."

---

## Section 2: 安装 CLI

**Key Concept**: 技能包不携带二进制，由 `scripts/setup.sh` 从官方清单安全下载安装。

**Content**:
- 下载 `zhihu-cli 0.3.0`（`linux-amd64`）
- 校验：域名、文件大小、SHA-256、归档结构、二进制自报版本
- 安装到 `~/.local/share/zhihu-cli/current/zhihu-cli`（XDG 用户数据目录）
- 不需要 sudo，也不修改 PATH
- 状态检查：`installed: true` 与 `compatible: true`（最低要求 0.1.0，无可用更新）

**Visual Element**:
- Type: 编号步骤图标（1→5 箭头串联）
- Subject: 下载→校验→安装→检查
- Treatment: 每步一个编号图标，箭头指向下一步

**Text Labels**:
- Headline: "安装 CLI"
- Labels: "0.3.0", "installed: true", "compatible: true", "无 sudo", "PATH 不变"

---

## Section 3: 无头 (headless) 环境下的认证

**Key Concept**: 无头环境没有桌面会话 D-Bus，密钥链不可用，改用 `ZHIHU_ACCESS_SECRET` 环境变量完成认证。

**Content**:
- 无头环境：没有图形界面，只能通过命令行或 SSH 交互（远程服务器、CI 构建机、容器）
- `auth set --secret-stdin` 通常写入操作系统密钥链（Linux 为 Secret Service/D-Bus，如 GNOME Keyring）
- 本机无可用会话 D-Bus → 返回 `KEYCHAIN_UNAVAILABLE`；CLI 不把凭证降级保存为普通文件
- 回退方案：进程级环境变量 `ZHIHU_ACCESS_SECRET`，由宿主注入
- 业务命令优先读取环境变量、其次读密钥链；环境变量存在但无效时不静默回退
- `auth status` 确认：`source: environment`，脱敏值 `f8af...657d`，`keychain: unavailable`

**Visual Element**:
- Type: 左右对比图
- Subject: 桌面环境（密钥链 ✔）vs 无头环境（密钥链 ✘ → 环境变量）
- Treatment: 中间用箭头表示"回退"

**Text Labels**:
- Headline: "无头环境下的认证"
- Left: "桌面 · Secret Service/D-Bus"
- Right: "无头 · ZHIHU_ACCESS_SECRET"
- Labels: "KEYCHAIN_UNAVAILABLE", "source: environment"

---

## Section 4: 验证

**Key Concept**: 初始化用两次联网调用验证（都会消耗接口额度）。

**Content**:
- `auth status --verify` → `verification: valid`（发起一次本人内容请求）
- `me contents --type all --limit 1` → `Code 0, success`，内容列表为空（空列表同样视为通过）
- 技能现已可用于搜索、热榜、知乎直答以及读取用户本人的内容

**Visual Element**:
- Type: 检查清单图标
- Subject: 两条带 ✓ 状态的命令
- Treatment: 绿色通过标记

**Text Labels**:
- Headline: "验证"
- Labels: "verification: valid", "Code 0, success"

---

## Section 5: 安全说明

**Key Concept**: Access Secret 只通过标准输入或环境变量传入，绝不落盘、绝不提交。

**Content**:
- 只通过 stdin（`auth set --secret-stdin`）或 `ZHIHU_ACCESS_SECRET` 环境变量传入
- 绝不在回复中复述
- 绝不写入技能目录、项目目录或 `.env` 文件
- 也绝不提交
- `.opencode/skills/zhihu/` 目录目前尚未被 git 跟踪，提交仍待处理

**Visual Element**:
- Type: 图标列表
- Subject: 四条禁止项（✘ 复述 / ✘ 落盘 / ✘ .env / ✘ 提交）
- Treatment: 每条一个禁止符号图标

**Text Labels**:
- Headline: "安全说明"
- Labels: "stdin", "ZHIHU_ACCESS_SECRET", "不落盘", "不提交"

---

## Data Points (Verbatim)

### Statistics
- "zhihu-cli 0.3.0"（linux-amd64）
- "最低要求 0.1.0"

### Status Codes
- "installed: true"
- "compatible: true"
- "KEYCHAIN_UNAVAILABLE"
- "source: environment"
- "脱敏值 (masked) f8af...657d"
- "keychain: unavailable"
- "verification: valid"
- "Code 0, success"

### Key Terms
- **无头 (headless) 环境**: 没有图形界面的机器，只能通过命令行或 SSH 交互，例如远程服务器、CI 构建机或容器
- **密钥链 (keychain)**: 操作系统存储凭证的组件，Linux 桌面为 Secret Service/D-Bus（如 GNOME Keyring）
- **Access Secret**: 用户在 https://developer.zhihu.com/profile 生成，用于开放平台鉴权
- **接口额度 (API quota)**: 在线验证与业务调用会消耗的开放平台额度

### 安装路径
- "~/.local/share/zhihu-cli/current/zhihu-cli"（XDG 用户数据目录）

---

## Design Instructions

### Style Preferences
- 无（用户未指定）

### Layout Preferences
- 无（用户未指定）

### Other Requirements
- 面向中文读者，正文用简体中文
- 技术命令与状态码保持英文原样（technical-schematic 风格下适合蓝底白字/工程图纸风）
