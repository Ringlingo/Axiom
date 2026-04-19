# Axiom Quick Start — 3 Steps to a Reliable AI

## Step 1: Install the Brain

Copy `brain/` into your project. Where depends on your AI tool:

### Claude Code
```bash
cp -r brain/ /path/to/project/.claude/brain/
```
Add to `CLAUDE.md`:
```
Read .claude/brain/ACTIVATE.md first at the start of every conversation.
```

### Cursor
```bash
cp -r brain/ /path/to/project/.cursor/brain/
```
Create `.cursor/rules/axiom.mdc`:
```markdown
---
description: Axiom cognitive layer
globs:
alwaysApply: true
---
Read .cursor/brain/ACTIVATE.md first at the start of every conversation.
```

### Any LLM (ChatGPT, Gemini, etc.)
Copy the content of `axiom-single.md` into your AI's "Custom Instructions".

## Step 2: Add Your Domain

1. Copy `brain/domains/_TEMPLATE.md` → `brain/domains/your_project.md`
2. Fill in your project knowledge
3. Add to `brain/FOCUS.md`:
```yaml
domain: my_project
keywords: [your, keywords, here]
knowledge_file: domains/my_project.md
```

## Step 3: Start

That's it. Three steps. Five minutes.

Start a conversation:
> "This is my project. It uses [describe briefly]."

The AI loads your domain knowledge. Axiom's five laws are always active.

---

## Advanced Tools

```bash
pip install -r tools/requirements.txt

python tools/domain_generator.py --name "My Project" --keywords "react,typescript"
python tools/validator.py
```
