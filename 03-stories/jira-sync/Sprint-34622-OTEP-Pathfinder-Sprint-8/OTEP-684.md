# OTEP-684: Refactor ingestion model (split otg /cag importer.SourceRecord)

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 8 (34622)

---

## Description

Opportunity Sync Architecture: Final State & Refactoring Plan Final State Overview The "God Object" importer is dismantled into highly cohesive, domain-driven packages. We achieve a strict separation between pure computation (domain), data translation (edges), and database orchestration (use case). 1. Core Domain ( domain  package) Responsibility:  Pure business logic and normalized validation guarantees. Components: Opportunity  struct: Handles its own structural, intrinsic validation (e.g., missing titles). OpportunityValidator  (Domain Service): Orchestrates contextual validation (e.g., verifying an Agency ID exists) by consuming a  ReferenceChecker  interface. Rule:  Zero IO. Zero knowledge of Excel, JSON, or database transactions. 2. The Shared Cache ( refdata  package) Responsibility:  Fast, in-memory reference data lookups to satisfy both edge hydration and domain validation. Components: RefCache : Populated once on startup. Exposes explicit  ByID ,  ByCode , and  ByLabel  methods. Rule:  Replaces the functional options ( WithResolveBy... ) to provide unambiguous  O(1)  lookups. 3. The Translators ( otg  &  careersatgov  packages) Responsibility:  Read external data, hydrate references, and manage source-specific audit trails. Components: Parsers for their specific formats (Excel/SAP JSON). Hydration logic (translating a label like "GovTech" into a populated  domain.Agency  via the  RefCache ). Source-specific business rules (e.g., "OTG Gigs require time commitments"). GORM models for their specific audit tables ( SourceOTGOpportunity , etc.). Implementations of the  AuditSaver  interface. Rule:  They output a standardized batch of  ImportRecord s ready for the orchestrator. 4. The Orchestrator ( oppsync  package) Responsibility:  The vertical slice for saving batches of opportunities atomically. Components: ImportRecord  DTO (holds the domain object, raw payload, warnings, and errors). AuditSaver  interface (consumer-defined, implemented by  otg  /  cag ). Syncer : Takes the  ImportRecord  batch, runs the  OpportunityValidator , and executes the atomic GORM transaction (saving core records, relations, and audit logs). Rule:  Agnostic to data origin. Focuses entirely on performant, transactional database writes. 5. Core Persistence ( repository  package) Responsibility:  Dumb data access for the core domain. Components: Core GORM models ( Opportunity ,  OpportunitySummary ). Standard CRUD operations ( Get ,  GetAll ). Rule:  Stripped of the complex generic  sourceOpportunityModel[T]  constraints.  Step-by-Step Refactoring Plan Step 1: Secure the Domain (Validation) Start from the center. Move the validation rules into the  domain  package to establish the normalized guarantee. Add a parameterless  Validate()  method to  domain.Opportunity  for intrinsic structural checks. Create  OpportunityValidator  (Domain Service) in  domain/service.go . Define the  ReferenceChecker  interface here for contextual validation (verifying IDs). Step 2: Unify the Reference Cache Clean up the reference resolution so it can serve both the edges and the domain. Move away from the  WithResolveBy...  options. Create a unified  RefCache  that builds  byID ,  byCode , and  byLabel  maps on startup. Expose explicit methods ( AgencyByID ,  AgencyByLabel , etc.). Step 3: Scaffold the Orchestrator ( oppsync ) Extract the atomic transaction logic from the generic repository. Create the  oppsync  package. Define the  ImportRecord  DTO and the  AuditSaver  interface. Move the transaction, batch upsert, and relations-syncing logic from  repository/syncer.go  into  oppsync.Syncer . Step 4: Push Translators to the Edges ( otg  &  cag ) Dismantle the generic  importer  package. Move parsing and hydration logic directly into  otg  and  cag . Move the audit GORM models ( SourceOTGOpportunity , etc.) out of  repository  and into their respective source packages. Have  otg  and  cag  implement the  AuditSaver  interface to save to their specific tables. Update their entry points to produce  []oppsync.ImportRecord  and hand them to  oppsync.Syncer . Step 5: Clean Up Delete the  importer  package. Delete  repository/syncer.go  and the generic constraint interfaces. Update tests to match the new boundaries.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-11*
