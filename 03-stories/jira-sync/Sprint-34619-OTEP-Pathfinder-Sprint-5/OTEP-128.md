# OTEP-128: View opportunity detail page

**Status:** QA
**Assignee:** N/A
**Story Points:** 3

---

## Description

As an  officer,  I want to  view the full details of an opportunity on a dedicated page,  So that  I can decide whether to apply without leaving OTEP.  Acceptance Criteria The system must display a detail page containing the Title, Agency, Posting Date, Closing Date, Type, Description, "What you'll develop" text, and Commitment type. The system must format all dates in an absolute format (e.g., "12 May 2026"). The system must provide a clearly visible "Back to opportunities" link to return to the listing. The system must load the detail page correctly when accessed directly via a bookmark or shared URL. The system must display an "Opportunity not found" message with a link back to the listing if the provided opportunity ID is invalid. The system must style the Type label identically to how it appears on the listing card. The apply button will be disabled.  Edge cases (UX) Closed opportunity opened thru deep-link → page loads with "closed" notice, no apply action Broken / invalid link → "not found" message with link back to listing Missing optional field (e.g. no "what you'll develop" text) → that section hides, page doesn't show an empty header

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-334 | backend endpoint for opportunity detail | Done |
| OTEP-327 | Opportunity detail page using design system  | Done |
| OTEP-314 | Opportunity detail page consuming OTEP-295 response shape | Done |

---

## Latest Comments

**Rathika Ramalingam** (2026-06-04)
Test Cases:  Scenario 1: Navigating to the opportunity detail page  Given  a user is viewing the opportunities listing page When  the user clicks on an active opportunity card Then  the system navigates the user to the opportunity detail page And  the URL dynamically updates to include the specific opportunity ID (e.g.,  /opportunities/{id} ).  Scenario 2: Displaying core opportunity details Given  an opportunity is active  When  the user views the opportunity detail page Then  the UI renders the Title, Agency, Commitment type, Type pill and Closing date tag. And  the “About this opportunity” section, with "What you'll develop/gain" sub-section. Scenario 3: Formatting the posting date Given  an opportunity has a valid Posting Date timestamp When  the frontend renders the detail page Then  the date is formatted strictly in an absolute "DD Month YYYY" format (e.g., "Posted on 7 March 2026"). Scenario 4 : Navigating back to the listing via breadcrumb/link Given  a user is viewing the opportunity detail page When  the user clicks the "Back to opportunities" link (or "Jobs & Opportunities" breadcrumb) Then  the system navigates the user back to the opportunities listing page. Scenario 5: Direct URL access to a valid active opportunity Given  a user possesses a direct URL to a valid opportunity detail page When  the user accesses the URL directly via their browser (e.g., via a bookmark) Then  the system successfully fetches the data and renders the detail page. Scenario 6: Direct URL access to a closed opportunity Given  an opportunity has a Closing Date in the past When  a user accesses that specific opportunity's URL directly Then  the detail page loads successfully And  the UI displays a "closed" notice And  the Apply button is completely removed or hidden. Scenario 7: Direct URL access to an invalid opportunity ID Given  a user accesses a direct URL containing an opportunity ID that does not exist When  the system attempts to fetch the opportunity details Then  the system renders an "Opportunity not found" message And  provides a functioning link to return to the main listing page. Scenario 8: Job duration for short term jobs Given  an opportunity is classified with the Type "Gig" or "STIP" And  the backend API provides a valid start date and end date for the assignment When  the user views the opportunity detail page Then  the UI renders the job duration metadata alongside a calendar icon And  the duration is visually formatted strictly as "[Start Date] - [End Date]" (e.g., "1 Apr 2026 - 30 Jun 2026") And  the dates use the absolute format without zero-padding for single-digit days (e.g., "1 Apr", not "01 Apr") ?

---

**Pow Hwee TAN (PSD)** (2026-05-18)
OTEP-285 ACs (click-through to detail and return-to-page state) are folded into this story: Card click navigates to this detail page. "Back to opportunities" preserves page position via URL query params (?page=N). Consistent ordering guaranteed by Posting Date + ID tie-breaker in OTEP-85. Suggest also splitting the error handling into two distinct ACs: If the opportunity ID does not exist, display "Opportunity not found" with a link back to the listing. If the system cannot load the opportunity (e.g. server error), display a generic error message with a retry option. The AC "display a clear This opportunity is closed notice" overlaps with OTEP-129 which owns open/closed labelling. Suggest removing it from this ticket to avoid double-counting.

---

**Amber Tong** (2026-05-13)
figma link  here
