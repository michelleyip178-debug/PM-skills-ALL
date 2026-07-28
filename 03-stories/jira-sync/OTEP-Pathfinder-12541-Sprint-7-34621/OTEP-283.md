# OTEP-283: Opportunity Detail - Add Ministry icons to detail page

**Status:** In Progress
**Assignee:** Michelle Yip
**Story Points:** 1
**Sprint:** OTEP-Pathfinder Sprint 7 (2026-07-26 → 2026-08-09)

---

## Description

Acceptance Criteria The system must display the Ministry icon next to the agency name.

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-541 | Implement agencies fetching/maping in FE | Done |
| OTEP-540 | Find source for agencies icons | Done |

---

## Latest Comments

**Rathika Ramalingam** (2026-07-15)
Hi    , is this deployed to qa env? I can’t see the logos in detail page.

---

**Michelle Yip** (2026-07-01)
For those with missing logos, we will just have a placeholder.    ok for us to have the placeholder done?   For those logos in the csv without matching agencies, we will need to create them in the reference table

---

**Thomas Huchedé** (2026-06-29)
The list you shared here (   ) looks good but I do have a few gaps: agencies from our reference table (imported from pocdex) that are without icons in the mapping above •	10801085: MHA-HAD
•	18101810: The Cabinet
•	18201820: Industrial Arbitration Court
•	18301831: Members of Parliament
•	18301832: Legal Assistants and Secretariat Assistants
•	18351835: Public Service Commission
•	20402040: MOH Professional Boards and Bodies
•	20402041: Singapore Nursing Board
•	20402042: Singapore Pharmacy Council
•	20402043: Singapore Dental Council
•	20402044: Traditional Chinese Medicine Practitioners Board
•	S-10002023: MUIS Secondment Out Ministry of Culture, Community and Youth (HOLDING)
•	S-10002027: MUIS Secondment Out Ministry of Foreign Affairs (HOLDING)
•	S-11010119: Quality & Operations icons in the csv without matching agencies in our reference table •	Agency for Science, Technology and Research : Agency_for_Science_Technology_and_Research.png
•	Central Provident Fund Board : Central_Provident_Fund_Board.jpg
•	Centre for Strategic Infocomm Technologies : Centre_for_Strategic_Infocomm_Technologies.png
•	Defence Science and Technology Agency : Defence_Science_and_Technology_Agency.png
•	JTC Corporation : JTC_Corporation.png
•	Maritime and Port Authority of Singapore : Maritime_and_Port_Authority_of_Singapore.png
•	MHA - Internal Security Department (ISD) : MHA_Internal_Security_Department_ISD.jpg
•	Military Security Department : Military_Security_Department.png
•	Science and Technology Policy And Plans Office : Science_and_Technology_Policy_And_Plans_Office.png
•	Security & Intelligence Division : Security_Intelligence_Division.png
•	Singapore Legal Service : Singapore_Legal_Service.png
•	Singapore Medical Council : Singapore_Medical_Council.png
•	Supreme Court : Supreme_Court.png What should we do for those?  Do we plan to have a fallback when there’s a missing logo? Or just hide the logo from the card?

---
*Synced from Jira: 2026-07-28*
