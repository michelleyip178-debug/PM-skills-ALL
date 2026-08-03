# OTEP-860: [CORE] EDITCOMP-03 — Hide a competency (save & reversible) (OTEP-126)

**Status:** Backlog
**Assignee:** N/A
**Type:** Task
**Labels:** CORE, OTEP-126, Profile_Page, uat

---

## Description

h3. Account

*Account Q — Jia Hao Teo · jiahao.teo@psd_test.gov.sg · password: Jiahao@Cc2026 · (SANDBOX (single-use, mirrors B): hide role competencies. Used by EDITCOMP-01..05 - the hide flow mutates the account, so it is disposable and never shared.)*

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as Q.
# Click the pen icon under role-based competencies.
# Untick one competency (a "Save changes" button now appears).
# Click "Save changes", you’ll be redirect back to the profile page
# Check it is hidden on your profile.
# Re-open the edit page.

h3. Test Data

Account Q — jiahao.teo@psd_test.gov.sg.

h3. Expected Result

A "Save changes" button appears only after a change; on save a green confirmation toast shows; the competency is hidden on the profile but still listed (unticked) in the edit page - not deleted.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-03*
