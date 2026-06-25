# OTEP-86: Filter Opportunities by type (Internal Jobs, STIPs, Gigs)

**Status:** QA
**Assignee:** N/A
**Story Points:** 2

---

## Description

User story:  As an officer, I want to filter the listing by opportunity type so I can focus on what's relevant to me. Scope: Type filter only. Category/function filter is OTEP-318. Clear all is OTEP-317. Acceptance Criteria I can filter by type: STIP, Gig, Jobs  I can select more than one type at a time. The listing updates to show only opportunities matching the selected types. I can see which filters are active (badge count or highlighted state). My filter selection persists as I page through results. Each type has a tooltip explaining what it is - link to EOM Microsite.  Type filter works in combination with any other active filters. The result count updates to reflect the filtered set. When no results match, the empty state from OTEP-268 is shown. Jobs will subsume from OTG (Internal Jobs and Secondments), and C@G Jobs. Out of Scope Filter by category/function — OTEP-318 (conditional on OTEP-289 spike output) Clear all filters — OTEP-317 SJR:  Structured job rotation. Extended placement in a different role or agency. Secondments and Internal Jobs are excluded from MVP (decision made 15 Jun 2026 by WD during design review with BO meeting).

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-380 | [BE] Handle filtering params | Done |
| OTEP-381 | [FE] Handle filtering params | Done |

---

## Latest Comments

**Michelle Yip** (2026-06-11)
I have removed it and it’s replaced with    as I need Amber to come up with the page.

---

**Thomas Huchedé** (2026-06-11)
I think I missed out AC6. Can I double check where is this supposed to be displayed?

---

**Pow Hwee TAN (PSD)** (2026-05-28)
Careers@Gov is not listed as a filter option. Suggest creating a Sprint 4 ticket to add C@G as a filter option once C@G listings are live.
