# 用一個最小化的 VSCodium AppImage 取代 Cursor

> 簡體版：[用一個最小化的 VSCodium AppImage 取代 Cursor](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261014-cursor-to-vscodium-zh-hans.md)

**原文：** [261014-cursor-to-vscodium.md](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261014-cursor-to-vscodium.md)

**目標：** 一個只做 3 件事、幾乎不做別的的編輯器，自包含 (self-contained)，一步即可刪除。

**結論：** VSCodium AppImage（一種 Linux 應用打包格式）+ 一套最小化的 Open VSX 擴充套件 (extension) 組合，就能覆蓋全部 3 項功能，不需要新增任何 pacman/AUR 軟體包，不需要賬號，也沒有強制彈出的智慧體 (agent) 面板。選擇它而不是系統包，是為了“刪掉就沒了”的模型。

**它必須做的 3 件事：** (1) 帶 **git 狀態標記 (status tags)** 的檔案樹；(2) 用 **Vim 鍵位** 檢視/編輯 **原始碼**；(3) **渲染帶 Mermaid + PlantUML 圖的 Markdown**。其他一切都被刻意排除在範圍之外——細節見下文的“把 3 項功能對映到工具”。

![資訊圖：用一個最小化的 VSCodium AppImage 取代 Cursor——Cursor 與 VSCodium 的對比、你的程式碼流向哪裡、佔用空間，以及三項功能](../imgs/261014-cursor-to-vscodium.png)

## 為什麼離開 Cursor

我最不喜歡的兩點，其他問題都是它們的下游：

1. **啟動時強制開啟智慧體 (agent)**——智慧體是 Cursor 的重心，所以它會自己開啟；不存在“只做編輯器”的預設落地狀態。
2. **遙測 (telemetry) 與隱私暴露**——這個編輯器在設計上就是一條資料通路 (data path)（下一節展開）。

| 不滿之處 | Cursor 的行為 | VSCodium 的行為 |
|---|---|---|
| 啟動時強制開啟智慧體 | 聊天/智慧體面板自己開啟 | 沒有智慧體；你在自己的終端（Kitty）裡啟動 **OpenCode**，完全在 VSCodium 之外 |
| 賬號/登入門檻 | 必須登入才能進入這個 AI 原生 (AI-native) 編輯器 | 啟動、編輯、安裝擴充套件都**不需要登入** |
| 被單一廠商的智慧體鎖定 | 內建，只能靠變通辦法替換 | 核心開源軟體 (OSS) 不繫結特定智慧體；OpenCode 只是你自己終端裡的一個終端使用者介面 (TUI) |
| 更新騷擾 | 頻繁、強制的升級提示 | `update.mode: none`；只有**你**替換檔案時 AppImage 才更新 |
| 功能臃腫/說教感 | 賬號、AI、遙測、提示彈窗 | 通過 `settings.json` 精簡到編輯器 + 檔案樹 + 預覽 |

## 遙測 (telemetry) 與終端使用者隱私

結構性的區別：**Cursor 的編輯器 *就是* 一條資料通路；VSCodium 的編輯器不是。**

### VSCodium——構建時削弱遙測，且相關設定預設關閉

比“移除”稍弱一些，VSCodium 自己也這麼說：他們 *“不傳入遙測構建標誌，並且想盡辦法削弱內建遙測”*，但警告說 *“根據你的設定，Microsoft 仍可能預設追蹤使用情況。”* 保證來自一個沒有 MS 遙測標誌的構建，**再加上**這些偏好項——VSCodium 預設將它們**關閉**（依據其 `docs/telemetry.md`）：

```
telemetry.telemetryLevel
telemetry.enableCrashReporter
telemetry.enableTelemetry
telemetry.editStats.enabled
workbench.enableExperiments
workbench.settings.enableNaturalLanguageSearch
workbench.commandPalette.experimental.enableNaturalLanguageSearch
```

Microsoft 的 *線上服務* 是被**替換**，而不只是停用：

- **更新檢查** → `updateUrl` 指向專案的 GitHub 頁面；在 **Linux 上，應用更新服務在構建時就被停用**，無論 `update.mode` 如何設定。
- **擴充套件市場 (extension gallery)** → 替換為 **Open VSX**（Eclipse 基金會）；不會呼叫 Microsoft 市場。
- **歡迎頁** 公告從 GitHub 獲取（`workbench.welcomePage.extraAnnouncements: false` 可停止）。
- 惡意/棄用擴充套件列表從 EclipseFdn URL 獲取（`extensions.excludeUnsafes: false` 可停止，但代價是安全性）。

