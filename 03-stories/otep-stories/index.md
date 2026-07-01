# Epic 4: Opportunities — User Stories

**Owner:** Michelle

**Epic goal:** Unified Opportunities experience with two-pipeline model (OTG + Careers@Gov)

**MVP target:** Opportunities discoverable in one place; OTG full lifecycle end-to-end; C@G deep-link handoff functional

**Status:** In Progress

---

## Story Groups

| Group | Description | Status | Link |
|-------|-------------|--------|------|
| Profile Dependency | Officer profile (HR-sourced) + competencies + pre-fill — critical path foundation | Draft | [profile-dependency.md](profile-dependency.md) |
| Discovery & Filters | Officers finding and filtering opportunities across both pipelines | Draft | [filters.md](filters.md) |
| OTG Application Lifecycle | Discovery → FormSG application → confirmation (end-to-end) | Draft | [otg-lifecycle.md](otg-lifecycle.md) |
| C@G Deep-link Handoff | Discovery on OTEP → handoff to Careers@Gov | Draft | [cag-handoff.md](cag-handoff.md) |
| Application Status Tracking | Officers tracking their OTG application status | Draft | [tracking.md](tracking.md) |

---

## All Stories (Summary)

### Profile Dependency (3 stories — cross-pillar)

| ID | Story | Priority | DoR |
|----|-------|----------|-----|
| US-P1 | View my HR-sourced profile | MVP | Pending |
| US-P2 | View my competencies | MVP | Pending |
| US-P3 | Pre-fill application from profile | MVP (if FormSG supports) / R1 (if not) | Pending |

### Discovery & Listing (5 active stories + 2 absorbed — OTEP-128 moved to OTG Lifecycle)

| ID | Story | Priority | DoR |
|----|-------|----------|-----|
| OTEP-85 | Display opportunity cards with real/mock OTG data (absorbs "Closing soon" label) | MVP | Ready |
| ~~OTEP-85a~~ | ~~"Closing soon" label~~ | — | **Re-absorbed into OTEP-85 (2026-05-15)** |
| OTEP-285 | Click-through to detail + return-to-page state | MVP | Ready (highest-risk — state architecture) |
| OTEP-267 | Pagination for the listing page | MVP | Ready |
| OTEP-268 | Empty/error/partial-load states | — | **Deferred — unticketed / unplanned (2026-05-15)** |
| OTEP-276 | [Spike] Investigate custom design system reimplementation (Thomas) | MVP (Sprint 2) | New 2026-05-15 |
| ~~OTEP-129~~ | ~~Sort by posting date~~ | — | Absorbed into OTEP-85 (2026-05-14) |
| ~~OTEP-128 (old)~~ | ~~Identify opportunity type on card~~ | — | Type badge absorbed into OTEP-85. OTEP-128 repurposed as Detail Page → OTG Lifecycle group (2026-05-14) |
| OTEP-86 | Filter opportunities by type | MVP | Sprint 3 (deferred from Sprint 2, 2026-05-14) |
| OTEP-317 | Clear filters and reset view *(was US-05)* | MVP | Sprint 3 — ticketed 2026-05-21 |
| OTEP-318 | Filter opportunities by category *(was US-03)* | MVP | Sprint 3 — ticketed 2026-05-21 (conditional on OTEP-289 spike; no Jira description yet) |
| US-07 | Persist filter selections | R1 | — |

### OTG Application Lifecycle (4 stories)

| ID | Story | Priority | DoR |
|----|-------|----------|-----|
| OTEP-128 | View opportunity detail page (Sprint 2 base) | MVP | Written 2026-05-14 |
| OTEP-87 | Enhance detail page: apply CTA only (Sprint 3, builds on OTEP-128) | MVP | ⚠️ Jira ACs include competency scope — reconcile before grooming |
| OTEP-319 | Apply via FormSG — basic redirect, Internal Jobs/STIPs/Gigs *(was US-18)* | MVP | Sprint 3 — ticketed 2026-05-21; `formsg_url` confirmed ✔ |
| OTEP-130 | Apply to an OTG opportunity via FormSG (full) | MVP | Pending |
| ~~US-10~~ | ~~Receive application confirmation~~ | — | **Dropped — scenario no longer applies (2026-06-29)** |

### C@G Deep-link Handoff (3 stories)

| ID | Story | Priority | DoR |
|----|-------|----------|-----|
| OTEP-89 | View C@G opportunity summary on OTEP | MVP | Pending |
| OTEP-133 | Redirect to Careers@Gov to apply | MVP | Pending |
| OTEP-88 | Understand the difference between OTG and C@G flows | MVP | Pending |

### Application Status Tracking (4 stories)

| ID | Story | Priority | DoR |
|----|-------|----------|-----|
| US-14 | View my submitted applications | MVP | Pending |
| US-15 | See the status of an individual application | MVP | Pending |
| US-16 | Receive notification when status changes | MVP | Pending |
| US-17 | Withdraw an OTG application | MVP | Pending |

---

## Where cut ACs live

Should-haves, good-to-haves, and R1-deferred items are pulled out of the individual story files into [deferred-acs.md](../deferred-acs.md). Story files keep must-haves only.

---

## Story Lifecycle

```
Draft here → Groom with eng → DoR met → Confluence one-pager → Jira
```

## Dropped Stories

| ID | Story | Reason | Date |
|----|-------|--------|------|
| ~~US-19~~ | ~~Apply via OTG redirect (SJR)~~ | SJR apply deferred to future release — all apply flows will go through OTEP (decision 2026-05-13) | 2026-05-13 |

## Notes

- OTEP-85 was split into OTEP-85 / OTEP-267 / OTEP-268 (2026-05-13) — original story too large for one sprint
- Story numbering is sequential across all groups (OTEP-85, OTEP-86... US-XX)
- Each group gets its own detailed file with full acceptance criteria
- This file is the index — detailed stories live in their respective group files

*Last updated: 2026-05-21 — Sprint 3 Jira sync: US-05 → OTEP-317, US-03 → OTEP-318, US-18 → OTEP-319. OTEP-87 ACs mismatch flagged (Jira scope wider than agreed). Auth stories (OTEP-71/110/304/305) in Jira Sprint 3 but should be Sprint 4+.*
