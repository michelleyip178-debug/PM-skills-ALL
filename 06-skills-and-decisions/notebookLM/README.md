# NotebookLM Query Prompts

Ready-to-use prompts for querying your NotebookLM notebooks as a PM. Copy-paste any prompt, or say "query my notebook" followed by it.

## How to use

- **Slash commands** (`/groom`, `/week`, `/brief`, `/decision`, `/retro`, `/scan`) are pre-built workflows in `.claude/commands/`. Type them directly.
- **Ad-hoc prompts** (this folder) are for when you need something the slash commands don't cover. Paste the prompt or describe what you need.

## Prompt categories

| File | When to reach for it |
|---|---|
| [sprint-delivery.md](sprint-delivery.md) | Grooming readiness, sprint planning, mid-sprint checks, review prep |
| [scope-decisions.md](scope-decisions.md) | Scope calls, conflict checks, decision audits, assumption mapping, MVP/R1 triage |
| [stakeholder-comms.md](stakeholder-comms.md) | Exec updates, pre-meeting briefs, alignment checks, one-pagers |
| [document-health.md](document-health.md) | Health checks, gap finding, PRD-to-story consistency, spec reviews |
| [research-discovery.md](research-discovery.md) | Interview synthesis, pattern finding, competitive context, user needs mapping |
| [planning-priorities.md](planning-priorities.md) | Monday planning, Friday retro, prioritisation |

## Tips for better queries

- **Be specific about format.** "List as a table" or "group by pillar" or "max 200 words" gets you tighter output.
- **Name the audience.** "For Pow Hwee" vs "for Mark" changes the level of technical detail.
- **Ask for citations.** Add "cite which document" to any prompt so you can trace claims back to sources.
- **Chain queries.** Run `/scan` first to find gaps, then query specific gaps in detail.
- **Scope it down.** "Only look at Epic 4 stories" or "focus on Sprint 2 items" avoids noise from unrelated sources.
