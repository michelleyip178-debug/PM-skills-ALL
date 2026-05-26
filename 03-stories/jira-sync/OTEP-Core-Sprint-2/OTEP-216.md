# OTEP-216: Import competencies from CFTP

**Type:** Sub-task
**Status:** In Progress
**Assignee:** Kingsley Low
**Story Points:** N/A

---

## Description

As part of OTEP’s data integration, we need to bring *Role Profile* and *Competency Bank* data into OTEP via *CFTP*. This will allow OTEP to consume authoritative role and competency data for downstream use cases (e.g. role matching, competency assessment, and talent workflows).

This task covers the end‑to‑end setup and implementation of the CFTP-based integration, including data ingestion, transformation (if required), validation, and storage within OTEP.

h3. Scope

* Configure secure CFTP connectivity between source systems and OTEP
* Ingest Role Profile and Competency Bank data files via CFTP
* Parse and map incoming data to OTEP’s internal data model
* Implement validation checks (e.g. schema, mandatory fields, data consistency)
* Handle updates/refreshes according to agreed frequency
* Log processing status and errors for monitoring and support

h3. Out of Scope

* Changes to source system data definitions
* Manual data correction outside agreed validation rules
* Frontend/UI changes consuming this data (covered under separate tasks)

h3. Acceptance Criteria

* Role Profile and Competency Bank data can be successfully received via CFTP
* Data is correctly mapped and persisted in OTEP according to the agreed data model
* Invalid or malformed files are rejected with clear error logs
* Processing status (success/failure) is auditable
* Initial end-to-end run is validated with sample/production-like data

h3. Dependencies / Notes

* Confirmation of file format, schema, and delivery schedule from source systems
* Network and security approvals for CFTP access
* Alignment on data ownership and refresh frequency



[https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2243857685/How+competency+is+mapped+from+Source|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2243857685/How+competency+is+mapped+from+Source|smart-link] 

[https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2198668238/Detailed+Data+Model+-+Competencies|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2198668238/Detailed+Data+Model+-+Competencies|smart-link] 



The following files are only accessible for PSD staffs. for developers, please use the confluence where we have sample file.

Role Profile Bank - [https://gccprod.sharepoint.com/:x:/r/sites/PSD-OTEP-MST-OTEPITC-WD/_layouts/15/Doc.aspx?sourcedoc=%7B761208E5-086A-412A-80F6-B2E126FD1ECD%7D&file=Role%20Profiles%20Bank%20for%20OTEP%20MVP.xlsx&action=default&mobileredirect=true|https://gccprod.sharepoint.com/:x:/r/sites/PSD-OTEP-MST-OTEPITC-WD/_layouts/15/Doc.aspx?sourcedoc=%7B761208E5-086A-412A-80F6-B2E126FD1ECD%7D&file=Role%20Profiles%20Bank%20for%20OTEP%20MVP.xlsx&action=default&mobileredirect=true|smart-link]



Competency Bank - [https://gccprod.sharepoint.com/:x:/r/sites/PSD-OTEP-MST-OTEPITC-WD/_layouts/15/Doc.aspx?sourcedoc=%7BA99397FB-A2DD-4215-A205-2023A33196E7%7D&file=%5BMVP%5D%20OTEP%20Competency%20Bank.xlsx&action=default&mobileredirect=true&wdExp=TEAMS-TREATMENT&web=1&linkOpenTime=1778131421091|https://gccprod.sharepoint.com/:x:/r/sites/PSD-OTEP-MST-OTEPITC-WD/_layouts/15/Doc.aspx?sourcedoc=%7BA99397FB-A2DD-4215-A205-2023A33196E7%7D&file=%5BMVP%5D%20OTEP%20Competency%20Bank.xlsx&action=default&mobileredirect=true&wdExp=TEAMS-TREATMENT&web=1&linkOpenTime=1778131421091|smart-link]





Competency Bank -

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pow Hwee TAN (PSD):** Summarized 4 points from our discussion:

* You are right competency is not ref data.   I am good to remove the ref_competency.  Side note on definition of ref vs competencies, officer type of tables.  Ref generally refer to ‘code’ like values that does not change frequently eg. country codes, agency codes.   Officer, competencies, and going forward, courses too are considered Master Data. 
* About role id - this is new in otep.  For info - the end state is this will be propagated back in the to-be unified HR data platform in PSD
* About jsonb usage - request that you create an ADR to deliberate the use.  I am good to go with this first. As we are not sure of future use cases.  But it is definitely cleaner than concatenated job family+ role id etc.
* About is_wog - yes it is present in pocdex.   There are agency-specific competency.  I am not sure if it still apply in your case.



Others - noted about the need for order number in ref tables.  Will remove those unneeded.  Align your naming convention.

[~accountid:712020:5a4717ac-69a7-49e9-a198-16817e2d37a5] [~accountid:712020:a67da354-dac1-4916-9690-e37d5fb54f47] [~accountid:70121:9d369513-d725-4e3d-a2b8-675d4d862e3a] 

I suggest we record our ADR in gitlab as well under otep-docs.  I am stll trying to find out how to sync gitlab content back to confluence for wider audience awareness besides engineers.

**Adrian Lo:** *Tech Solutioning quesitons:*

Need to figure out the below:

* How to get notified when there is a file in CFTP to be picked up
* How to notify the import process to pick up the file for pprocessing
* Where will the import mechanism be hosted in?
* How will we pick up the file from CFTP?
** direct HTTPS retrieval?
* Do we need to archive files processed for audit purposes?
** will need to provision a S3 bucket if we need this

**Kingsley Low:** [~accountid:70121:9d369513-d725-4e3d-a2b8-675d4d862e3a] As of context from Rama, it’s a webhook

