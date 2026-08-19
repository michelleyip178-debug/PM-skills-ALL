# OTEP-581: Update Agency Seed

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Replace the  ref_agency  seed so the canonical agency reference data is the  126-agency acronym list  (from the attached  Agency.csv ), instead of the previous 126 POCDEX full-name "ORGANISATION" agencies. The acronym set is what the application and the  job / competency  data actually reference, so the old full-name seed was effectively duplicate/divergent data. Background ref_agency  is seeded by  internal/shared/database/seeds/002_ref_agency.sql  (the only  INSERT INTO ref_agency  in the repo). The local DB had  249  rows — 126 official full-name agencies (from the old seed)  plus  ~125 legacy acronym rows (UUID codes) that no seed produced. Reference tables were split:  employment / opportunity  pointed at the official set, while  job  (49k rows) and  competency  referenced the acronyms. The canonical, app-aligned set is the acronym list. What changed Seed ( 002_ref_agency.sql ): Now seeds the  126 canonical agencies  from  Agency.csv , with  code = label = agency  (e.g.  MHA- SPF ),  is_active = true ,  status = active ,  display_order  = row order. Keeps the existing  upsert-by- code  ( ON CONFLICT (code) DO UPDATE ). A fresh DB now seeds exactly these 126. parent_agency  from the CSV is  not  stored (the table has no parent column; deferred). Local DB reconciliation (one-off, not shipped as a migration): Remapped  hard (FK) references  off the 123 non-canonical agencies onto the matching canonical agency —  employment  5,  job  133,  opportunity  45 — using an explicit official→acronym mapping (e.g.  Ministry of Finance → MOF ,  Public Service Division → PSD ; placeholders  ALL / DNU  →  ZZZ ). Deleted  role_relation  placeholder rows ( ALL / DNU , 15) — they'd collide on  uq_role_relation  if remapped. Deleted the  123  non-canonical agencies; normalised survivor  code = label . Run as a  single transaction with assertions  (exactly 126 agencies, 0 dangling references), and verified the 5 demo accounts kept their agency (thomas→PSD, rama→MOF, peiern→MOH, rathika→MCCY, powhwee→MOE). Acceptance criteria 002_ref_agency.sql  seeds exactly the 126 agencies from  Agency.csv  (code = label = agency). Seed is idempotent (upsert-by-code; re-run is a no-op). A fresh DB (migrate + seed) yields  only  the 126 canonical agencies. No FK reference points at an agency outside the canonical set.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
