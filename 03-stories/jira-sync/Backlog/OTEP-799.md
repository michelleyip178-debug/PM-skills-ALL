# OTEP-799: Update OTG Import Mapping: Map Assignment Start Date to Application Closing Date

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Context:   Currently, OTG opportunities are imported into the system via an Excel sheet. These records only provide an "Open" status and lack a dedicated application closing date. Because the status remains perpetually "Open," no housekeeping is performed on the OTG side to clean up closed opportunities, resulting in stale data persisting in our system. To resolve this and ensure automated housekeeping functions properly, we need to adjust our data mapping logic to use the opportunity's Assignment Start Date as the proxy for the Application Closing Date. The current behaviour of the import logic relies on  end_date  and  closing_date  mapping that lack a distinct closing date.   Acceptance criteria: The system must successfully map the  start-date  value from the OTG Excel import sheet directly to the  closing_date  field in the database. System should successfully recognise and hide OTG opportunities once their newly mapped  closing_date  has passed.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Rathika Ramalingam** (2026-08-03)
Blocked - Decided NOT to implement for now.  Reason - There will be way less qualifying otg opportunities left if we implement this condition.

---

**Rathika Ramalingam** (2026-07-22)
Hi   , created this task as discussed. Thanks
