# Discovery Plan: Workable ATS Integration Pivot

**Date:** 2026-05-19
**Product stage:** Existing (CareerCompass / OTEP R1)
**Decision this informs:** What to scope into R1 vs defer, given ATS partnership is unconfirmed until June
**Discovery question:** How do we build a resilient application experience for officers across all opportunity types — regardless of whether the Workable ATS integration materialises?

---

## Context

The R1 scope has pivoted to mandate deep Workable ATS integration. The revised scope includes:

- In-app applications across STIP, GIG, SJR, C@G, and Internal job types
- ATS-driven job creation, posting, and end-to-end status tracking
- External Facing Profile (read-only officer profile during application)
- Saved Jobs

**Critical constraint:** The ATS partnership decision cannot happen before June, with no guarantee it will proceed. If it doesn't, the team needs to scope in OTEP-native opportunity creation, application submission, and tracking — a significantly larger build. Additionally, applicant matching is explicitly undetermined, and there is no structured, unified application format across all five opportunity types.

---

## Two Worlds Framework

Before ideating, it's useful to name the two scenarios this discovery must account for:

**World A — ATS confirmed:** Workable handles job creation, application routing, and status tracking. CareerCompass is the officer-facing front end. Core challenge: integration depth and data model mapping.

**World B — ATS not confirmed:** OTEP owns the full stack — opportunity creation, application submission, and status management. Core challenge: scope is 2–3x larger; delivery risk is high.

Two features are **decoupled** from this choice and can ship in either world:
- External Facing Profile (display-only, no ATS dependency)
- Saved Jobs (a bookmark mechanism, backend-agnostic)

Everything else — the application flow, status tracking, and matching — is **ATS-dependent** in World A and OTEP-native in World B.

---

## Ideas Explored (Brainstorm)

Generated from PM, Designer, and Engineer perspectives.

**PM lens**
1. Dual-track architecture — build for both worlds simultaneously using a feature flag. ATS integration is an enhancement on top of a working OTEP-native baseline.
2. ATS-lite pilot — pilot Workable integration with one job type (GIGs, lowest friction) before committing to all five.
3. FormSG bridge — build a thin webhook layer that keeps FormSG as the submission backend but surfaces the experience inside CareerCompass. No ATS dependency; no duplicate data collection.
4. Competency-first matching gate — before building matching UI, formally audit whether competency data quality is sufficient to produce meaningful results.

**Designer lens**
5. Profile-first launch — ship External Facing Profile as the first deliverable regardless of ATS outcome. It's standalone value, decoupled from application flow.
6. Unified "My Applications" view — design a status tracking page that is backend-agnostic (works with FormSG, Workable, or OTEP-native).
7. Saved Jobs as the quick win — decouple entirely from application flow and ship early.

**Engineer lens**
8. Unified opportunity schema — define a canonical data model across all five job types before building any UI. This is a prerequisite for everything, regardless of ATS outcome.
9. Generic status webhook — build a status update mechanism that any backend can push into. ATS and OTEP-native become interchangeable at the status layer.
10. Phased application form component — a shared UI form that routes to different backends (FormSG, Workable API, or OTEP-native) based on job type and ATS availability.

---

## Selected Ideas to Carry Forward

Five ideas shortlisted for assumption mapping, based on their relevance to the phasing decision:

| # | Idea | Rationale |
|---|------|-----------|
| 1 | Dual-track architecture | De-risks the ATS dependency at the system level |
| 2 | External Facing Profile (profile-first) | Decoupled from ATS; high value; shippable now |
| 3 | Unified opportunity schema | Prerequisite for everything; must resolve first |
| 4 | FormSG bridge / phased application form | Works in both worlds; reduces rework |
| 5 | Saved Jobs as quick win | Decoupled; adds officer value regardless of ATS outcome |

---

## Critical Assumptions

All assumptions across the pivot scope, mapped by risk category.

