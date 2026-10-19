# Unix 是艺术 (Unix Is Art)

> 繁体版：[Unix 是艺术 (Unix Is Art)](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261011-unix-is-art-zh-hant.md)

**原文：** [261011-unix-is-art.md](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261011-unix-is-art.md)

Unix 哲学不是一份规格说明 (specification)。没有哪个委员会批准过它，也没有任何标准定义过它——POSIX 标准化的是调用 (call)，不是品味。它是一套文化惯例 (cultural norms)——软件设计上的民间传统 (folk tradition)——围绕贝尔实验室 (Bell Labs) 的一个操作系统生长起来，又比那个系统活得更久。**Eric S. Raymond** 写这件事的书甚至就叫《Unix 编程艺术》(*The Art of Unix Programming*)，而“艺术”这个词正是关键：这套哲学像手艺 (craft) 一样，靠范例和习惯传承，就像一间工坊教人如何造物。这就是它的故事——从 1960 年代末到 2004 年乃至更晚——以及把这一切串起来的思想。

![信息图：Unix 是艺术——核心论点、1969 至 2004 年的时间线、原则、另一面、纪念 Dennis Ritchie，以及 Unix 如何塑造了我](../imgs/261011-unix-is-art.png)

## 历史 (History)

它始于一种约束。1969–70 年，在贝尔实验室 (Bell Labs)，**Ken Thompson** 与 **Dennis Ritchie** 在一台配有慢速打印终端 (printing terminal) 的小机器上构建了一个操作系统——机器的限制成了它的风格。正如 **Raymond** 所说，这套哲学“起源于 **Ken Thompson** 早期的思考：如何用一个干净的服务接口 (service interface) 设计出小巧却够用的操作系统”。小不是偏好，而是预算。

**Ritchie** 和 **Thompson** 把设计考量写进了 1974 年发表于《ACM 通讯》(*Communications of the ACM*) 的论文《The UNIX Time-Sharing System》（UNIX 分时系统），读起来像一条诞生于匮乏的信条：让程序易于编写、测试和运行；用交互式使用 (interactive use) 取代批处理 (batch processing)；*因为*体积限制而追求经济与优雅 (economy and elegance)——借用一句现成的话，“在苦难中得救” (salvation through suffering)；并让系统自给自足 (self-supporting)，所有 Unix 软件都在 Unix 下维护。

到 1978 年，这种风格有了代言人。**Doug McIlroy**——发明 Unix 管道 (pipe) 的人——只是把周围人早已在做的事记了下来，写在他为《贝尔系统技术期刊》(*Bell System Technical Journal*) Unix 专号所写的序言里：让每个程序只把一件事做好，宁可从头构建，也不要给旧工具硬加功能；预期每个程序的输出都会成为另一个尚不可知的程序的输入。让软件尽早被试用，最好在几周之内，并且毫不迟疑地扔掉那些笨拙的部分；宁可用工具，也不用不熟练的帮手，哪怕工具得你自己造。后来他把这整套东西压缩成一句我重复了三十年的话：*写只做一件事并把它做好的程序；写能协同工作的程序；写处理文本流的程序，因为文本流是一种通用接口。*

1984 年，这套哲学变成了文献。**Brian Kernighan** 和 **Rob Pike** 的《UNIX 编程环境》(*The UNIX Programming Environment*) 把它明白无误地描述了出来——Unix 之所以有效，“在于它的编程方式，一种使用计算机的哲学……系统的力量更多来自程序之间的关系，而不是程序本身”——并把 `cat` 举为“把一件通用的事做好”的原型工具，同时指出更新一些的系统 4.2BSD 和 System V 正是不停往上堆选项的那一类。

十年之后，1994 年，这个名字彻底定了下来：**Peter Salus** 在《A Quarter Century of Unix》（Unix 四分之一世纪）中把“Unix 哲学”一词归功于 **McIlroy**，而到了第二年，**Mike Gancarz** 的《The UNIX Philosophy》（Unix 哲学）把它浓缩成九条主要信条——“小即是美”、“把数据存成扁平文本文件”、“让每个程序都成为过滤器 (filter)”。

