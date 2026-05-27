# Sprint Planning Brief — Sprint 3
**Prepared:** 27 May 2026 (updated post story sync) | **Planning session:** Thu 29 May 2026
**Sprint 3 dates:** 2 Jun – 13 Jun 2026

---

## Proposed Sprint Goal

**Option A — Conservative:**
> By end of Sprint 3, an officer can filter OTG opportunities by type and initiate an application via FormSG redirect, using live data delivered by the OTG recurring import job.

**Option B — Ambitious:**
> By end of Sprint 3, an officer can discover, filter, and apply to any active OTG opportunity (Internal Job, STIP, or Gig) — completing the full browse-to-apply loop, end-to-end, powered by live daily-imported OTG data.

**Recommendation:** Start with Option A and let the team upgrade to Option B if they confirm OTEP-128 closes early Sprint 3 and Thomas has capacity after carry-overs are sized. Option B depends on that sequencing landing cleanly.

---

## Candidate Stories

| Story ID | Title | Readiness | Risk |
|---|---|---|---|
| ~~OTEP-128~~ | View opportunity detail page *(carry-over)* | ✅ AC conflict resolved — "opportunity is closed" notice removed; sub-tasks OTEP-334 in QA, OTEP-314 In Progress | ⚠️ OTEP-327 (design system subtask) still Backlog. Minor gap: Pow Hwee suggested a server error AC ("can't load → generic error + retry") — not yet in Jira ACs. Not blocking |
| ~~OTEP-129~~ | Open/closed indicator *(carry-over)* | ✅ AC conflict resolved — visibility rule removed; now owns badge + deep-link behaviour only | Thomas assigned; no subtasks. Clean scope |
| ~~OTEP-267~~ | Pagination *(carry-over)* | Jira ACs present; Thomas assigned | ⚠️ API dep: `total_count` must be in GET /opportunities response. Pow Hwee to confirm in API spec |
| OTEP-192 | OTG recurring import job | ✅ Rewritten with user story + testable ACs | 3 open questions to resolve before build: file arrival mechanism, ingestion cadence, flag vs auto-deactivate. Assign to Léo or Pow Hwee |
| OTEP-86 | Filter by opportunity type | ✅ ACs written; scoped to type filter only | Tooltip copy (STIP/Gig/Internal Job/SJR definitions) needs Amber + BO sign-off before build. OTEP-92 subtask has no description — clarify with Pow Hwee |
| OTEP-317 | Clear filters | ✅ ACs written; depends on OTEP-86 + OTEP-318 | Straightforward; no blocking issues |
| OTEP-87 | Enhanced detail — apply CTA only | ✅ ACs reconciled to Sprint 3 scope; competency section explicitly out | Blocked until OTEP-128 closes. AC 6 (preserve filter + pagination state on back-navigation) — confirm this doesn't conflict with OTEP-128/OTEP-285 handling the same behaviour |
| OTEP-319 | Apply via FormSG basic redirect | ✅ Pre-fill dropped; ACs tight | One open question: should redirect append tracking params? Engineering to confirm before build |
| OTEP-324 | OAuth 2.0 refresh token rotation (NextAuth + Keycloak) | Jira description present; Thomas assigned | Adds to Thomas's Sprint 3 load. Developer/QA story — prevents 401 errors during sessions as Sprint 3 test coverage matures. No officer-facing ACs |
| OTEP-271 | Local POCDEX database (container + schema) | ⚠️ No AC file in our docs — Pow Hwee owns | Backend plumbing; parallel to above. Unblocks Sprint 4 ringfencing. Pow Hwee to confirm task breakdown at planning |
| OTEP-203 | Standalone POCDEX API service | ⚠️ No AC file in our docs — Pow Hwee owns | Backend plumbing; parallel to above. Pow Hwee to confirm task breakdown at planning |
| OTEP-318 | Filter by category | ⚠️ **Conditional** — OTEP-289 spike still shows no written output; Jira description is empty | Do not commit until Pow Hwee presents mapping table + go/no-go in the planning room |

**Not in Sprint 3:**
- OTEP-71/110/304/305 — auth epic deferred to Sprint 4+. No WOG AD UAT environment. Do not re-enter.
- OTEP-130 — full FormSG webhook integration. Sprint 4 (confirmed by OTEP-194 spike output).
- OTEP-87 competency section — Sprint 4+. Open item #18 unresolved.

