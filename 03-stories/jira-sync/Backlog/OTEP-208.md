# OTEP-208: Wire up golang-migrate in cmd/migrate

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

The cmd/migrate entrypoint currently only connects to the database but does not run migrations. Wire up golang-migrate so it reads .up.sql/.down.sql files from the migrations/ directory. Scope Add golang-migrate/migrate dependency to go.mod Update cmd/migrate/main.go to run migrations from migrations/ directory Support up (apply all pending) and down (rollback last) operations Wire into Makefile: make db-migrate, make db-migrate-down Acceptance Criteria make db-migrate applies all pending .up.sql files in order make db-migrate-down rolls back the last applied migration Migration state tracked in schema_migrations table Idempotent: running migrate when already up-to-date is a no-op

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
