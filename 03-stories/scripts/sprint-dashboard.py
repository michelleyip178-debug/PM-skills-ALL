#!/usr/bin/env python3
"""
Generate a self-contained HTML sprint dashboard from live Jira data.
Appends a daily snapshot to a CSV for burndown tracking.

Usage:
    python3 sprint-dashboard.py                       # Pathfinder board (12541)
    JIRA_BOARD_ID=13640 python3 sprint-dashboard.py   # Core board
    python3 sprint-dashboard.py --sprint 34617        # specific sprint id
    python3 sprint-dashboard.py --out ~/dash.html

Reads JIRA_EMAIL / JIRA_API_TOKEN / JIRA_SITE from 03-stories/.env
Run with sandbox OFF — sgtechstack.atlassian.net needs direct network.
"""

import argparse
import base64
import csv
import json
import os
import sys
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # 03-stories/
DEFAULT_BOARD = os.environ.get("JIRA_BOARD_ID", "12541")
HUB = ROOT.parent / "00-hub"

DONE = {"done", "closed", "resolved"}
TODO = {"to do", "open", "backlog", "selected for development"}

STATUS_ORDER = ["To Do", "Open", "Selected for Development", "In Progress",
                "In Development", "In Review", "Code Review", "QA", "Done", "Closed"]


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


def update_burndown_csv(sprint_id, sprint_name, total, done_n, inprogress_n):
    """Append today's snapshot. One row per day — overwrites if same date."""
    csv_path = HUB / f"sprint-burndown-{sprint_id}.csv"
    today = datetime.now().strftime("%Y-%m-%d")
    rows = []
    if csv_path.exists():
        rows = list(csv.DictReader(csv_path.open()))
    # Remove any existing row for today (idempotent re-runs)
    rows = [r for r in rows if r.get("date") != today]
    rows.append({
        "date": today,
        "total": total,
        "done": done_n,
        "inprogress": inprogress_n,
        "remaining": total - done_n,
    })
    with csv_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "total", "done", "inprogress", "remaining"])
        w.writeheader()
        w.writerows(rows)
    return rows


