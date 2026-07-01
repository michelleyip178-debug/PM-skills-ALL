# Duplicate Cleanup Candidates - Jira Sync Cache

**Generated:** 2026-07-01 (W27)
**Source:** Jira-sync cache audit, agent `ab401d18d99996339`
**Scope:** `PM-skills-ALL-1/03-stories/jira-sync/`
**Status:** Report only. No files deleted. Human review required before any deletion.

## Summary

- **180 duplicate groups** documented (one OTEP ticket key with 2+ copies across folders)
- Total stale files flagged as delete candidates: **314**
- Original scratch data (`all_dup_groups_final.json`) was still present in `$TMPDIR/jsync/` this session, so this report uses that data directly (not re-derived from disk).

### Cluster sizes (biggest first)

| Cluster (stale folder) | Groups | Note |
|---|---|---|
| `OTEP-Core-Sprint-3/` | 93 | Old-naming Core Sprint 3 folder, superseded by newer sprint folders per ticket |
| `OTEP-Pathfinder-12541-Sprint-4-34618/` | 67 | New-naming Pathfinder Sprint 4 folder also appears stale in some groups (superseded by a different canonical, e.g. re-sprinted ticket) |
| `Sprint-34619-OTEP-Pathfinder-Sprint-5/` | 11 | Old-naming Pathfinder Sprint 5 folder (74 files on disk; only 11 have a matching file in the new-naming Sprint-5 folder captured in this dup dataset — see note below) |
| `Backlog/` | 5 | Backlog folder copies superseded by sprint-allocated canonical copies |
| `OTEP-Core-Sprint-4/` | 3 | Old-naming Core Sprint 4 folder |
| `OTEP-Pathfinder-12541-Sprint-5-34619/` | 1 | New-naming Sprint 5 folder itself flagged stale in one group (superseded elsewhere) |

> **Note on Pathfinder Sprint 5:** The old-naming folder `Sprint-34619-OTEP-Pathfinder-Sprint-5/` has 74 ticket files on disk, but the new-naming folder `OTEP-Pathfinder-12541-Sprint-5-34619/` only has 12. The duplicate dataset only flags a file as "stale" when a canonical counterpart exists elsewhere — so only 11 of the 74 old-folder files show up here as confirmed duplicates. The remaining ~63 old-folder files do not have a matching canonical file captured in this dataset; they may be genuinely unique (never re-synced into the new folder) rather than safe-to-delete duplicates. Recommend a follow-up `/jira-sync` pass to confirm whether those 63 tickets still belong in the current sprint before deleting anything in that folder wholesale.

---

## Cluster: `OTEP-Core-Sprint-3/` (93 groups)

