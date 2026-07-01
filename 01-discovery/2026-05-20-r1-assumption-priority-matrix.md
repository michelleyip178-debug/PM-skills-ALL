# Assumption Priority Matrix: R1 — Seamless Application

**Date:** 2026-05-20 (timeline revised 2026-05-20 — R1 starts Oct '26)
**Product:** CareerCompass (OTEP)
**Sources:** `2026-05-20-r1-discovery-plan.md` + `2026-05-20-r1-brainstorm-seamless-apply.md` + `2026-05-20-r1-experiments-seamless-apply.md`
**Framework:** Impact × Risk matrix. Impact = value if validated × officers affected. Risk = (1 − confidence) × effort to validate.

> **Timeline note (revised 2026-05-20):** R1 build starts Oct '26. MVP go-live is also Oct '26 (16 Oct). R1 design must be locked Aug-Sep '26. R1 backlog grooming must happen Sep '26. This compresses the experiment window significantly — any experiment that needs to *inform* R1 design decisions cannot wait until UAT. See revised priority table below.

---

## The matrix

| Quadrant | What it means | Action |
|---|---|---|
| 🔴 High Impact, High Risk | If wrong, R1 fails or fundamentally changes. We don't know yet. | Design experiment now |
| 🟡 High Impact, Low Risk | High value, confirmable quickly or confidence already high | Spike / audit; proceed |
| 🟠 Medium Impact, Medium Risk | Worth testing but not blocking | Test if capacity allows |
| 🟢 Low Impact, Low/Medium Risk | Low stakes regardless of outcome | Defer or build and monitor |
| ⛔ Any Impact, High Risk + Unresolvable | External or structural blocker we can't validate alone | Escalate, don't design around |

---

## 🔴 High Impact, High Risk — Design experiment now

These are your leap-of-faith assumptions. If any one of them is false, the feature it underpins cannot ship as designed. Run experiments before committing to R1 backlog.

---

**A1 — Officers will choose CareerCompass to apply, rather than going directly to OTG/C@G**

- **Why high impact:** The entire R1 OKR (20% applied via CareerCompass) is unreachable if officers default to source systems out of habit. This is the single most existential assumption for R1.
- **Why high risk:** Officers have years of OTG muscle memory. We have zero behavioural evidence that they'll shift channels. Confidence: very low.
- **Experiment:** Fake door "My Applications" tab (Exp 3b) + Apply CTR from detail page in MVP (Exp 4b). Both passive — no extra build beyond analytics hooks.
- **Success threshold:** ≥20% of active sessions click "My Applications" tab; ≥25% of detail page visitors click Apply CTA.
- **Gap:** Neither experiment is running yet. Must instrument before MVP launch.

---

**A2 — Officer profile data will be accurate and complete enough to pre-fill meaningfully at R1 launch**

- **Why high impact:** Pre-fill that surfaces wrong data is worse than no pre-fill. It destroys trust in CareerCompass faster than it builds it. Affects every officer who applies.
- **Why high risk:** MVP launches without profile enrichment at scale. We genuinely do not know what completeness looks like in the wild. Confidence: low.
- **Experiment:** Wizard of Oz pre-fill with real profile data during UAT (Exp 2a). Audit profile completion across pilot cohort before the session.
- **Success threshold:** Correction rate < 25% across sampled fields. ≥3/5 officers react positively.
- **Gap:** Experiment requires real profile data from UAT cohort. Pow Hwee must pull data before sessions run.

---

**A5 — Officers abandon STIP applications mid-way at meaningful rates**

- **Why high impact:** Save-and-resume is non-trivial to build (especially with government data handling constraints). If abandonment is low, it's wasted capacity. If high, skipping it kills completion for CareerCompass's highest-value opportunity type.
- **Why high risk:** No data. Abandonment could be caused entirely by redirect friction (solved by the drawer in R1) rather than form length — in which case draft save adds complexity with no lift.
- **Experiment:** Observed STIP task test in UAT (Exp 4a) + MVP abandonment funnel segmented by type (Exp 4b).
- **Success threshold:** ≥3/5 officers pause or express intent to stop in UAT task. Abandonment rate >40% in MVP funnel.
- **Gap:** Funnel instrumentation must be built before MVP launch (Sprint 5). Segment by opportunity type from the start.

---

**A9 / A10 — OTG and C@G expose application status events at useful granularity (≥3 distinct states)**

- **Why high impact:** Status tracking is the entire "track" part of "Click-Apply-Track." Without event APIs, the My Applications dashboard is just a submission log. The 24-hour latency OKR is impossible to meet without it.
- **Why high risk:** Completely unknown. OTG and C@G are external systems we don't control. They may have no event model at all, or only expose aggregate data.
- **Experiment:** API/event granularity spike (Exp 3a). Pow Hwee + one stakeholder call with OTG and C@G integration contacts.
- **Success threshold:** ≥3 distinct status states confirmed from OTG. ≥2 from C@G. At least one system supports push webhooks.
- **Gap:** This must run in Sprint 4–5 — the single hardest deadline in the experiment plan. If not resolved by Jul '26, R1 backlog grooming proceeds without the status dashboard.

---

**A14 — OTG, C@G, and ATS vendors will agree to API/webhook access in time for R1 build**

- **Why high impact:** Even if the APIs exist (A9/A10 confirmed), access may require procurement, legal review, or vendor approvals that take months. Missing this gate means R1 ships without status tracking.
- **Why high risk:** External dependency. Government procurement processes are slow. Confidence: low. We have no open conversations with vendors on this yet.
- **Experiment:** Escalate to Adrian by end of Sprint 2 to open vendor conversations. This isn't an experiment — it's a dependency that needs an owner and a deadline. Michelle to raise at the next steering touchpoint.
- **Success threshold:** Written API access agreement (or confirmed pathway) from OTG + C@G by Sprint 6 (end of Jul '26).
- **Gap:** No one has started this conversation yet. This is the highest-urgency action from this entire analysis.

---

**A12 — In-app application flows for 5 opportunity types are achievable within the 3-month R1 window**

- **Why high impact:** If this is false, R1 ships partial — some types have in-app apply, others still redirect. "Application within CareerCompass" becomes a half-truth.
- **Why high risk:** Thomas is sole FE developer. 5 types are not trivial. 3 months is tight given compliance, security review, and cross-squad competition for his time. Confidence: medium-low.
- **Experiment:** Engineering capacity spike — Pow Hwee and Thomas estimate effort per application type once form schemas are documented (builds on Exp 5a). Sequence: build STIP + GIG first (highest volume). SJR, C@G, Internal Jobs as fast-follow or R1.1.
- **Success threshold:** Effort estimate shows STIP + GIG achievable within R1 window with current team. All 5 types achievable with one additional FE or extended timeline.
- **Gap:** No capacity estimate exists yet. Pow Hwee and Thomas need to produce one before R1 backlog is sized.

---

## 🟡 High Impact, Low-Medium Risk — Spike or audit, then proceed

Assumptions worth confirming quickly. Risk is lower because we can validate fast or confidence is already reasonable.

---

**A11 — Profile fields map cleanly to STIP/GIG/SJR/C@G/Internal form schemas**

- **Why high impact:** Pre-fill doesn't work if profile data doesn't cover the right fields. Coverage < 50% means pre-fill is noise.
- **Why lower risk:** We have the data model. Getting form schemas from OTG/C@G is a known task. Confidence: medium.
- **Experiment:** Schema mapping spike (Exp 5a — schema audit and stability check). Can be combined with A9/A10 spike.
- **Success threshold:** ≥60% field coverage across STIP and GIG (primary types). Gap count defined. Missing fields flagged for profile enrichment stories.

---

**B1 — STIP and GIG application forms are simple enough to render inside a drawer**

- **Why high impact:** If forms are too complex for a drawer, Amber's entire R1 design direction changes. This decision gates all downstream design work.
- **Why lower risk:** Can be audited quickly by counting fields and sections against a 375px drawer sketch. One day of work.
- **Experiment:** Form complexity audit (Exp 1a). Pow Hwee retrieves schemas; Amber sketches drawer at actual mobile width.
- **Success threshold:** All core types fit without exceeding 3 full scrolls on a standard phone screen.
- **Note:** Run this in Sprint 3 — the earliest it can inform design direction.

---

**B4 — All 5 form schemas are stable for the R1 build window (no breaking changes Oct '26 – Jan '27)**

- **Why high impact:** Build a schema registry on schemas that are about to change and you rebuild the foundation mid-sprint.
- **Why lower risk:** Schema stability is a confirmable fact, not a behaviour. One conversation with OTG/C@G contacts.
- **Experiment:** Combined with Exp 5a (schema audit). Add one question to the stakeholder call: "Any planned schema changes in the next 9 months?"
- **Success threshold:** All 5 schemas stable. At most 1 "unknown" with a named contact to chase.

---

## 🟠 Medium Impact, Medium Risk — Test if capacity allows

Worth validating but not blocking. Run alongside UAT sessions if bandwidth permits.

| Assumption | What it affects | Suggested test |
|---|---|---|
| A4 — Officers want cross-system status in one place | Dashboard UX priority and depth | Fake door tab click rate (Exp 3b) already covers this |
| A3 — Pre-fill reduces time net (no correction overhead) | Whether pre-fill is a net positive | Observation during Wizard of Oz sessions (Exp 2a) |
| A7 — Officers trust pre-filled data enough to submit | Pre-fill adoption rate | Observation during Exp 2a; secondary signal |
| B2 — Officers engage with the pre-fill confirmation card (don't dismiss) | Whether the card UX is worth the friction | Prototype test (Exp 2b), combined with Exp 1b |

---

## 🟢 Low Impact / Low Risk — Defer or build and monitor

| Assumption | Rationale |
|---|---|
| A6 — Single "Apply" CTA reduces confusion | Industry-standard pattern. Confidence high. Build it, monitor for confusion signals post-launch. |
| A8 — Officers will find and return to saved drafts | Depends on A5 first. If abandonment isn't real, draft save isn't built. Moot until A5 is resolved. |
| A15 — Hiring managers will use the CareerCompass profile handoff | Hiring manager behaviour is out of scope for R1 OKR measurement. Deprioritise. |

---

## ⛔ Escalate — Don't design around

**A13 — Storing draft application data will clear government data classification and security review**

- **Why escalate:** This isn't an experiment — it's a compliance question with a binary answer. If draft data is classified at a level that requires additional controls, building the feature and then hitting the security review wall is the worst outcome.
- **Action:** Michelle to raise with Adrian and the security review contact in Sprint 2 W2. Ask: what data classification applies to in-progress application form data? What controls are required? Get written confirmation before draft save goes into R1 backlog.
- **If blocked:** Descope save-and-resume from R1. Offer "email yourself a reminder" as a lightweight alternative. Flag as R2.

---

## Priority order — what to act on, and when

> **Revised timeline:** R1 design locks Aug-Sep '26. R1 backlog grooming Sep '26. R1 build Oct '26. Any experiment meant to *inform* R1 design must complete by end of Aug '26 — not UAT. UAT (Sep-Oct '26) overlaps with R1 build start and is too late to change design direction.

| Priority | Assumption | Owner | Deadline | Revised from | Status |
|---|---|---|---|---|---|
| 1 | A14 — Vendor API access agreements | Michelle → Adrian | Sprint 2 W2 | — | ⚠️ Not started |
| 2 | A13 — Draft data security classification | Michelle → Security | Sprint 2 W2 | — | ⚠️ Not started |
| 3 | B1 — Form complexity audit (drawer fit) | Pow Hwee + Amber | Sprint 3 | — | ⚠️ Not started |
| 4 | A9/A10 — OTG + C@G status API spike | Pow Hwee | Sprint 4–5 | — | ⚠️ Not started |
| 5 | A11 + B4 — Schema mapping + stability | Pow Hwee | Sprint 4–5 | — | ⚠️ Not started |
| 6 | A12 — FE capacity estimate for 5 types | Pow Hwee + Thomas | Sprint 4–5 | — | ⚠️ Not started |
| 7 | A5 — Abandonment funnel (instrument at MVP) | Leo/Thomas | Sprint 5 | — | ⚠️ Not started |
| 8 | A2 — Wizard of Oz pre-fill | Michelle + Pow Hwee | Sprint 6–7 (Jul–Aug) | ~~UAT Sep-Oct~~ | ⚠️ Not started |
| 9 | A5 — Observed STIP task test | Michelle | Sprint 6–7 (Jul–Aug) | ~~UAT Sep-Oct~~ | ⚠️ Not started |
| 10 | B2, A3, A7 — Pre-fill card + trust signals | Amber + Michelle | Sprint 6–7 (Jul–Aug) | ~~UAT Sep-Oct~~ | ⚠️ Not started |
| 11 | A1 — Apply CTR + fake door tab | Leo/Thomas | MVP launch (Oct) | — | ⚠️ Not started — see note |

> **⚠️ A1 timing gap:** Apply CTR and fake door data only become available at MVP launch (Oct '26) — the same month R1 build starts. This means A1 (channel choice) **cannot be validated before R1 build begins.** R1 is proceeding as a bet that officers will choose CareerCompass. Mitigate by: (a) treating the fake door as an in-flight signal that can accelerate or de-scope R1 features, not a go/no-go gate; (b) running one qualitative question during Sprint 6-7 research sessions — "When you apply for an OTG opportunity today, where do you go first?"

---

## Finding research participants before UAT

Experiments 8-10 move to Sprint 6-7 (Jul-Aug '26) — before the official UAT cohort is available. Options for officer participants:

1. **Internal PSD staff** — PSD officers are themselves public service officers and can act as proxy testers for discovery sessions (not UAT acceptance). Quickest to recruit.
2. **BO network** — ask Jacky or Xian Zhang to identify 5-8 willing officers from their agencies for a 30-minute research session. Frame as "help shape the product."
3. **Existing OTG users** — PSD Ops may have a list of active OTG users willing to participate in research ahead of formal UAT.

Frame these as **research sessions** (not UAT) — lower burden to recruit, no formal sign-off needed.

---

## The so-what

The R1 Oct '26 start date compresses everything. What looked like a comfortable sequence — spikes in Sprint 4-5, officer tests in UAT, backlog grooming in Nov — is actually a race.

R1 design must lock in Aug-Sep '26. That means officer-facing experiments (pre-fill Wizard of Oz, STIP task test, prototype usability) need to run in Jul-Aug '26 with proxy research participants, not wait for the official UAT cohort. Amber can't start designing until B1 (form complexity audit) is done in Sprint 3, and she can't lock direction until those Jul-Aug sessions are complete.

Two things are still actionable this sprint and cannot wait: A14 (vendor API agreements) and A13 (draft data security). Both are external conversations that take weeks — raise with Adrian in the next 1:1 or BO sync.

The one genuine gap that can't be closed before R1 starts is A1 (channel choice). Accept the risk, treat fake door data as an in-flight signal, and plan a scope adjustment mechanism if officers don't shift channels in the first 4 weeks post-MVP.

---

*Living document — update status column as experiments run. Log outcomes in `../../PM-OS/outputs/decisions/2026-05-29-W22-decisions-log.md`.*
