# 备份 Hermes Agent

**核心要点：** 定期备份你的 `~/.hermes` 目录。用 `hermes backup` 做全量快照，或者 `hermes backup --quick` 只备份关键文件。把生成的 zip 存到安全的地方。

## 为什么要定期备份

这话你都听了一千遍了——记得备份数据。我本人是每天跑一次备份。原因嘛，无非就这几个：

- 在翻车之前先备份（崩溃这种事谁说得准）
- 换电脑迁移数据
- 出问题了可以回滚

## 备份 Hermes 数据

### Hermes 自带备份命令

Hermes 的核心记忆、人格设定和配置都放在 `~/.hermes/` 里。

自带的 CLI 命令可以创建一个完整的、带时间戳的压缩包：

```bash
hermes backup
```

跑起来大概长这样：

```sh
hermes backup
Scanning ~/.hermes ...
Backing up 4579 files ...
  500/4579 files ...
  ...
  4500/4579 files ...

Backup complete: /home/jeff/hermes-backup-2026-06-01-101955.zip
  Files:       4579
  Original:    311.7 MB
  Compressed:  129.1 MB
  Time:        14.8s

  Excluded directories:
    checkpoints/
    hermes-agent/
    node/lib/node_modules/
    skills/autonomous-ai-agents/hermes-agent/

Restore with: hermes import hermes-backup-2026-06-01-101955.zip
```

**小贴士：** 如果你只需要配置、会话记录、API 密钥和认证信息这些核心数据，用 `--quick` 参数就行了。快得多，不用扫一遍所有文件：

```bash
hermes backup --quick
```

这个命令底层用的是 SQLite 的 `backup()` API，所以就算 Hermes 正在运行，也能安全备份。

### 手动 / 脚本备份

如果你想自己写脚本备份，记得带上这几个东西：

- **`~/.hermes/SOUL.md`** — agent 的核心身份（人格、语气、行为边界）
- **`~/.hermes/memories/MEMORY.md`** 和 **`~/.hermes/memories/USER.md`** — agent 跨会话的记忆：环境信息、使用习惯，还有你的个人偏好
- **`~/.hermes/skills/`** — 自定义技能和自动学会的能力
- **`$HERMES_HOME/.env`** — API 密钥和机器人 token。把这文件当成你的银行卡来保管。当 Hermes 弹出权限请求要读它（为了访问外网模型），搞清楚你在授权什么。我一般只批准一次。

`hermes backup` 命令已经自动帮你打包上面这些了。但如果你想自己写脚本，或者想更精细地控制备份内容，上面就是关键文件清单。

#### 关于技能 (skills) 和缓存 (cache) 输出目录的说明

有些自定义技能如果没指定输出目录，生成的东西（文章、图片等）会丢到 `~/.hermes/skills/` 或 `~/.hermes/cache/` 里。这个很容易漏掉——跑完了你可能都找不到那些文件。如果发现技能产出的东西不见了，去这两个目录翻翻。

## `~/.hermes/state.db` —— 要不要备份？

如果你只是日常聊聊天，这个数据库不备份也没太大关系。但如果你在意聊天记录——比如想搜索之前的对话，或者建个**语义索引**——那就一定要留一份。来看看里面都有什么：

### 核心数据类型

数据库里存的是：

- **消息历史** —— 每一条用户消息、agent 回复、推理步骤、工具调用和工具返回结果
- **会话元数据** —— 会话 ID、标题、来源平台（CLI、Telegram、Discord 等）、时间戳
- **经济数据** —— 输入/输出的 token 数和每次会话的大致花费
- **模型配置** —— 每次会话用的模型名称、系统提示词和配置参数

### 数据库结构

根据官方文档，数据库的表结构是这样的：

- **`sessions`** —— 会话元数据、token 数、计费信息
- **`messages`** —— 每个会话的完整消息历史
- **`messages_fts`** / **`messages_fts_trigram`** —— FTS5 虚拟表，用来快速全文搜索所有对话记录
- **`state_meta`** —— 一个简单的键值表，存通用元数据

如果你决定要备份这个数据库，记得用 SQLite 的在线备份 API，不要直接复制文件——这样才能保证数据一致性。`hermes backup` 命令已经自动帮你处理好这些了。

所以，去跑一遍 `hermes backup`，把生成的 zip 存好吧。
