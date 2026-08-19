# OTEP-661: Fix: scope down ports for gov corporate network (10.0.0.0/8) in nacl for security

**Type:** Task
**Status:** Backlog
**Assignee:** Hao Eng
**Story Points:** N/A

---

## Description

Context:  we are allowing 10.0.0.0/8 over all ports which can be insecure. although there are higher priority rules which block common ports like 22(ssh), 3389(rdp), we should only allow the ports which we want to expose i.e (80 for redirect and 443 for ssl connections)    this also applies to outbound rules where we should not allow all ports for gov corp network.   we should only allow ephemeral ports (1024 - 65535) for return paths.   Starting Point to work from:   https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-iac/-/blob/main/module/networking/main.tf?ref_type=heads#L2207  AC: look through all nacls and ensure we do not have any rules which allow all ports (use claude code for this to inspect iac) test the app to ensure we can still get http responses (i.e app behavior should remain the same and there should not be any timeout conenctions e.g from comet, cft webhook)

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
