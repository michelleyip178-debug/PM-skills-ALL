# OTEP-278: Pass the coverage report artifact to the SonarQube job.

**Type:** Sub-task
**Status:** QA
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

SonarQube is excellent for tracks *Branch Coverage* (checking every decision path) rather than just *Line Coverage*.

To make this work:

# Ensure your {{unit-tests}} job runs *before* or in the same stage as {{ship-sonarqube-scan}}.
# Pass the coverage report artifact to the SonarQube job.
# SonarQube will then flag "Quality Gate Failed"

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** [https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-service/-/pipelines/19196198|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-service/-/pipelines/19196198]

!image-20260514-103458.png|width=465,alt="image-20260514-103458.png"!

