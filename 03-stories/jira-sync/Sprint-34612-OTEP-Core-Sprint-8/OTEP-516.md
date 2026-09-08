# OTEP-516: Import DLE ID for POCDEX ID for JumpStart Integration

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

To integrate with the external  Jumpstart  AI course-recommendation service (which keys on the learner's  DLE ID ), we need to map our officers to their DLE ID. We know officers by  NRIC , not DLE ID. The Jumpstart team provides a  CSV mapping DLE ID → NRIC  we import it so a future Jumpstart call can resolve an officer's DLE ID by NRIC  This task is the import + storage only — calling Jumpstart / exposing the DLE ID is a later task. Why a dedicated table:  officers are created only on  first login , but the mapping is delivered ahead of time. Storing  dle_id  on the officer would drop the mapping for any officer who hasn't logged in yet. So the mapping is kept in its  own table keyed by NRIC  decoupled from the officer lifecycle; the future integration looks up  dle_id  by  NRIC  (=  officer.nric ). What's built New  dle_pocdex_mapping  table ( nric  unique,  dle_id , audit columns). New ingest type that consumes a two-column CSV ( dle_id, nric ) through the existing  POST /api/v1/competencies/ingest  workflow and  upserts  each row into the table. Acceptance Criteria A  dle_pocdex_mapping  table exists with a  unique  nric  and a  dle_id  (migration). Importing the CSV  upserts  each row: insert, or overwrite  dle_id  if the  nric  already exists. The mapping is stored  regardless of whether the officer exists yet  (no officer lookup, no dependency on the officer record). Header row, rows with fewer than two columns, and empty values are skipped without failing the import. A per-row DB error is logged and skipped; the import continues. Routed via the existing ingest flow using a dedicated workflow id ( CFTP_DLE_MAPPING_WORKFLOW_ID ); the file is downloaded as CSV. dle_id  is  not  exposed via any API yet.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-09-07*
