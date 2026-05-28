# OTEP-192: Recurring OTG data ingestion job

**Type:** Technical Task (non-visible — no officer-facing UI)
**Status:** Backlog
**Assignee:** Pow Hwee / Leo
**Story Points:** N/A
**Updated:** 2026-05-28 — Reshaped from user story to technical task. ACs rewritten as system-behaviour criteria.

---

## Description

Build a scheduled job that reads the latest OTG Excel export, transforms records to match the OTEP opportunity schema, and upserts them into the database. Runs on a recurring schedule. Officers see current opportunities automatically, with no manual intervention needed.

This is a non-visible backend story. There is no officer-facing UI component.

**Acceptance Criteria**

1. The job runs on a defined recurring schedule. *(Cadence TBC — confirm with Pow Hwee + Rama at Planning: daily assumed but not confirmed.)*
2. Each run reads the latest OTG Excel file from the configured source *(file delivery mechanism TBC — SFTP, manual upload, or shared path — confirm with Pow Hwee + Rama at Planning)*, stores the raw data, and loads the processed opportunity records into the database.
3. Opportunities present in a previous export but missing from the latest export are automatically deactivated — removed from the officer listing but kept in the database (soft delete). *(Product decision: auto-deactivate — 2026-05-28)*
4. Invalid or incomplete records are skipped and logged; a bad row does not abort the run.
5. Each run produces a summary log: records read, inserted, updated, skipped, and errors.

**Design Note**

Structure the pipeline so a future C@G API source can be added without rewriting the transform/upsert layer. *(Open item #23)*

**Decisions Made (Pre-Planning)**

- ✅ Disappearing opportunities → auto-deactivate (soft delete). Decided 2026-05-28.
- ✅ Failure alerting → deferred to post-MVP. Not in scope for Sprint 3. Decided 2026-05-28.

**Open Questions (Resolve at Planning)**

- ❓ How does the OTG Excel file arrive? (SFTP, manual upload, shared path — determines trigger mechanism)
- ❓ What is the ingestion cadence? (daily assumed but not confirmed)

**Sub-task**

- OTEP-313 — OTG raw ingest table (Leo, In Progress in Sprint 2 — must land before this story can build)

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
