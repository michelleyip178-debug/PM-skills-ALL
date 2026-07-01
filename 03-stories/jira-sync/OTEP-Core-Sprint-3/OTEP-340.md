# OTEP-340: OTEP Resolve Identity API

**Type:** Sub-task
**Status:** Done
**Assignee:** Pei Ern Lim
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 3

---

## Description

Create an API endpoint to resolve identity of the logged in user in OTEP.
The API will be used for:
Resolved logged in user identity
Provide an id for auth session to preserve
API Endpoint
POST /profiles/identity
Response Fields
The API should return:
profile_id
Acceptance Criteria
Endpoint /profiles/identity is implemented
User profile was inserted into DB
User competencies was inserted into DB
Returns valid profile id
Returns appropriate error (e.g. 404) if user is not found
API integrates with POCDEX data source and Competencies Bank
Meets performance expectations

---

## Subtasks

_No subtasks._

*Synced from Jira: 2026-07-01*
