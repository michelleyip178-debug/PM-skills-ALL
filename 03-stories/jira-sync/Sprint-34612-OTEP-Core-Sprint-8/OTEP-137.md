# OTEP-137: Base setup

**Status:** Done
**Assignee:** Adrian Lo
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

Base setup for backend repository I want  to establish a clean, standard Go project structure with graceful lifecycle management and common build tooling,  So that  the team can immediately start building features with a consistent, production-ready foundation.  Requirement Technical Specification Checked Project Structure Adopt standard Go layout ( /cmd ,  /internal ,  /pkg ).  Graceful Shutdown Implement signal handling ( SIGINT / SIGTERM ) to shutdown  http.Server  without dropping active requests.  Basic Server main.go  must run an  http.Server  and expose a  /health  endpoint returning  200 OK .  Configuration Centralize configuration loading (use standard environment variable overrides).  Tooling Provide a  Makefile  that encapsulates build, test, lint, and run commands.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._

---
*Synced from Jira: 2026-08-20*
