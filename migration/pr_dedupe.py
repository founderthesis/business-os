"""Find duplicate PR contacts in People and propose flags for a human to resolve (decision 53).

Usage:
  python migration/pr_dedupe.py            build the export, the pairs CSV and the Notion updates file
  python migration/pr_dedupe.py --snap D   use snapshots saved on date D (default 2026-10-05)

Reads (saved Notion SQL results, one row each with 'rows' = fields joined by \\x1f, rows joined by \\x1e):
  data/raw/notion/pr_people_query_{SNAP}.json   scope rows from People:
      id, createdTime, Name, Email, Other emails, Organisation ids, Tags, Match status, Source, Migration batch,
      Source ID, LinkedIn, n Brought in (Via), n Stakeholder on, n Engagements (Guest), Duplicate check
  data/raw/notion/pr_people_links_{SNAP}.json   id, engagement ids from Brought in + Stakeholder on + Engagements
  data/raw/notion/orgs_query_{SNAP}.json        Organisations: id, Name, Domain, Type
  data/raw/notion/pr_engagements_query_{SNAP}.json  Engagements with a Via or Stakeholder: id, Guest ids, Organisation ids
  Scope: Tags has "PR contact" or "Role inbox", or the person is Via (Brought in) or a Stakeholder on any Engagement.
  The SQL used is in the comment block at the bottom of this file.

Writes:
  data/out/pr_dedupe/pr_people.json      every scoped person, parsed
  data/review/pr_dedupe_pairs.csv        every candidate pair, Strong, Medium and Weak
  data/out/pr_dedupe/updates.json        Notion property updates for duplicates in Strong and Medium pairs only

Rules
  Strong: same email in Email or Other emails (case-insensitive).
  Strong: same normalised full name and same email domain (not free mail) or same Organisation.
  Medium: one name is a first-name-only or initial form of the other, same email domain or Organisation.
          A sheet name like "Ananya Teamwork" counts its last word as the agency when it matches the other row's
          domain or organisation and the row has no agency of its own.
  Medium: same full name, different or missing organisation (PR people move agencies).
  Weak:   compatible names where agency cannot be compared because one side has no domain or organisation.
          The reason says when both rows work engagements for the same guest or guest company (a hint, not proof).
          CSV only, never written to Notion.
  A role inbox is never paired with a person.

Keeper: the row with an email, then the oldest (createdTime, which follows migration order). The other row gets
Duplicate of = keeper, Match status = Possible duplicate and a one-line Duplicate check. Nothing is merged or deleted:
Akshay decides (decision 53). Re-run safely; rows already pointing at the same keeper are skipped.
"""
import argparse
import csv
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw/notion"
OUT = ROOT / "data/out/pr_dedupe"
REVIEW = ROOT / "data/review"
PAGE = "https://app.notion.com/p/"