然后在 2003–2004 年，**Eric S. Raymond** 的《Unix 编程艺术》(*The Art of Unix Programming*) 给了我这套哲学最常回望的形式——“保持简单，愚蠢” (Keep It Simple, Stupid)——以及十七条法则，从模块化法则 (Rule of Modularity，即“写由干净接口连接的简单部件”) 到可扩展性法则 (Rule of Extensibility，即“为未来而设计，因为它会比你想象的更早到来”)。但比法则更重要的是，他点明了此前一直隐含的东西：这套哲学是自下而上 (bottom-up) 而非自上而下的；务实 (pragmatic) 且扎根于经验；它不在官方标准里，而在那种“隐性的、半反射式的知识，即 Unix 文化所传递的专业素养”里。

AT&T 让 Unix 保持专有 (proprietary)，设计却还是逃了出来：Linux 从头重新实现了那套接口，GNU 提供了工具和许可证，而到世纪之交，Unix 画下的那套架构已经自由了——以一种它的代码从未有过的自由。比它活得更久的，正是这一点——形态，而不是源码。

## 哲学 (Philosophy)

把日期剥掉，反复出现的还是那一小撮思想——这些年里，它们从我在纸上读到的规则，变成了我的习惯。

- **只做一件事，并做好它 (Do one thing well)。** 这条法则后来被社群缩写成 DOTADIW：小程序各自只做一件差事，胜过一个什么都做的大程序。宁可从头构建，也不要给旧工具硬加功能。这条是我违背最多、也最后悔的一条。
- **组合 (Compose)。** 预期每个程序的输出都会成为另一个程序的输入。文本流是通用接口——用 **Raymond** 的话说，对 Unix 工具而言，它就像对象世界里的消息对对象 (object) 那样。
- **简单胜过聪明 (Simplicity over cleverness)。** 清晰压倒机巧；只在必须之处增加复杂度。还是 **McIlroy**：“错综复杂又优美的复杂性”这个说法，几乎是个矛盾的修辞 (oxymoron)。
- **把策略与机制分开 (Separate policy from mechanism)。** 让接口 (interface) 与引擎 (engine) 彼此独立，这样两者可以按各自的节奏变化。
- **先原型，再打磨 (Prototype, then polish)。** 先让它跑起来，再去优化——**Knuth** 的“过早优化是万恶之源” (premature optimization is the root of all evil)，或 **Thompson** 更直接的说法：“拿不准时，就用蛮力” (when in doubt, use brute force)。
- **该报错就大声报错，其余时候保持沉默 (Fail loudly; stay silent otherwise)。** 程序没有出人意料的话要说时，就该什么都不说；必须失败时，它就应当吵闹地、尽快地失败。
- **数据重于代码 (Data over code)。** 把知识折叠进数据里，这样程序逻辑就可以很笨，却很健壮。

**Rob Pike** 在《Notes on C Programming》(C 编程笔记) 里加上了自己的规则，结尾是那条著名的非规则：“规则 6：没有规则 6。”而 **Richard Gabriel** 给了这套哲学最令人不安的推论——*更差即更好* (worse is better)——即接口与实现的简单性比正确性、一致性或完整性更重要。

## 另一面 (The other side)

没有哪套哲学是不付代价的，这一套也招来了实实在在的批评。

**Don Norman** 在 1981 年《Datamation》上那篇题为《关于 Unix 的真相：界面糟透了》(“The truth about Unix: the user interface is horrid”) 的文章里主张，这套哲学对最终用户的认知模型 (cognitive model) 漠不关心，使得灾难性的错误变得轻易可犯。这是关于友善的抱怨，而不是关于诚实的抱怨——而 Unix 从未承诺过友善。更近一些，游戏开发者 **Jonathan Blow** 说这套哲学已经过时，把它的链式工具比作微服务 (microservices)——那种缺少全局统筹就会变得低效的架构。

而这套文化也会自我纠察。**McIlroy** 看着现代 Linux 抱怨说：“爱慕者们把 Linux 喂成了一副令人沮丧的肥胖状态”——直接违背了 **Raymond** 的简约法则 (Rule of Parsimony)，那条法则说：只有在别无他法时才写大程序。这套哲学不是一份定了案的教义；它是 Unix 社群不断与自己进行的争论。

## 为什么是艺术 (Why art)

**Raymond** 称之为*艺术*而不是*方法*。**Kernighan** 和 **Pike** 在 1984 年给出了理由：“那套哲学无法用一句话写下来。”能写下来的是风格——一种造物的方式——而风格是学来的，不是规定出来的。这套哲学生活在工具本身里：让两个程序合而为一的管道 (pipe)、读入一条文本流再写出另一条流的过滤器、把一件事做好并且只做一件的小命令。

