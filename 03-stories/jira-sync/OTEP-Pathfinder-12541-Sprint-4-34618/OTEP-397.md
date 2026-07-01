# OTEP-397: [spike] Discover OTG excel file upload - Flow and UI

**Status:** Done
**Assignee:** Michelle Yip
**Story Points:** 3.0

---

## Description

User story Users will want to upload excels (once a week frequency) so that backend to pick up and process these files. These excels sheet can come from various sources e.g. OTG. The uploaded file will first be scanned in Cloud File Transfer (CFT), then webhook notification to backend API. UI Component Acceptance criteria I must select a data source from dropdown before the file upload input becomes available I cannot see the upload UI if I don't have upload permissions I can upload a valid  .xlsx  file and see a success confirmation I see an inline error if I try to select a non- .xlsx  file I see an inline error if my file exceeds the size limit I see a "scanning" state while my file is being checked for threats I see an error and can retry if my file fails the virus scan I see a generic error and can retry if the server fails (500) Out of Scope Actual CFT integration — scan responses are mocked/stubbed Actual role/permission system — upload access is mocked via a hardcoded profile ID list Backend data import and processing logic Invalid file content errors (400) — backend validation of missing columns, empty sheets, etc. Row-level data warnings   — bad data rows, unrecognised labels, invalid formats Upload history or audit trail UI Multiple file upload in one submission

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Hao Eng** (2026-06-09)
mermaid diagram sequenceDiagram
    actor Admin as Admin User
    participant Page as /upload<br>Server Component
    participant Form as UploadForm<br>Client Component
    participant API as otep-service<br>Go Backend
    participant DB as Database

    Admin->>Page: GET /upload
    Note over Page: Check profile ID against hardcoded<br>allowlist (mocked permission check)
    alt Not authorised
        Page-->>Admin: Render "Not authorised"
    else Authorised
        Page-->>Admin: Render upload form
    end

    Admin->>Form: Select "OTG" from Data Source dropdown
    Note over Form: File upload control becomes enabled

    Admin->>Form: Select file
    Note over Form: Client-side validation:<br>check .xlsx extension + MIME type,<br>check file size limit
    alt Invalid file type
        Form-->>Admin: "Only .xlsx files are supported"
    else File exceeds size limit
        Form-->>Admin: Inline size limit error
    else Valid .xlsx within size limit
        Form-->>Admin: Show filename, enable Submit button
    end

    Admin->>Form: Click Upload
    Note over Form: Show loading indicator<br>Disable submit button

    Form->>API: POST /api/v1/upload<br>multipart/form-data (file, dataSource)
    Note over API: Validates auth & file,<br>stubs CFT scan — returns uploadId immediately
    API->>DB: INSERT upload record<br>{ uploadId, status: "pending" }

    API-->>Form: 202 Accepted — { "uploadId": "<string>" }

    Note over Form: Show "Scanning file for security threats..."<br>Poll backend every 3 s — timeout after 60 s

    loop Poll until terminal state or 60 s timeout
        Form->>API: GET /api/v1/upload/{uploadId}/status
        API->>DB: SELECT status WHERE uploadId = ?
        DB-->>API: { status }
        API-->>Form: { "status": "pending" | "infected" | "processed" }
    end

    alt Status "processed"
        Form-->>Admin: Success confirmation
        Note over Form: After dismiss — reset form for next upload
    else Status "infected"
        Form-->>Admin: "File failed security scan and was rejected"
        Note over Form: Reset form for retry
    else Polling timeout (60 s)
        Form-->>Admin: Timeout error message
        Note over Form: Reset form for retry
    else Backend 500
        Form-->>Admin: "Something went wrong. Please try again."
        Note over Form: Reset form for retry
    end

---

**Hao Eng** (2026-06-09)
there will be a new field called “role” to be added in keycloak  no Jira ticket yet!

---

**Hao Eng** (2026-06-08)
hi   , heard from Rama that only specific users can access this upload UI. how to identify such user?

*Synced from Jira: 2026-07-01*
