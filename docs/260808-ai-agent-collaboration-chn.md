# AI 智能体协作：基于 AGENTS.md 与 SKILL.md 的 OpenCode 实战手册

*我是如何学会与一个 AI 智能体协作的——用 ***OpenCode*** 与 `big-pickle` 模型——穿过一个混乱而真实的多仓库项目，以及它教给我的关于 AGENTS.md、SKILL.md、项目边界与思维流架构的东西。*

---

这篇文章是一个我与 AI 智能体真实完成的项目总结，加上从中得出的教训。它不是一条一帆风顺的教程。它是一份实践记录——包括错误、分歧，以及智能体对了而我错了的时刻，还有少数几个我对了而智能体错了的时刻。这种诚实很重要，因为大多数关于 AI 智能体的文章展示的都是打磨好的最终状态，而不是抵达那里的混乱过程。

这个项目：用 GitHub Actions 把三个 GitHub 仓库里的 `SKILL.md` 文件自动发布到 **ClawHub**（一个技能注册中心）——不安装任何本地 CLI 工具、不转换任何现有技能、也不破坏一套已经正常工作的双语发布流水线。听起来很简单。其实并不。而正因为如此，它才值得写下来。如果你想要压缩版，文末的快速要点一节把它提炼成了五条规则。

> **如何阅读本文。** 这篇随笔刻意分层：**步骤**是证据，**亮点**与**原则**是推理，**失败目录**是参考表，**快速要点**是真正要用的五条规则。每一层都是同一批教训的不同压缩，所以你可以停在任意一层。

## 背景，一段话说清

做这个项目时，我的技能和文章散落在 superproject 之下的三个子仓库里——此后这套体系又有所增长：

- `history/` — `.opencode/skills/` 下有两个技能（`astro-sync`、`zh-history-literature-culture`）
- `ai-thoughts/` — `.opencode/skills/` 下有三个技能（`astro-sync`、`resize-for-banner`、`translate-to-chn`）
- `ai-custom-skills/` — 一个更大的技能矩阵，分布在 `openclaw/`、`hermes/` 和 `claude-code/` 根目录下，外加一个嵌套得别扭的技能

每个子仓库都有**两个 remote**：`j3ffyang`（我的个人 GitHub 账号）和 `negtivspace`（第二个个人账号）。每次改动都会同时推送到两个。一切基于 Linux，一切在终端里，一切从简。

> **两个账号，一个作者。** 两个都是我的：`j3ffyang` 是我的主要个人 GitHub 账号；`negtivspace`（「Negative Space 留白」）是我用来镜像同一批仓库的第二个个人账号。三个子仓库 × 两个账号，这就是「六个仓库」的来历，而同时推送到两个账号正是第 4 步双发布竞争（double-publish race）存在的原因。另外别把 `negtivspace` 这个 GitHub 账号和容纳一切的 `negtivSpace` superproject 目录搞混。

目标：当我推送对某个 `SKILL.md` 的改动时，一个 GitHub Action 应该检测到什么发生了变化，并把新的或更新的技能发布到我账号下的 ClawHub——自动化、幂等，而且我不用在本地运行任何工具。

## 思维流：我们如何协作的高层流程

