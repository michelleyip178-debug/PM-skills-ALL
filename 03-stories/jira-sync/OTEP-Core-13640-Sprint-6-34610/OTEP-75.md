# OTEP-75: View My Competencies

**Type:** Story
**Status:** Done
**Assignee:** N/A
**Story Points:** N/A

---

## Description

*User Story*

As a logged in officer, I can view My Competencies so I can track and build my competencies for future career growth

*Acceptance Criteria*

*Default View*

# Logged in users can clearly see the section titled as “My Competencies”
# There are three distinct sections: "Functional Competencies" and "Core Competencies" under Job Role Competencies, followed by a Self-declared Competencies section below.
# Users can see a maximum of 8 competencies per section. If there are 9 or more competencies, a “view more” will trigger a collapsible drawer, hiding the 9th and more competency 

*Job Role Competencies*

# Job Role competencies are competencies that are assigned to the officer’s current role. These competencies are sourced from the HR systems
# Users' can see their competencies sorted into two categories - 1) Core Competencies and 2) Functional Competencies 
# A descriptor should read: “These are competencies associated with your role. Choose which to feature on your profile.”
# User should be able to understand the difference between FC and CC through a tooltip
## For Core Competencies: “Core Competencies articulate the behaviours expected of all public officers and apply across all jobs.”
## For Function Competencies: “Functional Competencies articulate the behaviours expected of officers based on the specific functional domain of their jobs.”

*Self-declared Competencies Display*

# Self-declared Competencies are competencies that are manually added by the user
# This section only contains functional competencies
# A descriptor should read: “Add more competencies to reflect your full range of skills." 

*Duplicate competency handling (from role profile competencies ie. not self-added)*

# Competencies should not be duplicated across sections 
# If there are duplicates, check and assign according to this logic
## First check if it is a core competency assigned to the officer’s role profile. If yes, then park in this section.
## If no, check if it is a functional competency assigned to officer’s role profile. If yes, then park in this section
## If no, add it to “self-declared” competency section 

