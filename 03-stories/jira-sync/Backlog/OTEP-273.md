# OTEP-273: Harmonise POCDEX API data and authentication 'pocdex' data

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Background:  Currently (as implemented in MR !24), the `otep-service` Auth Middleware validates a user's JWT and performs a direct database lookup (`UserExistsWithEmail`) against the local database to verify if the officer exists in POCDEX. Now that the standalone `otep-pocdex` API service is operational (  ), we need to harmonise the authentication layer to use the API contract for identity resolution rather than relying on direct database coupling. Task List: Remove DB Coupling:  Refactor the Auth Middleware in `otep-service` to remove direct database queries for POCDEX user verification. Integrate POCDEX API:  Update the identity resolution logic to make an HTTP client call to the `otep-pocdex` API (e.g., via the `/v1/officers/identity/resolve` endpoint) to verify the user. Context Enrichment:  Update the middleware to extract and store the resolved `pocdex_uid` into the request context (alongside the email), ensuring downstream feature handlers have the correct identifier for subsequent API calls. Schema Migration:  Move the POCDEX schema currently residing in the authentication service setup over to the `otep-pocdex` repo and its database setup. Cache Alignment:  Ensure the existing 10-minute TTL LRU caching mechanism correctly caches the API resolution results. Type Harmonisation:  Harmonise any authentication-related Go structs/types in `otep-service` to align with the JSON schema exposed by `otep-pocdex`. Acceptance Criteria: The `otep-service` Auth Middleware successfully verifies users by calling the standalone `otep-pocdex` API instead of querying the local database directly. The POCDEX database schema is successfully migrated out of the auth setup and into `otep-pocdex`. The resolved `pocdex_uid` is successfully injected into the request context and accessible by downstream domain handlers. The LRU cache correctly caches the API identity resolution results. Unit tests for the Auth Middleware are updated to mock the `otep-pocdex` HTTP responses rather than database calls.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
