# Full Discovery: Seamless Application — ATS Status Tracking vs. OTEP-Native Status

**Date:** 2026-05-19
**Last updated:** 2026-05-19 (aligned to revised R1 slide)
**Product:** CareerCompass (OTEP R1 — Jan '27)
**Stage:** Existing product, major scope pivot
**Discovery question:** What is the right application experience for officers across all opportunity types — and how does status tracking work if the Workable ATS integration doesn't materialise?

---

## Confirmed R1 Scope (from revised roadmap slide)

The R1 "Seamless Application" release is defined as: **Click-Apply-Track. Frictionless action on career opportunities.**

Five features are in scope:

1. **Streamlined Application** — For HR: post jobs directly in CareerCompass. For officers: pre-filled job applications, apply directly from CareerCompass without redirects.
2. **Status Tracking** — End-to-end application monitoring, with ATS (Workable) integration if confirmed.
3. **Application within CareerCompass** — Seamless application experience with no redirects to external forms.
4. **Saved Jobs** — Officers can quickly resume applications for target jobs.
5. **External Facing Profile page** — Officer profile accessed during the application process, displayed as read-only.

**Formally deprioritised (not in R1):**
- Smart Assistant (auto-populates strengths/experience)
- Gap Radar (insights for target roles)
- Intelligence Dashboard (usage pattern tracking)

---

## Revised Scope Interpretation

The slide resolves one major ambiguity from the original pivot description: **job creation now explicitly lives in CareerCompass** ("Post jobs in Compass"), not in the ATS. This changes the Two Worlds framework significantly.

The ATS (Workable) is now scoped specifically to **status tracking** — not to job creation or application submission routing. Both of those happen in Compass regardless of whether the ATS partnership confirms.

**What this means:**

- OTEP must build a job posting tool for HR regardless of ATS outcome
- OTEP must build an application submission flow regardless of ATS outcome
- The June ATS decision now only affects **one** capability: whether status tracking is automated (via Workable webhooks) or manual (hiring managers update in OTEP)

This is a much narrower fork than originally framed. The Two Worlds are now much closer together.

**One open question the slide creates:** Does "Post jobs in Compass" mean (a) HR creates jobs directly in OTEP's database, or (b) HR creates jobs in Workable and they sync to Compass? The slide implies (a) — which means OTEP owns the job creation data layer — but this needs explicit confirmation before sprint planning.

**The critical fork:** If the Workable ATS partnership doesn't confirm in June, the team builds a manual status management layer in OTEP. This is a scoped additional build, not a full product pivot.

This discovery covers both worlds so the team arrives at the June gate with evidence, not assumptions.

---

## Two Worlds (Revised)

Both worlds now share the same foundation. The only difference is how status tracking works.

| Dimension | World A — With ATS | World B — OTEP Native |
|-----------|-------------------|----------------------|
| Job creation | HR posts directly in CareerCompass | HR posts directly in CareerCompass |
| Application submission | Officers apply in CareerCompass (OTEP-native form) | Officers apply in CareerCompass (OTEP-native form) |
| Status tracking | Workable webhooks → automated status in OTEP | Hiring managers update status manually in OTEP |
| OTEP's role | Full-stack product + ATS status layer | Full-stack product, fully self-contained |
| Engineering scope | OTEP build + Workable integration (status only) | OTEP build + hiring manager status UI |
| Risk type | External dependency for status (vendor, data residency) | Internal adoption (will HMs update statuses?) |
| External Facing Profile | Same in both worlds | Same in both worlds |
| Saved Jobs | Same in both worlds | Same in both worlds |

**The critical difference is smaller than previously scoped.** The previous framing had the ATS as the system of record for jobs and applications. The slide confirms that OTEP owns job creation and application submission in both worlds. ATS is now only a status data source.

---

## Ideas Explored

### World A — With ATS (10 ideas)

**PM perspective**

1. **Progressive ATS rollout** — pilot Workable with GIGs only (simplest job type, smallest field set). Prove the integration pattern, then expand to STIP, Internal, SJR, and C@G in sequence. Reduces risk of a big-bang integration across five incompatible schemas at once.

2. **ATS as source of truth** — OTEP owns zero application or job data. Workable is the system of record; OTEP is purely the officer-facing display and submission layer. Clean separation of concerns, but creates a hard dependency on Workable uptime and API reliability.

3. **Hybrid status model** — Workable tracks formal application status (shortlisted, interviewed, rejected, hired). OTEP adds a "soft" status layer visible only to officers: saved, draft, submitted, withdrawn. Officers see richer context than what Workable exposes.

**Designer perspective**

4. **Single unified application flow** — one UI regardless of job type. Officers see the same form, the same submission confirmation, the same status dashboard. Backend routing to different Workable pipelines is invisible. Simplifies the officer experience but requires significant field normalisation work upfront.

5. **Application status dashboard** — a "My Applications" hub that translates Workable's hiring-manager-centric status language into officer-readable language. "Under review" instead of "pipeline stage 2". Status is push-notified when it changes.

6. **External Facing Profile as pre-application gate** — officers must complete their profile to a minimum completeness threshold before the Apply button activates. Drives profile quality, but adds friction. Could be a toggle rather than a hard gate.

**Engineer perspective**

7. **Workable webhook listener** — OTEP registers a webhook endpoint with Workable. When an application status changes (any stage), Workable pushes an event. OTEP updates its local status display in near-real-time. No polling needed.

8. **ATS job sync (pull model)** — OTEP fetches job listings from Workable on a schedule (e.g., every 15 minutes). Workable remains the posting tool for agencies; OTEP displays what's there. Lower complexity than a full bidirectional sync.

9. **Canonical application schema layer** — a mapping layer that translates OTEP's unified application fields into Workable's job-type-specific API fields. This is the critical engineering piece that makes a single UI possible across five job types.

10. **FormSG bridge as interim** — while Workable integration is being built, maintain FormSG as the submission backend. OTEP wraps the FormSG form in an iframe or deep-link that feels in-app. Officers don't see the redirect; technically it still happens. Allows the team to ship "in-app applications" before ATS integration is complete.

---

### World B — OTEP Native (10 ideas)

**PM perspective**

1. **OTEP as a lightweight ATS** — build a minimal applicant tracking system natively: officers submit applications, hiring managers see a candidate list, statuses get updated. Not a full ATS — no interview scheduling, no offers — just enough to manage the pipeline.

2. **FormSG as permanent middleware** — keep FormSG as the submission backend permanently. OTEP wraps it with a native-feeling UI: the form is embedded or the submission is triggered programmatically. Officers don't see a redirect. Agencies keep their existing FormSG-to-downstream integrations intact.

3. **Staged subsumption** — OTEP takes ownership in three phases: (a) application submission first, (b) status tracking second, (c) opportunity creation third. Each phase is a separate release. Don't try to build all three in R1.

4. **Federated status aggregation** — OTEP doesn't own status; it aggregates it from multiple sources (email parsing, agency-submitted updates, C@G deep-links). Status is "best available" rather than authoritative. Works without requiring agencies to change their workflows.

**Designer perspective**

5. **"Apply here" universal button** — regardless of backend, the officer experience is identical: one button, one confirmation screen, one status entry in "My Applications." Whether submission routes to FormSG, an email, or OTEP's own database is invisible.

6. **Officer-controlled status** — when automated tracking isn't possible (agency hasn't updated), officers can self-report: "I got an interview," "I withdrew," "No response." Keeps the status dashboard useful even with incomplete data. Risk: self-reported data is unreliable.

