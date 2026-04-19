# FOCUS — Project Knowledge Map

> **Role**: When you know what project you're in, load the right knowledge.
> **Mechanism**: Keyword → Domain → Knowledge file.

---

## How FOCUS Works

```
User says something
    ↓
Keyword matches a domain?
    ↓ YES → Load that domain's core knowledge
    ↓ NO  → Use general knowledge
```

This happens automatically at the start of every session.

---

## Your Project Domains

> Add your domains below. Each domain links keywords to a knowledge file.

### Example: Software Development

```yaml
domain: software_dev
keywords: [code, develop, debug, deploy, API, framework, git, test, refactor, react, vue, node, python]
knowledge_file: domains/software_dev.md
```

### Example: Creative Writing

```yaml
domain: creative_writing
keywords: [story, plot, character, narrative, dialogue, worldbuilding, novel, chapter, scene]
knowledge_file: domains/creative_writing.md
```

### Example: Data Science

```yaml
domain: data_science
keywords: [data, analysis, model, ML, pipeline, visualization, statistics, pandas, sklearn, tensor]
knowledge_file: domains/data_science.md
```

---

## Adding a New Domain

1. Copy `domains/_TEMPLATE.md` → `domains/your_domain.md`
2. Fill in your project knowledge
3. Add the domain definition above with the keywords that trigger it

---

## Domain Knowledge File Format

Each domain file in `domains/` should have:

```yaml
## Core Knowledge
- Project type:
- Tech stack / tools:
- Key conventions:

## Key Preferences
- How the human likes things done:
- What to always do:
- What to never do:

## Important Context
- Current state of the project:
- Known blockers:
- What's being worked on right now:
```

---

## Loading Priority

If multiple domains match, load them in this order:
1. Domain mentioned most recently in CONTEXT.md
2. Domain with most keywords in current input
3. Domain added most recently to FOCUS

---

## When No Domain Matches

If no keyword triggers a domain, the AI operates with general knowledge.
Do not force a domain match. Default to THINK methods if analysis is needed.

---

_Load what's relevant. Ignore what isn't._
