# OTEP-192: OTG data ingestion

**Status:** Done

**Assignee:** Léo Milbor

**Story Points:** N/A

---

## Description

Build a scheduled job that reads the latest OTG Excel export, transforms records to match the OTEP opportunity schema, and upserts them into the database. Runs on a recurring schedule. Officers see current opportunities automatically, with no manual intervention needed. This is a non-visible backend story. There is no officer-facing UI component. Acceptance Criteria: Each run reads the latest OTG Excel file, stores the raw data, and loads the processed opportunity records into the database. Opportunities missing from the latest export are automatically deactivated — removed from the officer listing but kept in the database.  (Product decision: auto-deactivate — 2026-05-28) Invalid or incomplete records are skipped and logged; a bad row does not abort the run. Design note:  Structure the pipeline so a future C@G API source can be added without rewriting the transform/upsert layer.  (Open item #23) Details on what is an invalid row:  an error means the row is invalid and we skip it (no  opportunity  row created in our db). A warning does not prevent the creation of the opportunity. Field Name Error/Warning opportunity type   error  agency   error  title   error  description   error  job function   warning  competencies   at least one is not found: error  application link   warning  closing date   warning

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Léo Milbor** (2026-06-10)
, here is the logic I previously implemented, error means the row is skipped, warning will still create a row, in any case,  source_otg_opportunity  is populated with  errors ,  warnings  and source row as JSONB. Field Name Error/Warning opportunity type   error  agency   error  title   error  description   error  job function   warning  competencies   warning application link   warning  closing date   warning  What you’re asking is for  competencies  to raise an error is  at least one  is not found?

---

**Michelle Yip** (2026-06-10)
Hard-skip on all fields including competencies — if any required mapped field is missing or unresolvable, skip the whole row. This is consistent with the pipeline rule confirmed with Pow Hwee on 2026-06-08. Competency matching on ingested opportunities is a separate problem that will be handled in a follow-on spike (OTEP-127). OTEP-192 can close on this basis.      any strong objections?

---

**Léo Milbor** (2026-06-05)
in the story it’s said “Invalid or incomplete records are skipped”. How rigorous should that be? As soon as one reference cannot be matched → skip the row Be more lenient on some rows (I’m thinking of competencies for instance) something else?