7. **Opportunity creation as a simple form** — a structured form that agencies fill in to post opportunities directly in OTEP. Fields map to the five job types. Submissions go into OTEP's database, not OTG. Simpler than a full CMS but gives agencies direct control.

**Engineer perspective**

8. **OTEP-native application store** — a proper application database: officer ID, opportunity ID, submission timestamp, status, documents. Hiring managers have a read-only view. All status changes are manual but auditable.

9. **Agency notification layer** — when an officer submits an application in OTEP, the hiring manager receives an email with the officer's External Facing Profile attached. No login required to see the applicant. Reduces the need for hiring managers to adopt a new tool immediately.

10. **FormSG webhook bridge** — OTEP registers a webhook with FormSG. When an officer submits a FormSG form linked to an OTEP opportunity, the submission triggers an event that creates an application record in OTEP. Officers get confirmation inside CareerCompass even though FormSG handled the actual submission.

---

## Selected Ideas to Carry Forward

Five ideas per world, selected for assumption mapping based on relevance to the phasing decision.

### World A
| # | Idea | Rationale |
|---|------|-----------|
| A1 | Progressive ATS rollout (GIGs first) | Reduces integration risk; allows learning before full commitment |
| A2 | ATS as source of truth, OTEP as UI layer | Clean architecture that defines team responsibility boundaries |
| A3 | Single unified application flow (invisible routing) | Officer experience goal; but requires solving the schema problem first |
| A4 | Workable webhook for status sync | The technical mechanism that makes status tracking work |
| A5 | FormSG bridge as interim | Decouples "in-app feel" from "ATS integration complete" — ships value sooner |

