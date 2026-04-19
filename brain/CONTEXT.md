# CONTEXT — The Living Project Memory

> This file is the AI's primary working memory.
> Both human and AI can write here. This is the project diary.
> It is not a prompt library. It is a record of decisions and state.

---

## What This File Is

CONTEXT is a shared, structured notepad between human and AI.
When you return after days or weeks, you should be able to read this and know:
- What the project is
- What was decided last time
- What is currently open
- What the AI already knows about the project

**This file is AI-writable.** The AI should update this when:
- A significant decision is made
- Direction changes
- A feature is completed
- A blocker is identified
- User preferences are clarified

---

## Update Protocol

### When to Write
Write when something is worth remembering next session:

```
✅ Write when:
- A decision was made
- Direction changed
- Feature completed or started
- Blocker found or resolved
- User said "always do X this way"

❌ Do NOT write when:
- Casual conversation
- One-off questions
- Things that won't matter next week
```

### How to Update
When the AI makes a significant decision:

```markdown
## [YYYY-MM-DD] Session Update

**Status**: [What is the current project state]

**Decisions Made**:
- [Decision 1]
- [Decision 2]

**Completed**:
- [What was finished]

**Open Issues**:
- [What needs to be done next]
- [What is blocking progress]

**Current Focus**: [What is being worked on right now]
```

---

## How to Read (Startup)

At the start of every session:
1. Read this file
2. Find the most recent entry
3. Load that state into working context
4. Ask: "What should I focus on today?"

---

## Project Baseline

Fill in once, then maintain:

```markdown
## Project Baseline

**Project Name**: [Name]
**Type**: [Web app / research / writing / data analysis / ...]
**Started**: [YYYY-MM-DD]
**Last Active**: [YYYY-MM-DD]

**What It Does**: [One sentence]

**Tech Stack / Tools**:
- [List key technologies]

**User Preferences**:
- [Key conventions, style, tools]

**Known Blockers**:
- [Current blockers]

**Next Action**:
- [Immediate next step]
```

---

## Session Log

<!-- Newest entry first. Keep last 7-10 entries. Archive older ones. -->

---

## Archive

<!-- Move completed/old entries below this line. Keep for history. -->

