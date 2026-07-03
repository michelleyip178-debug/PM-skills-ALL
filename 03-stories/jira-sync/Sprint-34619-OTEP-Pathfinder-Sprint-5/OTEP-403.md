# OTEP-403: OTG data import hardening

**Status:** Backlog
**Assignee:** Léo Milbor
**Story Points:** 5

---

## Description

OTG Data Import Hardening Current Context Concurrent execution is  not  catered for No way to tie an import attempt to corresponding  source_otg_opportunity  row No tracing or metrics, we only have basic default endpoint logging Unit&Integration testing review according to     Use custom models and repo method instead of  refdata  package’s. No role base access, every one authenticated can trigger the uploads. Suggested Evolution Concurrent execution For now, we run a single instance of otep-service. But this is not guaranteed to always be true. So we cannot just use a worker in service to force sequential operation. We can use postgresql locking mechanism. This would avoid pulling another dependency for queuing import request. Grouping Import per Request In  otg_importer.go  we can create an ID (and either add it to the  context.Context  or pass it explicitly) that would be saved in each  source_otg_opportunity . Observability We shouldn’t need a log for every row being processed, a summary is already created and the detail is accessible in  source_otg_opportunity.[errors|warnings] . We could however add tracing and metrics (time per row, time per batch, etc.)

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Michelle Yip** (2026-06-26)
The changes for the ingestion logic and rules.

---

**Léo Milbor** (2026-06-10)
I added this story to highlight current limitation and possible solution.
