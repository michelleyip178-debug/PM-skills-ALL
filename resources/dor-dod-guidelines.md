# Definition of Ready (DoR) & Definition of Done (DoD) Guidelines

**Source:** Rama (facilitator)
**Date added:** 2026-05-13

---

## Epic

| Stage | DoR | DoD |
|-------|-----|-----|
| **Ready** | Impact, outcomes, and benefits clearly identified. Team members identified. Where applicable: Service Design flows thoroughly mapped and reviewed; UX flows and UI assets outlined (design system compliant); Diagram and HLD architected and documented; API Precontract defined and agreed across teams | — |
| **In Development** | — | Development is completed and ready for testing |
| **Testing in Staging** | All child issues are in UAT | — |
| **Testing in UAT** | — | All UAT defects resolved and all user stories accepted by BOs. Item approved and authorised for release to Production |
| **Done** | All child issues are released. All feature flags of releases removed from code | All child issues closed |

---

## Story

| Stage | DoR | DoD |
|-------|-----|-----|
| **Ready** | Prioritised and able to deliver in a sprint. All platform subtasks (including test cases) identified and created. UI assets and UX flows designed and linked to all Acceptance Criteria. Feature flag designed with entry point identified. API Contract identified and documented | — |
| **In Development** | — | Code implementation done with new tests written against test cases. PR raised and assigned to reviewers; all merge checks passed (comment resolution, builds passing, minimum approval). If SDK functionality added/modified, SDK documentation updated as part of PR |
| **Testing in Staging** | PR merged. Implementation deployed and tested (functional tests, design review if applicable) to staging | All bugs found in staging are closed |
| **Testing in UAT** | Implementation deployed and tested in staging, then deployed to UAT release with feature flag turned off (if used) | All bugs found in UAT closed. Feature flag turned on for all users in UAT. End-to-end tests for the feature released into UAT platform |
| **Done** | No open Critical or High severity defects. Release scope confirmed and approved. Rollback or mitigation plan in place (if applicable). Deployment scheduled and approved | Change successfully deployed to Production. Feature flag enabled for intended users in Production (if applicable). Post-deployment checks completed with no blocking issues. No production defects reported within agreed monitoring window. Release formally communicated and closed |

---

## Bug

| Stage | DoR | DoD |
|-------|-----|-----|
| **Ready** | Bug triaged and prioritised. Expected behaviour stated against actual behaviour. Bug successfully reproduced from stated steps and proven to break expected behaviour. Feature flag designed, if applicable | — |
| **In Development** | — | New test case documented. Code implementation done with new tests written against test cases. PR raised and assigned to reviewers; all merge checks passed (comment resolution, builds passing, minimum approval) |
| **Testing in Staging** | PR merged. Implementation deployed and tested (functional tests, design review if applicable) to staging | Re-test in staging passes test case |
| **Testing in UAT** | Implementation deployed and tested in staging, then deployed to UAT release with feature flag turned off (if used) | All bugs found in UAT closed. Feature flag turned on for all users in UAT. End-to-end tests for the feature released into UAT platform |
| **Done** | No open Critical or High severity defects. Release scope confirmed and approved. Rollback or mitigation plan in place (if applicable). Deployment scheduled and approved | Change successfully deployed to Production. Feature flag enabled for intended users in Production (if applicable). Post-deployment checks completed with no blocking issues. No production defects reported within agreed monitoring window. Release formally communicated and closed |

---

## Chore

| Stage | DoR | DoD |
|-------|-----|-----|
| **Ready** | Prioritised. Expected output and all test cases identified. UI/UX designs linked to expected output. Feature flag designed, if applicable | — |
| **In Development** | — | Code implementation done with new tests written against test cases. PR raised and assigned to reviewers; all merge checks passed (comment resolution, builds passing, minimum approval). If SDK functionality added/modified, SDK documentation updated as part of PR |
| **Testing in Staging** | PR merged. Implementation deployed and tested (functional tests, design review if applicable) to staging | All bugs found in staging are closed |
| **Testing in UAT** | Implementation deployed and tested in staging, then deployed to UAT release with feature flag turned off (if used) | All bugs found in UAT closed. Feature flag turned on for all users in UAT. End-to-end tests for the feature released into UAT platform |
| **Done** | No open Critical or High severity defects. Release scope confirmed and approved. Rollback or mitigation plan in place (if applicable). Deployment scheduled and approved | Change successfully deployed to Production. Feature flag enabled for intended users in Production (if applicable). Post-deployment checks completed with no blocking issues. No production defects reported within agreed monitoring window. Release formally communicated and closed |
