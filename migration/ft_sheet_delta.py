"""List the FT Pipeline sheet edits made after the 5 Oct export, and where each one stands in Notion today.

Usage:
  python migration/ft_sheet_delta.py                 diff the two exports, write the review CSV and the Notion lookup list
  python migration/ft_sheet_delta.py --notion FILE   same, then fill the Notion columns from a saved query result (JSON list of rows)

Reads (all git-ignored, never modified):
  data/raw/sheets/ft_pipeline.xlsx                   the 5 Oct ~07:12 UTC export that migration/ft_pipeline.py migrated
  data/raw/sheets/ft_pipeline_2026-10-06.xlsx        the 6 Oct re-export, after Mamatha's later edits
  data/out/ft_pipeline/{engagements_new,engagements_update,skipped}.json   what the 5 Oct run wrote, per sheet row
  FILE (optional)                                    Engagements rows: url, Source ID, Status, date:Next date:start,
                                                     Next action, date:Claude updated:start
Writes:
  data/review/ft_sheet_delta.csv                     one line per changed field, plus added and removed rows
  data/out/ft_pipeline/delta_lookup.json             Source IDs and page URLs to query in Notion

Rows are matched across the exports by tab + normalised guest name cell (n-th occurrence to n-th occurrence), never by row
number, because rows moved. Fields compared are the ones ft_pipeline.py reads for Status, Next date and Next action, plus
the eval cell and the tier parsed from it. Text cells are redacted (emails, phone numbers) with ft_pipeline.redact.
Each changed row is tied to the engagement the 5 Oct run wrote for it: a new engagement keyed by its group's primary
row ("FT Pipeline/<tab>/<row>"), or an existing engagement it updated or was skipped against.
"""
import argparse
import collections
import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ft_pipeline import (clean, map_row, parse_cold, parse_eval, parse_inbound, parse_p1, parse_paid, read_tab,  # noqa: E402
                         redact)
from paas import fold, page_url  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OLD = ROOT / "data/raw/sheets/ft_pipeline.xlsx"
NEW = ROOT / "data/raw/sheets/ft_pipeline_2026-10-06.xlsx"
OUT = ROOT / "data/out/ft_pipeline"
CSV_OUT = ROOT / "data/review/ft_sheet_delta.csv"
LOOKUP = OUT / "delta_lookup.json"
PARSERS = {"Inbound": parse_inbound, "P1": parse_p1, "Paid": parse_paid, "FT Cold Lead": parse_cold}

# (field, column index, header as written) per tab; these are the columns ft_pipeline.py reads for each Notion field
FIELDS = {
    "Inbound": [("status", 1, "Status"), ("next_action", 3, "Column 4"), ("next_action", 4, "Next action - AD"),
                ("next_date", 5, "FU/ Rec Date"), ("eval", 6, "Dossier/ guest eval")],
    "P1": [("status", 1, "Status"), ("eval", 2, "Verdict"), ("next_action", 4, "Next Action - mamatha"),
           ("next_action", 5, "Next action - AD"), ("next_action", 6, "Name dropping"), ("next_date", 7, "Dates"),
           ("eval", 8, "Column 1")],
    "Paid": [("next_action", 3, "Comment"), ("next_date", 4, "Nxt FU Date"), ("status", 5, "GST Details recvd"),
             ("status", 6, "Invoice Sent"), ("status", 7, "First payment Made"), ("status", 8, "Planning Call Done"),
             ("status", 9, "Recording Scheduled"), ("status", 10, "Final Payment Made"), ("status", 11, "Released")],
    "FT Cold Lead": [("status", 2, "Status"), ("next_action", 6, "Status (2nd)")],
}
EVAL_COLS = {"Inbound": [6], "P1": [2, 8], "Paid": [], "FT Cold Lead": []}
COLUMNS = ["tab", "old_row", "new_row", "guest_name", "field", "column", "old_value", "new_value",
           "mapped_status_5oct", "mapped_status_now", "engagement_id", "engagement_source", "notion_status",
           "notion_next_date", "notion_next_action", "claude_updated", "touched_in_notion"]


