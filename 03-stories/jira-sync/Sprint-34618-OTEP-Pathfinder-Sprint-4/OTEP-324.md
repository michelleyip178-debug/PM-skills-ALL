# OTEP-324: Implement OAuth 2.0 Refresh Token Rotation in NextAuth and Keycloak

**Status:** Done
**Assignee:** Thomas Huchedé
**Story Points:** N/A

---

## Description

As a  Developer/QA using the XXX app,  I want  the application to automatically refresh expired access tokens in the background using OAuth 2.0 refresh tokens,  So that  I can maintain a continuous session without experiencing sudden  401 Unauthorized  API errors or being abruptly forced to log back in. Acceptance criteria refresh the token when expired using  next-auth redirect user to a temp login page to easily log back in when credentials are expired instead of showing a error edit: taking out redirection since it’s part of

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Rathika Ramalingam** (2026-06-24)
Testing Done in Dev Scenario Actual Result Status Capture Initial Session State Action:  Log into the application and open the token debug UI. Verification:  Expand the token details to reveal the raw string values.   PASS Wait for token expiry Action : Wait for the initial token to expire exactly in 5m time Verification:  Expand the token details to reveal the raw string values is the same as initial state.  PASS Trigger Token Rotation Send the request again to server to trigger a session update. Verification:  The user remains seamlessly authenticated without being forced to the login screen.  PASS Capture Rotated Session State Action:  Open the token debug UI again. Verification:  Confirm that a completely new Access Token  and  a completely new Refresh Token have been issued by comparing the new strings against the screenshot from Step 1. Both expiration timers should also be reset.  PASS

---

**Rathika Ramalingam** (2026-06-10)
Testing in LOCAL:  Checked by adding console logs.  Issue When an access token expires, multiple components in the app fire simultaneous refresh requests     We got unexpectedly logged out well before the 10-hour limit could be due to this token refresh race condition. Hi    I added the description of the issue above. Please help to check.

---

**Pow Hwee TAN (PSD)** (2026-05-28)
AC is quite thin — "refresh token when expired" and "redirect to temp login page". Suggest expanding to cover: what triggers expiry detection (API 401? proactive check?), token rotation strategy (one-time use refresh tokens?), session lifetime expectations, and edge cases (concurrent tabs, token reuse after rotation).

*Synced from Jira: 2026-08-07*
