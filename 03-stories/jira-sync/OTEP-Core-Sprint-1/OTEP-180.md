# OTEP-180: Auditing strategy

**Type:** Story
**Status:** Backlog
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

h1. Auditing Strategy

h2. Goal

Settle on how to handle auditing.

h2. Expected Outcome

Documentation repository should be updated with decision and justification

h2. Scope

* Incoming stream should be stored?
** Dynamo DB
** S3
** other
* Database Changes
** created_at, created_by, updated_at, updated_by
** for all table, GORM makes this easy
** Use PostgreSQL triggers to update an Audit table
** One audit table per schema
** Soft-delete

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
