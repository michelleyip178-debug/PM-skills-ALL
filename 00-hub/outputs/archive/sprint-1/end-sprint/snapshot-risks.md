# Risks & Dependencies

> Active blockers, field gaps, and cross-team dependencies.
> This file tracks tactical/sprint-level risks. Strategic risks live in the PRD (Section 10).
> Open items needing owner/deadline are in [open-items.md](open-items.md).

## Unconfirmed OTG Fields

Six fields were tracked in [open-items.md](open-items.md) items #1–6. Five now resolved (2026-05-13): `eligibility` not needed (#1); `closing_date` confirmed as application closing date (#3); `is_published` does not exist — use `closing_date` for visibility (#4); `reporting_line` not available (#5); `developmental_outcome` confirmed available (#6). Only `formsg_url` (#2) remains open — Rama + PSD Ops to confirm before Sprint 2.

## Cross-Team Dependencies

Detailed tracking (owner, deadline, status) lives in [open-items.md](open-items.md). Below captures the *risk* — what breaks if they don't land.

| Dependency | What breaks | Escalation trigger |
|------------|------------|-------------------|
| OTG file import (Excel → OTEP) | Sprint 2 listing has nothing to display. OTG has no API — data comes via Excel reports (decided 2026-05-14). Open item #24 (which reports to ingest) is the critical input. | File import job (OTEP-192) must land Sprint 2 W1 |
| ~~C@G ingestion method~~ | ~~Half the "unified" promise~~ — **Resolved 2026-05-14: C@G = API.** | Sprint 2 ships OTG-only regardless; C@G API integration is Sprint 5 |
| FormSG URL format | STIP/Gig apply flow (OTEP-130) can't be built | Needed by Sprint 4 start (Jun 16) |
| FormSG pre-fill support | US-P3 stays in limbo — can't groom or defer | Pow Hwee to confirm by Sprint 3 |
| WOGAD / Azure AD via COMET | Auth blocked if ESG not onboarded | Out of Michelle's scope — monitor only |
| Rama: `formsg_url` confirmation (#2) | US-18 (Sprint 3 STIP/Gig apply) can't be groomed. 5 of 6 OTG fields resolved 2026-05-13; `formsg_url` is the last unconfirmed field. | No response before Sprint 3 grooming → escalate via Adrian |

## Schedule Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| OTG file import not delivering by Sprint 2 W1 | Sprint 2 core UI work blocked — OTEP-85 has no data to display | Open item #24 (which Excel reports) must be resolved before OTEP-192 can be built |
| Sprint 3 cascade: OTEP-133 depends on OTEP-87 + OTEP-127 | If either slips, OTEP-133 moves to Sprint 4 | Monitor at mid-sprint review |
| Security review monthly cycle | Must submit by early Sep to hit the Oct go-live window | Plan submission date now (per Sprint Ceremonies v2, Go-Live is Fri 16 Oct) |

## Team & Delivery Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Senior-stakeholder direction is frequent but keeps shifting (PM Weekly 11 May) | Scope instability, rework, team morale — e.g. the apply-flow path flipping after being decided | Log every scope shift in `decisions-log.md`; hold the MVP line; surface drift to Adrian early |
| Engineers split across too many scopes (profiles, competencies, onboarding, auth, opportunities) | Reduced capacity per scope; Sprint 2+ opportunities work may be under-resourced if Leo/Thomas are still on Sprint 1 auth | Watch at planning + mid-sprint; flag to Adrian/Jace if it bites |
| Thomas is sole FE developer and fielding dependencies from another squad (standup 13 May) | Single point of failure for all frontend Sprint 2 work (OTEP-85, 267, 268, OTEP-128 detail page). Cross-squad pulls reduce his capacity. OTEP-86/US-05 deferred to Sprint 3 (2026-05-14). | Pow Hwee monitoring; escalate if sprint velocity at risk. Contract-first approach (Pow Hwee, 2026-05-14) decouples FE/BE. |
| FE and design capacity shared across squads (internal groom 13 May) | Design and frontend resources are not dedicated to OTEP — other squads draw from the same pool. Mid-sprint resource conflicts possible. | Needs alignment with leadership. Dedicated design system story to reduce reliance on single FE dev. Longer-term: engineers own vertical slices (front+back), not strict FE/BE split. |

## Mitigations Already in Place

- OTEP-133 fallback error state covers both null URL scenarios
- Binary competency model avoids dependency on proficiency framework
- Competency match ratio descoped to R1 (decision: May 8)
- Scoping gaps tracker populated with 13 items — reviewed monthly

---

*Updated: 2026-05-15*