这是整篇随笔中最值得先读的部分。经过几轮会话，一个**流程浮现出来**——我们如何分享想法并做出决定：有时分歧，多数时候一致——关于何时以及如何生成 AGENTS.md 和 SKILL.md。它不是僵硬的流程。它是一种**思维流的架构**，一个收敛的循环。读后面的实践时请记住它——故事的每一步都是这些阶段之一的活例子。

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  1. INTENT         ──  what do I want? state it plainly        │
│          │                                                     │
│  2. CONSTRAINTS    ──  what must not change? boundaries,       │
│                       tools, remotes, conventions, approvals   │
│          │                                                     │
│  3. PROPOSE        ──  agent drafts a plan + options +         │
│                       recommendation                           │
│          │                                                     │
│  4. PRESS          ──  I push back where it conflicts with     │
│                       my constraints; we negotiate             │
│          │                                                     │
│  5. PRACTICE       ──  approve, build, run, observe            │
│                       (real failures live here)                │
│          │                                                     │
│  6. INVESTIGATE    ──  when it fails, verify against the       │
│                       real system before blaming the tool      │
│          │                                                     │
│  7. CODIFY         ──  distill the practice into AGENTS.md     │
│                       rules and SKILL.md steps                 │
│          │                                                     │
│  8. BOUNDARY-CHECK ──  is this the right repo / worktree /     │
│                       scope for this knowledge? resize if not  │
│          │                                                     │
│          └────── loop ── practice again, refine again ──────┘  │
└────────────────────────────────────────────────────────────────┘
```

关于每个阶段，有几点说明，因为只有当各个阶段被理解时，这个循环才有效：

- **Intent（1）与 Constraints（2）是最昂贵的阶段。** 之后的一切都更便宜。花十分钟说清约束，就能省下一小时的返工。在这个项目里，「不装本地工具」这句短语让我避开了一整类问题，而「推送到两个 remote」制造了那次碰撞，最后由「只从一个 remote 发布」修复。
- **Propose（3）应当始终包含选项和一个建议。** 只有一个路径的计划不是提议，而是命令。我想看到权衡，这样才能有意义地反对。
- **Press（4）不是冲突，而是谈判。** 分歧发生在我持有的约束与智能体持有的系统知识交汇之处。`astro-sync` 的结果——既不是智能体的最初想法，也不是我的——就是我希望分歧如何收场的范本。
- **Practice（5）是循环最诚实的地方。** 任何计划都经不起真实注册中心、真实密钥和两个 GitHub 账号的检验。这个阶段暴露的失败，才是最能教人的。
- **Investigate（6）是把调试与猜测区分开的纪律。** 读源码。打 API。对照真实系统验证主张。正是它把「工作流坏了」变成了「工作流有一个我设计出来的竞争条件」。
- **Codify（7）是回报。** 当一个流程第二次跑通，它就成为 SKILL.md 的候选。当一条规则对整一个仓库都成立，它就成为 AGENTS.md 的一条。
- **Boundary-check（8）是元技能。** 问自己：这份知识该属于父层、子仓库层，还是哪里都不该有？太宽泛就会被稀释。太狭窄就会碎片化。worktree 是我放 AGENTS.md 的自然单位；反复出现的流程是我放 SKILL.md 的自然单位。

## 实际发生了什么，一步步来

### 第 1 步——计划被批准，边界被划定

智能体做的第一件事不是写代码，而是请我定义边界：哪些仓库、哪些 remote、哪些技能、哪些约束。我说：从三个子仓库发布技能，不修改任何技能内容，不本地安装任何东西，并按仓库规则推送到两个 remote。

这是第一个教训，我会直说：

> **结果的质量更多取决于我如何描述问题，而不是模型本身。**

### 第 2 步——可复用工作流被钉死，第一堵墙出现

ClawHub 自带一个官方的可复用 GitHub Action：`openclaw/clawhub/.github/workflows/skill-publish.yml`。最显然的选择是用 `@v1` 引用它。智能体检查后发现 **`@v1` 根本不存在**——当时最新的 tag 是 `@v0.23.3`。所以我们钉到了那个版本。

第一次运行立刻以 `startup_failure` 失败：

```
The nested job 'publish' is requesting 'id-token: write', but is only allowed 'id-token: none'
```

这是 GitHub Actions 的一个怪癖：调用可复用工作流的上游 job 必须在 **job 级别**声明 `permissions: { contents: read, id-token: write }`，否则可复用工作流自己的 OIDC token 请求会被拒绝。这种错误在你第一次撞上之前毫无意义，撞上之后则终生可辨。

修复一：加上 job 级别的权限。推送。看它跑得更远。

### 第 3 步——密钥，与双账号之谜

发布需要 token。我在 ClawHub 上只有一个账号：`j3ffyang`。智能体提议在全部六个仓库（三个子仓库 × 两个 remote）上设置 `clawhub_token` 仓库密钥。那是第一处真正的摩擦：**其中两个仓库的 `negtivspace` 副本上，密钥根本设置不进去。**

为什么？因为 `negtivspace` 是**用户账号**，不是组织。用户账号的仓库只允许所有者本人设置密钥，而所有者就是账号自己——我的另一个账号（`j3ffyang`）在没有写权限的情况下无法在那里设置密钥。GitHub 的密钥 API 要求调用方拥有仓库的写权限，而协作者级别的权限当时并没有授予。

修复是一次虽小但真实的协作变更：我授予了 `j3ffyang` 账号在 `negtivspace/ai-custom-skills` 和 `negtivspace/ai-thoughts` 上的 **Write** 协作者权限。然后密钥就进去了。

### 第 4 步——运行跑起来了。然后失败了。出于两个截然不同的原因。

现在工作流真的执行了。日志显示了失败，但这些失败分成两个族，而区分它们就是整场游戏：

**家族 A——`Version X.Y.Z already exists. Increment the version number and try again.`**

`astro-sync`（在 `history` 和 `ai-thoughts` 里都有）、`zh-history-literature-culture`（`history`）以及 `blog-image-enricher`、`indepth-perspective`、`image-to-video-gen`（`ai-custom-skills`）全部以此失败。我以为是工作流坏了。智能体并不那么确定，它钻进了 ClawHub CLI 的源码（`/tmp/opencode/publish-v0233.ts`），去读版本解析实际是怎么工作的。

根本原因既漂亮又令人恼火：**每个子仓库的两个 remote 都运行同一套工作流，而且都发布到同一个 ClawHub 账号。** `j3ffyang/history` 和 `negtivspace/history` 正在竞速发布同一个 `astro-sync`。谁先落地谁创建 `1.0.0`；另一个则得到「Version 1.0.0 already exists.」。这根本不是我的工作流的 bug。那是我把「推送到两个 remote」这件事设计进系统里的**双发布竞争（double-publish race）**。

智能体不只是断言。它带着 token 查询 ClawHub API，把真实记录给我看：每一个「撞车」的版本都以 `j3ffyang` 的名义存在于 ClawHub 上，时间戳正好落在工作流运行的窗口内。这就是我现在最珍视的实践：**当某样东西看起来坏了，先对照真实系统验证，再假设是工具的问题。**

**家族 B——`Invalid publish output: 'pending-publication'`**

这个看起来也像真正的错误。智能体读了上游可复用工作流的 Python，找到了真相：该工作流的状态映射只认识 `would-publish`、`published` 和 `unchanged`。而 ClawHub CLI 在发布已提交、正在等待异步安全扫描时，会返回 `pending-publication`——上游工作流没有映射它，于是抛出异常，把技能报告为*失败*。

但技能**确实**发布了。API 确认 `blog-polish-zhcn@1.0.14`、`resize-for-banner@1.0.0` 等全部在 ClawHub 上正常在线。这个「失败」是一个**纯表面性的上游状态映射 bug**——第三方工作流里内置的虚惊一场，而不是我的系统有问题。

### 第 5 步——真正的修复：单一来源发布

针对家族 A 的修复只有一个条件，加在三个工作流文件的两个 job 里：

```yaml
if: github.event_name != 'pull_request' && github.repository_owner == 'j3ffyang'
```

`github.repository_owner` 会在运行时从实际运行工作流的那个仓库解析。在 `j3ffyang/*` 上，owner 匹配，发布 job 运行。在 `negtivspace/*` 上，owner 是 `negtivspace`，条件为假，job 被跳过。`negtivspace` 的副本保留文件——镜像保持同步——但它们在**设计上成为空操作（no-op）**。单一来源发布。竞争消失了。此后的每次运行都是绿的。这是整个项目中最重要的一个工程决策，而且它来自一次小小的对话：我描述了症状（「撞车」），智能体把它追溯到设计（两个 remote），我同意了这个修复（一个守卫），而不是试图让两个 remote 共存。这条规则如今活在一个技能里，被写成文档，这样我们俩谁都不会忘记它。

### 第 6 步——slug 冲突，以及一场以良好妥协收尾的分歧

竞争修复之后，一个更隐蔽的问题浮出水面。`history/.opencode/skills/astro-sync` 和 `ai-thoughts/.opencode/skills/astro-sync` 都存在。它们有**相同的 slug 但内容不同**——`ai-thoughts` 里的版本被改造过（不同的源路径、没有事实核查步骤、多了一个 `featured` 参数）。ClawHub 把 slug 视为同一 owner 下的唯一标识，所以两份副本在**每次发布时互相覆盖。** `ai-thoughts` 刚刚发布了 `astro-sync@1.0.1`，把 `history` 的 `1.0.0` 覆盖掉了。

智能体提议删除或重命名 `history` 里的副本。我反对：**`history` 项目里仍然需要 `astro-sync`。** 它是把历史文章发布到我的博客的技能；删掉它就会弄坏我自己的工作流。

这时智能体做对了一件事：它没有争论，也没有简单地同意。它查了 **OpenCode** 是怎么发现技能的（从当前目录向上走到 git worktree 根，加载 `.opencode/skills`、`.claude/skills` 和 `.agents/skills`），然后提出了一个我没想过的折中方案：

- 把 `history` 的 `astro-sync` 原样留在原地——本地的、原汁原味的、在 `history` 项目里可加载。
- 把 `history` 的工作流从 `root: .opencode/skills` 改成只点名 `zh-history-literature-culture` 的 `skill_path`，从而停止发布它。
- 让 `ai-thoughts` 保持唯一*被发布*的 `astro-sync`。

什么都没丢。本地技能保持了原汁原味，注册中心不再被覆盖，我的博客工作流也继续运转。这就是我希望从协作中得到的那种结果：**不是智能体的第一个想法，也不是我的，而是一个尊重真实约束的第三个选项。**

### 第 7 步——把我们学到的东西沉淀下来

最后一步是把混乱的过程变成持久的知识。我们创建了一个技能 `.opencode/skills/clawhub-publish/SKILL.md`，记录整个流水线：单一来源规则、owner 守卫、版本语义、`pending-publication` 虚惊、slug 冲突策略，以及如何用 ClawHub API 验证一次发布。我们最初的直觉是把它放在父层——但一个在子仓库内打开的会话看不到父层的技能，所以它落在了 `ai-thoughts/.opencode/skills/`，也就是发布工作真正发生的地方。工作流文件提交到了两个 remote，子模块指针被更新，`j3ffyang` 的每次运行都变绿。

整个旅程花了几轮会话。其中没有任何一步是单次的妙手。它是一轮又一轮的 *intent → constraints → propose → press → practice → investigate → codify → boundary-check*，反复跑到系统变得无聊而可靠为止。

## 亮点——我实际学到的东西

现在进入我想保留的部分。以下是亮点，每一条都由实践挣来——而且每一条都会在下面的失败目录里以压缩的形式再次出现。

### 1. 搭载 `big-pickle` 模型的 OpenCode 很强大——而且意外地免费

我在终端里跑 **OpenCode**，在 Arch Linux 上。我的默认模型是 **`big-pickle`**——免费、快速、而且始终靠谱。这套组合不要订阅费，也不会把我限流到没法用。`big-pickle` 模型处理了一个多仓库、多账号、外部注册中心的自动化项目而毫无波折：它读了上游工作流源码、查询线上 API 验证假设，还推理了 GitHub Actions 的权限怪癖——这些它显然以前就见过。

### 2. 它能做的远超我的想象——只要我放手让它去做

改变我态度的时刻在第 4 步，当时智能体说，大意是：「让我读一下 ClawHub CLI 源码，弄清版本解析是怎么工作的。」我原本以为碰撞是配置错误；智能体深入了一层，下载源码，读了实际的解析逻辑。那不是模式匹配——那是调查，而这正是关键：一个好的智能体配上正确的工具（bash、网页抓取、文件读取、git），能对一个我看不见的系统做真正的调试。限制我的是我的想象力，而不是模型。

### 3. 当结果不是我预期的那样，问题通常在我

关于这一点我要直言不讳，因为它是最有用也是最不舒服的教训：

> **当智能体的输出与我的预期不符时，问题通常出在我如何对它说话，而不是智能体本身。**

这个项目里每一个令人沮丧的失败，都能追溯到我某个没说清楚的地方：

- 我说了「把技能发布到 ClawHub」，却没有说「只从恰好一个 remote 发布」——于是设计出了一个双发布竞争。
- 我没有划清「已发布」与「仅本地」技能之间的边界——于是制造了一个 slug 冲突。
- 我批准了一个计划，却没注意到它会重命名或移动一个我本地仍在使用的技能。

那些我得到预期结果的时刻，恰恰是我指令精确的时刻：单一来源、不改内容、不装本地、推送到两个 remote。精确输入，精确输出。含糊输入，猜测输出。

这并非为智能体开脱——它也真的犯过错，当它缺少我知道的上下文时，我也推翻过它。但诚实算下来，**大多数失误是我的**，而且大多数是沟通失误。

### 4. AGENTS.md 和 SKILL.md 才是真正的技术

这是我最在意的主张：

> **AGENTS.md 和 SKILL.md 不是文档。它们是我如何思考与智能体如何运作之间的接口。**

- **AGENTS.md** 是一个仓库的宪法：它是做什么的、文件如何命名、必须始终检查什么、工作规则是什么。它是让智能体记住我的约定、而不是我每个会话都重复一遍的方式。
- **SKILL.md** 是一个打包好的流程：一个可重复的工作流，包含步骤、规则和错误处理，当任务匹配时就加载。一旦写好，一整个多步骤流程就变成了一次请求。

在这个项目里，AGENTS.md 文件做了实打实的工作。`history/AGENTS.md` 告诉智能体每次改动都需要批准、事实需要两个来源、文件名遵循 `YYMMDD-slug`。父级 `negtivSpace/AGENTS.md` 告诉它推送到两个 remote 以及 profile README 同步怎么工作。没有它们，智能体就得每个会话都问我同样的问题，而答案会逐渐漂移。

技能也做了实打实的工作。`astro-sync` 把一长串编辑流程变成了一次请求。`clawhub-publish` 把一场来之不易的调试会话变成了一张智能体下次可以照做的检查清单。努力是前置的——但回报是复利的，因为知识在会话结束后存活了下来。

### 5. 项目边界：太大则含糊，太小则难以维护

最微妙的一课是关于**技能或 AGENTS.md 应该放在哪里**。

我通过实践发现，**OpenCode** 发现技能的方式是从当前目录向上走，**直到到达 git worktree 根**，而且它不会跨入父级 superproject。证据：我在父仓库创建了 `.opencode/skills/clawhub-publish/`，而在 `history/` 内打开的会话根本看不到它。这个技能不可见，恰恰因为 `history/` 是它自己的 git worktree。

这就是浓缩版边界问题：

- **范围太大**——一个涵盖 superproject 下一切的巨型 AGENTS.md——意味着每条指令都被稀释到适用于所有仓库，于是没有一个仓库得到具体、准确的规则。含糊的指令产生含糊的行为。
- **范围太小**——每个琐碎的文件夹都配一个 AGENTS.md 和技能——意味着我要被淹没在需要维护的文件里，而同样的知识被重复然后漂移。

我最终找到的最佳点：每个 git worktree 一份 AGENTS.md（每个子仓库一份，外加父仓库一份），而 SKILL.md 只为那些我实际跑过不止一次的流程。`astro-sync` 碰撞让我用最难的方式学到了边界：技能必须*对使用它的项目而言是本地的*，并且*只从一个仓库发布*。同一个技能，两个关切，各有一条边界。

### 6. 让 AI 提建议——但不要每次都同意

我想把这个说得简短些，因为它很重要：智能体建议把 `clawhub-publish` 放在父层，我最初接受了——直到我们发现在子仓库里打开的会话看不到父层技能，才撤回了这个决定。它也给过我一个我拒绝的建议（把 `history` 的 `astro-sync` 移到 `.claude/skills/`，我拒绝是因为这个技能是为 **OpenCode** 写的，不是为 Claude 写的），还有一个我最终非常喜欢的建议（`skill_path` 折中方案）。

本事不在于是不是每条建议都听，也不在于全都无视。本事在于**把智能体的提议当作一次决策的初稿，而不是决策本身。** 我握着约束（`history` 项目仍然需要 `astro-sync`；技能必须保持原汁原味；本地什么都不装；两个 remote 都要推）。智能体握着系统知识（**OpenCode** 如何加载技能、ClawHub 如何解析版本、工作流如何映射状态）。最好的决策来自我说出约束、然后让智能体在约束中找路——之后再对照我的约束检查这条路，才接受它。

### 7. 把你的要求写进 AGENTS.md

一个小而有效的习惯：**直接把操作偏好写进 AGENTS.md，让智能体永远不用问。**

对我来说是这些：

```
- minimalist, Linux only, prefer command line
- no local installs unless approved
- get approval before any change
- commit only when asked; stage only intended files
```

这些不是技术指令。它们是*性格*。而它们改变了每一个会话的行为。智能体不会提议 GUI 工具，不会不问就装东西，不会在编辑上闷头猛冲，只暂存我让它暂存的东西。最后一条反复救了我：当父仓库有改动的子模块指针和一个我不想碰的未跟踪文件夹时，「只暂存我指定的文件」这条规则意味着提交里恰好只有那个 SKILL.md，别无其他。

### 8. 我爱终端里的 OpenCode

我要把显而易见的话直说：我爱终端里的这个工具。TUI 是我生活的地方——快、键盘驱动、不用切标签页到网页应用。它跑在我的 Linux 机器上，尊重我的约束，读我的 AGENTS.md 文件，把我的工作流留在 git 里。`Tab` 键切换 plan/build 模式，而这正是整个项目运作的方式：计划、批准、构建、验证、重复。它给人的感觉不太像「使用一个产品」，更像「雇了一位非常快、非常刻板的同事，它记得我写下的每一样东西」。

魅力的一部分在于终端会**展示它自己的思考过程。** 智能体产生的每一条消息都打印在我面前——它运行的每个工具调用、它经历的推理、它遵循的思维流与逻辑。我可以看着 AI 思考，而不只是读它的结论。而且因为我生活在 Linux 上，错误消息大多是原生的系统错误——`No such file or directory`、`error: failed to push some refs`、`startup_failure`、退出码——我一看就懂。当某样东西失败时，我能看到*确切地*发生了什么，没有翻译层，没有友好但含糊的包装器把原因藏起来。对我来说，这种透明正是「信任一个工具」和「仅仅使用它」的全部区别。

## 失败目录——这本实战手册的原材料

上面的一切都是从具体的失败中提炼出来的。值得把它们留成一份目录，因为每一个都对应着我如今强制执行的一条教训和一条规则：

| 失败 | 我起初以为 | 实际是什么 | 修复 | 教训 |
| --- | --- | --- | --- | --- |
| `startup_failure`: "requesting 'id-token: write', but is only allowed 'id-token: none'" | 工作流文件写错了 | 可复用工作流的调用方必须在 job 级别声明 `permissions: { contents: read, id-token: write }` | 加上 job 级别的权限 | 平台怪癖看起来像配置错误；去读确切的错误文本 |
| 多个技能报 `Version X.Y.Z already exists` | 注册中心坏了 | 两个 remote 竞速把同一个 slug 发布到同一个账号 | `github.repository_owner == 'j3ffyang'` 守卫让 `negtivspace` 副本成为空操作 | 我通过推送到两个 remote 设计出了一个双发布；单一来源发布 |
| `Invalid publish output: 'pending-publication'` | 发布失败了 | CLI 的 `pending-publication` 状态（异步安全扫描）在上游工作流里没有映射；技能其实发布成功了 | 无需任何操作——用 API 验证，按成功处理 | 别相信包装器的状态映射；去查真实系统 |
| `astro-sync` 覆盖它自己 | 两个仓库共享一个 slug 无妨 | ClawHub 的 slug 在同一 owner 下唯一；两个不同副本互相覆盖 | `ai-thoughts` 保持发布；`history` 的副本通过 `skill_path` 保留在本地 | 同名不等于同物；给每个技能划边界 |
| 技能在子仓库里不可见 | 我忘了提交它 | **OpenCode** 只把技能加载到 git worktree 根为止；父层技能在子模块里不可见 | 把技能放到真正使用它的仓库里 | 发现规则就是边界规则 |
| 密钥在 `negtivspace` 仓库上设不进去 | CLI 出问题了 | `negtivspace` 是用户账号；只有所有者（或有 Write 权限的协作者）能设置密钥 | 在两个仓库上给 `j3ffyang` 授予 Write 权限 | 两个账号意味着两套权限模型 |

每一行的模式都一样：**错误消息是线索，不是结论。** 解开每一行的纪律也一样——在改动任何东西之前，先对照真实系统调查（读上游源码、调 API、检查 token 的身份）。

## 落到约定上是什么样子

为了让这本实战手册更具体，这里给出最终浮现出的 AGENTS.md 和 SKILL.md 文件的形状。不是拿来照抄的模板——而是这套模式的证据。

一个内容仓库的最小 AGENTS.md 长这样：

```markdown
# AGENTS.md

## Project
Bilingual repository of articles on <topic>. Written in <language>.

## Working rules
- Get approval before any change. Present the plan and wait for the go-ahead.
- Commit only when asked; stage only intended files.
- Linux only; prefer command line; minimalist.

## Filename conventions
- docs/<YYMMDD>-<slug>.md — 6-digit date, hyphen, lowercase slug. No spaces.
- imgs/<YYMMDD>-<slug>.<ext> — images share the article's date prefix.

## Repository layout
- docs/ — articles; imgs/ — images; README.md — index (hand-edited).
```

三个小节。这就够了。其余一切——profile 同步、两个 remote、发布规则——要么存在于需要它的文件里，要么存在于某个 SKILL.md 里。

一个重复流程的 SKILL.md 是这个形状：

```markdown
---
name: clawhub-publish
description: Publish SKILL.md files to ClawHub and diagnose publish failures.
---

# ClawHub Skill Publish

## Single-source rule — read before anything else
- Only the j3ffyang/* copies publish. negtivspace/* copies are no-ops by design.

## Pipeline
- Workflow per repo calls the reusable workflow, pinned to a specific tag.

## Status & version semantics
- unchanged → nothing to do; new → 1.0.0; changed → next patch.
- 'pending-publication' → actually succeeded; verify with the API.

## Procedure
1. Add/edit a skill in the correct root.
2. Push to both remotes; the j3ffyang copy publishes.
3. Wait for the run; check the summary for the slug.
4. Verify on ClawHub with the API; check the latestVersion and owner.

## Error Handling
- Version already exists → already published; next run marks it synced.
- Slug collision → only one repo publishes a given slug.
```

细节因项目而异。形状不变：**必须放在最上面、不能被跳过的规则，作为地图的流水线，让虚惊不被当成故障的状态语义，以及短到能照着做的流程。**

## 原则，直白地说

我最终得到的这套方法是个人的。我不声称它是正确的方法，也不是唯一的方法。在这片领域里没有百分百的对错——没有非黑即白。我能说的是，这套方法对我有效，而且它建立在我不断回归的几条原则上：

1. **精确输入，精确输出。** 智能体工作的质量跟随我描述的质量。含糊的意图产生猜测；精确的约束产生我恰恰想要的自动化。
2. **边界就是工作本身。** 知识住在哪里——哪个仓库、哪个 worktree、哪个文件——决定了它是否具体到有用、又小到可维护。把边界搞错是我两次最难的失败的来源。
3. **先验证，再责备。** 当结果不对时，先查真实系统——上面的失败目录就是同一个教训的六行。版本碰撞看起来像我的 bug，其实是我的设计；`pending-publication` 看起来像失败，其实是成功。两者都不是看起来的样子。
4. **把有效的沉淀下来。** 一条没有写下来的教训，就是一条将来要再付一次学费的教训。AGENTS.md 和 SKILL.md 是我让智能体停止反复重学我已经知道的东西的方式。
5. **智能体是同事，不是神谕。** 它提建议；我来决定。它的提议是我要对照自己的约束来检查的草稿。最好的决策都来自这种摩擦。
6. **正确的模型重要，编排同样重要。** `big-pickle` 免费又出色，但它在这里成功靠的是这个循环——提议、实践、调查、沉淀——而不是模型本身。在好的约定包裹下的智能体编排与操作，才是真正的放大器。

## 快速要点

如果只从这篇文章里记住五件事：

1. **用架构和逻辑的方式思考。** 在写任何代码之前，先在脑子里画出完整流程——仓库、remote、负责发布的账号、失败模式。这个项目里几乎每一个 bug 都是我没想到的设计缺陷，而不是语法错误。

2. **通过 `gh` 用 GitHub 自己的工具来自动化。** 你想要的东西很多已经以 CLI 命令的形式存在了：`gh run watch`、`gh run view --log`、`gh api repos/<owner>/<repo>/actions/runs` 能把运行历史、日志和任何字段以 JSON 返回。告诉 **OpenCode**「用 `gh`」，一个需要点点点的 UI 操作就变成了智能体能运行并解析的可脚本化命令。

3. **把 API 当作主要的验证方式。** 明确告诉 **OpenCode**：「用 API」或「把 API 作为首选选项」。注册中心自己的报告是错的（`pending-publication` 其实是成功）；API 是对的。在相信一条状态消息之前，`curl` 一下线上端点，检查记录。

4. **工作完成时就沉淀。** 一旦一个任务跑通了，把流程打包成一个自定义 `SKILL.md`，让它成为一次请求即可重复的步骤。如果这条改动是应该跨项目成立的规则——命名、remote、审批——就放进 `AGENTS.md` 里。流程进 SKILL.md，宪法进 AGENTS.md。

5. **让智能体去修——但要读它请求运行的东西。** 我让它自由执行，但前提是它对每一条 shell 或 Python 命令都先征求批准。我可能并不完全理解一段很长的脚本——至少我会读它关于即将做什么的摘要，而当我拿不准时，我会暂停运行，请它先详细说明再决定。

## 结语

我最初想做的是自动发布技能。最后我得到的是一条小而可靠的流水线、一套让下一个项目更快的约定，以及对如何与 AI 智能体协作的清晰得多的认识。流水线本身现在几乎无聊了——而这正是我想要的。有趣的是产生它的那个循环。

让它运转起来的实践是写下我所知道的——规则写进 AGENTS.md，流程写进 SKILL.md，而现在，思考写进这篇文章。

如果你只能带走一点，那就是这一点：**智能体有多好，取决于你给它的边界有多好；而边界只有在写下来之后才起作用。** 其余一切都是练习。

btw, i use arch 
