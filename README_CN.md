# Axiom

> **让 AI 可靠的认知层。**

**Axiom** 是一个零依赖的 AI 认知层。它让 AI 对话可预测、安全、一致——全部基于你控制的 Markdown 文件。

把它想象成**给 AI 安装好判断力**：知道什么不能破坏、什么要记住、什么问题怎么思考、什么时候该问而不是猜。

---

## 五条定律

这不是建议。这是 Axiom 驱动的 AI 的存在法则。

| 定律 | 含义 |
|------|------|
| **一：保全** | 不经明确确认，绝不破坏任何东西 |
| **二：边界** | 不碰系统文件，未经授权不碰他人数据 |
| **三：真实** | 不撒谎、不隐藏不确定性、不编造 |
| **四：上下文** | 不遗忘项目知识和用户偏好 |
| **五：授权** | 外部行动需要明确批准 |

这五条定律，是"有能力的 AI"和"可信赖的 AI"之间的区别。

---

## 五大模块

| 模块 | 功能 |
|------|------|
| **AXIOM** | 五条不可违背的定律 — 始终生效 |
| **FOCUS** | 关键词触发知识加载 — 知道当前在哪个项目 |
| **CONTEXT** | AI 可写的项目日志 — 跨会话状态持久化 |
| **RULES** | 标准指令 — 你说一次，AI 永远遵守 |
| **THINK** | 20 种结构化思维方法 — 需要时调用 |

---

## 快速开始

### 第一步：复制 `brain/` 到你的项目

| AI 工具 | 位置 | 激活方式 |
|---------|------|---------|
| **Claude Code** | `.claude/brain/` | 加入 `CLAUDE.md` |
| **Cursor** | `.cursor/brain/` | 加入 `.cursor/rules/` |
| **WorkBuddy** | `.workbuddy/brain/` | Skill 触发 |
| **任何 LLM** | 任意位置 | 告诉它："先读 brain/ACTIVATE.md" |

### 第二步：填写你的项目知识

复制 `brain/domains/_TEMPLATE.md` → 你的域文件，然后加入 `FOCUS.md`。

### 第三步：开始对话

> "这是我的 React 项目，用 Next.js 和 Prisma。"

AI 自动加载你的项目知识。Axiom 五定律始终生效。

---

## 单文件版

ChatGPT、Gemini 等不支持文件的 AI：

1. 打开 `axiom-single.md`
2. 复制到 AI 的"自定义指令"
3. 完成

---

## 架构

```
brain/
├── ACTIVATE.md       ⭐ 入口 — 每次首先读取
├── AXIOM.md         ⚖️ 五条定律 — 始终生效，不可绕过
├── FOCUS.md         🎯 关键词 → 域知识映射
├── CONTEXT.md       📝 AI 可写项目日志（状态跨会话持久化）
├── RULES.md         📋 标准指令（你写，AI 遵守）
├── THINK.md         🧠 20 种思维方法（按需调用）
└── domains/         📦 你的项目知识
```

---

## 为什么需要 Axiom

大多数 AI 问题不是智能问题，是判断力问题：

> *"让它清理日志，它删了生产数据。"*
> *"它总是忘记我的项目规范。"*
> *"它没问就发了邮件。"*

**Axiom 解决判断力问题。** 五定律防止破坏。FOCUS 和 CONTEXT 提供连续性。RULES 捕获偏好。THINK 结构化推理。

---

## 工具

```bash
pip install -r tools/requirements.txt

python tools/validator.py              # 验证 brain/ 配置
python tools/domain_generator.py --name "项目名" --keywords "react,api"
python tools/sync_manager.py --personal /path --direction pull
```

---

## 许可证

MIT — 随便用。

---

*Axiom：让 AI 可靠的定律。*
