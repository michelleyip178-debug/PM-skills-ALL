# User Stories: WOG AD Authentication for Login

**Epic:** WOG AD Authentication (Epic 5)
**One-pager:** _TODO: Confluence link_
**Status:** Sprint 1 — in progress. Auth flow accepted for MVP (decision 2026-05-12).
**Criticality:** MVP blocker — all other epics depend on this
**Scope decision:** Officers only for now. Agency admin login deferred to Sprint 6.

---

## Stories

### OTEP-71 (OTEP-71a): Log in with WOG AD credentials

**As a** public officer from an onboarded agency,
**I want to** log in to OTEP via WOG AD with a single click,
**So that** I can access the platform using my existing government credentials without creating a separate account.

**Flow:** Officer clicks "Log in with WOG AD" → OTEP authenticates against AD in the background (no login form) → OTEP loads on success.

**Data returned from AD:** Email, SOE-ID

**Access rule:** Officer must have a valid WOG AD account AND their agency must be onboarded to OTEP.

**Acceptance Criteria:**
- [ ] When I click "Log in with WOG AD" on the login page, I land on the OTEP home page — no manual credential entry needed.
- [ ] When OTEP loads after login, my identity shows as my government email and SOE-ID from WOG AD. [ASSUMPTION: AD returns email + SOE-ID only]
- [ ] If my agency is not yet on OTEP, I see a message explaining my agency isn't onboarded — not a generic error.
- [ ] If my WOG AD credentials are invalid (not a public officer), login fails and I see a clear error message.
- [ ] After a successful login, I go straight to OTEP — there's no additional account creation or registration step.

**Edge cases:**
- Officer's WOG AD account is disabled/locked — should show specific message (not generic failure)
- Officer's agency was onboarded but is later removed — what happens on next login?
- AD returns only email + SOE-ID — any profile data (name, job title, unit) must come from elsewhere or be collected from officer
- Network/AD service is down — graceful error message needed
- Multiple concurrent sessions on different devices — allowed or not?

**Priority:** MVP — nothing works without this

**Open:** Since AD only returns email + SOE-ID (not name/agency name), how does OTEP determine which agency the officer belongs to? Is it derived from the email domain, SOE-ID prefix, or a separate lookup?

---

### WOG-02: Log in as agency admin with elevated permissions

**As an** agency admin,
**I want to** log in and be recognised as an admin,
**So that** I can access admin-level features (e.g. posting opportunities, viewing analytics) in addition to officer features.

**Acceptance Criteria:** [DEFERRED to Sprint 6]
- [ ] If I'm registered as an agency admin in WOG AD, OTEP grants me admin-level access when I log in.
- [ ] As an admin, I see admin navigation and features that a standard officer doesn't see.
- [ ] As a standard officer, I cannot access admin-only features — they're hidden, not just disabled.

**Edge cases:**
- An officer is promoted to admin — how quickly does the role update? Real-time from AD, or synced periodically?
- An admin is demoted — access should be revoked promptly
- Can a person be both officer AND admin? (e.g. admin who also browses opportunities)

**Priority:** Deferred to Sprint 6 — agency admins are a core user type for posting opportunities, but officer login ships first

---

### OTEP-110: See a clear error when login fails

**As a** user attempting to log in,
**I want to** see a specific, helpful error message when login fails,
**So that** I know what went wrong and how to fix it.

**Acceptance Criteria:**
- [ ] If I enter incorrect credentials, I see "Incorrect credentials. Please try again." — not a generic server error.
- [ ] If my WOG AD account is locked, I see a message that directs me to my agency's IT helpdesk.
- [ ] If WOG AD is unreachable or down, I see "Service temporarily unavailable. Please try again later."

**Edge cases:**
- Rate limiting — after X failed attempts, what happens? (WOG AD policy may handle this)
- Error messages should not leak information about whether an account exists

**Priority:** MVP — critical for user trust and reducing helpdesk load

**Risks:**
- Sprint assignment TBD — could be Sprint 1 carry-over or Sprint 3. Confirm at Sprint 1 finalisation (Fri 15 May). If it carries to Sprint 3, it competes with apply-flow stories for capacity.
- Error message copy needs to avoid leaking account-existence info (security constraint) — may need compliance review.

---

### WOG-04: Stay logged in during my session

**As a** logged-in user (officer or admin),
**I want to** remain authenticated while I'm actively using OTEP,
**So that** I don't get interrupted by repeated login prompts.

**Acceptance Criteria:**
- [ ] While I'm actively using OTEP, navigating between pages keeps me logged in — I'm not prompted to re-authenticate mid-session.
- [ ] If I've been idle for more than [X minutes — TBD], my session expires and I'm redirected to the login page. [ASSUMPTION: idle timeout value TBD — pending government compliance policy]
- [ ] If my session has expired and I try to do something, I see "Session expired, please log in again" — not a broken or blank page.

**Edge cases:**
- User is filling out a FormSG application and session expires mid-form — data loss risk. What's the grace period?
- Browser tab left open overnight — should auto-expire
- What's the government-mandated session timeout? (Open question #6 in brief)

**Priority:** MVP — broken sessions destroy trust

