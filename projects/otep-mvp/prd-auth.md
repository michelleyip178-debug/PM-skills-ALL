# PRD: WOG AD Authentication for OTEP

**Author:** Michelle
**Created:** 2026-05-06
**Last updated:** 2026-05-13
**Status:** Draft (auth flow accepted for MVP — decision 2026-05-12)
**Target Release:** Go-Live Fri 16 Oct 2026 (per programme plan, decision 2026-05-12)

> **Story ID note:** This PRD uses internal reference IDs (OTEP-85, US-03, etc.) that predate Jira ticket creation. The canonical IDs in [story-id-map.md](story-id-map.md) are: OTEP-71 (login parent + subtasks), OTEP-111 (no access), OTEP-72 (account creation), OTEP-110 (login fail), WOG-04 (session), WOG-05 (logout), WOG-06 (first-time login), WOG-02 (admin login), WOG-07 (RBAC). Use the story-id-map IDs in Jira and sprint planning.

---

## Problem Statement

### What problem are we solving?

Public officers have no way to securely access OTEP today. Without verified identity, no platform feature — opportunities discovery, applications, competency profiles — can be delivered. OTEP cannot distinguish a legitimate officer from an unauthorized user, meaning the platform is effectively unusable.

### Who has this problem?

- **Public officers** across onboarded agencies who need to discover and apply for opportunities
- **OTEP platform team** who cannot ship any user-facing feature without authenticated access

### How do we know this is a problem?

- **Mandatory requirement:** WOG AD is the required authentication mechanism for Singapore government platforms — non-negotiable for launch
- **MVP dependency:** Every other OTEP epic (Opportunities, Competency Profiles, Analytics) requires a verified officer identity to function
- **OKR alignment:** Phase 1 MVP (Oct 2026) cannot be met without authenticated access — all success metrics require officers to be on the platform

### What happens if we don't solve it?

OTEP cannot launch. This is a hard blocker to the Oct 2026 MVP. Every other epic is dependent on authenticated access. Without it:
- Zero officers can access the platform
- The OTG -> OTEP migration timeline slips entirely
- Phase 1 OKR targets are unachievable

---

## Solution Overview

### Proposed Solution

Integrate WOG AD (Whole-of-Government Active Directory) as the primary authentication mechanism for OTEP, using **Keycloak** as the identity broker. Officers authenticate using their existing government credentials — no new accounts, no separate passwords.

> **Sprint 1 status (as of 2026-05-15, finalisation):** Simple authentication through Keycloak (OTEP-190) **done**. Auth flow exploration (OTEP-173) **done**. POCDEX profile lookup spike (OTEP-183) **done**. Adrian confirmed the current WOG AD flow ships as-is for MVP (decision 2026-05-12), acknowledged it may not be the final/complete flow.

### Key Capabilities

1. **Single-click login** — Officers click "Log in with WOG AD" and are authenticated in the background via Keycloak -> AD (email + SOE-ID returned)
2. **Access control** — Only pre-provisioned officers can access OTEP; non-provisioned users are denied with a clear message
3. **Session management** — Secure sessions with government-compliant timeout, clean logout, and back-button protection
4. **First-time onboarding** — Officers completing their first login provide mandatory profile fields (name, agency) before accessing the platform
5. **Clear error handling** — Specific, helpful messages for each failure scenario (wrong credentials, locked account, service down)

### What we're NOT building (Scope boundaries)

- Agency admin login and role differentiation (deferred to Sprint 6 — WOG-02)
- Officer provisioning interface (separate epic — admin creates officer records before they can log in)
- MFA implementation (WOG AD handles this at their end)
- Password management / account recovery (WOG AD responsibility)
- Role-based access control (deferred to Sprint 6 — WOG-07)
- Rich onboarding experience (MVP = welcome screen + mandatory fields; rich onboarding is R1)
- External/public user access (all OTEP users are public officers in MVP)

---

## User Stories

### Primary User: Public Officer

| As a... | I want to... | So that... | Priority | Story-ID-Map Ref |
|---------|--------------|------------|----------|------------------|
| Officer | Log in with WOG AD in a single click | I can access OTEP without creating a separate account | P0 | OTEP-71 (parent) |
| Officer with no access | See that my agency is not onboarded | I understand why I can't access OTEP | P0 | OTEP-111 |
| New officer | Have my account created on first login | I don't need a separate registration step | P0 | OTEP-72 |
| Officer | See a clear error when login fails | I know what went wrong and how to fix it | P0 | OTEP-110 |
| Officer | Stay logged in while actively using OTEP | I'm not interrupted by repeated login prompts | P0 | WOG-04 |
| Officer | Log out of OTEP | No one else can access my account on this device | P0 | WOG-05 |
| Officer (first-time) | Set up my profile on first login | I can start using the platform with my identity established | P0 | WOG-06 |

