# OTEP-324: Implement OAuth 2.0 Refresh Token Rotation in NextAuth and Keycloak

**Status:** QA

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

**Rathika Ramalingam** (2026-06-10)
Testing in LOCAL:  Checked by adding console logs.  Issue When an access token expires, multiple components in the app fire simultaneous refresh requests     We got unexpectedly logged out well before the 10-hour limit could be due to this token refresh race condition. Hi    I added the description of the issue above. Please help to check.

---

**Pow Hwee TAN (PSD)** (2026-05-28)
AC is quite thin — "refresh token when expired" and "redirect to temp login page". Suggest expanding to cover: what triggers expiry detection (API 401? proactive check?), token rotation strategy (one-time use refresh tokens?), session lifetime expectations, and edge cases (concurrent tabs, token reuse after rotation).

*Synced from Jira: 2026-06-17*
