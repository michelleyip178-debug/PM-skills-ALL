# OTEP-85: Display opportunity cards with real/mock OTG data

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

User Story As an  officer,  I want to  see open opportunities displayed as cards,  So that  I can easily discover career and development options. Acceptance Criteria Grid Layout:  The system must display open opportunities as summary cards in a 3-column grid (up to 15 cards per page, filling row-by-row, left-to-right). Card Data:  The system must display the Title, Agency, Posting Date (e.g., "12 May 2026"), and Type on each card. Visibility:  The system must only display opportunities with a closing date strictly in the future, evaluated against server time. Closing Date >= 7 days. Sorting:  The system must sort the cards by Posting Date (newest first). Deterministic Order:  The system must use the Opportunity ID (descending) as a secondary sorting tie-breaker if posting dates match exactly. Critical Error Handling:  The system must silently drop and log any card that is missing mandatory data (ID, Title, Agency, Type, Posting Date, or Closing Date), while ensuring the rest of the valid cards render normally.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-05-18)
Clarification needed on the visibility rule: The AC currently says "Closing Date >= 7 days" and also "strictly in the future." These are different rules: "Strictly in the future" = show everything that hasn’t closed yet. ">= 7 days" = hide listings that close within the next week. I suspect the 7-day rule is meant for the "Closing soon" label in OTEP-129, not the visibility filter here. Can you confirm? Also, the AC "silently drop and log any card missing mandatory data" — suggest reframing as: "The system must exclude any opportunity with incomplete mandatory data (ID, Title, Agency, Type, Posting Date, or Closing Date) from the listing and log the exclusion for investigation." In our contract-first approach, the API guarantees complete data, so data completeness belongs in the API contract, not the frontend story.

---

**Amber Tong** (2026-05-13)
hi here is the screenshot of the Jobs& opportunities list page. see the design file  here