剩餘的網路面 (network surface) 是上面那個擴充套件控制列表的獲取，加上 (a) 可選加入的後設資料 (metadata) 和 (b) 擴充套件自身的行為。這裡的 PlantUML 是**本地**渲染——MPE（Markdown Preview Enhanced）內建的 `plantuml.jar` + 系統 `java`，沒有伺服器——但有兩個誠實的注意事項：**VSCodium 管不了擴充套件的遙測**（有些擴充套件，例如 Microsoft 的 C#，會回傳資料，那是擴充套件作者的選擇），以及 **MPE 的預覽 webview（網頁檢視）可能從 `cdn.jsdelivr.net` 獲取資源**（獲取 JS/CSS，不是程式碼外洩 (code egress)）。審計實際連線：

```sh
# while VSCodium is idle, expect zero established connections
ss -tpn | grep -i codium
# or, per-socket, watch during extension install
lsof -i -a -c VSCodium
```

也不需要賬號：VSCodium 從不會要求你登入才能啟動、編輯或安裝擴充套件——*“只有當擴充套件主動要求時才會發生賬號認證”*（`docs/accounts-authentication.md`）。它唯一的登入是可選的、基於令牌 (token) 的（`Sign in with GitHub`，只有 GitLens 這類擴充套件需要時才用）：沒有賬號牆，不像 Cursor 的啟動流程。

### Cursor——AI 優先，所以所有流量都按設計經過它的後端

摘自 Cursor 自己的 *Data Use & Privacy Overview*（更新於 2026-09-03）：

- **隱私模式 (Privacy Mode) 關閉（它是一個開關，不是底線）：** *“我們可能使用並存儲程式碼庫資料、提示詞 (prompt)、編輯器操作、程式碼片段……來改進我們的 AI 功能並訓練我們的模型。”* 開啟後，訓練會停止（與提供商簽訂零資料保留 (zero-data-retention) 協議）——但風險/濫用分類器仍可能執行，一旦觸發，*“你的資料可能被儲存用於調查。”*
- **你自己的 API key 也繞不過去：** *“即使你使用自己的 API key，你的請求仍然會經過我們的後端！我們就是在那裡做最終的提示詞構建。”*
- **檔案內容會快取在 Cursor 的伺服器上**（加密、臨時），以降低延遲；客戶端會為 API、更新和市場呼叫 Cursor 的後端域名。

你可以用隱私模式退出 *訓練*，但你無法退出 *路由 (routing)*——編輯器和智慧體是同一個產品，而這個產品就是後端。

### 淨效果

| | 程式碼流向哪裡 | 何時 | 流向誰 |
|---|---|---|---|
| **Cursor** | 按設計流向 Cursor 後端 | 正常的編輯器/智慧體使用時 | Cursor，然後是它們的模型子處理商 (subprocessor) |
| **VSCodium + OpenCode** | 只有在你呼叫智慧體時才離開本機 | 你執行 OpenCode 時 | *你*配置的提供商，按*該*提供商的條款 |

所以，棄用 Cursor 就移除了一條你無法控制的常駐資料通路；用 VSCodium 時，編輯器是惰性的，唯一的出口 (egress) 是你刻意呼叫的 OpenCode，指向你選擇的提供商。

## 把 3 項功能對映到工具

1. **帶 git 狀態標記的檔案導航器** → 資源管理器 (Explorer) + **內建的** `git` 擴充套件 (`git.decorations.enabled`)。不需要額外依賴——`git` 已經安裝。
2. **檢視/編輯原始碼，包括 Markdown** → 內建編輯器 + Markdown 語法，由 **Vim** 鍵位驅動 (`vscodevim.vim`)。
3. **Markdown 渲染 + mermaid + plantuml 圖** → **Mermaid 已內置於預設預覽**（作為內建的 `mermaid-markdown-features` 擴充套件提供）；**PlantUML** 來自 **Markdown Preview Enhanced** (`shd101wyy.markdown-preview-enhanced`)，通過其內建的 `plantuml.jar` + 系統 `java` **本地**渲染。MPE 也能渲染 Mermaid，所以兩種預覽都可以——下面的設定說明會處理 MPE 的一個預設值，它會隱藏內建預覽按鈕。

