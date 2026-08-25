# OTEP-939: [CORE] DISC-03 - Free-text search returns relevant courses (OTEP-83)

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
# Search using a Course Name keyword (3+ characters), then press Enter or click "Search".
# Repeat, searching using a Domain name.
# Repeat, searching using a Programme Code.

h3. Test Data

* Keyword: “Data” → 25 courses returned (autocomplete also shows the Domain “Data Analytics” + course-name suggestions).
* Course name: “Hidden data test spy school” 
* Domain name: “Data Analytics” (3 courses).
* Programme Code: “E11DRTJ” → returns the course “[DNT] Test Data for 4309 Rollback Timer tst 01 [JCO]”.

h3. Expected Result

Courses relevant to the search term are returned from across the catalogue for each of the three search types (Course Name, Domain name, Programme Code), and the results count reflects them.

Searching course name should return that one course as the first result, followed by the default search logic in the results list.

Searching programme code should only return that one specific course

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Imelda Mo** (2026-08-18)
this can be moved to done?

---

**Imelda Mo** (2026-08-18)
i have clarified this. please ignore this. thank you

---

**Pei Ern Lim** (2026-08-18)
Hi  , not sure if the understanding is wrong on my side. Per the AC here in no.17 in  OTEP-83 , the free text search will be ordered as below:  So when free text/click in auto-complete, the “full search phrase” should be the first result, but the following will be the rest.

---
*Synced from Jira: 2026-08-24*
