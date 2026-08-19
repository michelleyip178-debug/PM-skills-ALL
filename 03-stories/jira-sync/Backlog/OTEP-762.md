# OTEP-762: Provision Standalone Keycloak ECS Service and Runtime Configuration

**Type:** Task
**Status:** Backlog
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Context OTEP-745 provisions the dedicated Aurora PostgreSQL database for Keycloak and OTEP-747 wires the DB credentials into the existing embedded Keycloak ECS task. This ticket goes further: it provisions Keycloak as a fully standalone ECS service, independent from  otep-service , with its own task definition, ALB integration, and production-mode runtime configuration per ADR-008. Scope ECS task definition and service: Dedicated ECS task definition for Keycloak (separate from  otep-service ) Dedicated ECS service with desired count of at least 2 in prd Container ports:  8080 / 8443  (frontend),  9000  (management, internal only),  7800  and  57800  (Infinispan cluster) Runtime environment: KC_DB=postgres
KC_DB_URL=jdbc:postgresql://<aurora-cluster-endpoint>:5432/<keycloak_db>
KC_DB_USERNAME=<from secret>
KC_DB_PASSWORD=<from secret>
KC_HOSTNAME=https://auth.<domain>
KC_HOSTNAME_STRICT=true
KC_PROXY_HEADERS=xforwarded
KC_HTTP_ENABLED=true
KC_CACHE=ispn
KC_HEALTH_ENABLED=true
KC_METRICS_ENABLED=true ALB integration: Target group for Keycloak frontend traffic Listener rules for public login/OIDC paths Admin path ( /admin/ ) restricted Health check strategy configured ECS deployment behavior: Rolling or recreate strategy documented Deployment circuit breaker configured if supported Log group configured Acceptance Criteria [ ] Keycloak ECS service is deployed independently from  otep-service [ ] Keycloak starts in production mode (not  start-dev ) [ ] ECS service reaches steady state [ ] ALB target group reports healthy targets [ ] Keycloak connects to the dedicated Aurora database [ ] Keycloak public hostname resolves to the ALB [ ] OIDC discovery endpoint responds correctly [ ] Management port  9000  is not publicly exposed [ ] Admin path is restricted per the agreed access model [ ] prd desired count is at least 2 [ ] Infinispan cluster formation is visible from logs or metrics References Keycloak: Configuring a reverse proxy Keycloak: Configuring distributed caches Notes Depends on: OTEP-745 (database), OTEP-747 (DB wiring), Keycloak module (Ticket 1), CI/CD onboarding (Ticket 2). Blocks: migration and cutover ticket. Epic: OTEP-759.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Léo Milbor** (2026-08-19)
For restricted Admin path ( /admin/ ):  - We want it only in dev (maybe qa also) but deactivated in higher env.  - It should also allow  /admin  (at the time of writing,  /admin  leads to career compass).

---

**Léo Milbor** (2026-08-12)
, I think this one is done already. Can you confirm?