---

## Carry-over AC Fixes — ✅ Done

**OTEP-128** — "This opportunity is closed" notice AC removed. ✅ Pow Hwee's flagged conflict with OTEP-129 is resolved. Minor gap remaining: Pow Hwee also suggested adding a server error state AC ("if the system cannot load the opportunity, show a generic error + retry option") — not in Jira ACs yet. Not a planning blocker; flag it to Pow Hwee as a first-day refinement.

**OTEP-129** — Visibility rule AC ("Closed or expired postings are hidden from the listing") removed. ✅ Story now cleanly owns the "Closing soon" badge (≤7 days) and the deep-link behaviour for already-closed opportunities. No conflict with OTEP-85.

---

## Capacity Flags

- **Thomas is the only FE developer — and now has 8 Sprint 3 items.** Carry-overs (OTEP-128, OTEP-129, OTEP-267) + new Sprint 3 FE work (OTEP-86, OTEP-317, OTEP-87, OTEP-319) + OTEP-324 (OAuth token rotation, just added) = 8 items through one person. Surface this at planning. Let Thomas size and sequence — don't assume it all fits.
- **OTEP-87 and OTEP-319 cannot start until OTEP-128 closes.** The whole apply loop is blocked behind that carry-over. Accept the sequencing dependency out loud so Thomas can plan his first two days accordingly.
- **OTEP-313 (Léo, OTG ingest table)** is still In Progress at sprint end. If it doesn't close by EOD 29 May, it carries into Sprint 3 and stacks with OTEP-192 (the recurring import job). Two ingest stories on Léo at the same time.
- **OTEP-192 has three open questions** that need answers before Léo or Pow Hwee can start building (file arrival mechanism, ingestion cadence, flag vs auto-deactivate). These are not blocking planning — they can be resolved in the first days of Sprint 3 — but flag them as Day 1 actions, not "figure it out later" items.
- **No public holidays** in Sprint 3 (2–13 Jun). Full 2-week window.
- **Fullstack dev joining from Core squad in Sprint 4** — confirmed 2026-05-22. Not available for Sprint 3.

---

## DoR Status — Sprint 3

