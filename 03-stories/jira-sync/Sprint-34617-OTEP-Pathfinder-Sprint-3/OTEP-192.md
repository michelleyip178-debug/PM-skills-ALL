# OTEP-192: OTG data ingestion

**Status:** QA

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

**Léo Milbor** (2026-06-05)
in the story it’s said “Invalid or incomplete records are skipped”. How rigorous should that be? As soon as one reference cannot be matched → skip the row Be more lenient on some rows (I’m thinking of competencies for instance) something else?

**Michelle Yip** (2026-06-10)
Hard-skip on all fields including competencies — if any required mapped field is missing or unresolvable, skip the whole row. Consistent with pipeline rule confirmed with Pow Hwee 2026-06-08. Competency matching on ingested opportunities is a separate concern handled in OTEP-127 (spike, S4). OTEP-192 can close on this basis.

---

**Léo Milbor** (2026-06-05)
I updated acceptance criteria to remove mentions about a recurring job or summary of insert/update/deactivate/error opportunities since the other story for these is created.

---

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

*Synced from Jira: 2026-06-10*
