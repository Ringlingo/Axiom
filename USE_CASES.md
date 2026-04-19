# MindKit Use Cases

Real-world scenarios where MindKit makes a measurable difference.

---

## Use Case 1: Long-Term Software Project

**Who**: Solo developer or small team
**Tools**: Claude Code, Cursor, or any AI coding assistant
**Problem**: AI forgets project conventions after each session

### Before MindKit

Every session starts the same way:

```
You: "I'm working on my Next.js project, it uses Prisma and Tailwind."
AI: "Got it! What would you like help with?"
You: "Don't use CSS modules, use Tailwind. Don't touch schema.prisma directly."
[... 20 minutes later ...]
You: "I told you, Tailwind not CSS modules!"
```

### With MindKit

Once, add to `brain/domains/my_project.md`:

```yaml
## Core Conventions
- UI: Tailwind CSS (no CSS modules)
- ORM: Prisma (never edit schema.prisma directly, use migrations)
- API: tRPC endpoints in `src/server/routers/`
- State: React Query + Zustand

## Key Preferences
- Always run `pnpm lint` before commit
- Use TypeScript strict mode
- No console.log in production code
```

Now every session — even a week later:

```
You: "Add a user profile endpoint"
AI: "Got it. I'll create a tRPC router in src/server/routers/ using Prisma..."
[automatically follows Tailwind, TypeScript strict, lint-before-commit]
```

**Time saved per session**: ~5-10 minutes of repeated context-setting

---

## Use Case 2: Multi-Subject Research

**Who**: Researcher, student, or technical writer
**Tools**: Any LLM (ChatGPT, Gemini, Perplexity)
**Problem**: AI gives generic answers because it doesn't know your field

### Before MindKit

```
You: "Explain this paper's methodology"
AI: [Generic explanation based on training data]

You: "No, I'm working on CRISPR gene drives in Anopheles mosquitoes"
AI: "Ah, in that context... [still generic because context window is limited]
```

### With MindKit

Add to `brain/domains/research.md`:

```yaml
## Research Domain
- Field: Evolutionary biology / genetics
- Organism: Anopheles gambiae (malaria vector)
- Technology: CRISPR-Cas9, gene drives, HMEJ editing
- Key papers: Esvelt (2014), Hammond (2016), Kistler (2022)

## Methodology Preferences
- Statistical: R over Python for ecological models
- Sequencing: RNA-seq differential expression
- Citations: Always cite year + authors in first mention
```

**Result**: AI immediately contextualizes answers within your research domain.

---

## Use Case 3: Safety-Critical Operations

**Who**: Developer working with production systems
**Tools**: Any AI with terminal access
**Problem**: Accidental destructive operations (wrong server, wrong database)

### Before MindKit

```
You: "Clean up the old logs"
AI: "Sure, running: rm -rf /var/log/*"
[Wait, that was production]
```

### With MindKit

Add to `brain/domains/production.md`:

```yaml
## Safety Rules
- NEVER run rm -rf without listing files first
- ALWAYS confirm before: delete, truncate, DROP TABLE
- ALWAYS confirm before: curl POST/PUT to external URLs
- staging vs production: ALWAYS ask "which environment?"

## Known Pitfalls
- Production DB: 54.123.45.67:5432 (NEVER touch)
- Staging DB: staging-db.internal:5432
- Backup before any migration
```

Now MindKit's safety guardrails block destructive commands automatically.

---

## Use Case 4: Creative Writing (Novelist)

**Who**: Fiction writer using AI as a writing assistant
**Tools**: Claude, ChatGPT, Gemini
**Problem**: AI contradicts established worldbuilding details

### With MindKit

Add to `brain/domains/my_novel.md`:

```yaml
## World Rules (100% fictional)
- Magic system: Gene-tech based (CRISPR + nanotech), NOT traditional fantasy
- Technology level: Near-future (2035), biotech = wealth
- Economy: Energy Credits as currency

## Character: Lin (protagonist)
- Age: 28
- Background: Ex-gene surgeon turned fugitive
- Voice: Clinical, precise, hides emotions behind medical terminology

## Tone
- Show don't tell
- 3+ senses per scene
- No info dumps > 2 sentences
```

**Result**: AI maintains consistent worldbuilding across thousands of words and multiple sessions.

---

## Why These Work

All four use cases share a common pattern:

1. **One-time setup**: Add domain knowledge once
2. **Keyword-triggered**: No need to say "use my project knowledge"
3. **Session-persistent**: Works across days/weeks
4. **No infrastructure**: Plain Markdown, no database, no API

---

*Have a use case to share? Contributions welcome — open an Issue or PR!*
