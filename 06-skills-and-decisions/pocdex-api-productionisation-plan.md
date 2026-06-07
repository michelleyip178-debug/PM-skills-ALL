# POCDEX API Productionisation Plan (Pow Hwee)

**Source:** POCDEXPLUS-00 — POCDEX API Productionisation Plan (PDF, shared 2026-06-05)

**Status:** Draft

**Owner:** Pow Hwee TAN (PSD)

**Target cutover:** ~23 Jul 2026

**Effort:** ~31 working days over 9 calendar weeks

---

## Strategic Intent

1. **Escape a Closed Ecosystem** — Break away from the vendor-managed POCDEX environment (no API, low agility) by replicating data into an environment we control.
2. **Shape and Type the Data** — Restructure raw, flat data so consumers get a clean, predictable typed API.
3. **Serve Operational APIs** — Real-time operational APIs for consumers like OTEP. (Analytics/AI workloads handled by a separate UHDP segment.)

---

## Platform

`uhdp-pocdex` — reads from MSSQL replica (synced from vendor POCDEX), applies data transformation (type coercion, ref-table resolution, field pruning), serves a clean typed API to consumers.

---

## Phases

| Phase | Weeks | Key Outcomes |
|-------|-------|--------------|
| Foundation & Dev Infra | 1–3 | Repo + CI, MSSQL client, dev networking/compute applied, transform layer, sync scheduler |
| Platform Deployment | 3–5 | Dev deployment, MSSQL vs Postgres decided, STG deployed + validated |
| Validation | 5–7 | Reconciliation < 0.1%, failure mode tests, PRD infra ready |
| Cutover | 7–9 | PRD sync enabled, go/no-go, consumer switches, 7-day stabilisation |

> Note: Phases overlap — e.g., PRD infra work begins during Validation. Week ranges = bulk of work, not strict boundaries.

---

## Critical Path

| # | What | Who | Deadline |
|---|------|-----|----------|
| 1 | UHDP VPC CIDR + GitLab group | Cloud/DevOps | **6 Jun (Wk 1)** — tomorrow |
| 2 | Read replica: confirm prod instance, ownership, credentials | Vendor/DBA | 13 Jun (Wk 2) |
| 3 | TGW route: UHDP → POCDEX read replica (MSSQL 1433) | Network | 20 Jun (Wk 3) |
| 4 | Decision: stay MSSQL or transform to Postgres | Dev lead | 20 Jun (Wk 3) |
| 5 | TGW route: consumer → UHDP (HTTPS 443) | Network | 4 Jul (Wk 5) |

---

## PM Notes (added 2026-06-05)

- **OTEP dependency:** OTEP's ringfencing story (OTEP-127) and POCDEX integration epic (OTEP-271, 203, 202) consume this API. OTEP can't validate POCDEX integration without this platform live.
- **Daryll session needed:** Open-item #31 — planning session with Daryll (POCDEX team lead) before Sprint 4 planning (14 Jun). This plan makes that session more urgent: CP item #2 (read replica confirmation) is due 13 Jun, and Daryll's team owns it.
- **Timeline vs OTEP sprint alignment:** Target cutover 23 Jul = mid-Sprint 5 (28 Jun–12 Jul). OTEP ringfencing (OTEP-127) currently slated for Sprint 4. If this plan slips even one week, OTEP-127 has no API to integrate against in S4.
- **MSSQL vs Postgres decision (20 Jun)** — dev lead call, but PM should know: Postgres = cleaner long-term, MSSQL = faster short-term. Watch for the decision in the Wk 3 window; it affects the data model OTEP engineers will code against.

---

*Filed 2026-06-05. Source: Pow Hwee's PDF shared during OTEP planning.*