| # | Assumption | Category | Impact | Uncertainty | Priority |
|---|-----------|----------|--------|-------------|----------|
| A1 | Workable ATS partnership is confirmed by June | Viability | High | High | 🔴 Leap of faith |
| A2 | Workable API supports all 5 job types (STIP, GIG, SJR, C@G, Internal) | Feasibility | High | High | 🔴 Leap of faith |
| A3 | Government data sovereignty requirements are compatible with Workable | Viability | High | High | 🔴 Leap of faith |
| B1 | A unified application format can be agreed across all 5 opportunity types | Feasibility | High | High | 🔴 Leap of faith |
| B2 | Business owners (Jacky, Xian Zhang) will agree to migrate off FormSG workflows | Viability | High | High | 🔴 Leap of faith |
| E1 | Competency data across all job types is structured and queryable enough for matching | Feasibility | High | High | 🔴 Leap of faith |
| A4 | Integration can be built within 2–3 sprints post-ATS confirmation | Feasibility | High | Medium | 🟠 High priority |
| A5 | Workable data model maps cleanly to OTEP's opportunity schema | Feasibility | High | Medium | 🟠 High priority |
| B3 | Officers prefer in-app application over FormSG redirect | Value | High | Medium | 🟠 High priority |
| C1 | Officer profile data (from OTG) is complete enough to be useful to hiring managers | Value | High | Medium | 🟠 High priority |
| D1 | Officers browse without immediate intent to apply (validating Saved Jobs need) | Value | Medium | Medium | 🟡 Medium priority |
| C2 | Hiring managers will actively use External Facing Profiles during screening | Value | Medium | High | 🟡 Medium priority |
| E2 | A common competency framework exists across all 5 job types | Feasibility | Medium | High | 🟡 Medium priority |
| B4 | Application data in OTEP won't duplicate what agencies already collect via FormSG | Viability | Medium | Medium | 🟡 Medium priority |
| C3 | Officers will keep their profiles updated over time | Usability | Low | Medium | 🟢 Lower priority |
| D2 | Officers return to the platform to complete saved applications | Value | Low | Medium | 🟢 Lower priority |
| E3 | Matching algorithm produces trustworthy results with current data quality | Value | High | Very High | ⛔ Defer — too early |

---

## Validation Experiments

Focused on the six leap-of-faith assumptions. These are what to run before committing to full scope.

---

### Experiment 1 — ATS Partnership Viability Probe (A1, A2, A3)

**Tests assumptions:** A1, A2, A3 (three ATS assumptions in one structured discovery call)

**Method:** Structured vendor discovery session with Workable (or their Singapore reseller) + parallel consultation with PSD IT security on data residency.

**What to ask Workable:**
- Can they share sandbox API access for evaluation?
- Does the API support government-defined job types (not just commercial hiring pipelines)?
- Where is data stored? Can they guarantee Singapore residency?
- What is the procurement timeline for a government client?

**What to ask PSD IT/legal:**
- Is Workable's data handling policy compatible with government classification requirements?
- What sign-off process is needed before integrating a commercial ATS?

**Define go/no-go criteria BEFORE the call** so the outcome is a decision, not a conversation.

Go criteria:
- API supports ≥4 of 5 job types without custom workarounds
- Data residency is achievable or has a clear path
- Procurement can be completed within 6 weeks of June confirmation

**Effort:** 1 vendor call + 1 internal security consult. Low effort, very high signal.

**Owner:** Michelle + Pow Hwee (API assessment) + PSD legal/IT (data residency)

**Timeline:** Before June. Ideally run in May so there's time to act on findings.

---

### Experiment 2 — Application Schema Workshop (B1, B4)

**Tests assumptions:** B1 (unified format exists), B4 (no duplicate data collection)

**Method:** Workshop with Jacky, Xian Zhang, Pow Hwee, and the Ops team. Map required application fields per job type side-by-side. Find the intersection. Name the exceptions explicitly.

**Workshop structure (2 hours):**
1. Each job type owner lists their mandatory fields (30 min)
2. Group maps overlap and identifies unique fields per type (45 min)
3. Decide: standardise or handle per-type? (30 min)
4. Confirm: does any field duplicate what FormSG already collects? (15 min)

**Success criteria:**
- A shared schema covering ≥80% of fields across all five types
- Documented list of per-type exceptions with agreed handling
- Explicit answer on FormSG duplication risk

**Output:** Canonical application schema v1. This feeds directly into the PRD and Pow Hwee's grooming.

**Effort:** 1 x 2-hour workshop + prep time to pull field lists from existing FormSGs.

**Owner:** Michelle leads; Pow Hwee facilitates field mapping; Jacky + Xian Zhang as domain experts.

**Timeline:** Run this regardless of ATS outcome — it unblocks both World A and World B.

---

### Experiment 3 — Business Owner FormSG Migration Conversation (B2)

**Tests assumption:** B2 (Jacky and Xian Zhang will agree to migrate off FormSG)

**Method:** One-on-one conversations with Jacky and Xian Zhang separately. Don't pitch — probe.

**Key question to ask:** "If we built the application experience entirely inside CareerCompass, what would have to be true for you to be comfortable moving off FormSG?"

Listen for:
- Data ownership concerns
- Audit trail requirements
- Workflow dependencies outside OTEP (downstream systems that consume FormSG data)
- Approval process concerns

**Success criteria:**
- Explicit endorsement, or documented conditions for buy-in that the team can design against
- If resistance: understand whether it's a hard blocker or a solvable concern

**Effort:** 2 x 30-minute conversations.

**Owner:** Michelle (this is a stakeholder influence exercise, not a technical one).

**Timeline:** This week or next. Don't wait for ATS confirmation.

---

### Experiment 4 — Competency Data Audit (E1, E2)

**Tests assumptions:** E1 (data is structured enough for matching), E2 (common framework exists)

