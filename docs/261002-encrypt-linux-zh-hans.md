# 加密 Linux：从 20 多年前的一次入侵到 LUKS 与 Veracrypt

**原文：** [261002-encrypt-linux.md](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261002-encrypt-linux.md)

*Arch Linux。LUKS 加密的根分区 (root, xfs)、未加密的 `/boot` (vfat)、Veracrypt USB 卷 (btrfs)。*

我的 Linux 经历可以追溯到 20 多年前。这是一份个人记述：一次入侵如何把我从*检测*篡改推向了*预防*它——以及为什么我现在会加密自己拥有的每一块磁盘。

![信息图：加密 Linux——那次入侵、从检测到预防、LUKS、cryptsetup、开销、Veracrypt 与 rsync 备份](../imgs/261002-encrypt-linux.png)

## 1. 起因：那次入侵 (the hack that started it)

- 我的经历：20 多年前通过猫 (modem) 拨号安装系统时被入侵了好几次。破绽是 `ls`——列出的文件与我确信本该在那里的文件对不上，说明二进制文件已被替换。（这段故事在 Linux 生日那篇里也讲过：[`260828-happy-birthday-linux-from-aix-to-arch.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260828-happy-birthday-linux-from-aix-to-arch.md)。）
- 应对方式是 `tripwire`：它为已安装的二进制文件（如 `/bin/ls`）建立哈希 (hash) 数据库，然后保护这个数据库，使入侵者无法悄悄改写它——最初的 Tripwire 把数据库保存为人类可读的文本，靠文件权限和离线/只读副本来守护；而如今的 Open Source Tripwire 用由口令派生的 site 和 local 密钥对它**签名 (signs)**。检查时把当前的二进制文件与基线 (baseline) 比对；若有二进制被升级或被篡改，就会显现出来，然后你重新计算哈希并更新基线。
- 当年的背景：包管理 (package management) 很弱，所以安装一个独立驱动有时意味着重新编译内核 (compile the kernel)。
- 注：`tripwire` 今天并未装在机器上（历史工具）。现代的文件完整性监控 (file-integrity monitoring)：AIDE，或自建的 `sha256sum` 基线。（`pacman -Qk` 只检查包内文件是否*存在*；`-Qkk` 再加上权限、大小与 mtime——两者都不对内容做哈希，所以一个大小不变、被调包的 `/bin/ls` 能蒙混过关。）

## 2. 转变：从检测到预防 (detection to prevention)

- “在那之后，我对数据库隐私 (database privacy) 与安全变得相当敏感”——并花了大量时间琢磨数据如何在磁盘上被保护、以及笔记本被盗会怎样。
- 用**威胁模型 (threat model)** 来框定：加密能防什么、不能防什么。
  - 能防：**静态 (at rest)** 数据——已关机或被盗的磁盘。
  - 不能防：正在运行、已解锁的机器；操作系统已经打开时的恶意软件 (malware)；而且它的强度仅取决于口令。

## 3. LUKS：加密整个操作系统

- 我的原则：LUKS 加密整个操作系统，**唯独 `/boot` 除外**——它必须在输入任何口令*之前*就可被读取。
- 时机：LUKS 是在**安装操作系统期间**启用的——在创建根文件系统 (root filesystem) 之前就设置好加密分区。它并不适合事后加装到正在使用的根磁盘上，除非重装，或做一次有风险的原地重新加密 (in-place re-encryption)。
- 本机已验证：`/boot` 是 `vfat`（EFI 系统分区），LUKS 分区 (`crypto_LUKS`) 直接承载 `xfs` 根分区（没有 LVM）。`/etc/crypttab` 存在。
- 为什么 `/boot` 保持明文 (cleartext)：固件 (firmware) 与引导加载程序 (bootloader) 必须在磁盘解锁之前读取它；UEFI 的 **ESP** 按规范就是 FAT32。（严谨地说：“`/boot` 必须是 fat32” 实际描述的是 ESP——在非 UEFI 环境下，独立的 `/boot` 也可以是 ext4。）
- 涉及的 `cryptsetup` 命令：`luksFormat`、`luksOpen`、`luksAddKey` / `luksChangeKey`、`luksDump`、`luksHeaderBackup`，以及用于开机解锁的 `/etc/crypttab`。
- 实践中，安装时以及备份头部 (header) 时：
  ```bash
  cryptsetup luksFormat <partition>
  cryptsetup open <partition> root          # 解锁，然后 mkfs + mount
  cryptsetup luksHeaderBackup <partition> --header-backup-file luks-header.img
  ```
  **注意：** `luksFormat` 会**摧毁**目标分区——运行前请确认设备。
- 最要命的坑：**备份 LUKS 头部**——弄丢它，数据就不可恢复。多个 **key slot** 允许设置多个口令。
- 性能：有了硬件 AES（AES-NI，或 ARMv8 加密扩展），开销很小。本机实测 `aes-xts` 512b 约 6 GiB/s（`cryptsetup benchmark`）——比 NVMe 的常见吞吐还快，所以瓶颈是磁盘而非加密。顺序 (sequential) I/O 上预计**几乎没有**延迟，随机 4K 上是低个位数百分比；没有 AES 加速时，代价会跳到 2–3 倍甚至更多。
- TRIM/discard：NVMe 支持 discard，`/etc/crypttab` **没有** `discard` 选项，而 `fstrim.timer` 已启用——所以这套配置用的是**周期性批量 TRIM**，而非持续 discard：既保持磁盘健康，又不会实时泄露哪些块正在被使用。

## 4. Veracrypt：加密分区与 USB 磁盘

- 我的原则：Veracrypt（源自 TrueCrypt）加密**分区**，用来加密我**所有**的 USB 磁盘。
- 时机：与 LUKS 不同，Veracrypt 可以**随时、事后**再应用——在磁盘、分区或容器文件 (container file) 上创建卷 (volume)，无需重装。
- 本机已验证：一个 `veracrypt1` 卷 (btrfs) 挂载在 `/mnt/sda1`。
- 可移动介质 (removable media) 为什么用 Veracrypt 而非 LUKS：跨平台容器 (Linux/Windows/macOS)，以及支持隐藏卷 (hidden volumes)。
- 创建卷是交互式的：`veracrypt -c` 会逐步询问卷类型（分区 vs 容器文件）、大小与算法。**注意：** `veracrypt -c` 会**覆盖**目标——开始前请确认设备或路径。
- 分工：LUKS 用于固定的系统盘；Veracrypt 用于在多台机器之间携带的可移动介质。

## 5. 如果笔记本被盗会怎样

- 静态下，没有口令，LUKS 磁盘毫无用处——这正是全部意义所在，也是采用预启动认证 (pre-boot authentication) 的原因。
- 但未加密的 `/boot` 仍会暴露内核/initramfs，且可能被篡改（**evil-maid**）；一台处于挂起（而非关机）状态的机器会面临冷启动/内存 (cold-boot/RAM) 攻击。这些就是老实的边界。
- 加密不等于备份：磁盘损坏或头部丢失都意味着彻底丢失。唯一的保护是别处有一份加密副本。

## 6. 每日备份：从 LUKS 磁盘 rsync 到 Veracrypt USB

- 例行做法：挂载 Veracrypt 卷，然后用 `rsync` 把 LUKS 加密的家目录 (home) 镜像过去。两端都是在内核中解密的本地块设备 (block device)，所以没有任何东西交给第三方——LUKS 保护源，Veracrypt 保护副本，都是静态保护。
- 在 Veracrypt 卷挂载后（此处它出现在 `/mnt/sda1`，btrfs），每日命令是：
  ```bash
  rsync -aAXH --delete --info=progress2 \
    --exclude='.cache/' \
    --exclude='.local/share/Trash/' \
    $HOME/ /mnt/sda1/backup/
  ```
- 参数说明：`-a` 归档 (archive)（它已经隐含了 `-r` / `--recursive`——递归对任何目录都必不可少，所以实用的 rsync 应当始终覆盖它）；`-A`/`-X` 保留 ACL 与扩展属性 (extended attributes)；`-H` 硬链接 (hard links)；`--delete` 镜像删除（使副本保持真正的镜像）；`--info=progress2` 显示总体进度。源路径末尾的斜杠表示“目录的内容”。
- 首次运行：加上 `-n` / `--dry-run` 预览究竟会改动什么，然后再去掉。
- 要让它真正每日执行，就把它排进计划 (systemd timer 或 cron)，并守护 USB 是否已插入且已挂载。

## 7. 习惯 (habits)

- 加密成了**默认**，而非补救：每一块磁盘上都用 `veracrypt` + `luks`，防火墙链 (firewall chains) 用 `iptables`（从 kernel 2.4+ 起），没有 `openssh` 就不开远程会话。
- 从那时延续至今的主线：安全是一种习惯，而不是一次性的修复（见 [`260828-happy-birthday-linux-from-aix-to-arch.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260828-happy-birthday-linux-from-aix-to-arch.md) 与 [`260706-brave-post.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260706-brave-post.md)）。

## 待解决的问题 (open questions)

- LUKS1 还是 LUKS2？分离头部 (detached header) 还是随附的 (attached)？
- LUKS 头部备份究竟存在哪里、如何测试？
- 是否有完整性工具 (integrity tool) 取代了 `tripwire`？
- 每日 rsync 是手工运行，还是排进了计划 (systemd timer / cron)？

## 验证命令 (verification commands)

```bash
lsblk -o NAME,FSTYPE,MOUNTPOINT
findmnt -no FSTYPE /
findmnt -no FSTYPE /boot
command -v cryptsetup veracrypt
# requires root; inspect key slots and header info
sudo cryptsetup luksDump <luks-device>
```

## 术语表 (glossary)

- **LUKS** —— Linux Unified Key Setup；Linux 磁盘加密的标准盘上格式 (on-disk format)，是 dm-crypt 之上的前端 (front-end)。
- **dm-crypt** —— 执行实际磁盘加密的内核 device-mapper 目标。
- **AES-NI** —— 加速 AES 加密的 CPU 指令；没有它，LUKS 吞吐会急剧下降。
- **Veracrypt** —— 开源、跨平台的卷加密，从 TrueCrypt 分叉而来。
- **tripwire** —— 文件完整性监控器；记录基线哈希，数据库受签名保护（早期版本则是靠文件权限守护的人类可读文件）。
- **ESP** —— EFI 系统分区；UEFI 系统上存放引导加载程序的 FAT32 分区。
- **initramfs** —— 早期启动文件系统镜像，在真正的根挂载之前解锁加密根。
- **threat model** —— 明确说明你在防什么、不防什么。
- **evil-maid** —— 短暂获得物理访问权限、篡改启动路径的攻击者。
- **TRIM / discard** —— SSD 维护操作，同时会泄露哪些块正在被使用。

## 参考来源 (sources)

- `cryptsetup` 文档与 man 手册（`luksFormat`、`luksHeaderBackup`、`luksDump`）。
- Veracrypt 文档（卷类型、隐藏卷、跨平台支持）。
- Open Source Tripwire 上游 README —— 关于签名数据库的行为：[`Tripwire/tripwire-open-source`](https://github.com/Tripwire/tripwire-open-source)。
- 交叉链接：[`260828-happy-birthday-linux-from-aix-to-arch.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260828-happy-birthday-linux-from-aix-to-arch.md)、[`260706-brave-post.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260706-brave-post.md)。

btw, i use arch
