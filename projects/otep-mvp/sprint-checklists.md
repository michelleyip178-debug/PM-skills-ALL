# Sprint Checklists

Per-story grooming readiness and DoR blockers, per sprint. **Which stories are in which sprint comes from [sprint-allocation.md](../sprint-allocation.md)** — this file tracks readiness, not assignment. Updated each sprint.

**Cut ACs (should-have, good-to-have, R1) live in [deferred-acs.md](deferred-acs.md).** Pull from there at grooming when capacity allows.

---

## Sprint 2 — Opportunities Listing Hub

**Sprint dates:** 18 May – 29 May 2026
**Sprint goal:** Officers can browse and filter every OTG opportunity on a single authenticated page, newest first, published-only.

### Stories (5 stories — reconciled against Jira Sprint 2 board 2026-05-15)

| ID | Title | Story file | Grooming-ready? |
|---|---|---|---|
| OTEP-85 | Display opportunity cards with real/mock OTG data | [filters.md](stories/filters.md) | Ready — rendering foundation. Absorbs "Closing soon" label (formerly OTEP-85a). Field rendering rules defined. Loading state AC added. **Must ship first.** |
| OTEP-285 | Click-through to detail + return-to-page | [filters.md](stories/filters.md) | Ready — split from OTEP-85. **Highest-risk story** (state persistence architecture). Needs contract sync decision. |
| OTEP-128 | View opportunity detail page | [otg-lifecycle.md](stories/otg-lifecycle.md) | Ready — Loading state AC added. |
| OTEP-267 | Pagination for listing page | [filters.md](stories/filters.md) | Ready — page indicator promoted to must-have. Hidden-on-empty AC added. |
| OTEP-276 | [Spike] Investigate custom design system reimplementation | — | New 2026-05-15. Thomas owns. Confirms or replaces LifeSG as base. AC to be drafted. |

**Absorbed:** ~~OTEP-129~~ (sort + type interleave) → into OTEP-85. ~~Old OTEP-128~~ (type badge) → into OTEP-85. ~~OTEP-85a~~ ("Closing soon") → re-absorbed into OTEP-85 (2026-05-15).
**Removed from Sprint 2 (2026-05-15):** OTEP-268 (empty/error/partial states) — deferred / unticketed / unplanned.
**Deferred to Sprint 3 (2026-05-14):** OTEP-86 (type filter) + US-05 (clear filters) — to make room for detail page.
**Also Sprint 3:** US-18 (apply via FormSG), OTEP-127 (ringfencing), auth edge-cases (OTEP-110, WOG-04/05/06).
**Dropped:** ~~US-19~~ (SJR apply deferred — decision 2026-05-13).
**Not in Sprint 2:** C@G data, US-03 category filter, search.

### DoR Blockers (Sprint 2)

