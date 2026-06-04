# OTEP-192: Recurring OTG data ingestion job

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

**Léo Milbor** (2026-06-02)
Here is temporary query that can be used to query created opportunities: select o.title
  , ot.label as type
  , a.label as agency
  , o.description
  , o.time_commitment_quantity
  , o.time_commitment_unit
  , o.apply_url
  from opportunity as o
  left join ref_agency as a on a.id = o.agency_id
  left join ref_opportunity_type as ot on ot.id = o.opportunity_type_id

---

**Léo Milbor** (2026-06-02)
As part of previous story   , here is what has been accomplished:  - An endpoint is accessible to import an excel file `POST /opportunities`  - It is append only → No update of existing opportunity  - Current excel provided by Michelle is still raising errors (72/~200 rows can be parsed), so the parsing logic might need to be updated.  - Some refactor will need to be addressed also

---

**Pow Hwee TAN (PSD)** (2026-05-28)
Scheduler and observability criteria (recurring schedule, summary logging, skip-and-log behaviour) have been split into a companion ticket OTEP-348. Suggest trimming this ticket’s AC to focus on the transform & upsert logic only: read from staging table (OTEP-313), map to opportunity schema, upsert to production table, deactivate missing records.
