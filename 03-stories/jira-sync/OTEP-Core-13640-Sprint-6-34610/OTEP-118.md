# OTEP-118: OTEP Get User Profile API

**Type:** Sub-task
**Status:** Done
**Assignee:** Pei Ern Lim
**Story Points:** N/A

---

## Description

Create an API endpoint to retrieve user profile details from POCDEX (via read replica / API wrapper).

The API will be used for:

* Profile display

h3. *API Endpoint*

GET /users/{userId} (internal user ID, newly added to DB, dont mix with Pocdex UUID)

h3. *Response Fields*

The API should return:

* first_name
* last_name
* employment_title
* agency
* job_grade
* job_family
* job_function

h3. *Acceptance Criteria*

* Endpoint /users/{userId} is implemented
* Returns user profile data for a valid userId
* Response includes all required fields
* Returns appropriate error (e.g. 404) if user is not found
* API integrates with POCDEX data source
* Meets performance expectations

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pei Ern Lim:** Based on latest discussion, this task will consist of 2 API endpoints:

API Endpoint 1: 

[POST] /profiles/identity

Request Body:

{noformat}{
  "email": "john.doe@psd.gov.sg"
}{noformat}

Response Body:

{noformat}{
  "profile_uid": "2d694628-c6d5-4f9b-b715-67e6f77aa880" //Example
}{noformat}

[GET] /api/profiles/{profile_uid}

This endpoint will need the “profile_uid” from above endpoint. 
Response Body:

{noformat}{
    "firstname": "Nurul",
    "lastname": "Aisyah",
    "email": "john.doe@psd.gov.sg",
    "employment_title": "Manager",
    "agency": "Ministry of Health",
    "job_grade": "MX04",
    "job_family": "Corporate Administration",
    "job_function": "Build Community Relations & Foster Partnerships Through Engagement 117"
}{noformat}

**Pei Ern Lim:** Please refer to here for both API Endpoints workflow:

[https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2288189532/Sprint+1+identify-profile-competency-flow|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2288189532/Sprint+1+identify-profile-competency-flow|smart-link] 

Due to the complexity of the Resolve Identity endpoint, propose to create another ticket to reflect the design.

**Pow Hwee TAN (PSD):** MR !48 ([otep-service!48|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-service/-/merge_requests/48]) adds the shared refdata.Reader interface that provides GetAgencyByID() and GetAgencyByCode(). This unblocks the GetAgencyRefByAgencyID panic in MR !44.

Jira: [OTEP-332|https://sgtechstack.atlassian.net/browse/OTEP-332]

*Synced from Jira: 2026-07-23*
