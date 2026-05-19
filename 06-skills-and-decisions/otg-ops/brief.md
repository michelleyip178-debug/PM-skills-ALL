# OTG Ops — Project Brief

**Owner:** Michelle Yip
**Type:** BAU (ongoing, no end date)
**Platform:** OTG (One Talent Gateway) — the existing talent mobility platform that OTEP will eventually replace for discovery/apply flows

---

## What This Covers

Ongoing maintenance, bug fixes, user support, and operational tasks for the live OTG platform. This is the "keep the lights on" work that runs alongside OTEP MVP development.

## Why It Matters

OTG is the production system officers and agencies use today. Until OTEP ships and migrates users (target: Sep 2026), OTG must stay operational and reliable. Issues here also surface data quality and integration problems that directly affect OTEP's data pipeline.

## Key Responsibilities

- Triage and resolve platform bugs reported by agencies or officers
- Coordinate operational requests (user access reviews, account issues, data corrections)
- Support data exports and field confirmations (feeds into OTEP data pipeline work)
- Liaise with Rama and PSD Ops on OTG-side changes that affect OTEP
- Escalate infrastructure or security issues to Pow Hwee / Infra

## Key Contacts

| Person | Role | When to engage |
|--------|------|---------------|
| Rama | OTG data owner | Field mappings, export schema, data quality issues |
| PSD Ops | Operational support | User access, account reviews, FormSG link issues |
| Pow Hwee | Tech Lead | Infrastructure, integration, escalations |
| Jacky / Xian Zhang | Business owners | Scope decisions, priority calls on BAU vs new work |

## Relationship to OTEP

OTG Ops and OTEP MVP share dependencies:
- OTG → OTEP data pipeline (Sprint 1 deliverable) depends on OTG export schema staying stable
- 6 unconfirmed OTG fields (`eligibility`, `formsg_url`, `closing_date`, `is_published`, `reporting_line`, `developmental_outcome`) are tracked in `context/open-items.md` items #1–6
- Any OTG schema changes during OTEP build could break the pipeline — flag immediately

## Scope Boundaries

**In scope:** Platform bugs, user support, data ops, access reviews, operational requests
**Out of scope:** New OTG features (OTG is in maintenance mode), OTEP development work (separate project)

---

*Created: 2026-05-11*