EMAIL = re.compile(r"[A-Za-z0-9._%+'-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
FREE_MAIL = {"gmail.com", "googlemail.com", "yahoo.com", "yahoo.co.in", "outlook.com", "hotmail.com", "live.com",
             "icloud.com", "me.com", "rediffmail.com", "protonmail.com", "proton.me", "aol.com", "ymail.com"}
ROLE_WORDS = {"pr", "press", "media", "comms", "communications", "communication", "marketing", "info", "hello",
              "contact", "team", "admin", "support", "office", "partnerships", "brand", "social", "news", "corpcomm",
              "publicrelations", "events", "mediarelations"}
HONORIFICS = {"dr", "mr", "mrs", "ms", "miss", "mx", "prof", "professor", "ca", "adv", "sir", "shri", "smt", "sri"}
FIELDS = ["id", "created", "name", "email", "other_emails", "org_ids", "tags", "match_status", "source", "batch",
          "source_id", "linkedin", "n_via", "n_stakeholder", "n_guest", "duplicate_check"]
STRENGTH_ORDER = {"Strong": 0, "Medium": 1, "Weak": 2}


def load_rows(path):
    res = json.load(open(path))["results"][0]
    rows = [r.split("\x1f") for r in res["rows"].split("\x1e")] if res.get("rows") else []
    assert len(rows) == int(res["n"]), f"{path.name}: {len(rows)} rows parsed, query said {res['n']}"
    return rows


def fold(s):
    return unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()


def name_tokens(name):
    toks = re.sub(r"[^a-z0-9 ]", " ", fold(name).replace(".", " ")).split()
    toks = [t for t in toks if not t.isdigit()]
    while toks and toks[0] in HONORIFICS:
        toks = toks[1:]
    return toks


def domain_stem(domain):
    parts = domain.lower().split(".")
    while len(parts) > 2 and parts[-2] in {"co", "com", "org", "net", "ac", "gov"}:
        parts = parts[:-2] + [parts[-1]]
    return parts[-2] if len(parts) >= 2 else parts[0]


def emails_of(p):
    return {e.lower().strip(".") for e in EMAIL.findall(f"{p['email']} {p['other_emails']}")}


def build_people(snap):
    orgs = {r[0]: {"name": r[1], "domain": (r[2] or "").lower().removeprefix("www."), "type": r[3]}
            for r in load_rows(RAW / f"orgs_query_{snap}.json")}
    links = {r[0]: sorted({x.strip() for x in r[1].split(",") if x.strip()})
             for r in load_rows(RAW / f"pr_people_links_{snap}.json")}
    engs = {r[0]: [x for x in (r[1] + "," + r[2]).split(",") if x] for r in load_rows(RAW / f"pr_engagements_query_{snap}.json")}
    people = []
    for r in load_rows(RAW / f"pr_people_query_{snap}.json"):
        p = dict(zip(FIELDS, r))
        p["url"] = PAGE + p["id"]
        p["tags"] = [t for t in p["tags"].split(",") if t]
        p["org_ids"] = [o for o in p["org_ids"].split(",") if o]
        p["org_names"] = [orgs[o]["name"] for o in p["org_ids"] if o in orgs]
        for k in ("n_via", "n_stakeholder", "n_guest"):
            p[k] = int(p[k] or 0)
        p["engagement_ids"] = links.get(p["id"], [])
        p["client_ids"] = sorted({c for e in p["engagement_ids"] for c in engs.get(e, [])})  # guests and guest companies served
        p["emails"] = sorted(emails_of(p))
        doms = {e.split("@", 1)[1] for e in p["emails"]}
        p["domains"] = sorted(d for d in doms if d not in FREE_MAIL)
        p["domains"] += sorted({orgs[o]["domain"] for o in p["org_ids"] if o in orgs and orgs[o]["domain"]} - set(p["domains"]))
        p["stems"] = sorted({domain_stem(d) for d in p["domains"]})
        p["org_keys"] = sorted({re.sub(r"[^a-z0-9]", "", fold(n)) for n in p["org_names"]} - {""})
        p["tokens"] = name_tokens(p["name"])
        locals_ = {e.split("@", 1)[0] for e in p["emails"]}
        p["role_inbox"] = "Role inbox" in p["tags"] or bool(locals_) and all(
            re.sub(r"[^a-z]", "", l) in ROLE_WORDS for l in locals_)
        people.append(p)
    return people


# ---------------------------------------------------------------- name comparison

def first_name_form(a, b):
    """a is a shorter form of b: 'Sharon' of 'Sharon Lucas', 'P Sharma' of 'Priya Sharma', 'Psharma' of 'Priya Sharma'."""
    if len(b) < 2 or a == b:
        return False
    if len(a) == 1:
        t = a[0]
        return t == b[0] or t in {b[0][0] + b[-1], b[0] + b[-1][0]}
    if len(a) == len(b):
        full_equal = 0
        for x, y in zip(a, b):
            if x == y:
                full_equal += len(x) > 1
            elif not (len(x) == 1 and y.startswith(x)):
                return False
        return full_equal >= 1
    if len(a) < len(b):  # 'Megha Bharti' of 'Megha S Bharti'
        return a[0] == b[0] and a[-1] == b[-1] and len(a) >= 2
    return False


def agency_hint(p, other):
    """For a row with no agency of its own, a trailing name word that matches the other row's agency."""
    if p["stems"] or p["org_ids"] or len(p["tokens"]) < 2:
        return None
    t = p["tokens"][-1]
    if len(t) < 3:
        return None
    keys = other["stems"] + other["org_keys"]
    if any(k.startswith(t) or (len(k) >= 4 and t.startswith(k)) for k in keys):
        return t
    return None


def compare(a, b):
    """-> (strength, reason, shorter) or None. 'shorter' is the row whose name is the short form, if any."""
    if a["role_inbox"] != b["role_inbox"]:
        return None
    if set(a["emails"]) & set(b["emails"]):
        return "Strong", "same email", None
    if a["role_inbox"]:
        return None
    same_org = bool(set(a["org_ids"]) & set(b["org_ids"]))
    same_dom = bool(set(a["stems"]) & set(b["stems"]))
    agency = "agency domain" if same_dom else "organisation" if same_org else None
    ta, tb = a["tokens"], b["tokens"]
    if not ta or not tb:
        return None
    # A sheet-style name "Ananya Teamwork": drop the agency word before comparing.
    ha, hb = agency_hint(a, b), agency_hint(b, a)
    if ha or hb:
        ta = ta[:-1] if ha else ta
        tb = tb[:-1] if hb else tb
        agency = "agency named in the sheet"
    full_a, full_b = "".join(ta), "".join(tb)
    multi = max(len(ta), len(tb)) >= 2
    if full_a == full_b and multi:
        if agency:
            return "Strong", f"same name and {agency}", None
        return "Medium", "same name, different or missing organisation", None
    if full_a == full_b:  # one word each: 'Deepa' and 'Deepa'
        if agency == "agency named in the sheet":
            return "Medium", "same first name; name ends with the agency in the other row's email domain", None
        if agency:
            return "Medium", f"same first name and {agency}", None
        return None
    short = a if first_name_form(ta, tb) else b if first_name_form(tb, ta) else None
    if not short:
        return None
    longer = b if short is a else a
    if agency:
        return "Medium", f"first-name form of {longer['name']} at same agency", short
    has_a = bool(a["stems"] or a["org_ids"])
    has_b = bool(b["stems"] or b["org_ids"])
    if has_a and has_b:
        return None  # both have an agency and they differ: different people
    if set(a["engagement_ids"]) & set(b["engagement_ids"]):
        where = "on the same engagement"
    elif set(a["client_ids"]) & set(b["client_ids"]):
        where = "both work the same guest or company, agency unknown on one side"
    else:
        where = "agency unknown on one side"
    return "Weak", f"first-name form of {longer['name']}, {where}", short


def keeper_order(p):
    return (0 if p["emails"] else 1, p["created"], p["id"])


def n_eng(p):
    return len(p["engagement_ids"])


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--snap", default="2026-10-05")
    args = ap.parse_args()

    people = build_people(args.snap)
    by_id = {p["id"]: p for p in people}
    OUT.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    json.dump(people, open(OUT / "pr_people.json", "w"), indent=1, ensure_ascii=False)

    batches = defaultdict(int)
    for p in people:
        batches[p["batch"] or p["source"] or "none"] += 1
    print(f"scope: {len(people)} people ({', '.join(f'{k} {v}' for k, v in sorted(batches.items()))})")
    print(f"  tagged PR contact {sum('PR contact' in p['tags'] for p in people)}, role inbox {sum(p['role_inbox'] for p in people)}, "
          f"Via on an engagement {sum(p['n_via'] > 0 for p in people)}, stakeholder {sum(p['n_stakeholder'] > 0 for p in people)}")

    # Block on keys that any rule needs, so the comparison stays linear-ish.
    blocks = defaultdict(set)
    for p in people:
        for e in p["emails"]:
            blocks["e:" + e].add(p["id"])
        if p["tokens"]:
            blocks["f:" + p["tokens"][0]].add(p["id"])
            blocks["n:" + "".join(p["tokens"])].add(p["id"])
            if len(p["tokens"]) >= 2:
                blocks["f:" + "".join(p["tokens"][:-1])].add(p["id"])  # 'Ananya Teamwork' -> 'ananya'
                blocks["n:" + "".join(p["tokens"][:-1])].add(p["id"])
                blocks["i:" + p["tokens"][0][0] + p["tokens"][-1]].add(p["id"])
                blocks["n:" + p["tokens"][0][0] + p["tokens"][-1]].add(p["id"])
                blocks["n:" + p["tokens"][0] + p["tokens"][-1][0]].add(p["id"])
            else:
                blocks["i:" + p["tokens"][0]].add(p["id"])
    candidates = set()
    for ids in blocks.values():
        ids = sorted(ids)
        for i, x in enumerate(ids):
            for y in ids[i + 1:]:
                candidates.add((x, y))

    pairs = []
    for x, y in sorted(candidates):
        if "Merged into another row" in (by_id[x]["match_status"], by_id[y]["match_status"]):
            continue
        hit = compare(by_id[x], by_id[y])
        if not hit:
            continue
        strength, reason, _ = hit
        keeper, dup = sorted([by_id[x], by_id[y]], key=keeper_order)
        pairs.append({"keeper": keeper, "dup": dup, "strength": strength, "reason": reason})

    # One Duplicate of per row. Strong and Medium pairs form clusters; each cluster has one keeper.
    parent = {}

    def find(a):
        parent.setdefault(a, a)
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    flag_pairs = [q for q in pairs if q["strength"] != "Weak"]
    for q in flag_pairs:
        parent[find(q["keeper"]["id"])] = find(q["dup"]["id"])
    clusters = defaultdict(list)
    for pid in list(parent):
        clusters[find(pid)].append(by_id[pid])
    best = {}
    for q in sorted(flag_pairs, key=lambda q: STRENGTH_ORDER[q["strength"]]):
        for a, b in ((q["keeper"], q["dup"]), (q["dup"], q["keeper"])):
            best.setdefault((a["id"], b["id"]), q)

    updates, flagged = [], {}
    for members in clusters.values():
        keeper = min(members, key=keeper_order)
        for m in sorted(members, key=keeper_order):
            if m is keeper:
                continue
            q = best.get((m["id"], keeper["id"]))
            if q:
                strength, reason = q["strength"], q["reason"]
            else:  # linked to the keeper only through another member
                via = next(o for o in members if (m["id"], o["id"]) in best)
                q2 = best[(m["id"], via["id"])]
                strength, reason = q2["strength"], f"{q2['reason']} (matched {via['name']}, who matches the keeper)"
            line = f"{reason}; keeper {keeper['name']} (pr_dedupe, 5 Oct)" if "keeper" not in reason else f"{reason} (pr_dedupe, 5 Oct)"
            if reason == "same email":
                line = f"same email as {keeper['name']} (pr_dedupe, 5 Oct)"
            flagged[m["id"]] = {"keeper": keeper, "strength": strength, "reason": reason}
            already = m["match_status"] == "Possible duplicate" and m["duplicate_check"]
            if not already:
                updates.append({"page_id": m["id"], "name": m["name"], "keeper": keeper["name"], "strength": strength,
                                "properties": {"Duplicate of": [keeper["url"]], "Match status": "Possible duplicate",
                                               "Duplicate check": line}})

    rows = []
    for q in sorted(pairs, key=lambda q: (STRENGTH_ORDER[q["strength"]], q["keeper"]["name"].lower())):
        k, d = q["keeper"], q["dup"]
        f = flagged.get(d["id"])
        applied = "yes" if f and f["keeper"]["id"] == k["id"] else ("via cluster keeper " + f["keeper"]["name"] if f else "no (weak)" if q["strength"] == "Weak" else "no")
        rows.append({"keeper_name": k["name"], "duplicate_name": d["name"], "reason": q["reason"], "strength": q["strength"],
                     "keeper_url": k["url"], "duplicate_url": d["url"], "keeper_engagements": n_eng(k),
                     "duplicate_engagements": n_eng(d), "keeper_batch": k["batch"] or k["source"],
                     "duplicate_batch": d["batch"] or d["source"], "flagged_in_notion": applied})
    with open(REVIEW / "pr_dedupe_pairs.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else ["keeper_name"])
        w.writeheader()
        w.writerows(rows)
    json.dump(updates, open(OUT / "updates.json", "w"), indent=1, ensure_ascii=False)

    counts = defaultdict(int)
    for q in pairs:
        counts[q["strength"]] += 1
    print(f"pairs: Strong {counts['Strong']}, Medium {counts['Medium']}, Weak {counts['Weak']} (total {len(pairs)})")
    reasons = defaultdict(int)
    for q in pairs:
        reasons[(q["strength"], re.sub(r" of .*? at", " of X at", re.sub(r"form of .*?,", "form of X,", q["reason"])))] += 1
    for (s, r), n in sorted(reasons.items(), key=lambda kv: (STRENGTH_ORDER[kv[0][0]], -kv[1])):
        print(f"  {s:6} {n:4}  {r}")
    print(f"clusters {len(clusters)}; rows to flag {len(flagged)} "
          f"(Strong {sum(f['strength'] == 'Strong' for f in flagged.values())}, Medium {sum(f['strength'] == 'Medium' for f in flagged.values())}); "
          f"updates to send {len(updates)}")
    print(f"wrote {OUT / 'pr_people.json'}, {REVIEW / 'pr_dedupe_pairs.csv'} ({len(rows)} rows), {OUT / 'updates.json'}")


if __name__ == "__main__":
    sys.exit(main())

# SQL used for the snapshots (People = collection://e6c44319-7f81-4da6-8b80-8441a4875d7a,
# Organisations = collection://c43c280a-3b37-4821-96ef-dab688a53aea). SCOPE is:
#   "Tags" LIKE '%PR contact%' OR "Tags" LIKE '%Role inbox%' OR json_array_length("Brought in")>0
#   OR json_array_length("Stakeholder on")>0
# ("Brought in" is the People side of Engagements.Via; 609 links on both sides on 5 Oct.)
#
# pr_people_query:
#   SELECT COUNT(*) AS n, group_concat(r, char(30)) AS rows FROM (SELECT substr(url,-32) || char(31) || createdTime
#   || char(31) || ifnull("Name",'') || char(31) || ifnull("Email",'') || char(31) || ifnull("Other emails",'')
#   || char(31) || <Organisation ids, prefix and JSON stripped> || char(31) || <Tags, JSON stripped>
#   || char(31) || ifnull("Match status",'') || char(31) || ifnull("Source",'') || char(31) || ifnull("Migration batch",'')
#   || char(31) || ifnull("Source ID",'') || char(31) || ifnull("LinkedIn",'')
#   || char(31) || ifnull(json_array_length("Brought in"),0) || char(31) || ifnull(json_array_length("Stakeholder on"),0)
#   || char(31) || ifnull(json_array_length("Engagements"),0) || char(31) || ifnull("Duplicate check",'') AS r
#   FROM People WHERE SCOPE ORDER BY createdTime, url)
# pr_engagements_query (Engagements = collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5):
#   SELECT COUNT(*) AS n, group_concat(substr(url,-32) || char(31) || <Guest ids> || char(31) || <Organisation ids>, char(30))
#   AS rows FROM Engagements WHERE json_array_length("Via")>0 OR json_array_length("Stakeholders")>0
# pr_people_links:
#   SELECT COUNT(*) AS n, group_concat(substr(url,-32) || char(31) || <Brought in, Stakeholder on, Engagements ids
#   joined by commas>, char(30)) AS rows FROM People WHERE SCOPE
# orgs_query:
#   SELECT COUNT(*) AS n, group_concat(substr(url,-32) || char(31) || ifnull("Name",'') || char(31)
#   || ifnull("Domain",'') || char(31) || ifnull("Type",''), char(30)) AS rows FROM Organisations
