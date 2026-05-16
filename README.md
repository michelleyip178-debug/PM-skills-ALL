# Michelle's PM Operating System

A Claude Code-native workspace for product management, built on BASB's CODE + PARA method.

**Owner:** Michelle Yip, BA-to-PM transition, PSD Singapore
**Product:** OTEP (One Talent Engagement Platform) — internal talent marketplace for Singapore Public Service
**Current:** Sprint 1 (4–15 May) — Auth + Data Infrastructure  ·  **Programme:** 12 sprints, 4 May – 16 Oct 2026 (Feature Freeze end of Sprint 8, 21 Aug · Go-Live 16 Oct)

---

## How It Works

Everything enters through `inbox.md`. Morning triage sorts items into PARA folders. Nothing stays in the inbox longer than 24 hours. Slash commands read `context/` files before producing any output — keeping context current is what makes the system accurate.

```
inbox.md  -->  projects/   (time-bound deliverables)
               areas/      (ongoing responsibilities)
               resources/  (reference material)
               archive/    (inactive items)
```

### What makes it useful

The system works when three things stay current:

1. **`context/current-sprint.md`** — every command reads this first. If it's stale, every output is wrong.
2. **`tasks/active.md`** — the daily driver. What's in progress, what's next, what's blocked.
3. **`context/decisions-log.md`** — single source of truth for all scope/design/prioritisation decisions.

Beyond those three, the operating rules — MVP scope guardrails, writing standards, the decisions protocol, how to work with Michelle — live in [.claude/CLAUDE.md](.claude/CLAUDE.md), which Claude loads every session.

---

## Folder Structure

```
PM-skills-ALL/
├── inbox.md                  <- Single capture point
├── changelog.md              <- Triage + OS-change history (the layer behind inbox.md)
├── GOALS.md                  <- Identity, ownership, Q2 goals
│
├── context/                  <- Sprint state (read before any command)
│   ├── current-sprint.md        Sprint goal, committed stories, constraints
│   ├── open-items.md            Unresolved items needing owner/deadline
│   ├── decisions-log.md         Canonical decision log — every scope/design/prioritisation call
│   ├── risks.md                 Active blockers + cross-team dependencies
│   └── sprint-calendar.md       Ceremony dates
│
├── tasks/
│   ├── active.md                Current sprint tasks, blockers, waiting-on
│   └── backlog.md               Future process / stakeholder work (not story-level)
│
│── PARA ──────────────────────────────────────────────
│
├── projects/
│   ├── otep-mvp/                Auth + Opportunities: PRDs, stories, research
│   ├── otg-ops/                 BAU: OTG platform maintenance + ops
│   ├── pm-conversion/           BA→PM: evidence tracker + one-pager for panel
│   └── sprint-allocation.md     Sprint plan (Sprints 1–11)
│
├── areas/
│   ├── sprint-delivery/         Ceremony prep guide
│   ├── stakeholders/people/     Profiles: Adrian, Pow Hwee, Amber, Jace, Leo, Thomas
│   ├── pm-growth/               Habit card, day-in-the-life guide
│   └── product-ops/             Company, product, team context + rituals
│
├── resources/
│   ├── otep-mvp-release.md      Sprint plan + dependency map + scope concerns
│   ├── otep-roadmap-okrs-2627.md
│   └── workflows/
│       ├── sprint-boundary/     Close sprint, update tasks, open new sprint
│       ├── story-pipeline/      Draft → groom → refine → DoR → Jira
│       ├── post-meeting-capture/ D/A/Q triage → route to correct files
│       ├── weekly-stakeholder-update/
│       ├── quarterly-planning/
│       └── user-research-synthesis/
│
├── archive/
│   ├── meetings/                Past grooming + planning notes
│   └── outputs/                 Past sprint artifacts
│
│── Standalone ────────────────────────────────────────
│
├── outputs/                  <- Current sprint generated briefs
├── scripts/                  <- Jira API helpers (jira-test.sh, jira-sprint.sh)
├── skills/                   <- PM library: Dean (9) + Pawel (65) + NotebookLM (7)
└── .claude/                  <- 14 commands, 4 skills, 1 agent, registry/
```

---

## How I Work — Daily Rhythm + Workflows

Three workflows underpin the system. Commands and skills handle the day-to-day. Workflows handle the transitions where things fall through cracks.

### Daily Rhythm

**Morning (10 min)**

