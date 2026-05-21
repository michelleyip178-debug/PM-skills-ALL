# Workflow Coverage Audit: OTEP Opportunities

**Date:** 2026-05-13
**Scope:** All officer-facing workflows for Epic 4 (Opportunities) + Epic 5 (Auth) + supporting backend
**Source:** PRD, story files, sprint-allocation.md, story-id-map.md, open-items.md, decisions-log.md

---

## Officer Journey (end-to-end)

```
Entry → Discovery → Detail → Apply → Confirm → Track → Status → Withdraw
```

---

## Coverage by Workflow Stage

### 1. Entry Points

| Workflow | Story | Status |
|----------|-------|--------|
| Log in via WOG AD | OTEP-71a | Covered |
| First-time login (onboarding) | WOG-06 | Covered |
| Return via bookmarked/shared filtered URL | OTEP-86 (URL params) | Covered |
| Email deep-link (EDM) → detail page | OTEP-133 (combined) | Bundled — see gap #1 |
| Login denied (agency not onboarded) | OTEP-111 | Covered |
| Login fail (bad credentials / AD down) | OTEP-110 | Covered |
| Session timeout → re-auth | WOG-04 | Covered |
| Log out | WOG-05 | Covered |

### 2. Discovery (Browse + Search + Filter)

| Workflow | Story | Status |
|----------|-------|--------|
| Browse all OTG listings | OTEP-85 | Covered (split into OTEP-85 / OTEP-267 / OTEP-268 on 2026-05-13) |
| Filter by opportunity type | OTEP-86 | Covered |
| Filter by category/job function | US-03 | Covered |
| Clear all filters | US-05 | Covered |
| Sort by posting date (newest first) | OTEP-85 (absorbed from OTEP-129, 2026-05-14) | Covered |
| Identify type on card (badge) | OTEP-85 (absorbed from old OTEP-128, 2026-05-14) | Covered |
| Identify C@G vs OTG source | OTEP-88 | Covered |
| Keyword search | — | **No story** — gap #2 |
| "Closing soon" indicator on card | — | Mentioned in PRD, no AC — gap #3 |
| Pagination | OTEP-267 | Covered — dedicated story with ACs (split 2026-05-13) |

### 3. Detail View

| Workflow | Story | Status |
|----------|-------|--------|
| View OTG opportunity detail | OTEP-87 | Covered |
| View C@G opportunity summary | OTEP-89 | Covered |
| View competencies ("What you'll develop") | OTEP-87 ACs | Covered |
| Back to listing preserves filter state | sprint-allocation note | Mentioned but no AC on a story |
| Closed opportunity deep-link → "no longer available" | OTEP-87 AC + PRD Section 7 | Covered |
| Incomplete data (missing fields) | OTEP-87 edge case | Covered |

### 4. Application

| Workflow | Story | Status |
|----------|-------|--------|
| Apply to STIP via FormSG | US-18 (basic) → OTEP-130 (full) | Covered — US-18 written 2026-05-13, ~~gap #4 resolved~~ |
| Apply to Gig via FormSG | US-18 → OTEP-130 | Same |
| Apply to Internal Job via FormSG | US-18 → OTEP-130 | Same |
| SJR card — no apply action in MVP | — | **No story** — open item #20, gap #5 |
| C@G deep-link redirect | OTEP-133 | Covered |
| Pre-redirect notice ("Leaving OTEP") | OTEP-133 AC | Covered |
| FormSG link missing/broken → fallback | Sprint 4 placeholder | Mentioned |
| FormSG is down | OTEP-130 edge case | Covered |
| Pre-fill from profile | US-P3 | Written (R1 unless FormSG supports) |
| "Already applied" indicator on listing card | — | **Not covered** — gap #6 |
| Double-submit prevention | OTEP-130 edge case (question) | Asked but no resolution |

### 5. Post-Application

| Workflow | Story | Status |
|----------|-------|--------|
| Submission confirmation | US-10 | Covered |
| View applications list | US-14 | Covered |
| View individual application status | US-15 | Covered |
| Status change notification (in-app) | US-16 | Covered |
| Withdraw application | US-17 | Covered |
| Post-FormSG redirect back to OTEP | — | **No resolution** — gap #7 |
| Webhook missed → state sync | US-10 edge case | Asked but no resolution |
| C@G application — can we track it? | — | **Unscoped** — gap #8 |

### 6. Ringfencing & Profile

| Workflow | Story | Status |
|----------|-------|--------|
| Ringfenced listing (eligible only) | OTEP-127 | Covered |
| Agency transfer → listing refreshes | PRD Section 7 | Mentioned |
| View HR-sourced profile | US-P1 | Covered |
| View competencies | US-P2 | Covered |

### 7. Backend / Operational

| Workflow | Story | Status |
|----------|-------|--------|
| OTG → OTEP file import (Excel) | OTEP-192 (file import job, carry-over) | **No story with ACs** — gap #9. OTG has no API; data via Excel (decided 2026-05-14). |
| C@G ingestion | — | **No story** — open item #11 |
| Opportunity lifecycle (open/closed) | — | **No story** — open item #17, gap #10 |
| Instrumentation (success metrics) | Sprint 6 placeholder | No story with ACs |
| Application status source of truth | — | **Unresolved** — gap #11 |

---

## Gaps (11 total — 1 resolved, 10 remaining)

### High severity (write before Sprint 3 planning)

