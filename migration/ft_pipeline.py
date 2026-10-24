"""Migrate the Founder Thesis guest pipeline sheet into Notion Engagements, and fill Status on the guest rows that are already there.

Usage:
  python migration/ft_pipeline.py                      profile, match, export JSON and the review CSV (re-runnable, read-only)
  python migration/ft_pipeline.py --batches orgs       write create-pages payloads (batches of 100) for orgs | people | engagements
  python migration/ft_pipeline.py --created orgs FILE  record created page URLs from a saved Notion query result (Source ID -> url)
  python migration/ft_pipeline.py --updates            write update-page payloads for existing engagements (Part A + sheet matches)
  python migration/ft_pipeline.py --reconcile          print expected counts to check against COUNT queries in Notion

Reads (all git-ignored):
  data/raw/sheets/ft_pipeline.xlsx                       tabs Inbound, P1, Paid, FT Cold Lead
  data/raw/notion/people_snapshot_2026-10-05.json        People as of 5 Oct (url, Name, LinkedIn, Email, Other emails, Organisation, Match status, Tags)
  data/raw/notion/orgs_snapshot_2026-10-05.json          Organisations as of 5 Oct
  data/raw/notion/engagements_guests_2026-10-05.json     the 227 guest Engagements (Type null) as of 5 Oct
Writes:
  data/out/ft_pipeline/{people_new,orgs_new,engagements_new,engagements_update}.json
  data/out/ft_pipeline/skipped.json                      sheet rows whose existing engagement is already further along
  data/out/ft_pipeline/batches/*.json, created.json, updates.json
  data/review/ft_pipeline_review.csv

Mapping follows docs/statuses.md ("Where today's sheet values land"). Matching reuses migration/paas.py's Index:
LinkedIn slug, then email, then exact name at the same organisation, then a full name whose only existing row has no
organisation. A name-only clash is never merged: the person is created as "Possible duplicate" and both candidates go to
the review CSV. Never edits the raw files. Re-run safely.
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
from paas import Index, EMAIL, emails, fold, is_role, li_slug, li_url, name_key, org_key, page_url  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw"
OUT = ROOT / "data/out/ft_pipeline"
BATCH = "ft-pipeline-2026-10-05"
TODAY = dt.date(2026, 10, 5)
SNAP = "2026-10-05"
FT_SHOW = "https://app.notion.com/p/3ed19a301a7f817c9367e0d88afc5776"
BATCH_SIZE = {"orgs": 100, "people": 80, "engagements": 50}  # keeps each payload under the 30 KB a terminal print carries
SOURCES = {"people": "collection://e6c44319-7f81-4da6-8b80-8441a4875d7a",
           "orgs": "collection://c43c280a-3b37-4821-96ef-dab688a53aea",
           "engagements": "collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5"}

# the guest ladder in journey order; everything else (LT chase, Parked, declined, Unresponsive) is off the ladder
LADDER = ["New", "Contacted", "Interested", "Decision pending", "Precall requested", "Precall done", "Sponsored offered",
          "Booking", "Booked", "Recorded", "Form filled"]
RANK = {s: i for i, s in enumerate(LADDER)}
CLOSED = {"Form filled", "They declined", "We declined", "Unresponsive"}
OUTCOME_TO_STATUS = {"Live": "Form filled", "Done": "Form filled", "Declined": "They declined", "No response": "Unresponsive",
                     "Dropped out": "They declined"}
VERDICTS = [("book immediately", "Book immediately"), ("strong consider", "Strong consider"),
            ("evaluate after call", "Evaluate after call"), ("declined", "Decline"), ("decline", "Decline")]
TIERS = [("tier 1.5", "Tier 1.5"), ("tier 1", "Tier 1"), ("tier 2", "Tier 2")]
MONTHS = {m: i + 1 for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}
HONORIFIC = re.compile(r"^(dr|mr|ms|mrs|prof|shri|smt|ca)(\.\s*|\s+)", re.I)
ROLE_WORD = re.compile(r"^(president|founder|co-?founder|ceo|coo|cto|cfo|md|director|chairman|partner|head|vp|svp|owner)$", re.I)
PHONE = re.compile(r"\+?\d[\d \-]{8,}\d")
URL = re.compile(r"https?://[^\s|]+")
COMPANYISH = re.compile(r"\b(ltd|limited|pvt|private|inc|llp|llc|technolog|ventures|capital|partners|fund|labs|films|group|"
                        r"solutions|services|india|global|digital|media|foundation|consult|systems|network|academy|institute|"
                        r"client|unknown|confidential|not disclosed|story|thesis)\b", re.I)
SPONSORED = re.compile(r"sponsor|commerc|paid", re.I)
PRECALL_DONE = re.compile(r"pre[- ]?call done|preliminary call done|planning call done|precall happened", re.I)
PRECALL = re.compile(r"pre[- ]?call|prelim|perlim|preliminary|planning call", re.I)
WE_DECLINED = re.compile(r"akshay|decline[d]? by|already (a guest|featured)|featured already|featured earlier", re.I)


def redact(s):
    s = EMAIL.sub("", str(s or ""))
    return re.sub(r"\s+", " ", PHONE.sub("", s)).strip(" -|,")


def clean(s):
    return re.sub(r"\s+", " ", str(s or "").replace("\t", " ")).strip()


def strip_honorific(s):
    return HONORIFIC.sub("", clean(s)).strip()


def company_like(s):
    toks = clean(s).split()
    return len(toks) <= 1 or bool(COMPANYISH.search(s)) or len(toks) > 4


def split_people(person):
    """'Ankit and Anshul Agrawal' -> ['Ankit Agrawal', 'Anshul Agrawal']; 'A & B' -> ['A', 'B']. Up to three guests."""
    person = re.sub(r"\(.*?\)", "", person)
    parts = [strip_honorific(p) for p in re.split(r"\s*(?:,|/|\s+and\s+|\s*&\s*)\s*", person) if strip_honorific(p)]
    if len(parts) > 3:
        return []
    out = []
    for i, p in enumerate(parts):
        if len(p.split()) == 1 and i + 1 < len(parts) and len(parts[i + 1].split()) >= 2:
            p = p + " " + parts[i + 1].split()[-1]  # shared surname written once
        out.append(p)
    return [p for p in out if 1 <= len(p.split()) <= 4 and not ROLE_WORD.match(p)]


def parse_name_cell(cell, hyperlink):
    """Return (people, company, li_slug, note). people is a list of clean names, company a display string or None."""
    s = clean(cell)
    li = li_slug(hyperlink) or next((li_slug(u) for u in URL.findall(s) if li_slug(u)), None)
    s = URL.sub("", s)
    s = re.sub(r"\s*\|\s*linke?d\s*in\w*\s*$", "", s, flags=re.I)
    s = re.sub(r"\s*\|\s*.*$", "", s)
    s = re.sub(r"\s+and\s*$|\s*[-–]\s*$", "", s).strip(" ,-–:'")
    note = None
    if "@" in s:
        person, company = s.split("@", 1)
        person = re.sub(r",\s*$", "", person.strip())
        company = company.strip(" ,")
        if re.search(r"\s[-–]\s", company) and len(company.split()) > 6:
            company = re.split(r"\s[-–]\s", company)[0]
    elif "," in s or re.search(r"\b(is the|is a|founder of|ceo of|co-?founder of|founders? of)\b", s, re.I):
        segments = [p.strip() for p in s.split(",") if p.strip()]
        if len(segments) >= 4 and all(len(p.split()) <= 2 for p in segments[:3]):
            return [], None, li, "guest name unparseable"
        person = re.split(r",|\s[-–]\s|\s+is\s+|\s+(?:founder|ceo|co-?founder)s?\s+of\b", s, 1, flags=re.I)[0].strip()
        tail = s[len(person):]
        m = re.search(r"\b(?:of|at|from)\s+(.+?)\s*$", tail, re.I)
        if m and not re.search(r"\b(head|director|vp|officer)\s+of\b", m.group(0), re.I):
            company = m.group(1)
        else:
            company = segments[-1] if len(segments) > 1 else None
        if company:
            company = re.sub(r"^(the\s+)?(founder|co-?founder|ceo|chairman|director|md|head)\b.*?\bof\s+", "", company, flags=re.I).strip(" ,:")
            if company_like(company) is False and len(company.split()) > 5:
                company = None
    elif re.search(r"\s[-–]\s", s):
        left, right = [p.strip() for p in re.split(r"\s[-–]\s", s, 1)]
        # 'Company - Person' is how the referred-by rows were written; the LinkedIn slug or company words settle it
        def score(side):
            sc = 0
            if li and any(t.lower() in li for t in side.split() if len(t) > 2):
                sc += 2
            if company_like(side):
                sc -= 1
            return sc
        person, company = (left, right) if score(left) >= score(right) else (right, left)
    else:
        person, company = s, None
        if company_like(s):
            return [], s, li, "company only, no guest name"
    if company:
        company = re.sub(r"^(founder|co-?founder|ceo|chairman)\s+(and\s+\w+\s+)?of\s+", "", company, flags=re.I)
        company = re.sub(r"\s+and\s+(co-?founder|founder|head|chairman|director|managing|author|host)\b.*$", "", company, flags=re.I).strip(" ,")
        role_words = re.search(r"\b(director|founder|ceo|coo|author|advisor|photographer|consultant|curator|professional|head of|"
                               r"regional|speaker|writer|coach|entrepreneur|educationist|developer|systems|maker)\b", company, re.I)
        company = re.sub(r"\s*[-–]\s*no linkedin.*$", "", company, flags=re.I).strip(" ,")
        if company.count(")") > company.count("("):
            company = company.rstrip(")").strip()
        if role_words and ("," in company or len(company.split()) > 4 and not COMPANYISH.search(company)):
            company = None  # a role description, not a company
        if company and re.fullmatch(r"(confidential|unknown( client)?|client|n/?a|-)", company, re.I):
            company = None
    people = split_people(person)
    if not people:
        note = "guest name unparseable"
    return people, (clean(company) or None), li, note


def parse_eval(cell, hyperlink):
    """-> (verdict, tier, eval_link, dossier_link, title, mixed)."""
    text = clean(cell)
    low = text.lower()
    found = [v for k, v in VERDICTS if k in low]
    found = list(dict.fromkeys(found))
    verdict = found[0] if found else None
    tier = next((v for k, v in TIERS if k in low), None)
    link = hyperlink or next(iter(URL.findall(text)), None)
    eval_link = dossier_link = None
    if link:
        if re.search(r"dossier|guest prep|preparation|prep note", low):
            dossier_link = link
        else:
            eval_link = link
    is_title = bool(text) and not verdict and not tier and not URL.search(text)
    return verdict, tier, eval_link, dossier_link, (text if is_title else None), (len(found) > 1)


def as_date(v):
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    return None


def date_in_text(text, anchor):
    """'Scheduled as on Oct 7th' -> the Oct 7 nearest to anchor (a date), else None."""
    low = clean(text).lower()
    m = re.search(r"(\d{1,2})(?:st|nd|rd|th)?\s+(?:of\s+)?([a-z]{3,9})\b", low) or re.search(r"\b([a-z]{3,9})\s+(\d{1,2})(?:st|nd|rd|th)?\b", low)
    if not m:
        return None
    a, b = m.groups()
    day, mon = (int(a), b) if a.isdigit() else (int(b), a)
    month = MONTHS.get(mon[:3])
    if not month or not 1 <= day <= 31:
        return None
    anchor = anchor or TODAY
    best = None
    for y in (anchor.year - 1, anchor.year, anchor.year + 1):
        try:
            d = dt.date(y, month, day)
        except ValueError:
            continue
        if best is None or abs((d - anchor).days) < abs((best - anchor).days):
            best = d
    return best


def chase_step(*texts):
    for t in texts:
        m = re.search(r"(\d)\s*(?:follow|fu\b)|(\d)(?:st|nd|rd|th)\s+follow", clean(t), re.I)
        if m:
            return int(m.group(1) or m.group(2))
    return None


def parse_via(raw):
    """-> (name or None, org or None, tags, direction or None, skipped_reason)."""
    s = clean(raw)
    if not s:
        return None, None, [], None, None
    tags, direction = [], None
    if re.match(r"referred by\b", s, re.I):
        s = re.sub(r"^referred by\s*", "", s, flags=re.I)
        tags.append("Warm intro")
    if re.match(r"cold lead", s, re.I):
        direction = "Outbound"
        s = re.sub(r"^cold lead\s*[-:]?\s*(linkedin\s*\(m\)\s*-\s*)?", "", s, flags=re.I)
    if re.search(r"\bself\b|^wa\b|^linkedin$|^guest eval", s, re.I):
        return None, None, tags, direction, "self or no PR contact"
    s = re.sub(r"\s*[-–]\s*(paid|pr co|self)\s*$", "", s, flags=re.I)
    s = EMAIL.sub("", PHONE.sub("", s))
    s = re.split(r"\s*\|\s*|\s*/\s*|\s+and\s+|\s*[-–]\s+", s)[0].strip(" ,-–")
    org = None
    if "@" in s:
        s, org = [p.strip() for p in s.split("@", 1)]
    s = re.sub(r"\(.*?\)", "", strip_honorific(s)).strip()
    if "," in s and len(s.split(",")) == 2:  # 'Ahuja, Paras Raj'
        a, b = [p.strip() for p in s.split(",")]
        s = f"{b} {a}"
    toks = s.split()
    if len(toks) < 2 or len(toks) > 4 or company_like(s) and not org:
        return None, None, tags, direction, f"via not a full name: {redact(raw)[:60]}"
    return s, org, tags, direction, None


def first_amount(*texts):
    for t in texts:
        m = re.search(r"(?:inr|rs\.?|₹)?\s*(\d+(?:\.\d+)?)\s*([kK]|lakh|L)\b", clean(t))
        if m:
            n = float(m.group(1))
            return int(n * (100000 if m.group(2).lower() in ("lakh", "l") else 1000))
        m = re.search(r"(?:inr|rs\.?|₹)\s*([\d,]{4,})", clean(t), re.I)
        if m:
            return int(m.group(1).replace(",", ""))
    return None


# ---------------------------------------------------------------- sheet parsing

def read_tab(wb, tab):
    ws = wb[tab]
    rows = []
    for i, r in enumerate(ws.iter_rows(min_row=2), 2):
        if r[0].value is None or not clean(r[0].value):
            continue
        rows.append({"tab": tab, "row": i, "cells": [c.value for c in r], "links": [c.hyperlink.target if c.hyperlink else None for c in r]})
    return rows


def parse_inbound(r):
    c, h = r["cells"], r["links"]
    people, company, li, note = parse_name_cell(c[0], h[0])
    status_raw, via_raw, route, next_ad = clean(c[1]), clean(c[2]), clean(c[3]), clean(c[4])
    fu = as_date(c[5])
    verdict, tier, eval_link, dossier_link, title, mixed = parse_eval(c[6], h[6])
    return {**r, "people": people, "company": company, "li": li, "note": note, "status_raw": status_raw, "via_raw": via_raw,
            "route": route, "next_m": None, "next_ad": next_ad, "date": fu, "verdict": verdict, "tier": tier,
            "eval_link": eval_link, "dossier_link": dossier_link, "eval_title": title, "mixed_eval": mixed, "direction": "Inbound"}


def parse_p1(r):
    c, h = r["cells"], r["links"]
    people, company, li, note = parse_name_cell(c[0], h[0])
    verdict, tier, eval_link, dossier_link, title, mixed = parse_eval(c[2], h[2])
    v2, t2, e2, d2, _, _ = parse_eval(c[8], h[8])  # Column 1 holds a second doc (eval or prep note) on 17 rows
    return {**r, "people": people, "company": company, "li": li, "note": note, "status_raw": clean(c[1]), "via_raw": clean(c[3]),
            "route": clean(c[6]), "next_m": clean(c[4]), "next_ad": clean(c[5]), "date": as_date(c[7]),
            "verdict": verdict or v2, "tier": tier or t2, "eval_link": eval_link or e2, "dossier_link": dossier_link or d2,
            "eval_title": title, "mixed_eval": mixed, "direction": "Inbound"}


def parse_paid(r):
    c, h = r["cells"], r["links"]
    people, company, li, note = parse_name_cell(c[0], h[0])
    company = clean(c[1]) or company
    flags = {k: bool(c[i]) for k, i in [("gst", 5), ("invoice", 6), ("pay1", 7), ("planning", 8), ("scheduled", 9), ("pay2", 10), ("released", 11)]}
    return {**r, "people": people, "company": company, "li": li, "note": note, "status_raw": "Paid", "via_raw": clean(c[2]),
            "route": clean(c[3]), "next_m": None, "next_ad": None, "date": as_date(c[4]), "verdict": None, "tier": "Sponsored",
            "eval_link": None, "dossier_link": None, "eval_title": None, "mixed_eval": False, "direction": "Inbound",
            "flags": flags, "amount": first_amount(c[12], c[3])}


def parse_cold(r):
    c, h = r["cells"], r["links"]
    name = strip_honorific(f"{clean(c[0])} {clean(c[1])}")
    name = re.sub(r"\(.*?\)\s*", "", name).strip()
    mails = emails(c[3])
    return {**r, "people": [name] if len(name.split()) >= 2 else [], "company": clean(c[4]) or None, "li": None,
            "note": None if len(name.split()) >= 2 else "guest name unparseable", "status_raw": clean(c[2]), "via_raw": "",
            "route": clean(c[6]), "next_m": None, "next_ad": None, "date": None, "verdict": None, "tier": None, "eval_link": None,
            "dossier_link": None, "eval_title": None, "mixed_eval": False, "direction": "Outbound", "emails": mails,
            "role": clean(c[5]) or None, "investor": "investor" in clean(c[2]).lower()}


# ---------------------------------------------------------------- status mapping (docs/statuses.md)

def map_row(r):
    """Return the Notion field values for one sheet row."""
    m = {"Status": None, "Direction": r["direction"], "Tier": r.get("tier"), "Decision": None, "Eval verdict": r.get("verdict"),
         "Eval link": r.get("eval_link"), "Dossier link": r.get("dossier_link"), "Payment": None, "Amount": r.get("amount"),
         "Next action": None, "Next date": None, "Chase step": None, "Tags": []}
    s, route, notes = r["status_raw"], r["route"] or "", " ".join(filter(None, [r["route"], r.get("next_m"), r.get("next_ad"), r.get("eval_title")]))
    tab = r["tab"]
    if tab == "FT Cold Lead":
        m["Status"] = "New"
        low = route.lower()
        if "bounce" in low:
            m["Status"], m["Tags"] = "Unresponsive", ["No email"]
        elif PRECALL_DONE.search(route):
            m["Status"] = "Precall done"
        elif re.search(r"not interested", low):
            m["Status"] = "They declined"
        elif re.search(r"next year|later", low):
            m["Status"], m["Next date"] = "Parked", dt.date(2027, 1, 26) if "jan 26" in low else TODAY + dt.timedelta(days=90)
        elif re.search(r"schedule the recording", low):
            m["Status"], m["Decision"] = "Booking", "Book"
        elif PRECALL.search(route) or re.search(r"pre call|planning call", low):
            m["Status"], m["Decision"] = "Precall requested", "Precall"
        elif "interested" in low:
            m["Status"] = "Interested"
        if route and m["Status"] not in CLOSED:
            m["Next action"] = route
        return m
    if tab == "Paid":
        f = r["flags"]
        m["Tier"] = "Sponsored"
        m["Payment"] = ("Payment 2 received" if f["pay2"] else "Payment 1 received" if f["pay1"] else "Invoice 1 sent" if f["invoice"]
                        else "GST received" if f["gst"] else "Not started")
        m["Decision"] = "Sponsored"
        if f["released"]:
            m["Status"] = "Form filled"
        elif f["scheduled"]:
            m["Status"] = "Recorded" if re.search(r"recording done|recorded", route, re.I) else "Booked"
        elif f["planning"]:
            m["Status"] = "Precall done"
        elif f["pay1"] or f["invoice"] or f["gst"]:
            m["Status"] = "Booking"
        elif re.search(r"decline|backed ?out", route, re.I):
            m["Status"] = "They declined"
        else:
            m["Status"] = "Sponsored offered"
        if m["Status"] not in CLOSED:
            m["Next action"], m["Next date"] = route or None, date_in_text(route, r["date"]) if m["Status"] == "Booked" else r["date"]
        return m

    # Inbound and P1
    sponsored_route = bool(SPONSORED.search(route)) or s in ("Sponsored", "Paid")
    if sponsored_route:
        m["Tier"], m["Decision"] = "Sponsored", "Sponsored"
    elif PRECALL.search(route) and not PRECALL_DONE.search(route):
        m["Decision"] = "Precall"
    if s == "Declined":
        m["Status"] = "We declined" if WE_DECLINED.search(notes) else "They declined"
        if m["Status"] == "We declined":
            m["Decision"] = "Decline"
    elif s == "Unresponsive":
        m["Status"] = "Unresponsive"
    elif s == "Propsed Alt":
        m["Status"] = "They declined"
        m["Tags"].append("Alternative proposed")
    elif s in ("P2", "Maybe Later", "Later"):
        m["Status"] = "Parked"
        m["Next date"] = r["date"] or TODAY + dt.timedelta(days=90)
    elif s == "LT Chase":
        m["Status"] = "LT chase"
    elif s == "Form Filled":
        m["Status"] = "Form filled"
    elif s == "Recorded":
        m["Status"] = "Recorded"
    elif s == "Scheduled":
        m["Status"] = "Booked"
        m["Next date"] = date_in_text(r.get("next_m") or "", r["date"]) or r["date"]
    elif s == "To be Scheduled":
        m["Status"], m["Decision"] = "Booking", "Book"
    elif s == "Add to outbound":
        m["Status"], m["Direction"] = "New", "Outbound"
    elif s == "Precall Scheduled":
        m["Status"], m["Decision"] = "Precall requested", "Precall"
        m["Next date"] = date_in_text(route, r["date"]) or r["date"]
    elif s == "Sponsored":
        m["Status"] = "Precall done" if PRECALL_DONE.search(route) else "Sponsored offered"
    elif s == "Paid":  # Inbound row without a Paid tab row; the Paid tab wins when it exists (see collapse)
        m["Status"] = "Precall done" if PRECALL_DONE.search(route) else "Booking"
    elif s in ("Chase", "Interested", "TBD", "P1"):
        low = (r.get("next_m") or route).lower()
        if PRECALL_DONE.search(notes):
            m["Status"] = "Precall done"
        elif re.search(r"reconnect|revisit|next year|in dec|in jan|post ", low) and s != "TBD":
            m["Status"], m["Next date"] = "Parked", r["date"] or TODAY + dt.timedelta(days=90)
        elif re.search(r"recording|wait till", low) and s == "Chase":
            m["Status"], m["Decision"] = "Booking", "Book"
        elif PRECALL.search(low):
            m["Status"], m["Decision"] = "Precall requested", "Precall"
        elif sponsored_route:
            m["Status"] = "Sponsored offered"
        elif s == "Interested":
            m["Status"] = "Interested"
        else:
            m["Status"] = "Decision pending"
    else:
        m["Status"] = "Decision pending"
        m["Tags"].append("Unmapped sheet status")
    if m["Status"] not in CLOSED and m["Status"] not in ("LT chase", "Parked", "Booked"):
        m["Next date"] = m["Next date"] or r["date"]
    if m["Status"] in ("LT chase",) and not m["Next date"]:
        m["Next date"] = r["date"]
    if m["Status"] not in CLOSED:
        m["Next action"] = r.get("next_m") or r.get("next_ad") or (route if tab == "Inbound" else None) or None
        if m["Next action"]:
            m["Next action"] = redact(m["Next action"])[:200]
    if m["Status"] in ("Chase", "LT chase", "Contacted", "Precall requested", "Booking") or s in ("Chase", "LT Chase"):
        m["Chase step"] = chase_step(r.get("next_m"), r.get("next_ad"), route)
    if m["Next date"] and m["Status"] in CLOSED:
        m["Next date"] = None
    if m["Status"] in ("Recorded", "Form filled") and m["Decision"] != "Sponsored":
        m["Decision"] = None
    return m


def more_advanced(a, b):
    """True if status a should replace status b when both describe the same conversation."""
    if b is None:
        return True
    if b in ("Recorded", "Form filled"):
        return RANK.get(a, -1) > RANK[b]
    return True


# ---------------------------------------------------------------- the run

class Run:
    def __init__(self, idx, existing_engs, orgs_snap):
        self.idx = idx
        self.org_names = {page_url(o["url"]): o["Name"] for o in orgs_snap}
        self.orgs, self.people, self.engs, self.updates, self.review, self.skipped = [], [], [], [], [], []
        self.matched = collections.Counter()
        self.eng_by_guest = {}
        for e in existing_engs:
            if FT_SHOW in [page_url(u) for u in (e.get("Show") or [])]:
                for g in e.get("Guest") or []:
                    self.eng_by_guest.setdefault(page_url(g), []).append(e)
        self.by_name = collections.defaultdict(list)
        for key, hits in idx.by_name.items():
            self.by_name[key] = list(hits)
        self.person_names = {}  # ref -> display name, for the review CSV

    def org(self, name, sid, org_type=None, create=True):
        if not name:
            return None
        ref = self.idx.org(name)
        if ref:
            return ref
        for o in self.orgs:
            if org_key(o["props"]["Name"]) == org_key(name):
                return o["key"]
        if not create:
            return None
        key = f"{sid}/org"
        props = {"Name": name, "Source": "Migration", "Source ID": key, "Migration batch": BATCH, "date:Captured:start": str(TODAY)}
        if org_type:
            props["Type"] = org_type
        self.orgs.append({"key": key, "props": props})
        self.idx.add_org(key, name, None)
        self.org_names[key] = name
        return key

    def similar_org(self, name, company):
        """The org of a same-name person when the sheet company is a longer or shorter spelling of it (Wonderchef Home Appliances / Wonderchef)."""
        if not company:
            return None
        kc = org_key(company)
        for ref, orgs_of in self.idx.by_name.get(name_key(name), []):
            for o in orgs_of:
                ko = org_key(self.org_names.get(o, ""))
                if min(len(kc), len(ko)) >= 5 and (kc.startswith(ko) or ko.startswith(kc)):
                    return ref, o
        return None

    def person(self, name, li, mails, org_ref, sid, tags, label, role=None, company=None, recorded=False):
        personal = [e for e in mails if not is_role(e)]
        ref, how = self.idx.person(name, li, personal, org_ref)
        if ref:
            self.matched[how] += 1
            return ref, org_ref
        sim = self.similar_org(name, company)
        if sim:
            self.matched["name and similar organisation"] += 1
            return sim
        hits = self.idx.by_name.get(name_key(name), [])
        if recorded and len(hits) == 1 and hits[0][0] in self.eng_by_guest and len(name_key(name).split()) >= 2:
            # the sheet says this person recorded, and exactly one person with this full name already has an FT engagement
            self.matched["name, recorded guest with an FT engagement"] += 1
            return hits[0][0], (hits[0][1][0] if hits[0][1] else org_ref)
        hits = self.idx.by_name.get(name_key(name), [])
        props = {"Name": name, "Source": "Migration", "Source ID": sid, "Migration batch": BATCH, "date:Captured:start": str(TODAY),
                 "Match status": "Possible duplicate" if hits else "Clean", "Tags": json.dumps(tags)}
        if li:
            props["LinkedIn"] = f"https://www.linkedin.com/in/{li}"
        if personal:
            props["Email"] = personal[0]
            if personal[1:]:
                props["Other emails"] = ", ".join(personal[1:])
        if role:
            props["Role"] = role
        self.people.append({"key": sid, "props": props, "org": org_ref})
        self.idx.add_person(sid, name, li, personal, org_ref)
        self.person_names[sid] = name
        if hits:
            cands = [h[0] for h in hits][:2]
            self.review.append({"source": label, "name": name, "issue": how or "same name exists",
                                "candidate_1": cands[0], "candidate_2": cands[1] if len(cands) > 1 else "",
                                "action": "Created as Possible duplicate; merge in Notion if the same person"})
        self.matched["new"] += 1
        return sid, org_ref

    def via(self, raw, sid, label):
        """Link the PR contact. Returns (ref or None, tags, direction)."""
        name, org, tags, direction, why = parse_via(raw)
        if not name:
            if why and raw:
                self.review.append({"source": label, "name": redact(raw)[:60], "issue": f"Via not linked: {why}", "candidate_1": "",
                                    "candidate_2": "", "action": "Raw Via text kept on the engagement page; link by hand if needed"})
            return None, tags, direction
        hits = self.idx.by_name.get(name_key(name), [])
        org_ref = self.idx.org(org) if org else None
        if len(hits) == 1 or (org_ref and any(org_ref in h[1] for h in hits)):
            ref = next((h[0] for h in hits if org_ref in h[1]), hits[0][0]) if hits else None
            self.matched["via by name"] += 1
            return ref, tags, direction
        if len(hits) > 1:
            self.review.append({"source": label, "name": name, "issue": "Via name matches two people", "candidate_1": hits[0][0],
                                "candidate_2": hits[1][0], "action": "Not linked; pick the right person in Notion"})
            return None, tags, direction
        ref, _ = self.person(name, None, [], org_ref, f"{sid}/via", ["PR contact"] if "Warm intro" not in tags else [], label)
        return ref, tags, direction


def collapse(rows):
    """Group sheet rows that describe the same person. Key: LinkedIn slug, else folded full name of the first guest."""
    groups = collections.OrderedDict()
    key_of = {}
    for r in rows:
        if not r["people"]:
            k = f"row:{r['tab']}/{r['row']}"
        else:
            k = name_key(r["people"][0])
        if r.get("li"):
            key_of.setdefault(name_key(r["people"][0]) if r["people"] else k, r["li"])
        groups.setdefault(k, []).append(r)
    # merge name groups that share a LinkedIn slug under different name spellings
    by_li = collections.defaultdict(list)
    for k, rs in groups.items():
        slug = next((r["li"] for r in rs if r.get("li")), None)
        by_li[slug or k].append(k)
    merged = collections.OrderedDict()
    for slug, keys in by_li.items():
        merged[keys[0]] = [r for k in keys for r in groups[k]]
    return list(merged.values())


TAB_PRIORITY = {"Paid": 3, "P1": 2, "Inbound": 1, "FT Cold Lead": 0}


def choose_primary(rs):
    """Paid beats P1 beats Inbound beats Cold Lead; within a tab the later row is the newer pitch."""
    return sorted(rs, key=lambda r: (TAB_PRIORITY[r["tab"]], r["row"]))[-1]


def body_for(rs):
    lines = ["## From the FT Pipeline sheet (5 Oct 2026)", ""]
    for r in sorted(rs, key=lambda r: (TAB_PRIORITY[r["tab"]], r["row"]), reverse=True):
        lines.append(f"- **{r['tab']} row {r['row']}**: status {r['status_raw'] or 'blank'}")
        for label, key in [("Route or note", "route"), ("Next action (Mamatha)", "next_m"), ("Next action (AD)", "next_ad"),
                           ("Via as written", "via_raw"), ("Eval or dossier title", "eval_title")]:
            v = redact(r.get(key))
            if v:
                lines.append(f"  - {label}: {v[:300]}")
        if r.get("date"):
            lines.append(f"  - Sheet date: {r['date']}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batches", choices=["orgs", "people", "engagements"])
    ap.add_argument("--created", nargs=2, metavar=("KIND", "FILE"))
    ap.add_argument("--updates", action="store_true")
    ap.add_argument("--reconcile", action="store_true")
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "batches").mkdir(exist_ok=True)
    (ROOT / "data/review").mkdir(parents=True, exist_ok=True)
    if args.created:
        return record_created(*args.created)

    people_snap = json.load(open(RAW / f"notion/people_snapshot_{SNAP}.json"))
    orgs_snap = json.load(open(RAW / f"notion/orgs_snapshot_{SNAP}.json"))
    existing = json.load(open(RAW / f"notion/engagements_guests_{SNAP}.json"))
    idx = Index(people_snap, orgs_snap)
    run = Run(idx, existing, orgs_snap)
    wb = openpyxl.load_workbook(RAW / "sheets/ft_pipeline.xlsx")
    parsers = {"Inbound": parse_inbound, "P1": parse_p1, "Paid": parse_paid, "FT Cold Lead": parse_cold}
    rows, per_tab = [], {}
    for tab, fn in parsers.items():
        raw = read_tab(wb, tab)
        per_tab[tab] = len(raw)
        rows += [fn(r) for r in raw]
    print("rows per tab:", per_tab, "total", len(rows))
    for r in rows:
        if r["note"]:
            run.review.append({"source": f"{r['tab']}/{r['row']}", "name": redact(r["cells"][0])[:80], "issue": r["note"],
                               "candidate_1": "", "candidate_2": "", "action": "Engagement created without a Guest; add the person by hand"
                               if "company" in r["note"] else "Engagement created without a Guest; fix the name by hand"})
        if r["mixed_eval"]:
            run.review.append({"source": f"{r['tab']}/{r['row']}", "name": redact(r["cells"][0])[:80], "issue": "two eval labels in one cell, first kept",
                               "candidate_1": "", "candidate_2": "", "action": "Check Eval verdict"})

    groups = collapse(rows)
    print(f"distinct conversations after collapsing across tabs: {len(groups)} (from {len(rows)} rows)")
    status_dist = collections.Counter()
    eng_new = eng_upd = 0
    for rs in groups:
        primary = choose_primary(rs)
        sid = f"FT Pipeline/{primary['tab']}/{primary['row']}"
        label = sid
        mapped = map_row(primary)
        # a P1 or Paid row carries the latest status, but never pulls a Form filled / Recorded row backwards
        best = None
        for r in sorted(rs, key=lambda r: (TAB_PRIORITY[r["tab"]], r["row"])):
            m = map_row(r)
            if best is None or more_advanced(m["Status"], best["Status"]):
                best = m
        if best["Status"] != mapped["Status"]:
            mapped["Status"] = best["Status"]
        # fill blanks from the other rows (eval link from Inbound, dossier from P1, payment from Paid)
        for r in rs:
            m = map_row(r)
            for k in ("Eval verdict", "Eval link", "Dossier link", "Payment", "Amount", "Tier", "Decision"):
                if not mapped.get(k) and m.get(k):
                    mapped[k] = m[k]
            mapped["Tags"] = list(dict.fromkeys(mapped["Tags"] + m["Tags"]))
        if primary["tab"] == "FT Cold Lead" and len(rs) > 1:
            mapped["Direction"] = "Inbound" if any(r["tab"] != "FT Cold Lead" for r in rs) else "Outbound"

        org_type = "Fund" if any(r.get("investor") for r in rs) else None
        company = next((r["company"] for r in sorted(rs, key=lambda r: (TAB_PRIORITY[r["tab"]], r["row"]), reverse=True) if r["company"]), None)
        org_ref = run.org(company, sid, org_type, create=False)
        li = next((r["li"] for r in rs if r.get("li")), None)
        mails = [e for r in rs for e in r.get("emails", [])]
        role = next((r.get("role") for r in rs if r.get("role")), None)
        names = primary["people"] or next((r["people"] for r in rs if r["people"]), [])
        guest_refs = []
        for i, nm in enumerate(names):
            psid = sid if i == 0 else f"{sid}/g{i + 1}"
            if i == 0:
                # match the person first: a known guest at "Wonderchef" settles the org for "Wonderchef Home Appliances"
                ref, matched_org = run.person(nm, li, mails, org_ref, psid, ["FT guest pipeline"], label, role, company=company,
                                              recorded=mapped["Status"] in ("Recorded", "Form filled"))
                org_ref = matched_org or org_ref or run.org(company, sid, org_type)
                if ref == psid and org_ref:
                    run.people[-1]["org"] = org_ref
                    run.idx.by_name[name_key(nm)][-1] = (psid, [org_ref])
                guest_refs.append(ref)
                continue
            ref, _ = run.person(nm, None, [], org_ref, psid, ["FT guest pipeline"], label, role)
            guest_refs.append(ref)
        if not org_ref and company:
            org_ref = run.org(company, sid, org_type)
        via_ref, via_tags, via_dir = None, [], None
        via_raw = next((r["via_raw"] for r in sorted(rs, key=lambda r: (TAB_PRIORITY[r["tab"]], r["row"]), reverse=True) if r["via_raw"]), "")
        if via_raw:
            via_ref, via_tags, via_dir = run.via(via_raw, sid, label)
            if via_ref in guest_refs:
                via_ref = None
        if via_dir and mapped["Status"] == "New" or via_dir and primary["tab"] == "Inbound" and not any(r["tab"] == "P1" for r in rs):
            mapped["Direction"] = via_dir
        mapped["Tags"] = list(dict.fromkeys(mapped["Tags"] + via_tags))

        existing_hits = [e for g in guest_refs for e in run.eng_by_guest.get(g, [])]
        status_dist[mapped["Status"]] += 0
        if existing_hits:
            e = sorted(existing_hits, key=lambda e: (e.get("Outcome") == "Live", e["url"]))[-1]
            base = OUTCOME_TO_STATUS.get(e.get("Outcome"))
            if not more_advanced(mapped["Status"], base):
                run.skipped.append({"engagement": e["url"], "existing": base, "sheet": mapped["Status"], "source": [f"{r['tab']}/{r['row']}" for r in rs]})
                status_dist[base] += 1
                continue
            props = {"Status": mapped["Status"]}
            for k in ("Direction", "Tier", "Decision", "Eval verdict", "Eval link", "Dossier link", "Payment", "Amount"):
                if mapped.get(k) and not e.get(k):
                    props[k] = mapped[k]
            if mapped["Status"] not in CLOSED:
                if mapped.get("Next action"):
                    props["Next action"] = mapped["Next action"]
                if mapped.get("Next date"):
                    props["date:Next date:start"] = str(mapped["Next date"])
                if mapped.get("Chase step") is not None:
                    props["Chase step"] = mapped["Chase step"]
            tags = list(dict.fromkeys((e.get("Tags") or []) + mapped["Tags"]))
            if tags:
                props["Tags"] = json.dumps(tags)
            if via_ref and not e.get("Via"):
                props["Via"] = [via_ref]
            if org_ref and not e.get("Organisation"):
                props["Organisation"] = [org_ref]
            run.updates.append({"page": e["url"], "name": e["Name"], "props": props, "source": [f"{r['tab']}/{r['row']}" for r in rs]})
            status_dist[mapped["Status"]] += 1
            eng_upd += 1
            continue

        title = (" and ".join(names) if names else company or "Unnamed pitch") + (f" @ {company}" if names and company else "") + ", Founder Thesis"
        props = {"Name": title, "Status": mapped["Status"], "Source": "Migration", "Source ID": sid, "Migration batch": BATCH,
                 "date:Captured:start": str(TODAY)}
        for k in ("Direction", "Tier", "Decision", "Eval verdict", "Eval link", "Dossier link", "Payment", "Amount", "Next action", "Chase step"):
            if mapped.get(k) is not None and mapped.get(k) != "":
                props[k] = mapped[k]
        if mapped.get("Next date"):
            props["date:Next date:start"] = str(mapped["Next date"])
        if mapped["Tags"]:
            props["Tags"] = json.dumps(mapped["Tags"])
        run.engs.append({"key": sid, "props": props, "show": FT_SHOW, "guest": guest_refs, "via": [via_ref] if via_ref else [],
                         "org": org_ref, "body": body_for(rs), "rows": [f"{r['tab']}/{r['row']}" for r in rs]})
        if mapped["Status"] in ("Recorded", "Form filled"):
            run.review.append({"source": sid, "name": title, "issue": "sheet says recorded, but Notion has no FT engagement for this person"
                               + (" (person matched)" if any(g.startswith("http") for g in guest_refs) else " (person new)"),
                               "candidate_1": "", "candidate_2": "", "action": "Created as a new engagement; link the episode or merge by hand"})
        status_dist[mapped["Status"]] += 1
        eng_new += 1

    # Part A: every existing guest row gets Status from Outcome; sheet-matched rows already carry it in run.updates
    touched = {u["page"] for u in run.updates}
    part_a = 0
    for e in existing:
        if e["url"] in touched:
            continue
        status = OUTCOME_TO_STATUS.get(e.get("Outcome"))
        if not status:
            continue
        props = {"Status": status}
        if e.get("Via"):
            props["Direction"] = "Inbound"
        run.updates.append({"page": e["url"], "name": e["Name"], "props": props, "source": ["Part A: Outcome"]})
        part_a += 1
        if FT_SHOW in [page_url(u) for u in (e.get("Show") or [])]:
            status_dist[status] += 1

    for name, data in [("orgs_new", run.orgs), ("people_new", run.people), ("engagements_new", run.engs),
                       ("engagements_update", run.updates), ("skipped", run.skipped)]:
        json.dump(data, open(OUT / f"{name}.json", "w"), indent=1, ensure_ascii=False, default=str)
    with open(ROOT / "data/review/ft_pipeline_review.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["source", "name", "issue", "candidate_1", "candidate_2", "action"])
        w.writeheader()
        w.writerows(run.review)

    print(f"people: matched existing {sum(v for k, v in run.matched.items() if k not in ('new', 'via by name'))} "
          f"({dict((k, v) for k, v in run.matched.items() if k not in ('new', 'via by name'))}), "
          f"via linked by name {run.matched['via by name']}, new {run.matched['new']} "
          f"(guests {sum(1 for p in run.people if '/via' not in p['key'])}, PR contacts {sum(1 for p in run.people if '/via' in p['key'])}, "
          f"possible duplicates {sum(1 for p in run.people if p['props']['Match status'] == 'Possible duplicate')})")
    print(f"organisations new {len(run.orgs)}")
    print(f"engagements: new {eng_new}, updated from the sheet {eng_upd}, skipped (existing row further along) {len(run.skipped)}, "
          f"Part A only {part_a}; total updates {len(run.updates)}")
    print("review rows", len(run.review), collections.Counter(r["issue"].split(':')[0] for r in run.review).most_common())
    print("Status distribution, Show = Founder Thesis, after the run (existing 159 + new):")
    for s in LADDER + ["LT chase", "Parked", "They declined", "We declined", "Unresponsive"]:
        print(f"  {s:18} {status_dist.get(s, 0)}")
    print("direction of new engagements:", collections.Counter(e["props"].get("Direction") for e in run.engs))
    assert eng_new + eng_upd + len(run.skipped) == len(groups), "conversation count does not reconcile"
    if args.batches:
        write_batches(args.batches, run)
    if args.updates:
        write_updates(run)
    if args.reconcile:
        print({"orgs": len(run.orgs), "people": len(run.people), "engagements": len(run.engs), "updates": len(run.updates)})


# ---------------------------------------------------------------- apply helpers

def load_created():
    p = OUT / "created.json"
    return json.load(open(p)) if p.exists() else {"orgs": {}, "people": {}, "engagements": {}}


def resolve(ref, created):
    """A Notion page reference as the bare 32-hex id (shorter payloads; create-pages accepts ids or URLs)."""
    if ref is None:
        return None
    if not ref.startswith("http"):
        for kind in ("orgs", "people", "engagements"):
            if ref in created[kind]:
                ref = created[kind][ref]
                break
        else:
            raise KeyError(f"unresolved reference {ref}: create its table first and record the result with --created")
    return re.search(r"([0-9a-f]{32})", ref.replace("-", "")).group(1)


def write_batches(kind, run):
    created = load_created()
    pages = []
    if kind == "orgs":
        for o in run.orgs:
            if o["key"] not in created["orgs"]:
                pages.append({"properties": o["props"]})
    elif kind == "people":
        for p in run.people:
            if p["key"] in created["people"]:
                continue
            props = dict(p["props"])
            if p["org"]:
                props["Organisation"] = [resolve(p["org"], created)]
            pages.append({"properties": props})
    else:
        for e in run.engs:
            if e["key"] in created["engagements"]:
                continue
            props = dict(e["props"])
            props["Show"] = [e["show"]]
            if e["guest"]:
                props["Guest"] = [resolve(g, created) for g in e["guest"]]
            if e["via"]:
                props["Via"] = [resolve(v, created) for v in e["via"]]
            if e["org"]:
                props["Organisation"] = [resolve(e["org"], created)]
            pages.append({"properties": props, "content": e["body"]})
    for old in (OUT / "batches").glob(f"{kind}_*.json"):
        old.unlink()
    size = BATCH_SIZE.get(kind, 100)
    for i in range(0, len(pages), size):
        json.dump(pages[i:i + size], open(OUT / "batches" / f"{kind}_{i // size + 1:02d}.json", "w"), ensure_ascii=False, separators=(",", ":"))
    print(f"{kind}: {len(pages)} pages to create in {(len(pages) + size - 1) // size} batches of {size} (data source {SOURCES[kind]})")


def record_created(kind, path):
    """FILE is a saved Notion query result: one row with 'rows' = url<US>Source ID<US>Name joined by <RS>."""
    created = load_created()
    data = json.load(open(path))
    res = data["results"][0]
    rows = res["rows"].split("\x1e") if res.get("rows") else []
    n = 0
    for row in rows:
        url, sid, _ = row.split("\x1f", 2)
        if sid not in created[kind]:
            n += 1
        created[kind][sid] = page_url(url)
    json.dump(created, open(OUT / "created.json", "w"), indent=1)
    print(f"{kind}: {len(rows)} rows in Notion with Migration batch {BATCH}; {n} newly recorded; {len(created[kind])} total mapped")


def write_updates(run):
    created = load_created()
    out = []
    for u in run.updates:
        props = dict(u["props"])
        for k in ("Via", "Organisation"):
            if k in props:
                props[k] = [resolve(v, created) for v in props[k]]
        out.append({"page_id": re.search(r"([0-9a-f]{32})", u["page"]).group(1), "name": u["name"], "properties": props})
    json.dump(out, open(OUT / "updates.json", "w"), indent=1, ensure_ascii=False)
    print(f"updates: {len(out)} pages")


if __name__ == "__main__":
    sys.exit(main())
