# 生日快乐，Linux——从 AIX 到 Arch 的个人之旅

**原文：** [260828-happy-birthday-linux-from-aix-to-arch.md](260828-happy-birthday-linux-from-aix-to-arch.md)

35 年。**其中大部分，我都在场。**

![信息图：生日快乐，Linux——从 AIX 到 Arch 的个人之旅](../imgs/260828-happy-birthday-linux.png)

免责声明
- 仅限于百分百的个人观点和个人经验
- 无意争论哪个发行版、桌面环境、终端更好或更差
- 它们都只是我的个人偏好，没有别的

关于我的思考方式
- 极简主义 (minimalist)——我尽量去除臃肿软件 (bloatware)
- 对安全（加密）和隐私敏感
- 开源坚定派 (open-source hard-core)

## 一切从哪里开始 (Where It All Began)

上世纪 90 年代初我开始在 IBM 工作，**第一次知道**了 AIX 的存在。

那时我只认识微软的 Windows。我第一次听说 Linux 大约在 1998 年，当时一位同事告诉我他打算**玩玩 Linux**。

2000 年，我有幸加入加拿大多伦多的 IBM 软件实验室，并有机会**接触 Linux**——因为 WebSphere 作为 IBM 的主力中间件 (middleware) 产品之一，需要跑在 Linux 上。

我也开始记录在一个可以追溯到那个年代、一直留到今天的文档里——https://github.com/j3ffyang/instguid——专门存放命令和配置，帮我在**同一处地方**回忆和记住它们。这个仓库看起来不算精致，但它是纯文本，在命令行里就能取用，坐在客户现场时这就足够了。

我仍记得 Lotus Notes 是整个 IBM 内部使用的主要沟通工具，而不巧的是，它是最后没有移植到 Linux 上的主要软件。我不得不用一个**模拟器 (emulator)**在我的 Linux 上运行 Windows 版的 Lotus Notes。在我的记忆里，Lotus Notes 后来终于支持了浏览器版本，所以我不需要再装虚拟机播放器 (virtual machine player)。

## 走进 Linux 安全 (Getting into Linux Security)

那时候我运行的是 Red Hat **个人版 (personal edition)**。

2000 年，我在用猫 (modem) 拨号上网安装系统的过程中**被黑**了好几次。起初，我惊讶地发现 `ls` 列出的二进制文件清单并不真实；于是我用 `tripwire` 去检测被篡改过的二进制文件，才发现它们已经被替换掉了。

然后我花大量业余时间钻研用于加密的 `gnupg` 和 `pgp`。现在我使用 `veracrypt` 和 `luks` 做**磁盘加密 (disk encryption)**。

`openssh` 从此成了**必修课**，与 `rsync` 一起，迅速取代了 `ftp` 和 `telnet`。

我研究 Linux 内核，用 `ipchains`（内核 2.2）再到 `iptables`（内核 2.4 及之后）写了很多脚本，这让我真正理解了**网络流量逻辑 (network traffic logic)**。

从那时起，安全成了**一种习惯**，而不是一时的补救。那些工具也一直留了下来——我至今仍用 `veracrypt` 和 `luks` 加密每一块磁盘，没有 `openssh` 就不开远程会话。我用 `ipchains` 和 `iptables` 搭建的防火墙逻辑，后来在云计算里被证明完全正确：虚拟机的网络活在宿主机的网络内部，既要**保持隔离**，又要能访问外网。

## 发行版岁月 (The Distro Years)

我记得在 IBM 软件实验室做云计算开发时，我创建了一个 Fedora 镜像，把它当作标准的虚拟机镜像来用。后来我发现它因为打开的文件太多而**崩溃**了，如果我没记错的话，是因为 Fedora 内核的默认配置没有限制 `fs.file-max`。于是我意识到自己必须使用 RHEL 这样的**企业级 Linux (enterprise Linux)**，它后来成为实验室面向产品的官方标准 Linux 操作系统。

在工作中，我用 SuSE 和 RHEL 负责**官方产品托管 (product hosting)** 和镜像操作系统。

我算是那种**在 Linux 发行版之间跳来跳去的人 (distro hopper)**。多年来我在 Fedora 和 Ubuntu 之间来回摇摆，然后又用了几年 Debian。最近 8 年是：Manjaro，短暂用过 CachyOS，然后是 Arch。SteamOS 只坚持了 1 天——它是不可变的 (immutable)，不允许我装自己想装的东西。

现在我留在 Arch Linux，它提供**极简安装 (minimal installation)**（依赖更少）和高度自定义。我在 Linux 上的原则是**讨厌臃肿软件 (bloatware)**——比如 `gnome-games`。我不讨厌它们本身，但对我来说它们完全没用又烦人，我从一开始就不想装它们。

## 编译源代码 (Compiling Source Code)

