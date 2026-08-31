# Current Sprint Context

> Update this file at the start of each sprint.
> All commands read this file — keeping it current makes every
> output accurate and specific to where you actually are.

> ✅ **Resolved 2026-07-16:** the stale-2026-07-01 flag below and the "Sprint 6 not started" line above it were both superseded by the 2026-07-14 sync (Sprint 6 confirmed `active` since midday that day) and are no longer accurate — left visible in the history below for traceability, not as current state. Current Sprint 6 counts refreshed against a fresh 2026-07-16 pull; see the Sprint 6 section.

---

## Sprint details
- **Sprint number:** **Sprint 8 — CLOSED (11–23 Aug 2026, closed 1 day early against its 24 Aug scheduled end; sprint 34622, `completeDate` 2026-08-23).** Goal was: "Clean up defects from Phase 1 - UAT and enable Phase 2 - UAT on Ringfencing and Competency Matching." Final state: 73 issues — 52 Done, 8 In Progress, 4 QA, 8 Backlog, 1 To Do; 20 did not reach Done (see Sprint 8 section below). The week of 24–28 Aug is **Phase 3 UAT by design** (PM-confirmed 2026-08-24). **Sprint 9 (id 42637) is confirmed `future` state in live Jira as of 2026-08-31, dates 6–20 Sep — NOT "w/c 31 Aug" as previously tracked here.** That prior claim was sourced only to a PM verbal confirmation (2026-08-24) and was never checked against Jira directly; this pull corrects it. This leaves 31 Aug–5 Sep as a week with no active Pathfinder sprint container — **confirmed intentional by PM 2026-08-31**, not a planning gap. Sprint 9 already holds 21 issues (mostly Backlog/Done, one In Progress) but none of the 6 WOG AD/auth tickets (OTEP-71/594/331/110/305/111 — all confirmed `sprint: []`, i.e. unassigned to any sprint, as of this pull).
- **Sprint 2:** closed (Sprint 34616) — 6 stories Done at close.
- **Sprint 3 dates:** 2–14 Jun 2026 (Pathfinder Sprint 3 / Sprint 34617). Final state: 23 Done, 9 in QA at close (carry-in to S4), 4 Backlog carry-in.
- **Sprint 4 dates:** 15–26 Jun 2026. CLOSED 29 Jun 2026. Final state: 28 Done, 11 in QA (carry-in to S5), 11 In Progress (carry-in), 1 To Do, 12 Backlog carry-in.
- **Sprint 5 dates:** 29 Jun – 12 Jul 2026. Goal: officers browsing the opportunity listing can see which roles they're eligible for and filter by job category — so they spend less time on opportunities that aren't relevant to them.

**Confirmed sprint schedule (updated 2026-06-23):**

| Sprint | Dates | Notes |
|--------|-------|-------|
| S5 | 29 Jun – 12 Jul | |
| S6 | 13 Jul – 26 Jul | |
| S7 | 27 Jul – 9 Aug | |
| S8 | 11–23 Aug | CLOSED 23 Aug (1 day early). UAT Phase 1–2 ran during it. |
| Phase 3 UAT | w/c 24 Aug | Phase 3 UAT by design (PM-confirmed 2026-08-24) — not a sprint. |
| S9 | 6–20 Sep (live Jira, `future` state) | Corrected 2026-08-31 from "w/c 31 Aug" — that date was a PM verbal confirmation never checked against Jira. Scope vs pure VAPT/UAT-continuation still to confirm. 31 Aug–5 Sep has no active Pathfinder sprint container — confirmed intentional by PM 2026-08-31. |

**Post-dev timeline (updated 2026-08-28 per PM):** Code freeze ~28 Aug → **VAPT 7 Sep – 8 Nov** (POCDEX VAPT decoupled 25 Aug; scope expanded to 5 POCDEX APIs; target completion 8 Nov per 25 Aug programme coordination) → **MVP launch targeted 24–25 Nov 2026.** ⚠️ The old chain (Deploy 19–23 Oct → Soft launch 26–30 Oct → First release week of 2 Nov) is superseded. AI IDSC approval (~1 Sep) and NCS PO (by 4 Sep) are hard gates on this path.

## Sprint goal
**Sprint 2:** By end of Sprint 2, an officer can open OTEP, see every published OTG opportunity on a listing page (newest first), and click into a detail page for any opportunity — proving the Listing → Detail end-to-end journey works.

**Sprint 3:** By end of Sprint 3, an officer can find relevant opportunities using filters and successfully initiate an application to any active OTG opportunity (except SJRs), powered by live imported data.

**Sprint 4 (agreed at planning 2026-06-11):** Deliver a complete, usable opportunity listing experience — officers can search, filter, and sort opportunities, understand what each type means, and trust that the data they're seeing is current and accurate.

**Sprint 5 (confirmed at start 2026-06-29):** By end of sprint, officers browsing the opportunity listing can see which roles they're eligible for and filter by job category — so they spend less time on opportunities that aren't relevant to them.

---

## Sprint 6 — ✅ ACTIVE (13–26 Jul 2026)

> Source: OTEP-Pathfinder Sprint 6 (Sprint 34620). **Live pull: 2026-07-23 (direct Jira REST API, `/rest/api/3/search/jql`).** 95 issues total (up from 91 on 2026-07-20 — OTEP-755, 768, 791, 803 added). Goal: still not formally set in Jira as of this pull.

**In Progress (16):** OTEP-88 (C@G listing, Léo), OTEP-723 (integration testing, Léo), OTEP-305 (login/logout, unassigned), OTEP-405 (keyword search, Thomas), OTEP-386 (opportunity type tooltip, Thomas), OTEP-439 (ineligible states design, Amber), OTEP-350 (WOG AD onboarding, Fabian), OTEP-361 (ADR forum, Pow Hwee), OTEP-283 (Ministry icons, unassigned), OTEP-349 (competency matching spike, Pow Hwee), OTEP-437 (filter by job family, Hao Eng), OTEP-390 (ringfenced detail states, Thomas), OTEP-131 (broken FormSG link, Thomas), OTEP-595 (Keycloak realm displayName, Pow Hwee), OTEP-444 (Azure/Entra AD mock, Léo), OTEP-683 (opportunity detail update, Thomas)

