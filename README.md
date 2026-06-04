# Michelle's PM Operating System

A workflow-oriented prompt bank and Claude Code workspace for product management.

**Owner:** Michelle Yip, BA-to-PM transition, PSD Singapore

**Product:** OTEP (One Talent Engagement Platform) — internal talent marketplace for the Singapore Public Service

**Programme:** 12 sprints, 4 May – 16 Oct 2026 (Feature Freeze Sprint 8 · Go-Live 16 Oct)

---

## Folders

Seven numbered folders cover the full PM lifecycle. Each works as a standalone prompt bank.

| Folder | What's in it |
|---|---|
| [00-hub/](00-hub/) | Daily ops — sprint status, tasks, open items, risks, outputs |
| [01-discovery/](01-discovery/) | Discovery cycle — research, synthesis, frameworks |
| [02-prd/](02-prd/) | PRD writing — auth + opportunities PRDs, MVP release plan |
| [03-stories/](03-stories/) | Story management — story files, story-id-map, Jira scripts |
| [04-ceremonies/](04-ceremonies/) | Sprint ceremonies — prep, rhythm, allocation, meeting archive |
| [05-prototypes/](05-prototypes/) | Feature ideation + UI brief handoff |
| [06-skills-and-decisions/](06-skills-and-decisions/) | Decisions log, skills library (Dean + Pawel), OTEP context, stakeholder profiles |

Plus [inbox.md](inbox.md) (single capture point), [GOALS.md](GOALS.md), and [.claude/](.claude/) (commands, agents, skills).

---

## Keep these three current

Everything else follows from these. If they're stale, every command output is wrong.

1. **[00-hub/sprint-status.md](00-hub/sprint-status.md)** — sprint goal, stories, dates. Update each sprint start.
2. **[00-hub/tasks-active.md](00-hub/tasks-active.md)** — in progress / blocked / waiting. Update daily.
3. **[06-skills-and-decisions/decisions-log.md](06-skills-and-decisions/decisions-log.md)** — every decision, with date, rationale, owner.

---

## Daily rhythm

- **Morning** — capture into [inbox.md](inbox.md), run `/triage`, then `/daily-plan` (the PM-OS skill; pulls calendar + live Jira)
- **After meetings** — dump notes into [inbox.md](inbox.md), tag D/A/Q/I
- **Evening** — update [tasks-active.md](00-hub/tasks-active.md), run `/endday`
- **Sprint boundary** — update [sprint-status.md](00-hub/sprint-status.md), archive outputs, refresh [risks.md](00-hub/risks.md)

---

## Commands & skills

Full descriptions: [00-hub/commands-reference.md](00-hub/commands-reference.md)

| Type | Items |
|---|---|
| Daily | `/daily-plan` (PM-OS) · `/midday` · `/endday` · `/triage` |
| Ceremony prep | `/groom-prep` · `/groom` · `/sprint-plan-prep` · `/mid-sprint-review` · `/retro-prep` |
| Strategic | `/week` · `/brief` · `/decision` · `/retro` · `/scan` · `/archive` |
| Skills | `weekly-update` · `meeting-prep` · `draft-prd-section` · `synthesize-research` · `standup` |
| Agents | `pm-reviewer` · `scope-guardian` · `anti-ai-editor` · `decision-auditor` |

---

## Current state

| Project | Status |
|---|---|
| OTEP MVP (Auth + Opportunities) | Sprint 2 — active |
| OTG Ops | Ongoing BAU |
| BA-to-PM Conversion | Evidence gathering |
