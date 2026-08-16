# Active Tasks

Current sprint: **Sprint 8 ACTIVE (11–24 Aug 2026) — final MVP dev sprint, no Sprint 9 buffer.** See [sprint-status.md](sprint-status.md) for the live-verified breakdown (Pathfinder Sprint 8: 73 issues — 3 To Do, 9 In Progress, 11 QA, 37 Done, 13 Backlog, as of 2026-08-17 jira pull; goal set in Jira: "Clean up defects from Phase 1 - UAT and enable Phase 2 - UAT on Ringfencing and Competency Matching.").
Sprint 3 final state (2026-06-12): ~23 Done, 9 in QA carry-in (85/86/89/128/192/268/305/317/319), 4 Backlog carry-in. Sprint goal near-met (filters + apply + deep-link all reached QA). Sprint 4 goal: complete, usable listing experience — search, filter, sort, data currency.

Story pipeline tracking lives in [sprint-checklists.md](../04-ceremonies/sprint-checklists.md). (Old story-readiness.md archived 2026-05-15.)

---

## This Week's Focus

**Theme:** Sprint 8 (11–24 Aug) is active and confirmed as the **final MVP dev sprint — no Sprint 9 buffer** (confirmed 2026-08-11). 73 issues: 37 Done, 9 In Progress, 11 QA, 3 To Do, 13 Backlog (live 2026-08-17). Sprint goal per Jira: clean up defects from Phase 1 UAT, enable Phase 2 UAT on Ringfencing and Competency Matching.

**What's actively in motion this sprint:** WOG AD login (OTEP-71, Léo — In Progress) and the two other WOG AD-adjacent tickets (OTEP-594 unassigned, In Progress; OTEP-331/110 unassigned, QA) are the sharpest open risk — dev-environment re-enable was confirmed working 2026-08-13, but prod/UAT confirmation has not landed and OTEP-71 is still In Progress, not Done, as of this pull. Per PM-OS's W33 weekly review, this status was unchanged across three consecutive named check-in days (13, 14 Aug) with no resolution — worth a direct escalation, not another status check.

