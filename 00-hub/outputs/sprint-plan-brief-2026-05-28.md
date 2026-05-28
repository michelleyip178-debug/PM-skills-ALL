# Sprint Planning Brief — Sprint 3
**Planning session:** Thu 28 May 2026 (today) | **Sprint 3 dates:** 2 Jun – 13 Jun 2026

---

## Proposed Sprint Goal

**Option A — Conservative:**
> By end of Sprint 3, an officer can filter OTG opportunities by type and initiate an application via FormSG redirect, using live data delivered by the OTG recurring import job.

**Option B — Ambitious:**
> By end of Sprint 3, an officer can discover, filter, and apply to any active OTG opportunity (Internal Job, STIP, or Gig) — completing the full browse-to-apply loop, end-to-end, powered by live daily-imported OTG data.

**Recommendation:** Open with Option A. Upgrade to Option B once Thomas confirms carry-overs (OTEP-128, OTEP-129, OTEP-267) don't consume his first week. Option B depends on OTEP-128 closing early enough to unblock OTEP-87 and OTEP-319 in the same sprint.

---

## Candidate Stories

| Story ID | Title | Readiness | Risk |
|---|---|---|---|
| ~~OTEP-128~~ | View opportunity detail page *(carry-over)* | ✅ AC conflicts resolved | 🟢 **In Progress as of today** (Thomas). OTEP-327 (design system subtask) still Backlog. Server error AC gap — Day 1 refinement with Pow Hwee |
| ~~OTEP-129~~ | Open/closed indicator *(carry-over)* | ✅ Clean scope — badge + deep-link only | Thomas assigned |
| ~~OTEP-267~~ | Pagination *(carry-over)* | ✅ ACs present | ⚠️ API dep: `total_count` in GET /opportunities response — Pow Hwee to confirm |
| OTEP-192 | OTG recurring import job | ✅ ACs written; auto-deactivate resolved (2026-05-28) | 2 open questions remain: file arrival mechanism + cadence. Confirm at planning; resolve Day 1 |
| OTEP-86 | Filter by opportunity type | ✅ ACs scoped to type filter only | Tooltip copy (STIP/Gig/Internal Job/SJR) needs Amber + BO sign-off before build. OTEP-92 subtask has no description — ask Pow Hwee |
| OTEP-317 | Clear filters | ✅ Clean ACs | Depends on OTEP-86 |
| OTEP-87 | Enhanced detail — apply CTA only | ✅ Competency scope explicitly out | Blocked until OTEP-128 closes. Confirm AC 6 (state preservation) doesn't double-count with OTEP-128 |
| OTEP-319 | Apply via FormSG basic redirect | ✅ Pre-fill dropped; ACs tight | Minor: confirm whether tracking params should be appended (engineering call) |
| OTEP-324 | OAuth token rotation (NextAuth + Keycloak) | ✅ Thomas assigned | Dev/QA story — adds to Thomas's load |
| OTEP-271 | Local POCDEX database | ⚠️ No AC file in docs | Pow Hwee owns; confirm task breakdown in room |
| OTEP-203 | Standalone POCDEX API service | ⚠️ No AC file in docs | Pow Hwee owns; confirm task breakdown in room |
| OTEP-318 | Filter by category | ❌ Conditional — Jira description empty | Only commit if Pow Hwee presents OTEP-289 spike mapping table + go/no-go today |

**Not in Sprint 3:**
- OTEP-71/110/304/305 — auth epic, Sprint 4+. No WOG AD UAT environment. Do not re-enter.
- OTEP-130 — FormSG webhook. Sprint 4.
- OTEP-87 competency section — Sprint 4+. Open item #18 unresolved.

---

## Capacity Flags

- **Thomas has 8 Sprint 3 items.** Carry-overs (OTEP-128, OTEP-129, OTEP-267) + new FE (OTEP-86, OTEP-317, OTEP-87, OTEP-319) + OTEP-324 = 8 through one FE developer. Raise this first. Let Thomas size and self-select — don't assume it all fits.
- **OTEP-87 and OTEP-319 are sequentially blocked behind OTEP-128.** Thomas started OTEP-128 today — OTEP-87 and OTEP-319 are still blocked until it closes. Watch for OTEP-327 (design system subtask, still Backlog) as the last gating item.
- **OTEP-313 (Léo, OTG ingest table) may carry from Sprint 2.** If it doesn't close today, Léo starts Sprint 3 with two ingest stories (OTEP-313 + OTEP-192) simultaneously.
- **OTEP-192: 2 open questions remain.** File arrival mechanism and ingestion cadence — quick answers from Pow Hwee + Rama. Flag as Day 1 sprint actions.
- **No public holidays** in Sprint 3 (2–13 Jun). Full capacity.
- **Fullstack dev joining Sprint 4** — not available for Sprint 3.