### World B
| # | Idea | Rationale |
|---|------|-----------|
| B1 | FormSG as permanent middleware | Lowest-disruption path; agencies keep existing workflows |
| B2 | Staged subsumption (submission → tracking → creation) | Makes the scope manageable; avoids a big-bang R1 |
| B3 | OTEP-native application store | Required if OTEP is to own application history and status |
| B4 | Agency notification layer (email-based) | Reduces hiring manager adoption barrier; doesn't require them to learn a new tool |
| B5 | Opportunity creation as a structured form | Required for World B — agencies have no other way to post to OTEP |

---

## Critical Assumptions

### Shared assumptions (both worlds — OTEP owns job creation and application submission in both)

These assumptions apply regardless of ATS outcome. They must be validated before any sprint work starts.

| # | Assumption | Category | Impact | Uncertainty | Priority |
|---|-----------|----------|--------|-------------|----------|
| S1 | HR will adopt CareerCompass as their job posting tool — this is a new behavior on top of existing workflows | Viability | Very high | High | 🔴 Leap of faith |
| S2 | A unified application schema can be agreed across STIP, GIG, SJR, C@G, and Internal job types | Feasibility | Very high | High | 🔴 Leap of faith |
| S3 | Business owners (Jacky, Xian Zhang) will endorse removing the FormSG redirect from the officer-facing application flow | Viability | High | High | 🔴 Leap of faith |
| S4 | "Post jobs in Compass" means HR creates jobs directly in OTEP's database (not: Workable creates jobs and syncs to Compass) | Feasibility | High | High | 🔴 Leap of faith — **confirm before sprint planning** |
| S5 | The team has capacity to build job creation (HR-facing) + application submission + status UI within R1 | Viability | Very high | High | 🔴 Leap of faith |
| S6 | OTEP-native application store can cover all five job types within R1 sprint capacity | Feasibility | High | Medium | 🟠 High priority |
| S7 | A single unified application UI can accommodate all five job types despite different field requirements | Usability | High | High | 🟠 High priority |
| S8 | Officers meaningfully prefer in-app application over FormSG redirect (does removing the redirect drive higher application rates?) | Value | High | Medium | 🟠 High priority |
| S9 | External Facing Profile data from OTG is complete enough to be useful to hiring managers at launch | Feasibility | Medium | Medium | 🟡 Medium priority |
| S10 | Hiring managers will actively use External Facing Profiles during screening | Value | Medium | High | 🟡 Medium priority |
| S11 | Officers browse opportunities without immediate intent to apply, validating the Saved Jobs need | Value | Medium | Medium | 🟡 Medium priority |
| S12 | SJR apply behaviour is defined — previously no apply action existed for SJRs in MVP scope | Usability | Medium | High | 🟡 Medium priority |
| S13 | Officers will maintain their profile to a completeness level that's useful for External Facing Profile | Usability | Low | Medium | 🟢 Lower priority |

### World A — With ATS (status tracking only)

The ATS (Workable) is now scoped only to status tracking. Job creation and application submission are OTEP-native in both worlds.

| # | Assumption | Category | Impact | Uncertainty | Priority |
|---|-----------|----------|--------|-------------|----------|
| A1 | Workable ATS partnership is confirmed and procured by June | Viability | High | Very high | 🔴 Leap of faith |
| A2 | Government data sovereignty requirements are compatible with Workable (for status data, not application data) | Viability | High | High | 🔴 Leap of faith |
| A3 | Workable API supports status retrieval and webhook events for all five job types | Feasibility | High | High | 🔴 Leap of faith |
| A4 | Workable's status model (hiring-manager-centric) can be translated into officer-readable language | Usability | Medium | Medium | 🟠 High priority |
| A5 | Workable webhook reliability is sufficient for a near-real-time status tracking feature in production | Viability | Medium | Medium | 🟠 High priority |

