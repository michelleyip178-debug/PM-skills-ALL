# OTEP-304: Logged-in officer remains authenticated while actively using OTEP

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

As an officer who is actively using OTEP, I want to remain authenticated throughout my session so that I am not interrupted by unexpected login prompts. Active session While I'm actively using OTEP, navigating between pages keeps me logged in —  I am not prompted to re-authenticate mid-session Session expiry handling If my WOG AD session has expired ( timeout managed at the WOG AD level ), OTEP detects the  expired token  and redirects me to the login page — I am not left on a broken or blank page If my session has expired and I try to take an action, I see  "Session expired, please log in again"  — not a broken or blank page Out of scope OTEP does not own or configure the session timeout value  — that is enforced at the WOG AD level

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
