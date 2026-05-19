# User Stories: WOG AD Authentication (Epic 5)

**Epic:** WOG AD Authentication (Epic 5)
**One-pager:** _TODO: Confluence link_
**Status:** Draft — 20 stories, needs grooming
**Criticality:** MVP blocker — all other epics depend on this
**Scope decision:** Officers only for MVP. Agency admin login + RBAC (WOG-02, WOG-07) deferred to Sprint 6 (decision 2026-05-12).

---

## Story Summary

| ID | Story | Priority |
|----|-------|----------|
| OTEP-71 | Log in with WOG AD credentials (single click) | MVP |
| WOG-08 | Be told clearly when my agency isn't onboarded | MVP |
| WOG-09 | Be blocked when I'm not a valid public officer | MVP |
| WOG-10 | Have OTEP resolve my agency from my AD identity | MVP |
| WOG-11 | Skip separate account creation (go straight to OTEP) | MVP |
| OTEP-110 | See a clear error when login fails | MVP |
| WOG-12 | See a helpful message when my AD account is locked or disabled | MVP |
| WOG-13 | See a graceful message when WOG AD is unreachable | MVP |
| WOG-14 | Be protected by rate limiting after repeated failed attempts | MVP |
| WOG-15 | Not have error messages reveal whether an account exists | MVP |
| WOG-04 | Stay logged in during my active session | MVP |
| WOG-16 | Be warned before my idle session expires | MVP |
| WOG-05 | Log out of OTEP | MVP |
| WOG-17 | Have a complete logout on shared government devices | MVP |
| WOG-18 | Manage concurrent sessions across multiple devices | MVP |
| WOG-06 | First-time login: welcome and profile setup | MVP |
| WOG-19 | Skip the welcome on subsequent logins | MVP |
| WOG-20 | Resume an abandoned first-time profile setup | MVP |
| WOG-02 | Log in as agency admin with elevated permissions | Deferred — Sprint 6 |
| WOG-07 | Role-based access control | Deferred — Sprint 6 |

---

## Stories

### OTEP-71: Log in with WOG AD credentials (single click)

**As a** public officer from an onboarded agency,
**I want to** log in to OTEP via WOG AD with a single click,
**So that** I can access the platform using my existing government credentials without creating a separate account.

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

**Priority:** MVP — nothing works without this; all other epics depend on auth.

---

### WOG-08: Be told clearly when my agency isn't onboarded

**As a** public officer with a valid WOG AD account whose agency hasn't been onboarded to OTEP,
**I want to** see a message that explains my agency isn't onboarded yet,
**So that** I understand why I can't get in and don't assume the platform or my credentials are broken.

**Acceptance Criteria:**
- [ ] If my WOG AD credentials are valid but my agency isn't onboarded to OTEP, I'm blocked from the home page and see a message stating my agency isn't onboarded — not a generic error.
- [ ] When I see the not-onboarded message, it's distinct from the invalid-credentials error so I can tell the two situations apart.
- [ ] If my agency was onboarded before but has since been removed, my next login shows the same not-onboarded message rather than a broken or blank page.

**Edge cases:**
- Officer's agency was onboarded but is later removed — must fail closed at next login, not leave a stale session
- Message should not leak which agencies are or aren't onboarded beyond the officer's own
- Officer whose agency onboards later — login should succeed on next attempt with no extra steps

**Priority:** MVP — without a clear not-onboarded path, valid officers from pending agencies flood the helpdesk.

---

### WOG-09: Be blocked when I'm not a valid public officer

**As a** person without a valid WOG AD public officer account,
**I want to** be blocked from OTEP with a clear error,
**So that** only legitimate public officers can access the platform and I'm not left guessing why login failed.

**Acceptance Criteria:**
- [ ] If my WOG AD credentials are invalid or I'm not a public officer, login fails and I see a clear error message rather than being let in.
- [ ] When login fails on invalid credentials, the error doesn't reveal whether a given account exists.
- [ ] If my WOG AD account is disabled or locked, I see a specific message directing me to my agency's IT helpdesk — not a generic failure. [ASSUMPTION: WOG AD handles password management, MFA, and account lockout — OTEP does not re-implement these]
- [ ] When login fails for any reason, I stay on the login page and can retry without the app entering a broken state.

**Edge cases:**
- WOG AD account disabled/locked vs. simply invalid — distinct messages, both non-generic
- Error copy must avoid leaking account-existence info (security constraint — may need compliance review)
- Rate limiting after repeated failed attempts — WOG AD policy may govern this

