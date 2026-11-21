"""Turn the un# guest sheet ("un# Pipeline") into one clean candidate list for Notion Engagements.

Usage:
  python migration/un_pipeline.py          parse, dedupe across tabs, map statuses, write candidates + review CSV

Reads (git-ignored):
  data/raw/sheets/un_pipeline.xlsx         export of Google Sheet 1QvWXTrGeLTtuExsFVZzvrbe8vWNdvw8kYT3MJybHm4g, 6 Oct 2026
Writes:
  data/out/un_pipeline/candidates.json     one record per guest, every source row it came from, mapped fields
  data/review/un_pipeline_review.csv       rows that could not be parsed or need a human call

Tabs used: Pipeline v2 (the live pipeline), Sponsored, Old Pipeline (both tables on it), YAP Clients and
Theprgenius Client (PR agency rosters), Defillama 49 Lead (outbound target list), CRM (contact details only).
Tabs not used: Podcast Leads and pod Campaign (Sri pitching himself to other podcasts, not guests), Post Release.

Status mapping follows docs/statuses.md and decision 66 (P2 and Maybe Later are timing, so LT chase). The writing
step (matching People and Engagements, creating rows) is done against live Notion and logged in
data/review/un_pipeline_written.csv. Never edits the raw file. Re-run safely.
"""
import collections
import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ft_pipeline import URL, as_date, clean, parse_eval, parse_name_cell, redact  # noqa: E402
from paas import EMAIL, fold, li_slug, li_url, name_key  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw/sheets/un_pipeline.xlsx"
OUT = ROOT / "data/out/un_pipeline"
REVIEW = ROOT / "data/review/un_pipeline_review.csv"
TODAY = dt.date(2026, 10, 6)
SRC = "un# Pipeline"

# Pipeline v2 Status -> (Status, Direction, Route)
V2_STATUS = {
    "recorded": ("Recorded", None, None),
    "unresponsive": ("Unresponsive", None, None),
    "uncontactable": ("Unresponsive", None, None),
    "declined": ("They declined", None, None),          # We declined when the note says Sri, Akshay or Ravi said no
    "p2": ("LT chase", None, None),
    "maybe later": ("LT chase", None, None),
    "lt chase": ("LT chase", None, None),
    "inbound": ("Decision pending", "Inbound", None),
    "approval pending": ("Decision pending", None, None),
    "sponsored": ("Sponsored offered", "Inbound", "Sponsored"),
    "to be scheduled": ("Booking", None, None),
    "scheduled": ("Booked", None, None),
    "chasing": ("Contacted", "Outbound", None),           # Precall requested when the note asks for a pre call
    "cold lead": ("New", "Outbound", None),               # Contacted when the note says mail sent
    "precall done": ("Precall done", None, None),
    "precall scheduled": ("Precall requested", None, None),
    "precall pending": ("Precall requested", None, None),
    "proposed alt": ("They declined", None, None),
}
OLD_STATUS = {
    "proposed/ chasing": ("Contacted", "Outbound"),
    "proposed/ interested": ("Interested", "Outbound"),
    "proposed/ unresponsive": ("Unresponsive", "Outbound"),
    "inbound": ("Decision pending", "Inbound"),
    "recorded": ("Recorded", None),
    "sri to connect": ("New", "Outbound"),
    "follow up needed": ("Contacted", "Outbound"),
    "declined": ("They declined", None),
}
SPONSORED_STATUS = {"inbound": "Sponsored offered", "declined": "They declined", "unresponsive": "Unresponsive"}
HOST = {"yes": "Yes", "no": "No", "ask": "Not asked"}
WE_DECLINED = re.compile(r"\b(sri|akshay|ravi)\b.*\b(not interested|declin|no\b)|declined by (sri|akshay|ravi)|not interested", re.I)
PRECALL = re.compile(r"pre[- ]?call|prelim", re.I)
MAIL_SENT = re.compile(r"mail sent|connected|reached out|dm sent", re.I)
LADDER = ["New", "Contacted", "Interested", "Decision pending", "Precall requested", "Precall done", "Sponsored offered",
          "Booking", "Booked", "Recorded", "Form filled"]
