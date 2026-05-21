# Active Tasks

Current sprint: **Sprint 2 (May 18 – May 29)** — Opportunities Listing → Detail end-to-end.
Jira sync 2026-05-20: **In Progress:** OTEP-170 (Thomas), OTEP-193 (Léo), OTEP-288 (Léo), OTEP-296 (Michelle) · **Done:** OTEP-252 (Thomas) · **Backlog:** OTEP-85, OTEP-128, OTEP-129, OTEP-267, OTEP-268, OTEP-289, OTEP-194, OTEP-276, OTEP-295.

Story pipeline tracking lives in [sprint-checklists.md](../04-ceremonies/sprint-checklists.md). (Old story-readiness.md archived 2026-05-15.)

---

## This Week's Focus

**Theme:** Sprint 2 Week 1 kick-off. Unblock Pow Hwee on data model and file import (#24), run Squad Grooming, lock design lock date (#22) with Amber.

---

## In Progress

**Engineering (Jira — as of 2026-05-20):**
- [ ] **OTEP-170** (Thomas) — Base layout for Opportunity Listing Page. MR in progress.
- [ ] **OTEP-193** (Léo) — Design data model for Opportunities. .sql migration + Go structs. ⚠️ Must align with OTEP-296.
- [ ] **OTEP-288** (Léo) — Setup simple backend endpoint with in-memory list. ⚠️ WIP risk — Léo has 2 In Progress items. New comment 2026-05-19.
- [ ] **OTEP-296** (Michelle) — Prepare defined report format matching data model. Standardises OTG Excel format.

---

## Up Next

- [ ] **Map out dependencies in high-level Jira stories → `00-hub/risks.md`** — document cross-story dependency map *(captured 2026-05-21)*
- [ ] **Do up the OTG report in Excel format and share to Leo via the user story** — include sample records *(captured 2026-05-21)*
- [ ] **Ping Adrian — WOG AD onboarding**: Domain is `careercompass.gov.sg`. Two asks: (1) COMET onboarding status — is ESG/OTEP onboarded? (2) Approval to test against WOG AD Prod. Starts the 6-week SSO chain (WOG AD 2 wks → CSC 4 wks). Before EOD today. (#26)
- [ ] **Sync with Imelda (OTEP-Core Squad PM)** — four asks: (1) Who owns passing documents to CSC after WOG AD completes — her squad, Pathfinder, or joint? (#30) (2) How does OTEP consume job family, job function, agency, competency data from her squad — API? file? push? (#18) (3) Schema + field names for that reference data? (4) Timeline — when is it available for OTEP to integrate? (#18)
- [ ] **Schedule POCDEX planning session with Daryll** — POCDEX team lead. First project with POCDEX API, support not settled. Must happen before Sprint 4 planning. Loop Pow Hwee in. (#31)
- [ ] **Create high-level dependency stories** (Pow Hwee's ask from Teams thread) — one placeholder story each for POCDEX go-live prep (#31), WOG AD onboarding (#26), CSC SSO (#30). No ACs yet — titles and sprint-window targets in Jira.
- [ ] **Run `/groom-prep`** — today (Wed 20 May) afternoon; Backlog Grooming is tomorrow 14:00 (L11 Anson)
- [ ] **Chase Pow Hwee on #23** — harmonised data model (OTG + C@G); Léo is building OTEP-193 now, alignment is urgent
- [x] **Share OTG opportunity reports (Excel files) with the team** — resolved 2026-05-18, open item #24 closed
- [x] **[PM action — #28] Confirm OTEP-85 visibility rule** — resolved 2026-05-19: `closing_date > today`; "Closing soon" badge (≤7 days) is OTEP-129's
- [x] **[PM action — #29] Define OTEP-289 ACs, timebox, expected outcome** — resolved 2026-05-19: 2-day timebox, written recommendation output
- [ ] **[PM action] Clean OTEP-128 AC** — remove "This opportunity is closed" notice AC from OTEP-128 (it belongs to OTEP-129). Raise with Pow Hwee at grooming.
- [ ] **Heads-up to Thomas: OTEP-285 absorbed into OTEP-128, OTEP-276 resolved.** No new Sprint 3 ticket needed for OTEP-285.
- [ ] **Sharpen ACs for Sprint 2 stories** — OTEP-85, OTEP-128, OTEP-267 before tomorrow's grooming; cross-check [sprint-checklists.md](../04-ceremonies/sprint-checklists.md)
- [ ] Consolidate sprint stories + ACs into a doc for Rethna (ThoughtWorks QA)
- [ ] Run test script review session with Rethna — story by story against AC; log gaps before sign-off
- [ ] Chase Rama on `formsg_url` (#2) — last unconfirmed OTG field. Blocks US-18 (Sprint 3).
- [ ] **[Carry-over] OTEP-192 & OTEP-193** — Design data model and file import job (Sprint 2 blockers; NOT yet on Sprint 2 board — confirm placement with Pow Hwee)
- [ ] **[Carry-over] OTEP-202, OTEP-203, OTEP-271** — POCDEX seed DB, API service, local DB — NOT on Sprint 2 board; confirm Sprint 2 vs Sprint 3 placement with Pow Hwee (open item #27)
- [ ] **[Carry-over] OTEP-194** — FormSG integration discovery (Thomas, in Sprint 2 Backlog)
- [ ] Clarify OTEP-133 email deep-link: OTEP auto-sends or manually composed link? Determines notification service scope (#15) — Sprint 4+, low priority
- [ ] Clarify OTEP-130 auto-populate: backend capture only (MVP) or programmatic pre-fill (R1)? Confirm with Pow Hwee (#14) — Sprint 3
- [ ] Validate categorisation hybrid model (Option C) with Adrian on officer-facing labelling
- [ ] Loop Diana into opportunities decisions going forward (Jace's call, PM Weekly 11 May); add `06-skills-and-decisions/stakeholders/people/diana.md`
- [ ] Load Adrian's OKR doc into NotebookLM — confirm it isn't already `06-skills-and-decisions/otep-roadmap-okrs-2627.md`
- [ ] Clarify the "OTG test cases — session notes co-innovation" request, then route to `projects/otg-ops/task-log.md`
- [ ] **Conduct PIM risk assessment (OTG ops)** — scope to the no-PIM scenario: identify worst-case damage if privileged accounts are abused, then submit residual risk for formal acceptance *(captured 2026-05-20)*
- [ ] Clean up email inbox *(captured 2026-05-20)*

---

## Waiting On

| Item | Waiting for | Since | Next action |
|------|-------------|-------|-------------|
| OTG file import (OTEP-192/193) | Pow Hwee | May 4 | Reports shared (2026-05-20). Blocked by #24 resolved. Pow Hwee to build. |
| POCDEX account creation (OTEP-72) | Pow Hwee | May 4 | Confirm push mechanism works — bundle into Pow Hwee check-in |
| `formsg_url` field (#2) | Rama + PSD Ops | May 4 | Last unconfirmed OTG field. Sprint 3 blocker. Chase this week. |
| Auth edge-cases (OTEP-110, WOG-04/05/06) | Pow Hwee / Leo | May 11 | **NOT on Sprint 2 board.** Confirm Sprint 3 placement at mid-sprint review Mon 26 May. |
| POCDEX go-live support structure | Daryll (POCDEX team) | 2026-05-21 | Schedule planning session with Daryll (#31) |
| CSC SSO ownership decision | Imelda (Core Squad PM) | 2026-05-21 | Who passes documents to CSC after WOG AD completes? (#30) |
| ~~OTEP-276 design system spike~~ | Thomas | — | **Resolved** — OTEP-252 Done confirms Flagship/LifeSG adopted. No further action. |
| QA review session with Rethna | Michelle (doc first) | May 13 | Create Sprint 2 AC summary doc first; schedule session after grooming settles. |

---

## Done This Sprint

- [x] **OTEP-252** — Setup design system in otep-web (Thomas). Done in Jira as of Sprint 2 start. Sub-task of OTEP-276 spike — design system foundation complete.
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
- [x] Release 4 prioritised on opportunity creation & posting (May 12)
- [x] PRD updated with 5-group user story structure, timeline, scoping gaps, risks (May 11)
- [x] Scoping gaps tracker populated with 13 items (May 11)
- [x] Projects reorganised: otep-opportunities + otep-wog-ad-login merged into otep-mvp (May 11)
- [x] Full OS cleanup — stale references fixed across 8 files (May 11)
- [x] Competency match ratio descoped to R1 (May 8)
- [x] Align with Adrian on target launch date — resolved (May 12)
- [x] Review Amber's Hub UI + card designs — alignment check done
- [x] ~~Verify COMET onboarding with Imelda~~ — stale. COMET = Michelle → Adrian (#26). Imelda's scope = CSC SSO (#30).

---

*Updated: 2026-05-18 — Jira comment sync. Scope changes applied (OTEP-285 absorbed, OTEP-129/268 re-added, OTEP-191 deprioritised). Three new PM action items added: #28 OTEP-85 visibility, #29 OTEP-289 ACs/timebox, OTEP-128 AC cleanup.*
