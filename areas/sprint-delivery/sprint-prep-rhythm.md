# Sprint Prep Rhythm

When to run each prep command, mapped to your 2-week sprint cycle.
Update the dates section at sprint start. The pattern stays the same.

---

## The Pattern

**First step for any prep session:** Open [sprint-checklists.md](../../projects/otep-mvp/sprint-checklists.md) to check story readiness and DoR blockers. Then run the prep command.

> **Cadence note:** Sprint 1 ran a transitional combined cadence (Backlog Grooming + Sprint Planning together on Thu W2 — Thu 14 May). The pattern below applies **from Sprint 2 onwards** per the OTEP-Pathfinder Sprint Ceremonies v2 doc: Backlog Grooming is Thu **W1**, Sprint Planning is Thu **W2** — separate. Sprint 1's checklist below keeps the combined Thursday.

### Week 1

| Day | Ceremony | Prep steps | Timing |
|-----|----------|-----------|--------|
| Mon | Sprint starts · Retro & Demo (prev sprint) · (optional) stakeholder pre-grooming walkthrough (Jacky, Mark) | Run `/retro` (prep done last Fri), `/daily`, `/week`; if walkthrough, `/groom-prep` first | Morning |
| Tue | [Internal] Squad Grooming (next sprint) | 1. Check sprint-checklists.md — which stories are blocked? 2. `/groom-prep` (done Mon) then `/groom` | `/groom` morning of |
| Wed | (prep day — no ceremony) | Check sprint-checklists.md for new blockers; `/groom-prep` to catch AC gaps before Thu's Backlog Grooming | Afternoon |
| Thu | Backlog Grooming (next sprint) | Run `/groom` | Morning of |
| Fri | Dependency sync (Li Hui) · weekly retro | Bring unresolved DoR blockers from sprint-checklists.md; `/retro` | — |

### Week 2

| Day | Ceremony | Prep steps | Timing |
|-----|----------|-----------|--------|
| Mon | [Internal] Mid-Sprint Review | 1. Run `/mid-sprint-review` 2. Update resolved DoR blockers in sprint-checklists.md | Morning of |
| Wed | (prep day — no ceremony) | Check DoR status; `/sprint-plan-prep` to catch gaps before Thu's planning | Afternoon |
| Thu | Sprint Planning (next sprint) | Run `/sprint-plan-prep` (refresh); after planning, populate next sprint's section in sprint-checklists.md | Morning of |
| Fri | Sprint Ends + Finalisation | 1. Run `/archive` then `/retro-prep` | After finalisation sign-off |

---

## This Sprint: Sprint 2 (May 18 – May 29)

### Week 1
- [ ] **Mon May 18** — Sprint starts + Retro & Demo (Sprint 1): run `/retro` (if ceremony runs — PH + Michelle out PM). Check with squad.
- [ ] **Tue May 19** — Squad Grooming (Sprint 2 internal): run `/groom` (morning of)
- [ ] **Thu May 22** — Backlog Grooming (Sprint 3): run `/groom` (morning of; Leo out PM)
- [ ] **Fri May 23** — Dependency sync: bring unresolved DoR blockers from sprint-checklists.md

### Week 2
- [ ] **Mon May 26** — Mid-Sprint Review: run `/mid-sprint-review`, tick off resolved blockers in sprint-checklists.md
- [ ] **Wed May 28** — Prep day: check sprint-checklists.md, run `/sprint-plan-prep`
- [ ] **Thu May 29** — Sprint Planning (Sprint 3): run `/sprint-plan-prep` refresh; populate Sprint 3 section in sprint-checklists.md
- [ ] **Fri May 30** — Sprint Ends: run `/archive` then `/retro-prep`

### New Sprint Monday
- [ ] **Mon Jun 1** — Retro + Demo: run `/retro`, fill in Sprint 3 dates + DoR blockers in sprint-checklists.md

---

## Next Sprint Template

Copy this block at sprint start. Fill in dates.

```
## This Sprint: Sprint __ (date -- date)

### Week 1
- [ ] **Mon ___** — Stakeholder walkthrough: check sprint-checklists.md blockers, run `/groom-prep`
- [ ] **Tue ___** — Squad Grooming: run `/groom`
- [ ] **Fri ___** — Dependency sync: bring unresolved DoR blockers from sprint-checklists.md

### Week 2
- [ ] **Mon ___** — Mid-Sprint Review: run `/mid-sprint-review`, tick off resolved blockers in sprint-checklists.md
- [ ] **Wed ___** — Prep day: check sprint-checklists.md, run `/groom-prep`
- [ ] **Thu ___** — Backlog Grooming + Sprint Planning: run `/groom` then `/sprint-plan-prep`, populate next sprint in sprint-checklists.md
- [ ] **Fri ___** — Sprint Ends: run `/archive` then `/retro-prep`

### New Sprint Monday
- [ ] **Mon ___** — Retro + Demo: run `/retro`, fill in next sprint dates + DoR blockers in sprint-checklists.md
```

---

## Why This Order Matters

**sprint-checklists.md first, then the command.** The checklist tells you what's in scope and what's blocked. The command does the detailed analysis. Checking the checklist first means you catch "this story still has no design" before the command runs — so you're not prepping stories that aren't ready.

`/groom-prep` always runs the day before grooming — it flags AC gaps, missing designs, and dependency risks while you still have time to fix them. `/groom` runs morning-of because it does a deep pass on edge cases, dependencies, and cross-cutting concerns from the local story and context files — sharpens your facilitation right before the session.

`/sprint-plan-prep` runs after `/groom` on Thursday because grooming surfaces last-minute scope changes that affect which stories are sprint-ready.

`/retro-prep` runs Friday (not Monday morning) so you have the weekend buffer if you need to chase down a demo recording or clarify a shipped story with eng.

**When to update sprint-checklists.md:** Three touchpoints per sprint — mid-sprint review (tick resolved blockers), sprint planning (populate next sprint), and new sprint Monday (fill in dates). The Friday dependency sync is also a natural time to update if Li Hui resolves something.

---

*Updated: 2026-05-11*
