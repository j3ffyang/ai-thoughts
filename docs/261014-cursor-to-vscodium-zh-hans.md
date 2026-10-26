# 用一个最小化的 VSCodium AppImage 取代 Cursor

> 繁体版：[用一个最小化的 VSCodium AppImage 取代 Cursor](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261014-cursor-to-vscodium-zh-hant.md)

**原文：** [261014-cursor-to-vscodium.md](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261014-cursor-to-vscodium.md)

**目标：** 一个只做 3 件事、几乎不做别的的编辑器，自包含 (self-contained)，一步即可删除。

**结论：** VSCodium AppImage（一种 Linux 应用打包格式）+ 一套最小化的 Open VSX 扩展 (extension) 组合，就能覆盖全部 3 项功能，不需要新增任何 pacman/AUR 软件包，不需要账号，也没有强制弹出的智能体 (agent) 面板。选择它而不是系统包，是为了“删掉就没了”的模型。

**它必须做的 3 件事：** (1) 带 **git 状态标记 (status tags)** 的文件树；(2) 用 **Vim 键位** 查看/编辑 **源码**；(3) **渲染带 Mermaid + PlantUML 图的 Markdown**。其他一切都被刻意排除在范围之外——细节见下文的“把 3 项功能映射到工具”。

![信息图：用一个最小化的 VSCodium AppImage 取代 Cursor——Cursor 与 VSCodium 的对比、你的代码流向哪里、占用空间，以及三项功能](../imgs/261014-cursor-to-vscodium.png)

## 为什么离开 Cursor

我最不喜欢的两点，其他问题都是它们的下游：

1. **启动时强制打开智能体 (agent)**——智能体是 Cursor 的重心，所以它会自己打开；不存在“只做编辑器”的默认落地状态。
2. **遥测 (telemetry) 与隐私暴露**——这个编辑器在设计上就是一条数据通路 (data path)（下一节展开）。

| 不满之处 | Cursor 的行为 | VSCodium 的行为 |
|---|---|---|
| 启动时强制打开智能体 | 聊天/智能体面板自己打开 | 没有智能体；你在自己的终端（Kitty）里启动 **OpenCode**，完全在 VSCodium 之外 |
| 账号/登录门槛 | 必须登录才能进入这个 AI 原生 (AI-native) 编辑器 | 启动、编辑、安装扩展都**不需要登录** |
| 被单一厂商的智能体锁定 | 内置，只能靠变通办法替换 | 核心开源软件 (OSS) 不绑定特定智能体；OpenCode 只是你自己终端里的一个终端用户界面 (TUI) |
| 更新骚扰 | 频繁、强制的升级提示 | `update.mode: none`；只有**你**替换文件时 AppImage 才更新 |
| 功能臃肿/说教感 | 账号、AI、遥测、提示弹窗 | 通过 `settings.json` 精简到编辑器 + 文件树 + 预览 |

## 遥测 (telemetry) 与终端用户隐私

结构性的区别：**Cursor 的编辑器 *就是* 一条数据通路；VSCodium 的编辑器不是。**

### VSCodium——构建时削弱遥测，且相关设置默认关闭

比“移除”稍弱一些，VSCodium 自己也这么说：他们 *“不传入遥测构建标志，并且想尽办法削弱内置遥测”*，但警告说 *“根据你的设置，Microsoft 仍可能默认追踪使用情况。”* 保证来自一个没有 MS 遥测标志的构建，**再加上**这些偏好项——VSCodium 默认将它们**关闭**（依据其 `docs/telemetry.md`）：

```
telemetry.telemetryLevel
telemetry.enableCrashReporter
telemetry.enableTelemetry
telemetry.editStats.enabled
workbench.enableExperiments
workbench.settings.enableNaturalLanguageSearch
workbench.commandPalette.experimental.enableNaturalLanguageSearch
```

