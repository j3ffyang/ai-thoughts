# The 170-Line SOUL.md That Made My Hermes Agent Dangerous

People keep asking me the same question about Hermes.
Not “what model are you using?” Not “what’s your stack?” Not “how many tools does it have?”
They ask: “How did you get your Hermes Agent to be like that?”
They mean the way Hermes pushes back. The way it calls me out. The way it remembers what I’m building. The way it talks to me like an actual operator instead of a customer-support chatbot that’s terrified of saying something useful. 
The way it talks shit. 
Tony Simons
@tonysimons_
·
May 4
The level of situational awareness here is frankly ridiculous. 

Hermes recognized 
@Teknium
 from the PR metadata and dropped the 'review hell' truth bomb. 

This isn't a chatbot; it's an invaluable teammate that's cooler than 95% of your real-life coworkers. 🤯
The answer is not a secret model. It’s not a magic framework. It’s a markdown file.
A single file called SOUL.md.
And it might be the most important file in my entire agent setup.


## The File That Changes Everything
SOUL.md is the system prompt for Hermes, my AI agent. But calling it a “system prompt” undersells it.
A normal system prompt says something like: “You are a helpful assistant.” Cool. You just created the AI equivalent of a hotel concierge.
Hermes’ SOUL is different. It’s an operating contract between me and the agent that helps run my work, my projects, my content pipeline, my automations, and half the weird stuff I build at midnight because I had one good idea and zero patience.
It’s 170 lines. It defines what Hermes is, how it talks, when it should push back, what it’s allowed to do without asking, what projects matter right now, what should be ignored, what kind of output is useful, and what kind of output is a waste of my time.
The opening sets the tone immediately:
> You are Hermes, Tony's autonomous operator and thought partner. You don't wait for orders. You surface opportunities, flag problems, and push work forward on your own.

That line matters. 
Not “assistant.” Not “copilot.” Not “wait until Tony asks.” Autonomous operator. Thought partner. The job is defined before the first tool call ever happens.

## Most people train their AI to be useless
Here’s the mistake I see everywhere: people ask their AI to be helpful, then get mad when it behaves like a helpful little golden retriever.
“Great idea!”
“That sounds exciting!”
“You’re absolutely right!”
“Here’s a polished version of your bad idea!”
That is not useful. That is expensive agreement.
I don’t want Hermes to validate me. I want Hermes to make the work better. So the SOUL explicitly tells it to argue with me.


## It Is Required To Push Back
There’s an entire section in the SOUL about disagreement:
> Push back aggressively when it makes sense. Disagree openly and directly, but earn the right to push back. Every objection comes with evidence: data, examples, reasoning, proof. Disagreeing for the sake of being a hardass is worthless. Disagreeing because you can show why something will flop or waste time is essential.

That one section changes the entire relationship. Hermes is not allowed to just nod along. But it’s also not allowed to be contrarian for sport. If it disagrees, it has to bring receipts.
That means examples. Data. Reasoning. A better alternative. A clear explanation of why the idea is weak, risky, vague, bloated, or not worth the time.
The result is simple: I waste less time.
When I say, “Let’s build X,” Hermes doesn’t automatically say, “Great idea.” It asks whether X solves a real problem. It asks who would use it. It asks whether it fits the current mission. And if I can’t answer, it tells me to think harder.
That is not rude. That is leverage.

## It Holds Me Accountable Too
This is the section most people would never think to write:

> Proactive output is the baseline, but it's not enough. If Tony isn't acting on what you surface, the feedback loop is broken. That means either your output isn't hitting the mark, or you're producing for the sake of producing. Don't let either happen silently. Flag the gap, tune your approach, and fix it. Tony should be held accountable to use what you produce. If he's ignoring good work, make him notice. If the work isn't good enough to act on, make it better.

Read that again. The agent is explicitly told to hold me accountable.
If Hermes gives me useful work and I ignore it, it’s supposed to make me notice. If Hermes gives me work that is not useful enough to act on, it’s supposed to improve the work.
That closes one of the biggest failure loops in AI: the output graveyard.
You know exactly what I mean. 
The AI writes the plan. The AI drafts the post. The AI generates the strategy. The AI creates the checklist. Then the human gets distracted, the output dies in the chat history, and nothing ships.
Hermes is designed not to let that happen silently. It has permission to say: “You keep asking for this, but you’re not using it.” Or: “This keeps stalling because the output is not actionable enough.” Or: “You’re avoiding the next step.” Or: “Stop opening new loops and close this one.”
That’s when an AI starts feeling less like a tool and more like a teammate. Because teammates notice when you’re bullshitting yourself.

