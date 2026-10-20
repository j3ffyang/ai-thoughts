# 規則，而非詞語：ASD-STE100 與智慧體指令

> 簡體版：[規則，而非詞語：ASD-STE100 與智慧體指令](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261019-ste100-agent-instructions-zh-hans.md)

**原文：** [261019-ste100-agent-instructions.md](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261019-ste100-agent-instructions.md)

*ASD-STE100 是一門為飛機維修手冊而設的受控語言 (controlled language)。它有 53 條寫作規則，和一份 875 詞的詞典。*

**來源：** Andrej Karpathy，X 推文串 (thread)，2026 年 10 月 1 日 17:37 PDT（2026 年 10 月 2 日 00:37 UTC）—— [x.com/karpathy/status/2105819303471976479](https://x.com/karpathy/status/2105819303471976479)

**論點：** 在 AI 工作中，價值在規則，而不在詞典。這些規則是：**一句話一個動作、祈使語氣、條件在前、一個事物一個名稱。** 它們直擊智慧體指令 (agent instructions) 的失敗模式——一個無法勾選核對的複合句。

**結論：** 只把規則用在指令上，絕不用於文章。保留那些高價值的詞彙替換。把 Karpathy 的建議看作起點，而不是標準：他本人也只要求"達到 ASD-STE100 的 80%"。

![Infographic: ASD-STE100 for agent instructions — the standard's two parts, the four rules that carry the work, a compound prompt split into two steps, the measured before-and-after counts, rule versus skill versus linter, and the four things the standard cannot buy](../imgs/261019-ste100-agent-instructions.png)

## 這條建議從哪來

這條推文串講的是如何閱讀模型輸出，而不是泛泛的提示詞技巧 (prompting tricks)。Karpathy 的第一個建議，是讓模型用 ASD-STE100 解釋某件事——"一份受控語言規範 (controlled language specification)"，最初為飛機維修手冊而開發。他說模型對這個標準相當熟悉，它"對乾淨寫作風格的嚴苛約束"能產出他覺得"可讀性強得多"的文字。他也承認這份規範"相當嚴格"，有時會把要求放寬成"達到 ASD-STE100 的 80%"。

推文的其餘部分離開了寫作：先是圖表，然後是 HTML 頁面，再是 3Blue1Brown 風格的講解影片，每一個都被稱作"更好"。所以這條帖子真正講的是更容易驗證的輸出格式。STE 這條建議是四者中唯一的語言約束，也是試起來最省力的那一個。

有一個跳躍值得點明。Karpathy 是讓模型寫給人看。這篇文章是讓人寫給智慧體看。兩個方向並不對稱。人遇到歧義句，可以追問一句。而在無人看管時載入 `AGENTS.md` 的智慧體，通常不會問。它會挑一種讀法，然後照著做。這種不對稱，正是規則可以遷移、而證據不能的原因。下面要講的失敗模式，就寫在文字本身裡。

有兩點要誠實說明。第一，這是軼事（"我試過，有效"），不是基準測試 (benchmark)。第二，我自己寫的 **`asd-ste100` SKILL.md** 就是範例：

[https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/asd-ste100/SKILL.md](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/asd-ste100/SKILL.md)

那份檔案不含標準的詞典。ASD 只授權特定組織複製。

## ASD-STE100 究竟是什麼

ASD 把這項工作追溯到 1970 年代末：一個為歐洲航空公司設立的 AECMA 專案，美國的 AIA 也受邀參與。第一版指南問世於 1986 年。現行版本 Issue 9 於 2025 年 1 月釋出，這份文件也在那時成為國際標準 (international standard)。它可以免費閱讀：從 [asd-ste100.org](https://www.asd-ste100.org/) 開始，下面的每條規則、每個例子都出自那裡的 [Issue 9 PDF](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)。

它存在的理由很窄，也很有用：供非英語母語者閱讀的維修文件，讀錯一句就可能出人命。這個出身既解釋了它的長處，也解釋了它的邊界。它在"只有一個正確動作"的程式 (procedure) 上非常出色。它不是通用的散文 (prose) 風格。

它的範圍分兩部分，其中只有一部分是詞表：

- **第 1 部分——53 條寫作規則。** 語法、句長、動詞形式、安全指令、寫作實踐。
- **第 2 部分——受控詞典 (controlled dictionary)。** Issue 9 收錄 **875 個批准詞 (approved words)** 和 **1,274 個未批准詞 (non-approved words)** 及其替換詞。FAQ 把它約等於"約 900 個"。舉例來說，`ensure (v)` 未被批准，替換詞是 `MAKE SURE (v)`。未批准詞表就是這類替換：標準裡最無趣的部分，也是人們最容易高估的部分。

詞典不是硬牆。技術名詞和技術動詞 (technical nouns and verbs) 按設計就是開放的（標準的 Rules 1.5–1.13）：公司、行業或專業領域可以新增自己的術語。規則禁止的是把這些術語用得太隨意——當動詞用、給同一個物件換不同名字、或當行話 (jargon) 用。

最省力的收益先來：幾個替換詞，加上兩條結構規則，各配一個小例子。之後還有三條結構規則。

- `make sure`——"Make sure that the valve is closed."（確保閥門已關閉）。不要用 "verify" 或 "ensure"。
- `remove`、`install`、`set`——一個動作一個動詞："Remove the four bolts."（拆下四顆螺栓）"Install the new O-ring."（裝上新的 O 型圈）"Set the switch to ON."（把開關撥到 ON）。
- `do`——通用動作動詞 (generic action verb)："Do the pressure test."（做壓力測試）。不要用 "perform" 或 "conduct"。
- 條件在前——"When the light comes on, set the switch to NORMAL."（燈亮時，把開關撥到 NORMAL）。
- 不用分號——寫成兩句話："Examine the removed parts for damage. Replace the damaged parts."（檢查拆下的零件有無損傷。更換損壞的零件）。

## 標準裡的三個例子

### 1. 一句話一條指令 (Rule 5.2)

> 非 STE：`Set the TEST switch to the middle position and release the SHORT-CIRCUIT TEST switch.`
>
> STE：`A. Set the TEST switch to the middle position.` / `B. Release the SHORT-CIRCUIT TEST switch.`

規則允許一個例外：同時發生的兩個動作，可以留在一句話裡（"Remove and discard the seal."，取下並丟棄密封件）。有先後順序的動作，則拆成各自獨立的步驟。這是我在提示詞上最想先用的一條規則，因為編號步驟可以核對，複合句不能。

同樣的辦法也適用於一次性的提示詞 (one-off prompt)，不涉及任何檔案：

> 非 STE：`Review the diff and fix the failing test.`
>
> STE：`1. Review the diff. 2. Fix the failing test.`

智慧體可以勾掉兩個步驟。複合版本只有一個勾選框，卻裝著兩件事。

### 2. 短句是拆開，不是刪減 (Rule 5.1)

> 非 STE（25 詞）：`Put preservation oil into the unit through the vent hole until the oil level is approximately 6 mm below the surface of the flange cover.`
>
> STE：`Put preservation oil into the unit through the vent hole.`（10 詞）`Continue until the oil level is approximately 6 mm below the surface of the flange cover.`（16 詞）

程式裡每句上限 20 詞，描述 (description) 上限 25 詞。標準明確要求你把句子拆開。不能為了卡住字數，就把條件刪掉。這個區別很關鍵：大多數"寫短點"的建議會產出電報式 (telegraphic) 的文字，而 STE 明確反對這種做法。

### 3. 一個事物，一個名稱 (Rule 1.11)

> 非 STE：`1. Make sure that the servo control unit is in the open position. 2. Do the operational test of the actuator. 3. Disconnect the control unit from the test rig.`
>
> STE：`1. Make sure that the actuator is in the open position. 2. Do the operational test of the actuator. 3. Disconnect the actuator from the test rig.`

同義詞在散文裡讀作變化，在程式裡讀作歧義。讀者——或者智慧體——分不清 "control unit" 和 "actuator" 是不是同一個物件。

## 它對指令意味著什麼

### 測量 (measurement)

我把標準對準了我每次會話都會載入的檔案：一份全域性規則檔案 (`AGENTS.md`)，一份專案規則檔案。兩者都剛被重寫過，所以每一對行，都是同一段文字的前後對比，而不是兩種風格的比較。

在技能資料夾 (skill folder) 下執行 `python scripts/ste_lint.py --stats <file>`。這個工具會去掉粗體標記，排除程式碼塊、標題和表格行，並把一個程式碼片段 (code span) 記作一個詞。它按檔案列印六個數字：句子數、超過 20 詞、超過 25 詞、分號、錯誤、警告。

| 規則檔案 | 句子數 | 超過 20 詞 | 超過 25 詞 | 分號 | 錯誤 |
|---|---|---|---|---|---|
| 全域性 (Global)（改前） | 98 | **21 (21%)** | 11 | 7 | 18 |
| 全域性 (Global)（改後） | 147 | **0** | 0 | 0 | 0 |
| 專案 (Project)（改前） | 77 | **17 (22%)** | 6 | 9 | 15 |
| 專案 (Project)（改後） | 116 | **0** | 0 | 0 | 0 |

改造之前，兩個檔案裡大約五分之一的句子突破了 20 詞上限。現在每一項都是零。兩個檔案的長度變化都不大：句子是被拆開的，不是被刪掉的。

完整的改前/改後記錄，連同統一 diff，都在[重寫日誌 (rewrite log)](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261019-ste100-rewrite-log.md) 裡。

### 最糟的一條 (worst offender)

我全域性規則檔案裡的那條安全規則，試點前接近 60 詞，觸發條件被埋在三個祈使句後面：

> "**STOP and RAISE HANDS immediately** — halt the run, do not continue, report to the user at once with what was attempted — if executed code reads the filesystem outside `/tmp`…"

那句後面還接著四個觸發條件：憑據 (credentials)、資料外洩、子程序或網路連線，以及欺騙行為。我應用了 Rule 5.4（條件在前）和 Rule 5.2（一句話一個動作）：

```
If executed code does any of these things, stop:
- reads files outside /tmp
- touches process.env, keys, tokens, or credentials
- collects or sends local data off the machine
- starts child processes, or opens unauthorized network connections
- shows malicious, harmful, deceptive, cheating, or stealing behavior
Do not continue the run. Report to the user now. Say what was attempted.
```

同一套策略，沒有丟掉任何一個條件，四個可勾選的動作，五個平鋪的觸發條件。改寫後並不比原文更短：那條規則從 59 詞變成 62 詞。STE 用簡潔換可核查性，試點也證明了這一點——檔案從 18 個 linter 錯誤降到零。

### SKILL.md 裡該改什麼

技能 (skill) 只被讀一次，就在智慧體認為它相關的那一刻。因此規則落在三處：描述 (description)、正文 (body)，以及它點名引用的檔案。

- **`description` 就是觸發器。** 把它寫成一個智慧體能匹配的條件："Use when auditing an `AGENTS.md` or a prompt."（在審查 AGENTS.md 或提示詞時使用）。不要寫成主題標籤，比如 "STE compliance helper"。
- **正文就是程式。** 每個編號步驟一個動作，不要複合步驟，步驟裡不要夾帶推理。排除項 (exclusions) 放進一份扁平清單，或者一張範圍表 (scope table)："Never rewrite essays."（絕不改寫散文）就是一行可核查的規則。
- **支援檔案按路徑點名。** 這樣智慧體不用猜就能開啟它們。

`asd-ste100` 技能就是這個形狀。它的 description 寫明何時載入，它的工作流是一段編號程式，它的範圍表寫明不許碰什麼。

### 這套約束帶來什麼

- **可核查性 (checkability)。** 一句話一個動作，意味著每條規則都能被勾成"已做"或"未做"。
- **策略與描述之分。** Rule 5.3（祈使語氣）要求寫 "Run the linter."，而不是 "the linter should be run"——後者是建議，不是規則。
- **條件在前的順序。** Rule 5.4 直接對應許可權規則與安全規則：觸發條件必須先被讀到，動作在其後。
- **不漂移的同義詞。** Rule 1.11 要求每條規則裡同一個事物用同一個名字。給配置檔案選定一個名字就守住它，不要一條規則裡叫 `config`，下一條叫 `settings`。
- **更少的沉默歧義。** 保留冠詞 (articles)、使用主動語態 (active voice)（Rules 4.5 和 3.6），能避免那種讓短規則無法解析的電報式風格。Rule 4.5 是 Issue 9 新增的。

### 它買不到什麼

**它修不了正確性。** 一項用 STE 提示詞的公開實驗（[Mysore, Oct 2026](https://medium.com/@visrow/karpathy-says-make-your-llm-write-like-an-aircraft-manual-i-built-a-browser-tool-to-measure-it-17f0aaeb86b4)）發現，格式化後的答案仍然漏掉了關鍵的安全細節。它說 "connect cables to both battery terminals"，卻沒說是哪根線接哪個端子。形式約束不會讓事實變真。任何宣稱相反的文章，都是誇大其詞。

**策略不是程式。** `AGENTS.md` 承載優先順序、例外和理由：*prefer X unless Y. Ask if unsure.*（除非 Y，否則優先 X。不確定就問。）STE 是為"只有一個正確動作"的程式設計的，它沒有表達取捨 (tradeoff) 的詞彙。把帶條件的策略壓平成祈使句，會讓智慧體更字面、更不準確。改動作，把推理留作描述性文字，控制在 25 詞以內。

**詞典不是可靠的控制手段。** 模型對 STE 的熟悉程度看似合理，但未經測量；875 詞的清單也不能直接打包分發。ASD 擁有版權，只對一份名單上的組織授予免費複製權。名單包括 ASD 與 AIA 的成員、他們的客戶、各國國防部、適航當局 (airworthiness authorities)，以及用於教育目的的大學。其他人需要 ASD 的書面授權。若你要的是確定性，linter 加上你自己的一份短停用詞表是唯一誠實的路，而不是一條點名了標準的提示詞。

**詞數在識別符號上會失效。** 一個配置檔名、一個路徑、一個 API 名稱，對人是 1 個詞，對計數器是幾個詞。任何 linter 都必須排除程式碼片段和識別符號，否則每條技術規則都會誤判。

**這個 linter 是給自己批作業。** 改寫和檢查都是我寫的，閾值來自我正在論證的那套標準。linter 能測形式。它無法告訴你，改寫後的規則是否還表達原來的意思。

**語感流失。** `docs/` 裡的文章是散文。在那裡套 STE，會把讓它們好讀的語域 (register) 壓平。約束屬於指令，不屬於散文。這篇文章本身就是散文，所以它保留自己的長句。用 Rule 5.1 去評判它，是範疇錯誤 (category error)。

## 寫成 AGENTS.md 規則，還是做成 SKILL.md？

兩個選項並不互斥。把一條短規則放進常駐載入的檔案，再加上一個裝著程式的技能，兩者的代價都很低。這條規則每次會話只花幾行上下文，而技能在被載入前不花任何代價。

| 組成 | 放在哪 | 為什麼 |
|---|---|---|
| 簡短的範圍規則 | 常駐規則檔案 → Writing conventions 一節，**尚未新增** | 始終載入。短到能被遵守 |
| 完整規則集與改寫程式 | `.opencode/skills/asd-ste100/` | 按需載入。53 條規則不該常駐上下文 |
| 確定性檢查 | `.opencode/skills/asd-ste100/scripts/ste_lint.py` | 讓模型自己判斷句長並不可靠 |

只有規則，太含糊，無法執行。只有技能，可能在日常編輯中不被載入。規則界定範圍，技能承載細節，指令碼裁決爭論。

把它裝在 OpenCode 本來就會查詢的位置：`~/.config/opencode/skills/asd-ste100/SKILL.md` 用於所有會話，或 `.opencode/skills/asd-ste100/SKILL.md` 只用於某個專案。若是共享資料夾，把它的絕對路徑加到 `opencode.jsonc` 的 `skills` 數組裡。此外什麼都不需要，也無需為每個倉庫各複製一份。

下面是一條候選的 `AGENTS.md` 規則，短到它自己能遵守。兩個規則檔案都還沒收錄它：上面那一輪改寫的是既有措辭，今天唯一在執行的還是技能。

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

技能位於 `.opencode/skills/asd-ste100/`。它的檔案：

| 檔案 | 用途 |
|---|---|
| [`SKILL.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/asd-ste100/SKILL.md) | 範圍、10 條核心規則、寫作與審查兩套程式、linter、驗證 |
| [`references/rules.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/asd-ste100/references/rules.md) | 按章節壓縮的 53 條規則 |
| [`scripts/ste_lint.py`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/asd-ste100/scripts/ste_lint.py) | 句長、分號、停用詞、被動語態、短語動詞 |

linter 是讓這件事超出"風格偏好"的那一環。有用的檢查包括：句長超過 20 或 25 詞、程式碼之外的分號、以及停用詞。停用詞表以 `ensure`、`utilize`、`leverage`、`facilitate`、`commence`、`prior to`、`in order to` 開頭。它還會標記被動語態（`be` 加過去分詞）和短語動詞 (phrasal verbs)。它不檢查含義、不檢查是否一句話一個動作、也不檢查同義詞漂移。

## 怎麼用

1. **先在一個檔案上試點。** 試點在全域性規則檔案上做，用 `.opencode/skills/asd-ste100/scripts/ste_lint.py --stats` 做了改前與改後的測量。數字站得住之後，才輪到專案檔案。
2. **改規則，不改理由。** 把"為什麼"的句子留作描述性文字，控制在 25 詞以內。為了湊字數刪掉推理，是淨損失。
3. **從 `STOP and RAISE HANDS` 開始。** 它是風險最高的規則，也是最長的句子。試點從它開始，最後收斂到零錯誤。
4. **用這個技能。** 把資料夾複製到 `~/.config/opencode/skills/asd-ste100/`（所有會話）或 `.opencode/skills/asd-ste100/`（單個專案）。釋出環節是一個工作流 (workflow) 檔案 [`.github/workflows/clawhub-skill-sync.yml`](https://github.com/j3ffyang/ai-thoughts/blob/main/.github/workflows/clawhub-skill-sync.yml)，它在 push 時執行。要在合併前審閱，而不是合併後。
5. **別動文章。** 如果 STE 對一篇文章有幫助，它幫的是消除技術步驟裡的歧義，而不是把語感壓平。

## 還沒做完的事

這一輪覆蓋了兩個規則檔案。我逐行讀了[重寫日誌](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261019-ste100-rewrite-log.md)裡的兩份 diff：沒有漏掉任何一條規則、條件或例外。[`asd-ste100`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/asd-ste100/SKILL.md) 技能概括了規則，去掉了詞典。它不是標準本身。現在的問題，不再是"這些限制能不能在真實規則上活下來"，而是"改寫後的檔案，讀給人聽是否和讀給 linter 一樣清楚"。

下一步是拿改寫後的規則用一週，然後把 linter 接進評審流程。一條無法被檢查的規則，一個月內就會漂回原來的形狀。

要點不是這套標準。而是上面那份自定義的 `SKILL.md`：複製它，對你的規則跑 linter，先修最長的那條規則。

btw, i use arch
