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
| WOG AD onboarding (`careercompass.gov.sg`) | Auth blocked (OTEP-71/110/304/305) AND CSC SSO blocked (#30) if onboarding delayed. Domain confirmed 2026-05-21. Remaining: COMET status + prod testing approval. **Minimum 2 weeks from approval — longer if errors or back and forth. Treat 3 weeks as the working estimate.** | Michelle → Adrian. Two asks: (1) COMET status — is ESG/OTEP onboarded? (2) Approval to test against WOG AD Prod. Domain = careercompass.gov.sg. Then session with Pow Hwee to map the process steps. (#26) |
| No WOG AD UAT environment (Pow Hwee, grooming 2026-05-21) | OTEP-71, OTEP-110, OTEP-304, OTEP-305 can't be validated against real WOG AD before go-live. **Auth epic moved to Sprint 4+ (2026-05-21) as a direct result.** Must resolve before auth is rescheduled into any sprint. **Cross-squad risk (2026-05-22):** OTEP-71, 72, 110, 111 also appear in Imelda's prd-officer-profile.md — her Epic 1 cannot go to user testing without a logged-in officer. Auth slip hits both squads simultaneously. | Domain careercompass.gov.sg confirmed 2026-05-21. Remaining blockers: COMET onboarding status + prod testing approval (Adrian, #26). Once confirmed, 2-week onboarding starts. Then CSC SSO can start (4 weeks, #30). Interim: Keycloak stub (OTEP-190) available for local dev. |
| CSC SSO (Imelda, 2026-05-21) | SSO blocked until WOG AD completes. 4-week CSC lead time after documents received. 6-week total chain. Ownership TBC. | Start WOG AD onboarding today. Sync with Imelda: who owns passing documents to CSC? (#30) |
| POCDEX API go-live (Daryll's team) | First POCDEX API project — no support structure settled. OTEP-202 (seed data) unassigned. Sprint 3 plumbing can't be validated without Daryll's team engaged. **Cross-squad risk (2026-05-22):** Imelda's squad also depends on POCDEX (Epic 1 profile, Epic 2 competency personalisation, Epic 3 course recommendations). Two squads competing for Daryll's team — if Daryll's team prioritises Imelda's use cases, our Sprint 4 ringfencing (OTEP-127) slips. | **In progress (2026-05-28):** Michelle emailed Daryll asking for his team's availability next week. Awaiting response to confirm planning session date. Confirm both squads' POCDEX needs and agree on priority order. Assign OTEP-202. (#31) |
| Reference data — Imelda's squad (confirmed 2026-05-21) | Imelda's squad owns master source of truth for job family, job function, agency, and competencies. OTEP must consume from them. Integration method (API / file / push), schema, and availability timeline all TBC. Blocks: competency section of OTEP-87, WOG-10 (agency resolution), any future competency features. **Cross-squad risk (2026-05-22):** Epics 1–3 PRDs confirm this dependency is active — schema and availability are unresolved for their builds too. Add reference data schema + method as an explicit agenda item at next Imelda sync. | Confirm method + timeline with Imelda. Add reference data schema + method to Imelda sync agenda (#18). |
| OTG opportunity competency mapping (grooming 2026-05-21) | OTG opportunities carry competency tags. These must map to the OTEP competency bank (owned by Imelda's squad) before ingestion produces clean data. Without mapping, competency display on OTEP-87 detail page will be inconsistent or unmapped. | Confirm OTG competency tag format with Pow Hwee; align with Imelda's schema (#18). Required before OTEP-87 competency section can be groomed. |
| ~~Rama: `formsg_url` confirmation (#2)~~ | **Resolved 2026-05-21.** `formsg_url` confirmed in OTG Export for Internal Jobs, STIPs, Gigs. SJRs excluded (no apply flow in MVP — decision 2026-05-13). US-18 is unblocked and ready to groom. |

## Schedule Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Lack of live OTG file data in Sprint 2 | Core UI listing (OTEP-85) has no real database data to display | Mitigated by Léo's static backend endpoint stub (OTEP-288) for Sprint 2 UI work. Ingestion (OTEP-192) shifted to Sprint 3. |
| Sprint 3 integration stagger risk | POCDEX DB/API plumbing (OTEP-271, OTEP-203) or basic FormSG redirect (US-18) slipping | Staggering POCDEX plumbing to Sprint 3 explicitly unblocks Sprint 4 ringfencing (OTEP-127) and onboarding (WOG-06). |
| VAPT (vuln assessment + pen test) — **7 Sep – 16 Oct** (updated 2026-06-23, open-item #39). ⚠️ **PENDING SUPERSESSION (flagged 2026-08-07):** a PS/DS approval note is in flight proposing MVP launch move from early Oct 2026 to end Nov 2026, with VAPT itself moving to **early-Sep–mid-Nov 2026** (7 weeks negotiated with NCS + 3-week remediation/re-test buffer). Note sent to PS/DS, approval not yet confirmed. This likely supersedes the 16 Oct vs. 23 Oct conflict below rather than sitting alongside it — do not resolve that conflict independently of this approval. See [2026-08-07 daily plan appendix](../../PM-OS/outputs/daily-plans/2026-08-07-W32-daily-plan.md) for the full proposed timeline (UAT shifts to mid-Aug–early-Sep, Release 1 Jan→Feb 2027, onboarding waves cascade ~1 month each). ⚠️ **Prior CONFLICT, flagged 2026-07-31 (superseded pending above):** the 2026-07-30 VAPT Planning Slack thread has Rama Moorthy confirming with NCS a **23 Oct** closure, not 16 Oct — a 7-day tightening against the 19–23 Oct go-live approval window below. Two sources disagree (this file's 16 Oct vs. Rama's 23 Oct confirmation) and neither is unambiguously the newer authoritative update in writing here. | UAT: 11 Aug – 4 Sep (staggered modules: Profile + Opportunities from 11 Aug; remaining from 17 Aug) — **note: PS/DS proposal would shift this to mid-Aug–early-Sep; confirm which is current with CSC.** **Feature freeze: end of S8 (21 Aug)** — pending confirmation this doesn't also shift. Dev continues S9 for bug fixes only. VAPT starts 7 Sep (old) / early Sep per proposal (pending approval). Go-live approval / deploy to prod: 19–23 Oct (old, likely stale). Soft launch: 26–30 Oct (old, likely stale). **First release: week of 2 Nov (old)** — PS/DS proposal would push MVP launch to end Nov 2026. ⚠️ Adrian away 5–9 Oct (mid-VAPT — no approvals that week; may fall outside VAPT window if proposal is approved). ⚠️ Jace away 26 Oct – 5 Nov (soft launch + first release) — cover: Adrian, Rama, Barry, Pow Hwee. VAPT scope (POCDEX/CSC/Cumulus) still TBC — confirm with Barry/Pow Hwee before S07 planning. | Confirm PS/DS approval status on the revised timeline before touching anything else in this row. **Do not resolve the 16 Oct vs. 23 Oct conflict independently — it's likely moot once approval status is known.** Once approved, rewrite this entire row against the new dates. **Intranet routing/VAPT ownership confirmed 2026-08-07: Rama** — closes the gap flagged independently across 3 meetings this week (CSC SIT progress review 8/6, OTEP Squad Sync 8/7, CSC-Compass SIT standup 8/7), all of which surfaced intranet-vs-internet routing as unowned. Rama to define migration plan, timeline, and test approach — none of that exists yet, only ownership is now clear. |
| 6-week SSO chain (WOG AD + CSC) | Auth + CSC SSO both slip if WOG AD onboarding delayed. **Best case (clean run): auth S04, CSC SSO S05. Realistic (back and forth): auth S05, CSC SSO S06. Delay + errors: Feature Freeze at risk.** Best case requires Adrian this week AND no errors in the process — two things that must both go right. | Treat auth in S05 as the working assumption. Plan S04 with a contingency stream. Adrian ping today. Pow Hwee session this week to map onboarding steps and known failure points. |
| HDB off HRPS/Cumulus — custom data piping (Implementation Details, 2026-06-02) | HDB is a Release 3 (Jul 2027) test case but is **not on the HRPS/Cumulus system**, so officer/competency data needs separate, custom data piping. If unplanned, R3 onboarding slips and the custom pipe becomes a late surprise. | Log now for R3 planning. Scope the custom HDB pipe well before R3 (Jul 2027) — treat as a known integration exception, not a discovery. |
| OTG contract sunset — Mar 2028 hard stop (Implementation Details, 2026-06-02) | OTG contract expires March 2028. Full cutover to CareerCompass targeted Oct 2027 (R4). Any slip in the R1–R4 rollout compresses the buffer before OTG goes dark for the ~108K officers on legacy. | Hold the R4 (Oct 2027) cutover as the working deadline with ~5 months contract buffer. Track rollout slippage against this; escalate if R3/R4 dates move right. OTG onboarding for remaining 24 agencies already halted (decision 2026-06-02). |

## Team & Delivery Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Senior-stakeholder direction is frequent but keeps shifting (PM Weekly 11 May) | Scope instability, rework, team morale — e.g. the apply-flow path flipping after being decided | Log every scope shift in `../../PM-OS/outputs/decisions/2026-05-29-W22-decisions-log.md`; hold the MVP line; surface drift to Adrian early |
| Engineers split across too many scopes (profiles, competencies, onboarding, auth, opportunities) | Reduced capacity per scope; Sprint 2+ opportunities work may be under-resourced if Leo/Thomas are still on Sprint 1 auth | Watch at planning + mid-sprint; flag to Adrian/Jace if it bites |
| Thomas is sole FE developer and fielding dependencies from another squad (standup 13 May) | Single point of failure for all frontend Sprint 2 work (OTEP-85, 267, 268, OTEP-128 detail page). Cross-squad pulls reduce his capacity. OTEP-86/US-05 deferred to Sprint 3 (2026-05-14). | Pow Hwee monitoring; escalate if sprint velocity at risk. Contract-first approach (Pow Hwee, 2026-05-14) decouples FE/BE. |
| FE and design capacity shared across squads (internal groom 13 May) | Design and frontend resources are not dedicated to OTEP — other squads draw from the same pool. Mid-sprint resource conflicts possible. | Needs alignment with leadership. Dedicated design system story to reduce reliance on single FE dev. Longer-term: engineers own vertical slices (front+back), not strict FE/BE split. |
| **Environment/config governance gap — manual env var and secret changes observed (Team 2 standup, 2026-07-14)** | Pow Hwee Tan observed manual changes to environment variables and secrets while capturing baseline configurations. Environments may be inconsistent with each other; reproducing issues could get harder; unexpected breakages could surface between environments with no clear cause. Acknowledged in the standup but no governance mechanism discussed. Rated 🔴 Red in the meeting's own SteerCo-style assessment. Continues the same root cause tracked in [open-items.md #58](open-items.md) (cross-team comms gaps / late-surfaced infra issues). | No mitigation defined yet. Needs a change-control mechanism for env vars/secrets before the next baseline capture. Owner: Pow Hwee Tan. |

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
| OTEP-71 | Login Authentication — moved from Sprint 3 (2026-05-21) | Moved to Sprint 4+ in Jira ✔ |
| OTEP-110 | Login fail — moved from Sprint 3 (2026-05-21) | Moved to Sprint 4+ in Jira ✔ |
| OTEP-304 | Stay logged in (was WOG-04) — moved from Sprint 3 (2026-05-21) | Moved to Sprint 4+ in Jira ✔ |
| OTEP-305 | Log out (was WOG-05) — moved from Sprint 3 (2026-05-21) | Moved to Sprint 4+ in Jira ✔ |

## Mitigations Already in Place

- OTEP-133 fallback error state covers both null URL scenarios
- Binary competency model avoids dependency on proficiency framework
- Competency match ratio descoped to R1 (decision: May 8)
- Scoping gaps tracker populated with 13 items — reviewed monthly

---

*Updated: 2026-07-31 (stale-check — flagged, not fixed: VAPT closure date conflict. This file says 16 Oct; 2026-07-30 VAPT Planning Slack has Rama confirming 23 Oct with NCS. Two sources disagree, neither self-evidently supersedes the other in writing here — needs a person to confirm before treating either as current.). Prior: 2026-07-01 (stale-check — content verified current against open-items #39, no changes). Prior: 2026-06-24 (timeline update — VAPT moved to 7 Sep–16 Oct; UAT now 11 Aug–4 Sep staggered; soft launch 26–30 Oct; first release 2 Nov; Jace leave 26 Oct–5 Nov risk added).*
