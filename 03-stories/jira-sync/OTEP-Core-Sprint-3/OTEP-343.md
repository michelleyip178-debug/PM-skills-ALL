# OTEP-343: Implement OTG Competency Staging & First-Login Migration

**Type:** Sub-task
**Status:** QA
**Assignee:** Kingsley Low
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 3

---

## Description

Implement logic to:
Load OTG competencies from the provided Excel file into a staging layer
On user’s first login, retrieve and map these competencies into the user profile with correct categorisation
Scope
✅ Phase 1 – Staging Load (Config-triggered)
Ingest OTG competencies from raw_users_skills file
Store competencies for later retrieval during login
✅ Phase 2 – First Login Processing
On first login, map staged OTG competencies into:
Role-based Core competencies
Role-based Functional competencies
Self-declared competencies
Trigger Mechanism
Staging Load
Triggered via config / admin execution:
migration.otg.load.enabled = true
First Login Processing
Trigger condition:
user.firstLogin == true
Core Processing Flow
1. User Filtering
Process only users where:
user_id starts with "P" (POCDEX ID)
Ignore:
NRIC-based users
Email-based users
2. First Login – Retrieve Staged Competencies
Fetch all competencies associated with the user from the staging layer
3. Load User Context
Retrieve:
User role
Load role-based competencies:
Core competencies
Functional competencies
4. Competency Mapping
Matching is based on:
competency_name (from OTG) → competency_name (OTEP bank)
Use exact or normalised matching (case-insensitive)
5. Categorisation Logic (Key Business Rule)
For each competency:
✅ Case 1 – Matches Role-Based Core
→ display under Core competencies (role-based)
✅ Case 2 – Matches Role-Based Functional
→ display under Functional competencies (role-based)
✅ Case 3 – Exists in Competency Bank
→ add to self-declared competencies
✅ Case 4 – No Match
→ omit (Fuel50 / unsupported competencies)
6. Exclusion Rules
Exclude completely:
CEG competencies
Any competency not in OTEP competency bank
7. State Update
Role-based competencies → marked as displayed
Self-declared competencies → added to user profile
8. Completion
Ensure staged competencies for user are not reprocessed on subsequent logins
Acceptance Criteria (Sub-task)
OTG competencies successfully ingested via config-triggered load
Only users with POCDEX ID are processed
On first login, competencies are retrieved and processed
Competencies correctly categorised into:
Core (role-based)
Functional (role-based)
Self-declared
CEG competencies are excluded
Unmatched competencies are omitted
No duplicate competencies created
Migration occurs only once per user (first login)
Migrated competencies are reflected in the user profile
Dev Notes
Matching must be:
case-insensitive
trimmed / normalised
Use in-memory lookup for competency name mapping (performance)
Ensure:
first-login logic runs only once per user
Log metrics:
total competencies processed
matched / unmatched / excluded
✅ Important Alignment Note
OTG competencies are staged upfront and only materialised into user profile at first login to ensure seamless user transition without requiring re-entry.

---

## Subtasks

_No subtasks._

*Synced from Jira: 2026-07-01*
