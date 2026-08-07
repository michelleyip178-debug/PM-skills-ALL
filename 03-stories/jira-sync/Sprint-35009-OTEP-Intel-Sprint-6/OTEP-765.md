# OTEP-765: Provisioning of CIE Feedback SQS through OTEP IAC

**Status:** Done
**Assignee:** Fanxu Wang
**Story Points:** N/A
**Sprint:** OTEP-Intel Sprint 6 (35009)

---

## Description

Currently deployed locally on engineers laptop into DEV and QA for testing. Proper provisioning needs to be done through OTEP’s IaC

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Fanxu Wang** (2026-07-23)
ok I cant provision UAT because otep-intel-sqs-queue-service-otep-uat-task this roles doesnt exist. I think can only provision it once CIE have uat env. This ticket now is blocked.

---

**Fanxu Wang** (2026-07-23)
Dev and QA alrady applied before by    , I’ll create for uat and prod

---

**Fanxu Wang** (2026-07-23)
For now CIE team only have dev env that can be integrated for feedback queue. To provision from UAT env, thats the only possible env we can integrate.    We need to update the IaC later to change the env variables/CIE accounts to CIE uat env later once available.       I think we need seperate ticket to track it. Along with input/output queues.

---
*Synced from Jira: 2026-08-07*
