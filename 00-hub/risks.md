# Risks & Dependencies

> Active blockers, field gaps, and cross-team dependencies.
> This file tracks tactical/sprint-level risks. Strategic risks live in the PRD (Section 10).
> Open items needing owner/deadline are in [open-items.md](open-items.md).

## Unconfirmed OTG Fields

Six fields were tracked in [open-items.md](open-items.md) items #1–6. All six now resolved: `eligibility` not needed (#1); `formsg_url` confirmed for Internal Jobs/STIPs/Gigs, SJRs excluded — no apply flow (#2, 2026-05-21); `closing_date` confirmed as application closing date (#3); `is_published` does not exist — use `closing_date` for visibility (#4); `reporting_line` not available (#5); `developmental_outcome` confirmed available (#6). All OTG fields resolved — US-18 unblocked.

## Cross-Team Dependencies

Detailed tracking (owner, deadline, status) lives in [open-items.md](open-items.md). Below captures the *risk* — what breaks if they don't land.

| Dependency | What breaks | Escalation trigger |
|------------|------------|-------------------|
| OTG file import (Excel → OTEP) | Risk: Excel format ingestion alignment (OTEP-296) before Sprint 3. (Sprint 2 Listing UI uses Léo's OTEP-288 static mock backend). | File import job (OTEP-192) must land Sprint 3 |
| ~~C@G ingestion method~~ | ~~Half the "unified" promise~~ — **Resolved 2026-05-14: C@G = API.** | Sprint 2 ships OTG-only regardless; C@G API integration is Sprint 5 |
| FormSG URL/redirect format | Complex FormSG Phase 2 callback flow (OTEP-130) deferred to Sprint 5. Basic redirect (US-18) pulled to Sprint 3. | Basic redirect needed for Sprint 3; OTEP-130 callback needed by Sprint 5 start (Jun 29) |
| FormSG pre-fill support | US-P3 stays in limbo — can't groom or defer | Pow Hwee to confirm by Sprint 3 (deferred to Sprint 5 webhook flow) |
| WOGAD / Azure AD via COMET | Auth blocked if ESG not onboarded | Out of Michelle's scope — monitor only |
| No WOG AD UAT environment (Pow Hwee, grooming 2026-05-21) | OTEP-71, OTEP-110, OTEP-304, OTEP-305 can't be validated against real WOG AD before go-live. **Auth epic moved to Sprint 4+ (2026-05-21) as a direct result.** Must resolve before auth is rescheduled into any sprint. | Escalation path: Michelle → Adrian. Identify who owns the UAT environment request — COMET onboarding, GovTech/WOG AD team, or Adrian. Interim: Keycloak stub (OTEP-190) available for local dev. |
| ~~Rama: `formsg_url` confirmation (#2)~~ | **Resolved 2026-05-21.** `formsg_url` confirmed in OTG Export for Internal Jobs, STIPs, Gigs. SJRs excluded (no apply flow in MVP — decision 2026-05-13). US-18 is unblocked and ready to groom. |

## Schedule Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Lack of live OTG file data in Sprint 2 | Core UI listing (OTEP-85) has no real database data to display | Mitigated by Léo's static backend endpoint stub (OTEP-288) for Sprint 2 UI work. Ingestion (OTEP-192) shifted to Sprint 3. |
| Sprint 3 integration stagger risk | POCDEX DB/API plumbing (OTEP-271, OTEP-203) or basic FormSG redirect (US-18) slipping | Staggering POCDEX plumbing to Sprint 3 explicitly unblocks Sprint 4 ringfencing (OTEP-127) and onboarding (WOG-06). |
| Security review monthly cycle | Must submit by early Sep to hit the Oct go-live window | Plan submission date now (per Sprint Ceremonies v2, Go-Live is Fri 16 Oct) |

## Team & Delivery Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Senior-stakeholder direction is frequent but keeps shifting (PM Weekly 11 May) | Scope instability, rework, team morale — e.g. the apply-flow path flipping after being decided | Log every scope shift in `decisions-log.md`; hold the MVP line; surface drift to Adrian early |
| Engineers split across too many scopes (profiles, competencies, onboarding, auth, opportunities) | Reduced capacity per scope; Sprint 2+ opportunities work may be under-resourced if Leo/Thomas are still on Sprint 1 auth | Watch at planning + mid-sprint; flag to Adrian/Jace if it bites |
| Thomas is sole FE developer and fielding dependencies from another squad (standup 13 May) | Single point of failure for all frontend Sprint 2 work (OTEP-85, 267, 268, OTEP-128 detail page). Cross-squad pulls reduce his capacity. OTEP-86/US-05 deferred to Sprint 3 (2026-05-14). | Pow Hwee monitoring; escalate if sprint velocity at risk. Contract-first approach (Pow Hwee, 2026-05-14) decouples FE/BE. |
| FE and design capacity shared across squads (internal groom 13 May) | Design and frontend resources are not dedicated to OTEP — other squads draw from the same pool. Mid-sprint resource conflicts possible. | Needs alignment with leadership. Dedicated design system story to reduce reliance on single FE dev. Longer-term: engineers own vertical slices (front+back), not strict FE/BE split. |

## Jira Board — Cleanup Actions Needed

### Sprint 2 Board Cleanup Actions Needed

| Story | Issue | Action |
|---|---|---|
| OTEP-276 | Resolved design system spike (Flagship/LifeSG adopted via OTEP-252 Done) | Remove from Sprint 2 board (still showing in Backlog) |
| OTEP-192 | recurring job to fetch OTG data — confirmed Sprint 3 | Remove from Sprint 2 board |
| OTEP-191 | credential manager and vault — confirmed Sprint 3 | Remove from Sprint 2 board |

### Sprint 3 Board Prep Actions Needed (updated 2026-05-21)

| Story | Issue | Action |
|---|---|---|
| OTEP-192 | Recurring OTG job — confirmed Sprint 3 | Add to Sprint 3 board |
| OTEP-271 | Local POCDEX database (container + schema) — confirmed Sprint 3 | Add to Sprint 3 board and assign to Leo |
| OTEP-203 | Standalone POCDEX API service — confirmed Sprint 3 | Add to Sprint 3 board and assign to Pow Hwee |
| OTEP-86 | Filter by opportunity type — moved to Sprint 3 (2026-05-21) | Add to Sprint 3 board |
| OTEP-317 | Clear filters and reset view *(was US-05)* — ticketed 2026-05-21 | Confirm on Sprint 3 board |
| OTEP-318 | Filter by category *(was US-03)* — conditional on OTEP-289 spike output | Add to Sprint 3 board only if spike is green; no Jira description yet |
| OTEP-87 | Enhanced detail page, apply CTA only — moved to Sprint 3 (2026-05-21) | Add to Sprint 3 board; note competency section deferred |
| OTEP-319 | Apply via FormSG basic redirect *(was US-18)* — ticketed 2026-05-21, `formsg_url` ✔ | Confirm on Sprint 3 board; ready to groom |
| OTEP-191 | Credential manager / vault — in Jira Sprint 3 (sync 2026-05-21) | Verify: resolved by AWS infra or needs active Sprint 3 work? |
| OTEP-92 | "Tracking" subtask of OTEP-86 — no story file in our docs | Clarify purpose with Pow Hwee; confirm if ACs needed |

### Sprint 4+ Board Actions Needed (updated 2026-05-21)

| Story | Issue | Action |
|---|---|---|
| OTEP-71 | Login Authentication — moved from Sprint 3 (2026-05-21) | Move to Sprint 4+ in Jira — **still in Sprint 3 (2026-05-21 sync)** |
| OTEP-110 | Login fail — moved from Sprint 3 (2026-05-21) | Move to Sprint 4+ in Jira — **still in Sprint 3 (2026-05-21 sync)** |
| OTEP-304 | Stay logged in (was WOG-04) — moved from Sprint 3 (2026-05-21) | Move to Sprint 4+ in Jira — **still in Sprint 3 (2026-05-21 sync)** |
| OTEP-305 | Log out (was WOG-05) — moved from Sprint 3 (2026-05-21) | Move to Sprint 4+ in Jira — **still in Sprint 3 (2026-05-21 sync)** |

## Mitigations Already in Place

- OTEP-133 fallback error state covers both null URL scenarios
- Binary competency model avoids dependency on proficiency framework
- Competency match ratio descoped to R1 (decision: May 8)
- Scoping gaps tracker populated with 13 items — reviewed monthly

---

*Updated: 2026-05-21 (Sprint 3 reallocation — auth epic moved to Sprint 4+; Sprint 3 board prep updated to reflect filter + detail work; WOG AD UAT dependency note updated)*
