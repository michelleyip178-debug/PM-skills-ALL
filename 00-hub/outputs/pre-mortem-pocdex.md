# Pre-Mortem: POCDEX Integration

**Date**: 2026-05-22
**Scenario**: It is November 2026, one month after Go-Live. The POCDEX integration is a disaster. Officers are locked out, support tickets are piling up, and the opportunity ringfence is leaking. Why did this happen?

## 1. The "Real-Time Sync" Illusion
**What went wrong**: We assumed POCDEX pushes to OTEP instantaneously when HR creates a profile in HRPS/Cumulus. In reality, HR batch-processes new hires at the end of the week, or the sync pipeline takes 24-48 hours.
**The impact**: New hires are logging into OTEP on Day 1, hitting the "Profile pending" error, and spamming the helpdesk. The "edge case" became the norm.
**How to prevent this now**: 
- Get a strict SLA from Daryll's team on the exact P95 latency between HR profile creation and the POCDEX push.
- Re-design the "Profile pending" error state to tell the officer *exactly* when to check back (e.g., "Profiles usually take 48 hours to sync"), deflecting support tickets.

## 2. Dirty Data Breaks the Ringfence
**What went wrong**: We built the ringfence (OTEP-127) assuming a pristine `agency_code` field. HRPS data entry was messy—agencies used abbreviations, trailing spaces, or left it null for contractors. 
**The impact**: Eligible officers in the pilot group were locked out of opportunities, or worse, non-pilot officers bypassed the filter because of a null-handling bug in our backend logic.
**How to prevent this now**: 
- Demand the exact Enum schema for `agency_code` from Imelda's Reference Data dependency (#18).
- Implement strict payload validation on our API service (OTEP-203). If the agency code isn't an exact match to our whitelist, default to "deny access."

## 3. The Cross-Squad Bandwidth Squeeze
**What went wrong**: Daryll's team had limited bandwidth. They prioritized Imelda's Core Squad requirements (Epic 1 Profile, Epic 2 Competency) over Pathfinder's Ringfencing needs.
**The impact**: Pow Hwee and Léo finished OTEP-271 and OTEP-203 in Sprint 3, but we couldn't get a UAT test environment or integration testing support from Daryll's team in Sprint 4. The Ringfencing release slipped past Feature Freeze.
**How to prevent this now**: 
- In the upcoming planning session with Daryll (#31), force a stack-ranked prioritization between Pathfinder's Ringfencing and Imelda's Epics. Get a documented commitment for integration testing windows.

## 4. No Reconciliation Job (The "Silent Drop")
**What went wrong**: We relied entirely on webhooks/pushes from POCDEX. When the network blipped or our OTEP-203 service restarted during a deployment, payloads were dropped. 
**The impact**: Dozens of officer profiles were never created in OTEP. Because we had no mechanism to "pull" or reconcile missing data, they remained permanently locked out until they complained.
**How to prevent this now**: 
- Ask Daryll's team: *Does POCDEX support a bulk reconciliation endpoint or a retry mechanism for failed pushes?* If not, we must build a nightly cron job to sync state.
