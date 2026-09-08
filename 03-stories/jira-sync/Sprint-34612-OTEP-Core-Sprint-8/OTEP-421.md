# OTEP-421: My Dev - Profile Details 

**Status:** QA
**Assignee:** Pei Ern Lim
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

User Story As a logged-in officer, I can view a summary of my current role, and functional competencies, so that I can quickly verify my profile information and understand my competency areas. Acceptance Criteria Officer can see his current role title The displayed role title must match the officer’s profile page data and retrieved from the same data source  Officer is able to see his functional competencies, grouped into:  “From this role” - role based functional competencies “You’ve added these” for self-declared competencies  These competencie s are a read-only as officers cannot add, edit or remove competencies direction from this section All the user’s role-based and self-declared competencies must match their profile page. competency names and competency order must match any updates made to the officer’s functional competencies on the profile page must be reflected here. The officer can see a Manage competencies button. When the officer clicks Manage competencies, the system navigates the officer to the profile page and anchors directly to the My Competency section. The officer should land at the relevant section, not just the top of the profile page. A tooltip is found next to “Functional Competencies” with the text “Functional Competencies articulate the behaviours expected of officers based on the functional domain of their roles.” The tooltip is accessible via hover Like the profile page, users can see a maximum of 8 competencies per section. If there are 9 or more competencies, a “view more” will trigger a collapsible drawer, hiding the 9th and more competency.  Clicking “view more” will expand to see all competencies, and “view less” will collapse it back to 8. Any updates to the user’s functional competencies in the profile page has to be updated on this page too  Explore new roles bar Users see a call to action prompting them to “Explore new roles”.   Update: No longer show grade - as of 29 Jun

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-542 | Wiring up backend APIs to UI | Done |
| OTEP-674 | [Your Dev] Refactor wiring between client and server in UI | Done |

---

## Latest Comments

**Rathika Ramalingam** (2026-07-01)
cc:

---

**Imelda Mo** (2026-07-01)
BOs have confirmed to drop Grade entirely cc

---
*Synced from Jira: 2026-09-07*
