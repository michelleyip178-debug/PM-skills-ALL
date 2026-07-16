# OTEP-677: [BUG] OTG and C@G data import NOT done

**Status:** To Do
**Assignee:** Thomas Huchedé
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

Overview  The OTG / C@G data import process is currently failing. As a result, the expected opportunity data is not surfacing in the API. The failure appears to be occurring during or before the raw ingestion phase into the newly created  sourceOTGOpportunity  staging table. Steps to Reproduce Trigger a standard OTG data import payload to the ingest endpoint/worker. Query the API to retrieve the newly imported OTG opportunities. Check the database to see if the raw JSON payload was appended to the  sourceOTGOpportunity  table.  Expected Result  The system should successfully accept the OTG payload and surface the parsed opportunity data via the API.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-07-16*