| Story | DoR status | Remaining action |
|---|---|---|
| OTEP-192 | ✅ Grooming-ready | 3 open questions to resolve Day 1 of Sprint 3 |
| OTEP-86 | ✅ Grooming-ready | Tooltip copy needs Amber + BO sign-off before build. OTEP-92 description needed |
| OTEP-317 | ✅ Grooming-ready | None |
| OTEP-87 | ✅ Grooming-ready | Confirm AC 6 doesn't conflict with OTEP-128 click-through state handling |
| OTEP-319 | ✅ Grooming-ready | Tracking param question for engineering |
| OTEP-128 | ✅ Carry-over — AC conflict resolved | Minor: add server error AC (Pow Hwee's suggestion) as Day 1 refinement |
| OTEP-129 | ✅ Carry-over — AC conflict resolved | None |
| OTEP-267 | ⚠️ Carry-over | API dep: total_count in GET /opportunities response |
| OTEP-324 | ✅ In Sprint 3 — Thomas assigned | Monitor Thomas capacity impact |
| OTEP-271 | ⚠️ No AC file | Pow Hwee confirms task breakdown at planning |
| OTEP-203 | ⚠️ No AC file | Pow Hwee confirms task breakdown at planning |
| OTEP-191 | ✅ Done — resolved at infra layer | OTEP-330 (IAM audit) and OTEP-329 (Keycloak secret) created as follow-ups; both Backlog |
| OTEP-318 | ❌ Conditional | Jira description empty; OTEP-289 spike output needed before committing |
| OTEP-192 | ✅ Story written | Set Jira assignee at planning |
| Sprint 3 goal | ❌ Not set | Set in Jira after the session |

---

## Story Prioritisation (Michelle's recommendation)

Walk through in this order. Team sizes and self-selects — this is the PM's recommended sequence.

1. **OTEP-128** — carry-over, must close first. Blocks OTEP-87 and OTEP-319.
2. **OTEP-192** — OTG import job. Critical path for live data. Assign today.
3. **OTEP-86 + OTEP-317** — type filter + clear. Delivers the discoverability half of the sprint goal.
4. **OTEP-129** — open/closed indicator. Small; completes the Sprint 2 listing work.
5. **OTEP-267** — pagination carry-over. Thomas owns; depends on OTEP-85 being live.
6. **OTEP-87** — enhanced detail with apply CTA. Depends on OTEP-128 closing.
7. **OTEP-319** — FormSG apply redirect. Depends on OTEP-87. Completes the browse-to-apply loop.
8. **OTEP-324** — OAuth token rotation. Thomas owns; infrastructure work that protects Sprint 3 QA from session disruption. Size alongside his other items.
9. **OTEP-271 + OTEP-203** — POCDEX plumbing. Parallel backend; Léo + Pow Hwee. Unblocks Sprint 4.
10. **OTEP-318** — conditional. Only enter if Pow Hwee has spike output in the room and Thomas confirms headroom.

**Cut-line if Thomas runs out of capacity:** Drop OTEP-318 first. Then negotiate OTEP-267 into early Sprint 4 if pagination has no live data to page through yet. Do not cut OTEP-192, OTEP-86, or OTEP-319.

---

## Michelle's Opening Statement

> "Sprint 3 takes what we proved in Sprint 2 and makes it actually useful. We want an officer to be able to filter down to the right opportunities and click Apply — not just browse a list. The things that need to land to get there: the OTG import job so we're showing live data, the type filter so officers can narrow their search, and the FormSG apply redirect so the journey completes. Before we size Sprint 3 stories, I want to confirm with Thomas what's realistic to close on carry-overs — OTEP-128, OTEP-129, and OTEP-267 are all coming in, and OTEP-87 and OTEP-319 can't start until OTEP-128 is done."

---

## What NOT to Do in This Session

- **Don't assign stories to engineers — let them self-select.** Thomas especially needs space to say what's realistic before new Sprint 3 stories land on his plate.
- **Don't commit OTEP-318 without the OTEP-289 spike output in the room.** If Pow Hwee can't present the mapping table and go/no-go, leave it out.
- **Don't plan OTEP-87 as a Day 1 story.** It can't start until OTEP-128 closes. Accept this dependency explicitly — don't let it surface as a surprise mid-sprint.
- **Don't accept "we'll figure it out" on OTEP-271 and OTEP-203.** These are backend stories with no task breakdown in our docs. Pow Hwee should have subtask-level clarity before they're committed.
- **Don't let OTEP-192 open questions drift.** The three questions (file mechanism, cadence, flag vs deactivate) are fast to answer — get Pow Hwee and Rama to agree on them in the first day, not after the job is half built.

---

## What Changed Since Last Brief (updated post story sync)

| Story | Before | Now |
|---|---|---|
| OTEP-192 | ❌ Mechanism-AC only, not groom-able | ✅ Full user story + testable ACs; 3 open questions explicitly called out |
| OTEP-87 | ⚠️ Jira ACs included competency scope | ✅ ACs reconciled to apply CTA only; competency explicitly out of scope |
| OTEP-319 | ⚠️ Pre-fill question open | ✅ Pre-fill dropped (Squad Sync 2026-05-26); tracking param question minor |
| OTEP-86 | ✅ (no change) | ✅ Tooltip copy flagged as needing Amber + BO sign-off |
| OTEP-317 | ✅ (no change) | ✅ No change |
| OTEP-128 | ⚠️ AC conflicts flagged by Pow Hwee | ✅ "Opportunity is closed" AC removed; minor server error gap (Day 1 refinement) |
| OTEP-129 | ⚠️ Visibility rule AC conflict | ✅ Visibility rule removed; story now owns badge + deep-link only |
| OTEP-191 | ⚠️ "Verify or close" DoR blocker | ✅ Confirmed Done — credential management handled at AWS infra layer (Pow Hwee, 2026-05-21) |
| OTEP-324 | Not in brief | ✅ New Sprint 3 task (OAuth token rotation) — Thomas assigned; adds to capacity |
| OTEP-333 | Not tracked | New backlog story: ref_job_family/function tables — blocked on POCDEX team finalising taxonomy. Relevant to open item #18 (Imelda sync) |

---

*Generated: 2026-05-27 | Updated: full sync (Sprint 2 + Sprint 3 + Backlog) | Sources: jira-sync (2026-05-27), sprint-status.md (2026-05-21), open-items.md (2026-05-22)*
