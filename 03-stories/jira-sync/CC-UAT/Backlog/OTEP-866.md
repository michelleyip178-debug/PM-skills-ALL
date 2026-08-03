# OTEP-866: [CORE] REP-03 — Reported state persists across login (OTEP-290)

**Status:** Backlog
**Assignee:** N/A
**Type:** Task
**Labels:** CORE, OTEP-290, Profile_Page, uat

---

## Description

h3. Account

*Account R — Farah Osman · farah.osman@psd_test.gov.sg · password: Farah@Cc2026 · (SANDBOX (single-use, mirrors C): report issue. Used by REP-01..03 - reporting mutates the account, so it is disposable and never shared.)*

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as R and click "Report Issue".
# Log out.
# Log back in as R.
# Go to the Home page.

h3. Test Data

Account R — farah.osman@psd_test.gov.sg (already reported an issue in REP-02).

h3. Expected Result

The button stays grey "Issue Reported" across logins until the issue is resolved.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-03*