### World B — OTEP Native (status tracking only delta)

World B is now a narrower scope change than originally framed — OTEP needs a manual status management layer instead of ATS webhooks.

| # | Assumption | Category | Impact | Uncertainty | Priority |
|---|-----------|----------|--------|-------------|----------|
| B1 | Hiring managers will update application statuses in OTEP without an external mandate | Value | High | High | 🔴 Leap of faith |
| B2 | A hiring manager–facing status management UI can be scoped and built within R1 capacity | Feasibility | High | Medium | 🟠 High priority |
| B3 | Agency email notifications (officer profile attached) reduce the need for hiring managers to log in to OTEP to see applicants | Feasibility | Medium | Medium | 🟡 Medium priority |
| B4 | PSD leadership will accept manual status tracking as a valid R1 feature if ATS doesn't confirm | Viability | High | Medium | 🟡 Medium priority |

### Formally out of scope — removed from assumption tracking

Smart Assistant, Gap Radar, and Intelligence Dashboard are deprioritised. No assumptions tracked for these. If they resurface as stakeholder requests, flag immediately as scope creep.

---

## Validation Experiments

Experiments are now ordered by urgency, not by world. Experiments 1–4 start immediately and are independent of the ATS decision.

---

### Experiment 1 — Confirm job creation architecture [S4 — CRITICAL, run first]

**What we're testing:** Does "Post jobs in Compass" mean HR creates jobs directly in OTEP's database, or does Workable remain the job creation system with a sync to Compass?

**Why this is first:** If it's a sync, OTEP is still the UI layer for job discovery and the ATS owns the data. If it's direct creation, OTEP owns the job database. These are different products and different engineering builds. Every other sprint decision depends on this answer.

**Method:** One conversation with Adrian (or Jacky) to confirm the intended data architecture. Present both options explicitly and ask which one the slide intended.

**Success criteria:** A written, confirmed answer. No ambiguity. Shared with Pow Hwee before the next grooming.

**Effort:** 1 x 15-minute conversation.

**Owner:** Michelle.

**Timeline:** Before anything else. This week.

---

### Experiment 2 — Application schema workshop [S2, S7]

**What we're testing:** Can we define a unified application schema across all five job types? What are the exceptions?

**Method:** A structured 2-hour workshop with Jacky, Xian Zhang, Pow Hwee, and Ops. Bring the current FormSG field list for each job type. Map side by side.

**Workshop agenda:**
1. Each domain owner lists mandatory application fields per job type (30 min)
2. Group maps overlap — what's universal, what's job-type-specific, what's agency-specific (45 min)
3. Agree: standardise, or handle exceptions with conditional fields? (30 min)
4. Confirm: what does FormSG currently send downstream after submission? What breaks if it's removed? (15 min)

**Success criteria:**
- Shared schema covering ≥80% of fields across all five types
- Documented exceptions with agreed handling
- Explicit answer on downstream FormSG dependencies

**Output:** Canonical application schema v1. This is the prerequisite for Pow Hwee's sprint grooming.

**Effort:** 1 x 2-hour workshop + 2 hours prep.

**Owner:** Michelle (facilitate); Pow Hwee (technical schema output).

**Timeline:** This sprint. No ATS dependency.

---

### Experiment 3 — Business owner conversation: FormSG and HR job posting [S1, S3]

**What we're testing:** Two questions in one conversation.
- Will Jacky and Xian Zhang agree to move application submission off FormSG?
- Are they willing to post jobs directly in CareerCompass as part of their workflow?

**Method:** Separate 30-minute conversations with Jacky and Xian Zhang. Don't pitch. Probe.

**On FormSG:**
- "Walk me through what happens after an officer submits a FormSG application. Where does that data go?"
- "What would have to be true for you to be comfortable moving submission into CareerCompass?"

**On HR job posting:**
- "If posting a job in CareerCompass took 10 minutes and gave you a direct applicant list, would you use it instead of your current process?"
- "What's your current process for getting a new opportunity visible to officers?"

**Success criteria:**
- Explicit buy-in on both flows, OR a clear list of conditions the team can design against
- Understanding of downstream system dependencies on FormSG

**Effort:** 2 x 30-minute conversations.

**Owner:** Michelle. Stakeholder influence exercise — not technical.

