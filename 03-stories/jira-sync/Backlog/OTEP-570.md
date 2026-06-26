# OTEP-570: View matched competencies on Gig/STIP detail page

**Type:** Story

**Status:** Backlog

**Assignee:** N/A

**Story Points:** N/A

**Splits from:** OTEP-336 (listing card match signal)

**Jira ticket:** OTEP-570

---

## User Story

As an officer browsing a Gig or STIP, I want to see which of the competencies I'd develop from this opportunity I already have, so I can assess my fit and factor growth potential into my decision before applying.

---

## Acceptance Criteria

**AC1 — "What you'll develop" section renders with match states**

Given an officer views a Gig or STIP detail page,
When their competency profile is successfully retrieved from the Core competency endpoint,
Then a "What you'll develop" section renders listing each competency associated with the opportunity.
Each competency shows one of two states: matched (the competency appears in the officer's profile) or unmatched (it does not).
No proficiency level is compared — presence only.

**AC2 — Matched competencies are visually distinct from unmatched**

Given the "What you'll develop" section is rendered with match states,
When the officer scans the list,
Then matched competencies are visually distinct from unmatched ones (e.g. tick vs empty indicator).
Matched competencies appear first, followed by unmatched — so the officer sees what they already have before what they'd gain.

**AC3 — Officer has some competencies but none match**

Given an officer's profile is loaded and has competencies,
When none of them match the opportunity's competencies,
Then the section renders all competencies in the unmatched state. No error or "no match" message is shown.

**AC4 — Officer has no competency profile**

Given an officer has no competency data in their POCDEX profile,
When they view a Gig or STIP detail page,
Then the section renders all the opportunity's competencies without match states. No error is surfaced.

**AC5 — Competency profile fails to load**

Given the Core competency endpoint returns an error or times out,
When the officer views a Gig or STIP detail page,
Then the section still renders the opportunity's competency list without match states. No error message is shown. The rest of the detail page is unaffected.

**AC6 — No competency data: section is hidden**

Given a Gig or STIP has no competency data,
When an officer views the detail page,
Then the "What you'll develop" section is not rendered at all. It does not appear as "Not specified" or an empty container.

**AC7 — Section does not block page load**

Given the competency profile fetch is in progress,
When the officer lands on the detail page,
Then the rest of the page content renders immediately. The "What you'll develop" section loads independently — a loading state is shown until the profile fetch completes or times out.

**AC8 — Read-only**

Given an officer views the "What you'll develop" section,
When they interact with any competency item,
Then there is no edit action available. The officer cannot update their profile from the detail page.

**AC9 — Competency profile nudge banner shown on detail page**

Given an officer views a Gig or STIP detail page,
When the "What you'll develop" section renders,
Then a banner is shown encouraging the officer to keep their competency profile current.

If the officer has no competency profile, the banner copy is a clear CTA to add competencies so they can see how they match against this opportunity.
If the officer has a competency profile, the banner copy is a softer nudge — acknowledging their existing profile while encouraging them to keep it up to date for accurate matches.

The banner is read-only. It does not provide an inline edit path — profile editing is R1.

---

## Out of Scope (MVP)

- Internal Jobs competency matching — deferred to R1
- Proficiency level comparison — R1
- Editing officer competency profile from the detail page — R1

---

## Subtasks

| # | Area | Title | Notes |
|---|---|---|---|
| 1 | BE | Confirm competency list in Gig/STIP detail API response | Verify field is returned by opportunity detail endpoint; add if missing |
| 2 | BE | Expose officer competency profile via OTEP API | Shared with OTEP-336 (listing card); build once, used in both |
| 3 | FE | Render "What you'll develop" section — static | Competency tags on detail page, no match states; can ship before subtask 2 is done. **Layout note:** competency section renders before time commitment section (decision: S5 planning 2026-06-25) |
| 4 | FE | Add match state computation and visual treatment | Intersect opportunity competencies vs officer profile; render matched/unmatched; sort matched first |
| 5 | FE | Loading and fallback states | Loading skeleton while profile fetches; degrade to unmatched-only display if profile is empty or errors |
| 6 | QA | Unit tests | Cover: all matched, none matched, partial match, empty profile, profile load failure, no competency data (section hidden) |

**Parallelisation note:** Subtask 3 (static section) can start as soon as subtask 1 is confirmed. Subtask 4 depends on subtask 2. Thomas (FE) and Léo (BE) can work in parallel.

**Dependency:** BE subtask 2 (officer profile endpoint) is shared with OTEP-336. Whichever story is picked up first should build the endpoint; the other story picks it up from there.
