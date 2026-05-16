# Sprint 2 — Final user stories (all six)

**Date:** 2026-05-14
**Sprint goal:** By end of Sprint 2, an officer can browse open OTG opportunities and click into any one to see the full details — the core "discover → decide" loop, working end-to-end on real data.

**Sprint 2 stories:**
- OTEP-85 — Display open opportunities as cards (the rendering foundation)
- OTEP-85a — "Closing soon" label on cards and detail page
- OTEP-85b — Click-through to detail and return-to-page state
- OTEP-128 — View opportunity detail page
- OTEP-267 — Pagination for the listing page
- OTEP-268 — Empty, error, and partial-load states for the listing

**Cross-cutting Sprint 2 boundaries (applies to all six stories):**
- OTG data only — no C@G opportunities this sprint
- Desktop only — mobile/tablet layouts come later
- No apply flow — apply actions are Sprint 3 (US-18)
- No filters or search — Sprint 3
- Authentication states (logged-out, session expired) are handled by the OTEP-71 family, not these stories

---

## OTEP-85 — Display open opportunities as cards

**Sprint:** Sprint 2 | **Priority:** MVP | **Epic:** Opportunities (Epic 4)
# OTEP-85 — Display open opportunities as cards

## Refined User Story
As an officer, I want to see open opportunities displayed as cards, so that I can easily discover career and development options.

## Acceptance Criteria (Must-Haves)
- The system must display open opportunities as summary cards in a 3-column grid (up to 15 cards per page, filling row-by-row, left-to-right).
- The system must display the Title, Agency, Posting Date (e.g., "12 May 2026"), and Type on each card.
- The system must only display opportunities with a closing date strictly in the future, evaluated against server time.
- The system must sort the cards by Posting Date (newest first).
- The system must use the Opportunity ID (descending) as a secondary sorting tie-breaker if posting dates match exactly.
- The system must silently drop and log any card that is missing mandatory data (ID, Title, Agency, Type, Posting Date, or Closing Date), while ensuring the rest of the valid cards render normally.
- The system must render the card normally but display the label "Other" if the opportunity type is missing or unrecognized by the system.

## Technical Subtasks

**Back-End (BE)**
- Build `GET /opportunities` endpoint
- Implement business logic to filter out records where `closing_date <= now()` (server time)
- Implement sorting logic `ORDER BY posting_date DESC, id DESC`
- Map and return clean JSON payload for valid opportunity records

**Front-End (FE)**
- Build base UI Card component (HTML/CSS) to LifeSG design spec
- Build responsive 3-column CSS grid layout
- Integrate with `GET /opportunities` API and render list
- Implement client-side logic to drop malformed cards and apply "Other" type fallback

## Execution Timeline

**Day 2 Checkpoint:** `GET /opportunities` API returns valid JSON payload; FE grid renders correctly on screen using mocked data payload.

**Day 3 Checkpoint:** FE successfully calls real BE API and renders dynamic cards; error dropping logic is functional and observable.

## Should-Have Split Tickets
- Implement data fetching loading states — The system must display the standard LifeSG loading spinner while fetching data.
- Enforce uniform card heights for missing data — The system must maintain uniform card heights even if optional data is missing by preserving empty layout space.

## Nice-to-Haves (Backlog)
- Truncate long opportunity titles — The system must visually truncate card titles that exceed two lines with an ellipsis.

---

# OTEP-85a — "Closing soon" label on cards and detail page

## Refined User Story
As an officer, I want to see at a glance which opportunities are closing soon, so that I can prioritise the ones I might miss if I wait.

## Acceptance Criteria (Must-Haves)
- The system must display a "Closing soon" label on the opportunity card if the closing date is within 7 days of the current date.
- The system must display the identical "Closing soon" label on the opportunity detail page if the closing date is within 7 days.
- The system must not display the label if the closing date is more than 7 days away.
- The system must ensure the label is visually distinct from the opportunity type label.
- The system must ensure the label is readable without relying solely on color (e.g., by including accompanying text or an icon).

