# CareerCompass User Personas

**Created:** 2026-05-20
**Scope:** Full product — Discovery through Apply (OTG + Careers@Gov pipelines)
**Segments:** 2 Officer personas, 1 HR/Agency persona
**Data sources:** CareerCompass OKR deck (problem spaces, survey statistics), R1 candidate list, scoping-gaps-tracker, decisions-log

> **Purpose:** Anchor R1 discovery and the Adrian conversation. These personas define *who we're solving for*, which failure modes matter most, and where the Seamless Application investment has the clearest ROI.

---

## Persona 1 — The Intentional Mover

**Role:** Senior Executive / Senior Officer
**Career stage:** 5–10 years in service, approaching mid-career review
**Org type:** Ministry or statutory board

### Primary Job-to-be-Done

Find a stretch assignment that closes a specific competency gap — before their next performance review or promotion board. The job is *targeted and time-pressured*: they know what they want, they have a window, and they need it done cleanly.

Frequency: once or twice a year, triggered by performance conversation or a nudge from their supervisor.

### Top 3 Pain Points

1. **Multi-platform search friction.** They check OTG, then Careers@Gov, sometimes both in the same week. The two platforms show different opportunities with different formats. There's no "one place" that's complete — so they either accept an incomplete view or do the work twice.

2. **Apply flow abandonment.** When they find the right opportunity, the FormSG form re-asks information that's already in their HR record (grade, posting history, supervisor). The duplication signals effort, and for a mid-career officer already balancing delivery, it becomes a reason to defer.

3. **Post-application silence.** After submitting, they have no visibility on whether the form reached the right person, where they are in the process, or whether the opportunity is still open. They follow up by email, which is uncomfortable and slow.

### Top 3 Desired Gains

1. A single listing that combines OTG and Careers@Gov opportunities with consistent fields — type, agency, duration, competencies developed.
2. An application form that pre-populates from their profile so they only fill in what's genuinely new (motivation statement, availability).
3. A status tracker: submitted → under review → outcome. Even a "no decision yet" state is better than silence.

### One Unexpected Insight

They've already decided to apply before they open the platform. The discovery step happened via word-of-mouth (a colleague mentioned it, their supervisor flagged it in a 1:1). By the time they visit CareerCompass, they're validating a decision, not making one. This means the *apply flow* is where we win or lose them — not the listing.

**Product implication:** Pre-fill and status tracking (R1 D1, D3) have higher ROI for this persona than any discovery feature. Improving the listing for them is near-zero marginal value; removing apply friction is high.

### Product Fit Assessment