**In QA (5):** OTEP-87 (C@G opp detail, Thomas), OTEP-438 (admin view, Hao Eng), OTEP-392 (federated logout, Thomas), OTEP-505 (CFT upload/webhook, Hao Eng), OTEP-304 (stay-authenticated, Hao Eng)

**To Do (4):** OTEP-667 (BUG — opportunities details page, unassigned), OTEP-668 (BUG — search opportunities, Thomas), OTEP-445 (POCDEX code table import spike), OTEP-663 (BUG — competencies listing, Thomas)

**Done (46):** OTEP-86, OTEP-380, OTEP-381, OTEP-375, OTEP-374, OTEP-482, OTEP-539, OTEP-536, OTEP-666, OTEP-268, OTEP-326, OTEP-325, OTEP-369, OTEP-368, OTEP-128, OTEP-334, OTEP-327, OTEP-314, OTEP-495, OTEP-496, OTEP-284, OTEP-440, OTEP-441, OTEP-289, OTEP-129, OTEP-362, OTEP-363, OTEP-367, OTEP-276 (design-system spike — moved from In Progress), OTEP-541, OTEP-540 (Michelle), OTEP-406, OTEP-571, OTEP-484, OTEP-499, OTEP-662 (login-error investigation — moved from Backlog), OTEP-752 (integration testing harness — moved from In Progress), OTEP-613, OTEP-85, OTEP-677 (OTG/C@G import bug — moved from To Do), OTEP-193, OTEP-288, OTEP-296 (Michelle), OTEP-313, OTEP-320, OTEP-170

**Backlog (24):** OTEP-404, OTEP-329, OTEP-393, OTEP-403, OTEP-348, OTEP-408, OTEP-409, OTEP-336, OTEP-570, OTEP-130, OTEP-502 (Thomas), OTEP-569, OTEP-679 (Fanxu), OTEP-483, OTEP-485 (Léo), OTEP-659 (Thomas), OTEP-680 (Léo), OTEP-681, OTEP-682, OTEP-684, OTEP-755 (new — seed POCDEX ref agency code table), OTEP-768 (new — Bug, Hao Eng, cft_upload db table scope), OTEP-791 (new — Sub-task, BUG C@G import not working in QA), OTEP-803 (new — Sub-task, investigate date timezone)

**Net movement since 2026-07-20 pull:** OTEP-276, 662, 677, 752 moved to Done (4 fixes/spikes closed out). 4 new sub-tasks/bugs added to Backlog (OTEP-755, 768, 791, 803). 8 tickets that had been sitting in the Sprint 6 folder but were actually reassigned to future sprints or dropped from all sprints (OTEP-110, 111, 331, 425, 594, 614, 615, 71) relocated to `Backlog/` folder — cache now correctly reflects that these are not part of the active sprint. **2026-07-24 update:** 4 of those 8 (OTEP-71, 110, 111, 594) relocated a second time, from `Backlog/` into the newly-created `OTEP-Pathfinder-12541-Sprint-7-34621/` folder — see the new Sprint 7 section below.

**PM-owned:** OTEP-296 ✅ Done, OTEP-540 ✅ Done. No other Michelle stories active in S6.

**2026-07-14 jira-sync — Pathfinder scope:** Relocated 76 files from the `Sprint-34619-OTEP-Pathfinder-Sprint-5` folder to `Sprint-34620-OTEP-Pathfinder-Sprint-6` (live Jira confirms these tickets now sit in Sprint 6). 2 files stayed in the Sprint 5 folder correctly (OTEP-322, OTEP-328 — both Done, historically placed in earlier closed sprints per Jira's own sprint history). 1 stale duplicate (OTEP-613) removed from the Sprint 5 folder — canonical copy already existed in Sprint 6. 4 status corrections applied: OTEP-283 (In Progress→QA), OTEP-505 (In Progress→QA), OTEP-541 (In Progress→Done), OTEP-86 (QA→Done). All 98 files in the Sprint 6 folder now carry a `Sprint:` field and today's sync stamp.

**✅ Resolved 2026-07-14 midday:** Sprint 6 (34620) is now Jira state `active` — someone hit "Start Sprint" between this morning's pull (still `future`) and this midday pull. No longer a flag.

**2026-07-14 afternoon jira-sync (3rd pass today) — 1 delta since midday:** OTEP-437 (filter by job family) moved Backlog→To Do, assigned to Hao Eng. OTEP-505 re-confirmed unchanged again (QA, Hao Eng) — three independent pulls today (morning, midday, afternoon) all agree, consistent with today's separate confirmation that OTEP-505 is resolved/ready for QA. Core board's 4 cached tickets (OTEP-78/82/83/84) unchanged since midday. The 8 out-of-sprint leftover tickets (OTEP-110/111/331/425/594/614/615/71) are unchanged — still flagged, still no Sprint 7/8 folders to relocate into.

**2026-07-14 midday jira-sync (2nd pass today) — 3 further deltas found since the morning sync:**
- OTEP-613: Backlog→QA, assignee N/A→Thomas Huchedé
- OTEP-683: Backlog→In Progress
- OTEP-604: relocated from Sprint-6 cache folder to Sprint-5 folder — live Jira places it in the closed Sprint 5 (34619), not Sprint 6, despite being Done. Cache had it misfiled.
- **8 tickets confirmed moved out of Sprint 6 to future sprints, left in place (flagged, not relocated — no Sprint 7/8 Pathfinder folders exist yet):** OTEP-110, OTEP-111 → Sprint 7; OTEP-331, OTEP-614, OTEP-615 → Sprint 8; OTEP-71 → Sprint 7; OTEP-425 → no sprint (removed from all sprints in Jira). These are the original 07-07 provisional-pull files that predate this morning's 76-file rollover — worth a follow-up run once Sprint 7/8 folders exist or get created.
- **OTEP-505 re-confirmed unchanged: still QA, still Hao Eng.** No movement between the morning and midday pulls — this is a real stall, not a sync artifact.

## OTEP-Core Sprint 8 (34612) — 🟡 ACTIVE, overrunning its own end date

> **Live pull: 2026-08-24.** Sprint state `active`, `endDate` was 2026-08-20T16:00 — **4 days past its own scheduled end with no successor sprint started.** Same shape as Pathfinder's pre-correction Sprint 9 gap; unconfirmed whether this is deliberate (e.g. also absorbed into this week's Phase 3 UAT) or an actual planning gap. **Flagged, not assumed** — needs a person to confirm, the same way Pathfinder's was.
>
> **238 issues total (up sharply from 100 on the 2026-08-20 pull)** — Done 110, QA 50, Backlog 31, In Progress 6, To Do 2, UAT 1. The jump from 100→238 issues is too large to be pure status movement; likely additional stories rolled into this sprint since 20 Aug, or the 20 Aug pull was scoped narrower than the full board. **Not yet reconciled against the per-ticket cache** (`03-stories/jira-sync/Sprint-34612-OTEP-Core-Sprint-8/`, still only 100 files) — run `/jira-sync core` to relocate/create the missing ~138 ticket files and confirm which are genuinely new scope vs. a pull-scope difference.