| Ticket | Canonical (KEEP) | Stale (DELETE CANDIDATE) | Reason |
|---|---|---|---|
| OTEP-74 | `OTEP-Core-13640-Sprint-5-34609/OTEP-74.md` | `OTEP-Core-Sprint-3/OTEP-74.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-75 | `OTEP-Core-13640-Sprint-5-34609/OTEP-75.md` | `OTEP-Core-Sprint-3/OTEP-75.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-105 | `OTEP-Core-13640-Sprint-5-34609/OTEP-105.md` | `OTEP-Core-Sprint-3/OTEP-105.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-112 | `OTEP-Core-13640-Sprint-5-34609/OTEP-112.md` | `OTEP-Core-Sprint-3/OTEP-112.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-116 | `OTEP-Core-13640-Sprint-5-34609/OTEP-116.md` | `OTEP-Core-Sprint-2/OTEP-116.md<br>OTEP-Core-Sprint-3/OTEP-116.md` | richest of stale copies (picked OTEP-Core-Sprint-2), copied into correct sprint folder |
| OTEP-117 | `OTEP-Core-13640-Sprint-5-34609/OTEP-117.md` | `OTEP-Core-Sprint-3/OTEP-117.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-118 | `OTEP-Core-13640-Sprint-5-34609/OTEP-118.md` | `OTEP-Core-Sprint-3/OTEP-118.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-119 | `OTEP-Core-13640-Sprint-5-34609/OTEP-119.md` | `OTEP-Core-Sprint-3/OTEP-119.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-120 | `OTEP-Core-13640-Sprint-5-34609/OTEP-120.md` | `OTEP-Core-Sprint-3/OTEP-120.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-126 | `OTEP-Core-13640-Sprint-5-34609/OTEP-126.md` | `OTEP-Core-Sprint-3/OTEP-126.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-134 | `OTEP-Core-13640-Sprint-5-34609/OTEP-134.md` | `OTEP-Core-Sprint-3/OTEP-134.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-136 | `OTEP-Core-13640-Sprint-5-34609/OTEP-136.md` | `OTEP-Core-Sprint-3/OTEP-136.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-137 | `OTEP-Core-13640-Sprint-5-34609/OTEP-137.md` | `OTEP-Core-Sprint-2/OTEP-137.md<br>OTEP-Core-Sprint-3/OTEP-137.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-138 | `OTEP-Core-13640-Sprint-5-34609/OTEP-138.md` | `OTEP-Core-Sprint-2/OTEP-138.md<br>OTEP-Core-Sprint-3/OTEP-138.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-139 | `OTEP-Core-13640-Sprint-5-34609/OTEP-139.md` | `OTEP-Core-Sprint-2/OTEP-139.md<br>OTEP-Core-Sprint-3/OTEP-139.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-140 | `OTEP-Core-13640-Sprint-5-34609/OTEP-140.md` | `OTEP-Core-Sprint-2/OTEP-140.md<br>OTEP-Core-Sprint-3/OTEP-140.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-141 | `OTEP-Core-13640-Sprint-5-34609/OTEP-141.md` | `OTEP-Core-Sprint-2/OTEP-141.md<br>OTEP-Core-Sprint-3/OTEP-141.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-142 | `OTEP-Core-13640-Sprint-5-34609/OTEP-142.md` | `OTEP-Core-Sprint-2/OTEP-142.md<br>OTEP-Core-Sprint-3/OTEP-142.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-143 | `OTEP-Core-13640-Sprint-5-34609/OTEP-143.md` | `OTEP-Core-Sprint-2/OTEP-143.md<br>OTEP-Core-Sprint-3/OTEP-143.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-144 | `OTEP-Core-13640-Sprint-5-34609/OTEP-144.md` | `OTEP-Core-Sprint-3/OTEP-144.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-145 | `OTEP-Core-13640-Sprint-5-34609/OTEP-145.md` | `OTEP-Core-Sprint-3/OTEP-145.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-146 | `OTEP-Core-13640-Sprint-5-34609/OTEP-146.md` | `OTEP-Core-Sprint-3/OTEP-146.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-147 | `OTEP-Core-13640-Sprint-5-34609/OTEP-147.md` | `OTEP-Core-Sprint-3/OTEP-147.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-148 | `OTEP-Core-13640-Sprint-5-34609/OTEP-148.md` | `OTEP-Core-Sprint-3/OTEP-148.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-149 | `OTEP-Core-13640-Sprint-5-34609/OTEP-149.md` | `OTEP-Core-Sprint-3/OTEP-149.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-150 | `OTEP-Core-13640-Sprint-5-34609/OTEP-150.md` | `OTEP-Core-Sprint-2/OTEP-150.md<br>OTEP-Core-Sprint-3/OTEP-150.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-151 | `OTEP-Core-13640-Sprint-5-34609/OTEP-151.md` | `OTEP-Core-Sprint-2/OTEP-151.md<br>OTEP-Core-Sprint-3/OTEP-151.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-152 | `OTEP-Core-13640-Sprint-5-34609/OTEP-152.md` | `OTEP-Core-Sprint-2/OTEP-152.md<br>OTEP-Core-Sprint-3/OTEP-152.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-153 | `OTEP-Core-13640-Sprint-5-34609/OTEP-153.md` | `OTEP-Core-Sprint-3/OTEP-153.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-154 | `OTEP-Core-13640-Sprint-5-34609/OTEP-154.md` | `OTEP-Core-Sprint-3/OTEP-154.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-155 | `OTEP-Core-13640-Sprint-5-34609/OTEP-155.md` | `OTEP-Core-Sprint-2/OTEP-155.md<br>OTEP-Core-Sprint-3/OTEP-155.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-156 | `OTEP-Core-13640-Sprint-5-34609/OTEP-156.md` | `OTEP-Core-Sprint-3/OTEP-156.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-157 | `OTEP-Core-13640-Sprint-5-34609/OTEP-157.md` | `OTEP-Core-Sprint-3/OTEP-157.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-158 | `OTEP-Core-13640-Sprint-5-34609/OTEP-158.md` | `OTEP-Core-Sprint-2/OTEP-158.md<br>OTEP-Core-Sprint-3/OTEP-158.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-159 | `OTEP-Core-13640-Sprint-5-34609/OTEP-159.md` | `OTEP-Core-Sprint-3/OTEP-159.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-160 | `OTEP-Core-13640-Sprint-5-34609/OTEP-160.md` | `OTEP-Core-Sprint-3/OTEP-160.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-161 | `OTEP-Core-13640-Sprint-5-34609/OTEP-161.md` | `OTEP-Core-Sprint-3/OTEP-161.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-162 | `OTEP-Core-13640-Sprint-5-34609/OTEP-162.md` | `OTEP-Core-Sprint-3/OTEP-162.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-166 | `OTEP-Core-13640-Sprint-5-34609/OTEP-166.md` | `OTEP-Core-Sprint-2/OTEP-166.md<br>OTEP-Core-Sprint-3/OTEP-166.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-167 | `OTEP-Core-13640-Sprint-5-34609/OTEP-167.md` | `OTEP-Core-Sprint-3/OTEP-167.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-168 | `OTEP-Core-13640-Sprint-5-34609/OTEP-168.md` | `OTEP-Core-Sprint-3/OTEP-168.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-169 | `OTEP-Core-13640-Sprint-5-34609/OTEP-169.md` | `OTEP-Core-Sprint-3/OTEP-169.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-180 | `OTEP-Core-13640-Sprint-5-34609/OTEP-180.md` | `OTEP-Core-Sprint-3/OTEP-180.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-187 | `OTEP-Core-13640-Sprint-5-34609/OTEP-187.md` | `OTEP-Core-Sprint-3/OTEP-187.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-188 | `OTEP-Core-13640-Sprint-5-34609/OTEP-188.md` | `OTEP-Core-Sprint-3/OTEP-188.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-189 | `OTEP-Core-13640-Sprint-5-34609/OTEP-189.md` | `OTEP-Core-Sprint-3/OTEP-189.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-195 | `OTEP-Core-13640-Sprint-5-34609/OTEP-195.md` | `OTEP-Core-Sprint-2/OTEP-195.md<br>OTEP-Core-Sprint-3/OTEP-195.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-198 | `OTEP-Core-13640-Sprint-5-34609/OTEP-198.md` | `OTEP-Core-Sprint-2/OTEP-198.md<br>OTEP-Core-Sprint-3/OTEP-198.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-199 | `OTEP-Core-13640-Sprint-5-34609/OTEP-199.md` | `OTEP-Core-Sprint-2/OTEP-199.md<br>OTEP-Core-Sprint-3/OTEP-199.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-200 | `OTEP-Core-13640-Sprint-5-34609/OTEP-200.md` | `OTEP-Core-Sprint-2/OTEP-200.md<br>OTEP-Core-Sprint-3/OTEP-200.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-211 | `OTEP-Core-13640-Sprint-5-34609/OTEP-211.md` | `OTEP-Core-Sprint-3/OTEP-211.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-213 | `OTEP-Core-13640-Sprint-5-34609/OTEP-213.md` | `OTEP-Core-Sprint-2/OTEP-213.md<br>OTEP-Core-Sprint-3/OTEP-213.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-214 | `OTEP-Core-13640-Sprint-5-34609/OTEP-214.md` | `OTEP-Core-Sprint-2/OTEP-214.md<br>OTEP-Core-Sprint-3/OTEP-214.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-215 | `OTEP-Core-13640-Sprint-5-34609/OTEP-215.md` | `OTEP-Core-Sprint-3/OTEP-215.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-216 | `OTEP-Core-13640-Sprint-5-34609/OTEP-216.md` | `OTEP-Core-Sprint-3/OTEP-216.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-217 | `OTEP-Core-13640-Sprint-5-34609/OTEP-217.md` | `OTEP-Core-Sprint-3/OTEP-217.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-218 | `OTEP-Core-13640-Sprint-5-34609/OTEP-218.md` | `OTEP-Core-Sprint-3/OTEP-218.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-219 | `OTEP-Core-13640-Sprint-5-34609/OTEP-219.md` | `OTEP-Core-Sprint-2/OTEP-219.md<br>OTEP-Core-Sprint-3/OTEP-219.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-225 | `OTEP-Core-13640-Sprint-5-34609/OTEP-225.md` | `OTEP-Core-Sprint-3/OTEP-225.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-226 | `OTEP-Core-13640-Sprint-5-34609/OTEP-226.md` | `OTEP-Core-Sprint-2/OTEP-226.md<br>OTEP-Core-Sprint-3/OTEP-226.md` | richest of stale copies (picked OTEP-Core-Sprint-2), copied into correct sprint folder |
| OTEP-227 | `OTEP-Core-13640-Sprint-5-34609/OTEP-227.md` | `OTEP-Core-Sprint-3/OTEP-227.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-229 | `OTEP-Core-13640-Sprint-5-34609/OTEP-229.md` | `OTEP-Core-Sprint-3/OTEP-229.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-234 | `OTEP-Core-13640-Sprint-5-34609/OTEP-234.md` | `OTEP-Core-Sprint-2/OTEP-234.md<br>OTEP-Core-Sprint-3/OTEP-234.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-237 | `OTEP-Core-13640-Sprint-5-34609/OTEP-237.md` | `OTEP-Core-Sprint-3/OTEP-237.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-261 | `OTEP-Core-13640-Sprint-5-34609/OTEP-261.md` | `OTEP-Core-Sprint-3/OTEP-261.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-262 | `OTEP-Core-13640-Sprint-5-34609/OTEP-262.md` | `OTEP-Core-Sprint-3/OTEP-262.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-263 | `OTEP-Core-13640-Sprint-5-34609/OTEP-263.md` | `OTEP-Core-Sprint-2/OTEP-263.md<br>OTEP-Core-Sprint-3/OTEP-263.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-266 | `OTEP-Core-13640-Sprint-5-34609/OTEP-266.md` | `OTEP-Core-Sprint-2/OTEP-266.md<br>OTEP-Core-Sprint-3/OTEP-266.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-269 | `OTEP-Core-13640-Sprint-5-34609/OTEP-269.md` | `OTEP-Core-Sprint-2/OTEP-269.md<br>OTEP-Core-Sprint-3/OTEP-269.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-270 | `OTEP-Core-13640-Sprint-5-34609/OTEP-270.md` | `OTEP-Core-Sprint-3/OTEP-270.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-272 | `OTEP-Core-13640-Sprint-5-34609/OTEP-272.md` | `OTEP-Core-Sprint-3/OTEP-272.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-275 | `OTEP-Core-13640-Sprint-5-34609/OTEP-275.md` | `OTEP-Core-Sprint-2/OTEP-275.md<br>OTEP-Core-Sprint-3/OTEP-275.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-277 | `OTEP-Core-13640-Sprint-5-34609/OTEP-277.md` | `OTEP-Core-Sprint-3/OTEP-277.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-278 | `OTEP-Core-13640-Sprint-5-34609/OTEP-278.md` | `OTEP-Core-Sprint-3/OTEP-278.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-279 | `OTEP-Core-13640-Sprint-5-34609/OTEP-279.md` | `OTEP-Core-Sprint-3/OTEP-279.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-280 | `OTEP-Core-13640-Sprint-5-34609/OTEP-280.md` | `OTEP-Core-Sprint-3/OTEP-280.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-293 | `OTEP-Core-13640-Sprint-5-34609/OTEP-293.md` | `OTEP-Core-Sprint-3/OTEP-293.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-294 | `OTEP-Core-13640-Sprint-5-34609/OTEP-294.md` | `OTEP-Core-Sprint-3/OTEP-294.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-297 | `OTEP-Core-13640-Sprint-5-34609/OTEP-297.md` | `OTEP-Core-Sprint-2/OTEP-297.md<br>OTEP-Core-Sprint-3/OTEP-297.md` | richest of stale copies (picked OTEP-Core-Sprint-3), copied into correct sprint folder |
| OTEP-298 | `OTEP-Core-13640-Sprint-5-34609/OTEP-298.md` | `OTEP-Core-Sprint-3/OTEP-298.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-306 | `OTEP-Core-13640-Sprint-5-34609/OTEP-306.md` | `OTEP-Core-Sprint-3/OTEP-306.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-308 | `OTEP-Core-13640-Sprint-5-34609/OTEP-308.md` | `OTEP-Core-Sprint-3/OTEP-308.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-310 | `OTEP-Core-13640-Sprint-5-34609/OTEP-310.md` | `OTEP-Core-Sprint-3/OTEP-310.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-311 | `OTEP-Core-13640-Sprint-5-34609/OTEP-311.md` | `OTEP-Core-Sprint-3/OTEP-311.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-312 | `OTEP-Core-13640-Sprint-5-34609/OTEP-312.md` | `OTEP-Core-Sprint-3/OTEP-312.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-338 | `Backlog/OTEP-338.md` | `OTEP-Core-Sprint-3/OTEP-338.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-339 | `OTEP-Core-13640-Sprint-5-34609/OTEP-339.md` | `OTEP-Core-Sprint-3/OTEP-339.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-340 | `OTEP-Core-13640-Sprint-5-34609/OTEP-340.md` | `OTEP-Core-Sprint-3/OTEP-340.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-341 | `OTEP-Core-13640-Sprint-5-34609/OTEP-341.md` | `OTEP-Core-Sprint-3/OTEP-341.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-342 | `OTEP-Core-13640-Sprint-5-34609/OTEP-342.md` | `OTEP-Core-Sprint-3/OTEP-342.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-343 | `OTEP-Core-13640-Sprint-5-34609/OTEP-343.md` | `OTEP-Core-Sprint-3/OTEP-343.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-365 | `OTEP-Core-13640-Sprint-5-34609/OTEP-365.md` | `OTEP-Core-Sprint-3/OTEP-365.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-384 | `OTEP-Core-13640-Sprint-5-34609/OTEP-384.md` | `OTEP-Core-Sprint-3/OTEP-384.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |

## Cluster: `OTEP-Pathfinder-12541-Sprint-4-34618/` (67 groups)

| Ticket | Canonical (KEEP) | Stale (DELETE CANDIDATE) | Reason |
|---|---|---|---|
| OTEP-85 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-85.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-85.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-85.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-85.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-86 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-86.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-86.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-86.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-87 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-87.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-87.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-87.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-88 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-88.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-88.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-88.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-88.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-127 | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-127.md` | `OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-127.md` | already in correct live-sprint folder (Sprint-34618-OTEP-Pathfinder-Sprint-4) |
| OTEP-128 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-128.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-128.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-128.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-128.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-129 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-129.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-129.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-129.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-129.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-131 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-131.md` | `Backlog/OTEP-131.md<br>Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-131.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-131.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-170 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-170.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-170.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-170.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-170.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-193 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-193.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-193.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-193.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-193.md<br>OTEP-Pathfinder-12541-Sprint-2-34616/OTEP-193.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-268 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-268.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-268.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-268.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-268.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-276 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-276.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-276.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-276.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-276.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-284 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-284.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-284.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-284.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-288 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-288.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-288.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-288.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-288.md<br>OTEP-Pathfinder-12541-Sprint-2-34616/OTEP-288.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-289 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-289.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-289.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-289.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-289.md<br>OTEP-Pathfinder-12541-Sprint-2-34616/OTEP-289-spike-definition.md<br>OTEP-Pathfinder-12541-Sprint-2-34616/OTEP-289.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-296 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-296.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-296.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-296.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-296.md<br>OTEP-Pathfinder-12541-Sprint-2-34616/OTEP-296.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-305 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-305.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-305.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-305.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-305.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-313 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-313.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-313.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-313.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-313.md<br>OTEP-Pathfinder-12541-Sprint-2-34616/OTEP-313.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-314 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-314.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-314.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-314.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-314.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-320 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-320.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-320.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-320.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-320.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-322 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-322.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-322.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-322.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-322.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-324 | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-324.md` | `OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-324.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-324.md` | already in correct live-sprint folder (Sprint-34618-OTEP-Pathfinder-Sprint-4) |
| OTEP-325 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-325.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-325.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-325.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-325.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-326 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-326.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-326.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-326.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-326.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-327 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-327.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-327.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-327.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-327.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-328 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-328.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-328.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-328.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-329 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-329.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-329.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-329.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-334 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-334.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-334.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-334.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-334.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-348 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-348.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-348.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-348.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-348.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-349 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-349.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-349.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-349.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-350 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-350.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-350.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-350.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-350.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-358 | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-358.md` | `OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-358.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-358.md` | already in correct live-sprint folder (Sprint-34618-OTEP-Pathfinder-Sprint-4) |
| OTEP-361 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-361.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-361.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-361.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-361.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-362 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-362.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-362.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-362.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-362.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-363 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-363.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-363.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-363.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-363.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-367 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-367.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-367.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-367.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-367.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-368 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-368.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-368.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-368.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-368.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-369 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-369.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-369.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-369.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-369.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-374 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-374.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-374.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-374.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-374.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-375 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-375.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-375.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-375.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-375.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-380 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-380.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-380.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-380.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-380.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-381 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-381.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-381.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-381.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-381.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-386 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-386.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-386.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-386.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-392 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-392.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-392.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-392.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-393 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-393.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-393.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-393.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-397 | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-397.md` | `OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-397.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-397.md` | already in correct live-sprint folder (Sprint-34618-OTEP-Pathfinder-Sprint-4) |
| OTEP-403 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-403.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-403.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-403.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-404 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-404.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-404.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-404.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-405 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-405.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-405.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-405.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-406 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-406.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-406.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-406.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-427 | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-427.md` | `OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-427.md` | already in correct live-sprint folder (Sprint-34618-OTEP-Pathfinder-Sprint-4) |
| OTEP-438 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-438.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-438.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-438.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-438.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-439 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-439.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-439.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-439.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-440 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-440.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-440.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-440.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-441 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-441.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-441.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-441.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-444 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-444.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-444.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-444.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-445 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-445.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-445.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-445.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-482 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-482.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-482.md<br>OTEP-Pathfinder-12541-Sprint-3-34617/OTEP-482.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-482.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-483 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-483.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-483.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-483.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-484 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-484.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-484.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-484.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-485 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-485.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-485.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-485.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-495 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-495.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-495.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-495.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-496 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-496.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-496.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-496.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-499 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-499.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-499.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-499.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-505 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-505.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-505.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-505.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-536 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-536.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-536.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-536.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |
| OTEP-539 | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-539.md` | `Sprint-34618-OTEP-Pathfinder-Sprint-4/OTEP-539.md<br>OTEP-Pathfinder-12541-Sprint-4-34618/OTEP-539.md` | already in correct live-sprint folder (Sprint-34619-OTEP-Pathfinder-Sprint-5) |