**Carried-forward risks still open (per this stale-check against `open-items.md`/`risks.md`):** VAPT closure date conflict (16 Oct vs. 23 Oct, #39 — still unresolved; PS/DS 7-week-delay proposal is also still pending approval as of the W33 weekly review, likely supersedes this conflict entirely once resolved — needs a person to confirm, not a file edit); Huiting/Mark data-sharing approval (#55 — Data Sharing Form now confirmed locked/approved 2026-08-14, but ≥25 additional UAT scenarios and Day-2 support scoping remain open with no owner); POCDEX ETL/infra core-team questions (#31 — still outstanding). None of these are Sprint-8-build blockers directly, but WOG AD and the VAPT date conflict both threaten the feature-freeze gate (end of Sprint 8, 21 Aug) with no Sprint 9 to absorb slippage.

*(Updated 2026-08-17 — stale-check: rewrote this section from Sprint 7 framing [closed 9 Aug] to Sprint 8's actual state, a full week after Sprint 8 started. Cross-checked against PM-OS's 2026-08-14 W33 weekly review for the WOG AD/PS/DS/#55 status updates.)*

---

## In Progress

**Engineering (Jira — live 2026-08-17, Sprint 34622):**

*Pathfinder Sprint 8 In Progress (9) · In QA (11):* See [sprint-status.md](sprint-status.md) for the full, live-verified list.

*Pathfinder Sprint 8 To Do (3), Done (37), Backlog (13):* See sprint-status.md for full list.

*Core Sprint 8:* not synced this pass — see sprint-status.md's Core board notes for last full sync. Run `/jira-sync core` for a current Core board read.

---

## Up Next

> 🎯 **SPRINT 4 & 5 GATES (added 2026-06-04)** — what each sprint needs from *Michelle specifically*. Plan-of-record = [Pow Hwee's Confluence plan](https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2293796526/Planning+draft+for+sprint+3+and+after) (adopted 2026-06-04, native apply→R1). See [S4/S5 reconciliation](../../PM-OS/outputs/archive/2026-W23-Jun01-Jun07/analyses/2026-06-04-W23-adopt-powhwee-plan-reconciliation.md).
>
> **Sprint 4 (15–28 Jun) — goal agreed at planning 2026-06-11:**
> - [x] ~~**Lock the Sprint 4 goal**~~ — ✅ Done 2026-06-11. Goal: complete, usable listing experience — search, filter, sort, data currency.
> - [ ] **Fix OTEP-87 AC conflict in Jira** — FormSG vs C@G deep-link; Pow Hwee flagged ×2. Before S4 starts (Mon 15 Jun).
> - [ ] **Call OTEP-127 + OTEP-130 in-or-out** — both on S4 board but un-contracted. Flag "unknown" or pull.
> - [ ] **Reconcile S4 board to plan** — OTEP-71 flipped off again (no sprint, verify); spine (319/86/87/88/89/192) not pulled forward yet.
> - [ ] Sharpen OTEP-348 · confirm new-dev 70/30 FE split · C@G deep-link UX at design review.
>
> **Sprint 5 (28 Jun–12 Jul) — unblock 4 external gates (each is a Michelle→someone session; book this week — lead times):**
>
> - [x] ~~**WOG AD onboarding session — Fabian** (#26)~~ — no longer required (2026-06-09).
> - [x] ~~**POCDEX planning session — Daryll** (#31)~~ — no longer required (2026-06-09).
> - [x] ~~**CSC SSO requirements + ownership — #30**~~ — Resolved via email 2026-06-26 (technical feasibility confirmed, DLE testing targeted August). Approval/governance docs still TBC per open-items.md, but the requirements/ownership question itself is closed.
> - [x] ~~**Competency SSOT — Imelda** (#18)~~ — Fully resolved (sourcing + governance architecture settled at Dependencies Sync 2026-06-11, per open-items.md).
> - *Also: resolve OTEP-110 error-spec mismatch (#32) before auth grooms clean.*

> 📌 ~~**REVIEW TOMORROW (parked 2026-06-02):** Pow Hwee's **Sprint 3 Proposed Backlog** — review against sprint-status (50 issues, carry-over QA + new scope). Act/comment after reading.~~ **STALE — now Day 6 of Sprint 3. Board is live at 50 issues. Action moot.**

> **LNO re-sort applied 2026-06-02** ([analysis](../../PM-OS/outputs/archive/2026-W23-Jun01-Jun07/analyses/2026-06-02-W23-lno-prioritization.md)). This week's **Leverage** (do deeply): feed Adrian the R1 resource ask · drive R1 design alignment w/ designers · force the ATS fork (C1) · CSC SSO feasibility · finish WOG Auth metrics. Overhead items below struck/delegated/deferred to protect that time.

> **BAU / standing tasks — prioritised** (linked from daily plans):
> - **🔴 P1 (this week, unblocks others):** WOG AD response — Adrian (#26, open-items.md last updated 2026-06-30, blocked on Léo/Keycloak config with no ETA). ⚠️ **Flagged, not fixed:** open-items.md #26's last update is over a month old, but live Jira now shows OTEP-71 (WOG AD login) In Progress in Sprint 7 — worth a fresh status check with Léo/Adrian rather than assuming the June blocker still holds; this needs a person to confirm, not a file edit. (CSC SSO + ref data — Imelda, #18/#30 — pruned from this line: both confirmed resolved per open-items.md, no longer live BAU.)
> - **🟠 P2 (batch soon):** Jira housekeeping (POCDEX epic, OTEP-128 AC, placeholder stories) · DQ issue — Daryll (#33) · ~~dependency map~~ → delegated to Pow Hwee
> - **🟡 P3 (whenever):** Diana loop-in + stakeholder file · ~~OKR doc → NotebookLM~~ (killed) · clean inbox (15-min timebox)
> - **🗓️ Deferred out of June:** Cybersecurity quiz (Dec) · PIM risk assessment (post-feature-freeze)

- [x] **Send ARK request email for Jobelle** — ✅ Done (confirmed 2026-06-19).
- [x] **Review monthly progress report for OTG** — ~~due before Wed 10 Jun~~ **Delegated to Jobelle 2026-06-17.** Jobelle to own going forward.
- [x] **Set up Working Level deck for WD's update** — ✅ Done 2026-06-08.
- [ ] ~~**Email DDs on PSC — send today (Fri 29 May)**~~ — ⚠️ **STALE (LNO 2026-06-02): deadline 4 days past. Verify it was sent, then close. If not sent, it's likely moot.**
- [x] **Prepare Jobelle handover** — ✅ Complete. Jobelle operating independently as of 2026-06-26. Full 12-session 4-week plan delivered.
- [x] **Follow up on session-notes test cases** — ✅ Done 2026-06-02.
- [x] **Revert to Clarissa by 4 Jun — Malaysian NRIC + downstream OTG impact** — ✅ Done 2026-06-02. **Note:** Cumulus Phase 3 (open-item #36) production deadline (OTG ready for Malaysia ID by 6 Jul 2026) still stands — the 4 Jun reply was the near-term gate only.
- [ ] **Design PostHog OKR + metric instrumentation** — Rama scheduling a call w/c 2 Jun to work through event taxonomy together. Attend and define metric definitions to measure OTEP OKRs and North Star. *(Squad-Sync 2026-05-26; updated 2026-05-29)*
- [x] **Send post-Design Review async follow-up to Xian Zhang + Jacky** — sent 2026-05-28. ✅
- [x] ~~**Update FormSG PRD**~~ — **Dropped 2026-06-17. No longer required.** Pre-fill already deferred (decisions-log I-013); PRD update not needed.
- [x] ~~**Update OTEP-130 in Jira**~~ — **Superseded 2026-06-10.** Webhook removed from S4 and moved to Backlog. BO alignment needed before it re-enters planning. No Jira update required until BOs confirm MVP value. *(decisions-log 2026-06-10)*
- [x] **Check in with Pathfinder team on current demo state** — ✅ Done 2026-06-02. *(Squad-Sync 2026-05-26)*
- [x] **Run through with Amber: design-vs-implementation check** — ✅ Done 2026-06-02. *(Squad-Sync 2026-05-26)*
- [x] ~~**Check with Acacia on POCDEX data model familiarity**~~ — **Cancelled 2026-06-02.** No longer needed.
- [x] **Attend/track Thursday WD×DO job family model discussion** — ✅ Done 29 May 2026. *(Pow Hwee adhoc 2026-05-25)*
- [ ] **Write user story: opportunity matching using competencies** — not yet in backlog. Flagged by Pow Hwee. For Sprint 3 planning. *(Pow Hwee adhoc 2026-05-25)*
- [ ] **Research in-platform application form vs FormSG** — Pow Hwee proposing Sprint 3 spike; Michelle to research pilot agency customisation needs before spike scoping. Before Sprint 3 planning. *(Pow Hwee adhoc 2026-05-25)*
- [ ] **WOG Auth success metrics** — committed to Adrian this week. Grounded in Dec '26 OKR baselines from BO deck. Start Thursday at latest. *(daily plan 2026-05-26)*
- [ ] **OTEP-87 + OTEP-318 AC alignment** — needed before Sprint 3 grooming. If design review didn't cover it, schedule async with Amber. *(daily plan 2026-05-26)*
- [ ] **Drive R1 design alignment + discovery WITH the designers** — R1 deep-dive praised at PM Weekly, but the ask is to move it from PM-solo to a real cross-functional effort. Get Amber (+ Michelle Chen's design capacity if it lands) aligned on the three R1 surfaces: apply, agency-creation, manager dashboard. Before R1 grooming. *(PM Weekly 2026-06-02)*
- [ ] **Feed Adrian the specific R1 resource ask** — concrete framing for his Michelle Chen conversation: three net-new R1 builds (native apply + native creation + the seam), one FE dev. Reference the R1 capacity reality-check. This week. *(PM Weekly 2026-06-02)*
- [ ] **CSC SSO technical-feasibility deep-dive** — with Pow Hwee/Fabian; surface why there's an intentional re-login. Feeds open-item #30. Before Sprint 5 (~2 Jul). *(PM Weekly 2026-06-02)*
- [x] **Create the new "POCDEX Integration" Epic in Jira** and move OTEP-271, 203, 202, 127 under it — ✅ Done 2026-06-02
- [ ] **Follow up with Daryll/Pow Hwee on raising DQ issue** for OTEP code table in UAT read replica
- [x] **Work out next steps for WOG AD onboarding with Fabian and Pow Hwee** — WOG AD form submitted by Pow Hwee 2026-06-10; 2-4 week approval clock now running. (#26)
- [ ] **Complete Cybersecurity quiz by 2026-12-31** — **DEFER out of June (LNO 2026-06-02): 7 months out, not on the MVP/R1 spine.**
- [ ] **Map out dependencies in high-level Jira stories → `00-hub/risks.md`** — document cross-story dependency map. **→ DELEGATE to Pow Hwee (LNO 2026-06-02): he asked for it and owns the technical map; Michelle reviews, doesn't author.** *(captured 2026-05-21)*
- [x] **Ping Adrian — WOG AD onboarding**: Domain is `careercompass.gov.sg`. Two asks: (1) COMET onboarding status — is ESG/OTEP onboarded? (2) Approval to test against WOG AD Prod. ✅ Pinged 2026-05-21. Waiting on response. (#26)
- [ ] **Sync with Imelda (OTEP-Core Squad PM)** — four asks: (1) Who owns passing documents to CSC after WOG AD completes — her squad, Pathfinder, or joint? (#30) (2) How does OTEP consume job family, job function, agency, competency data from her squad — API? file? push? (#18) (3) Schema + field names for that reference data? (4) Timeline — when is it available for OTEP to integrate? (#18)
- [ ] **Schedule POCDEX planning session with Daryll** — POCDEX team lead. Must happen before Sprint 4 planning. Loop Pow Hwee in. (#31)
- [ ] **Create high-level dependency stories** (Pow Hwee's ask from Teams thread) — one placeholder story each for POCDEX go-live prep (#31), WOG AD onboarding (#26), CSC SSO (#30). No ACs yet — titles and sprint-window targets in Jira.
- [x] **[PM action — #28] Confirm OTEP-85 visibility rule** — resolved 2026-05-19: `closing_date > today`; "Closing soon" badge (≤7 days) is OTEP-129's
- [x] **[PM action — #29] Define OTEP-289 ACs, timebox, expected outcome** — resolved 2026-05-19: 2-day timebox, written recommendation output
- [ ] **[PM action] Clean OTEP-128 AC** — remove "This opportunity is closed" notice AC from OTEP-128 (it belongs to OTEP-129).
- [x] Loop Diana into opportunities decisions going forward (Jace's call, PM Weekly 11 May) — ✅ Done 2026-06-02
- [ ] ~~Load Adrian's OKR doc into NotebookLM~~ — **KILL (LNO 2026-06-02): it's already `06-skills-and-decisions/otep-roadmap-okrs-2627.md`. No action.**
- [x] Clarify the "OTG test cases — session notes co-innovation" request, then route to `projects/otg-ops/task-log.md` — ✅ Done 2026-06-02
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

*Updated: 2026-08-17 — stale-check. Sprint 7→Sprint 8 rollover: header, This Week's Focus, and In Progress sections were all still describing Sprint 7 [closed 9 Aug] a full week into Sprint 8. Rewrote all three against live Sprint 8 counts (73 issues: 37 Done, 9 In Progress, 11 QA, 3 To Do, 13 Backlog) and cross-checked WOG AD/PS/DS/#55 narrative against PM-OS's 2026-08-14 W33 weekly review. Prior: 2026-08-07 — stale-check. Pathfinder Sprint 7 counts re-pulled live (Done 22→23, In Progress 9→8); engineering section header/lists updated to match. Prior: 2026-08-06 (2nd pass) — stale-check. PM confirmed "we are in Sprint 7 now"; rewrote "This Week's Focus" from Sprint 6 close-out framing to Sprint 7's actual state (goal, active build threads, carried-forward risks); dropped stale "Sprint 6 closed" trailer from the header line. Prior (same day, 1st pass): Refreshed Engineering section header/counts to live 2026-08-06 pull (In Progress 9 [was 8], QA 8 [was 6], To Do 2, Done 22 [was 16], Backlog 15 [was 22]); "This Week's Focus" section (still describing closed Sprint 6) left flagged, not rewritten — needs PM judgement, see note in that section. Prior: 2026-08-04 — stale-check. Refreshed Engineering section header/counts to live 2026-08-04 pull (In Progress 8, QA 6 [was 2 — OTEP-131 moved], To Do 2, Done 16, Backlog 22 [was 24]); "This Week's Focus" section (still describing closed Sprint 6) left flagged, not rewritten — needs PM judgement, see note in that section. Prior: 2026-07-31 — stale-check. Corrected sprint header (Sprint 6→7, Sprint 6 had closed); corrected Engineering section header/counts to live Sprint 7 pull (In Progress 8, QA 2, To Do 2, Done 16, Backlog 24); pruned resolved CSC SSO/ref-data (#18/#30) from the P1 BAU line per the file's own prior flag, kept WOG AD (#26) but flagged for a fresh status check rather than assuming June's blocker still holds; flagged (not rewrote) "This Week's Focus" as describing closed Sprint 6, needs PM judgement at next `/weekly-plan`. Prior: 2026-07-24 — stale-check. Corrected "ends today" (written 2026-07-20, sprint actually ends Sun 26 Jul) → "ends Sunday". Prior: 2026-07-20 — stale-check. Corrected Sprint 6 week label (W1→W2, was 1 day into W2), engineering section counts (5/18/5/42/21, was 6 days stale at 6/12/16/33/23). Prior: 2026-07-14 — stale-check. Corrected sprint header (Sprint 5→6, was 11 days stale), engineering section counts (now points to live sprint-status.md, Sprint 6: 6/12/16/33/23), and This Week's Focus (refreshed with #55 escalation, UAT duplicate-thread flag, #58 environment-governance finding, #52 resolution). Prior: 2026-07-03 (stale-check. Corrected In Progress/QA counts and #43 status). Prior: 2026-07-01 (stale-check — engineering counts refreshed to live Sprint 5 pull). Prior: 2026-06-29 (sprint line S4→S5, engineering section left stale pointing to sprint-status.md).*
