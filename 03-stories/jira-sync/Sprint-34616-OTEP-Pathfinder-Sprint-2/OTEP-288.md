# OTEP-288: Setup a simple backend endpoint with in-memory list

**Status:** In Progress
**Assignee:** Léo Milbor
**Story Points:** N/A

---

## Description

Acceptance Criteria GET /v1/opportunities?offset=X&limit=Y returns a JSON array of at least 10 hardcoded opportunity objects, each with: id, title, agency, opportunity_type, posted_date, deadline, status, is_closing_soon, location Response envelope: {"data": [...], "total_count": N, "offset": X, "limit": Y}. Frontend owns page calculation. In-memory data must cover all 4 opportunity types (STIP, Gig, Secondment, SJR) — at least 2 of each.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Léo Milbor** (2026-05-19)
any preference regarding  page_size  and  page  vs  offset  and  limit ? So far I did with  page_size  and  page  but it’s trivial to change, especially now if needed.
