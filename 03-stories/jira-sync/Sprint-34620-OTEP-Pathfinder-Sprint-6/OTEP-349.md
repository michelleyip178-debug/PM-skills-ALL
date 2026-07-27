# OTEP-349: spike: competency matching integration with OTEP-Core squad

**Status:** Done
**Assignee:** Pow Hwee TAN (PSD)
**Story Points:** 3
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

Investigate the integration work required between Pathfinder and OTEP-Core for competency matching on the opportunity detail page. Scope Identify what data OTEP-Core will provide (officer competency profile, proficiency levels) Determine API contract or integration pattern between squads Identify blockers or dependencies on officer competency data model (ref: open item #18 from Imelda squad) Output: document findings and recommend approach for Sprint 4 implementation

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-07-24)
Spike findings — competency matching integration (Pathfinder ↔ OTEP-Core). Finding: as currently built, opportunity ↔ officer competency matching returns effectively zero, and this is caused by the data model, not by data quality. Verified read-only against the otep dev DB on 24 Jul 2026. Two stacked causes: Layer 1 — key-space mismatch.  Opportunity tags are stored as competency UUIDs; officer holdings are keyed by a text competency_code (JSONB CompetencyID). Direct join = 0 overlapping pairs across all 209 opportunity requirements. Layer 2 — catalogue multiplication.  The same competency concept is stored as many family/function-specific rows, each with its own ID (e.g. "Serving with Heart..." = 95 rows; catalogue = 8,602 rows for 7,324 names). Collapsing both sides to competency name: opportunities 64 names, officers 41 names, only 2 in common. Recommended approach — separate a competency's identity from its context and proficiency:  (1) competency = one row per concept, no family/function/grade/level; (2) requirements = owner (job/role/position/opportunity) → competency_id + required_level; (3) holdings = officer → competency_id + attained_level. Matching then = intersection on the same competency_id with attained_level >= required_level. This also puts OTEP-610's agency-suffix on a sound base (owning-agency becomes an attribute, not a workaround) and enables proficiency-aware matching. No existing ticket owns this defect. OTEP-810 addresses Layer 1 only (and is empty/backlog); OTEP-610 fixes Layer 2 as display-only. A remodel + one-time migration ticket is needed; a normalised-key stopgap is possible but re-introduces label fragility. Full write-up (PM-readable, with worked example and evidence): 2026-07-24-competency-matching-never-matches-and-the-fix.md. Related: 2026-07-24-two-derivations-review-and-fix.md.

---
*Synced from Jira: 2026-07-27*
