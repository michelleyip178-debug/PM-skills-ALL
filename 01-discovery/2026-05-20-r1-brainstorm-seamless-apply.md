# Brainstorm: R1 — Seamless Application (Friction Reduction)

**Date:** 2026-05-20
**Product:** CareerCompass (OTEP)
**Focus:** R1 Seamless Application — reduce friction in the apply flow
**Outcome target:** Officers can move from opportunity discovery to submitted application with less effort, confusion, and drop-off
**Method:** Multi-perspective ideation (PM / Designer / Engineer)

---

## The friction we're solving for

In MVP, applying means leaving CareerCompass entirely — redirect to FormSG, jump to Careers@Gov, or for SJRs, nothing at all. R1 promises "application within CareerCompass." The friction points are:

- Context switch (officer leaves the platform, loses their place)
- Re-entering data they've already given CareerCompass
- Not knowing what happens after they submit
- Forgetting opportunities they meant to apply for
- Longer applications (STIP) requiring a single uninterrupted sitting

---

## PM lens — business value and strategic alignment

**P1. Single routing CTA**
One "Apply" button with adaptive label — "Apply via CareerCompass", "View on Careers@Gov" — set from opportunity type at render time. Officer never has to guess where they're going before they click. Sets accurate expectations; reduces mid-flow abandonment when the destination surprises them.

**P2. My Applications dashboard**
A dedicated view showing all submitted applications across STIP/GIG/SJR/C@G/Internal, with status and timestamp. Closes the "I applied, now what?" loop — the most anxiety-producing moment in any application flow. Directly supports the R1 OKR: application status latency ≤ 24 hours.

**P3. Profile-to-form pre-fill mapper**
Automatically maps CareerCompass profile fields to application form fields before the officer sees the form. Officer reviews, edits if needed, and submits. Cuts repeat data-entry for officers who apply frequently — the power users who drive the 20% OKR.

**P4. Saved jobs with deadline nudges**
One-tap bookmark on any opportunity card or detail page. Surface a "Closes in 3 days" badge when a saved opportunity is approaching deadline. Addresses the most common reason officers miss opportunities: intention without follow-through.

**P5. Post-submission confirmation + next prompt**
After submitting, show a clear confirmation (application reference, expected timeline) and suggest one next action (similar opportunity, relevant course). Reduces the post-apply anxiety that generates support tickets and repeat logins just to check status.

---

## Designer lens — UX, usability, and delight

**D1. In-context application drawer**
Application form loads in a side panel anchored to the detail page — officer can still see the opportunity description while filling in the form. No navigation away, no "how do I get back" confusion. This is the single highest-leverage UX move for "application within CareerCompass."

**D2. Progress stepper with save-and-resume**
Multi-step form with a visible step indicator and the ability to save a draft mid-way and return later. Critical for STIP applications, which are substantive. Without this, any officer who can't finish in one sitting abandons — and longer applications are exactly where CareerCompass can add the most value vs. redirect-based MVP.

**D3. One-tap pre-fill confirmation card**
Instead of silently pre-filling the form, show a preview card: "Here's what we'd fill in from your profile." Officer taps "Looks good" or edits inline before the form opens. Addresses the trust gap — officers are more likely to trust pre-fill they reviewed than pre-fill that appeared without explanation.

**D4. Opportunity type indicator on the CTA**
Before the officer clicks Apply, the button label and a small badge signal what happens next: a lock icon for in-app, an external link icon for Careers@Gov. Sets expectations at the point of decision, not mid-flow. Reduces the disorientation of landing somewhere unexpected.

**D5. Smart inline field hints**
As officers fill in form fields, show context-sensitive hints: "This will be shared with your reporting officer" or "This maps to your CareerCompass profile — you can update it there." Reduces hesitation on ambiguous fields. Builds mental model of how CareerCompass and the application are connected.

---

## Engineer lens — technical leverage and scalability

**E1. Form schema registry**
A central config layer that maps each opportunity type (STIP, GIG, SJR, C@G, Internal) to its form schema — required fields, optional fields, field types, validation rules. Powers pre-fill, validation, routing, and the drawer UI from a single source of truth. This is infrastructure, but it's the unlock that lets all other R1 features work across all 5 types without 5 separate implementations.

**E2. Application state machine**
Standardised state model: Draft → Submitted → Under Review → Shortlisted → Decision. With an event log per transition. Enables My Applications dashboard (P2), status tracking OKR, and future notification features — all built on one consistent model rather than a patchwork per opportunity type.

**E3. Webhook normaliser / adapter layer**
A thin translation layer that receives status events from OTG, C@G, and ATS (each in their own format) and normalises them into CareerCompass's unified event model. Engineers add a new source system by writing one adapter — not touching the status UI. Keeps the integration surface clean as more systems are onboarded.

**E4. Idempotent apply endpoint**
Apply API that handles duplicate submissions gracefully — officer double-taps, network retry, back-button re-submit. Returns the same confirmation rather than creating duplicate records. Reduces a significant source of support load and officer confusion ("did it go through?").

**E5. Pre-fill confidence scoring**
Score each profile field by recency and source reliability before pre-filling. Auto-fill only high-confidence fields (e.g. name, agency, grade from POCDEX). Flag low-confidence fields (e.g. self-assessed competencies) for officer review. Reduces correction overhead and the trust erosion that comes from pre-filling stale or wrong data.

