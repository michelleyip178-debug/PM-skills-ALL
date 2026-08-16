# OTEP-88: C@G opportunities in the listing page

**Status:** Done
**Assignee:** Léo Milbor
**Story Points:** 5
**Sprint:** OTEP-Pathfinder Sprint 8 (34622)

---

## Description

User story: As an officer, I want to see Careers@Gov opportunities alongside OTG opportunities in the listing, so I can discover all available roles in one place without switching portals. Acceptance Criteria: Data ingestion — C@G opportunities are ingested via the C@G data pipeline and returned by the listing API alongside OTG opportunities. Requires source field and agency field exposed in API (OTEP-374). C@G badge on card — each C@G card displays a Careers@Gov badge, visible without hover or click. Badge design per Amber spec. Card fields — C@G cards render: title, agency, opportunity type, closing date. Same card layout as OTG. Graceful degradation — if a required field is missing from the C@G payload, the card renders with available fields and does not break the listing. Fallback behaviour TBC with Pow Hwee + Amber on Mon 8 Jun. Listing behaviour consistent — pagination, type filter (OTEP-86), and empty/error states apply to C@G results in the same way as OTG results. Out of scope — C@G detail page content (OTEP-87) and apply deep-link (OTEP-89) are not part of this ticket. Dependencies: OTEP-374 (BE: source + agency fields in listing API), C@G ingestion confirmed live for S4. Open items (confirm Mon 8 Jun with Pow Hwee + Amber): AC4 fallback behaviour (hide field / show placeholder / drop card entirely), AC2 badge spec (visual treatment).

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-375 | Add Careers@Gov badge/metadata to OpportunityCard | Done |
| OTEP-374 | Expose source and agency fields in listing API | Done |
| OTEP-482 | Import C@G opportunities | Done |
| OTEP-539 | Make C@G import run as a background task | Done |
| OTEP-536 | update frontend filters for `jobs` | Done |
| OTEP-666 | Enable scheduled trigger of import | Done |
| OTEP-723 | CAG - Integration testing | Done |

---

## Latest Comments

**Rathika Ramalingam** (2026-08-11)
Test cases covered here -

---

**Pow Hwee TAN (PSD)** (2026-06-02)
Hi   , this ticket should be the actual listing page for Careers@Gov opportunities. Right now it is only saying to differentiate the flows. Could you please revise the description and scope to reflect that this will be the actual C@G Opportunities listing page? I have updated the title accordingly.

---

**Pow Hwee TAN (PSD)** (2026-05-28)
AC is clear on the UI requirement (label on card, visible without hover). Missing: where does C@G data come from? Is there a dependency on a C@G ingest pipeline or data source? Suggest noting the data dependency so this isn’t blocked at implementation time.

---
*Synced from Jira: 2026-08-17*
