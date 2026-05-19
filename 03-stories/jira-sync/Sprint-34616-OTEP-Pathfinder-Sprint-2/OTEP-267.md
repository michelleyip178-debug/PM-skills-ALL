# OTEP-267: Pagination for listing page

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

As an  officer,  I want to  page through all available opportunities,  So that  I can find listings beyond the first screen. Acceptance Criteria: The system must display "Next" and "Previous" pagination controls when there are more than 15 total opportunities. The user can click the pagination controls to navigate between pages of results. The system must display the current page number and the total number of pages (e.g., "Page 1 of 5"). The system must completely hide the pagination controls when there are zero opportunities to display.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-05-18)
Clean and well-scoped. Two notes: API contract dependency: GET /opportunities needs to include total_count or total_pages in the response so the frontend can render the page counter. Will capture this in the API spec on Day 1. Loading indicator: the ACs mention a "simple spinner". Suggest upgrading to a skeleton loading state (shimmer placeholders) — it’s ~half a day of work and gives a noticeably more polished feel. Recommend treating this as must-have rather than nice-to-have.
