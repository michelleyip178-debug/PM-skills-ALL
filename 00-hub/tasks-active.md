# Active Tasks

Current sprint: **Sprint 3 active (started Tue 2 Jun). Sprint 2 closed — carry-over QA/In-Progress pulled into S3.**
Jira sync 2026-06-02 (live): **Sprint 3:** carry-over QA in flight (finish first), new-scope stories in Backlog. New: OTEP-358 (Michelle, nil-date OTG spike), OTEP-361 (Pow Hwee, ADR forum). **OTEP-129 now on the S3 board, split into OTEP-362 (backend) + OTEP-363 (UI).** · **Sprint 2 (closed) In Progress carried to S3:** OTEP-85, OTEP-322 (Rathika) · **In QA (carried):** OTEP-128, OTEP-170, OTEP-268, OTEP-314, OTEP-320, OTEP-325/326, OTEP-327, OTEP-332, OTEP-334, OTEP-303 · **Done:** OTEP-191, OTEP-267, OTEP-313 (Léo), OTEP-252, OTEP-194, OTEP-193, OTEP-288, OTEP-296.

Story pipeline tracking lives in [sprint-checklists.md](../04-ceremonies/sprint-checklists.md). (Old story-readiness.md archived 2026-05-15.)

---

## This Week's Focus

**Theme:** Sprint 3 in flight (started 2 Jun) — finish carried-over QA, then new-scope pickup. Key gates: R1 capacity + ATS-fork decisions (this session's work), CSC SSO feasibility, design-lock confirmation. *(Prior week's Sprint 2-close theme retired 2026-06-02.)*

---

## In Progress

**Engineering (Jira — live 2026-06-02):**

*Sprint 3 (all Backlog — no pickup yet, Day 1):* OTEP-86/317 (filters), OTEP-87/88/89 (C@G), OTEP-319 (FormSG redirect), OTEP-305 (login/logout), OTEP-192/348 (OTG ingestion), OTEP-324 (token rotation, Thomas), OTEP-349/351 (spikes), OTEP-350 (WOG AD, Fabian), OTEP-352 (POCDEX code table, Pow Hwee), **OTEP-358 (nil-date OTG spike, Michelle)**, OTEP-361 (ADR forum, Pow Hwee).

*Carried-over In Progress (live 2026-06-02):* OTEP-85 (cards w/ real OTG data), OTEP-322 (Rathika, Playwright).

*Carried-over In QA:* OTEP-128 (detail page), OTEP-268 (empty/error parent), OTEP-170 (base layout), OTEP-314 (detail page), OTEP-327 (detail w/ design system), OTEP-320 (replace mock endpoint), OTEP-325/326 (empty/error states), OTEP-303 (POCDEX field check), OTEP-332 (reference data repo), OTEP-334 (backend detail endpoint).

*Newly Done since 05-29:* OTEP-267 (pagination), OTEP-313 (Léo, raw ingest).

---

## Up Next

> **LNO re-sort applied 2026-06-02** ([analysis](../../../PM-OS/outputs/analyses/2026-06-02-lno-prioritization.md)). This week's **Leverage** (do deeply): feed Adrian the R1 resource ask · drive R1 design alignment w/ designers · force the ATS fork (C1) · CSC SSO feasibility · finish WOG Auth metrics. Overhead items below struck/delegated/deferred to protect that time.

