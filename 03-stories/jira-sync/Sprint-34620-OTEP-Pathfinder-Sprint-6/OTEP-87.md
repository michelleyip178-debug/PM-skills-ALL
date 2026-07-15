# OTEP-87: View Careers@Gov Opportunity Detail

**Status:** QA
**Assignee:** Thomas Huchedé
**Story Points:** 8
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

User story  As an officer who is actively exploring career moves, I want to view the full details of a Careers@Gov opportunity so I can assess whether it's the right fit and apply directly on the C@G platform. Detail page display The detail page renders the C@G opportunity payload sourced from the C@G API (via  OTEP-377 ) Fields displayed:  title ,  agency ,  description ,  duration , and all available structured job-info fields returned by the C@G payload Responsibilities and pre-requisites are NOT shown inline  — Amber's message directs the officer to click "Apply via Careers@Gov" to find out more. This applies even if the C@G payload includes those fields If any displayed field has no data, show  "Not specified."  Do not hide the field label Layout is consistent with the OTG detail page  ( OTEP-128 ) — same card structure, same "Not specified" fallback, same back-navigation behaviour Apply CTA A single prominent CTA is shown:  "Apply via Careers@Gov" Clicking opens the specific C@G opportunity in a new tab, deep-linking directly to that posting on Careers@Gov ( OTEP-89 ) OTEP captures a  click-to-cag  event at the point of redirect If the opportunity is no longer available on C@G after click-through, that is handled on the C@G side  — OTEP shows no error state for this There is no FormSG redirect and no OTG apply flow for C@G listings Navigation When the officer navigates back using the  in-page "back" link  (not browser back), their filter and pagination state is exactly as they left it Out of scope (S5) Competency match section  — deferred until Imelda's squad confirms schema + field mapping (open item). Do not build a placeholder or empty section Responsibilities and pre-requisites inline — replaced by Amber's "Apply via C@G to find out more" message Out of MVP scope Proficiency-level matching Personalisation of any kind SJR apply handling Dependencies OTEP-377  — Fetch C@G specific payload in detail API (BE) OTEP-378  — Map C@G payload to Detail Page UI (FE) OTEP-379  — Automated tests for C@G detail rendering OTEP-89  — Deep-link CTA behaviour

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Michelle Yip** (2026-06-18)
updated and sharpened this AC as well.

---

**Pow Hwee TAN (PSD)** (2026-06-02)
Hi   , while the title is correct, the details of this ticket currently talk mostly about click to apply. Could you please amend the description and scope to ensure it fully covers showing the actual opportunity details?

---

**Pow Hwee TAN (PSD)** (2026-05-28)
Title has been updated to "View Careers@Gov Opportunity Detail" since Internal Jobs/STIPs/Gigs detail is done in Sprint 2 (OTEP-128/327/314). However, the AC still references FormSG redirect and "Internal Jobs, STIPs, Gigs". Suggest revising AC to reflect C@G behaviour — the Apply CTA should deep-link to Careers@Gov platform (per OTEP-89), not trigger FormSG.

---
*Synced from Jira: 2026-07-15*
