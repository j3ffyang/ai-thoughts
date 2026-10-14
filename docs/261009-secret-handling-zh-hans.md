# 把机密挡在 Git 之外 (keeping secrets out of Git)

> 繁体版：[把机密挡在 Git 之外 (keeping secrets out of Git)](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261009-secret-handling-zh-hant.md)

**原文：** [261009-secret-handling.md](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261009-secret-handling.md)

机密 (secret)、凭据 (credential) 与密钥 (key) 只应留在本地磁盘上，别处一概不留——不进提交 (commit)、不进推送 (push)、不进分支 (branch)、不进拉取请求 (pull request)。一旦某个机密到达远端 (remote)，它就已经暴露，哪怕之后的提交把它删掉也无济于事，因为 git 会保留历史。本笔记列出在一个仓库里应当考虑什么、改动什么，好让机密无从溜入。

![信息图：把机密挡在 git 之外——「已提交即已泄露」的警告、机密的种类、.gitignore 模式、是护栏不是墙、README/AGENTS 政策、三条验证命令，以及安全习惯](../imgs/261009-secret-handling.png)

## 应当考虑什么

- 机密 (secret) 是任何能授予访问权的值：API 密钥 (API key)、令牌 (token)、口令 (password)、私钥 (private key)、密钥对 (keypair)、连接字符串 (connection string)、`.env` 文件。
- git 会保留历史。删掉文件并不会移除机密；把已提交的机密视为已泄露，并轮换 (rotate) 它。
- `.gitignore` 是护栏，不是墙：`git add -f` 能覆盖它，而在忽略规则之前就已加入的文件会一直处于被跟踪 (tracked) 状态。
- 最安全的机密是从未进入暂存区 (staged) 的那一个。从第一次提交起，就把机密放在被忽略的路径里。
- 优先使用机密管理器 (secret manager) 或环境变量 (environment variable)，而不是工作区 (working tree) 里的文件。
- 每次提交前读一遍 `git diff --cached`；扫一眼就能抓住混进来的密钥。

## 该在 .gitignore 里改什么

列出机密通常以哪些模式出现，让 git 无法跟踪它们：

```gitignore
# Secrets, credentials, keys — never commit or push
.env
.env.*
*.key
*.pem
*.p12
*.pfx
id_rsa
id_ed25519
secrets/
credentials/
```

当有新工具引入新的机密文件时，就补上对应的模式。

## 该往 README.md 里加什么

把政策写在读者看得到的地方：

> 机密、凭据与密钥永不提交、永不推送；它们留在本地磁盘上，`.gitignore` 排除了它们的常见模式。

如果 README 是生成的——就像本仓库，由 `articles.yaml` 生成——就把这一行加进模板或生成它的源头，绝不要手工编辑 README。

## 该往 AGENTS.md 里加什么

给智能体 (agent) 同样的规则，让它不会暂存或提交机密：

> 永不提交或推送机密、凭据或密钥；它们留在本地磁盘上。`.gitignore` 排除了它们的常见模式。

## 验证

- `git ls-files | git check-ignore --stdin` 会列出任何会被新规则隐藏的已跟踪文件；它应当为空。
- `git log -p -- <path>` 显示某个机密是否曾被提交过。
- `git status --short` 显示没有意外的机密文件。

btw, i use arch
