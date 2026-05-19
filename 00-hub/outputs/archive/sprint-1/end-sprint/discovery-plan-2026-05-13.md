# Discovery Plan: OTEP MVP Value Proposition

**Date:** 2026-05-13
**Product stage:** Existing (build in progress, Sprint 1 week 2)
**Discovery question:** Is the unified Opportunities Hub solving the right problem, scoped to the right features, and buildable within the Oct 16 window?

---

## Ideas Explored

19 ideas brainstormed across PM, Designer, and Engineer perspectives:

### PM (value + outcomes)
1. "One search, all types" as the hero moment
2. FormSG-only apply flow with tracking confirmation
3. Smart defaults over advanced filters
4. "What's new this week" digest
5. SJR "window shopping" as a teaser
6. Opportunity health signal for host agencies
7. Single-click FormSG with pre-fill

### Designer (usability + experience)
8. Card-first, not list-first
9. Type colour coding on every surface
10. "Closing soon" urgency indicator
11. Progressive detail: card -> half-sheet -> full page
12. Empty state that educates
13. SJR card without apply = clear UX treatment

### Engineer (feasibility + sustainability)
14. OTG polling with change-detection, not real-time sync
15. C@G as a scrape-and-cache, not a live integration
16. Elasticsearch from day one
17. Feature flags for opportunity types
18. FormSG webhook as a thin proxy
19. Static ringfencing by agency list

---

## Critical Assumptions (24 total, top 12 shown)

| # | Assumption | Category | Impact | Uncertainty | Priority |
|---|-----------|----------|--------|-------------|----------|
| B2 | Stakeholder direction will stabilise enough to ship | Viability | 5 | 5 | **25** |
| F1 | OTG pipeline delivers complete records by Sprint 1 end | Feasibility | 5 | 4 | **20** |
| B5 | October go-live achievable given 10 open scoping gaps | Viability | 5 | 4 | **20** |
| F2 | C@G data is obtainable without an API | Feasibility | 4 | 5 | **20** |
| V1 | Fragmentation is the real barrier, not just inconvenience | Value | 5 | 4 | **20** |
| B4 | MVP without notifications can drive adoption | Viability | 4 | 4 | **16** |
| V2 | Aggregation alone creates enough switching value | Value | 4 | 4 | **16** |
| F6 | Team capacity covers both OTG + C@G in 8 sprints | Feasibility | 5 | 3 | **15** |
| V3 | Officers care about SJRs they can't apply to | Value | 3 | 4 | **12** |
| B1 | Channel migration is the right North Star metric | Viability | 4 | 3 | **12** |
| B3 | SJR deferral doesn't undermine "unified" pitch | Viability | 3 | 4 | **12** |
| F3 | Elasticsearch provisionable by Sprint 3 | Feasibility | 4 | 3 | **12** |

### Testing clusters

- **Cluster A (Value):** V1, V2, B1 -- Is the hub solving a real problem with the right metric?
- **Cluster B (Feasibility):** F1, F2, F3, F6 -- Can we build it with what we have?
- **Cluster C (Stakeholder/timeline):** B2, B3, B5 -- Will the org hold still?

---

## Validation Experiments

### Cluster A -- Value Validation

