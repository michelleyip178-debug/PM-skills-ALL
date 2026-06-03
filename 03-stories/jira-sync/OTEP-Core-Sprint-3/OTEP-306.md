# OTEP-306: Verify the env is not impacted with Mini Shai-Hulud" and lock the env to strictly use the locked versions only.

**Type:** Sub-task
**Status:** QA
**Assignee:** Soumya Routa
**Story Points:** N/A

---

## Description

To remain current lockfile configuration remains uncompromised moving forward, integrate these security practices immediately:



* *Enforce the Firewall Flag in CI/CD:* Ensure that your GitLab pipeline maps package installations strictly through this parameter:
{noformat}Bash{noformat}
{noformat}pnpm install --frozen-lockfile
{noformat}
* *Do Not Blindly Regenerate:* If your pipeline fails due to a dependency mismatch error or peer conflict, *do not delete* {{pnpm-lock.yaml}} *and re-run installation*. Treat a sudden, unexpected lockfile validation failure as a warning that an upstream package might have been modified or hijacked.
* *Targeted Upgrades Only:* If you must update a specific module, avoid running a blanket {{pnpm update}}. Isolate changes to single packages using:
{noformat}Bash{noformat}
{noformat}pnpm update <package-name>
{noformat}

Your lockfile successfully creates a completely deterministic, immutable snapshot of your code infrastructure. Keep it versioned, frozen in production, and you will stay insulated from these supply-chain pivots.

---

## Subtasks

_No subtasks._

---

## Latest Comments

**Soumya Routa:** The required review has been completed, and the repository is not impacted by the Mini Shai-Hulud issue.

As preventive measures, the required changes have already been implemented for both the Docker build process and npm installation flow. [https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-web/-/merge_requests/21|https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-web/-/merge_requests/21]

*Synced from Jira: 2026-06-03*
