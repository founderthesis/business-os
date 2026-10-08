"""Build the FT Network rows from the WhatsApp group doc extract.

Usage:
  python3 -I migration/whatsapp_network.py sql      # print People-matching SQL (name lists)
  python3 -I migration/whatsapp_network.py matches  # people_by_*.txt -> people_matches.json
  python3 -I migration/whatsapp_network.py build    # build rows, batches, review CSV, counts

Inputs:
  data/raw/whatsapp/blurbs_2026-10-08.json                 parsed doc (never edited)
  data/fixes/whatsapp_network_oneliners*.json|tsv          hand-written one-liners and company fills
                                                           (tsv: raw_index, one-liner, company, doc company to override)
  data/out/whatsapp_network/people_by_name.txt             People rows pulled from Notion by exact name:
                                                           "<page id> <Y|N FT guest> <name>[|<organisation>]"
  data/out/whatsapp_network/people_by_org.txt              same format, People linked to the companies of
                                                           first-name-only rows
  data/out/whatsapp_network/loaded_names.txt               optional: "|"-separated FT Network names already
                                                           in Notion (batch whatsapp-doc-2026-10-08); batches skip them
Outputs (data/out/whatsapp_network/): rows.json, batch_NN.json, counts.json
Review list: data/review/whatsapp_network_review.csv
Re-runnable; no Notion writes here.
"""
import csv, json, os, re, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data/raw/whatsapp/blurbs_2026-10-08.json")
FIXDIR = os.path.join(ROOT, "data/fixes")
OUT = os.path.join(ROOT, "data/out/whatsapp_network")
MATCH = os.path.join(OUT, "people_matches.json")
LOADED = os.path.join(OUT, "loaded_names.txt")
REVIEW = os.path.join(ROOT, "data/review/whatsapp_network_review.csv")
BATCH = "whatsapp-doc-2026-10-08"
CAPTURED = "2026-10-08"

# same person listed twice in the doc under different spellings: {dropped raw_index: kept raw_index}
FOLD = {451: 393}   # "Anurakt" (Klub, Pending Invites, struck) = "Anurukt Jain" (Klub, intro blurb)
LABEL_ROWS = {"CynLR", "Giottus founders"}          # not people
NAME_COMPANY_SPLIT = {                             # "first-name Company" written in one cell
    "Dilip Modi DigiSpice": ("Dilip Modi", "DigiSpice"),
    "Nipun Likeminds": ("Nipun", "Likeminds"),
    "Ranjeet Pratilipi": ("Ranjeet", "Pratilipi"),
    "Prateek Mindler": ("Prateek", "Mindler"),
    "Bhavin Patel LenDenClub": ("Bhavin Patel", "LenDenClub"),
}

# first-name rows whose matched People name is not a clean full name
KEEP_FIRST_NAME = {"306", "398", "396", "454"}

NAME_FIX = {"VIknesh Jain": "Viknesh Jain"}   # typos in the doc

def clean_name(n):
    n = NAME_FIX.get(n.strip(), n)
    n = re.sub(r"\s+aka\s+.*$", "", n.strip())
    n = re.sub(r"^Dr\.?\s+", "", n)
    return re.sub(r"\s+", " ", n).strip()

def key(n):
    return clean_name(n).lower()

def clean_blurb(b):
    b = b.replace("**", "")
    b = re.sub(r"\s?\u00f0\u009f[^\sA-Za-z0-9.,!?)]*", "", b)   # broken emoji bytes from the doc export
    return re.sub(r"[ \t]{2,}", " ", b).strip()

def norm_url(u):
    if not u: return None
    u = u.strip()
    return u if u.startswith("http") else "https://" + u.lstrip("/")

def load():
    d = json.load(open(RAW))
    assert len(d) == 474, len(d)
    return d

def base_rows(d):
    rows, skipped, merged = [], [], []
    by_idx = {r["raw_index"]: r for r in d}
    for r in d:
        if r["name"] in LABEL_ROWS:
            skipped.append((r, "Label, not a person"))
            continue
        if r["duplicate_of"] is not None:
            merged.append((r, f"Same blurb as raw row {r['duplicate_of']}"))
            continue
        if r["raw_index"] in FOLD:
            merged.append((dict(r, duplicate_of=FOLD[r["raw_index"]]), f"Same person as raw row {FOLD[r['raw_index']]} (spelling differs)"))
            continue
        name, company = r["name"], r["company"]
        notes = []
        if name in NAME_COMPANY_SPLIT:
            name, company = NAME_COMPANY_SPLIT[name]
            notes.append(f'Doc wrote "{r["name"]}"; split into name and company')
        cn = clean_name(name)
        if cn != name:
            notes.append(f'Doc wrote "{name}"')
        rows.append(dict(raw=r, name=cn, company=company, notes=notes))
    # fold duplicates: keep LinkedIn if only the duplicate had it
    for r, _ in merged:
        keep = next(x for x in rows if x["raw"]["raw_index"] == r["duplicate_of"])
        if not keep["raw"]["linkedin"] and r["linkedin"]:
            keep["raw"] = dict(keep["raw"], linkedin=r["linkedin"])
    return rows, skipped, merged

