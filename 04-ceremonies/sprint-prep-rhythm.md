# Sprint Prep Rhythm

When to run each prep command, mapped to your 2-week sprint cycle.
Update the "This Sprint" section at sprint start. The pattern stays the same.

---

## The Pattern

**First step for any prep session:** Open [sprint-checklists.md](sprint-checklists.md) to check story readiness and DoR blockers. Then run the prep command.

### Week 1

| Day | Ceremony | Prep steps | Timing |
|-----|----------|-----------|--------|
| Mon | Sprint starts · Retro & Demo (prev sprint) | Run `/retro` (prep done last Fri), `/daily`, `/week` | Morning |
| Tue | Squad Grooming (next sprint, internal) | `/groom-prep` done Mon; run `/groom` morning-of | Morning of |
| Wed | (prep day — no ceremony) | `/groom-prep` to catch AC gaps before Thu Backlog Grooming | Afternoon |
| Thu | Backlog Grooming (next sprint) | Run `/groom` | Morning of |
| Fri | OTEP Squad Sync · dependency sync | Bring unresolved DoR blockers from sprint-checklists.md | — |

### Week 2

| Day | Ceremony | Prep steps | Timing |
|-----|----------|-----------|--------|
| Mon | Mid-Sprint Review | Run `/mid-sprint-review`; tick resolved blockers in sprint-checklists.md | Morning of |
| Wed | (prep day — no ceremony) | `/sprint-plan-prep` to catch gaps before Thu planning | Afternoon |
| Thu | Sprint Planning (next sprint) | Run `/sprint-plan-prep` (refresh); populate next sprint in sprint-checklists.md | Morning of |
| Fri | Sprint Ends + Finalisation | Run `/archive` then `/retro-prep` | After finalisation sign-off |

---

## This Sprint: Sprint 2 (Mon 18 May – Fri 29 May)

### Week 1
- [ ] **Mon 18 May** — Sprint starts + Retro & Demo (Sprint 1): run `/retro` (deferred — PH + Michelle out)
- [ ] **Tue 19 May** — Squad Grooming (Sprint 2 internal): run `/groom` (morning of). ⚠️ Resolve #28 + #29 BEFORE session.
- [ ] **Wed 20 May** — Prep day: run `/groom-prep` (afternoon)
- [ ] **Thu 21 May** — Backlog Grooming (Sprint 3): run `/groom` (morning of; Leo out PM)
- [ ] **Fri 22 May** — Squad Sync: bring unresolved DoR blockers

### Week 2
- [ ] **Mon 25 May** — Mid-Sprint Review: run `/mid-sprint-review`, tick resolved blockers in sprint-checklists.md
- [ ] **Wed 27 May** — Prep day: run `/sprint-plan-prep` (afternoon)
- [ ] **Thu 29 May** — Sprint Planning (Sprint 3): run `/sprint-plan-prep` refresh; populate Sprint 3 in sprint-checklists.md
- [ ] **Fri 30 May** — Sprint Ends: run `/archive` then `/retro-prep`

### New Sprint Monday
- [ ] **Mon 01 Jun** — Retro + Demo (Sprint 2): run `/retro`, fill in Sprint 3 dates + DoR blockers in sprint-checklists.md

---

## Next Sprint Template

Copy this block at sprint start. Fill in dates.

```
## This Sprint: Sprint __ (date – date)

### Week 1
- [ ] **Mon ___** — Sprint starts + Retro & Demo (prev sprint): run `/retro`, `/daily`, `/week`
- [ ] **Tue ___** — Squad Grooming: run `/groom`
- [ ] **Wed ___** — Prep day: run `/groom-prep` (afternoon)
- [ ] **Thu ___** — Backlog Grooming: run `/groom`
- [ ] **Fri ___** — Squad Sync: bring unresolved DoR blockers

### Week 2
- [ ] **Mon ___** — Mid-Sprint Review: run `/mid-sprint-review`, tick resolved blockers in sprint-checklists.md
- [ ] **Wed ___** — Prep day: run `/sprint-plan-prep` (afternoon)
- [ ] **Thu ___** — Sprint Planning: run `/sprint-plan-prep` refresh; populate next sprint in sprint-checklists.md
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

**When to update sprint-checklists.md:** Three touchpoints — mid-sprint review (tick resolved blockers), sprint planning (populate next sprint), and new sprint Monday (fill in dates).

---

*Updated: 2026-05-19*
