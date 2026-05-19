# BO Grooming Script — May 7, 2026 (14:00–16:00)

---

## Opening (2 min)

> "Thanks everyone for joining. Today's session has two parts: first, a quick Sprint 1 status update — where we are and what's on track. Second, I need a few decisions from you that will unblock Sprint 2.
>
> Sprint 2 is where officers actually start seeing the opportunity hub, so today's decisions directly shape what they'll experience."

---

## Part 1: Sprint 1 Status (10 min)

> "Quick status check. Our Sprint 1 goal is: **Login and navigate to Jobs and Opportunities.** We're on day 4 of 14. 13 work items in the sprint."

> "**What's done:**
> - Frontend repo is set up
> - Database conventions are baselined
> - Schema migration is in QA — nearly done
>
> **What's actively being built:**
> - Login authentication through Keycloak — in progress, on track
> - Auth flow exploration — in progress, on track
>
> **Still in backlog (8 items):**
> - Data model, pipeline design, listing page scaffold, POCDEX spike, FormSG discovery, plus local dev setup items
>
> **But here's the key framing** — and this was agreed with the team:
> - Sprint 1 is about getting **login working end-to-end** and **landing data decisions**. Not building the full pipeline.
> - The opportunity listing will be a skeleton at most. Real data and features are Sprint 2.
> - The 8 backlog items aren't 'behind' — the decision-making ones (data model, pipeline approach) are what we're here to unblock today."

> "So: auth is on track. The risk isn't in building — it's in **decisions**. If we don't land certain decisions today, Sprint 2 can't start cleanly. That's what Part 2 is about."

---

## Part 2: Sprint 2 Preview (5 min)

> "Let me show you what officers will get by end of Sprint 2 — May 30."

*[Show the Sprint 2 scope mockups]*

> "By end of Sprint 2 — May 30 — an officer can:
> 1. Log in with their gov.sg email
> 2. See OTG opportunities they're **eligible for** — ringfencing applied based on their profile
> 3. Browse STIPs, Gigs, SJRs, and Internal Jobs in one listing
> 4. Filter by opportunity type — four categories
> 5. Sort by posted date or closing date
> 6. See a 'Closing soon' label on opportunities expiring within 7 days
> 7. Click into a full detail page — reporting line, what they'll gain, competency tags
> 8. Click 'Apply via OTG' and get redirected to the specific posting on OTG
>
> **What we're NOT doing in Sprint 2:**
> - No Careers@Gov listings — we're prioritising OTG first. C@G comes after OTG is stable.
> - No function filter — type filter only. We're still investigating the function taxonomy.
> - No competency match scoring — the detail page shows competency tags as 'What you'll develop,' but doesn't calculate how well you match. That's Release 1.
> - No FormSG application route — STIPs and Gigs apply flow comes later.
> - Data will be seed/mock data — the live OTG pipeline is a fast-follow. We've already agreed mock data is acceptable for Sprint 2."

> "Think of Sprint 2 as: **the full discovery-to-apply experience works for OTG opportunities.** We're building the UI and interaction layer. Live data and C@G get layered in once OTG is stable."

---

## Part 3: Decisions (30–40 min)

### Decision 1: Data Freshness (5 min)

> "When we sync opportunity data from OTG into OTEP — how fresh does it need to be?
>
> Options:
> - **Real-time** — complex, higher infrastructure cost
> - **Daily sync** — simpler, some lag but manageable for MVP
> - **Weekly** — probably too stale
>
> **My recommendation:** Daily sync for MVP. Officers aren't going to notice a few hours' lag. Real-time adds significant complexity and we can upgrade to it in Release 1 if needed.
>
> Are we comfortable with daily?"

*[Capture decision]*

---

### Decision 2: Careers@Gov Ingestion (10 min)

> "We need to decide how Careers@Gov data gets into OTEP. This won't block Sprint 2 — we're doing OTG first — but we need to start planning so C@G isn't months behind.
>
> Three options:"

| Option | What it means | Trade-off |
|--------|---------------|-----------|
| API | Real-time sync from C@G system | Cleanest, but needs C@G team to give us access |
| File export | Periodic data dump | Simple, but data can go stale |
| Scrape | Pull from C@G website | No dependency on their team, but fragile |

> "**My recommendation:** Push for API access as our default path. It's the cleanest long-term solution. If the C@G team can't support it within our timeline, we fall back to file export.
>
> Either way — this is decoupled from OTG. We don't need C@G sorted to start Sprint 2. But I'd like a direction today so we can start conversations with the C@G team."

*[Capture decision]*

---

### Decision 3: Pilot Group Definition (5 min)

