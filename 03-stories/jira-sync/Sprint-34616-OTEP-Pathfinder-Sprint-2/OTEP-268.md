# OTEP-268: Empty, error, and partial-load states for the listing

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

As an officer, I want to see clear guidance when there are no opportunities or when something goes wrong, so that I'm not confused by a blank or broken page.   Acceptance Criteria The system must display an empty state ("No opportunities available right now", with supporting text and an illustration) when there are zero open opportunities. The system must not display any pagination tools.

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-325 | Create an empty state for opportunity listing | In Progress |
| OTEP-326 | Create an error state for opportunity listing | In Progress |

---

## Latest Comments

**Rathika Ramalingam** (2026-05-19)
High level test cases: Scenario 1: Valid response returns zero opportunities Given  the user navigates to the Opportunities listing page When  the listing API successfully responds with an empty array ( [] ) Then  the UI displays the empty state illustration (as per figma) And  the heading reads: "No opportunities available right now." And  no pagination is shown

---

**Pow Hwee TAN (PSD)** (2026-05-18)
Added to Sprint 2 — empty, error, and loading states are part of the Listing→Detail journey. Feedback on ACs: Recommend removing the "partial load" AC entirely. With our Tailwind stack, the listing page fetches a single API response and renders all cards from that array. Either the entire call succeeds (all cards render) or it fails (error state). There is no mechanism for individual cards to fail independently. Good-to-have items (truncation, correlation IDs) would be better as separate low-priority backlog tickets. When buried inside this story, they either block it from closing or get quietly dropped. Draft copywriting for acceptance: Empty state: Heading "No opportunities available right now", Body "Check back soon — new opportunities are posted regularly.", no retry button (valid empty result, not an error). Error state: Heading "We couldn’t load opportunities", Body "Something went wrong on our end. Please try again.", "Try again" button that re-fetches.
