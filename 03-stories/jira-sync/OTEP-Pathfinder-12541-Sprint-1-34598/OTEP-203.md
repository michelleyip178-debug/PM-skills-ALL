# OTEP-203: Standalone POCDEX API service

**Type:** Task
**Status:** Done
**Assignee:** Pow Hwee TAN (PSD)
**Story Points:** N/A
**Sprint:** Sprint 3 (1–12 Jun 2026)
**Note:** No story file exists yet — ACs to be confirmed with Pow Hwee at Sprint 3 Planning (2026-05-28).

---

## Description

Build a standalone API service for POCDEX (job families and competency data) that can be called by OTEP and other consuming services. This is plumbing infrastructure required before Sprint 4's ringfencing feature (OTEP-127) and other competency-dependent flows.

This story was staggered into Sprint 3 specifically so the service exists when Sprint 4 needs it. *(Sequencing decision — 2026-05-20)*

**Acceptance Criteria**

ACs TBC — confirm with Pow Hwee at Sprint 3 Planning.

Key questions to resolve:
- What endpoints does this service expose? (job families, competencies, or combined?)
- What is the data source? (feeds from OTEP-271 local DB, or separate upstream?)
- Who are the consumers — OTEP only, or other squads?
- What authentication model does the API use?

**Dependencies**

- Depends on: OTEP-271 (Local POCDEX database) — service needs the data store
- Blocks: OTEP-127 (Sprint 4 ringfencing feature)

**Risk**

Same risk as OTEP-271 — WD×DO job family model discussion at 16:00 on 2026-05-28 may affect what this service needs to expose. At Planning, consider committing provisionally with the caveat that scope may shift after the 16:00 session.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-07-01*
