# Epic 5: WOG Authentication - Identity Verification

| Doc Created |  |
|---|---|
| PM |  |
| Tech |  |
| Designer | Name |
| Business Owner | Name |
| Infra Eng | Name |
| Target launch | Date |
| Epic Link | Link to Jira Epic (PM to input) |
| Figma Link | Link to Figma file (Designer to input) |

## 1. Background & Context

**Purpose:** Help the reader understand why this exists now.

- 

Strategic context (org priority / policy / OKR / roadmap theme)

- 

Who requested this and why

- 

What has changed (new data, new constraint, new opportunity)

OTG is currently used by…

## 2. Problem Statement

**Purpose:** Clearly define the problem before jumping to solution. 

[User] struggles to [do what] because [root cause], resulting in [negative outcome].

When officer try to…

## 3. Data Analysis & Evidence

**Purpose:** Show this is not opinion-driven. What proof do we have that this is real and worth solving?

Include if available or mark it for development:

**Examples:**

- 

% of users affected/dropped-off

- 

Time taken today vs desired

- 

Error or dropout rate

- 

Support tickets or complaints

- 

From our survey results on 1380 officers, X% indicated that

- 

Y% of officers do not have a second login within 3mths of first login.

## 4. Market / Benchmark Scan

**Purpose:** Avoid reinventing the wheel. Find out how other teams or companies solves a similar problem. Designers can help with this. 

- 

How do others solve this? 

- 

Known best practices or patterns

- 

What we should copy vs avoid

**Table (optional):**

| Organisation | Approach | What works | What doesn’t |
|---|---|---|---|

## 5. Target User

**Purpose:** Clarify who is your target user.

HR officers posting STIPs or GIGs.

## 6. Hypothesis (Value Proposition)

**Purpose:** Make your belief explicit and testable.

Example:

> 

If we provide a one-stop shop for all government scholarship opportunities[capability/solution], then students [user] will be able to easily and quickly search for suitable scholarships [new behaviour], leading to increase application completion rate [measurable outcome].

If officers understand their top competency gaps, they will take action to seek growth opportunities

## 7. Success Metrics

**Purpose:** Define what “good” looks like. Must be quantifiable. 

### 7.1 Outcome Metrics (North Star)

Examples

- 

User outcome metric: Increased scholarship application completion rate

- 

Business/org outcome metric: Improved GES score for XX.

### 7.2 Input Metrics 

Examples

- 

Officer login rate

- 

Officer conversion rate from competency gap analysis to opportunity page

### 7.3 Guardrail Metrics (Events that will lead to rollback or pause)

**Purpose:** Early warning signals. What tells us this is breaking or harming users?

- 

Drop-off rates exceed XX

- 

Error rates. Scholarship applicant’s profile is inaccurate.

- 

Complaints / tickets

- 

Data freshness

- 

Latency / availability

## 8. Scope (Stories + Success Criteria)