---

## DoR Status

| Story | DoR status | Action |
|---|---|---|
| OTEP-192 | ✅ Ready | Set assignee today; resolve file mechanism + cadence Day 1 |
| OTEP-86 | ✅ Ready | Tooltip copy sign-off with Amber + BO before build; OTEP-92 description needed |
| OTEP-317 | ✅ Ready | None |
| OTEP-87 | ✅ Ready | Confirm AC 6 doesn't conflict with OTEP-128 state handling |
| OTEP-319 | ✅ Ready | Tracking param question — engineering confirms |
| OTEP-128 | ✅ **In Progress** — Thomas started today | Server error AC — Day 1 refinement |
| OTEP-129 | ✅ Carry-over, conflicts resolved | None |
| OTEP-267 | ✅ Carry-over | total_count API dep — Pow Hwee confirms |
| OTEP-324 | ✅ In Sprint 3 | Monitor Thomas capacity |
| OTEP-271 | ⚠️ No task breakdown | Pow Hwee in room |
| OTEP-203 | ⚠️ No task breakdown | Pow Hwee in room |
| OTEP-191 | ✅ Done (infra layer) | No action |
| OTEP-318 | ❌ Conditional | Spike output in room or leave it out |
| Sprint 3 goal | ❌ Not set | Set in Jira immediately after session |

---

## Story Prioritisation (Michelle's recommended order)

1. **OTEP-128** — carry-over; unblocks OTEP-87 and OTEP-319. Thomas's Day 1.
2. **OTEP-192** — OTG import job. Critical path for live data. Set assignee now.
3. **OTEP-86 + OTEP-317** — type filter + clear. Delivers the discoverability half of the sprint goal.
4. **OTEP-129** — open/closed indicator. Small; completes Sprint 2 listing work.
5. **OTEP-267** — pagination. Thomas; depends on OTEP-85 being live.
6. **OTEP-87** — enhanced detail + apply CTA. Depends on OTEP-128.
7. **OTEP-319** — FormSG redirect. Depends on OTEP-87. Completes the apply loop.
8. **OTEP-324** — OAuth token rotation. Thomas; size alongside his other items.
9. **OTEP-271 + OTEP-203** — POCDEX plumbing. Parallel backend; Léo + Pow Hwee.
10. **OTEP-318** — conditional only.

**Cut-line:** Drop OTEP-318 first. Then OTEP-267 if Thomas is at ceiling (pagination needs live data anyway — nothing to page through until OTEP-192 lands). Do not cut OTEP-192, OTEP-86, or OTEP-319.

---

## Michelle's Opening Statement

> "Sprint 3 takes what we proved in Sprint 2 and makes it actually useful. We want an officer to be able to filter down to the right opportunities and click Apply — not just browse a list. To get there, three things need to land: the OTG import job so we're showing live data, the type filter so officers can narrow their search, and the FormSG apply redirect so the journey completes. Before we size anything, I want to confirm with Thomas what's realistic on carry-overs — OTEP-128, OTEP-129, and OTEP-267 are all coming in, and OTEP-87 and OTEP-319 can't start until OTEP-128 is done."

---

## What NOT to Do in This Session

- **Don't assign stories — let engineers self-select.** Thomas especially needs to name his own ceiling before new items land on him.
- **Don't commit OTEP-318 without Pow Hwee's OTEP-289 spike output in the room.** Mapping table + go/no-go, or it stays out.
- **Don't treat OTEP-87 as a Day 1 story.** It's blocked until OTEP-128 closes. Say it explicitly.
- **Don't accept "we'll figure it out" on OTEP-271 and OTEP-203.** Pow Hwee should have task-level clarity before they're committed.
- **Don't let OTEP-192's two remaining questions drift** (file mechanism, cadence). They're fast to answer — confirm with Pow Hwee + Rama in the room or flag as Day 1.

---

## What's New Since Yesterday's Brief

| Item | Change |
|---|---|
| OTEP-192 | Auto-deactivate open question resolved (2026-05-28 — confirmed in Jira description). Now 2 open questions, not 3 |
| OTEP-128 | **Backlog → In Progress** (2026-05-28). Thomas picked it up today — carry-over is actively moving |
| Sprint 2 board | OTEP-129, OTEP-267 still Backlog (confirmed carry-overs). OTEP-128 now In Progress |

---

*Final version for Thu 28 May planning session. Previous prep brief: sprint-plan-brief-2026-05-27.md*
