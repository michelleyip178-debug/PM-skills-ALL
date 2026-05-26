# OTEP-234: frontend CI set up

**Type:** Sub-task
**Status:** Done
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

*Security related pipeline are not included in this ticket, it focus on base developer pipeline.*

Set up a  GitLab CI/CD pipeline for the Next.js web app. Replaces the current Auto-DevOps stub with a custom pipeline.



defines  ordered stages: {{quality → test → build → e2e → docker → deploy}}





h3. Code Quality Gates

* {{lint}} job runs {{pnpm lint}} (oxlint) — fails pipeline on violations
* {{fmt-check}} job runs {{pnpm fmt:check}} (oxfmt) — fails pipeline on formatting issues
* Both jobs run in parallel in the {{quality}} stage
* Both jobs trigger on MRs and pushes to main



h3. Unit Test Reporting (MR + Main)

* {{unit-tests}} job runs {{pnpm test run}} (Vitest) in the {{test}} stage
* JUnit XML report is published as an artifact
* GitLab MR shows the *Tests* widget with pass/fail counts, 80% coverage must be met
* Job triggers on MRs and pushes to main



h3. Production Build Validation (MR + Main)

* {{next-build}} job runs {{pnpm build}} (Next.js standalone output)
* TypeScript errors fail the build (Next.js runs {{tsc}} internally)
* {{.next/standalone/}}, {{.next/static/}}, and public exported as pipeline artifacts (1-day expiry)
* {{.next/cache/}} cached for incremental build speedup
* Job triggers on MRs and pushes to main

h3. Docker Build & Push  (MR + Main)

* Image is tagged with both {{$CI_COMMIT_SHA}} and {{latest}}
* Image is pushed to GitLab Container Registry ({{$CI_REGISTRY_IMAGE}})
* Job only triggers on main, and only after build job passes
* No credentials stored in code — uses built-in {{$CI_REGISTRY_*}} variables

h3. E2E Tests will be triggered from QA deployment stage(CD pipelines), not part of CI process, excluded from this ticket



h3.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Fanxu Wang:** pipelines:

{code:yaml}  - local: .gitlab/ci/ci-image.yml
  - local: .gitlab/ci/quality.yml
  - local: .gitlab/ci/test.yml
  - local: .gitlab/ci/build.yml
  - local: .gitlab/ci/docker.yml{code}



ci-image: build custom image for CI jobs

quality: format & lint 
test: unit test coverage, must meet threshold 80%

build: build application artifacts

docker: build application docker image and push to gitlab registry

**Fanxu Wang:** [https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2247299582/WIP+OTEP+CI+CD+Pipelines|https://sgtechstack.atlassian.net/wiki/spaces/OTEP/pages/2247299582/WIP+OTEP+CI+CD+Pipelines|smart-link]