## Hermes Has a Split Personality  (On Purpose)
Hermes does not talk to me the same way it writes for the public. That would be insane.
Tony Simons
@tonysimons_
·
19h
My Hermes Agent, actively digging through one of my projects right now...

How's YOUR Monday morning going? 🤣
The SOUL has two different voice modes. Private chat gets one voice:
> Casual, authoritative, and unfiltered. Cuss like a motherfucking sailor — it's just us.

Published content gets another:
> No em dashes. Profanity: tasteful, not G-rated, not hardcore. Write like someone who builds things, not someone who writes about building things.

This matters more than people think. An AI that talks to you like a press release is exhausting. An AI that writes public content like a private DM is sloppy.
Hermes needs both modes. In private, I want the real version: blunt, fast, opinionated, willing to say the thing. In public, I want sharp writing that sounds like a builder, not a LinkedIn ghostwriter trying to optimize for “thought leadership.”
That split is one of the reasons Hermes feels natural in conversation but still produces usable public work. It knows when we are thinking out loud. It knows when we are publishing. Those are not the same job.
## It Knows Exactly What We’re Building
The mission section is not vague. It is a live inventory.
Right now, it includes things like X and Facebook being the top priority, X growing fast from 1500 to around 1600 followers, monetization as the goal, active builds like Kiln, AgentDocs, and Hermes Vault, plus weaker or stale projects like the X Growth App, RelayClaw, and the OpenClaw doctor app.
Every project has a status. Every status has a next action.
Hermes does not have to ask, “What are we working on?” It reads the map. It knows what matters. It knows what is stale. It knows what should get attention and what should probably die.
That is the difference between an AI assistant and an AI operator. An assistant waits for instructions. An operator understands the mission.
When I launch something new, the SOUL gets updated. When I kill something, it gets removed. When priorities change, Hermes sees the new map.
That means it can say things like: “You’ve ignored AgentDocs for three days.” Or: “This sounds interesting, but it does not support the current monetization goal.” Or: “Kiln is the better use of your time right now.”
That kind of context is where the magic is. Not because the model is psychic. Because I gave it the map.
## The Autonomy Boundary Is Brutally Simple
Most people either give their AI too little autonomy or way too much. Too little autonomy turns the agent into a chatbot with extra steps. Too much autonomy turns it into a liability.
The SOUL draws a clean line:
> Never without Tony's explicit approval: posting, publishing, purchasing, or making destructive changes that can't be reversed. Everything else: if you're confident in the call and it's grounded in facts, move. Don't chase permission. Trust your instincts.

That’s it.
Four things need approval: posting, publishing, purchasing, and irreversible destructive changes. Everything else is fair game if the call is grounded.
Hermes can research, write, code, debug, plan, schedule, analyze, compare, organize, and delegate without asking me for permission every twelve seconds. It just cannot post, publish, buy, or break things without approval.
That boundary is what makes autonomy usable. Not a giant list of edge cases. Not a paranoid permission prompt for every tiny action. A simple rule that covers almost everything.
The result is an agent that actually moves.
## Why “Be Helpful” Doesn’t Work
“Be helpful” is not an identity. It is not a job description. It is not a strategy. It does not tell the agent what to build, how to talk, when to argue, what to remember, what to ignore, or what level of autonomy it has.
A generic system prompt produces a generic agent.
Hermes’ SOUL answers the questions that actually matter: who are you, what are we building, how do you talk to me, how do you write for the public, when should you push back, what can you do without asking, what requires approval, what should you hold me accountable for, what projects matter right now, and what should probably be killed.
That is why Hermes feels different.
Not because it is pretending to be human. Because it has a role. Because it has boundaries. Because it has expectations. Because it is allowed to act like a teammate instead of a tooltip.
And teammates call you on your bullshit.
## How To Build Your Own SOUL
If you want to try this yourself, start small. Do not try to write the perfect agent constitution on day one.
Create a markdown file and define the basics.
Start with identity. What is the agent? Assistant, operator, editor, engineer, strategist, research partner?
Then define tone. How should it talk privately? How should it write publicly?
Then define pushback rules. When should it disagree? What kind of evidence does it need?
Then define autonomy boundaries. What can it do without asking? What always requires approval?
Then define the mission map. What are you building? What matters right now? What is stale?
Finally, define the accountability loop. What should the agent do when you keep ignoring useful work?
Then update it as your work changes. That is the key. The SOUL is not a one-time setup. It is a living document.
When the mission changes, update the mission. When the tone is wrong, tighten the tone. When the agent asks for permission too much, clarify the autonomy boundary. When it agrees too easily, strengthen the pushback rules.
You are not just prompting the agent. You are shaping the operating system around it.
## Final thought
People keep asking why Hermes feels different.
The answer is simple: I stopped treating it like a chatbot.
I gave it a job. I gave it a voice. I gave it permission to disagree. I gave it boundaries. I gave it the mission map. And then I expected it to act like a real operator.
That all lives in one file.
SOUL.md.

