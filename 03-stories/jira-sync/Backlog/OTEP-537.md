# OTEP-537: Provision new dedicated ecs service to consume sqs q from otep code

**Type:** Task
**Status:** Backlog
**Assignee:** Benjamin Aw
**Story Points:** N/A

---

## Description

Currently cie backend is an api server and this will eventually be exposed to other teams who will want to consume the api. therefore, as of now, this service is not fit for the use case of being a sqs consumer    Therefore, we should create a dedicated consumer to consume the sqs messages from otep. This also improves security as permissions are not given to a potentially shared api server.    we already have iac modules which can provision these infra so we can just quickly do it.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
