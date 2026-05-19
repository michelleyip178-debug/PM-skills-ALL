# Sprint Planning Briefing — Sprint 2

**Prepared:** 2026-05-11
**Planning session:** Thu May 15 (Week 2, Sprint 1)
**Sprint 2 dates:** May 19 – May 30
**Vesak Day:** May 31 (Saturday) — no impact on Sprint 2 capacity.

---

## Proposed Sprint Goal

**Option A (conservative):**
By end of sprint, officers can browse all opportunity listings from both pipelines on a single authenticated page, with type filter and source indicators — proving the "one place to see it all" promise works.

**Option B (ambitious):**
By end of sprint, officers can browse, filter, and scan all opportunities with full auth edge-case coverage (error states, session, logout, first-login) — completing the authenticated browsing experience end-to-end.

**Difference:** Option A is Opportunities only (5 stories). Option B adds auth completion (4 stories), which closes out the login epic. Option B is the better target if Sprint 1 auth stories ship clean — the auth edge cases are well-scoped and lower-risk.

---

## Candidate Stories

### Track 1: Opportunities — Core Hub (5 stories)

| Story ID | Title | Readiness | Risk |
|----------|-------|-----------|------|
| OTEP-85 | View all opportunities in one place | AC written. Design in progress (Amber). | **High** — blocked if OTG pipeline not delivering by May 16. C@G ingestion unconfirmed — may ship OTG-only. |
| OTEP-86 | Filter opportunities by type | AC written. Filter UI pattern not finalised (Amber). | **Medium** — Secondment classification unresolved (open item #12). Default to SJR-only if Jacky doesn't confirm. |
| OTEP-128 | Identify opportunity source (OTG vs C@G) | AC written. Part of card design (Amber). | **Low** — no external blockers. Needs user-friendly label decision. |
| US-05 | Clear filters and reset view | AC written. Straightforward. | **Low** — depends on OTEP-86 existing. No Jira ticket yet. |
| OTEP-129 | Sort by recency / posting date | AC written. | **Medium** — `closing_date` vs `end_date` unconfirmed (open item #3). Can default to posted_date and adjust. |

### Track 2: Auth Completion — WOG AD Edge Cases (4 stories)

| Story ID | Title | Readiness | Risk |
|----------|-------|-----------|------|
| OTEP-110 | Login fail / clear error | AC written. Grooming tasks done. | **Low** — well-scoped, no external dependencies. |
| WOG-04 | Stay logged in during session | AC written. Grooming tasks done. | **Low** — needs session timeout policy confirmed (gov compliance). No Jira ticket yet. |
| WOG-05 | Log out of OTEP | AC written. Grooming tasks done. | **Low** — straightforward. No Jira ticket yet. |
| WOG-06 | First-time login experience | AC written. Grooming tasks done. | **Low** — minimal: welcome + mandatory fields. Design needed from Amber. No Jira ticket yet. |

### Stretch (only if team pulls it in)

| Story ID | Title | Readiness | Risk |
|----------|-------|-----------|------|
| OTEP-127 | Apply ringfencing criteria | Draft only. | **High** — POCDEX field mapping unconfirmed. Eligibility service not designed. Recommend Sprint 3. |

### Recommended OUT of Sprint 2

| Story | Why | When |
|-------|-----|------|
| US-03 (Category filter) | Categorisation hybrid model needs 4-person validation | Sprint 3 |
| OTEP-127 (Ringfencing) | POCDEX eligibility fields unconfirmed; service not designed | Sprint 3 |
| Search | Search indexing infrastructure needs spike first (scoping gap #4) | Sprint 3 |

---

## Sprint 1 Status Check (do this May 15, before planning)

| Prerequisite | How to check | Fallback if not done |
|-------------|-------------|---------------------|
| Auth core flow (OTEP-71, 71b/c/d) working | Demo in planning session | Drop auth completion stories from Sprint 2 |
| OTG pipeline delivering records | Pow Hwee confirms testable | FE builds against mock data; pipeline joins mid-sprint |
| C@G ingestion method confirmed | Pow Hwee confirms API vs file | Sprint 2 ships OTG-only listings |
| Hub UI + card designs finalised | Amber presents in planning | Block OTEP-85 FE start until designs land |

---

## Capacity Flags

- **No public holidays** in Sprint 2 window (Vesak Day is May 31, Saturday)
- **Sprint 1 carry-over risk** — if auth core flow doesn't ship clean by May 16, auth completion stories (OTEP-110, WOG-04/05/06) may need to wait
- **Data pipeline dependency** — if OTG → OTEP pipeline isn't testable by May 16, OTEP-85 has nothing to display
- **Amber's bandwidth** — Sprint 2 needs: finalised card designs (Sprint 1), filter UI pattern, first-login screen (WOG-06). Confirm she can cover all three.
- **No known leave** — verify with team at planning

---

## Decisions to Surface in Planning

| Decision | Who decides | Why it matters |
|----------|------------|---------------|
| Secondment = SJR or distinct type? | Jacky (BO) — propose default: SJR-only | Determines OTEP-86 filter options |
| User-friendly labels for OTG vs C@G | Amber + Michelle | Officers don't know what "OTG" means |
| Default sort order | Michelle (recommend: most recent first) | OTEP-129 needs a defined default |
| Mock data acceptable if pipeline is late? | Pow Hwee + team | Determines whether OTEP-85 FE work can start day 1 |

---

## Open Items Blocking Sprint 2 (from open-items.md)

Only 2 of the 6 Rama field confirmations actually block Sprint 2:

| # | Item | Owner | Impact |
|---|------|-------|--------|
| 3 | `closing_date` vs `end_date` | Rama | OTEP-129 sort logic undefined |
| 4 | `is_published` field name/values | Rama | OTEP-85 can't determine which records to show |
| 11 | C@G ingestion method | Pow Hwee | Half the "unified" promise missing |
| 12 | Secondment classification | Jacky | OTEP-86 filter options undefined |

Items #1, 2, 5, 6 (eligibility, formsg_url, reporting_line, developmental_outcome) are Sprint 3–4 concerns, not Sprint 2 blockers.

---

## Michelle's Opening Statement

"Sprint 2 is where officers see the product for the first time. The goal: an authenticated officer opens OTEP and sees real opportunities from both pipelines, with type filter and source indicators. I have 9 candidate stories across two tracks — 5 for the listing experience, 4 to close out the login epic. I'll walk through readiness and risks, then I want the team to tell me what fits in the sprint."

---

## What NOT to Do in This Session

- Don't assign stories to engineers — let them self-select
- Don't commit to scope the team hasn't agreed to
- Don't let the OTG field questions slide — flag `closing_date` (#3) and `is_published` (#4) as sprint risks
- Don't include OTEP-127 (ringfencing) unless the team explicitly pulls it in
- Don't present 9 stories as a fixed scope — present the goal and let the team size it

---

*Prepared by Michelle (with Claude) | 2026-05-11*