**Method:** Pow Hwee pulls a sample of OTG competency data across all five job types. Assess completeness, consistency, and queryability.

**What to evaluate:**
- What % of opportunities have competency tags?
- Are the tags using a consistent taxonomy across job types?
- Is the data structured enough to run a match query against an officer's profile?
- Are competency fields officer-inputted or HR-inputted? (affects reliability)

**Success criteria:**
- >70% of opportunities have structured competency tags
- Tags are consistent enough to run matching logic (i.e., same taxonomy, not free-text)
- If criteria not met: matching is explicitly deferred from R1 with documented rationale

**Effort:** Pow Hwee runs this as a 1-sprint spike. Low opportunity cost; very high decisioning value.

**Owner:** Pow Hwee (data pull); Michelle + Pow Hwee (interpret findings).

**Timeline:** Can run in parallel with Experiments 1–3.

---

### Experiment 5 — External Facing Profile Prototype Test (C1, C2)

**Tests assumptions:** C1 (profile data is useful to hiring managers), C2 (they'll actually use it)

**Method:** Amber builds a low-fidelity prototype of the External Facing Profile. Show it to 5 hiring managers from different agencies. Ask: "If you saw this during screening, would it change how you shortlist?"

**What to observe:**
- What information do they actually focus on?
- What's missing that they currently look for?
- Would they trust the data enough to act on it?

**Success criteria:**
- ≥4 of 5 say they'd use it to meaningfully inform a shortlisting decision
- Qualitative signal on what data fields matter most

**Effort:** Amber: 1–2 days on prototype. Michelle: recruit 5 hiring managers + facilitate sessions. ~1 week total.

**Owner:** Amber (prototype); Michelle (research sessions).

**Timeline:** Can start immediately — no dependency on ATS decision.

---

## Discovery Timeline

| Week | Activity | Owner | Unblocks |
|------|----------|-------|----------|
| Week 1 (now) | Experiment 2: Application schema workshop | Michelle, Jacky, Xian Zhang, Pow Hwee | Everything — this is the prerequisite |
| Week 1–2 | Experiment 3: Business owner FormSG conversation | Michelle | B2 assumption resolved |
| Week 1–2 | Experiment 4: Competency data audit (sprint spike) | Pow Hwee | Matching scope decision |
| Week 2–3 | Experiment 5: External Facing Profile prototype test | Amber, Michelle | C1, C2 resolved |
| Before June | Experiment 1: Workable vendor call + data residency check | Michelle, Pow Hwee, PSD IT | ATS go/no-go |
| June | ATS partnership decision | Leadership | World A vs World B confirmed |
| Post-June | R1 scope finalised based on findings | Michelle | Sprint planning |

---

## Decision Framework

Use these findings to make the phasing call.

**If ATS is confirmed AND application schema workshop succeeds:**
→ Proceed with World A. Prioritise: in-app applications (FormSG bridge first, then Workable migration), External Facing Profile, Saved Jobs. Defer matching pending data audit.

**If ATS is confirmed BUT application schema workshop fails (no consensus):**
→ Pilot in-app applications with GIGs only (lowest complexity job type). Remaining types stay on FormSG redirect. Revisit at R2.

**If ATS is NOT confirmed:**
→ Trigger World B scoping. External Facing Profile and Saved Jobs ship as planned. In-app applications use FormSG bridge. Opportunity creation and OTEP-native tracking becomes a new epic for R1.5 or R2. Matching explicitly deferred.

**Matching (independent of ATS):**
→ If competency data audit passes: begin matching discovery in parallel as a future release. If it fails: formally document deferral with rationale and remove from R1 roadmap discussions.

---

## Open Questions (to resolve via experiments)

1. Can the Workable API be evaluated in a government-compliant sandbox before June? Who initiates the vendor conversation?
2. What downstream systems consume FormSG submission data today? (Ops team needs to answer this before migration can be considered.)
3. Is there a shared competency framework that spans STIP, GIG, SJR, C@G, and Internal — or does each type use its own taxonomy?
4. For SJRs: the previous scope had no apply action in MVP. Does the ATS pivot change this assumption?
5. Who owns hiring manager recruitment for Experiment 5? Does Michelle have access to them, or does this go through Jacky?

---

## Scope Recommendation (PM position)

**Don't treat this as one scope decision. It's two:**

**Decision 1 (now, regardless of ATS):** Ship External Facing Profile and Saved Jobs in R1. Both are decoupled from ATS and add immediate officer value. No reason to wait.

**Decision 2 (post-June, based on experiments):** Commit to either World A or World B for the application flow. Run Experiments 1–4 before June so the team arrives at that decision with evidence, not hope.

Trying to hold all of the new scope in R1 without validating the ATS assumption first is the biggest risk here. The experiments above can be run in 3–4 weeks and will give enough signal to make a confident call before the June gate.
