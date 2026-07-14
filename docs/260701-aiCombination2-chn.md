---
presentation:
  theme: black.css
  width: 960
  height: 700
  margin: 0.1
  minScale: 0.2
  maxScale: 1.5
  controls: true
  progress: true
  slideNumber: true
  history: false
  keyboard: true
  overview: true
  center: true
  touch: true
  loop: false
  rtl: false
  shuffle: false
  fragments: true
  embedded: false
  help: true
  showNotes: false
  autoSlide: 0
  autoSlideStoppable: true
  mouseWheel: false
  hideAddressBar: true
  previewLinks: false
  transition: 'default'
  transitionSpeed: 'default'
  backgroundTransition: 'default'
  viewDistance: 3
  parallaxBackgroundHorizontal: 200
  parallaxBackgroundVertical: 50
  enableSpeakerNotes: false
---

<!-- slide -->

# 优化AI使用：从豆包用户到高级用户

<!--
## 介绍
- IT专业人员AI使用演进概述。
- 日常AI集成用于文档和演示的挑战。
-->

<!-- slide -->

## 挑战
- **依赖**单一AI提供商，限制灵活性
- 多平台的高费用和订阅费用
- **快速消耗**使用 token
- 存在访问**封禁**风险
- 不断重复的需求，可以写成 SKILL.md

<!-- slide -->

## 解决方案：AI使用组合策略

<!-- slide -->

### OpenRouter.ai
- 使用**单一计费平台**简化支付。
- 按**实际使用量**付费，避免高额订阅。
- 访问**多个高质量免费AI模型**（例如Nvidia Nemotron）。
- You'd have to pay $10 for using free models, without being charged
- 限制：一些免费AI模型非常缓慢

<!-- slide -->

### OpenCode.ai
- Vendor <font color=orange>**unlocked**</font>! 不像 Claude, Google, etc
- **无缝管理和切换**100多个AI提供商。
- 高效的**命令行界面**快速切换。
- 限制：仅支持命令行

<!-- slide -->

### 提升效率的 AI Agent 
- **Hermes** ☤ 和 **OpenClaw** 🦞
  - 两个差不多
  - Hermes 社区更活跃
- 使用预定义技能（SKILL.md）自动化**多任务和复杂工作流**。
- 将**重复或来回的任务**委托给这些代理。

<!-- slide -->

## 使用AI代理的工作流程 Hermes ☤ 和 OpenClaw 🦞

1. 从一个**想法**开始，并将其写入一个**通用技能框架**。
2. 与AI协作，**润色和头脑风暴**你的技能框架，完善为**生产级SKILL.md**。特别强调 SKILL.md 的标准 (standard) 和规则 (compliance)
3. **安装**自定义技能到AI代理中。
4. 使用AI代理**触发并执行**自定义技能。
5. 案例 > 
  https://clawhub.ai/j3ffyang/skills/luo-shen-fu
  https://clawhub.ai/j3ffyang/skills/260620-silk-essay-chn


<!--

1. 想法生成
2. 技能框架草拟（编写通用SKILL.md）
3. AI协作与润色（头脑风暴与技能完善）
4. 技能安装（在AI代理中安装自定义技能）
5. 技能执行（触发并运行技能）
-->

<!-- slide -->

## SKILL.md

个人自定义SKILL.md 
- https://clawhub.ai/j3ffyang
- https://github.com/j3ffyang/ai-custom-skills

<!-- slide -->

## Benefits 

- 通过基于使用量的付费模式实现**成本效率**。
- **提升灵活性**，减少供应商锁定。
- 通过AI代理自动化实现**生产力提升**。
- **更好地控制**AI资源管理。
- Custom SKILL.md - 提高效率，减少 token usage，复用
- (bonus) Agent 如 OpenClaw 🦞 & Hermes ☤，都有 `self-improve` skill，自动记录重复的需求，如你每次问豆包

<!-- slide -->

## 结论
**结合多个平台和AI代理**，解决关键挑战，促进更有效的AI采用：

1. 简化为**单一付款**平台。
2. 实现多个提供商和AI模型的**灵活切换**。
3. 通过多样化AI来源降低**被封禁风险**。
4. 支持创建并执行**自定义AI技能**以自动化工作流。
