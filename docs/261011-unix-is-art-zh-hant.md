# Unix 是藝術 (Unix Is Art)

> 簡體版：[Unix 是藝術 (Unix Is Art)](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261011-unix-is-art-zh-hans.md)

**原文：** [261011-unix-is-art.md](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261011-unix-is-art.md)

Unix 哲學不是一份規格說明 (specification)。沒有哪個委員會批准過它，也沒有任何標準定義過它——POSIX 標準化的是呼叫 (call)，不是品味。它是一套文化慣例 (cultural norms)——軟體設計上的民間傳統 (folk tradition)——圍繞貝爾實驗室 (Bell Labs) 的一個作業系統生長起來，又比那個系統活得更久。**Eric S. Raymond** 寫這件事的書甚至就叫《Unix 程式設計藝術》(*The Art of Unix Programming*)，而“藝術”這個詞正是關鍵：這套哲學像手藝 (craft) 一樣，靠範例和習慣傳承，就像一間工坊教人如何造物。這就是它的故事——從 1960 年代末到 2004 年乃至更晚——以及把這一切串起來的思想。

![資訊圖：Unix 是藝術——核心論點、1969 至 2004 年的時間線、原則、另一面、紀念 Dennis Ritchie，以及 Unix 如何塑造了我](../imgs/261011-unix-is-art.png)

## 歷史 (History)

它始於一種約束。1969–70 年，在貝爾實驗室 (Bell Labs)，**Ken Thompson** 與 **Dennis Ritchie** 在一臺配有慢速列印終端 (printing terminal) 的小機器上構建了一個作業系統——機器的限制成了它的風格。正如 **Raymond** 所說，這套哲學“起源於 **Ken Thompson** 早期的思考：如何用一個乾淨的服務介面 (service interface) 設計出小巧卻夠用的作業系統”。小不是偏好，而是預算。

**Ritchie** 和 **Thompson** 把設計考量寫進了 1974 年發表於《ACM 通訊》(*Communications of the ACM*) 的論文《The UNIX Time-Sharing System》（UNIX 分時系統），讀起來像一條誕生於匱乏的信條：讓程式易於編寫、測試和執行；用互動式使用 (interactive use) 取代批處理 (batch processing)；*因為*體積限制而追求經濟與優雅 (economy and elegance)——借用一句現成的話，“在苦難中得救” (salvation through suffering)；並讓系統自給自足 (self-supporting)，所有 Unix 軟體都在 Unix 下維護。

到 1978 年，這種風格有了代言人。**Doug McIlroy**——發明 Unix 管道 (pipe) 的人——只是把周圍人早已在做的事記了下來，寫在他為《貝爾系統技術期刊》(*Bell System Technical Journal*) Unix 專號所寫的序言裡：讓每個程式只把一件事做好，寧可從頭構建，也不要給舊工具硬加功能；預期每個程式的輸出都會成為另一個尚不可知的程式的輸入。讓軟體儘早被試用，最好在幾周之內，並且毫不遲疑地扔掉那些笨拙的部分；寧可用工具，也不用不熟練的幫手，哪怕工具得你自己造。後來他把這整套東西壓縮成一句我重複了三十年的話：*寫只做一件事並把它做好的程式；寫能協同工作的程式；寫處理文本流的程式，因為文本流是一種通用介面。*

1984 年，這套哲學變成了文獻。**Brian Kernighan** 和 **Rob Pike** 的《UNIX 程式設計環境》(*The UNIX Programming Environment*) 把它明白無誤地描述了出來——Unix 之所以有效，“在於它的程式設計方式，一種使用計算機的哲學……系統的力量更多來自程式之間的關係，而不是程式本身”——並把 `cat` 舉為“把一件通用的事做好”的原型工具，同時指出更新一些的系統 4.2BSD 和 System V 正是不停往上堆選項的那一類。

十年之後，1994 年，這個名字徹底定了下來：**Peter Salus** 在《A Quarter Century of Unix》（Unix 四分之一世紀）中把“Unix 哲學”一詞歸功於 **McIlroy**，而到了第二年，**Mike Gancarz** 的《The UNIX Philosophy》（Unix 哲學）把它濃縮成九條主要信條——“小即是美”、“把資料存成扁平文本檔案”、“讓每個程式都成為過濾器 (filter)”。

