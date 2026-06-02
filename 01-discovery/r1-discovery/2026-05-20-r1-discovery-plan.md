# Discovery Plan: R1 — Seamless Application

**Date:** 2026-05-20  
**Product Stage:** Existing product (continuous discovery — R1 builds on MVP Oct'26)  
**Product:** CareerCompass (OTEP) — internal talent platform, Singapore Public Service  
**Owner:** Michelle Yip  
**Discovery Question:** What does "Seamless Application" actually need to be true — technically, behaviourally, and operationally — for R1 to move officers from discovery to action at scale?

---

## Context

### R1 Revised Scope (Q1'27 target — ~3 months post-MVP)

| Feature | Status |
|---|---|
| Pre-filled applications — STIP, GIG, C@G, Internal Jobs | ✅ In |
| Pre-filled applications — SJR | ⚠️ Unconfirmed — SJR excluded from MVP entirely (no apply flow, not ingested; D 2026-05-21). Re-introducing SJR apply in R1 is a major new integration track. Needs explicit confirmation (see Scope Concern #3) |
| Post jobs on ATS | ✅ In |
| Status tracking: end-to-end with ATS integration | ✅ In |
| Application within CareerCompass (no redirects) | ✅ In |
| Saved Jobs | ✅ In |
| External-facing read-only Profile page | ✅ In |
| Smart Assistant (auto-populate strengths/experience) | ❌ Deprioritised |
| Gap Radar (insights for specific target roles) | ❌ Deprioritised |
| Intelligence Dashboard (usage pattern tracking) | ❌ Deprioritised |

### R1 OKR Targets
- 20% of onboarded officers have applied for at least one opportunity through CareerCompass within 6 months of launch
- Application status update latency ≤ 24 hours of hiring manager action
- Officer satisfaction ≥ 3.5/5
- 50% of required OTG features built on CareerCompass

### What MVP tells us (as of Sprint 3, updated 2026-06-02)
- Application flow in MVP = FormSG redirect (Internal Jobs/STIP/GIG), C@G deep-link. SJR = not ingested at all (D 2026-05-21, supersedes "visible but no apply")
- `formsg_url` field confirmed ✅ (2026-05-21, open-items #2) — unblocked OTEP-319 (was US-18)
- No WOG AD UAT environment yet, but auth FE is de-risked: login/logout build now against Keycloak, WOG AD swaps in later (D 2026-06-02, OTEP-305)
- Scope instability from senior stakeholders (logged risk) — CareerCompass branding + MVP-6 pilot confirmed 2026-06-02
- Thomas is sole FE developer — bandwidth is a constraint into R1 planning
- No abandonment data yet — MVP analytics baseline not established

---

## Ideas Explored (Brainstorm)

Ten ideas generated across PM, Designer, and Engineer perspectives:

**PM lens**
1. **Unified application inbox** — all submitted applications (across STIP/GIG/SJR/C@G/Internal) visible in one "My Applications" view with live status. MVP routes out; R1 pulls the officer back in.
2. **Smart pre-fill service** — profile fields mapped to form fields. Officer confirms/edits before submitting. Eliminates copy-paste overhead.
3. **Application type router with single UX** — officer sees one "Apply" CTA; system routes based on opportunity type. Complexity is invisible to the officer.
4. **Saved opportunities queue** — bookmark any opportunity; resurface with deadline proximity nudges. Addresses "I'll do it later" drop-off.
5. **Hiring manager profile handoff** — submitted application includes a read-only CareerCompass profile link. Removes the "who is this person" gap in OTG today.

**Designer lens**

6. **In-app application drawer** — form loads in a side panel without navigating away from the detail page. Preserves the officer's context.
7. **Application progress stepper with save-draft** — multi-step form with pause-and-resume. Critical for longer STIP applications.
8. **Status timeline card** — post-submission view showing Submitted → Under Review → Decision. Visual, not just a label.
9. **Deadline proximity indicator** — "Closes in 3 days" badge that escalates visually on saved jobs. Reduces missed deadlines.

**Engineer lens**

10. **ATS webhook integration layer** — standardised event receiver that translates status updates from OTG, C@G, and any future ATS into CareerCompass's application state machine. Foundational for everything above.

---

## Selected Ideas for Validation

Five ideas carried forward — chosen because they are directly load-bearing for the R1 OKR and each has at least one non-obvious assumption underneath it.

| # | Idea | Rationale |
|---|---|---|
| 1 | Unified application inbox | Directly tied to the 20% applied OKR — won't hit the number if officers can't see and trust their applications |
| 2 | Smart pre-fill service | Core UVP of R1; if profile data isn't good enough, this is an illusion |
| 3 | Application type router | Usability backbone — officers applying across the in-scope types (STIP, GIG, C@G, Internal; SJR pending Concern #3) need a consistent mental model |
| 7 | Save draft + progress stepper | Abandonment is unvalidated but plausible — needs evidence before building |
| 10 | ATS webhook layer | Technical foundation without which ideas 1, 3, 8 cannot work |

---

## Critical Assumptions

### Full assumption register

| # | Assumption | Category | Impact | Uncertainty | Priority |
|---|---|---|---|---|---|
| A1 | Officers will choose to apply through CareerCompass rather than navigating directly to OTG/C@G | Value | High | High | 🔴 Leap of faith |
| A2 | Officer profile data will be accurate and complete enough at R1 launch to pre-fill meaningfully | Value | High | High | 🔴 Leap of faith |
| A9 | OTG exposes webhooks or polling APIs for application status events at the right granularity | Feasibility | High | High | 🔴 Leap of faith |
| A14 | OTG, C@G, and ATS vendors will agree to API/webhook access agreements in time for R1 | Viability | High | High | 🔴 Leap of faith |
| A5 | Officers abandon applications mid-way at meaningful rates (i.e. draft save is worth the build) | Value | High | Medium | 🟡 Test quickly |
| A11 | CareerCompass profile fields map cleanly enough to STIP/GIG/SJR/C@G/Internal form schemas | Feasibility | High | Medium | 🟡 Test quickly |
| A12 | Building in-app application flows for 5 opportunity types is achievable in a 3-month R1 window | Feasibility | High | Medium | 🟡 Test quickly |
| A3 | Pre-fill reduces officer time/effort net — doesn't create correction overhead that costs more time | Value | Medium | Medium | 🟠 Monitor |
| A4 | Officers want cross-system application status in one place (not in OTG, not in C@G separately) | Value | Medium | Medium | 🟠 Monitor |
| A6 | Hiding routing complexity behind a single "Apply" CTA reduces confusion rather than creating it | Usability | Medium | Medium | 🟠 Monitor |
| A7 | Officers will trust pre-filled data enough to submit without excessive re-verification | Usability | Medium | Low | 🟢 Lower priority |
| A13 | Storing draft application data will clear government data classification and security review | Feasibility | Medium | Medium | 🟠 Monitor |
| A15 | Hiring managers will use the CareerCompass profile handoff during shortlisting | Value | Low | High | 🟢 Lower priority |

### The four leap-of-faith assumptions

**A1 — Channel choice.** The entire R1 premise rests on officers choosing CareerCompass as the application channel, not out of habit going directly to OTG. If they don't, the 20% OKR is unreachable regardless of how good the in-app experience is. Think of it like building a new checkout page while customers are still walking to a different register — the UX doesn't matter if they don't choose your lane.

**A2 — Profile data quality.** Pre-fill that's wrong is worse than no pre-fill. Officers who encounter stale or inaccurate data will lose trust in CareerCompass faster than they gain it. MVP launches without profile enrichment at scale; we don't know what completeness looks like in the wild.

**A9 — OTG API/webhook.** Without confirmed API access to OTG's status events, there's no status tracking — which undercuts both the 24-hour latency OKR and the "apply-and-know-what-happens" promise. This is a gate, not a risk.

**A14 — Vendor agreements.** External dependencies on three systems (OTG, C@G, ATS) need access agreements before Sprint work begins in R1. A verbal "yes" is not enough — we need the API contract. The earlier this is confirmed, the earlier R1 de-risks.

---

## Validation Experiments

### Experiment 1 — Test A1: Will officers choose CareerCompass to apply?

**Hypothesis:** At least 25% of officers who view an opportunity detail page in MVP will click the Apply CTA (vs. independently navigating to OTG/C@G).  
**Method:** Instrument clickthrough-to-apply rate from the detail page from MVP launch. If the Apply CTA in MVP is a redirect stub, use it as a fake-door signal — track intent regardless of completion. Layer in 3–5 intercept interviews with UAT officers: "What would you normally do when you want to apply for an opportunity?"  
**Success criteria:** ≥25% detail page → apply CTA conversion in first 4 weeks post-MVP. Interview signal: officers say they'd prefer applying without leaving the platform.  
**Effort:** Low — analytics hooks already required for OKR baseline. Intercept interviews = half a day.  
**Timeline:** MVP launch (Oct'26) + 4 weeks → results available Nov'26, before R1 design lockdown.  
**Decision rule:** CTR < 10% → investigate before committing to R1 application build. Find out *why* (habit? trust? friction?). CTR ≥ 25% → proceed with in-app application as R1 centrepiece.

---

### Experiment 2 — Test A9 + A14: OTG webhook and API access

**Hypothesis:** OTG's system can provide application status events within 24 hours via webhook or polling API; C@G can do the same.  
**Method:** Technical spike — Pow Hwee to investigate OTG's event/webhook architecture and confirm API access terms. Parallel: confirm C@G API access and field granularity. Output: documented API contract or confirmed endpoint from both systems. If neither exposes event-level status, document the polling alternative and its latency implications.  
**Success criteria:** Written API contract or confirmed webhook endpoint from OTG + C@G by Sprint 6 (end of July'26). Vendor agreement in principle (email confirmation) from both by the same date.  
**Effort:** Medium — 1 sprint spike for Pow Hwee + one stakeholder call with OTG/C@G integration contacts.  
**Timeline:** Sprint 5–6 (Jul'26) — must resolve before R1 design begins.  
**Decision rule:** No webhooks confirmed by Sprint 6 → descope live status tracking to R2; replace with "submitted" confirmation + email notification only. Surface to Adrian as a scope adjustment, not a failure.

---

### Experiment 3 — Test A2: Profile data quality at R1 launch

**Hypothesis:** ≥70% of officer profiles at R1 launch will have sufficient data (name, role, agency, competency tags) to pre-fill at least 50% of application form fields without requiring correction.  
**Method:** During MVP UAT (Sep–Oct'26), audit profile completion across the **MVP-6 pilot cohort (PSD, ESG, MDDI, URA, MCCY, CAAS — ~5,400 officers)**. Sample across all 6 agencies, not just one — profile completeness likely varies by agency HR practice, and that variance is itself a finding. Map CareerCompass profile fields against STIP and GIG form schemas (the highest-volume application types). Run one usability session: give 5 officers a pre-filled application draft and observe correction behaviour.  
**Success criteria:** Field coverage ≥ 70% average across sampled profiles, **and no single pilot agency below 50%** (a low-coverage agency drags down that agency's pilot experience). Correction rate < 20% in usability session (officers accept, not rewrite, pre-filled content).  
**Effort:** Medium — requires actual pilot profile data and OTG form schemas. One usability session.  
**Timeline:** UAT (Sep–Oct'26).  
**Decision rule:** Coverage < 50% or correction rate > 40% → descope smart pre-fill; prioritise profile enrichment as R1's primary feature instead of form pre-fill. Reframe R1 value prop from "apply faster" to "build your profile, then apply."

---

### Experiment 4 — Test A5: Is abandonment real?

**Hypothesis:** Officers who click Apply in MVP but redirect to OTG/FormSG complete the application at rates below 60% (i.e. abandonment is real and draft save is worth building).  
**Method:** Instrument the clickthrough-to-webhook-receipt funnel in MVP. Click event fired on Apply CTA; FormSG submission webhook is already in MVP scope (US-18). Compare clicks vs. confirmed submissions. Gap = abandonment proxy.  
**Success criteria:** If abandonment > 40% → draft save validated as R1 priority. If abandonment < 20% → descope draft save; re-evaluate for R2.  
**Effort:** Low — hooks into MVP instrumentation already planned.  
**Timeline:** Sprint 5 onward (Jul–Aug'26), with data available before R1 backlog grooming.  
**Decision rule:** Data informs R1 backlog prioritisation directly. Low abandonment = simplify the application flow; don't add draft complexity.

---

### Experiment 5 — Test A11: Profile-to-form field mapping

**Hypothesis:** CareerCompass profile fields cover ≥60% of required fields across STIP, GIG, C@G, and Internal Job application schemas.  
**Method:** Engineering spike — Pow Hwee maps current data model fields to each form schema. **SJR is excluded** — it has no apply flow and isn't ingested (D 2026-05-21); only re-add it here if Scope Concern #3 resolves SJR back into R1. Output: a field coverage matrix with gap count and gap severity (nice-to-have vs. required field).  
**Success criteria:** Coverage matrix completed; gap count defined; recommendation made on whether to add missing fields to the R1 profile model or flag as out-of-scope.  
**Effort:** Low-medium — 1 sprint sub-task for Pow Hwee, combined with ATS spike (Experiment 2).  
**Timeline:** Sprint 4–5 (Jun–Jul'26).  
**Decision rule:** If ≥3 required fields are missing across all form types → add profile enrichment stories to R1 backlog before pre-fill stories. Don't build pre-fill on an incomplete profile model.

---

### Experiment 6 — Test A14: Vendor access agreements (split from Exp 2)

> Carved out of Experiment 2 because A14 is a different risk with a different owner and a longer lead time. A webhook can exist technically (A9) while the vendor still won't sign an access agreement (A14) — that's a legal/procurement gate, not an engineering one, and it's the single longest-lead item in R1. It needs its own trigger, earlier.

**Hypothesis:** OTG, C@G, and the relevant ATS will grant written API/webhook access agreements in time for R1 design (Aug–Sep'26).  
**Method:** Non-technical track owned by Michelle (not Pow Hwee). Identify the agreement owner in each of OTG, C@G, and the ATS org. Get the access request into each one's process early — government data-sharing agreements have multi-week approval cycles. Output: written confirmation (email or signed agreement) of access terms from each system.  
**Success criteria:** Agreement-in-principle (email) from OTG + C@G by **end of June'26**; ATS confirmed once "which ATS" resolves (Scope Concern #2). Full written terms by Aug'26.  
**Effort:** Low engineering, high coordination — stakeholder identification + follow-through across three orgs.  
**Timeline:** Start **now (Sprint 3)** — earliest of any experiment, because the approval clock is external and out of your control.  
**Decision rule:** No agreement-in-principle from a given system by end of June → escalate to Adrian as a viability risk, not a technical one. If OTG won't agree → status tracking descopes to R2 regardless of whether the webhook exists (ties to Exp 2's decision rule).

---

## Discovery Timeline

> **Revised 2026-05-20 — R1 build starts Oct '26.** Original plan assumed R1 backlog grooming Nov '26. Actual constraint: R1 design must lock Aug-Sep '26; backlog groomed Sep '26; build starts Oct '26. Any experiment meant to inform R1 design must complete by end of Aug '26. UAT (Sep-Oct '26) overlaps R1 build start — too late to change design direction. Officer-facing experiments moved to Sprint 6-7 with proxy research participants.

**Sprint 3 (Jun'26) — Gate: drawer vs. full-page design decision**
- Form complexity audit: Pow Hwee retrieves STIP/GIG schemas; Amber sketches drawer at 375px
- Output: drawer fit confirmed or full-page fallback decided before Amber starts R1 design

**Sprint 3 onward — Vendor access track (earliest start)**
- Experiment 6: vendor access agreements for OTG/C@G/ATS (Michelle) — start now; external approval clock is the longest lead in R1

**Sprint 4–5 (Jun–Jul'26) — Validate technical foundations**
- Experiment 2: OTG/C@G webhook spike — technical feasibility only (Pow Hwee); vendor-agreement half split out to Exp 6
- Experiment 5: Profile-to-form field mapping + schema stability check (Pow Hwee) — 4 in-scope types, SJR excluded pending Concern #3
- FE capacity estimate: Pow Hwee + Thomas size effort per in-scope application type

**Sprint 5 onward — Instrument MVP for behavioural signals**
- Experiment 4: Abandonment funnel live from MVP launch; first data Jul '26
- First data available ~2 months before R1 backlog grooming

**Sprint 6–7 (Jul–Aug'26) — Officer-facing research sessions (proxy participants)**
- Experiment 3: Wizard of Oz pre-fill — real profile data, 5 officers (PSD staff or via Jacky/Xian Zhang)
- Observed STIP task test — blank form, 5 officers, note abandonment moments
- Prototype usability test — drawer + pre-fill confirmation card (Amber's Figma)
- Recruit via: internal PSD staff, or BO network (Jacky/Xian Zhang). Frame as research, not UAT.

**Sep '26 — R1 backlog grooming**
- All experiment outputs reviewed; scope decisions made for: in-app application, pre-fill, draft save, status tracking
- R1 backlog sized and sequenced before Oct '26 build start

**MVP launch (Oct '26) — In-flight signal only**
- Experiment 1: Apply CTR + fake door tab goes live
- ⚠️ This data lands after R1 build starts — treat as an in-flight adjustment signal, not a pre-build gate
- If apply CTR < 10% in first 4 weeks → scope adjustment conversation with Adrian

---

## Decision Framework

| If... | Then... |
|---|---|
| Apply CTR from MVP ≥ 25% (Exp 1) | Proceed with in-app application as R1 centrepiece |
| Apply CTR < 10% | Investigate root cause before committing to R1 application build |
| OTG + C@G webhook confirmed by Sprint 6 (Exp 2) | Build status tracking on event-driven model |
| No webhooks by Sprint 6 | Descope live status tracking; replace with submission confirmation + email. Raise with Adrian. |
| Profile coverage ≥ 70%, correction rate < 20% (Exp 3) | Build smart pre-fill for STIP + GIG first; expand to other types by mid-R1 |
| Profile coverage < 50% | Descope pre-fill; prioritise profile enrichment in R1 instead |
| Abandonment > 40% (Exp 4) | Validate draft save as R1 priority |
| Abandonment < 20% | Descope draft save to R2; simplify the application flow |
| ≥ 3 required fields missing from field mapping (Exp 5) | Add profile enrichment stories to R1 backlog before pre-fill |

---

## Scope Concerns Not Yet Resolved

These aren't assumptions for experiments — they're questions that need a decision before R1 grooming.

1. **"Application within CareerCompass" definition.** Does "no redirects" mean the officer never sees OTG or C@G? Or that the experience *starts* in CareerCompass even if the final submission goes to the source system? The answer determines the technical scope by an order of magnitude. Get a crisp definition from the deck author before R1 planning.

2. **Which ATS?** The deck references "ATS integration" but OTEP integrates with OTG (file import), C@G (API), and potentially a separate ATS for internal jobs. Which system(s) is "ATS" in the R1 status tracking feature? Confirm with Jacky/Xian Zhang.

3. **SJR in R1.** Update (2026-06-02): the MVP position hardened — decision **2026-05-21** excludes 2026 SJRs from ingestion entirely (supersedes "visible but no apply"). So SJR has no MVP footprint at all: not ingested, no apply flow, no card. The R1 deck still lists SJR under pre-filled applications. Re-introducing SJR in R1 therefore isn't an increment on MVP — it's a net-new integration track (ingestion + apply + schema mapping) with its own engineering cost. **Decision needed before R1 grooming:** is SJR genuinely in R1, or did it carry over from an older deck? Confirm with Adrian/Jace. Until confirmed, treat SJR as out and exclude it from Exp 5 schema mapping.

4. **External-facing Profile security model.** Sharing an officer's profile externally (to hiring managers) raises data classification questions. Is this a public link, a permissioned link, or a system-to-system API call? Government data handling rules apply. Needs a decision and a security review scope update.

---

## Next Steps

> Re-baselined 2026-06-02 (now Sprint 3). The five items originally tagged "Sprint 2 W2 / this week" are still open and now **overdue** — they were the discovery's earliest gates and need clearing this sprint before they block R1 design lockdown.

| Action | Owner | When | Urgency |
|---|---|---|---|
| Run vendor access-agreement track (A14 — now Exp 6) | Michelle | **Sprint 3 — start now** | 🔴 Overdue — longest external lead time |
| Confirm draft data security classification with security contact (A13) | Michelle | **Sprint 3** | 🔴 Overdue |
| Clarify "application within CareerCompass" definition (Adrian/Jace) | Michelle | **Sprint 3** | 🔴 Overdue — sets technical scope by an order of magnitude |
| Confirm which systems count as "ATS" in R1 status tracking | Michelle + Jacky/Xian Zhang | **Next BO sync** | 🔴 Overdue |
| Confirm whether SJR apply flow is in R1 at all (Scope Concern #3) | Michelle | **Sprint 3** | 🔴 Overdue — gates Exp 5 schema scope |
| Form complexity audit — drawer fit decision | Pow Hwee + Amber | Sprint 3 | 🟡 Blocks design |
| Run Experiment 2 + 5 as combined spike (OTG/C@G APIs + schema mapping) | Pow Hwee | Sprint 4–5 | 🟡 Blocks backlog |
| FE capacity estimate for in-scope application types (4; +SJR if confirmed) | Pow Hwee + Thomas | Sprint 4–5 | 🟡 Blocks backlog |
| Instrument apply CTR and abandonment funnel | Leo/Thomas | Sprint 5 | 🟡 Before MVP |
| Recruit proxy research participants (PSD staff or BO network) | Michelle | Sprint 5 | 🟡 Before Sprint 6-7 |
| Run Sprint 6-7 research sessions (pre-fill WoZ, STIP task test, prototype) | Michelle + Amber | Sprint 6–7 (Jul–Aug) | 🟠 Before Sep grooming |
| Review all experiment outputs and groom R1 backlog | Michelle | Sep '26 | 🟠 Gate for R1 start |

---

## Offer: What to do next

- **Write an interview script** to run with 5 UAT officers on application channel preference (feeds Experiment 1)
- **Create a PRD skeleton** for the top R1 feature (in-app application) with the open scope questions flagged
- **Set up a metrics plan** for the MVP analytics instrumentation needed for Experiments 1 and 4
- **Draft the BO sync ask** to get SJR and ATS scope confirmed with Jacky/Xian Zhang

---

*Living document — update as experiments run and scope decisions are logged in `decisions-log.md`.*  
*Source: Project OTEP OKR Review and Roadmap deck (uploaded 2026-05-20) + sprint-status.md + risks.md*  
*Reconciled 2026-06-02 against current state: pilot → MVP-6; SJR excluded from MVP (D 2026-05-21); formsg_url confirmed; auth de-risked via Keycloak (D 2026-06-02); A14 split into Experiment 6; Next Steps re-baselined to Sprint 3.*
