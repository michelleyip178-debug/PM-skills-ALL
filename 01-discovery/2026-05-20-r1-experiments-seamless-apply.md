# Experiments: R1 — Seamless Application (Friction Reduction)

**Date:** 2026-05-20
**Product:** CareerCompass (OTEP)
**Source ideas:** `2026-05-20-r1-brainstorm-seamless-apply.md`
**Principle:** Measure actual behaviour, not opinion. Test the riskiest assumption first. Maximum learning, minimum build.

---

## Summary table

| # | Idea | Experiment | Method | Metric | Success threshold | Effort | When |
|---|---|---|---|---|---|---|---|
| 1a | Application drawer | Form complexity audit | Schema analysis + design sketch | Field count + drawer fit | All core types fit in drawer at 375px | Low | Sprint 3 |
| 1b | Application drawer | Prototype usability test | Figma clickthrough + task observation | Task completion + reference behaviour | ≥4/5 complete without leaving drawer | Medium | UAT (Sep–Oct) |
| 2a | Pre-fill confirmation card | Wizard of Oz pre-fill | Manual pre-fill with real profile data | Correction rate + trust signals | Correction rate <25% across sampled fields | Medium | UAT (Sep–Oct) |
| 2b | Pre-fill confirmation card | Card engagement prototype test | Figma prototype with card intercept | Dismiss rate vs. read + edit | <50% dismissal; ≥30% make at least one edit | Low | UAT (Sep–Oct) |
| 3a | State machine + dashboard | API/event granularity spike | Technical investigation | Status event types confirmed | ≥3 status states available from OTG + C@G | Medium | Sprint 4–5 |
| 3b | State machine + dashboard | My Applications fake door | Stub tab in MVP with "coming soon" | Click rate on tab | ≥20% of active sessions click the tab | Low | MVP launch (Oct) |
| 4a | Progress stepper + draft save | Observed STIP task test | Moderated usability session | Time-on-task + drop-off moments | ≥3/5 officers pause or express intent to stop | Low | UAT (Sep–Oct) |
| 4b | Progress stepper + draft save | MVP abandonment funnel | Analytics instrumentation | Apply click → FormSG submission gap | Abandonment >40% validates draft save need | Low | Sprint 5 onward |
| 5a | Form schema registry | Schema audit + stability check | Document all 5 schemas + ask about planned changes | Schema stability over 6 months | All schemas stable; no planned changes in R1 window | Low | Sprint 4–5 |

---

## Experiment detail

### Idea #1 — In-context application drawer

**The assumption:** Application forms for STIP, GIG, SJR, C@G, and Internal Jobs are simple enough to render inside a drawer — they're not so long or multi-sectioned that they need a full-page experience.

---

**Experiment 1a — Form complexity audit**

*The drawer is the right container only if the form fits. Find out before designing.*

- **Method:** Pow Hwee retrieves the field schemas for all 5 application types from OTG and C@G. Amber sketches the drawer at actual mobile-first width (375px). Count: total fields per form, number of multi-line fields, number of sections, scroll depth estimate.
- **Metric:** Field count per form type; estimated scroll depth inside drawer; binary fit/no-fit judgement per type.
- **Success threshold:** All core types (STIP + GIG at minimum) fit in the drawer without exceeding 3 full scrolls on a standard phone screen.
- **What happens if it fails:** Drawer is the wrong container for STIP. Switch design approach to a full-page in-app form (still within CareerCompass — the "no redirect" promise holds, but the UX pattern changes). SJR and shorter types may still use the drawer.
- **Effort:** Low — half a day for Pow Hwee (schema retrieval) + half a day for Amber (sketch).
- **When:** Sprint 3 (before Amber starts R1 design).
- **Owner:** Pow Hwee + Amber.

---

**Experiment 1b — Prototype usability test**

*Even if the form fits, will officers actually use the opportunity description while applying — the main UX promise of the drawer?*

