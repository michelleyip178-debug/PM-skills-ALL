# OTEP-195: OpenAPI integration

**Type:** Sub-task
**Status:** Done
**Assignee:** Pei Ern Lim
**Story Points:** N/A

---

## Description

*I want* to automatically generate and serve OpenAPI 3.0 documentation from my Go source code, *So that* API consumers can discover endpoints, understand data structures, and test the API via a built-in UI.



|*Requirement*|*Technical Specification*|
|*Tooling*|Install and initialize {{https://github.com/swaggo/swag}}|
|*Documentation UI*|Expose a {{/swagger/*}} endpoint using {{[github.com/swaggo/http-swagger](https://github.com/swaggo/http-swagger)}} (or the gin/echo equivalent).|
|*General Info*|Define Global API info (Title, Version, BasePath) in {{main.go}}.|
|*Endpoint Metadata*|Annotate the {{/health}} endpoint with {{@Summary}}, {{@Produce}}, and {{@Success}} tags.|
|*Build Integration*|Add a {{make swag}} command to the Makefile to re-generate the {{docs/}} folder.|
|*CI/CD*|Ensure the generated {{docs/}} are committed or generated during the build process to stay in sync.|
|*Toggles*|Ability to toggle the endpoints on or off, depending on the deployment environment.
We will want to have this disabled in Prod, and maybe UAT, but on in other lower environments.|

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pei Ern Lim:** /docs folder are committed into the repository in this MR

*Synced from Jira: 2026-06-08*