## Cluster: `Sprint-34619-OTEP-Pathfinder-Sprint-5/` (11 groups)

| Ticket | Canonical (KEEP) | Stale (DELETE CANDIDATE) | Reason |
|---|---|---|---|
| OTEP-283 | `OTEP-Pathfinder-12541-Sprint-5-34619/OTEP-283.md` | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-283.md` | already in correct live-sprint folder (OTEP-Pathfinder-12541-Sprint-5-34619) |
| OTEP-304 | `OTEP-Pathfinder-12541-Sprint-5-34619/OTEP-304.md` | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-304.md` | already in correct live-sprint folder (OTEP-Pathfinder-12541-Sprint-5-34619) |
| OTEP-336 | `OTEP-Pathfinder-12541-Sprint-5-34619/OTEP-336.md` | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-336.md` | already in correct live-sprint folder (OTEP-Pathfinder-12541-Sprint-5-34619) |
| OTEP-390 | `OTEP-Pathfinder-12541-Sprint-5-34619/OTEP-390.md` | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-390.md` | already in correct live-sprint folder (OTEP-Pathfinder-12541-Sprint-5-34619) |
| OTEP-408 | `OTEP-Pathfinder-12541-Sprint-5-34619/OTEP-408.md` | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-408.md` | already in correct live-sprint folder (OTEP-Pathfinder-12541-Sprint-5-34619) |
| OTEP-409 | `OTEP-Pathfinder-12541-Sprint-5-34619/OTEP-409.md` | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-409.md` | already in correct live-sprint folder (OTEP-Pathfinder-12541-Sprint-5-34619) |
| OTEP-437 | `OTEP-Pathfinder-12541-Sprint-5-34619/OTEP-437.md` | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-437.md` | already in correct live-sprint folder (OTEP-Pathfinder-12541-Sprint-5-34619) |
| OTEP-540 | `OTEP-Pathfinder-12541-Sprint-5-34619/OTEP-540.md` | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-540.md` | already in correct live-sprint folder (OTEP-Pathfinder-12541-Sprint-5-34619) |
| OTEP-541 | `OTEP-Pathfinder-12541-Sprint-5-34619/OTEP-541.md` | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-541.md` | already in correct live-sprint folder (OTEP-Pathfinder-12541-Sprint-5-34619) |
| OTEP-570 | `OTEP-Pathfinder-12541-Sprint-5-34619/OTEP-570.md` | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-570.md` | already in correct live-sprint folder (OTEP-Pathfinder-12541-Sprint-5-34619) |
| OTEP-571 | `OTEP-Pathfinder-12541-Sprint-5-34619/OTEP-571.md` | `Sprint-34619-OTEP-Pathfinder-Sprint-5/OTEP-571.md` | already in correct live-sprint folder (OTEP-Pathfinder-12541-Sprint-5-34619) |

