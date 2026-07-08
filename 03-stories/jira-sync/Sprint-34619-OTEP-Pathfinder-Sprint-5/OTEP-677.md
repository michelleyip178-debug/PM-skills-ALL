# OTEP-677: [BUG] OTG data is NOT imported 

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Overview  The OTG data import process is currently failing. As a result, the expected opportunity data is not surfacing in the API. The failure appears to be occurring during or before the raw ingestion phase into the newly created  sourceOTGOpportunity  staging table. Steps to Reproduce Trigger a standard OTG data import payload to the ingest endpoint/worker. Query the API to retrieve the newly imported OTG opportunities. Check the database to see if the raw JSON payload was appended to the  sourceOTGOpportunity  table.  Expected Result  The system should successfully accept the OTG payload and surface the parsed opportunity data via the API.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
