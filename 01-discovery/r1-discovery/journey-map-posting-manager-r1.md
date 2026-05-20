# Customer Journey Map — Posting Manager (R1+ Future State)

**Persona:** Posting Manager — HR Executive/Officer at Ministry or Statutory Board
**State:** R1+ future state (assumes ATS decision resolved: OTEP owns application records)
**Created:** 2026-05-20
**Dependencies:** ATS architecture decision (Conflict C1 in r1-candidate-list.md) — this journey is blocked until that call is made

> **Important caveat:** Posting creation still happens in OTG in R1 (agency-owner side deferred to R4, per 2026-05-12 BO Senior Level direction). This map starts from the point where a posting already exists in CareerCompass and officers are beginning to apply.

---

## Journey Stages

### Stage 1 — Awareness
**How the Posting Manager first encounters OTEP as a tool for them**

| | Detail |
|---|---|
| **Touchpoint** | Email from agency IT / HR leadership: "Applications for your OTG postings are now managed in CareerCompass" |
| **User action** | Reads the communication; clicks through to CareerCompass agency login |
| **Thoughts** | "Do I still get the FormSG emails? Is this replacing my spreadsheet or adding to it?" |
| **Emotion** | 😐 Cautious — new system, no pain yet but also no reason to be excited |
| **Pain point (current)** | No awareness path today — they only know about applications when a FormSG email lands. There's no dashboard. |
| **Opportunity** | Proactive email digest ("3 new applications for [Posting Name] this week") beats waiting for them to log in. |

---

### Stage 2 — Onboarding
**First login; getting oriented**

| | Detail |
|---|---|
| **Touchpoint** | CareerCompass agency dashboard — list of active postings, application counts |
| **User action** | Scans postings list; clicks into the one with the most applications |
| **Thoughts** | "Where are my postings? Can I see who applied? Is this up to date?" |
| **Emotion** | 😟 Slightly anxious — if this doesn't match their mental model of what they had in spreadsheets, they'll revert |
| **Pain point** | Posting list must feel complete and familiar — if one posting is missing, trust is gone |
| **Opportunity** | Show "linked from OTG" label next to each posting. Small signal of continuity — "this is your OTG data, just here too." |

---

### Stage 3 — First Application Review
**⭐ Aha moment — "this is better than email"**

| | Detail |
|---|---|
| **Touchpoint** | Applicant profile page: name, grade, current agency, competency tags from POCDEX, motivation statement |
| **User action** | Reviews first applicant — all structured data visible without chasing HR systems |
| **Thoughts** | "Oh — I can see their competency profile already. I don't have to email their HR." |
| **Emotion** | 😌 Relieved → 😊 Interested — this is the moment the system earns trust |
| **Pain point (current)** | FormSG submissions are freeform. Assessing fit requires going back to HR systems manually or trusting officer self-report. |
| **Opportunity** | Surface 2–3 most relevant data points prominently: current grade, competency tags matching the posting, service tenure. Don't overwhelm — filter to what matters for a development posting decision. |

---

### Stage 4 — Shortlisting
**Reviewing multiple applicants, making a defensible recommendation**

| | Detail |
|---|---|
| **Touchpoint** | Applicant list view with sortable columns; bulk status update action |
| **User action** | Marks 3 applicants as "Shortlisted", 4 as "Not proceeding", 2 as "Hold" |
| **Thoughts** | "I need an audit trail. If I'm questioned about why I didn't shortlist someone, I need to show my reasoning." |
| **Emotion** | 🧐 Careful — this is a defensible decision, not just a preference |
| **Pain point (current)** | Spreadsheet has no audit trail. If HR leadership asks "why was this officer not selected?", the answer is a private email. |
| **Opportunity** | Optional free-text note per status change — not mandatory, but available. Builds the audit trail without adding friction. |

---

### Stage 5 — Communication
**Status changes trigger automatic notifications to applicants**

| | Detail |
|---|---|
| **Touchpoint** | OTEP sends officer-facing emails when status changes ("Your application for [Posting] is under review") |
| **User action** | Posting Manager updates status; doesn't write individual emails |
| **Thoughts** | "Do the officers know their status changed? I don't want a flood of 'what's happening with my application' emails." |
| **Emotion** | 😌 Relieved — no manual follow-up needed |
| **Pain point (current)** | Today they write individual emails or ignore applicants entirely until a decision is made. Applicants chase. |
| **Opportunity** | Status update confirmation screen showing "X applicants have been notified" gives the Posting Manager visible control — they know it happened. |

