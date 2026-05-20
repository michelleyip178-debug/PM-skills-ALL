# Grooming Brief — 21 May 2026 (Sprint 3 Backlog Grooming)

**Session:** 14:00–16:00 · L11 Anson · Facilitator: Rama · Content lead: Michelle
**Sprint 3 dates:** 2 Jun – 13 Jun · **Leo is out PM — wrap on time**

---

## Sprint Goal (propose in session)

> An officer can log in to OTEP using their WOG AD credentials, stay authenticated during their session, and log out securely — completing the auth end-to-end flow. OTG opportunities start loading in the background (OTEP-192 recurring job).

*Sprint-checklists.md Sprint 3 goal says TBD — propose this today.*

---

## Readiness Scorecard

| Story | Story Format | AC Written | AC Language | Design | Dependencies | Ready? |
|-------|-------------|------------|-------------|--------|-------------|--------|
| OTEP-305 Log out | ✅ | ✅ | ✅ | ❌ no logout button design | Decision #4 concurrent sessions | ⚠️ |
| OTEP-304 Stay logged in | ✅ | ⚠️ timeout TBD | ✅ | ❌ session expiry UI not designed | Decision #1 idle timeout (compliance) | ⚠️ |
| OTEP-71 Login via WOG AD | ✅ | ⚠️ Jira weak; auth.md complete | ✅ (auth.md) | ❌ login page not linked to Jira | Decision #2 agency source; OTEP-111 | ⚠️ |
| OTEP-110 Login fail errors | ⚠️ | ❌ Jira AC = 1 line, mechanism language | ❌ mechanism | ❌ error states not designed | Compliance sign-off (WOG-15 NFR) | ❌ |
| OTEP-192 Recurring OTG job | ❌ no user story | ❌ one partial mechanism AC | ❌ mechanism | N/A backend | OTEP-193 data model (In Progress) | ❌ |
| OTEP-191 Credential vault | ❌ no description | ❌ none | — | — | AWS infra may have resolved | ❌ verify/close |

---

## Fix Before You Walk In

These two stories will be called out immediately if not fixed. Do this now, before 14:00.

**OTEP-110 Jira ACs are empty.** The current Jira description is: *"Authentication failure will be handled at WOG AD."* — one mechanism sentence, no user ACs. Paste the ACs from `auth.md` into Jira before the session:
- If credentials incorrect → "Incorrect credentials. Please try again."
- If account locked → message directs to IT helpdesk (distinct from wrong-password message)
- If account disabled → message names inactive account + who to contact
- If WOG AD unreachable → "Service temporarily unavailable. Please try again later."
- If AD times out → service-unavailable message appears within a defined wait — not an indefinite hang
- Once WOG AD recovers → officer can log in normally without clearing cache

⚠️ **NFR flag (WOG-15 non-enumeration):** Error messages must not reveal whether an account exists. Locked vs. invalid account messages must be indistinguishable *to an outsider*. This needs compliance sign-off before Amber writes the copy. Raise this in the session — don't let copy be written without it.

**OTEP-192 has no user story format and one mechanism AC.** The Jira description says: *"The system must silently drop and log any card that is missing mandatory data."* This is an implementation note, not an AC. Rewrite before grooming:

**Proposed story:**
> As a product team, I want OTG opportunity data to be fetched and refreshed automatically, so that officers always see current listings without manual intervention.

**Proposed ACs (to discuss at grooming):**
- [ ] Opportunities data is refreshed from the OTG Excel export on a recurring schedule — officers see up-to-date listings without a manual trigger.
- [ ] When a record in the OTG export is missing any mandatory field (ID, Title, Agency, Type, Posting Date, or Closing Date), it is excluded from the listing — other valid records are not affected.
- [ ] When the OTG export file is unavailable or malformed, the most recently fetched valid data remains displayed — the listing does not go blank.
- [ ] *(Scope to confirm with Pow Hwee: What triggers the job? What is the run frequency? What is the SLA for data freshness?)*

---

## Grooming Order (recommended)