def cell_text(v, link=None):
    if isinstance(v, (dt.datetime, dt.date)):
        v = v.date() if isinstance(v, dt.datetime) else v
        s = v.isoformat()
    else:
        s = redact(clean(v)) if v is not None else ""
    if link and link not in s:
        s = f"{s} <{link}>".strip()
    return s


def name_cell(tab, r):
    c = r["cells"]
    raw = f"{clean(c[0])} {clean(c[1])}" if tab == "FT Cold Lead" else clean(c[0])
    return redact(raw)


def load(path):
    wb = openpyxl.load_workbook(path)
    out = {}
    for tab, fn in PARSERS.items():
        rows = []
        for r in read_tab(wb, tab):
            p = fn(r)
            p["key"] = fold(name_cell(tab, r))
            rows.append(p)
        out[tab] = rows
    return out


def pair(old_rows, new_rows):
    """Match by normalised name cell, n-th occurrence to n-th occurrence. Returns (pairs, removed, added)."""
    by_new = collections.defaultdict(list)
    for r in new_rows:
        by_new[r["key"]].append(r)
    pairs, removed = [], []
    for r in old_rows:
        bucket = by_new.get(r["key"])
        if bucket:
            pairs.append((r, bucket.pop(0)))
        else:
            removed.append(r)
    added = [r for b in by_new.values() for r in b]
    # second pass for edited name cells ('A @ X' -> 'A and B @ X', or a proposed alternative at the same firm):
    # same first guest, or same company and same Via as written
    def same(a, b):
        if a["people"] and b["people"] and fold(a["people"][0]) == fold(b["people"][0]):
            return True
        ca, cb = fold(a.get("company")), fold(b.get("company"))
        return bool(ca and cb and (ca in cb or cb in ca) and a.get("via_raw") and fold(a["via_raw"]) == fold(b.get("via_raw")))
    still_removed = []
    for r in removed:
        hit = next((a for a in added if same(r, a)), None)
        if hit:
            added.remove(hit)
            pairs.append((r, hit))
        else:
            still_removed.append(r)
    return pairs, still_removed, sorted(added, key=lambda r: r["row"])


def tier_of(tab, r):
    for i in EVAL_COLS[tab]:
        t = parse_eval(r["cells"][i], r["links"][i])[1] if i < len(r["cells"]) else None
        if t:
            return t
    return ""


def diff(tab, o, n):
    out = []
    if o["key"] != n["key"]:
        out.append(("name", "guest name cell", name_cell(tab, o), name_cell(tab, n)))
    for field, i, header in FIELDS[tab]:
        ov = cell_text(o["cells"][i] if i < len(o["cells"]) else None, o["links"][i] if field == "eval" and i < len(o["links"]) else None)
        nv = cell_text(n["cells"][i] if i < len(n["cells"]) else None, n["links"][i] if field == "eval" and i < len(n["links"]) else None)
        if ov != nv:
            out.append((field, header, ov, nv))
    if EVAL_COLS[tab]:
        ot, nt = tier_of(tab, o), tier_of(tab, n)
        if ot != nt:
            out.append(("tier", "parsed from eval", ot, nt))
    return out


def written_by_row():
    """sheet row 'tab/row' -> (engagement key, kind, what the 5 Oct run set: Status, Next date, Next action)."""
    m = {}
    for e in json.load(open(OUT / "engagements_new.json")):
        p = e["props"]
        for r in e["rows"]:
            m[r] = (e["key"], "new", p.get("Status"), p.get("date:Next date:start"), p.get("Next action"))
    for u in json.load(open(OUT / "engagements_update.json")):
        p = u["props"]
        for r in u["source"]:
            if "/" in r and not r.startswith("Part A"):
                m.setdefault(r, (page_url(u["page"]), "updated", p.get("Status"), p.get("date:Next date:start"), p.get("Next action")))
    for s in json.load(open(OUT / "skipped.json")):
        for r in s["source"]:
            m.setdefault(r, (page_url(s["engagement"]), "skipped", s.get("existing"), None, None))
    return m


