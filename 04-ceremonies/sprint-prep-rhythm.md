# Sprint Prep Rhythm

When to run each prep command, mapped to your 2-week sprint cycle.
Update the "This Sprint" section at sprint start. The pattern stays the same.

---

## The Pattern

**First step for any prep session:** Open [sprint-checklists.md](sprint-checklists.md) to check story readiness and DoR blockers. Then run the prep command.

### Week 1

| Day | Ceremony | Prep steps | Timing |
|-----|----------|-----------|--------|
| Mon | Sprint starts · Retro & Demo (prev sprint) | Run `/retro` (prep done last Fri), `/daily-plan`, `/week` | Morning |
| Tue | Design review (stories for sprint after next) | `/groom-prep` done Mon; run `/groom` morning-of | Morning of |
| Wed | (prep day — no ceremony) | `/groom-prep` to catch AC gaps before Thu grooming | Afternoon |
| Thu | Backlog grooming (stories for coming sprint) | Run `/groom`; run `/grooming-close` after session | Morning of |
| Fri | OTEP Squad Sync · dependency sync | Bring unresolved DoR blockers from sprint-checklists.md | — |

### Week 2

| Day | Ceremony | Prep steps | Timing |
|-----|----------|-----------|--------|
| Mon | Mid-Sprint Review | Run `/mid-sprint-review`; tick resolved blockers in sprint-checklists.md | Morning of |
| Wed | (prep day — no ceremony) | Run `/sprint-check` to verify shelf depth; `/sprint-plan-prep` to catch gaps | Afternoon |
| Thu | Sprint Planning (next sprint) | Run `/sprint-plan-prep` (refresh); populate next sprint in sprint-checklists.md | Morning of |
| Fri | Sprint Ends + Finalisation | Run `/archive` then `/retro-prep` | After finalisation sign-off |

---

## This Sprint: Sprint 4 (Mon 15 Jun – Sat 28 Jun)

### Week 1
- [x] **Mon 16 Jun** — Sprint starts + Retro & Demo (Sprint 3): run `/retro`
- [x] **Tue 16 Jun** — Design review (S5+ stories)
- [x] **Wed 17 Jun** — Prep day: run `/groom-prep` (afternoon)
- [ ] **Thu 18 Jun** — Backlog Grooming (Sprint 5): run `/groom` morning-of; run `/grooming-close` after
- [ ] **Fri 19 Jun** — Squad Sync: bring unresolved DoR blockers

### Week 2
- [ ] **Mon 22 Jun** — Mid-Sprint Review: run `/mid-sprint-review`, tick resolved blockers in sprint-checklists.md
- [ ] **Wed 24 Jun** — Prep day: run `/sprint-check` then `/sprint-plan-prep` (afternoon)
- [ ] **Thu 25 Jun** — Sprint Planning (Sprint 5): run `/sprint-plan-prep` refresh; populate Sprint 5 in sprint-checklists.md
- [ ] **Fri 27 Jun** — Sprint Ends: run `/archive` then `/retro-prep`

### New Sprint Monday
- [ ] **Mon 29 Jun** — Retro + Demo (Sprint 4): run `/retro`, fill in Sprint 5 dates + DoR blockers in sprint-checklists.md

---

## Next Sprint Template

Copy this block at sprint start. Fill in dates.

```
## This Sprint: Sprint __ (date – date)

### Week 1
- [ ] **Mon ___** — Sprint starts + Retro & Demo (prev sprint): run `/retro`, `/daily-plan`, `/week`
- [ ] **Tue ___** — Design review (stories for sprint after next): run `/groom-prep` Mon; run `/groom` morning-of
- [ ] **Wed ___** — Prep day: run `/groom-prep` (afternoon) to catch AC gaps before Thu
- [ ] **Thu ___** — Backlog grooming (stories for coming sprint): run `/groom` morning-of; run `/grooming-close` after
- [ ] **Fri ___** — Squad Sync: bring unresolved DoR blockers

### Week 2
- [ ] **Mon ___** — Mid-Sprint Review: run `/mid-sprint-review`, tick resolved blockers in sprint-checklists.md
- [ ] **Wed ___** — Prep day: run `/sprint-check` then `/sprint-plan-prep` (afternoon)
- [ ] **Thu ___** — Sprint Planning (next sprint): run `/sprint-plan-prep` refresh; populate next sprint in sprint-checklists.md
- [ ] **Fri ___** — Sprint Ends: run `/archive` then `/retro-prep`

### New Sprint Monday
- [ ] **Mon ___** — Retro + Demo: run `/retro`, fill in next sprint dates in sprint-checklists.md
```

---

## Why This Order Matters

**sprint-checklists.md first, then the command.** The checklist tells you what's in scope and what's blocked. The command does the detailed analysis. Checking the checklist first means you catch "this story still has no design" before the command runs.

`/groom-prep` always runs the day before grooming — flags AC gaps, missing designs, and dependency risks while you still have time to fix them. `/groom` runs morning-of — deep pass on edge cases and cross-cutting concerns right before the session.

`/sprint-plan-prep` runs after grooming on Thursday because grooming surfaces last-minute scope changes that affect which stories are sprint-ready.

`/retro-prep` runs Friday (not Monday morning) so you have the weekend buffer if you need to chase a demo recording or clarify a shipped story with eng.

> **Optional deeper layer:** for a high-conflict sprint, a tricky reprioritisation, or any time you want the backlog read through PM + Tech Lead + Designer lenses at once, spawn the **sprint-trio** agent alongside `/groom-prep` (or `/mid-sprint-review` / `/sprint-plan-prep`). It pulls live Jira and produces story-shaping / backlog-prep output you take into the session. It preps the backlog; the team sizes at grooming. Use it as an add-on, not a replacement for the commands.

**When to update sprint-checklists.md:** Three touchpoints — mid-sprint review (tick resolved blockers), sprint planning (populate next sprint), and new sprint Monday (fill in dates).

---

*Updated: 2026-06-18 — ceremony cadence updated: Tue W1 = design review, Thu W1 = backlog grooming, Thu W2 = sprint planning. New commands added: `/grooming-close` (post-Thu grooming), `/sprint-check` (Wed W2 prep).*
