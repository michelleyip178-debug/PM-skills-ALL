# OTEP-74: Profile Details

**Type:** Story
**Status:** UAT
**Assignee:** Imelda Mo
**Story Points:** N/A

---

## Description

*User Story*

As a logged in officer, I can view my profile information right after login so that I can confirm my identity and the role context being used

*Acceptance criteria*

# User will login using WOGAD. During login, unique email address will be used to match and pull the information record from POCDEX
# Users can see these details, pulled from POCDEX fields
## Avatar icon with the initials of the first name
## firstname
## lastname
## email
## employment title/business title
## agencyname
# For the name 
## order it by first name first, followed by last name
# For employment title/business title, look from field “Source System”
## If “HRP”, take {{employmentitle}}
## If “CUMULUS”, take {{businesstitle}}
## If the field contains any other text apart from “HRP” or “Cumulus”, then hide the field
# Each officer will only have one title
## if HRP: take “Primary position”
## if Cumulus: take the latest created time
# For agencyname
## If agency name is “NA” or blank, then this field will be hidden
# If both title and agency name are unavailable, then the divider line is removed
# For 2a to 2f - details should appear in sentence case, with the exception of email (2d), which should be in lower case
# No details in the profile card is clickable.

----

*Tech Notes*

* User details are mapped from fields from POCDEX (see attached file for sample POCDEX data)[^Sample POCDEX data for OTEP.xlsx]

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-116 | Database Schema & Mapping for POCDEX Employee Data | In Progress |
| OTEP-117 | Integrate POCDEX API for Employee Data Retrieval | In Progress |
| OTEP-118 | OTEP Get User Profile API | In Progress |
| OTEP-119 | Implement User Profile UI | Backlog |

---

## Latest Comments

**Adrian Lo:** May need to verify if incoming data are:

* Complete - Defaults to empty of no data in field?
** Or are there any attributes that may come from possibly multiple data fields, and we have priority on which field to use first?
* Up to date
* Title: use Primary position

People can double hat. 

* For double hats, take only primary position (flagged as {{true}})
* To confirm for those with single hat data field

Name: to take from pocdex.

Followup:
- check in with Pathfinder team on FE plans. Which screen to start with first? Do we need to add in a fake login in the mean time, etc


Assumptions:

* Pathfinder team able to make pocdex API available when sprint 2 starts

**Amber Tong:** figma link: [here|https://www.figma.com/design/YzHUyFZTTXV3u4SQbty4ZJ/CareerCompass--Amber-?node-id=5815-58908&t=pQDMYSAdz9lYucEE-4]

!Screenshot 2026-05-14 at 2.22.25 PM.png|width=565,alt="Screenshot 2026-05-14 at 2.22.25 PM.png"!

**Rathika Ramalingam:** *_High Level Test Cases:_*

# _Standard profile loading_ - _Covers AC: 1, 2, 3, 8, 9_

*Scenario 1: Officer logs in and views standard profile details*

* *Given* an officer successfully logs in
* *When* the system matches their unique email and pulls the record from POCDEX
* *Then* the profile card displays the following information:
** Avatar icon with the initial of the first name
** Full name ordered as [First Name] [Last Name]
** Email address in lowercase
** Employment/Business title in sentence case
** Agency name in sentence case
* *And* the UI strictly matches the layout, spacing, and typography defined in the Figma link . [https://www.figma.com/design/YzHUyFZTTXV3u4SQbty4ZJ/CareerCompass--Amber-?node-id=5767-56684&t=tBCCbjo6fgOPCHf8-0|https://www.figma.com/design/YzHUyFZTTXV3u4SQbty4ZJ/CareerCompass--Amber-?node-id=5767-56684&t=tBCCbjo6fgOPCHf8-0|smart-link] 
* *And* none of the details on the profile card are clickable

# _Title Resolution Logic_ - _Covers AC: 4, 5_

*Scenario 2: Displaying title for HRP source system for single job*

* *Given* the officer's record indicates the "Source System" is "HRP"
* *When* the profile data is processed for display
* *Then* the system retrieves the {{employmenttitle}}

*Scenario 3: Displaying title for HRP source system for more than one job*

* *Given* the officer's record indicates the "Source System" is "HRP"
* *When* the profile data is has more than one title
* *And* display the specific {{employmenttitle}} marked as primary position.

*Scenario 4: Displaying title for Cumulus source system for single job*

* *Given* the officer's record indicates the "Source System" is "Cumulus"
* *When* the profile data is processed for display
* *Then* the system retrieves the {{businesstitle}}

*Scenario 5: Displaying title for Cumulus source system for more than one  job*

* *Given* the officer's record indicates the "Source System" is "Cumulus"
* *When* the profile data has more than one title
* *Then* the system retrieves the {{businesstitle}} with the latest created date/time.

*Scenario 6: Hiding the title for unsupported source systems*

* *Given* the officer's record has a "Source System" containing text other than "HRP" or "Cumulus"
* *When* the profile data is processed for display
* *Then* the employment/business title field is completely hidden from the UI

# _Null state or missing data logic - Covers AC: 6, 7_

*Scenario 7: Hiding missing or "NA" agency names*

* *Given* the officer's title ({{employmenttitle}}/ {{businesstitle}}) or {{agencyname}} in POCDEX is blank or explicitly set to "NA" 
* *When* the profile card is rendered
* *Then* the respective field(s) is hidden.

*Scenario 8: Removing the divider line when context is missing*

* *Given* an officer's profile resolves to have NO valid title and hidden
* *And* NO valid agency name and hidden
* *When* the profile card is rendered
* *Then* the UI divider line is removed to prevent awkward spacing

*Synced from Jira: 2026-07-23*