然後在 2003–2004 年，**Eric S. Raymond** 的《Unix 程式設計藝術》(*The Art of Unix Programming*) 給了我這套哲學最常回望的形式——“保持簡單，愚蠢” (Keep It Simple, Stupid)——以及十七條法則，從模組化法則 (Rule of Modularity，即“寫由乾淨介面連接的簡單部件”) 到可擴充性法則 (Rule of Extensibility，即“為未來而設計，因為它會比你想像的更早到來”)。但比法則更重要的是，他點明瞭此前一直隱含的東西：這套哲學是自下而上 (bottom-up) 而非自上而下的；務實 (pragmatic) 且紮根於經驗；它不在官方標準裡，而在那種“隱性的、半反射式的知識，即 Unix 文化所傳遞的專業素養”裡。

AT&T 讓 Unix 保持專有 (proprietary)，設計卻還是逃了出來：Linux 從頭重新實現了那套介面，GNU 提供了工具和許可證，而到世紀之交，Unix 畫下的那套架構已經自由了——以一種它的程式碼從未有過的自由。比它活得更久的，正是這一點——形態，而不是原始碼。

## 哲學 (Philosophy)

把日期剝掉，反覆出現的還是那一小撮思想——這些年裡，它們從我在紙上讀到的規則，變成了我的習慣。

- **只做一件事，並做好它 (Do one thing well)。** 這條法則後來被社群縮寫成 DOTADIW：小程式各自只做一件差事，勝過一個什麼都做的大程式。寧可從頭構建，也不要給舊工具硬加功能。這條是我違背最多、也最後悔的一條。
- **組合 (Compose)。** 預期每個程式的輸出都會成為另一個程式的輸入。文本流是通用介面——用 **Raymond** 的話說，對 Unix 工具而言，它就像物件世界裡的訊息對物件 (object) 那樣。
- **簡單勝過聰明 (Simplicity over cleverness)。** 清晰壓倒機巧；只在必須之處增加複雜度。還是 **McIlroy**：“錯綜複雜又優美的複雜性”這個說法，幾乎是個矛盾的修辭 (oxymoron)。
- **把策略與機制分開 (Separate policy from mechanism)。** 讓介面 (interface) 與引擎 (engine) 彼此獨立，這樣兩者可以按各自的節奏變化。
- **先原型，再打磨 (Prototype, then polish)。** 先讓它跑起來，再去最佳化——**Knuth** 的“過早最佳化是萬惡之源” (premature optimization is the root of all evil)，或 **Thompson** 更直接的說法：“拿不準時，就用蠻力” (when in doubt, use brute force)。
- **該報錯就大聲報錯，其餘時候保持沉默 (Fail loudly; stay silent otherwise)。** 程式沒有出人意料的話要說時，就該什麼都不說；必須失敗時，它就應當吵鬧地、儘快地失敗。
- **資料重於程式碼 (Data over code)。** 把知識摺疊進資料裡，這樣程式邏輯就可以很笨，卻很健壯。

**Rob Pike** 在《Notes on C Programming》(C 程式設計筆記) 裡加上了自己的規則，結尾是那條著名的非規則：“規則 6：沒有規則 6。”而 **Richard Gabriel** 給了這套哲學最令人不安的推論——*更差即更好* (worse is better)——即介面與實作的簡單性比正確性、一致性或完整性更重要。

## 另一面 (The other side)

沒有哪套哲學是不付代價的，這一套也招來了實實在在的批評。

**Don Norman** 在 1981 年《Datamation》上那篇題為《關於 Unix 的真相：介面糟透了》(“The truth about Unix: the user interface is horrid”) 的文章裡主張，這套哲學對終端使用者的認知模型 (cognitive model) 漠不關心，使得災難性的錯誤變得輕易可犯。這是關於友善的抱怨，而不是關於誠實的抱怨——而 Unix 從未承諾過友善。更近一些，遊戲開發者 **Jonathan Blow** 說這套哲學已經過時，把它的鏈式工具比作微服務 (microservices)——那種缺少全域性統籌就會變得低效的架構。

而這套文化也會自我糾察。**McIlroy** 看著現代 Linux 抱怨說：“愛慕者們把 Linux 喂成了一副令人沮喪的肥胖狀態”——直接違背了 **Raymond** 的簡約法則 (Rule of Parsimony)，那條法則說：只有在別無他法時才寫大程式。這套哲學不是一份定了案的教義；它是 Unix 社群不斷與自己進行的爭論。

## 為什麼是藝術 (Why art)

**Raymond** 稱之為*藝術*而不是*方法*。**Kernighan** 和 **Pike** 在 1984 年給出了理由：“那套哲學無法用一句話寫下來。”能寫下來的是風格——一種造物的方式——而風格是學來的，不是規定出來的。這套哲學生活在工具本身裡：讓兩個程式合而為一的管道 (pipe)、讀入一條文本流再寫出另一條流的過濾器、把一件事做好並且只做一件的小命令。