## Technical Subtasks

**Back-End (BE)**
- None (Logic is pure presentation based on existing `closing_date` payload)

**Front-End (FE)**
- Create "Closing soon" badge UI component
- Implement 7-day client-side date calculation logic
- Integrate badge into Listing Card component conditionally
- Integrate badge into Detail Page component conditionally

## Execution Timeline

**Day 2 Checkpoint:** FE date calculation logic is written and unit tested; badge component is built in isolation.

**Day 3 Checkpoint:** Badges dynamically appear correctly on both the Listing and Detail pages when hitting a mocked API with varying closing dates.

## Should-Have Split Tickets
- Enforce consistent label positioning — The system must display the label in a consistent, anchored position on every card to prevent visual jumping in the grid layout.

## Nice-to-Haves (Backlog)
- None

---

# OTEP-85b — Click-through to detail and return-to-page state

## Refined User Story
As an officer, I want to click into an opportunity and return to where I was when I'm done, so that I can browse fluently without losing my place.

## Acceptance Criteria (Must-Haves)
- The user can click an opportunity card to navigate to its full detail page.
- The system must return the user to the exact listing page number they were previously viewing when they use the "Back to opportunities" link or the browser's back button.
- The system must maintain consistent newest-first ordering across pages without items reshuffling or repeating as the user navigates back and forth.

## Technical Subtasks

**Back-End (BE)**
- None

**Front-End (FE)**
- Wrap Listing Cards in router links pointing to `/opportunities/:id`
- Implement router history/state preservation for back-navigation
- Wire "Back to opportunities" link to trigger router back action

## Execution Timeline

**Day 2 Checkpoint:** Clicking a card successfully routes to the detail page URL.

**Day 3 Checkpoint:** Clicking the back button or link on the detail page returns the user to the exact previous listing page without losing pagination state.

## Should-Have Split Tickets
- Implement deep-linking and state preservation — The system must maintain the current page state (e.g., stay on page 3) if the user refreshes the browser, and support URL deep-linking.

## Nice-to-Haves (Backlog)
- None

---

# OTEP-128 — View opportunity detail page

## Refined User Story
As an officer, I want to view the full details of an opportunity on a dedicated page, so that I can decide whether to apply without leaving OTEP.

## Acceptance Criteria (Must-Haves)
- The system must display a detail page containing the Title, Agency, Posting Date, Closing Date, Type, Description, "What you'll develop" text, and Commitment type.
- The system must format all dates in an absolute format (e.g., "12 May 2026").
- The system must provide a clearly visible "Back to opportunities" link to return to the listing.
- The system must load the detail page correctly when accessed directly via a bookmark or shared URL.
- The system must display a clear "This opportunity is closed" notice instead of standard actions if the closing date has passed.
- The system must display an "Opportunity not found" message with a link back to the listing if the provided opportunity ID is invalid.

## Technical Subtasks

**Back-End (BE)**
- Build `GET /opportunities/:id` endpoint to fetch a single record
- Implement 404 Not Found error handling for invalid IDs

**Front-End (FE)**
- Build full Detail Page UI layout based on design specs
- Integrate with `GET /opportunities/:id` API and map payload fields
- Implement absolute date formatting logic
- Build and render "Opportunity is closed" view state
- Build and render "Opportunity not found" 404 view state

## Execution Timeline

**Day 2 Checkpoint:** `GET /opportunities/:id` API returns single record JSON; FE detail page layout is built and maps mocked data.

**Day 3 Checkpoint:** Direct navigation to a real ID URL loads the page end-to-end; navigating to an invalid ID successfully displays the 404 UI.

## Should-Have Split Tickets
- Implement detail page loading state — The system must display a loading indicator while fetching the detail page data.
- Add Ministry icons to detail page — The system must display the Ministry icon next to the agency name.