# Rows the generic name parser gets wrong, fixed by hand (source id -> people, company).
NAME_FIX = {
    "un# Pipeline/v2/21": (["Izzy Passadis"], "Lido Labs Foundation"),
    "un# Pipeline/v2/154": (["Marcos Viriato"], "Rayls / Parfin"),
    "un# Pipeline/v2/32": (["Matthias Wyss"], "Obligate"),
    "un# Pipeline/v2/34": (["Megan Knab"], "Franklin Templeton"),
    "un# Pipeline/v2/105": (["Rahul Rumalla"], "Safe Labs"),
    "un# Pipeline/v2/109": (["Konstantin Lomashuk"], "Lido & P2P.org"),
    "un# Pipeline/v2/110": (["Austin King"], "Omni Network"),
    "un# Pipeline/v2/112": (["Gavin Wood"], "Polkadot"),
    "un# Pipeline/v2/114": (["Paul Musson"], "Paddington Capital Management"),
    "un# Pipeline/v2/126": (["Arnaud Salomon"], None),
    "un# Pipeline/v2/129": (["Diego Baez"], "BLOX"),
    "un# Pipeline/v2/132": (["Himanshu Maradiya"], "CIFDAQ"),
    "un# Pipeline/v2/134": (["Ismael Hishon-Rezaizadeh"], "Lagrange Labs"),
    "un# Pipeline/v2/137": (["Nancy Beaton"], "Uphold"),
    "un# Pipeline/v2/138": (["Neil Mullins"], "Mojito"),
    "un# Pipeline/v2/142": (["Vakeesan Mahalingam"], "Torram"),
    "un# Pipeline/v2/143": (["Yemel Jardi"], "Decentraland"),
    "un# Pipeline/v2/153": (["Marc Boiron"], "Polygon Labs"),
    "un# Pipeline/v2/158": (["Olivier Dang"], "Kaiolabs"),
    "un# Pipeline/v2/167": (["Shawn Owen"], "SALT Lending"),
    "un# Pipeline/v2/171": (["Cooper Scanlon"], "Movement"),
    "un# Pipeline/v2/182": (["Iris"], "ahacreatorslaunch.info"),
    "un# Pipeline/v2/184": (["Ceres"], "rwaoutreach.com"),
    "un# Pipeline/sponsored/17": (["Andrea Muttoni"], "Story"),
    "un# Pipeline/old/15": (["Avinash Shekhar"], "Pi42"),
}
TAB_RANK = {"v2": 0, "sponsored": 1, "old": 2, "yap": 3, "prgenius": 3, "defillama": 4}


def cell(r, i):
    return r[i] if i < len(r) else None


def val(r, i):
    c = cell(r, i)
    return clean(c.value) if c is not None and c.value is not None else ""


def link(r, i):
    c = cell(r, i)
    if c is None:
        return None
    if c.hyperlink and c.hyperlink.target:
        return c.hyperlink.target
    m = URL.search(str(c.value or ""))
    return m.group(0) if m else None


def eval_bits(r, i):
    """Verdict, eval link and dossier link from one eval/dossier cell."""
    text = val(r, i)
    if not text and not link(r, i):
        return None, None, None
    verdict, _tier, ev, dos, _title, _mixed = parse_eval(text, link(r, i))
    if not (ev or dos) and re.match(r"^(dossier|guest dossier)", text, re.I):
        return verdict, None, None
    return verdict, ev, dos


def new_row(tab, rownum, raw_name, li):
    people, company, slug, note = parse_name_cell(raw_name, li)
    fix = NAME_FIX.get(f"{SRC}/{tab}/{rownum}")
    if fix:
        people, company, note = fix[0], fix[1], None
    return {"tab": tab, "source_id": f"{SRC}/{tab}/{rownum}", "raw_name": clean(raw_name), "people": people,
            "company": company, "li_slug": slug, "li_url": li_url(li) if slug else None, "parse_note": note,
            "status": None, "direction": None, "route": None, "eval_verdict": None, "eval_link": None,
            "dossier_link": None, "host_verdict": None, "next_date": None, "next_action": None, "via_name": None,
            "via_agency": None, "notes": []}


def read_v2(wb):
    ws = wb["Pipeline v2"]
    out = []
    for i, r in enumerate(ws.iter_rows(min_row=2), start=2):
        if not val(r, 0):
            continue
        x = new_row("v2", i, val(r, 0), link(r, 0))
        raw = val(r, 1).lower()
        status, direction, route = V2_STATUS.get(raw, (None, None, None))
        note = redact(val(r, 5))
        if raw == "declined" and WE_DECLINED.search(note):
            status = "We declined"
        if raw == "chasing" and PRECALL.search(note):
            status = "Precall requested"
        if raw == "cold lead" and MAIL_SENT.search(note):
            status = "Contacted"
        x.update(status=status, direction=direction, route=route, raw_status=val(r, 1))
        v1, e1, d1 = eval_bits(r, 2)
        v2, e2, d2 = eval_bits(r, 8)
        _, e3, d3 = eval_bits(r, 6)
        x["eval_verdict"] = v1 or v2
        x["eval_link"] = e1 or e2 or e3
        x["dossier_link"] = d3 or d2 or d1
        x["host_verdict"] = HOST.get(val(r, 3).lower())
        x["next_date"] = as_date(cell(r, 7).value) if cell(r, 7) is not None else None
        x["next_action"] = note or None
        pitch = redact(val(r, 4))
        if pitch:
            x["notes"].append(f"Short pitch: {pitch}")
        if val(r, 3):
            x["notes"].append(f"Sri approval (sheet): {val(r, 3)}")
        x["notes"].append(f"Sheet status: {val(r, 1)}")
        out.append(x)
    return out


