# OTEP-666: Enable scheduled trigger of import

**Status:** Done
**Assignee:** Léo Milbor
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 8 (34622)

---

## Description

Enable Scheduled Trigger of Import Context Currently, the Careers@Gov (C@G) import is triggered manually. It is however running as a background job and is ready to be run automatically on a schedule. Goal C@G should be triggered automatically following a schedule OPS should be able to monitor and manually trigger or rerun jobs Questions What technology to use? AWS native leverage  river  ui implement our own ui external middleware (airflow, temporal, etc.) What is the schedule? daily working day

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-07-06)
can take. a look at aws eventbridge scheduler and ecs scheduled tasks?  Also check with Adrian if he has something being considered.

---

**Léo Milbor** (2026-07-06)
This is to track the automatic trigger. I provided a basic description but we should update on the unknown and tech choices.

---
*Synced from Jira: 2026-08-17*