## 已驗證的環境（只讀檢查）

| 事實 | 值 |
|---|---|
| FUSE（使用者態檔案系統，AppImage 執行時） | `fuse2 2.9.9-6`、`fuse3 3.18.3-1`、`/usr/bin/fusermount{3}` 已設定 setuid——存在 |
| 現有 Cursor | AppImage 已不在；只剩配置（見“佔用空間”） |
| `git` | `2.56.0` |
| 圖表依賴 | `graphviz` 已安裝，`jre-openjdk 27` 已安裝，`~/pool/Downloads/rog_drive/plantuml.jar` 已存在 |
| OpenCode | `1.19.0`，位於 `~/.opencode/bin/opencode` |
| 最新 VSCodium | `1.140.06880`（GitHub releases 上釋出了 `x86_64` AppImage） |

## 安裝——AppImage，已校驗校驗和 (checksum)

非 root，不用 pacman。AppImage 位於系統包資料庫之外；刪除它除了配置目錄外不會留下足跡。選擇它而不是 AUR 的 `vscodium-bin` / `extra/code`（會拖入 pacman 依賴）和 Flatpak（會拖入整個執行時），正是為了這一點：自包含、刪掉即走。

```sh
mkdir -p ~/.local/bin
cd ~/.local/bin

VER=1.140.06880
BASE=https://github.com/VSCodium/vscodium/releases/download/$VER
curl -fLO "$BASE/VSCodium-$VER-anylinux-x86_64.AppImage"
curl -fLO "$BASE/VSCodium-$VER-anylinux-x86_64.AppImage.sha256"

sha256sum -c "VSCodium-$VER-anylinux-x86_64.AppImage.sha256"

chmod +x "VSCodium-$VER-anylinux-x86_64.AppImage"
ln -sf "VSCodium-$VER-anylinux-x86_64.AppImage" VSCodium.AppImage   # stable name, survives version bumps
```

**注意：** AppImage 的 `anylinux` 構建在 Arch 的 glibc 上可直接執行；如果某次無法自掛載 (self-mount)，用 `--appimage-extract-and-run` 執行（不需要 FUSE）。這裡 FUSE 已存在，所以預計不會遇到。

**更新：** 下載新的 AppImage，然後讓 `VSCodium.AppImage` 重新指向它（`ln -sf "VSCodium-$VER-anylinux-x86_64.AppImage" VSCodium.AppImage`）；沒有任何東西會自動更新，擴充套件也只按需重新整理。

## 擴充套件（Open VSX，無需 Microsoft 賬號）

Open VSX 是 Eclipse 基金會的廠商中立 (vendor-neutral) 擴充套件**登錄檔 (registry)**——Microsoft Visual Studio Marketplace 的免費替代品，後者只授權給官方 VS Code 使用（所以像 VSCodium 這樣的 OSS 構建用不了）。VSCodium 的擴充套件庫預設指向它，所以不需要市場標誌，也不需要 Microsoft 賬號。這套組合刻意保持**三個**——內建核心已經能做的事，不重複新增。安裝量來自 Open VSX API（可隨時複查其中任何一個，例如 `curl -s https://open-vsx.org/api/shd101wyy/markdown-preview-enhanced | jq .downloadCount`）：

| 功能 | 擴充套件（ID） | 版本 | Open VSX 安裝量 |
|---|---|---|---|
| **Vim 鍵位**（主要編輯模式） | `vscodevim.vim` | 1.32.4 | 1,956,779 |
| **Markdown 預覽 + PlantUML**（自帶預覽；也覆蓋 Mermaid） | `shd101wyy.markdown-preview-enhanced` | 0.8.40 | 2,437,299 |
| **Markdown → PDF**（可選） | `yzane.markdown-pdf` | 2.2.0 | 255,423 |

```sh
V=~/.local/bin/VSCodium.AppImage

$V --install-extension vscodevim.vim
$V --install-extension shd101wyy.markdown-preview-enhanced
$V --install-extension yzane.markdown-pdf
```

