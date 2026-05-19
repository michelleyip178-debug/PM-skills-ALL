# Story Readiness Board

> **Superseded for Sprint 2+ by [sprint-checklists.md](../sprint-checklists.md)** — that file has per-story grooming readiness, DoR blockers, and must-have/good-to-have tiering. This file is kept for reference but no longer actively maintained.

> Sprint 2 scope reshuffled 2026-05-14: **4 stories** (OTEP-85 listing, OTEP-267 pagination, OTEP-268 states, OTEP-128 detail page) + carry-overs. OTEP-129 absorbed into OTEP-85. OTEP-86/US-05 deferred to Sprint 3. OTEP-128 repurposed from "type badge" to "detail page."

**Current sprint:** Sprint 1 (May 4–15) — Auth + Data Infrastructure
**Planning horizon:** Sprint 2 + Sprint 3
**Updated:** 2026-05-14 (scope note only — detail in sprint-checklists.md)

---

## ID Reconciliation

Full mapping between PRD IDs, Jira/one-pager IDs, and sprint-allocation IDs lives in [story-id-map.md](../../03-stories/story-id-map.md). This board uses PRD numbering (US-XX).

---

## Sprint 2 (May 18–29): Listing Hub

**Goal:** Officers can browse and filter every OTG opportunity on one authenticated page, newest first, published-only. (No ringfencing, no apply flow, no C@G — Sprint 3+.)

