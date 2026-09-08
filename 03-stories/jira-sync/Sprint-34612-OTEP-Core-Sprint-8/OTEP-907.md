# OTEP-907: Gosec Rule ID G201: seed.go

**Status:** Done
**Assignee:** Léo Milbor
**Story Points:** N/A
**Sprint:** OTEP-Core Sprint 8 (34612)

---

## Description

"A1:2017 - Injection"; "Gosec Rule ID G201"; gosec.G202-1; "A03:2021 - Injection"; "Gosec Rule ID G202" With below details: Improper neutralization of special elements used in an SQL command ('SQL Injection')

SQL Injection is a critical vulnerability that can lead to data or system compromise. By\ndynamically generating SQL query strings, user input may be able to influence the logic of\nthe SQL statement. This could lead to an adversary accessing information they should\nnot have access to or in some circumstances, being able to execute OS functionality or code.\n\nReplace all dynamically generated SQL queries with parameterized queries. In situations where\ndynamic queries must be created, never use direct user input, but instead use a map or\ndictionary of valid values and resolve them using a user supplied key.\n\nFor example, some database drivers do not allow parameterized queries for `>` or `<` comparison\noperators. In these cases, do not use a user supplied `>` or `<` value, but rather have the\nuser\nsupply a `gt` or `lt` value. The alphabetical values are then used to look up the `>` and `<`\nvalues to be used in the construction of the dynamic query. The same goes for other queries\nwhere\ncolumn or table names are required but cannot be parameterized.\n\nExample using parameterized queries with `sql.Query`:\n```\nrows, err := db.Query("SELECT * FROM users WHERE userName = ?", userName)\nif err != nil {\n    return nil, err\n}\ndefer rows.Close()\nfor rows.Next() {\n  // ... process rows\n}\n```\n\nFor more information on SQL Injection see OWASP:\nhttps://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html\n
  internal/service/opportunity/opportunitytest/seed.go:202-217 internal/service/opportunity/opportunitytest/seed.go:68-81  I’ve taken a look at the code, but it don’t look to have any SQL injections to be of concern. But please help validate

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Adrian Lo** (2026-07-29)
Thanks Leo. Will likely flag this as a false positive since it’s not in actual production code

---

**Léo Milbor** (2026-07-28)
Thanks for checking   . I thinks it’s flagging it because we do `description = fmt.Sprintf("Test opportunity: %s", f.Title)`. In any cases, this is for integration testing only (package is  opportunitytest  which is our test harness for integration testing). I think we could update so it’s not flagged, but not sure on the priority regarding this.

---
*Synced from Jira: 2026-09-07*
