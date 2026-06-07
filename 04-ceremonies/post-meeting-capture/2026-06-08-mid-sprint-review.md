---
date: 2026-06-08
type: Mid-Sprint Review
sprint: OTEP-Pathfinder Sprint 3
attendees: Michelle, Pow Hwee, Amber, Rathika
---

# Mid-Sprint Review — Sprint 3 (Mon 8 Jun)

**Sprint dates:** 2–14 Jun 2026

**Sprint Planning:** Thu 11 Jun — decisions from this meeting feed directly into planning.

---

## Agenda

### 1. Sprint 3 QA tail (10 min)

- **OTEP-128** — Rathika posted 8 test cases on 4 Jun. Status: is the 500 error path covered? Split AC needed (500 vs 404). @Michelle to confirm AC before this meeting.
- **OTEP-326** — QA testing against `<MISSING_FIGMA_LINK>`. @Michelle to paste LifeSG error page reference before this meeting.
- **Thomas apply-URL fix** — merged or not? Rathika gated on this to close QA.
- **OTEP-85** — SGT timezone AC still missing. BE closing-date comparison must run in Asia/Singapore. Confirm with Rathika if this is a blocker for her test cases.

---

### 2. OTEP-88 — C@G opportunities in the listing page (15 min)

**Context:** Pow Hwee flagged twice (May 28 + Jun 2). AC rewritten and synced to Jira (2026-06-05). Two items still TBC — confirm both in this meeting before Thu 11 Jun planning.

**For Pow Hwee:**
- [ ] **AC4 fallback behaviour (TBC):** if a required field is missing from a C@G card, what's the fallback? Hide field / show placeholder / drop card entirely? (Product decision — needs your call as PM, not just Pow Hwee's confirmation.)
- ~~Data source / payload confirmation~~ — covered by Slack sent 2026-06-05. Pow Hwee to respond; no need to re-raise in meeting.

**For Amber:**
- [ ] **AC2 badge spec (TBC):** LifeSG/C@G brand guideline to follow, or design freedom? Propose visual treatment.
- [ ] Card layout: is the badge additive or does it replace an existing element? Any layout shift risk?
- [ ] Graceful degradation UI: if a required field is missing, what does the card look like? Amber to spec.

**For Rathika:**
- [ ] Test data: real C@G data in test env, or mocked fixtures from Léo?
- [ ] Cross-source listing test: how to verify OTG + C@G render side-by-side? Specific test account needed?
- [ ] Graceful degradation test case: needs AC confirmed by Pow Hwee + Amber first.
- [ ] Badge accessibility: contrast ratio or screen reader label requirement?

**Outcome needed:** AC4 fallback + AC2 badge spec confirmed. Michelle to lock final AC and re-sync to Jira same day.

---

### 3. OTEP-317 — Clear all filters (10 min)

**Context:** Scope needs to be locked to type-filter-only (OTEP-86) so it doesn't appear blocked on OTEP-318 (category filter, still undecided).

**For Pow Hwee:**
- [ ] Scope lock: "Clear all" = type-filter-only in S4. Category filter is a conditional extension — OTEP-317 ships without it. Confirm.
- [ ] Trigger condition: "Clear all" visible only when ≥1 filter active, hidden when none — or always visible but disabled?

**For Amber:**
- [ ] Trigger condition design: visible-only-when-active vs always-visible-but-disabled — which pattern?
- [ ] Page-reset behaviour: if user clears filters on page 3, does view snap back to page 1?
- [ ] "Clear all" placement: inline with filter chips, below, or in a filter bar?

**For Rathika:**
- [ ] Test cases: (a) clear all resets results, (b) result count updates to unfiltered total, (c) "Clear all" hidden when no filters active.
- [ ] Page-reset edge case: if user clears on page 3, does view reset to page 1? Needs AC before she can test.

**Outcome needed:** Trigger condition + page-reset behaviour locked. AC updated before Thu 11 Jun.

---

### 4. Sprint 3 carry-over risks (10 min)

**Context:** Sprint ends 14 Jun. 4 Done, 7 In Progress, 13 QA, 25 Backlog as of 5 Jun. These are the stories most likely to slip into S4.

| Ticket | Risk | Decision needed |
|--------|------|----------------|
| **OTEP-85** — Listing cards w/ real data | In Progress, unassigned. Rathika has 6 test cases ready but SGT timezone AC missing. Won't close QA without it. | Assign owner today. @Michelle to add timezone AC. |
| **OTEP-192** — Recurring ingestion job | 72/200 rows parsing only. Append-only (not upsert). AC not met. | Léo to confirm: is upsert next? Michelle to send corrected Excel or get failing rows from Léo. |
| **OTEP-348** — Scheduler & observability | Backlog, unowned. Split from OTEP-192 by Pow Hwee. | Assign owner + sprint slot before Thu 11 Jun or it floats indefinitely. |
| **OTEP-319** — Apply via FormSG | Still Backlog. Sprint goal floor — if not started by Mon, S4 goal needs fallback framing. | Confirm with Thomas: is this starting Mon? |
| **OTEP-276** — Design system spike | Shows In Progress but Pow Hwee moved to backlog in May. Likely zombie. | Confirm status: close or keep? |

**Outcome needed:** Carries confirmed, owners assigned, S4 goal framing locked before Thu 11 Jun planning.

---

### 5. Sprint 4 readiness check (10 min)

- **C@G payload confirmation** — has Pow Hwee's Slack reply come in? If yes, unblocks OTEP-87/88/89 estimation.
- **OTEP-374, 377, 378, 379** — all unowned. Assign BE owners before Sprint Planning or Thomas stalls week 1.
- **OTEP-318 go/no-go** — OTEP-289 spike output: is it closed? Decide if category filter goes into S4 or deferred.
- **OTEP-284 (Closing soon)** — any open questions before it goes into S4?

---

### 6. AOB (5 min)

- Any other QA blockers Rathika needs resolved before Sprint 3 closes (14 Jun)?
- Any design questions Amber needs answered before S4 design work starts?

---

## Pre-meeting checklist (Michelle — before Mon 8 Jun)

- [ ] Split OTEP-128 error AC → 500 vs 404
- [ ] Paste LifeSG reference into OTEP-326
- [ ] Add SGT timezone AC to OTEP-85
- [ ] Add filter-zero-results empty state to OTEP-268/325
- [x] Draft OTEP-88 rewrite — AC written, synced to Jira (2026-06-05). Two TBC items for Mon: AC4 fallback behaviour (Pow Hwee), AC2 badge spec (Amber).
- [ ] Check if C@G payload Slack reply received from Pow Hwee (Slack sent 2026-06-05)
- [ ] Churn out listing + detail page edge case answers for Amber discussion

---

*Created 2026-06-05 · Feeds into Sprint 4 Planning Thu 11 Jun*
