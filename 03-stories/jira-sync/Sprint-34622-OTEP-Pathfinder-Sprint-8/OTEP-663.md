# OTEP-663: [BUG] Open issues for opportunities listing page

**Status:** Done
**Assignee:** Thomas Huchedé
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 8 (34622)

---

## Description

DefectId Defect Description Screenshot Severity Status 1 Issue:  When an opportunity is missing the optional  ministry_logo  field, a broken image icon is displayed on the card instead of failing gracefully.   Expected Result:  The card should display neatly without broken layouts or missing image icons when optional fields are null.  FIXED A default logo is added  ISSUE   Low CLOSED 2 Issue:  The visual tag for "SJR" (Short-Term Job Role) opportunities fails to display on the respective opportunity cards in the UI.   Expected Result:  The card should correctly display the respective visual tag (e.g., "[SJR]" pill/badge) without layout distortion.   Medium NA (out of scope for MVP) 3 Issue:  The "Closing soon" label fails to display on opportunity cards closing  tomorrow  (e.g., Today: 26-06-2026, Closing: 27-06-2026).   Expected Result:  The "Closing soon" label must be displayed on both the card and detail page for any opportunity closing in 7 calendar days or less. FIXED for listing page and details page when closing date = tomorrow 08-08-2026 the opportunity is closed   https://qa.careercompass.gov.sg/opportunities/019fcb50-bb75-7cf5-bf1b-fb8879d49806?ms=search   ISSUE  Medium CLOSED 4 Issue:  Opportunities with a closing date of  today  is hidden from the listing grid.   Expected Result:  Opportunities closing today should consistently display on the grid with a "Closing today" badge.  FIXED for details page too OTG  C@G    FIXED for listing page  with closing_date = today 07/08/2026  FAILS  for detail page  https://qa.careercompass.gov.sg/opportunities/019fda70-ad4b-75cf-900c-b25baef91282?ms=search Medium CLOSED REOPEN 5 Issue:  Toggling the sort criteria to "Closing date" incorrectly sorts the grid to show the farthest closing dates first.   Expected Result:  The grid should instantly re-sort to display the nearest approaching deadlines first. FIXED     ISSUE  High CLOSED 6 Issue:  Opportunity cards missing the mandatory  posted_date  field ( null  value) incorrectly display a fallback Unix epoch date of "Posted on 1 Jan 1970".   Expected Result:  The card should  show  “Posted > 3 months ago”  for missing date for OTG ,  hides for C@G,  or the system should block the creation of opportunities missing this mandatory field.  (Ref: TC-3)  FIXED (And moved to the end of the list)   All the otg opportunities with posted-date listed first then cag opps that have posted-date = NULL  ISSUE  Medium CLOSED 7 For some  evergreen  and other opportunities,formSG URL is broken   id = 019f8dfd-77e5-78b9-9a01-6f21bbc695f3 FormSg URL is unavailable:  https://qa.careercompass.gov.sg/opportunities/019f8dfd-77e5-78b9-9a01-6f21bbc695f3?ms=searc Same issue     https://qa.careercompass.gov.sg/opportunities/019fcb50-bb79-74e7-9863-8b90c441bb90?ms=filter  NA

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Thomas Huchedé** (2026-08-13)
the fix for the closing date has been merged and a more recent commit as been deployed already in QA so you should be able to test it already

---
*Synced from Jira: 2026-08-19*