| # | Gap | Detail | Recommendation |
|---|-----|--------|----------------|
| 2 | **Keyword search has no user story** | Confirmed MVP (decision 2026-05-08). Has 2 open items (#9 UX approach, #16 infra). Sprint-allocation says "possibly its own story in Sprint 3" but no ACs exist. | Write a dedicated search story. ACs: keyword match on title/description/agency; partial match + typo tolerance; zero-results state; search state in URL; search clears on "Clear all." |
| ~~4~~ | ~~**US-18 (basic FormSG redirect) has no written ACs**~~ | **Resolved 2026-05-13.** US-18 written in [otg-lifecycle.md](stories/otg-lifecycle.md) with 4 ACs: redirect to `formsg_url` in new tab, null-URL fallback error state, SJR exclusion. `formsg_url` confirmed 2026-05-21 \u2014 US-18 fully unblocked. | ~~Write US-18 story file.~~ Done. |
| 9 | **OTG file import has no story with ACs** | Scoping gap #1, flagged since day one. Sprint 1 has OTEP-192 (carry-over) but no buildable story covering import frequency, Excel schema mapping, error handling, retry, data freshness. OTG has no API — data via Excel (decided 2026-05-14). | Write an import story before Sprint 2 W1. Without it, the foundation of Sprint 2 has no definition of done. |
| 11 | **Application status source of truth undefined** | Tracking stories (US-14–17) assume status updates flow in, but don't specify how. Agency manual update? FormSG webhook? Automated from OTG? Shapes the entire tracking group. | Resolve before tracking stories are groomed. Recommend: FormSG webhook = "Submitted" (automated). Subsequent statuses = agency manual update via admin panel (MVP). |

### Medium severity (resolve before the affected sprint)

| # | Gap | Detail | Recommendation |
|---|-----|--------|----------------|
| 1 | **EDM deep-link is bundled into OTEP-133** | Two distinct flows in one story: "email → OTEP detail page" and "C@G apply redirect." What if officer isn't logged in? What if opportunity is closed? | Split or add ACs to OTEP-133 covering: unauthenticated deep-link → login → return to detail; closed opportunity deep-link → message. |
| 5 | **SJR card with no apply action has no story** | Open item #20. Amber needs to design the treatment but there's no story to groom. | Write a story or add ACs to OTEP-128: "Given an SJR opportunity, when I view the card/detail page, then I see [Coming soon / Express interest / info-only] instead of an Apply button." |
| 7 | **Post-FormSG redirect back to OTEP unresolved** | PRD open question. If FormSG can redirect back, US-10 works inline. If not, confirmation depends on the webhook. Changes the UX. | Resolve with Pow Hwee: does FormSG support a return-URL param? Then update US-10 ACs. |
| 10 | **Opportunity lifecycle (open → closed) has no story** | Open item #17. `closing_date` confirmed, `is_published` doesn't exist. Rule is likely "visible if closing_date > today" but needs ACs covering: what triggers closed, what happens to the card, what happens to detail page, what about in-progress applications. | Add ACs to OTEP-85 or write a separate story. |

### Low severity (tidy up at next grooming pass)

| # | Gap | Detail | Recommendation |
|---|-----|--------|----------------|
| ~~3~~ | ~~**"Closing soon" indicator has no AC**~~ | **Resolved 2026-05-14:** "Closing soon" label is now a must-have AC on OTEP-85 (absorbed from OTEP-129). Threshold: `closing_date` ≤ 7 days. | Done. |
| 6 | **"Already applied" indicator on listing cards** | OTEP-130 AC covers the detail page but not the card in the listing view. | Add AC to OTEP-128 or OTEP-85: "Given I have applied, when I see its card, then an 'Applied' badge is shown." |
| 8 | **C@G application tracking explicitly unscoped** | Officers who apply via C@G have no status visibility in OTEP. Tracking stories (US-14–17) only cover OTG. | Add to PRD Section 3 "What we're NOT building": "No application status tracking for Careers@Gov opportunities (off-platform)." |

---

## PRD Sections Stale After May 13 Decisions

| Section | What's stale | Update needed |
|---------|-------------|---------------|
| Section 3 — Solution Overview table | Still shows SJR → OTG redirect, Internal Jobs → OTG redirect | Update: SJR = no apply in MVP; Internal Jobs = FormSG |
| Section 11 — Decision Tracker | Missing May 8–13 decisions; "Secondment vs SJR" still shows TBD | Add May 8–13 entries; mark Secondment resolved |
| Section 13 — Open Questions | "Is 'Secondment' distinct?" still open | Mark resolved |

---

## Summary

- **21 stories written** (US-18 added 2026-05-13), 4 with missing or incomplete ACs
- **10 workflow gaps remaining** (gap #4 resolved) — 3 high, 4 medium, 3 low
- Biggest structural gap: **the backend is under-storied** — data pipeline, opportunity lifecycle, and status source of truth have no buildable stories
- Officer-facing workflows are well covered from login through tracking
- OTEP-85 split into OTEP-85 / OTEP-267 / OTEP-268 improved pagination and empty/error state coverage

### Priority actions

1. Write search story (#2) and pipeline story (#9) before Sprint 3 planning
2. Resolve status source of truth (#11) before tracking group is groomed
3. Flag gaps #1 (EDM deep-link), #5 (SJR card UX), and #10 (lifecycle) at next grooming
4. Update stale PRD sections to reflect May 13 decisions

---

*Review at each sprint's grooming. When a gap is resolved, note the date and which story/AC addressed it.*
