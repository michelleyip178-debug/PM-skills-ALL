# OTEP-408: [BE] Listing API — apply ringfencing eligibility filter

**Status:** QA
**Assignee:** Thomas Huchedé
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 8 (34622)

---

## Description

Listing API filters by officer's POCDEX data resolved at login Ineligible opportunities excluded from response Eligible ringfenced Internal Jobs pinned to top POCDEX unavailable → silent fallback to unfiltered listing Unauthenticated officer → redirect to login before data returned

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Thomas Huchedé** (2026-08-18)
That was my understanding also of the following:  “Eligible ringfenced Internal Jobs pinned to top"  So in the Backend, we currently dont have any sorting for OTG’s ringfenced STIP and GIG.   Same for the Frontend, we dont have any additional sorting logic (   ) Listing renders the filtered response from OTEP-408 with no additional FE filtering logic

---

**Rathika Ramalingam** (2026-08-17)
Hi    ,  “Eligible ringfenced Internal Jobs pinned to top” - is this only for Internal Jobs and NOT for other OTG opps?   Also Internal jobs id NOT for MVP. Pls confirm.  So basically no change in sort order for the eligible opportunity. cc:

---
*Synced from Jira: 2026-08-18*
