# OTEP-85: Display opportunity cards with real OTG data

**Status:** Done
**Assignee:** N/A
**Story Points:** 8
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

User Story As an  officer,  I want to  see open opportunities displayed as cards,  So that  I can easily discover career and development options. Acceptance Criteria Grid Layout:  The system must display open opportunities as summary cards in a 3-column grid (up to 15 cards per page, filling row-by-row, left-to-right). Card Data:  The system must display the Title, Agency, Posting Date (e.g., "12 May 2026"), and Type on each card. Visibility:  The system must only display opportunities with a closing date strictly in the future. Sorting:  The system must sort the cards by Posting Date (newest first). Deterministic Order:  The system must use the Opportunity ID (descending) as a secondary sorting tie-breaker if posting dates match exactly.

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-663 | [BUG] Open issues for competencies listing page | To Do |
| OTEP-677 | [BUG] OTG and C@G data import NOT done | To Do |
| OTEP-193 | Design Data Model for Opportunities | Done |
| OTEP-288 | Setup a simple backend endpoint with in-memory list | Done |
| OTEP-296 | Prepare defined report format that matches data model | Done |
| OTEP-313 | OTG raw ingest table and source model | Done |
| OTEP-320 | Replace mock /opportunities endpoint with real db access | Done |
| OTEP-170 | Base Layout for Opportunity Listing Page | Done |

---

## Latest Comments

**Rathika Ramalingam** (2026-07-06)
Testing done in DEV with Test Report added to confluence and bug card created as sub-task for failed cases.

---

**Rathika Ramalingam** (2026-05-19)
High Level Test Cases Scenario 1: Displaying all required fields on an opportunity card as in figma Given  an opportunity exists with complete mandatory data; Title, Agency, Posting Date, Type, Closing Date When  the opportunity is rendered in the UI grid Then  the card displays the opportunity Title And  the card displays the Agency name And  the card displays the Type And  the card displays the Posting Date strictly formatted as "DD Month YYYY" (e.g., "02 May 2026") Scenario 2 :  Rendering opportunities with future closing dates Given  the database contains an opportunity where the Closing Date is strictly greater than the current date/time (in SGT) When  the user views the Opportunities landing page Then  the opportunity is visible in the list of returned cards. Scenario 3: Hiding opportunities that have already closed Given  the database contains an opportunity where the Closing Date is exactly the current date/time or in the past When  the user views the Opportunities landing page Then  the opportunity is strictly excluded from the list of returned cards. Scenario 4: Primary sorting by posting date Given  the system fetches multiple valid opportunities with different posting dates When  the UI renders the opportunity cards Then  the cards are sorted chronologically by Posting Date And  the opportunity with the newest (most recent) Posting Date appears first. Scenario 5: Secondary tie-breaker sorting by Opportunity ID Given  the system fetches two valid opportunities (Opportunity A and Opportunity B) And  both opportunities have the exact same Posting Date And  Opportunity A has a higher Opportunity ID (e.g.,  1005 ) than Opportunity B (e.g.,  1002 ) When  the UI renders the opportunity cards Then  Opportunity A is rendered before Opportunity B in the grid Scenario: Grid structure for 15 or fewer opportunities Given  the API successfully returns  15 or fewer  valid opportunities (e.g., 4 or exactly 15 opportunities) When  the user views the page on a Desktop viewport Then  all returned cards are displayed on the page And  the cards strictly adhere to the 3-column grid structure without stretching to fill empty column space And  the cards populate sequentially row-by-row, from left-to-right. Scenario: Enforcing the maximum limit for more than 15 opportunities Given  the API successfully returns  more than 15  valid opportunities When  the user views the page on a Desktop viewport Then  the UI limits the display to exactly 15 cards on the current view And  the cards are visually arranged in a 3-column grid And  the cards populate the grid sequentially row-by-row, from left-to-right.

---

**Michelle Yip** (2026-05-19)
Have removed >= 7 days and will put into the closing soon label ticket. have removed the AC of silently drop and that will be in the designing recurring job, i assume?

---
*Synced from Jira: 2026-07-16*
