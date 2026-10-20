# 规则，而非词语：ASD-STE100 与智能体指令

> 繁体版：[规则，而非词语：ASD-STE100 与智能体指令](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261019-ste100-agent-instructions-zh-hant.md)

**原文：** [261019-ste100-agent-instructions.md](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261019-ste100-agent-instructions.md)

*ASD-STE100 是一门为飞机维修手册而设的受控语言 (controlled language)。它有 53 条写作规则，和一份 875 词的词典。*

**来源：** Andrej Karpathy，X 推文串 (thread)，2026 年 10 月 1 日 17:37 PDT（2026 年 10 月 2 日 00:37 UTC）—— [x.com/karpathy/status/2105819303471976479](https://x.com/karpathy/status/2105819303471976479)

**论点：** 在 AI 工作中，价值在规则，而不在词典。这些规则是：**一句话一个动作、祈使语气、条件在前、一个事物一个名称。** 它们直击智能体指令 (agent instructions) 的失败模式——一个无法勾选核对的复合句。

**结论：** 只把规则用在指令上，绝不用于文章。保留那些高价值的词汇替换。把 Karpathy 的建议看作起点，而不是标准：他本人也只要求"达到 ASD-STE100 的 80%"。

![Infographic: ASD-STE100 for agent instructions — the standard's two parts, the four rules that carry the work, a compound prompt split into two steps, the measured before-and-after counts, rule versus skill versus linter, and the four things the standard cannot buy](../imgs/261019-ste100-agent-instructions.png)

## 这条建议从哪来

这条推文串讲的是如何阅读模型输出，而不是泛泛的提示词技巧 (prompting tricks)。Karpathy 的第一个建议，是让模型用 ASD-STE100 解释某件事——"一份受控语言规范 (controlled language specification)"，最初为飞机维修手册而开发。他说模型对这个标准相当熟悉，它"对干净写作风格的严苛约束"能产出他觉得"可读性强得多"的文字。他也承认这份规范"相当严格"，有时会把要求放宽成"达到 ASD-STE100 的 80%"。

推文的其余部分离开了写作：先是图表，然后是 HTML 页面，再是 3Blue1Brown 风格的讲解视频，每一个都被称作"更好"。所以这条帖子真正讲的是更容易验证的输出格式。STE 这条建议是四者中唯一的语言约束，也是试起来最省力的那一个。

有一个跳跃值得点明。Karpathy 是让模型写给人看。这篇文章是让人写给智能体看。两个方向并不对称。人遇到歧义句，可以追问一句。而在无人看管时加载 `AGENTS.md` 的智能体，通常不会问。它会挑一种读法，然后照着做。这种不对称，正是规则可以迁移、而证据不能的原因。下面要讲的失败模式，就写在文字本身里。

有两点要诚实说明。第一，这是轶事（"我试过，有效"），不是基准测试 (benchmark)。第二，我自己写的 **`asd-ste100` SKILL.md** 就是范例：

[https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/asd-ste100/SKILL.md](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/asd-ste100/SKILL.md)

那份文件不含标准的词典。ASD 只授权特定组织复制。

## ASD-STE100 究竟是什么

ASD 把这项工作追溯到 1970 年代末：一个为欧洲航空公司设立的 AECMA 项目，美国的 AIA 也受邀参与。第一版指南问世于 1986 年。现行版本 Issue 9 于 2025 年 1 月发布，这份文档也在那时成为国际标准 (international standard)。它可以免费阅读：从 [asd-ste100.org](https://www.asd-ste100.org/) 开始，下面的每条规则、每个例子都出自那里的 [Issue 9 PDF](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)。

它存在的理由很窄，也很有用：供非英语母语者阅读的维修文档，读错一句就可能出人命。这个出身既解释了它的长处，也解释了它的边界。它在"只有一个正确动作"的程序 (procedure) 上非常出色。它不是通用的散文 (prose) 风格。

它的范围分两部分，其中只有一部分是词表：

- **第 1 部分——53 条写作规则。** 语法、句长、动词形式、安全指令、写作实践。
- **第 2 部分——受控词典 (controlled dictionary)。** Issue 9 收录 **875 个批准词 (approved words)** 和 **1,274 个未批准词 (non-approved words)** 及其替换词。FAQ 把它约等于"约 900 个"。举例来说，`ensure (v)` 未被批准，替换词是 `MAKE SURE (v)`。未批准词表就是这类替换：标准里最无趣的部分，也是人们最容易高估的部分。

词典不是硬墙。技术名词和技术动词 (technical nouns and verbs) 按设计就是开放的（标准的 Rules 1.5–1.13）：公司、行业或专业领域可以添加自己的术语。规则禁止的是把这些术语用得太随意——当动词用、给同一个物件换不同名字、或当行话 (jargon) 用。

最省力的收益先来：几个替换词，加上两条结构规则，各配一个小例子。之后还有三条结构规则。

- `make sure`——"Make sure that the valve is closed."（确保阀门已关闭）。不要用 "verify" 或 "ensure"。
- `remove`、`install`、`set`——一个动作一个动词："Remove the four bolts."（拆下四颗螺栓）"Install the new O-ring."（装上新的 O 型圈）"Set the switch to ON."（把开关拨到 ON）。
- `do`——通用动作动词 (generic action verb)："Do the pressure test."（做压力测试）。不要用 "perform" 或 "conduct"。
- 条件在前——"When the light comes on, set the switch to NORMAL."（灯亮时，把开关拨到 NORMAL）。
- 不用分号——写成两句话："Examine the removed parts for damage. Replace the damaged parts."（检查拆下的零件有无损伤。更换损坏的零件）。

## 标准里的三个例子

### 1. 一句话一条指令 (Rule 5.2)

> 非 STE：`Set the TEST switch to the middle position and release the SHORT-CIRCUIT TEST switch.`
>
> STE：`A. Set the TEST switch to the middle position.` / `B. Release the SHORT-CIRCUIT TEST switch.`

规则允许一个例外：同时发生的两个动作，可以留在一句话里（"Remove and discard the seal."，取下并丢弃密封件）。有先后顺序的动作，则拆成各自独立的步骤。这是我在提示词上最想先用的一条规则，因为编号步骤可以核对，复合句不能。

同样的办法也适用于一次性的提示词 (one-off prompt)，不涉及任何文件：

> 非 STE：`Review the diff and fix the failing test.`
>
> STE：`1. Review the diff. 2. Fix the failing test.`

智能体可以勾掉两个步骤。复合版本只有一个勾选框，却装着两件事。

### 2. 短句是拆开，不是删减 (Rule 5.1)

> 非 STE（25 词）：`Put preservation oil into the unit through the vent hole until the oil level is approximately 6 mm below the surface of the flange cover.`
>
> STE：`Put preservation oil into the unit through the vent hole.`（10 词）`Continue until the oil level is approximately 6 mm below the surface of the flange cover.`（16 词）

程序里每句上限 20 词，描述 (description) 上限 25 词。标准明确要求你把句子拆开。不能为了卡住字数，就把条件删掉。这个区别很关键：大多数"写短点"的建议会产出电报式 (telegraphic) 的文字，而 STE 明确反对这种做法。

### 3. 一个事物，一个名称 (Rule 1.11)

> 非 STE：`1. Make sure that the servo control unit is in the open position. 2. Do the operational test of the actuator. 3. Disconnect the control unit from the test rig.`
>
> STE：`1. Make sure that the actuator is in the open position. 2. Do the operational test of the actuator. 3. Disconnect the actuator from the test rig.`

同义词在散文里读作变化，在程序里读作歧义。读者——或者智能体——分不清 "control unit" 和 "actuator" 是不是同一个物件。

## 它对指令意味着什么

### 测量 (measurement)

我把标准对准了我每次会话都会加载的文件：一份全局规则文件 (`AGENTS.md`)，一份项目规则文件。两者都刚被重写过，所以每一对行，都是同一段文字的前后对比，而不是两种风格的比较。

在技能文件夹 (skill folder) 下运行 `python scripts/ste_lint.py --stats <file>`。这个工具会去掉粗体标记，排除代码块、标题和表格行，并把一个代码片段 (code span) 记作一个词。它按文件打印六个数字：句子数、超过 20 词、超过 25 词、分号、错误、警告。

| 规则文件 | 句子数 | 超过 20 词 | 超过 25 词 | 分号 | 错误 |
|---|---|---|---|---|---|
| 全局 (Global)（改前） | 98 | **21 (21%)** | 11 | 7 | 18 |
| 全局 (Global)（改后） | 147 | **0** | 0 | 0 | 0 |
| 项目 (Project)（改前） | 77 | **17 (22%)** | 6 | 9 | 15 |
| 项目 (Project)（改后） | 116 | **0** | 0 | 0 | 0 |

改造之前，两个文件里大约五分之一的句子突破了 20 词上限。现在每一项都是零。两个文件的长度变化都不大：句子是被拆开的，不是被删掉的。

完整的改前/改后记录，连同统一 diff，都在[重写日志 (rewrite log)](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261019-ste100-rewrite-log.md) 里。

### 最糟的一条 (worst offender)

我全局规则文件里的那条安全规则，试点前接近 60 词，触发条件被埋在三个祈使句后面：

> "**STOP and RAISE HANDS immediately** — halt the run, do not continue, report to the user at once with what was attempted — if executed code reads the filesystem outside `/tmp`…"

那句后面还接着四个触发条件：凭据 (credentials)、数据外泄、子进程或网络连接，以及欺骗行为。我应用了 Rule 5.4（条件在前）和 Rule 5.2（一句话一个动作）：

```
If executed code does any of these things, stop:
- reads files outside /tmp
- touches process.env, keys, tokens, or credentials
- collects or sends local data off the machine
- starts child processes, or opens unauthorized network connections
- shows malicious, harmful, deceptive, cheating, or stealing behavior
Do not continue the run. Report to the user now. Say what was attempted.
```

同一套策略，没有丢掉任何一个条件，四个可勾选的动作，五个平铺的触发条件。改写后并不比原文更短：那条规则从 59 词变成 62 词。STE 用简洁换可核查性，试点也证明了这一点——文件从 18 个 linter 错误降到零。

### SKILL.md 里该改什么

技能 (skill) 只被读一次，就在智能体认为它相关的那一刻。因此规则落在三处：描述 (description)、正文 (body)，以及它点名引用的文件。

- **`description` 就是触发器。** 把它写成一个智能体能匹配的条件："Use when auditing an `AGENTS.md` or a prompt."（在审查 AGENTS.md 或提示词时使用）。不要写成主题标签，比如 "STE compliance helper"。
- **正文就是程序。** 每个编号步骤一个动作，不要复合步骤，步骤里不要夹带推理。排除项 (exclusions) 放进一份扁平清单，或者一张范围表 (scope table)："Never rewrite essays."（绝不改写散文）就是一行可核查的规则。
- **支持文件按路径点名。** 这样智能体不用猜就能打开它们。

`asd-ste100` 技能就是这个形状。它的 description 写明何时加载，它的工作流是一段编号程序，它的范围表写明不许碰什么。

### 这套约束带来什么

- **可核查性 (checkability)。** 一句话一个动作，意味着每条规则都能被勾成"已做"或"未做"。
- **策略与描述之分。** Rule 5.3（祈使语气）要求写 "Run the linter."，而不是 "the linter should be run"——后者是建议，不是规则。
- **条件在前的顺序。** Rule 5.4 直接对应权限规则与安全规则：触发条件必须先被读到，动作在其后。
- **不漂移的同义词。** Rule 1.11 要求每条规则里同一个事物用同一个名字。给配置文件选定一个名字就守住它，不要一条规则里叫 `config`，下一条叫 `settings`。
- **更少的沉默歧义。** 保留冠词 (articles)、使用主动语态 (active voice)（Rules 4.5 和 3.6），能避免那种让短规则无法解析的电报式风格。Rule 4.5 是 Issue 9 新增的。

### 它买不到什么

**它修不了正确性。** 一项用 STE 提示词的公开实验（[Mysore, Oct 2026](https://medium.com/@visrow/karpathy-says-make-your-llm-write-like-an-aircraft-manual-i-built-a-browser-tool-to-measure-it-17f0aaeb86b4)）发现，格式化后的答案仍然漏掉了关键的安全细节。它说 "connect cables to both battery terminals"，却没说是哪根线接哪个端子。形式约束不会让事实变真。任何宣称相反的文章，都是夸大其词。

**策略不是程序。** `AGENTS.md` 承载优先级、例外和理由：*prefer X unless Y. Ask if unsure.*（除非 Y，否则优先 X。不确定就问。）STE 是为"只有一个正确动作"的程序设计的，它没有表达取舍 (tradeoff) 的词汇。把带条件的策略压平成祈使句，会让智能体更字面、更不准确。改动作，把推理留作描述性文字，控制在 25 词以内。

**词典不是可靠的控制手段。** 模型对 STE 的熟悉程度看似合理，但未经测量；875 词的清单也不能直接打包分发。ASD 拥有版权，只对一份名单上的组织授予免费复制权。名单包括 ASD 与 AIA 的成员、他们的客户、各国国防部、适航当局 (airworthiness authorities)，以及用于教育目的的大学。其他人需要 ASD 的书面授权。若你要的是确定性，linter 加上你自己的一份短禁用词表是唯一诚实的路，而不是一条点名了标准的提示词。

**词数在标识符上会失效。** 一个配置文件名、一个路径、一个 API 名称，对人是 1 个词，对计数器是几个词。任何 linter 都必须排除代码片段和标识符，否则每条技术规则都会误判。

**这个 linter 是给自己批作业。** 改写和检查都是我写的，阈值来自我正在论证的那套标准。linter 能测形式。它无法告诉你，改写后的规则是否还表达原来的意思。

**语感流失。** `docs/` 里的文章是散文。在那里套 STE，会把让它们好读的语域 (register) 压平。约束属于指令，不属于散文。这篇文章本身就是散文，所以它保留自己的长句。用 Rule 5.1 去评判它，是范畴错误 (category error)。

## 写成 AGENTS.md 规则，还是做成 SKILL.md？

两个选项并不互斥。把一条短规则放进常驻加载的文件，再加上一个装着程序的技能，两者的代价都很低。这条规则每次会话只花几行上下文，而技能在被加载前不花任何代价。

| 组成 | 放在哪 | 为什么 |
|---|---|---|
| 简短的范围规则 | 常驻规则文件 → Writing conventions 一节，**尚未添加** | 始终加载。短到能被遵守 |
| 完整规则集与改写程序 | `.opencode/skills/asd-ste100/` | 按需加载。53 条规则不该常驻上下文 |
| 确定性检查 | `.opencode/skills/asd-ste100/scripts/ste_lint.py` | 让模型自己判断句长并不可靠 |

只有规则，太含糊，无法执行。只有技能，可能在日常编辑中不被加载。规则界定范围，技能承载细节，脚本裁决争论。

把它装在 OpenCode 本来就会查找的位置：`~/.config/opencode/skills/asd-ste100/SKILL.md` 用于所有会话，或 `.opencode/skills/asd-ste100/SKILL.md` 只用于某个项目。若是共享文件夹，把它的绝对路径加到 `opencode.jsonc` 的 `skills` 数组里。此外什么都不需要，也无需为每个仓库各复制一份。

下面是一条候选的 `AGENTS.md` 规则，短到它自己能遵守。两个规则文件都还没收录它：上面那一轮改写的是既有措辞，今天唯一在执行的还是技能。

```md
**Instruction writing (STE-lite).** Applies to prompts, AGENTS.md, SKILL.md, and checklists — never to articles, essays, or translations.
- Write one action per sentence. Split compound steps.
- Write instructions in the imperative: "Run the linter." Not "the linter should be run".
- Put the condition first, then a comma: "If the check fails, read the log."
- Use one name for one thing. Do not rotate synonyms for a file, command, or concept.
- Keep instructions to 20 words and descriptions to 25. Do not count code spans or identifiers.
- Keep the reason for a rule as description. Do not delete a condition or exception to meet the limit.
- Keep technical names verbatim: paths, commands, identifiers.
For the full standard, load the `asd-ste100` skill.
```

技能位于 `.opencode/skills/asd-ste100/`。它的文件：

| 文件 | 用途 |
|---|---|
| [`SKILL.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/asd-ste100/SKILL.md) | 范围、10 条核心规则、写作与审查两套程序、linter、验证 |
| [`references/rules.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/asd-ste100/references/rules.md) | 按章节压缩的 53 条规则 |
| [`scripts/ste_lint.py`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/asd-ste100/scripts/ste_lint.py) | 句长、分号、禁用词、被动语态、短语动词 |

linter 是让这件事超出"风格偏好"的那一环。有用的检查包括：句长超过 20 或 25 词、代码之外的分号、以及禁用词。禁用词表以 `ensure`、`utilize`、`leverage`、`facilitate`、`commence`、`prior to`、`in order to` 开头。它还会标记被动语态（`be` 加过去分词）和短语动词 (phrasal verbs)。它不检查含义、不检查是否一句话一个动作、也不检查同义词漂移。

## 怎么用

1. **先在一个文件上试点。** 试点在全局规则文件上做，用 `.opencode/skills/asd-ste100/scripts/ste_lint.py --stats` 做了改前与改后的测量。数字站得住之后，才轮到项目文件。
2. **改规则，不改理由。** 把"为什么"的句子留作描述性文字，控制在 25 词以内。为了凑字数删掉推理，是净损失。
3. **从 `STOP and RAISE HANDS` 开始。** 它是风险最高的规则，也是最长的句子。试点从它开始，最后收敛到零错误。
4. **用这个技能。** 把文件夹复制到 `~/.config/opencode/skills/asd-ste100/`（所有会话）或 `.opencode/skills/asd-ste100/`（单个项目）。发布环节是一个工作流 (workflow) 文件 [`.github/workflows/clawhub-skill-sync.yml`](https://github.com/j3ffyang/ai-thoughts/blob/main/.github/workflows/clawhub-skill-sync.yml)，它在 push 时运行。要在合并前审阅，而不是合并后。
5. **别动文章。** 如果 STE 对一篇文章有帮助，它帮的是消除技术步骤里的歧义，而不是把语感压平。

## 还没做完的事

这一轮覆盖了两个规则文件。我逐行读了[重写日志](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261019-ste100-rewrite-log.md)里的两份 diff：没有漏掉任何一条规则、条件或例外。[`asd-ste100`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/asd-ste100/SKILL.md) 技能概括了规则，去掉了词典。它不是标准本身。现在的问题，不再是"这些限制能不能在真实规则上活下来"，而是"改写后的文件，读给人听是否和读给 linter 一样清楚"。

下一步是拿改写后的规则用一周，然后把 linter 接进评审流程。一条无法被检查的规则，一个月内就会漂回原来的形状。

要点不是这套标准。而是上面那份自定义的 `SKILL.md`：复制它，对你的规则跑 linter，先修最长的那条规则。

btw, i use arch