| New ID | Story | Pipeline Stage | Design | API Contract | Blockers | Owner |
|--------|-------|---------------|--------|-------------|----------|-------|
| OTEP-85 | View all opportunities in one place | Draft | Amber — card designs due 15 May | Pow Hwee — listing endpoint; needs OTG field mapping from Rama | Pipeline must deliver real data by 12 May; `is_published` (#4) | Michelle |
| OTEP-86 | Filter opportunities by type | Draft | Amber — filter UI pattern not yet chosen | Filter/sort query params | Filter UI pattern (Amber); Secondment affects option list (Jacky) | Michelle |
| OTEP-128 | ~~Identify opportunity type on card~~ → **View opportunity detail page** (repurposed 2026-05-14) | DoR met | Amber's detail page design finalised | `GET /opportunities/:id` (Pow Hwee) | Type badge absorbed into OTEP-85. Detail in [otg-lifecycle.md](../../03-stories/otep-stories/otg-lifecycle.md) | Michelle |
| OTEP-129 | ~~Sort by posting date~~ — **absorbed into OTEP-85** (2026-05-14). Sort, interleave, "Closing soon" label. | Closed | — | — | — | — |
| US-05 | Clear filters and reset view | Draft | "Clear all" + active-filter indicators (Amber) | None | Depends on OTEP-86 existing | Michelle |

**Design dependency:** Amber's Hub UI + card designs need to be final by end Sprint 1 (Fri 15 May) for Sprint 2 stories to be refinable.

**Data dependency:** OTG file import (Excel → OTEP DB) must be delivering records. OTG has no API (decided 2026-05-14).

### What needs to happen this week (Sprint 1 week 2)

**Write:**
- [ ] Write missing story: OTG → OTEP file import (Excel import frequency, schema mapping, error handling) — scoping gap #1
- [ ] Write missing story: C@G → OTEP data ingestion (method, schema, refresh cadence) — scoping gap #2
- [ ] Refine AC for OTEP-85, OTEP-86, OTEP-128, OTEP-129 to groom-ready standard

**Validate:**
- [ ] Review Amber's Hub UI + card designs against OTEP-85, OTEP-86, OTEP-128 AC
- [ ] Validate categorisation hybrid model with Amber (design feasibility) — impacts OTEP-86
- [ ] Confirm OTG date field with Rama (impacts OTEP-129 sort logic)

**Prep:**
- [ ] Run `/groom-prep` before Tuesday internal groom
- [ ] Prepare Sprint 2 backlog grooming — OTEP-85, OTEP-86, OTEP-128, OTEP-129 need estimation

---

## Sprint 3 (Jun 2–13): Deep Discovery

**Goal:** Officers see personalised, searchable results and can drill into full opportunity details.

| New ID | Story | Pipeline Stage | Design | API Contract | Blockers | Owner |
|--------|-------|---------------|--------|-------------|----------|-------|
| OTEP-127 | Ringfencing (filter by officer's POCDEX data) | Draft | Needs ringfencing UI states (Amber) | Eligibility service (Pow Hwee) | POCDEX field mapping for filtering — which fields drive eligibility? | Michelle |
| OTEP-87 | View OTG opportunity details | Draft | Amber — Sprint 2 design work (detail page) | Detail page API: which fields, what shape? (Pow Hwee) | Depends on OTEP-85 being built (navigates from card) | Michelle |
| OTEP-89 | View C@G opportunity summary on OTEP | Draft | Part of detail page design (Amber) | C@G data schema — what metadata do we get? | C@G ingestion method must be confirmed (Pow Hwee, end Sprint 1) | Michelle |
| OTEP-133 | Redirect to Careers@Gov to apply | Draft | "Leaving OTEP" interstitial (Amber) | Deep-link URL format (C@G team) | C@G deep-link URL pattern needed | Michelle |
| — | Search (keyword search across listings) | Not written | Search interaction patterns (Amber, Sprint 2) | Elasticsearch query layer (Pow Hwee) | Search indexing infra spike needed before Sprint 3 | Michelle |

**Note:** Search doesn't have a story in the new index — it's folded into OTEP-85 AC. Consider whether it needs its own story given it's a Sprint 3 build item with separate design + backend work. **Decision needed.**

### What needs to happen in Sprint 2

- [ ] Write Sprint 3 story AC to draft-ready by Sprint 2 week 1 (for internal groom)
- [ ] Confirm POCDEX fields that drive ringfencing (OTEP-127 blocker)
- [ ] Get detail page designs from Amber (Sprint 2 design track)
- [ ] Confirm C@G deep-link URL pattern with C@G team
- [ ] Decide: does search need its own user story, or is it AC within OTEP-85?
- [ ] Search indexing spike — Pow Hwee to confirm infra readiness

---

## Sprint 4 (Jun 16–27): Application Layer — Lookahead

Not actively managing yet. Candidate stories for awareness:

| New ID | Story | Notes |
|--------|-------|-------|
| OTEP-130 | Apply to OTG via FormSG | Core action. FormSG webhook + missing link handling. |
| US-10 | Receive application confirmation | Depends on FormSG webhook working. |
| OTEP-133 | Redirect to Careers@Gov to apply | If not completed in Sprint 3 (cascade risk). |
| OTEP-88 | Understand difference between OTG and C@G flows | Button labels, visual cues. |

---

## Pipeline Stage Key

| Stage | What it means | Who's working |
|-------|--------------|---------------|
| **Not written** | Story doesn't exist yet | Michelle needs to draft it |
| **Draft** | Story + AC written in group file | Michelle |
| **Groom-ready** | AC complete, edge cases documented, priority clear | Ready for internal groom |
| **In refinement** | Amber designing, Pow Hwee reviewing API, AC being updated | Parallel tracks |
| **DoR met** | Design linked, API contract done, feature flag identified, subtasks created | Ready for sprint planning |
| **Committed** | In the sprint, assigned to an engineer | Engineering |

---

## How to Use This File

1. **Before internal groom (Tue week 1):** Check next sprint's stories. Are they all at "Groom-ready" or better?
2. **Before backlog groom (Thu week 2):** Check next sprint's stories. Are they all at "In refinement" or better?
3. **At sprint boundary:** Shift the board — current "Sprint 3" becomes "Sprint 2", add new Sprint 4 lookahead.
4. **When a story advances:** Update its Pipeline Stage and clear resolved blockers.

This file pairs with `/groom-prep` — run that command for detailed readiness scoring before any grooming session.
