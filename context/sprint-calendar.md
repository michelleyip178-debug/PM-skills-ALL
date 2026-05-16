# Sprint Cadence Calendar

**Timezone:** Asia/Singapore (SGT, UTC+8)
**Source of truth:** OTEP-Pathfinder Sprint Ceremonies v2 (4 May – 16 Oct 2026, 12 sprints, 2-week cadence).
**Sprint 1 start:** Mon 4 May 2026
**Feature Freeze:** end of Sprint 8 — **Fri 21 Aug 2026** (end of Phase 1, Feature Build)
**Go-Live:** end of Sprint 12 — **Fri 16 Oct 2026**

**Phases:** 🟢 Phase 1 Feature Build (Sprints 1–8, 4 May – 21 Aug) · 🔵 Phase 2 Compliance & Go-Live (Sprints 9–12, 24 Aug – 16 Oct).

> **Cadence change at Sprint 2.** Sprint 1 ran a transitional *combined* cadence — internal Squad Grooming early in week 1, then Backlog Grooming + Sprint Planning together on Thu of week 2 (Thu 14 May for Sprint 2). **From Sprint 2 onwards, ceremonies follow the v2 pattern below:** Squad Grooming Tue W1, **Backlog Grooming Thu W1**, Sprint Planning **Thu W2** — separate. Sprint 1's section below keeps the combined cadence; Sprints 2–12 use the v2 split.

> This file owns **dates and ceremonies**. Which stories ship in which sprint → [sprint-allocation.md](../projects/sprint-allocation.md) (it wins on scope). The "Ships:" lines below are a convenience copy only.

---

## Recurring Cadence — Feature Sprints 2–8 (Sprint 1 was transitional, see its section)

| Day | Ceremony | My role | Run |
|---|---|---|---|
| **W1 Mon** | Sprint starts · Retro & Demo (previous sprint) | Coordinate demo, join retro | `/retro` · `/daily` · `/week` |
| **W1 Tue** | [Internal] Squad Grooming (next sprint) | Lead content | `/groom-prep` then `/groom` |
| **W1 Thu** | Backlog Grooming (next sprint) | Lead content | `/groom-prep` (Wed) then `/groom` |
| **W1 Fri** | — (personal weekly retro) | — | `/retro` |
| **W2 Mon** | [Internal] Mid-Sprint Review | Participant | `/mid-sprint-review` then `/archive` (mid checkpoint) |
| **W2 Thu** | Sprint Planning (next sprint) | Present sprint goal | `/sprint-plan-prep` (Wed) then refresh morning of |
| **W2 Fri** | Sprint Ends · Finalisation (next sprint) | Confirm AC met | `/archive` (end checkpoint) then `/retro-prep` |
| **W2 Fri (every 2 sprints)** | 🔴 Bi-weekly Steering — Mark & GK | Pow Hwee attends | `/brief` (Mark/GK audience) |

Compliance sprints (9–12) run lighter: Sprint Start + Retro/Demo Mon W1, a focused Mid-Sprint Check-in Mon W2, bi-weekly Steering check-ins, and the Go-Live gate at the end of Sprint 12.

### Daily Rhythm (every working day, SGT)

| When | Command |
|---|---|
| 9:00 AM | `/daily` — schedule, carries, status, top 3, PM rep |
| 1:00 PM | `/midday` — pulse check, afternoon priorities |
| 5:30 PM | `/endday` — what got done, carry-forward, reflection |

### Weekly Rhythm (SGT)

| When | Command |
|---|---|
| Monday 9:00 AM | `/week` — decisions needed, stakeholder conversations, spec gaps |
| Friday 4:00 PM | `/retro` — Signal-Sense-Shift + PM growth lens |
| Friday 4:30 PM | `weekly-update` skill — stakeholder email for Jace/Adrian |

---

# Phase 1 — Feature Build (Sprints 1–8)

## Sprint 1 — 4–15 May · Login + Foundation + Discovery/Design  ·  *(transitional combined cadence)*
**Goal:** Login and navigate to Jobs and Opportunities.

| Date | Day | Ceremony | Run |
|---|---|---|---|
| Mon 4 May | W1 Mon | Sprint 1 starts | `/daily`, `/week` |
| Tue 5 May | W1 Tue | [Internal] Squad Grooming for Sprint 2 | `/groom-prep`, `/groom` |
| Fri 8 May | W1 Fri | weekly retro | `/retro` |
| Mon 11 May | W2 Mon | [Internal] Mid-Sprint 1 Review | `/mid-sprint-review`, `/archive` |
| Wed 13 May | W2 Wed | (prep day / optional internal pre-groom for Sprint 2) | `/groom-prep` |
| Thu 14 May | W2 Thu | Backlog Grooming + Sprint Planning for Sprint 2 (combined, 2pm L11 Anson) | `/groom` then `/sprint-plan-prep` |
| Fri 15 May | W2 Fri | Sprint 1 Ends · Finalisation for Sprint 2 | `/archive`, `/retro-prep` |

