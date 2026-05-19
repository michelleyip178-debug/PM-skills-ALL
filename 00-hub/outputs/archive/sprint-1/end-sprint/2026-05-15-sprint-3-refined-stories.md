# Sprint 3 Refined Stories & Keyword Search

**Date:** 2026-05-15
**Status:** Refined for Sprint 3 Grooming

---

## 1. Keyword Search (Missing Story Identified in Audit)

### Refined User Story
As an officer, I want to search opportunities by keyword, so that I can quickly find roles matching my specific interests or skills.

### Acceptance Criteria (Must-Haves)
- [ ] I can enter a keyword into a search bar to filter the opportunity listing.
- [ ] The search matches against opportunity title, description, and agency name.
- [ ] The search handles partial matches and minor typos gracefully.
- [ ] If my search returns zero results, I see a clear "No opportunities found" empty state.
- [ ] My search keyword is preserved in the URL so I can share the link or refresh the page.
- [ ] Clicking "Clear all" removes my search query and resets the listing.

### Technical Subtasks

**Back-End (BE)**
- Set up Elasticsearch / OpenSearch indexing for opportunity title, description, and agency.
- Update `GET /opportunities` API to accept and process a `q` (query) parameter with partial match/typo tolerance logic.

**Front-End (FE)**
- Implement search bar component with debounced input handling.
- Wire search input to the `q` parameter in the URL and fetch updated results from the API.
- Implement "No opportunities found" empty state.

### Execution Timeline

**Day 2 Checkpoint:** BE search API accepts `q` parameter and returns matching results using basic ILIKE or text search (indexing may be stubbed). FE search bar updates the URL and fetches data.

**Day 3 Checkpoint:** Elasticsearch/OpenSearch indexing is fully wired with partial match and typo tolerance. FE "No results" empty state and "Clear all" integration are complete.

### Should-Have Split Tickets
- Autocomplete / Suggested Search — Add drop-down suggestions as the user types (split to R1).

### Nice-to-Haves (Backlog)
- Search term highlighting in the results cards.

---

## 2. OTEP-86: Filter by opportunity type

### Refined User Story
As an officer, I want to filter the opportunity listing by type, so that I can focus only on the kinds of roles I am eligible for or interested in.

### Acceptance Criteria (Must-Haves)
- [ ] I can filter by opportunity type: Internal Job, SJR, or STIP/Gig.
- [ ] I can select more than one type at once (e.g., viewing both SJR and STIP).
- [ ] If no filter is selected, all opportunity types are shown by default.
- [ ] If my selected filters return no results, I see "No opportunities found" (shared with Search).
- [ ] My filter selections are preserved in the URL query parameters.
- [ ] Active filters are visually distinct so I know the list is filtered.

### Technical Subtasks

**Back-End (BE)**
- Update `GET /opportunities` API to accept an array of `type` parameters and filter the database query accordingly.

**Front-End (FE)**
- Implement the filter UI component (checkboxes/pills) per Amber's designs.
- Wire filter selections to URL query parameters and trigger API fetch.
- Add visual active state to selected filter buttons.

### Execution Timeline

**Day 2 Checkpoint:** BE API correctly filters by single or multiple `type` arguments. FE filter UI renders and successfully updates the URL.

**Day 3 Checkpoint:** FE correctly syncs UI state from URL on page load (refresh persistence). Empty state for zero-results is fully integrated.

### Should-Have Split Tickets
- Filter result counts — Show the number of matching opportunities next to each filter option.

### Nice-to-Haves (Backlog)
- "Broaden your filters" suggestions on the empty state.

---

## 3. US-05: Clear filters and reset view

### Refined User Story
As an officer, I want to clear all active filters and searches with one click, so that I can easily return to viewing the complete opportunity listing.

### Acceptance Criteria (Must-Haves)
- [ ] A "Clear all" option is visible whenever one or more filters (or a search query) are active.
- [ ] Clicking "Clear all" removes all filter selections and search keywords.
- [ ] "Clear all" resets the URL back to the default unfiltered state and returns the user to Page 1.
- [ ] "Clear all" is hidden if no filters or searches are active.

