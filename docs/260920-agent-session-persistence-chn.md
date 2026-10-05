# OpenCode 中的智能体会话持久化 (agent session persistence)

**原文：** [260920-agent-session-persistence.md](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260920-agent-session-persistence.md)

*OpenCode v1.18.34.*

当窗口关闭之后，一个编码智能体 (coding agent) 的会话去了哪里：`opencode -c` 如何恢复它、为什么累积起来的存储是团队或组织规模下的业务数据资产 (§2)、字节存在哪里、哪些可以复用、何时该清理，以及如何备份。

![信息图：OpenCode 会话持久化——恢复、SQLite 存储、模式规模、业务数据资产、压缩、清理与备份](../imgs/260920-agent-session-persistence.png)

## 1. 什么是会话，以及 `-c` 恢复什么

OpenCode 里的一个**会话 (session)** 就是一条对话线：一组有序的消息 (message)，每条消息又被拆成带类型的分段 (part)。经核实的分段类型有 `text`、`tool`、`reasoning`、`step-start`、`step-finish`、`patch`、`file`、`compaction` 和 `agent`，而消息本身只有 `user` 与 `assistant` 两种角色。`opencode -c`（或 `opencode --continue`）恢复**最后一个会话**；`-s <id>` / `opencode --session <id>` 恢复指定的那一个。帮助文本没有说明“最后一个”是否限定在当前项目内，所以这仍是一个待解决的问题。`--fork` 把会话复制成一个新会话再继续，原会话保持完好；迷你 (mini) 界面可以用 `--replay-limit` 和 `--no-replay` 限制或关闭历史重放——这些是迷你/TUI 参数，不在主 CLI 页面上。

## 2. 存储的会话日志作为业务数据资产 (business data asset, team / org)

持久化不只是“恢复我的聊天”。在团队规模下，这个数据库 (DB) 是一份**结构化、可查询的工作记录**——它很大一部分价值就在这里。

本机截至 2026-10-04 的存储里共有 **218 个会话**，每一个都带有 `model` 和 `agent`，其中 **132 个 `cost` 非零**；日志总计 **$23.67**，消耗 **94.7M 输入 / 4.44M 输出 token**。这些数字来自 `session` 本就维护的列——`cost`、`tokens_input/output/reasoning/cache_read/cache_write`——外加 `time_created`/`time_updated`、`project_id`、`agent` 和 `model`（以 JSON 存储，含 `id`、`providerID`、`variant`）。因为数据已经结构化，成本归集 (cost attribution) 与成本分摊 (chargeback) 无需解析转录 (transcript)：

```sql
SELECT p.worktree,
       json_extract(s.model,'$.id') AS model,
       COUNT(*)                     AS sessions,
       ROUND(SUM(s.cost), 2)        AS cost_usd,
       SUM(s.tokens_input + s.tokens_output) AS tokens
FROM session s JOIN project p ON p.id = s.project_id
GROUP BY p.worktree, model ORDER BY cost_usd DESC;
```

这个汇总就是成本展示/分摊、预算告警，以及发现哪里用更便宜的模型就够了（模型组合优化 (model-mix optimization)）的基础。每个项目的会话数与 token 量还能显示智能体真正加速了哪些工作流——以及哪些投入大、回报小。转录同时也是一条取证 (forensics) 线索（确切的命令、时间戳、触发它的那条消息），正如那次人格/临时产物事故复盘中所用的那样。而消息与分段是真实“问题→解法”配对的语料库；做语义索引 (§11) 之后，它们就成了内部知识库或入职材料。