**Ships:** auth via Keycloak, base listing page layout, data model designed, POCDEX/FormSG patterns explored.

## Sprint 2 — 18–29 May · Opportunities Listing Hub  ·  *(v2 cadence from here on)*
**Goal:** Officers can browse and filter every OTG opportunity on one authenticated page, newest first, published-only.

| Date | Day | Ceremony | Run |
|---|---|---|---|
| Mon 18 May | W1 Mon | Sprint 2 starts · Retro & Demo for Sprint 1 | `/retro`, `/daily`, `/week` |
| Tue 19 May | W1 Tue | [Internal] Squad Grooming for Sprint 3 | `/groom-prep`, `/groom` |
| Thu 21 May | W1 Thu | Backlog Grooming for Sprint 3 | `/groom-prep` (Wed), `/groom` |
| Fri 22 May | W1 Fri | 🔴 Bi-weekly Steering (Mark & GK) · weekly retro | `/brief`, `/retro` |
| Mon 25 May | W2 Mon | [Internal] Mid-Sprint 2 Review | `/mid-sprint-review`, `/archive` |
| Thu 28 May | W2 Thu | Sprint Planning for Sprint 3 | `/sprint-plan-prep` |
| Fri 29 May | W2 Fri | Sprint 2 Ends · Finalisation for Sprint 3 | `/archive`, `/retro-prep` |

**Ships:** OTEP-85 (listing cards — absorbs sort + type badge), OTEP-267 (pagination), OTEP-268 (empty/error states), OTEP-128 (detail page) — Listing → Detail end-to-end, OTG data only. OTEP-86 (type filter) + US-05 (clear filters) deferred to Sprint 3 (2026-05-14). OTEP-129 absorbed into OTEP-85.

## Sprint 3 — 1–12 Jun · Search + Type Filter + Detail Page
| Date | Day | Ceremony | Run |
|---|---|---|---|
| Mon 1 Jun | W1 Mon | Sprint 3 starts · Retro & Demo for Sprint 2 | `/retro`, `/daily`, `/week` |
| Tue 2 Jun | W1 Tue | [Internal] Squad Grooming for Sprint 4 | `/groom-prep`, `/groom` |
| Thu 4 Jun | W1 Thu | Backlog Grooming for Sprint 4 | `/groom-prep` (Wed), `/groom` |
| Fri 5 Jun | W1 Fri | weekly retro | `/retro` |
| Mon 8 Jun | W2 Mon | [Internal] Mid-Sprint 3 Review | `/mid-sprint-review`, `/archive` |
| Thu 11 Jun | W2 Thu | Sprint Planning for Sprint 4 | `/sprint-plan-prep` |
| Fri 12 Jun | W2 Fri | Sprint 3 Ends · Finalisation for Sprint 4 | `/archive`, `/retro-prep` |

> Vesak Day 2026 is Sun 31 May → observed **Mon 1 Jun** (= Sprint 3 start). Sprint start + Sprint 2 Retro/Demo may shift to Tue 2 Jun — verify.

## Sprint 4 — 15–26 Jun · Apply Flows (FormSG + OTG)
| Date | Day | Ceremony | Run |
|---|---|---|---|
| Mon 15 Jun | W1 Mon | Sprint 4 starts · Retro & Demo for Sprint 3 | `/retro`, `/daily`, `/week` |
| Tue 16 Jun | W1 Tue | [Internal] Squad Grooming for Sprint 5 | `/groom-prep`, `/groom` |
| Thu 18 Jun | W1 Thu | Backlog Grooming for Sprint 5 | `/groom-prep` (Wed), `/groom` |
| Fri 19 Jun | W1 Fri | 🔴 Bi-weekly Steering (Mark & GK) · weekly retro | `/brief`, `/retro` |
| Mon 22 Jun | W2 Mon | [Internal] Mid-Sprint 4 Review | `/mid-sprint-review`, `/archive` |
| Thu 25 Jun | W2 Thu | Sprint Planning for Sprint 5 | `/sprint-plan-prep` |
| Fri 26 Jun | W2 Fri | Sprint 4 Ends · Finalisation for Sprint 5 | `/archive`, `/retro-prep` |

> Hari Raya Haji 2026 typically falls late May / mid-Jun — verify the exact date and adjust if it lands on a ceremony day.

