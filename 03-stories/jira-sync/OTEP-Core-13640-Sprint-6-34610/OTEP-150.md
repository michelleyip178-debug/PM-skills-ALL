# OTEP-150: OpenSpec integration into repository

**Type:** Sub-task
**Status:** Done
**Assignee:** Adrian Lo
**Story Points:** N/A

---

## Description

*I want to* integrate OpenSpec into the existing Go repository and configure GitHub Copilot context, *So that* we can transition to a contract-first development workflow where AI agents generate type-safe boilerplate, handlers, and tests with 100% alignment to the specification.



|*Category*|*Requirement*|*Implementation Detail*|
|*Tooling*|*OpenSpec Initialization*|Initialize {{openspec.yaml}} at root. Integrate {{SpecKit}} or OpenSpec CLI into the {{Makefile}}/{{Taskfile}} for local validation.|
|*Architecture*|*Type Scaffolding*|Map OpenSpec components to internal Go structs/interfaces. Ensure a clear separation between generated spec models and domain logic.|
|*AI Alignment*|*Copilot Instructions*|Create/update {{.github/copilot-instructions.md}}. Define the spec as the "Source of Truth" and enforce idiomatic Go patterns (e.g., standard library, specific error handling).|
|*Workflow*|*Directory Structure*|Establish a {{/spec}} directory for modularized definitions. Update CI pipelines (GitHub Actions) to include {{spec-lint}} and {{breaking-change}} checks.|
| | | |





|*ID*|*Criteria*|*Definition of Done (DoD)*|
|*AC 1*|*Spec Validity*|{{openspec.yaml}} exists in the root and passes all {{openspec-cli lint}} rules without warnings.|
|*AC 2*|*Copilot Verification*|Successful demonstration of Copilot generating a valid Go handler or test case using _only_ the context provided by the OpenSpec file.|
|*AC 3*|*Process Docs*|{{README.md}} updated with the new SDD workflow: *Modify Spec → Validate → Generate Code → Logic Implementation.*|
|*AC 4*|*CI Integration*|The build pipeline fails if the implementation deviates from the OpenSpec contract or if the spec is syntactically invalid.|

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Fanxu Wang:** [~accountid:70121:9d369513-d725-4e3d-a2b8-675d4d862e3a] please help fill in the ticket description

*Synced from Jira: 2026-07-23*
