# 智慧體可以審計的健康檔案

> 簡體版：[智慧體可以審計的健康檔案](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261021-medical-record-review-zh-hans.md)

**原文：** [261021-medical-record-review.md](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261021-medical-record-review.md)

*一套兩層技能 (skill)，用於讓 AI 輔助複閱 (review) 個人與家庭的病歷 (medical record)：通用流程加專案本地事實，不宣稱任何臨床權威。*

**來源：** [`medical-record-review`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/medical-record-review/SKILL.md) 技能，首次於 2026 年 10 月 21 日抽出，於 2026 年 10 月 27 日更新到 1.5.3 版，來自一個私有檔案集 (record set)。該檔案集積累了數年的化驗 (lab)、處方 (prescription)、影像 (imaging) 和衝突 (conflict)。技能是「怎麼做」，本文是「為什麼」。

**論點：** 智慧體 (agent) 在這個領域裡的價值，不是更聰明的分析，而是一套**拒絕猜測 (refuse to guess)** 的流程 (procedure)——遇到衝突就停下，引用所用的來源，把記錄與推斷分開，並且無法悄悄改寫任何一行資料。

**結論：** 證據紀律 (evidence discipline) 可以遷移，臨床判斷 (clinical judgement) 不能。臨床醫生的判斷說了算；技能只負責把證據結構化。把流程發出去，把事實留在本地，並把輸出標註得足夠響，沒人會把它當成醫生。

> ⚠️ **免責宣告。** 這是 AI × 醫療結合的實踐 (practice)，不是醫療器械 (medical device)，也不是官方醫療建議、診斷、處方或治療決定。作者不對使用或誤用的後果承擔任何責任。採用之前，請先讀技能頂部的完整宣告。

![資訊圖：一套兩層的病歷複閱技能——AGENTS.md → 專案層技能 (project-layer skill) → 通用技能 (generic skill) 的權威鏈、十條規則、帶安全護欄的四個階段、技能拒絕做的事，以及「證據紀律可遷移而臨床判斷不可」的結論](../imgs/261021-medical-record-review.png)

## 為什麼是流程，而不是提示詞

病歷不會以乾淨的資料集 (dataset) 形式到手。它們是一堆來自多家機構、跨越多年、許多還是掃描件的 PDF，同一個指標印著三種縮寫和兩種單位。真正有意思的失敗不是「模型不知道 LDL 重要」，而是：模型讀錯了行，把兩家機構參考範圍 (reference range) 不同的值平均了，或者悄悄「修正」了一個看起來不對的數字。

每一種失敗模式都有對應的解法，而這些解法沒有一個是更好的提示詞 (prompt)。它們是衝突協議 (conflict protocol)、只追加規則 (append-only rule)、變更閘門 (change gate) 和證據分級 (evidence grading)。這就是這套技能。

還有第二個約束。這些記錄是一個人擁有的最敏感的檔案，而託管模型 (hosted model) 意味著每讀一個檔案，就是把那個檔案傳出去——不可撤回。所以在讀取第一份記錄之前，外傳預檢 (egress pre-check) 決定要不要開工——而不是分析技巧。所謂外傳 (egress)，就是把本機資料送進模型提供方的上下文；一旦送出去，就收回不來。

## 兩層，一條權威鏈

技能之所以拆開，是因為流程和本地事實的變化速度不同。

```
AGENTS.md (AUTHORITY)         ← project constitution: privacy, egress, evidence standard
  └─ project-layer skill      ← configuration, precedent table, language conventions
       └─ generic skill       ← procedure only, no patient data, no patient paths
```