## Sprint 5 — 29 Jun – 10 Jul · Careers@Gov Integration + EDM
| Date | Day | Ceremony | Run |
|---|---|---|---|
| Mon 29 Jun | W1 Mon | Sprint 5 starts · Retro & Demo for Sprint 4 | `/retro`, `/daily`, `/week` |
| Tue 30 Jun | W1 Tue | [Internal] Squad Grooming for Sprint 6 | `/groom-prep`, `/groom` |
| Thu 2 Jul | W1 Thu | Backlog Grooming for Sprint 6 | `/groom-prep` (Wed), `/groom` |
| Fri 3 Jul | W1 Fri | weekly retro | `/retro` |
| Mon 6 Jul | W2 Mon | [Internal] Mid-Sprint 5 Review | `/mid-sprint-review`, `/archive` |
| Thu 9 Jul | W2 Thu | Sprint Planning for Sprint 6 | `/sprint-plan-prep` |
| Fri 10 Jul | W2 Fri | Sprint 5 Ends · Finalisation for Sprint 6 | `/archive`, `/retro-prep` |

## Sprint 6 — 13–24 Jul · Admin Login + Instrumentation + Polish
| Date | Day | Ceremony | Run |
|---|---|---|---|
| Mon 13 Jul | W1 Mon | Sprint 6 starts · Retro & Demo for Sprint 5 | `/retro`, `/daily`, `/week` |
| Tue 14 Jul | W1 Tue | [Internal] Squad Grooming for Sprint 7 | `/groom-prep`, `/groom` |
| Thu 16 Jul | W1 Thu | Backlog Grooming for Sprint 7 | `/groom-prep` (Wed), `/groom` |
| Fri 17 Jul | W1 Fri | 🔴 Bi-weekly Steering (Mark & GK) · weekly retro | `/brief`, `/retro` |
| Mon 20 Jul | W2 Mon | [Internal] Mid-Sprint 6 Review | `/mid-sprint-review`, `/archive` |
| Thu 23 Jul | W2 Thu | Sprint Planning for Sprint 7 | `/sprint-plan-prep` |
| Fri 24 Jul | W2 Fri | Sprint 6 Ends · Finalisation for Sprint 7 | `/archive`, `/retro-prep` |

## Sprint 7 — 27 Jul – 7 Aug · E2E Testing / Stabilisation
| Date | Day | Ceremony | Run |
|---|---|---|---|
| Mon 27 Jul | W1 Mon | Sprint 7 starts · Retro & Demo for Sprint 6 | `/retro`, `/daily`, `/week` |
| Tue 28 Jul | W1 Tue | [Internal] Squad Grooming for Sprint 8 (compliance prep focus) | `/groom-prep`, `/scan` |
| Thu 30 Jul | W1 Thu | Backlog Grooming for Sprint 8 | `/groom-prep` (Wed), `/groom` |
| Fri 31 Jul | W1 Fri | weekly retro | `/retro` |
| Mon 3 Aug | W2 Mon | [Internal] Mid-Sprint 7 Review | `/mid-sprint-review`, `/archive` |
| Thu 6 Aug | W2 Thu | Sprint Planning for Sprint 8 | `/sprint-plan-prep` |
| Fri 7 Aug | W2 Fri | Sprint 7 Ends · Finalisation for Sprint 8 | `/archive`, `/retro-prep` |

## Sprint 8 — 10–21 Aug · ⭐ Feature Freeze
| Date | Day | Ceremony | Run |
|---|---|---|---|
| Mon 10 Aug | W1 Mon | **National Day observed (public holiday)** — Sprint 8 start + Sprint 7 Retro & Demo shift to Tue 11 Aug | — |
| Tue 11 Aug | W1 Tue | Sprint 8 starts · Retro & Demo for Sprint 7 · [Internal] Squad Grooming (compliance prep) | `/retro`, `/daily`, `/week`, `/groom-prep`, `/scan` |
| Thu 13 Aug | W1 Thu | Backlog Grooming (compliance prep) | `/groom-prep`, `/groom` |
| Fri 14 Aug | W1 Fri | 🔴 Bi-weekly Steering (Mark & GK) · weekly retro | `/brief`, `/retro` |
| Mon 17 Aug | W2 Mon | [Internal] Mid-Sprint 8 Review | `/mid-sprint-review`, `/archive` |
| **Fri 21 Aug** | **W2 Fri** | **Sprint 8 Ends — ⭐ FEATURE FREEZE** (Full squad + Mark + GK) | `/archive`, `/brief` |

> National Day 2026: Sun 9 Aug → observed **Mon 10 Aug** (public holiday) = Sprint 8 start. Shift the Monday ceremonies to Tue 11 Aug. There is **no** public holiday on 31 Aug.

