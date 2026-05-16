# Projects

Time-bound work with deliverables. Each project gets its own folder.

**Last updated:** 2026-05-11

---

## Active Projects

| Project | Owner | Status | Folder |
|---------|-------|--------|--------|
| OTEP MVP (Auth + Opportunities) | Michelle | In Progress — Sprint 1 | `otep-mvp/` |
| OTG Ops | Michelle | Ongoing (BAU) | `otg-ops/` |
| BA-to-PM Conversion | Michelle | In Progress — evidence gathering | `pm-conversion/` |

## Sprint Plan

See [sprint-allocation.md](sprint-allocation.md) for the full sprint-to-story mapping.

See [otep-mvp-release.md](../resources/otep-mvp-release.md) for the dependency map, scope concerns, and detailed sprint breakdown.

**Story ID reconciliation:** [story-id-map.md](otep-mvp/story-id-map.md) — PRD IDs vs Jira/one-pager IDs.

## Folder Structure

```
projects/
├── README.md                 <- You are here
├── sprint-allocation.md      <- Sprint-to-story mapping (cross-epic)
├── otep-mvp/                 <- Merged: Auth (Epic 5) + Opportunities (Epic 4)
│   ├── prd-opportunities.md  <- Epic 4 PRD
│   ├── prd-auth.md           <- Epic 5 PRD
│   ├── brief-opportunities.md
│   ├── brief-auth.md
│   ├── scoping-gaps-tracker.md
│   ├── story-id-map.md       <- PRD ↔ Jira ID reconciliation
│   ├── stories/
│   │   ├── index.md          <- Story index (all groups)
│   │   ├── auth.md           <- WOG AD stories (7)
│   │   ├── filters.md        <- Discovery & filter stories (7)
│   │   ├── otg-lifecycle.md  <- OTG apply flow (3)
│   │   ├── cag-handoff.md    <- C@G deep-link handoff (3)
│   │   ├── tracking.md       <- Application tracking (4)
│   │   ├── profile-dependency.md  <- Profile stories (3)
│   │   └── grooming/         <- Auth grooming prep tasks
│   └── research/
│       ├── categorisation-research.md
│       └── hallway-test-filters.md
├── otg-ops/                  <- BAU: OTG platform maintenance + ops
│   ├── brief.md
│   └── task-log.md           <- Running log of BAU requests
└── pm-conversion/            <- BA-to-PM: evidence tracker + one-pager
    ├── brief.md
    ├── evidence-tracker.md
    └── one-pager.md
```

## Also in resources/

- `resources/otep-vision-stories/` — 43 product-level user stories (Officer, HR, Supervisor, Owner, JTBDs) spanning the full OTEP roadmap. Reference material, not sprint deliverables.
- `resources/otep-mvp-release.md` — dependency map, sprint breakdown, scope concerns.

## Conventions

- One folder per project
- Stories are working drafts here — Confluence is the source of truth once groomed
- Decisions are logged in `context/decisions-log.md` (not in project folders)
- Tag each story with: MVP / R1 priority and DoR status
