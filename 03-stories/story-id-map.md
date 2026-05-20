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
| OTEP-129 | ~~Sort by posting date~~ → **fully absorbed into OTEP-85** (sort, interleave, "Closing soon" label). Closed. | US-06 | **Absorbed** (2026-05-14) |
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

*Reconciled 2026-05-20 — reduced from 20 bulk-generated stories to ~9 MVP build stories. See auth.md for full detail.*

| Jira ID | Title | Working ID | Sprint | Notes |
|---------|-------|------------|--------|-------|
| OTEP-71 | Log in with WOG AD credentials | OTEP-71a | **3** | Absorbs WOG-11 (no separate account creation) |
| *(subtask of OTEP-71)* | WOGAD token handling | OTEP-71b | **3** | |
| *(subtask of OTEP-71)* | WOGAD session management | OTEP-71c | **3** | |
| *(subtask of OTEP-71)* | Login UI + error states | OTEP-71d | **3** | |
| OTEP-111 | Officers with no access | OTEP-71e | 1 ✓ | Confirm it covers WOG-08 (agency not onboarded) + WOG-09 (invalid officer) — amend if not |
| OTEP-72 | New Officer account creation | OTEP-72 | 1 ✓ | |
| WOG-10 *(Jira TBD)* | Resolve agency from AD identity | WOG-10 | **3** | New — blocked on agency-resolution source decision (Pow Hwee) |
| OTEP-110 | Login fail / clear error | WOG-03 | **3** | Absorbs WOG-12 (locked/disabled) + WOG-13 (AD unreachable); WOG-15 (no-enumeration) is an NFR constraint on this ticket |
| WOG-04 *(Jira TBD)* | Stay logged in during session | WOG-04 | **3** | Blocked on idle-timeout compliance value |
| WOG-05 *(Jira TBD)* | Log out of OTEP | WOG-05 | **3** | |
| WOG-17 *(Jira TBD)* | Complete logout on shared devices | WOG-17 | **3** | New — pairs with WOG-05 |
| WOG-06 *(Jira TBD)* | First-time login + profile setup (name only) | WOG-06 | **3** | Trimmed to name-only; absorbs WOG-19 (skip on return) + WOG-20 (resume — collapsed to 1 AC) |
| WOG-14 *(Jira TBD)* | Spike — confirm rate-limiting ownership | WOG-14 | **3 pre-work** | Spike, not delivery — likely build nothing (WOG AD owns lockout per assumption) |
| WOG-16 *(Jira TBD)* | Pre-expiry session warning | WOG-16 | **Deferred** | Pairs with apply flow (Sprint 3+); FormSG-data AC dropped |
| WOG-18 | Concurrent-session default | WOG-18 | **Decision only** | Not a delivery ticket — log a one-line policy decision in decisions-log.md |
| WOG-02 *(Jira TBD)* | Log in as agency admin (deferred) | WOG-02 | 6 | Consolidate with WOG-07 |
| WOG-07 *(Jira TBD)* | Role-based access control (deferred) | WOG-07 | 6 | Consolidate with WOG-02 |

**Absorbed / closed working IDs (do not ticket separately):**
- WOG-08 → OTEP-111 (agency not onboarded — confirm coverage)
- WOG-09 → OTEP-111 (invalid officer — confirm coverage)
- WOG-11 → OTEP-71 (no separate account creation)
- WOG-12 → OTEP-110 (locked/disabled message)
- WOG-13 → OTEP-110 (AD unreachable message)
- WOG-15 → NFR on OTEP-110 (no-enumeration constraint)
- WOG-19 → WOG-06 (skip welcome on return)
- WOG-20 → WOG-06 (resume setup — collapsed to 1 AC)

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
| WOG-06 | First-time login + profile setup (name only) | Sprint 3, needs ticket |
| WOG-10 | Resolve agency from AD identity | Sprint 3, needs ticket — blocked on agency-resolution source decision |
| WOG-17 | Complete logout on shared devices | Sprint 3, needs ticket |
| WOG-14 | Spike — rate-limiting ownership | Sprint 3 pre-work, spike not delivery |
| WOG-02 | Log in as agency admin | Sprint 6, deferred |
| WOG-07 | Role-based access control | Sprint 6, deferred |

---

## When a new Jira ticket is created

1. Add the OTEP-NNN ID to this map
2. Find-and-replace the old working ID (e.g. `US-05` → `OTEP-XXX`) across all .md files
3. Stories without Jira tickets are marked *(Jira TBD)* above

---

*Updated: 2026-05-20 — Auth (Epic 5) reconciled: reduced from 20 bulk-generated stories to ~9 MVP build stories. Added WOG-10, WOG-17 as new tickets. Registered absorbed IDs (WOG-08/09 → OTEP-111, WOG-11 → OTEP-71, WOG-12/13/15 → OTEP-110, WOG-19/20 → WOG-06). WOG-14 reclassified as spike; WOG-16 deferred; WOG-18 converted to policy decision.*

*Updated: 2026-05-19 — Jira backlog sync: added OTEP-131, 132, 172, 196, 197, 231, 232, 281, 282, 283, 284, 290, 295, 296. Fixed OTEP-268 (re-added Sprint 2 by Pow Hwee 2026-05-18). Fixed OTEP-285 (absorbed into OTEP-128). Flagged OTEP-133 title mismatch. Added "Stories still without Jira tickets" table. Added OTEP-284 (Closing soon re-ticketed).*