---

### Stage 6 — Closing the Posting
**Marking filled; system handles the rest**

| | Detail |
|---|---|
| **Touchpoint** | "Mark as filled" action on the posting; system sets closing_date-based auto-close as a fallback |
| **User action** | Clicks "Mark filled" → confirms selected applicant → remaining applicants notified automatically |
| **Thoughts** | "Did everyone get told? I don't want people still expecting a decision." |
| **Emotion** | 😊 Satisfied — clean end state, no awkward individual rejection emails |
| **Pain point (current)** | Manual process: email each rejected applicant individually, or don't. Many don't. Applicants are left wondering. |
| **Opportunity** | Auto-close on `closing_date` as a safety net — even if the Posting Manager forgets to close it manually, the system closes and notifies. |

---

### Stage 7 — Retention / Repeated Use
**Second and third postings; building a habit**

| | Detail |
|---|---|
| **Touchpoint** | OTEP agency dashboard as default starting point for posting season |
| **User action** | Opens dashboard at start of each STIP/Gig cycle to check status across all active postings |
| **Thoughts** | "This is faster than opening my spreadsheet. I can see everything in one place." |
| **Emotion** | 🙂 Settled — system is now the source of truth |
| **Pain point** | If OTG and OTEP ever fall out of sync (a posting exists in OTG but not in OTEP), trust breaks fast |
| **Opportunity** | Daily sync health indicator on the dashboard — small, unobtrusive. "Last synced: today 08:00." Prevents "where's my posting?" tickets. |

---

### Stage 8 — Advocacy
**When they recommend CareerCompass to other HR colleagues**

| | Detail |
|---|---|
| **Touchpoint** | HR community of practice meeting; informal peer conversation |
| **User action** | "We moved to CareerCompass for applications — the applicant profiles are already populated, I don't have to chase records." |
| **Thoughts** | Worth recommending because it made a recurring pain (applicant tracking) clearly better |
| **Emotion** | 😊 Confident — it solves a real problem they've had for a long time |
| **Trigger** | Advocacy happens after Stage 3 (first review with pre-populated profile). That's the moment that converts a cautious user into a recommender. |

---

## Critical Moments Summary

| Moment | Stage | What happens |
|---|---|---|
| ⭐ Aha moment | Stage 3 — First applicant review | Structured POCDEX profile data is visible without manual chase |
| 🔑 Moment of truth | Stage 2 — Onboarding | If the posting list feels incomplete or unfamiliar, they revert to spreadsheets |
| ⚠️ Churn trigger | Stage 4 — Shortlisting | If there's no audit trail mechanism, they'll keep a shadow spreadsheet alongside OTEP |
| ⚠️ Churn trigger | Stage 7 — Retention | OTG/OTEP sync failure breaks trust — even one missing posting sends them back to the old workflow |

---

## Prioritised Improvements

**High impact, directly enables the aha moment:**
1. POCDEX competency data surfaced on applicant profile — this is the single feature that makes stage 3 work
2. Automatic applicant notifications on status change — removes the manual communication burden

**High impact, trust/retention:**
3. OTG sync health indicator on the dashboard (small; prevents the highest-frequency support ticket)
4. Optional free-text note on status change (audit trail without mandatory friction)

**Medium impact, polish:**
5. "Last updated" timestamp on posting list — keeps the Posting Manager confident the data is live
6. Bulk status update (select 10 applicants → mark all as "not proceeding") — reduces repetitive clicking

**Structural prerequisite (blocks everything above):**
- ATS architecture decision: applications must live in OTEP, not in FormSG email inboxes. Without this, stages 3–8 don't exist. Raise with Adrian before R1 scoping starts.

---

## What's Out of Scope Until R4+

- Posting creation and editing (currently in OTG — R4 per BO Senior Level direction 2026-05-12)
- Competency-based applicant filtering ("show me only officers with Foundation-level competency X") — R2
- Cross-agency posting visibility — not scoped

---

## So What

The Posting Manager's aha moment is narrow and specific: seeing structured officer profile data without having to chase HR systems. Everything before that moment (stages 1–2) is setup friction that needs to be minimised. Everything after it (stages 4–8) is either trust-building or efficiency — they're already converted.

The single biggest risk is the ATS decision. If applications stay in FormSG email inboxes in R1, this entire journey doesn't exist. The Posting Manager gets nothing out of R1 and remains an unserved persona until R2 at earliest. That's the decision to make before any R1 scoping for the agency side.
