# MindKit

> **给你的 AI 装上真正能工作的认知架构——不是数据库，不是插件，只是更好的思考方式。**

[![CI](https://github.com/RingLingo/mindkit/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/RingLingo/mindkit/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Last Commit](https://img.shields.io/github/last-commit/RingLingo/mindkit/main.svg)](https://github.com/RingLingo/mindkit/commits/main)

**MindKit** 是一个零依赖的认知工程框架，让任何 LLM 获得结构化注意力、可复用模式、共享日志和安全护栏——全部基于你控制的 Markdown 文件。

把它想象成**升级 AI 的行为规范**：不再每次重复同样的嘱咐，AI 会记住你定的规则、主动思考你要它思考的问题、绝不擅自执行危险操作。

---

## 解决什么问题

大多数 AI 对话都以同样的挫败感开始：

> *"上周我说过了，这个项目用 Tailwind，不是 CSS Modules。"*
> *"你又忘了我的偏好。"*
> *"为什么你没问就删了那个文件？"*

**MindKit** 用纯 Markdown 解决，不需要任何基础设施。

---

## 五大模块

| 模块 | 功能 | 触发方式 |
|------|------|---------|
| 🛡️ **安全护栏** | 删除/覆盖/外发 → 必须确认 | **不可绕过，始终生效** |
| 🎯 **注意力引擎** | 提到关键词 → 自动加载相关项目知识 | 说"React" → 加载 React 知识 |
| ⚡ **模式规则** | 你写一次 → AI 每次都遵守 | "我说 X 的时候，总是 Y" |
| 📋 **每日日志** | 你和 AI 共同维护的记录——决定了什么，待处理什么 | "上次我们做了什么？" |
| 🔧 **思维工具** | 16 种结构化方法：第一性原理、费曼检验、逆向思维等 | "用第一性原理分析" |

**不是记忆魔法。不是 AI 意识。只是更好用的结构化提示词。**

---

## 快速开始

### 第一步：复制 `brain/` 到你的项目

| AI 工具 | 存放位置 | 激活方式 |
|---------|---------|---------|
| **Claude Code** | `.claude/brain/` | 在 `CLAUDE.md` 添加：`Read .claude/brain/ACTIVATE.md first` |
| **Cursor** | `.cursor/brain/` | 在 `.cursor/rules/mindkit.mdc` 引用 |
| **WorkBuddy** | `.workbuddy/brain/` | 使用 Skill 触发 |
| **任何 LLM** | 任意位置 | 告诉它："先读 brain/ACTIVATE.md" |

### 第二步：添加你的域

```bash
pip install -r tools/requirements.txt
python tools/domain_generator.py --name "我的项目" --keywords "react,api,后端"
```

### 第三步：开始对话

> "这是我用 Next.js 和 Prisma 的项目。"

AI 自动加载你的项目知识，不需要额外提示。

---

## 单文件版（无文件访问）

使用 ChatGPT、Gemini 等不支持文件的 AI：

1. 打开 [`mindkit-single.md`](mindkit-single.md)
2. 复制全部内容到 AI 的"自定义指令"或"系统提示词"
3. 完成 — 框架从文本中直接生效

---

## 架构

```
brain/
├── ACTIVATE.md       ⭐ 入口 — AI 首先读取
├── FOCUS.md          🎯 关键词 → 域知识映射
├── INTUITION.md      ⚡ 你的标准指令（模式规则）
├── EPISODES.md       📋 共享每日日志（决定+待处理）
├── THINKKIT.md       🔧 16 种结构化思维方法
├── META.md           🛡️ 安全规则 — 始终生效，不可绕过
└── domains/          📦 你的项目知识
    ├── _TEMPLATE.md
    └── example_*.md
```

**加载策略**：`ACTIVATE.md`（约 500 tokens）是唯一必读文件。其他模块按需加载。

---

## 兼容性

| LLM / 工具 | 支持 | 最佳场景 |
|-----------|------|---------|
| Claude Code | ✅ | 原生文件访问 |
| Cursor | ✅ | 基于规则的激活 |
| WorkBuddy | ✅ | Skill 触发激活 |
| GPT-4 / o1 / o3 | ✅ | 通过 mindkit-single.md |
| Gemini | ✅ | 通过 mindkit-single.md |
| Qwen | ✅ | 结构化中文提示词 |
| DeepSeek | ✅ | 简洁结构化格式 |
| 任何 LLM API | ✅ | 粘贴到 system prompt |

---

## 进阶工具

```bash
pip install -r tools/requirements.txt

python tools/validator.py              # 验证 brain/ 配置
python tools/domain_generator.py --name "项目名" --keywords "react,api"
python tools/sync_manager.py --personal /path --direction pull
```

---

## 贡献

欢迎贡献！详见 [docs/contributing.md](docs/contributing.md)。

---

## 许可证

MIT — 随便用。

---

*MindKit：因为"想想看"在你有思考工具的时候效果更好。*
