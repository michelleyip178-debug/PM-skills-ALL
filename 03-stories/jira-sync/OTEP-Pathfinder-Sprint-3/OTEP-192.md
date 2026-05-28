# OTEP-192: Recurring OTG data ingestion job

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Build a scheduled job that reads the latest OTG Excel export, transforms records to match the OTEP opportunity schema, and upserts them into the database. Runs on a recurring schedule. Officers see current opportunities automatically, with no manual intervention needed. This is a non-visible backend story. There is no officer-facing UI component. Acceptance Criteria: The job runs on a defined recurring schedule.  (Cadence TBC — confirm with Engineers at Planning) Each run reads the latest OTG Excel file, stores the raw data, and loads the processed opportunity records into the database. Opportunities missing from the latest export are automatically deactivated — removed from the officer listing but kept in the database.  (Product decision: auto-deactivate — 2026-05-28) Invalid or incomplete records are skipped and logged; a bad row does not abort the run. Each run produces a summary log: records read, inserted, updated, skipped, and errors. Design note:  Structure the pipeline so a future C@G API source can be added without rewriting the transform/upsert layer.  (Open item #23)

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