## Nice-to-Haves (Backlog)
- Dynamic browser tab titles — The system must update the browser tab title to reflect the specific opportunity name.
- Consistent Type label styling — The system must style the Type label identically to how it appears on the listing card.

---

# OTEP-267 — Pagination for the listing page

## Refined User Story
As an officer, I want to page through all available opportunities, so that I can find listings beyond the first screen.

## Acceptance Criteria (Must-Haves)
- The system must display "Next" and "Previous" pagination controls when there are more than 15 total opportunities.
- The user can click the pagination controls to navigate between pages of results.
- The system must display the current page number and the total number of pages (e.g., "Page 1 of 5").
- The system must completely hide the pagination controls when there are zero opportunities to display.

## Technical Subtasks

**Back-End (BE)**
- Update `GET /opportunities` endpoint to accept `page` and `limit` query parameters
- Implement SQL `LIMIT` and `OFFSET` pagination
- Append `total_count` and `total_pages` metadata to API response payload

**Front-End (FE)**
- Build UI for Next/Previous controls and page indicator
- Implement click handlers to append query params and fetch new page data
- Conditionally hide entire pagination component when `total_count === 0`

## Execution Timeline

**Day 2 Checkpoint:** BE API correctly respects `page`/`limit` params and returns accurate total count metadata.

**Day 3 Checkpoint:** FE pagination controls are visible; clicking Next fetches and renders the second page of data smoothly.

## Should-Have Split Tickets
- Implement pagination loading state — The system must display a loading spinner specifically while fetching the next page of results.

## Nice-to-Haves (Backlog)
- None

---

# OTEP-268 — Empty, error, and partial-load states for the listing

## Refined User Story
As an officer, I want to see clear guidance when there are no opportunities or when something goes wrong, so that I'm not confused by a blank or broken page.

## Acceptance Criteria (Must-Haves)
- The system must display an empty state ("No opportunities available right now", with supporting text and an illustration) when there are zero open opportunities.
- The system must not display a "Try again" button on the empty state.
- The system must display an error state ("We couldn't load opportunities", with supporting text and an illustration) if the page fails to load due to a server or network error.
- The system must provide a functional "Try again" button on the error state that reloads the data.
- The system must silently ignore individual malformed cards (partial load failure), rendering only the successfully loaded cards without displaying any error warnings to the user.
- The system must maintain accurate pagination totals based on the server response, regardless of whether some individual cards failed to render locally.

## Technical Subtasks

**Back-End (BE)**
- None (Behavior triggered by empty datasets or standard 500 HTTP codes)

**Front-End (FE)**
- Build Empty State UI component (illustration + text)
- Build Error State UI component (illustration + text + button)
- Implement catch logic on API requests to trigger Error State UI
- Wire "Try again" button to re-trigger API fetch

## Execution Timeline

**Day 2 Checkpoint:** FE Empty State and Error State UI components are built and visually perfect in isolation.

**Day 3 Checkpoint:** Disconnecting the local BE server reliably triggers the Error State UI; clicking "Try again" after reconnecting successfully reloads the grid.

## Should-Have Split Tickets
- None

## Nice-to-Haves (Backlog)
- Truncate long agency names — The system must truncate excessively long agency names with an ellipsis ("…") and display the full name via a tooltip on hover.

---

# OTEP-193 — Design and implement Opportunities data model

## Refined User Story
As a backend engineer, I want to establish the core data model for Opportunities, so that the database can reliably store imported OTG data and serve the listing/detail APIs.

## Acceptance Criteria (Must-Haves)
- The system must define a database schema that captures all mandatory and optional fields required by the MVP (ID, Title, Agency, Type, Posting Date, Closing Date, Commitment type, Ministry, Description, "What you'll develop").
- The system must support nullable fields for optional data without failing.
- The system must apply appropriate indexing (e.g., on `closing_date`, `posting_date`, and `id`) to support fast query sorting and filtering.

