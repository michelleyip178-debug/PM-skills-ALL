# OTEP-180: Auditing strategy

**Type:** Story
**Status:** Backlog
**Assignee:** Fanxu Wang
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 6 (id 34610, active)

---

## Description

Auditing Strategy Goal Settle on how to handle auditing. Expected Outcome Documentation repository should be updated with decision and justification Scope Incoming stream should be stored? Dynamo DB S3 other Database Changes created_at, created_by, updated_at, updated_by for all table, GORM makes this easy Use PostgreSQL triggers to update an Audit table One audit table per schema Soft-delete

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-07-23*
