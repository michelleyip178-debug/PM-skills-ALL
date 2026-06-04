# OTEP-87: View Careers@Gov Opportunity Detail

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

User story:  As an officer viewing an opportunity, I want to see a clear Apply button without hunting for it, so I can start my application from the detail page. Sprint 3 scope: Apply CTA only. Competency section is deferred — see Out of Scope below. Acceptance Criteria The Apply CTA is visible - no scrolling needed to find it. For Internal Jobs, STIPs, and Gigs: Apply button is shown and triggers the FormSG redirect (OTEP-319). If  formsg_url  is missing: replace Apply button with “Application form unavailable — contact the posting agency.” If a mandatory display field has no data: show “Not specified.” When I navigate back to the listing (clicking on the “back” link (not- browser)), my filter and pagination state is exactly as I left it. Out of Scope (Sprint 3) Competency match section — deferred pending open item #18 (officer competency data model from Imelda’s squad) Proficiency-level matching Personalisation of any kind For SJRs: no Apply button. Show: “Applications for secondments are managed externally.”

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-377 | Fetch C@G specific payload in detail API | Backlog |
| OTEP-378 | Map C@G payload to Detail Page UI | Backlog |
| OTEP-379 | Automated tests for C@G detail rendering | Backlog |

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-06-02)
Hi   , while the title is correct, the details of this ticket currently talk mostly about click to apply. Could you please amend the description and scope to ensure it fully covers showing the actual opportunity details?

---

**Pow Hwee TAN (PSD)** (2026-05-28)
Title has been updated to "View Careers@Gov Opportunity Detail" since Internal Jobs/STIPs/Gigs detail is done in Sprint 2 (OTEP-128/327/314). However, the AC still references FormSG redirect and "Internal Jobs, STIPs, Gigs". Suggest revising AC to reflect C@G behaviour — the Apply CTA should deep-link to Careers@Gov platform (per OTEP-89), not trigger FormSG.