Note: For cases when officer is self-adding competencies, see here instead [https://sgtechstack.atlassian.net/browse/OTEP-112?atlOrigin=eyJpIjoiZWZmNWRhNzVlMWQyNGZhMmI3NzcwMjNjYThmMjUxNjIiLCJwIjoiaiJ9|https://sgtechstack.atlassian.net/browse/OTEP-112?atlOrigin=eyJpIjoiZWZmNWRhNzVlMWQyNGZhMmI3NzcwMjNjYThmMjUxNjIiLCJwIjoiaiJ9|smart-link] 

*Edge-case: No job role profile and no pre-existing self-declared competencies (OTG competencies)*

Users with no job role profile will not see any role competencies. There are two scenarios: 

# For users with no role profiles and no OTG competencies
## Both job role competencies and self-declared competencies sections will be empty
## They are able to see a feedback mechanism to report the issue in the form of a button “Report Issue”
## Clicking the button will alert us in the backend that there is a missing role problem for us to troubleshoot
## A toast with message “We’ve received your report and are looking into it.” will appear

*[For additional context]* Story: [https://sgtechstack.atlassian.net/browse/OTEP-105|https://sgtechstack.atlassian.net/browse/OTEP-105|smart-link]

For users with no role profile but with OTG competencies

# The OTG competencies will only be populated under the self-declared competencies section 
# The job role competencies section should be empty
# These are previously self-added competencies from OTG 

----

*Tech notes*

+Mapping from POCDEX to HR systems - “HRPS PSD-MCCY-MDDI Profiles” and “Cumulus ESG-CAAS-URA Profiles” tabs+

# Identify officer using NRIC or email address 
# Obtain Job ID 
# Look up Job ID in the HR systems in order to get the expected competencies tagged 
# in HRPS: One officer can have multiple Job IDs. Each job ID can contain multiple job family and function, up to a max of 3
# In Cumulus: One officer has one job ID tagged, but each job ID can contain multiple job family and function, unlimited

+Mapping from POCDEX to OTG Role Profile Bank tab for competencies+

# Get officer job family, function and grade from POCDEX
# String to form {{roleID}}. eg. “Academic OperationsTechnicalOperationsJR10”
# Lookup {{roleID}} in OTG Profile bank file
# under column J “{{skillsIds}}” - these are the competencies assigned to the role
# Map {{skillsIds}} to competencies inside the WOG FC Bank to find the corresponding competency name and description



*Reference Docs*

# [OTEP MVP Competency Bank|https://gccprod.sharepoint.com/:x:/r/sites/PSD-OTEP-MST-OTEPITC-WD/Shared%20Documents/OTEP%20ITC-WD/Competencies%20and%20Role%20Profiles%20Banks/%5BMVP%5D%20OTEP%20Competency%20Bank.xlsx?d=wa99397fba2dd4215a2052023a33196e7&csf=1&web=1&e=rIxs2V]
# [Role Profile Bank for OTEP MVP|https://gccprod.sharepoint.com/:x:/r/sites/PSD-OTEP-MST-OTEPITC-WD/Shared%20Documents/OTEP%20ITC-WD/Competencies%20and%20Role%20Profiles%20Banks/Role%20Profiles%20Bank%20for%20OTEP%20MVP.xlsx?d=w761208e5086a412a80f6b2e126fd1ecd&csf=1&web=1&e=MqR3jq]

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-120 | Get User Competencies API OTEP Service | In Progress |
| OTEP-216 | Import competencies from CFTP | In Progress |
| OTEP-217 | UI to view the competencies | In Progress |
| OTEP-226 | Setup CFTP | In Progress |

---

## Latest Comments

**Imelda Mo:** Refine “report issue” backend and logic for sprint 3.

**Amber Tong:** figma link [here|https://www.figma.com/design/YzHUyFZTTXV3u4SQbty4ZJ/CareerCompass--Amber-?node-id=5767-60306&t=pQDMYSAdz9lYucEE-4]

**Rathika Ramalingam:** High Level Test Cases

# *Scenario 1: Default View and Section Headers*
#* *Given* an officer with valid competencies logs into OTEP
#* *When* they navigate to the Competencies page
#* *Then* the main section is titled "My competencies"
#* *And* a parent section titled job role competencies is rendered
#* *And* under job role competencies, a sub-section titled "Core Competencies" is displayed
#* *And* under job role competencies, a sub-section titled "Functional Competencies" is displayed
#* *And* under job role competencies, a sub-section self-declared competencies from OTG is rendered without a title 
# *Scenario 2: Descriptor Texts Render Correctly*
#* *Given* the Competencies page is rendered
#* *When* the user views the different sections
#* *Then* the Job role section displays the descriptor: "These are competencies associated with your role. Choose which to feature on your profile."
#* *And* the Self-declared section displays the descriptor: "Add more competencies to reflect your full range of skills."
# *Scenario 3: Tooltip Informational Text*
#* *Given* the user is viewing the Job role competencies section
#* *When* they hover over or activate the tooltip or by clicking the info icon for Core competencies
#* *Then* it displays: "Core competencies articulate the behaviours expected of all public officers and apply across all jobs."
#* *When* they activate the tooltip for Functional competencies
#* *Then* it displays: "Functional Competencies articulate the behaviours expected of officers based on the specific functional domain of their jobs."
# *Scenario 4: Displaying 8 or fewer competencies*
#* *Given* a user has exactly 8 Functional/Core competencies assigned
#* *When* the Functional competencies section is rendered
#* *Then* all 8 competencies are visible
#* *And* the "view more" trigger is NOT rendered in the DOM.
# *Scenario 5: Displaying 9 or more competencies (view more trigger)*
#* *Given* a user has 10 Functional/Core competencies assigned
#* *When* the Core competencies section is rendered
#* *Then* exactly 8 competencies are visible by default
#* *And* a "view more" trigger is rendered.
# *Scenario 6: Expanding the view more drawer*
#* *Given* a section has a "view more" trigger visible
#* *When* the user clicks the trigger
#* *Then* a collapsible drawer opens to display the 9th competency and beyond
#* *And* a “view less” trigger is rendered
# *Scenario 7: Collapsing the view less drawer*
#* *Given* a section has a "view less" trigger visible
#* *When* the user clicks the trigger
#* *Then* the collapsible drawer closes, hiding the 9th competency and beyond
#* *And* exactly 8 competencies remain visible on the screen
#* *And* the trigger button text reverts back to "view more".
# *Scenario 7.1: Priority 1 - Resolving duplicates involving Core competencies*
#* *Given* a user's raw data contains the exact same competency as a "Core competency" AND a "Functional competency" AND/OR Self-declared competencies
#* *When* the backend prepares the data payload
#* *Then* the backend assigns the competency exclusively to the {{coreCompetencies}} 
#* *And* removes it from the {{functionalCompetencies}} and {{selfDeclaredCompetencies}} 
# *Scenario 7.2: Priority 2 - Resolving duplicates between Functional and Self-declared competencies*
#* *Given* a user's raw data contains the exact same competency as a "Functional Competency" AND a "Self-declared Competency"
#* *And* the competency is NOT listed as a "Core Competency"
#* *When* the backend prepares the data payload
#* *Then* the backend assigns the competency exclusively to the {{functionalCompetencies}} array
#* *And* removes it completely from the {{selfDeclaredCompetencies}} array.
# *Scenario 7.3: Priority 3 - Retaining unique Self-declared competencies*
#* *Given* a user's raw data contains a "Self-declared Competency"
#* *And* this competency does NOT exist in their "Core" or "Functional" role profiles
#* *When* the backend prepares the data payload
#* *Then* the backend retains the competency in the {{selfDeclaredCompetencies}} array
#* *And* no deduplication action is taken against it.
# *Scenario 8: User with NO job role profile and NO OTG Competencies*
#* *Given* an officer has no role profile mapped in HRPS/Cumulus AND no pre-existing OTG competencies
#* *When* they view the Competencies page
#* *Then* both the Job Role competencies and Self-declared competencies lists are rendered empty
#* *And* a "Report Issue" button is visible to the user.
# *Scenario 9: Submitting a Missing Role Report*
#* *Given* the user is viewing the empty state with the "Report Issue" button
#* *When* they click the "Report Issue" button
#* *And* display a notification toaster at the top right with a text; “We have received your report and are looking into it”, appears for 4 seconds and disappear
#* *And* the the "Report Issue" button is disabled
# *Scenario 10: User with NO Job Role Profile but HAS OTG Competencies*
#* *Given* an officer has no role profile mapped in HRPS/Cumulus
#* *And* the user has previously self-added competencies via OTG
#* *When* they view the Competencies page
#* *Then* the Job Role competencies section is rendered empty
#* *And* the OTG competencies are populated exclusively under the "Self-declared competencies" section.

*Synced from Jira: 2026-08-07*