现实的差距在于聚合：这是一个**每用户、单机的 SQLite 文件**，默认没有跨开发者、跨机器的汇总。真正的组织级分析意味着把这些存储（或 `opencode export` 导出的数据）汇集到一个数据仓库 (warehouse)——Postgres/pgvector、BigQuery 等等——那是一个项目，而不是一个功能。制衡 (counterweight) 在于敏感性：同一份数据包含源码、密钥和客户上下文，所以留存 (retention)、访问控制和脱敏是前提，而不是事后补充；`--sanitize` 不是 ZDR，也不是隐私保证——见 [`260927-opencode-openrouter-model-selection.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260927-opencode-openrouter-model-selection.md)。

## 3. 它存在哪里

一切都位于 XDG 数据目录之下：`~/.local/share/opencode/`（路径可由 `opencode db path` 打印）。存储是**单个 SQLite 数据库**，而不是“每个会话一个目录”：`opencode.db`，外加它的 `-wal` 与 `-shm` 附属文件。本机实测 `opencode.db` 为 **1.3 GB**，`log/` 28 MB，`snapshot/` 80 MB，`tool-output/` 35 MB，`auth.json` 4 KB（权限 `600`）。持久化**默认并非永久**：除非设置了 `OPENCODE_DISABLE_PRUNE`，否则 OpenCode 会清理旧数据，所以较旧的会话可能会被自动回收；`OPENCODE_DISABLE_AUTOCOMPACT` 同理可关闭自动压缩（见 §6）。

## 4. 目录与模式结构 (schema)

`opencode.db` 存放会话、消息、分段、待办、分享、权限、项目、凭据与事件。在它旁边，`snapshot/<project-id>/` 是每个项目一个 git 快照 (snapshot) 仓库——顶层目录名与 `project.id` 一致——看起来是用于回退 (revert) 的（属推断），在 `global/` 之下还有一层由路径哈希构成的层级。`tool-output/` 存放溢出到磁盘的大型工具结果（文件名形如 `tool_<id>`），由分段引用；`log/` 存放运行时日志（是否轮转未核实）；`auth.json` 存放供应商凭据 (credentials)，这是一个既不可打印也不可提交的机密。

关键表（已核实，行数截至 2026-10-04）有 `session`（218 行）、`message`（15,369）、`part`（58,664）、`project`（8），另有 `todo`、`session_share`、`session_context_epoch`、`permission`、`workspace`、`credential`、`event`。一行 `session` 携带 `project_id`、`workspace_id`、`parent_id`（用于分叉与子会话）、`slug`、`directory`、`path`、`title`、`version`、token 与成本计数器、`revert`、`time_archived`。`message` 和 `part` 都把各自的载荷 (payload) 存为一个 `data` JSON 大字段，以 `session_id` 为键；这也是为什么一条临时 (ad-hoc) SQL 查询就能重建完整的转录。该模式 (schema) 是**内部且不稳定的**，所以不要在未锁定 OpenCode 版本的情况下基于它构建工具。

## 5. 恢复是如何工作的（机制）

启动时，OpenCode 从 `project` 表解析出项目（依据 `worktree`），挑出会话，按 `time_created` 顺序加载其消息与分段，并重建模型上下文——不过这是推断而非读自源码，附件、快照与溢出的 `tool-output` 的按需重新载入 (re-hydrate) 同样属推断。相比之下，状态作用域 (state scoping) 是已核实的：`todo` 行是会话级的，随会话消亡；而 `permission` 行以 `project_id` 为键，所以一次“always”批准会在该项目内跨会话保留（见 [`260811-agents-opencode-config.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260811-agents-opencode-config.md)）；持久规则放在 config 与 `AGENTS.md`（见 [`260821-agents-md-not-a-persona.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260821-agents-md-not-a-persona.md)）。这个 DB 同时也是取证记录——确切的命令、时间戳、触发它的那条用户消息——也就是那次人格/临时产物事故复盘里用到的线索。

## 6. 上下文压缩 (context compaction, long sessions)

长会话最终会超出模型的上下文窗口，于是智能体会**压缩 (compact)**：概括并裁剪历史，让同一条线程继续下去。存储里能看到压缩在起作用——类型为 `compaction` 的 `part` 行在本机有 62 个，分布在 26 个会话中——外加一个 `session.time_compacting` 时间戳列，以及一张 `session_context_epoch` 表（存在但本机为空；其确切作用属推断）。这对持久化很重要，因为**原始转录留在 DB 里**，而模型在恢复时*看到*的是压缩后的视图：持久化保全了记录，压缩重塑了工作上下文。

## 7. 还能做什么（CLI 命令面 surface）

除了恢复，CLI 还能管理和搬运会话。`opencode session list` 列出它们，`opencode session delete <id>` 删除其中一个。`opencode export [sessionID]` 把会话导出为 JSON，`--sanitize` 会脱敏转录和文件数据；`opencode import <file|url>` 从该 JSON 或分享 URL 恢复会话。`opencode db` 对存储执行一条 SQL 查询，`opencode stats` 报告 token 与成本聚合（`--models`、`--project`、`--days` 可做细分）。分享**没有独立的 `opencode share` 命令**——它通过 `opencode run --share`、`OPENCODE_AUTO_SHARE` 环境变量或 TUI 完成，产出的链接记录在 `session_share` 表中。

## 8. 复用：会话何时有用，何时该重新开始

当你在继续一个长任务、崩溃后恢复，或分叉以尝试另一种方案而不丢失原会话时，会话是有用的。而当工作不相关时，它就有害：陈旧的历史会撑大上下文、稀释提示词 (prompt)，所以规则是“新任务 → 新会话”。分叉是给决策树开分支的廉价方式，原会话仍是记录。

## 9. 什么时候可以忽略它

有些会话不值得保留：没有任何内容值得留存的只读问答线程，或者价值已经沉淀进 `AGENTS.md` 或某个 `SKILL.md` 的会话——持久的产物是文件，而不是转录。执行 `opencode session delete` 之后（会通过外键级联删除消息与分段），不应残留任何东西；请核实。

## 10. 备份——什么重要，什么可弃

保留 `auth.json`（凭据）和 `opencode.db`（历史）。因为旧数据会被自动清理（见 §3），停止运行时的 DB 副本是唯一持久的全量历史备份；按会话导出只覆盖你选择保留的那些会话。`log/` 可弃，而 `tool-output/` 与 `snapshot/` 体积大但不宜随手删除——溢出的工具结果由分段引用，快照则是保存过去状态用于回退的 git 仓库，且不会重新生成。因此备份按意图拆分：`opencode export <id>`（可选 `--sanitize`）用于分享或归档**单个**会话，OpenCode 停止时复制的 DB 副本用于**全量**备份（SQLite 的 WAL 可能让运行中的文件副本不一致——此处未实测），因为并没有文档化的批量导出命令。这与 [`260528-hermes-backup.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260528-hermes-backup.md) 中的 Hermes 模式一致——配置、会话、鉴权为基本要素。

