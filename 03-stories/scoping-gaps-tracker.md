# Scoping Gaps Tracker: OTEP Opportunities (Epic 4)

**Last updated:** 2026-05-29

**Target:** All items resolved or formally deferred to R1

**Alignment needed:** Mark, Adrian, Jacky, Xian Zhang

> **This is the analysis layer** — what's still undefined in the Epic 4 spec, which category it sits in, and which gaps have been formally deferred to R1. It pairs with the PRD (Section 11).
> Anything being actively chased (owner, deadline, status) is tracked in [open-items.md](../../00-hub/open-items.md) — the rows below *link* to it rather than copying it. A live item has one home: open-items.

---

## Summary

| Status | Count |
|--------|-------|
| Open | 7 |
| Resolved | 5 |
| Deferred to R1 | 3 |
| **Total** | **15** |

---

## Gap Items

| # | Gap Item | Category | Status | Chase / resolution |
|---|----------|----------|--------|--------------------|
| 1 | OTG → OTEP data pipeline: no ACs for sync frequency, schema mapping, failure handling — ~~and several export fields unconfirmed~~ | Technical | Open | All 6 OTG field confirmations resolved: #1 `eligibility` not needed, #2 `formsg_url` confirmed for Internal Jobs/STIPs/Gigs \u2014 SJRs excluded (2026-05-21), #3 `closing_date` confirmed, #4 `is_published` doesn't exist, #5 `reporting_line` not available, #6 `developmental_outcome` confirmed. Pipeline ACs: write the story before Sprint 2. |
| 2 | Careers@Gov → OTEP ingestion method unconfirmed (API vs manual feed) | Technical | Resolved | C@G ingestion = API confirmed. Resolved via open-items #11 (2026-05-14). |
| 3 | Email/notification service: US-10 references submission email; OTEP-133 references email with deep-link — existing platform service or new build? | Technical | Open | → open-items #15 (Pow Hwee) |
| 4 | Search indexing infrastructure: OTEP-86 assumes elastic matching | Technical | Open | → open-items #16 (Pow Hwee) — story or spike before Sprint 3 |
| 5 | Opportunity lifecycle (admin): who/what marks opportunities closed? Date-driven or manual? | Operational | Resolved | Date-driven — `closing_date > today`. Resolved via open-items #17 (2026-05-13). |
| 6 | Officer competency data model: where does opportunity competency data come from? Part of OTG export? | Technical | Open | → open-items #18 (Pow Hwee). Impacts US-P2 and detail pages. |
| 7 | Function/Job function taxonomy mismatch: OTG and C@G use different category systems | Technical | Open | Hybrid model (Option C) recommended — see [categorisation-research.md](research/categorisation-research.md). Mapping deferred to R1 (decision 2026-05-06, see decisions-log). Not an active chase — needs validation with Amber/Adrian/Jacky. |
| 8 | Secondment vs SJR classification: distinct type or sub-type? | Stakeholder | Resolved | Secondment subsumed under SJR — no separate filter value. Resolved 2026-05-13 via Jacky (BO). |
| 9 | Target launch date: Sep 2026 (sprint plan) vs Dec 2026 (brief/Confluence) | Stakeholder | Resolved | Go-live confirmed Fri 16 Oct 2026. Resolved via open-items #13 (2026-05-12). |
| 10 | FormSG pre-fill support: does FormSG accept URL params or API for pre-fill? | Technical | Resolved | Pre-fill deferred to R1 (Squad-Sync 2026-05-26). Question moot for MVP. Resolved via open-items #14. |
| 11 | Competency match ratio display on detail page | Technical | Deferred to R1 | Decision 2026-05-08. MVP shows "What you'll develop" tags only, no scoring. |
| 12 | Auto-populate OTG form fields from POCDEX | Technical | Deferred to R1 | Keep FormSG as-is for MVP; revisit when pre-fill mechanism confirmed (links to #10). |
| 13 | Persist filter selections across sessions (US-07) | Design | Deferred to R1 | Decision 2026-05-08. Not required for the "discoverable in one place" target. |
| 14 | POCDEX → Compass sync cadence and data-currency model unconfirmed — is it near-real-time push (per POCDEX Integration PRD assumption) or gated by upstream HR systems' daily update to POCDEX (per 2026-07-08 conversation)? Also unconfirmed: whether POCDEX carries future-dated (effective-start-date) records or is current-state only, and per-field refresh cadence (name/email/agency/competencies may not all refresh together) | Technical | Open | → open-items #56 (Imelda / Rama for data-domain side; Daryll for platform/SLA side — see [POCDEX sync lag, open-items #31/#55] for the related platform-side thread already tracked). Impacts POCDEX Authorisation epic's unfiltered-listing fallback sizing (OTEP-337) — if sync is daily rather than near-real-time, more Day-1 officers may hit the fallback state than currently assumed. |
| 15 | OTEP-594 (routing after auth) re-scope — **all three named decisions resolved 2026-07-08**, traced from [otep-stories/auth.md](otep-stories/auth.md): ~~**#7** — OTEP-111/OTEP-594 boundary~~ **RESOLVED** — "pilot agency, no POCDEX profile yet" shows its own system-error state, not OTEP-111's unauthorised page; ~~**#8** — system-error copy + 2-day retry assumption + screen existence~~ **RESOLVED (two parts)** — copy revised to generic wording ("try again shortly," decoupled from gap #14 / open-items #56's sync-cadence question); screen confirmed **not built yet**; ~~**#9** — auto-log-to-report-issue ownership~~ **RESOLVED** — no auto-logging, officer-clicked "Report issue" CTA instead (simplifies original ownership question; small follow-up on post-click routing/triage owner, not a blocker). AC rewritten directly in Jira 2026-07-08 to reflect all three resolutions — clean, no decision-number references or unconfirmed assumptions left in the ticket text. A fourth item, **decision #11** (route-guard NFR — direct URL access without a session), is also named in OTEP-594's AC but is independently buildable and doesn't block on #7/#8/#9 — see Sprint 6 test scenarios Scenario 17. | Technical | Open (decisions resolved; screen not built) | **Re-scope complete.** Remaining gap is pure build work — the system-error screen (design + copy + CTA all settled) doesn't exist yet. **Decision 2026-07-08: keep as one ticket** — the screen build stays inside OTEP-594 rather than splitting into a separate story. Not committed to Sprint 6 (13–26 Jul) until built and tested. Test coverage in [sprint6-test-scenarios.md](../../PM-OS/outputs/analyses/2026-07-08-W28-sprint6-test-scenarios.md) (Scenarios 14–17). |

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