| # | Story | Why this order | Expected time |
|---|-------|---------------|---------------|
| 1 | **OTEP-305** Log out | Best-formed ACs; quick win to start. Surfaces concurrent-session default needed for OTEP-304. | ~15 min |
| 2 | **OTEP-304** Stay logged in | Builds on session discussion from OTEP-305; confirm timeout source with Pow Hwee. | ~20 min |
| 3 | **OTEP-71** Login via WOG AD | Core story; get Pow Hwee to commit to decision #2 (agency source) in the room. | ~25 min |
| 4 | **OTEP-110** Login fail errors | Related to OTEP-71 errors; fix the mechanism AC issue before session — then discuss NFR. | ~25 min |
| 5 | **OTEP-192** Recurring OTG job | Scope is broad — timebox the discussion. Main ask: confirm trigger, frequency, and freshness SLA. | ~20 min |
| 6 | **OTEP-191** Credential vault | Pow Hwee flagged this himself — quick verify-or-close. Ask if AWS infra resolved it. | ~5 min |

---

## Decisions to Get in the Room

| Decision | Owner | Why it matters |
|---------|-------|---------------|
| Agency determination source — email domain, SOE-ID prefix, or lookup table? | Pow Hwee | OTEP-71 edge case + WOG-10 unblocked by this |
| Concurrent session default — allow multiple or enforce single? | Security / Pow Hwee | OTEP-305 edge case "does logout on one device affect all?" |
| Idle timeout value — what is the government-mandated timeout? | Pow Hwee / compliance | OTEP-304 has `[30 minutes — TBD]` placeholder |
| OTEP-192 job trigger — time-based, manual, or event-driven? And run frequency? | Pow Hwee | AC can't be written without this; story can't be estimated |
| OTEP-191 — is this ticket still needed or resolved by AWS infra? | Pow Hwee | Close if resolved; define if not |

---

## Open Items — Assign Owner in Session

| # | Item | Suggested owner | Needed by |
|---|------|----------------|-----------|
| 26 | Define expected auth test outcome without AzureAD | Pow Hwee / Leo | Sprint 3 start |
| — | Compliance sign-off for OTEP-110 error copy (WOG-15 NFR) | Michelle → route to compliance | Before Amber designs error states |
| — | Amber: design login error states (OTEP-110), logout flow (OTEP-305), session expiry screen (OTEP-304) | Michelle to brief Amber | Before Sprint 3 build |

---

## R1 Deflection List

If these come up, park them immediately:
- **Welcome/onboarding screen** → "R1 — name entry only for MVP, no explainer screen"
- **WOG-16 pre-expiry session warning** → "Deferred until apply flow is live — Sprint 3+ at earliest"
- **WOG-14 rate limiting** → "Pow Hwee to confirm WOG AD owns this; if yes, no OTEP ticket needed"
- **WOG-18 concurrent sessions** → "This is a one-line policy decision, not a feature. Log it and move on."
- **WOG-17 shared device logout hardening** → "Engineering note, not an AC. Flag it for the AC test plan."
- **Agency admin login (WOG-02)** → "Sprint 6 — out of scope today"
- **RBAC / role-based access (WOG-07)** → "Sprint 6 — out of scope today"
- **Competency on profile** → "R1 — name-only for MVP"

---

## Pow Hwee Will Probably Ask...

- *"How does OTEP know which agency the officer belongs to?"* — Be ready to drive decision #2; don't leave it open-ended.
- *"OTEP-110 only has one sentence in Jira — what are we actually building?"* — Pre-empt this: paste the ACs before the session.
- *"OTEP-192 — how often does the job run? What's the trigger? What's the SLA for data freshness?"* — Have your proposed ACs ready; ask him to fill in the trigger/frequency.
- *"What's the actual idle timeout? Is there a GovSG standard?"* — Push back: "What's your reading of the government policy? I'll chase compliance if you don't know."
- *"Is OTEP-191 still needed? I think AWS may have resolved it."* — His call to close it; ask him to confirm today.
- *"Are OTEP-304 and OTEP-305 new? They weren't in the original Sprint 3 plan."* — Confirm: pulled forward from Sprint 4+; confirmed in Jira as OTEP-304/305.
- *"WOG-17 shared device logout — is this in scope or separate?"* — Fold into OTEP-305 as an engineering note; no separate ticket needed.

---

## Self-Check

- [ ] Pasted OTEP-110 ACs from auth.md into Jira
- [ ] Rewrote OTEP-192 into user story format with proposed ACs
- [ ] Confirmed OTEP-304 and OTEP-305 are visible on Sprint 3 Jira board
- [ ] Checked OTEP-191 is on Sprint 3 board with Pow Hwee's comment visible
- [ ] Briefed Amber: she needs to design login error states, logout flow, session expiry screen before Sprint 3 build starts
