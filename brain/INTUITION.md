# ⚡ MindKit — Pattern Rules

> **Role**: Your standing instructions — patterns you define once, AI follows every time.
> **How it works**: You write rules. AI reads them as standing instructions. No magic.

---

## How Pattern Rules Work

You define a trigger (keyword or phrase) and a response (what the AI should do).
When the trigger appears in conversation, the AI follows the rule automatically.

```
You write in INTUITION.md:
  "don't execute" → AI outputs plan only, no execution

Result in conversation:
  You say "don't execute yet" → AI gives you the plan, waits
```

**No count tracking. No automatic strengthening. Just written rules that work.**

---

## Your Pattern Rules

| ID | Trigger | AI Response |
|----|---------|-------------|
| INT-001 | "don't execute yet" / "analyze only" | Switch to analysis mode, output plan only |
| INT-002 | C: drive / deletion / high-risk ops | Scan → Report risk → Wait for confirmation |

---

## Adding New Rules

Add to this file when you find yourself repeating the same instruction:

```yaml
- id: INT-00X
  trigger: "your trigger phrase or keyword"
  response: "what the AI should do when triggered"
  added: YYYY-MM-DD
```

**Rule of thumb**: If you've said it twice, write it down as a rule.

---

## What Belongs Here

✅ **Good rules**:
- "When the user says 'X', always do Y"
- "Never do Z without explicit confirmation"
- "My preferred format for X is Y"

❌ **Don't put here**:
- Facts or knowledge → put in `domains/your_domain.md`
- Daily events → put in `EPISODES.md`
- Complex procedures → put in a thinking tool in THINKKIT.md

---

## Strength (Optional)

If you want to track how often a rule is triggered, add a manual count.
This is optional — the rule works whether or not you track it.

```yaml
- id: INT-00X
  trigger: "..."
  response: "..."
  count: 3   # manually track if you want
```

---

_Pattern rules: say it once, have it forever._
