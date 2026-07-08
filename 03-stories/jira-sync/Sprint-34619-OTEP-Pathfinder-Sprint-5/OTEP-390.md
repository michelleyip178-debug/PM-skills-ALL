# OTEP-390: Ringfenced opportunity detail page states (eligible + ineligible)

**Status:** In Progress
**Assignee:** Thomas Huchedé
**Story Points:** N/A

---

## Description

User story:  As a public service officer, I want the opportunity detail page to clearly tell me whether I am eligible for this opportunity, so that I don't waste time pursuing a role I can't apply for — and if I'm not eligible, I can still find something relevant. Sprint 5 scope:  FE detail page states for eligible and ineligible officers, including the ineligible deep-link entry path (EDM or shared URL). Absorbs OTEP-133.   Eligibility rules (as per OTG ingested) : INCLUSION / LIMIT to officers based on Agency-level, Job Family.  Acceptance Criteria Eligible officer (default detail experience) When an eligible officer views a ringfenced opportunity, the detail page renders normally with no additional eligibility notice. The Apply CTA is shown as standard. There is no eligible opportunity indicator.  Opportunity Listing logic will be: Ringfenced STIP and Gig Opportunities based on posted date (latest first) Open opportunities (mixed of all) based on posted date (latest first).   Ineligible officer — arrives via direct URL or shared link When an officer who is not eligible for a ringfenced opportunity lands on its detail page (e.g. via a shared URL, EDM, or bookmark), the page loads but displays a clear ineligibility notice: "This opportunity is not available to you." The officer must be logged in.  A link back to the full listing is always visible. POCDEX unavailable (fallback) If POCDEX data cannot be resolved at the time of the detail page load (lookup failure on officer’s agency and/or job family), the page renders normally without eligibility rules applied. The system does not block access on a failed lookup — degrade silently. Unauthenticated access An unauthenticated officer accessing any opportunity detail page via direct URL is redirected to login first, then returned to the original URL after authentication. Out of Scope (Sprint 5) Eligibility indicator of opportunity Agency/grade/scheme-level eligibility display (e.g. "Open to MX officers only") — R1+ Personalised alternative opportunity recommendations — basic eligibility match only Absorbs OTEP-133 (Access the hub via a deep link from an EDM) — ineligible-via-deep-link scenario fully covered by AC3–6 above. OTEP-133 can be closed.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Michelle Yip** (2026-07-07)
Updated in purple for 1 and 3. For #2, there is no indicator and have removed the occurrences.

---

**Rathika Ramalingam** (2026-07-07)
Hi    , please update the following.  Eligibility Rules or POCDEX Data Logic (Blocker) What is the visual eligibility indicator on the detail page? (if we decided to show) Is sorting the default by posted_date within the pinned items (listed first) and ineligible cards?