- **Vim** (`vscodevim.vim`) 在程序內模擬 Vim；`useNeovim` 預設關閉，所以**不會新增系統 `vim`/`neovim` 依賴**。
- **Markdown PDF** (`yzane.markdown-pdf`) 是三項功能之外的附加項（僅匯出）；它通過 **`puppeteer-core` 驅動的 Chromium** 渲染，而不是編輯器的 Electron。
- **Mermaid 已內建——不需要擴充套件。** VSCodium 自帶一個內建的 `mermaid-markdown-features` 擴充套件（已在 AppImage 內驗證），所以預設預覽開箱就能渲染 ` ```mermaid ` 圍欄。因此去掉了 `bierner.markdown-mermaid`。
- **PlantUML 通過 MPE 本地渲染。** MPE 通過捆綁的 `plantuml.jar` + 你的 `jre-openjdk 27` 在**本機**渲染，不使用伺服器。這取代了被去掉的 `jebbs.plantuml`。
- **CDN（內容分發網路）注意事項（誠實）：** MPE 的預覽 webview 可能從 `jsdelivrCdnHost`（預設 `cdn.jsdelivr.net`）載入庫——預覽時是 *獲取資源* 的網路請求，不是程式碼外洩。要完全離線預覽，你得把這些資源本地化；否則預計會有 CDN 呼叫。

## 最小化的 `settings.json`

寫入 `~/.config/VSCodium/User/settings.json`——不會碰 `~/.config/Cursor/`。其他一切保持預設。

```json
{
  "update.mode": "none",
  "extensions.autoCheckUpdates": false,
  "extensions.autoUpdate": false,
  "telemetry.telemetryLevel": "off",
  "telemetry.feedback.enabled": false,
  "workbench.startupEditor": "none",
  "workbench.tips.enabled": false,
  "workbench.enableExperiments": false,
  "workbench.welcomePage.extraAnnouncements": false,
  "workbench.settings.enableNaturalLanguageSearch": false,
  "workbench.commandPalette.experimental.enableNaturalLanguageSearch": false,
  "window.restoreWindows": "none",
  "editor.minimap.enabled": false,
  "git.enabled": true,
  "git.decorations.enabled": true,
  "vim.useSystemClipboard": true,
  "markdown-pdf.executablePath": "/usr/bin/chromium",
  "markdown-preview-enhanced.plantumlServer": "",
  "markdown-preview-enhanced.plantumlJarPath": "/home/jeff/pool/Downloads/rog_drive/plantuml.jar",
  "markdown-preview-enhanced.hideDefaultVSCodeMarkdownPreviewButtons": false
}
```

- `git.decorations.enabled` 提供功能 (1) 要求的檔案樹**標記**——每個狀態一個字母（`M`/`A`/`U`），帶顏色，不需要額外擴充套件。
- `window.restoreWindows: none` + `workbench.startupEditor: none` 把落地狀態固定在資源管理器 + 編輯器，所以沒有任何東西（智慧體面板、恢復的面板）會自動開啟。
- `vim.useSystemClipboard` 讓 Vim 模式共享系統剪貼簿。
- MPE 的這些鍵讓 PlantUML 保持本地：`plantumlServer` 為空 = 使用內建 jar，它自己的描述說 *“`java` 需要在系統 PATH 中”*；`plantumlJarPath` 指向你自己的 jar（刪掉它就用 MPE 捆綁的那個）；`hideDefaultVSCodeMarkdownPreviewButtons: false` 讓內建預覽按鈕留在 MPE 的按鈕旁邊（它的預設值 `true` 會隱藏內建按鈕）。
- `markdown-pdf.executablePath` 把 PDF 匯出器固定到系統 Chromium，所以 `puppeteer-core` 永遠不會自動下載 Chrome。
- 遙測相關的鍵與 VSCodium 的隱私預設值一致，除了 `telemetry.feedback.enabled` 和 `workbench.welcomePage.extraAnnouncements`——VSCodium 會保留這兩個。其餘是對上游預設值的刻意偏離：`update.mode`、兩個擴充套件更新鍵、`workbench.startupEditor`、`workbench.tips.enabled`、`window.restoreWindows`、`editor.minimap.enabled`、`vim.useSystemClipboard`、`markdown-pdf.executablePath`、`plantumlJarPath` 和 `hideDefaultVSCodeMarkdownPreviewButtons`。把它們列出來能讓意圖更明確，也能在匯入設定後保留。

## 在編輯器之外使用 OpenCode

沒有擴充套件，也沒有整合。在你自己的終端模擬器裡執行 OpenCode——這裡是 **Kitty**，完全在 VSCodium 之外：

```
opencode
```

VSCodium 永遠不會自己開啟智慧體面板，OpenCode 也從不執行在它裡面。這就是棄用 Cursor 的全部要點：編輯器和智慧體是兩個獨立程序。

## 可選——啟動器條目和 `$PATH`

只有當你想要選單/快捷鍵啟動時才需要。`~/.local/share/applications/VSCodium.desktop`：

```ini
[Desktop Entry]
Type=Application
Name=VSCodium
Exec=/home/jeff/.local/bin/VSCodium.AppImage %F
Terminal=false
Categories=Utility;TextEditor;Development;
MimeType=text/plain;text/markdown;inode/directory;
```

AppImage 不會安裝圖示，所以省略 `Icon=`（如上），或者用 `$V --appimage-extract 'code.svg'` 提取真正的圖示——圖示是 `code.svg`（也是 `.DirIcon`），而 `*.png` 會拉出 170 多個無關的 UI 圖示，不是應用圖示。把 `Icon=` 指向提取出來的 SVG。Shell 用法：`ln -s "$V" ~/.local/bin/codium`。

## 這不是什麼（誠實的權衡）

- **它仍然是 Electron——贏的是行為，不是體積。** 磁碟上解壓後約 **795 MiB**（`du`），約 10 個程序——不是 Unix 式的節儉程式。VSCodium 是 *Cursor 減去 AI、遙測、更新伺服器和強制智慧體*：AppImage 只比 Cursor 的小約 34%，真正的成本是解壓後的目錄樹（見下面的“佔用空間”）。
- **如果哪天受不了 Electron，** 終端原生的退路是 `nvim` + `gitsigns`/`neo-tree` + `render-markdown.nvim` + `plantuml.jar`——更輕，但要 N 個外掛，而且沒有瀏覽器級預覽。

### 佔用空間

| 產物 | 位元組 | MiB |
|---|---:|---:|
| Cursor AppImage（移除前） | 294,255,096 | 280.6 |
| VSCodium AppImage | 193,460,378 | 184.5 |
| VSCodium 解壓後磁碟佔用 (`du`) | 833,792,301 | 795.2 |
| 留下的 Cursor 配置 (`~/.config/Cursor` + `~/.cursor`) | — | ≈ 825 |

## 回滾/解除安裝

一切都包含在：

```sh
rm -f ~/.local/bin/VSCodium.AppImage ~/.local/bin/VSCodium-*.AppImage*
rm -rf ~/.config/VSCodium ~/.vscode-oss ~/.cache/VSCodium ~/.local/share/VSCodium
rm -f ~/.local/bin/codium ~/.local/share/applications/VSCodium.desktop
```

沒有新增 pacman 包；沒有其他東西引用它。

### 如果你也要退役 Cursor（手動）

Cursor 是手動移除的，與 VSCodium 的解除安裝**分開**。刪除應用和任何啟動器，然後刪除它留下的配置（見“佔用空間”）：

```sh
# adjust the AppImage path to wherever you kept Cursor
rm -f ~/Downloads/Cursor-*.AppImage ~/.local/bin/cursor ~/.local/share/applications/cursor.desktop
rm -rf ~/.config/Cursor ~/.cursor
ls -d ~/.config/Cursor ~/.cursor 2>/dev/null || echo "Cursor purged"
```

無論哪種方式都不涉及 pacman 包——Cursor 從未進入系統包資料庫。

## 驗證清單

- [ ] 首次執行前 `sha256sum -c` 通過
- [ ] 在髒倉庫裡，資源管理器顯示帶顏色的 `M`/`A`/`U` git 標記
- [ ] 開啟 `.md` 檔案並按 `Ctrl+Shift+V` 能渲染 Markdown
- [ ] ` ```mermaid ` 塊能在內建預覽中渲染（不需要擴充套件）
- [ ] ` ```plantuml ` 能在 MPE 的預覽中渲染，且沒有 PlantUML 伺服器連線（`ss -tpn | grep -i codium`；關閉 Wi-Fi *不是*乾淨的測試，因為 MPE 的 webview 還會從 `cdn.jsdelivr.net` 獲取 JS/CSS）
- [ ] 24 小時後沒有更新提示
- [ ] 啟動時或安裝擴充套件期間沒有登入/登入提示
- [ ] `opencode` 能在 Kitty 中執行，完全在 VSCodium 之外
- [ ] 空閒時，`ss -tpn | grep -i codium` 沒有已建立的連線

btw, i use arch
