# OTEP-444: Azure/Entra AD mock solution for testing (no WOG AD test env)

**Status:** In Progress
**Assignee:** Léo Milbor
**Story Points:** 3
**Sprint:** OTEP-Pathfinder Sprint 6 (34620)

---

## Description

Mock solution for WOG AD Context For MVP, users will authenticate through WOG AD (a dedicated Microsoft Entra AD, formerly Azure AD). Exploration Excluded solutions Public SaaS (Auth0, Okta Dev Tenants):  They introduce unnecessary data-residency risks. GitHub Mocks (e.g.,  mock-azure-ad ,  mock-oidc-provider ):  These seems like pet projects (few GitHub stars and one maintainer). API Mockers (WireMock, Mockoon):  Simulating a multi-step auth flow with a REST API mocker is an exercise in misery and fragility. Solutions Local or CI Secondary Keycloak Instance (Mock-Entra) Setup:  Already in our stack, requires configuring custom claim mappers once Fidelity:  Can precisely emit  oid ,  tid , and  groups  arrays via custom mappers. Validates signatures deterministically. Note: apparently, we don’t necessarily need a separate instance and can just create another dedicated realm in the one we have. However, I don’t think the “cost” of a second instance is a concern and this would keep our main keycloak configuration closer to prod. Cloud (Dev/QA) Dedicated Entra ID Tenant (M365 Dev) Setup:  Requires AzureAD provider. We should be able to leverage a terraform provider. Cost & Licensing  (free if we have a cloud subscription) There is a  hashicorp provider  for automated provisioning Needs to store new secrets in our vault Fidelity:  This  IS  Entra AD Secondary Keycloak Instance Same justification as for local or CI, we just also promote it to DEV and QA environment. This is  only  if we cannot use a real dedicated Entra ID. Attention points Token Version Mismatches:  Entra ID supports  v1.0  and  v2.0  OIDC endpoints.  v1.0  returns different claims (e.g.,  upn  instead of  preferred_username ). Our configuration should mirrors the exact production version. Claims:  I didn’t take into account how we would handle claims/groups/roles and such. As far as I understand, this is, for now, off loaded to pocdex.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pow Hwee TAN (PSD)** (2026-06-24)
From what I understand from Fabien’s message before he went on leave, the Azure AD is available for ‘testing’, in the sense that we can integrate with it except that to login will need a real user id.  Which I think is fine.  Again if I interpreted correctly, Fabien also whitelisted the dev env’s URL to the Azure AD.  Fabien should be back in Sprint 5.   In the current Sprint 4, Boon Siang is setting up the egress (a path for our backend to call Azure AD to validate token).  You can approach him on the status of egress.   Short of this, the fallback will be to use the Keycloak realm as you suggested.  This ticket will be brought forward to Sprint 5.

---
*Synced from Jira: 2026-07-16*