- [x] ~~Amber's card + filter UI + pagination + empty/error state designs finalised~~ — **resolved 2026-05-13**
- [x] ~~Rama confirms `closing_date` vs `end_date` (open item #3)~~ — **resolved 2026-05-13:** `closing_date` = application closing date. "Closing soon" label unblocked.
- [x] ~~Rama confirms `is_published` field name + values (open item #4)~~ — **resolved 2026-05-13:** field doesn't exist. Visibility = `closing_date` > today.
- [x] ~~Jacky confirms Secondment classification (open item #12)~~ — **resolved 2026-05-13:** subsumed under SJR. No separate type.
- [ ] OTG file import testable with real Excel data — OTG has no API; data comes via Excel reports (decided 2026-05-14). Depends on open item #24 (which reports to ingest).
- [ ] Listing-endpoint API contract documented (Pow Hwee) — OTEP-85 subtask #1. This is OTEP's internal API (frontend ↔ backend), not OTG ingestion.
- [x] ~~Sort key confirmed~~ — `posting_date`, newest first (Michelle)

---

## Sprint 3 — Apply Routing, Detail Pages, Personalisation

**Sprint dates:** 2 Jun – 13 Jun 2026
**Sprint goal:** *(TBD — populate at Sprint 2 mid-point)*

### Stories (provisional — from story-id-map + Sprint 2 deferrals)

| ID | Title | Story file | Grooming-ready? |
|---|---|---|---|
| OTEP-86 | Filter opportunities by type | [filters.md](stories/filters.md) | Written + tiered. Deferred from Sprint 2 (2026-05-14). Design finalised. |
| US-05 | Clear filters and reset view | [filters.md](stories/filters.md) | Written + tiered. Pairs with OTEP-86. |
| US-18 *(Jira TBD)* | Apply via FormSG (basic redirect) — Internal Jobs, STIPs, Gigs | [otg-lifecycle.md](stories/otg-lifecycle.md) | Written. Blocked on `formsg_url` (Rama, open item #2). |
| OTEP-87 | Enhance detail page: apply CTA + competencies | [otg-lifecycle.md](stories/otg-lifecycle.md) | Updated 2026-05-14. Builds on OTEP-128 (Sprint 2 base). Only Sprint 3 additions: apply CTA, SJR treatment, competencies. |
| OTEP-127 | Apply ringfencing criteria | [filters.md](stories/filters.md) | Not started |
| US-03 | Filter opportunities by category | [filters.md](stories/filters.md) | Blocked on categorisation research |
| OTEP-110 | Login fail / clear error | [auth.md](stories/auth.md) | Sprint 3 or Sprint 1 carry-over — confirm at finalisation Fri 15 May |
| WOG-04 *(Jira TBD)* | Stay logged in during session | [auth.md](stories/auth.md) | Same as above |
| WOG-05 *(Jira TBD)* | Log out of OTEP | [auth.md](stories/auth.md) | Same as above |
| WOG-06 *(Jira TBD)* | First-time login experience | [auth.md](stories/auth.md) | Same as above |

**Deferred from Sprint 2 (2026-05-14):** OTEP-86 (type filter) + US-05 (clear filters) — to make room for OTEP-128 (detail page).
**Dropped from Sprint 3:** ~~US-19~~ (SJR apply deferred — decision 2026-05-13).

### DoR Blockers

- [ ] Rama confirms `formsg_url` field name and structure (open item #2) — gates US-18. **Last unconfirmed OTG field.**
- [ ] Categorisation hybrid model validated (Amber, Pow Hwee, Adrian, Jacky/XZ) — gates US-03
- [ ] Auth edge-case stories reviewed and sharpened — confirm scope at Sprint 1 finalisation
- [x] ~~Amber's detail page designs for OTEP-87 (including SJR card treatment without apply action)~~ — **resolved 2026-05-13**
- [x] ~~Opportunity lifecycle (open item #17)~~ — **resolved 2026-05-13:** date-driven, `closing_date` > today. Pow Hwee agreed.

---

## Sprint 4 — Application Routes End-to-End

**Sprint dates:** 16 Jun – 27 Jun 2026
**Sprint goal:** *(TBD)*

### Stories (provisional from story-id-map)

| ID | Title | Story file | Grooming-ready? |
|---|---|---|---|
| OTEP-130 | Apply to OTG opportunity via FormSG (full) | [otg-lifecycle.md](stories/otg-lifecycle.md) | Draft |
| US-10 | Receive application confirmation | [otg-lifecycle.md](stories/otg-lifecycle.md) | Draft |

### DoR Blockers

*(To be populated during Sprint 3)*

---

## Sprint 5 — C@G Handoff, Integration Testing, Polish

**Sprint dates:** 30 Jun – 11 Jul 2026
**Sprint goal:** *(TBD)*

### Stories (provisional from story-id-map)

| ID | Title | Story file | Grooming-ready? |
|---|---|---|---|
| OTEP-89 | View C@G opportunity summary | [cag-handoff.md](stories/cag-handoff.md) | Draft |
| OTEP-133 | Redirect to Careers@Gov to apply | [cag-handoff.md](stories/cag-handoff.md) | Draft |
| OTEP-88 | Understand OTG vs C@G flow difference | [cag-handoff.md](stories/cag-handoff.md) | Draft |

### DoR Blockers

*(To be populated during Sprint 4)*

---

*Updated: 2026-05-13*