### Technical Subtasks

**Back-End (BE)**
- None (UI/routing concern only).

**Front-End (FE)**
- Implement "Clear all" button visibility logic (show if `type` or `q` params exist).
- Wire "Clear all" click handler to strip URL parameters and reset pagination state to page 1.

### Execution Timeline

**Day 1 Checkpoint:** FE "Clear all" button appears conditionally and correctly clears URL state.

**Day 2 Checkpoint:** Reset fully integrates with search, filters, and pagination components, snapping the user back to the default Page 1 view smoothly.

### Should-Have Split Tickets
- None (this is a small, atomic feature).

### Nice-to-Haves (Backlog)
- Keyboard shortcut (e.g., Esc) to clear active filters.

---

## 4. OTEP-87: Enhance detail page with apply CTA + competencies

### Refined User Story
As an officer, I want to see required competencies and a clear apply action on the opportunity detail page, so that I can determine if I am a good fit and begin my application.

### Acceptance Criteria (Must-Haves)
- [ ] If viewing an Internal Job, STIP, or Gig, an "Apply" button is visible.
- [ ] If viewing an SJR, the "Apply" button is intentionally hidden (no apply in MVP).
- [ ] If the opportunity has closed, the "Apply" button is hidden and replaced with "This opportunity is closed."
- [ ] The detail page displays the required competencies for the role.

### Technical Subtasks

**Back-End (BE)**
- Ensure the `GET /opportunities/:id` endpoint returns competency data.
- Ensure the endpoint returns opportunity type and closing date (already built in Sprint 2, verify).

**Front-End (FE)**
- Update the detail page layout to include the "Apply" CTA block with conditional logic based on opportunity type and status.
- Add the Competencies section to the detail page layout.

### Execution Timeline

**Day 2 Checkpoint:** FE displays the Apply CTA conditionally based on mock API data (SJR = hidden, Closed = hidden). Competencies section renders.

**Day 3 Checkpoint:** Fully wired to the actual BE API. Edge cases for missing competency data handled gracefully without breaking the layout.

### Should-Have Split Tickets
- Profile incomplete warning — Show a warning banner before applying if the officer's profile is incomplete (requires cross-service profile data, defer if blocked).

### Nice-to-Haves (Backlog)
- Competency match scoring against the officer's profile.

---

## 5. US-18: Apply via FormSG - basic redirect

### Refined User Story
As an officer viewing an Internal Job, STIP, or Gig, I want to click "Apply" and be taken to the relevant application form, so that I can submit my details.

### Acceptance Criteria (Must-Haves)
- [ ] Clicking the "Apply" button opens the specific `formsg_url` for that opportunity in a new browser tab.
- [ ] If the `formsg_url` is missing or null, the "Apply" button is disabled and shows an error tooltip or fallback text ("Application form unavailable — contact the posting agency").

*Assumes `formsg_url` is confirmed and available in the data payload (Open Item #2).*

### Technical Subtasks

**Back-End (BE)**
- Ensure the `GET /opportunities/:id` endpoint exposes the `formsg_url` string.

**Front-End (FE)**
- Wire the "Apply" button's `href` to the `formsg_url` and set `target="_blank"`.
- Implement disabled state and fallback UI text for null `formsg_url` values.

### Execution Timeline

**Day 1 Checkpoint:** Apply button accurately redirects to the URL provided in the API payload in a new tab.

**Day 2 Checkpoint:** Fallback state for missing URL is implemented and tested.

### Should-Have Split Tickets
- FormSG URL pre-fill — Pass officer's name/email via URL parameters to pre-fill the FormSG form (requires confirmation FormSG supports this).

### Nice-to-Haves (Backlog)
- Track "Apply" clicks for analytics (redirect via an internal endpoint to capture the event).