Microsoft 的 *在线服务* 是被**替换**，而不只是禁用：

- **更新检查** → `updateUrl` 指向项目的 GitHub 页面；在 **Linux 上，应用更新服务在构建时就被禁用**，无论 `update.mode` 如何设置。
- **扩展市场 (extension gallery)** → 替换为 **Open VSX**（Eclipse 基金会）；不会调用 Microsoft 市场。
- **欢迎页** 公告从 GitHub 获取（`workbench.welcomePage.extraAnnouncements: false` 可停止）。
- 恶意/弃用扩展列表从 EclipseFdn URL 获取（`extensions.excludeUnsafes: false` 可停止，但代价是安全性）。

剩余的网络面 (network surface) 是上面那个扩展控制列表的获取，加上 (a) 可选加入的元数据 (metadata) 和 (b) 扩展自身的行为。这里的 PlantUML 是**本地**渲染——MPE（Markdown Preview Enhanced）内置的 `plantuml.jar` + 系统 `java`，没有服务器——但有两个诚实的注意事项：**VSCodium 管不了扩展的遥测**（有些扩展，例如 Microsoft 的 C#，会回传数据，那是扩展作者的选择），以及 **MPE 的预览 webview（网页视图）可能从 `cdn.jsdelivr.net` 获取资源**（获取 JS/CSS，不是代码外泄 (code egress)）。审计实际连接：

```sh
# while VSCodium is idle, expect zero established connections
ss -tpn | grep -i codium
# or, per-socket, watch during extension install
lsof -i -a -c VSCodium
```

也不需要账号：VSCodium 从不会要求你登录才能启动、编辑或安装扩展——*“只有当扩展主动要求时才会发生账号认证”*（`docs/accounts-authentication.md`）。它唯一的登录是可选的、基于令牌 (token) 的（`Sign in with GitHub`，只有 GitLens 这类扩展需要时才用）：没有账号墙，不像 Cursor 的启动流程。

### Cursor——AI 优先，所以所有流量都按设计经过它的后端

摘自 Cursor 自己的 *Data Use & Privacy Overview*（更新于 2026-09-03）：

- **隐私模式 (Privacy Mode) 关闭（它是一个开关，不是底线）：** *“我们可能使用并存储代码库数据、提示词 (prompt)、编辑器操作、代码片段……来改进我们的 AI 功能并训练我们的模型。”* 打开后，训练会停止（与提供商签订零数据保留 (zero-data-retention) 协议）——但风险/滥用分类器仍可能运行，一旦触发，*“你的数据可能被存储用于调查。”*
- **你自己的 API key 也绕不过去：** *“即使你使用自己的 API key，你的请求仍然会经过我们的后端！我们就是在那里做最终的提示词构建。”*
- **文件内容会缓存在 Cursor 的服务器上**（加密、临时），以降低延迟；客户端会为 API、更新和市场调用 Cursor 的后端域名。

你可以用隐私模式退出 *训练*，但你无法退出 *路由 (routing)*——编辑器和智能体是同一个产品，而这个产品就是后端。

### 净效果

| | 代码流向哪里 | 何时 | 流向谁 |
|---|---|---|---|
| **Cursor** | 按设计流向 Cursor 后端 | 正常的编辑器/智能体使用时 | Cursor，然后是它们的模型子处理商 (subprocessor) |
| **VSCodium + OpenCode** | 只有在你调用智能体时才离开本机 | 你运行 OpenCode 时 | *你*配置的提供商，按*该*提供商的条款 |

所以，弃用 Cursor 就移除了一条你无法控制的常驻数据通路；用 VSCodium 时，编辑器是惰性的，唯一的出口 (egress) 是你刻意调用的 OpenCode，指向你选择的提供商。

## 把 3 项功能映射到工具