1. **Scan channels → capture into `inbox.md`** (5 min)

   | Channel | What to scan for | Extract to inbox |
   |---------|-----------------|-----------------|
   | **Slack / Teams** | Decisions made without you, blockers raised overnight, scope requests, design questions from Amber/Pow Hwee | Decisions, blockers, and requests only. Skip status updates and FYI threads. |
   | **Email** | Approvals from Jacky/Adrian/steering, action requests, meeting invites with pre-reads | Requests and approvals. Forward pre-reads to inbox Parking Lot if not urgent. |
   | **Jira** | Story status changes, new comments on your stories, sprint board drift | Only if action needed — a status change isn't an inbox item unless it changes your plan. |
   | **Confluence** | Spec edits by Pow Hwee or Jace, new pages tagged to OTEP | Scope or requirement changes only. Don't duplicate the doc — link it. |
   | **Calendar** | Today's meetings — who, what, any prep needed | Meeting names + attendees. Prep happens via `/meeting-prep`, not in the inbox. |

   **The filter:** For each item, ask: is this a **D** (decision), **A** (action), or **Q** (open question)? If it's none of these — it's info. Let it go.

   **What good captures look like** — concrete examples, mirroring the `### From …` sections in `inbox.md`. Tag each line `[D]` / `[A]` / `[Q]`; the `❌` lines show what to *let go* — don't capture those, they're here to mark the boundary:

   ```
   ### From Slack / Teams
   - [D] Pow Hwee + Leo: auth FE is done, full WOG AD flow finalising Tue — confirm at mid-sprint review
   - [Q] Amber blocked — needs the filter UI pattern call (sidebar vs top chips) before she can design OTEP-86
   - [A] Jace asked me to loop Diana into opportunities decisions from now on
   - ❌ "OTEP-201 moved to QA" — status update, doesn't change my plan
   - ❌ FYI thread on the design-system navbar MR — already tracked in active.md

   ### From Email
   - [D] Steering approved proceeding with the Opportunities MVP → log in decisions-log.md
   - [A] Rama replied asking which date field OTEP sorts on — needs an answer today
   - [Parking Lot] BO Senior Level deck attached for Thursday — read before the session, not urgent now
   - ❌ "OTEP May newsletter" — FYI

   ### From Jira
   - [A] OTEP-85: Pow Hwee can't size it without the `is_published` rule → chase Rama (open item #4)
   - ❌ "OTEP-209 marked Done" — status change, no action
   - ❌ Leo's comment on OTEP-170 navbar config — already in active.md

   ### From Confluence
   - [check scope] Pow Hwee added a session-timeout section to the auth flow page — does it change WOG-04? Link the page, don't copy it.
   - ❌ new "OTEP onboarding draft" page — link it from resources/ if it matters; don't duplicate the content

   ### Ceremony Prep / Calendar
   - Wed 13 May — internal Squad groom (Pow Hwee, Leo, Thomas, Amber) — prep via /groom-prep
   - Thu 14 May — Backlog Grooming + Sprint Planning (squad + Jacky/XZ) — prep via /sprint-plan-prep
   - capture the meeting + attendees only — the prep task itself lives in active.md, not the inbox

   ### From Meetings
   - don't free-form here — use the Post-Meeting Capture workflow: dump raw notes, then tag every line D / A / Q / I. See the worked "PM Weekly Catch Up" entry in inbox.md.
   ```

2. **Triage inbox** — route each item to `tasks/`, `projects/`, `context/`, or delete; anything still pending → tag it D/A/Q/I and move it to `## Triaged — pending routing`
3. **Log the triage** — append today's entry to [changelog.md](changelog.md): what came in, what got routed to which file, what was deleted, what's still pending
4. **Run `/daily`** — closes yesterday's loop (carries + age), then the outcome pulse, schedule + PM moves, one status-&-moves table, top 3, what's parked, and a concrete PM rep
5. **Skim `context/open-items.md`** — `/daily` surfaces the urgent ones; a quick scan catches anything it didn't flag

**After every meeting (2 min)** — [Post-Meeting Capture workflow](resources/workflows/post-meeting-capture/workflow-spec.md)
1. Dump raw notes into `inbox.md`
2. Tag each item: **D** (decision), **A** (action item), **Q** (open question), or **I** (info — let it go)
3. Route: D → `decisions-log.md`, A (mine) → `active.md`, A (theirs) / Q → `open-items.md`

**Evening (5 min)**
1. Update `tasks/active.md` — mark done, add new, update Waiting On
2. Dump uncaptured items into `inbox.md`
3. Run `/endday`

**Friday (10 min)**
- Run `weekly-update` skill
- Review inbox Parking Lot — move to backlog or delete

### Sprint Boundary (every 2 weeks) — [Sprint Boundary workflow](resources/workflows/sprint-boundary/workflow-spec.md)

The highest-leverage workflow. Stale `current-sprint.md` breaks every command.

**Friday (sprint end, 10 min)**
1. Archive outputs and meeting notes
2. Log any undocumented decisions from the sprint
3. Update `tasks/active.md` — done items, carry-forward, pull from backlog
4. Update `projects/pm-conversion/evidence-tracker.md` — add at least one PM-mode entry from this sprint

**Monday (sprint start, 10 min)**
1. Update `context/current-sprint.md` — sprint goal, committed stories, constraints
2. Update `context/risks.md` — new dependencies, resolved items
3. Run `/daily` to verify the system reads correctly

### Story Pipeline (ongoing) — [Story Pipeline workflow](resources/workflows/story-pipeline/workflow-spec.md)

Stories need to be **2 sprints ahead** of build. This pipeline gets them from draft to sprint-ready.