- **通用層 (generic layer)** 持有工作流：入庫 (intake)、畫像 (profile)、登錄檔 (registry)、比較、衝突協議、證據分級、輸出骨架、合併與改名、壓縮，以及一箇中醫 (Traditional Chinese Medicine, TCM) 子流程。它不攜帶任何病人數值、病人路徑或姓名——這正是它能被公開的原因。
- **專案層 (project layer)** 只持有一個檔案集才成立的東西：九個配置鍵 (config key)（無論是在專案層裡，還是在 `AUTHORITY` 指名的 `AGENTS.md` 小節裡）、語言約定，以及一張記錄真實錯誤及其裁定的**判例表 (precedent table)**。
- **`AGENTS.md` 高於這兩者。** 它是 `AUTHORITY` 指名的那個規則檔案——通常是採用者自己的 `AGENTS.md`，絕不是本流程附帶的一個生效中的權威檔案。技能旁邊附帶了一個不含病人資料的起點模板 [`references/AGENTS.example.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/medical-record-review/references/AGENTS.example.md)：複製它，或者把 `AUTHORITY` 指向智慧體已經在載入的規則檔案。通用層把隱私和外傳交給它，而不是自己重述一遍，因為重述的規則會偏離源頭。

這次拆分也是被一次具體失敗逼出來的。拆之前，通用技能一旦為專案特化，就把病人人口學資訊 (demographics) 硬編碼進了一條分析規則——違反了它自己的「不含病人資料」條款。把一條規則通用化，逼著這個錨點從流程裡移出去、落到配置裡，而它本來就該在那裡。

## 撐著分量的規則

十條規則承擔了大部分工作。每一條都錨定在一次事故或一次複閱發現上，而不是錨定在品味上。其中兩條是在複閱這套技能時定下的：一條是因為一條舊的分析語句已經追溯不回寫它的模型了，另一條是因為一個派生分數無法復現。

| 規則 (rule) | 它禁止什麼 |
|---|---|
| **只追加的資料行 (append-only data rows)** | 就地修改歷史值。錯誤的行走衝突協議 |
| **衝突協議 (conflict protocol)** | 在兩個版本里悄悄挑一個。停下，點名兩者，分類，交給使用者 |
| **變更閘門 (change gate)** | 任何對現有資料行的改動，只要沒有「舊值 → 新值 + 依據」和人類確認 |
| **豁免範圍 (exemption scope)** | 一個覆蓋資料行的使用者豁免。它只覆蓋過程筆記和分析語句 |
| **證據五項 (evidence five)** | 在安全性、事實性、可驗證性、特異性 (specificity) 或可信度 (credibility) 任一項上失敗的論斷。它們降級為 `low-confidence`，轉交臨床複閱 |
| **適用性 (applicability)** | 把一般人群的參考範圍當作久病患者的目標 |
| **歸因時間線 (attribution timeline)** | 把症狀歸咎於一種新藥，而症狀開始於停藥的空檔期 |
| **單一副本 (single copy)** | 派生檢視的第二份複製，或同一個事實在正文、表格和矩陣裡重複出現。複製會漂移，而漂移正是同一天兩個值進入記錄的方式 |
| **派生值算術 (derived-value arithmetic)** | 一個算出來的 eGFR 或指數，沒給出公式、輸入和單位——悄悄算錯比測錯更難發現 |
| **出處戳 (provenance stamp)** | 一個沒有 `model · date · skill version` 行的分析塊，多年之後就無法重新判斷 |

其中兩條特殊到值得展開。**豁免範圍**存在，是因為「讓我整理一下」和「讓我改掉這個數字」會出現在同一句話裡，卻該得到不同答案。**歸因時間線**存在，是因為整份檔案裡最有說服力的錯誤結論，是一個被歸因於新療法的症狀——而那個療法開始於病人已經停掉上一個方案之後好幾周。

工作流本身被畫成四個階段——攝取 (ingest)、分析 (analyse)、輸出 (output)、維護 (maintain)——旁邊還有一張快路徑表。三十秒的回答可以跳過 ASCII 趨勢圖、重讀整個登錄檔和可選模組。它絕不能跳過外傳檢查、衝突閘門、證據分級、一人一個資料夾的規則，或禁止編輯資料行的規則。

## 技能拒絕做的事

- 診斷、指定疾病亞型 (subtype)、開處方，或調整劑量 (dose)。
- 用推斷填補空缺。缺失就是缺失，並且會被點名。
- 跨機構相減，或把它們的趨勢合併。
- 跨檔案批次替換檔名字串。一次批次替換曾改寫了歷史日誌行，而日誌存在的意義正是防止這件事。
- 用行號作為定位。只寫小節標題加條目名；行號會漂移。用 `grep -n` 找行是另一回事。
- 聲稱分析是官方的，或聲稱發生過一次並未發生的複閱。每份輸出都是草稿 (draft)，都可能自信地出錯；沒有一位具名臨床醫生讀過，就不能貼上「已驗證」或「已批准」的標籤。

## 採用它

你需要兩樣東西才能開始：一個能從目錄載入技能、並能讀取本機檔案的智慧體，以及一個讓它讀取的規則檔案。這套流程除此之外假定得很少。

**從一個只放這一件事的資料夾開始。** 不放程式碼，不放無關筆記，不放第二個專案——智慧體自己的技能目錄除外，那是基礎設施，不是專案內容。把規則檔案放在根目錄，把記錄放在它下面。混雜的資料夾會以三種方式失敗：智慧體讀到它本不該看到的檔案，登錄檔把不是記錄的檔案吸收進來，另一個專案的指令和你剛寫下的隱私規則打架。讓這個資料夾遠離任何會推送的倉庫，或者在 git 裡忽略記錄目錄和畫像目錄。

1. **原樣複製通用技能**到你的智慧體載入技能的目錄——OpenCode 是 `<project>/.opencode/skills/medical-record-review/SKILL.md`。不要為遷就你的記錄去改流程；那是專案層的職責。
2. **從規則模板開始。** 把 [`references/AGENTS.example.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/medical-record-review/references/AGENTS.example.md)（與 `SKILL.md` 放在一起隨技能附帶）複製為 `<project>/AGENTS.md`（如果還沒有這個檔案）；如果已經有，就把缺的小節補進去。按這個順序填寫：
   - **先設九個鍵。** `AUTHORITY` 指向這個檔案。`PROFILE` 指明畫像檔案。`DOCS_DIR` 和 `IMGS_DIR` 指明記錄目錄和掃描件目錄。`REGISTRY` 指明趨勢登錄檔，首次執行時建立。`INDEX` / `INDEX_CMD` 指明索引和它的生成器；沒有生成器時，把索引標為 `hand-maintained: true`。`LANG` 設定寫作語言。`MODULES` 啟用分析模組；先只開 `western`。`UNWRAP_CMD` 是可選項。未解析的必需鍵意味著停下，而不是取預設值；可選的鍵也要顯式設定，因為技能表把 `DOCS_DIR` 預設成 `docs/`，那可能是個混雜資料夾。
   - **把畫像放到規則之外。** 模板只裝規則和配置。年齡、性別、診斷及病程、帶服藥時間的用藥、測量條件，寫進 `PROFILE` 指名的檔案。
   - **保留五個規則小節不動。** 隱私、外傳、證據、測量條件、資料變更，是這套技能能跑起來的原因。不要為了省篇幅刪減它們。
   - **跑一遍完整度檢查。** 模板末尾有五項。在讀取第一份記錄之前修好任何失敗項。
   - **絕不要建第二個規則檔案。** 如果專案裡已經有 `AGENTS.md` 或等效的 `CLAUDE.md`，把 `AUTHORITY` 指向它，補上缺的小節。兩個規則檔案會漂移，而漂移正是這套技能存在的理由。
