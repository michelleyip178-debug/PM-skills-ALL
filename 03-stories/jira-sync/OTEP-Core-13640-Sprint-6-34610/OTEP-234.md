# OTEP-234: frontend CI set up

**Type:** Sub-task
**Status:** Done
**Assignee:** Fanxu Wang
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 6 (id 34610, active)

---

## Description

Security related pipeline are not included in this ticket, it focus on base developer pipeline. Set up a  GitLab CI/CD pipeline for the Next.js web app. Replaces the current Auto-DevOps stub with a custom pipeline. defines  ordered stages:  quality → test → build → e2e → docker → deploy Code Quality Gates lint  job runs  pnpm lint  (oxlint) — fails pipeline on violations fmt-check  job runs  pnpm fmt:check  (oxfmt) — fails pipeline on formatting issues Both jobs run in parallel in the  quality  stage Both jobs trigger on MRs and pushes to main Unit Test Reporting (MR + Main) unit-tests  job runs  pnpm test run  (Vitest) in the  test  stage JUnit XML report is published as an artifact GitLab MR shows the  Tests  widget with pass/fail counts, 80% coverage must be met Job triggers on MRs and pushes to main Production Build Validation (MR + Main) next-build  job runs  pnpm build  (Next.js standalone output) TypeScript errors fail the build (Next.js runs  tsc  internally) .next/standalone/ ,  .next/static/ , and public exported as pipeline artifacts (1-day expiry) .next/cache/  cached for incremental build speedup Job triggers on MRs and pushes to main Docker Build & Push  (MR + Main) Image is tagged with both  $CI_COMMIT_SHA  and  latest Image is pushed to GitLab Container Registry ( $CI_REGISTRY_IMAGE ) Job only triggers on main, and only after build job passes No credentials stored in code — uses built-in  $CI_REGISTRY_*  variables E2E Tests will be triggered from QA deployment stage(CD pipelines), not part of CI process, excluded from this ticket

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-07-23*
