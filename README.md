# MindKit

> **Give your AI a working brain — not a database, not a plugin, just better thinking.**

[![CI](https://github.com/RingLingo/mindkit/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/RingLingo/mindkit/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Last Commit](https://img.shields.io/github/last-commit/RingLingo/mindkit/main.svg)](https://github.com/RingLingo/mindkit/commits/main)

**MindKit** is a zero-dependency cognitive engineering framework for AI agents. It gives any LLM structured attention, repeatable patterns, experience indexing, and safety guardrails — using only Markdown files you control.

Think of it as **upgrading your AI's RAM**: instead of starting every conversation from scratch, your AI remembers what matters, thinks when you ask it to, and never surprises you with destructive actions.

---

## The Problem

Most AI conversations start with the same frustration:

> *"I told you about this project last week."*
> *"You keep forgetting my preferences."*
> *"Why did you delete that file without asking?"*

The root cause: **AI has no persistent context layer**. Every session starts at zero.

**Existing solutions** require databases, APIs, or cloud services. That's overhead you don't need.

**MindKit** solves this with plain Markdown files. No dependencies. No backend. Just better AI.

---

## What MindKit Gives You

| Module | What It Does | Trigger |
|--------|-------------|---------|
| 🎯 **Focus Engine** | Activates relevant project knowledge when you mention keywords | Say "React" → loads your React knowledge |
| ⚡ **Intuition Rules** | Repeats become reflexes — 3 uses → automatic response | Repeated patterns trigger without prompting |
| 📋 **Episodic Buffer** | Indexes what happened each day, recent events weighted higher | "What did we do on Thursday?" |
| 🛡️ **Safety Guardrails** | Blocks destructive operations, always asks confirmation | Delete / overwrite / external send |
| 🔧 **Thinking Tools** | 16 structured methods: First Principles, Feynman Test, Reverse Thinking, etc. | "Use first principles on this" |

---

## Quick Start

### One-line summary

Copy `brain/` into your project → tell your AI to read `ACTIVATE.md` → done.

### Step 1: Copy `brain/` to your project

| AI Tool | Where to put `brain/` | How to activate |
|---------|----------------------|-----------------|
| **Claude Code** | `.claude/brain/` | Add `Read .claude/brain/ACTIVATE.md first` to `CLAUDE.md` |
| **Cursor** | `.cursor/brain/` | Reference in `.cursor/rules/mindkit.mdc` |
| **WorkBuddy** | `.workbuddy/brain/` | Use the skill trigger |
| **Any LLM** | Anywhere | Tell it: "Read brain/ACTIVATE.md first" |

### Step 2: Add your domain

```bash
# Option A: Use the generator (after pip install)
pip install -r tools/requirements.txt
python tools/domain_generator.py --name "my_project" --keywords "react,api,backend"

# Option B: Manual
cp brain/domains/_TEMPLATE.md brain/domains/my_project.md
# Edit my_project.md with your project knowledge
# Add domain definition to brain/FOCUS.md
```

### Step 3: Start talking

> "Here's my React project, it uses Next.js and Prisma."

AI automatically loads your domain knowledge. No extra prompting needed.

---

## Single-File Version (No File Access)

If you're using ChatGPT, Gemini, or any LLM without a file system:

1. Open [`mindkit-single.md`](mindkit-single.md)
2. Copy its content into your AI's "Custom Instructions" or "System Prompt"
3. Done — the framework works from text alone

---

## Architecture

```
brain/
├── ACTIVATE.md       ⭐ Entry point — AI reads this first
├── FOCUS.md          🎯 Attention engine + domain definitions
├── EPISODES.md       📋 Daily experience index (recency-weighted)
├── INTUITION.md      ⚡ Pattern→reflex rules (use-count reinforced)
├── THINKKIT.md       🔧 16 structured thinking methods
├── META.md           🛡️ Safety guardrails (hard rules)
└── domains/          📦 Your project knowledge
    ├── _TEMPLATE.md
    └── example_*.md
```

**Loading strategy**: `ACTIVATE.md` (~500 tokens) is the only required read. Everything else loads on demand.

---

## Compatibility

| LLM / Tool | Works? | Best for |
|-----------|--------|---------|
| Claude Code | ✅ | Native file access, best implicit context |
| Cursor | ✅ | Rule-based activation |
| WorkBuddy | ✅ | Skill-triggered activation |
| GPT-4 / o1 / o3 | ✅ | Via mindkit-single.md |
| Gemini | ✅ | Via mindkit-single.md |
| Qwen | ✅ | Structured Chinese prompts |
| DeepSeek | ✅ | Brief structured formats |
| Any LLM API | ✅ | Paste framework into system prompt |

---

## Advanced Tools

```bash
pip install -r tools/requirements.txt

# Validate your brain/ configuration
python tools/validator.py

# Generate a new domain from template
python tools/domain_generator.py --name "Marketing" --keywords "campaign,analytics"

# Sync personal ↔ OSS version
python tools/sync_manager.py --personal /path/to/project --direction pull
```

---

## Contributing

We welcome contributions! See [docs/contributing.md](docs/contributing.md).

Areas where we need help:
- 🌍 Translations (中文, 日本語, ...)
- 📦 New domain templates
- 🔧 Tool improvements
- 📊 Real-world use cases

---

## License

MIT — use it however you want.

---

*MindKit: Because "think about it" works better when you have tools for thinking.*
