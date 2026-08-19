# OTEP-449: Add Target Role modal

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

GO THROUGH EXPLORE NEW ROLE FIRST - SHOULD WE STILL HAVE “ADD TARGET MODAL?  User Story As an officer, I want to search for and add a new target role, so that I can select roles I want to work towards.  Acceptance Criteria Entry Points There are two entry points to trigger this modal Click “Add Target role” button in the “Target Roles” container to directly add target roles Click “Add Target role” button proceeding from the limit reached modal, after selecting roles to remove Search and select The modal should have clear copy to “Add target role” and instructions to select the role to add  There is a search input and drop-down field  After a role is selected, the “Save” becomes active Clicking “Cancel” will close the modal and return back to the original page  Clicking “x” will also close the modal  Clarifying whether this is a checkbox, search keyword?  Saved target roles must be de-duplicated against the drop-down list.  The selection options are disabled once the limit of 3 target roles has been hit (note that if user only has 1 target role saved previously, he will be able to select 2 target roles from this list. If he has 2 saved, then he can only select 1 here)  When the officer clicks “Save”, the selected roles are added to the Target Roles container, the modal closes and the UI updates immediately to reflect the new role(s) added Upon successful addition, TBC DESIGN Check with BOs What is the source of this role list? Should it be all the roles avail in WOG or pre-filtered?? That would be many many  What is the sorting logic? eg. alphabet?    When accessing through the limit-reached flow On “Save”, the system removes selected roles from the remove-role flow, the modal closes and updates the Target Role container accordingly with the new target roles.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