1. **带 git 状态标记的文件导航器** → 资源管理器 (Explorer) + **内置的** `git` 扩展 (`git.decorations.enabled`)。不需要额外依赖——`git` 已经安装。
2. **查看/编辑源码，包括 Markdown** → 内置编辑器 + Markdown 语法，由 **Vim** 键位驱动 (`vscodevim.vim`)。
3. **Markdown 渲染 + mermaid + plantuml 图** → **Mermaid 已内置于默认预览**（作为内置的 `mermaid-markdown-features` 扩展提供）；**PlantUML** 来自 **Markdown Preview Enhanced** (`shd101wyy.markdown-preview-enhanced`)，通过其内置的 `plantuml.jar` + 系统 `java` **本地**渲染。MPE 也能渲染 Mermaid，所以两种预览都可以——下面的设置说明会处理 MPE 的一个默认值，它会隐藏内置预览按钮。

## 已验证的环境（只读检查）

| 事实 | 值 |
|---|---|
| FUSE（用户态文件系统，AppImage 运行时） | `fuse2 2.9.9-6`、`fuse3 3.18.3-1`、`/usr/bin/fusermount{3}` 已设置 setuid——存在 |
| 现有 Cursor | AppImage 已不在；只剩配置（见“占用空间”） |
| `git` | `2.56.0` |
| 图表依赖 | `graphviz` 已安装，`jre-openjdk 27` 已安装，`~/pool/Downloads/rog_drive/plantuml.jar` 已存在 |
| OpenCode | `1.19.0`，位于 `~/.opencode/bin/opencode` |
| 最新 VSCodium | `1.140.06880`（GitHub releases 上发布了 `x86_64` AppImage） |

## 安装——AppImage，已校验校验和 (checksum)

非 root，不用 pacman。AppImage 位于系统包数据库之外；删除它除了配置目录外不会留下足迹。选择它而不是 AUR 的 `vscodium-bin` / `extra/code`（会拖入 pacman 依赖）和 Flatpak（会拖入整个运行时），正是为了这一点：自包含、删掉即走。

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

**注意：** AppImage 的 `anylinux` 构建在 Arch 的 glibc 上可直接运行；如果某次无法自挂载 (self-mount)，用 `--appimage-extract-and-run` 运行（不需要 FUSE）。这里 FUSE 已存在，所以预计不会遇到。

**更新：** 下载新的 AppImage，然后让 `VSCodium.AppImage` 重新指向它（`ln -sf "VSCodium-$VER-anylinux-x86_64.AppImage" VSCodium.AppImage`）；没有任何东西会自动更新，扩展也只按需刷新。

## 扩展（Open VSX，无需 Microsoft 账号）

Open VSX 是 Eclipse 基金会的厂商中立 (vendor-neutral) 扩展**注册表 (registry)**——Microsoft Visual Studio Marketplace 的免费替代品，后者只授权给官方 VS Code 使用（所以像 VSCodium 这样的 OSS 构建用不了）。VSCodium 的扩展库默认指向它，所以不需要市场标志，也不需要 Microsoft 账号。这套组合刻意保持**三个**——内置核心已经能做的事，不重复添加。安装量来自 Open VSX API（可随时复查其中任何一个，例如 `curl -s https://open-vsx.org/api/shd101wyy/markdown-preview-enhanced | jq .downloadCount`）：

| 功能 | 扩展（ID） | 版本 | Open VSX 安装量 |
|---|---|---|---|
| **Vim 键位**（主要编辑模式） | `vscodevim.vim` | 1.32.4 | 1,956,779 |
| **Markdown 预览 + PlantUML**（自带预览；也覆盖 Mermaid） | `shd101wyy.markdown-preview-enhanced` | 0.8.40 | 2,437,299 |
| **Markdown → PDF**（可选） | `yzane.markdown-pdf` | 2.2.0 | 255,423 |

```sh
V=~/.local/bin/VSCodium.AppImage

$V --install-extension vscodevim.vim
$V --install-extension shd101wyy.markdown-preview-enhanced
$V --install-extension yzane.markdown-pdf
```

