# OTEP-374: Expose source and agency fields in listing API

**Status:** Done
**Assignee:** Léo Milbor
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

Scope: Schema + GORM models + API response only. No ingestion logic in this ticket. This ticket covers: (1) DB migration for new columns, (2) GORM model updates, (3) listing and detail API DTO changes. C@G ingestion/parsing will be a separate ticket. Context With C@G opportunities coming into OTEP alongside OTG, we need to extend the core  opportunity  table to accommodate fields that C@G provides but OTG doesn't. C@G Data Reference There is a C@G API available — Pow Hwee will look up the endpoint details and share separately. In the meantime, the OGP team maintains a community dataset that mirrors the portal's data structure, useful for understanding the field shape: Repo:  opengovsg/careersgovsg-jobs-data Sample JSON:  job-listings.json Why separate columns, not concatenation C@G provides descriptions as separate fields ( jobDescription ,  jobResponsibilities ,  jobRequirements ,  experienceYearsMin/Max ), unlike OTG which has a single  about_this_oppr  blob. We don't want to concatenate these into the existing  description  field because the AI squad will need the breakdown for embeddings, matching, and summarisation. For OTG opportunities, these new columns will be  null  for now. In a future release, we may look at structuring OTG's description similarly, but that's out of scope. New columns Column Type Purpose responsibilities text, nullable C@G  jobResponsibilities requirements text, nullable C@G  jobRequirements experience_min_years int, nullable C@G  experienceYearsMin experience_max_years int, nullable C@G  experienceYearsMax The existing  description  field continues to hold the general "about" text. Deliverables (this ticket only) DB migration adding the new columns GORM model updates ( OpportunitySummary ,  Opportunity  in  repository/models.go ) OpportunityDTO  returns the new fields in detail response Unit tests updated for the new DTO fields Not in scope:  C@G parser, C@G importer, OTG importer changes References C@G data shape:  job-listings.json OTG parser (for field comparison):  internal/service/opportunity/otg/parser.go Current listing DTO:  internal/service/opportunity/controller/get_all_handler.go Current detail DTO:  internal/service/opportunity/controller/get_handler.go Unblocks: OTEP-375 (Thomas — C@G badge on card)

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Léo Milbor** (2026-06-10)
After checking with   , for now we will only display the existing description field. Front end is  not  displaying any of the new field as of now. So in this story I will: update the db model  Opportunity not  OpportunitySummary do the migration script cc:   ,

---
*Synced from Jira: 2026-07-16*
