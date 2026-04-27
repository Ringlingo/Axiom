# Axiom — AI Skill Integration Guide

> Load Axiom cognitive framework into any AI assistant that supports Skills, Custom Instructions, or Rules.

---

## Method 1: Claude Code CLAUDE.md Integration (Recommended)

Add this to your project's `CLAUDE.md`:

```markdown
# Axiom Cognitive Framework

Read .claude/brain/ACTIVATE.md first at every session start.
Follow its startup sequence to activate the framework.

Key protocols:
- Focus: Scan FOCUS.md for domain matches based on user keywords
- Episodes: Check EPISODES.md for recent experiences (recency weighted)
- Intuition: Check INTUITION.md for quick-response rules (LTP enhanced)
- Thinking: Load THINKKIT.md tools on demand (catalog first)
- Safety: Never auto-execute destructive operations (HR-001 to HR-005)
```

---

## Method 2: Cursor Rules

Create `.cursor/rules/axiom.mdc`:

```markdown
---
description: Axiom cognitive framework — read brain/ACTIVATE.md first
globs:
alwaysApply: true
---

Read .cursor/brain/ACTIVATE.md first at the start of every conversation.
This is your cognitive framework — follow its protocols.
```

---

## Method 3: Any LLM (Manual Paste)

1. Open `brain/ACTIVATE.md` and copy its full content
2. Paste into your AI's "Custom Instructions" or "System Prompt"
3. Optionally also paste `brain/FOCUS.md` content
4. The AI will follow the protocols from the text alone

---

## How It Works

```
CLAUDE.md / .mdc triggers
    ↓
AI reads ACTIVATE.md (~500 tokens)
    ↓
Startup sequence activates:
  1. Scan FOCUS.md → match user's topic to a domain
  2. Check EPISODES.md → recent experiences (recency weighted)
  3. If domain hit → load domain knowledge
  4. Check INTUITION.md → quick-response rules (LTP enhanced)
  5. Load THINKKIT.md tools → when analysis needed
    ↓
Full cognitive framework is active
```

---

_The integration is just a trigger. The architecture is in the files._
