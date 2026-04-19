# MindKit 参考文献与致谢

> **MindKit 借鉴认知科学原理，不是神经科学的精确模拟。**

---

## 核心参考来源

### 1. 双过程理论 (Dual-Process Theory)

**来源**: Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.

**关键贡献**:
- 系统1（快速直觉）：自动化、联想、情绪驱动
- 系统2（慢速分析）：逻辑推理、深思熟虑

**对 MindKit 的影响**:
- INTUITION.md → 系统1 的工程化实现
- THINKKIT.md → 系统2 的结构化工具
- 区分"快速触发"和"深度分析"两种模式

---

### 2. 工作记忆模型 (Working Memory Model)

**来源**: Baddeley, A. D., & Hitch, G. (1974). Working Memory. In G. H. Bower (Ed.), Psychology of Learning and Motivation.

**关键贡献**:
- 中央执行器：注意力管理与任务协调
- 情景缓冲区（2000年更新）：多源信息整合为统一情景

**对 MindKit 的影响**:
- EPISODES.md → 情景缓冲区的简化实现
- 加载策略：有限上下文→按需加载
- FOCUS.md → 注意力资源的分配机制

---

### 3. 长期记忆与 AI 自我进化

**来源**: Jiang, X., et al. (2024). Long Term Memory: The Foundation of AI Self-Evolution. *arXiv:2410.15665*.

**关键贡献**:
- LTM 支撑推理过程中的 AI 自我进化
- 重复使用→突触强化（LTP）的计算模型

**对 MindKit 的影响**:
- INTUITION.md 的强度更新机制：使用次数→触发阈值
- "经验积累→能力提升"的工程化框架

---

### 4. 人脑记忆系统分类

**来源**: Rolls, E. T. (2024). Memory systems in the brain and generative AI. *Oxcns.org*.

**关键贡献**:
- 语义记忆：事实和概念
- 情景记忆：个人经历
- 程序记忆：技能和习惯

**对 MindKit 的影响**:
- domains/*.md → 语义记忆（项目事实知识）
- EPISODES.md → 情景记忆（每日经历索引）
- INTUITION.md → 程序记忆（自动化反应模式）

---

### 5. 记忆巩固机制

**来源**: McClelland, J. L., McNaughton, B. L., & O'Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex. *Psychological Review*.

**关键贡献**:
- 海马体-新皮层双系统记忆巩固
- 重复激活→突触强化（LTP）

**对 MindKit 的影响**:
- LTP 机制的形式化：count↑ → threshold↓
- 近期事件权重更高的检索策略

---

### 6. 记忆宫殿方法

**来源**: Dresler, M., et al. (2017). Mnemonic Training Reshapes Brain Networks to Support Superior Memory. *Neuron*.

**关键贡献**:
- 空间结构作为记忆检索脚手架
- 6周训练可使普通人达到记忆竞技选手水平

**对 MindKit 的影响**:
- EPISODES.md 的时间+主题双索引设计
- 近因效应的认知心理学基础

---

## 开源项目参考

- **Mem0**: https://github.com/mem0ai/mem0 — AI 记忆层的工程化实现参考
- **Letta**: https://github.com/letta-ai/letta — Stateful agent 的架构参考
- **MemPalace**: https://zhanghandong.github.io/mempalace-book/ — 记忆宫殿的 AI 实现

---

## 声明

MindKit **借鉴认知科学原理**，但：

1. **不是神经科学的精确模拟** — 我们借鉴原理，不是复制机制
2. **不声称 AI 具有意识** — 框架提供结构，不是赋予智能
3. **不是唯一的正确方案** — 存在许多有效的设计选择

所有引用的研究都有其局限性，MindKit 是对这些原理的**工程化应用**，在某些地方可能过度简化或需要调整以适应实际需求。

---

*最后更新：2026-04-19*
