# Active Tasks

Current sprint: **Sprint 2 (May 18 – May 31)** — Opportunities Listing → Detail end-to-end.
Sprint 1 closed 2026-05-15 (partial sign-off — auth edge-cases OTEP-110, WOG-04/05/06 carry forward). Sprint 2 Jira board synced 2026-05-18: **In Progress:** OTEP-170 (Thomas), OTEP-288 (Léo) · **Done:** OTEP-252 (Thomas) · **Backlog:** 10 stories. ⚠️ OTEP-285 not found in Jira — confirm with Thomas.

Story pipeline tracking lives in [sprint-checklists.md](../projects/otep-mvp/sprint-checklists.md). (Old story-readiness.md archived 2026-05-15.)

---

## This Week's Focus

**Theme:** Sprint 2 Week 1 kick-off. Unblock Pow Hwee on data model and file import (#24), run Squad Grooming, lock design lock date (#22) with Amber.

---

## In Progress

**Engineering (Jira):**
- [ ] **OTEP-170** (Thomas) — Base layout for Opportunity Listing Page. MR in progress — not closed in Jira despite local "done" note from May 15.
- [ ] **OTEP-288** (Léo) — Setup simple backend endpoint with in-memory list. Sub-task of OTEP-170.

---

## Up Next

- [ ] **Run `/groom-prep`** — today (Mon 18 May) before noon; Squad Grooming is tomorrow 10am
- [ ] **Chase Pow Hwee on #23 + #24** — harmonised data model (OTG + C@G) and which OTG Excel reports to ingest; both block OTEP-192/193
- [ ] **Confirm OTEP-285 with Thomas** — committed in sprint but not in Jira; create ticket or remove from commitment before grooming
- [ ] **Share OTG opportunity reports (Excel files) with the team** — unblocks #24, OTEP-192, OTEP-193 (overdue — was due Fri 15 May)
- [ ] **Sharpen ACs for Sprint 2 stories** — OTEP-85, OTEP-128, OTEP-267 before tomorrow's grooming; cross-check [sprint-checklists.md](../projects/otep-mvp/sprint-checklists.md)
- [ ] Consolidate sprint stories + ACs into a doc for Rethna (ThoughtWorks QA)
- [ ] Run test script review session with Rethna — story by story against AC; log gaps before sign-off
- [ ] Chase Rama on `formsg_url` (#2) — last unconfirmed OTG field. Blocks US-18 (Sprint 3).
- [ ] **[Carry-over] OTEP-192 & OTEP-193** — Design data model and file import job (Sprint 2 blockers; NOT yet on Sprint 2 board — confirm placement with Pow Hwee)
- [ ] **[Carry-over] OTEP-202, OTEP-203, OTEP-271** — POCDEX seed DB, API service, local DB — NOT on Sprint 2 board; confirm Sprint 2 vs Sprint 3 placement with Pow Hwee (open item #27)
- [ ] **[Carry-over] OTEP-194** — FormSG integration discovery (Thomas, in Sprint 2 Backlog)
- [ ] Clarify OTEP-133 email deep-link: OTEP auto-sends or manually composed link? Determines notification service scope (#15) — Sprint 4+, low priority
- [ ] Clarify OTEP-130 auto-populate: backend capture only (MVP) or programmatic pre-fill (R1)? Confirm with Pow Hwee (#14) — Sprint 3
- [ ] Validate categorisation hybrid model (Option C) with Adrian on officer-facing labelling
- [ ] Loop Diana into opportunities decisions going forward (Jace's call, PM Weekly 11 May); add `areas/stakeholders/people/diana.md`
- [ ] Load Adrian's OKR doc into NotebookLM — confirm it isn't already `resources/otep-roadmap-okrs-2627.md`
- [ ] Clarify the "OTG test cases — session notes co-innovation" request, then route to `projects/otg-ops/task-log.md`

---

## Waiting On

| Item | Waiting for | Since | Next action |
|------|-------------|-------|-------------|
| OTG file import (Excel → OTEP DB) | Pow Hwee | May 4 | OTG has no API (decided 2026-05-14). Depends on #24 (which reports). Michelle sharing reports — **Fri 15 May** if not done Thu 14. |
| POCDEX account creation (OTEP-72) | Pow Hwee | May 4 | Confirm push mechanism works |
| `formsg_url` field (#2) | Rama + PSD Ops | May 4 | Last unconfirmed OTG field. Chase after the other 5 were confirmed. |
| Tue/Fri "squad sync" rename | Jace (PM Weekly 11 May) | May 11 | When confirmed, update `ceremony-prep.md` + `sprint-prep-rhythm.md` |
| Auth edge-case scope (OTEP-110, WOG-04/05/06) | Sprint 1 finalisation | May 11 | Fri 15 May finalisation decides: carry-over vs Sprint 3 |
| Design system assessment (OTEP-276) | Thomas | May 13 | Now ticketed as **OTEP-276** — Sprint 2 spike. Investigates custom design system reimplementation. If inconclusive → proceed with LifeSG. |
| Sprint 1 overflow list | Thomas | Before Sprint 1 finalisation (Fri 15 May) | Which Sprint 1 stories will carry over to Sprint 2? Affects Sprint 2 capacity — Thomas is sole FE. |
| QA review session with Rethna | Michelle (doc first) | May 13 | Consolidate stories + ACs into a shareable doc, then schedule session. |

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
- [x] Verify COMET onboarding with Imelda — out of scope for Michelle

---

*Updated: 2026-05-18 — Jira live sync (Sprint 2 board). OTEP-170 back to In Progress; OTEP-252 added as Done; OTEP-288 added as In Progress.*
