# User Stories: Opportunity Discovery & Filters

**Epic:** Opportunities (Epic 4)
**One-pager:** _TODO: Confluence link_
**Status:** Sprint 2 — ready for grooming
**Sprint 2 scope:** OTG data only (STIPs, Gigs, SJRs, Internal Jobs). C@G data lands in a later sprint.

---

## Sprint 2 Stories

### Sprint 2: 5 stories (reconciled against Jira board 2026-05-15)

OTEP-85 is the rendering foundation — all other stories depend on it. OTEP-285 was split from OTEP-85 (renamed from OTEP-85b on 2026-05-15 when ticketed) to isolate click-through/state-preservation behaviour into an independently shippable (and cuttable) unit. **OTEP-85a ("Closing soon" label) was re-absorbed into OTEP-85 on 2026-05-15.** OTEP-276 (design system spike, Thomas) added 2026-05-15. OTEP-268 deferred / unticketed.

**Sprint 2 boundary (applies to all six):**
- OTG data only — no C@G this sprint
- Desktop only — mobile/tablet comes later
- No apply flow — apply actions are Sprint 3 (OTEP-319)
- No filters or search — Sprint 3
- Auth states (logged-out, session expired) handled by OTEP-71 family, not these stories

**Dependency chain:**
```
OTEP-85 (foundation — now includes "Closing soon" label) ──┬──> OTEP-267 (pagination)
                                                           ├──> OTEP-128 (detail page) ──> OTEP-285 (click-through + state)
                                                           └──> OTEP-285 also depends on OTEP-85
OTEP-276 (design system spike, Thomas) — parallel work, informs FE direction
```

**Cut-line if Sprint 2 slips:**
1. First cut: OTEP-285 good-to-have ACs (refresh/share URL persistence) — journey degrades but works
2. Do not cut: OTEP-85, OTEP-128, OTEP-267 — these ARE the journey. OTEP-276 spike runs in parallel.
3. OTEP-268 (empty/error/partial) is already out of Sprint 2 (deferred 2026-05-15)

---

### OTEP-85: Display open opportunities as cards

> **Updated 2026-05-15:** The rendering foundation. All other Sprint 2 stories depend on this. **"Closing soon" label re-absorbed (was OTEP-85a, now part of OTEP-85).** Click-through + state preservation split to OTEP-285 (was OTEP-85b until ticketed 2026-05-15).

**As an** officer,
**I want to** see opportunities displayed as cards on the listing page,
**So that** I can scan what's available across all opportunity types in one place.

**Acceptance Criteria:**