Unix 的藝術性和一件好工具一樣：美不在任何單個零件裡，而在零件如何契合。正如 **Kernighan** 和 **Pike** 所說：“許多 UNIX 程式單獨看來做的事相當瑣碎，但與其他程式組合起來，就成了通用而有用的工具。”這就是全部想法——也是為什麼同一套哲學在半多個世紀之後，仍然到處冒頭，從 shell 一直到現代 agent 那套由小而可組合的技能 (skill) 組成的工具箱。

## 紀念 Ritchie (Remembering Ritchie)

**Dennis Ritchie** 於 2011 年 10 月 12 日在紐澤西州伯克利海茨 (Berkeley Heights) 的家中去世，享年 70 歲。一週之前，**Steve Jobs** 去世——世界為 **Jobs** 停擺，而 **Ritchie** 的死訊幾乎沒有走出行業媒體。這種不對稱值得坐下來想一想。

**Jobs** 賣的是未來；**Ritchie** 造的是未來賴以奔跑的地基。**Ritchie 共同創造了 Unix，並創造了 C 語言**——Unix、Linux、macOS 和 Windows 的核心 (kernel) 與核心 (core) 都是用這門語言寫的，它也是 C++、Objective-C、Java 和 C# 的祖先。正如 **Brian Kernighan** 所說：“**Dennis** 造出的工具——以及它們的直系後代——幾乎執行著今天的一切。”計算機史學家 **Paul Ceruzzi** 說得更好：“如果你有一臺顯微鏡，能看進一臺計算機內部，你會在每一處看到他的工作。”

說 **Ritchie** 的影響更深，並不是對 **Jobs** 的不敬。一個造的是我們隨身攜帶的產品；另一個造的是其他一切賴以搭建的那一層。**Ritchie** 去世時，Fedora 16 和 FreeBSD 9.0 都獻給了他的記憶，還有一顆小行星 (asteroid) 以他命名。訃告是安靜的。工作不是。

我們記得他。

## 好玩與痛苦 (For fun and for pain)

終端裡的兩段記憶——一段為樂，一段為痛。

第一段是純粹的力量。我曾在自己個人的 Linux 機器上對 `/dev/sda1` 執行 `dd`，把根分割槽 (root partition) 抹得一乾二淨。系統連眼睛都沒眨：它還活著，活在記憶體裡，彷彿什麼都沒發生——但底下已經什麼都不剩了。我斷電的那一刻，它就沒了。一條命令，徹底而即時，沒有撤銷。這就是終端：它照你說的做。

第二段是舒適感反過來咬我。我飛到美國為 IBM 的軟體實驗室做事，頂著時差，講完一場之後我想關掉自己的筆記本——就是我做演示用的那臺——於是在終端裡敲了 `sudo shutdown -h now`。終端黑了；我的機器沒有。那一刻我明白了：我敲命令的那個終端不是我的——它是實驗室的 DNS 伺服器，為大約 200 臺伺服器上的 6,000 臺虛擬機器 (virtual machine) 解析名字。那個會話是我早些時候為一場演示開啟的——Terminator 裡的一個 SSH 視窗——而我至今想不起那場演示為什麼需要一臺 DNS 伺服器。更糟的是，那臺伺服器由一位聰明——有時也懶——的工程師管著，他打了補丁卻沒重啟，所以它沒能乾淨地起來。凌晨五點我打電話給管理員——我的錯誤，她的清晨——到十點它又能解析名字了，正好趕在當天的負載湧進來之前。

兩個故事是同一個教訓的兩個方向：終端照字面理解你。想法和後果之間沒有任何東西擋著，這就是它為什麼這麼快，也是它為什麼會傷人。而我愛在終端裡工作，問題恰恰就在這裡：它們看起來全都一樣——一塊黑屏，一個綠色游標在閃——有那麼一秒鐘，你忘了自己在跟哪臺機器說話。

## Unix 塑造了我 (What Unix made me)

我從沒打算採納一套哲學。我只是想用一臺計算機，而 Unix 的做事方式一點點沉澱進我身上，直到它不再是一件工具，而是一種氣質。

