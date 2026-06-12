#!/usr/bin/env python3
"""
Generate a self-contained HTML planning dashboard for the NEXT (future) sprint.

Usage:
    python3 next-sprint-dashboard.py                    # next future sprint on Pathfinder (12541)
    JIRA_BOARD_ID=13640 python3 next-sprint-dashboard.py
    python3 next-sprint-dashboard.py --sprint 34618     # specific sprint id
    python3 next-sprint-dashboard.py --current 34617    # override current sprint id for carry-over check
    python3 next-sprint-dashboard.py --out ~/plan.html

Shows: scope summary, assignee load, readiness flags, carry-over risk from current sprint.
Reads JIRA_EMAIL / JIRA_API_TOKEN / JIRA_SITE from 03-stories/.env. Run with sandbox OFF.
"""

import argparse
import base64
import json
import os
import sys
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BOARD = os.environ.get("JIRA_BOARD_ID", "12541")
HUB = ROOT.parent / "00-hub"

DONE = {"done", "closed", "resolved"}
TODO = {"to do", "open", "backlog", "selected for development"}

STATUS_ORDER = ["To Do", "Open", "Selected for Development", "Backlog",
                "In Progress", "In Development", "In Review", "Code Review", "QA", "Done", "Closed"]


def load_env():
    env = {}
    envfile = ROOT / ".env"
    if not envfile.exists():
        sys.exit(f"No .env at {envfile}")
    for line in envfile.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def jget(url, auth):
    req = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "Authorization": "Basic " + base64.b64encode(auth.encode()).decode(),
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def bucket(status_name):
    s = status_name.lower()
    if s in DONE:
        return "done"
    if s in TODO:
        return "todo"
    return "inprogress"


def pull_issues(base, auth, sprint_id):
    issues = []
    start_at = 0
    while True:
        page = jget(
            f"{base}/rest/agile/1.0/sprint/{sprint_id}/issue"
            f"?fields=summary,status,assignee,issuetype,priority,description,labels"
            f"&maxResults=100&startAt={start_at}", auth)
        issues.extend(page.get("issues", []))
        if start_at + page.get("maxResults", 100) >= page.get("total", 0):
            break
        start_at += page.get("maxResults", 100)
    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--board", default=DEFAULT_BOARD)
    ap.add_argument("--sprint", default=None, help="next sprint id (default: first future sprint)")
    ap.add_argument("--current", default=None, help="current sprint id for carry-over check")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    env = load_env()
    site = env["JIRA_SITE"]
    auth = f"{env['JIRA_EMAIL']}:{env['JIRA_API_TOKEN']}"
    base = f"https://{site}"

    # Resolve next sprint
    if args.sprint:
        next_sprint = jget(f"{base}/rest/agile/1.0/sprint/{args.sprint}", auth)
    else:
        data = jget(f"{base}/rest/agile/1.0/board/{args.board}/sprint?state=future", auth)
        vals = [v for v in data.get("values", []) if v.get("originBoardId") == int(args.board)
                or True]  # take first future regardless
        if not vals:
            sys.exit(f"No future sprints on board {args.board}")
        next_sprint = vals[0]

    # Resolve current sprint for carry-over
    current_sprint = None
    if args.current:
        current_sprint = jget(f"{base}/rest/agile/1.0/sprint/{args.current}", auth)
    else:
        data = jget(f"{base}/rest/agile/1.0/board/{args.board}/sprint?state=active", auth)
        vals = data.get("values", [])
        if vals:
            current_sprint = vals[0]

    nsid = next_sprint["id"]
    nsname = next_sprint["name"]
    ns_start = (next_sprint.get("startDate") or "")[:10]
    ns_end = (next_sprint.get("endDate") or "")[:10]

    # Pull next sprint issues
    ns_issues = pull_issues(base, auth, nsid)

    # Pull current sprint issues for carry-over risk
    carry_over = []
    cur_name = ""
    if current_sprint:
        cur_name = current_sprint["name"]
        cur_issues = pull_issues(base, auth, current_sprint["id"])
        for i in cur_issues:
            f = i["fields"]
            b = bucket(f["status"]["name"])
            if b != "done":
                carry_over.append({
                    "key": i["key"],
                    "status": f["status"]["name"],
                    "bucket": b,
                    "assignee": (f.get("assignee") or {}).get("displayName") or "Unassigned",
                    "type": f["issuetype"]["name"],
                    "summary": f["summary"],
                })

    # Analyse next sprint issues
    rows = []
    type_counts = Counter()
    assignee_load = defaultdict(lambda: {"count": 0, "stories": 0, "tasks": 0, "subtasks": 0})
    not_ready = []  # readiness flags

    for i in ns_issues:
        f = i["fields"]
        key = i["key"]
        st = f["status"]["name"]
        a = (f.get("assignee") or {}).get("displayName") or "Unassigned"
        t = f["issuetype"]["name"]
        pr = (f.get("priority") or {}).get("name") or ""
        desc = f.get("description") or {}
        # description can be Atlassian Document Format (dict) or plain string
        if isinstance(desc, dict):
            desc_len = len(json.dumps(desc))
        else:
            desc_len = len(str(desc))
        labels = f.get("labels") or []

        type_counts[t] += 1
        assignee_load[a]["count"] += 1
        tl = t.lower()
        if "story" in tl:
            assignee_load[a]["stories"] += 1
        elif "sub" in tl or "subtask" in tl:
            assignee_load[a]["subtasks"] += 1
        else:
            assignee_load[a]["tasks"] += 1

        flags = []
        if a == "Unassigned":
            flags.append("no assignee")
        if desc_len < 50:
            flags.append("no description")
        if st.lower() == "backlog":
            flags.append("still in Backlog")

        if flags:
            not_ready.append({"key": key, "type": t, "assignee": a, "status": st,
                               "flags": flags, "summary": f["summary"]})

        rows.append({"key": key, "status": st, "type": t, "assignee": a,
                     "priority": pr or "—", "flags": flags, "summary": f["summary"]})

    total = len(rows)
    unassigned_n = sum(1 for r in rows if r["assignee"] == "Unassigned")
    not_ready_n = len(not_ready)

    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    html = build_html(
        nsname, ns_start, ns_end,
        total, unassigned_n, not_ready_n,
        rows, type_counts, assignee_load, not_ready,
        carry_over, cur_name,
        generated,
    )

    out = args.out or str(HUB / "next-sprint-dashboard.html")
    Path(out).write_text(html, encoding="utf-8")
    print(f"✓ {nsname} ({ns_start} → {ns_end}): {total} issues")
    print(f"  {not_ready_n} readiness flag(s) · {unassigned_n} unassigned · {len(carry_over)} carry-over risk(s)")
    print(f"  → {out}")


