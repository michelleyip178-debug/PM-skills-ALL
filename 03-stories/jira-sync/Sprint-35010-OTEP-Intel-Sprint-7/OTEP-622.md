# OTEP-622: Generalize golden-set eval to JD & Course + scheduled runs

**Status:** In Progress
**Assignee:** Benjamin Aw
**Story Points:** N/A
**Sprint:** OTEP-Intel Sprint 7

---

## Description

As a  CIE team,  we want  the CIE-12 harness to score JD and Course datasets and run nightly per variant  so that  synthetic performance is tracked continuously. Acceptance criteria Dataset contract  {items/, labels.json, input_type} ;  eval/  restructured to  eval/datasets/{cv,jd,course}/  with per-dataset  _dataset  version headers (existing CV set migrates unchanged). run_eval.py  takes  --dataset ; metrics stay in app-agnostic  metrics.py . Runner writes an  eval_runs  row +  source=synthetic  records, in addition to  eval/results/ . Nightly EventBridge rule runs eval for every  variants  row with status  champion|shadow ; failures alarm to the team channel.

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-638 | Restructure eval/ to multi-dataset layout; migrate CV set; keep pytest non-collection intact. | Done |
| OTEP-639 |  --dataset flag + store emission in run_eval.py. | Done |
| OTEP-640 | Seed JD and Course golden sets (placeholder-flagged until labelled, same convention as CVs). | Done |
| OTEP-641 | ECS task family cie-eval, EventBridge schedule, CloudWatch alarm → team channel. Blocks nightly runs. | Done |
| OTEP-701 | Getting labelled HRPS & Cumulus CV + JD data | In Progress |

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-07*
