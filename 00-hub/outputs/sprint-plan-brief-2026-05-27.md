# Sprint Planning Brief — Sprint 3
**Prepared:** 27 May 2026 | **Planning session:** Thu 29 May 2026
**Sprint 3 dates:** 2 Jun – 13 Jun 2026

---

## Proposed Sprint Goal

**Option A — Conservative:**
> By end of Sprint 3, an officer can filter OTG opportunities by type and initiate an application via FormSG redirect, using live data delivered by the OTG recurring import job.

**Option B — Ambitious:**
> By end of Sprint 3, an officer can discover, filter, and apply to any active OTG opportunity (Internal Job, STIP, or Gig) — completing the full browse-to-apply loop, end-to-end, powered by live daily-imported OTG data.

**Recommendation:** Start with Option A and let the team upgrade to Option B if capacity allows after carry-over stories are accounted for. Option B depends on OTEP-128 closing in Sprint 2 — which is not confirmed as of today.

---

## Candidate Stories

| Story ID | Title | Readiness | Risk |
|---|---|---|---|
| ~~OTEP-128~~ | View opportunity detail page *(carry-over)* | ACs written; sub-tasks in QA/In Progress | ⚠️ Carry-over — OTEP-327 (design system sub-task) still Backlog. Must close early Sprint 3 to unblock OTEP-87 |
| ~~OTEP-129~~ | Open/closed indicator *(carry-over)* | ACs in sprint-checklists; design confirmed | ⚠️ Carry-over — Thomas assigned, not started. Scope: "Closing soon" badge (≤7 days) + deep-link error state |
| ~~OTEP-267~~ | Pagination *(carry-over)* | ACs written; API dep on `total_count` | ⚠️ Carry-over — Thomas assigned, not started. API contract dep confirmed |
| OTEP-192 | OTG recurring import job | ❌ **Not ready** — mechanism AC only; no user story format | Critical path for live data. Rewrite before planning (PM action — today) |
| OTEP-86 | Filter by opportunity type | ✅ ACs written (filters.md); Amber's design confirmed | Depends on OTEP-85 closing (Sprint 2). Low risk if Sprint 2 delivers |
| OTEP-317 | Clear filters and reset view | ✅ ACs written; pairs with OTEP-86 | Depends on OTEP-86. Thomas FE only |
| OTEP-87 | Enhanced detail page — apply CTA only | ⚠️ Partial — ACs in otg-lifecycle.md are clean; **Jira ACs include competency scope that must be removed before grooming** | Depends on OTEP-128 closing. Competency section explicitly deferred (Sprint 4+) |
| OTEP-319 | Apply via FormSG — basic redirect | ✅ `formsg_url` confirmed; ACs written | Depends on OTEP-87 (detail page must have Apply CTA). Sequential dependency |
| OTEP-271 | Local POCDEX database (container + schema) | ⚠️ No AC file in our docs — Pow Hwee owns | Backend plumbing; parallel to above. Unblocks Sprint 4 ringfencing |
| OTEP-203 | Standalone POCDEX API service | ⚠️ No AC file in our docs — Pow Hwee owns | Backend plumbing; parallel to above. Staggered per 2026-05-20 decision |
| OTEP-318 | Filter by category | ⚠️ **Conditional** — only if OTEP-289 spike output is green | No Jira description yet. Ask Pow Hwee for spike output status before committing |

**Stories NOT in Sprint 3:**
- OTEP-71/110/304/305 (auth epic) — moved to Sprint 4+. No WOG AD UAT environment. Do not re-enter.
- OTEP-130 (full FormSG integration with webhook) — Sprint 5. OTEP-194 spike confirmed basic redirect is the MVP path.
- OTEP-87 competency section — Sprint 4+. Open item #18 (Imelda sync) unresolved.

---

## Capacity Flags

- **Thomas is the only FE developer.** He has 3 likely carry-overs (OTEP-128, OTEP-129, OTEP-267) plus 4 new Sprint 3 FE stories (OTEP-86, OTEP-317, OTEP-87, OTEP-319). That's 7 stories through one person. Surface this at planning — team needs to size and sequence explicitly, not assume everything fits.
- **Thomas carry-over creates a sequencing trap.** OTEP-87 and OTEP-319 (the apply loop) can't start until OTEP-128 closes. If OTEP-128 takes 2–3 days into Sprint 3, Thomas has a short window for the rest. The sprint goal depends on getting OTEP-128 done first.
- **Léo's OTEP-313** (OTG ingest table) is still In Progress at sprint end. If it doesn't close by EOD Fri 29, it carries into Sprint 3 and stacks on top of OTEP-192 (the recurring import job). Two ingest stories + Léo at the same time.
- **No public holidays in Sprint 3 window** (2–13 Jun). Full capacity — no buffer events.
- **Fullstack dev joining from Core squad in Sprint 4** (per 2026-05-22 decision). Not available for Sprint 3 — don't plan around it.
- **OTEP-289 spike status unknown.** Timebox was May 19–20; Jira still shows Backlog. Confirm with Pow Hwee today. If no written output exists, OTEP-318 cannot be committed.

