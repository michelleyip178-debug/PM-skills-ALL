# OTEP-205: Add competencies with CIE

**Type:** Story
**Status:** QA
**Assignee:** N/A
**Story Points:** N/A

---

## Description

*User Story*

As an officer, I can use the inference tool to suggest competencies to add to my profile so that there is less friction and effort on my part to build my competency profile 

*Acceptance Criteria*

This story focuses on the other 2 methods of inferring competencies

*“Upload CV” - Inference through CV, which appears in two places on the profile* 

*Triggering this feature*

# when clicking the “+” sign under self-declared competencies section
##  a pop-up will appear with two options for the users, one is keyword search (covered in ticket 112), and another is to generate competencies. Clicking on the option to generate competencies will lead to asking the user to upload a CV
# in the bottom bar targeted only for uploading a CV to generate competencies
## a pop-up will appear asking users to upload a CV

*Uploading a CV*

# Users can upload a .docx document 
# Users can either drag and drop in the upload area or click “Upload CV” to select a system file.

*Generating competencies*

# Clicking “Generate” will trigger the CIE and return a list of 8 most relevant competencies, sorted by relevance. There will be no confidence score indicated
# User will be able to see the name of the competency and the description
# The competencies that are recommended are only functional competencies and are only from the WOG FC bank and excludes core and agency-specific competencies
# These competencies will all be automatically pre-selected. If users click Save, all 8 will be added to their profile
# *To discuss withvictor*
## *to add a diclaimer that this is generate through AI?* 
## *to check with victor whether more competencies should be suggested based on length of CV?* 
## *to check if there might be a situation where all of the inferred copmetencies are role-based competencies?*

*Selecting and saving* 

# Users can tap on the competencies to deselect it from the proposed list. If users click Save, these deselected competencies will not be added to their profile.
# For the competencies added to the profile, they will be automatically sorted into role-based functional competencies or self-declared competencies 
## If a role-based functional competency was previously hidden by the user, if the user saves the same competency in the upload CV pop-up, then it will be displayed ie un-hide.

*Unaccepted file format and error handling*

# If file format for “Upload CV” is not readable, then the user will see an error message, “Unsupported file type, please upload a .docx file.” 
# For any other error handing for “Upload CV” apart from wrong file format, for eg if the doc is password protected or cannot be read for any other reason, then display the error message, “An error occurred in the upload, please try again.”

----

*Tech Notes*

CIE requirements 

* File type: restrict to .docx
* 5mb file limit 
* CIE handles text extraction or OCR (processing centralised in CIE)

Need to do SIS whitelisting in order for officers to upload CV onto OTEP without being blocked

Note: CIE is only trained with the WOG FC bank. This means the competency recommendations is only limited to those found from this bank and not the entire competency bank which includes the agency-specific competency

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

*Synced from Jira: 2026-07-23*