def membership(r):
    if r.get("status_conflict"):
        return "Added", "Doc conflict: " + r["status_conflict"]
    ls = r["list_status"]
    if ls == "non_joiners": return "Declined", None
    if ls == "to_be_added": return "To invite", None
    if ls == "not_joined_yet": return "Invited", None
    if ls == "pending_invites" and not r["added"]: return "Invited", None
    if r["added"]: return "Added", None
    return "Invited", "Status unclear in doc"

def cmd_sql():
    d = load()
    rows, _, _ = base_rows(d)
    full = sorted({key(x["name"]) for x in rows if len(x["name"].split()) >= 2})
    first = sorted({(x["name"].lower(), (x["company"] or "")) for x in rows if len(x["name"].split()) < 2})
    esc = lambda s: s.replace("'", "''")
    print("FULL", len(full))
    print(",".join(f"'{esc(n)}'" for n in full))
    print("FIRST", len(first))
    print(json.dumps(first))

def load_fixes():
    """One-liner and company fixes, keyed by raw_index (str). Later files win."""
    fixes = {}
    for f in sorted(os.listdir(FIXDIR)):
        if not f.startswith("whatsapp_network_oneliners"): continue
        path = os.path.join(FIXDIR, f)
        if f.endswith(".json"):
            fixes.update(json.load(open(path)))
        elif f.endswith(".tsv"):
            for line in open(path, encoding="utf-8"):
                if not line.strip(): continue
                idx, one, company, old = (line.rstrip("\n").split("\t") + ["", "", ""])[:4]
                fx = {"one_liner": one}
                if company and old: fx["company_override"] = company
                elif company: fx["company"] = company
                fixes[idx] = fx
    return fixes

def read_people(path):
    out = []
    for line in open(path, encoding="utf-8"):
        if not line.strip(): continue
        pid, ft, rest = line.rstrip("\n").split(" ", 2)
        name, _, orgs = rest.partition("|")
        out.append({"id": pid, "ft": ft == "Y", "name": name, "orgs": orgs, "ms": "Clean"})
    return out

def cmd_matches():
    """Turn the People pulls into people_matches.json: exact full-name candidates, and
    first-name + company candidates (first name equals a word of the People name)."""
    d = load()
    rows, _, _ = base_rows(d)
    fixes = load_fixes()
    full = defaultdict(list)
    for p in read_people(os.path.join(OUT, "people_by_name.txt")):
        full[key(p["name"])].append(p)
    by_org = read_people(os.path.join(OUT, "people_by_org.txt"))
    first = {}
    for x in rows:
        if len(x["name"].split()) >= 2: continue
        idx = str(x["raw"]["raw_index"])
        company = x["company"] or fixes.get(idx, {}).get("company")
        fn = x["name"].lower()
        cands = [p for p in by_org if org_match(company, p["orgs"])
                 and fn in re.sub(r"\(.*?\)", "", p["name"]).lower().replace(".", " ").split()]
        if cands: first[idx] = cands
    json.dump({"full": full, "first": first}, open(MATCH, "w"), indent=1)
    print("full names with candidates", len(full), "first-name rows with candidates", len(first))

def norm_org(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower().replace("technologies", "").replace("pvt", "").replace("ltd", ""))

def org_match(company, orgs):
    c = norm_org(company)
    if not c: return False
    for o in (orgs or "").split(" / "):
        o = norm_org(o)
        if o and (o == c or (len(c) >= 4 and (c in o or o in c))):
            return True
    return False