## Cluster: `Backlog/` (5 groups)

| Ticket | Canonical (KEEP) | Stale (DELETE CANDIDATE) | Reason |
|---|---|---|---|
| OTEP-78 | `OTEP-Core-13640-Sprint-6-34610/OTEP-78.md` | `Backlog/OTEP-78.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-82 | `OTEP-Core-13640-Sprint-6-34610/OTEP-82.md` | `Backlog/OTEP-82.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-83 | `OTEP-Core-13640-Sprint-6-34610/OTEP-83.md` | `Backlog/OTEP-83.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-84 | `OTEP-Core-13640-Sprint-6-34610/OTEP-84.md` | `Backlog/OTEP-84.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-290 | `OTEP-Core-13640-Sprint-5-34609/OTEP-290.md` | `Backlog/OTEP-290.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |

## Cluster: `OTEP-Core-Sprint-4/` (3 groups)

| Ticket | Canonical (KEEP) | Stale (DELETE CANDIDATE) | Reason |
|---|---|---|---|
| OTEP-77 | `Backlog/OTEP-77.md` | `OTEP-Core-Sprint-4/OTEP-77.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-205 | `OTEP-Core-13640-Sprint-5-34609/OTEP-205.md` | `OTEP-Core-Sprint-4/OTEP-205.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
| OTEP-321 | `OTEP-Core-13640-Sprint-5-34609/OTEP-321.md` | `OTEP-Core-Sprint-4/OTEP-321.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |

## Cluster: `OTEP-Pathfinder-12541-Sprint-5-34619/` (1 groups)

| Ticket | Canonical (KEEP) | Stale (DELETE CANDIDATE) | Reason |
|---|---|---|---|
| OTEP-281 | `Backlog/OTEP-281.md` | `OTEP-Pathfinder-12541-Sprint-5-34619/OTEP-281.md` | relocated to match live Jira sprint (single copy, was in wrong folder) |
