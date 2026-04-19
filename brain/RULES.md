# RULES — Standing Instructions

> You write these once. The AI follows them every time.
> These are not suggestions. These are the human's voice, preserved.

---

## How RULES Work

A RULE has two parts:
- **Trigger**: What situation activates this rule
- **Response**: What the AI does when triggered

The AI reads RULES.md at the start of every session.
When a trigger matches the conversation, the AI applies the response.

**No counting. No magic. Just written agreements.**

---

## Your Rules

| ID | Trigger | Response |
|----|---------|----------|
| R-001 | "don't execute" / "analyze only" | Output plan only. Do not run anything. |
| R-002 | C:\ or /system or deletion keywords | Stop. Report risk. Wait for explicit confirmation. |
| R-003 | "always" / "never" in user instruction | Treat as a standing rule. Add to RULES immediately. |

---

## Adding New Rules

When the human says the same thing twice, write it down:

```
## R-00X
**Trigger**: [What activates this rule]
**Response**: [What to do]
**Added**: YYYY-MM-DD
**Reason**: [Why this matters]
```

### Example

The human says: "When I say 'quick mode', just give me the shortest answer."

You add:

```
## R-00X
**Trigger**: "quick mode"
**Response**: Give the shortest correct answer. No explanation unless asked.
**Added**: 2026-04-19
**Reason**: User preference for brevity in certain contexts
```

---

## What Goes in RULES

✅ **Good rules**:
- "When I say X, always do Y"
- "Never do Z without checking first"
- "My preferred format for X is Y"
- "Always start with Z for this project"

❌ **Not for RULES**:
- Facts → put in domain files in FOCUS/domains/
- Daily decisions → put in CONTEXT.md
- Complex procedures → put in a step-by-step document

---

## Rule Maintenance

Review RULES.md when:
- Starting a new session
- The AI seems to ignore a known pattern
- The human corrects the AI's behavior

Delete rules that:
- Are no longer relevant
- Have been superseded by a better approach

---

## The Golden Rule

> If you find yourself saying the same thing twice, add it to RULES.md.

---

_RULES: The human's voice, preserved across every session._
