# OTEP — Product Overview

## What OTEP Is

OTEP (One Talent Engagement Platform) is an internal talent marketplace for the Singapore Public Service. It gives government officers a single place to discover and apply for development opportunities — STIPs, Gigs, SJRs, internal jobs, and Careers@Gov public listings — without navigating multiple portals.

## Delivery Timeline (MVP Release)

**Sprint cadence:** 2-week sprints. Full team: Pow Hwee (Tech Lead), Leo, Thomas, Amber (Design).

| Phase | Window | Notes |
|-------|--------|-------|
| Development | 4 May – 11 Jul 2026 | 5 sprints |
| Buffer + UAT + Security | 14 Jul – 30 Sep 2026 | Security review (submit by early Sep), UAT with ESG + PSD |
| Target Go Live | Sep 2026 (target) / Dec 2026 (outer bound) | Date alignment needed — see `context/decisions-log.md` |

Sprint breakdown: see [otep-mvp-release.md](../../resources/otep-mvp-release.md).

## MVP Scope

Two epics:

### 1. Opportunities (Epic 4)
Unified discovery experience across two pipelines:
- **OTG pipeline** — full lifecycle: discovery → FormSG application → tracking (end-to-end on OTEP)
- **Careers@Gov pipeline** — discovery on OTEP with deep-link handoff to Careers@Gov

20 user stories across 5 groups: Profile Dependency, Discovery & Filters, OTG Lifecycle, C@G Handoff, Application Tracking.

PRD: [prd-opportunities.md](../../projects/otep-mvp/prd-opportunities.md)

### 2. WOG AD Authentication
Login via Whole-of-Government Active Directory. Gates access to the rest of the product. 7 user stories covering SSO, account creation, error handling, session management.

PRD: [prd-auth.md](../../projects/otep-mvp/prd-auth.md)

## R1 (Post-MVP) — Deferred Scope

| Item | Why deferred |
|------|-------------|
| Competency proficiency levels | Binary only for MVP; proficiency tiers add complexity |
| "Save for later" | Low priority vs core apply flow |
| Supervisor endorsement backend | UI copy only in MVP; workflow is R1 |
| Recommendation / AI-matching engine | Requires structured taxonomy + scoring |
| Email/push notifications | In-app only for MVP |
| Persist filter selections across sessions | Not required for "discoverable in one place" target |
| Function/Job function taxonomy mapping | OTG and C@G taxonomies don't match; mapping deferred |
| Agency/grade/commitment filters | Type filter only for MVP |

## Integrations

| System | Integration | Notes |
|--------|------------|-------|
| OTG | Daily data export → OTEP | STIPs, Gigs, SJRs, Internal Jobs. Field mapping with Rama pending. |
| Careers@Gov | Separate ingestion (method TBC) | Discovery only; deep-link handoff for apply |
| FormSG | Redirect to new tab + webhook back | Submission confirmation received by OTEP |
| POCDEX | Officer profile data on login | Powers ringfencing + pre-fill (if supported) |
| WOG AD / Azure AD | SSO login | Requires COMET onboarding |

## Known Constraints

- GovTech managed settings block MCP servers — no automated Linear/Calendar integration
- Security reviews happen monthly — must plan submission early
- FormSG pre-fill support unconfirmed — determines whether US-P3 is MVP or R1
- OTG and C@G use different category taxonomies — cannot unify filters in MVP
