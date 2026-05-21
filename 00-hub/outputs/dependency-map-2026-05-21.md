# Integration Dependency Map — OTEP MVP
> Generated: 2026-05-21 post-grooming. For Pow Hwee review.
> Covers all external integration chains that gate Sprint 4+ delivery.

---

## Dependency Chain Overview

```
TODAY (21 May)
    │
    ▼
[Adrian confirms: COMET + prod approval] ── 2 weeks ──▶ WOG AD onboarding done
                                                               │
                                    ┌──────────────────────────┴─────────────────────────┐
                                    ▼                                                     ▼
                       Auth stories land (Sprint 4)                    Documents → CSC (4 weeks)
                       OTEP-71, 110, 304, 305                                    │
                       + Ringfencing (OTEP-127)                                  ▼
                       + First-time login (WOG-06)                  CSC SSO live (Sprint 5/6)
                                    │
                                    ▼
                           UAT with real auth (Sprint 8)
                                    │
                                    ▼
                     Security review submission (Sep, Sprint 9)
                                    │
                                    ▼
                          🚀 Go-Live Fri 16 Oct 2026


POCDEX CHAIN (runs in parallel):
[Daryll session booked] ──▶ Support structure agreed ──▶ OTEP-271/203 (Sprint 3 plumbing) ──▶ OTEP-127 ringfencing (Sprint 4) ──▶ WOG-06 onboarding (Sprint 4)


OTG INGEST CHAIN:
OTEP-193 data model (Sprint 2) ──▶ OTEP-192 recurring ingest job (Sprint 3) ──▶ Live data in listing (Sprint 3 end)


C@G CHAIN:
C@G API ingestion story (unwritten) ──▶ C@G listing cards (Sprint 5) ──▶ C@G detail + apply (Sprint 5: OTEP-89)


FORMSG CHAIN:
OTEP-194 discovery (Sprint 2) ──▶ OTEP-319 basic redirect (Sprint 3) ──▶ OTEP-130 full webhook (Sprint 5)
```

---

## Dependency Table (for Jira/Confluence)

