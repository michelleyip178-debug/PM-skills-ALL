# Active Tasks

Current sprint: **Sprint 2 (May 18 – Jun 1)** — Opportunities Listing → Detail end-to-end.
Sprint 1 closed 2026-05-15 (partial sign-off — auth edge-cases OTEP-110, WOG-04/05/06 carry forward). Sprint 2 scope per Jira board 2026-05-15: **5 stories** — OTEP-85 (cards, absorbs "Closing soon"), OTEP-128 (detail page), OTEP-267 (pagination), OTEP-285 (click-through + state), OTEP-276 (design system spike — Thomas). Cut-line: OTEP-285 first (highest risk — state architecture).

Story pipeline tracking lives in [sprint-checklists.md](../projects/otep-mvp/sprint-checklists.md). (Old story-readiness.md archived 2026-05-15.)

---

## This Week's Focus

**Theme:** Sprint 1 finalisation (Fri 15 May). Archive + retro prep after sign-off; clear last Sprint 2 blockers.

---

## In Progress

- [ ] Clarify OTEP-133 email deep-link: OTEP auto-sends or manually composed link? Determines notification service scope for MVP (#15) — Sprint 4+, deprioritise this week
- [ ] Clarify OTEP-130 auto-populate: backend capture only (MVP) or programmatic form pre-fill (R1)? Confirm with Pow Hwee (#14) — Sprint 3, deprioritise this week

---

## Up Next

- [ ] **[Carry-over] OTEP-192 & OTEP-193** — Design data model and file import job (Sprint 2 blockers)
- [ ] **[Carry-over] OTEP-202 & OTEP-203** — POCDEX seed DB and API service
- [ ] **[Carry-over] OTEP-271** — Local POCDEX database (container + schema, Leo)
- [ ] **[Carry-over] OTEP-194** — FormSG integration discovery
- [ ] Consolidate sprint stories + ACs into a doc for Rethna (ThoughtWorks QA) — she needs this ahead of the QA review session
- [ ] Run test script review session with Rethna — story by story against AC (happy path, edge cases, error states); log gaps before sign-off
- [ ] **Sharpen acceptance criteria** for Sprint 2 user stories (Pow Hwee) — groom-ready standard before Sprint 2 kickoff Mon 18 May; cross-check [sprint-checklists.md](../projects/otep-mvp/sprint-checklists.md)
- [ ] **Share OTG opportunity reports (Excel files) with the team** — unblocks #24, OTEP-192, OTEP-193. If not done before Thu 14 May grooming, complete **Fri 15 May**.
- [ ] Chase Rama on `formsg_url` (#2) — last unconfirmed OTG field. Blocks US-18 (Sprint 3).
- [ ] Validate categorisation hybrid model (Option C) with Adrian on officer-facing labelling
- [ ] Load Adrian's OKR doc into the NotebookLM notebook — confirm it isn't already `resources/otep-roadmap-okrs-2627.md`
- [ ] Loop Diana into opportunities decisions going forward (Jace's call, PM Weekly 11 May); add `areas/stakeholders/people/diana.md`
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

- [x] **OTEP-190 — Simple auth through Keycloak** done (Fri 15 May, finalisation day). Closes the Sprint 1 auth goal.
- [x] OTEP-170 base listing page layout and navbar MR completed (May 15)
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

*Updated: 2026-05-15 — Jira reconciliation pass (OTEP-190 done, status sync against Sprint 1 board).*