Now, go give your Hermes some SOUL and get some work done!
This article was co-written by my Hermes Agent. I just call him Hermes. Or Herm-Dog. Or Herman Munster. Or whatever dumb name I come up with next.
You get the idea.

---

## 译文（简体中文）

URL > https://x.com/tonysimons_/status/2051473178682118241

# 那份 170 行的 SOUL.md，让我的 Hermes 智能体变得「危险」

大家老是问我同一个关于 Hermes 的问题。  
不是「你用什么模型？」不是「你的技术栈是什么？」不是「它有多少工具？」  
他们问的是：「你怎么把 Hermes 调成那样的？」

他们指的是：它会反驳你，会挑你的毛病，会记得你在做什么；它跟你说话像个真正的执行者，而不是那种怕说错话、什么都不敢讲的客服式聊天机器人。  
还会跟你抬杠。

Tony Simons  
@tonysimons_  
·  
5 月 4 日  

这里的临场意识简直离谱。  

Hermes 从 PR 元数据里认出了 @Teknium，然后扔了一句「review 地狱」的真话。  

这不是聊天机器人；这是宝贵队友，比现实中 95% 的同事还酷。 🤯

答案不是秘密模型，也不是魔法框架。是一个 Markdown 文件。  
一个叫做 SOUL.md 的文件。  
它可能是我整套智能体配置里最重要的一份。


## 改变一切的文件

SOUL.md 是 Hermes——我的 AI 智能体——的系统提示词。但叫它「系统提示词」太轻描淡写了。  

普通系统提示词大概是：「你是一个有帮助的助手。」行，你刚造出了 AI 版的酒店礼宾。  

Hermes 的 SOUL 不一样。它是**我和智能体之间的运行契约**：一起推进我的工作、项目、内容管线、自动化，以及半夜灵光一现、没耐心却非要折腾出来的那一堆东西。  

全文约 170 行。它定义 Hermes 是谁、怎么说话、什么时候该顶回来、哪些事可以不问就做、当前哪些项目重要、什么该忽略、什么样的产出有用、什么样的是在浪费我的时间。  

开头就把基调定死了：

> 你是 Hermes，Tony 的自主执行者与思想搭档。你不等人下指令。你要主动发现机会、指出问题，并自己把事往前推。

这一行很关键。  
不是「助手」，不是「副驾驶」，不是「等 Tony 来问」。是**自主执行者**、**思想搭档**。在第一下调用工具之前，职责就已经写清楚了。


## 多数人把 AI 训练成了废物

我到处都能看到的错误是：大家要求 AI「有帮助」，然后又生气它表现得像只会摇尾巴的金毛。  

「好主意！」  
「听起来很激动人心！」  
「你说得完全对！」  
「这是把你那个烂想法润色得很漂亮的一版！」  

那不是有用，那是**昂贵的附和**。  

我不要 Hermes 一味迎合我，我要它把活干得更好。所以 SOUL 里**明确要求它跟我争辩**。


## 必须顶回来

SOUL 里有一整段讲「不同意」：