- **極簡是一種價值，不是偏好。** 我是個極簡主義者，我討厭臃腫軟體 (bloatware)；我選 Arch 正是為了它的最小化安裝，而不是無視它。終端幾乎從零開始，只隨你添的東西生長。
- **哲學就是美學。** “只做一件事並把它做好”不只是工程法則——它也是美學法則。一條管道鏈就是一次小小的構成，誠實的部件組合成比任何一個都更偉大的東西。這就是我稱它為藝術的原因。
- **透明勝過黑箱 (black box)。** 圖形介面 (GUI) 壞了，我就茫然無措；終端壞了，我可以讀錯誤資訊並修好它。機器不再是黑箱——檔案、程序、管道、許可權，都是看出來的，而不是點出來的。
- **可組合、能長久的作品。** 圖形介面的工作流活在肌肉記憶裡，隨你的耐心一起消亡；終端的工作流活在一個檔案裡，能存續下去。從 2000 年起，我的筆記就一直放在一個純文本 (plain text) 的地方，可以從命令列取回。
- **自由，在設計之中 (Free, in the design)。** Unix 的原始碼有主，它的靈魂沒有。你的資料是文本，你的工具是檔案，你的工作流是一個指令碼，整臺機器可以用你叫得出名字的零件重建。沒有把你的作品扣為人質的格式，沒有只向主人敞開的城堡大門。自由的靈魂，而不是免費的下載。
- **誠實，而且把過程攤開給你看 (Honest, and it shows its work)。** 系統照你說的做，事後你還能讀到它究竟做了什麼：結果可以一路追到某個檔案、某個指令碼、你敲下的某一行。你建什麼就得到什麼，也擁有它——包括你剛剛抹掉的那塊磁碟。沒有和善的中間層，沒有躲在暗處把你的意思重新解釋一遍的隱藏代理 (agent)。當它出乎你意料時，那意外是你自己的；機器從不撒謊，它只是照字面理解了你。
- **穩定勝過新奇。** 我今天敲的一條命令，在 1975 年的系統上也能用；計算中最可靠的介面，也正是最老的那個。我被那種小而設計精良、比閃亮之物活得更久的東西吸引。
- **手藝勝過名聲。** 最深的一條線——我敬重造物者，甚於產品製造者：安靜的地基，甚於明亮的外表。
- **習慣勝過搶救。** 安全變成了一種習慣，而不是一次性的修補——小而健壯、可組合的防線，做一次，就一直守著。
- **如魚得水。** 當我碰到 Unix 或 Linux 終端時，我感覺像魚在水裡——不是我在用的工具，而是我遊動其中的水。

將近三十年，從 AIX 到 Arch，歸根到底就是這一句：Unix 教給我的不只是怎麼用計算機；它給了我一種思考方式——極簡、透明、自由、誠實、可組合、長久、手藝優先——然後讓我看見，那種方式就是藝術。這個故事的部分內容我之前講過，在 [`260811-terminal-is-an-art.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260811-terminal-is-an-art.md) 和 [`260828-happy-birthday-linux-from-aix-to-arch.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/260828-happy-birthday-linux-from-aix-to-arch.md) 裡。`btw, i use arch` 不是一句玩笑；它是用四個詞說完的整個論證。

## 來源 (Sources)

- Dennis M. Ritchie、Ken Thompson，〈The UNIX Time-Sharing System〉，《Communications of the ACM》17 (7)，1974 年 7 月——<https://cs.nyu.edu/~mwalfish/classes/ut/f09-cs395t/ref/ritchie74.pdf>
- M. D. McIlroy、E. N. Pinson、B. A. Tague，〈Unix Time-Sharing System: Foreword〉，《The Bell System Technical Journal》57 (6)，1978 年 7–8 月，第 1902–1903 頁
- Donald A. Norman，〈The truth about Unix: the user interface is horrid〉，《Datamation》27 (12)，1981 年
- Brian W. Kernighan、Rob Pike，《The UNIX Programming Environment》，Prentice-Hall，1984 年——<https://www.cs.princeton.edu/~bwk/upe/upe.html>
- Rob Pike、Brian W. Kernighan，〈Program Design in the UNIX Environment〉，《AT&T Bell Laboratories Technical Journal》63 (8)，1984 年 10 月
- Rob Pike，〈Notes on Programming in C〉，1989 年
- Richard P. Gabriel，〈Lisp: Good News, Bad News, How to Win Big〉，1991 年
- Peter H. Salus，《A Quarter Century of Unix》，Addison-Wesley，1994 年
- Mike Gancarz，《The UNIX Philosophy》，Digital Press，1995 年
- Eric S. Raymond，《The Art of Unix Programming》第 1.6 章〈Basics of the Unix Philosophy〉——<http://www.catb.org/esr/writings/taoup/html/ch01s06.html>
- Jonathan Blow，訪談，《On the Metal》播客
- 維基百科，《Unix 哲學》(*Unix philosophy*)——<https://en.wikipedia.org/wiki/Unix_philosophy>
- 維基百科，《Dennis Ritchie》——<https://en.wikipedia.org/wiki/Dennis_Ritchie>

btw, i use arch
