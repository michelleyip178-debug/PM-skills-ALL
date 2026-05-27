# OTEP-128: View opportunity detail page

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

As an  officer,  I want to  view the full details of an opportunity on a dedicated page,  So that  I can decide whether to apply without leaving OTEP.  Acceptance Criteria The system must display a detail page containing the Title, Agency, Posting Date, Closing Date, Type, Description, "What you'll develop" text, and Commitment type. The system must format all dates in an absolute format (e.g., "12 May 2026"). The system must provide a clearly visible "Back to opportunities" link to return to the listing. The system must load the detail page correctly when accessed directly via a bookmark or shared URL. The system must display an "Opportunity not found" message with a link back to the listing if the provided opportunity ID is invalid. The system must style the Type label identically to how it appears on the listing card. The apply button will be disabled.  Edge cases (UX) Closed opportunity opened thru deep-link → page loads with "closed" notice, no apply action Broken / invalid link → "not found" message with link back to listing Missing optional field (e.g. no "what you'll develop" text) → that section hides, page doesn't show an empty header

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-327 | Opportunity detail page using design system  | Backlog |
| OTEP-334 | backend endpoint for opportunity detail | QA |
| OTEP-314 | Opportunity detail page consuming OTEP-295 response shape | In Progress |

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-05-18)
OTEP-285 ACs (click-through to detail and return-to-page state) are folded into this story: Card click navigates to this detail page. "Back to opportunities" preserves page position via URL query params (?page=N). Consistent ordering guaranteed by Posting Date + ID tie-breaker in OTEP-85. Suggest also splitting the error handling into two distinct ACs: If the opportunity ID does not exist, display "Opportunity not found" with a link back to the listing. If the system cannot load the opportunity (e.g. server error), display a generic error message with a retry option. The AC "display a clear This opportunity is closed notice" overlaps with OTEP-129 which owns open/closed labelling. Suggest removing it from this ticket to avoid double-counting.

---

**Amber Tong** (2026-05-13)
figma link  here