| Dependency | What it unlocks | Owner | Must land by | Sprint | Status |
|---|---|---|---|---|---|
| **WOG AD onboarding** (`careercompass.gov.sg`) — COMET status + prod testing approval from Adrian | Auth stories (OTEP-71/110/304/305), ringfencing (OTEP-127), CSC SSO chain (#30) | Michelle → Adrian | Before Sprint 4 start (15 Jun) — **tight; errors add weeks** | S02–S03 (admin) | 🔴 Not started — Adrian ping needed today. Domain confirmed. Process = min 2 wks from approval, longer if back and forth. |
| **CSC SSO** — documents passed to CSC after WOG AD; 4-week lead time | Officer login via CSC SSO | Michelle + Imelda (ownership TBC) | Before Sprint 5 end (10 Jul) best case | S05–S06 | 🔴 Not started — WOG AD must close first |
| **POCDEX planning session (Daryll)** — support structure for first POCDEX API project | OTEP-271/203 can be validated; OTEP-127 ringfencing can be confirmed; OTEP-202 seed DB can be assigned | Michelle (book session) | Before Sprint 4 planning (5 Jun) | S02–S03 (admin) | 🔴 Not booked |
| **POCDEX plumbing** (OTEP-271 local DB + OTEP-203 API service) | Ringfencing (OTEP-127), first-time login (WOG-06), OTEP-202 seeding | Leo (271), Pow Hwee (203) | Sprint 3 end (12 Jun) | S03 | Planned |
| **OTG data model** (OTEP-193) | OTG ingest job (OTEP-192), real listing data | Leo | Sprint 2 end (29 May) | S02 | In Progress |
| **OTG ingest job** (OTEP-192) | Live opportunities in listing | Leo | Sprint 3 end (12 Jun) | S03 | Planned |
| **FormSG discovery** (OTEP-194) | FormSG Phase 2 webhook (OTEP-130), pre-fill scope | Thomas | Sprint 2 end (29 May) | S02 | Backlog |
| **C@G API ingestion** (story unwritten) | C@G cards on listing, OTEP-89 detail + apply | Pow Hwee | Sprint 5 start (29 Jun) | S04–S05 | ⚠️ No story exists |

---

## Critical Path (longest chain)

```
Adrian confirmation (today)
→ WOG AD onboarding done (2 wks, ~5 Jun)
→ Auth stories complete (Sprint 4, ~26 Jun)
→ CSC documents sent (~26 Jun)
→ CSC SSO live (4 wks, ~24 Jul)
→ CSC SSO integration (Sprint 6, ~24 Jul)
→ Feature freeze (21 Aug) ← TIGHT
→ Security review (Sep)
→ Go-Live (16 Oct)
```

**Total chain: ~13 weeks from today.** Feature freeze is 13 weeks away. Zero slack.

---

## Placeholder Stories — Ready to create in Jira

### Story A: WOG AD Onboarding — careercompass.gov.sg
- **Type:** Task / Dependency story
- **Description:** OTEP must be onboarded onto WOG AD / Azure AD via COMET using the domain `careercompass.gov.sg`. Onboarding process takes ~2 weeks once (1) COMET status confirmed with Adrian and (2) approval to test against WOG AD Prod received. This is a PM-led admin track, not a dev story — engineering starts auth stories (OTEP-71/110/304/305) once onboarding is complete.
- **Sprint window:** Admin S02–S03 / Dev unlock Sprint 4
- **Owner:** Michelle (chase Adrian) + Pow Hwee (tech lead once approved)
- **Blocks:** OTEP-71, OTEP-110, OTEP-304, OTEP-305, OTEP-127, CSC SSO (#30)
- **Open item:** #26

### Story B: CSC SSO Integration
- **Type:** Story (to be groomed)
- **Description:** After WOG AD onboarding completes, OTEP must complete SSO integration with CSC (Civil Service College). WOG AD documents passed to CSC; CSC requires 4 weeks. Integration work (scope TBC with Imelda) follows. Ownership of passing documents: TBC — Pathfinder, Core Squad (Imelda), or joint. Total SSO chain from WOG AD kickoff: 6 weeks.
- **Sprint window:** Sprint 5 (29 Jun–10 Jul) best case; Sprint 6 (13–24 Jul) realistic
- **Owner:** Michelle (Imelda = context source, not co-owner)
- **Blocked by:** WOG AD onboarding (Story A above)
- **Open item:** #30

### Story C: POCDEX Go-Live Prep — Planning Session + Support Structure
- **Type:** Task / Dependency story
- **Description:** First OTEP project using the POCDEX API. Support structure not settled — no agreement with Daryll's team (POCDEX team lead) on how issues are escalated, how test data is managed, or what production support looks like. Planning session with Daryll must happen before Sprint 4 so that OTEP-271/203 (Sprint 3 plumbing) can be validated and OTEP-127 ringfencing can start safely. OTEP-202 (seed database) must be assigned a sprint at this session.
- **Sprint window:** Admin S03 (session); OTEP-202 seed DB Sprint 3–4
- **Owner:** Michelle (book + chair session) + Pow Hwee
- **Blocks:** OTEP-127 (ringfencing), OTEP-202 (seed DB), WOG-06 (first-time login)
- **Open item:** #31

### Story D: C@G API Ingestion Setup
- **Type:** Story (to be groomed)
- **Description:** Careers@Gov opportunities are ingested via the C@G API (confirmed 2026-05-14, open item #11 resolved). No story exists for the ingestion setup — schema mapping, sync frequency, error handling. This is a prerequisite for OTEP-89 (C@G opportunity detail + apply CTA) and any C@G listing cards appearing in the opportunity hub.
- **Sprint window:** Sprint 4–5
- **Owner:** Pow Hwee
- **Blocks:** OTEP-89 (C@G detail), US-10 (C@G card label)

### Story E: OTEP-131 — Handle missing/null formsg_url gracefully
- **Type:** Story (Sprint 3)
- **Description:** When an OTG opportunity has a null or missing `formsg_url`, the Apply CTA must not break. Fallback: CTA disabled + "Contact the agency directly" message (ref OTEP-133 fallback AC). Required before OTEP-319 (basic FormSG redirect) ships.
- **Sprint window:** Sprint 3
- **Owner:** TBC
- **Blocks:** OTEP-319 (Apply via FormSG redirect)

---

## Working Sessions to Book

> Note: Adrian ping (COMET status + prod testing approval) is a separate async message — not a session. Sessions below are working sessions to thrash out the details.

### Session 1: WOG AD onboarding process — Pow Hwee
- **Who:** Michelle + Pow Hwee
- **When:** This week (before Sprint 2 end 29 May)
- **Duration:** 30–45 min
- **Context:** WOG AD is a formal onboarding process, not a one-off tech setup. Domain name (`careercompass.gov.sg`) is now confirmed — that was the gate to start. Clock starts when Adrian gives approval. Minimum 2 weeks, longer if there are errors or back and forth.
- **Agenda:** (1) What are the steps in the onboarding process — who does what, in what order? (2) What can go wrong and cause back and forth — what errors have we seen before? (3) Who from Pow Hwee's side tracks the process? (4) What's the earliest realistic date auth stories can start, assuming we kick off this week vs end of May?
- **What you need from this:** A process map + realistic date range for Sprint 4 auth planning. Not just "2 weeks" — what's the p50 and p90 duration?

### Session 2: POCDEX planning — Daryll
- **Who:** Michelle + Daryll (POCDEX team lead) + Pow Hwee
- **When:** Before Sprint 4 planning (5 Jun). Target: first week of Sprint 3 (2–6 Jun).
- **Duration:** 1 hour
- **Agenda:** (1) Support model for OTEP's POCDEX API usage — escalation path, known issues. (2) OTEP-202 sprint placement — Leo needs to seed test profiles before ringfencing UAT. (3) Are there API limits, sandbox access, or test data constraints we need to know about?
- **What you need from this:** Support structure agreed + OTEP-202 sprint confirmed.

### Session 3: CSC SSO context — Imelda
- **Who:** Michelle + Imelda (Core Squad PM)
- **When:** This week
- **Duration:** 30 min
- **Agenda:** (1) What does passing documents to CSC involve — what format, what process? (2) Can she give a timeline for job function/family test data? (3) Does Core Squad have context on competency data source (open item #18)?
- **What you need from this:** Process clarity so Michelle can own the CSC SSO track end-to-end. Imelda is a source — Michelle owns the outcome.
- **Owner of CSC SSO:** Michelle

### Session 4: Dependency map review — Pow Hwee
- **Who:** Michelle + Pow Hwee
- **When:** After Sessions 1–3 are booked (can be async via Teams if needed)
- **Duration:** 30 min
- **Agenda:** Walk through the dependency map + 5 placeholder stories. Confirm sprint windows. Confirm OTEP-202 and C@G ingestion story owners.
- **What you need from this:** Pow Hwee's sign-off on the map before it goes to BO/Steering.

---

*Produced: 2026-05-21. For Pow Hwee review + Sprint Planning preparation.*
