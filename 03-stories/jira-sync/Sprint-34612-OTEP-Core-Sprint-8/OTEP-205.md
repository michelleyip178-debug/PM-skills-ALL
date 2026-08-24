# OTEP-205: Add competencies with CIE

**Status:** In Progress
**Assignee:** N/A
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

User Story As an officer, I can use the inference tool to suggest competencies to add to my profile so that there is less friction and effort on my part to build my competency profile  Acceptance Criteria “Upload CV” - Inference through CV, which appears in two places on the profile  Triggering this feature In the “edit” competencies page, clicking the “+” sign under self-declared competencies section will lead the user to a page to add competencies  the page presents two options for the users, one is keyword search (covered in ticket 112), and another is to generate competencies. Clicking on the option to generate competencies will lead to asking the user to upload a CV in the bottom bar targeted only for uploading a CV to generate competencies a pop-up will appear asking users to upload a CV Uploading a CV Users can upload a .docx document  The document can be a maximum of 5mb only. Users can either drag and drop in the upload area or click “Upload CV” to select a system file. Upon successful uploading of a CV, the “review competencies” button will appear in active state Users can click the trash can icon to remove the document  Generating competencies Clicking “Review competencies” will trigger the CIE and return a list of   0 to 12 most relevant competencies, sorted by relevance. There will be no confidence score indicated. If the competencies are not returned immediately, users will see a loading state while the engine is working. How long the user stays on this page depends on how fast the engine returns with the inferred competencies. The number of returned competencies is dependent on the length of the document and what the CIE engine returns, capped at 12 maximum. There could be 0 competencies returned, in cases for example where the text is irrelevant or too short There is no need to de-duplicate the list with any competencies from the profile (be it role-based or self-declared). User will be able to see the name of the competency and clicking the “eye” icon will trigger a pop-up showing the competency description.  There is no formatting for the competency description, only line breaks The competencies that are recommended are only functional competencies and are only from the WOG FC bank and excludes core and agency-specific competencies These competencies will all be automatically pre-selected.  If users click Save, all competencies will be added to their profile. The competencies returned by the engine for the same document might have some differences, although very minimal. Selecting and saving  Users can tap on the competencies to deselect it from the proposed list. If users click “add to profile”, these deselected competencies will not be added to their profile. Upon clicking “add to profile”, selected competencies should be updated on the profile page accordingly. If the saved competency is a role-based competency, and it is already displayed, do nothing if the saved competency is a role-based competency, and it is hidden on the profile, unhide it  If the saved competency is a self-declared competency, ensure it is not duplicated on the profile For new saved competencies, add under the self-declared competency section Unaccepted file format and error handling If file format for “Upload CV” is not readable, then the user will see an error message, “Unsupported file type, please upload a .docx file.”  For any other error handing for “Upload CV” apart from wrong file format, for eg if the doc is password protected or cannot be read for any other reason, then display the error message, “An error occurred in the upload, please try again.” Other edge case If clicking “review competencies” return zero competencies because the content of the document is too little or blank, then an error state will appear with the title “We could not infer any competencies from the uploaded CV.” If clicking “review competencies” could not call the inference engine (eg. wifi down, connection interrupted etc), then an error state will appear with the title “We couldn't generate your competencies at the moment.”   Tech Notes CIE requirements  File type: restrict to .docx 5mb file limit  CIE handles text extraction or OCR (processing centralised in CIE) Need to do SIS whitelisting in order for officers to upload CV onto OTEP without being blocked Note: CIE is only trained with the WOG FC bank. This means the competency recommendations is only limited to those found from this bank and not the entire competency bank which includes the agency-specific competency

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-416 | UI to send the resume to BE and show the competencies | Done |
| OTEP-597 | Add PDF as supported file type | Done |
| OTEP-407 | Connect OTEP and Intelligence VPC in AWS  | Done |
| OTEP-489 | Backend - Setup client for SQS, S3 and Secret Manager | Done |
| OTEP-410 | API  - Upload resume to Intelligence API and return competencies | Done |
| OTEP-989 | IAC - Update CIE ARN for feedback-task in IAC | Done |
| OTEP-1135 | [BUG] Open items for Competency Inference Engine | To Do |

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-20*
