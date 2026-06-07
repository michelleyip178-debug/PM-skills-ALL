# OTEP-192: Recurring OTG data ingestion job

**Status:** In Progress

**Assignee:** Léo Milbor

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

---

## PM Analysis (2026-06-05)

### What Léo’s SQL confirms

The query joins `opportunity` → `ref_opportunity_type` → `ref_agency` and exposes: title, type, agency, description, time_commitment_quantity, time_commitment_unit, apply_url.

**Schema observations:**
- `apply_url` is present — confirms the data model supports OTEP-319 (FormSG redirect). Good.
- `time_commitment_quantity` and `time_commitment_unit` are separate columns, not a single string. FE will need to concatenate (e.g. "3 months") — flag for Thomas / Amber card spec.
- Agency and type are lookup tables (`ref_agency`, `ref_opportunity_type`), not free text. A new opportunity type or agency not in the ref tables won’t render on cards.

**Critical fields missing from this query:**
- `closing_date` — required for OTEP-85 (SGT timezone AC) and OTEP-284 (Closing soon label). Not in query. Either not ingested yet or omitted from the validation query.
- `posting_date` — Rathika’s OTEP-85 test case 4 (sort by posting date) depends on this. Not in query.
- `source` field — needed for OTEP-88 C@G badge differentiation. Absent, consistent with OTEP-374 being unstarted.

### AC gaps vs current state

| AC | Status | Gap |
|----|--------|-----|
| Reads OTG Excel + loads to DB | Partial | 72/~200 rows parse. ~128 rows failing — Excel format inconsistencies or parser too strict. |
| Upsert (update existing records) | Not done | Append-only. AC requires upsert; deactivation of missing records also not implemented. |
| Skip invalid rows, don’t abort | Unknown | Errors raised but unclear if run aborts or continues. |
| Scheduler (recurring) | Split to OTEP-348 | Out of scope for this ticket per Pow Hwee. |
| Summary log per run | Split to OTEP-348 | Out of scope for this ticket per Pow Hwee. |

### Open questions for Léo

1. Are `closing_date` and `posting_date` in the schema but just omitted from the validation query, or not ingested yet?
2. Which rows in Michelle’s Excel are failing — can you share the error log so the source data can be fixed?
3. Is upsert + deactivation your next task on this ticket, or is something else blocking?
4. Does the current pipeline structure support adding a C@G source without rewriting the transform layer (design note in AC)?

---

*Synced from Jira: 2026-06-05*