def read_sponsored(wb):
    ws = wb["Sponsored"]
    out = []
    for i, r in enumerate(ws.iter_rows(min_row=3), start=3):
        if not val(r, 0):
            continue
        x = new_row("sponsored", i, val(r, 0), link(r, 0))
        raw = val(r, 1).lower()
        via = val(r, 2)
        x.update(status=SPONSORED_STATUS.get(raw), route="Sponsored", raw_status=val(r, 1),
                 direction="Outbound" if via.lower() == "cold lead" else "Inbound",
                 via_name=None if via.lower() in ("cold lead", "inbound", "") else via,
                 next_date=as_date(cell(r, 5).value), next_action=redact(val(r, 3)) or None)
        _, e, d = eval_bits(r, 6)
        x["eval_link"], x["dossier_link"] = e, d
        x["notes"].append(f"Sheet status (Sponsored tab): {val(r, 1)}")
        out.append(x)
    return out


def read_old(wb):
    ws = wb["Old Pipeline"]
    out, layout = [], "a"
    for i, r in enumerate(ws.iter_rows(min_row=2), start=2):
        first = val(r, 0)
        if not first:
            continue
        if first == "Linkedin Link":
            layout = "b"  # a second, older table sits under the first one
            continue
        if layout == "a":
            name = first + (f" @ {val(r, 2)}" if val(r, 2) else "")
            x = new_row("old", i, name, link(r, 1) or link(r, 0))
            raw = val(r, 3).lower()
            status, direction = OLD_STATUS.get(raw, (None, None))
            x.update(status=status, direction=direction, raw_status=val(r, 3), next_action=redact(val(r, 6)) or None)
            v, e, d = eval_bits(r, 5)
            x["eval_link"], x["dossier_link"], x["eval_verdict"] = e, d, v
            if val(r, 4):
                x["notes"].append(f"Funding / scale (sheet): {redact(val(r, 4))}")
            if val(r, 6):
                x["notes"].append(f"Comments: {redact(val(r, 6))}")
        else:
            x = new_row("old", i, first, link(r, 0))
            raw = val(r, 1).lower()
            status, direction = OLD_STATUS.get(raw, (None, None))
            x.update(status=status, direction=direction, raw_status=val(r, 1), next_action=redact(val(r, 3)) or None)
            if val(r, 2):
                x["notes"].append(f"Reason to shortlist: {redact(val(r, 2))}")
        x["notes"].append(f"Sheet status (Old Pipeline): {x.get('raw_status') or 'blank'}")
        out.append(x)
    return out


def read_roster(wb, tab, key, agency, rec_col, eval_col):
    ws = wb[tab]
    out = []
    for i, r in enumerate(ws.iter_rows(min_row=2), start=2):
        if not val(r, 0):
            continue
        name = val(r, 0) if "@" in val(r, 0) else f"{val(r, 0)} @ {val(r, 1)}"
        x = new_row(key, i, name, link(r, 0))
        rec = val(r, rec_col) if rec_col is not None else ""
        v, e, d = eval_bits(r, eval_col)
        verdict = v or parse_eval(rec, None)[0]
        x.update(eval_verdict=verdict, eval_link=e, dossier_link=d, direction="Inbound", via_agency=agency,
                 status="We declined" if verdict == "Decline" else "New",
                 next_action=f"On {agency}'s client roster; not yet pitched to Sri")
        blurb = redact(val(r, 5 if tab == "YAP Clients" else 4))
        if blurb and blurb != "None":
            x["notes"].append(f"Blurb: {blurb}")
        x["notes"].append(f"From the {tab} tab ({agency} roster). Eval: {verdict or 'none'}")
        out.append(x)
    return out


def read_defillama(wb):
    ws = wb["Defillama 49 Lead"]
    out = []
    for i, r in enumerate(ws.iter_rows(min_row=2), start=2):
        if not val(r, 0):
            continue
        x = new_row("defillama", i, f"{val(r, 0)} @ {val(r, 1)}", link(r, 2))
        flag = val(r, 4).strip("'")
        x.update(status="New", direction="Outbound",
                 next_action="DefiLlama top-protocol target list; not contacted" if not flag else f"Target list flag: {flag}")
        x["notes"].append(f"From the Defillama 49 Lead tab (outbound target list). Flag: {flag or 'none'}")
        out.append(x)
    return out