*Must-have:*
- [ ] When I open the Opportunities page, I see opportunity cards
- [ ] Each card shows me: the opportunity title, which agency posted it, when it was posted (e.g. "12 May 2026"), and what type of opportunity it is
- [ ] I only see opportunities that are still accepting applications (closing date hasn't passed — an opportunity that closes today is still visible)
- [ ] The most recently posted opportunities appear first
- [ ] All types of opportunities are mixed together by date — they're not grouped into separate sections
- [ ] On desktop, I see 15 cards arranged in 3 columns
- [ ] While the page is loading, I see a spinner — not a blank page
- [ ] I can tell what type each opportunity is without relying on colour alone — there's a clear text label

*Good-to-have:*
- [ ] Long titles wrap to a maximum of 2 lines and trail off with "..."
- [ ] The agency's ministry icon appears next to the agency name
- [ ] The card shows whether the opportunity is full-time, part-time, or project-based
- [ ] If two opportunities were posted on the same day, they appear in a consistent order each time I visit
- [ ] If an opportunity has an unexpected type, the card still shows up with a generic label instead of breaking

*Not in scope:* Filtering. Sorting in different directions. Mobile or tablet layouts. Click-through to detail (OTEP-285).
*Now in scope (re-absorbed 2026-05-15):* "Closing soon" label on cards (was separate OTEP-85a).

**Field rendering rules:**

A card needs all mandatory fields to show up. If any mandatory field is missing, the card doesn't appear — the team logs it for review. Officers aren't shown a warning (partial-load handling removed from OTEP-268 per 2026-05-19 refinement — Tailwind stack renders all-or-nothing).

| Field | Required? | If missing |
|---|---|---|
| Title | Yes | Card doesn't show |
| Agency | Yes | Card doesn't show |
| Type | Yes | Card doesn't show |
| Posting date | Yes | Card doesn't show |
| Closing date | Yes (drives visibility) | Card doesn't show |
| Whether it's full-time/part-time/project | No | That info is hidden; card still shows |
| Ministry icon | No | Icon hidden; card still shows |

**Subtasks:**

| # | Task | Track | Notes |
|---|------|-------|-------|
| 1 | Listing API: paginated, sorted by posting date, only open opportunities | Backend | API contract sync Fri 15 May |
| 2 | Card component: title, agency, type label, posting date | Frontend | Builds on Amber's design |
| 3 | Wire listing page to API + render grid | Frontend | Builds on OTEP-170 base layout |
| 4 | Feature flag: `opportunities_hub` | Frontend | Flag off = nav link hidden |
| 5 | Loading indicator while data fetches | Frontend | Confirm design with Amber |
| 6 | Test: only open opportunities shown, newest first | Test | |
| 7 | Test: card with missing optional fields still renders | Test | |

**Design dependency:** ~~Amber's card layout~~ — finalised 2026-05-13
**Data dependency:** OTG file import (Excel → OTEP DB). Depends on #24 (which reports) and OTEP-192.

**Priority:** MVP — **must ship first** — blocks all other Sprint 2 stories.

**Risks:**
- OTG file import not delivering testable data by Sprint 2 W1 — blocks everything.
- Loading indicator AC is new — confirm with Amber it's in the design.

---

### ~~OTEP-85a: "Closing soon" label on cards and detail page~~ — **RE-ABSORBED INTO OTEP-85 (2026-05-15)**

> **Re-absorbed 2026-05-15.** "Closing soon" label is now part of OTEP-85. The ACs below are preserved here for grooming reference — they continue to apply, but as part of OTEP-85's scope, not a separate ticket.
>
> **Created 2026-05-14** — originally split from OTEP-85 (kept for history).

**As an** officer,
**I want to** see at a glance which opportunities are closing soon,
**So that** I can prioritise the ones I might miss if I wait.

**Acceptance Criteria:**

*Must-have:*
- [ ] If an opportunity's closing date is within 7 days of today, the card shows a "Closing soon" label
- [ ] If the closing date is more than 7 days away, no label appears
- [ ] An opportunity that closes today still shows the label (today is within 7 days)
- [ ] The same label appears on the detail page (OTEP-128) when the opportunity is within 7 days
- [ ] The label is visually distinct from the type label — I can tell them apart at a glance
- [ ] The label includes text (not just a coloured dot or badge) so it's readable without relying on colour alone

*Good-to-have:*
- [ ] The label appears in a consistent position on every card (per Amber's design)

*Not in scope:* Sorting or filtering by "Closing soon." Email reminders. Custom thresholds (7 days is locked).

**Edge cases:**
- Opportunity closes today → label still appears (within 7 days)
- Opportunity closed yesterday → not shown on listing (OTEP-85 visibility rule)

**Depends on:** OTEP-85 (cards must exist), OTEP-128 (detail page must exist)
**Design dependency:** Amber's "Closing soon" label — finalised 2026-05-13

**Priority:** MVP — but safe to cut first if Sprint 2 slips

---

### OTEP-285: Click-through to detail and return-to-page state

> **Created 2026-05-14** — split from OTEP-85. Isolates click-through and state preservation into one story because they share one architectural concern (how listing state is persisted). **Highest-risk story in Sprint 2.**

**As an** officer,
**I want to** click into an opportunity and come back to where I was when I'm done,
**So that** I can browse without losing my place.

**Acceptance Criteria:**

*Must-have:*
- [ ] When I click an opportunity card, I'm taken to the detail page for that opportunity
- [ ] When I go back to the listing — using either the "Back to opportunities" link or the browser back button — I land on the page I was viewing, not page 1
- [ ] When I move to the next page, the ordering stays the same — opportunities don't repeat or reshuffle

*Good-to-have:*
- [ ] If I refresh the browser while on page 3, I stay on page 3
- [ ] If I share the listing link while on page 3, the other person also lands on page 3

*Not in scope:* Remembering my scroll position. Remembering filters or search. Remembering state across browser sessions or tabs.

**Edge cases:**
- I close the tab and come back later → I start from page 1 (no cross-session memory)
- I'm on page 5 of 5, an opportunity closes while I'm reading detail, I click back → I land on the new last page, not an empty page 5
- Both "Back to opportunities" and the browser back button must work — flag if eng proposes only one

**Depends on:** OTEP-85 (listing), OTEP-128 (detail page), OTEP-267 (pagination)

**Priority:** MVP — but **highest-risk story in Sprint 2.** Forces an architectural decision about how page state is preserved. Discuss at tomorrow's API contract sync.

**Fallback if it slips:** Ship without return-to-same-page — officers reset to page 1 every time. Not ideal, but the journey still works. Confirm with Adrian if it comes to that.

**Risks:**
- State persistence architecture — URL params vs client state vs session storage. Needs a decision at the contract sync.
- Long dependency chain: needs OTEP-85, OTEP-128, OTEP-267 all in place to test. Realistically picks up Day 5–6.

---

### OTEP-267: Pagination for the listing page

**As an** officer,
**I want to** page through all available opportunities,
**So that** I can find listings beyond the first screen.

**Acceptance Criteria:**

*Must-have:*
- [ ] If there are more than 15 opportunities, I can move to the next page to see more
- [ ] I can go back to the previous page to see earlier results
- [ ] I can see which page I'm on and how many pages there are (e.g. “Page 1 of 5” or “Showing 1–15 of 96”)
- [ ] When there are no opportunities to show, the page controls disappear — I don't see an empty “Page 1 of 0” or a non-functional Next button

*Good-to-have:*
- [ ] While the next page is loading, I see a spinner so I know it's working
- [ ] The page controls look and feel consistent with the rest of the platform

*Not in scope:* Sharing a link to a specific page (that's in OTEP-285's good-to-have). Placeholder loading animations. Infinite scroll.

**Edge cases:**
- I'm on the last page and some opportunities close → next time I load, I see the correct last page even if the total shrunk
- Zero results → page controls hidden entirely (empty state deferred to Sprint 3 with filters)
- Exactly 15 opportunities (1 full page) → Next and Previous are visible but disabled

**Subtasks:**

| # | Task | Track | Notes |
|---|------|-------|-------|
| 1 | Pagination controls component (per Amber's finalised design) | Frontend | Pattern confirmed. |
| 2 | Simple spinner/progress indicator during page transitions (skeleton loading deferred) | Frontend | Follow LifeSG patterns. |
| 3 | Wire pagination params to listing API (page, per_page) | Frontend | No deep-linking — URL params not required for pagination. |
| 4 | Test: Pagination with 50+ records; boundary pages (first, last, middle); no duplicates across pages | Test | |

**Design dependency:** ~~Amber's pagination pattern~~ — finalised 2026-05-13
**Depends on:** OTEP-85 (listing API must exist). Can be developed in parallel with OTEP-268.

**Priority:** MVP

**Risks:**
- If OTEP-85 slips, this is blocked. No independent path.

---

### OTEP-268: Error and empty states for the listing — **re-added to Sprint 2 (2026-05-18)**

> **Re-added 2026-05-18 by Pow Hwee** — overrides May 15 deferral. ACs refined 2026-05-19 [PH]: partial-load AC removed (Tailwind stack fetches all-or-nothing); good-to-haves (truncation, correlation IDs) spun to separate backlog tickets.

**As an** officer,
**I want to** see clear guidance when the opportunities page is empty or fails to load,
**So that** I'm not confused by a blank or broken page.

**Acceptance Criteria:**

*Must-have:*
- [ ] **When the page loads successfully but there are no opportunities:** I see a heading "No opportunities available right now" and body text "Check back soon — new opportunities are posted regularly." No retry button — this is a valid result, not an error.
- [ ] **When the page fails to load:** I see a heading "We couldn't load opportunities" and body text "Something went wrong on our end. Please try again." with a "Try again" button that re-fetches. The page doesn't show a blank screen.

*Not in scope:* Partial-load handling (not possible with current Tailwind stack — API call either succeeds fully or fails). Automatic retries. Agency name truncation (separate backlog ticket). Correlation IDs in error logs (separate backlog ticket).

**Spun-out backlog items (low priority — do not block this story):**
- Long agency name truncation with hover tooltip → new low-priority backlog ticket
- Correlation ID logging on error → new low-priority backlog ticket

**Design decisions:**
1. One simple error message covers all failure types — officers don't need the technical reason.
2. Empty state has no retry — it's a valid system state, not a failure.
3. Professional, government tone.

**Subtasks:**

| # | Task | Track | Notes |
|---|------|-------|-------|
| 1 | Error state component + "Try again" re-fetch handler | Frontend | |
| 2 | Empty state component (no retry) | Frontend | |
| 3 | Test: error state on 500 + "Try again" re-fetches successfully | Test | |
| 4 | Test: empty state renders when API returns empty array | Test | |

**Design dependency:** ~~Amber's empty state + error state designs~~ — finalised 2026-05-13
**Depends on:** OTEP-85 (card component must exist). Can be developed in parallel with OTEP-267.

**Priority:** MVP

**Risks:**
- Low risk if OTEP-85 ships. No remaining blockers.

---

### ~~OTEP-128~~ — Repurposed (2026-05-14)

OTEP-128 was "Identify opportunity type on card." That functionality is now **absorbed into OTEP-85** (type badge is a must-have AC on the card). OTEP-128 has been **repurposed as the Detail Page story** — see [otg-lifecycle.md](otg-lifecycle.md).

---

### ~~OTEP-129~~ — Absorbed into OTEP-85 (2026-05-14)

Sort by posting date, "Closing soon" label, interleave-by-date, and stable ordering are all now ACs on OTEP-85. OTEP-129 is closed.

---

## Sprint 3 Stories

### OTEP-86: Filter by opportunity type
**Status:** Sprint 3 (deferred from Sprint 2, 2026-05-14). **In Jira Sprint 3 ✔**
**When:** Sprint 3.

**Acceptance Criteria:** [DEFERRED to Sprint 3]

*Must-have:*
- [ ] I can filter by opportunity type: Internal Job, SJR, or STIP/Gig. Secondment shows under SJR. [ASSUMPTION: Secondment classification resolved 2026-05-13 — subsumed under SJR]
- [ ] I can select more than one type at once — selecting two types shows opportunities matching either type.
- [ ] If I haven't selected any filter, all opportunity types are shown by default.
- [ ] If my selected filters return no results, I see "No opportunities found" — not a blank list.

*Good-to-have:*
- [ ] If I select filters and then press the browser back button, my filter selections are preserved. [ASSUMPTION: URL query params used for filter state]
- [ ] Active filters are visually distinct — I can see at a glance which types I've selected.
- [ ] If there are no results, I see a prompt to broaden my filters.

*Not in scope:* Filter counts per type. Category/function filter (US-03). Competency filter.

### OTEP-317: Clear filters and reset view *(was US-05)*
**Status:** Sprint 3. **Ticketed OTEP-317 (2026-05-21 sync) ✔**

**Acceptance Criteria:** [Sprint 3]

*Must-have:*
- [ ] If one or more filters are active, I can see a "Clear all" option.
- [ ] When I click "Clear all", all my filter selections are removed and the full listing is shown again.
- [ ] If no filters are active, "Clear all" is hidden.

*Good-to-have:*
- [ ] "Clear all" also resets the URL back to the default unfiltered state.
- [ ] "Clear all" takes me back to page 1.

### OTEP-318: Filter opportunities by category *(was US-03)*
**Status:** Sprint 3 — conditional on OTEP-289 spike output. **Ticketed OTEP-318 (2026-05-21 sync) ✔. No Jira description yet — ACs below to be added.**
**When:** Sprint 3 if OTEP-289 spike is green.

### US-07: Persist filter selections across sessions
**Status:** R1. Within-session persistence via URL params (OTEP-86) is sufficient for MVP.

---

## Open Questions (Sprint 2 relevant)

1. ~~Categorisation model~~ — **not Sprint 2.** Deferred with US-03.
2. ~~**Filter UI pattern**~~ — **resolved 2026-05-13:** Amber's designs finalised for Sprint 2 and 3.
3. ~~Filter counts~~ — recommend skip for Sprint 2, revisit later
4. ~~Default sort~~ — **resolved:** newest first (OTEP-129 / OTEP-85)
5. ~~Search vs filter~~ — search is MVP but **not Sprint 2**
6. ~~**Mobile filter behavior**~~ — **resolved 2026-05-13:** covered in Amber's finalised designs.
7. ~~`closing_date` vs `end_date`~~ — **resolved 2026-05-13:** `closing_date` = application closing date. "Closing soon" label now unblocked.
8. ~~Secondment classification~~ — **resolved 2026-05-13:** subsumed under SJR.
9. ~~`is_published` field~~ — **resolved 2026-05-13:** field doesn't exist. Visibility = `closing_date` > today.
10. ~~**Pagination pattern**~~ — **resolved 2026-05-13:** confirmed in Amber's finalised designs.
11. ~~**OTEP-129 overlap**~~ — **resolved 2026-05-14:** absorbed into OTEP-85. Sort, interleave, "Closing soon" label all moved to OTEP-85 ACs.

## Assumptions

- OTG file import (Excel → OTEP DB) delivers structured records with at minimum: type, title, agency, posting_date, closing_date
- No ringfencing in Sprint 2 — all officers see all OTG listings (OTEP-127 is Sprint 3)
- Detail page IS in Sprint 2 (OTEP-128 repurposed as detail page, 2026-05-14). OTEP-87 enhances it in Sprint 3.
- Visibility rule: `closing_date` > today (no `is_published` field — resolved 2026-05-13)

## Sprint 2 DoR Blockers

- [x] ~~Amber's card + filter UI + pagination + empty/error state designs finalised~~ — **resolved 2026-05-13**
- [x] ~~Rama confirms `closing_date` vs `end_date` (open item #3)~~ — resolved 2026-05-13
- [x] ~~Rama confirms `is_published` field (open item #4)~~ — resolved 2026-05-13: doesn't exist
- [x] ~~Jacky confirms Secondment classification (open item #12)~~ — resolved 2026-05-13: SJR
- [ ] OTG file import testable with real Excel data — depends on open item #24 (which reports to ingest) and OTEP-192 (import job)
- [ ] Listing-endpoint API contract documented (Pow Hwee) — OTEP-85 subtask #1. Internal API (frontend ↔ backend), separate from OTG ingestion.
- [x] ~~Sort key confirmed~~ — `posting_date`, newest first (Michelle)

---

*Updated: 2026-05-21 — Sprint 3 Jira sync: US-05 → OTEP-317, US-03 → OTEP-318 (ticketed; no Jira description yet). OTEP-268 re-added to Sprint 2 (Pow Hwee, 2026-05-18). Deferred section header updated to Sprint 3 (now current). OTEP-319 reference added for apply flow.*