| **Jira ID** | **Story** | **Acceptance Criteria** | **Instrumentation** | **Notes to Designer** | **Notes to Tech/Other** |
|---|---|---|---|---|---|
| **OTEP-71** | **As a** public officer from an onboarded agency, **I want to** log in to OTEP via WOG AD with a single click, **So that** I can access the platform using my existing government credentials without creating a separate account.    *(Sprint: 4+ — moved from Sprint 3 due to no WOG AD UAT environment available.)* | 1. When I click "Log in with WOG AD" on the login page, I land on the OTEP home page — no manual credential entry needed.   2. If my agency is not yet on OTEP, I see a message explaining my agency is not onboarded — not a generic error.   3. If my WOG AD credentials are invalid (not a public officer), login fails and I see a clear error message.   4. After a successful login, I go straight to OTEP — no additional account creation or registration step. | Login success    Login attempt |  | - We will use Azure AD via COMET.   - Azure can only be accessed via COMET, not GSIB.   - WOGAD approval process takes 2-4 weeks — submit early.   - COMET onboarding required. |
| **OTEP-304** | **As a** logged-in user (officer), **I want to** remain authenticated while I'm actively using OTEP, **So that** I don't get interrupted by repeated login prompts. | -   While I'm actively using OTEP, navigating between pages keeps me logged in — I'm not prompted to re-authenticate mid-session.   -   If I've been idle for more than [30 minutes — TBD], my session expires and I'm redirected to the login page.    -   If my session has expired and I try to do something, I see "Session expired, please log in again" — not a broken or blank page. |  |  | [https://importal.mof.gov.sg/portal/home/ict-ss/im8-reform/releases/20250917/system-security-plans/low-risk-cloud.html](https://importal.mof.gov.sg/portal/home/ict-ss/im8-reform/releases/20250917/system-security-plans/low-risk-cloud.html)   -   12 hours session duration, 30 mins of inactivity |
| **OTEP-72** | **As a** public officer logging into OTEP for the first time, **I want to** set up my profile and understand what OTEP offers, **So that** I can orient myself and start using the platform.        **Flow:** First login detected (no existing OTEP profile for this SOE-ID) → welcome screen → officer fills in required profile fields → lands on home page. | 1.   User will log in using WOGAD   2.   The first time I log in, I see the default landing view of profile details and My Competency section.   3.   On first login, my name, email is already filled in — I don't need to type it.    4.   On every subsequent login, I will land on the default landing view of profile details and My Competency section. |  |  | -   When a new officer onboards, their profile will be created by the respective agency HR in either HRPS or Cumulus   -   This record will get pushed into POCDEX and into OTEP (instantaneously)   -   Account is created on OTEP |
| **OTEP-110** ⚠️ | As an officer who should have access to OTEP, I want to see clear instructions on what to do if I failed to login so I can troubleshoot. | 1. If user is part of pilot group and the authentication fails, they should be prompted to retry or troubleshoot.   ⚠️ **Jira ACs mismatch**: Jira OTEP-110 ACs state only "Authentication failure will be handled at WOG AD" — significantly simpler than the PRD ACs above. **Confirm before Sprint 4 grooming: does OTEP show any error messaging, or does WOG AD handle all error states?** If WOG AD owns it entirely, these PRD ACs should be removed. (Also absorbs WOG-12 locked/disabled and WOG-13 AD unreachable; WOG-15 no-enumeration is an NFR constraint on this ticket.) | Login failed — ability to troubleshoot the reason for login failure    Retry attempts |  | - Absorbs WOG-12 (locked/disabled message) + WOG-13 (AD unreachable message)   - WOG-15 (no-enumeration) is an NFR constraint, not a delivery AC |
| **OTEP-111** | As an officer who have no access or have a deactivated status, I want to be able to see a clear message telling me I do not have access so I am not left wondering or trying multiple times. | 1.   These user groups should not be allowed to login to OTEP     -   Users who are not part of pilot     -   Users who have left the service/gone on long-leave etc and whose profile is considered inactive/deactivated in POCDEX     2.   See a message “Oops, you do not seem to have access at the moment. Please contact your HR for more information.” | Login attempt failed due to access denied |  | 1.   [TBC] Backend check for either “agency name” or “agency” ID |
| **OTEP-305** | **As a** logged-in user, **I want to** log out of OTEP, **So that** my session is ended and no one else can access my account on this device. | -   When I click "Log out", my session ends and I'm taken to the login page.   -   After logging out, pressing the browser back button doesn't let me back into OTEP — I'm redirected to login.   -   After logging out, typing any OTEP URL directly into the browser redirects me to the login page.      **Edge cases:**   -   Logging out on one device — does it log out all devices? (Depends on session architecture)   -   Shared computer scenario (common in government) — logout must be complete, no cached credentials |  |  |  |

## 9. Go-To-Market Plan

**Purpose:** Shipping ≠ adoption. Think of what you need to do to drive adoption and scale. 

- 

Target launch group: Which agency/persona first?

- 

Comms plan:

- 

Training / enablement:

- 

Change management:

- 

Support model:

**Phases:**

- 

Pilot: When

- 

Scale: When

- 

Steady state: When

## 10. Risks, Assumptions & Mitigations

**Purpose:** Think ahead. 

| Risk/Assumption | Type (Tech / Ops / Policy / Adoption) | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| Security review only happens once a month |  |  |  |  |
| Review with pilot agency for suitability |  |  |  |  |
| If POC with Team A fails |  |  |  |  |

## 11. Dependencies & Assumptions

- 

Systems depended on:

- 

Teams needed:

- 

Policy assumptions:

- 

Data availability assumptions:

## 12. Decision Tracker (If needed)

**Purpose:** Make it actionable.

- 

Decision required from leadership:

- 

If approved, next milestone:

- 

Owner:

- 

Review date:
