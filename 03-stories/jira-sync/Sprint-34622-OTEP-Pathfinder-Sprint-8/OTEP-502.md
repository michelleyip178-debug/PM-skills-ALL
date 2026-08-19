# OTEP-502: Track opportunity engagement events and person aggregates in PostHog

**Status:** In Progress
**Assignee:** Thomas Huchedé
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 8 (34622)

---

## Description

Instrument the opportunities journey in PostHog as an  event-first funnel  ( search / filter  →  impression  →  click  →  viewed  →  applied ) so the product/data analyst can measure discovery → interest → conversion, and report  OKR 2  ("~1,850 officers applied via CareerCompass")  without joining an external data source . Why The original story proposed denormalized person-property  counters  ( opportunities_viewed_count , etc.). Those (a) duplicate PostHog's native event aggregation and (b)  can't be maintained client-side  — the SDK runs flags-disabled (OTEP-488; the deployment blocks  /flags ), so it can't read a current person value to increment, and PostHog has no atomic increment operator. After PM discussion the model is  event-first : counts/CTR/conversion are derived from events; only cheap timestamp person-properties are  $set . Scope — 6 events Typed catalog in  src/lib/analytics/events.ts  (camelCase args → snake_case PostHog props). Event Fires when Transport opportunity_search a search is run on the listing (incl. zero-result) XHR opportunity_filter_applied a non-default filter (type/sort) is applied XHR opportunity_impression a card scrolls into view (deduped once per card per listing view) XHR opportunity_click a card is clicked sendBeacon  (survives navigation) opportunity_viewed the detail page mounts XHR opportunity_applied Apply is clicked XHR Opportunity core  (on  impression / click / viewed / applied ):  opportunity_id ,  opportunity_title ,  opportunity_type ,  opportunity_source ,  opportunity_agency ,  is_ringfenced . opportunity_title  is  denormalized for readability  — point-in-time;  opportunity_id  is the join key. Person properties  (timestamps only,  $set / $set_once  inside the event  properties ):  last_opportunity_viewed_at ,  last_opportunity_applied_at ,  first_opportunity_applied_at . Enums opportunity_type  ∈  STIP | Gig | SJR | Job | C@G opportunity_source  ∈  OTG | CareersAtGov match_source  ∈  search | filter | browse | recommendation  ( recommendation  deferred — no rec surface yet) application_method  ∈  FormSG | OTG-redirect | native is_ringfenced  boolean —  false  in v1 (OTEP-127 dep)  Example payloads opportunity_search {
  "event": "opportunity_search",
  "properties": {
    "search_term": "data engineer",
    "results_count": 12
  }
}  opportunity_filter_applied {
  "event": "opportunity_filter_applied",
  "properties": {
    "opportunity_types": [
      "stip",
      "gig"
    ],
    "sort_by": "closing_date",
    "results_count": 5
  }
} sort_by  is  null  when no sort is selected.  opportunity_impression {
  "event": "opportunity_impression",
  "properties": {
    "opportunity_id": "opp-8a1f",
    "opportunity_title": "Data Engineer (STIP)",
    "opportunity_type": "STIP",
    "opportunity_source": "OTG",
    "opportunity_agency": "psd",
    "is_ringfenced": false,
    "match_source": "search",
    "list_position": 2,
    "page": 1
  }
}  opportunity_click  — same shape as impression, sent via  sendBeacon {
  "event": "opportunity_click",
  "properties": {
    "opportunity_id": "opp-8a1f",
    "opportunity_title": "Data Engineer (STIP)",
    "opportunity_type": "STIP",
    "opportunity_source": "OTG",
    "opportunity_agency": "psd",
    "is_ringfenced": false,
    "match_source": "search",
    "list_position": 2,
    "page": 1
  }
}  opportunity_viewed  — carries  match_source  from the listing via  ?ms= ;  $set s the view timestamp {
  "event": "opportunity_viewed",
  "properties": {
    "opportunity_id": "opp-8a1f",
    "opportunity_title": "Data Engineer (STIP)",
    "opportunity_type": "STIP",
    "opportunity_source": "OTG",
    "opportunity_agency": "psd",
    "is_ringfenced": false,
    "match_source": "search",
    "$set": {
      "last_opportunity_viewed_at": "2026-06-25T05:12:30.000Z"
    }
  }
} opportunity_applied  —  $set  last +  $set_once  first (never overwritten) {
  "event": "opportunity_applied",
  "properties": {
    "opportunity_id": "opp-8a1f",
    "opportunity_title": "Data Engineer (STIP)",
    "opportunity_type": "STIP",
    "opportunity_source": "OTG",
    "opportunity_agency": "psd",
    "is_ringfenced": false,
    "application_method": "FormSG",
    "$set": {
      "last_opportunity_applied_at": "2026-06-25T05:14:02.000Z"
    },
    "$set_once": {
      "first_opportunity_applied_at": "2026-06-25T05:14:02.000Z"
    }
  }
} PostHog also attaches its autocapture context ( distinct_id ,  $current_url ,  $session_id , etc.) to every event — the  properties  above are only the custom keys this feature adds.  Acceptance criteria Each of the 6 events fires per its trigger;  impression  deduped once per card per listing view; zero-result searches still fire  opportunity_search . opportunity_click  survives navigation (sendBeacon). opportunity_viewed / applied   $set  the timestamp person-properties;  first_opportunity_applied_at  is  $set_once . All props use the stable enums above;  opportunity_title  present on the 4 core events. Funnel  impression → click → viewed → applied  and OKR 2 (unique persons with  opportunity_applied ) are derivable from events — no person-property counters. Non-goals Count /  opportunity_types_applied  person properties (derived from events; ingestion may materialize later — same deferral as  is_ringfenced /OTEP-127). recommendation  match_source (no recommendation surface yet). Confirming the external application actually submitted (FormSG/C@G happen off-site);  applied  records the Apply action. Building the PostHog funnel/insight in the UI (analyst task).

---

## Subtasks

| Key | Summary | Status |
|-----|---------|--------|
| OTEP-569 | Events | Backlog |

---

## Latest Comments

**Thomas Huchedé** (2026-08-18)
Yes, any preference for the new label?  C@G-redirect ?  Careers@Gov ? something else?

---

**Michelle Yip** (2026-08-17)
This does not make any sense for C@G, and we dont have OTG redirection at all either. Shall we keep  FormSG  for OTG opportunities and get a new label for C@G?    Agree with your proposal.

---

**Michelle Yip** (2026-08-17)
yes pls. Thanks u!

---
*Synced from Jira: 2026-08-19*
