# OTEP-663: [BUG] Open issues for competencies listing page

**Status:** To Do
**Assignee:** Thomas Huchedé
**Story Points:** N/A

---

## Description

DefectId Defect Description Screenshot Severity Status 1 Issue:  When an opportunity is missing the optional  ministry_logo  field, a broken image icon is displayed on the card instead of failing gracefully.   Expected Result:  The card should display neatly without broken layouts or missing image icons when optional fields are null.   Low OPEN 2 Issue:  The visual tag for "SJR" (Short-Term Job Role) opportunities fails to display on the respective opportunity cards in the UI.   Expected Result:  The card should correctly display the respective visual tag (e.g., "[SJR]" pill/badge) without layout distortion.   Medium OPEN 3 Issue:  The "Closing soon" label fails to display on opportunity cards closing tomorrow (e.g., Today: 26-06-2026, Closing: 27-06-2026).   Expected Result:  The "Closing soon" label must be displayed on both the card and detail page for any opportunity closing in 7 calendar days or less.  Medium OPEN 4 Issue:  Opportunities with a closing date of today is hidden from the listing grid.   Expected Result:  Opportunities closing today should consistently display on the grid with a "Closing today" badge.   Medium OPEN 5 Issue:  Toggling the sort criteria to "Closing date" incorrectly sorts the grid to show the farthest closing dates first.   Expected Result:  The grid should instantly re-sort to display the nearest approaching deadlines first.  High OPEN 6 Issue:  Opportunity cards missing the mandatory  posted_date  field ( null  value) incorrectly display a fallback Unix epoch date of "Posted on 1 Jan 1970".   Expected Result:  The card should either handle the missing date gracefully, or the system should block the creation of opportunities missing this mandatory field.  (Ref: TC-3)  Medium OPEN

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-07-10*
