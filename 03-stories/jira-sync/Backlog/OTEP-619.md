# OTEP-619: Variant identity & registry

**Type:** Story
**Status:** UAT
**Assignee:** Benjamin Aw
**Story Points:** N/A

---

## Description

As a  CIE engineer,  I want  every deployable to carry a deterministic  variant_id   so that  any output, eval report, or judge score can be traced to the exact configuration that produced it. Acceptance criteria variant_id = hash(git_sha, prompt file hashes, model ids, retrieval params, bank index name/version)  computed at build/startup, identical for identical config. Both  cie-inference  and  cie-inference-worker  stamp  variant_id  into every result envelope/response metadata (additive, non-breaking). variants  table maps  variant_id  → config snapshot (JSONB) + created-at + status. Registration at startup is idempotent ( INSERT ... ON CONFLICT DO NOTHING ).

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-626 | cie.core.variant — config fingerprint + variant_id derivation (unit-tested, stable across processes). | Backlog |
| OTEP-627 | Stamp variant_id in HTTP response metadata and SQS output envelope. | Backlog |
| OTEP-628 | Startup registration hook in both services (blocked by CIE-22b schema); docs in CLAUDE.md. | Backlog |

---

## Latest Comments

_No comments._
