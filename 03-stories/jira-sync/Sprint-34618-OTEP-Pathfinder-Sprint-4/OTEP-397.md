# OTEP-397: [spike] Discover OTG excel file upload - Flow and UI

**Status:** Done
**Assignee:** Michelle Yip
**Story Points:** 3.0

---

## Description

User story Users will want to upload excels (once a week frequency) so that backend to pick up and process these files. These excels sheet can come from various sources e.g. OTG. The uploaded file will first be scanned in Cloud File Transfer (CFT), then webhook notification to backend API. UI Component Acceptance criteria I must select a data source from dropdown before the file upload input becomes available I cannot see the upload UI if I don't have upload permissions I can upload a valid  .xlsx  file and see a success confirmation I see an inline error if I try to select a non- .xlsx  file I see an inline error if my file exceeds the size limit I see a "scanning" state while my file is being checked for threats I see an error and can retry if my file fails the virus scan I see a generic error and can retry if the server fails (500) Out of Scope Actual CFT integration — scan responses are mocked/stubbed Actual role/permission system — upload access is mocked via a hardcoded profile ID list Backend data import and processing logic Invalid file content errors (400) — backend validation of missing columns, empty sheets, etc. Row-level data warnings   — bad data rows, unrecognised labels, invalid formats Upload history or audit trail UI Multiple file upload in one submission

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Hao Eng** (2026-06-09)
there will be a new field called “role” to be added in keycloak  no Jira ticket yet!

---

**Hao Eng** (2026-06-08)
hi   , heard from Rama that only specific users can access this upload UI. how to identify such user?

*Synced from Jira: 2026-07-01*
