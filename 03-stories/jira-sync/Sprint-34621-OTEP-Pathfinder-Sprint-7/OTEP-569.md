# OTEP-569: Events

**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 7 (34621)

---

## Description

As a product/data analyst, I want each authenticated officer's opportunity engagement (what they view, what they apply to, how they found it, and whether they're a returning applicant or a first-timer) tracked in PostHog with event properties and person-level aggregates, so I can segment opportunity behaviour by type, source, and discovery method — and measure  OKR 2  (~1,850 officers applied via CareerCompass) without joining to an external data source. Background / Context Opportunity events fire client-side on the listing and detail pages. The officer is already identified ( distinct_id  =  profileId ) via OTEP-488 — this story attaches opportunity-specific properties to their events and person record. User-level aggregates (viewed/applied counts, timestamps) are written via  $set  on each event so OKR dashboard queries run without aggregation. Event-level properties (type, source, agency, match source, application method) support funnel and discovery analysis. is_ringfenced  ships as  false  for all events in v1; it will populate correctly once the ingestion pipeline joins  RAW_GIG_AUDIENCE_FILTERS  (OTEP-127 dependency). User properties (person traits — opportunity aggregates) Property Source / rule $set v1 value opportunities_viewed_count incremented on each  opportunity_viewed  event ✓ 0 until first view opportunities_applied_count incremented on each  opportunity_applied  event ✓ 0 until first apply last_opportunity_viewed_at timestamp of most recent  opportunity_viewed ✓ null  until first view last_opportunity_applied_at timestamp of most recent  opportunity_applied ✓ null  until first apply first_opportunity_applied_at timestamp of first  opportunity_applied ;  never overwritten ✓ null  until first apply opportunity_types_applied array of distinct types applied to ( STIP  /  Gig  /  SJR  /  Job  /  C@G ) ✓ [] until first apply Event properties (on every opportunity event) Property Values Events opportunity_id string — joins to OTG source record all opportunity_type enum:  STIP  /  Gig  /  SJR  /  Job  /  C@G all opportunity_source enum:  OTG  /  CareersAtGov all opportunity_agency string — agency code of posting agency all is_ringfenced bool all match_source enum:  search  /  filter  /  browse  /  recommendation opportunity_viewed application_method enum:  FormSG  /  OTG-redirect  /  native opportunity_applied Acceptance Criteria Opportunity events — core When an officer opens an opportunity detail page, an  opportunity_viewed  event is captured with  opportunity_id ,  opportunity_type ,  opportunity_source , and  opportunity_agency . When an officer submits an application, an  opportunity_applied  event is captured with the same core properties plus  application_method . match_source  is included on  opportunity_viewed  events to record how the officer found the opportunity. is_ringfenced  (bool) is included on all opportunity events —  true  if the opportunity has an audience filter set,  false  if open to all. User-level aggregates opportunities_viewed_count  is incremented via  $set  on each  opportunity_viewed  event. opportunities_applied_count  is incremented via  $set  on each  opportunity_applied  event. last_opportunity_viewed_at  is updated to the event timestamp on each  opportunity_viewed  event. last_opportunity_applied_at  is updated to the event timestamp on each  opportunity_applied  event. first_opportunity_applied_at  is set once on the officer's  first   opportunity_applied  event and  never overwritten . opportunity_types_applied  is a real array (not stringified) accumulating distinct types the officer has applied to. Privacy No NRIC, name, or email  is sent. Only  opportunity_id  and  opportunity_agency  (agency code only) — no officer PII. Out of Scope (v1) application_method: native  — not applicable until R1 native apply is built. Dependencies OTEP-488  — officer identity in PostHog ( distinct_id  =  profileId  must be set before opportunity events fire) OTEP-127  — ringfencing ingestion pipeline (gates  is_ringfenced = true ) Definition of Done AC 1–11 met Verified in PostHog:  opportunity_viewed  and  opportunity_applied  events visible with correct properties; person aggregates updating correctly after each event Privacy check: no PII in event or person properties

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-05*
