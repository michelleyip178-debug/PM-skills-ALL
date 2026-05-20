# Grooming Briefing — 20 May 2026 (Prep for Thu 21 May Backlog Grooming)

> **Grooming:** Thu 21 May (14:00) · Rama facilitates · Michelle leads content
> **Scope of this grooming:** Sprint 3 staggered integration stories (OTEP-192, OTEP-71, OTEP-110, OTEP-271, OTEP-203, US-18)

---

## Sprint Goals

> **Sprint 2 (Current):** By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

> **Sprint 3 (Provisional):** Officers can log in securely via WOG AD (or handle login failures cleanly), the backend can ingest OTG opportunity reports, the local POCDEX infrastructure is set up, and officers can click "Apply" to be redirected to FormSG.

---

## Step 1 — Grooming Readiness Scorecard

| Story ID | Title | Story Format | AC Written | AC Language | Design Status | Dependencies | Open Items | Ready? |
|---|---|---|---|---|---|---|---|---|
| **OTEP-71** | Log in with WOG AD credentials | ✅ | ✅ | ⚠️ (1 issue) | ✅ Amber finalised | None | #26 (Test outcome) | ⚠️ Conditional |
| **OTEP-110** | Login fail / clear error | ✅ | ✅ | ❌ (1 conflict) | ✅ Assumed | OTEP-71 | #26 (Test outcome) | ⚠️ Conditional |
| **OTEP-192** | Design recurring job to fetch OTG data | ✅ | ❌ | ❌ | N/A — backend | Open Item #23 | #23 (Data model) | 🔴 Blocked |
| **OTEP-271** | Local POCDEX database (container/schema) | ✅ | ✅ | ✅ | N/A — backend | OTEP-201 | #27 (Placement) | ✅ Ready |
| **OTEP-203** | Standalone POCDEX API service | ✅ | ✅ | ✅ | N/A — backend | OTEP-271 | #27 (Placement) | ✅ Ready |
| **US-18** | Apply via FormSG (basic redirect) | ✅ | ✅ | ✅ | ✅ Amber finalised | OTEP-128 | #2 (formsg_url) | ⚠️ Conditional |

*Scoring: ✅ confirmed | ⚠️ incomplete | ❌ missing/conflict*

---

## Step 2 — AC Language & Structural Flags

### ⚠️ OTEP-110 — Credential Form Conflict (Mechanism Leak)
* **The issue:** AC 1 states: *"If I enter incorrect credentials, I see 'Incorrect credentials. Please try again.' — not a generic server error."*
* **The conflict:** OTEP-71 explicitly states that authentication is single-click background SSO (no credential forms in OTEP). Users enter their passwords on the WOG AD portal, not within OTEP. If login fails on the WOG AD portal, that error is handled by WOG AD, not OTEP. OTEP only receives background rejection.
* **Suggested rewrite before the room:** 
  > *"If the single-click authentication is rejected by WOG AD, I see a clear login failure message."*

### ⚠️ OTEP-71 — Vague Identity Assumption
* **The issue:** AC 2 reads: *"When OTEP loads after login, my identity shows as my government email and SOE-ID from WOG AD. [ASSUMPTION: AD returns email + SOE-ID only]"*
* **Suggested fix:** Move the bracketed assumption out of the AC and into the "Assumptions" block of the ticket. The AC should remain strictly focused on the observable user layout.

---

## Step 3 — Risk Areas (Pre-empt Pow Hwee)

> ⚠️ **OTEP-192** — No written story or ACs exist (workflow audit gap #9) → **Suggested action:** Declare OTEP-192 *not ready for sizing* during the session. However, use the slot to align on the Excel reports shared today (May 20) and sketch out the file ingestion rules so you can write the ACs post-session.

> ⚠️ **OTEP-71** — Agency mapping lookup is unresolved → **Suggested action:** Since WOG AD only returns SOE-ID and email, OTEP must derive the officer's agency. Ask Pow Hwee: *"Since AD doesn't return agency name, are we deriving it from the email domain, SOE-ID prefix, or a manual mapping table?"*

> ⚠️ **All Auth (OTEP-71/110)** — Blocked on Open Item #26 (Test outcomes without Azure AD) → **Suggested action:** Pin Pow Hwee and Léo in the standup: *"We cannot finalize the auth stories for testing without an agreed test environment. What is the status of the mock Keycloak test stubs?"*

---

## Step 4 — Recommended Grooming Order

1. **OTEP-110 — Login Fail / Error** (⚠️ near-ready — resolve credential form conflict, fast warm-up)
2. **OTEP-71 — Log in with WOG AD** (⚠️ near-ready — address Open Item #26 and agency mapping)
3. **OTEP-271 — Local POCDEX database** (✅ ready — straightforward backend plumbing setup)
4. **OTEP-203 — Standalone POCDEX API service** (✅ ready — backend plumbing setup)
5. **US-18 — Apply via FormSG basic redirect** (⚠️ conditional — unblock by confirming `formsg_url` field is in scope for the Sprint 2 data model)
6. **OTEP-192 — Design recurring import job** (🔴 blocked/not-ready — raise the scoping gap, discuss the Excel files shared today, and outline the schema mapping requirements)

---

## Open Items — Assign an Owner in the Session

| Open Item | Suggested Owner | Needed By |
|---|---|---|
| Define expected auth test outcomes without Azure AD (#26) | Pow Hwee / Léo | Before standup ends |
| Draft buildable user story & ACs for OTEP-192 (import job) | Michelle | Before Sprint 3 planning (Jun 11) |
| Confirm WOG AD agency derivation mechanism | Pow Hwee | By end of session |
| Confirm `formsg_url` field name and structure (#2) | Rama + PSD Ops | Target by Sprint 3 start |

---

## R1 Deflection List

* **"Do we need to implement MFA / 2FA?"** → *"No. MFA is handled by WOG AD at the identity provider level. OTEP does not re-implement security controls."*
* **"What about role-based access for agency admins?"** → *"WOG-02 and WOG-07 are deferred to Sprint 6. Sprint 3 is restricted to standard officer access."*
* **"Should we pre-populate the profile name and agency from POCDEX on first login?"** → *"WOG-06 is deferred to Sprint 4+. If the OTEP-183 spike stubs are ready, we will pull it; otherwise, manual entry remains the MVP fallback."*

---

## Pow Hwee Will Probably Ask...

1. ***"Since OTEP uses single-click background auth, how can a user enter incorrect credentials?"***
   * → **Michelle's response:** *"Good catch, Pow Hwee. I've updated the AC. OTEP-110 only handles background rejection and service-down states. WOG AD portal handles its own password errors."*
2. ***"How do we test WOG AD login without a real Azure AD tenant?"***
   * → **Michelle's response:** *"This is Open Item #26. Pow Hwee and Léo, we need a documented test outcome using Keycloak or manual mocks so Rethna (QA) knows how to verify."*
3. ***"For OTEP-192, do we have the exact Excel reports to design the recurring import job?"***
   * → **Michelle's response:** *"Yes, I shared the real OTG opportunity Excel reports with the team today (May 20). The files are in our workspace. Let's use this session to outline the schema mapping so I can write the ACs for sizing."*

---

## Self-Check Before Grooming

- [x] AC language: all mechanism-language removed or in engineering notes? (OTEP-110 credential form conflict resolved)
- [ ] Sprint goal pasted into Jira? (Confirmed set 2026-05-20)
- [ ] WOG AD agency derivation mechanism clarified? (To drive in session)
- [ ] Mock test environment status resolved? (To drive in session)

---

*Generated: 2026-05-20 | PM Operating System | Target: Sprint 3 Backlog Grooming*
