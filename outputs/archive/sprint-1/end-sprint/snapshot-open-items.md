# Open Items Log

> The active chase list — anything with an owner and a near-term deadline that someone needs to push on.
> Add items as they come up in ceremonies or async. Update status; mark resolved items ✅ (don't delete — keep the record).
> Read by `/daily` and `/mid-sprint-review`.
>
> **This is the action layer.** Spec-completeness analysis (what's missing from the PRD, by category, plus the R1-deferred decisions) lives in [scoping-gaps-tracker.md](../projects/otep-mvp/scoping-gaps-tracker.md). That file *links* to rows here for anything being actively chased — it doesn't copy owner/deadline. A live item has exactly one home: this one.

---

## Open items

| # | Item | Owner | Needed By | Impacts / why | Status |
|---|---|---|---|---|---|
| 2 | Confirm `formsg_url` field name and structure | Rama + PSD Ops | Before Sprint 2 | STIP/Gig apply flow | 🔴 Open |
| 8 | Agency contact field name for OTEP-133 fallback | Rama | Before Sprint 3 | Email deep-link fallback state | 🔴 Open |
| 14 | Does FormSG support pre-fill via URL params? | Pow Hwee | Before Sprint 3 | Determines whether US-P3 is MVP or R1 | 🔴 Open |
| 15 | Email/notification service — existing platform service or new build? | Pow Hwee | Before Sprint 3 | US-10 submission email, OTEP-133 deep-link email — scopes notification work for MVP | 🔴 Open |
| 16 | Search indexing infrastructure — provisioning + refresh strategy | Pow Hwee | Before Sprint 3 | OTEP-86 assumes elastic matching; needs a story or spike | 🔴 Open |
| 18 | Officer competency data model — where does opportunity competency data come from? In OTG export? | Pow Hwee | Before Sprint 3 | US-P2, opportunity detail pages | 🔴 Open |
| 20 | SJR card UX when no apply action exists — no button, "Coming soon" indicator, or hide SJRs from listing? | Amber | Before Sprint 3 (US-18 build) | SJRs appear in OTG listing but have no apply flow in MVP (decision 2026-05-13). Card needs a clear treatment so officers aren't confused by a missing action. | 🟡 Design finalised 2026-05-13 — confirm treatment at grooming |
| 19 | Is a competency page in OTEP MVP scope? PM Weekly (11 May) said it must be in formal design reviews + sprints; Imelda drafts the template, Adrian gets it into reviews — but it's not in the MVP guardrails as a build item | Adrian / Michelle | Before it lands in a sprint | Could expand MVP scope; ties to #18 | 🔴 Open |
| 9 | Search UX approach — typeahead vs submit | Amber | Design review | OTEP-86 search interaction | 🟡 In discussion |
| 21 | Set up Confluence/Jira view for async BO visibility on sprint goals and key tickets | Michelle | Sprint 2 start | BO involvement working agreement (2026-05-11) — BOs need async visibility without attending grooming | 🔴 Open |
| 22 | Set a design lock date for Sprint 2 — no major design changes after that point | Michelle / Amber | Sprint 2 W1 | Prevents mid-sprint design churn. Screenshots + behavior notes to be attached to Jira. Agreed at internal groom 2026-05-13. | 🔴 Open |
| 23 | Harmonised data model: confirm it supports both OTG (now) and C@G (later) before finalising OTEP-193 | Pow Hwee | Before Sprint 2 dev | Data model must be extensible. Agreed at internal groom 2026-05-13. | 🔴 Open |
| 24 | Specify which OTG reports to ingest (STIPs & Gigs, SJR, audience filters, etc.) for OTEP-192 | Michelle / Pow Hwee | Before Sprint 2 dev | Ingestion story needs to name the exact Excel reports and fields. Agreed at internal groom 2026-05-13. | 🔴 Open |
| 25 | Profile story split: identify which parts are feasible for Sprint 2 (basic: name, email) vs deferred (competency — depends on another team) | Michelle / Pow Hwee | Sprint 2 planning (Thu 14 May) | Large profile story too big as-is. Only basic auth profile goes into Sprint 2. | 🔴 Open |
| 26 | Define expected auth test outcome without AzureAD access — team has an alternative tool for testing but expected outcomes need to be explicit | Pow Hwee / Leo | Sprint 2 start | Auth stories (OTEP-71a–d, OTEP-111) can't be finalised without agreement on what "done" looks like in a non-AzureAD test env. Source: Thomas (Slack, 14 May). | 🔴 Open |
| 27 | **OTEP-271** (local POCDEX DB + seed 5 profiles) — confirm sprint placement: Sprint 2 carry-over vs backlog? Split from **OTEP-202** (Leo): OTEP-271 = infra setup; OTEP-202 = seed data only (Pow Hwee, Sprint 1). Parent OTEP-99. | Michelle / Pow Hwee | Sprint 2 start | Sequences POCDEX vs seed work; affects capacity and OTEP-192/193 dependencies | 🔴 Open |

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

---

*New items: append the next number (don't renumber — `risks.md` and `scoping-gaps-tracker.md` reference these by #). Last updated: 2026-05-15 (audit cleanup — moved 9 resolved items out of Open table).*