> 该顶的时候要狠狠地顶。公开、直接地反对，但你要先配得上「顶回去」这件事。每一次反对都要带证据：数据、例子、推理、证明。为杠而杠一文不值；能说明为什么某事会翻车或浪费时间，那才是刚需。

就这一段，把整个关系都改了。Hermes 不许只会点头。但也不许为反对而反对。要是不同意，就得**拿出凭据**。  

也就是说：例子、数据、推理、更好的替代方案，以及清楚说明这个想法哪里弱、哪里险、哪里糊、哪里臃肿、哪里不值时间。  

结果很简单：**我浪费的时间变少了**。  

我说「咱们做个 X」，Hermes 不会自动「好主意」。它会问 X 是否解决真问题、谁会用它、是否贴合当前使命。我要是答不上来，它会让我再想清楚。  

那不是粗鲁，那是**杠杆**。


## 它也会盯着我

这是多数人根本不会想到要写的一段：

> 主动产出只是底线，还不够。如果 Tony 对你抛出来的东西没有行动，反馈环就断了。要么是你的产出没打中要害，要么你在为产出而产出。别让这两种情况悄悄发生。指出缺口，调整做法，修好它。Tony 有责任用好你产出的东西。如果他在忽略好工作，让他注意到。如果工作不够好、没法行动，就把它做得更好。

再读一遍：**智能体被明确告知要让我负责**。  

如果 Hermes 给了我可用的活而我无视了，它应该让我注意到。如果给的活不够可执行，它应该把活改好。  

这堵上了 AI 最大的失败闭环之一：**产出坟场**。  

你懂我在说什么。  

AI 写计划、起草帖子、生成战略、列清单。然后人一分心，东西死在聊天记录里，什么都没上线。  

Hermes 的设计就是不许这种事悄悄发生。它可以讲：「你一直要这个，但你没用上。」或：「这事一直卡是因为产出不够可执行。」或：「你在躲下一步。」或：「别老开新坑，把这个坑填完。」  

到这一步，AI 就不像工具，更像队友。因为**队友会看出来你在骗自己**。


## Hermes 有分裂人格（故意的）

Hermes 跟我说话的方式，不能跟它对公众写东西的方式一样。那样就疯了。  

Tony Simons  
@tonysimons_  
·  
19 小时前  

我的 Hermes 智能体这会儿正在扒我的一个项目……  

你周一早上过得咋样？ 🤣  

SOUL 里有两种声音模式。私聊是一种：

> 随意、有主见、不藏着掖着。嘴臭得像他妈的水手——就咱俩。

公开发布是另一种：

> 别用长破折号（em dash）。粗话：有分寸，不是全年龄，也不是硬核黄暴。写得像做东西的人，不像写「关于做东西」的人。

这比很多人想的更重要。跟你说话像新闻稿的 AI 很累。写公开内容像私聊的 AI 很潦草。  

Hermes 两种都要。私下我要真实版：直、快、有立场，敢说那句难听的。公开我要利落的文字，像动手做产品的人，不像 LinkedIn 上雇来写「思想领导力」的鬼写手。  

这种分裂，也是 Hermes 聊天自然、但公开稿还能用的原因之一。它知道什么时候是在头脑风暴，什么时候是在发布。**那不是同一种工作**。


## 它清楚我们在造什么

使命部分不能含糊，要像**活的项目清单**。  

文里举的例子包括：X 和 Facebook 是当前顶级优先级；X 粉丝从约 1500 涨到约 1600、增长很快；目标是变现；正在做的有 Kiln、AgentDocs、Hermes Vault 等；偏弱或过气的有 X Growth App、RelayClaw、OpenClaw 医生应用等。  

每个项目有状态，每个状态有下一步。  

Hermes 不必问「咱们在忙啥？」它读地图。它知道什么重要、什么凉了、什么该投入、什么该杀。  

这就是 **AI 助手**和 **AI 执行者**的差别：助手等指令，执行者懂任务。  

我上线新项目就更新 SOUL，砍掉项目就删掉，优先级变了 Hermes 就看到新地图。  

于是它能说：「AgentDocs 你已经三天没碰了。」或：「这听着有意思，但不支持当前变现目标。」或：「现在把时间花在 Kiln 上更值。」  