def load_notion(path):
    rows = json.load(open(path))
    by = {}
    for r in rows:
        if r.get("Source ID"):
            by[r["Source ID"]] = r
        if r.get("url"):
            by[page_url(r["url"])] = r
    return by


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--notion", metavar="FILE")
    args = ap.parse_args()
    old, new = load(OLD), load(NEW)
    written = written_by_row()
    notion = load_notion(args.notion) if args.notion else {}
    lines, keys = [], set()
    counts = collections.Counter()
    changed_rows = collections.Counter()
    touched = {}
    for tab in PARSERS:
        pairs, removed, added = pair(old[tab], new[tab])
        print(f"{tab}: old {len(old[tab])}, new {len(new[tab])}, matched {len(pairs)}, removed {len(removed)}, added {len(added)}")
        counts[(tab, "added")] += len(added)
        counts[(tab, "removed")] += len(removed)
        for o, n in pairs:
            d = diff(tab, o, n)
            if not d:
                continue
            changed_rows[tab] += 1
            src = f"{tab}/{o['row']}"
            key, kind, w_status, w_date, w_action = written.get(src, (f"FT Pipeline/{tab}/{o['row']}", "fallback", None, None, None))
            keys.add((key, kind))
            nrow = notion.get(key, {})
            n_status, n_date, n_action = nrow.get("Status") or "", nrow.get("date:Next date:start") or "", nrow.get("Next action") or ""
            c_upd = nrow.get("date:Claude updated:start") or ""
            if nrow:
                differs = (n_status != (w_status or "")) or (kind != "skipped" and (n_date[:10] != (w_date or "")[:10]
                                                                                    or n_action != (w_action or "")))
                t = "yes" if c_upd or differs else "no"
            else:
                t = "not found" if args.notion else ""
            touched[(tab, o["row"])] = t
            ms_old, ms_new = map_row(o)["Status"], map_row(n)["Status"]
            for field, header, ov, nv in d:
                counts[(tab, field)] += 1
                lines.append({"tab": tab, "old_row": o["row"], "new_row": n["row"], "guest_name": name_cell(tab, n)[:80],
                              "field": field, "column": header, "old_value": ov[:300], "new_value": nv[:300],
                              "mapped_status_5oct": ms_old, "mapped_status_now": ms_new,
                              "engagement_id": (nrow.get("url") and page_url(nrow["url"])) or key, "engagement_source": kind,
                              "notion_status": n_status, "notion_next_date": n_date, "notion_next_action": redact(n_action)[:200],
                              "claude_updated": c_upd, "touched_in_notion": t})
        for r, label in [(r, "row removed") for r in removed] + [(r, "row added") for r in added]:
            is_old = label == "row removed"
            st = cell_text(r["cells"][FIELDS[tab][0][1]]) if tab != "Paid" else ""
            lines.append({"tab": tab, "old_row": r["row"] if is_old else "", "new_row": "" if is_old else r["row"],
                          "guest_name": name_cell(tab, r)[:80], "field": label, "column": "",
                          "old_value": st if is_old else "", "new_value": "" if is_old else st,
                          "mapped_status_5oct": map_row(r)["Status"] if is_old else "",
                          "mapped_status_now": "" if is_old else map_row(r)["Status"],
                          **{k: "" for k in COLUMNS[10:]}})
            if is_old:
                src = f"{tab}/{r['row']}"
                key, kind = written.get(src, (f"FT Pipeline/{tab}/{r['row']}", "fallback"))[:2]
                lines[-1]["engagement_id"], lines[-1]["engagement_source"] = key, kind
    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(CSV_OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(lines)
    OUT.mkdir(parents=True, exist_ok=True)
    json.dump({"source_ids": sorted(k for k, kind in keys if not k.startswith("https://")),
               "page_urls": sorted(k for k, kind in keys if k.startswith("https://"))}, open(LOOKUP, "w"), indent=1)
    print("changed rows per tab:", dict(changed_rows), "total", sum(changed_rows.values()))
    print("changes by tab and field:", {f"{t}/{f}": c for (t, f), c in sorted(counts.items())})
    if args.notion:
        print("touched in Notion since 5 Oct:", collections.Counter(touched.values()))
    print(f"wrote {len(lines)} lines to {CSV_OUT.relative_to(ROOT)}; lookup keys {len(keys)}")


if __name__ == "__main__":
    main()
