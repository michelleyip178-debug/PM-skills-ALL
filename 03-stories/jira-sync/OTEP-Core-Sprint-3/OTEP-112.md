# OTEP-112: Add competencies without CIE

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

*User Story*

As an officer, I can search for a specific competency I have in mind to add to my profile so I can build a comprehensive list that represents my capabilities, even if its outside of my current role

*Acceptance Criteria*

Users have 2 ways to add competencies

# Keyword search
# “Upload CV” (using CIE)

*This story focuses only on:*

* *the pop-up after “+” button is clicked*
* *keyword search front-end and backend*
* *upload CV front-end only. The backend is in this ticket* [https://sgtechstack.atlassian.net/browse/OTEP-205?atlOrigin=eyJpIjoiM2EzZDk1NzgwYWZjNDg2ZTg5MDQyZGNhMWU3YzY0ZDkiLCJwIjoiaiJ9|https://sgtechstack.atlassian.net/browse/OTEP-205?atlOrigin=eyJpIjoiM2EzZDk1NzgwYWZjNDg2ZTg5MDQyZGNhMWU3YzY0ZDkiLCJwIjoiaiJ9|smart-link] 

*Search and save competencies*

# Users click the “+” icon at the right to trigger a pop-up with two options to add competencies
## keyword search
## upload CV (front-end only for this ticket. nothing happens when you click this option)
# When users click on the search bar without entering any input, they will not see any recent searches
# Users will be able to type a word to look for a functional competency within the “WOG FCs” and “Agency FCs” tabs of the [OTEP MVP Competency Bank|https://gccprod.sharepoint.com/:x:/r/sites/PSD-OTEP-MST-OTEPITC-WD/Shared%20Documents/OTEP%20ITC-WD/Competencies%20and%20Role%20Profiles%20Banks/%5BMVP%5D%20OTEP%20Competency%20Bank.xlsx?d=wa99397fba2dd4215a2052023a33196e7&csf=1&web=1&e=rIxs2V]
# Only functional competencies can be added to this section
# As users type the word, suggestions matching the competency names will appear as a dropdown according to
## User will type a minimum of three characters before the triggering the auto-suggest
## First priority = keyword “starting with”
## followed by = “contains”
## users will see 10 search results loaded, upon scrolling downwards, another 10 will load 
## Max search results is 20
# Users will be able to see the competency description alongside each of the competency names in the dropdown so they understand the definition
# Users can scroll to browse competencies 
# When the user clicks on a competency, it will be indicated as selected. 
# In the selected state, competency name and description is shown.
# User can proceed to search and select more competencies before saving and the selected competencies should be clear to the user.
# Users can add as many competencies as they want
# Click “Save” to add selected competencies to the My Competency section
# Clicking “cancel” or “X” will close the entire modal

*No Results edge case*

# “No results” should be displayed when doing a keyword search that returns no results.

*Search Display logic*

# Role-based competencies (both OCC and FC), should not be displayed in the dropdown search list. For context, users can only display or hide role-based competencies using the “edit” tool. (See story here: [https://sgtechstack.atlassian.net/browse/OTEP-126?atlOrigin=eyJpIjoiY2Q1NDQ5ZGEwNzUwNDNlZmE0NjA2YTYzZGIyZDA4YTYiLCJwIjoiaiJ9|https://sgtechstack.atlassian.net/browse/OTEP-126?atlOrigin=eyJpIjoiY2Q1NDQ5ZGEwNzUwNDNlZmE0NjA2YTYzZGIyZDA4YTYiLCJwIjoiaiJ9|smart-link] )
# FCs that are already displayed in the self-declared section of the profile is omitted from the drop down search list 
# In the edge case where a duplicated competency is shown in the search list, selected and saved by the user, categorise them according to the respective sections while saving.
## First, check if it is a FC under role-based competencies section
### If it is, check if it is selected as displayed by the user
### If it is not displayed, then display it in profile since the user has searched and selected it
## If it is not a role-based FC, then park it under self-declared competencies section

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-310 | Competency Search API | Backlog |
| OTEP-311 | User Competency CRUD API- Add | Backlog |

---

## Latest Comments

_No comments._
