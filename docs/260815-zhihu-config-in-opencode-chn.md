# 知乎 技能 (skill) + CLI —— 在 OpenCode 中的安装与配置

本文记录 `zhihu` 技能 (skill)（v0.3.0）及其官方 CLI 在本机 OpenCode 中的安装与配置过程，包括无头 (headless) 环境下绕道完成认证的部分。以下事实均于 2026-08-15 通过实际运行命令验证，并非凭记忆写成。

## 技能 (skill) 是什么

`zhihu` 技能通过官方 CLI（`zhihu-cli`）接入知乎开放平台 (open platform)。在 OpenCode 中，它位于 `.opencode/skills/zhihu/`，会话 (session) 启动时自动发现。日常任务全部走 CLI —— `search zhihu`（社区回答）、`search global`（全网搜索）、`hot`（热榜）、`answer`（知乎直答）以及 `me ...`（当前用户自己的内容）；而原始 HTTP API、OAuth 与 MCP 文档只在开发接入场景才读取。

## 安装 CLI

技能包不携带二进制 (binary)。用户授权后，`scripts/setup.sh` 读取官方清单 (manifest)，下载适用于 `linux-amd64` 的 `zhihu-cli 0.3.0`，依次校验域名、文件大小、SHA-256、归档结构 (archive structure) 与二进制自报版本后，安装到 `~/.local/share/zhihu-cli/current/zhihu-cli`（XDG 用户数据目录）。不需要 sudo，也不修改 PATH。随后的状态检查返回 `installed: true` 与 `compatible: true`（最低要求 0.1.0，无可用更新）。

## 无头 (headless) 环境下的认证

无头 (headless) 环境指没有图形界面 (GUI) 的机器——"无头"即没有显示器、没有桌面，只能通过命令行或 SSH 交互，例如远程服务器、CI 构建机或容器。因为没有桌面会话，也就没有图形密钥链可用的 D-Bus，所以本机只能用环境变量存凭证。

Access Secret 由用户在 https://developer.zhihu.com/profile 自行生成。`auth set --secret-stdin` 通常把凭证 (credential) 写入操作系统密钥链 (keychain) —— 在 Linux 上是 Secret Service/D-Bus（如 GNOME Keyring）。本机没有可用的会话 D-Bus，首次尝试因此返回 `KEYCHAIN_UNAVAILABLE`；CLI 刻意不把凭证降级保存为普通文件。

按照 CLI 文档，面向 SSH/CI/容器这类环境的回退方案是进程级环境变量 (environment variable) `ZHIHU_ACCESS_SECRET`，由宿主（这里是 opencode）注入。业务命令优先读取环境变量、其次才读密钥链，且当环境变量存在但无效时不会静默回退。`auth status` 确认了这一切换：`source: environment`，脱敏值 (masked) `f8af...657d`，`keychain: unavailable`。

## 验证

初始化用两次联网调用验证（都会消耗接口额度 (API quota)）：

- `auth status --verify` → `verification: valid`（发起一次本人内容请求）。
- `me contents --type all --limit 1` → `Code 0, success`，内容列表为空 —— 空列表同样视为通过。

技能现已可用于搜索、热榜 (hot list)、知乎直答以及读取用户本人的内容。

原始 HTTP API 冒烟测试 (smoke test)：

```bash
curl -G 'https://developer.zhihu.com/api/v1/content/zhihu_search' --data-urlencode 'Query=怎么理解opensource文 化'   -H "Authorization: Bearer $ZHIHU_ACCESS_SECRET" -H "X-Request-Timestamp: $(date +%s)" -H 'Content-Type: application/json'
```

## 安全说明

Access Secret 只通过标准输入 (stdin)（`auth set --secret-stdin`）或 `ZHIHU_ACCESS_SECRET` 环境变量传入，绝不在回复中复述，绝不写入技能目录、项目目录或 `.env` 文件，也绝不提交。`.opencode/skills/zhihu/` 目录目前尚未被 git 跟踪 (tracked)，提交仍待处理。

## 参考

- [知乎开发者文档 —— zhihu CLI](https://developer.zhihu.com/docs?key=zhihu_cli)

btw, i use arch
