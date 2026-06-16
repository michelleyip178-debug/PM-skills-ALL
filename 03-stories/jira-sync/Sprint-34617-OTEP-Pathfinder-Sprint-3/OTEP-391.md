# OTEP-391: Spike: Virus scanning capability on AWS GuardDuty vs CFT

**Status:** Done
**Assignee:** Hao Eng
**Story Points:** N/A

---

## Description

Background OTEP backend is hosted in the intranet. Users will want to upload excels (once a week frequency) for backend to pick up and process these files. It will be a webhook call to the backend API. Proposed using custom UI to upload to our S3 or CFT within intranet zone.  Custom UI can define the file format type to strictly  .xls ,  .xlsx . However, virus scanning capability is required. Options  Cloud File Transfer (CFT) Proposed Flow:  Custom UI →  CFT (Scans & Crosses Zone)  -> Intranet Backend Processing AWS GuardDuty Flow : Custom UI -> AWS S3 ->  GuardDuty Malware Scan  -> EventBridge triggers Webhook -> Backend Processing (in the same AWS GCC) What is it   CFT stores files in transit temporarily in S3 buckets. CFT manages these S3 buckets to perform the necessary upload, scan, transfer, and download functions. Your Receiver application can retrieve the files and move them to your own S3 buckets. retain files for 7 days, then will be deleted virus-scanning CDR file sanitisation remove macros from excels. malware scanning enabled by default can scan encrypted and zipped files cannot process the transfer of password-protected files and folders unless bypass scan override with same filename unless configure specifically not to file size limit: HTTPS Application : Up to 1 GB HTTPS Single-Page Application (SPA) : Internet : Up to 50 MB Intranet : Up to 500 MB webhook notification  to both sender and receiver on file status API specs:      what are the additional things required? S3 bucket to store those downloaded files if required      GuardDuty is a monitoring tool for any malicious activities in aws accounts and workloads can set up GuardDuty Malware Protection for your S3 buckets even without GuardDuty enabled for your AWS account will require event bridge to be configured to send out event notifications/alerting still need to setup a temp bucket so that virus scanning will take place in that bucket what are the additional things required? a temp S3 bucket to kick start scan (with Guard Duty enabled on this bucket) a final S3 bucket to store the scanned files event bridge between temp S3 to lambda for moving file/notification how-to lambda function to move fie from temp S3 to final S3 bucket Conclusion Q: Do we want to retain the file for record-keeping? Yes, preferred. CFT is preferred: since is a govt product, the compliance stuff already there. lesser components to setup since CFT has temp buckets to store the files instead it already does the moving of files before and after scan between buckets (owned by them)  Confluence

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Hao Eng** (2026-06-09)
created confluence tagged in the ticket!

---

**Pow Hwee TAN (PSD)** (2026-06-08)
Agree with the CFT approach.  Good comparison. Can you add a sequence diagram showing the end-to-end flow for the CFT option? i.e. from the user uploading the file in otep-web all the way through to otep-service picking it up for ingestion.      fyi.
