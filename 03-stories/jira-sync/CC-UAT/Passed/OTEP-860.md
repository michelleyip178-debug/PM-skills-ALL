# OTEP-860: [CORE] EDITCOMP-03 — Hide a competency (save & reversible) (OTEP-126)

**Status:** Done
**Assignee:** N/A
**Type:** Task
**Labels:** CORE, OTEP-126, Profile_Page, uat

---

## Description

h3. Account

*Account C — Davien Soh · Davien_SOH_FROM.TP@cscollege.gov.sg · password: Davien@Cc2026* 

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as C.
# Click the pen icon under role-based competencies.
# Untick one competency (a "Save changes" button now appears).
# Click "Save changes", you’ll be redirect back to the profile page
# Check it is hidden on your profile.
# Re-open the edit page.

h3. Test Data

Account C.

h3. Expected Result

A "Save changes" button appears only after a change; on save a green confirmation toast shows; the competency is hidden on the profile but still listed (unticked) in the edit page - not deleted.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-11)
🎉 Looks good!

---

**Christopher Woo** (2026-08-11)
passed

---
*Synced from Jira: 2026-08-24*
