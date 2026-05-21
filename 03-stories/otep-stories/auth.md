# User Stories: WOG AD Authentication (Epic 5)

**Epic:** WOG AD Authentication (Epic 5)
**One-pager:** _TODO: Confluence link_
**Status:** Draft — Auth epic deferred to Sprint 4+ (2026-05-21). Needs grooming before Sprint 4 planning. Auth stories still showing in Jira Sprint 3 — must be moved in Jira by Pow Hwee.
**Criticality:** MVP blocker — all other epics depend on this
**Scope decision:** Officers only for MVP. Agency admin login + RBAC (WOG-02, WOG-07) deferred to Sprint 6 (decision 2026-05-12). Auth accepted as-is (decision 2026-05-12). Sprint 2 auth scope = minimal, check user exists + name (decision 2026-05-13). **Auth epic (OTEP-71, OTEP-110, OTEP-304, OTEP-305) moved from Sprint 3 to Sprint 4+ (decision 2026-05-21) — no WOG AD UAT environment available (open item #26).**

---

## Decisions needed before grooming

These are decisions, not open questions. Each blocks at least one story from reaching "ready."

| # | Decision needed | Owner | Blocks |
|---|---|---|---|
| 1 | **Idle-timeout value** — what is the government-mandated idle timeout? | Compliance / security | WOG-04 |
| 2 | **Agency-resolution source** — email domain, SOE-ID prefix, or a lookup table? | Pow Hwee | WOG-10 |
| 3 | **Rate-limit ownership** — does WOG AD already enforce account lockout, or must OTEP build it? | Pow Hwee | WOG-14 spike |
| 4 | **Concurrent-session default** — allow multiple sessions (simplest) or enforce single-session? Pick a default; don't build a management feature. | Security team | WOG-18 |
| 5 | **Mandatory profile field** — name only, or name + something else? (email auto-fills; agency comes from WOG-10) | Michelle + team | WOG-06 |
| 6 | **OTEP-111 scope** — does the existing Sprint 1 "Officers with no access" ticket already cover the not-onboarded and invalid-officer messages? | Pow Hwee | WOG-08/09 absorbed |

---

## Story Summary

| ID | Story | Sprint | Action |
|----|-------|--------|--------|
| OTEP-71 | Log in with WOG AD credentials | **4+** ⚠️ *(was 3, deferred 2026-05-21 — no WOG AD UAT env)* | Keep (absorbs WOG-11). Still in Jira Sprint 3 — move to Sprint 4+ |
| OTEP-111 | Officers with no access | 1 ✔ | Existing ticket — confirm it covers WOG-08/09 ACs |
| WOG-10 | Resolve agency from AD identity | **4+** *(was 3)* | Keep — spike decision #2 first |
| OTEP-110 | Login fail / clear error | **4+** ⚠️ *(was 3, deferred 2026-05-21)* | Keep (absorbs WOG-12, WOG-13; NFR from WOG-15). Still in Jira Sprint 3 — move to Sprint 4+ |
| OTEP-304 | Stay logged in during session *(was WOG-04)* | **4+** ⚠️ *(was 3, deferred 2026-05-21)* | Ticketed OTEP-304. Still in Jira Sprint 3 — move to Sprint 4+ |
| OTEP-305 | Log out of OTEP *(was WOG-05)* | **4+** ⚠️ *(was 3, deferred 2026-05-21)* | Ticketed OTEP-305. Still in Jira Sprint 3 — move to Sprint 4+ |
| WOG-17 | Complete logout on shared devices | **4+** *(was 3)* | Keep (trim service-worker AC) |
| WOG-06 | First-time login + profile setup | **4+** *(was 3)* | Trim — name only, no welcome screen (R1) |
| WOG-14 | Rate limiting | — | **Convert to spike** (decision #3) |
| WOG-16 | Pre-expiry session warning | — | **Defer** — pairs with apply flow (Sprint 3+) |
| WOG-18 | Concurrent sessions | — | **Replace with default policy decision** (decision #4) |
| WOG-02 | Agency admin login | 6 | Deferred — Sprint 6 |
| WOG-07 | Role-based access control | 6 | Deferred — Sprint 6 |

---

## Stories

### OTEP-71: Log in with WOG AD credentials

**As a** public officer from an onboarded agency,
**I want to** log in to OTEP via WOG AD with a single click,
**So that** I can access the platform using my existing government credentials without creating a separate account.

**Acceptance Criteria:**
- [ ] When I click "Log in with WOG AD" on the login page, I land on the OTEP home page — no manual credential entry needed.
- [ ] When OTEP loads after login, my identity shows as my government email and SOE-ID from WOG AD. [ASSUMPTION: AD returns email + SOE-ID only]
- [ ] After a successful login, there is no additional account creation or registration step — I go straight to OTEP.
- [ ] If login fails for any reason (invalid credentials, agency not onboarded, AD unreachable), I see a specific error — not a generic server error. See OTEP-110 for error-state detail.
- [ ] If my agency is not onboarded or my WOG AD credentials are invalid, I am blocked with a specific message. See OTEP-111 for no-access detail.

**Edge cases:**
- AD returns only email + SOE-ID — profile data (name, job title, unit) must come from officer or a separate source
- Officer's agency was onboarded but is later removed — fail closed on next login (see OTEP-111)
- Multiple concurrent sessions on different devices — default policy decision #4 applies

**Priority:** MVP — nothing works without this; all other epics depend on auth.

---

### OTEP-111: Officers with no access

> **Note:** This is an existing Sprint 1 Jira ticket ("Officers with no access"). It is not re-groomed here. Confirm with Pow Hwee that it covers the following two scenarios — if not, raise an amendment to OTEP-111 rather than creating new tickets.

**Scenarios that must be covered by OTEP-111:**

**Not-onboarded agency (was WOG-08):**
- [ ] If my WOG AD credentials are valid but my agency isn't onboarded, I'm blocked and see a message stating my agency isn't onboarded — not a generic error.
- [ ] If my agency was previously onboarded but has since been removed, my next login shows the same not-onboarded message — not a broken or blank page.
- [ ] The not-onboarded message is distinct from the invalid-credentials error so I can tell the two situations apart.

**Invalid officer (was WOG-09):**
- [ ] If my WOG AD credentials are invalid or I'm not a public officer, login fails with a clear error and I'm not let in.
- [ ] When login fails for any reason, I stay on the login page and can retry — the app doesn't break.

**Priority:** Sprint 1 — already ticketed. Amend OTEP-111 if these scenarios are not covered.

---

### WOG-10: Resolve my agency from my AD identity

**As a** public officer logging in via WOG AD,
**I want** OTEP to resolve which agency I belong to from my AD identity,
**So that** I get the right agency context without typing my agency in by hand.

> **Dependency:** Blocked on decision #2 (agency-resolution source). Raise with Pow Hwee before grooming — once the source is confirmed this becomes straightforward delivery.

**Acceptance Criteria:**
- [ ] When I log in, my agency is resolved automatically from my WOG AD identity — I'm not asked to select or type it. [ASSUMPTION: AD returns email + SOE-ID only — resolution source TBD: email domain, SOE-ID prefix, or separate lookup]
- [ ] The resolved agency drives the onboarded-agency access check — the same value powers both.
- [ ] If my agency can't be resolved from my AD identity, I'm blocked with a clear message rather than dropped into OTEP with no agency context.

**Edge cases:**
- Email domain doesn't map cleanly to one agency — ambiguous resolution needs a defined fallback
- Secondment / cross-posting — out of MVP scope; flag for later

**Priority:** MVP — agency must be known to run the access check; manual entry breaks the single-click flow.

---

### OTEP-110: See a clear error when login fails

**As a** public officer attempting to log in,
**I want to** see a specific, helpful error message when login fails,
**So that** I know what went wrong and how to fix it.

**Acceptance Criteria:**
- [ ] If I enter incorrect credentials, I see "Incorrect credentials. Please try again." — not a generic server error.
- [ ] If my WOG AD account is locked, I see a message that directs me to my agency's IT helpdesk — not a generic "login failed."
- [ ] If my WOG AD account is disabled, I see a message explaining the account is inactive and who to contact — distinct from the incorrect-credentials message.
- [ ] If WOG AD is unreachable or down, I see "Service temporarily unavailable. Please try again later." — not a message that implies my credentials are wrong.
- [ ] When the AD connection times out, the service-unavailable message appears within a defined wait — not an indefinite hang. [ASSUMPTION: timeout threshold TBD — confirm with Pow Hwee]
- [ ] Once WOG AD is reachable again, I can log in normally without clearing cache or restarting.

**NFR — account enumeration (from WOG-15):** Error messages must not reveal whether an account exists. An unknown identity and a valid identity with a wrong password must produce the same message and a consistent response time. No AD detail, stack trace, or account-status field is exposed. This constraint applies to all error copy — get compliance sign-off before build.

**Edge cases:**
- Locked vs. disabled vs. invalid — three distinct messages, none generic, none leaking account existence
- Timing side-channel — response time must not differ measurably by account existence
- Locked account copy ("go to IT helpdesk") vs. not confirming account existence — one compliance call resolves both; WOG-15 is the owner

**Priority:** MVP — critical for user trust and reducing helpdesk load

**Risks:**
- Sprint assignment TBD (S1 carry-over vs S3) — confirm at Sprint 1 finalisation.
- Error message copy needs compliance sign-off to balance locked-account helpfulness against non-enumeration. Don't build until copy is approved.

---

### WOG-04 (now OTEP-304): Stay logged in during my active session

> **Ticketed OTEP-304 (2026-05-21 sync). Deferred to Sprint 4+ (2026-05-21).** Still showing in Jira Sprint 3 — move to Sprint 4+ in Jira.

**As a** logged-in public officer,
**I want to** remain authenticated while I'm actively using OTEP,
**So that** I don't get interrupted by repeated login prompts.

**Acceptance Criteria:**
- [ ] While I'm actively using OTEP, navigating between pages keeps me logged in — I'm not re-prompted mid-session.
- [ ] If I've been idle for more than [X minutes — TBD], my session expires and I'm redirected to the login page. [ASSUMPTION: idle timeout value TBD — pending government compliance policy; see decision #1]
- [ ] If my session has expired and I try to do something, I see "Session expired, please log in again" — not a broken or blank page.

**Edge cases:**
- Browser tab left open overnight — auto-expire on next interaction
- User switches tabs/apps for an extended period — idle timer still applies

**Priority:** MVP — broken sessions destroy trust

**Risks:**
- Government-mandated idle timeout is unknown. Build with a placeholder; rework is likely if compliance answer lands late.

---

### WOG-05 (now OTEP-305): Log out of OTEP

> **Ticketed OTEP-305 (2026-05-21 sync). Deferred to Sprint 4+ (2026-05-21).** Still showing in Jira Sprint 3 — move to Sprint 4+ in Jira.

**As a** logged-in public officer,
**I want to** log out of OTEP,
**So that** my session ends and no one else can access my account on this device.

**Acceptance Criteria:**
- [ ] When I click "Log out", my session ends and I'm taken to the login page.
- [ ] After logging out, pressing the browser back button doesn't return me to OTEP — I'm redirected to login.
- [ ] After logging out, typing any OTEP URL directly into the browser redirects me to the login page.

**Edge cases:**
- Logging out on one device — effect on other sessions governed by the concurrent-session default (decision #4)
- Shared workstations — see WOG-17 for hardening requirements

**Priority:** MVP — security requirement for government platforms

---

### WOG-17: Complete logout on shared government devices

**As a** public officer using a shared government workstation,
**I want to** be confident that logging out fully clears my session,
**So that** the next person on that device cannot access my OTEP account or data.

**Acceptance Criteria:**
- [ ] After I log out on a shared device, the next person who opens OTEP in the same browser sees the login page — not my account.
- [ ] After I log out, pressing the browser back button shows the login page — no cached OTEP content from my session.
- [ ] If a new person logs in after me on the same device, they see only their own account — none of my profile, applications, or history.

**NFR — implementation note:** Session tokens, service workers, and any background processes must be invalidated on logout. This belongs in the engineering acceptance test plan, not an AC.

**Edge cases:**
- Officer closes the browser without clicking "Log out" — define expected behaviour (idle timeout is the fallback)
- Browser autofill / saved-password prompts — out of OTEP's control; flag for IT guidance

**Priority:** MVP — shared workstations are common in government; incomplete logout is a security exposure

**Risks:**
- High rework cost if session architecture doesn't account for shared-device scenarios upfront. Raise with Pow Hwee during technical design.

---

### WOG-06: First-time login and profile setup

**As a** public officer logging into OTEP for the first time,
**I want to** enter my name so my profile is complete,
**So that** I can start using the platform with a usable identity.

**Flow:** First login detected (no existing OTEP profile for this SOE-ID) → profile setup screen → officer enters name → lands on home page.

**Data from AD:** Email + SOE-ID only. Name must be entered by officer. Agency resolved via WOG-10 — do not ask the officer to type it.

**Acceptance Criteria:**
- [ ] The first time I log in, I'm taken to a profile setup screen before the home page.
- [ ] On the setup screen, my email is already filled in — I don't need to type it. [ASSUMPTION: AD provides email only]
- [ ] I'm asked to enter my name before continuing. [ASSUMPTION: mandatory field is name only — per decision #5]
- [ ] On every subsequent login, I go straight to the home page — no setup screen. *(absorbed from WOG-19)*
- [ ] If I started profile setup on a previous login but didn't finish entering my name, my next login returns me to the setup screen — not the home page. *(absorbed from WOG-20)*

**Edge cases:**
- If agency auto-resolution (WOG-10) fails, what does the setup screen show for agency? Define the fallback before Amber designs the screen.
- Welcome/explainer screen deferred to R1 — MVP setup screen is name entry only.

**Priority:** MVP — but keep to one field (name). Rich onboarding is R1.

**Risks:**
- Mandatory field set must be agreed before Amber designs the screen. Name-only is the recommendation; hold to it.
- If POCDEX can pre-populate name from SOE-ID, this story collapses to zero — confirm OTEP-183 spike outcome before building.

---

## Parked — not build-ready for MVP

### WOG-14: Spike — confirm rate-limiting ownership

**What to answer:** Does WOG AD already enforce account lockout and rate limiting? The standing assumption says yes ("WOG AD handles password management, MFA, and account lockout — OTEP does not re-implement these"). If confirmed, OTEP builds nothing here. Only create a delivery ticket if WOG AD does *not* cover it.

**Owner:** Pow Hwee
**When:** Before Sprint 3 grooming

---

### WOG-16: Pre-expiry session warning (deferred)

Deferred to the sprint that ships the apply flow (Sprint 3+). The FormSG data-loss risk that motivated this story only exists once apply is live.

**Note:** The AC about "FormSG entered data stays intact" is unachievable — OTEP does not control state inside an external FormSG form. Rescope to "warn before expiry + offer to extend session" when this is picked up.

---

### WOG-18: Concurrent sessions — policy decision, not a feature

This does not need a delivery ticket. Make a one-line default decision and record it in `decisions-log.md`:

> *"Allow multiple concurrent sessions. Each session respects the idle timeout independently."*

If the security team rules differently, revisit. Do not build a session-management feature in MVP.

---

## Deferred to Sprint 6

### WOG-02: Log in as agency admin with elevated permissions

**As an** agency admin,
**I want to** log in and be recognised as an admin,
**So that** I can access admin-level features (e.g. posting opportunities, viewing analytics) in addition to officer features.

**Acceptance Criteria:** [DEFERRED to Sprint 6]
- [ ] If I'm registered as an agency admin in WOG AD, OTEP grants me admin-level access when I log in.
- [ ] As an admin, I see admin navigation and features that a standard officer doesn't see.
- [ ] As a standard officer, I cannot access admin-only features — they're hidden, not just disabled.

**Edge cases:**
- Officer promoted to admin — how quickly does the role update? Real-time from AD or synced periodically?
- Admin demoted — access must be revoked promptly
- Can a person be both officer and admin? (e.g. admin who also browses opportunities)

**Priority:** Deferred to Sprint 6. Consolidate with WOG-07 — they're the same mechanism.

---

### WOG-07: Role-based access control

**As a** public officer or agency admin,
**I want** OTEP to enforce the correct access level based on my WOG AD role,
**So that** I only see features appropriate to my role.

**Acceptance Criteria:** [DEFERRED to Sprint 6]
- [ ] When I log in, OTEP assigns me the correct role (officer or agency admin) based on my WOG AD attributes.
- [ ] If I have the officer role, admin-only pages and features are hidden — not just greyed out or disabled.
- [ ] If my role changes in WOG AD, the next time I log in OTEP reflects the updated role.

**Edge cases:**
- Role source: AD groups vs. custom attribute vs. OTEP-managed lookup? (Technical decision for Pow Hwee — resolve before Sprint 6 grooming)
- Grace period for role changes — immediate or next login?

**Priority:** Deferred to Sprint 6 with WOG-02. Start with 2 roles (officer, agency admin).

---

## Assumptions

- WOG AD handles password management, MFA, and account lockout — OTEP does not re-implement these
- All OTEP users are public officers — no external/public user access in MVP
- Two roles only in MVP: officer and agency admin
- AD returns only **email + SOE-ID** on auth — name must come from officer input; agency resolved via WOG-10

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

- [ ] Pow Hwee: confirm agency-resolution source (decision #2) — unblocks WOG-10
- [ ] Pow Hwee: confirm WOG AD owns rate limiting (decision #3) — likely kills WOG-14
- [ ] Security team: pick a concurrent-session default (decision #4) — closes WOG-18 without build
- [ ] Michelle + team: confirm name-only is the mandatory profile field (decision #5) — unblocks WOG-06
- [ ] Pow Hwee: confirm OTEP-111 covers WOG-08/09 scenarios (decision #6)
- [ ] Compliance: idle-timeout value (decision #1) — unblocks WOG-04
- [ ] Compliance: error message copy sign-off for OTEP-110 + NFR from WOG-15
- [ ] Amber: design WOG-06 profile screen (name entry + email pre-fill) and OTEP-110 error states
- [ ] Confirm OTEP-183 POCDEX spike outcome — may simplify WOG-06 to zero
- [ ] Grooming session
- [ ] Move to Confluence one-pager
- [ ] DoR met → Jira
