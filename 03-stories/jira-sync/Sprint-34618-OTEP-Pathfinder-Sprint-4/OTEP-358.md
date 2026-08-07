# OTEP-358: [Spike] Robust nil-date handling for OTG Excel import

**Status:** Done
**Assignee:** Michelle Yip
**Story Points:** N/A

---

## Description

Question to answer What is the correct, robust approach for handling nil and invalid dates in the OTG Excel import pipeline, so the parser does not break when OTG export format changes? Context The OTG Excel parser (internal/service/opportunity/otg) hit a day out of range error on "00/01/1900" — OTG sentinel for no closing date (evergreen opportunities). Sprint 3 fix hardcodes an intercept for this specific string and maps to nil. This is fragile: any change to OTG export format or a new nil-date representation breaks the parser again. Decision (2026-05-29): Parse "00/01/1900" as nil closing date. This spike defines the permanent replacement for the hardcoded intercept. Investigation questions What date values does OTG use to represent no closing date across all report types (STIPs, Gigs, Internal Jobs)? Are there variants beyond "00/01/1900"? Could other nil-date representations appear — null cells, empty strings, N/A, TBC, Excel error values? What does the Go/Excel parsing library do natively with invalid dates? Can it be configured to return nil automatically rather than erroring? Which layer is the right home for nil-date handling — parser, mapper, or validation? Are other date fields in the OTG data model at risk of the same issue? Expected output Written recommendation: chosen approach, which layer, and rationale If implementation is straightforward within timebox: PR raised If non-trivial: follow-up engineering story added to backlog with scoped ACs Timebox 2 days Out of scope How nil closing dates appear in the UI Nil-date handling for C@G ingestion (separate pipeline) Changes to the Sprint 3 hardcoded intercept — that ships as-is

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-08-07*
