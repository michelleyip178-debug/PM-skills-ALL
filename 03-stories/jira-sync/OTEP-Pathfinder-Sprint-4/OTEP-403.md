# OTEP-403: OTG data import hardening

**Type:** Story

**Status:** Backlog

**Assignee:** Léo Milbor

**Story Points:** N/A

**Sprint:** OTEP-Pathfinder Sprint 4

---

## Description

**Context (from Léo, 2026-06-10):**
Current limitations in the ingestion pipeline:
- Concurrent execution is not catered for — no locking mechanism to prevent two import runs from running simultaneously
- No way to tie an import attempt to its corresponding `source_otg_opportunity` row
- No tracing or metrics, only basic default endpoint logging

For concurrency: OTEP currently runs a single instance of otep-service, but this is not guaranteed to stay true. A PostgreSQL locking mechanism is proposed to force sequential operation without pulling in a queuing dependency. To be implemented in `otg_importer`.

**Product hardening scope (Michelle, 2026-06-10):**
Beyond concurrency, this ticket also covers pipeline resilience against malformed or unexpected OTG Excel inputs:

**Acceptance Criteria:**

1. **Malformed Excel file — pipeline does not crash.** If the OTG Excel file is structurally invalid, the pipeline exits cleanly with an error log. The most recently imported valid data remains in the database untouched.
2. **Unexpected column schema — pipeline does not crash.** If the OTG export adds, removes, or renames a column, the pipeline logs a warning and continues processing rows it can map. It does not crash on a missing column.
3. **Nil and invalid date handling — permanent fix in place.** Following OTEP-358 spike output: the hardcoded "00/01/1900" intercept is replaced with the permanent approach. All nil-date representations are handled consistently.
4. **Unrecognised type prefix — skip and log, do not crash.** Unrecognised GigName prefixes are hard-skipped with a log entry. Consistent with the unrecognised type decision (2026-06-04).
5. **Malformed formsg_url — skip and log.** If `formsg_url` is present but not a valid URL, the row is hard-skipped with a log entry.
6. **Concurrent import protection.** A PostgreSQL locking mechanism prevents two simultaneous import runs. If a lock cannot be acquired, the second run exits cleanly with a log entry.
7. **Run log captures hardening events.** The per-run summary log includes a count of rows skipped per hardening rule, distinct from rows skipped for missing required fields.

**Out of scope:**
- Changes to the hard-skip rule for required fields (OTEP-192, now closed)
- Per-agency skip reports visible to agencies (S5/S6)
- C@G ingestion hardening (separate pipeline)

**Dependencies:**
- OTEP-192 (closed) — builds on the established skip-and-log pattern
- OTEP-358 spike output — AC3 implements the spike recommendation; confirm output with Léo before starting AC3

**Open question before grooming:**
- What is the file size threshold for oversized file handling? Confirm with Léo based on current OTG export size.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Léo Milbor** (2026-06-10)
I added this story to highlight current limitations and possible solutions.

*Synced from Jira: 2026-06-10*