## Technical Subtasks

**Back-End (BE)**
- Draft schema definition mapping the OTG Excel columns to database columns
- Write and execute the database migration to create the `opportunities` table
- Write a basic unit test to verify record insertion and retrieval

**Front-End (FE)**
- None

## Execution Timeline

**Day 1 Checkpoint:** Database migration is merged; table exists in the local development database.

**Day 2 Checkpoint:** (Prerequisite for OTEP-85 APIs)

## Should-Have Split Tickets
- None

## Nice-to-Haves (Backlog)
- None

---

# OTEP-192 — File import job for OTG data (Excel)

## Refined User Story
As a system administrator, I want to import OTG opportunity data from an Excel report into the database, so that officers can view the most up-to-date opportunities on OTEP.

## Acceptance Criteria (Must-Haves)
- The system must provide a secure programmatic way (e.g., an endpoint or CLI script) to upload and parse the specified OTG Excel report.
- The system must map the rows in the Excel report to the OTEP-193 data model.
- The system must strictly filter out and exclude any records identified as **SJR (Senior Job Rotation)** or **SGL**.
- The system must update existing records if the Opportunity ID already exists, and insert new records if it does not (upsert behavior).
- The system must log a summary of the import (e.g., "Inserted X, Updated Y, Failed Z") upon completion.

## Technical Subtasks

**Back-End (BE)**
- Confirm the exact OTG Excel reports to be ingested (resolves Open Item #24)
- Build the CSV/Excel parser script
- Implement the SJR and SGL exclusion logic
- Implement the upsert database logic using the Opportunity ID

**Front-End (FE)**
- None (This is a backend cron/script process for MVP)

## Execution Timeline

**Day 2 Checkpoint:** Script can successfully parse a sample Excel file locally and print the mapped JSON objects to the console.

**Day 3 Checkpoint:** Script successfully upserts the parsed records into the local database; Thomas (FE) now has real data to build OTEP-85 against.

## Should-Have Split Tickets
- **Automated SFTP fetch:** The system automatically fetches the file from an OTG secure server on a cron schedule, rather than requiring a manual script trigger.

## Nice-to-Haves (Backlog)
- None

---

## Cross-story summary

### Dependency chain
```
OTEP-85 (render foundation) ──┬──> OTEP-267 (pagination)
                              ├──> OTEP-268 (empty/error/partial)
                              ├──> OTEP-128 (detail page) ──┬──> OTEP-85a (closing soon, card + detail)
                              │                             └──> OTEP-85b (click-through + state)
                              └──> [OTEP-85a, OTEP-85b also depend on OTEP-85]
```

OTEP-85 must ship first. OTEP-128 unblocks OTEP-85a and OTEP-85b. OTEP-267 and OTEP-268 can run in parallel with OTEP-128.

### Risk-ranked
1. **OTEP-85b** — state persistence architecture (high)
2. **OTEP-128** — detail page design lock + data shape for "what you'll develop" (medium)
3. **OTEP-85** — OTG data availability (medium, but blocks everything)
4. **OTEP-267, OTEP-268, OTEP-85a** — low risk, designs finalised

### Cut-line if Sprint 2 slips
1. First cut: OTEP-85a (closing-soon label) — pure UI polish, journey still works
2. Second cut: OTEP-85b "return to same page" AC — journey degrades but still works
3. Do not cut: OTEP-85, OTEP-128, OTEP-267, OTEP-268 — these are the journey

### What needs decided at tomorrow's API contract sync
1. **OTEP-85b** — how is listing state persisted? URL params, client state, session storage? PM recommends URL params (page number only).
2. **Open item #24** — which OTG Excel reports get ingested for OTEP-192? Blocks real data by Day 3-4.
3. **OTEP-128** — confirm "what you'll develop" data shape so detail page can render it without rework.