Unix 的艺术性和一件好工具一样：美不在任何单个零件里，而在零件如何契合。正如 **Kernighan** 和 **Pike** 所说：“许多 UNIX 程序单独看来做的事相当琐碎，但与其他程序组合起来，就成了通用而有用的工具。”这就是全部想法——也是为什么同一套哲学在半多个世纪之后，仍然到处冒头，从 shell 一直到现代 agent 那套由小而可组合的技能 (skill) 组成的工具箱。

## 纪念 Ritchie (Remembering Ritchie)

**Dennis Ritchie** 于 2011 年 10 月 12 日在新泽西州伯克利海茨 (Berkeley Heights) 的家中去世，享年 70 岁。一周之前，**Steve Jobs** 去世——世界为 **Jobs** 停摆，而 **Ritchie** 的死讯几乎没有走出行业媒体。这种不对称值得坐下来想一想。

**Jobs** 卖的是未来；**Ritchie** 造的是未来赖以奔跑的地基。**Ritchie 共同创造了 Unix，并创造了 C 语言**——Unix、Linux、macOS 和 Windows 的内核 (kernel) 与核心 (core) 都是用这门语言写的，它也是 C++、Objective-C、Java 和 C# 的祖先。正如 **Brian Kernighan** 所说：“**Dennis** 造出的工具——以及它们的直系后代——几乎运行着今天的一切。”计算机史学家 **Paul Ceruzzi** 说得更好：“如果你有一台显微镜，能看进一台计算机内部，你会在每一处看到他的工作。”

说 **Ritchie** 的影响更深，并不是对 **Jobs** 的不敬。一个造的是我们随身携带的产品；另一个造的是其他一切赖以搭建的那一层。**Ritchie** 去世时，Fedora 16 和 FreeBSD 9.0 都献给了他的记忆，还有一颗小行星 (asteroid) 以他命名。讣告是安静的。工作不是。

我们记得他。

## 好玩与痛苦 (For fun and for pain)

终端里的两段记忆——一段为乐，一段为痛。

第一段是纯粹的力量。我曾在自己个人的 Linux 机器上对 `/dev/sda1` 执行 `dd`，把根分区 (root partition) 抹得一干二净。系统连眼睛都没眨：它还活着，活在内存里，仿佛什么都没发生——但底下已经什么都不剩了。我断电的那一刻，它就没了。一条命令，彻底而即时，没有撤销。这就是终端：它照你说的做。

第二段是舒适感反过来咬我。我飞到美国为 IBM 的软件实验室做事，顶着时差，讲完一场之后我想关掉自己的笔记本——就是我做演示用的那台——于是在终端里敲了 `sudo shutdown -h now`。终端黑了；我的机器没有。那一刻我明白了：我敲命令的那个终端不是我的——它是实验室的 DNS 服务器，为大约 200 台服务器上的 6,000 台虚拟机 (virtual machine) 解析名字。那个会话是我早些时候为一场演示打开的——Terminator 里的一个 SSH 窗口——而我至今想不起那场演示为什么需要一台 DNS 服务器。更糟的是，那台服务器由一位聪明——有时也懒——的工程师管着，他打了补丁却没重启，所以它没能干净地起来。凌晨五点我打电话给管理员——我的错误，她的清晨——到十点它又能解析名字了，正好赶在当天的负载涌进来之前。

两个故事是同一个教训的两个方向：终端照字面理解你。想法和后果之间没有任何东西挡着，这就是它为什么这么快，也是它为什么会伤人。而我爱在终端里工作，问题恰恰就在这里：它们看起来全都一样——一块黑屏，一个绿色光标在闪——有那么一秒钟，你忘了自己在跟哪台机器说话。

## Unix 塑造了我 (What Unix made me)

我从没打算采纳一套哲学。我只是想用一台计算机，而 Unix 的做事方式一点点沉淀进我身上，直到它不再是一件工具，而是一种气质。

