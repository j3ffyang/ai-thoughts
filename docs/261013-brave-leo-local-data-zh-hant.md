# Brave 的 Leo AI 把你的資料存放在哪裡？

> 簡體版：[Brave 的 Leo AI 把你的資料存放在哪裡？](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261013-brave-leo-local-data-zh-hans.md)

**原文：** [261013-brave-leo-local-data.md](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261013-brave-leo-local-data.md)

*Arch Linux。開啟 `AIChat` —— Brave 的 Leo 側邊欄 (sidebar) 背後那一個 SQLite 檔案 —— 看看這些對話、它讀過的頁面，以及搜尋結果到底存放在哪裡。*

有時候我用 Brave 的 Leo AI，只是為了讀眼前這個頁面：選中文字，讓 Leo 總結一下，關掉側邊欄，然後繼續幹別的。這是最懶的一種 AI 用法 —— 沒有賬號，沒有想儲存的對話，也沒有提示詞工程 (prompt engineering)。正是這種隨意讓我好奇。如果我從來不“儲存”任何東西，它到底去了哪裡？我那一小堆問題、頁面和答案，是放在 Brave 的伺服器上，還是在我自己的磁碟上？於是我去自己的配置檔案 (profile) 裡找了一遍，沒有克隆、也沒有安裝任何東西。

![資訊圖：Brave 的 Leo AI 把你的資料存放在哪裡 —— AIChat 這個 SQLite 儲存、它的資料庫模式 (schema)、v10 AES-128-CBC 加密與 peanuts 回退金鑰、本地儲存與本地處理之別，以及關於團隊使用的結論](../imgs/261013-brave-leo-local-data.png)

## 一個檔案，就在我自己的磁碟上

答案就在我自己的磁碟上，而且幾乎平淡得讓人失望。Leo 關於你的對話保留的一切，都放在瀏覽器配置檔案裡的一個 SQLite 資料庫裡：

```text
~/.config/BraveSoftware/Brave-Browser/Default/AIChat
~/.config/BraveSoftware/Brave-Browser/Default/AIChat-journal
```

我看的時候，`AIChat` 剛過 300 KB，`file` 判定它是 "SQLite 3.x database"。那個 `-journal` 檔案是回滾日誌 (rollback journal)：瀏覽器空閒時它保持 0 位元組，只有在寫入進行中才會增長。這裡沒有 `leo/` 目錄，沒有按對話拆分的 JSON，也沒有同步的文件。就是一個數據庫。

這個單獨的事實就是整篇文章的縮影：你的 AI 歷史和一個普通瀏覽器檔案一樣本地化，也一樣可移植。

有一處例外值得知道：Leo 被要求跨對話記住的那些事實，根本不在這個檔案裡。它們以純字串的形式追加到配置檔案 `Preferences` 裡的 `brave.ai_chat.user_memories` —— 未加密的 JSON，沒有 `v10`，也不需要任何金鑰。在我的配置檔案裡那個列表是空的，但這個設定在出廠時預設是開啟的。對話存在資料庫裡；記憶存在一個偏好設定裡。

## 裡面到底有什麼

Brave 鎖住了這個檔案，所以我開啟的是副本。資料庫模式 (schema) 讀起來就像是對那個側邊欄功能的白話描述：

| 表 (table) | 存放的內容 |
| --- | --- |
| `conversation` | 每一個聊天會話 —— uuid、標題、模型、token 數 |
| `conversation_entry` | 每一輪 (turn) —— 你的提示詞 (prompt)、你選中的文本、日期、模型 |
| `associated_content` | 你正在讀的那個頁面 —— url、標題、Leo 最後一次拉取的內容，以及 `content_used_percentage` |
| `conversation_entry_event_completion` | Leo 的回答，每個完成事件 (completion event) 一行 |
| `conversation_entry_event_search_queries` | Leo 發出的搜尋查詢 (query) |
| `conversation_entry_event_web_sources` | 某次搜尋背後的網頁來源，序列化 (serialized) 後存放 |
| `conversation_entry_event_inline_search` | 內聯搜尋 (inline search) 事件 |
| `conversation_entry_event_tool_use` | 工具呼叫 (tool call) |
| `conversation_entry_uploaded_files` | 你拖進去的檔案，以及從裡面提取出的文本 |
| `ai_chat_sync_metadata` | 同步 (sync) 的記賬資訊 |