| # | Tests | Method | Success criteria | Effort | When |
|---|-------|--------|-----------------|--------|------|
| A1 | V1 | 5 officer interviews: "Walk me through the last time you looked for a development opportunity" (don't mention OTEP) | 3+ of 5 describe multi-portal friction unprompted | Low (5 x 30 min) | May 19-23 |
| A2 | V2 | Prototype clickthrough: show Amber's Hub UI to same 5 officers, ask "Would you use this instead of going to OTG directly?" | 4+ of 5 say they'd check OTEP first if it had everything | Low (reuse Amber's designs) | May 26-29 |
| A3 | B1 | Metric audit with Pow Hwee: map the data flow from "Apply" click through FormSG to webhook. Where does OTEP attribution break? | Clear yes/no on whether channel migration is measurable | Very low (1 hour) | May 14-16 |

### Cluster B -- Feasibility Pipeline

| # | Tests | Method | Success criteria | Effort | When |
|---|-------|--------|-----------------|--------|------|
| B1 | F1 | OTG export field audit: get 10 sample records from Rama, map against card/detail requirements | All 6 unconfirmed fields resolved or escalated (no "still checking") | Low (2 hours) | By May 16 |
| B2 | F2 | C@G ingestion spike: 1-day investigation -- API, scrape, or data-sharing agreement? | One of three answers: API exists, scrape viable, or neither | 1 day (Pow Hwee) | By May 16 |
| B3 | F3 | Elasticsearch provisioning check: can OpenSearch/ES be deployed in GCC? Approval timeline? | Confirmed service + provisioning estimate fits Sprint 3 | Very low (1 inquiry) | By May 23 |
| B4 | F6 | Capacity model: map stories to engineer-days for Sprints 2-8, flag any sprint >80% loaded | No sprint >90% allocated | Low (1 hour session) | Before Sprint 2 planning (May 14) |

### Cluster C -- Stakeholder & Timeline

| # | Tests | Method | Success criteria | Effort | When |
|---|-------|--------|-----------------|--------|------|
| C1 | B2 | Scope freeze agreement: present locked MVP scope to Adrian, ask for freeze until Sprint 5 | Adrian agrees or explicitly names what's still fluid | Very low (15 min) | May 14-16 |
| C2 | B3 | Steering narrative test: draft "unified minus SJR apply" pitch, test with Jace + Adrian before steering | Both say it's defensible | Low (1 draft + 2 chats) | May 19-23 |
| C3 | B5 | Open-items burndown: plot 10 gaps on timeline, identify which slip past Sprint 4 and what cascades | Clear risk picture: "if X isn't resolved by Y, Z stories drop" | Low (1 hour) | May 14-16 |

---

## Discovery Timeline

### Week 1: May 14-16 (rest of Sprint 1)

- [ ] A3: Metric audit with Pow Hwee (1 hour)
- [ ] B1: OTG export field audit (when Rama delivers sample)
- [ ] B2: C@G ingestion spike (Pow Hwee, 1 day)
- [ ] B4: Capacity model session (1 hour, before Sprint 2 planning Thu)
- [ ] C1: Scope freeze conversation with Adrian (15 min)
- [ ] C3: Open-items burndown projection (1 hour)

### Week 2: May 19-23 (Sprint 2 week 1)

- [ ] A1: 5 officer interviews (30 min x 5, spread across week)
- [ ] B3: Elasticsearch provisioning check (1 inquiry)
- [ ] C2: Steering narrative test with Jace + Adrian

### Week 3: May 26-29 (Sprint 2 week 2)

- [ ] A2: Prototype clickthrough test (after Amber's designs land)
- [ ] Synthesis: compile findings, update assumptions, present decisions

---

## Decision Framework

| If experiment shows... | Then... |
|----------------------|---------|
| A1: Officers don't feel fragmented | Re-examine "unified hub" as the pitch. Consider pivoting to "better application experience" as the value prop |
| A2: Low intent to switch from OTG direct | Add a differentiating feature to MVP (smart defaults, pre-fill, or "what's new") to create a reason to switch |
| A3: Channel migration is unmeasurable | Switch North Star to "application starts from OTEP" or "time-to-first-apply" |
| B1: OTG export has critical gaps | Escalate to Adrian by May 19. Build "graceful degradation" plan: which cards ship with incomplete data? |
| B2: C@G has no viable data path | Defer all C@G work to R1. Rebrand MVP as "OTG Opportunities Hub" and adjust steering narrative |
| B3: Elasticsearch won't be ready by Sprint 3 | Use Postgres full-text search as interim. Migrate to ES in Sprint 5 buffer |
| B4: Capacity overloaded | Pull 1-2 stories from Sprint 3 or 4 into Sprint 5 |
| C1: Adrian won't freeze scope | Build 1-sprint buffer by proactively deferring lowest-priority Sprint 4 story |
| C2: "Unified minus SJR apply" doesn't hold at steering | Add lightweight SJR "express interest" CTA to MVP, or reframe as "discover all, apply to most" |
| C3: 3+ items slip past Sprint 4 | Trigger formal scope review with Adrian -- present burndown and ask for explicit de-scoping |

---

*Generated 2026-05-13. Review after Week 3 synthesis.*
