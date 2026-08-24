# OTEP-140: HTTP client

**Status:** Done
**Assignee:** Kingsley Low
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

Reusable http client I want  to instantiate a central, reusable HTTP client with configurable retry and timeout policies,  So that  our service handles downstream failures gracefully and prevents cascading latency issues.  Requirement Technical Specification Checked Centralization Provide a  NewClient  constructor used to instantiate a shared client during service startup. x Configurability Support parameters for  Timeout ,  MaxRetries ,  RetryWaitMin , and  RetryWaitMax  via environment/config. x Resilience Integrate an exponential backoff strategy (do not use aggressive retries). x Context Awareness Ensure the client respects  context.Context  for request cancellation propagation. x Logging Log outgoing and incoming requests Outgoing and response times as INFO payload & response as DEBUG This will be resolve together in  OTEP-141

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Kingsley Low** (2026-04-29)
Library  go-retryablehttp  is introduced into this task  The reason is to implement standardized resiliency patterns, including exponential backoff and automatic request rewinding, ensuring our service handles transient downstream failures without manual error-handling logic.

---
*Synced from Jira: 2026-08-20*
