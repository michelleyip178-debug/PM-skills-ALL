# OTEP-129: See whether an opportunity is open or closed before applying.

**Status:** QA
**Assignee:** Thomas Huchedé
**Story Points:** 2.0

---

## Description

User Story As an officer, I want to know whether an opportunity is still accepting applications before I click through, so that I'm not caught off guard by a posting I can no longer act on.   Acceptance Criteria Deep-links to closed postings show a simple posting message: “This opportunity is no longer available” with a link back to the listing.  Postings approaching their end date display a “Closing soon” label on both the card and the detail page (threshold will be 7 days or less).

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-362 | Update backend to not return closed opportunities | Done |
| OTEP-363 | Create UI component to display closed opportunity | Done |
| OTEP-367 | Update UI for competencies of opened opportunities | Done |

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-05-18)
Added to Sprint 2 — Open/Closed labels and "Closing soon" badge complete the Listing→Detail journey. Feedback on ACs: Business rule conflict with OTEP-85: OTEP-85 says hide listings where Closing Date >= 7 days (only show opportunities closing more than 7 days from now). This ticket says show "Closing soon" for opportunities closing within 7 days. If OTEP-85 hides them, "Closing soon" can never appear. Suggest: OTEP-85 visibility = show all where closing_date > now. This ticket = "Closing soon" badge where closing date is within 7 days. The AC "Closed or expired postings are hidden from the listing" is already handled by OTEP-85 visibility filter. Suggest removing it from this ticket to avoid double-counting. This ticket should own labels and deep-link behaviour only.

*Synced from Jira: 2026-07-01*
