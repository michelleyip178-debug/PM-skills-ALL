# OTEP-624: CI regression gate & champion promotion

**Type:** Story
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

As a  CIE team,  we want  every candidate build scored against the golden sets and compared to the champion  so that  no detectable quality regression reaches prod. Acceptance criteria PR pipeline stage: build image → eval harness against candidate (in-process with CI creds) for all golden datasets →  compare  step fetches the champion's baseline  eval_run  from RDS. Comparison is  paired per-item  (SQL join on item id across the two runs), gating on: macro F1 and P@5 not below champion beyond noise threshold ε (documented), hard-negative hit rate not above champion. Gate failure blocks merge with a per-item diff table in the PR; pass recorded as an  eval_runs  row. On merge + deploy: promotion is a single transaction updating  champions  (input_type → variant_id + baseline run_id); atomic and audited by design. ε and per-dataset thresholds live in one in-repo config file, reviewed like code.

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-647 | eval/compare.py: paired per-item comparison, ε thresholds, exit code + markdown diff (no cie import — same liftable seam as metrics.py). | Backlog |
| OTEP-648 | CI OIDC role for candidate eval runs (Bedrock + OpenSearch + RDS access from the pipeline).  | Backlog |
| OTEP-649 |  CI workflow stage: candidate eval + compare + PR comment. | Backlog |
| OTEP-650 | Champion promotion transaction wired into the existing merge-to-main deploy. | Backlog |
| OTEP-651 | Runbook: gate override (explicit, logged, two-person) for intentional trade-offs. | Backlog |

---

## Latest Comments

**boonsiangteh** (2026-08-04)
Benjamin AW  mentioned this issue in  a commit  of  WOG / PSD / pdo / intelligence / apps / CIE backend  on branch  OTEP-1123 : [Ben]   chore: merge main (   v3 extraction +   )

---

**boonsiangteh** (2026-08-04)
Benjamin AW  mentioned this issue in  a commit  of  WOG / PSD / pdo / intelligence / apps / CIE backend  on branch  main : Merge branch 'OTEP-624' into 'main'

---

**boonsiangteh** (2026-08-03)
Benjamin AW  mentioned this issue in  a merge request  of  WOG / PSD / pdo / intelligence / apps / CIE backend  on branch  OTEP-624 : [Ben]   fix: re-render golden-set PDF items clipped by fpdf2 cursor bug
