# OTEP-336: Show competency match signal on Gig/STIP listing cards

**Status:** QA
**Assignee:** Thomas Huchedé
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 8 (34622)

---

## Description

User Story As an officer browsing the opportunity listing, I want to see at a glance how many competencies I already have for each Gig or STIP, so I can quickly identify high-fit opportunities without opening every detail page.  Acceptance Criteria AC1 — Competency match count renders on Gig/STIP cards Given an officer views the opportunity listing, When their competency profile is successfully retrieved, Then each Gig and STIP card shows a match count (e.g. "3 of 5 competencies match your profile"). No proficiency level is compared — presence only. AC2 — No match indicator when officer has no profile Given an officer has no competency data in their POCDEX profile, When they view the listing, Then Gig and STIP cards render without a competency match count. No error is shown. The card is otherwise unchanged. AC3 — No match indicator when profile fails to load Given the Core competency endpoint returns an error or times out, When the officer views the listing, Then cards render without a competency match count. No error is shown to the officer. AC4 — No match indicator when opportunity has no competencies Given a Gig or STIP has no competency data, When it appears on the listing, Then no match count is shown on that card. Other cards with competency data are unaffected. AC5 — Match count does not block listing load Given the competency profile fetch is in progress, When the officer lands on the listing page, Then the listing renders immediately. Match counts appear on cards once the profile fetch completes — cards do not hold back waiting for the profile. AC6 — Internal Job cards do not show a match count Given an officer views the listing, When Internal Job cards are displayed, Then no competency match count is shown on those cards. MVP scope is Gigs and STIPs only.  Out of Scope (MVP) Internal Jobs competency match signal — deferred to R1 Sorting or filtering the listing by match count — R1 Proficiency level comparison — R1  Subtasks # Area Title Notes 1 BE Confirm competency list is available per opportunity in listing API response Verify the field is returned for Gig/STIP cards; add if missing 2 BE Expose officer competency profile via OTEP API Proxy or call Core competency endpoint (#41); shared with detail page story (OTEP-TBD) 3 FE Render match count on Gig/STIP listing cards Show "X of Y competencies match" once profile is loaded; hide if no data 4 FE Loading and fallback states Cards render without match count while profile fetches or if fetch fails — no error shown 5 QA Unit tests Cover: profile loaded with matches, profile loaded with no matches, empty profile, profile load failure, opportunity has no competencies Note:  BE subtask 2 (officer profile endpoint) is shared with the detail page story (OTEP-TBD). Build once, use in both.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-11*
