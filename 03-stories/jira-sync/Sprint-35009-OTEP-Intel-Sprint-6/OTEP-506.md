# OTEP-506: Switch ACM Certificate from RSA 2048 to ECDSA P-256

**Status:** In Progress
**Assignee:** Fanxu Wang
**Story Points:** N/A
**Sprint:** OTEP-Intel Sprint 6 (35009)

---

## Description

Description Migrate the application TLS certificate from the existing ACM-issued  RSA 2048  certificate to an  ECDSA P-256  certificate. The goal is to use a smaller and more efficient certificate key algorithm while maintaining strong security. ECDSA P-256 is preferred over RSA 2048 because it provides stronger effective security with better TLS handshake efficiency for modern clients.   AC ECDSA should be the default ACM cert for all the environments.  Use ECDSA P-256 instead of ECDSA P-384 as the latter is an overkill with lower performance despite stronger security

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-07-28*
