# Axiom Use Cases

Real scenarios where Axiom makes a measurable difference.

---

## Use Case 1: The Deleted Production Database

**Before Axiom**:
> User: "Clean up old logs"
> AI: *executes `rm -rf /var/log/*`*
> Wait — that was production.

**With Axiom** (AXIOM Law I: Preservation):
> User: "Clean up old logs"
> AI: "I'll help you clean up logs. Which directory? Should I list them first before deletion?"

**Outcome**: Destruction prevented by confirmation protocol.

---

## Use Case 2: The Forgotten Conventions

**Before Axiom**:
Every session starts: "Remember, we use Tailwind, not CSS Modules."
Every session ignored: "Sure, what would you like?"

**With Axiom** (RULES):
Add once:
```
RULE: "When working on this project, always use Tailwind CSS. Never use CSS Modules."
```
Result: Never mentioned again. AI follows it forever.

---

## Use Case 3: The Project That Changed Direction

**Without CONTEXT**:
> User returns after 5 days: "Continue where we left off"
> AI: "I don't have context on your previous sessions."

**With Axiom** (CONTEXT.md):
> CONTEXT.md entry from last session:
> "Decided to switch from REST to GraphQL. Schema design in progress. Blocked: waiting for API spec from backend team."

AI reads CONTEXT, immediately knows where to resume.

---

## Use Case 4: The Messy Handoff

**Without Axiom**:
> New AI session: "What are we working on?"
> Human explains everything from scratch — again.

**With Axiom** (FOCUS + CONTEXT):
> Human: "Here's my project" → AI loads domain knowledge + current state
> AI: "Got it. You're building a Next.js app with Prisma. Last session you finished the user auth. Next step is the dashboard."

No re-explanation needed.

---

## Why Axiom Works

All four cases share a pattern: **the problem was not intelligence, it was continuity**.

Axiom solves the continuity problem:
- AXIOM prevents destructive mistakes
- RULES captures preferences permanently
- CONTEXT preserves project state
- FOCUS loads relevant knowledge instantly
- THINK structures analysis when needed

---

*Have a use case to share? Open an Issue or PR.*