3. **寫一份畫像。** 年齡、性別、診斷及病程、帶服藥時間的用藥、體重的測量條件，以及這個人真正在意的兩三件事。每個值都引用一條來源記錄。不要寫姓名。
4. **建一張判例表。** 三列：發生了什麼、下次怎麼做、來自哪裡。先檢查有沒有現成的規則；把判例折進那條規則，而不是重複一條。這是會複利的部分。
5. **跑一次，然後讓它停下。** 第一個真實衝突就是測試：如果智慧體報告它而不是自行解決，技能就算工作正常。

對家庭來說，規則是一人一個資料夾。配置和畫像按資料夾注入，資料夾之間從不互相引用。跨人比較超出這套流程的範圍，而且會在資料夾之間洩露上下文。

## 這次複閱改了什麼，還有什麼仍然吃緊

第一版技能按它自己的標準被複閱過。四個缺口 (gap) 合上了：兩個成了上表裡的規則，一個收緊了索引契約，一個成了登錄檔小節裡的欄位結構 (schema)：

- **索引 (index) 原本可以手工維護**，這又把技能在別處禁止的「第二份複製」風險放了回來。現在手工維護的索引必須宣告 `hand-maintained: true`，讀者要把每個欄位對著檔案重新核實。
- **非指標序列 (non-metric series) 原本沒有欄位結構。** 症狀、方劑和影像現在有了最小列集——起病時間、歸因狀態；藥味數、劑量；檢查方式、隨訪——而不是隨便落在上一個編輯者留下的地方。
- **派生分數 (derived score) 原本可能被悄悄算錯。** 公式、輸入和單位現在是必需的，缺一項就降級為 `low-confidence`。
- **模型漂移 (model drift) 原本沒有記錄。** 現在每個分析塊都以 `provenance: model · date · skill version` 結尾。

還有三件事仍然吃緊，而且大概永遠會：

- **免責宣告不是法律意見。** 缺少針對具體司法轄區 (jurisdiction) 的條款，也沒有律師讀過責任措辭 (liability language)。
- **規則是文字，不是程式碼檢查器 (linter)。** 沒有任何東西強制執行出處戳或派生值三件套（公式、輸入、單位）；兩者都依賴智慧體記得住——而這恰恰是技能本該解決的問題。
- **輸出骨架沒有強制性的免責宣告。** 免責宣告在技能頂部，不在輸出骨架的七個塊裡。生成的複閱可以把它省掉，所以「把輸出標註清楚」仍然只是建議，不是被強制的步驟。

## 什麼會讓這套做法不值得用

三種結構性條件會讓它不值得用。

如果記錄太稀疏 (sparse)，證據紀律就沒有立足點，誠實的輸出是「資料不足」——而使用者會把它讀成工具失敗。如果託管模型不可接受，工作流必須在本地跑或靠口述；兩種方式都會讓吞吐量和質量下降。如果臨床醫生 (clinician) 始終看不到輸出，技能對「記錄」與「推斷」的仔細區分就白費了。

只有當有人在專業人員的參與下依據它的輸出行動時，這套流程才值得保留。

## 檔案

- [`medical-record-review/SKILL.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/medical-record-review/SKILL.md) — 通用流程：配置鍵、工作流、證據分級、趨勢圖、frontmatter、判例、邊界、地區配置 (locale profile)，以及文章對齊的附錄。文章講為什麼，技能定義怎麼做。
- [`references/AGENTS.example.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/medical-record-review/references/AGENTS.example.md) — 不含病人資料的 `AUTHORITY` 起點模板：隱私紅線、外傳政策、證據標準、資料變更規則、測量條件，以及九個鍵，全部是佔位符。
- 專案層——不公開。它是一個小技能，提供——或指向——九個鍵、語言約定、判例表，以及每人一份畫像。
- [`LICENSE`](https://github.com/j3ffyang/ai-thoughts/blob/main/LICENSE) — MIT。複製這套流程，保留版權宣告。

btw, i use arch
