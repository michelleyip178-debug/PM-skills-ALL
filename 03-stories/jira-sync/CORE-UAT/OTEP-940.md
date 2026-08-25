# OTEP-940: [CORE] DISC-04 - Autocomplete trigger, max and grouping (OTEP-83)

**Status:** Done
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Account Account D — padmin2 ·  padmin2@cscollege.gov.sg  · password: Padmin@Cc2026 Test Steps Go to the  UAT site  and log in as D. Click "Explore all courses" from the Learning & Courses landing page. Type 1–2 characters (e.g. “Ma”) and confirm no autocomplete appears. Type 3+ characters (e.g. “Manage”) and note the grouped suggestions and their order. Clear the search bar and confirm the autocomplete closes. Test Data Keyword: “Manage” — 10 total suggestions available (3 Domains + 5 Course Names), so the list is capped at 8. Domains (starts-with ranks first): “Management Domain [JSHRMR WOG]” (starts-with, 2 courses) → then “Land and Estate Management”, “Programme and Project Management” (contains). Course Names: “Class Management”, “[LXP_UATGrp1][CR] Flow Time Management & Prioritisation”, “Risk Management in Government”, SAP … Management courses (all contain “Manage”). Expected Result Autocomplete appears only after 3+ characters, shows at most 8 suggestions, grouped into “Domains” and “Course Names”. Within each group, suggestions starting with the typed term rank above those that merely contain it (e.g. “Management Domain [JSHRMR WOG]” ranks above “Land and Estate Management”).

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-18)
🎉 Looks good!

---

**Charles Ho** (2026-08-18)
working as intended

---

**Christopher Woo** (2026-08-18)
ok

---
*Synced from Jira: 2026-08-25*
