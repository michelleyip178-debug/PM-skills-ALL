# Grooming + Sprint Planning Brief — Thu 14 May 2026

Combined output: `/groom` (edge cases from NotebookLM + local files) then `/sprint-plan-prep` (goal, stories, capacity).

---

## Part 1: /groom — Edge Cases from NotebookLM

The local-file analysis ([grooming-brief-2026-05-14-groom.md](grooming-brief-2026-05-14-groom.md)) covers story readiness, gaps, dependencies, and per-story edge cases. Below are the **additional findings from NotebookLM** that the local files missed.

### New edge cases to raise with Pow Hwee

| # | Edge case | Source | Sprint 2 impact | Recommendation |
|---|-----------|--------|-----------------|----------------|
| N1 | **SJR forms must be excluded from OTG ingest.** MVP testing doc says "SJR forms are excluded from MVP for now." Pipeline must filter them out. | MVP testing doc | **High** — SJRs in the listing would confuse officers. | Add to OTEP-192 ACs: "Exclude SJR records from ingest." Ask Pow Hwee: how do we identify SJR in the Excel export? |
| N2 | **Browsing privacy — clicking a card must not notify the officer's home agency.** JTBD #11 says "no privacy default = no trust = low adoption." Officers need to explore without political risk. | Officers JTBD doc | **Medium** — Sprint 2 is listing-only (no apply action), so no external redirects yet. But telemetry/logging decisions made now persist. | Confirm with Pow Hwee: does the listing API log officer-specific browsing data? If yes, who can see it? Lock the privacy default before launch, not before Sprint 2. Flag it as a pre-launch decision. |
| N3 | **Session timeout on the listing page.** Auth JTBD says sessions expire after 30 min of inactivity. If an officer leaves the grid open, walks away, comes back — what happens? | Auth releases doc | **Medium** — Sprint 2 has no apply action, so the worst case is a stale page, not a broken application. | Graceful re-login prompt on next interaction, not a silent redirect. This is auth behaviour (WOG-04, Sprint 3), but the listing page should handle it cleanly: show "Session expired — log in again" overlay, not a blank page. |
| N4 | **"Guidance copy" about where the application will be completed.** MVP testing doc requires the UI to "display guidance copy about where the application will be completed (in-app vs external)" before the user clicks. | MVP testing doc | **Low for Sprint 2** — no apply action on cards yet. But the card's type label (Internal Job / SJR / STIPs & Gigs) is the first signal of "what kind of experience this is." | Not Sprint 2 scope. Log for Sprint 3 (US-18 apply redirect). The type label on the card is sufficient for Sprint 2 browsing. |
| N5 | **State persistence after redirect.** MVP testing doc flags: "Try returning to the Opportunities listing after starting an application; confirm state persistence or loss." | MVP testing doc | **Low for Sprint 2** — no redirects yet. But back-button behaviour after clicking a card matters if cards are clickable. | Reinforces the "cards are view-only in Sprint 2" decision. No click = no redirect = no state persistence issue. |

### JTBD framing for the sprint goal

The JTBDs say officers need three things from a first look at the listing:

