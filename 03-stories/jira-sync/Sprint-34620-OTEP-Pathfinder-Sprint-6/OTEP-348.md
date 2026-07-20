# OTEP-348: OTG data ingestion — scheduler & observability

**Status:** Backlog
**Assignee:** N/A
**Story Points:** 3
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

Companion to OTEP-192. Build the scheduled execution layer and observability for the OTG ingestion pipeline. Acceptance Criteria The job runs on a defined recurring schedule (cadence TBC with engineers at planning) Each run produces a summary log: records read, inserted, updated, skipped, and errors Invalid or incomplete records are skipped and logged; a bad row does not abort the run Alerts or notifications on repeated failures (threshold TBC)

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Léo Milbor** (2026-06-24)
I think this story should be re-evaluated since AFAIK, the task is not scheduled but manually triggered with the upload flow    is implementing. There is several  TBC  in the ACs that needs clarification or decisions. Observability wise, is the  source_otg_opportunity  table with  warnings  and  errors  sufficient or do we need a way to display the results in FE (if so the scope is different from what we first thought). In terms of ops observability (logs/metrics/trace), I’d say we track it with

---

**Rathika Ramalingam** (2026-06-05)
Test Cases Document:

---
*Synced from Jira: 2026-07-20*