## Sprint 8 — 🔴 CLOSED (11–23 Aug 2026, closed 1 day early against its 24 Aug scheduled end)

> Source: OTEP-Pathfinder Sprint 8 (Sprint 34622). **Live pull: 2026-08-24** — sprint state is `closed` (`completeDate` 2026-08-23T23:40:53Z). Goal: "Clean up defects from Phase 1 - UAT and enable Phase 2 - UAT on Ringfencing and Competency Matching." **This was confirmed as the final MVP dev sprint with no Sprint 9 buffer** (per weekly-plan/daily-plan record in PM-OS, 2026-08-11) — **no Sprint 9 exists on this board as of this pull. Confirmed 2026-08-24 (PM, direct): this is by design, not a gap — the week of 24 Aug is Phase 3 UAT, and Sprint 9 starts the week after (w/c 31 Aug).** The earlier framing of this as a structural gap needing escalation is corrected; the open question narrows to whether the 20 tickets below have a confirmed path into Sprint 9.
>
> **Final state, 73 issues: Done 52, In Progress 8, QA 4, Backlog 8, To Do 1 — 20 issues (27%) did not reach Done at sprint close**, including several WOG AD/auth-adjacent tickets: OTEP-71 (Login Authentication using WOG AD, Léo — In Progress), OTEP-594 (WOG AD routing, unassigned — In Progress), OTEP-331 (WOG AD SSO/CSC, unassigned — QA), OTEP-110 (Login fail using WOG AD, unassigned — QA), OTEP-305 (Login/Logout, Thomas — QA), OTEP-111 (unauthorised-access page, unassigned — Backlog). This matters because this week's PM-OS daily plans (18–20 Aug) and weekly review report the underlying WOG AD and UAT Gate 2 *blockers* as resolved (prod/UAT access confirmed 18 Aug) — that is a different claim from these *tickets* reaching Done. **Flagged, not fixed:** whether these 20 open tickets roll to Sprint 9 (starting w/c 31 Aug), get closed as done-in-substance, or represent real remaining scope needs a person's call, not a file edit.

## Sprint 7 — ✅ CLOSED (28 Jul – 9 Aug 2026)

> Source: OTEP-Pathfinder Sprint 7 (Sprint 34621), Jira state `active`. **Live pull: 2026-08-07 (jira-sync /rest/api/3/search/jql).** Goal set in Jira: "Ship ringfenced opportunity listing and detail views, and close out login/auth replacement (Keycloak → real WOG AD flow) and CFT file-upload integration." 56 issues total: 15 Backlog, 23 Done, 8 In Progress, 8 QA, 2 To Do (re-confirmed via stale-check live pull 2026-08-07, afternoon — Done 22→23, In Progress 9→8, one ticket moved).
>
> **Note on dates:** Jira itself reports the sprint window as 28 Jul – 9 Aug, not 26 Jul as earlier notes stated — corrected here to match Jira directly.

**Jumped 5→52 issues since the 2026-07-24 pull.** The 30 open carryovers rolled from Sprint 6 into Sprint 7 in Jira on close-out; the cache hadn't followed. This pass relocated all 30 from `Sprint-34620-OTEP-Pathfinder-Sprint-6/` into `OTEP-Pathfinder-12541-Sprint-7-34621/` and corrected fields to match live Jira. Most reset **Status In Progress → Backlog** on rollover — a real Jira behavior on sprint close, not a sync error (verified against the raw pull, not assumed): OTEP-131, 405, 88, 723. Two assignee corrections: OTEP-283 → Michelle Yip, OTEP-305 → Thomas Huchedé. The 5 tickets already in the Sprint 7 folder (OTEP-71/110/111/594/810) were confirmed accurate — no field drift, stamps bumped only.

