# OTEP-937: [CORE] [D] DISC-01 - Discovery page structure (OTEP-83)

**Status:** Done
**Assignee:** Adrian Lo
**Type:** Task
**Labels:** CORE, OTEP-83, uat

---

## Description

h3. Account

*Account D — padmin2 ·* [*padmin2@cscollege.gov.sg*|mailto:padmin2@cscollege.gov.sg] *· password: Padmin@Cc2026*

h3. Test Steps

# Go to the [UAT site|https://uat.careercompass.gov.sg/] and log in as D.
# Click "Explore all courses" from the Learning & Courses landing page.
# Note the page elements and the courses shown, with no search query or filters applied.

h3. Test Data

Uses account D; searches/filters the full course catalogue.

h3. Expected Result

The page shows a search bar, a filter panel (class type, domain, provided by), course listing, and pagination controls. 

With no search query or filters applied, all available courses are displayed, sorted by earliest start date to latest start date

E-learning courses do not have any start or end date

No course count is shown in this default state.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Guo XZ** (2026-08-22)
Separately clarified with Rama that there are 4 logics applied to course sorting.  1. Upcoming courses (start date later than today) - the soonest is shown first Past courses (start date alr passed) - the most recent one is shown first (i.e., start data closest to today) Ok with the sorting.

---

**Imelda Mo** (2026-08-19)
Sent an email to CSC team for guidance

---

**Adrian Lo** (2026-08-19)
verified, this is in UAT now

---
*Synced from Jira: 2026-08-24*