def load_burndown(sprint_id):
    csv_path = HUB / f"sprint-burndown-{sprint_id}.csv"
    if not csv_path.exists():
        return []
    return list(csv.DictReader(csv_path.open()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--board", default=DEFAULT_BOARD)
    ap.add_argument("--sprint", default=None, help="sprint id (default: active sprint)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    env = load_env()
    site = env["JIRA_SITE"]
    auth = f"{env['JIRA_EMAIL']}:{env['JIRA_API_TOKEN']}"
    base = f"https://{site}"

    if args.sprint:
        sprint = jget(f"{base}/rest/agile/1.0/sprint/{args.sprint}", auth)
    else:
        data = jget(f"{base}/rest/agile/1.0/board/{args.board}/sprint?state=active", auth)
        vals = data.get("values", [])
        if not vals:
            sys.exit(f"No active sprint on board {args.board}")
        sprint = vals[0]

    sid = sprint["id"]
    sname = sprint["name"]
    goal = sprint.get("goal") or ""
    start = (sprint.get("startDate") or "")[:10]
    end = (sprint.get("endDate") or "")[:10]

    # Pull all issues (paginate)
    issues = []
    start_at = 0
    while True:
        page = jget(
            f"{base}/rest/agile/1.0/sprint/{sid}/issue"
            f"?fields=summary,status,assignee,issuetype,priority,customfield_10016,labels"
            f"&maxResults=100&startAt={start_at}", auth)
        issues.extend(page.get("issues", []))
        if start_at + page.get("maxResults", 100) >= page.get("total", 0):
            break
        start_at += page.get("maxResults", 100)

    rows = []
    status_counts = Counter()
    bucket_counts = Counter()
    assignee_load = defaultdict(lambda: {"count": 0, "points": 0.0, "done": 0})
    type_counts = Counter()
    total_points = 0.0
    done_points = 0.0
    blockers = []

    for i in issues:
        f = i["fields"]
        key = i["key"]
        st = f["status"]["name"]
        a = (f.get("assignee") or {}).get("displayName") or "Unassigned"
        t = f["issuetype"]["name"]
        pr = (f.get("priority") or {}).get("name") or ""
        pts = f.get("customfield_10016") or 0
        try:
            pts = float(pts)
        except (TypeError, ValueError):
            pts = 0.0
        labels = f.get("labels") or []
        b = bucket(st)

        status_counts[st] += 1
        bucket_counts[b] += 1
        type_counts[t] += 1
        total_points += pts
        if b == "done":
            done_points += pts
        assignee_load[a]["count"] += 1
        assignee_load[a]["points"] += pts
        if b == "done":
            assignee_load[a]["done"] += 1

        is_blocked = pr.lower() in ("highest", "blocker") or any(
            "block" in lb.lower() for lb in labels)
        if is_blocked and b != "done":
            blockers.append((key, st, a, pr or "—", f["summary"]))

        rows.append({
            "key": key, "status": st, "bucket": b, "assignee": a,
            "type": t, "priority": pr or "—", "points": pts, "summary": f["summary"],
        })

    total = len(rows)
    done_n = bucket_counts["done"]
    pct = round(100 * done_n / total) if total else 0
    pts_pct = round(100 * done_points / total_points) if total_points else 0

    # Day progress
    day_str = ""
    time_pct = 0
    total_days = 0
    try:
        sd = datetime.fromisoformat(start)
        ed = datetime.fromisoformat(end)
        today_dt = datetime.now(timezone.utc).replace(tzinfo=None)
        total_days = (ed - sd).days or 1
        elapsed = max(0, min(total_days, (today_dt - sd).days))
        day_str = f"Day {elapsed}/{total_days}"
        time_pct = round(100 * elapsed / total_days)
    except Exception:
        pass

    # Burndown: append today's snapshot, then load full history
    history = update_burndown_csv(sid, sname, total, done_n, bucket_counts["inprogress"])

    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    html = build_html(
        sname, goal, start, end, day_str, time_pct, total_days,
        total, done_n, pct, total_points, done_points, pts_pct,
        status_counts, bucket_counts, assignee_load,
        type_counts, blockers, rows, history, generated,
    )

    out = args.out or str(HUB / "sprint-dashboard.html")
    Path(out).write_text(html, encoding="utf-8")
    print(f"✓ {sname}: {total} issues, {done_n} done ({pct}%)")
    print(f"  {len(blockers)} blocker(s) · {len(history)} burndown snapshots")
    print(f"  → {out}")


def build_html(sname, goal, start, end, day_str, time_pct, total_days,
               total, done_n, pct, total_points, done_points, pts_pct,
               status_counts, bucket_counts, assignee_load,
               type_counts, blockers, rows, history, generated):

    def status_color(st):
        b = bucket(st)
        return {"done": "#22c55e", "inprogress": "#3b82f6", "todo": "#94a3b8"}[b]

    # Status bar segments
    status_bars = ""
    for st in sorted(status_counts, key=lambda s: STATUS_ORDER.index(s) if s in STATUS_ORDER else 99):
        n = status_counts[st]
        w = 100 * n / total if total else 0
        status_bars += (f'<div class="seg" style="width:{w:.1f}%;background:{status_color(st)}"'
                        f' title="{st}: {n}">{n if w > 6 else ""}</div>')

    status_legend = "".join(
        f'<span class="lg"><i style="background:{status_color(st)}"></i>{st} ({status_counts[st]})</span>'
        for st in sorted(status_counts, key=lambda s: STATUS_ORDER.index(s) if s in STATUS_ORDER else 99))

    # Assignee rows
    asg = sorted(assignee_load.items(), key=lambda kv: -kv[1]["count"])
    max_count = max((v["count"] for _, v in asg), default=1)
    asg_rows = ""
    for name, v in asg:
        w = 100 * v["count"] / max_count
        donew = 100 * v["done"] / v["count"] if v["count"] else 0
        asg_rows += (f'<tr><td class="nm">{esc(name)}</td>'
                     f'<td class="bar"><div class="track">'
                     f'<div class="fill" style="width:{w:.0f}%">'
                     f'<div class="filldone" style="width:{donew:.0f}%"></div>'
                     f'</div></div></td>'
                     f'<td class="num">{v["count"]}</td>'
                     f'<td class="num">{v["done"]}</td></tr>')

    # Type chips
    type_chips = "".join(
        f'<span class="chip">{esc(t)} <b>{n}</b></span>'
        for t, n in type_counts.most_common())

    # Blockers
    if blockers:
        blk = "".join(
            f'<tr><td class="k">{esc(k)}</td><td>{esc(st)}</td>'
            f'<td>{esc(a)}</td><td>{esc(pr)}</td><td>{esc(sm)}</td></tr>'
            for k, st, a, pr, sm in blockers)
        blockers_html = (f'<table class="tbl"><thead><tr>'
                         f'<th>Key</th><th>Status</th><th>Assignee</th>'
                         f'<th>Priority</th><th>Summary</th>'
                         f'</tr></thead><tbody>{blk}</tbody></table>')
    else:
        blockers_html = '<p class="ok">No flagged blockers. 🎉</p>'

    # All-issues table
    issue_rows = ""
    for r in sorted(rows, key=lambda r: (r["bucket"] != "inprogress", r["bucket"] == "done", r["key"])):
        issue_rows += (f'<tr data-b="{r["bucket"]}">'
                       f'<td class="k">{esc(r["key"])}</td>'
                       f'<td><span class="dot" style="background:{status_color(r["status"])}"></span>'
                       f'{esc(r["status"])}</td>'
                       f'<td>{esc(r["type"])}</td>'
                       f'<td>{esc(r["assignee"])}</td>'
                       f'<td>{esc(r["summary"])}</td></tr>')

    goal_html = f'<p class="goal">🎯 {esc(goal)}</p>' if goal else ""

    # Pace card
    diff = pct - time_pct
    if total_points > 0:
        second_card = (f'<div class="card"><h2>Points Done</h2>'
                       f'<div class="big">{pts_pct}%'
                       f'<small> · {done_points:.0f}/{total_points:.0f}</small></div></div>')
    else:
        if diff >= 5:
            pace, pcolor = "ahead", "#22c55e"
        elif diff <= -5:
            pace, pcolor = "behind", "#ef4444"
        else:
            pace, pcolor = "on track", "#3b82f6"
        sign = "+" if diff > 0 else ""
        second_card = (f'<div class="card"><h2>Pace</h2>'
                       f'<div class="big" style="color:{pcolor}">{pace}'
                       f'<small> · {sign}{diff}pt vs time</small></div></div>')

    # Burndown chart data
    burndown_json = json.dumps([
        {"date": r["date"], "done": int(r["done"]), "remaining": int(r["remaining"]), "total": int(r["total"])}
        for r in history
    ])

    # Ideal line: from (sprint_start, total) to (sprint_end, 0)
    # Both endpoints embedded for JS to draw
    burndown_section = build_burndown_section(history, start, end, total_days, total)

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(sname)} — Sprint Dashboard</title>
<style>
  :root{{--bg:#0f172a;--card:#1e293b;--mut:#94a3b8;--fg:#e2e8f0;--line:#334155;}}
  *{{box-sizing:border-box}}
  body{{margin:0;font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
    background:var(--bg);color:var(--fg);padding:24px;max-width:1100px;margin:0 auto}}
  h1{{font-size:22px;margin:0 0 2px}}
  .sub{{color:var(--mut);font-size:13px}}
  .goal{{color:#fbbf24;margin:8px 0 0;font-size:14px}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;margin:20px 0}}
  .card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px}}
  .card h2{{font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut);margin:0 0 10px}}
  .big{{font-size:30px;font-weight:700}}
  .big small{{font-size:14px;color:var(--mut);font-weight:400}}
  .progbar{{height:22px;border-radius:6px;overflow:hidden;display:flex;background:#0b1220}}
  .seg{{display:flex;align-items:center;justify-content:center;font-size:11px;color:#fff;min-width:2px}}
  .legend{{display:flex;flex-wrap:wrap;gap:10px 16px;margin-top:12px;font-size:12px;color:var(--mut)}}
  .lg i{{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:5px;vertical-align:middle}}
  .track{{background:#0b1220;border-radius:5px;height:16px;overflow:hidden}}
  .fill{{background:#3b82f6;height:100%;border-radius:5px;position:relative}}
  .filldone{{background:#22c55e;height:100%;position:absolute;left:0;top:0;border-radius:5px}}
  table{{width:100%;border-collapse:collapse}}
  .atbl td{{padding:6px 8px;vertical-align:middle}}
  .atbl .nm{{width:160px;color:var(--fg)}}
  .atbl .bar{{width:auto}}
  .atbl .num{{text-align:right;width:50px;color:var(--mut);font-variant-numeric:tabular-nums}}
  .atbl thead th{{font-size:11px;text-transform:uppercase;color:var(--mut);text-align:right;padding:4px 8px}}
  .atbl thead th:first-child,.atbl thead th:nth-child(2){{text-align:left}}
  .chip{{display:inline-block;background:#0b1220;border:1px solid var(--line);border-radius:999px;
    padding:4px 12px;margin:0 6px 6px 0;font-size:13px}}
  .chip b{{color:#60a5fa}}
  .tbl{{font-size:13px;margin-top:6px}}
  .tbl th{{text-align:left;font-size:11px;text-transform:uppercase;color:var(--mut);
    border-bottom:1px solid var(--line);padding:6px 8px}}
  .tbl td{{padding:6px 8px;border-bottom:1px solid #243044}}
  .k{{font-family:ui-monospace,monospace;color:#60a5fa;white-space:nowrap}}
  .dot{{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px}}
  .ok{{color:#22c55e}}
  section{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;margin:16px 0}}
  section h2{{font-size:14px;margin:0 0 14px}}
  .filters{{margin-bottom:10px}}
  .filters button{{background:#0b1220;color:var(--fg);border:1px solid var(--line);
    border-radius:6px;padding:5px 12px;margin-right:6px;cursor:pointer;font-size:12px}}
  .filters button.on{{background:#3b82f6;border-color:#3b82f6}}
  canvas{{display:block;width:100%;border-radius:6px}}
  .chart-wrap{{position:relative;height:220px}}
  .chart-legend{{display:flex;gap:16px;margin-top:10px;font-size:12px;color:var(--mut)}}
  .chart-legend span{{display:flex;align-items:center;gap:6px}}
  .chart-legend i{{display:inline-block;width:24px;height:3px;border-radius:2px}}
  .foot{{color:var(--mut);font-size:12px;margin-top:24px;text-align:center}}
</style></head><body>

<header>
  <h1>{esc(sname)}</h1>
  <div class="sub">{start} → {end} · {day_str} · {total} issues</div>
  {goal_html}
</header>

<div class="grid">
  <div class="card"><h2>Issues Done</h2>
    <div class="big">{pct}%<small> · {done_n}/{total}</small></div></div>
  {second_card}
  <div class="card"><h2>In Progress</h2>
    <div class="big">{bucket_counts['inprogress']}<small> issues</small></div></div>
  <div class="card"><h2>Time Elapsed</h2>
    <div class="big">{time_pct}%<small> of sprint</small></div></div>
</div>

{burndown_section}

<section>
  <h2>Status Breakdown</h2>
  <div class="progbar">{status_bars}</div>
  <div class="legend">{status_legend}</div>
</section>

<section>
  <h2>Workload by Assignee <span class="sub" style="font-size:12px">(blue = total · green = done)</span></h2>
  <table class="atbl"><thead><tr>
    <th>Assignee</th><th></th><th>Issues</th><th>Done</th>
  </tr></thead><tbody>{asg_rows}</tbody></table>
</section>

<section><h2>Issue Types</h2>{type_chips}</section>

<section><h2>Blockers &amp; High Priority ({len(blockers)})</h2>{blockers_html}</section>

<section>
  <h2>All Issues</h2>
  <div class="filters">
    <button class="on" data-f="all">All ({total})</button>
    <button data-f="inprogress">In Progress ({bucket_counts['inprogress']})</button>
    <button data-f="todo">To Do ({bucket_counts['todo']})</button>
    <button data-f="done">Done ({bucket_counts['done']})</button>
  </div>
  <table class="tbl"><thead><tr>
    <th>Key</th><th>Status</th><th>Type</th><th>Assignee</th><th>Summary</th>
  </tr></thead><tbody id="issues">{issue_rows}</tbody></table>
</section>

<div class="foot">Generated {generated} · live from Jira · {len(history)} burndown snapshot(s)</div>

<script>
const HISTORY = {burndown_json};
const SPRINT_START = "{start}";
const SPRINT_END = "{end}";
const TOTAL_DAYS = {total_days};

// Filter buttons
document.querySelectorAll('.filters button').forEach(b => b.onclick = () => {{
  document.querySelectorAll('.filters button').forEach(x => x.classList.remove('on'));
  b.classList.add('on');
  const f = b.dataset.f;
  document.querySelectorAll('#issues tr').forEach(tr => {{
    tr.style.display = (f === 'all' || tr.dataset.b === f) ? '' : 'none';
  }});
}});

// Burndown chart (vanilla canvas — no CDN needed)
(function() {{
  const canvas = document.getElementById('burndown-canvas');
  if (!canvas || !HISTORY.length) return;
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const wrap = canvas.parentElement;
  const W = wrap.clientWidth || 800;
  const H = 220;
  canvas.width = W * dpr;
  canvas.height = H * dpr;
  canvas.style.width = W + 'px';
  canvas.style.height = H + 'px';
  ctx.scale(dpr, dpr);

  const PAD = {{top: 16, right: 16, bottom: 36, left: 44}};
  const cw = W - PAD.left - PAD.right;
  const ch = H - PAD.top - PAD.bottom;

  // Data range
  const maxIssues = Math.max(...HISTORY.map(d => d.total), 1);
  const allDates = HISTORY.map(d => d.date);

  // Build full date axis from sprint start → end
  function addDays(dateStr, n) {{
    const d = new Date(dateStr);
    d.setDate(d.getDate() + n);
    return d.toISOString().slice(0, 10);
  }}
  const axis = [];
  for (let i = 0; i <= TOTAL_DAYS; i++) axis.push(addDays(SPRINT_START, i));

  function xOf(dateStr) {{
    const idx = axis.indexOf(dateStr);
    if (idx < 0) return null;
    return PAD.left + (idx / (axis.length - 1)) * cw;
  }}
  function yOf(val) {{
    return PAD.top + ch - (val / maxIssues) * ch;
  }}

  // Grid
  ctx.strokeStyle = '#1e3050';
  ctx.lineWidth = 1;
  const yTicks = 5;
  for (let i = 0; i <= yTicks; i++) {{
    const v = Math.round((maxIssues / yTicks) * i);
    const y = yOf(v);
    ctx.beginPath(); ctx.moveTo(PAD.left, y); ctx.lineTo(PAD.left + cw, y); ctx.stroke();
    ctx.fillStyle = '#64748b';
    ctx.font = '11px system-ui';
    ctx.textAlign = 'right';
    ctx.fillText(v, PAD.left - 6, y + 4);
  }}

  // X axis date labels (show every 2nd day or so)
  ctx.fillStyle = '#64748b';
  ctx.font = '10px system-ui';
  ctx.textAlign = 'center';
  const step = Math.max(1, Math.ceil(axis.length / 8));
  axis.forEach((d, i) => {{
    if (i % step !== 0 && i !== axis.length - 1) return;
    const x = PAD.left + (i / (axis.length - 1)) * cw;
    ctx.fillText(d.slice(5), x, H - 8);  // MM-DD
  }});

  // Ideal burndown line (total → 0, start → end)
  const idealTotal = HISTORY[0]?.total || maxIssues;
  ctx.setLineDash([6, 4]);
  ctx.strokeStyle = '#475569';
  ctx.lineWidth = 1.5;
  ctx.beginPath();
  ctx.moveTo(PAD.left, yOf(idealTotal));
  ctx.lineTo(PAD.left + cw, yOf(0));
  ctx.stroke();
  ctx.setLineDash([]);

  // Done line (green)
  ctx.strokeStyle = '#22c55e';
  ctx.lineWidth = 2.5;
  ctx.beginPath();
  let first = true;
  HISTORY.forEach(d => {{
    const x = xOf(d.date);
    if (x === null) return;
    const y = yOf(d.done);
    if (first) {{ ctx.moveTo(x, y); first = false; }} else ctx.lineTo(x, y);
  }});
  ctx.stroke();

  // Remaining line (blue)
  ctx.strokeStyle = '#3b82f6';
  ctx.lineWidth = 2.5;
  ctx.beginPath();
  first = true;
  HISTORY.forEach(d => {{
    const x = xOf(d.date);
    if (x === null) return;
    const y = yOf(d.remaining);
    if (first) {{ ctx.moveTo(x, y); first = false; }} else ctx.lineTo(x, y);
  }});
  ctx.stroke();

  // Dots
  HISTORY.forEach(d => {{
    const x = xOf(d.date);
    if (x === null) return;
    [[d.done, '#22c55e'], [d.remaining, '#3b82f6']].forEach(([v, c]) => {{
      ctx.beginPath();
      ctx.arc(x, yOf(v), 3.5, 0, Math.PI * 2);
      ctx.fillStyle = c;
      ctx.fill();
    }});
  }});
}})();
</script>
</body></html>"""


def build_burndown_section(history, start, end, total_days, total):
    if not history:
        note = ('<p style="color:var(--mut);font-size:13px">'
                'No history yet. Run the script daily to build the burndown.</p>')
        return (f'<section><h2>Burndown</h2>{note}</section>')

    return """<section>
  <h2>Burndown</h2>
  <div class="chart-wrap"><canvas id="burndown-canvas"></canvas></div>
  <div class="chart-legend">
    <span><i style="background:#22c55e"></i>Done</span>
    <span><i style="background:#3b82f6"></i>Remaining</span>
    <span><i style="background:#475569;opacity:.7"></i>Ideal</span>
  </div>
</section>"""


def esc(s):
    return (str(s)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


if __name__ == "__main__":
    main()