> **BAU / standing tasks — prioritised** (linked from daily plans):
> - **🔴 P1 (this week, unblocks others):** WOG AD response — Adrian (#26) · CSC SSO + ref data — Imelda (#18/#30)
> - **🟠 P2 (batch soon):** Jira housekeeping (POCDEX epic, OTEP-128 AC, placeholder stories) · DQ issue — Daryll (#33) · ~~dependency map~~ → delegated to Pow Hwee
> - **🟡 P3 (whenever):** Diana loop-in + stakeholder file · ~~OKR doc → NotebookLM~~ (killed) · clean inbox (15-min timebox)
> - **🗓️ Deferred out of June:** Cybersecurity quiz (Dec) · PIM risk assessment (post-feature-freeze)

- [ ] ~~**Email DDs on PSC — send today (Fri 29 May)**~~ — ⚠️ **STALE (LNO 2026-06-02): deadline 4 days past. Verify it was sent, then close. If not sent, it's likely moot.**
- [ ] **Prepare Jobelle handover** — Jobelle joins 3 Jun. Step 1: share Phoebe's copy first. Step 2: share Daniel's handover after 30–60 days (i.e. ~3 Jul–3 Aug).
- [ ] **Follow up on session-notes test cases** — no hard due date; follow up when opportunity arises. **DEFER (LNO 2026-06-02): "whenever" = not June.**
- [ ] **Revert to Clarissa by 4 Jun — Malaysian NRIC + downstream OTG impact** — Clarissa needs confirmation by Thu 4 Jun. Assess downstream OTG impact before responding. **Ties to Cumulus Phase 3 (open-item #36): OTG must be production-ready for Malaysia ID changes by 6 Jul 2026.** The 4 Jun reply is the near-term gate; 6 Jul is the production deadline.
- [ ] **Design PostHog OKR + metric instrumentation** — Rama scheduling a call w/c 2 Jun to work through event taxonomy together. Attend and define metric definitions to measure OTEP OKRs and North Star. *(Squad-Sync 2026-05-26; updated 2026-05-29)*
- [x] **Send post-Design Review async follow-up to Xian Zhang + Jacky** — sent 2026-05-28. ✅
- [ ] **Update FormSG PRD** — remove pre-fill from MVP scope; note R1 direction (native in-OTEP application form). This week, before next grooming. *(Squad-Sync 2026-05-26)*
- [ ] **Update OTEP-130 in Jira** — re-scope to MVP: basic FormSG redirect + webhook only, no pre-fill. This week. *(Squad-Sync 2026-05-26)*
- [ ] **Check in with Pathfinder team on current demo state** — what can be shown to users right now? Get the URL and share with the team for early checks. *(Squad-Sync 2026-05-26)*
- [ ] **Run through with Amber: design-vs-implementation check** — verify the implemented UI matches Amber's intended design. Bring any gaps back to standup before sprint ends. Note Amber also has user testing by end of week — flag potential capacity conflict. *(Squad-Sync 2026-05-26)*
- [x] ~~**Check with Acacia on POCDEX data model familiarity**~~ — **Cancelled 2026-06-02.** No longer needed.
- [ ] **Attend/track Thursday WD×DO job family model discussion** — 29 May 2026. POCDEX requirements depend on its outcome. Capture any implications for Daryll session. *(Pow Hwee adhoc 2026-05-25)*
- [ ] **Write user story: opportunity matching using competencies** — not yet in backlog. Flagged by Pow Hwee. For Sprint 3 planning. *(Pow Hwee adhoc 2026-05-25)*
- [ ] **Research in-platform application form vs FormSG** — Pow Hwee proposing Sprint 3 spike; Michelle to research pilot agency customisation needs before spike scoping. Before Sprint 3 planning. *(Pow Hwee adhoc 2026-05-25)*
- [ ] **WOG Auth success metrics** — committed to Adrian this week. Grounded in Dec '26 OKR baselines from BO deck. Start Thursday at latest. *(daily plan 2026-05-26)*
- [ ] **OTEP-87 + OTEP-318 AC alignment** — needed before Sprint 3 grooming. If design review didn't cover it, schedule async with Amber. *(daily plan 2026-05-26)*
- [ ] **Drive R1 design alignment + discovery WITH the designers** — R1 deep-dive praised at PM Weekly, but the ask is to move it from PM-solo to a real cross-functional effort. Get Amber (+ Michelle Chen's design capacity if it lands) aligned on the three R1 surfaces: apply, agency-creation, manager dashboard. Before R1 grooming. *(PM Weekly 2026-06-02)*
- [ ] **Feed Adrian the specific R1 resource ask** — concrete framing for his Michelle Chen conversation: three net-new R1 builds (native apply + native creation + the seam), one FE dev. Reference the R1 capacity reality-check. This week. *(PM Weekly 2026-06-02)*
- [ ] **CSC SSO technical-feasibility deep-dive** — with Pow Hwee/Fabian; surface why there's an intentional re-login. Feeds open-item #30. Before Sprint 5 (~2 Jul). *(PM Weekly 2026-06-02)*
- [ ] **Create the new "POCDEX Integration" Epic in Jira** and move OTEP-271, 203, 202, 127 under it
- [ ] **Follow up with Daryll/Pow Hwee on raising DQ issue** for OTEP code table in UAT read replica
- [ ] **Work out next steps for WOG AD onboarding with Fabian and Pow Hwee** — OTEP-350 (Onboard WOG AD, Fabian Peh) now in Sprint 3; coordinate next steps.
- [ ] **Complete Cybersecurity quiz by 2026-12-31** — **DEFER out of June (LNO 2026-06-02): 7 months out, not on the MVP/R1 spine.**
- [ ] **Map out dependencies in high-level Jira stories → `00-hub/risks.md`** — document cross-story dependency map. **→ DELEGATE to Pow Hwee (LNO 2026-06-02): he asked for it and owns the technical map; Michelle reviews, doesn't author.** *(captured 2026-05-21)*
- [x] **Ping Adrian — WOG AD onboarding**: Domain is `careercompass.gov.sg`. Two asks: (1) COMET onboarding status — is ESG/OTEP onboarded? (2) Approval to test against WOG AD Prod. ✅ Pinged 2026-05-21. Waiting on response. (#26)
- [ ] **Sync with Imelda (OTEP-Core Squad PM)** — four asks: (1) Who owns passing documents to CSC after WOG AD completes — her squad, Pathfinder, or joint? (#30) (2) How does OTEP consume job family, job function, agency, competency data from her squad — API? file? push? (#18) (3) Schema + field names for that reference data? (4) Timeline — when is it available for OTEP to integrate? (#18)
- [ ] **Schedule POCDEX planning session with Daryll** — POCDEX team lead. Must happen before Sprint 4 planning. Loop Pow Hwee in. (#31)
- [ ] **Create high-level dependency stories** (Pow Hwee's ask from Teams thread) — one placeholder story each for POCDEX go-live prep (#31), WOG AD onboarding (#26), CSC SSO (#30). No ACs yet — titles and sprint-window targets in Jira.
- [x] **[PM action — #28] Confirm OTEP-85 visibility rule** — resolved 2026-05-19: `closing_date > today`; "Closing soon" badge (≤7 days) is OTEP-129's
- [x] **[PM action — #29] Define OTEP-289 ACs, timebox, expected outcome** — resolved 2026-05-19: 2-day timebox, written recommendation output
- [ ] **[PM action] Clean OTEP-128 AC** — remove "This opportunity is closed" notice AC from OTEP-128 (it belongs to OTEP-129).
- [ ] Loop Diana into opportunities decisions going forward (Jace's call, PM Weekly 11 May); add `06-skills-and-decisions/stakeholders/people/diana.md`
- [ ] ~~Load Adrian's OKR doc into NotebookLM~~ — **KILL (LNO 2026-06-02): it's already `06-skills-and-decisions/otep-roadmap-okrs-2627.md`. No action.**
- [ ] Clarify the "OTG test cases — session notes co-innovation" request, then route to `projects/otg-ops/task-log.md`
- [ ] **Conduct PIM risk assessment (OTG ops)** — scope to the no-PIM scenario: identify worst-case damage if privileged accounts are abused, then submit residual risk for formal acceptance. **DEFER out of June (LNO 2026-06-02): important but not on the MVP/R1 critical spine; revisit post-feature-freeze.** *(captured 2026-05-20)*
- [ ] Clean up email inbox *(captured 2026-05-20)*

---

## Waiting On

> Reconciled against live Jira + open-items 2026-06-02. Resolved/active-now rows struck through.

| Item | Waiting for | Since | Next action |
|------|-------------|-------|-------------|
| ~~OTG file import (OTEP-192/193)~~ | Pow Hwee | May 4 | ✅ **Moved to active work 2026-06-02** — OTEP-193 Done; OTEP-192 now in Sprint 3 Backlog (active build, no longer a "waiting on"). Tracked in sprint-status. |
| POCDEX account creation (OTEP-72) | — | May 4 | Live: OTEP-72 "New Officer account creation" still Backlog, unassigned. Confirm push mechanism works — bundle into Pow Hwee check-in. Still open. |
| ~~`formsg_url` field (#2)~~ | ~~Rama + PSD Ops~~ | May 4 | ✅ **RESOLVED 2026-05-21** — confirmed present for Internal Jobs/STIPs/Gigs, SJRs excluded. US-18 → OTEP-319 unblocked. |
| Auth edge-cases (OTEP-110, WOG-04/05/06) | Pow Hwee / Leo | May 11 | Live: OTEP-110 "Login fail using WOG AD" now in Sprint 3 Backlog (auth epic deferred to S4+ per 2026-05-21 decision). Stale "next action" removed — no longer pending a 26 May review. |
| POCDEX go-live support structure | Daryll (POCDEX team) | 2026-05-21 | Schedule planning session with Daryll (#31). **Still open.** |
| CSC SSO ownership decision | Imelda (Core Squad PM) | 2026-05-21 | Who passes documents to CSC after WOG AD completes? (#30). **Still open.** |
| ~~OTEP-276 design system spike~~ | Thomas | — | **Resolved** — OTEP-252 Done confirms Flagship/LifeSG adopted. No further action. |
| ~~QA review session with Rethna~~ | Michelle | May 13 | ✅ **Closed 2026-06-02** — Sprint 2 closing; AC-summary-doc prerequisite moot. No longer needed. |

---

## Done This Sprint

- [x] **OTEP-193** (Léo) — Design data model for Opportunities. Done ✅
- [x] **OTEP-288** (Léo) — Setup simple backend endpoint with in-memory list. Done ✅
- [x] **OTEP-296** (Michelle) — Prepare defined report format matching data model. Done ✅
- [x] **OTEP-252** — Setup design system in otep-web (Thomas). Done ✅
- [x] **OTEP-194** — FormSG integration discovery (Thomas). Done ✅
- [x] **OTG sync cadence decision** — D-016 logged 2026-05-29. One-time port only; no ongoing automated sync. See open-items #34.
- [x] **OTEP-190 — Simple auth through Keycloak** done (Fri 15 May, finalisation day). Closes the Sprint 1 auth goal.
- [ ] ~~OTEP-170 base listing page layout and navbar MR completed (May 15)~~ — **reverted to In Progress** (Jira shows In Progress; MR not yet merged)
- [x] OTEP-173 (Auth exploration), OTEP-183 (POCDEX spike), and OTEP-223 (OTG data preparation) completed (May 15)
- [x] Opportunity lifecycle (#17) resolved: date-driven, `closing_date > today` = visible. Pow Hwee agreed. (May 13)
- [x] Apply-flow decision routed from inbox + CLAUDE.md updated: SJR redirect dropped, Internal Jobs → FormSG (May 13)
- [x] US-18 story written (Apply via FormSG basic redirect — Internal Jobs, STIPs, Gigs) in otg-lifecycle.md (May 14)
- [x] Sprint 2 scope reshuffled: Listing → Detail end-to-end. OTEP-128 repurposed as detail page (written from scratch). OTEP-129 absorbed into OTEP-85. OTEP-86/US-05 deferred to Sprint 3. OTEP-268 sharpened with PM-mode decisions. All ACs written officer-perspective for contract-first approach. (May 14)
- [x] OTG ingestion architecture clarified: OTG = file import (Excel), C@G = API. Open item #11 resolved. (May 14)
- [x] 7 OTG field confirmations resolved in one pass (May 13): `eligibility` (not needed), `closing_date` (confirmed), `is_published` (doesn't exist — use `closing_date`), `reporting_line` (not in export), `developmental_outcome` (confirmed available), Secondment (SJR sub-type), SJR deep-link (#7, no longer needed)
- [x] Apply flow decision: FormSG for Internal Jobs, STIPs, Gigs only. SJR apply deferred to future release. US-19 dropped. (May 13)
- [x] Sprint 2 scope decided: 5 stories, OTG data only. Logged in decisions-log.md. (May 11)
- [x] Sprint 2 stories sharpened — OTEP-85, OTEP-86, OTEP-128, OTEP-129, US-05 in filters.md (May 11–13)
- [x] Sprint checklists file created (sprint-checklists.md) — per-sprint grooming readiness + DoR blockers (May 13)
- [x] Grooming briefs generated — internal squad groom (05-13), formal backlog grooming (05-14) (May 11–13)
- [x] Sprint plan brief generated (sprint-plan-brief-2026-05-14.md) (May 13)
- [x] Auth flow accepted for MVP — Adrian confirmed (May 12)
- [x] Programme plan adopted: 12 sprints, Go-Live Fri 16 Oct 2026 (May 12)
- [x] ~~Release 4 prioritised on opportunity creation & posting (May 12)~~ — **superseded 2026-06-02: creation moved to R1** (see decisions-log)
- [x] PRD updated with 5-group user story structure, timeline, scoping gaps, risks (May 11)
- [x] Scoping gaps tracker populated with 13 items (May 11)
- [x] Projects reorganised: otep-opportunities + otep-wog-ad-login merged into otep-mvp (May 11)
- [x] Full OS cleanup — stale references fixed across 8 files (May 11)
- [x] Competency match ratio descoped to R1 (May 8)
- [x] Align with Adrian on target launch date — resolved (May 12)
- [x] Review Amber's Hub UI + card designs — alignment check done
- [x] ~~Verify COMET onboarding with Imelda~~ — stale. COMET = Michelle → Adrian (#26). Imelda's scope = CSC SSO (#30).

---

*Updated: 2026-06-02 — stale-check + live Jira sync (Board 12541). Header refreshed: Sprint 2 CLOSED, Sprint 3 active with carry-overs; OTEP-129→362/363, OTEP-313 Done, OTEP-128/268 in QA. LNO re-sort applied. R4-creation entry marked superseded (creation→R1).*