Full acceptance criteria, edge cases, and DoR checklists: [stories/auth.md](stories/auth.md)

### Sprint 1 Stories (in progress)

| Jira | Story | Status |
|------|-------|--------|
| OTEP-190 | Simple authentication through Keycloak | Done (15 May) |
| OTEP-173 | Exploration: auth flow and tech | Done |
| OTEP-71 (subtasks) | Login parent — WOGAD SSO, token handling, session management, login UI | In progress |
| OTEP-111 | Officers with no access — denial/access states | In progress |
| OTEP-72 | New officer account creation (POCDEX push) | In progress |

### Sprint 3 or carry-over (decide at Sprint 1 finalisation, Fri 15 May)

| Story-ID-Map Ref | Story | Notes |
|-------------------|-------|-------|
| OTEP-110 | Login fail / clear error | Depends on Sprint 1 finalisation |
| WOG-04 | Stay logged in during session | Depends on Sprint 1 finalisation |
| WOG-05 | Log out of OTEP | Depends on Sprint 1 finalisation |
| WOG-06 | First-time login experience | Depends on Sprint 1 finalisation |

### Deferred (Sprint 6)

| Story-ID-Map Ref | Story | Reason |
|-------------------|-------|--------|
| WOG-02 | Log in as agency admin | Officers first; admin login scoped separately |
| WOG-07 | Role-based access control | No role differentiation needed until admin login exists |

---

## Success Metrics

### Primary Metrics (Must hit for launch)

| Metric | Current | Target | Measurement Method |
|--------|---------|--------|-------------------|
| WOG AD login functional end-to-end (officers) | N/A (not built) | 100% working | QA sign-off + UAT |
| Login success rate (valid, provisioned officers) | N/A | >99% | Server logs |
| Compliance requirements met | N/A | All mandatory WOG AD standards | Security review sign-off |

### Secondary Metrics (Monitor post-launch)

| Metric | Baseline | Expected Direction |
|--------|----------|-------------------|
| Login latency (click to home page) | N/A | < 3 seconds |
| Auth-related helpdesk tickets | N/A | Trending down post-launch |
| First-time profile completion rate | N/A | > 95% (mandatory, so should be near-total) |
| Session timeout-related complaints | N/A | Low / stable |

### Guardrail Metrics (Should not regress)

- Zero unauthorized access incidents
- Zero data leakage via error messages (account enumeration)
- Session security meets government audit requirements

---

## Design & UX

### User Flow

```
Login page -> Click "Log in with WOG AD" -> Loading state
    |
Keycloak -> AD authenticates in background
    |
Success? -> Check: officer exists in OTEP?
    |-- Yes + first time -> Welcome screen -> Profile setup -> Home page
    |-- Yes + returning -> Home page (skip onboarding)
    +-- No -> Access denied screen ("Contact your agency admin")
    |
Auth failed?
    |-- Wrong credentials -> "Incorrect credentials. Please try again."
    |-- Account locked -> "Contact your agency IT helpdesk"
    +-- Service down -> "Service temporarily unavailable. Try again later."
```

### Key Design Decisions

1. **Single-click login** — No login form; Keycloak -> AD auth happens in background after button click
2. **Access denied vs auth failed** — Two distinct screens: "not in OTEP" (valid officer, not provisioned) vs "authentication failed" (invalid credentials)
3. **Single role only** — All authenticated officers have the same access level; no role differentiation in this phase
4. **Minimal first-time onboarding** — Welcome + mandatory fields only; no multi-step wizard in MVP
5. **Auth flow ships as-is** — Adrian confirmed current WOG AD flow is accepted for MVP (2026-05-12); acknowledged it may not be the final/complete flow

### Accessibility Considerations

- Error messages meet WCAG colour contrast standards
- Screen reader-friendly error announcements
- Keyboard-navigable login flow
- Loading state communicated to assistive technology

---

## Technical Approach

### Architecture Overview

- **Identity broker:** Keycloak (OTEP-190, Sprint 1)
- **Auth protocol:** TBD — SAML / OAuth2 / OIDC (decision for Pow Hwee based on AD documentation, exploration in OTEP-173)
- **Session management:** Server-issued token (JWT or session cookie) with government-compliant timeout
- **Access gate:** Middleware checks user existence on every authenticated request
- **Data from AD:** Email + SOE-ID confirmed. Name, agency, job title come from officer input or POCDEX lookup.

### Dependencies

- **External:** WOG AD infrastructure / API access — provisioning in progress (Pow Hwee + Leo)
- **External:** Government session timeout policy — compliance team confirmation needed
- **Internal:** Officer provisioning interface (separate epic) — must be available before officers can log in
- **Internal:** POCDEX integration — lookup for profile data and ringfencing (spike OTEP-183, Sprint 1)
- **Internal:** Home page / landing experience — where officers land after successful auth