def read_crm(wb):
    ws = wb["CRM"]
    crm = {}
    for r in ws.iter_rows(min_row=2):
        if not val(r, 0):
            continue
        mails = EMAIL.findall(val(r, 3) + " " + val(r, 6))
        crm[name_key(val(r, 0))] = {"name": val(r, 0), "role": val(r, 1) or None, "company": val(r, 2) or None,
                                    "emails": list(dict.fromkeys(m.lower() for m in mails)),
                                    "li_slug": li_slug(val(r, 7)), "li_url": li_url(val(r, 7)) if li_slug(val(r, 7)) else None,
                                    "phone": re.sub(r"[^\d+]", "", val(r, 5)) or None,
                                    "dossier_link": link(r, 8)}
    return crm


def person_key(x):
    if x["li_slug"]:
        return "li:" + x["li_slug"]
    if x["people"]:
        return "nm:" + name_key(x["people"][0])
    return "raw:" + fold(x["raw_name"])


def merge(rows):
    groups = collections.OrderedDict()
    by_name = {}
    for x in sorted(rows, key=lambda x: TAB_RANK[x["tab"]]):
        k = person_key(x)
        nk = "nm:" + name_key(x["people"][0]) if x["people"] else None
        if k not in groups and nk and nk in by_name:
            k = by_name[nk]  # same person, one row has a LinkedIn link and the other does not
        groups.setdefault(k, []).append(x)
        if nk:
            by_name.setdefault(nk, k)
    merged = []
    for k, xs in groups.items():
        head = dict(xs[0])
        head["source_ids"] = [x["source_id"] for x in xs]
        head["tabs"] = list(dict.fromkeys(x["tab"] for x in xs))
        for f in ("company", "li_slug", "li_url", "eval_verdict", "eval_link", "dossier_link", "host_verdict",
                  "next_date", "via_name", "via_agency", "route", "direction"):
            if not head.get(f):
                head[f] = next((x[f] for x in xs[1:] if x.get(f)), None)
        if not head.get("people"):
            head["people"] = next((x["people"] for x in xs[1:] if x["people"]), [])
        head["notes"] = [n for x in xs for n in x["notes"]]
        head["key"] = k
        merged.append(head)
    return merged


def main():
    wb = openpyxl.load_workbook(RAW)
    rows = read_v2(wb) + read_sponsored(wb) + read_old(wb)
    rows += read_roster(wb, "YAP Clients", "yap", "YAP", 4, 3)
    rows += read_roster(wb, "Theprgenius Client", "prgenius", "The PR Genius", None, 3)
    rows += read_defillama(wb)
    crm = read_crm(wb)
    cands = merge(rows)
    review = []
    for c in cands:
        nk = name_key(c["people"][0]) if c["people"] else None
        info = crm.get(nk)
        if info:
            c["crm"] = info
            c["li_slug"] = c["li_slug"] or info["li_slug"]
            c["li_url"] = c["li_url"] or info["li_url"]
            c["dossier_link"] = c["dossier_link"] or info["dossier_link"]
        if c["next_date"]:
            c["next_date"] = c["next_date"].isoformat()
        if c["status"] is None and c["tab"] == "old" and not c.get("raw_status", "").strip(" '"):
            # Old Pipeline rows with a blank status were names on Sri's target list.
            c["status"], c["direction"] = "New", "Outbound"
        if not c["people"]:
            review.append([";".join(c["source_ids"]), c["raw_name"], c.get("parse_note") or "no guest name", ""])
        if c["status"] is None:
            review.append([";".join(c["source_ids"]), c["raw_name"], f"unmapped status {c.get('raw_status')!r}", ""])
        if len(c["people"]) > 1:
            review.append([";".join(c["source_ids"]), c["raw_name"], "several guests on one row: one Engagement, first as Guest",
                           ", ".join(c["people"])])
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "candidates.json").write_text(json.dumps(cands, indent=1, default=str))
    REVIEW.parent.mkdir(parents=True, exist_ok=True)
    with REVIEW.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source", "name", "issue", "detail"])
        w.writerows(review)
    print(f"rows read {len(rows)}  by tab {dict(collections.Counter(r['tab'] for r in rows))}")
    print(f"candidates after merge {len(cands)}  with LinkedIn {sum(1 for c in cands if c['li_slug'])}  "
          f"CRM-enriched {sum(1 for c in cands if c.get('crm'))}  review rows {len(review)}")
    print("status", dict(collections.Counter(c["status"] for c in cands)))
    print("lead tab", dict(collections.Counter(c["tab"] for c in cands)))


if __name__ == "__main__":
    main()