> "For the MVP, only ESG and PSD officers can log in. How do we determine who's 'in'?
>
> Option A: Pull from POCDEX agency code — system-driven, automatic.
> Option B: Manual whitelist that we maintain.
>
> **My recommendation:** POCDEX agency code. It's automatic, scales with new officers joining, and doesn't require us to maintain a list.
>
> Does anyone see a reason to go manual?"

*[Capture decision]*

---

### Decision 4: Secondment Classification (5 min)

> "Quick one. Is 'Secondment' a separate opportunity type in the filter — or is it a sub-type of SJR?
>
> This affects how many filter categories we show. Right now we have four OTG types: STIP, Gig, SJR, Internal Jobs. No C@G in this sprint since we're doing OTG first.
>
> **My recommendation:** Treat Secondment as a sub-type of SJR for MVP. We can split it out later if officers find it confusing. Keeps the filter simple — four categories.
>
> Thoughts?"

*[Capture decision]*

---

### Decision 5: Edge Case — Officer Logs In Before POCDEX Push (5 min)

> "Scenario: A new officer joins public service on Monday. They try to log in to OTEP on their first day, but POCDEX hasn't pushed their record yet. What do they see?
>
> Option A: 'You don't have access' — same as unauthorised users.
> Option B: 'Your profile is being set up, check back shortly.'
>
> **My recommendation:** Option B — 'profile pending.' Option A would confuse a legitimate new officer and might generate support tickets. Option B sets the right expectation.
>
> Comfortable with that?"

*[Capture decision]*

---

### Decision 6: Function Filter (5 min)

> "The original design included a function/job-family filter — things like 'Arts & Culture,' 'Business & Innovation,' 'Finance,' etc.
>
> We've agreed with the team that this is **not in Sprint 2**. But I want to flag a deeper issue we've discovered:
>
> **OTG and Careers@Gov use different taxonomies.**
> - OTG categorises opportunities by **Job Functions** — things like HR, Finance, IT, Policy.
> - Careers@Gov uses what looks like **sectoral categorisation** — Arts & Culture, Health & Social, Environment & Sustainability.
>
> These don't map 1:1. So when we eventually build a function filter that spans both sources, we have a decision to make:
> - Do we create a **unified taxonomy** and map both into it? (Clean UX, but significant mapping work)
> - Do we show **two separate filter dimensions** — function + sector? (Confusing for officers)
> - Do we pick **one system's taxonomy as master** and map the other into it? (Simpler, but lossy)
>
> **My recommendation:** Defer the function filter to Release 1. For MVP, type filter + keyword search is sufficient. This gives us time to investigate the taxonomy mismatch properly without rushing a bad mapping.
>
> But I want to flag this now so it's on everyone's radar — this isn't just a 'build the filter' task, it's a data architecture decision.
>
> Are BOs comfortable deferring function filter to Release 1?"

*[Capture decision]*

---

## Part 4: Priority Confirmation (5 min)

> "If the sprint gets tight and we can only deliver a subset by May 18, here's my suggested priority order:
>
> 1. **Login authentication** — gates everything
> 2. **Data decisions landed** — gates Sprint 2 build
> 3. **POCDEX spike started** — gates account creation
> 4. **Listing page skeleton** — head start for Sprint 2
> 5. **Error states** — can harden in Sprint 2
> 6. **FormSG discovery** — Sprint 4 dependency, can wait
>
> Does this order make sense? Anything you'd move up or down?"

*[Capture priority order]*

---

## Closing (2 min)

> "To summarise what we've landed today:"

*[Read back captured decisions]*

> "Just to confirm what was already decided earlier:
> - Ringfencing is per-opportunity — set on each posting
> - Lifecycle is auto-close by date — no closing date means evergreen, pushed to bottom
> - Mock data is acceptable for Sprint 2
>
> With today's decisions, Sprint 2 is unblocked. The team can start building the full OTG discovery-to-apply experience.
>
> Next session we'll review Sprint 2 progress — by then you should see the listing page with cards, filters, and the detail page coming together. Any questions?"

---

## Time Budget

| Section | Duration | Running total |
|---------|----------|---------------|
| Opening | 2 min | 0:02 |
| Sprint 1 status | 10 min | 0:12 |
| Sprint 2 preview | 5 min | 0:17 |
| Decisions (6) | 35 min | 0:52 |
| Priority confirmation | 5 min | 0:57 |
| Closing | 3 min | 1:00 |
| **Buffer / discussion overflow** | **60 min** | **2:00** |

You have a full hour of buffer for discussions that run long or new topics that surface.
