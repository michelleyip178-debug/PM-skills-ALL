# OTEP-866: [CORE] REP-03 — Reported state persists across login (OTEP-290)

**Status:** Done
**Assignee:** N/A
**Type:** Task
**Labels:** CORE, OTEP-290, Profile_Page, uat

---

## Description

h3. Account

*Account F - Email -* [+joseph_elizabeth_francis@psd.test.gov.sg+|mailto:joseph_elizabeth_francis@psd.test.gov.sg], password: {{joseph_elizabeth_francis}}

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as R and click "Report Issue".
# Log out.
# Log back in as F.
# Go to the Home page.

h3. Test Data

Account F

h3. Expected Result

The button stays grey "Issue Reported" across logins until the issue is resolved.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-11)
🎉 Looks good!

---

**Alan Lim** (2026-08-11)
Retested with Account F, but issue already reported. Seems ok.

---

**Alan Lim** (2026-08-11)
Same as 865:  Unable to test under Account B - but Account J worked.

---
*Synced from Jira: 2026-08-24*