## 11. 可选：对历史做向量化 / 语义索引 (vectorization / semantic index)

DB 是一个可搜索的转录存储，显而易见的扩展是把消息与分段做嵌入 (embedding) 以支持语义搜索 (semantic search)。本地路线可以是 `sqlite-vec` 或 FTS5，但该 DB 由应用独占、在 WAL 下打开，所以挂载扩展未实测，且可能与 OpenCode 冲突；Supabase (pgvector) 是托管路线。风险是成本与隐私——索引历史意味着要把源码和密钥送出或做嵌入。

## 待解决的问题 (open questions)

- `log/` 会轮转吗？
- 分享/导出默认包含文件内容和工具输出吗？
- 是否有受支持的批量导出/备份，还是只能逐会话？
- 在大会话上，`-c` 重放会消耗多少上下文/token？
- 当多个项目共享同一目录时，`-c` 会选哪个会话？
- 压缩保留什么、丢弃什么，被丢弃的上下文能恢复吗？
- 自动清理会移除什么，按什么时间表或留存窗口？

## 验证命令 (verification commands)

```bash
opencode --version
opencode db path
opencode session list
du -sh ~/.local/share/opencode/*
sqlite3 "file:$HOME/.local/share/opencode/opencode.db?mode=ro" \
  "SELECT 'session',COUNT(*) FROM session UNION ALL SELECT 'message',COUNT(*) FROM message;"
```

## 术语表 (glossary)

- **ZDR** —— 零数据留存 (Zero Data Retention)：供应商在每次请求后丢弃提示词与补全结果（一种留存保证，与“选择不用于训练”不同）。
- **WAL** —— SQLite 的预写日志 (Write-Ahead Log)（`opencode.db-wal`），在检查点 (checkpoint) 之前保存近期变更的附属文件。
- **XDG** —— freedesktop 基础目录约定 (`~/.local/share`、`~/.config` 等)。
- **DB** —— 数据库 (database)；此处指 SQLite 文件 `opencode.db`。
- **CLI** —— 命令行界面 (command-line interface)；**TUI** —— 终端用户界面（不带参数运行 `opencode`）。
- **JSON** —— JavaScript Object Notation；OpenCode 存储消息/分段载荷的文本格式。
- **SQL** —— 结构化查询语言 (Structured Query Language)；**FTS5** 是 SQLite 的全文检索扩展。
- **pgvector / sqlite-vec** —— 用于 Postgres 和 SQLite 的向量嵌入扩展。

## 参考来源 (sources)

- OpenCode v1.18.34 CLI 帮助：`opencode --help`、`opencode session --help`、`opencode export --help`、`opencode import --help`、`opencode db --help`、`opencode stats --help`（检索于 2026-10-04）。
- 实时 SQLite 模式：`opencode db path` → `~/.local/share/opencode/opencode.db`。
- 交叉链接：[`260811-agents-opencode-config.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260811-agents-opencode-config.md)、[`260821-agents-md-not-a-persona.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260821-agents-md-not-a-persona.md)、[`260528-hermes-backup.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260528-hermes-backup.md)、[`260927-opencode-openrouter-model-selection.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260927-opencode-openrouter-model-selection.md)。

btw, i use arch
