# OTEP-336: View matched competencies on opportunity detail page

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

As an officer, I want to see which of this opportunity's required competencies I already have when I view the detail page, so that I can assess my fit before deciding to apply.

**Acceptance Criteria**

For Internal Jobs:
1. The detail page renders a "Competencies" section listing each required competency for the opportunity.
2. Each competency shows one of two states — matched or unmatched — based on whether it appears in the officer's POCDEX competency profile. No proficiency level is compared.
3. If the officer's competency profile fails to load, the section renders the opportunity's competency list without match states. No error is surfaced to the officer.

For Gigs and STIPs:
4. The detail page renders the opportunity's competency tags under the heading "What you'll develop." The officer's profile is not referenced.

General:
5. If the opportunity has no competency data, the competency section is not rendered. It does not appear as "Not specified."
6. Competency data on this page is read-only. The officer cannot edit their profile from the detail page.

**Out of scope:**
- Competency match ratio ("X of Y competencies matched") — deferred to R1
- Proficiency level comparison — binary match only for MVP
- C@G opportunities — C@G API integration is Sprint 5+

**Dependencies:**
- Open item #18: Imelda's squad must confirm competency schema, consumption method (API/file/push), and availability timeline before this story can be groomed or sprint-assigned
- OTG competency tags must be mapped to the OTEP competency bank
- POCDEX integration live (OTEP-271, OTEP-203 — Sprint 3 plumbing)

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
