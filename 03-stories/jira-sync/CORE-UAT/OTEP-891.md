# OTEP-891: [CORE] EXPD-01 — Explore - results listing (OTEP-493)

**Status:** Done
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Account Account B — Richard Ramos ·  Richard_RAMOS_FROM.TP@cscollege.gov.sg  · password: Richard@Cc2026 Test Steps Go to the  UAT site  and Log in as B. Run a search in Explore new roles - “Industry Engagement” and press enter or Search Select a role from the results Note the details in the right panel, look at expected results. Test Data Uses account B. Expected Result Result cards in the results listing (left side) show role title, Job family, match %, and a progress bar (grey/orange/green). Ranked by match % high→low. Up to 10 in the viewport, scrollable. Roles should always have agency, family, function and competencies. In the right role panel, detail panel shows title, agency, job function, job family, matched + missing counts, and the full functional competency list with "You have this"/"To develop" tags. Row are collapsed by default. Collapsed rows show competency name, match status, and an expand icon. Expanding a row reveals the competency description alongside the name and status. Clicking "+ Expand all" expands all competency rows and the control changes to "- Collapse all"; clicking "- Collapse all" collapses all rows and the control reverts to "+ Expand all". Match % = overlapping functional competencies ÷ total functional competencies required for the role × 100, rounded to the nearest whole number. The matched count shown equals the number tagged "You have this"; the missing count equals the number tagged "To develop".

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-17)
🎉 Looks good!

---

**Imelda Mo** (2026-08-17)
Known issue of Agency not showing in the role panel for WOG roles already addressed in the ticket here:      This ticket can continue being checked excluding this criteria.

---

**Charles Ho** (2026-08-17)
Working as intended

---
*Synced from Jira: 2026-08-25*
