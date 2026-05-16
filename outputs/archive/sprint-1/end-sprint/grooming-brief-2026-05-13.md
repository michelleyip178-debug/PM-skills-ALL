# Grooming Briefing — Wed 13 May: Internal Squad Groom, Sprint 2

**Regenerated 2026-05-13 evening.** Reflects 7 resolved open items, OTEP-85 split into OTEP-85/267/268, apply-flow decision, Sprint 1 Jira status, and auth carry-over (OTEP-71 + OTEP-110 into Sprint 2). Original brief (May 11) is superseded.

This is the last internal pass before Thursday's formal Backlog Grooming + Sprint Planning (Thu 14 May, with the BOs). Wednesday's job: walk the **nine stories** with the squad (Pow Hwee, Leo, Thomas, Amber), introduce the OTEP-85 split, confirm auth carry-over, close every gap that's closeable in the room, and decide everything you own — so Thursday's estimation isn't built on open questions. Rama facilitates. You lead content.

**Sprint 2 scope: 9 stories** — 7 Opportunities (OTEP-85, OTEP-267, OTEP-268, OTEP-86, OTEP-128, OTEP-129, US-05) + 2 Auth carry-over (OTEP-71, OTEP-110).

---

## What Changed Since the May 11 Brief

| Change | Old state | New state | Impact on grooming |
|--------|-----------|-----------|-------------------|
| **OTEP-85 split** | 1 story (5 stories total) | 3 stories: OTEP-85/267/268 (7 Opportunities total) | Walk the split first. Squad hasn't seen it. |
| **Auth carry-over** | OTEP-71 Sprint 1, OTEP-110 Sprint 3 | Both moved to Sprint 2 (9 stories total) | OTEP-71 is already in progress. OTEP-110 is new Sprint 2 work. |
| **`is_published` (#4)** | 🔴 Unconfirmed | ✅ Field doesn't exist — use `closing_date > today` | OTEP-85 visibility rule is clear. No longer blocked. |
| **`closing_date` (#3)** | 🔴 Unconfirmed | ✅ = application closing date | OTEP-129 "Closing soon" unblocked. Sort key confirmed. |
| **Secondment (#12)** | 🔴 Pending Jacky | ✅ Subsumed under SJR | OTEP-86 filter list + OTEP-128 type badge confirmed. |
| **5 other OTG fields** | 🔴 Open | ✅ #1 not needed, #5 not available, #6 available, #7 dead | Detail page design implications (Sprint 3) — not Sprint 2. |
| **Apply-flow decision** | SJR via OTG redirect | FormSG only (STIP/Gig/Internal Job). SJR deferred. US-19 dropped. | Sprint 3 context. Not Sprint 2 scope. |
| **DoR/DoD guidelines** | Not documented | Saved from Rama. Story DoR = subtasks + tests + UI linked to ACs + feature flag + API contract. | OTEP-85/267/268 have subtasks + tests. Others need subtasks in the room. |

---

## Sprint 1 Backlog Review — What's Landing, What's At Risk

Sprint 1 ends Fri 15 May. Review status with the squad before talking Sprint 2 — what overflows directly affects Sprint 2 capacity, especially with Thomas as sole FE.

### Done (6 items)

| Jira | Story | Notes |
|------|-------|-------|
| OTEP-209 | Baseline database conventions | — |
| OTEP-171 | Frontend repo setup | Was In Progress on May 11 — now done. Unblocks all Sprint 2 FE work. |
| OTEP-201 | Ref table schema migration | Was QA on May 11 — now done. |
| OTEP-207 | Seed ref tables with POCDEX data | New item (not in previous tracking). |
| OTEP-204 | Seed core entity tables | Was Backlog — now done. Fallback data available if pipeline isn't ready. |
| OTEP-224 | Core entity table schema migration | New item (not in previous tracking). |

### In Progress (3 items)

| Jira | Story | Sprint 2 impact | Question to ask |
|------|-------|-----------------|-----------------|
| OTEP-190 | Simple authentication through Keycloak | **High** — OTEP-85 needs authenticated access. | On track for Friday? |
| OTEP-173 | Exploration: auth flow and tech | Low — informs auth, not Sprint 2 Opportunities. | Findings ready to share? |
| OTEP-170 | Base layout for Opportunity Listing Page | **High** — OTEP-85 subtask #3 builds on this. | Will it merge by Friday? |

### Still in Backlog (7 items — 2 days left)

| Jira | Story | Sprint 2 impact | Risk |
|------|-------|-----------------|------|
| **OTEP-193** | Design data model for Opportunities | **High** — OTEP-85 API endpoint needs this | 🔴 Still in Backlog. Not started. |
| **OTEP-192** | Design recurring job to fetch opportunities data | **Critical** — this IS the pipeline. No data = empty listing. | 🔴 Still in Backlog. Not started. Escalate today. |
| OTEP-251 | Create ER diagram for OTEP data model | Medium — design documentation, ties to OTEP-193 | New item (not in previous tracking) |
| OTEP-194 | FormSG integration & callback flow | Low — apply is Sprint 3 | |
| OTEP-183 | POCDEX profile lookup spike | Low — ringfencing is Sprint 3 | |
| OTEP-202 | POCDEX seed database for local dev | Low — dev tooling | |
| OTEP-203 | POCDEX mock API stub for local dev | Low — dev tooling | |

### Auth carry-over — decided

| Story | Sprint 2? | Notes |
|-------|-----------|-------|
| **OTEP-71** — Login Authentication (parent + subtasks: token, session, UI) | **Yes — carry-over** | In Progress via OTEP-190. Must complete for authenticated listing access. |
| **OTEP-110** — Login fail / clear error | **Yes — moved from Sprint 3** | Clear error messages for wrong credentials, locked account, service down. |
| WOG-04 — Stay logged in during session | Sprint 3 | Decide at Sprint 1 finalisation (Fri 15) |
| WOG-05 — Log out of OTEP | Sprint 3 | Same |
| WOG-06 — First-time login experience | Sprint 3 | Same |

**What to say:** "OTEP-71 carries over — it's already in progress and must complete for Sprint 2. OTEP-110 moves into Sprint 2 so officers see real error messages, not generic failures. WOG-04/05/06 stay Sprint 3 unless they land by Friday."

### What to walk out of this section knowing

1. **Which Sprint 1 items will overflow?** Thomas to confirm — he flagged in Slack that "there will be some leftover from Sprint 1 already."
2. **Is the OTG pipeline (OTEP-192) delivering data?** If no, escalate today.
3. **Is the base listing page (OTEP-170) merged?** If no, OTEP-85 can't start on day 1 of Sprint 2.
4. **Is the data model (OTEP-193) finalised?** OTEP-85 API endpoint needs it.

---

## Sprint 2 Goal

**Officers can browse and filter every OTG opportunity on one authenticated page, newest first, published-only.**

---

## Readiness Scorecard

| Story | Quality | Readiness | What's blocking | Fallback |
|-------|:-------:|-----------|-----------------|----------|
| **OTEP-85** — Cards + API | ✅ | 🟡 | Pipeline delivering data? Amber's card design? API contract? | FE builds against seed data (OTEP-204). Groom on draft designs. API contract = grooming output. |
| **OTEP-267** — Pagination | ✅ | 🟡 | Pagination pattern (Amber). Page size (Pow Hwee). | Default: page numbers, 20 per page. |
| **OTEP-268** — States + resilience | ✅ | 🟡 | Empty/error state designs (Amber). | Groom on wireframe-level spec. Design polish can follow. |
| **OTEP-128** — Type badge | ✅ | 🟡 | Officer-friendly labels (Amber). | Ship raw names (STIP/Gig/SJR/Internal Job), rename later. |
| **OTEP-129** — Sort | ✅ | ⚠️ | **Overlaps with OTEP-85.** | Absorb into OTEP-85? "Closing soon" becomes Sprint 3 or separate AC. Decide today. |
| **OTEP-86** — Type filter | ✅ | 🟡 | Filter UI pattern (Amber). | Default: top-bar chips. |
| **US-05** — Clear filters | ✅ | 🟢 | Nothing. | — |
| **OTEP-71** — Login Authentication (carry-over) | ✅ | 🟡 | In Progress (OTEP-190). Not done by Sprint 1 end. | Continues into Sprint 2. Already being worked. |
| **OTEP-110** — Login fail / clear error | ✅ | 🟡 | ACs written (stories/auth.md). Subtasks needed. | Create subtasks in the room. |

**Secondment, `closing_date`, `is_published` are no longer blocking anything.** The remaining gaps are: pipeline data, Amber's designs, API contract, OTEP-129 overlap decision, and OTEP-110 subtasks. All closeable in the room.

---

## Grooming Order

### 0. Walk the OTEP-85 split (5 min)

Do this first, before any estimation. The squad hasn't seen it.

"I split the view-all story into three pieces so we can build and demo incrementally. OTEP-85 is the full-stack core — listing API, card component, feature flag. OTEP-267 is pagination. OTEP-268 is empty state, error state, and missing-field resilience. OTEP-267 and OTEP-268 are both FE-only and can run in parallel once OTEP-85's API and card component exist."

```
OTEP-85 (cards + API)  <-- must ship first
   |-- OTEP-267 (pagination)     <-- parallel
   |-- OTEP-268 (states)         <-- parallel
   |-- OTEP-86 (type filter)
   |-- OTEP-128 (type badge)
   +-- OTEP-129 (sort -- overlap?)
```

### 1. US-05 — Clear filters (2 min)

🟢 Ready. Confirm "Clear all" behaviour + URL-param reset. Warm the room.

### 2. OTEP-128 — Type badge (5 min)

Lock the type taxonomy: STIP, Gig, SJR, Internal Job. Secondment = SJR (confirmed). Accessibility: distinguishable without colour alone. Get Amber to commit to label wording or accept raw names as default.

### 3. OTEP-85 — Cards + API (15 min)

The anchor. Give it the most time. Surface:
- **Pipeline status:** testable real data? If no → escalate to Adrian, don't estimate against air.
- **Visibility rule:** `closing_date > today` — confirmed. If `closing_date` is null, show and flag as data quality. State it, get a nod.
- **API contract:** `GET /opportunities?page=1&per_page=20` → `{items: [...], total, page, per_page}`. Each item: id, title, type, agency, ministry_icon, commitment_type, posting_date, closing_date. Ask Pow Hwee to confirm or counter-propose.
- **Card click behaviour:** no detail page in Sprint 2. Recommend view-only (no click action). Settle it.
- **Feature flag:** `opportunities_hub`, entry point = Opportunities nav link. One flag for all 7 stories.

### 4. OTEP-129 overlap decision (5 min)

OTEP-85 already includes default sort (newest first, `posting_date`, tiebreak by ID). OTEP-129 adds: single-direction, interleaved by date not grouped by type, secondary sort. Most is already in OTEP-85.

**Your recommendation:** absorb OTEP-129 into OTEP-85. "Closing soon" label (<=7 days to `closing_date`) becomes either a Sprint 2 AC on OTEP-85 (if Amber has a design) or moves to Sprint 3. Ask the squad: "Does anyone see a reason to keep 129 separate?"

### 5. OTEP-267 — Pagination (5 min)

FE-only, small. Confirm pagination pattern with Amber (pages vs infinite scroll). Default page size 20 — Pow Hwee confirms API performance is fine. Loading state during page fetch.

### 6. OTEP-268 — States + resilience (5 min)

FE-only. Three components: empty state, error state, missing-field card resilience. Designs from Amber (or groom on wireframe-level spec). Test matrix for missing fields.

### 7. OTEP-86 + US-05 — Type filter (10 min)

Force the filter-UI-pattern decision (Amber's in the room). Confirm: multi-select OR logic, URL-param format (Pow Hwee's call), zero-results state, no filter counts for Sprint 2.

### 8. OTEP-71 + OTEP-110 — Auth carry-over (5 min)

Quick status check, not a deep groom — OTEP-71 is already in progress and the ACs are written. Confirm:
- **OTEP-71:** What's left? Token handling, session management, login UI — which subtasks are done, which carry over?
- **OTEP-110:** Login error states — 3 ACs (wrong credentials, locked account, service down). Create subtasks in the room.
- **Capacity impact:** These are primarily Pow Hwee/Leo work. Confirm they don't compete with OTEP-85 backend work.

**Total: ~55 min.**

---

## Decisions to Walk In With (PM mode)

These are yours. Present them as decisions, not options:

| Decision | Status | Notes |
|----------|--------|-------|
| Sort key = `posting_date` | **Confirmed** | Was a fallback assumption — now confirmed by Rama (closing_date resolution). |
| Tiebreak = opportunity ID ascending | **Decided** | Stable ordering. |
| Visibility = `closing_date > today` | **Confirmed** | No `is_published` field. Resolved May 13. |
| Secondment = SJR | **Confirmed** | Jacky (BO), May 13. No separate filter option. |
| Filter UI default = top-bar chips | **Your default** | Amber can override with a reasoned alternative. |
| Feature flag = one `opportunities_hub` | **Your proposal** | Close it in the room. |
| "Closing soon" label | **Your call** | Unblocked. Sprint 2 if Amber has a design, Sprint 3 if not. |
| Absorb OTEP-129 into OTEP-85 | **Your recommendation** | Ask the squad, but lead with this. |

---

## Open Items — Close in the Room

| Item | Owner | Action |
|------|-------|--------|
| #17 — Opportunity lifecycle | Michelle / Pow Hwee | Propose `closing_date > today` = visible. One sentence. Close it. |
| API contract for listing endpoint | Pow Hwee | Confirm request/response shape. DoR requirement. |
| Pagination pattern | Amber | Pages or infinite scroll? |
| Card click behaviour | Amber + Pow Hwee | View-only recommended. |
| Feature flag scope | Squad | One flag, all stories. |
| OTEP-129 overlap | Squad | Absorb or keep? |
| Officer-friendly type labels | Amber | Raw names as fallback. |
| "Closing soon" — Sprint 2 or 3? | Squad | Depends on Amber's design readiness. |

---

## R1 Deflection List

| Topic | Response |
|-------|----------|
| Search | "MVP but not Sprint 2. Indexing spike needed (#16). Sprint 3." |
| C@G listings | "Ingestion unconfirmed (#11). Sprint 2 = OTG-only." |
| Detail page | "Sprint 3 — OTEP-87." |
| Ringfencing | "Sprint 3 — OTEP-127. Sprint 2 = all officers see all OTG listings." |
| Apply flow | "Sprint 3 — US-18. FormSG for STIP/Gig/Internal Job. SJR deferred (May 13)." |
| Category filter | "Sprint 3 — US-03. Blocked on hybrid model." |
| Filter counts | "Skip Sprint 2. Add if officers ask." |
| Persist filters | "R1. URL params = within-session persistence." |
| Competency matching | "R1 (May 8). Tags only, no scoring." |
| SJR apply via OTG | "Killed. All future flows through OTEP (May 13)." |
| Save / bookmark | "R1 guardrail." |
| Card expansion | "No. Fixed-size cards. Overflow → detail page (Sprint 3)." |

---

## Pow Hwee Will Probably Ask...

| Question | Your answer |
|----------|-------------|
| "What's the visibility rule?" | "`closing_date > today`. No `is_published` field — confirmed with Rama May 13. If `closing_date` null, show and flag as data quality." |
| "What's the sort key?" | "`posting_date`, newest first. Tiebreak: opportunity ID ascending." |
| "What's the API contract?" | "Subtask #1 in OTEP-85 proposes: `GET /opportunities?page=1&per_page=20` → items + total + page + per_page. Each item: id, title, type, agency, ministry_icon, commitment_type, posting_date, closing_date. Confirm?" |
| "Why split 85?" | "Too large to estimate as one. Three vertical slices: OTEP-85 is the full-stack core, OTEP-267/268 are FE-only and can run in parallel. Same total scope." |
| "Can OTEP-267/268 start before OTEP-85?" | "Components in isolation (Storybook) yes. Integration no — needs OTEP-85's API and card." |
| "Pipeline ready?" | "That's my question to you. If not by Friday, FE builds against seed data (OTEP-204)." |
| "What if a card has null fields?" | "OTEP-268 handles it. Card renders with available fields, missing ones collapse. Test matrix in subtasks." |
| "One flag or per-story?" | "One: `opportunities_hub`. Entry = nav link." |
| "Secondment?" | "SJR. Jacky confirmed May 13." |
| "OTEP-129 is already in OTEP-85?" | "Exactly. I recommend absorbing it. Only independent value = 'Closing soon' label." |
| "What about the OTG type enum?" | "STIP / Gig / SJR / Internal Job. Are those the exact values in the export, or do we map?" |
| "URL params for filters?" | "Your call on format. Just bookmarkable + survives back-nav." |
| "Who marks an opp closed?" | "Proposing date-driven: `closing_date > today` = visible, else hidden. No manual flag. Sound right?" (#17) |
| "How many active listings?" | "~100-300 at any time based on PRD data (~4,700/year)." |

---

## PM Growth Nudge

Last week you walked into grooming with 6 unresolved field questions and a Secondment decision pending Jacky. Today you walk in with all of them answered. That's the shift from "waiting on answers to groom" to "grooming on confirmed facts." The next step: when Pow Hwee probes the visibility rule or the sort key, you don't say "we decided" — you say "I decided, here's why." Own the call, not just the outcome.

---

*Regenerated 2026-05-13 evening. Supersedes the May 11 version. Sources: filters.md (updated with OTEP-85/267/268 split), open-items.md, decisions-log.md, sprint-allocation.md, dor-dod-guidelines.md. Companion: [grooming-brief-2026-05-14.md](grooming-brief-2026-05-14.md) (Thu formal session) and [sprint-plan-brief-2026-05-14.md](sprint-plan-brief-2026-05-14.md) (planning framing).*
