Here’s what was agreed for **Sprint 1** based on the meeting:

## Sprint 1 – Agreed Scope

**1. Authentication / Login**

- Implement a **very basic login flow**:
  - A simple, possibly “ugly” **Sign‑in button** is acceptable.
  - Goal: allow frontend to **trigger login**, hit the backend, and **receive a token** so the app knows whether the user is logged in.
- **Frontend**:
  - Build the minimal sign‑in / sign‑out button and wiring to handle the token.
  - Submit this for **review within the sprint** so the other team can start using it by the **start of next sprint**.
- **Backend**:
  - Implement **authentication logic** for Pathfinder (auth flow on the server side).
  - Set up **baseline database connection** and start on **reference table / schema** work (Bowie on DB model & ref tables).
- **Design**:
  - No need to wait for a polished login screen; a placeholder / non‑final UI is fine as long as auth works.

**2. Opportunities – Sprint 1 Deliverables**

- **No full-featured listing yet**:
  - For Sprint 1, focus is on **getting auth and backend foundations ready**, not on delivering the complete opportunities experience.
- Agreement that after Sprint 1:
  - You will have **authentication working end‑to‑end** (front + back).
  - For opportunities:
    - At most, a **skeleton / base layout** can exist.
    - **Real data, filters, sorting, and search** are expected to come in **Sprint 2 and beyond**, not in Sprint 1.

**3. Function Filter & Categorization – Not in Sprint 1**

- The **function filter** on the opportunities listing:
  - **Will not be implemented in Sprint 1.**
  - You will first **investigate and discuss** with Huawei / Paul Yi how to handle:
    - OTG vs Careers@Gov categorization.
    - Whether to combine, hide, or defer the function filter.
- Target within Sprint 1:
  - **Clarify the approach** and dependency (e.g., may decide to remove function filter for now and rely only on type/sort).
  - But the **actual function‑based filtering will not be delivered** in Sprint 1.

**4. Data Model & Upstream Dependencies**

- Sprint 1 includes:
  - **Raising and clarifying the dependency** on:
    - Job family / function model.
    - Competency bank (Imelda / competency squads).
  - You will **not own or design** the full job‑family/function/competency model in Sprint 1.
- The outcome for this sprint is:
  - **Alignment and escalation**, not technical implementation of the full model.

---

In short, Sprint 1 is about **getting login/authentication and basic backend & DB foundations working**, plus **clarifying (not building) the function/competency data model and filters**. The full opportunities listing experience—including filters, sorting, and real data—is explicitly pushed to **Sprint 2+**.

---

Would you like me to extract just the **user stories / acceptance criteria** implied for Sprint 1, so you can check them against what’s currently in JIRA?