# Story ID Map

**Jira project key:** OTEP
**Canonical IDs:** Jira OTEP-NNN. Stories without Jira tickets keep working IDs (US-XX, WOG-XX) until ticketed.
**Sprint column mirrors [sprint-allocation.md](../sprint-allocation.md)** — that's the source of truth for which sprint a story is in. When a story moves, change it there first, then update the Sprint column here.

---

**Sprint checklists and DoR blockers:** [sprint-checklists.md](sprint-checklists.md)
**Deferred ACs (should-have / good-to-have / R1):** [deferred-acs.md](deferred-acs.md)

---

## All Stories — Opportunities (Epic 4)

| Jira ID | Title | Old PRD ID | Sprint |
|---------|-------|-----------|--------|
| ~~OTEP-85~~ | ~~View all opportunities in one place~~ | US-01 | **Split** → OTEP-85 / 267 / 268 (2026-05-13) |
| OTEP-85 | Display opportunity cards with real/mock OTG data (absorbs OTEP-129 sort, old OTEP-128 type badge, and "Closing soon" label formerly OTEP-85a) | US-01a | 2 |
| ~~OTEP-85a~~ | ~~"Closing soon" label~~ | — | **Re-absorbed into OTEP-85 (2026-05-15)** |
| OTEP-285 | Click-through to detail + return-to-page state (renamed from OTEP-85b on 2026-05-15 when ticketed) | — | 2 |
| OTEP-267 | Pagination for the listing page | US-01b | 2 |
| OTEP-268 | Empty/error/partial-load states | US-01c | **Deferred — unticketed / unplanned (2026-05-15)** |
| **OTEP-276** | **[Spike] Investigate custom design system reimplementation (Thomas)** | — | **2** *(new, 2026-05-15)* |
| OTEP-128 | **View opportunity detail page** *(repurposed 2026-05-14 — was "type badge on card"; type badge absorbed into OTEP-85)* | US-04 | **2** |
| OTEP-129 | ~~Sort by posting date~~ → **fully absorbed into OTEP-85** (sort, interleave, "Closing soon" label). Closed. | US-06 | **Absorbed** (2026-05-14) |
| OTEP-86 | Filter opportunities by type | US-02 | **3** *(deferred from Sprint 2 — 2026-05-14, to make room for detail page)* |
| US-05 *(Jira TBD)* | Clear filters and reset view | US-05 | **3** *(deferred from Sprint 2 — 2026-05-14, pairs with OTEP-86)* |
| US-18 *(Jira TBD)* | Apply via FormSG (basic redirect) — Internal Jobs, STIPs, Gigs | — | **3** |
| ~~US-19~~ | ~~Apply via OTG redirect (SJR)~~ | — | **Dropped** — SJR apply deferred to future release; all apply flows will go through OTEP (decision 2026-05-13) |
| OTEP-127 | Apply ringfencing criteria | US-01b | 3 |
| US-03 *(Jira TBD)* | Filter opportunities by category | US-03 | 3 |
| OTEP-87 | Enhance detail page: apply CTA + competencies *(builds on OTEP-128 Sprint 2 base)* | US-08 | 3 |
| OTEP-130 | Apply to OTG opportunity via FormSG (full) | US-09 | 4 |
| US-10 *(Jira TBD)* | Receive application confirmation | US-10 | 4 |
| OTEP-89 | View C@G opportunity summary | US-11 | 5 |
| OTEP-133 | Redirect to Careers@Gov to apply | US-12 | 5 |
| OTEP-88 | Understand OTG vs C@G flow difference | US-13 | 5 |
| US-07 *(Jira TBD)* | Persist filter selections | US-07 | R1 |
| US-14 *(Jira TBD)* | View my submitted applications | US-14 | TBD |
| US-15 *(Jira TBD)* | See status of individual application | US-15 | TBD |
| US-16 *(Jira TBD)* | Receive notification on status change | US-16 | TBD |
| US-17 *(Jira TBD)* | Withdraw an OTG application | US-17 | TBD |

### Profile Dependency (cross-pillar)

| Jira ID | Title | Old PRD ID | Sprint |
|---------|-------|-----------|--------|
| US-P1 *(Jira TBD)* | View my HR-sourced profile | US-P1 | TBD |
| US-P2 *(Jira TBD)* | View my competencies | US-P2 | TBD |
| US-P3 *(Jira TBD)* | Pre-fill application from profile | US-P3 | R1 (unless FormSG supports) |

## All Stories — Auth (WOG AD — Epic 5)

| Jira ID | Title | Old ID | Sprint |
|---------|-------|--------|--------|
| OTEP-71 | Login Authentication (parent) | OTEP-71a | **3** *(tracked separately — not in Sprint 2 confirmed scope)* |
| *(subtask of OTEP-71)* | WOGAD token handling | OTEP-71b | **3** |
| *(subtask of OTEP-71)* | WOGAD session management | OTEP-71c | **3** |
| *(subtask of OTEP-71)* | Login UI + error states | OTEP-71d | **3** |
| OTEP-111 | Officers with no access | OTEP-71e | 1 |
| OTEP-72 | New Officer account creation | OTEP-72 | 1 |
| OTEP-110 | Login fail / clear error | WOG-03 | **3** *(deferred from Sprint 2 — capacity review 2026-05-13)* |
| WOG-04 *(Jira TBD)* | Stay logged in during session | WOG-04 | **3** *(or S1 carry-over)* |
| WOG-05 *(Jira TBD)* | Log out of OTEP | WOG-05 | **3** *(or S1 carry-over)* |
| WOG-06 *(Jira TBD)* | First-time login experience | WOG-06 | **3** *(or S1 carry-over)* |
| WOG-02 *(Jira TBD)* | Log in as agency admin (deferred) | WOG-02 | 6 |
| WOG-07 *(Jira TBD)* | Role-based access control (deferred) | WOG-07 | 6 |

---

## When a new Jira ticket is created

1. Add the OTEP-NNN ID to this map
2. Find-and-replace the old working ID (e.g. `US-05` → `OTEP-XXX`) across all .md files
3. Stories without Jira tickets are marked *(Jira TBD)* above

---

*Updated: 2026-05-15 — Sprint 2 Jira reconciliation: OTEP-85b renamed to OTEP-285 (now ticketed); OTEP-85a re-absorbed into OTEP-85; OTEP-268 deferred unticketed; OTEP-276 added (design system spike, Thomas).*
