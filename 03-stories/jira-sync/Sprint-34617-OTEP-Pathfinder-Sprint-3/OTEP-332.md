# OTEP-332: feat: implement shared reference data repository for cross-domain table lookups

**Status:** Done
**Assignee:** Pow Hwee TAN (PSD)
**Story Points:** N/A

---

## Description

Context Reference tables (ref_agency, ref_employment_type, etc.) have been created with schema migrations and seed data, but there is no Go repository layer to query them. Both squads need to resolve FK references against these tables. This is currently blocking MR !44 (OTEP-118: Resolve Identity + Get User Profile) where GetAgencyRefByAgencyID panics with 'implement me'. Scope Create internal/shared/refdata/ package with GORM models and read-only repository methods (GetByID, GetByCode, ListAll) for: ref_agency, ref_employment_type Wire repository into service bootstrap (service.go) so domain constructors can accept it as a dependency Include ingestion path: ref table data sourced from POCDEX flows through this package Out of Scope ref_competency lookups — owned by Kingsley's competency domain, to avoid confusion and duplication Acceptance Criteria Profile domain (Squad 1) can call refdata.GetAgencyByID() to resolve agency references Opportunity domain (Squad 2) can call the same repository for opportunity detail display Unblocks MR !44 (GetAgencyRefByAgencyID panic)

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-06-10)
This issue was already completed and merged into main. See merge commit: ffaa60d Merge branch 'feat/OTEP-332-shared-refdata-repository' into 'main'.

---

**Rathika Ramalingam** (2026-06-10)
Testing in LOCAL:
