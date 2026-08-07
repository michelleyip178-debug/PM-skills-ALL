# OTEP-117: Integrate POCDEX API for Employee Data Retrieval

**Type:** Sub-task
**Status:** Done
**Assignee:** Pei Ern Lim
**Story Points:** 2.0

---

## Description

Integrate with the POCDEX API to retrieve and map employee information into the system for identification and profile usage.

The integration should fetch the following fields for each employee:

* First Name
* Last Name
* Employment Title
* Agency
* Job Grade
* Job Family
* Job Function
* (Kingsley Todo, update the complete field)

*Requirements:*

# Establish secure connection with POCDEX API.
# Retrieve employee data based on provided identifier or query parameters.
# Map API response fields to internal system fields accurately.
# Implement error handling for API failures, timeouts, or incomplete data.
# Log responses and failures for monitoring and debugging.

*Acceptance Criteria:*

* System successfully retrieves all listed fields from POCDEX API.
* Data is correctly mapped and stored/displayed in the system.
* API errors are handled gracefully with appropriate logging.
* Integration is tested with valid and invalid scenarios.

*Notes:*

* Confirm API authentication method (e.g., OAuth, API key).
* Validate field formats and data consistency from POCDEX.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Kingsley Low:** Personal Draft, Ignorable:

# Establish get client from Pocdex
#  [https://sgtechstack.atlassian.net/browse/OTEP-116|https://sgtechstack.atlassian.net/browse/OTEP-116|smart-link] 
# Database mapping + store
# Encryption
# Error handling

**Kingsley Low:** Assuming actual API implementation will be handled by Path Finder team as we dont have access to actual Pocdex API call

*Synced from Jira: 2026-08-07*