**Priority:** MVP — access gating is a government security requirement; non-officers must never reach OTEP.

---

### WOG-10: Have OTEP resolve my agency from my AD identity

**As a** public officer logging in via WOG AD,
**I want** OTEP to work out which agency I belong to from my AD identity,
**So that** I get the right agency context without typing my agency in by hand.

**Acceptance Criteria:**
- [ ] When I log in, my agency is resolved from my WOG AD identity and I'm not asked to select or type it. [ASSUMPTION: AD returns only email + SOE-ID — agency must be derived from email domain, SOE-ID prefix, or a separate lookup]
- [ ] When my agency is resolved, OTEP uses it to decide whether my agency is onboarded — the same agency drives the access check.
- [ ] If my agency can't be resolved from my AD identity, I'm blocked with a clear message rather than dropped into OTEP with no agency context.

**Edge cases:**
- Resolution source not yet decided — email domain vs. SOE-ID prefix vs. separate lookup table (Open Question #4, confirm with Pow Hwee)
- Officer's email domain doesn't map cleanly to a single agency — ambiguous resolution needs a defined fallback
- Agency resolved differs from where the officer actually sits (secondment, cross-posting) — out of MVP scope, flag for later

**Priority:** MVP — agency must be known to run the onboarded-agency access rule; manual entry undermines the single-click flow.

---

### WOG-11: Skip separate account creation (go straight to OTEP)

**As a** public officer with WOG AD credentials,
**I want to** reach OTEP without creating a separate account,
**So that** I'm not slowed down by a registration step for a platform tied to credentials I already hold.

**Acceptance Criteria:**
- [ ] After a successful WOG AD login, I go straight to OTEP — there's no additional account creation or registration step.
- [ ] When I log in for the first time, OTEP recognises me from my WOG AD identity without me signing up. [ASSUMPTION: AD returns email + SOE-ID only — any first-login profile fields are collected, not a separate account]
- [ ] On every later login, I'm taken straight in with no repeat of any setup step.

**Edge cases:**
- First login may still need minimal profile fields (name, agency) since AD returns only email + SOE-ID — that's profile collection, not account creation (see WOG-06)
- Officer abandons any first-login profile step — define whether partial is saved or access is blocked until complete
- Returning officer must never be re-prompted for setup already completed

**Priority:** MVP — zero-signup access is core to the single-click value proposition.

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

### WOG-12: See a helpful message when my AD account is locked or disabled

**As a** public officer whose WOG AD account is locked or disabled,
**I want to** see a specific message that tells me where to get help,
**So that** I can resolve the lockout instead of repeatedly failing a generic login.

**Acceptance Criteria:**
- [ ] If my WOG AD account is locked, I see a message that directs me to my agency's IT helpdesk — not a generic "login failed".
- [ ] If my WOG AD account is disabled, I see a message explaining the account is inactive and who to contact — distinct from the incorrect-credentials message.
- [ ] When I see the locked/disabled message, OTEP does not let me retry endlessly against the same blocked account on this screen.
- [ ] When my account is locked or disabled, the message does not confirm whether my email or SOE-ID matches a real account.

**Edge cases:**
- Officer's WOG AD account is disabled/locked — should show specific message (not generic failure)
- Lockout originates in WOG AD, not OTEP — OTEP must surface AD's state, not re-implement lockout
- Account is unlocked by IT mid-session — next login attempt should succeed without a stale error

**Priority:** MVP — locked-account users flood the helpdesk if the message is generic

---

### WOG-13: See a graceful message when WOG AD is unreachable

**As a** user attempting to log in,
**I want to** see a graceful message when WOG AD is unreachable or down,
**So that** I understand the problem is temporary and not my fault.

**Acceptance Criteria:**
- [ ] If WOG AD is unreachable or down, I see "Service temporarily unavailable. Please try again later." — not a broken or blank page.
- [ ] When WOG AD is unreachable, I am not told my credentials are wrong — the message clearly states it's a service issue.
- [ ] When the AD connection times out, I see the service-unavailable message within a reasonable wait rather than an indefinite hang.
- [ ] Once WOG AD is reachable again, I can log in normally without clearing cache or restarting.

**Edge cases:**
- Network/AD service is down — graceful error message needed
- Partial AD outage (slow but not fully down) — timeout threshold needs definition
- AD recovers between retries — retry should succeed cleanly

**Priority:** MVP — AD outages will happen and must not look like a credential failure

---

### WOG-14: Be protected by rate limiting after repeated failed attempts

**As a** user (and the platform on my behalf),
**I want** repeated failed login attempts to be rate limited,
**So that** my account and OTEP are protected from brute-force attempts.

**Acceptance Criteria:**
- [ ] If I make repeated failed login attempts, further attempts are throttled or temporarily blocked rather than accepted indefinitely.
- [ ] When I am rate limited, I see a clear message that too many attempts were made and when I can try again.
- [ ] When I am rate limited, the message does not reveal whether the account exists or which field was wrong.
- [ ] After the cool-down period, I can attempt to log in again with valid credentials.

**Edge cases:**
- Rate limiting — after X failed attempts, what happens? (WOG AD policy may handle this — confirm with Pow Hwee whether OTEP enforces this or relies on WOG AD)
- Shared government workstation — one officer's failures should not lock out the next legitimate user unnecessarily
- Threshold (X attempts) and cool-down duration undefined — pending WOG AD / compliance policy

**Priority:** MVP — security baseline for a government platform

**Risks:**
- Ownership unclear — WOG AD policy may already enforce account lockout/rate limiting. If so, OTEP must not double-implement. Confirm with Pow Hwee what WOG AD handles before building.
- Threshold and cool-down values are TBD pending compliance — eng may build with a guess and rework if the mandated policy differs.

---

### WOG-15: Not have error messages reveal whether an account exists

**As a** user attempting to log in,
**I want** login error messages to never reveal whether an account exists,
**So that** my identity and other officers' accounts cannot be probed by attackers.

**Acceptance Criteria:**
- [ ] If I enter an unknown identity versus a valid identity with a wrong password, I see the same generic "Incorrect credentials. Please try again." message.
- [ ] When login fails, the message and response timing do not differ in a way that signals whether the account exists.
- [ ] When my account is locked, disabled, or rate limited, the message directs me to help without confirming the account is real to an unauthenticated user.
- [ ] When any login error is shown, no underlying AD detail, stack trace, or account-status field is exposed to me.

**Edge cases:**
- Error messages should not leak information about whether an account exists
- Timing side-channel — failure responses should not differ measurably by account existence
- Locked/disabled messaging must balance helpfulness with not confirming account existence — needs copy review with compliance

**Priority:** MVP — account-enumeration is a security constraint for government platforms

**Risks:**
- Error message copy must avoid leaking account-existence info (security constraint) — may need compliance review, shared with OTEP-110.
- Tension between WOG-12's "tell the user it's locked, go to IT helpdesk" and not confirming account existence to an unauthenticated user — resolve the copy with compliance before grooming.

---

### WOG-04: Stay logged in during my active session

**As a** logged-in user (officer or admin),
**I want to** remain authenticated while I'm actively using OTEP,
**So that** I don't get interrupted by repeated login prompts.

**Acceptance Criteria:**
- [ ] While I'm actively using OTEP, navigating between pages keeps me logged in — I'm not prompted to re-authenticate mid-session.
- [ ] If I've been idle for more than [X minutes — TBD], my session expires and I'm redirected to the login page. [ASSUMPTION: idle timeout value TBD — pending government compliance policy]
- [ ] If my session has expired and I try to do something, I see "Session expired, please log in again" — not a broken or blank page.

**Edge cases:**
- Browser tab left open overnight — should auto-expire on next interaction
- What's the government-mandated session timeout? (Open question #6 in brief)
- User switches tabs/apps for an extended period — idle timer should still apply

**Priority:** MVP — broken sessions destroy trust

**Risks:**
- Government-mandated session timeout unknown — the idle-timeout AC has a TBD value. If the compliance answer comes late, eng builds with a guess and may need to rework.
- Session expiry during FormSG form fill (edge case) risks data loss. Grace period or warning mechanism needs design input from Amber.

---

### WOG-16: Be warned before my idle session expires

**As a** logged-in user filling out an application,
**I want to** be warned before my idle session expires,
**So that** I don't lose work I've entered in a FormSG application.

**Acceptance Criteria:**
- [ ] If I've been idle and my session is about to expire, I see a warning before I'm logged out — not a silent redirect mid-task.
- [ ] When I see the expiry warning, I can choose to stay signed in, and doing so resets my idle timer and keeps me on the same page.
- [ ] If I'm part-way through a FormSG application when the warning appears, acting on it keeps my entered data intact — no silent data loss.
- [ ] If I don't respond to the warning within the grace period, my session expires and I see "Session expired, please log in again" rather than a broken page.

**Edge cases:**
- Grace period length is tied to the [TBD] idle timeout — pending government compliance policy
- User dismisses the warning but stays idle — should still expire after the grace period
- Warning fires while user is on an external FormSG form opened from OTEP — coordinate behaviour with apply flow

**Priority:** MVP — prevents data loss during the core apply flow, which directly destroys user trust

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

### WOG-17: Have a complete logout on shared government devices

**As a** public officer using a shared government workstation,
**I want to** be confident that logging out fully clears my session,
**So that** the next person on that device cannot access my OTEP account or data.

**Acceptance Criteria:**
- [ ] When I log out on a shared device, no cached credentials or session tokens remain that let the next user resume my session.
- [ ] After I log out, pressing the browser back button shows no cached OTEP page content — I'm redirected to login instead.
- [ ] After I log out, any active service worker or background session is invalidated so OTEP can't reload my data without a fresh login.
- [ ] If a new person logs in on the same device after me, they see only their own account — none of my profile, applications, or history.

**Edge cases:**
- Officer closes the browser without clicking "Log out" — next user should still not inherit the session
- Multiple officers using the same workstation in sequence through a shift
- Browser autofill / saved-password prompts on shared devices — out of OTEP's control but flag for IT guidance

**Priority:** MVP — shared workstations are common in government; incomplete logout is a security exposure

**Risks:**
- Cached credentials, service workers, and the browser back button all need explicit testing on shared-device scenarios. High rework cost if session architecture doesn't account for this upfront.

---

### WOG-18: Manage concurrent sessions across multiple devices

**As a** logged-in user,
**I want to** understand and control my sessions when I'm logged in on more than one device,
**So that** session behaviour across my devices is predictable and secure.

**Acceptance Criteria:**
- [ ] If I'm logged in on more than one device, OTEP applies a defined, consistent rule for concurrent sessions [ASSUMPTION: concurrent-session policy TBD — allow multiple vs. single active session, pending security team].
- [ ] When I log out on one device, the effect on my other devices follows that same defined rule — not unpredictable behaviour.
- [ ] If a concurrent session is ended remotely, on the affected device I see "Session expired, please log in again" rather than a broken page.
- [ ] When I log in on a new device, my existing sessions behave according to the policy and I'm not silently locked out without explanation.

**Edge cases:**
- Officer logs in on desktop and mobile simultaneously — allowed or single-session enforced?
- Logging out on one device — does it end all sessions, or only that device's?
- Stale session on a forgotten device — should still respect the idle timeout independently

**Priority:** MVP — resolves the open concurrent-sessions question from OTEP-71 and WOG-05; security team must confirm the policy before grooming

---

### WOG-06: First-time login: welcome and profile setup

**As a** public officer logging into OTEP for the first time,
**I want to** set up my profile and understand what OTEP offers,
**So that** I can orient myself and start using the platform.

**Flow:** First login detected (no existing OTEP profile for this SOE-ID) → welcome screen → officer fills in required profile fields → lands on home page.

**Data from AD:** Email + SOE-ID only. Name, agency, job title must come from officer or a separate data source.

**Acceptance Criteria:**
- [ ] The first time I log in, I see a welcome screen that explains what OTEP is.
- [ ] On first login, my email is already filled in — I don't need to type it. [ASSUMPTION: AD provides email only; name and agency must be entered manually]
- [ ] On first login, I'm asked to enter my name and agency before continuing. [ASSUMPTION: mandatory fields are name + agency — TBD with team]

**Edge cases:**
- Can we derive agency from email domain or SOE-ID format? (Would remove one manual step)
- What's mandatory vs. optional for profile setup? (Impacts how quickly officers get to value)

**Priority:** MVP — but keep minimal (welcome + mandatory fields only). Rich onboarding is R1.

**Risks:**
- Mandatory profile fields TBD — if the team can't agree on what's required vs optional, scope creeps from "minimal welcome screen" toward a full onboarding flow. Decide before grooming: name + agency is likely sufficient.
- If POCDEX can pre-populate officer data (name, agency) from SOE-ID, this story simplifies significantly. Depends on OTEP-183 spike outcome from Sprint 1.

---

### WOG-19: Skip the welcome on subsequent logins

**As a** returning public officer who has already completed first-time setup,
**I want to** skip the welcome screen and go straight to the home page,
**So that** I'm not slowed down by onboarding I've already seen.

**Acceptance Criteria:**
- [ ] On every subsequent login, I skip the welcome and go straight to the home page.
- [ ] When OTEP detects an existing profile for my SOE-ID, no welcome or profile-setup screen is shown.
- [ ] If my profile already has the mandatory fields filled, I'm never asked to re-enter name or agency on login.

**Edge cases:**
- A returning officer whose profile is incomplete from a prior abandoned setup — do they see the home page or get routed back to setup?
- Profile exists for the SOE-ID but mandatory fields were since cleared — treat as first-time or as resume?

**Priority:** MVP — pairs with WOG-06; returning officers are the common case and must not be re-onboarded.

---

### WOG-20: Resume an abandoned first-time profile setup

**As a** public officer who left first-time profile setup before completing it,
**I want to** resume and finish the setup on my next login,
**So that** I don't lose progress and can still get full access to OTEP.

**Acceptance Criteria:**
- [ ] If I abandon profile setup mid-way and log in again, I'm returned to profile setup rather than the home page.
- [ ] When I resume setup, any mandatory fields I already entered are still filled — I don't start from scratch. [ASSUMPTION: mandatory fields are name + agency — TBD with team]
- [ ] If I have not completed the mandatory fields, I cannot reach the home page until setup is complete.
- [ ] Once I finish the remaining mandatory fields, I land on the home page and subsequent logins skip setup.

**Edge cases:**
- What if officer abandons profile setup mid-way? (Save partial? Block access until complete?)
- Partial data persisted but officer never returns — how long is the incomplete profile retained?
- Officer abandons setup, agency is removed before they return — what happens on resume?

**Priority:** MVP — resolves the WOG-06 abandonment edge case; without it officers can be locked out or lose entered data.

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

1. **Session timeout policy** — What's the government-mandated idle timeout? (30 min? 60 min? Configurable?) Drives WOG-04 / WOG-16.
2. **Role source** — Are roles determined by AD groups, a custom AD attribute, or an OTEP-managed table synced with AD? Drives WOG-07 / WOG-02.
3. **MFA** — Does WOG AD enforce MFA at their end, or does OTEP need to implement it?
4. **Data from AD** — Exactly what fields does WOG AD provide? (name, email, agency, role, job title, unit?) Drives OTEP-71 / WOG-10 / WOG-06.
5. **Agency resolution** — Is agency derived from email domain, SOE-ID prefix, or a separate lookup? Drives WOG-10.
6. **Rate limiting ownership** — Does WOG AD policy already enforce lockout/rate limiting, or must OTEP? Drives WOG-14.
7. **Concurrent sessions** — Allow multiple active sessions or enforce single? Drives WOG-18.
8. **Shared devices** — Do officers commonly use shared workstations? Drives WOG-17 / WOG-05.
9. **First-time profile** — What's mandatory to collect on first login vs. what can be deferred? Drives WOG-06 / WOG-20.

## Assumptions

- WOG AD handles password management, MFA, and account lockout — OTEP does not re-implement these
- All OTEP users are public officers — no external/public user access in MVP
- Two roles only in MVP: officer and agency admin
- AD returns only **email + SOE-ID** on auth — name, agency, job title must come from officer input or separate data source

## Definition of Ready Checklist (from Eng Manager)

- [ ] Prioritised and able to deliver in a sprint
- [ ] All platform subtasks (including test cases) identified and created
- [ ] UI assets and UX flows designed and linked to all Acceptance Criteria (Amber)
- [ ] Feature flag designed with entry point identified
- [ ] API Contract identified and documented (Pow Hwee)

### Additional checks (PM)

- [ ] Acceptance criteria are clear and testable
- [ ] Dependencies identified
- [ ] Edge cases and error states documented

## Next Steps

- [ ] Confirm with Pow Hwee: what data does WOG AD return on auth? What role mechanism is planned? (Open Questions #2, #4, #5, #6)
- [ ] Review with Amber: login page UX, error states, first-time experience, session-expiry warning (WOG-16)
- [ ] Confirm session timeout + concurrent-session policy (compliance/security team)
- [ ] Compliance copy review for error messages (WOG-15 / OTEP-110)
- [ ] Grooming session
- [ ] Move to Confluence one-pager
- [ ] DoR met → Jira