```
Draft (Michelle writes)
  → Internal Groom (Tue week 1, squad reviews)
    → Refine (Amber designs, Pow Hwee reviews API, Michelle updates AC)
      → Backlog Groom (Thu week 1, full team estimates)
        → DoR Met (all checklist items green)
          → Sprint Planning (Thu week 2) → Jira
```

Track progress in [projects/otep-mvp/sprint-checklists.md](projects/otep-mvp/sprint-checklists.md) — per-story grooming readiness and DoR blockers, per sprint. Updated as stories advance. Cut ACs (should-haves, good-to-haves, R1) get pulled into [projects/otep-mvp/deferred-acs.md](projects/otep-mvp/deferred-acs.md).

Key tools: `/groom-prep` before grooming sessions, `pm-reviewer` agent to check story quality.

---

## Channel-to-System Mapping

| Channel | Capture | Route to |
|---------|---------|----------|
| **Meetings** | Use Post-Meeting Capture (D/A/Q triage) | Decisions → `decisions-log.md`. Actions → `active.md` or `open-items.md`. |
| **Slack/Teams** | Decisions, blockers only | Decisions → `decisions-log.md`. Blockers → `active.md`. |
| **Email** | Requests, approvals | Requests → `active.md`. Approvals → `decisions-log.md`. |
| **Jira** | Only if action needed | Status → `current-sprint.md`. Scope → `projects/`. |
| **Confluence** | Spec updates | Project changes → `projects/`. Reference → `resources/`. |

Jira and Confluence are systems of record — link, don't duplicate. Everything else is a stream — capture D/A/Q only.

---

## Integrations

**Jira (live).** Auth via API token in `.env` (gitignored). Helper scripts in `scripts/`:
- `jira-test.sh` — connectivity check; whoami + 5 issues assigned to me
- `jira-sprint.sh` — active sprint on OTEP-Pathfinder (board 12541), grouped by status with assignees. Override with `JIRA_BOARD_ID=…` for other boards (OTEP-Core 13640, Product Backlog 5789).

`/daily` pulls live sprint state from Jira and adds a Sprint Pulse section (in-progress / done / backlog counts, WIP overload flags, late-sprint backlog risk). Fails gracefully to local context if Jira is unreachable.

---

## Commands & Skills

The day-to-day runs on slash commands and a few named skills. Full descriptions and when-to-use each: [.claude/CLAUDE.md](.claude/CLAUDE.md) — in Claude Code, type `/` to see them. Index:

- **Daily:** `/daily` · `/midday` · `/endday`
- **Ceremony prep:** `/groom-prep` · `/groom` · `/sprint-plan-prep` · `/mid-sprint-review` · `/retro-prep`
- **Strategic (query NotebookLM):** `/week` · `/brief` · `/decision` · `/retro` · `/scan` — plus `/archive`
- **Named skills:** `weekly-update` · `meeting-prep` · `draft-prd-section` · `synthesize-research`
- **Reusable agent:** `pm-reviewer` — checks user-story / AC quality

---

## PM Skills Library

Two libraries for any PM task — **Dean Peters** for guided thinking and frameworks, **Pawel Huryn** for fast, sharp outputs. Check these before defaulting to a generic answer.

Full routing tables (which skill for which situation): [skills/SKILL-INDEX.md](skills/SKILL-INDEX.md). A short "which tool for what" quick-reference lives in [.claude/CLAUDE.md](.claude/CLAUDE.md).

---

## Current State (Sprint 1)

**Sprint goal:** Auth flows end-to-end. OTG data pipeline delivering records. C@G ingestion method confirmed.

**Active projects:**

| Project | Status | Key file |
|---------|--------|----------|
| OTEP MVP (Auth + Opportunities) | Sprint 1 — Auth + Data Infrastructure | [prd-opportunities.md](projects/otep-mvp/prd-opportunities.md), [prd-auth.md](projects/otep-mvp/prd-auth.md) |
| OTG Ops | Ongoing BAU — platform maintenance + ops | [brief.md](projects/otg-ops/brief.md), [task-log.md](projects/otg-ops/task-log.md) |
| BA-to-PM Conversion | Evidence gathering — updated every sprint boundary | [evidence-tracker.md](projects/pm-conversion/evidence-tracker.md) |

**Key files:**
- Sprint plan: [context/sprint-calendar.md](context/sprint-calendar.md) — 12 sprints, 4 May – 16 Oct 2026 (v2 cadence). ([otep-mvp-release.md](resources/otep-mvp-release.md) predates this — needs updating.)
- Story ID map: [story-id-map.md](projects/otep-mvp/story-id-map.md) — PRD ↔ Jira ID reconciliation
- Scoping gaps: [scoping-gaps-tracker.md](projects/otep-mvp/scoping-gaps-tracker.md) — the PRD spec-gap register: 13 gaps (10 open, 3 deferred to R1), reviewed monthly
- Open items: [open-items.md](context/open-items.md) — the active chase list, owners + deadlines
- Deferred ACs: [deferred-acs.md](projects/otep-mvp/deferred-acs.md) — should-haves, good-to-haves, R1 deferrals pulled out of story files
- Conversion one-pager: [one-pager.md](projects/pm-conversion/one-pager.md) — updated monthly or before panel