在我這臺機器上，我當時看到的：十來個對話、幾十輪對話、十二個關聯頁面、若干次搜尋與內聯搜尋事件，以及零個上傳檔案。

所以“搜尋結果”並不是一樣東西。Leo 跑過的查詢在 `search_queries` 裡；它找到的來源在 `web_sources` 裡；它替我總結的那個頁面在 `associated_content` 裡，緊挨著 `content_used_percentage` —— 也就是模型實際讀到了這個頁面的多少。最後一列悄悄地有用：它告訴你這次摘要是看到了整頁，還是只看到了一部分。在我的頁面上，這一列清一色是 100 —— 沒有一個撞到上限；只有當 Leo 為了塞進模型的上下文 (context) 而截斷一個長頁面時，它才會降到 100 以下。

## 本地儲存 (local storage) 不等於本地處理 (local processing)

在我開始對隱私抒情之前，先說一個前提：存在本地，不等於在本地處理。歷史、頁面和答案都在磁碟上 —— 但提示詞和頁面文本仍然會發到 Brave 的伺服器，並且繼續交給為你所選模型提供服務的第三方模型供應商 (model provider)（Mixtral、Anthropic 的 Claude、Meta 的 Llama），而搜尋查詢則發往 Brave Search。Brave 自己的頁面寫得很明確：瀏覽器會分享“你最新的提示詞、當前對話的上下文，以及——當用例需要時——你正在檢視的頁面中的必要上下文。”

如果這讓你不舒服 —— 而且如果資料安全和隱私是你的優先項，它就該讓你不舒服 —— Leo 可以改用本地模型，通過 BYOM（Bring Your Own Model，自帶模型）：比如在你自己機器上跑 Ollama。那才是把整段對話留在本地磁碟、什麼都不發出去的方式 —— 提示詞不離開，頁面上下文不離開，答案在你自己的硬體上生成。本地資料庫是你做過什麼的回執；本地模型才讓這張回執成為完整的故事。

## “加密” (encryption) 是真的 —— 裡面的保護未必

每一條訊息和頁面相關的列 —— 標題、提示詞、選中的文本、回答、頁面 URL 與內容、搜尋查詢與來源 —— 都是開頭為 `v10` 位元組的 BLOB：

```text
76 31 30 ...   # "v10" + AES-128-CBC ciphertext
```

結構性列是例外：uuid、日期（Windows FILETIME —— 100 納秒的計時單位，不是 Unix 時間）、token 數，以及——值得知道的——`model_key` 都以明文 (cleartext) 儲存，所以你的歷史長什麼樣、到底哪個模型在回答，不用任何金鑰就能讀懂。

那個 `v10` 是 Chromium 的 OSCrypt —— 而 Brave 基於 Chromium，自然繼承了下來。它用的是 AES-128-CBC，和保護已儲存的 cookie 與密碼的是同一套機制。正常情況下金鑰來自系統金鑰環 (keyring，即存放應用金鑰的系統服務)（libsecret、GNOME Keyring、KWallet）。但看看我這臺機器：

- `Local State` 裡的 `os_crypt.portal` 報出 `prev_init_success: false`。
- `secret-tool` 報告沒有可通訊的 Secret Service。

