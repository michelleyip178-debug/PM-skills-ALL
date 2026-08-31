# OTEP-899: Add X-Source-Env SQS message attribute to all messages sent to CIE input and feedback queues (all envs)

**Status:** Done
**Assignee:** Pei Ern Lim
**Story Points:** N/A
**Sprint:** OTEP-Intel Sprint 7 (35010)

---

## Description

Add one new SQS message attribute, X-Source-Env, on every message OTEP sends to both CIE queues, in all environments. Environments: dev, qa, uat New attribute: X-Source-Env (String), value is the sending OTEP environment, one of dev, qa or uat. Today’s message attributes: X-Signature: <base64 HMAC> (String)
X-Signature-Alg: HMAC-SHA256 (String)
X-Canonical-Ver: v1 (String) Become (example for uat): X-Signature: <base64 HMAC>
X-Signature-Alg: HMAC-SHA256
X-Canonical-Ver: v1
X-Source-Env: uat  (new)

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-31*
