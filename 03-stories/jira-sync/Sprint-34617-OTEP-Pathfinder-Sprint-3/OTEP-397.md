# OTEP-397: UI for OTG excel file upload

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

User story Users will want to upload excels (once a week frequency) so that backend to pick up and process these files. These excels sheet can come from various sources e.g. OTG. The uploaded file will first be scanned in Cloud File Transfer (CFT), then webhook notification to backend API. Caveats mock a list of profile id for role-based visibility mock CFT at service backend Acceptance Criteria  Select data source before uploading Given I am on the upload page

When the page loads

Then I see a dropdown labelled "Data Source" (or similar)
  And it contains at least the option "OTG"
  And no file upload box is active / submit is disabled
    until a data source is selected

When I select "OTG" from the dropdown

Then the file upload box becomes available
  And I can proceed to select a file Role-based visibility of upload UI (Mock a list of profile Id) Given I am logged in as a user WITHOUT upload permissions

When I navigate to the upload page

Then I cannot see the upload UI at all
  And I am shown a "Not authorised" message Upload a valid OTG Excel file Given I am logged in as a user with upload permissions
  And I am on the upload page
  And I have selected "OTG" from the data source dropdown
  And I have selected a valid .xlsx file in the upload box

When I click "Upload"

Then I see a loading state while the file is uploading
  And then I see "Scanning file for security threats..." while scan is running
  And when complete, a success dialog appears confirming the upload Reject a non-Excel file Given I am on the upload page
  And I have selected a data source from the dropdown

When I attempt to select a non-.xlsx file in the upload box
  (e.g. .csv, .pdf, .png)

Then the file is rejected immediately in the browser
  And the upload box shows an error: "Only .xlsx files are supported"
  And no network request is made
  And I can select a different file File quarantined by virus scan Given I am on the OTG upload page

When I upload a file named "virus.xlsx"
  And the scan service returns an infected result

Then I see an error: "File failed security scan and was rejected"
  And the file is NOT forwarded to the backend
  And no data is imported
  And I can upload a different file
 Scanning in progress — polling state Given I have uploaded a valid .xlsx file and clicked Upload

When the file is submitted and the virus scan is running
  And the browser is polling for scan status

Then I see "Scanning file for security threats..."
  And the Upload button is disabled
  And I cannot submit the form again
  And the UI transitions automatically when the scan result arrives
  And if no result after N seconds, I see a timeout error
 Invalid file content (400) Given I am on the OTG upload page

When I upload an .xlsx file that passes virus scan
  But the backend rejects it (e.g. missing columns, empty sheet)

Then I see the backend's error message (e.g. "file is required", "no rows found")
  And the upload form is reset to allow retry
 Server error (500) Given I am on the OTG upload page

When I upload a valid .xlsx file
  And the backend returns a 500 Internal Server Error

Then I see: "Something went wrong. Please try again."
  And the upload form is reset to allow retry
  And no partial data is shown as successful
 Upload a file with row-level data errors  (bonus) Given I am on the OTG upload page

When I upload a valid .xlsx file that contains rows with bad data
  (e.g. unrecognised agency label, invalid date format)

Then I see a success message indicating the file was received
  And I see a list of row-level warnings, each showing the row number
    and a human-readable error message

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Hao Eng** (2026-06-08)
hi   , heard from Rama that only specific users can access this upload UI. how to identify such user?
