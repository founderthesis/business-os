#!/usr/bin/env python3
"""Read-only profiler for the manually maintained guest / pipeline spreadsheets.

Usage:
    python migration/profile_sheets.py data/raw [--json out.json] [--private-dir DIR] [--as-of YYYY-MM-DD]

Reads every .xlsx in the given folder (Google Sheets exported as xlsx work too).
Never writes to the source files.

Outputs
  * stdout: human-readable aggregate summary (no personal data beyond header text)
  * --json: aggregate statistics per tab and across sources
  * --private-dir: person-level CSVs (records, clusters, tricky matches) for manual
    review. These CONTAIN PERSONAL DATA and must never be committed.

This file intentionally holds no personal data: only header vocabularies,
regexes and matching logic.
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

import openpyxl

# --------------------------------------------------------------------------- #
# Vocabularies
# --------------------------------------------------------------------------- #
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-']+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}")
LI_RE = re.compile(r"linkedin\.com/in/([^/?#\s]+)", re.I)
URL_RE = re.compile(r"^\s*(https?://|www\.)", re.I)
PHONEISH_RE = re.compile(r"\+?\d[\d\s\-()]{7,}\d")

ROLE_LOCALPARTS = {
    "press", "pr", "ir", "info", "contact", "hello", "hi", "support", "media", "team",
    "admin", "office", "ea", "investors", "investor", "marketing", "partnerships",
    "partners", "careers", "hr", "jobs", "submissions", "guests", "guest-pitch",
    "business", "tips", "podcasts", "podcast", "news", "comms", "communications",
    "enquiries", "inquiries", "sales", "founders", "ceo", "office.ceo", "help",
    "crypto-pitches", "pitch", "events", "general", "mediaqueries", "cs", "care",
    "customercare", "connect", "social", "brand", "invest", "ventures",
}
FREEMAIL_DOMAINS = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com",
                    "proton.me", "protonmail.com", "live.com", "me.com", "yahoo.co.in"}
PLACEHOLDER_EMAILS = {"(none)", "none", "no", "bounced", "not found", "n/a", "na", "-", "bounce",
                      "contact form on website", "contact via twitter dm"}

HEADER_VOCAB = {
    "name", "guest", "guest name", "founder name", "founder @ company", "name@company",
    "founder / company", "founder / ceo", "founder(s)", "company", "co name", "org name",
    "companyname", "status", "email", "email id", "linkedin link", "reason to shortlist",
    "follow up needed", "fu/ rec date", "dossier", "designation", "recommendation", "blurb",
    "via", "pr contact", "guest eval", "verdict", "comments", "notes", "country",
}

NAME_HDR = re.compile(
    r"^(name|guest|guest name|founder name|founder\s*@\s*company|name\s*@\s*company|"
    r"founder\s*/\s*company|founder\s*/\s*ceo|column 1|founder\(s\)|linkedin link|host name)$")
FIRST_HDR = re.compile(r"^first\s*name$")
LAST_HDR = re.compile(r"^last\s*name$")
COMPANY_HDR = re.compile(r"^(company|co name|org name|companyname|protocol name|podcastname)$")
EMAIL_HDR = re.compile(r"e-?mail")
SECONDARY_EMAIL_HDR = re.compile(r"other e-?mail|general contact")
LINKEDIN_HDR = re.compile(r"linked\s*in")
STATUS_HDR = re.compile(r"^(status|s|contact status)$")
VERDICT_HDR = re.compile(r"verdict|guest eval|recommendation")
APPROVAL_HDR = re.compile(r"approval|ad review|review status")
VIA_HDR = re.compile(r"^(via|pr contact)$")
FOLLOWUP_HDR = re.compile(
    r"^(follow\s*up\s*\d+|followup\s*\d+|fu\s*\d+|nxt fu date|fu/ ?rec date|last fu date|dates|"
    r"initial mail.*|li|follow up|fu date|date of last contact)$")
ACTION_HDR = re.compile(r"next action|comment|last conversation|follow up needed|^notes$|^fd$")

VERDICT_RE = re.compile(
    r"(book immediately|strong consider|evaluate after call|pre-?call needed|precall needed|"
    r"decline[d]?|tier\s*\d)", re.I)
VERDICT_CANON = {
    "book immediately": "Book immediately", "strong consider": "Strong consider",
    "evaluate after call": "Evaluate after call", "pre-call needed": "Pre-call needed",
    "precall needed": "Pre-call needed", "decline": "Decline", "declined": "Decline",
}

LEGAL_WORDS = {"pvt", "private", "ltd", "limited", "inc", "llc", "llp", "corp", "co", "the",
               "technologies", "technology", "tech", "labs", "lab", "group", "holdings", "gmbh",
               "sa", "ag", "bv", "plc", "foundation", "network", "protocol", "ai", "hq"}
TITLE_RE = re.compile(
    r"\b(ceo|cto|coo|cfo|cmo|md|vp|founder|co-founder|cofounder|director|head|president|partner|"
    r"officer|chief|manager|lead|chairman|chairperson|representative|leader|is the)\b", re.I)
TLD_RE = re.compile(r"\.(ai|com|io|in|co|xyz|fi|me|app|so|vc|tech|net|org|finance|money|fund|uk|sg)\b")


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def is_blank(v) -> bool:
    return v is None or v is False or (isinstance(v, str) and not v.strip())


def cf(v) -> str:
    return re.sub(r"\s+", " ", str(v or "")).strip().casefold()


def fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    return "".join(ch for ch in s if not unicodedata.combining(ch))


def looks_like_date_text(s: str) -> bool:
    return bool(re.match(r"^\s*\d{1,2}[/\-.]\d{1,2}[/\-.]\d{2,4}", s))


def source_label(path: Path) -> str:
    return re.sub(r"^[0-9a-f]{6,}-", "", path.stem)


def norm_name(s: str) -> str:
    s = fold(s)
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"^(dr|mr|ms|mrs|prof)\.?\s+", "", s.strip(), flags=re.I)
    s = re.sub(r"[^A-Za-z\s\-']", " ", s).replace("-", " ").replace("'", "")
    return re.sub(r"\s+", " ", s).strip().lower()


def name_key(n: str) -> str:
    toks = [t for t in n.split() if len(t) > 1]
    if len(toks) < 2:
        return ""
    return f"{toks[0]} {toks[-1]}"


def norm_company(s: str) -> str:
    s = fold(str(s or "")).lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = s.split("|")[0].split(",")[0]
    s = TLD_RE.sub(" ", s)
    toks = [t for t in re.sub(r"[^a-z0-9\s]", " ", s).split() if t not in LEGAL_WORDS]
    return "".join(toks)


def linkedin_slug(url: str) -> str:
    m = LI_RE.search(url or "")
    if not m:
        return ""
    return unquote(m.group(1)).strip().lower().rstrip("/")


def parse_name_cell(raw: str):
    """Return (format tags, [person names], company or '', role hint or '')."""
    s = re.sub(r"\s+", " ", str(raw)).strip()
    tags = []
    if re.search(r"\|\s*linked\s*in", s, re.I):
        tags.append("LinkedIn page title pasted (Name - Co | LinkedIn)")
    if re.search(r"\|\s*x account", s, re.I):
        tags.append("X page title pasted")
    if "http" in s or "linkedin.com" in s:
        tags.append("URL text inside name cell")
    if s.isupper() and len(s) > 4:
        tags.append("ALL CAPS")
    if "(" in s:
        tags.append("parenthetical alias/role")
    s2 = re.sub(r"\|\s*(linked\s*in|x account).*$", "", s, flags=re.I).strip(" |")
    company, role = "", ""
    left = s2
    if " @ " in s2 or re.search(r"\S@\S", s2):
        tags.append("Name @ Company" if " @ " in s2 else "Name@Company (no spaces)")
        parts = [p.strip() for p in s2.split("@")]
        left = parts[0]
        if len(parts) > 2:
            role = parts[1]
        company = parts[-1]
    elif re.search(r"\s[-\u2013\u2014]\s", s2):
        tags.append("Name - Company")
        left, company = [p.strip() for p in re.split(r"\s[-\u2013\u2014]\s", s2, maxsplit=1)]
    elif " | " in s2:
        tags.append("Name | Company")
        left, company = [p.strip() for p in s2.split(" | ", 1)]
    elif "," in s2:
        tags.append("Name, Title, Company (free text)")
        parts = [p.strip() for p in s2.split(",") if p.strip()]
        left = parts[0]
        company = re.sub(r"^.*\bof\s+", "", parts[-1]) if len(parts) > 1 else ""
    else:
        tags.append("Name only")
    left = re.sub(r"\s[-\u2013\u2014]\s.*$", "", left)
    people = []
    for part in re.split(r"\s+&\s+|\s+and\s+|\s*/\s*|,\s+", left):
        part = part.strip(" ,")
        if not part or TITLE_RE.search(part) or len(part.split()) > 4:
            continue
        people.append(part)
    if not people and left.strip():
        people = [left.split(",")[0].strip()]
    if len(people) > 1:
        tags.append("multiple people in one cell")
    return tags, people, company, role


def classify_email_cell(text: str):
    """Return (list of dicts with email + flags, set of marker tags)."""
    out, markers = [], set()
    t = str(text)
    if cf(t) in PLACEHOLDER_EMAILS:
        markers.add(f"placeholder '{cf(t)}'")
        return out, markers
    if "(verified)" in t.lower():
        markers.add("(verified)")
    if "†" in t:
        markers.add("dagger (address of another person)")
    if re.search(r"\(check|\bor\b", t, re.I):
        markers.add("alternatives / caveat text")
    found = EMAIL_RE.findall(t)
    if len(found) > 1:
        markers.add("multiple emails in one cell")
    if found and t != t.strip():
        markers.add("leading/trailing whitespace")
    for m in found:
        idx = t.find(m)
        prefix = t[max(0, idx - 12):idx]
        local, _, domain = m.lower().partition("@")
        flags = {
            "email": m.lower().strip(".'"),
            "role": local in ROLE_LOCALPARTS,
            "pr": bool(re.search(r"\bPR\b", prefix)),
            "dagger": "†" in t,
            "freemail": domain in FREEMAIL_DOMAINS,
            "academic": bool(re.search(r"\.edu$|\.ac\.[a-z]{2}$|mpg\.de$|ethz\.ch$", domain)),
        }
        if flags["role"]:
            markers.add("role inbox (press@/ir@/info@...)")
        if flags["pr"]:
            markers.add("PR contact email inside guest email cell")
        if flags["freemail"]:
            markers.add("personal freemail address")
        if flags["academic"]:
            markers.add("academic address")
        out.append(flags)
    if not found and t.strip():
        markers.add("non-email text in email column")
    return out, markers


# --------------------------------------------------------------------------- #
# Sheet reading
# --------------------------------------------------------------------------- #
def cell_link(c) -> str:
    if c.hyperlink is None:
        return ""
    return c.hyperlink.target or c.hyperlink.location or ""


def is_header_row(values) -> bool:
    hits = sum(1 for v in values if isinstance(v, str) and cf(v) in HEADER_VOCAB)
    return hits >= 2 and not any(isinstance(v, str) and EMAIL_RE.search(v) for v in values)


def detect_header(rows):
    for i, r in enumerate(rows[:8]):
        vals = [c.value for c in r]
        strs = [v for v in vals if isinstance(v, str) and v.strip()]
        if len(strs) >= 2 and (is_header_row(vals) or any(
                re.search(r"name|status|email|follow|company|guest|founder|podcast", cf(v)) for v in strs)):
            return i
    return 0


def assign_roles(headers, sample_rows):
    """Map column index -> role, based on header text (and a little content sniffing)."""
    roles = {}
    hdr = [cf(h) if isinstance(h, str) else "" for h in headers]

    def url_share(j):
        vals = [r[j].value for r in sample_rows if j < len(r) and isinstance(r[j].value, str)]
        return sum(1 for v in vals if URL_RE.match(v)) / max(1, len(vals))

    name_col = None
    for j, h in enumerate(hdr):
        if NAME_HDR.match(h) and url_share(j) < 0.5:
            name_col = j
            break
    first = next((j for j, h in enumerate(hdr) if FIRST_HDR.match(h)), None)
    last = next((j for j, h in enumerate(hdr) if LAST_HDR.match(h)), None)
    if name_col is None and first is not None:
        roles[first], roles[last] = "first_name", "last_name"
    elif name_col is not None:
        roles[name_col] = "name"
    for j, h in enumerate(hdr):
        if j in roles or not h:
            continue
        if COMPANY_HDR.match(h):
            roles[j] = "company"
        elif EMAIL_HDR.search(h):
            roles[j] = "email_secondary" if SECONDARY_EMAIL_HDR.search(h) else "email"
        elif LINKEDIN_HDR.search(h):
            roles[j] = "linkedin"
        elif STATUS_HDR.match(h):
            roles[j] = "status"
        elif VERDICT_HDR.search(h):
            roles[j] = "verdict"
        elif APPROVAL_HDR.search(h):
            roles[j] = "host_approval"
        elif VIA_HDR.match(h):
            roles[j] = "via"
        elif FOLLOWUP_HDR.match(h) or re.match(r"^\d{1,2}-[a-z]{3}$", h):
            roles[j] = "followup"
        elif ACTION_HDR.search(h):
            roles[j] = "action_note"
        elif h in ("or", "type", "outreach channel", "mode of contact"):
            roles[j] = "channel"
    # Unnamed column directly right of a follow-up column holding dates = implicit next follow-up
    for j, h in enumerate(hdr):
        if (not h or h == "none") and j - 1 in roles and roles[j - 1] == "followup":
            vals = [r[j].value for r in sample_rows if j < len(r) and not is_blank(r[j].value)]
            if vals and sum(isinstance(v, dt.datetime) for v in vals) / len(vals) > 0.6:
                roles[j] = "followup_unlabelled"
    return roles


def read_tab(ws):
    rows = [r for r in ws.iter_rows()]
    hidx = detect_header(rows)
    headers = [c.value for c in rows[hidx]] if rows else []
    body = rows[hidx + 1:]
    width = 0
    for r in rows:
        for j, c in enumerate(r):
            if not is_blank(c.value):
                width = max(width, j + 1)
    return hidx, headers[:width], body, width


# --------------------------------------------------------------------------- #
# Profiling
# --------------------------------------------------------------------------- #
def profile_tab(source, ws, as_of):
    hidx, headers, body, width = read_tab(ws)
    nonempty = [r for r in body if any(not is_blank(c.value) for c in r[:width])]
    roles = assign_roles(headers, nonempty[:200])
    p = {
        "source": source, "tab": ws.title, "header_row": hidx + 1, "width": width,
        "rows_nonempty": 0, "rows_named": 0, "rows_unnamed_or_notes": 0,
        "embedded_header_rows": 0, "hyperlinks": 0, "columns": [],
        "name_formats": collections.Counter(), "email_markers": collections.Counter(),
        "status": {}, "verdicts": collections.Counter(), "host_approval": collections.Counter(),
        "followup": {"columns": 0, "date_cells": 0, "text_cells": 0, "future_dated": 0,
                     "text_values": collections.Counter(), "max_depth": collections.Counter()},
        "via": collections.Counter(), "bool_columns": {}, "unlabelled_columns_with_data": 0,
        "data_validation_lists": [],
    }
    for d in ws.data_validations.dataValidation:
        f1 = (d.formula1 or "")
        if f1.startswith('"'):
            p["data_validation_lists"].append(f1.strip('"').split(","))

    records = []
    cur_roles, cur_headers = roles, headers
    fill = collections.Counter()
    for r in body:
        vals = [c.value for c in r[:width]]
        if all(is_blank(v) for v in vals):
            continue
        if is_header_row(vals):
            p["embedded_header_rows"] += 1
            cur_headers = vals
            cur_roles = assign_roles(vals, [])
            continue
        p["rows_nonempty"] += 1
        p["hyperlinks"] += sum(1 for c in r[:width] if c.hyperlink is not None)
        for j, v in enumerate(vals):
            if not is_blank(v):
                fill[j] += 1
                if j >= len(cur_headers) or is_blank(cur_headers[j]) or cf(cur_headers[j]) == "none":
                    p["unlabelled_columns_with_data"] += 1
        rec = {"source": source, "tab": ws.title, "row": r[0].row, "people": [], "company": "",
               "emails": [], "linkedin": set(), "status": [], "verdict": [], "via": ""}
        fu_depth = 0
        for j, role in cur_roles.items():
            if j >= len(r):
                continue
            c = r[j]
            v = c.value
            link = cell_link(c)
            if role in ("name", "linkedin") and link:
                slug = linkedin_slug(link)
                if slug:
                    rec["linkedin"].add(slug)
            if is_blank(v):
                continue
            sv = str(v).strip()
            if role == "name":
                tags, people, company, _ = parse_name_cell(sv)
                if not re.search(r"not disclosed", sv, re.I):
                    rec["people"] = people
                for t in tags:
                    p["name_formats"][t] += 1
                if company:
                    rec["company"] = company
            elif role == "first_name":
                last = r[j + 1].value if j + 1 < len(r) else ""
                lcol = next((k for k, rr in cur_roles.items() if rr == "last_name"), None)
                last = r[lcol].value if lcol is not None and lcol < len(r) else last
                rec["people"] = [f"{sv} {last or ''}".strip()]
                p["name_formats"]["split First / Last columns"] += 1
            elif role == "company" and not rec["company"]:
                rec["company"] = sv
            elif role in ("email", "email_secondary"):
                found, markers = classify_email_cell(sv)
                for m in markers:
                    p["email_markers"][m] += 1
                for f in found:
                    f["secondary"] = role == "email_secondary"
                    rec["emails"].append(f)
            elif role == "channel" and EMAIL_RE.search(sv):
                found, markers = classify_email_cell(sv)
                p["email_markers"]["email stored in outreach-channel column"] += 1
                for f in found:
                    f["secondary"] = False
                    rec["emails"].append(f)
            elif role == "linkedin":
                slug = linkedin_slug(sv)
                if slug:
                    rec["linkedin"].add(slug)
            elif role == "status":
                key = f"{cur_headers[j]} (col {j + 1})"
                p["status"].setdefault(key, collections.Counter())[sv] += 1
                # ALL_CAPS_WITH_UNDERSCORES values are data-verification flags, not pipeline status
                if not re.fullmatch(r"[A-Z_]{3,}", sv):
                    rec["status"].append(sv)
            elif role == "host_approval":
                p["host_approval"][f"{cur_headers[j]}={sv}"] += 1
            elif role == "via":
                p["via"][sv] += 1
                rec["via"] = sv
            elif role in ("followup", "followup_unlabelled"):
                if isinstance(v, (dt.datetime, dt.date)):
                    p["followup"]["date_cells"] += 1
                    fu_depth += 1
                    if (v.date() if isinstance(v, dt.datetime) else v) > as_of:
                        p["followup"]["future_dated"] += 1
                elif isinstance(v, (int, float)) and not isinstance(v, bool):
                    p["followup"]["text_cells"] += 1
                    p["followup"]["text_values"]["(bare number)"] += 1
                else:
                    p["followup"]["text_cells"] += 1
                    label = "(date typed as text) " + sv[:20] if looks_like_date_text(sv) else sv[:60]
                    p["followup"]["text_values"][label] += 1
        # content-sniffed eval verdicts: verdict columns plus unlabelled / odd columns whose
        # display text starts with a verdict phrase (status and note columns are skipped)
        skip = {k for k, rr in cur_roles.items() if rr not in ("verdict",)}
        for j, c in enumerate(r[:width]):
            v = c.value
            if isinstance(v, str) and j not in skip:
                m = VERDICT_RE.match(v.strip())
                if m and len(v.strip()) < 90:
                    canon = VERDICT_CANON.get(m.group(1).lower(), m.group(1).title())
                    p["verdicts"][canon] += 1
                    rec["verdict"].append(canon)
        p["followup"]["max_depth"][fu_depth] += 1
        if rec["people"]:
            p["rows_named"] += 1
            rec["linkedin"] = sorted(rec["linkedin"])
            records.append(rec)
        else:
            p["rows_unnamed_or_notes"] += 1
    p["followup"]["columns"] = sum(1 for rr in roles.values() if rr.startswith("followup"))
    for j, h in enumerate(headers):
        n = fill.get(j, 0)
        p["columns"].append({"header": str(h) if h else "", "role": roles.get(j, ""),
                             "filled": n, "fill_pct": round(100 * n / max(1, p["rows_nonempty"]))})
    # checkbox (boolean) columns = milestone trackers
    for j, h in enumerate(headers):
        vals = [r[j].value for r in body if j < len(r) and r[j].value is not None]
        if vals and all(isinstance(v, bool) for v in vals):
            p["bool_columns"][str(h)] = sum(1 for v in vals if v)
    return p, records


# --------------------------------------------------------------------------- #
# Identity resolution
# --------------------------------------------------------------------------- #
class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.p[b] = a


def explode(records):
    """One entry per named person (multi-person cells are split)."""
    people = []
    for r in records:
        for nm in r["people"]:
            n = norm_name(nm)
            if not n:
                continue
            people.append({**r, "name_raw": nm, "name_norm": n, "name_key": name_key(n),
                           "company_norm": norm_company(r["company"]),
                           "multi": len(r["people"]) > 1})
    return people


def match_keys(p, stage):
    keys = []
    if stage >= 1 and not p["multi"]:
        for e in p["emails"]:
            if not (e["role"] or e["pr"] or e["dagger"] or e["secondary"]):
                keys.append("e:" + e["email"])
    if stage >= 2 and not p["multi"]:
        keys += ["l:" + s for s in p["linkedin"]]
    if stage >= 3 and p["name_key"] and p["company_norm"]:
        keys.append(f"n:{p['name_key']}|{p['company_norm']}")
    if stage >= 4 and p["name_key"]:
        keys.append(f"o:{p['name_norm']}")
    return keys


def resolve(people, stage):
    uf = UF(len(people))
    seen = {}
    for i, p in enumerate(people):
        for k in match_keys(p, stage):
            if k in seen:
                uf.union(seen[k], i)
            else:
                seen[k] = i
    clusters = collections.defaultdict(list)
    for i in range(len(people)):
        clusters[uf.find(i)].append(i)
    return list(clusters.values())


def cross_stats(people):
    out = {"person_mentions": len(people)}
    labels = {1: "email", 2: "email+linkedin", 3: "email+linkedin+name&company",
              4: "upper bound: +same full name only"}
    final = None
    for st in (1, 2, 3, 4):
        cl = resolve(people, st)
        out[f"unique_after_{labels[st]}"] = len(cl)
        if st == 3:
            final = cl
    multi_tab = [c for c in final if len({(people[i]["source"], people[i]["tab"]) for i in c}) > 1]
    multi_src = [c for c in final if len({people[i]["source"] for i in c}) > 1]
    out["people_in_2plus_tabs"] = len(multi_tab)
    out["people_in_2plus_sources"] = len(multi_src)
    out["max_tabs_for_one_person"] = max((len({(people[i]["source"], people[i]["tab"]) for i in c})
                                          for c in final), default=0)
    pair = collections.Counter()
    for c in multi_tab:
        tabs = sorted({f"{people[i]['source']}/{people[i]['tab']}" for i in c})
        for a in range(len(tabs)):
            for b in range(a + 1, len(tabs)):
                pair[(tabs[a], tabs[b])] += 1
    out["top_tab_overlaps"] = [[a, b, n] for (a, b), n in pair.most_common(15)]
    # conflict signals inside merged clusters
    emails_per = [len({e["email"] for i in c for e in people[i]["emails"]
                       if not (e["role"] or e["pr"] or e["dagger"] or e["secondary"])}) for c in final]
    out["clusters_with_2plus_personal_emails"] = sum(1 for n in emails_per if n > 1)
    status_conf = 0
    for c in multi_tab:
        sts = {cf(s) for i in c for s in people[i]["status"] if s}
        if len(sts) > 1:
            status_conf += 1
    out["multi_tab_people_with_conflicting_status"] = status_conf
    out["within_tab_duplicate_people"] = sum(
        1 for c in final
        if len(c) > len({(people[i]["source"], people[i]["tab"]) for i in c}))
    # shared addresses (one email on 2+ different names)
    by_email = collections.defaultdict(set)
    for p in people:
        for e in p["emails"]:
            by_email[e["email"]].add(p["name_norm"])
    out["emails_shared_by_2plus_names"] = sum(1 for v in by_email.values() if len(v) > 1)
    return out, final


# --------------------------------------------------------------------------- #
# Via / PR contacts
# --------------------------------------------------------------------------- #
def via_stats(tab_profiles):
    cnt = collections.Counter()
    kinds = collections.Counter()
    for p in tab_profiles:
        for raw, n in p["via"].items():
            s = re.sub(r"\s+", " ", str(raw)).strip()
            low = s.lower()
            if re.match(r"^cold\s*lead", low):
                kinds["cold lead"] += n
                continue
            if low in ("inbound", "outbound"):
                kinds[low] += n
                continue
            if low.startswith("referred by"):
                kinds["referral (Referred by X @ Y)"] += n
                s = s[len("referred by"):].strip()
            else:
                kinds["named PR / intro contact"] += n
            s = PHONEISH_RE.sub("", s)
            s = EMAIL_RE.sub("", s)
            s = re.split(r"\s[-|]\s|\|", s)[0]
            key = norm_name(s)
            if key:
                cnt[key] += n
    return {
        "kinds": dict(kinds),
        "distinct_contacts": len(cnt),
        "recurring_2plus": sum(1 for v in cnt.values() if v >= 2),
        "recurring_5plus": sum(1 for v in cnt.values() if v >= 5),
        "max_rows_for_one_contact": max(cnt.values(), default=0),
        "rows_covered_by_recurring": sum(v for v in cnt.values() if v >= 2),
        "_counter": cnt,
    }


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def jsonable(o):
    if isinstance(o, collections.Counter):
        return dict(o.most_common())
    if isinstance(o, set):
        return sorted(o)
    if isinstance(o, dict):
        return {str(k): jsonable(v) for k, v in o.items() if not str(k).startswith("_")}
    if isinstance(o, (list, tuple)):
        return [jsonable(x) for x in o]
    return o


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("raw_dir", help="folder holding the .xlsx exports (e.g. data/raw)")
    ap.add_argument("--json", help="write aggregate stats JSON here")
    ap.add_argument("--private-dir", help="write person-level CSVs here (contains personal data)")
    ap.add_argument("--as-of", default=dt.date.today().isoformat(), help="date for future-dated follow-ups")
    ap.add_argument("--exclude-tabs", default="Sheet2",
                    help="comma list of tabs that are not people lists (templates etc.)")
    ap.add_argument("--non-guest-tabs", default="Podcast Leads,pod Campaign",
                    help="people tabs that are not guests (e.g. other podcasts' hosts); profiled, "
                         "but kept out of guest identity resolution")
    a = ap.parse_args(argv)
    as_of = dt.date.fromisoformat(a.as_of)
    excl = {t.strip() for t in a.exclude_tabs.split(",") if t.strip()}
    nonguest = {t.strip() for t in a.non_guest_tabs.split(",") if t.strip()}

    files = sorted(Path(a.raw_dir).glob("*.xlsx"))
    if not files:
        sys.exit(f"no .xlsx files in {a.raw_dir}")
    profiles, guest_records, other_records = [], [], []
    for f in files:
        wb = openpyxl.load_workbook(f, data_only=True)  # read-only use; never saved
        for ws in wb.worksheets:
            prof, recs = profile_tab(source_label(f), ws, as_of)
            prof["excluded"] = ws.title in excl
            prof["non_guest"] = ws.title in nonguest
            profiles.append(prof)
            if ws.title in excl:
                continue
            (other_records if ws.title in nonguest else guest_records).extend(recs)

    people = explode(guest_records)
    cross, clusters = cross_stats(people)
    cross["named_rows_guest_tabs"] = len(guest_records)
    cross["named_rows_non_guest_tabs"] = len(other_records)
    cross["multi_person_cells"] = sum(1 for r in guest_records if len(r["people"]) > 1)
    vs = via_stats(profiles)

    status_all = collections.Counter()
    for p in profiles:
        for col, c in p["status"].items():
            for k, n in c.items():
                status_all[k.strip()] += n

    summary = {"as_of": a.as_of, "tabs": profiles, "cross": cross, "via": vs,
               "distinct_status_values": status_all}
    # ---- stdout report (aggregates only) ----
    print(f"{'source':<18} {'tab':<24} {'hdr':>3} {'rows':>5} {'named':>5} {'FUcols':>6} {'FUdate':>6} {'FUtext':>6}")
    for p in profiles:
        flag = " (excluded)" if p["excluded"] else (" (non-guest)" if p["non_guest"] else "")
        f = p["followup"]
        print(f"{p['source']:<18} {p['tab']:<24} {p['header_row']:>3} {p['rows_nonempty']:>5} "
              f"{p['rows_named']:>5} {f['columns']:>6} {f['date_cells']:>6} {f['text_cells']:>6}{flag}")
    print("\nCross-source identity:")
    for k, v in cross.items():
        if k != "top_tab_overlaps":
            print(f"  {k}: {v}")
    print("  top tab overlaps:")
    for a_, b_, n in cross["top_tab_overlaps"]:
        print(f"    {n:>4}  {a_}  <->  {b_}")
    print("\nVia / PR contacts:", {k: v for k, v in vs.items() if not k.startswith("_")})
    print("\nDistinct status values:", len(status_all))
    for k, n in status_all.most_common():
        print(f"  {n:>5}  {k}")

    if a.json:
        Path(a.json).write_text(json.dumps(jsonable(summary), indent=1, default=str))
    if a.private_dir:
        d = Path(a.private_dir)
        d.mkdir(parents=True, exist_ok=True)
        with open(d / "people.csv", "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["cluster", "source", "tab", "row", "name_raw", "company", "emails",
                        "email_flags", "linkedin", "status", "verdict", "via"])
            for ci, c in enumerate(sorted(clusters, key=len, reverse=True)):
                for i in c:
                    p = people[i]
                    w.writerow([ci, p["source"], p["tab"], p["row"], p["name_raw"], p["company"],
                                ";".join(e["email"] for e in p["emails"]),
                                ";".join(",".join(k for k in ("role", "pr", "dagger", "secondary",
                                                              "freemail", "academic") if e[k])
                                         for e in p["emails"]),
                                ";".join(p["linkedin"]), "|".join(p["status"]), "|".join(p["verdict"]),
                                p["via"]])
        with open(d / "via.csv", "w", newline="") as fh:
            w = csv.writer(fh)
            for k, n in vs["_counter"].most_common():
                w.writerow([k, n])
    return 0


if __name__ == "__main__":
    sys.exit(main())