當金鑰環不可用時，Chromium 會退回一個硬編碼的金鑰：`v10` 字首就是那個回退 (fallback) 提供者，它的金鑰由字串 `peanuts` 派生，而 `v11` 才標記由金鑰環支撐的提供者。在沒有 Secret Service 的機器上，比如我這臺，你拿到的就是回退方案 —— 所以 Leo 資料庫的“加密”，意思只是文本編輯器裡顯示亂碼，而不是它是安全的：任何拿到這個檔案副本的人都能讀，不需要登入、不需要金鑰環、也不需要金鑰。寫這篇文章時，我用那把公開金鑰解密了自己的儲存；標題、頁面 URL，以及 Leo 跑過的每一次搜尋查詢，都以明文回來了。它是披著 *encrypted* 這個詞的混淆 (obfuscation)。

這個教訓我已經反覆重新學過：*加密* 這個詞，不知道金鑰在哪就毫無意義。在金鑰環正常工作的桌面上，Leo 的歷史能防住另一個作業系統使用者，也能防住磁碟被偷 —— 不過任何已經以你的身份執行的東西，仍然可以問金鑰環、或者驅動瀏覽器去解密它。在像我這樣的機器上，它向任何複製這個檔案的人敞開。

有兩個控制項能讓上面大半問題失去意義，而且它們都在設定裡：臨時對話 (temporary chat) 根本不會寫進 `AIChat` —— 程式碼拒絕持久化它們 —— 而本地聊天儲存可以整個關掉。在你往那個側邊欄裡打字之前，這些值得知道。

## 這些資料還能用來做什麼

就是這一部分，把一次好奇變成了一個小專案。一個本地 SQLite 資料庫不只是資料的堆積處；它是一份等著被使用的資源。

- **備份它。** 只有一個檔案要複製 —— 但要複製得乾淨：瀏覽器開著時用 `sqlite3 AIChat ".backup leo.db"`，或者乾脆先關掉瀏覽器，這樣你永遠不會撞上寫到一半的狀態。在像我這樣的環境裡，副本到哪都能讀；而在由金鑰環支撐的配置檔案裡，金鑰留在金鑰環裡，所以在沒有舊金鑰環的情況下重灌，會讓備份變成一堆不透明的位元組。把金鑰也匯出，否則備份就不算備份。
- **讀懂自己的注意力。** 因為它是 SQL，這就成了一個關於“你讓 AI 讀什麼、模型消化了多少”的查詢 —— 只有一個坑：`url` 本身就是 `v10` 的 blob，所以直接跑 SQL 拿回來的是密文。誠實的版本是查那些明文列：

  ```sql
  SELECT content_type, content_used_percentage FROM associated_content;
  ```

  要把 URL 拿回來，得先解密那一列 —— 在 `peanuts` 環境裡，用同一把公開金鑰寫幾行 Python 就夠了。
- **審計什麼離開了這臺機器。** 查詢和來源都被記錄下來了。如果你在意自己問過什麼、它去了哪裡，這張回執已經寫好了。
- **搭建個人知識庫。** 對話加上它們碰過的頁面，就是一份閱讀日誌 —— 結構化、帶時間戳、可查詢。可以餵給本地模型，也可以壓縮成筆記。
- **按自己的方式同步。** `ai_chat_sync_metadata` 這張表存在，是因為 Leo 能同步；但一條同步鏈本身也會搬動資料。既然它就是一個數據庫，你可以按自己的方式同步 —— 一個加密目錄、一個被 git 忽略的目錄 —— 而不只是通過 Brave。
- **讓整個迴圈離線。** 有了本地模型，同一個資料庫就變成一個完全離線的迴圈：提示詞、頁面、答案，全在磁碟上，什麼都不出去。

這些都不需要 Brave 開發新功能。它需要的是資料留在本地並且結構化 —— 而這一點已經成立了。

## 整套搬到團隊裡可行嗎？我認為不可行

上面的一切都是一個使用者、一臺機器。下一個顯而易見的問題是公司層面：如果整個團隊都在用 Brave 和 Leo，是否值得把每一次對話都收集起來，用於商業和業務用途 —— 先把隱私放一邊，假定這些全都是團隊業務？

