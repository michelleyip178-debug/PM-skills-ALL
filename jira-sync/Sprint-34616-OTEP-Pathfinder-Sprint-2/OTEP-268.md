# OTEP-268: Empty, error, and partial-load states for the listing

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

As an  officer,  I want to  see clear guidance when there are no opportunities or when something goes wrong,  So that  I'm not confused by a blank or broken page. Must-have: [ ]  Empty state — zero opportunities returned:  Heading: "No opportunities available right now." Body: "Check back soon — new opportunities are posted regularly." Visual: illustration per Amber's design. No retry button (valid empty result, not an error). [ ]  Error state — API returns 500 or network failure:  Heading: "We couldn't load opportunities." Body: "Something went wrong on our end. Please try again." "Try again" button that re-fetches. Visual: error illustration per Amber's design. [ ]  Partial load — listing API succeeds but individual cards fail to render  (e.g. malformed data): Render the cards that loaded successfully. Do not show a full error screen. Do not show a partial-error banner — log it server-side instead. Pagination + sort still reflect total_count from API. [ ]  Card resilience — missing optional fields:  Missing  commitment_type ,  ministry_icon , or other optional fields → field hides gracefully, no broken layout, no empty placeholder text. Good-to-have: [ ] Very long agency name → truncated with ellipsis, full name on hover (title attribute) [ ] Error state — log the failure with correlation ID for debugging

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-05-18)
Added to Sprint 2 — empty, error, and loading states are part of the Listing→Detail journey. Feedback on ACs: Recommend removing the "partial load" AC entirely. With our Tailwind stack, the listing page fetches a single API response and renders all cards from that array. Either the entire call succeeds (all cards render) or it fails (error state). There is no mechanism for individual cards to fail independently. Good-to-have items (truncation, correlation IDs) would be better as separate low-priority backlog tickets. When buried inside this story, they either block it from closing or get quietly dropped. Draft copywriting for acceptance: Empty state: Heading "No opportunities available right now", Body "Check back soon — new opportunities are posted regularly.", no retry button (valid empty result, not an error). Error state: Heading "We couldn’t load opportunities", Body "Something went wrong on our end. Please try again.", "Try again" button that re-fetches.