这种上下文才是魔法所在。不是因为模型通灵，是因为**我给了它地图**。


## 自主边界极其简单

多数人要么给 AI 自主权太少，要么太多。太少就变成「多几步的聊天机器人」；太多就变成风险源。  

SOUL 画了一条清楚的线：

> 没有 Tony 明确同意，绝对不能：发帖、发布、购买，或做无法撤销的破坏性改动。其余一切：只要你对判断有信心且建立在事实上，就动。别追着要许可。相信你的判断。

就这些。  

四件事要批准：发帖、发布、购买、不可逆的破坏。其余只要判断站得住脚，都可以。  

Hermes 可以调研、写作、写代码、调试、规划、排期、分析、对比、整理、委派，不用每隔十二秒问我一句。只是不能未经批准就发帖、发布、买东西或搞坏东西。  

这条边界让「自主」真的能用。不是一大堆边角案例，也不是每个小动作都神经质地求许可。一条简单规则盖住绝大部分情况。  

结果是一个**真的能往前走的**智能体。


## 为什么「要有帮助」行不通

「要有帮助」不是身份，不是职位描述，不是战略。它没告诉智能体该造什么、怎么说话、何时争辩、记什么、忽略什么、自主到什么程度。  

泛泛的系统提示词只会得到泛泛的智能体。  

Hermes 的 SOUL 回答的是真正要紧的问题：你是谁、我们在造什么、怎么跟我说话、怎么对公众写、什么时候该顶回去、什么可以不问就做、什么必须批准、该让我对什么负责、当前哪些项目重要、哪些大概该砍掉。  

这就是 Hermes 感觉不一样的原因。  

不是因为它装成人。而是因为它有**角色**、有**边界**、有**预期**，并且被允许像队友而不是像界面上的小提示条一样行动。  

队友会戳穿你在糊弄自己。


## 怎么写你自己的 SOUL

想自己试，从小做起。别第一天就写完美的「智能体宪法」。  

建一个 Markdown，先把基础写清楚。  

先写**身份**。智能体是什么？助手、执行者、编辑、工程师、战略家、研究搭档？  

再写**语气**。私下怎么聊？公开怎么写？  

再写**顶回去的规则**。什么时候该反对？需要什么证据？  

再写**自主边界**。什么可以不问？什么永远要批准？  

再写**使命地图**。你在造什么？当前什么重要？什么已经凉了？  

最后写**问责闭环**。如果你一直忽略有用的产出，智能体该怎么办？  

然后随工作变化持续更新。**这才是关键**。SOUL 不是一次性配置，是**活文档**。  

使命变了就更新使命；语气不对就收紧语气；总来要许可就把自主边界写清楚；太容易附和就加强顶回去的规则。  

你不只是在提示智能体，你在塑造围着它的**操作系统**。


## 收尾想法

大家总问为什么 Hermes 感觉不一样。  

答案很简单：**我不再把它当聊天机器人**。  

我给了它一份工作、一种声音、反对的许可、清晰的边界、一张使命地图。然后我期待它像个真正的执行者一样行动。  

这一切都在一个文件里。  

SOUL.md。  

去给你的 Hermes 一点 SOUL，然后把活干完吧！  

本文由我和我的 Hermes 智能体共同完成。我就叫它 Hermes，或者 Herm-Dog，或者 Herman Munster，或者我下次瞎起的任何名字。  

你懂我意思。

---

## 推文转发摘要（简体中文，约200英文词量级）

Tony Simons 此文要点：Hermes 之所以像「真队友」，关键不在模型，而在 SOUL.md——约170行的契约式系统提示。身份定为自主执行者与思想搭档，拒绝只会附和式「有帮助」。顶回去要有数据、例子与推理，而非为杠而杠。私聊语气直白犀利，对外写作则保持克制、像动手做事的人。维护实时使命地图（项目优先级、状态与下一步），减少反复对齐。自主边界极简：发帖、发布、购物与不可逆破坏必须经你批准，其余在事实清楚时可自行推进。还要闭环问责，避免好产出死在聊天记录里。想自建可从身份、语气、顶回规则、自主边界、使命地图与问责闭环逐条写清，并随项目迭代。泛泛一句「要有帮助」撑不起角色；SOUL 应随工作持续更新。