- **极简是一种价值，不是偏好。** 我是个极简主义者，我讨厌臃肿软件 (bloatware)；我选 Arch 正是为了它的最小化安装，而不是无视它。终端几乎从零开始，只随你添的东西生长。
- **哲学就是美学。** “只做一件事并把它做好”不只是工程法则——它也是美学法则。一条管道链就是一次小小的构成，诚实的部件组合成比任何一个都更伟大的东西。这就是我称它为艺术的原因。
- **透明胜过黑箱 (black box)。** 图形界面 (GUI) 坏了，我就茫然无措；终端坏了，我可以读错误信息并修好它。机器不再是黑箱——文件、进程、管道、权限，都是看出来的，而不是点出来的。
- **可组合、能长久的作品。** 图形界面的工作流活在肌肉记忆里，随你的耐心一起消亡；终端的工作流活在一个文件里，能存续下去。从 2000 年起，我的笔记就一直放在一个纯文本 (plain text) 的地方，可以从命令行取回。
- **自由，在设计之中 (Free, in the design)。** Unix 的源码有主，它的灵魂没有。你的数据是文本，你的工具是文件，你的工作流是一个脚本，整台机器可以用你叫得出名字的零件重建。没有把你的作品扣为人质的格式，没有只向主人敞开的城堡大门。自由的灵魂，而不是免费的下载。
- **诚实，而且把过程摊开给你看 (Honest, and it shows its work)。** 系统照你说的做，事后你还能读到它究竟做了什么：结果可以一路追到某个文件、某个脚本、你敲下的某一行。你建什么就得到什么，也拥有它——包括你刚刚抹掉的那块磁盘。没有和善的中间层，没有躲在暗处把你的意思重新解释一遍的隐藏代理 (agent)。当它出乎你意料时，那意外是你自己的；机器从不撒谎，它只是照字面理解了你。
- **稳定胜过新奇。** 我今天敲的一条命令，在 1975 年的系统上也能用；计算中最可靠的接口，也正是最老的那个。我被那种小而设计精良、比闪亮之物活得更久的东西吸引。
- **手艺胜过名声。** 最深的一条线——我敬重造物者，甚于产品制造者：安静的地基，甚于明亮的外表。
- **习惯胜过抢救。** 安全变成了一种习惯，而不是一次性的修补——小而健壮、可组合的防线，做一次，就一直守着。
- **如鱼得水。** 当我碰到 Unix 或 Linux 终端时，我感觉像鱼在水里——不是我在用的工具，而是我游动其中的水。

将近三十年，从 AIX 到 Arch，归根到底就是这一句：Unix 教给我的不只是怎么用计算机；它给了我一种思考方式——极简、透明、自由、诚实、可组合、长久、手艺优先——然后让我看见，那种方式就是艺术。这个故事的部分内容我之前讲过，在 [`260811-terminal-is-an-art.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260811-terminal-is-an-art.md) 和 [`260828-happy-birthday-linux-from-aix-to-arch.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260828-happy-birthday-linux-from-aix-to-arch.md) 里。`btw, i use arch` 不是一句玩笑；它是用四个词说完的整个论证。

## 来源 (Sources)

- Dennis M. Ritchie、Ken Thompson，〈The UNIX Time-Sharing System〉，《Communications of the ACM》17 (7)，1974 年 7 月——<https://cs.nyu.edu/~mwalfish/classes/ut/f09-cs395t/ref/ritchie74.pdf>
- M. D. McIlroy、E. N. Pinson、B. A. Tague，〈Unix Time-Sharing System: Foreword〉，《The Bell System Technical Journal》57 (6)，1978 年 7–8 月，第 1902–1903 页
- Donald A. Norman，〈The truth about Unix: the user interface is horrid〉，《Datamation》27 (12)，1981 年
- Brian W. Kernighan、Rob Pike，《The UNIX Programming Environment》，Prentice-Hall，1984 年——<https://www.cs.princeton.edu/~bwk/upe/upe.html>
- Rob Pike、Brian W. Kernighan，〈Program Design in the UNIX Environment〉，《AT&T Bell Laboratories Technical Journal》63 (8)，1984 年 10 月
- Rob Pike，〈Notes on Programming in C〉，1989 年
- Richard P. Gabriel，〈Lisp: Good News, Bad News, How to Win Big〉，1991 年
- Peter H. Salus，《A Quarter Century of Unix》，Addison-Wesley，1994 年
- Mike Gancarz，《The UNIX Philosophy》，Digital Press，1995 年
- Eric S. Raymond，《The Art of Unix Programming》第 1.6 章〈Basics of the Unix Philosophy〉——<http://www.catb.org/esr/writings/taoup/html/ch01s06.html>
- Jonathan Blow，访谈，《On the Metal》播客
- 维基百科，《Unix 哲学》(*Unix philosophy*)——<https://en.wikipedia.org/wiki/Unix_philosophy>
- 维基百科，《Dennis Ritchie》——<https://en.wikipedia.org/wiki/Dennis_Ritchie>

btw, i use arch
