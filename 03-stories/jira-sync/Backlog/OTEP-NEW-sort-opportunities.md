# [NEW TICKET]: [FE] Sort Opportunities (Posted Date / Closing Date)

**Type:** Story

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

**Suggested Sprint:** Sprint 4

---

## Description

**User story:**
As an officer, I want to sort the opportunities listing by posted date or closing date, so that I can find the newest opportunities or prioritise ones closing soon.

**Acceptance Criteria:**

1. A "Sort by" control is displayed in the filter sidebar with two options: "Posted date" and "Closing date."
2. Default sort is "Posted date" (newest first) — consistent with current listing behaviour (OTEP-85 AC: sorted by posting date, descending).
3. Selecting "Closing date" re-sorts results ascending (soonest closing first) so officers can prioritise urgent opportunities.
4. The selected sort option persists while the officer navigates between pages — changing page does not reset the sort.
5. Sort and type filters (OTEP-86) and keyword search compose together — all three apply simultaneously.
6. Evergreen opportunities (nil closing date) are shown last when sorting by closing date — they have no deadline and should not crowd out time-sensitive listings.
7. The sort control is visible on all screen sizes — it does not collapse or become inaccessible on smaller viewports.

**Out of scope:**
- Sort by relevance or match score (deferred to R1 competency matching)
- Sort by agency name or opportunity type
- Saving sort preference across sessions

**Dependencies:**
- OTEP-85 (default posting-date sort already implemented — this ticket adds the sort toggle UI and closing-date sort)
- OTEP-86 (filters) — sort must compose with active filters
- BE: listing API must accept a `sort` param (`posted_date` | `closing_date`) and return results in correct order

**Notes for engineer:** Confirm with Léo whether the listing API already supports a `sort` param or if that needs to be added. Evergreen (nil closing date) sort behaviour needs explicit BE handling — confirm how nil dates are ordered in the closing-date sort query.
