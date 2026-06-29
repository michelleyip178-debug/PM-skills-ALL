# OTEP-367: Update UI for competencies of opened opportunities

**Status:** Done
**Assignee:** Thomas Huchedé
**Story Points:** N/A

---

## Description

There a few hard coded values in the current opportunity list/details.  the  “Closing Soon"  tag should be extracted out of the current components and use the actual date when appropriate the  <OpportunityTypePill />  should be extracted in it’s own file since it’s being used in two places The SJR can be removed for now     need to align the color/variant with figma (previous color might not match the current ones)

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Rathika Ramalingam** (2026-06-10)
Testing in Local “Closing Soon"  tag should be extracted out of the current components When closing date is today date (n) - The card is hidden      When closing date is tomorrow (n+1) - Label is  Closing today      When closing is from 3 days to 7 days (n+2 to n+7) -  Closing soon      <OpportunityTypePill />  should be extracted The color, border and bg of the tag are incorrect for SJR     Tags - careers@gov and  Internal Jobs  not displaying        I think using full timestamp will fix #1 and #2. For #3 we can ensure the closing soon time in hours is 168 . Also what is the logic to handle commitment_type, I can’t find the column in db. Thanks.
