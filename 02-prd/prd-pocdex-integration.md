## Product Requirements Document: POCDEX Integration

**Author**: Michelle Yip
**Date**: 2026-05-22
**Status**: Draft
**Stakeholders**: Daryll (POCDEX Team Lead), Pow Hwee (BE), Léo (BE), Imelda (Core Squad PM), Adrian

### 1. Executive Summary
This PRD outlines the integration between OTEP and POCDEX (the WOG central source of truth for public officer profiles). POCDEX integration is the backbone for OTEP account creation and opportunity ringfencing, ensuring that officers only see and apply for opportunities they are eligible for based on their agency and profile data. 

### 2. Background & Context
When a new officer onboards, their profile is created by agency HR in either HRPS or Cumulus. This record is pushed into POCDEX, which then pushes the data to OTEP in near real-time, triggering the creation of the officer's OTEP account. POCDEX provides critical data, such as the agency code, which determines if the officer is part of the initial MVP pilot group (e.g., ESG/PSD). 

Currently, OTEP is the first project using the POCDEX API, and we face cross-squad dependencies as Imelda's Core Squad also requires POCDEX integration for their Epics. We have consolidated all POCDEX integration work into a single Epic to streamline delivery and support from Daryll's team.

### 3. Objectives & Success Metrics
**Goals**:
1. Successfully receive and process officer profile data from POCDEX to create OTEP accounts.
2. Enable opportunity ringfencing so officers only see opportunities available to their specific agency or profile.
3. Establish a robust API integration and local development environment for POCDEX data.

**Non-Goals**:
1. **FormSG Pre-filling**: Auto-populating FormSG application fields using POCDEX data is explicitly deferred to Release 1 (R1). MVP will use FormSG as-is.
2. **Competency Mapping**: Resolving the competency tags is tracked separately under Reference Data dependencies with Imelda's squad, not this integration.

**Success Metrics**:
| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|
| Account Creation Success Rate | N/A | 99.9% | Percentage of successful OTEP account creations triggered by POCDEX pushes |
| Ringfencing Accuracy | N/A | 100% | Zero instances of officers viewing or applying for opportunities outside their agency's ringfence |
| Pre-POCDEX Login Edge Case Handling | N/A | 100% | All early logins caught with correct "profile pending" error message |

### 4. Target Users & Segments
- **Public Officers**: Specifically the pilot group (e.g., ESG/PSD) who need seamless account provisioning and relevant opportunity filtering.
- **OTEP Administrators & HR**: Relying on accurate access control without manual account provisioning.

### 5. User Stories & Requirements

**P0 — Must Have**:
| # | User Story | Acceptance Criteria | Jira |
|---|-----------|-------------------|---|
| 1 | As the system, I need a local POCDEX database container so engineers can build and test locally | Local DB container running with correct POCDEX schema | OTEP-271 |
| 2 | As the system, I need a standalone POCDEX API service to handle data exchange | API service accepts and processes POCDEX payloads | OTEP-203 |
| 3 | As a QA/Dev, I need a seeded POCDEX database to test ringfencing scenarios | Seed DB contains test profiles for ESG, PSD, and other agencies | OTEP-202 |
| 4 | As an officer, I only want to see opportunities I am eligible for (Ringfencing) | Opportunities are filtered by the officer's agency code upon login | OTEP-127 |
| 5 | As an officer who logs in before my POCDEX profile is synced, I want a clear error message | "Profile pending/Contact HR" message shown instead of system error. Support routing clear. | TBD |
| 6 | As the system, I need to handle malformed or missing agency codes from POCDEX gracefully | Officers with missing/invalid agency codes are treated as "non-pilot" and shown a restricted/error state, rather than crashing or bypassing the ringfence. | TBD |

**P1 — Should Have**:
*(None. MVP is strictly limited to the P0 path.)*

**P2 — Nice to Have / Future (Post-MVP)**:
| # | User Story | Acceptance Criteria | Jira |
|---|-----------|-------------------|---|
| 7 | As an officer who transfers agencies mid-session, I want my ringfenced view to update immediately | Webhook listener invalidates active sessions if agency code changes. MVP fallback: Updates on next login. | TBD |

### 6. Solution Overview
The integration relies on a push mechanism from POCDEX to OTEP. 
- **Infrastructure**: A standalone POCDEX API service (OTEP-203) will be built by Pow Hwee to handle incoming webhooks/pushes from POCDEX. 
- **Local Dev**: Léo is setting up a local database container (OTEP-271) and seed data (OTEP-202) to simulate POCDEX behavior without hitting production.
- **Ringfencing**: The frontend/backend will use the officer's agency code (stored in their OTEP profile) as a mandatory filter parameter when querying the `/opportunities` endpoint.

### 7. Open Questions
| Question | Owner | Deadline |
|----------|-------|----------|
| **Go-Live Support**: What is the SLA and support structure from Daryll's team since we are the first POCDEX API consumers? | Michelle | Before Sprint 4 Planning |
| **Cross-Squad Priority**: How do we sequence Pathfinder's ringfencing needs vs. Imelda's Epic 1-3 needs with Daryll's limited bandwidth? | Michelle / Imelda | Before Sprint 4 Planning |

### 8. Timeline & Phasing
- **Sprint 3 (Current)**: Backend plumbing. Léo sets up the local DB (OTEP-271), Pow Hwee builds the API service (OTEP-203).
- **Sprint 4**: Seed database creation (OTEP-202) and implementation of Ringfencing (OTEP-127). *Note: New fullstack developer joins to assist with backend velocity.*
- **Pre-Go-Live**: Planning session with Daryll to confirm production support structure.