---

## DoR Blockers — Sprint 3

| Blocker | Owner | Status |
|---|---|---|
| OTEP-192 rewritten as user story (user + outcome + testable ACs) | Michelle | ❌ PM action — do this today |
| OTEP-87 Jira ACs reconciled — remove competency scope, align with otg-lifecycle.md | Michelle | ❌ PM action — do this today |
| OTEP-289 spike output — written recommendation + go/no-go for OTEP-318 | Pow Hwee | ❓ Ask at standup / async today |
| OTEP-318 Jira description written (ACs from filters.md) | Michelle | ❌ Only if spike is green |
| OTEP-128 closes in Sprint 2 or confirmed carry-over with clear day-1 task | Thomas | ⚠️ Confirm at planning |
| OTEP-271 + OTEP-203 ACs / task breakdown | Pow Hwee | ⚠️ Pow Hwee owns — confirm at planning |
| Sprint 3 goal set in Jira | Michelle | ❌ Post-planning action |

---

## Story Prioritisation (Michelle's recommended order)

This is the order to walk through in the room. The team sizes and self-selects — this is the PM's recommended priority sequence, not an assignment.

1. **OTEP-128** — carry-over, unblocks the whole apply loop. Day 1 priority.
2. **OTEP-192** — OTG import job. Critical path for live data backing the sprint goal.
3. **OTEP-86 + OTEP-317** — type filter + clear. Directly delivers the discoverability half of the sprint goal.
4. **OTEP-129** — open/closed indicator. Small; completes Sprint 2 listing work.
5. **OTEP-267** — pagination carry-over. Dependent on OTEP-85 being live; Thomas owns.
6. **OTEP-87** — enhanced detail page. Depends on OTEP-128 closing.
7. **OTEP-319** — FormSG apply redirect. Depends on OTEP-87. Completes the browse-to-apply loop.
8. **OTEP-271 + OTEP-203** — POCDEX plumbing. Parallel backend work; unblocks Sprint 4. Léo + Pow Hwee.
9. **OTEP-318** — category filter. Conditional and lowest priority. Only commit if OTEP-289 output is green and Thomas has capacity after items 3–7.

**Cut-line if Thomas runs out of capacity:** Drop OTEP-318 first, then OTEP-267 (pagination works fine without it for Sprint 3), then negotiate OTEP-87/319 into the first week of Sprint 4. Do not cut OTEP-192 or OTEP-86.

---

## Michelle's Opening Statement

> "Sprint 3 takes what we proved in Sprint 2 — the listing and detail page — and makes it actually useful. We want an officer to be able to filter down to the right opportunities and click Apply. Three things have to land to get there: the OTG import job so we're showing live data, the type filter so officers can narrow their search, and the FormSG apply redirect so the journey actually completes. We're also carrying in OTEP-128, OTEP-129, and OTEP-267 from Sprint 2 — before we size Sprint 3 stories, I want to confirm with Thomas what's realistic to close by end of day Thursday."

---

## What NOT to Do in This Session

- **Don't assign stories to engineers — let them self-select.** Thomas in particular should have space to say how many carry-overs are realistic before new Sprint 3 stories land.
- **Don't commit OTEP-318 without seeing the OTEP-289 spike output.** If Pow Hwee can't produce the written recommendation in the room, leave it out.
- **Don't let OTEP-192 go into Sprint 3 with mechanism-only ACs.** The story currently says what the system does, not what an officer or operator can verify. It needs testable ACs before it can be groomed.
- **Don't plan around OTEP-87 starting Day 1.** It can't start until OTEP-128 closes. Accept the sequencing dependency out loud so Thomas doesn't get blocked silently.
- **Don't accept "we'll figure it out" on OTEP-271/203 (POCDEX plumbing).** These are backend stories with no AC file in our docs. Pow Hwee should have task-level clarity before they're committed.

---

## PM Pre-Work — Do Before Tomorrow's Session

| Action | Urgency |
|---|---|
| Rewrite OTEP-192 as a user story with testable ACs | 🔴 Today — cannot groom without this |
| Reconcile OTEP-87 Jira ACs — remove competency scope | 🔴 Today |
| Chase Pow Hwee: OTEP-289 spike — does written output exist? | 🔴 Today — gates OTEP-318 |
| Write OTEP-318 Jira description (from filters.md) | 🟡 Only if spike output is green |
| Run `/sprint-plan-prep` refresh tomorrow morning | 🟡 Morning of |
| Set Sprint 3 goal in Jira post-planning | 🟢 Post-session |

---

*Generated: 2026-05-27 | Sprint-status source: sprint-status.md (2026-05-21) | Jira sync: 2026-05-27*
