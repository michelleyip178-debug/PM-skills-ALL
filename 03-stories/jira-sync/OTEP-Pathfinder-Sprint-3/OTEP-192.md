# OTEP-192: Design recurring job to fetch opportunities data

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## User Story

**As an** officer using OTEP,
**I want** the opportunity listing to always reflect the latest OTG data,
**So that** I can see newly posted opportunities and don't miss ones I'd be eligible for.

---

## Acceptance Criteria

- [ ] A recurring job runs on a defined schedule to process the latest OTG Excel exports. *(Cadence TBD — confirm with Pow Hwee at grooming)*
- [ ] On each run, the job reads the designated OTG Excel reports (STIPs, Gigs, SJRs, Internal Jobs) and upserts opportunity records into the OTEP database.
- [ ] New opportunities in the export are added to the listing.
- [ ] Existing opportunities with changed fields are updated in the listing.
- [ ] Opportunities past their `closing_date` are marked as closed — not deleted.
- [ ] Records missing any mandatory field (ID, Title, Agency, Type, Posting Date, or Closing Date) are silently dropped and do not appear in the listing.
- [ ] Each dropped record is logged with the reason (which field was missing), so the team can track OTG data quality issues.
- [ ] Dropping bad records does not affect valid records in the same run.
- [ ] If the entire job fails, existing opportunity data in OTEP is unchanged.
- [ ] Each run logs: records processed, records upserted, records dropped, and errors.

---

## Open Questions

1. What is the job cadence — daily at a fixed time, or triggered by a file drop in S3?
2. How does the Excel file arrive — manually uploaded to a known location, or pushed by OTG?
3. Retry logic on failure — automatic retry, or manual re-trigger?

---

## Dependencies

- OTEP-193 — data model must be finalised before ingestion job can write to it
- OTG Excel reports specified (open item #24 resolved, 2026-05-18)

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
