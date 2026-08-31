# OTEP-618: CIE Evaluation & Quality Platform

**Status:** Backlog
**Assignee:** Victor ONG
**Story Points:** N/A
**Sprint:** OTEP-Intel Sprint 7 (35010)

---

## Description

CIE will run multiple variants (prompt, retrieval, rerank, model changes) over CVs, JDs, and Courses. Today we can deploy a change but cannot systematically answer: what did each variant output, how does it score against golden labels, how well does it perform on real traffic, and did the latest change regress quality? This epic delivers a single  evaluation store on the existing RDS (Postgres)  — structured records in tables, raw input documents as S3 blobs referenced by key — fed by every inference path and consumed by four capabilities: Output tracking  — every inference result stamped with a  variant_id  and persisted, queryable per variant/input-type. Synthetic/golden-set evaluation  — the existing  eval/  harness (CIE-12) generalized to JD/Course datasets, run per variant on a schedule. LLM-as-judge on real traffic  — sampled production outputs scored by a calibrated Bedrock judge, async, budget-capped. CI regression gate  — every candidate build evaluated against the golden set and compared (paired per-item SQL join) to the current champion; deploys blocked on detectable regression, champion promoted transactionally on pass. Core schema (v1):   variants  (registry: id, config snapshot JSONB, status  candidate|shadow|champion|retired ),  eval_runs  (run metadata: dataset version + labels sha, mode, git sha),  inference_records  (per request: variant_id, request_id, input_type, source  prod|shadow|synthetic , ranked predictions JSONB, latency, s3_raw_key, timestamp),  judge_scores  (record_id, judge prompt version, scores, calibration flag),  champions  (input_type → variant_id + baseline run_id, unique per input_type). Success criteria Any production or eval output traces to an exact  variant_id  (code + prompts + models + retrieval params + bank index version). Nightly per-variant P/R/F1/P@5 trends per input type on a dashboard (Grafana/QuickSight direct on Postgres). Judge scores exist for a sampled slice of real traffic, with a published judge-vs-human agreement number. No image reaches prod without passing the regression gate; every promotion is a transactional champion update.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-31*