### Technical Risks

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| WOG AD provisioning/onboarding takes longer than expected | Medium | Critical — blocks entire MVP | Start provisioning process immediately; identify GovTech contact | Pow Hwee |
| Unknown compliance/security requirements surface late | Medium | High | Engage security reviewer early; submit by early Sep for Oct go-live | Michelle |
| Session timeout policy unclear or conflicting | Low | Medium | Research gov standards proactively | Michelle |
| ESG not onboarded onto COMET for Azure AD access | Unknown | High | Out of Michelle's scope — monitor only | External |

---

## Launch Plan

### Rollout Strategy

- [x] Frontend repo setup (OTEP-171, Sprint 1)
- [ ] Dev complete in staging with Keycloak -> mock AD
- [ ] Integration testing with WOG AD sandbox
- [ ] Security review passed (submit by early Sep)
- [ ] Internal dogfood (team tests with own WOG AD accounts)
- [ ] UAT with pilot officers from onboarded agencies (Sprint 8)
- [ ] GA as part of OTEP MVP launch (16 Oct 2026)

### Feature Flags

- Login flow will be the default (and only) entry point — no feature flag needed
- Role-based features may be flag-gated if admin features from other epics aren't ready

### Rollback Plan

- If AD integration fails in production: display maintenance message on login page
- If session issues arise: revert to shorter timeout as safety measure
- Auth is all-or-nothing — no partial rollback (platform is inaccessible without it)

---

## Timeline & Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| PRD Approved | TBD | Draft |
| WOG AD sandbox access provisioned | Sprint 1 | In progress (Pow Hwee + Leo) |
| Keycloak auth working (OTEP-190) | Sprint 1 (May 15) | **Done** (15 May) |
| Auth flow exploration complete (OTEP-173) | Sprint 1 (May 15) | **Done** |
| Auth flow accepted for MVP | 12 May 2026 | **Done** (Adrian confirmed) |
| Auth edge-cases (OTEP-110, WOG-04/05/06) | Sprint 1 carry-over or Sprint 3 | Decide at Sprint 1 finalisation (Fri 15 May) |
| Design complete (Amber) | TBD | Not started |
| Admin login (WOG-02) + RBAC (WOG-07) | Sprint 6 (13-24 Jul) | Not started |
| Security review passed | Early Sep 2026 | Not started |
| UAT with pilot officers | Sprint 8 (10-21 Aug) | Not started |
| Feature Freeze | Fri 21 Aug 2026 | Not started |
| Go-Live | **Fri 16 Oct 2026** | Not started |

---

## Open Questions

| Question | Owner | Due Date | Resolution |
|----------|-------|----------|------------|
| What auth protocol does WOG AD support? (SAML/OAuth2/OIDC) | Pow Hwee | Sprint 1 | Exploration in OTEP-173 |
| What exactly does AD return on auth? (confirmed: email + SOE-ID — anything else?) | Pow Hwee / Leo | Sprint 1 | |
| What's the government-mandated session timeout? | Michelle (compliance team) | Before Sprint 3 | |
| Does WOG AD enforce MFA, or does OTEP need to? | Pow Hwee | TBD | Assumed AD handles it |
| Do officers commonly use shared workstations? (impacts logout security) | Michelle (user research) | TBD | |
| What mandatory profile fields for first-time login? (name + agency minimum) | Michelle + Amber | Before WOG-06 build | |
| Can agency be derived from email domain or SOE-ID? | Pow Hwee | TBD | |
| Multiple concurrent sessions allowed? | Pow Hwee + Security | TBD | |
| Which auth edge-cases carry over from Sprint 1 vs move to Sprint 3? | Squad | Fri 15 May (Sprint 1 finalisation) | |

---

## Appendix

### Assumptions

- WOG AD handles password management, MFA, and account lockout — OTEP does not re-implement
- All OTEP users are public officers — no external/public access in MVP
- Single role only in this phase — all officers have the same access level
- AD returns only email + SOE-ID on auth — name, agency, job title come from officer input or POCDEX
- Officers must be pre-provisioned in OTEP before they can log in (provisioning is a separate epic)
- Agency admin login and role-based access control will be scoped separately (Sprint 6)
- Keycloak is the identity broker (confirmed by Sprint 1 implementation choice)
- Current auth flow ships as-is for MVP (Adrian, 2026-05-12)

### Related Documents

- [User Stories (Auth)](stories/auth.md)
- [Story ID Map](story-id-map.md)
- [Sprint Allocation](../sprint-allocation.md)
- [Decision Log](../../context/decisions-log.md)
- [DoR/DoD Guidelines](../../resources/dor-dod-guidelines.md)
- [GOALS.md](../../GOALS.md)

### Stakeholder Sign-offs

- [ ] Engineering Lead: Pow Hwee
- [ ] Design: Amber
- [ ] Security/Compliance: TBD
- [ ] Manager: Jace
- [ ] Manager: Adrian