**Strong fit for MVP:** Listing page (unified view), type filter, basic search.
**Unmet need in MVP:** Pre-fill (blocked by open item #10, FormSG pre-fill), status tracking (R1 D3). Until these land, this persona will apply once, experience friction, and not return — which maps directly to the 9% re-login rate.

---

## Persona 2 — The Passive Watcher

**Role:** Officer / Associate (2–5 years in service)
**Career stage:** Early career, still mapping their options; not yet under pressure to move
**Org type:** Any

### Primary Job-to-be-Done

Stay aware of what's out there without it feeling like a second job. They're not searching — they're *open*. If something interesting crosses their path at low cost, they'll consider it. If it requires effort to find, they won't.

Frequency: sporadic; attention spikes around annual review season or when a colleague mentions an opportunity.

### Top 3 Pain Points

1. **No ambient awareness mechanism.** There's no digest, no alert, no "new opportunities matching your profile" touchpoint. If they don't actively visit the platform, they miss everything. Given the 47.4% satisfaction rate on visibility, this is the majority experience.

2. **No memory across sessions.** They browse, see something interesting, close the tab, lose it. There's no save, no history, no way to pick up where they left off. The 9% re-login rate reflects this — one bad session and they don't come back.

3. **Opportunity relevance is unclear.** Listings don't connect to their actual competency profile. They can't quickly tell if they're eligible, overqualified, or a good fit without reading the full description.

### Top 3 Desired Gains

1. Saved jobs / shortlist — the ability to bookmark an opportunity and return to it later.
2. Some signal of fit: "This opportunity develops competencies you're working on" without requiring a full scoring algorithm.
3. Low-effort re-entry: when they come back, their filters and browsing context are preserved.

### One Unexpected Insight

This persona isn't disengaged — they're *deferring*. The "not ready to apply yet" mental state is different from "not interested." They want a holding space for opportunities they're considering. Without Saved Jobs and filter persistence, CareerCompass is structurally unable to serve deferred intent. Every session starts from zero.

**Product implication:** Saved Jobs (R1 D2) is this persona's activation feature, not a nice-to-have. Filter persistence (Deferred to R1 in decisions-log, item #13) compounds the same problem. These two items together are what converts a one-time visitor into a returning user — which is what the 9% → higher re-login target requires.

### Product Fit Assessment

**Partial fit in MVP:** Listing and search give them a starting point.
**Critical gap in MVP:** No saved jobs, no filter persistence, no notification mechanism. MVP delivers a single session; it doesn't build a habit. This persona is the primary target for the re-login metric improvement in R1.

---

## Persona 3 — The Posting Manager

**Role:** HR Executive / HR Officer at Ministry or Statutory Board
**Career stage:** Mid-career, owns the administration of development postings for their agency
**Org type:** Ministry HR division or HR team at a statutory board

### Primary Job-to-be-Done

Fill a development posting with a qualified officer — quickly enough to meet the programme cycle, with enough information about applicants to make a defensible selection recommendation.

Frequency: Recurring, tied to programme cycles (STIPs, Gigs, SJRs). Typically manages 5–20 active postings at a time.

### Top 3 Pain Points

1. **Applicant tracking is entirely manual.** Currently receives FormSG submissions by email, tracks shortlist in a spreadsheet, and communicates back to applicants ad hoc. There's no shared view, no status history, no audit trail.

2. **Applicant profile data is thin.** FormSG submissions contain whatever the officer typed — no structured competency data, no grade history, no service record. Assessing fit requires either trusting the officer's self-report or going back to HR systems manually.

3. **Closing out postings requires manual intervention.** When a posting is filled or expired, there's no automated close. Officers continue submitting after the deadline. Telling late applicants "this is closed" is an additional workload.

### Top 3 Desired Gains

1. A single view of all applicants per posting — submission date, officer name, current grade, competency profile if available.
2. Ability to update posting status (active → under review → filled → closed) with automated communication to applicants.
3. Applicant profile data that draws from officer records, so assessment doesn't depend entirely on the officer's self-description.

### One Unexpected Insight

Their bottleneck is *applicant quality*, not volume. They'd take 3 well-matched applicants over 20 unfiltered submissions every time. This means competency matching — even a simple filter of "this officer has the required competency at foundation level" — has immediate operational value for them, not just for officers. The feature they care about most is one that hasn't been scoped yet: an applicant filter by competency profile.

**Product implication:** The ATS question in R1 (conflict C1 in the candidate list — FormSG-vs-OTEP-native application) is really a question about *who owns the application record*. This persona's participation in R1 depends on OTEP owning that record. If applications stay in FormSG email inboxes, the Posting Manager gets nothing out of R1. Resolving the ATS identity question is pre-req to designing for this persona at all.

### Product Fit Assessment

**Weak fit in MVP:** MVP is entirely officer-facing. Posting Managers interact only through OTG (on the supply side) and email (receiving FormSG submissions). OTEP doesn't serve them yet.
**R1 fit depends on ATS decision:** If R1 includes in-app application tracking, this persona's core job becomes solvable. If R1 only addresses officer-facing apply flow, this persona remains unserved until R2 at earliest.

---

## Cross-Persona Summary

| | Persona 1: Intentional Mover | Persona 2: Passive Watcher | Persona 3: Posting Manager |
|---|---|---|---|
| **Core job** | Apply to the right opportunity fast | Stay aware at low cost | Fill postings with qualified officers |
| **MVP coverage** | Partial (listing ✓, apply friction ✗) | Partial (listing ✓, habit-building ✗) | None |
| **R1 priority features** | Pre-fill (D1), Status tracking (D3) | Saved Jobs (D2), Filter persistence | ATS decision — unlocks everything |
| **Key metric** | Apply completion rate | Re-login rate, saves per session | Time to fill, applicant quality |
| **R1 risk** | Drops out at apply step | One session, doesn't return | Not served; builds workaround |

---

## So What

The three personas map to three different failure modes:

**Persona 1** fails at the apply step. The listing is good enough; the form loses them. Pre-fill is the highest-leverage R1 investment for this persona.

**Persona 2** fails between sessions. MVP can't build a habit — there's no mechanism to return. Saved Jobs is the activation feature; without it, re-login improvement is structurally blocked.

**Persona 3** is invisible in MVP. Whether they become CareerCompass users at all depends entirely on the ATS architecture decision. Resolve this with Adrian before any R1 scoping for the agency side.

The 9% OTG re-login rate is Persona 2's symptom. The apply drop-off is Persona 1's symptom. Neither is fixable in MVP. R1 is the release where CareerCompass stops being a listing page and starts being a tool people return to.