---

# Phase 2 — Compliance & Go-Live (Sprints 9–12)

Lighter internal ceremonies; focus shifts to audit readiness, sign-offs, and stakeholder approvals.

## Sprint 9 — 24 Aug – 4 Sep · Compliance
| Date | Day | What | Run |
|---|---|---|---|
| Mon 24 Aug | W1 Mon | Compliance Sprint 9 starts · Retro & Demo for Sprint 8 | `/retro`, `/daily`, `/week`, `/brief` (security team) |
| Mon 31 Aug | W2 Mon | [Internal] Mid-Sprint 9 Check-in | `/mid-sprint-review` |
| Thu 4 Sep | W2 Thu | 🔴 Steering Check-in (Mark & GK) · Sprint 9 Ends | `/brief`, `/archive` |

## Sprint 10 — 7–18 Sep · Compliance
| Date | Day | What | Run |
|---|---|---|---|
| Mon 7 Sep | W1 Mon | Compliance Sprint 10 starts | `/daily`, `/week` |
| Fri 11 Sep | W1 Fri | 🔴 Bi-weekly Steering (Mark & GK) | `/brief` |
| Mon 14 Sep | W2 Mon | [Internal] Mid-Sprint 10 Check-in | `/mid-sprint-review` |
| Fri 18 Sep | W2 Fri | Sprint 10 Ends | `/archive`, `/scan` |

## Sprint 11 — 21 Sep – 2 Oct · Compliance
| Date | Day | What | Run |
|---|---|---|---|
| Mon 21 Sep | W1 Mon | Compliance Sprint 11 starts | `/daily`, `/week` |
| Mon 28 Sep | W2 Mon | [Internal] Mid-Sprint 11 Check-in | `/mid-sprint-review` |
| Fri 2 Oct | W2 Fri | 🔴 Steering Check-in (Mark & GK) · Sprint 11 Ends | `/brief`, `/archive` |

## Sprint 12 — 5–16 Oct · 🚀 Go-Live
| Date | Day | What | Run |
|---|---|---|---|
| Mon 5 Oct | W1 Mon | Compliance Sprint 12 starts | `/daily`, `/week` |
| Fri 9 Oct | W1 Fri | 🔴 Final Steering Sign-off (Mark & GK) | `/brief` (go/no-go) |
| Mon 12 Oct | W2 Mon | [Internal] Final Pre-Launch Review | `/scan` (final doc health) |
| **Fri 16 Oct** | **W2 Fri** | **🚀 GO-LIVE — OTEP Pathfinder MVP** (Full squad + Mark + GK) | `/retro` (full programme retro) |

---

## Key Milestones Summary

| Date | Milestone |
|---|---|
| Fri 15 May | Sprint 1 ends — auth + foundation |
| Fri 29 May | Sprint 2 ends — OTG listing experience live |
| Fri 12 Jun | Sprint 3 ends — search + filter + detail |
| Fri 26 Jun | Sprint 4 ends — apply flows functional |
| Fri 10 Jul | Sprint 5 ends — C@G + email deep-links |
| Fri 24 Jul | Sprint 6 ends — admin + instrumentation + polish |
| Fri 7 Aug | Sprint 7 ends — E2E testing / stabilisation |
| **Fri 21 Aug** | **Sprint 8 ends — ⭐ FEATURE FREEZE** (end of Phase 1) |
| Thu 4 Sep | Sprint 9 ends — security review underway |
| Fri 18 Sep | Sprint 10 ends — compliance progressing |
| Fri 2 Oct | Sprint 11 ends — sign-offs in progress |
| **Fri 16 Oct** | **Sprint 12 ends — 🚀 GO-LIVE** |

---

## Public Holidays (Singapore 2026)

| Holiday | 2026 date | Sprint affected | Action |
|---|---|---|---|
| Vesak Day | Sun 31 May → observed Mon 1 Jun | Sprint 3 start | Shift Mon ceremonies to Tue 2 Jun — verify |
| Hari Raya Haji | late May / mid-Jun (verify) | Sprint 3 or 4 | Adjust if it lands on a ceremony day |
| National Day | Sun 9 Aug → observed Mon 10 Aug | Sprint 8 start | Confirmed — Mon ceremonies shift to Tue 11 Aug. (No holiday on 31 Aug.) |

If a ceremony falls on a public holiday, shift it to the next working day and note the shift in `context/current-sprint.md` under Known constraints.

---

*Reconciled to OTEP-Pathfinder Sprint Ceremonies v2 — 2026-05-12. Sprint 1 keeps its transitional combined cadence; Sprints 2–12 use the v2 split.*
