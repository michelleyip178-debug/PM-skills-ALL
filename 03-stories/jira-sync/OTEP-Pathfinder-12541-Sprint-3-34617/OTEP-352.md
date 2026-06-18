# OTEP-352: chore: load POCDEX production code table

**Status:** QA
**Assignee:** Hao Eng
**Story Points:** N/A

---

## Description

Load the POCDEX production code table into OTEP database for cross-domain reference lookups. Clarification Questions Responses  Which ref table to look at? ref_agency ref_employment_type Which sheet name to look at, and criteria to get agency and employment type? Acacia mentioned using the  POCDEX_CODE  sheet. Filter the category column “ORGANISATION” for agency Filter the category column = "EMPLOYMENT_TYPE" for employment type Existing data are loaded from POCDEX UAT. They are different from what is in the Masterlist excel.  To retain the UAT data, or considered as dirty data?  To consider them as dirty data. To wipe the seeding data for ref_agency and ref_employment_type and reinsert from excel sheet. Duplicated rows found in the sheet. How to de-duplicate them?    Acacia mentioned to look at the status “ACTIVE” and “INACTIVE”. inactive means pocdex is not usinG active means pocdex is using  to take the “ACTIVE” one if there is duplicate.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Hao Eng** (2026-06-11)
Local verification (wipe and reinsert based on excel) Excel Actual DB output  count is 24 (exclude header)      SELECT COUNT(*) FROM ref_employment_type;  count is 126 (exclude header)  SELECT COUNT(*) FROM ref_agency;    No trailing space based on excel   SELECT * FROM ref_employment_type WHERE code = 'Wholly_Foreign-Owned_Enterprise_(WFOE)';

---

**Hao Eng** (2026-06-10)
checked with Acacia through teams chat. She mentioned using the  POCDEX_CODE  sheet. Filter the category column “ORGANISATION” for agency Filter the category column = "EMPLOYMENT_TYPE" for employment type

---

**Hao Eng** (2026-06-09)
can look for Acacia from ITC (which one is the code table) create migration scripts to take in the excel sheets details - agency and employment type
