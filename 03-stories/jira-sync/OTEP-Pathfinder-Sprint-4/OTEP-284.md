# OTEP-284: "Closing soon" label on cards and detail page

**Type:** Story

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

---

## Description

**User story:** As an officer, I want to see a "Closing soon" label on opportunities that are about to close, so that I can prioritise applications before I miss the window.

**Decision (resolves Pow Hwee's conflict flagged 2026-05-18):**

- OTEP-85 visibility rule = show all opportunities where `closing_date > now` (strictly in the future). The 7-day rule is NOT a visibility filter.
- This ticket owns the "Closing soon" badge only — it appears when `closing_date` is within 7 days from today and strictly in the future.
- Closed/expired hiding is fully owned by OTEP-85 and OTEP-362. No duplication here.

---

## Acceptance Criteria

1. A "Closing soon" badge is displayed on the opportunity card and detail page when the closing date is within 7 calendar days from today and strictly in the future (i.e. `0 < days_remaining <= 7`).
2. The badge is not shown for evergreen opportunities (nil closing date) — they have no deadline.
3. The badge is not shown for opportunities closing more than 7 days away.
4. The badge text reads "Closing soon" — design treatment per Amber's spec.
5. The badge appears in the same position on both the listing card and the detail page header.
6. The 7-day threshold is calculated server-side and returned in the API response — the FE does not compute it independently from the closing date.

**Out of scope:**

- Hiding closed/expired opportunities — owned by OTEP-85 and OTEP-362
- Exact countdown ("Closes in 3 days") — badge label only for MVP

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---

*Synced from Jira: 2026-06-04 — relocated from Backlog (added to Sprint 4 / Sprint 34618 in Jira).*

*Synced from Jira: 2026-06-10*