**Timeline:** This week or next.

---

### Experiment 4 — R1 capacity spike [S5, S6, B2]

**What we're testing:** Can the full R1 scope — HR job creation tool, officer application submission, status tracking UI (in either world), External Facing Profile, Saved Jobs — actually fit in the remaining sprint capacity?

**Method:** Pow Hwee estimates effort for each surface:
- HR job creation form (OTEP-native)
- OTEP application submission store (database + officer form)
- Status display — officer-facing ("My Applications")
- Status management — World A (webhook integration) vs World B (hiring manager UI)
- External Facing Profile (read-only display)
- Saved Jobs (bookmark + resume)

Map estimates against remaining sprint capacity. Flag: what's R1, what's R1.5, what's R2.

**Success criteria:**
- A scoped R1 that fits capacity with clear phase boundaries, OR
- A clear articulation of what gets cut to make it fit

**Output:** Capacity plan with phased delivery recommendation. Feeds directly into sprint planning.

**Effort:** 1–2 days, Pow Hwee.

**Owner:** Pow Hwee (estimates); Michelle (prioritisation call).

**Timeline:** This sprint. Run in parallel with Experiments 1–3.

---

### Experiment 5 — Workable status API proof of concept [A1, A2, A3]

**What we're testing:** Does the Workable API support status retrieval and webhook events for the job types we have? Is the data residency compatible with government requirements?

**Method:** Two parallel tracks:
- Pow Hwee requests sandbox access. Tests: register a webhook, receive a status event, confirm latency and reliability. Map Workable's status model to officer-readable language.
- Michelle (or procurement lead) asks Workable: Where is data stored? Is Singapore-region hosting available? What is the data processing agreement?

**Define failure upfront:**
- Webhook latency >5 min → real-time status not viable
- No Singapore data residency option → World A blocked on sovereignty grounds
- Status model has no equivalent for all five job types → significant mapping work required

**Output:** A compatibility assessment: World A status integration is viable / not viable / viable with conditions.

**Effort:** Pow Hwee, 1-sprint spike (can start as soon as sandbox access is granted).

**Owner:** Pow Hwee (API); Michelle (vendor + data residency conversation).

**Timeline:** Before June. Initiate the Workable conversation this week alongside Experiment 1.

---

### Experiment 6 — Hiring manager status behavior test [B1]

**What we're testing:** In World B, will hiring managers update application statuses in OTEP without an external mandate?

**Method:** Amber builds a low-fidelity mockup of the hiring manager status view. Show 3 hiring managers. Ask:
- "If CareerCompass sent you a list of your applicants and asked you to update their status once a week, would you do it?"
- "What would make you ignore it?"
- "How do you currently track where candidates are?"

**Success criteria:**
- ≥2 of 3 say they'd update statuses regularly with minimal friction
- If fewer: World B status tracking requires a leadership mandate to function. Document this for Adrian.

**Effort:** Amber, 1 day (mockup); Michelle, 3 x 20-minute conversations.

**Owner:** Amber (mockup); Michelle (conversations).

**Timeline:** Week 2–3.

---

### Experiment 7 — External Facing Profile data completeness check [S9, S10]

**What we're testing:** Is OTG profile data complete enough for a hiring manager to use during screening?

**Method:** Pull a sample of 20 anonymised officer profiles from OTG. Assess field completion and accuracy. Show 3 hiring managers a real sample and ask: "Would this tell you enough to make a shortlisting decision?"

**Success criteria:**
- ≥70% field completion across sampled profiles
- ≥2 of 3 hiring managers say the profile contains the signals they need

If not met: External Facing Profile ships as a stub with a completion prompt. Full-data version deferred post-launch.

**Effort:** Pow Hwee (data pull, 1 day); Michelle (3 x 15-min conversations).

**Owner:** Pow Hwee + Michelle.

**Timeline:** Week 2. No ATS dependency — start immediately.

---

## Discovery Timeline

