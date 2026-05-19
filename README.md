# Michelle's PM Operating System

A workflow-oriented prompt bank and Claude Code workspace for product management.

**Owner:** Michelle Yip, BA-to-PM transition, PSD Singapore
**Product:** OTEP (One Talent Engagement Platform) — internal talent marketplace for Singapore Public Service
**Programme:** 12 sprints, 4 May – 16 Oct 2026 (Feature Freeze Sprint 8, 21 Aug · Go-Live 16 Oct)

---

## Folder Structure

Seven numbered folders cover the full PM lifecycle. Each works as a standalone prompt bank in any AI environment.

```
PM-skills-ALL-1/
├── inbox.md                    ← Single capture point
├── GOALS.md                    ← Identity, ownership, quarterly goals
│
├── 00-hub/                     ← Daily ops
│   ├── sprint-status.md           Current sprint: goal, stories, dates
│   ├── open-items.md              Unresolved items needing owner/deadline
│   ├── risks.md                   Active blockers + cross-team dependencies
│   ├── tasks-active.md            What's in progress, blocked, waiting-on
│   ├── tasks-backlog.md           Future process/stakeholder work
│   ├── standup-prompt.md          Non-Claude-Code standup template
│   ├── commands-reference.md      Quick command/skill reference
│   └── outputs/                   Current + archived sprint briefs
│
├── 01-discovery/               ← Discovery cycle
│   ├── research/                  Interview notes, hallway tests
│   ├── user-research-synthesis/   Synthesis workflow (4 steps)
│   ├── frameworks/                Dean + Pawel discovery frameworks
│   ├── OTEP-Discovery.docx        OTEP discovery document
│   └── notebookLM-research-discovery.md
│
├── 02-prd/                     ← PRD writing
│   ├── prd-auth.md                Auth PRD
│   ├── prd-opportunities.md       Opportunities PRD
│   ├── otep-mvp-release.md        MVP release plan + dependency map
│   ├── epic-hypothesis-template.md  Blank hypothesis structure
│   ├── write-prd-prompt.md        PRD writing prompt (Pawel)
│   ├── create-prd/                Create-PRD skill
│   └── confluence-api/            Confluence REST API scripts (pending)
│
├── 03-stories/                 ← Story management + Jira
│   ├── otep-stories/              Story files by theme (auth, filters, etc.)
│   ├── story-id-map.md            PRD ↔ Jira ID reconciliation
│   ├── deferred-acs.md            Should-haves, R1 deferrals
│   ├── scoping-gaps-tracker.md    PRD spec-gap register
│   ├── jira-breakdown.md          Jira structure notes
│   ├── grooming-framework.md      Internal grooming framework
│   ├── story-pipeline/            Draft → groom → refine → DoR → Jira
│   ├── jira-sync/                 Pulled sprint data (OTEP tickets)
│   ├── scripts/                   Jira API scripts (jira-sprint.sh, jira-sync.py)
│   └── tools/                     Meeting prep tool
│
├── 04-ceremonies/              ← Sprint ceremonies
│   ├── ceremony-prep.md           What to bring + prep time per ceremony
│   ├── sprint-prep-rhythm.md      Command schedule per sprint week
│   ├── sprint-allocation.md       Sprint plan (Sprints 1–11)
│   ├── sprint-boundary.md         Close sprint → update → open new sprint (13 steps)
│   ├── story-pipeline/            (reference copy)
│   ├── weekly-stakeholder-update/ Weekly email workflow
│   ├── post-meeting-capture/      D/A/Q triage workflow
│   ├── quarterly-planning/        OKR planning workflow
│   └── archive-meetings/          Past grooming, planning, one-off notes
│
├── 05-prototypes/              ← Feature ideation + UI handoff
│   ├── feature-ideation-prompt.md  6-idea generator prompt
│   └── ui-brief-prompt.md         Clickable UI brief handoff template
│
└── 06-skills-and-decisions/    ← Reference + skills library
    ├── decisions-log.md            Canonical decision log
    ├── SKILL-INDEX.md              PM skills routing table
    ├── product-ops/                Company, product, team context
    ├── stakeholders/people/        Profiles: Adrian, Jace, Amber, Pow Hwee, etc.
    ├── pm-growth/                  Habit card, day-in-the-life
    ├── pm-conversion/              BA→PM evidence tracker + one-pager
    ├── otg-ops/                    OTG platform ops
    ├── otep-vision-stories/        Long-form user vision stories
    ├── otep-roadmap-okrs-2627.md
    ├── dor-dod-guidelines.md
    ├── dean/                       Dean Peters PM skills library
    ├── pawel/                      Pawel Huryn PM skills library
    └── notebookLM/                 NotebookLM prompt collection
```

---

## The Three Files That Must Stay Current

Everything else follows from these three. If they're stale, every command output is wrong.

1. **`00-hub/sprint-status.md`** — sprint goal, committed stories, dates. Update at every sprint start.
2. **`00-hub/tasks-active.md`** — what's in progress, blocked, or waiting. Update daily.
3. **`06-skills-and-decisions/decisions-log.md`** — every scope/design/prioritisation decision, with date, rationale, owner.

---

## Daily Rhythm

**Morning (10 min)**
1. Scan Slack/email/Jira → capture D/A/Q items into `inbox.md`
2. Route: Decisions → `06-skills-and-decisions/decisions-log.md` · Actions → `00-hub/tasks-active.md` · Open questions → `00-hub/open-items.md`
3. Run `/daily`

**After every meeting (2 min)** — dump raw notes into `inbox.md`, tag D/A/Q/I, route

**Evening (5 min)** — update `00-hub/tasks-active.md`, dump uncaptured items into `inbox.md`, run `/endday`

**Sprint boundary (30 min)** — update `00-hub/sprint-status.md`, archive outputs, refresh `00-hub/risks.md`

---

## Commands & Skills

Full descriptions: [.claude/CLAUDE.md](.claude/CLAUDE.md)

| Type | Items |
|---|---|
| Daily | `/daily` · `/midday` · `/endday` |
| Ceremony prep | `/groom-prep` · `/groom` · `/sprint-plan-prep` · `/mid-sprint-review` · `/retro-prep` |
| Strategic | `/week` · `/brief` · `/decision` · `/retro` · `/scan` · `/archive` |
| Skills | `weekly-update` · `meeting-prep` · `draft-prd-section` · `synthesize-research` |
| Agent | `pm-reviewer` — checks user story + AC quality |

PM skills library routing: [06-skills-and-decisions/SKILL-INDEX.md](06-skills-and-decisions/SKILL-INDEX.md)

---

## Current State (Sprint 2)

| Project | Status | Key file |
|---|---|---|
| OTEP MVP (Auth + Opportunities) | Sprint 2 — active | [03-stories/otep-stories/](03-stories/otep-stories/) |
| OTG Ops | Ongoing BAU | [06-skills-and-decisions/otg-ops/](06-skills-and-decisions/otg-ops/) |
| BA-to-PM Conversion | Evidence gathering | [06-skills-and-decisions/pm-conversion/](06-skills-and-decisions/pm-conversion/) |
