# OTEP-268: Empty, error, and partial-load states for the listing

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

As an officer, I want to see clear guidance when there are no opportunities or when something goes wrong, so that I'm not confused by a blank or broken page.   Acceptance Criteria The system must display an empty state ("No opportunities available right now", with supporting text and an illustration) when there are zero open opportunities. The system must not display a "Try again" button on the empty state. The system must display an error state ("We couldn't load opportunities", with supporting text and an illustration) if the page fails to load due to a server or network error. The system must maintain accurate pagination totals based on the server response, regardless of whether some individual cards failed to render locally.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Rathika Ramalingam** (2026-05-19)
High level test cases: Scenario 1: Valid response returns zero opportunities Given  the user navigates to the Opportunities listing page When  the listing API successfully responds with an empty array ( [] ) Then  the UI displays the empty state illustration (as per figma) And  the heading reads: "No opportunities available right now." And  the body reads: "Check back soon — new opportunities are posted regularly." And  no retry or refresh button is rendered on the screen. Scenario 2: API failure triggers the error state Given  the user navigates to the Opportunities listing page When  the listing API request fails (e.g., 500 Internal Server Error or network timeout) Then  the UI displays the error state illustration (per Amber's design) And  the heading strictly reads: "We couldn't load opportunities." And  the body strictly reads: "Something went wrong on our end. Please try again." And  a "Try again" button is rendered on the screen. Scenario 3: User initiates a retry from the error state Given  the user is viewing the Error state screen When  the user clicks the "Try again" button Then  the system immediately re-triggers the listing API fetch request And  transitions the UI back to the Loading state. Scenario 4: Graceful handling of missing optional fields Given  the listing API returns an array of opportunities And  one or more missing optional fields ( Ex.commitment_type  ,  ministry_icon) are null or missing When  the UI renders the opportunity cards Then  the cards missing the data render successfully without breaking the CSS layout And  the UI completely hides the missing elements rather than displaying empty space, broken image icons, or placeholder text like "N/A".

---

**Pow Hwee TAN (PSD)** (2026-05-18)
Added to Sprint 2 — empty, error, and loading states are part of the Listing→Detail journey. Feedback on ACs: Recommend removing the "partial load" AC entirely. With our Tailwind stack, the listing page fetches a single API response and renders all cards from that array. Either the entire call succeeds (all cards render) or it fails (error state). There is no mechanism for individual cards to fail independently. Good-to-have items (truncation, correlation IDs) would be better as separate low-priority backlog tickets. When buried inside this story, they either block it from closing or get quietly dropped. Draft copywriting for acceptance: Empty state: Heading "No opportunities available right now", Body "Check back soon — new opportunities are posted regularly.", no retry button (valid empty result, not an error). Error state: Heading "We couldn’t load opportunities", Body "Something went wrong on our end. Please try again.", "Try again" button that re-fetches.