- **Vim** (`vscodevim.vim`) 在进程内模拟 Vim；`useNeovim` 默认关闭，所以**不会新增系统 `vim`/`neovim` 依赖**。
- **Markdown PDF** (`yzane.markdown-pdf`) 是三项功能之外的附加项（仅导出）；它通过 **`puppeteer-core` 驱动的 Chromium** 渲染，而不是编辑器的 Electron。
- **Mermaid 已内置——不需要扩展。** VSCodium 自带一个内置的 `mermaid-markdown-features` 扩展（已在 AppImage 内验证），所以默认预览开箱就能渲染 ` ```mermaid ` 围栏。因此去掉了 `bierner.markdown-mermaid`。
- **PlantUML 通过 MPE 本地渲染。** MPE 通过捆绑的 `plantuml.jar` + 你的 `jre-openjdk 27` 在**本机**渲染，不使用服务器。这取代了被去掉的 `jebbs.plantuml`。
- **CDN（内容分发网络）注意事项（诚实）：** MPE 的预览 webview 可能从 `jsdelivrCdnHost`（默认 `cdn.jsdelivr.net`）加载库——预览时是 *获取资源* 的网络请求，不是代码外泄。要完全离线预览，你得把这些资源本地化；否则预计会有 CDN 调用。

## 最小化的 `settings.json`

写入 `~/.config/VSCodium/User/settings.json`——不会碰 `~/.config/Cursor/`。其他一切保持默认。

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

- `git.decorations.enabled` 提供功能 (1) 要求的文件树**标记**——每个状态一个字母（`M`/`A`/`U`），带颜色，不需要额外扩展。
- `window.restoreWindows: none` + `workbench.startupEditor: none` 把落地状态固定在资源管理器 + 编辑器，所以没有任何东西（智能体面板、恢复的面板）会自动打开。
- `vim.useSystemClipboard` 让 Vim 模式共享系统剪贴板。
- MPE 的这些键让 PlantUML 保持本地：`plantumlServer` 为空 = 使用内置 jar，它自己的描述说 *“`java` 需要在系统 PATH 中”*；`plantumlJarPath` 指向你自己的 jar（删掉它就用 MPE 捆绑的那个）；`hideDefaultVSCodeMarkdownPreviewButtons: false` 让内置预览按钮留在 MPE 的按钮旁边（它的默认值 `true` 会隐藏内置按钮）。
- `markdown-pdf.executablePath` 把 PDF 导出器固定到系统 Chromium，所以 `puppeteer-core` 永远不会自动下载 Chrome。
- 遥测相关的键与 VSCodium 的隐私默认值一致，除了 `telemetry.feedback.enabled` 和 `workbench.welcomePage.extraAnnouncements`——VSCodium 会保留这两个。其余是对上游默认值的刻意偏离：`update.mode`、两个扩展更新键、`workbench.startupEditor`、`workbench.tips.enabled`、`window.restoreWindows`、`editor.minimap.enabled`、`vim.useSystemClipboard`、`markdown-pdf.executablePath`、`plantumlJarPath` 和 `hideDefaultVSCodeMarkdownPreviewButtons`。把它们列出来能让意图更明确，也能在导入设置后保留。

## 在编辑器之外使用 OpenCode

没有扩展，也没有集成。在你自己的终端模拟器里运行 OpenCode——这里是 **Kitty**，完全在 VSCodium 之外：

```
opencode
```

VSCodium 永远不会自己打开智能体面板，OpenCode 也从不运行在它里面。这就是弃用 Cursor 的全部要点：编辑器和智能体是两个独立进程。

## 可选——启动器条目和 `$PATH`

只有当你想要菜单/快捷键启动时才需要。`~/.local/share/applications/VSCodium.desktop`：

```ini
[Desktop Entry]
Type=Application
Name=VSCodium
Exec=/home/jeff/.local/bin/VSCodium.AppImage %F
Terminal=false
Categories=Utility;TextEditor;Development;
MimeType=text/plain;text/markdown;inode/directory;
```

AppImage 不会安装图标，所以省略 `Icon=`（如上），或者用 `$V --appimage-extract 'code.svg'` 提取真正的图标——图标是 `code.svg`（也是 `.DirIcon`），而 `*.png` 会拉出 170 多个无关的 UI 图标，不是应用图标。把 `Icon=` 指向提取出来的 SVG。Shell 用法：`ln -s "$V" ~/.local/bin/codium`。

## 这不是什么（诚实的权衡）

- **它仍然是 Electron——赢的是行为，不是体积。** 磁盘上解压后约 **795 MiB**（`du`），约 10 个进程——不是 Unix 式的节俭程序。VSCodium 是 *Cursor 减去 AI、遥测、更新服务器和强制智能体*：AppImage 只比 Cursor 的小约 34%，真正的成本是解压后的目录树（见下面的“占用空间”）。
- **如果哪天受不了 Electron，** 终端原生的退路是 `nvim` + `gitsigns`/`neo-tree` + `render-markdown.nvim` + `plantuml.jar`——更轻，但要 N 个插件，而且没有浏览器级预览。

### 占用空间

| 产物 | 字节 | MiB |
|---|---:|---:|
| Cursor AppImage（移除前） | 294,255,096 | 280.6 |
| VSCodium AppImage | 193,460,378 | 184.5 |
| VSCodium 解压后磁盘占用 (`du`) | 833,792,301 | 795.2 |
| 留下的 Cursor 配置 (`~/.config/Cursor` + `~/.cursor`) | — | ≈ 825 |

## 回滚/卸载

一切都包含在：

```sh
rm -f ~/.local/bin/VSCodium.AppImage ~/.local/bin/VSCodium-*.AppImage*
rm -rf ~/.config/VSCodium ~/.vscode-oss ~/.cache/VSCodium ~/.local/share/VSCodium
rm -f ~/.local/bin/codium ~/.local/share/applications/VSCodium.desktop
```

没有新增 pacman 包；没有其他东西引用它。

### 如果你也要退役 Cursor（手动）

Cursor 是手动移除的，与 VSCodium 的卸载**分开**。删除应用和任何启动器，然后删除它留下的配置（见“占用空间”）：

```sh
# adjust the AppImage path to wherever you kept Cursor
rm -f ~/Downloads/Cursor-*.AppImage ~/.local/bin/cursor ~/.local/share/applications/cursor.desktop
rm -rf ~/.config/Cursor ~/.cursor
ls -d ~/.config/Cursor ~/.cursor 2>/dev/null || echo "Cursor purged"
```

无论哪种方式都不涉及 pacman 包——Cursor 从未进入系统包数据库。

## 验证清单

- [ ] 首次运行前 `sha256sum -c` 通过
- [ ] 在脏仓库里，资源管理器显示带颜色的 `M`/`A`/`U` git 标记
- [ ] 打开 `.md` 文件并按 `Ctrl+Shift+V` 能渲染 Markdown
- [ ] ` ```mermaid ` 块能在内置预览中渲染（不需要扩展）
- [ ] ` ```plantuml ` 能在 MPE 的预览中渲染，且没有 PlantUML 服务器连接（`ss -tpn | grep -i codium`；关闭 Wi-Fi *不是*干净的测试，因为 MPE 的 webview 还会从 `cdn.jsdelivr.net` 获取 JS/CSS）
- [ ] 24 小时后没有更新提示
- [ ] 启动时或安装扩展期间没有登录/登录提示
- [ ] `opencode` 能在 Kitty 中运行，完全在 VSCodium 之外
- [ ] 空闲时，`ss -tpn | grep -i codium` 没有已建立的连接

btw, i use arch
