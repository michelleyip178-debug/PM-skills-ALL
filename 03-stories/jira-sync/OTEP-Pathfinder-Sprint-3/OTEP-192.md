# OTEP-192: Design recurring job to fetch opportunities data (exclude SJRs)

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

As an  officer using OTEP,  I want  the opportunity listing to always reflect the latest OTG data,  So that  I can see newly posted opportunities and don't miss ones I'd be eligible for. Acceptance Criteria Ingestion The job reads OTG Excel exports in the standardised format defined by OTEP-296. Each row is parsed into an opportunity record and written to the  sourceOTGOpportunity  staging table (OTEP-313) as a raw JSON payload before any transformation. Records are mapped from OTG field names to the OTEP opportunity schema (OTEP-193). The job upserts records into the opportunities table — new opportunities are inserted; existing opportunities are updated if the source data has changed. Opportunity lifecycle   An opportunity is active if  closing_date > today . Records where  closing_date  is today or in the past are marked inactive and excluded from the listing — not deleted from the database.  If an opportunity present in OTEP's database is absent from the latest Excel export, it is flagged for review rather than silently deleted.  (Confirm with Pow Hwee: flag vs. auto-deactivate.)  Validation and error handling   Required fields:  closing_date ,  formsg_url  (for STIPs, Gigs, Internal Jobs), opportunity type. Records missing required fields are skipped and logged with a reason.  If a record fails validation, the job continues processing remaining records. A single bad row does not abort the run.  The job produces a run log for each execution: total records read, inserted, updated, skipped, and errors with reasons.  Schedule   The job runs on a defined recurring schedule.  (Cadence TBC — confirm with Pow Hwee and Rama: how frequently does OTG publish updated exports?)  Extensibility   The ingestion pipeline is structured so that a future C@G API source can be added without rewriting the transform/upsert layer.  (Open item #23 — harmonised model for OTG + C@G.)  Open Questions (resolve before build starts) Question Owner Impact How does the Excel file arrive — pushed to a path, manual upload, SFTP, other? Pow Hwee + Rama Determines job trigger mechanism What is the ingestion cadence? Pow Hwee + Rama Determines scheduler config If an opportunity disappears from the export: flag for review or auto-deactivate? Pow Hwee Affects AC 6 and data integrity Does the job need alerting on failure? (Slack, email, oncall) Pow Hwee Affects operational runbook Is open item #23 (harmonised OTG + C@G model) resolved by OTEP-193? Léo Affects extensibility AC 11  Out of Scope C@G API ingestion — separate story, future sprint Officer-facing UI — this is a backend pipeline only Pre-processing of the Excel file before it reaches OTEP (received as-is from OTG)  Dependencies OTEP-193  ✅ Done — Léo: opportunity data model (DB schema + Go structs) OTEP-313  🔄 In Progress — Léo:  sourceOTGOpportunity  raw staging table (sub-task of this story) OTEP-296  ✅ Done — Michelle: standardised OTG Excel report format (sample files shared 2026-05-18) OTEP-85  — listing page has no live data until this job runs Subtasks OTEP-313 — OTG raw ingest table and source model (Léo, In Progress)

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