def build_html(nsname, ns_start, ns_end,
               total, unassigned_n, not_ready_n,
               rows, type_counts, assignee_load, not_ready,
               carry_over, cur_name, generated):

    # Readiness score
    ready_n = total - not_ready_n
    ready_pct = round(100 * ready_n / total) if total else 0
    if ready_pct >= 80:
        ready_color, ready_label = "#22c55e", "ready"
    elif ready_pct >= 50:
        ready_color, ready_label = "#f59e0b", "partially ready"
    else:
        ready_color, ready_label = "#ef4444", "needs grooming"

    # Type chips
    type_chips = "".join(
        f'<span class="chip">{esc(t)} <b>{n}</b></span>'
        for t, n in type_counts.most_common())

    # Assignee table
    asg = sorted(assignee_load.items(), key=lambda kv: -kv[1]["count"])
    max_count = max((v["count"] for _, v in asg), default=1)
    asg_rows = ""
    for name, v in asg:
        w = 100 * v["count"] / max_count
        is_unassigned = name == "Unassigned"
        style = ' style="color:#ef4444"' if is_unassigned else ""
        asg_rows += (f'<tr>'
                     f'<td class="nm"{style}>{esc(name)}</td>'
                     f'<td class="bar"><div class="track">'
                     f'<div class="fill{"x" if is_unassigned else ""}" style="width:{w:.0f}%"></div>'
                     f'</div></td>'
                     f'<td class="num">{v["count"]}</td>'
                     f'<td class="num">{v["stories"]}</td>'
                     f'<td class="num">{v["tasks"]}</td>'
                     f'<td class="num">{v["subtasks"]}</td></tr>')

    # Readiness flags table
    if not_ready:
        flag_rows = "".join(
            f'<tr>'
            f'<td class="k">{esc(r["key"])}</td>'
            f'<td>{esc(r["type"])}</td>'
            f'<td>{esc(r["assignee"])}</td>'
            f'<td>{esc(r["status"])}</td>'
            f'<td>{", ".join(f"<span class=\'flag\'>{esc(fl)}</span>" for fl in r["flags"])}</td>'
            f'<td>{esc(r["summary"])}</td>'
            f'</tr>'
            for r in not_ready)
        flags_html = (f'<table class="tbl"><thead><tr>'
                      f'<th>Key</th><th>Type</th><th>Assignee</th>'
                      f'<th>Status</th><th>Issues</th><th>Summary</th>'
                      f'</tr></thead><tbody>{flag_rows}</tbody></table>')
    else:
        flags_html = '<p class="ok">All issues are groomed and ready. 🎉</p>'

    # Carry-over risks
    if carry_over:
        co_rows = "".join(
            f'<tr data-b="{r["bucket"]}">'
            f'<td class="k">{esc(r["key"])}</td>'
            f'<td><span class="dot" style="background:{bucket_color(r["status"])}"></span>'
            f'{esc(r["status"])}</td>'
            f'<td>{esc(r["type"])}</td>'
            f'<td>{esc(r["assignee"])}</td>'
            f'<td>{esc(r["summary"])}</td>'
            f'</tr>'
            for r in carry_over)
        inprog_n = sum(1 for r in carry_over if r["bucket"] == "inprogress")
        todo_n = sum(1 for r in carry_over if r["bucket"] == "todo")
        carry_label = f"{len(carry_over)} unfinished in {cur_name} — {inprog_n} in progress, {todo_n} not started"
        carry_html = (f'<p class="carry-note">{esc(carry_label)}</p>'
                      f'<table class="tbl"><thead><tr>'
                      f'<th>Key</th><th>Status</th><th>Type</th><th>Assignee</th><th>Summary</th>'
                      f'</tr></thead><tbody>{co_rows}</tbody></table>')
    else:
        carry_html = f'<p class="ok">No open items in {esc(cur_name)}. Clean handoff. 🎉</p>'

    # All issues table
    issue_rows = "".join(
        f'<tr>'
        f'<td class="k">{esc(r["key"])}</td>'
        f'<td>{esc(r["type"])}</td>'
        f'<td>{esc(r["assignee"])}</td>'
        f'<td>{esc(r["status"])}</td>'
        f'<td>{", ".join(f"<span class=\'flag\'>{esc(fl)}</span>" for fl in r["flags"]) or "<span class=\'ok-sm\'>✓</span>"}</td>'
        f'<td>{esc(r["summary"])}</td>'
        f'</tr>'
        for r in sorted(rows, key=lambda r: (not r["flags"], r["assignee"] == "Unassigned", r["key"]))
    )

    days_away = ""
    try:
        sd = datetime.fromisoformat(ns_start)
        today = datetime.now()
        diff = (sd - today).days
        if diff > 0:
            days_away = f" · starts in {diff} day{'s' if diff != 1 else ''}"
        elif diff == 0:
            days_away = " · starts today"
    except Exception:
        pass

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(nsname)} — Planning Dashboard</title>
<style>
  :root{{--bg:#0f172a;--card:#1e293b;--mut:#94a3b8;--fg:#e2e8f0;--line:#334155;}}
  *{{box-sizing:border-box}}
  body{{margin:0;font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
    background:var(--bg);color:var(--fg);padding:24px;max-width:1100px;margin:0 auto}}
  h1{{font-size:22px;margin:0 0 2px}}
  .badge{{display:inline-block;background:#1e3a5f;color:#60a5fa;font-size:11px;
    border-radius:4px;padding:2px 8px;margin-left:8px;vertical-align:middle;font-weight:600}}
  .sub{{color:var(--mut);font-size:13px;margin-top:4px}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;margin:20px 0}}
  .card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px}}
  .card h2{{font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut);margin:0 0 10px}}
  .big{{font-size:30px;font-weight:700}}
  .big small{{font-size:14px;color:var(--mut);font-weight:400}}
  .track{{background:#0b1220;border-radius:5px;height:16px;overflow:hidden}}
  .fill{{background:#3b82f6;height:100%;border-radius:5px}}
  .fillx{{background:#ef4444;height:100%;border-radius:5px}}
  table{{width:100%;border-collapse:collapse}}
  .atbl td{{padding:6px 8px;vertical-align:middle}}
  .atbl .nm{{width:160px}}
  .atbl .bar{{width:auto}}
  .atbl .num{{text-align:right;width:52px;color:var(--mut);font-variant-numeric:tabular-nums}}
  .atbl thead th{{font-size:11px;text-transform:uppercase;color:var(--mut);text-align:right;padding:4px 8px}}
  .atbl thead th:first-child,.atbl thead th:nth-child(2){{text-align:left}}
  .chip{{display:inline-block;background:#0b1220;border:1px solid var(--line);border-radius:999px;
    padding:4px 12px;margin:0 6px 6px 0;font-size:13px}}
  .chip b{{color:#60a5fa}}
  .tbl{{font-size:13px;margin-top:6px}}
  .tbl th{{text-align:left;font-size:11px;text-transform:uppercase;color:var(--mut);
    border-bottom:1px solid var(--line);padding:6px 8px}}
  .tbl td{{padding:6px 8px;border-bottom:1px solid #243044;vertical-align:top}}
  .k{{font-family:ui-monospace,monospace;color:#60a5fa;white-space:nowrap}}
  .dot{{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px}}
  .ok{{color:#22c55e;font-size:13px}}
  .ok-sm{{color:#22c55e}}
  .flag{{display:inline-block;background:#3b1f1f;color:#fca5a5;border-radius:4px;
    padding:1px 7px;font-size:11px;margin-right:4px}}
  .carry-note{{color:var(--mut);font-size:13px;margin:0 0 10px}}
  section{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;margin:16px 0}}
  section h2{{font-size:14px;margin:0 0 14px}}
  .ready-bar{{height:10px;border-radius:5px;overflow:hidden;background:#0b1220;margin-bottom:8px}}
  .ready-fill{{height:100%;border-radius:5px;background:{ready_color};transition:width .3s}}
  .foot{{color:var(--mut);font-size:12px;margin-top:24px;text-align:center}}
</style></head><body>

<header>
  <h1>{esc(nsname)} <span class="badge">PLANNING</span></h1>
  <div class="sub">{ns_start} → {ns_end}{days_away} · {total} issues committed</div>
</header>

<div class="grid">
  <div class="card"><h2>Total Committed</h2>
    <div class="big">{total}<small> issues</small></div></div>
  <div class="card"><h2>Readiness</h2>
    <div class="big" style="color:{ready_color}">{ready_pct}%<small> · {ready_label}</small></div>
    <div class="ready-bar" style="margin-top:10px">
      <div class="ready-fill" style="width:{ready_pct}%"></div></div></div>
  <div class="card"><h2>Unassigned</h2>
    <div class="big" style="color:{'#ef4444' if unassigned_n > 0 else '#22c55e'}">{unassigned_n}
    <small> issue{'s' if unassigned_n != 1 else ''}</small></div></div>
  <div class="card"><h2>Carry-over Risk</h2>
    <div class="big" style="color:{'#f59e0b' if carry_over else '#22c55e'}">{len(carry_over)}
    <small> open in S3</small></div></div>
</div>

<section><h2>Issue Types</h2>{type_chips}</section>

<section>
  <h2>Workload by Assignee</h2>
  <table class="atbl"><thead><tr>
    <th>Assignee</th><th></th><th>Total</th><th>Stories</th><th>Tasks</th><th>Sub-tasks</th>
  </tr></thead><tbody>{asg_rows}</tbody></table>
</section>

<section>
  <h2>Readiness Flags ({not_ready_n} issues need attention)</h2>
  {flags_html}
</section>

<section>
  <h2>Carry-over Risk from {esc(cur_name)}</h2>
  {carry_html}
</section>

<section>
  <h2>All Committed Issues</h2>
  <table class="tbl"><thead><tr>
    <th>Key</th><th>Type</th><th>Assignee</th><th>Status</th><th>Flags</th><th>Summary</th>
  </tr></thead><tbody>{issue_rows}</tbody></table>
</section>

<div class="foot">Generated {generated} · live from Jira · next sprint planning view</div>

</body></html>"""


def bucket_color(status_name):
    b = bucket(status_name)
    return {"done": "#22c55e", "inprogress": "#3b82f6", "todo": "#94a3b8"}[b]


def esc(s):
    return (str(s)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


if __name__ == "__main__":
    main()
