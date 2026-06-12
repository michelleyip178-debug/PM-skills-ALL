# OTEP-391: Spike: Virus scanning capability on AWS GuardDuty vs CFT

**Status:** In Progress
**Assignee:** Hao Eng
**Story Points:** N/A

---

## Description

Background OTEP backend is hosted in the intranet. Users will want to upload excels (once a week frequency) for backend to pick up and process these files. It will be a webhook call to the backend API. Proposed using custom UI to upload to our S3 or CFT within intranet zone.  Custom UI can define the file format type to strictly  .xls ,  .xlsx . However, virus scanning capability is required. Options  Cloud File Transfer (CFT) Proposed Flow:  Custom UI →  CFT (Scans & Crosses Zone)  -> Intranet Backend Processing AWS GuardDuty Flow : Custom UI -> AWS S3 ->  GuardDuty Malware Scan  -> EventBridge triggers Webhook -> Backend Processing (in the same AWS GCC) What is it   CFT stores files in transit temporarily in S3 buckets. CFT manages these S3 buckets to perform the necessary upload, scan, transfer, and download functions. Your Receiver application can retrieve the files and move them to your own S3 buckets. retain files for 7 days, then will be deleted virus-scanning CDR file sanitisation remove macros from excels. malware scanning enabled by default can scan encrypted and zipped files cannot process the transfer of password-protected files and folders unless bypass scan override with same filename unless configure specifically not to file size limit: HTTPS Application : Up to 1 GB HTTPS Single-Page Application (SPA) : Internet : Up to 50 MB Intranet : Up to 500 MB webhook notification  to both sender and receiver on file status API specs:      what are the additional things required? S3 bucket to store those downloaded files if required      GuardDuty is a monitoring tool for any malicious activities in aws accounts and workloads can set up GuardDuty Malware Protection for your S3 buckets even without GuardDuty enabled for your AWS account will require event bridge to be configured to send out event notifications/alerting still need to setup a temp bucket so that virus scanning will take place in that bucket what are the additional things required? a temp S3 bucket to kick start scan (with Guard Duty enabled on this bucket) a final S3 bucket to store the scanned files event bridge between temp S3 to lambda for moving file/notification how-to lambda function to move fie from temp S3 to final S3 bucket Conclusion Q: Do we want to retain the file for record-keeping? Yes, preferred. CFT is preferred: since is a govt product, the compliance stuff already there. lesser components to setup since CFT has temp buckets to store the files instead it already does the moving of files before and after scan between buckets (owned by them)  Mermaid sequenceDiagram
    actor Admin as Admin User
    participant Page as /upload<br>Server Component
    participant Form as UploadForm<br>Client Component
    participant API as otep-service<br>Go Backend
    participant DB as Database
    participant CFT as Cloud File Transfer

    Admin->>Page: GET /upload
    Note over Page: auth() — server-side session &<br>upload permission check
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
    Note over API: Validates auth & file,<br>forwards to CFT using backend-stored credentials

    Note over API: Step 1 — obtain CFT auth code token
    API->>CFT: POST https://api.in.cft.stack.gov.sg/v2/auth<br>Authorization: Basic clientID:clientSecret<br>Header: workflowID<br>Query: application_type=backend
    CFT-->>API: { access_token, expires_in, token_type }

    Note over API: Step 2 — upload file to CFT workflow
    API->>CFT: PUT https://api.in.cft.stack.gov.sg/v2/workflows/{workflowID}/files/{filename}<br>Authorization: Bearer access_token<br>Content-Type: application/octet-stream
    CFT-->>API: 201 — Header: x-cft-file-id

    API->>DB: INSERT upload record<br>{ uploadId, cftFileId, status: "pending" }

    API-->>Form: 202 Accepted — { "uploadId": "<string>" }

    Note over Form: Show "Scanning file for security threats..."<br>Poll backend every 3 s — timeout after 60 s

    loop Poll until terminal state or 60 s timeout
        Form->>API: GET /api/v1/upload/{uploadId}/status
        API->>DB: SELECT status WHERE uploadId = ?
        DB-->>API: { status }
        API-->>Form: { "status": "pending" | "infected" | "processed" }
    end

    Note over CFT,API: CFT POSTs to configured webhook on scan completion
    CFT->>API: POST configured-webhook-url<br>{ workflowEvent: "FileReadyForDownload" | "FileNotClean",<br>  workflowID,<br>  fileDetails: { fileID, key, createdAt, receiverSHA256hash },<br>  sender: { applicationID, zone } }

    API->>DB: SELECT uploadId WHERE cftFileId = fileDetails.fileID
    DB-->>API: { uploadId }

    alt workflowEvent = "FileReadyForDownload"
        API->>CFT: GET https://api.in.cft.stack.gov.sg/v2/files/{fileDetails.fileID}/download<br>Authorization: Bearer access_token
        CFT-->>API: 200 — file binary
        Note over API: Parse Excel, upsert opportunities
        API->>DB: UPDATE status → "processed" WHERE uploadId = ?
    else workflowEvent = "FileNotClean"
        API->>DB: UPDATE status → "infected" WHERE uploadId = ?
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

## Subtasks

_No subtasks._

---

## Latest Comments

**Hao Eng** (2026-06-09)
updated using mermaid diagram in the ticket! will also update in  otep-docs  https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-docs/-/merge_requests/13

---

**Pow Hwee TAN (PSD)** (2026-06-08)
Agree with the CFT approach.  Good comparison. Can you add a sequence diagram showing the end-to-end flow for the CFT option? i.e. from the user uploading the file in otep-web all the way through to otep-service picking it up for ingestion.      fyi.
