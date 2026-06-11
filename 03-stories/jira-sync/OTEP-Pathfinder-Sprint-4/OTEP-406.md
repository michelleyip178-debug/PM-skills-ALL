# OTEP-406: [FE] Sort Opportunities (Posted Date / Closing Date)

**Type:** Story

**Status:** Backlog

**Assignee:** N/A

**Story Points:** 2

**Sprint:** OTEP-Pathfinder Sprint 4

---

## Description

**User story:**
As an officer, I want to sort the opportunities listing by posted date or closing date, so that I can find the newest opportunities or prioritise ones closing soon.

**Acceptance Criteria:**

1. A "Sort by" control is displayed in the filter sidebar with two options: "Posted date" and "Closing date."
2. Default sort is "Posted date" (newest first) — consistent with current listing behaviour (OTEP-85).
3. Selecting "Closing date" re-sorts results ascending (soonest closing first).
4. The selected sort option persists while the officer navigates between pages — changing page does not reset the sort.
5. Sort and type filters (OTEP-86) and keyword search (OTEP-405) compose together — all three apply simultaneously.
6. Evergreen opportunities (nil closing date) are shown last when sorting by closing date.
7. The sort control is visible on all screen sizes — it does not collapse on smaller viewports.

**Out of scope:**
- Sort by relevance or match score (deferred to R1)
- Sort by agency name or opportunity type
- Saving sort preference across sessions

**Dependencies:**
- OTEP-85 (default posting-date sort already implemented — this ticket adds the sort toggle UI)
- OTEP-86 (filters) — sort must compose with active filters
- BE: listing API must accept a `sort` param (`posted_date` | `closing_date`)

**Notes for engineer:** Confirm with Léo whether the listing API already supports a `sort` param. Nil closing date sort behaviour needs explicit BE handling — confirm how nil dates are ordered in the closing-date sort query.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-06-11*
