# Scoping Gaps Tracker: OTEP Opportunities (Epic 4)

**Last updated:** 2026-05-11
**Target:** All items resolved or formally deferred to R1
**Alignment needed:** Mark, Adrian, Jacky, Xian Zhang

> **This is the analysis layer** — what's still undefined in the Epic 4 spec, which category it sits in, and which gaps have been formally deferred to R1. It pairs with the PRD (Section 11).
> Anything being actively chased (owner, deadline, status) is tracked in [open-items.md](../../00-hub/open-items.md) — the rows below *link* to it rather than copying it. A live item has one home: open-items.

---

## Summary

| Status | Count |
|--------|-------|
| Open | 9 |
| Resolved | 1 |
| Deferred to R1 | 3 |
| **Total** | **13** |

---

## Gap Items

| # | Gap Item | Category | Status | Chase / resolution |
|---|----------|----------|--------|--------------------|
| 1 | OTG → OTEP data pipeline: no ACs for sync frequency, schema mapping, failure handling — ~~and several export fields unconfirmed~~ | Technical | Open | All 6 OTG field confirmations resolved: #1 `eligibility` not needed, #2 `formsg_url` confirmed for Internal Jobs/STIPs/Gigs \u2014 SJRs excluded (2026-05-21), #3 `closing_date` confirmed, #4 `is_published` doesn't exist, #5 `reporting_line` not available, #6 `developmental_outcome` confirmed. Pipeline ACs: write the story before Sprint 2. |
| 2 | Careers@Gov → OTEP ingestion method unconfirmed (API vs manual feed) | Technical | Open | → open-items #11 (Pow Hwee, by end Sprint 1). OTEP-89/OTEP-133 assume C@G data already in OTEP. |
| 3 | Email/notification service: US-10 references submission email; OTEP-133 references email with deep-link — existing platform service or new build? | Technical | Open | → open-items #15 (Pow Hwee) |
| 4 | Search indexing infrastructure: OTEP-86 assumes elastic matching | Technical | Open | → open-items #16 (Pow Hwee) — story or spike before Sprint 3 |
| 5 | Opportunity lifecycle (admin): who/what marks opportunities closed? Date-driven or manual? | Operational | Open | → open-items #17 (Michelle / Pow Hwee). Impacts OTEP-129. |
| 6 | Officer competency data model: where does opportunity competency data come from? Part of OTG export? | Technical | Open | → open-items #18 (Pow Hwee). Impacts US-P2 and detail pages. |
| 7 | Function/Job function taxonomy mismatch: OTG and C@G use different category systems | Technical | Open | Hybrid model (Option C) recommended — see [categorisation-research.md](research/categorisation-research.md). Mapping deferred to R1 (decision 2026-05-06, see decisions-log). Not an active chase — needs validation with Amber/Adrian/Jacky. |
| 8 | Secondment vs SJR classification: distinct type or sub-type? | Stakeholder | Resolved | Secondment subsumed under SJR — no separate filter value. Resolved 2026-05-13 via Jacky (BO). |
| 9 | Target launch date: Sep 2026 (sprint plan) vs Dec 2026 (brief/Confluence) | Stakeholder | Open | → open-items #13 (Michelle / Adrian). Align with steering. |
| 10 | FormSG pre-fill support: does FormSG accept URL params or API for pre-fill? | Technical | Open | → open-items #14 (Pow Hwee). Determines whether US-P3 is MVP or R1. |
| 11 | Competency match ratio display on detail page | Technical | Deferred to R1 | Decision 2026-05-08. MVP shows "What you'll develop" tags only, no scoring. |
| 12 | Auto-populate OTG form fields from POCDEX | Technical | Deferred to R1 | Keep FormSG as-is for MVP; revisit when pre-fill mechanism confirmed (links to #10). |
| 13 | Persist filter selections across sessions (US-07) | Design | Deferred to R1 | Decision 2026-05-08. Not required for the "discoverable in one place" target. |

---

## Categories

- **Technical** — Engineering unknowns, integration dependencies, data migration questions
- **Design** — UX gaps, unresolved interaction patterns, accessibility concerns
- **Stakeholder** — Misalignment on scope, success criteria, or priorities
- **Operational** — Process, rollout, support readiness, training gaps

---

## Review Cadence

Reviewed monthly (per PM cadence). Next review: end of May 2026.
At each review: pull the live status of each linked item from [open-items.md](../../00-hub/open-items.md), confirm nothing new should be added here, and check whether any "Open" gap should now be formally deferred to R1.

---

## Notes

_Use this space for context on tricky items, escalation history, or steering-level decisions._