1. **A unified view** — "the breadth of opportunities across the public service in one place" (JTBD #1: Orient to what's possible)
2. **Data they can trust** — "current, accurate, and traceable" so decisions don't "blow up later when the data turns out stale" (JTBD #2: Data accuracy)
3. **No political risk** — officers need to explore without their home agency knowing they're looking (JTBD #11: Visibility control)

Sprint 2 delivers #1 (unified view). #2 (data accuracy) depends on the pipeline quality. #3 (privacy) is a policy decision that must be locked before launch but doesn't need a Sprint 2 build.

---

## Part 2: /sprint-plan-prep — Sprint 2 Plan

### Sprint Goal (recommendation, not options)

> **An authenticated officer can open OTEP and see every active OTG opportunity — STIPs, Gigs, SJRs, and Internal Jobs — on one listing page, newest first.**

Why this wording:
- "Authenticated" — auth must work (OTEP-71 carry-over/Sprint 1 completion is a prerequisite)
- "Every active OTG opportunity" — visibility rule is clear (`closing_date > today`), scope is OTG-only
- "One listing page" — the core JTBD #1 promise
- "Newest first" — sort is baked in (OTEP-129 absorbed)
- No mention of filtering, apply, or C@G — those are Sprint 3+

*Reframe note (pattern #8 — spoken voice):* In the room, say it like this: "By end of Sprint 2, an officer logs in and sees all OTG opportunities on one page. That's the promise. Everything else — filters, apply, C@G — comes next."

### Candidate Stories

**New stories (3) — estimate today:**

| Jira | Title | Est. size | Dependencies | Risk |
|------|-------|-----------|-------------|------|
| **OTEP-85** | Display opportunity cards with real OTG data | 5-8 pts | OTEP-193 (data model) + OTEP-192 (pipeline). Both carry-over, both Backlog. | **High** — critical path. If model + pipeline don't start by day 2-3, OTEP-85 can't build. Fallback: seed data (OTEP-204). |
| **OTEP-267** | Pagination | 2-3 pts | OTEP-85 (API must exist) | Low — FE-only. Can start in Storybook before OTEP-85 API lands. |
| **OTEP-268** | Empty state, error state, data resilience | 3-5 pts | OTEP-85 (card component must exist) | Low — FE-only. Same parallel approach. |

**Carry-over from Sprint 1 (5) — status check, not re-estimate:**

| Jira | Title | Owner | Status | Sprint 2 blocker? |
|------|-------|-------|--------|-------------------|
| OTEP-193 | Design Data Model for Opportunities | **Unassigned** | Backlog | **Yes — OTEP-85 API needs this.** Assign today. |
| OTEP-192 | Design recurring job to fetch opportunities data | **Unassigned** | Backlog | **Yes — no pipeline = no data.** Assign today. |
| OTEP-202 | POCDEX seed database for local dev | Leo | Backlog (needs splitting) | No — dev tooling. |
| OTEP-194 | FormSG integration discovery | — | Backlog | No — Sprint 3 context. |
| OTEP-183 | POCDEX profile lookup spike | Pow Hwee | Backlog (needs splitting) | No — ringfencing is Sprint 3. |

### Capacity

| Person | Available days (10 working days, Sprint 2) | Notes |
|--------|---------------------------------------------|-------|
| Pow Hwee | 9 | 18 May PM out. Owns OTEP-193 / OTEP-192 (both need assigning). |
| Leo | 9 | 22 May PM out. OTEP-202 needs splitting. |
| Thomas | **TBD** | Sole FE. Cross-squad pulls. Leave plans not confirmed. **All 3 new stories are FE-heavy.** |
| Amber | — | Design finalised. Supports QA on edge cases. |
| Michelle | 9 | 18 May PM out. Consolidate AC doc for Rethna. Lead grooming + planning. |

**Capacity risk:** Thomas is the bottleneck. OTEP-85 subtasks #2-4 are FE. OTEP-267 is all FE. OTEP-268 is all FE. If Thomas loses 2+ days to cross-squad work, at least one story slips.

**Mitigation:** Can Leo take any FE subtasks? Or can OTEP-85 subtask #1 (backend API) run ahead while Thomas closes Sprint 1 carry-over?

### Development Sequence

```
Week 1 (18-22 May):
  Day 1-2: OTEP-193 (data model) + OTEP-192 (pipeline) — Pow Hwee/Leo
  Day 2-3: OTEP-85 subtask #1 (API endpoint) — starts once model exists
  Day 3-5: OTEP-85 subtasks #2-4 (card component, wire to API, feature flag) — Thomas
           OTEP-267 + OTEP-268 can start in parallel (Storybook) — Thomas

Week 2 (25-29 May):
  Day 6-8: Integration — cards rendered from real API, pagination wired, states tested
  Day 9-10: Bug fixes, QA with Rethna, sprint demo prep
```

### Decisions to Close in the Room

| # | Decision | Recommendation | Owner |
|---|----------|---------------|-------|
| 1 | **OTEP-193 + OTEP-192 owners** | Assign today. These are the critical path. | Squad |
| 2 | **API contract** for listing endpoint | Confirm request/response shape. OTEP-85 subtask #1. | Pow Hwee |
| 3 | **Card click behaviour** | View-only. No click action in Sprint 2. | Michelle (decided) |
| 4 | **`closing_date` null** — show or hide? | Show + flag as data quality issue. | Michelle (decided) |
| 5 | **SGL exclusion** from pipeline (NotebookLM finding) | Exclude from ingest. Add to OTEP-192 ACs. | Pow Hwee |
| 6 | **Profile story split (#25)** | Basic auth profile (name, email) in Sprint 2 scope. Competency profile deferred. | Squad |
| 7 | **OTG report specification (#24)** | Name the exact reports: STIPs & Gigs, SJR, audience filters. Confirm this is the full list. | Michelle / Pow Hwee |

### Opening Statement

"Sprint 2 is where OTEP goes from infrastructure to something officers can see. The goal: an authenticated officer logs in and sees every active OTG opportunity on one page — STIPs, Gigs, SJRs, Internal Jobs — newest first.

Three new stories: cards with real data, pagination, and error handling. Plus five carry-over items from Sprint 1 — the two that matter most are the data model and the pipeline job, because without them the listing has nothing to display.

The main risk is the same as last sprint: the data model and pipeline are both still in Backlog. If they don't start in the first two days, the listing API can't be built and the sprint goal is at risk. I need owners assigned to both today.

Thomas is the bottleneck for frontend — all three new stories are FE-heavy and he's fielding another squad's requests. We need to confirm his availability and decide whether Leo can pick up any FE work.

I'll walk the three new stories, then we estimate. The carry-over items are a status check, not a re-groom."

### R1 Deflection List

| Topic | Response |
|-------|----------|
| Type filter | "Sprint 3 — OTEP-86. Listing works without it." |
| Type badge design | "Sprint 3 — OTEP-128. Cards have a basic type label in Sprint 2." |
| Search | "Sprint 3. Needs an indexing spike." |
| C@G listings | "Ingestion unconfirmed. Sprint 2 = OTG-only." |
| Detail page | "Sprint 3 — OTEP-87." |
| Ringfencing | "Sprint 3 — OTEP-127." |
| Apply flow | "Sprint 3 — US-18. FormSG for STIP/Gig/Internal Job." |
| Mobile layout | "Desktop is the Sprint 2 commitment. Mobile follows later." |
| Competency profile | "Depends on another team. Basic profile (name, email) only for Sprint 2." |
| "Closing soon" label | "Sprint 3. Sort by posting date is in Sprint 2 via OTEP-85." |

---

*Generated 2026-05-14. Sources: local files (filters.md, sprint-allocation.md, open-items.md, risks.md) + NotebookLM (OTEP Epic 4 notebook — JTBD doc, MVP testing doc, Auth releases doc).*
