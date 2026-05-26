# OTEP-142: Dockerfile & docker-compose

**Type:** Sub-task
**Status:** Done
**Assignee:** Pei Ern Lim
**Story Points:** N/A

---

## Description

h1. Dockerfile & docker-compose

*I want* a multi-stage Dockerfile and a Docker Compose orchestration setup, *So that* I can ensure consistent, reproducible builds and spin up a complete local development environment (including Postgres) with a single command.



h2. 

|*Requirement*|*Technical Specification*|*Checked*|
|*Dockerfile*|Implement 2-stage build: {{builder}} stage (Go toolchain) and {{runtime}} stage (Distroless or Alpine).|Used Alpine image.|
|*Artifact Size*|Ensure final image does not include source code, git metadata, or build tools.| |
|*Compose Setup*|Define {{app}} and {{postgres}} services. Use a shared {{network}} and {{volume}} for persistence.| |
|*Dependency Wait*|Use {{healthcheck}} in Postgres and {{depends_on}} (with {{service_healthy}}) in the app to prevent boot race conditions.| |
|*Makefile Integration*|Expose targets: {{docker-build}}, {{docker-up}}, {{docker-down}}, and {{docker-logs}}.| |

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
