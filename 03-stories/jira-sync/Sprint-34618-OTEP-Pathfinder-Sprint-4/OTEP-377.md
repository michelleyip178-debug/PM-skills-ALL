# OTEP-377: Fetch C@G specific payload in detail API

**Status:** Backlog
**Assignee:** Léo Milbor
**Story Points:** N/A

---

## Description

Schema + API response only. No ingestion. Depends on OTEP-374. OTEP-374 adds  responsibilities ,  requirements ,  experience_min_years ,  experience_max_years  to the  opportunity  table. This ticket exposes them in the detail API ( GET /api/v1/opportunities/:id ) via  OpportunityDTO  in  get_handler.go . These fields are nullable — populated for C@G,  null  for OTG. Existing OTG responses should be unchanged. Unblocks OTEP-378.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