我手动编译源代码并创建**软链接 (soft-link)**。那是很多年前的事了，因为当时经过测试的软件包往往不是最新的源码。所以我得自己下载并**亲自编译**，然后创建软链接，让 Linux 默认就能找到它们——比如 OpenSSL 和 PostgreSQL。我手动管理安装好的软件包。

## 桌面环境 (Desktop Environment)

在我只有 ~4G 内存的时候，我用 `xfce` 作为**轻量级桌面环境**。

在所有的发行版上——Fedora、Ubuntu（不是 Unity）、Manjaro——我都更偏爱 `gnome`，并把 `gnome` 作为首选桌面环境 (DE)，而不是 `kde`，因为 `kde` 看起来**太像 Windows** 了。

受到 Omarchy Linux 的启发，我**转到了 `hyprland`**，并把它用作首选桌面环境整整一年。

## 终端与默认 Shell (Terminals and Default Shell)

我**用了差不多 20 年**的 `terminator`，它需要单独手动安装。偶尔我会用 `gnome-terminal`。我也用 `zsh` 配 `oh-my-zsh` 尝试过相当长一段时间，然而我的脑袋够笨——`bash`——才适合我。现在我改用 `kitty`。

## 软件包管理器 (Package Manager)

这些年来我从 `rpm` 换到 `dnf`，又在 `apt` 和/或 `aptitude` 之间切换（直到现在我也没搞懂它们的本质区别）。现在用的是 `pacman` 和 `yay`（`yay` 是包装 `pacman` 的 AUR 助手），我认为它是 Linux 上**最难用的软件包管理器**。但如果我坚持用 Arch，就别无选择。我从来不用图形界面的软件包管理器——我想直接从终端看到输出，而且我过去也是这样配置软件源位置的。

## 虚拟机、云计算与 Kubernetes (Virtual Machine, Cloud Computing, then Kubernetes)

我先试了 VMware，然后完全切换到 Xen，再到 KVM（`virt-manager`）配合 OpenStack。老实说它不如 VMware 好用，但它是**开源的，所以那是我们的选择**。

底层网络是这样工作的：虚拟机的网络应该**作为私有网络隔离**，同时虚拟机对外部的请求又要被允许经由宿主机的网络出去，通过私有网络地址转换 (NAT)。

进入云计算时代后，几乎一切都**跑在 Linux 上**，连 Azure 数据中心的主机也标配使用 Linux。

再后来 Kubernetes 出现，开始以更标准的方式——**用 YAML 声明式地 (declaratively)**——在**更细粒度**的计算模型上管理所有资源。

## 游戏是件大事 (Game is a Big Thing)

我喜欢**PC 游戏**。请听我说完，我曾经玩过：

- Red Dead Redemption 2
- Splinter Cell: Blacklist
- DCS（数字空战模拟器）
- Mafia I/ II/ III（以后想试试 Old Country）
- 不多，但基本就这些

这就是我不得不为它们保留一个 Windows 分区的原因。2024 年，我不小心弄坏了 `grub` 配置，Windows 分区没了，于是**我在 Linux 上试了 Steam**。没想到模拟器 (emulator) Proton 在 Linux 上配合 Arch（即 Steam 的默认基础系统）跑得非常好，用 Nvidia 4090，后来又换 AMD Radeon RX 显卡。大部分开箱即用，只需一点点微调。

总之，我把所有机器上的**所有 Windows 相关的东西都清除干净了**，确切地说是 4 台机器：一台 ROG Zephyrus G14（Nvidia 4090 16G 显存）、一台 GPD Win4（AMD Radeon 24G 显存）、一台自组台式机（Nvidia 3070）和一台只有核显的旧 Dell XPS；它们全都是 Arch Linux。

我很高兴拥有**一个统一的操作系统**，再也不用担心双系统启动，也不用担心微软不经用户同意就推送的意外更新——他们觉得用户永远是个笨蛋。我所有机器都用同样的方式管理得很好。唯一的区别就是各自的 GPU 专有驱动 :-P

## IDE（集成开发环境）

我是 `vi` 和 `vim` 的重度用户。我通常在 vim 里启用 Python IDE，带自动补全、LSP（语言服务器）、lint、自动缩进等，这样我就可以**在终端里**用 Vim IDE 写 Python 了。

每个软件工程师都需要一个 IDE。我从 Atom Editor 开始用（https://atom-editor.cc/ ——在微软 VS Code **占据主流**之后，于 2022 年停止维护的），然后不得不改用 VS Code，再到 Cursor Editor，日常配上若干个扩展。

我停止使用 Cursor 的智能体 (agent) 功能，因为它不支持自定义 LLM 提供商。现在我只把它当作**markdown 和代码渲染器**，用来画 PlantUML 图。

目前我用 OpenCode 作为我的智能体，它让我可以选择各种 AI 提供商和模型，以 OpenRouter 作为**统一的支付网关 (payment gateway)**。

## 总之，生日快乐，Linux (Anyway, Happy Birthday Linux)

btw, i use arch