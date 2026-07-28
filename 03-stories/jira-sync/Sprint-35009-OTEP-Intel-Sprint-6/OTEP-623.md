# OTEP-623: LLM-as-judge on real traffic, with calibration

**Status:** Done
**Assignee:** Benjamin Aw
**Story Points:** N/A
**Sprint:** OTEP-Intel Sprint 6 (35009)

---

## Description

As a  CIE team,  we want  a calibrated LLM judge scoring sampled production outputs  so that  we measure quality on real data where no golden labels exist. Acceptance criteria Judge runs as a  scheduled batch task  (not a service): each run samples unscored  source=prod  records via SQL ( JUDGE_SAMPLE_RATE ), scores with Bedrock Claude at temperature 0 using a per-input-type rubric, writes  judge_scores  rows keyed to the record. Judge prompts live in  cie/prompts/ , versioned; version recorded in every  judge_scores  row. Calibration job: judge over golden set → agreement vs human labels (Cohen's kappa + correlation) stored; minimum agreement threshold documented, below which judge scores are flagged non-authoritative. Hard daily Bedrock budget cap (max scored items/day, enforced via a count query); never touches the inference request path.

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-642 | Judge rubric prompts v1 (cie/prompts/judge_{cv,jd,course}_v1.txt). | Done |
| OTEP-643 | cie-judge batch task: SQL sampler → Bedrock → judge_scores; budget + rate caps; idempotent (skip already-scored records). | Done |
| OTEP-644 | Calibration runner + agreement metrics (extend metrics.py, keep app-agnostic). | Done |
| OTEP-645 | ECS task family cie-judge + EventBridge schedule + IAM (Bedrock invoke, RDS, S3 raw read) + Bedrock cost alarm. Blocks 25b in any deployed env. | Done |
| OTEP-646 | Dashboard panel: judge score trend per variant beside latest calibration number. | Done |

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-07-28*