**Flagged — not fixed:** OTEP-364 ("Update OTG competency information," Backlog, unassigned) is live in Sprint 7 but has **no local cache file at all** — needs one created (out of scope for a field sync; there's no prior file content to preserve). The Sprint 7 plan-of-record in `04-ceremonies/sprint-allocation.md` ("no new stories," 27 Jul–7 Aug) is now badly out of date against a 36-open-ticket, 28 Jul–9 Aug sprint — needs reconciliation at planning, not an auto-rewrite.

**Flagged — needs `/jira-sync`, not fixed here:** the 2026-07-31 live pull shows counts drifted since the 2026-07-28 pull (In Progress 7→8, QA 1→2, Backlog 27→24) and per-ticket cache files under `03-stories/jira-sync/OTEP-Pathfinder-12541-Sprint-7-34621/` haven't been refreshed to match — this file's headline counts are now corrected, but the individual ticket files still reflect the 07-28 pull. Run `/jira-sync` to reconcile the per-ticket cache; stale-check only corrects this summary file.

**Core board:** still no active sprint. OTEP-Core Sprint 7 (34611) is Jira state `future` even though its planned start date (26 Jul) has already passed. OTEP-78 (previously flagged as moved to Pathfinder Sprint 7) — Core board out of scope for this Pathfinder-scoped default run; re-check next `/jira-sync core`.

---

**Core board cache cleanup (2026-07-06):** 19 orphaned ticket files (OTEP-180, 187, 189, 213, 214, 219, 227, 234, 263, 266, 269, 275, 277, 279, 297, 298, 308, 321, 365) removed from `OTEP-Core-13640-Sprint-5-34609/` — confirmed they no longer belong to Core Sprint 5's live issue list, archived to `03-stories/jira-sync/Archive/OTEP-Core-13640-Sprint-5-34609-orphaned-2026-07-06/` rather than deleted. **2026-07-14 update:** OTEP-Core board (13640) has a genuine active "OTEP-Core Sprint 6" (34610, goal: JumpStart recommendations + course search/discovery from LEARN) with **183 live issues** — this is a much larger, mostly separate workstream (Profile, Course Discovery, Infra/DevSecOps, Analytics) from what this workspace's local cache tracks (only 4 files exist: OTEP-78/82/83/84). Confirmed those 4 files have correct status (all Backlog, unchanged) and bumped their sync stamps, but did not import the other 179 live issues — that's a scope decision (does this PM's tracking need the full Core board, or just the Pathfinder-adjacent slice?), not something to auto-decide. Also: OTEP-78 has moved to Sprint 7 (future) live — flagging for relocation once a Core Sprint 7 folder exists, not creating one unprompted.

