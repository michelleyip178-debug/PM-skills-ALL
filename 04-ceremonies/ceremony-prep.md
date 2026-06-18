# Ceremony Prep Guide

What to prepare and bring for each ceremony. For the command schedule and sprint dates, see `sprint-prep-rhythm.md`.

---

## Recurring Meetings

### Daily — OTEP Team 2 Standup (10am)
**Prep (5 min):**
- [ ] Know what's blocked and what you need to unblock
- [ ] Any priority changes to communicate

### Monday — BO sync (4pm)
**Prep (15 min):**
- [ ] Check sprint progress — are we on track?
- [ ] Have 1 update and 1 blocker ready (if any)
- [ ] Know your "ask" if you have one

### Tuesday W1 — Design review (stories for sprint after next)
**Prep (15 min):**
- [ ] Which designs for the sprint-after-next are ready to walk the BO through?
- [ ] Have ACs and the screen flow ready for what's being reviewed
- [ ] Know the BO decisions you need closed here — bring positions, not options
- [ ] Bring any user feedback / hallway-test findings

> No separate "Design review with Amber" appears on the calendar — Amber feedback happens async or inside this BO review. If a design decision needs a dedicated session with Amber, schedule one; don't assume a recurring slot exists.

### Biweekly — Mark & GK (1 hr)
**Prep (30 min) — high stakes, use `/meeting-prep`:**
- [ ] Progress against MVP milestones (concise + detailed — their preference)
- [ ] Scoping gaps status — any that need their decision?
- [ ] Risks flagged early with proposed mitigations
- [ ] MVP guardrails (CLAUDE.md) ready for any new ideas they throw out
- [ ] One clear "ask" if you need a decision from them
- [ ] Keep under 30 min for sprint cycle update, leave 30 min for discussion

---

## Sprint Ceremonies — What to Bring

### Stakeholder walkthrough (Mon wk 1)
**Prep (15 min):**
- [ ] Story scores and AC status for upcoming work
- [ ] Know which stories Jacky/Mark need to weigh in on
- [ ] One clear framing per story: what it does, why now

### Design Review (Tue W1, 30 min prep)
- [ ] Draft user stories written for the sprint after next
- [ ] Acceptance criteria drafted (doesn't need to be final)
- [ ] Identify which stories need design, API contracts, or tech spikes
- [ ] Know your priorities — what MUST go in that sprint vs. nice-to-have

### Backlog Grooming (Thu W1, 45 min prep — replaces Squad Grooming)
- [ ] Stories prioritised — high/urgent at the top
- [ ] Large stories broken down into sprint-sized items
- [ ] Acceptance criteria, descriptions, requirements clear enough to discuss
- [ ] Designs attached where available (or flag what's missing)
- [ ] Dependencies identified
- [ ] Be ready to answer "why this priority?" for each item
- [ ] Run `/grooming-close` after the session to gate stories and check shelf depth

### Mid-Sprint Review (Mon wk 2, 15 min prep)
- [ ] Check: are current sprint items on track to finish by Friday?
- [ ] Identify at-risk items — what might not make it?
- [ ] Any scope or priority changes needed mid-sprint?

### Sprint Planning (Thu W2, 1 hr prep — the big one)
- [ ] **All stories must meet DoR:**
  - [ ] UI assets and UX flows designed and linked to Acceptance Criteria (Amber)
  - [ ] Feature flag designed with entry point identified
  - [ ] API Contract identified and documented (Pow Hwee)
  - [ ] All platform subtasks (including test cases) identified
- [ ] Final priority order confirmed
- [ ] Design locked down with business
- [ ] Requirements and technical details ironed out
- [ ] Know the sprint goal — what's the one sentence that describes success?

### Retro + Demo (Mon new sprint, 20 min prep)
- [ ] **Demo:** What shipped that's worth showing? Coordinate with eng on who demos what
- [ ] **Retro:** Reflect on what went well, what didn't, what to change
  - Come with 1 specific thing to improve (not generic "communicate better")
  - Come with 1 thing that worked well (recognise the team)

**Two-tier demo format** (working agreement with Imelda + Rama, 2026-06-02):

| Tier | Audience | Format | Prep |
|------|----------|--------|------|
| **Regular demos** | Working level up to Jacky | Each PM/owner presents their own part. Scoped to **just the previous sprint's output** — these are *working sessions*, not a showcase. | Low. No cross-learning of each other's parts. |
| **Special sessions** | Mark, GK | Consolidate into **one coherent narrative** — PMs cover each other's parts, unified storyline. | High. Smoother Q&A, shared story. |

- Set expectations explicitly: tell the working level (up to Jacky) that regular demos are working sessions covering only the prev sprint — don't let them creep into showcase expectations.
- Reserve the consolidated-narrative effort for Mark/GK, where it pays off.

---

## PM-Only Cadences

### Monday morning — Personal Planning (30 min)
**Prep:** Just show up. Run `/daily-plan`. Pick your #1 thing.

### Friday — Weekly Update
**Prep (10 min):**
- [ ] Update active.md (if not already current)
- [ ] Run `/weekly-update` — review and send

### Sprint end — Sprint Sweep
- [ ] Move completed tasks → archive with impact notes
- [ ] Pull from backlog → active
- [ ] Update scoping gaps tracker

---

## The Lead Time Rule

| Ceremony | Stories need to be at... | By when |
|----------|------------------------|---------|
| Design Review (Tue W1) | Draft (AC written, priority clear) | Monday of W1 |
| Backlog Grooming (Thu W1) | Refined (designs in progress, requirements clear) | Wednesday of W1 |
| Sprint Planning (Thu W2) | **DoR met** (designs done, API contract, subtasks, test cases) | Wednesday of W2 |

You need to be writing stories **2 weeks before they're built** — prepping the sprint-after-next while the current sprint runs.

---

## Quick Reference: What To Bring

| Meeting | Bring | Don't bring |
|---------|-------|-------------|
| Standup | Blockers, priority changes | Long explanations |
| Design Review (Tue W1) | Draft stories, open questions | Final designs |
| Backlog Grooming (Thu W1) | Prioritised stories, requirements, designs-in-progress | Unwritten stories |
| Sprint Planning | DoR-ready stories, sprint goal | Anything that still needs design |
| Mid-Sprint Review | Risk assessment, at-risk items | New scope |
| Demo | What shipped, impact | Excuses for what didn't |
| Mark & GK | Progress, risks, one ask | Surprises |
| Design Review | ACs, user context, decision needed | Vague "make it good" briefs |

---

*Updated: 2026-06-18 — ceremony cadence updated: Tue W1 = design review, Thu W1 = backlog grooming, Thu W2 = sprint planning*
