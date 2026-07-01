# OTEP-281: [FE] Opportunity listing — data fetching loading state

**Type:** Story

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

---

## Description

**User story:**
As an officer, I want to see a loading indicator while the opportunities listing is fetching data, so I know the page is working and don't think it's broken or empty.

**Acceptance Criteria:**

1. When the listing page initiates a data fetch, a spinner is displayed immediately — the officer never sees a blank page or an empty card grid mid-load.
2. The spinner is shown for the full duration of the fetch. It is replaced by the card grid on success, or the error state (OTEP-268) on failure.
3. If the fetch resolves in under 300ms, the spinner may not be visible — no flash or flicker is introduced.
4. Card heights are uniform once the grid renders. If optional fields are absent (e.g. closing date, agency icon), the card layout does not collapse or shift — empty space is preserved.
5. Skeleton loading (per-card placeholder animation) is not in scope. Spinner only, consistent with pagination loading pattern.

**Out of scope:**

- Per-card loading states (not technically feasible with single API call architecture)
- Skeleton/shimmer animation
- Partial load states (covered and intentionally removed in OTEP-268)

**Dependencies:** OTEP-268 must be closed first — confirm no overlap on spinner behaviour before building.

**Notes for engineer:** Follow the spinner pattern already used on filter/pagination transitions. Reference `filters.md` row 2: "Simple spinner/progress indicator during page transitions (skeleton loading deferred)."

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-07-01*
