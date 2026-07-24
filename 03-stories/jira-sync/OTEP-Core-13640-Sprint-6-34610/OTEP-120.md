# OTEP-120: Get User Competencies API OTEP Service

**Type:** Sub-task
**Status:** Done
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Implement Get User Competencies API – /users/{userId}/competencies

h4. *Description*

Create an API endpoint to retrieve the list of competencies associated with a user. This includes both system-generated (role-based) and user-added competencies.

h4. *API Endpoint*

GET /users/{userId}/competencies

h4. *Response Structure*

The API should return:

* role_competencies (system-generated based on role_id)
* additional_competencies (user-added)

h4. *Sample Response*



{code:json}{
  "role_competencies": [
    {
      "competency_code": "comp_001",
      "competency_name": "Project Management",
      "competency_type": "core|functional",
      "competency_source":"hrps|cumulus|wog"
      "is_hidden":false,
    }
  ],
  "additional_competencies": [
    {
      "competency_code": "comp_123",
      "competency_name": "Data Visualization"
      "competency_type": "core|functional",
      "competency_source":"hrps|cumulus|wog"
    }
  ]
}{code}

h4. *Acceptance Criteria*

* Endpoint /users/{userId}/competencies is implemented
* Returns both:

** role_competencies
** additional_competencies



Reference: [https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2148533384/User+Profile+Authentication+Role+Mapping|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2148533384/User+Profile+Authentication+Role+Mapping|smart-link]

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Fanxu Wang:** sequence diagram:

[https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2288189532/Sprint+1+identify-profile-competency-flow|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2288189532/Sprint+1+identify-profile-competency-flow|smart-link]

**Fanxu Wang:** As discussed with [~accountid:712020:a67da354-dac1-4916-9690-e37d5fb54f47] and [~accountid:712020:f158b30e-da93-44df-b04c-6e83078033b3] . this ticket will focus on get competencies from table: {{officer_competency}}  . The scope to build data into {{officer_competency}} is not involved.

*Synced from Jira: 2026-07-23*
