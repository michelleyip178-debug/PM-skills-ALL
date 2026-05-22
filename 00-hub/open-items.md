# Open Items Log

> The active chase list — anything with an owner and a near-term deadline that someone needs to push on.
> Add items as they come up in ceremonies or async. Update status; mark resolved items ✅ (don't delete — keep the record).
> Read by `/daily` and `/mid-sprint-review`.
>
> **This is the action layer.** Spec-completeness analysis (what's missing from the PRD, by category, plus the R1-deferred decisions) lives in [scoping-gaps-tracker.md](../03-stories/scoping-gaps-tracker.md). That file *links* to rows here for anything being actively chased — it doesn't copy owner/deadline. A live item has exactly one home: this one.

---

## Open items

| # | Item | Owner | Needed By | Impacts / why | Status |
|---|---|---|---|---|---|
| 8 | Agency contact field name for OTEP-133 fallback | Rama | Before Sprint 3 | Email deep-link fallback state | 🔴 Open |
| 14 | Does FormSG support pre-fill via URL params? | Pow Hwee | Before Sprint 3 | Determines whether US-P3 is MVP or R1 | 🔴 Open |
| 15 | Email/notification service — existing platform service or new build? | Pow Hwee | Before Sprint 3 | US-10 submission email, OTEP-133 deep-link email — scopes notification work for MVP | 🔴 Open |
| 16 | Search indexing infrastructure — provisioning + refresh strategy | Pow Hwee | Before Sprint 3 | OTEP-86 assumes elastic matching; needs a story or spike | 🔴 Open |
| 18 | Officer competency data model — source confirmed 2026-05-21: Imelda's squad owns master source of truth for job family, job function, agency, and competencies. Open questions: (1) How does OTEP consume this data — API? file sync? push? (2) Schema + field names? (3) Availability timeline — when can OTEP integrate? (4) **New (grooming 2026-05-21):** OTG opportunities carry competency tags — how do these map to the OTEP competency bank? Backend mapping required before ingestion can be considered clean and before OTEP-87 competency section can be built. **(5) New (2026-05-22):** Confirm reference data schema and availability timeline — OTEP-87 competency section and OTG ingestion correctness both blocked until Imelda's squad confirms method + schema. Add to next Imelda sync agenda. | Michelle → Imelda | Before Sprint 4 planning | Competency section of OTEP-87 (deferred), WOG-10 (agency resolution), any future competency features. Competency mapping (OTG tags → bank) also blocks complete ingestion correctness. | 🟡 Source confirmed — method, schema, timeline, and OTG mapping all TBC |
| 19 | Is a competency page in OTEP MVP scope? PM Weekly (11 May) said it must be in formal design reviews + sprints; Imelda drafts the template, Adrian gets it into reviews — but it's not in the MVP guardrails as a build item | Adrian / Michelle | Before it lands in a sprint | Could expand MVP scope; ties to #18 | 🔴 Open |
| 9 | Search UX approach — typeahead vs submit | Amber | Design review | OTEP-86 search interaction | 🟡 In discussion |
| 21 | Set up Confluence/Jira view for async BO visibility on sprint goals and key tickets | Adrian / Barry | Sprint 2 start | BO involvement working agreement (2026-05-11) — BOs need async visibility without attending grooming | 🔴 Open |
| 23 | Harmonised data model: confirm it supports both OTG (now) and C@G (later) before finalising OTEP-193 | Pow Hwee | Before Sprint 2 dev | Data model must be extensible. Agreed at internal groom 2026-05-13. | 🔴 Open |
| 25 | Profile story split: identify which parts are feasible for Sprint 2 (basic: name, email) vs deferred (competency — depends on another team) | Pow Hwee | Sprint 2 planning (Thu 14 May) | Large profile story too big as-is. Only basic auth profile goes into Sprint 2. | 🔴 Open |
| 26 | WOG AD onboarding — intranet URL `careercompass.gov.sg` submitted to unblock 2-4 week approval clock (Decision 2026-05-22). Single URL (internet + intranet) policy investigation continues separately. Next step: Work out steps with Fabian and Pow Hwee. | Michelle → Fabian / Pow Hwee | Before auth is rescheduled (currently Sprint 4+) | Gates WOG AD auth (OTEP-71/110/304/305) AND CSC SSO (#30). 6-week total chain (2-4 wks WOG AD + 4 wks CSC) — every day delayed pushes both. | 🟡 Intranet URL submitted; pending next steps with Fabian/Pow Hwee |
| 30 | CSC SSO — confirmed by Imelda (OTEP-Core Squad PM) 2026-05-21. Sequential after WOG AD (#26): WOG AD must complete before documents passed to CSC. CSC needs 4 weeks. Michelle owns end-to-end. Imelda = context source (process, test data, #18). | Michelle | Before Sprint 5 (~2 Jul best case) | WOG AD (#26) must close first. 6-week total SSO chain from WOG AD kickoff. | 🔴 Open |
| 31 | POCDEX go-live prep — first project using POCDEX API; support structure not settled. Need planning session with Daryll (POCDEX team lead). OTEP-202 (seed database) has no sprint assigned — needed before Sprint 4 ringfencing (OTEP-127). **New (2026-05-22):** Imelda's squad also depends on POCDEX (Epic 1 officer profile, Epic 2 competency personalisation, Epic 3 course recommendations). Both squads competing for Daryll's team. Make clear in the planning session which squad's use cases have priority and whether Daryll's team can support both simultaneously. | Michelle | Before Sprint 4 planning | POCDEX plumbing (Sprint 3: OTEP-271/203) can't be validated without Daryll's team. Ringfencing (OTEP-127) blocked without seed data (OTEP-202). If POCDEX is deprioritised toward Imelda's squad, Sprint 4 ringfencing slips. | 🔴 Open |
| 32 | OTEP-110 Jira ACs and design spec mismatch | Michelle | Before Sprint 4 | Conflicting requirements block implementation | 🔴 Open |

---

## Resolved items

| # | Item | Resolved by | Date |
|---|---|---|---|
| 10 | Search (OTEP-130) confirmed MVP | Michelle | 2026-05-08 |
| 13 | Target launch date = Go-Live Fri 16 Oct 2026 (per Sprint Ceremonies v2) | Michelle / Adrian | 2026-05-12 |
| 1 | `eligibility` field not needed | Rama | 2026-05-13 |
| 3 | `closing_date` confirmed as application closing date | Rama | 2026-05-13 |
| 4 | `is_published` does not exist — use `closing_date` for visibility | Rama | 2026-05-13 |
| 5 | `reporting_line` not available in OTG export | Rama | 2026-05-13 |
| 6 | `developmental_outcome` will be available in OTG export | Rama | 2026-05-13 |
| 7 | `otg_url` (SJR redirect) no longer needed — SJR apply deferred | PSD Ops | 2026-05-13 |
| 12 | Secondment subsumed under SJR (not a distinct type) | Jacky (BO) | 2026-05-13 |
| 17 | Opportunity lifecycle = date-driven (`closing_date > today`) | Michelle / Pow Hwee | 2026-05-13 |
| 11 | C@G ingestion = API; OTG ingestion = file import (Excel) | Michelle | 2026-05-14 |
| 24 | OTG Excel reports shared with Pow Hwee — reports specified for OTEP-192 ingestion | Michelle | 2026-05-18 |
| 2 | `formsg_url` confirmed in OTG Export — field present for Internal Jobs, STIPs, Gigs. SJRs excluded (no apply flow in MVP — decision 2026-05-13). Unblocks US-18. | Rama + PSD Ops | 2026-05-21 |
| 28 | OTEP-85 visibility rule: clean split confirmed — OTEP-85 shows all `closing_date > today`; OTEP-129 owns "Closing soon" badge (within 7 days) | Michelle | 2026-05-19 |
| 29 | OTEP-289 spike defined: 2-day timebox (19–20 May), ACs cover C@G + OTG taxonomy mapping, output = written recommendation + go/no-go. Cut-line: defer to Sprint 3 if mapping is messy. | Michelle | 2026-05-19 |
| 27 | OTEP-271/202/203 (POCDEX stories) sprint placement confirmed — staggered backend DB container & standalone service setup to Sprint 3 to avoid Sprint 4 bottleneck | Michelle / Pow Hwee | 2026-05-20 |
| 20 | SJR card UX when no apply action exists — resolved by excluding SJRs from MVP ingestion entirely (decision 2026-05-21). No card, no UX question. | Grooming 2026-05-21 | 2026-05-21 |
| 22 | Set a design lock date for Sprint 2 — locked to 2026-05-22 | Michelle / Amber | 2026-05-22 |

---

*New items: append the next number (don't renumber — `risks.md` and `scoping-gaps-tracker.md` reference these by #). Last updated: 2026-05-22 (#18 updated with reference data schema agenda item; #31 updated with Imelda squad cross-dependency on POCDEX; #32 added).*
