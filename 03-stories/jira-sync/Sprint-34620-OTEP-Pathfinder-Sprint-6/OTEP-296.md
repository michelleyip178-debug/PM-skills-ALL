# OTEP-296: Prepare defined report format that matches data model

**Status:** Done
**Assignee:** Michelle Yip
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

No description provided.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Michelle Yip** (2026-05-19)
For Ringfencing.   Entity B: Audience_Filter (For Targeted Visibility)  This table dictates who is allowed to see the opportunity on their OTEP dashboard, matching the structure of your audience filters report. Filter_ID:  Unique identifier. Opportunity_ID:  Foreign Key to the opportunity. Filter_Type:  The dimension being restricted (e.g.,  Business Unit Filter Type ,  Function Filter Type ,  Location Filter Type ). Allowed_Values:  The IDs or names of the specific allowed groups.

---

**Michelle Yip** (2026-05-19)
Entity A: OTEP_Opportunity (The Parsed Core)  The backend will use an AI script to parse the raw  Description  block into structured fields so OTEP can filter and display them cleanly on the UI. Opportunity_ID:  Unique identifier (e.g., 4521, 4522). Title:  e.g., "[Gig] Virtual Intelligence Chat Assistant". Opportunity_Type:  Gig, STIP, etc.. Status:  Open, Closed, Delisted. Agency / Business_Unit:  Hosting organization (e.g., Government Technology Agency). Job_Function:  e.g., Infocomm Technology & Smart Systems. Location & Remote_Allowed:  Yes/No. Time_Commitment:  Expected hours/days (e.g., 2 days/week, 10 hours/week). Start_Date & End_Date:  Active period. Parsed_Deliverables:  Extracted from the "Key Deliverables" text. Parsed_Benefits:  Extracted from the "Potential Benefits" text. Parsed_Prerequisites:  Extracted from the "Other Pre-requisites" text. Extracted_Apply_Link:  The specific FormSG link isolated from the text block (e.g.,    ...). Extracted_Contact_Emails:  Extracted POC emails.                                  see if this data model is ok?

---

**Pow Hwee TAN (PSD)** (2026-05-18)
Currently there are variations of files with different format, need to define a standard format.

---
*Synced from Jira: 2026-07-14*
