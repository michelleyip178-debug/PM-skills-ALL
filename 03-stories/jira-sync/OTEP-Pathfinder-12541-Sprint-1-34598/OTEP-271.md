# OTEP-271: Local POCDEX database

**Type:** Task
**Status:** Done
**Assignee:** Léo Milbor
**Story Points:** N/A
**Sprint:** Sprint 3 (1–12 Jun 2026)
**Note:** No story file exists yet — ACs to be confirmed with Pow Hwee at Sprint 3 Planning (2026-05-28).

---

## Description

Set up a local POCDEX database within the OTEP service to store job family and competency reference data. This is plumbing infrastructure required before Sprint 4's ringfencing feature (OTEP-127) can build on top of it.

This story was staggered into Sprint 3 specifically so the infra exists when Sprint 4 needs it. Without it, Sprint 4 would block on infra that isn't there. *(Sequencing decision — 2026-05-20)*

**Acceptance Criteria**

ACs TBC — confirm with Pow Hwee at Sprint 3 Planning.

Key questions to resolve:
- What is the schema for the local POCDEX data store?
- How does data get seeded / updated? (manual load, sync from upstream, other?)
- What's the interface — API, direct DB access, or shared schema?

**Dependencies**

- Blocked by: nothing (can start Sprint 3 independently)
- Blocks: OTEP-203 (Standalone POCDEX API service); OTEP-127 (Sprint 4 ringfencing feature)

**Risk**

WD×DO job family model discussion is on 2026-05-28 at 16:00 — back-to-back with Sprint 3 Planning. If the job family model changes, requirements for this story could shift. At Planning, consider committing with the caveat that scope may adjust after the 16:00 session.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-07-01*