**我的答案是：看過這個檔案之後，不行 —— 那個假定就是整個論證本身，而它站不住。** Leo 會存下提示詞和任何選中的文本、它在 `associated_content` 裡總結過的完整頁面內容，以及任何上傳的檔案和其中提取的文本。人們會往那個側邊欄裡貼上憑據、客戶資料、人力與法務事務，還有私人問題。你收集到的並不是“團隊業務” —— 而是被提升成公司記錄的、附帶產生的個人內容與第三方內容，此後它就成了你要留存、按要求提供、並在洩露後為之辯護的受監管資料。

還有一道實際的高牆：資料並不集中。它住在每個使用者自己的配置檔案裡，Brave 既不保留也不分享它，所以根本沒有一個開關可以開啟。要收集，你要麼掃遍每臺機器（依靠管理策略或 MDM），要麼把 Leo 路由到公司自建的 BYOM 閘道器 (gateway) —— 一個自託管的、相容 OpenAI 的端點 —— 並在那裡記錄。閘道器是唯一站得住腳的收集點，而這是一個工程專案，不是一個設定項。

就算你把它建起來，法律和文化的賬單也是真的：員工監控需要披露，在很多地方還需要合法依據，以及一次 DPIA（資料保護影響評估）或一份工作委員會 (works council) 協議；收集客戶或合作方的內容，可能違反這些內容當初到來時依據的那份 NDA；而存下來的答案只是模型輸出 —— 幻覺 —— 把它們當作權威業務記錄是個錯誤。然後是信任成本：人們會自我審查，或者換到私人裝置上，你最終看到的更少，而不是更多。

價值真正所在的地方是派生出來、經過最小化的那一層 —— 不是原始對話記錄：後設資料與花費、少數自願貢獻的提示詞與答案、洩露憑據或不安全上傳之類的風險訊號，以及可複用的模板。收集那一層，在披露的前提下，最小化地，帶著一個保留期限 —— 而不是每個人的 `AIChat`。

所以：在本地，這是一份值得保留的個人記錄。而作為全公司範圍的收割 —— 把一切都當作團隊業務、把隱私揮揮手抹掉 —— **我認為它不值得。** 收集物件是錯的，假定是錯的，而最便宜的那部分，也就是儲存，是所有成本里最小的。

## 收尾

一件始於懶散問題的事 —— *這些東西去哪了？* —— 結束於我的終端好奇心通常結束的地方：一個我能開啟的檔案、一份我能讀懂的模式，和一個被磨利了的習慣。Leo 對我來說不再是黑箱了。它就是一個 SQLite 檔案、幾張表，和一套我現在能衡量其強弱的“加密”。這個側邊欄給我的，比 *encrypted* 這個詞暗示的要少，比我預期的要多 —— 因為整件事不過就是資料，就在我自己的磁碟上。

## 資料來源

- Brave，*Brave Leo AI* —— 功能、本地聊天曆史、BYOM，以及究竟哪些資料會發送到 Leo 的伺服器 —— <https://brave.com/leo/>
- Chromium，`components/os_crypt` —— OSCrypt 的實現，它加密已儲存的 cookie、密碼，以及這個資料庫 —— <https://chromium.googlesource.com/chromium/src/+/refs/heads/main/components/os_crypt/>
- Chromium，`posix_key_provider.cc` —— `v10` 回退提供者及硬編碼的 `peanuts` 金鑰 —— <https://chromium.googlesource.com/chromium/src/+/refs/heads/main/components/os_crypt/async/browser/posix_key_provider.cc>
- Chromium，`freedesktop_secret_key_provider.cc` —— `v11` 由金鑰環支撐的提供者 —— <https://chromium.googlesource.com/chromium/src/+/refs/heads/main/components/os_crypt/async/browser/freedesktop_secret_key_provider.cc>

btw, i use arch
