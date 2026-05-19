# OTEP-170: Base Layout for Opportunity Listing Page

**Status:** In Progress
**Assignee:** Thomas Huchedé
**Story Points:** N/A

---

## Description

As a user, I should be able to Jobs & Opportunities landing page when I click on Jobs and Opportunities.    The listing page should show the structural layout - filter side bar, search bar, and maximum 15 cards on a 3x5 matrix.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Rathika Ramalingam** (2026-05-18)
High Level Test Cases: Scenario 1: User navigates to the Jobs & Opportunities page Given  the user is logged into the application When  they click on "Jobs and Opportunities" tab in the Home Page Then  the system routes them to the Jobs & Opportunities page And  the UI successfully renders the Search Bar component at the top And  the UI successfully renders the Filter Sidebar component on the side. Scenario 2: Loading the listing with the more number of jobs than the page limit Given  the system database contains more than 15 active job opportunities to display When  the user loads the Jobs & Opportunities page Then  the system fetches a maximum of 15 job records And  displays exactly 15 job cards on the screen Scenario 3: Loading the listing with fewer jobs than the page limit Given  the system database contains exactly 7 active job opportunities When  the user loads the Jobs & Opportunities page Then  the system fetches all 7 job records And  displays exactly 6 job cards on the screen. Scenario 4: Loading the listing with no available jobs (Empty State) Given  the system database contains 0 active job opportunities When  the user loads the Jobs & Opportunities page Then  0 job cards are rendered And  the system displays a clear "No jobs available" empty state message. Scenario 5: Structural grid layout matches design intent Given  the Jobs & Opportunities page has successfully loaded 15 job cards When  the user views the page on a standard desktop viewport Then  the cards are arranged in a grid layout And  the overall structural layout (Sidebar, Search Bar, and the 3x5 card matrix) strictly matches the spatial design defined in  Figma:
