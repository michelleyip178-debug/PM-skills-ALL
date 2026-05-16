# Grooming Brief — Thu 14 May 2026 (v4 — post-reshuffle)

**Target:** Sprint 2 (18–29 May) — Listing → Detail End-to-End
**Sprint goal:** By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity.
**Scope:** 4 new stories + 6 carry-overs. No filters (Sprint 3).
**Sources:** filters.md, otg-lifecycle.md, sprint-checklists.md, sprint-allocation.md, open-items.md, decisions-log.md

---

## 1. Story Readiness

| ID | Title | Persona | Outcome | ACs | Must/GTH tiered | Deps/Blockers | Design | Rating |
|---|---|---|---|---|---|---|---|---|
| OTEP-85 | Listing cards | Officer | Scan + click | 9 must, 5 GTH | Yes | File import (#192) + API contract (Fri sync) | Finalised | **Ready** |
| OTEP-267 | Pagination | Officer | Find beyond first screen | 3 must, 3 GTH | Yes | Hard dep on OTEP-85 | Finalised | **Ready** (if 85 ships) |
| OTEP-268 | Empty/error/partial states | Officer | Not confused by blank page | 4 must, 1 GTH | Yes | Hard dep on OTEP-85 | Finalised | **Ready** (if 85 ships) |
| OTEP-128 | Detail page | Officer | Decide whether to apply | 9 must, 3 GTH | Yes | Hard dep on OTEP-85 + API contract | Finalised | **Ready** |

**Summary:** All 4 stories ready. ACs tiered (must-have / good-to-have), officer-perspective language, no technical implementation in ACs. API contracts are the only remaining blocker — Pow Hwee's contract sync with Thomas + Leo is tomorrow (Fri 15 May).

### Carry-overs (6 — foundation)

| ID | Title | Status | Why it must go first |
|---|---|---|---|
| OTEP-193 | Design data model | Not started | OTEP-85 API builds on this |
| OTEP-192 | File import job (OTG Excel) | Not started | No data → empty listing. Depends on #24 (which reports). |
| OTEP-202 | POCDEX seed data | Not started | Dev environment |
| OTEP-271 | POCDEX container (Leo) | Not started | Dev environment |
| OTEP-194 | FormSG discovery | Not started | Sprint 3 concern |
| OTEP-183 | POCDEX spike | Not started | Sprint 3 ringfencing |

---

## 2. Gaps and Ambiguities

| # | Source | Gap | Risk |
|---|--------|-----|------|
| 1 | OTEP-85 | Ministry icon mapping — where does agency → icon come from? Who maintains it? | Good-to-have, so won't block ship. But frontend needs a mapping or default. |
| 2 | OTEP-128 | "What you'll develop" content shape — string, array, or HTML? | Confirmed available from OTG, but format depends on import job (OTEP-192). |
| 3 | Open item #24 | **Which OTG Excel reports to ingest.** Still open. OTEP-192 can't be built without this. | **Critical path.** Michelle to share reports. |
| 4 | Open item #23 | Harmonised data model — must support OTG file import now + C@G API later. | Pow Hwee to confirm at contract sync. |
| 5 | Open item #22 | Design lock date not set for Sprint 2. | Agree with Amber in Sprint 2 W1. Prevents mid-sprint design churn. |
| 6 | OTEP-85 | "Closing soon" label — what's the exact visual treatment? Badge? Text? Colour? | Amber's design should specify this. Confirm at lock date. |

---

## 3. Dependencies

### Critical path

```
Michelle shares OTG Excel reports (#24)
  → OTEP-193 (data model) ← Day 1 priority
    → OTEP-192 (file import job)
      → OTEP-85 listing API ← contract sync Fri 15 May
        ├→ OTEP-267 (pagination) ← parallel with 268
        ├→ OTEP-268 (states) ← parallel with 267
        └→ OTEP-128 (detail page) ← needs detail API contract too
```

### Story-to-story

| From | To | Type | Reason |
|------|----|------|--------|
| OTEP-85 | OTEP-170 (Sprint 1, in progress) | Hard | Base listing page layout must land |
| OTEP-85 | OTEP-193 (carry-over) | Hard | Data model before API |
| OTEP-85 | OTEP-192 (carry-over) | Hard | File import before data exists |
| OTEP-267 | OTEP-85 | Hard | Listing API must exist |
| OTEP-268 | OTEP-85 | Hard | Card component must exist |
| OTEP-128 | OTEP-85 | Hard | Card click handler + listing page must exist |

---

## 4. Edge Cases Not in ACs

### OTEP-85
- **Null posting date** — sort breaks. Fallback: creation timestamp or put at the end?
- **Closing date = today** — "still open" means `>` today (hidden on closing day). Correct, or should it be `>=`?
- **OTG Excel has bad/malformed data** — import job should handle, but what reaches the listing API? Cards should degrade (OTEP-268 covers per-card resilience).
- **Zero opportunities** — OTEP-268 covers this (empty state). But OTEP-85 should still render the page shell.

### OTEP-267
- **Records change between page loads** — new postings, expirations. Duplicates or missed cards. Accept as known limitation for Sprint 2.
- **Browser back button** — returns to correct page or resets?
- **Filter + pagination (future)** — applying a filter should reset to page 1. Not Sprint 2, but design should accommodate.

### OTEP-268
- **Repeated retry failures** — same "Try again" button after N failures? Or show a different message?
- **Partial load with zero successful cards** — full error state or empty state? (Edge of empty vs error.)

### OTEP-128
- **Detail page for an opportunity that just expired** — officer bookmarked it yesterday, closing date passed today. Shows with "closed" banner per AC. But does the listing still link to it? (No — listing hides closed opportunities. Direct URL access only.)
- **Very long description text** — no truncation on detail page per design. But does the page handle extreme lengths (10,000 chars)?
- **Missing optional field ("what you'll develop")** — section hides per edge case. But what if ALL optional fields are empty? Detail page shows only title + agency + type?

---

## Pow Hwee Will Probably Ask...

1. **"What's the listing API response shape?"** — Agree at tomorrow's contract sync. Suggested: `{ items: [...], total: number, page: number, per_page: 15 }`.

2. **"What's the detail API response shape?"** — Agree at sync. Suggested: `GET /opportunities/:id` → single object with all fields from the card-vs-detail table.

3. **"How do we handle bad data in the Excel import?"** — PM call: skip bad rows and log them. Don't fail the whole import. Officers see the records that loaded (OTEP-268 partial-load AC covers the frontend side).

4. **"What if posting_date is null?"** — PM call needed. Recommend: sort to the end (not top). Officers shouldn't see undated cards first.

5. **"Who flips the feature flag?"** — PM confirms when to go live. Flag is `opportunities_hub`.

---

## R1 Deflection List

| Topic | Response |
|-------|----------|
| Type filter | "Sprint 3 — OTEP-86, deferred to make room for detail page." |
| Clear filters | "Sprint 3 — US-05, pairs with OTEP-86." |
| Apply button | "Sprint 3 — US-18. Detail page ships without it." |
| Mobile/tablet | "Desktop is the Sprint 2 commitment." |
| Search | "MVP but not Sprint 2. Needs indexing spike." |
| C@G data | "Sprint 5. C@G = API, separate integration." |
| Skeleton loading | "Simple spinner. Skeleton is polish." |
| Filter counts | "R1. Ship without, see if officers ask." |

---

## Recommended Dev Sequence (for contract sync tomorrow)

| Phase | What | Who | When |
|-------|------|-----|------|
| 1 | Data model (OTEP-193) | Pow Hwee | Sprint 2 Day 1 (Tue 19 May) |
| 2 | File import job (OTEP-192) | Pow Hwee / Leo | Immediately after data model |
| 3 | Listing API + Detail API (contracts) | Pow Hwee | Contract sync Fri 15 May; build W1 |
| 4 | Card component shell + detail page route | Thomas | W1 (can start before API lands using mock data) |
| 5 | Wire cards to listing API + detail page to detail API | Thomas | W2 (once APIs are live) |
| 6 | Pagination + states | Thomas | W2 (parallel with wiring) |

Thomas can start frontend in W1 using mock data against the agreed contract. Backend catches up by mid-W1. Full integration in W2.

---

*Generated 2026-05-14 (v4 — post-reshuffle). Sources: filters.md, otg-lifecycle.md, sprint-allocation.md, sprint-checklists.md, open-items.md, decisions-log.md.*
