# [Spike] Robust nil-date handling for OTG Excel import

**Type:** Spike
**Jira:** OTEP-358
**Status:** In Sprint 3 backlog — unassigned
**Timebox:** 2 days
**Open item:** #35

---

## Question to answer

What is the correct, robust approach for handling nil and invalid dates in the OTG Excel import pipeline, so the parser doesn't break when OTG's export format changes?

---

## Context

The OTG Excel parser (`internal/service/opportunity/otg`) hit a `day out of range` error on `"00/01/1900"` — OTG's sentinel for "no closing date" (evergreen opportunities). The Sprint 3 fix hardcodes an intercept for this specific string and maps it to `nil`. This unblocks the import but is fragile: any change to OTG's export format, or a new nil-date representation in another field, breaks the parser again.

**Decision (2026-05-29):** Parse `"00/01/1900"` as nil closing date. This spike defines the permanent replacement for the hardcoded intercept.

---

## Investigation questions

- What date values does OTG use to represent "no closing date" across all report types (STIPs, Gigs, Internal Jobs)? Are there variants beyond `"00/01/1900"`?
- Could other nil-date representations appear — null cells, empty strings, `"N/A"`, `"TBC"`, Excel error values?
- What does the Go/Excel parsing library do natively with invalid dates? Can it be configured to return `nil` automatically rather than erroring?
- Which layer is the right home for nil-date handling — parser, mapper, or validation? What are the trade-offs?
- Are other date fields in the OTG data model at risk of the same issue?

---

## Expected output

- Written recommendation: chosen handling approach, which layer, and rationale
- If implementation is straightforward within the timebox: PR raised
- If non-trivial: a follow-up engineering story added to the backlog with scoped ACs

---

## Done when

- Nil-date sentinels across all OTG report types are documented (or confirmed as just `"00/01/1900"`)
- Michelle and Léo have reviewed and agreed on the recommended approach
- Either a PR is raised, or a follow-up story is in the backlog

---

## Out of scope

- How nil closing dates appear in the UI
- Nil-date handling for C@G ingestion (separate pipeline)
- Changes to the Sprint 3 hardcoded intercept — that ships as-is

---

*Drafted: 2026-05-29 | Slack thread: Léo → Michelle, nil-date decision*