def cmd_build():
    d = load()
    rows, skipped, merged = base_rows(d)
    fixes = load_fixes()
    matches = json.load(open(MATCH))   # {"full": {key: [cand]}, "first": {"first|company": [cand]}}
    out, review = [], []
    for x in rows:
        r = x["raw"]; idx = str(r["raw_index"])
        fx = fixes.get(idx, {})
        notes = list(x["notes"])
        review_flag = False
        mem, mnote = membership(r)
        if mnote: notes.append(mnote); review_flag = True
        company = x["company"]
        if fx.get("company_override") and fx["company_override"] != company:
            notes.append(f'Doc listed company as "{company}"; set to the current venture from the blurb')
            company = fx["company_override"]
        if not company and fx.get("company"):
            company = fx["company"]; notes.append("Company read from the blurb")
            review_flag = True
        if not company:
            notes.append("No company"); review_flag = True
        if len(x["name"].split()) < 2:
            notes.append("First name only"); review_flag = True
        # People link
        person, ft = None, False
        if len(x["name"].split()) >= 2:
            cands = [c for c in matches["full"].get(key(x["name"]), []) if c["ms"] != "Merged into another row"]
            if len(cands) > 1 and company:
                narrowed = [c for c in cands if org_match(company, c["orgs"])]
                if len(narrowed) == 1: cands = narrowed
            if len(cands) == 1:
                person, ft = cands[0]["id"], cands[0]["ft"]
            elif len(cands) > 1:
                notes.append(f"{len(cands)} People rows share this name"); review_flag = True
            else:
                folded = [k for k, v in FOLD.items() if v == r["raw_index"]]
                fc = [c for k in folded for c in matches["first"].get(str(k), [])]
                if len(fc) == 1:
                    person, ft = fc[0]["id"], fc[0]["ft"]
                    notes.append(f'Linked to People row "{fc[0]["name"]}" (doc spells it two ways)'); review_flag = True
                else:
                    notes.append("No People match"); review_flag = True
        else:
            cands = matches["first"].get(idx, [])
            cands = [c for c in cands if c["ms"] != "Merged into another row"]
            if len(cands) == 1:
                person, ft = cands[0]["id"], cands[0]["ft"]
                full = cands[0]["name"]
                if idx in KEEP_FIRST_NAME:
                    notes.append(f"Linked by first name + company to the People row \"{full}\"")
                else:
                    notes.append(f'Doc wrote "{x["name"]}"; full name taken from the People row matched on first name + company')
                    x["name"] = full
            elif len(cands) > 1:
                notes.append(f"{len(cands)} People rows match first name + company")
            else:
                notes.append("No People match")
        blurb = clean_blurb(r["blurb"]) if r["blurb"] else None
        typ = {"founder": "Founder", "investor": "Investor"}.get(r["role_guess"], "Other")
        source = "FT guest" if ft else ("Group intro" if blurb else "Doc list")
        one = fx.get("one_liner")
        if blurb and not one:
            notes.append("One-liner missing"); review_flag = True
        row = {
            "raw_index": r["raw_index"], "Name": x["name"], "Company": company,
            "One-liner": one, "Blurb": blurb, "LinkedIn": r["linkedin"],
            "Membership": mem, "Type": typ, "Source": source,
            "Needs review": review_flag, "Review note": "; ".join(notes) or None,
            "Person": person, "Migration batch": BATCH,
        }
        out.append(row)
        if review_flag:
            review.append([r["raw_index"], x["name"], company or "", mem, row["Review note"]])
    for r, why in skipped + merged:
        review.append([r["raw_index"], r["name"], r["company"] or "", "SKIPPED", why])
    os.makedirs(OUT, exist_ok=True)
    json.dump(out, open(os.path.join(OUT, "rows.json"), "w"), indent=1, ensure_ascii=False)
    with open(REVIEW, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["raw_index", "name", "company", "membership", "note"]); w.writerows(review)
    # Notion page payloads, 50 per batch
    pages = []
    for row in out:
        p = {"Name": row["Name"], "Membership": row["Membership"], "Type": row["Type"],
             "Source": row["Source"], "Needs review": "__YES__" if row["Needs review"] else "__NO__",
             "Migration batch": BATCH, "date:Captured:start": CAPTURED, "date:Captured:is_datetime": 0}
        for k in ("Company", "One-liner", "Blurb", "Review note"):
            if row[k]: p[k] = row[k]
        if row["LinkedIn"]: p["LinkedIn"] = norm_url(row["LinkedIn"])
        if row["Person"]: p["Person"] = [row["Person"]]
        pages.append({"properties": p})
    loaded = set(open(LOADED).read().strip().split("|")) if os.path.exists(LOADED) else set()
    pages = [p for p in pages if p["properties"]["Name"] not in loaded]
    for f in os.listdir(OUT):
        if f.startswith("batch_"): os.remove(os.path.join(OUT, f))
    for i in range(0, len(pages), 50):
        json.dump(pages[i:i+50], open(os.path.join(OUT, f"batch_{i//50:02d}.json"), "w"), ensure_ascii=False)
    counts = {
        "extract_rows": len(d), "loaded": len(out), "skipped_labels": len(skipped), "merged_duplicates": len(merged),
        "membership": Counter(r["Membership"] for r in out), "type": Counter(r["Type"] for r in out),
        "source": Counter(r["Source"] for r in out),
        "linked": sum(1 for r in out if r["Person"]), "unlinked": sum(1 for r in out if not r["Person"]),
        "needs_review": sum(1 for r in out if r["Needs review"]),
        "already_in_notion": len(out) - len(pages), "to_load": len(pages),
    }
    assert counts["loaded"] + counts["skipped_labels"] + counts["merged_duplicates"] == len(d)
    json.dump(counts, open(os.path.join(OUT, "counts.json"), "w"), indent=1)
    print(json.dumps(counts, indent=1))

if __name__ == "__main__":
    {"sql": cmd_sql, "matches": cmd_matches, "build": cmd_build}[sys.argv[1]]()