| When | Experiment | Owners | Unblocks |
|------|------------|--------|----------|
| **This week** | Exp 1: Confirm job creation architecture (15-min convo) | Michelle | Every other decision |
| **This week** | Exp 3: Business owner conversations (FormSG + HR posting) | Michelle | S1, S3 |
| **This sprint** | Exp 2: Application schema workshop | Michelle, Jacky, Xian Zhang, Pow Hwee | S2, S7 — universal prerequisite |
| **This sprint** | Exp 4: R1 capacity spike | Pow Hwee | S5, S6, B2 |
| **This sprint** | Exp 5: Initiate Workable sandbox + data residency check | Michelle, Pow Hwee | A1, A2, A3 |
| **Week 2** | Exp 7: Profile data completeness check | Pow Hwee + Michelle | S9, S10 |
| **Week 2–3** | Exp 5 continued: API proof of concept results | Pow Hwee | World A viability confirmed |
| **Week 3** | Exp 6: Hiring manager status behavior test | Amber + Michelle | B1 |
| **Before June** | All experiments synthesised into go/no-go brief | Michelle | ATS gate decision |
| **June gate** | ATS partnership decision | Leadership | World A or B for status tracking |
| **Post-June** | R1 scope finalised, sprint plan updated | Michelle + Pow Hwee | Engineering kick-off |

---

## Decision Framework

### At the June gate — use experiment findings to make the call

**If ATS confirmed and all experiments pass:**
Full R1 as scoped. OTEP-native job creation and application submission, Workable webhook status tracking, External Facing Profile, Saved Jobs. SJR apply behaviour needs an explicit decision before sprint planning (previously had no apply action).

**If ATS confirmed but data sovereignty fails (Exp 5):**
World A blocked regardless of API capability. Default to World B status tracking (hiring manager manual updates). No change to job creation or application submission scope — those are OTEP-native in both worlds.

**If ATS confirmed but hiring manager behavior test fails (Exp 6):**
Status tracking (either world) requires a leadership mandate to function. Escalate to Adrian before committing to the feature. Don't build a status layer officers will see as empty.

**If ATS not confirmed:**
Switch status tracking to World B (OTEP-native manual updates). Everything else is unchanged. This is now a delta, not a full pivot.

**If schema workshop fails (Exp 2) — unified form not achievable:**
Scope in-app applications to GIGs and Internal jobs only (simplest schemas) for R1. STIP, SJR, C@G keep FormSG redirect with in-app wrapper. Full unification moves to R2.

**If capacity spike shows R1 is overloaded (Exp 4):**
Cut in this order: (1) hiring manager status UI → R1.5, (2) External Facing Profile → stub only, (3) Saved Jobs stays (lowest complexity). Do not cut job creation or application submission — those are the core of R1's stated value.

---

## Open Questions

1. **Job creation architecture (S4 — URGENT):** Does "Post jobs in Compass" mean HR creates directly in OTEP's database, or Workable syncs to Compass? Confirm with Adrian before sprint planning.
2. **SJRs:** The previous MVP scope had no apply action for SJRs. Does in-app applications change this? Who owns the decision?
3. **C@G jobs:** Previously a Careers@Gov deep-link. Does in-app applications replace that link, or is C@G always an external redirect regardless of ATS?
4. **FormSG downstream (Exp 3 must answer this):** What systems consume FormSG submission data today? What breaks if FormSG is removed from the flow?
5. **Hiring manager identity:** Are hiring managers named users with OTEP accounts, or does OTEP notify them externally? A hiring manager status UI requires accounts. External notifications don't.
6. **Saved Jobs complexity:** Is "saved" a bookmark (a flag on an opportunity record) or a draft application state ("continue where you left off")? These are very different in data complexity and UX.
7. **Matching:** Formally remove from R1 roadmap discussions and set expectations with stakeholders now. Revisit when competency data quality is audited.

---

## PM Position

**The Two Worlds are now much closer than originally framed.** The slide confirms OTEP owns job creation and application submission in both scenarios. The only decision that changes in June is how status tracking is implemented — webhook vs. manual. That's meaningful but it's not a full architectural pivot. Don't let the team treat it like one.

**The most urgent thing on this list is Experiment 1** — confirming what "Post jobs in Compass" actually means. It's a 15-minute conversation that unlocks every downstream decision. Run it before the end of this week.

**The highest-risk assumption isn't the ATS** — it's S1 and S3: whether HR will post jobs in Compass and whether Jacky will endorse removing FormSG from the officer flow. Both are behavior change asks on people who already have working processes. Experiment 3 answers both. Run it this sprint.

**External Facing Profile and Saved Jobs ship in R1 regardless.** Both are decoupled from the ATS decision and from the FormSG migration. Start designing them now without waiting for June.
