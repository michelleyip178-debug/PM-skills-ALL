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
| ~~OTEP-85a~~ | ~~"Closing soon" label~~ | — | **Re-absorbed into OTEP-85 (2026-05-15); re-ticketed as OTEP-284** |
| OTEP-284 | "Closing soon" label on cards and detail page *(re-ticketed from OTEP-85a)* | — | **TBD** *(confirm if in scope for S2 or S3)* |
| OTEP-281 | Opportunity Listing — data fetching loading states | — | **TBD** |
| OTEP-282 | Opportunity Listing — truncate long opportunity titles | — | **TBD** |
| ~~OTEP-285~~ | ~~Click-through to detail + return-to-page state~~ | — | **Absorbed into OTEP-128** *(2026-05-18)* |
| OTEP-267 | Pagination for the listing page | US-01b | 2 |
| OTEP-268 | Empty/error/partial-load states | US-01c | **2** *(re-added to Sprint 2 by Pow Hwee 2026-05-18)* |
| **OTEP-276** | **[Spike] Investigate custom design system reimplementation (Thomas)** | — | **2** *(new, 2026-05-15)* |
| OTEP-295 | Mock detail endpoint for opportunity | — | **2** *(tech story, Léo)* |
| OTEP-128 | **View opportunity detail page** *(repurposed 2026-05-14 — was "type badge on card"; type badge absorbed into OTEP-85; absorbs OTEP-285)* | US-04 | **2** |
| OTEP-283 | Opportunity Detail — Ministry icons on detail page | — | **TBD** |
| OTEP-129 | **See whether an opportunity is open or closed before applying** — re-added as separate Sprint 2 story (Pow Hwee, 2026-05-18). Owns: "Closing soon" badge (within 7 days) + deep-link error state. Overrides 2026-05-14 absorption into OTEP-85. | US-06 | **2** |
| OTEP-86 | Filter opportunities by type | US-02 | **3** *(deferred from Sprint 2 — 2026-05-14, to make room for detail page)* |
| US-05 *(Jira TBD)* | Clear filters and reset view | US-05 | **3** *(deferred from Sprint 2 — 2026-05-14, pairs with OTEP-86)* |
| US-03 *(Jira TBD)* | Filter opportunities by category | US-03 | 3 |
| US-18 *(Jira TBD)* | Apply via FormSG (basic redirect) — Internal Jobs, STIPs, Gigs | — | **3** |
| OTEP-131 | Handle missing or broken FormSG application link (error state) | — | **TBD** *(pairs with US-18 / OTEP-130)* |
| ~~US-19~~ | ~~Apply via OTG redirect (SJR)~~ | — | **Dropped** — SJR apply deferred to future release; all apply flows will go through OTEP (decision 2026-05-13) |
| OTEP-127 | Apply ringfencing criteria | US-01b | 3 |
| OTEP-87 | Enhance detail page: apply CTA + competencies *(builds on OTEP-128 Sprint 2 base)* | US-08 | 3 |
| OTEP-130 | Apply to OTG opportunity via FormSG (full, with webhook) | US-09 | 4 |
| OTEP-132 | Apply for an SJR or internal job via OTG redirect | — | **TBD** |
| US-10 *(Jira TBD)* | Receive application confirmation | US-10 | 4 |
| OTEP-89 | View C@G opportunity summary | US-11 | 5 |
| OTEP-133 | ⚠️ Jira title: "Access the hub via a deep link from an EDM" — **not** "Redirect to C@G". Mapping needs verification. | US-12 | 5 |
| OTEP-88 | Understand OTG vs C@G flow difference | US-13 | 5 |
| US-07 *(Jira TBD)* | Persist filter selections | US-07 | R1 |
| OTEP-290 | Report issue button | — | **R1** |
| OTEP-196 | Bookmark opportunity | — | **R1** |
| OTEP-197 | View list of bookmarked opportunities | — | **R1** |
| US-14 *(Jira TBD)* | View my submitted applications | US-14 | TBD |
| US-15 *(Jira TBD)* | See status of individual application | US-15 | TBD |
| US-16 *(Jira TBD)* | Receive notification on status change | US-16 | TBD |
| US-17 *(Jira TBD)* | Withdraw an OTG application | US-17 | TBD |

### Edge Cases / Eligibility

| Jira ID | Title | Old PRD ID | Sprint |
|---------|-------|-----------|--------|
| OTEP-231 | Officer on temporary roles | — | **TBD** |
| OTEP-232 | Officers who are double-hatting | — | **TBD** |

### Profile Dependency (cross-pillar)

| Jira ID | Title | Old PRD ID | Sprint |
|---------|-------|-----------|--------|
| US-P1 *(Jira TBD)* | View my HR-sourced profile | US-P1 | TBD |
| US-P2 *(Jira TBD)* | View my competencies | US-P2 | TBD |
| OTEP-172 | Application form pre-filled with officer data at FormSG *(candidate for US-P3)* | US-P3 | TBD |
| OTEP-296 | Prepare defined report format matching data model *(Sprint 2 PM-owned, Michelle)* | — | **2** |

### PM/Data Stories (Sprint 2)

| Jira ID | Title | Notes |
|---------|-------|-------|
| OTEP-295 | Mock detail endpoint for opportunity | Sprint 2, Léo — already listed above under detail page row |
| OTEP-296 | Prepare defined report format matching data model | Sprint 2, Michelle — PM-owned data model |

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

## Stories still without Jira tickets (Jira TBD)

These working IDs have no matching Jira ticket in the backlog as of 2026-05-19. Raise at next grooming to confirm whether to ticket or drop.

| Working ID | Title | Status |
|---|---|---|
| US-05 | Clear filters and reset view | Sprint 3 planned, needs ticket |
| US-03 | Filter opportunities by category | Sprint 3 planned, needs ticket |
| US-18 | Apply via FormSG (basic redirect) | Sprint 3 planned, needs ticket — blocked on `formsg_url` confirmation |
| US-10 | Receive application confirmation | Sprint 4 planned, needs ticket |
| US-07 | Persist filter selections | R1, no ticket needed yet |
| US-14–17 | Application tracking stories | TBD, no ticket needed yet |
| US-P1 | View my HR-sourced profile | TBD, needs ticket |
| US-P2 | View my competencies | TBD, needs ticket |
| WOG-04 | Stay logged in during session | Sprint 3, needs ticket |
| WOG-05 | Log out of OTEP | Sprint 3, needs ticket |
| WOG-06 | First-time login experience | Sprint 3, needs ticket |
| WOG-02 | Log in as agency admin | Sprint 6, deferred |
| WOG-07 | Role-based access control | Sprint 6, deferred |

---

## When a new Jira ticket is created

1. Add the OTEP-NNN ID to this map
2. Find-and-replace the old working ID (e.g. `US-05` → `OTEP-XXX`) across all .md files
3. Stories without Jira tickets are marked *(Jira TBD)* above

---

*Updated: 2026-05-19 — Jira backlog sync: added OTEP-131, 132, 172, 196, 197, 231, 232, 281, 282, 283, 284, 290, 295, 296. Fixed OTEP-268 (re-added Sprint 2 by Pow Hwee 2026-05-18). Fixed OTEP-285 (absorbed into OTEP-128). Flagged OTEP-133 title mismatch. Added "Stories still without Jira tickets" table. Added OTEP-284 (Closing soon re-ticketed).*
