# Sprint Planning Briefing — 14 May 2026 → Sprint 2 (v4 — post-reshuffle)

> Per-story readiness, dependencies, edge cases, and Pow Hwee questions are in the [grooming brief](grooming-brief-2026-05-14-groom.md). This doc covers goal, capacity, and the planning framing.

---

## Proposed Sprint Goal

**Option A (conservative):**
"By end of Sprint 2, an officer can open OTEP and see every published OTG opportunity on a listing page, newest first — with pagination, error handling, and a view-only detail page."

4 new stories (OTEP-85, OTEP-267, OTEP-268, OTEP-128) + 6 carry-overs. Listing → Detail end-to-end. No filters, no apply.

**Option B (ambitious):**
"By end of Sprint 2, an officer can browse every published OTG opportunity, click into a full detail page, and have a reliable, resilient experience — the core Listing → Detail journey is fully shippable."

Same stories, but "fully shippable" signals to the team that good-to-have ACs (ministry icons, title truncation, tab title) are expected, not just must-haves.

**Recommendation:** Go with Option A. The carry-over load is heavy (6 items, 2 of which are Sprint 2 blockers). "Fully shippable" puts pressure on Thomas that isn't realistic with one FE dev and a Mon public holiday. Ship the must-haves. Good-to-haves are the cut line.

---

## Candidate Stories

### New stories (4 — all grooming-ready)

| ID | Title | Readiness | Risk |
|---|---|---|---|
| OTEP-85 | Listing cards (absorbs sort + type badge) | **Ready** — 9 must-have ACs, officer language, subtasks defined | File import + API contract must land W1 |
| OTEP-267 | Pagination | **Ready** (if OTEP-85 ships) | Hard dep on OTEP-85 |
| OTEP-268 | Empty/error/partial-load states | **Ready** (if OTEP-85 ships) | Hard dep on OTEP-85 |
| OTEP-128 | Detail page | **Ready** — 9 must-have ACs, field map, API contract intent | Hard dep on OTEP-85 + detail API contract |

### Carry-overs from Sprint 1 (6)

| Jira | Story | Owner | Why it matters |
|---|---|---|---|
| OTEP-193 | Design data model for Opportunities | Pow Hwee | **Sprint 2 blocker.** OTEP-85 API builds on this. Day 1 priority. |
| OTEP-192 | File import job for OTG data (Excel) | Pow Hwee | **Sprint 2 critical blocker.** No import = no data. Depends on #24 (which reports). |
| OTEP-202 | POCDEX seed data | Pow Hwee | Dev environment setup |
| OTEP-271 | Local POCDEX database (container + schema) | Leo | Dev environment setup. Split from OTEP-202. |
| OTEP-194 | FormSG integration discovery | — | Sprint 3 concern, carried forward |
| OTEP-183 | POCDEX profile lookup spike | Pow Hwee | Sprint 3 ringfencing depends on this |

### Not in Sprint 2

| Story | Reason |
|---|---|
| OTEP-86 (type filter) + US-05 (clear filters) | Deferred to Sprint 3 (2026-05-14) — to make room for detail page |
| OTEP-129 (sort by posting date) | Absorbed into OTEP-85 |
| Old OTEP-128 (type badge) | Absorbed into OTEP-85 |
| US-18 (Apply via FormSG) | Sprint 3 — blocked on `formsg_url` (#2) |
| OTEP-87 (Enhance detail page) | Sprint 3 — builds on OTEP-128 base |
| OTEP-127 (Ringfencing) | Sprint 3 — depends on POCDEX spike |
| Auth edge-cases | Decided at tomorrow's finalisation |
| C@G data | Sprint 5. C@G = API (confirmed). |

---

## Capacity Flags

- **Mon 18 May PM** — public holiday + Pow Hwee + Michelle out. Sprint effectively starts **Tue 19 May** (9 working days, not 10).
- **Thu 22 May PM** — Leo out.
- **Thomas is sole FE.** All frontend work (card component, pagination, states, detail page) funnels through one person. This is the binding constraint.
- **6 carry-overs from Sprint 1.** Two are Sprint 2 blockers (OTEP-193, OTEP-192). Four are dev environment or Sprint 3 prep. The blockers must land W1 or OTEP-85 frontend has nothing to build against.
- **Contract-first approach.** Pow Hwee, Thomas, Leo aligning on API contracts tomorrow (Fri 15 May). Thomas can start frontend shell in W1 using mock data against the agreed contract. Backend catches up by mid-W1.
- **Open item #24 (which OTG Excel reports)** — critical path. Michelle sharing reports. Without this, OTEP-192 can't be built.

### Suggested dev sequence

| Phase | What | Who | When |
|-------|------|-----|------|
| 1 | Data model (OTEP-193) | Pow Hwee | Day 1 (Tue 19 May) |
| 2 | File import job (OTEP-192) | Pow Hwee / Leo | Immediately after |
| 3 | Listing + Detail APIs | Pow Hwee | W1 (contracts agreed Fri 15) |
| 4 | Card shell + detail page route | Thomas | W1 (mock data) |
| 5 | Wire to real APIs | Thomas | W2 |
| 6 | Pagination + states | Thomas | W2 (parallel) |

---

## Michelle's Opening Statement

"Sprint 2 delivers the core officer journey: open OTEP, browse every published OTG opportunity, and click into a detail page. Four new stories — listing cards, pagination, error handling, and the detail page — on top of six carry-overs, two of which are the data foundation that everything else chains from. The carry-overs aren't late work — they're the second half of a foundation that couldn't be built until field confirmations and the ingestion architecture landed this week. Pow Hwee is leading a contract-first approach so Thomas can start frontend on mock data while backend catches up. Thomas is our binding constraint, so I want the team to be honest about what fits."

---

## What NOT to Do in This Session

- **Don't assign stories** — let the team self-select. Thomas will naturally take frontend; Pow Hwee/Leo take backend.
- **Don't frame carry-overs as failures.** Foundation first, features second. Six carry-overs, but six infra tickets also shipped in Sprint 1.
- **Don't commit good-to-have ACs as must-ship.** Must-haves are the commitment. Good-to-haves are the cut line if Thomas runs out of time.
- **Don't let OTEP-193 and OTEP-192 stay ambiguous.** Who starts which, when? Day 1. This is the one thing that can't leave the room undecided.
- **Don't solve API contract details in planning.** That's tomorrow's sync. Planning is about scope and commitment, not implementation.

---

## Decisions to Log After Planning

Update these files after the session:
- `context/current-sprint.md` — swap in the Sprint 2 section on Monday
- `context/decisions-log.md` — Sprint 2 final commitment, any scope changes
- `projects/sprint-allocation.md` — reconcile if anything shifted
- `projects/otep-mvp/sprint-checklists.md` — update story status
- `context/open-items.md` — #24 and #23 status after resolution

---

*Generated 2026-05-14 (v4 — post-reshuffle). Sources: current-sprint.md, sprint-allocation.md, sprint-checklists.md, open-items.md, decisions-log.md, filters.md, otg-lifecycle.md.*
