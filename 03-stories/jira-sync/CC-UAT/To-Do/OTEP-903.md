# OTEP-903: Role Competency Logic

**Status:** Selected for Development
**Assignee:** Kingsley Low
**Type:** Task
**Labels:** OTEP-126, core, uat

---

## Description

h3. Background

The officer competency compute pipeline derives an officer's competencies from three sources: *additional* (POCDEX), *agency* (job-level core competencies), and *global* (job family + function + grade concatenation route). The pipeline was previously constrained to a single {{position_jobinfo}} row per {{position_id}}, and a single {{job}} per position.

h3. Problem

A {{position_id}} can map to *multiple* {{position_jobinfo}} rows (e.g., the same position code shared across different employments or job configurations). Each position can also link to *multiple* job records via a shared {{job_id}} key (jobs can differ by agency, family, or function). The old single-row lookup caused incomplete or incorrect competency sets for officers in these scenarios.

Additionally, the global competency route (fam + func + grade label concatenation) needed to be *configurable*: some environments require it to always run alongside agency competencies, while others only need it as a fallback when no job is found.

h3. What Changed

# *Multi-position lookup* — {{GetJobByPositionID}} replaced by {{ListPositionsByPositionID}}, which returns all active {{position_jobinfo}} rows for a given {{position_id}}.
# *Multi-job accumulation* — For each position, {{ListJobsByPositionID}} fetches all linked job records; agency competencies are accumulated across all of them.
# *New* {{Position}} domain type — {{OfficerCompetencyPosition}} carries {{JobFamilyID}}, {{JobFunctionID}}, and {{JobGradeID}} needed to drive the global concat route directly from the position record.
# *Configurable concat route* — {{enableConcatRoute}} boolean is threaded from config into the orchestrator:
#* {{true}} (default) — global competencies are always fetched for every position.
#* {{false}} — global competencies are only fetched when no job is found across all positions (fallback).
# *New env var* — {{COMPETENCY_ENABLE_CONCAT_ROUTE}} (boolean, default {{true}}) controls the flag at runtime.

h3. Scope

* {{internal/service/competency/domain/}}
* {{internal/service/competency/repository/}}
* {{internal/shared/config/}}
* {{internal/service/profile/router.go}} (wires the new flag)

No API contract changes. No new endpoints. No schema migrations.

----

h2. Acceptance Criteria

h3. AC1 — Multi-position support

* [ ] Given a {{position_id}} that maps to *N* {{position_jobinfo}} rows, the compute pipeline processes all N positions (not just the first).
* [ ] If {{ListPositionsByPositionID}} returns an empty list, the pipeline returns only additional (POCDEX) competencies and logs a warning.

h3. AC2 — Multi-job agency competency accumulation

* [ ] For each position, all active job records linked via {{job_id}} are fetched.
* [ ] Agency competencies from all jobs across all positions are merged into the final competency map.
* [ ] If a job yields no agency competencies, an error is logged but processing continues for remaining jobs.

h3. AC3 — Concat route feature flag ({{COMPETENCY_ENABLE_CONCAT_ROUTE}})

* [ ] When {{COMPETENCY_ENABLE_CONCAT_ROUTE=true}} (default), global competencies (fam + func + grade) are fetched for *every* position, regardless of whether a job was found.
* [ ] When {{COMPETENCY_ENABLE_CONCAT_ROUTE=false}}, global competencies are only fetched when *no job* is found across all positions (fallback behavior).
* [ ] The env var defaults to {{true}} when not set.
* [ ] An invalid (non-boolean) value for {{COMPETENCY_ENABLE_CONCAT_ROUTE}} causes the service to fail at startup with a descriptive error.

h3. AC4 — Repository contract

* [ ] {{ListPositionsByPositionID(ctx, positionID)}} returns all non-deleted {{position_jobinfo}} rows with the matching {{position_id}}.
* [ ] {{ListJobsByPositionID(ctx, positionID)}} returns all active, non-deleted {{job}} rows linked to the position's {{job_id}}.
* [ ] {{GetJobByID(ctx, jobID)}} looks up a job directly by its UUID (replaces the old position-joined query).

h3. AC5 — No regression

* [ ] All existing unit tests pass.
* [ ] New table-driven unit tests cover: single-position/single-job (happy path), multi-position/multi-job accumulation, empty positions (fallback), concat route enabled vs disabled.

h3. AC6 — Configuration

* [ ] {{CompetencyConfig}} is loaded at startup via {{config.Load()}}.
* [ ] {{.env.example}} documents {{COMPETENCY_ENABLE_CONCAT_ROUTE}}.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-03*
