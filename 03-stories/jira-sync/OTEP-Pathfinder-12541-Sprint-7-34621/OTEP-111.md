# OTEP-111: Officers with no access (unauthorised page - display only)

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

**Sprint:** OTEP-Pathfinder Sprint 7 (2026-07-26 → 2026-08-09)

---

## Description

As a  public officer who has authenticated via WOG AD but does not have access to Career Compass,  I want to  see a clear message explaining why,  So that  I know I'm not locked out by a technical error and I know what to do next. Acceptance Criteria: Given I am not from a pilot agency → show unauthorised page. Given I have a POCDEX profile but it is deactivated/inactive → show unauthorised page. Given my agency was previously in the pilot but has since been removed → show unauthorised page on next login (not broken/blank). Given my agency leaves the pilot while I'm mid-session → [NEEDS AC — decision #10, owner Rama] The unauthorised page shows: "Oops, you do not seem to have access at the moment. Please contact your HR for more information." The page does not expose which specific check failed (no distinguishing not-in-pilot vs. deactivated).  Explicitly out of scope now:  whitelisted agency + no POCDEX profile yet. That's no longer "no access" — it's a system/timing error, owned by OTEP-594's new scenario.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-07-28*
