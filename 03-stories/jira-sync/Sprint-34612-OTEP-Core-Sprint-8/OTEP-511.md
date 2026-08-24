# OTEP-511: Retrieve top recommended roles for a user profile based on competency matching

**Status:** Done
**Assignee:** rama moorthy
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

Provide the backend API for the "Based on your current role" section: given a logged-in officer's current role, grade, and competency profile, return up to  5 recommended target roles  ( 3 lateral  +  2 vertical ) with a functional-competency match for each, so the UI can show relevant career options and competency gaps.  API only — UI is a separate task. Roles come from two sources:  job  (agency-tagged: HRPS/Cumulus) and  role_competency  (global). Grades are normalized via a seeded level table so JR:left_right_arrow:MX and irregular codes compare consistently. Endpoint  GET /api/v1/roles/recommendations/{profileId}  →  { data: [...], meta, error } . Returns an  empty list  when the officer has no valid current role + grade. Each role:  id, source, type (lateral|vertical), title, jobFamily, matchPercent, matchedCount, missingCount, functionalCompetencies[{ code, name, status: you_have_this|to_develop, description }] . Acceptance Criteria Returns up to  3 lateral + 2 vertical  roles for an officer with a valid role + grade; empty list otherwise; 401 unauthenticated. Vertical  =  job  only, same  agency  +  job family  +  job function , grade  one level above ; if  < 2 , expand to same agency + job family (drop function); if  > 2 , random 2. Lateral  =  job  (all agencies) + global  role_competency , same  job family  +  job function ,  same grade level ; if  > 3 , random 3. Grades compared by  level  via a seeded mapping (JR/MX → canonical JR + level); vertical = level + 1. Match %  = overlapping ÷ total functional required × 100,  rounded ; compares the role's  functional  competencies against the officer's  functional + self-declared  (core excluded). Each functional competency tagged  "You have this"  (overlap) or  "To develop"  (no overlap); counts equal matched/missing. Exclude  roles with zero functional competencies and the officer's  own current role . Final list  ordered by match % descending . Competency name + description sourced from the competency data source. Grade levelling (the basis) Every grade (JR or MX) maps to an ordinal  Level  via a seeded reference table.  Higher Level number = more senior  (JR06/MX06 = Level 12 … JR09/MX09 = Level 9 … JR17/MX17 = Level 1). JR and MX at the same Level are equivalent. The officer's current grade → Level  L  (with agency, job family, job function from their current position). Vertical = promotion (one grade above) — 2 roles Grade:  Level = L + 1  (anchor: JR09 → JR08) Same agency Same Job Family AND Job Function Source:  job  table only  (global  role_competency  excluded) Fallback: if fewer than 2 → expand to  same agency + Job Family  (drop Job Function) If more than 2 → random 2 Lateral = sideways (same grade) — 3 roles Grade:  Level = L  (same) Across agencies  (all agencies excluding current agency)  + global  role_competency  roles Same Job Family AND Job Function If more than 3 → random 3 Competency matching (each role) Functional-only, against the officer's  functional + self-declared  competencies (core excluded), by code. matchPercent = round(matched / total × 100) ;  matchedCount  = "you_have_this",  missingCount  = "to_develop". Exclude  roles with zero functional competencies and the officer's own current role. Combine & order (final list) Build each pool independently, then  random-trim  to 3 lateral / 2 vertical. Concatenate  the two pools into one list of up to 5 ( vertical ++ lateral ). Sort the whole list by  matchPercent  descending  (tie → title A–Z). The lateral/vertical label is a property only — it does  not  affect ordering. Selection of  which  roles fill the slots is  random ; the  display order  is by match %. No back-filling — if a pool is short, the result is fewer than 5.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-20*