- **Method:** Amber builds a Figma clickthrough: detail page with a "Apply" CTA that opens a drawer, a short mock STIP form prefilled with sample data. Run a 20-minute moderated task session with 5 UAT officers. Task: "You want to apply for this opportunity. Go ahead." Observe: do they read the opportunity panel? Do they complete without wanting to close the drawer and go back?
- **Metric:** Task completion rate; number of participants who reference the opportunity description mid-form; number who express confusion or try to close/escape the drawer.
- **Success threshold:** ≥4 of 5 officers complete the task without trying to leave the drawer. At least 2 reference the opportunity panel unprompted.
- **What happens if it fails:** Officers don't actually refer to the description mid-apply — the dual-panel value is overstated. Simplify to full-page apply. Reduce scope.
- **Effort:** Medium — 1 day Amber (prototype) + half day Michelle (sessions).
- **When:** UAT (Sep–Oct '26) — run alongside auth and listing testing.
- **Owner:** Amber (prototype), Michelle (facilitation).

---

### Idea #2 — One-tap pre-fill confirmation card

**The assumption:** Officers will engage with the card (not dismiss it) and the pre-filled data will be accurate enough that correction rate is low — making pre-fill a time-saver, not a liability.

---

**Experiment 2a — Wizard of Oz pre-fill**

*Before building the pre-fill engine, manually pre-fill a form with a real officer's profile data and observe whether it helps or hurts.*

- **Method:** During UAT, for 5 officers: retrieve their CareerCompass profile data manually. Pre-populate a mock STIP form with their actual data before the session starts. Present it to them as "CareerCompass has filled this in from your profile." Observe: how long they spend reviewing, what they correct, what reactions they have. Do not tell them it was manual.
- **Metric:** Correction rate (fields changed out of total pre-filled fields); review time; qualitative trust signals ("this is wrong" vs. "oh that's helpful").
- **Success threshold:** Correction rate < 25% across sampled fields. At least 3 of 5 officers express a positive reaction to the pre-fill concept.
- **What happens if it fails:** Correction rate >50% means profile data at UAT is too incomplete/stale to pre-fill reliably. Deprioritise smart pre-fill; shift R1 focus to profile enrichment first.
- **Effort:** Medium — requires pulling real profile data and manually mapping to form fields. One afternoon per session set.
- **When:** UAT (Sep–Oct '26).
- **Owner:** Michelle (setup + facilitation), Pow Hwee (data pull).

---

**Experiment 2b — Card engagement prototype test**

*Will officers actually engage with the confirmation card, or dismiss it as friction?*

- **Method:** Add the pre-fill confirmation card as a step in the Experiment 1b prototype. After clicking Apply, officer sees: "Here's what we'd fill in from your profile" with 3–4 pre-filled fields shown. CTA: "Looks good" or "Edit." Observe dismiss vs. engage behaviour. Time how long officers spend on the card before proceeding.
- **Metric:** Dismissal rate (clicking through without reading); edit rate (at least one field changed); average time on card.
- **Success threshold:** Fewer than 50% dismiss without engaging. At least 30% make at least one edit (showing they read it). Average time on card > 5 seconds.
- **What happens if it fails:** Officers dismiss the card reflexively → it adds friction, not trust. Simplify to silent pre-fill with an inline "Edit" link per field instead of a gate-style confirmation.
- **Effort:** Low — add one screen to Experiment 1b prototype.
- **When:** UAT (Sep–Oct '26), combined with Experiment 1b.
- **Owner:** Amber.

---

### Idea #3 — Application state machine + My Applications dashboard

**The assumption:** OTG and C@G expose application status at meaningful granularity (more than just "submitted") — enough to power a useful dashboard with at least 3 distinct states.

---

**Experiment 3a — API / event granularity spike**

*If the status data doesn't exist at the source, the dashboard is smoke and mirrors. Find out now, not at R1 build.*

- **Method:** Pow Hwee investigates OTG's event or webhook API and C@G's status API. Key questions: what status states are available (e.g. Submitted / Under Review / Shortlisted / Outcome)? What is the typical event latency? Is the data available per-officer or aggregate only? Can it be polled, or does it require a push webhook? Document findings as an API contract stub.
- **Metric:** Number of distinct status states available from each system; confirmed latency; access model (push vs. pull).
- **Success threshold:** OTG provides ≥3 distinct status states. C@G provides ≥2. Both accessible within a 24-hour latency window. At least one system supports push webhooks.
- **What happens if it fails:** Only "submitted" is available → the dashboard is just a submission log. Deprioritise the status dashboard to R2; replace with a simple "Application submitted on [date]" confirmation. Raise as a scope change with Jacky/Xian Zhang.
- **Effort:** Medium — 2–3 days Pow Hwee, one stakeholder call with OTG/C@G integration contacts.
- **When:** Sprint 4–5 (Jun–Jul '26). Gate: must resolve before R1 design lockdown.
- **Owner:** Pow Hwee.

---

**Experiment 3b — My Applications fake door**

*Before building the dashboard, test whether officers actually want to track applications in CareerCompass — or whether they'd go to OTG directly.*

- **Method:** In MVP, add a "My Applications" tab in the navigation. Clicking it shows a "Coming soon — we're building this for you" holding page with a brief description and an optional "Notify me" CTA. Track click rate on the tab across active sessions in the first 2 weeks post-MVP launch.
- **Metric:** % of active sessions in which "My Applications" tab is clicked; % of those who click "Notify me."
- **Success threshold:** ≥20% of active sessions click the tab at least once. This signals genuine demand for in-platform status tracking.
- **What happens if it fails:** <5% click rate → officers either don't care about tracking status in CareerCompass, or don't know the tab is there. Investigate which before investing in R1 dashboard build.
- **Effort:** Low — one nav item and one static holding page. Thomas can build in half a day.
- **When:** MVP launch (Oct '26), first 2 weeks.
- **Owner:** Thomas (build), Michelle (review metrics).
- **Risk note:** This is a fake door — it promises a feature that doesn't exist yet. Keep copy honest: "coming soon" framing, not a confirmed commitment. Do not let the "Notify me" list go unactioned.

---

### Idea #4 — Progress stepper with save-and-resume

**The assumption:** Officers genuinely abandon STIP applications mid-way at meaningful rates — making draft save worth the build complexity.

---

**Experiment 4a — Observed STIP task test**

*Put a real STIP application form in front of officers during UAT and watch what happens.*

- **Method:** During UAT, give 5 officers a sample STIP form (not pre-filled — blank, as in MVP baseline) and ask them to complete it as they would in real life. Observe: where do they pause? Where do they say "I'd need to check something"? Where do they express a desire to stop and come back? Note the fields that cause the most hesitation.
- **Metric:** Number of officers who pause for >30 seconds; number who express intent to stop mid-form; specific fields/sections identified as blockers.
- **Success threshold:** ≥3 of 5 officers pause meaningfully or express intent to abandon before completing. At least 2 cite a specific field they'd need to look up.
- **What happens if it fails:** Officers complete STIP forms without pause → abandonment is not a real friction. Deprioritise save-and-resume; simplify to a single-page form without stepper complexity.
- **Effort:** Low — no build required. Half a day for Michelle to run and synthesise.
- **When:** UAT (Sep–Oct '26).
- **Owner:** Michelle.

---

**Experiment 4b — MVP abandonment funnel**

*Quantify how many officers click Apply but never complete the application — the structural evidence for whether draft save is needed.*

- **Method:** Instrument the MVP apply flow with two events: `apply_cta_clicked` (fired when officer clicks Apply on detail page) and `application_submitted` (fired when FormSG webhook receipt is confirmed for that officer). Compare counts over the first 4 weeks post-launch. Gap = abandonment proxy. Segment by opportunity type (STIP vs. GIG vs. C@G).
- **Metric:** Abandonment rate = (apply_cta_clicked − application_submitted) / apply_cta_clicked, per opportunity type.
- **Success threshold:** Abandonment rate > 40% for STIP → save-and-resume validated as R1 priority. Rate < 20% across all types → deprioritise to R2.
- **What happens at the threshold boundary (20–40%):** Investigate qualitatively — is drop-off due to redirect friction (solved by R1 drawer) or genuine mid-form abandonment (requiring draft save)? Don't build draft save on ambiguous data.
- **Effort:** Low — analytics event hooks needed for OKR baseline anyway. Add opportunity type as an event property.
- **When:** Sprint 5 onward (Jul '26); first data available ~2 weeks post-MVP launch.
- **Owner:** Leo/Thomas (instrumentation), Michelle (analysis).

---

### Idea #5 — Form schema registry

**The assumption:** All 5 application form schemas (STIP, GIG, SJR, C@G, Internal) are stable enough to register now — no planned breaking changes during the R1 build window (Oct '26 – Jan '27).

---

**Experiment 5a — Schema audit and stability check**

*Build the registry on schemas that are about to change and you'll rebuild the entire foundation mid-sprint.*

- **Method:** Pow Hwee retrieves and documents the full field schemas for all 5 application types from OTG and C@G. For each schema: field name, type, required/optional, validation rule, last modified date. Then: ask the OTG and C@G integration contacts directly — are there any planned schema changes in the next 9 months? Document as a schema stability matrix.
- **Metric:** Schema completeness (all 5 documented); stability flag per type (stable / change planned / unknown).
- **Success threshold:** All 5 schemas documented. No planned breaking changes flagged for the R1 build window. At most 1 "unknown" — with a named contact to follow up.
- **What happens if it fails:** ≥2 schemas have planned changes → delay schema registry build until changes land. Sequence the registry as a Sprint 2 R1 story (not Sprint 1 R1). Reduces blast radius if schemas shift mid-build.
- **Effort:** Low-medium — 1 day Pow Hwee (documentation) + one stakeholder check-in. Can be combined with Experiment 3a spike.
- **When:** Sprint 4–5 (Jun–Jul '26). Run alongside the API/event granularity spike.
- **Owner:** Pow Hwee.

---

## Sequencing guidance

> **Timeline revised 2026-05-20:** R1 build starts Oct '26. R1 design locks Aug-Sep '26. R1 backlog grooming Sep '26. Experiments originally planned for UAT (Sep-Oct) are too late to shape design — moved to Sprint 6-7 (Jul-Aug '26) with proxy research participants.

Run experiments in this order. Later experiments depend on earlier ones.

```
Sprint 3        Exp 1a (form complexity audit) ──────────────────────────── shapes drawer vs. full-page decision
                                                                              ↓
Sprint 4–5      Exp 3a (API spike) + Exp 5a (schema audit) ─────── run together; Pow Hwee owns both
Sprint 5+       Exp 4b (MVP abandonment funnel) ──────────────── instrumented now; first data Jul '26

Sprint 6–7      Exp 1b + 2b (prototype usability, combined) ────── ⚠️ MOVED from UAT — run with proxy participants
(Jul–Aug '26)   Exp 2a (Wizard of Oz pre-fill) ──────────────────── ⚠️ MOVED from UAT — separate session
                Exp 4a (observed STIP task) ─────────────────────── ⚠️ MOVED from UAT — separate session
                                                                              ↓
Sep '26         R1 backlog groomed using all experiment outputs above

MVP launch      Exp 3b (fake door tab) ─────────────────────────── Oct '26 — in-flight signal only,
(Oct '26)                                                            not a pre-build gate for R1
```

**Finding participants for Sprint 6-7 sessions:** UAT cohort isn't available yet. Use internal PSD staff as proxy testers, or ask Jacky/Xian Zhang to identify 5-8 willing officers from their agencies. Frame as a research session, not UAT — lower friction to recruit.

---

## Decision gates

| Gate | Experiment(s) | Decision | Deadline |
|---|---|---|---|
| Before Amber starts R1 design | 1a | Drawer vs. full-page form | Sprint 3 |
| Before R1 backlog grooming | 3a, 4b, 5a, 1b, 2a, 2b, 4a | Scope status dashboard; draft save; pre-fill approach; schema registry | Sep '26 |
| In-flight during R1 build | 3b | Channel choice signal — adjust R1 scope if apply CTR < 10% | Nov '26 |

---

*Source: `2026-05-20-r1-brainstorm-seamless-apply.md` + `2026-05-20-r1-discovery-plan.md`*
