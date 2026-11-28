#!/usr/bin/env python3
"""
Parse a social engagement export into the DASH JSON the template expects.

This is a STARTING TOOLKIT, not a black box. Inputs vary a lot (Google Sheets
HTML exports, CSV, pasted tables), so read your actual file first and adapt the
row-filtering rules. The compute() and build_dash() helpers are stable; the
parsing helpers are the part you usually tweak.

Golden rules (do not skip):
- Keep only rows that have a post URL AND at least one numeric metric.
- Drop header rows, "Week of ..." rows, "Total weekly" / "Total monthly" rows.
- Split merged rows (two records concatenated) — detect by 2 URLs in one row.
- Compute EVERYTHING from row-level data. If the sheet's own printed totals
  disagree, trust the computed numbers and tell the user about the gap.
"""
import re, json, statistics, sys
from datetime import datetime

# ---------- helpers ----------
def to_int(x):
    if x is None: return None
    x = str(x).strip().replace(",", "")
    return int(x) if re.fullmatch(r"-?\d+", x) else None

def iso_week_label(datestr):
    """Fallback weekly bucket from a date, when no 'Week of' headers exist."""
    for f in ("%Y-%m-%d","%d/%m/%Y","%m/%d/%Y","%b %d, %Y","%d %b %Y","%b %d"):
        try:
            d = datetime.strptime(datestr.strip(), f)
            if d.year == 1900: d = d.replace(year=datetime.now().year)
            monday = d.fromisocalendar(d.isocalendar()[0], d.isocalendar()[1], 1)
            return monday.strftime("%b %-d")
        except Exception:
            continue
    return None

# ---------- parse a Google Sheets HTML export ----------
def parse_gsheet_html(path, metric_cols):
    """
    metric_cols: ordered list of the metric keys as they appear left-to-right in
    the numeric columns (e.g. ["retweets","likes","views","total"]). The last one
    is normally the precomputed total; if there is none, pass the components and
    compute total in build_dash.
    Returns list of records: {date, values:{key:int}, link, week_label(optional)}
    """
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(open(path, encoding="utf-8").read(), "html.parser")
    records, cur_week = [], None
    for tr in soup.select("tbody tr"):
        cells = tr.find_all("td")
        vals = [c.get_text(strip=True) for c in cells]
        links = [a["href"] for c in cells for a in c.find_all("a") if a.get("href")]
        joined = " ".join(vals).lower()
        first = vals[0].strip() if vals else ""
        if first.lower().startswith("week of"):
            cur_week = first.replace("Week of ", "").strip(); continue
        if "total weekly" in joined or "weekly total" in joined or "total monthly" in joined:
            continue
        if not links:
            continue  # header / spacer / subtotal without a post link
        # pull the numeric run from the row (skip empty leading date cell)
        nums = [to_int(v) for v in vals if to_int(v) is not None]
        # split merged rows: 2 links usually means 2 records glued together
        groups = len(links)
        per = len(metric_cols)
        for gi, link in enumerate(links):
            chunk = nums[gi*per:(gi+1)*per] if groups > 1 else nums[:per]
            if len(chunk) < 1: continue
            values = {k: (chunk[i] if i < len(chunk) else 0) for i, k in enumerate(metric_cols)}
            records.append({"date": first if gi == 0 else "",
                            "values": values, "link": link, "week_label": cur_week})
    return records

# ---------- parse a CSV ----------
def parse_csv(path, col_map, link_col, date_col=None):
    """col_map: {metric_key: column_name}. link_col/date_col: column names."""
    import csv
    records = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            link = (row.get(link_col) or "").strip()
            if not link: continue
            values = {k: (to_int(row.get(c)) or 0) for k, c in col_map.items()}
            records.append({"date": (row.get(date_col) or "").strip() if date_col else "",
                            "values": values, "link": link, "week_label": None})
    return records

# ---------- compute one dataset ----------
def build_dataset(records, metric_keys, headline, ds_id, label, unit, unit_plural):
    # weekly buckets: prefer explicit week_label, else iso week from date
    weeks = {}
    order = []
    for r in records:
        wl = r.get("week_label") or (iso_week_label(r["date"]) if r["date"] else None) or "All"
        if wl not in weeks:
            weeks[wl] = {"label": wl, "count": 0, "values": {k: 0 for k in metric_keys}}
            order.append(wl)
        weeks[wl]["count"] += 1
        for k in metric_keys:
            weeks[wl]["values"][k] += r["values"].get(k, 0)
    weekly = [weeks[w] for w in order]

    totals = {"count": len(records)}
    for k in metric_keys:
        totals[k] = sum(r["values"].get(k, 0) for r in records)

    hv = [r["values"].get(headline, 0) for r in records]
    mean = round(statistics.mean(hv)) if hv else 0

    stars = sorted(records, key=lambda r: r["values"].get(headline, 0), reverse=True)[:5]
    stars = [{"date": s["date"], "link": s["link"], "values": s["values"]} for s in stars]

    return {"id": ds_id, "label": label, "unit": unit, "unitPlural": unit_plural,
            "weeks": weekly, "totals": totals, "mean": mean, "stars": stars}

# ---------- assemble full DASH object ----------
def build_dash(client, platform, metrics, headline, datasets, source="", eyebrow=None):
    """metrics: [{key,name,color}]. datasets: list of build_dataset() outputs."""
    return {"client": client, "platform": platform, "eyebrow": eyebrow,
            "headline": headline, "metrics": metrics, "datasets": datasets,
            "source": source}

def inject(template_path, dash, out_path, title):
    tpl = open(template_path, encoding="utf-8").read()
    tpl = tpl.replace("/*__DASH__*/", json.dumps(dash))
    tpl = tpl.replace("__TITLE__", title)
    open(out_path, "w", encoding="utf-8").write(tpl)
    print("wrote", out_path)

if __name__ == "__main__":
    print("Import these helpers and adapt per input. See SKILL.md for the flow.")