**✅ Resolved 2026-07-23 — Core board now fully synced, 100 issues.** Live Sprint 6 (34610) actually holds 100 issues, not 183 — the 2026-07-14 figure of 183 was almost certainly an unfiltered board-wide pull, not a sprint-scoped one. Full reconciliation this pass: 74 tickets relocated from the stale `OTEP-Core-13640-Sprint-5-34609/` folder (they'd rolled into Sprint 6 in Jira but the cache never followed) — this resolves the 2026-07-06 "orphaned" note above: those 19 tickets weren't dropped, they moved to Sprint 6. 22 status corrections applied on the relocated files (mostly QA/In Progress/Backlog → Done). 23 tickets had no cache file anywhere and were created fresh (OTEP-106, 180, 187, 189, 213, 214, 219, 227, 234, 263, 266, 269, 275, 277, 279, 297, 298, 308, 321, 401, 407, 410, 416). OTEP-78 dropped out of Sprint 6 back to Backlog live — relocated to `Backlog/` folder. OTEP-83/84 corrected Backlog→QA. Core Sprint 6 breakdown: 74 Done, 13 Backlog, 6 UAT, 4 QA, 2 In Progress, 1 To Do.

> Source: OTEP-Pathfinder Sprint 4. Final live pull: 2026-06-29. CLOSED.
> Goal: Complete, usable listing experience — search, filter, sort, data currency.

## Sprint 2 — CLOSED ✅ (synced 2026-06-02)

> Sprint 2 (Sprint 34616) is **closed**. 6 stories Done at close. Unfinished work (QA + In Progress + carry-overs) was pulled into Sprint 3 when it started.

**Done at close (6):** OTEP-267 (pagination), OTEP-252 (design system), OTEP-194 (FormSG spike), OTEP-193 (data model), OTEP-288 (backend stub), OTEP-296 (report format).

**Carried into Sprint 3** (not finished in S2): 11 QA items, OTEP-85/313/322 (In Progress), OTEP-128/268, OTEP-129 (open/closed story). See Sprint 3 below.

---

## Sprint 4 — CLOSING TODAY (15–26 Jun 2026)

> Source: OTEP-Pathfinder Sprint 4 (Sprint 34618). **Live pull: 2026-06-26.** 66 issues total.
> Goal: Deliver a complete, usable opportunity listing experience — officers can search, filter, and sort opportunities, understand what each type means, and trust that the data they're seeing is current and accurate.

**In Progress (12):** OTEP-88 (C@G listing, Léo), OTEP-405 (keyword search, Thomas), OTEP-495 (search backend, Thomas), OTEP-322 (Playwright, Rathika), OTEP-276 (design-system spike, Pow Hwee), OTEP-350 (WOG AD onboarding, Fabian), OTEP-349 (competency spike, Pow Hwee), OTEP-361 (ADR forum, Pow Hwee), OTEP-505 (CFT upload/webhook, Hao Eng), OTEP-539 (C@G background import, Léo), OTEP-386 (ringfencing tooltip, Amber), OTEP-439 (filter ineligible states, Amber)

**In QA (10):** OTEP-86 (filters), OTEP-268 (empty/error states), OTEP-85 (listing cards), OTEP-305 (login/logout), OTEP-128 (detail page), OTEP-129 (open/closed, Thomas), OTEP-284 (closing soon label, Thomas), OTEP-392 (federated logout, Thomas), OTEP-406 (sort opportunities, Thomas), OTEP-438 (admin view placeholder, Hao Eng)

**Done (31):** OTEP-127 ✅, OTEP-170, OTEP-193, OTEP-288, OTEP-296, OTEP-313, OTEP-314, OTEP-320, OTEP-324, OTEP-325, OTEP-326, OTEP-327, OTEP-334, OTEP-358 ✅, OTEP-362, OTEP-363, OTEP-367, OTEP-368, OTEP-369, OTEP-374, OTEP-375, OTEP-380, OTEP-381, OTEP-397 ✅, OTEP-427 ✅, OTEP-440, OTEP-441, OTEP-482, OTEP-496, OTEP-499, OTEP-536

**Backlog (13):** OTEP-87, OTEP-131, OTEP-289, OTEP-328, OTEP-329, OTEP-348, OTEP-393, OTEP-403, OTEP-404, OTEP-444, OTEP-483, OTEP-484, OTEP-485

**PM-owned:** OTEP-127 ✅ Done, OTEP-358 ✅ Done, OTEP-397 ✅ Done, OTEP-427 ✅ Done. All Michelle PM stories closed at sprint end.

---

## Sprint 3 — CLOSED (ended 12 Jun 2026)

> Source: OTEP-Pathfinder Sprint 3 (Sprint 34617), **state = closed 12 Jun**. Final live pull 2026-06-16. **53 issues** in folder (4 stale dupes removed 2026-06-16). 25 Done, remainder carried to S4.
> **OTEP-Core Sprint 3** (Sprint 34607): closed. (Live 2026-06-08.)

### Sprint 3 final state

**Done (25):** OTEP-170, OTEP-193, OTEP-288, OTEP-296, OTEP-303, OTEP-313, OTEP-314, OTEP-317, OTEP-320, OTEP-325, OTEP-326, OTEP-327, OTEP-332, OTEP-334, OTEP-351, OTEP-362, OTEP-363, OTEP-367, OTEP-368, OTEP-369, OTEP-374, OTEP-375, OTEP-380, OTEP-381, OTEP-391

**Carried to S4 (QA/In Progress/Backlog):** All remaining — see Sprint 4 above.

### New Sprint 3 scope (Backlog)

| Ticket | Title | Assignee | Notes |
|--------|-------|----------|-------|
| OTEP-86 | Filter opportunities by type | — | |
| OTEP-317 | Clear filters and reset view | — | Pairs with OTEP-86 |
| OTEP-87 | View C@G Opportunity Detail | — | ⚠️ Scope overlap w/ OTEP-319 — 87 keeps CTA visibility + back-state + empty-field; 319 owns click behaviour. Align PM afternoon 2026-06-02, confirm Wed grooming. |
| OTEP-88 | Identify C@G listings | — | |
| OTEP-89 | View C@G Job (Deep-Link) | — | |
| OTEP-319 | Apply via FormSG — basic redirect | — | `formsg_url` confirmed ✅ |
| OTEP-305 | Login and Logout (replace keycloak w/ actual) | — | **Build actual pages now against Keycloak; WOG AD swaps in later (D 2026-06-02).** Needs owner. |
| OTEP-192 | Recurring OTG data ingestion job | Léo Milbor | **In Progress** — critical path |
| OTEP-324 | OAuth 2.0 Refresh Token Rotation | Thomas | |
| OTEP-348 | OTG ingestion — scheduler & observability | — | |
| OTEP-349 | [Spike] Competency matching w/ OTEP-Core | — | Cross-squad |
| OTEP-350 | Onboard WOG AD | Fabian Peh | #26 |
| OTEP-351 | [Spike] Azure AD mock for testing | — | Unblocks auth testing w/o prod WOG AD |
| OTEP-352 | Load POCDEX production code table | Pow Hwee | |
| OTEP-358 | [Spike] Robust nil-date OTG import | **Michelle** | PM-owned. Scope + timebox. |
| OTEP-361 | Conduct ADR review forum | Pow Hwee | Cross-squad |
| OTEP-362 | 🆕 Backend: don't return closed opportunities | — | **NEW — OTEP-129 split (backend half)** |
| OTEP-363 | 🆕 UI: display closed opportunity | — | **NEW — OTEP-129 split (frontend half)** |
| OTEP-86/88/89… | (C@G + filter set above) | — | |
| OTEP-276 | [Spike] Custom design system reimpl | — | Likely drop — OTEP-252 Done resolves |
| OTEP-289 | [Spike] Filter by Functions (C@G) | — | Gates OTEP-318 go/no-go |

### Still NOT on the Sprint 3 board (⚠️ reconcile)

| Ticket | Title | Notes |
|--------|-------|-------|
| OTEP-271 | Local POCDEX database | Not on board — decide: add or accept out |
| OTEP-203 | Standalone POCDEX API service | Same |
| OTEP-318 | Filter by category | Correctly excluded — OTEP-289 spike still Backlog |

**Note:** OTEP-129 is now **on the Sprint 3 board (Backlog)** and split into OTEP-362/363 — earlier "not pulled into Sprint 3" note is resolved.

---

## Design lock + key Sprint 3 constraints

- **Design lock:** Wednesday 3 June — engineers must not start UI until Amber signs off final Figma
- **Vesak Day:** already passed (~1 June) — 2 June is a normal working day; standup runs
- **Mid-sprint review:** Monday 8 June (pulse check, not formal ceremony) — ✅ invite sent
- **Thomas:** sole FE engineer; design lock is the single biggest risk for his first week
- **OTEP-289 spike still Backlog:** OTEP-318 (filter by category) can't be confirmed until spike completes. Get outcome at today's Sprint Review.

---

## Scope decisions

- (2026-06-04) **Plan of record = Pow Hwee's "Planning draft for sprint 3 and after"** (Confluence, PSD-OTEP) — adopted as the team's S2–S6 shape. **Amendment:** native apply = R1, not an S4 spike (MVP apply = FormSG redirect, OTEP-319). S4 dates **15–28 Jun** (Sprint 34618, planning ceremony 14 Jun, engineers start 15 Jun). See decisions-log + [adoption reconciliation](../../PM-OS/outputs/archive/2026-W23-Jun01-Jun07/analyses/2026-06-04-W23-adopt-powhwee-plan-reconciliation.md).
- (2026-05-29) **OTG sync cadence: one-time port only** — no ongoing automated sync. Pilot agencies driven to adopt Compass directly. See D-016. Resolves open question from Sprint 3 Planning.
- (2026-05-28) **Design lock: Wednesday 3 June** (D-013)
- (2026-05-28) **OTG competency migration: file ingestion, not live API** (D-010) — Fanxu owns Sprint 3 one-time bulk import
- (2026-06-02) **OTEP-305 login/logout: build actual pages now against Keycloak; WOG AD swaps in later.** Confirmed in Sprint 3. Auth FE proceeds in parallel while WOG AD domain submission pending (#26). See decisions-log.
- (2026-05-21) **Auth epic deferred to Sprint 4+** — OTEP-71, OTEP-110, OTEP-304 deferred; no WOG AD UAT env (#26). (OTEP-305 login/logout pages excepted — buildable now via Keycloak, see above.)
- (2026-05-21) **OTEP-271/203 confirmed in Sprint 3** — but still not on Jira Sprint 3 board; reconcile.

---

## Jira board actions still needed

- [ ] Confirm OTEP-271 + OTEP-203 — add to Sprint 3 board if still committed (still NOT on board)
- [ ] **Assign OTEP-305 an owner** — login/logout pages buildable now via Keycloak; unassigned. Raise at standup.
- [ ] OTEP-289 spike output — go/no-go for OTEP-318 (still Backlog)
- [ ] OTEP-87 competency section — scope is firm (it's included); open dependency is **data, not scope**: ingestion lands first, so whether each C@G opportunity actually carries competencies isn't confirmed yet. Track via ingestion.
- [ ] OTEP-358 (Michelle, nil-date spike) — scope + timebox
- [ ] OTEP-361 (Pow Hwee, ADR forum) — confirm timing + PM involvement
- [x] ~~Confirm OTEP-305 Sprint 3 vs 4+~~ — resolved: in Sprint 3, build via Keycloak (D 2026-06-02)
- [x] ~~OTEP-129 placement~~ — resolved: on Sprint 3 board, split into OTEP-362/363

---

*Updated: 2026-08-31 (stale-check — live Jira pull, board 12541: corrected "Sprint 9 starts w/c 31 Aug" [PM verbal, 2026-08-24, never checked against Jira] to Sprint 9's actual state — `future`, dates 6–20 Sep. Confirmed none of the 6 WOG AD/auth tickets are in Sprint 9. Flagged the 31 Aug–5 Sep sprint-container gap for a person's call.) Prior: 2026-08-28 (stale-check — "Sprint details" header corrected from "Sprint 8 — ACTIVE" to CLOSED to match the file's own Sprint 8 section + tasks-active.md; sprint schedule table updated (S8 11–23 Aug closed, Phase 3 UAT w/c 24 Aug, S9 w/c 31 Aug); Post-dev timeline rewritten per PM: **MVP launch targeted 24–25 Nov 2026, VAPT 7 Sep–8 Nov, sign-off ~7 Nov** — old "Deploy 19–23 Oct / Soft launch 26–30 Oct / First release week of 2 Nov" chain marked superseded. Jira not re-pulled this run — the sprint script returned the wrong board.) Prior: 2026-08-24, 2nd pass (PM confirmed directly: the week of 24 Aug is Phase 3 UAT by design; Sprint 9 starts w/c 31 Aug. Corrected the 1st pass's "structural gap, no Sprint 9 buffer" framing below — that was premature. Open item narrows to confirming the 20 Sprint 8 tickets have an explicit destination in Sprint 9.) Prior: 2026-08-24, 1st pass (stale-check — **Sprint 8 (34622) confirmed CLOSED**, `completeDate` 2026-08-23T23:40:53Z, one day ahead of its scheduled 24 Aug end. Header/section rewritten from "ACTIVE" [stale since the 20 Aug pull] to closed, with final counts [73 issues: 52 Done, 8 In Progress, 4 QA, 8 Backlog, 1 To Do] and the 6 WOG AD/auth-adjacent tickets not reaching Done named explicitly (OTEP-71/594/331/110/305/111). Board 12541 confirmed to have no active or future Pathfinder sprint — flagged at the time as a possible gap, corrected above.) Prior: 2026-08-20 (jira-sync `core` + `cc-uat` — **OTEP-Core Sprint 8 (34612) confirmed live-active**, no local folder existed (last cached Core sprint was Sprint 7, 34611, whose 6 Aug end date had already passed with no successor tracked). Created `03-stories/jira-sync/Sprint-34612-OTEP-Core-Sprint-8/` fresh with all 100 live issues: 47 Done, 33 QA, 14 Backlog, 4 In Progress, 1 UAT, 1 To Do. 29 stale duplicate files identified in the old Sprint-6 (34610)/Sprint-7 (34611) Core folders — same ticket carried into Sprint 8 live but old copy never removed (OTEP-106, 134, 137–150, 153–155, 159, 160, 162, 195, 205, 407, 410, 416, 83, 84). Confirmed and deleted (Michelle, single batch confirm) — each had a correctly-placed, freshly-synced copy in the Sprint 8 folder. **CC-UAT board (20498, Kanban, uat+PATHFINDER labels) re-synced:** 44 issues, 42 Done / 1 To Do / 1 In Progress. 13 field deltas since 19 Aug: OTEP-971/1174/975/1301/1302 moved Ready For UAT/To Do → Done (Guo XZ sign-offs, 18–19 Aug); OTEP-1004 reverted Ready For UAT → To Do (Michelle Yip comment, 19 Aug); OTEP-1339 (duplicated competency match, Thomas) newly tracked, matches the bug flagged in the 19 Aug UAT Daily Review. No CC-UAT duplicates found in other folders — this board's ticket population doesn't overlap the sprint boards. Full per-ticket detail in `04-ceremonies/sprint-allocation.md`.) Prior: 2026-08-17 (stale-check — Sprint 7→Sprint 8 rollover: file header and top section were still describing Sprint 7 [closed 9 Aug] a full week into Sprint 8 [started 11 Aug, live-active]. New Sprint 8 section added with live counts [73 issues: Done 37, In Progress 9, QA 11, To Do 3, Backlog 13] and WOG AD ticket statuses [OTEP-71/594 In Progress, OTEP-331/110 QA] cross-checked against the 13 Aug dev-re-enable decision note — flagging that prod/UAT confirmation still isn't reflected in any ticket status, this needs a person to confirm, not a file edit). Prior: 2026-08-07 (stale-check, afternoon pass — Pathfinder Sprint 7 counts re-pulled live, Done 22→23, In Progress 9→8). Prior: 2026-08-07 (jira-sync `all` — full sweep of every cache folder + Backlog, all statuses, via `/rest/api/3/search/jql` (1031 issues project-wide). Pathfinder Sprint 7 counts confirmed unchanged from 2026-08-06 (56 issues: 15 Backlog, 22 Done, 9 In Progress, 8 QA, 2 To Do). **Core Sprint 7 (34611) confirmed live-active** (was flagged `future` on 2026-07-28 despite a passed start date — now genuinely active, dates 28 Jul–6 Aug, though that end date has also passed with no new sprint started; flagged below): 271 issues (144 Done, 55 QA, 50 Backlog, 16 In Progress, 4 To Do, 1 Selected for Development, 1 UAT). **Intel Sprint 7 (35010) active:** 30 issues (7 Done, 11 Backlog, 6 To Do, 5 In Progress, 1 QA). Per-ticket cache: 87 field corrections applied across all folders (Status/Assignee/Story Points), 28 tickets relocated to newly created `03-stories/jira-sync/OTEP-Core-13640-Sprint-7-34611/` (19) and `Sprint-35010-OTEP-Intel-Sprint-7/` (9) folders — both folders didn't exist before this run. 2 CC-UAT tickets (OTEP-955, 843) relocated `Backlog/`→`To-Do/` to match their new "Selected for Development" status. 69 stale duplicate files flagged for deletion (not deleted) — see `jira-sync/2026-07-01-duplicate-cleanup-candidates.md` lineage; full list in this run's report. 18 local ticket files reference Jira keys that now 404 (deleted/invalid) — flagged, not touched. 95 additional Core/Intel tickets show a "moved to active sprint" signal in Jira but are already Done — this is Jira's sprint-rollover carrying closed tickets forward, not real re-scoping; left in place, not relocated, flagged only.) Prior: 2026-08-06 (stale-check — refreshed Sprint 7 header counts against live 2026-08-06 pull [56 issues: 15 Backlog (was 22), 22 Done (was 16), 9 In Progress (was 8), 8 QA (was 6), 2 To Do] — per-ticket cache files under `03-stories/jira-sync/` still not reconciled, needs `/jira-sync`, out of scope here.) Prior: 2026-08-04 (stale-check — refreshed Sprint 7 header counts against live 2026-08-04 pull [54 issues: 22 Backlog (was 24), 16 Done, 8 In Progress, 6 QA (was 2 — OTEP-131 moved QA), 2 To Do] — per-ticket cache files under `03-stories/jira-sync/` still not reconciled, needs `/jira-sync`, out of scope here.) Prior: 2026-07-31 (stale-check — corrected top-of-file header from "Sprint 6 ACTIVE" to "Sprint 7 ACTIVE, 28 Jul–9 Aug" [Sprint 6 closed, header hadn't followed]; corrected Sprint 7 dates 26 Jul→28 Jul to match Jira directly; refreshed Sprint 7 counts against live 2026-07-31 pull [36 issues: 24 Backlog, 16 Done, 8 In Progress (was 7), 2 QA (was 1), 2 To Do] — flagged that per-ticket cache files under `03-stories/jira-sync/` still reflect the 07-28 pull and need `/jira-sync` to reconcile, not fixed here.) Prior: 2026-07-28 (jira-sync — Pathfinder Sprint 7 default-scope run, active sprint, open tickets only. Sprint 7 (34621) flipped Jira state `future`→`active` today; issues 5→52 (27 Backlog, 16 Done, 7 In Progress, 1 QA, 1 To Do) as 30 open carryovers rolled in from Sprint 6 close-out. Relocated those 30 from `Sprint-34620-OTEP-Pathfinder-Sprint-6/` → `OTEP-Pathfinder-12541-Sprint-7-34621/`; most reset Status In Progress→Backlog on rollover (confirmed real against raw pull, not a script error): OTEP-131/405/88/723. 2 assignee corrections: OTEP-283→Michelle Yip, OTEP-305→Thomas Huchedé. The 5 tickets already in the Sprint 7 folder confirmed accurate, stamps bumped only. Flagged: OTEP-364 live in Sprint 7, no local cache file — needs creation. OTEP-Core Sprint 7 (34611) still Jira state `future` despite its start date having passed — Core has no active sprint. Sprint 7 plan-of-record in `sprint-allocation.md` now well out of date against the real scope — flagged there, not rewritten here. Core board otherwise out of scope for this Pathfinder default run.) Prior: 2026-07-24 (jira-sync — Pathfinder Sprint 7 scoped run. Sprint 7 (34621, Jira state `future`, 26 Jul–9 Aug) confirmed with 5 live issues; local folder `OTEP-Pathfinder-12541-Sprint-7-34621/` created (didn't exist before). 4 tickets relocated a second time, `Backlog/` → Sprint 7 folder (OTEP-71/110/111/594 — their live Jira sprint since 2026-07-14, but no target folder existed until now). 1 new ticket created fresh (OTEP-810, Hao Eng, OTG ingestion Comp ID matching — no description yet). This resolves the flag repeated on 2026-07-14/07-20/07-23 below. Note: this 5-issue Sprint 7 count is separate from and much smaller than the Ready-shelf gating tracked in `outputs/analyses/2026-07-22-W30-grooming-close.md` — none of the 4 relocated auth stories carry `ready-for-sprint`, and the 19 ungroomed candidates from Tuesday's scorecard aren't in Sprint 7 in Jira at all yet.) Prior: 2026-07-23 (jira-sync — full active-sprint reconciliation, both boards. Pathfinder: 91→95 issues, 4 new (OTEP-755/768/791/803), 4 moved to Done (OTEP-276/662/677/752), 8 stale-placement tickets relocated Sprint-6-folder→Backlog-folder (OTEP-110/111/331/425/594/614/615/71 — confirmed no longer in Sprint 6 live). Core: went from 4 tracked files to 100 — 74 relocated from the stale Sprint-5 folder [confirmed rolled into Sprint 6 live, cache never followed], 23 created fresh [previously untracked], 22 status corrections on relocated files [mostly →Done], OTEP-78 relocated to Backlog [dropped from Sprint 6 live], OTEP-83/84 corrected Backlog→QA. This resolves the 2026-07-06 "19 orphaned tickets" note — they weren't orphaned, they moved sprints. Also corrects the 2026-07-14 "183 live issues" figure for Core, which was very likely an unfiltered board pull, not sprint-scoped; true Sprint 6 count is 100.) Prior: 2026-07-20 (stale-check — live re-pull found 90→91 issues, In Progress 17→18; OTEP-752 [integration testing harness setup, Léo] added since the 2026-07-16 sync. QA/To Do/Done/Backlog counts unchanged.) Prior: 2026-07-16 (jira-sync — fresh Pathfinder Sprint 6 pull, 90 files synced via `jira-sprint.sh` + `jira-sync.py`. 8 QA→Done sign-offs (Rathika), OTEP-666 In Progress→Done, 4 QA→In Progress reworks (OTEP-305/283/595/131), OTEP-723 added new. Counts: 17 In Progress (was 11), 5 QA (was 16), 5 To Do (was 6), 42 Done (was 33), 21 Backlog (was 23). Also cleared the top-of-file stale flag from 2026-07-01 and the "Sprint 6 not started" line — both superseded by the 2026-07-14 sync and no longer accurate, left in the history trail below for traceability.) Prior: 2026-07-14 afternoon (jira-sync, 3rd pass today — 1 delta: OTEP-437 Backlog→To Do, assigned Hao Eng. OTEP-505 re-confirmed unchanged (QA, Hao Eng) for the 3rd consecutive pull today.) Prior: 2026-07-14 midday (jira-sync, 2nd pass today — Sprint 6 now Jira state `active` (was `future` this morning). 3 deltas since morning sync: OTEP-613 Backlog→QA (+assignee), OTEP-683 Backlog→In Progress, OTEP-604 relocated Sprint-6→Sprint-5 cache folder (live Jira places it there despite being Done). OTEP-505 re-confirmed unchanged (QA, Hao Eng) — genuine stall, not a sync gap. 8 tickets confirmed dropped from Sprint 6 to future sprints (7/8) or removed from all sprints — flagged, not relocated, no target folders exist yet.) Prior: 2026-07-14 morning (jira-sync — Pathfinder Sprint 5→6 rollover synced: 76 files relocated, 4 status corrections (OTEP-283/505/541/86), 1 stale duplicate removed (OTEP-613). Total moved to Sprint 6 folder: 89 issues (26 Backlog, 5 To Do, 15 QA, 33 Done, 10 In Progress). Flagged: Sprint 6 still Jira state `future`, not formally started; Core board has 183 live issues vs 4 tracked locally — scope decision needed, not auto-imported.) Prior: 2026-07-06 (jira-sync — direct Jira REST API pull, MCP unavailable this session. Total 76→81: 6 new tickets (659, 662, 663, 666, 667, 668). Field corrections: OTEP-85 QA→Done, OTEP-322 In Progress→Done, OTEP-539 In Progress→Done, OTEP-87 In Progress→QA, OTEP-444 Backlog→In Progress, plus assignee updates for OTEP-390/484/485. Counts: 12 In Progress (was 13), 13 QA (was 14), 2 To Do (was 1), 33 Done (was 30), 21 Backlog (was 18).) Prior: 2026-07-03 (stale-check — corrected In Progress/QA counts and lists against live Jira: prior version had 14 In Progress / 13 QA transposed against live 13 In Progress / 14 QA, and OTEP-87 mis-tagged as In Progress when Jira shows it in QA. Backlog corrected 17→18 — OTEP-659 added live, not yet reflected. Total 75→76.) Prior: 2026-07-02 (jira-sync — Pathfinder Sprint 5 cache folder cleanup: deleted stale duplicate `OTEP-Pathfinder-12541-Sprint-5-34619` (11 partial files); canonical `Sprint-34619-OTEP-Pathfinder-Sprint-5` verified 75/75 against live Jira, zero field drift, all 75 files stamped. Counts: 75 issues total (was 74), 14 In Progress, 13 QA, 1 To Do, 30 Done (was 29 — OTEP-604 added, already Done), 17 Backlog. Source: direct Jira REST API pull, sprint 34619.) Prior: 2026-07-01 (jira-sync full sweep — Sprint 5 recomputed from live Jira: 74 issues total (was 55), 14 In Progress (was 12), 13 QA (was 11), 1 To Do, 29 Done, 17 Backlog (was 21)). Prior: 2026-06-26 (stale-check — IP 10→12 +386/439, Backlog 15→13, total 67→66 — OTEP-127 + OTEP-397 Done; OTEP-358 In Progress not Backlog; counts 14 IP→12, 8 QA→10, 20 Done→29). Prior: 2026-06-24 (timeline update — S4 close Fri 26 Jun; S5–S9 dates; VAPT 7 Sep–16 Oct; first release 2 Nov). Sprint 3 CLOSED 12 Jun. Sprint 4 ACTIVE 15–26 Jun. S4: 12 In Progress, 10 QA, 29 Done, 1 To Do (live 2026-06-25).*
