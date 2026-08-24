# OTEP-704: Search Behaviour updates

**Status:** QA
**Assignee:** Adrian Lo
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

Verify the current implemented behaviour if they correspond to the below. Otherwise update accordingly Search auto complete drop down will appear upon typing of 3 characters minimum User can trigger search via the below methods: select an auto complete item Search for the auto complete item click the search button Search for exact text in the text box press enter on the search text box Search for exact text in the text box  Search filter behaviour If the user has filters selected before the search, then the filters will apply to the search If the users searches first, and has an existing list of results, then selecting the filters will filter the existing search The state of the filters will persist, even if the user has performed a search Only way to reset the filters will be if the user manually clears the filters, or navigates away from the page and returns again If the user has filters selected with no text in the text box, and click Search button, the search will run with the filters selected. Same applies if enter is pressed with no text in the text box Search will only run if any of the below conditions are met One or more Filters are selected There is search text or both

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-20*
