# OTEP-872: [CORE] [R] REC-01 — Recommended roles (OTEP-447)

**Status:** Done
**Assignee:** Adrian Lo
**Story Points:** N/A

---

## Description

Account Account R — Rama Moorthy ·  rama_moorthy@psd.gov.sg  · password: rama Account R was seeded with a curated set of 12 functional competencies so its top-5 recommendations span all three progress-bar colours. Seed tagged uat-seed-rec01 (sandbox account, reversible). Test Steps Go to the  UAT site  and log in as R. On "Your development", view "Based on your current role". Confirm each recommended role shows a progress bar coloured by its match %. Confirm % match is accurate Test Data Account R — top-5 recommendations span all three bands: 3 × green (100%) — Associate (FP) 1 × orange (33%) — Dy Dir (Finance) 1 × grey (23%) — SAD (Governance and Corporate Finance) Expected Result Section "Based on your current role" + subheader "Discover roles tailored to your experience level and career path." Up to 5 recommended roles, ranked together by competency match % (high→low), each with a progress bar: grey 0–29%, orange 30–69%, green 70%+. % for competency match is determined by overlapping competencies divided by total functional competencies required for the selected role x 100. Display value is rounded to the nearest whole number.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-21)
Thanks for looking into this. The selection is OK now. Will move this to Passed.

---

**Imelda Mo** (2026-08-21)
fix for this done. please check

---

**Imelda Mo** (2026-08-21)
role not highlighted properly issue persists. likely due to restoration of backup. fix will be redeploye soon

---
*Synced from Jira: 2026-08-25*
