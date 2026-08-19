# OTEP-693: Fix DEV otep-service egress proxy config (FQDN, SG rule, CFT bypass)

**Type:** Task
**Status:** Backlog
**Assignee:** Pow Hwee TAN (PSD)
**Story Points:** N/A

---

## Description

CFT uploads register (201) but never process. Proxy env vars added to otep-service broke all outbound calls: short hostname doesn't resolve (Service Connect off on egress-proxy, Cloud Map DNS only), otep-service SG lacks TCP 3128 egress, and CFT (intranet-routed) must bypass the proxy. Proxy is only needed for the Careers@Gov import workers. Fix: use Cloud Map FQDN for HTTP(S)_PROXY, add egress_proxy_cidrs for the 3128 SG rule, add api.in.cft.stack.gov.sg to NO_PROXY (keep .amazonaws.com). MR:  otep-iac!67

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
