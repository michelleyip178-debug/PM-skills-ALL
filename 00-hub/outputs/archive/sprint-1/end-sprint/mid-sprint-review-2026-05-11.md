# Mid-Sprint Review — 11 May 2026 | Sprint 1, Week 2

## Sprint Health

**Status:** 🟡 At risk
**Sprint goal:** Login and navigate to Jobs and Opportunities
**Stories:** 0 completed / 2 committed (OTEP-85 in progress, OTEP-89 not started)
**Days remaining:** 4 (sprint ends Fri 15 May)

**Why 🟡:** We're halfway through with zero stories completed. OTEP-89 (Opportunity type label) hasn't started. The real Sprint 1 deliverables — WOGAD auth, POCDEX account creation, data pipeline decisions — are tracked in active.md but not reflected as committed stories in the sprint tracker. That means we have no shared visibility on whether the core infrastructure work is on track. The team may be further along than the tracker shows, but we don't know, and that's the problem.

**Context file gap:** `current-sprint.md` still has placeholder text for the sprint goal and lists OTEP-85/OTEP-89 as the only committed stories. The sprint calendar says Sprint 1 ships "Auth via Keycloak, base listing page layout, data model designed, POCDEX/FormSG patterns explored." These don't match. Update the file after today's review.

---

## Blockers to Raise in the Session

| Blocker | Story / deliverable affected | Owner | Since | Action needed |
|---|---|---|---|---|
| COMET onboarding status unknown | WOGAD auth (Azure AD prerequisite) | Imelda | May 7 (follow-up overdue since May 9) | Chase today — if ESG isn't onboarded, auth integration is blocked |
| WOGAD integration — no status update | Core Sprint 1 deliverable | Pow Hwee / Leo / Thomas | May 4 | Ask for concrete status: what's done, what's left, is it on track for Friday? |
| POCDEX account creation (OTEP-72) | Push mechanism validation | Engineering | May 4 | Confirm whether push mechanism works — this was a Sprint 1 target |
| C@G ingestion method unresolved | Blocks Sprint 2 data availability | Pow Hwee | May 4 | Need a decision (API vs file export vs scrape) this week or Sprint 2 starts without data |
| 6 unconfirmed OTG fields | Sprint 2 grooming readiness | Rama | Sprint start | All 6 needed before Thursday's grooming — raise today, escalate if no path to resolution by Wed |

---

## Scope Creep Flags

None identified. Five scope decisions were logged on May 8 (binary competency, no Save for Later, supervisor endorsement UI-only, FormSG/OTG apply split, search in MVP). All are holding. No evidence of informal additions.

---

## PM Decisions Needed Before Sprint End

| Decision | What Michelle needs to do | By when |
|---|---|---|
| Secondment type classification | Follow up with Business Owner — is Secondment a distinct type or sub-type of SJR? Impacts US-03 filter logic for Sprint 2 | May 12 (tomorrow) |
| Competency match ratio descope | Prepare recommendation for Adrian/Jace to descope US-05 to R1 — show tags only for MVP | Before Thu grooming (May 14) |
| Sprint 2 gap stories | Write OTG→OTEP pipeline and C@G→OTEP ingestion stories — Sprint 2 backlog needs them for Thursday | Before Thu grooming (May 14) |
| Hub UI design review | Review Amber's designs against OTEP-85/OTEP-128 ACs once delivered | When ready (waiting since May 4) |

---

## Open Items Scorecard

8 open items. 1 in discussion. 1 resolved. Most are OTG field confirmations owned by Rama, needed by next grooming.

| Status | Count |
|---|---|
| 🔴 Open | 8 |
| 🟡 In discussion | 1 (Search UX: typeahead vs submit) |
| ✅ Resolved | 1 (Search confirmed MVP) |

The ratio is concerning — 8 open items with grooming in 3 days. If these can't be resolved, the grooming session will stall on unknowns.

---

## Michelle's Key Question for the Session

> "Can we demo WOGAD login by Friday, or are we going to carry auth into Sprint 2?"

This is the sharpest question because it forces a binary answer on the sprint's most important deliverable. If auth slips, the entire Sprint 2 plan (which assumes auth is done) needs to be re-sequenced. Better to know now than Thursday.

---

## After the Session

1. Update `context/current-sprint.md` with actual committed stories and real sprint goal
2. Log any decisions made in `../../../../../../PM-OS/outputs/decisions/2026-05-29-W22-decisions-log.md`
3. Update `context/open-items.md` with any items that got resolved or re-assigned
4. Run `/archive` to checkpoint the mid-sprint state
