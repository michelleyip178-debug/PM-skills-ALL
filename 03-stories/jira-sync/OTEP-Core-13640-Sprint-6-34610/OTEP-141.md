# OTEP-141: Logging

**Type:** Sub-task
**Status:** Done
**Assignee:** Kingsley Low
**Story Points:** N/A

---

## Description

h1. Add logging support into repository

*I want* to integrate our internal logging library into the web server and GORM layer with environment-aware toggles and automated sanitization, *So that* we maintain strict production security standards while retaining full debuggability in non-production environments.

In order to make the terminal consistent below is the shared Terminal Log template for both Request(Incall and Outcall) Middleware and SQL

{{TIME | LEVEL | FLOW | METHOD/TYPE | PATH/URL/QUERY | STATUS | LATENCY | REQUEST_ID}}
Note: {{message}} was introduced to json(default empty string) to remain log and param consistency

|*Requirement*|*Technical Specification*|Json Log|*Checked*|
|*Library Usage*|We can leverage: [https://sgts.gitlab-dedicated.com/innersource/lib/go/-/tree/main/experimental/logger|https://sgts.gitlab-dedicated.com/innersource/lib/go/-/tree/main/experimental/logger]
Wrap it in a {{LogConfig}} struct to inject dependencies.| |Not using|
|*Request Middleware*|Create HTTP middleware to log {{Method}}, {{Path}}, {{Status}}, and {{Latency}}. Must include a {{RequestID}} for tracing.|IN
{code:json}{
  "time": "2026-04-30T09:07:33Z",
  "level": "INFO",
  "flow": "IN",
  "request_id": "req-123",
  "msg":"",
  "http": {
    "method": "GET",
    "path": "/api/v1/user",
    "status": 200
  }
}{code}
\\
Out
{code:json}{
  "time": "2026-04-30T09:07:34Z",
  "level": "INFO",
  "flow": "OUT",
  "request_id": "req-123",
  "msg":"",
  "http_client": {
    "method": "POST",
    "url": "https://api.google.com",
    "status": 201,
    "latency_ms": 450,
    "retries": 0
  }
}{code}|v|
|*Environment Toggling*|Implement logic to switch log levels based on {{APP_ENV}}. (e.g., {{LogLevelInfo}} for Prod, {{LogLevelDebug}} for Dev/SIT/UAT).| |v|
|*SQL Logging*|Implement GORM {{logger.Interface}} using our internal logger. Disable SQL log output in Production to prevent noise and potential data leaks.|{code:json}{
  "time": "2026-04-30T09:07:34Z",
  "level": "DEBUG",
  "flow": "INT",
  "request_id": "abc-12",
  "msg":"",
  "db": {
    "query": "SELECT * FROM users WHERE id = ?",
    "rows_affected": 1,
    "latency_ms": 3
  }
}{code}|Suggested to do in a follow-up ticket|
|*Sanitization*|Create a middleware/interceptor wrapper that masks predefined sensitive keys (e.g., {{password}}, {{authorization}}, {{token}}, {{ssn}}) before writing to the sink.| | |

---

## Subtasks

_No subtasks._

---

## Latest Comments

**rama moorthy:** [~accountid:712020:a67da354-dac1-4916-9690-e37d5fb54f47] [~accountid:70121:9d369513-d725-4e3d-a2b8-675d4d862e3a]  [~accountid:712020:f1b20f91-0679-4119-a517-0ec77a28c4f8]  lets align on where do we create the request id ?

**Kingsley Low:** [~accountid:712020:5a4717ac-69a7-49e9-a198-16817e2d37a5] For now it was designed that it will check from FrontEnd Header “X-Request-ID”, if dont have, it will random generate a uuid

**Kingsley Low:** [~accountid:70121:9d369513-d725-4e3d-a2b8-675d4d862e3a] [~accountid:712020:5a4717ac-69a7-49e9-a198-16817e2d37a5] 
Due to development complexity and effectiveness, I suggested to create below ticket as a follow up ticket:

* CloudWatch logging verification (Checked online, JSON format supported, but still need to verify in actual env)
* DB query logging

*Synced from Jira: 2026-07-23*
