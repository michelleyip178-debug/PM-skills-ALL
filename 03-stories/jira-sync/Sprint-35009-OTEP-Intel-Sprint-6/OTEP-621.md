# OTEP-621: Multi-variant output tracking — shadow & replay

**Status:** Done
**Assignee:** Benjamin Aw
**Story Points:** N/A
**Sprint:** OTEP-Intel Sprint 6 (35009)

---

## Description

As a  CIE engineer,  I want  to run ≥2 variants over the same inputs  so that  output differences are attributable to the variant, not the input mix. Acceptance criteria Replay mode: one-shot ECS task (pattern of  cie-ingest ) reads an input batch from the S3 raw archive (selected via SQL on  inference_records ), runs a named variant image in-process, writes  source=shadow  records. Optional live shadow: input queue fan-out to a shadow variant's queue; shadow results go only to the store, never to the OTEP output queue. A documented SQL join compares two variants item-by-item over the same request ids.

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-634 | cie-replay console script: batch selector (date range / sample N), writes source=shadow records. | Done |
| OTEP-635 | ECS task definition family cie-replay + run-task IAM (CI builds image, not auto-deployed — same as cie-ingest). | Done |
| OTEP-636 | Guard: shadow/replay must not publish to SQS_OUTPUT_QUEUE_URL (hard-fail if set). | Done |
| OTEP-637 | (stretch): live shadow fan-out (SNS/EventBridge Pipes + shadow queue) — only if replay proves insufficient. | Done |

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-07-28*