**Risks:**
- Government-mandated session timeout unknown — the idle-timeout AC has a TBD value. If the compliance answer comes late, eng builds with a guess and may need to rework.
- Session expiry during FormSG form fill (edge case) risks data loss. Grace period or warning mechanism needs design input from Amber.

---

### WOG-05: Log out of OTEP

**As a** logged-in user,
**I want to** log out of OTEP,
**So that** my session is ended and no one else can access my account on this device.

**Acceptance Criteria:**
- [ ] When I click "Log out", my session ends and I'm taken to the login page.
- [ ] After logging out, pressing the browser back button doesn't let me back into OTEP — I'm redirected to login.
- [ ] After logging out, typing any OTEP URL directly into the browser redirects me to the login page.

**Edge cases:**
- Logging out on one device — does it log out all devices? (Depends on session architecture)
- Shared computer scenario (common in government) — logout must be complete, no cached credentials

**Priority:** MVP — security requirement for government platforms

**Risks:**
- Shared-device scenario (common in government) means logout must be thorough — cached credentials, service workers, browser back-button all need testing. Low probability of being descoped, but high rework cost if session architecture doesn't account for this upfront.

---

### WOG-06: First-time login experience

**As a** public officer logging into OTEP for the first time,
**I want to** set up my profile and understand what OTEP offers,
**So that** I can orient myself and start using the platform.

**Flow:** First login detected (no existing OTEP profile for this SOE-ID) → welcome screen → officer fills in required profile fields → lands on home page.

**Data from AD:** Email + SOE-ID only. Name, agency, job title must come from officer or a separate data source.

**Acceptance Criteria:**
- [ ] The first time I log in, I see a welcome screen that explains what OTEP is.
- [ ] On first login, my email is already filled in — I don't need to type it. [ASSUMPTION: AD provides email only; name and agency must be entered manually]
- [ ] On first login, I'm asked to enter my name and agency before continuing. [ASSUMPTION: mandatory fields are name + agency — TBD with team]
- [ ] On every subsequent login, I skip the welcome and go straight to the home page.

**Edge cases:**
- Can we derive agency from email domain or SOE-ID format? (Would remove one manual step)
- What's mandatory vs. optional for profile setup? (Impacts how quickly officers get to value)
- What if officer abandons profile setup mid-way? (Save partial? Block access until complete?)

**Priority:** MVP — but keep minimal (welcome + mandatory fields only). Rich onboarding is R1.

**Risks:**
- Mandatory profile fields TBD — if the team can't agree on what's required vs optional, scope creeps from "minimal welcome screen" toward a full onboarding flow. Decide before grooming: name + agency is likely sufficient.
- If POCDEX can pre-populate officer data (name, agency) from SOE-ID, this story simplifies significantly. Depends on OTEP-183 spike outcome from Sprint 1.

---

### WOG-07: Role-based access control

**As a** platform administrator,
**I want** OTEP to enforce role-based access based on WOG AD attributes,
**So that** officers and admins only see features appropriate to their role.

**Acceptance Criteria:** [DEFERRED to Sprint 6]
- [ ] When I log in, OTEP assigns me the correct role (officer or agency admin) based on my WOG AD attributes.
- [ ] If I have the officer role, admin-only pages and features are hidden — not just greyed out or disabled.
- [ ] If my role changes in WOG AD, the next time I log in OTEP reflects the updated role.

**Edge cases:**
- Role determination: AD groups vs. custom attribute vs. OTEP-managed lookup table? (Technical decision for Pow Hwee)
- What if AD doesn't clearly indicate admin status? Fallback?
- Grace period for role changes — immediate or next login?

**Priority:** Deferred to Sprint 6 with WOG-02. Start with 2 roles (officer, agency admin). More granular roles in R1.

---

## Open Questions

1. **Session timeout policy** — What's the government-mandated idle timeout? (30 min? 60 min? Configurable?)
2. **Role source** — Are roles determined by AD groups, a custom AD attribute, or an OTEP-managed table synced with AD?
3. **MFA** — Does WOG AD enforce MFA at their end, or does OTEP need to implement it?
4. **Data from AD** — Exactly what fields does WOG AD provide? (name, email, agency, role, job title, unit?)
5. **Existing patterns** — Are there other government platforms with WOG AD login that we can reference for UX patterns?
6. **Shared devices** — Do officers commonly use shared workstations? Impacts session/logout security requirements.
7. **First-time profile** — What's mandatory to collect on first login vs. what can be deferred?

## Assumptions

- WOG AD handles password management, MFA, and account lockout — OTEP does not re-implement these
- All OTEP users are public officers — no external/public user access in MVP
- Two roles only in MVP: officer and agency admin
- AD returns only **email + SOE-ID** on auth — name, agency, job title must come from officer input or separate data source

## Next Steps

- [ ] Confirm with Pow Hwee: what data does WOG AD return on auth? What role mechanism is planned?
- [ ] Review with Amber: login page UX, error states, first-time experience
- [ ] Confirm session timeout policy (compliance/security team)
- [ ] Grooming session
- [ ] Move to Confluence one-pager
- [ ] DoR met → Jira
