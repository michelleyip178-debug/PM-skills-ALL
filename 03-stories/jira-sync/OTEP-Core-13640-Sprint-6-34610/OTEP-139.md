# OTEP-139: Database integration

**Type:** Sub-task
**Status:** Done
**Assignee:** Pei Ern Lim
**Story Points:** N/A

---

## Description

h1. Integration to Postgresql database

*I want* to integrate a PostgreSQL database using GORM with proper connection pooling and lifecycle management, *So that* the application can store data durably, perform migrations automatically, and maintain high availability via robust health checks.

|*Requirement*|*Technical Specification*|*Checked*|
|*Driver & ORM*|Import {{gorm.io/driver/postgres}} and {{gorm.io/gorm}}.| |
|*Config Integration*|DB credentials/DSN must be loaded via config (env vars/file) and validated at app startup.| |
|*Connection Pooling*|Configure {{sql.DB}} pool settings: {{SetMaxOpenConns(25)}}, {{SetMaxIdleConns(25)}}, and {{SetConnMaxLifetime(5 * time.Minute)}}.| |
|*Health Check*|Update {{/health}} to verify DB readiness via {{db.DB().Ping()}}. Return {{503 Service Unavailable}} if connection fails.| |
|*Migrations*|Implement migrations using golang-migrate.|*Notes:* 
We introduced a test migration to create a temp table for validation purposes.
This test migration wil be removed when we add the first actual table later|
|*Seeding*|Add a {{Seed()}} function that checks {{if count == 0}} before inserting initial data.| |
|*Make Targets*|Add {{make db-migrate}} and {{make db-seed}} to the Makefile.| |
|*Query logging*|Defaults to on for now
On/Off for different environments to be done later| |

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Pei Ern Lim:** Remove usage of AutoMigrate with GORM due to it does not support audit trail and migrate up/down.

Switch to use [golang-migrate|https://github.com/golang-migrate/migrate] to handle the migration.

*Synced from Jira: 2026-07-23*