---

## Top 5 prioritized ideas

Selected based on: direct alignment with R1 friction-reduction goal, strategic fit with "application within CareerCompass" promise, feasibility given Thomas as sole FE, and strength of the assumption underneath each idea.

---

### #1 — In-context application drawer (D1)

**What it is:** Application form loads as a side panel on the detail page. Officer never navigates away.

**Why it's first:** This is the literal definition of "application within CareerCompass." Without it, R1's promise is only partially true — officers still feel like they left. It's also the UX container that all other ideas (pre-fill, progress stepper, confirmation) live inside.

**Key assumption to validate:** The application forms for STIP and GIG can be rendered within CareerCompass's UI constraints — they're not so complex or long that a drawer is the wrong container. (If they are, a dedicated full-page flow is the fallback.)

---

### #2 — One-tap pre-fill confirmation card (D3)

**What it is:** A "here's what we'll fill in for you" preview before the form opens. Officer confirms or edits.

**Why it's second:** Pre-fill is only valuable if officers trust it. Showing the data before filling it removes the "where did this come from?" anxiety and reduces the correction overhead that turns a time-saver into a time-cost. This is a lower-effort, higher-trust version of smart pre-fill that doesn't require perfect profile completeness to work.

**Key assumption to validate:** Officers will engage with the confirmation card and not dismiss it reflexively. If they click "Looks good" without reading it, the benefit is lost — but so is the harm.

---

### #3 — Application state machine + My Applications dashboard (E2 + P2)

**What it is:** A unified state model for all applications, surfaced as a "My Applications" view with status per submission.

**Why it's third:** The post-submission experience is the most neglected part of any application flow. Officers who can't see their status re-apply, ask HR, or lose confidence in the platform. The state machine is the backend foundation; the dashboard is the officer-facing output. Together they close the loop that the 24-hour latency OKR is measuring.

**Key assumption to validate:** OTG and C@G can provide status events at the granularity needed for a meaningful dashboard (not just "submitted" — at least "under review" and "outcome"). This is Experiment 2 from the R1 Discovery Plan.

---

### #4 — Progress stepper with save-and-resume (D2)

**What it is:** Multi-step form with visible progress and draft save capability.

**Why it's fourth:** STIP applications are substantive — officers won't always finish in one sitting. Without draft save, CareerCompass's in-app apply advantage disappears for the highest-value opportunity type. The stepper also makes long forms feel manageable, which directly reduces abandonment.

**Key assumption to validate:** Officers actually start and don't finish STIP applications in MVP (abandonment evidence from Experiment 4 in the Discovery Plan). If abandonment is low, this is lower priority.

---

### #5 — Form schema registry (E1)

**What it is:** A central config layer mapping each opportunity type to its form schema, validation rules, and field mappings.

**Why it's fifth:** This is infrastructure, not user-facing — but it's the reason ideas 1–4 can work at scale across 5 application types without 5 separate codebases. Without it, each new type is a manual build. With it, adding a new type is config, not code. It belongs in R1 backlog as a foundational story, not an afterthought.

**Key assumption to validate:** All 5 application types have schemas that are stable enough to register — they're not changing mid-R1 build. Confirm with OTG and C@G.

---

## Ideas not prioritized (and why)

| Idea | Reason deprioritised |
|---|---|
| P4 — Saved jobs with deadline nudges | Valuable but notifications infrastructure is out of MVP/R1 scope. Saved jobs (bookmarking) is in R1; push nudges are R2+. |
| P5 — Post-submission confirmation prompt | Good UX, low lift — but it's a detail inside the drawer/flow, not a standalone idea. Build it as part of #1. |
| D4 — Opportunity type indicator on CTA | Small but useful. Build it as part of #1 (the drawer approach makes the CTA label design obvious). |
| D5 — Smart inline field hints | Right idea, but needs the form schema registry (#5) first. Phase 2 of R1 at earliest. |
| E3 — Webhook normaliser | Critical infrastructure but it's part of the state machine story (#3). Not a separate backlog item — it's a sub-task. |
| E4 — Idempotent apply endpoint | Engineering best practice — should be a standard AC on the apply endpoint story, not a separate idea. |
| E5 — Pre-fill confidence scoring | Technically elegant but adds complexity before we've validated that pre-fill is trusted at all. Start with the confirmation card (#2); add confidence scoring in R2 if needed. |

---

## Suggested next steps

- **Stress-test idea #1:** Confirm with Amber whether the drawer UX works for STIP form length. If forms are >5 fields or multi-section, consider a dedicated in-app page instead of a drawer.
- **Spike on idea #3:** Pow Hwee to confirm OTG/C@G status event granularity (this is Experiment 2 in the Discovery Plan — run in Sprint 4–5).
- **Validate abandonment before committing to idea #4:** Check MVP analytics (Experiment 4). If STIP abandonment is <20%, deprioritise save-and-resume.
- **Write user stories** for ideas 1–3 as the R1 backlog foundation.

---

*Source: R1 Discovery Plan (2026-05-20) + sprint-status.md + CareerCompass OKR Review deck*
