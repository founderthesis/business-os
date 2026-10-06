"""Second half of the un# migration: match candidates to live Notion, then build the write payloads.

Usage:
  python migration/un_pipeline_write.py sql N        print the match SQL for chunk N (60 candidates each)
  python migration/un_pipeline_write.py orgsql N     print the Organisation lookup SQL for chunk N
  python migration/un_pipeline_write.py plan         read the saved match results, write payloads and the written log

Reads (git-ignored):
  data/out/un_pipeline/candidates.json               from migration/un_pipeline.py
  data/raw/notion/un_matches_2026-10-06.txt          match SQL results, one line per hit: sid|person|has_email|has_li|org|eng|eng_status
  data/raw/notion/un_orgs_2026-10-06.txt             org lookup results, one line per hit: company_key|org
Writes:
  data/out/un_pipeline/{people_new,engagements_new,engagements_update,people_update}.json
  data/review/un_pipeline_written.csv

Matching: LinkedIn slug, then exact name (case-folded). A name hit on more than one person goes to review, never merged.
An existing un# Engagement for the guest is updated, never regressed: Form filled and agent rows with a later status keep
theirs, and only empty fields are filled.
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data/out/un_pipeline"
PEOPLE = "collection://e6c44319-7f81-4da6-8b80-8441a4875d7a"
ENGS = "collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5"
ORGS = "collection://c43c280a-3b37-4821-96ef-dab688a53aea"
UN_SHOW = "3ed19a301a7f8111b5e4d46002a7afe1"
CHUNK = 60


def q(s):
    return "'" + s.replace("'", "''") + "'"


def cands():
    return json.load(open(OUT / "candidates.json"))


def keys(c):
    """Every (name, slug) pair worth trying for a candidate: each guest name, the CRM name."""
    names = [n for n in c["people"]] + ([c["crm"]["name"]] if c.get("crm") and c["crm"].get("name") else [])
    seen, out = set(), []
    for n in names:
        k = " ".join(n.lower().split())
        if k and " " in k and k not in seen:  # a single first name is too weak to match on
            seen.add(k)
            out.append(k)
    return out or [""], (c.get("li_slug") or "").lower()


def match_sql(n):
    rows = []
    for c in cands()[n * CHUNK:(n + 1) * CHUNK]:
        names, slug = keys(c)
        for nm in names:
            rows.append(f"SELECT {q(c['source_id'])} AS sid, {q(nm)} AS nm, {q(slug)} AS slug")
    # The Notion SQL parser has no VALUES clause, so the key list is a UNION ALL of literal rows.
    return f'''WITH c AS ({" UNION ALL ".join(rows)})
SELECT c.sid || '|' || substr(p.url,-32) || '|' || (CASE WHEN p.Email IS NOT NULL AND p.Email <> '' THEN 1 ELSE 0 END)
 || '|' || (CASE WHEN p.LinkedIn IS NOT NULL AND p.LinkedIn <> '' THEN 1 ELSE 0 END)
 || '|' || coalesce(substr(p.Organisation, -34, 32), '') || '|' || coalesce(substr(e.url,-32), '') || '|' || coalesce(e.Status, '') AS m
FROM c JOIN "{PEOPLE}" p
 ON ((c.slug <> '' AND rtrim(lower(p.LinkedIn), '/') || '/' LIKE '%/in/' || c.slug || '/%') OR (c.nm <> '' AND lower(trim(p.Name)) = c.nm))
 AND p.Name NOT LIKE 'DELETE:%'
LEFT JOIN "{ENGS}" e ON e.Show LIKE '%{UN_SHOW}%' AND e.Guest LIKE '%' || substr(p.url,-32) || '%'
GROUP BY m ORDER BY m'''


def org_sql(n):
    comps = sorted({" ".join((c.get("company") or "").lower().split()) for c in cands()} - {""})
    chunk = comps[n * 90:(n + 1) * 90]
    vals = " UNION ALL ".join(f"SELECT {q(x)} AS k" for x in chunk)
    return f'''WITH c AS ({vals})
SELECT c.k || '|' || substr(o.url,-32) AS m FROM c JOIN "{ORGS}" o ON lower(trim(o.Name)) = c.k AND o.Name NOT LIKE 'DELETE:%' ORDER BY m'''


RAWN = ROOT / "data/raw/notion"
REVIEW = ROOT / "data/review"
BATCH = "un-pipeline-2026-10-06"
TODAY = "2026-10-06"
SHOW_NAME = "alpha un#"
LADDER = ["New", "Contacted", "Interested", "Decision pending", "Precall requested", "Precall done", "Sponsored offered",
          "Booking", "Booked", "Recorded", "Form filled"]
# Hand-settled matches after reading the review list: source id -> existing un# Engagement id.
ENG_FIX = {
    "un# Pipeline/v2/68": "3ed19a301a7f81528f00f1e9c22667d4",   # Sid Powell = Sidney Powell @ Maple, recorded
    "un# Pipeline/v2/144": "3ed19a301a7f81bdaf6cd3b748980e38",  # Ajeet Khurrana, typo of Ajeet Khurana
    "un# Pipeline/v2/154": "3ed19a301a7f8101837bddab90478e14",  # Marcos Viriato, Rayls episode
    "un# Pipeline/v2/145": "3ed19a301a7f8101837bddab90478e14",  # Alex Buelau, same Rayls episode
    "un# Pipeline/v2/156": "3ed19a301a7f8192809ee0c14b52d56b",  # Matthew Hougan = "Matt @ Bitwise"
    "un# Pipeline/old/7": "3ed19a301a7f81619bcfc566f9634d55",   # Aleksandar Mitrovic = Alexander Mitrovich
}
# Hand-settled person matches: source id -> People id (or "" to force a new person).
PERSON_FIX = {
    "un# Pipeline/v2/68": "3ed19a301a7f81a485dcc5c75e05cfd4",
    "un# Pipeline/v2/144": "3ed19a301a7f8131b25cda3c6e96c977",
    "un# Pipeline/v2/154": "3ed19a301a7f819eaf66d9dc24da7ce4",  # the Blue row holds both guests; split by hand
    "un# Pipeline/v2/145": "",
    "un# Pipeline/v2/156": "3ed19a301a7f81a1ac87f0c2f62f7efd",
    "un# Pipeline/old/7": "3ed19a301a7f819cbefad9e0fc1f62f0",
}
# People rows whose name is a stub the sheet completes.
RENAME = {"3ed19a301a7f81a1ac87f0c2f62f7efd": "Matthew Hougan"}
# Rows already covered by another candidate on the same Engagement.
SKIP = {"un# Pipeline/defillama/47": "Sidney Powell, recorded; v2/68 carries the sheet data"}


def lines(path):
    if not path.exists():
        return []
    return [x.strip() for x in path.read_text().splitlines() if x.strip() and not x.startswith("#")]


def load_matches():
    hits = {}
    for f in sorted((ROOT / "data/raw/notion").glob("un_matches_2026-10-06*.txt")):
        for ln in lines(f):
            sid, pid, he, hli, org, eng, est = (ln.split("|") + [""] * 7)[:7]
            hits.setdefault(sid, {}).setdefault(pid, {"has_email": he == "1", "has_li": hli == "1", "org": org,
                                                      "engs": {}})
            if eng:
                hits[sid][pid]["engs"][eng] = est
    return hits


def load_engs():
    out = {}
    for ln in lines(RAWN / "un_engagements_2026-10-06.txt"):
        eid, status, source, flags = ln.split("|")
        names = ["eval", "dossier", "host", "direction", "nextdate", "nextaction", "route", "verdict", "org"]
        out[eid] = {"status": status, "source": source, **{n: f == "1" for n, f in zip(names, flags)}}
    return out


def load_orgs():
    out = {}
    for f in sorted(RAWN.glob("un_orgs_2026-10-06*.txt")):
        for ln in lines(f):
            k, oid = ln.split("|")
            out.setdefault(ckey(k), []).append(oid)
    return out


def strip_marks(s):
    return re.sub(r"[\u200b-\u200f\u202a-\u202e\ufeff]", "", s or "").strip()


def ckey(s):
    return " ".join(strip_marks(s).lower().split())


def body(c, existing=False):
    head = "From the un# Pipeline sheet (6 Oct 2026)" + (", added to an existing row" if existing else "")
    out = [f"## {head}", "", f"- Rows: {', '.join(x.split('/', 1)[1] for x in c['source_ids'])}"]
    if c.get("raw_status"):
        out.append(f"- Sheet status: {c['raw_status']}")
    if c.get("via_name"):
        out.append(f"- Via as written: {c['via_name']}")
    if c.get("via_agency"):
        out.append(f"- PR agency: {c['via_agency']}")
    if len(c["people"]) > 1:
        out.append(f"- Guests on the row: {', '.join(c['people'])}")
    for n in c["notes"]:
        out.append(f"- {n}")
    if c.get("next_action"):
        out.append(f"- Next action (sheet): {c['next_action']}")
    return "\n".join(out)


def own_email(name, emails):
    """The CRM tab lists the guest, their PR people and colleagues in one cell, in no fixed order. Only an address
    whose local part carries the guest's first or last name is theirs; the rest go to review, never onto the person."""
    toks = [t for t in re.split(r"[^a-z]+", ckey(name)) if len(t) >= 3]
    mine = [e for e in emails if any(t in e.split("@")[0].lower() for t in toks)]
    return (mine[0] if mine else None), [e for e in emails if e not in mine[:1]]


def plan():
    cs = cands()
    hits, engs, orgs = load_matches(), load_engs(), load_orgs()
    review, written = [], []
    orgs_new, people_new, people_upd, eng_new, eng_upd = {}, [], [], [], []
    for c in cs:
        sid = c["source_id"]
        if sid in SKIP:
            written.append([sid, c["raw_name"], "skip", "", "", c["status"], SKIP[sid]])
            continue
        # all source rows of the candidate share its hits (the SQL used the head row's source id)
        h = hits.get(sid, {})
        pids = list(h)
        if sid in PERSON_FIX:
            pids = [PERSON_FIX[sid]] if PERSON_FIX[sid] else []
        with_eng = [p for p in pids if p in h and h[p]["engs"]]
        if len(pids) > 1 and len(with_eng) == 1:
            pids = with_eng
        if len(pids) > 1:
            review.append([sid, c["raw_name"], "name matches several People; created nothing, pick one", " ".join(pids)])
            continue
        pid = pids[0] if pids else None
        hit = h.get(pid, {}) if pid else {}
        if pid and not hit:
            hit = {"has_email": True, "has_li": True, "org": None, "engs": {}}  # hand match: fill nothing blind
        # organisation: the person's, else an exact name match, else a new one
        oid = hit.get("org") or None
        comp = ckey(c.get("company"))
        if not oid and comp and not PERSON_FIX.get(sid):
            found = orgs.get(comp, [])
            if len(found) == 1:
                oid = found[0]
            elif len(found) > 1:
                review.append([sid, c["raw_name"], "company name matches several Organisations; used the first", " ".join(found)])
                oid = found[0]
            else:
                orgs_new.setdefault(comp, {"properties": {
                    "Name": strip_marks(c["company"]), "Source": "Migration", "Source ID": f"{sid}/org", "Migration batch": BATCH,
                    "date:Captured:start": TODAY}})
                oid = f"new-org:{comp}"
        crm = c.get("crm") or {}
        name = c["people"][0] if c["people"] else (crm.get("name") or c["raw_name"])
        if not pid:
            props = {"Name": name, "Source": "Migration", "Source ID": sid, "Migration batch": BATCH,
                     "date:Captured:start": TODAY, "Match status": "Clean",
                     "Tags": json.dumps(["Guest" if c["status"] in ("Recorded", "Form filled") else "un# guest pipeline"])}
            if c.get("li_url"):
                props["LinkedIn"] = c["li_url"]
            mine, others = own_email(name, crm.get("emails", []))
            if mine:
                props["Email"] = mine
            if others:
                review.append([sid, c["raw_name"], "CRM addresses that are not the guest's (PR or colleagues); add as Stakeholders if they still matter", str(len(others))])
            if crm.get("role"):
                props["Role"] = crm["role"]
            if crm.get("phone"):
                props["Phone"] = crm["phone"]
            people_new.append({"properties": props, "org": oid})
            pid = f"new-person:{sid}"
        else:
            upd = {}
            if c.get("li_url") and not hit.get("has_li"):
                upd["LinkedIn"] = c["li_url"]
            mine, _ = own_email(name, crm.get("emails", []))
            if mine and not hit.get("has_email"):
                upd["Email"] = mine
            if not hit.get("org") and oid:
                upd["org"] = oid
            if pid in RENAME:
                upd["Name"] = RENAME[pid]
            if upd:
                people_upd.append({"page_id": pid, "properties": upd, "source": sid})
        # engagement: an existing un# one for this guest, else new
        eids = list(hit.get("engs", {})) if hit else []
        if sid in ENG_FIX:
            eids = [ENG_FIX[sid]]
        if len(eids) > 1:
            review.append([sid, c["raw_name"], "guest has several un# Engagements; updated none", " ".join(eids)])
            continue
        if eids:
            eid = eids[0]
            e = engs.get(eid, {})
            props = {}
            # status: only ever forward on Migration rows below Form filled; agent rows and Form filled keep theirs
            if e.get("source") == "Migration" and e.get("status") != "Form filled" and c["status"] in LADDER \
                    and e.get("status") in LADDER and LADDER.index(c["status"]) > LADDER.index(e["status"]):
                props["Status"] = c["status"]
            for flag, field, value in (("eval", "Eval link", c.get("eval_link")),
                                       ("dossier", "Dossier link", c.get("dossier_link")),
                                       ("host", "Host verdict", c.get("host_verdict")),
                                       ("direction", "Direction", c.get("direction")),
                                       ("route", "Tier", c.get("route")),  # Route folded into Tier, decision 74
                                       ("verdict", "Eval verdict", c.get("eval_verdict"))):
                if value and not e.get(flag):
                    props[field] = value
            eng_upd.append({"page_id": eid, "properties": props, "content": body(c, existing=True), "source": sid,
                            "existing_status": e.get("status")})
            written.append([sid, c["raw_name"], "update", eid, e.get("status"), c["status"], ""])
            continue
        title = f"{name} @ {c['company']}, {SHOW_NAME}" if c.get("company") else f"{name}, {SHOW_NAME}"
        props = {"Name": title, "Status": c["status"], "Source": "Migration", "Source ID": sid, "Migration batch": BATCH,
                 "date:Captured:start": TODAY}
        for field, key in (("Direction", "direction"), ("Tier", "route"), ("Host verdict", "host_verdict"),
                           ("Eval verdict", "eval_verdict"), ("Eval link", "eval_link"), ("Dossier link", "dossier_link"),
                           ("Next action", "next_action")):
            if c.get(key):
                props[field] = c[key]
        if c.get("next_date"):
            props["date:Next date:start"] = c["next_date"]
        eng_new.append({"properties": props, "content": body(c), "guest": pid, "org": oid})
        written.append([sid, c["raw_name"], "create", "", "", c["status"], pid if not pid.startswith("new") else "new person"])
    for name, data in (("orgs_new", list(orgs_new.values())), ("people_new", people_new), ("people_update", people_upd),
                       ("engagements_new", eng_new), ("engagements_update", eng_upd)):
        json.dump(data, open(OUT / f"{name}.json", "w"), indent=1, ensure_ascii=False)
    with open(REVIEW / "un_pipeline_match_review.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source", "name", "issue", "detail"])
        w.writerows(review)
    with open(REVIEW / "un_pipeline_written.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source", "name", "action", "engagement", "status before", "sheet status", "guest"])
        w.writerows(written)
    import collections
    print(f"candidates {len(cs)}: engagements new {len(eng_new)}, updated {len(eng_upd)}, held for review {len(review)}")
    print(f"people new {len(people_new)}, people filled {len(people_upd)}, organisations new {len(orgs_new)}")
    print("new engagement status", dict(collections.Counter(e["properties"]["Status"] for e in eng_new)))
    print("updates that move status", sum(1 for e in eng_upd if "Status" in e["properties"]),
          " updates by existing status", dict(collections.Counter(e["existing_status"] for e in eng_upd)))


def created(kind):
    """Source ID -> page id for rows this batch created, saved from a Notion query after each create step."""
    return dict(ln.split("|") for ln in lines(RAWN / f"un_created_{kind}_2026-10-06.txt"))


def write_batches(kind, size):
    """Create-pages payloads with every relation resolved to a real page id."""
    orgs_c = {ckey(sid.rsplit("/org", 1)[0]): pid for sid, pid in created("orgs").items()} if kind != "orgs" else {}
    org_by_name = {}
    if kind != "orgs":
        for o in json.load(open(OUT / "orgs_new.json")):
            org_by_name[ckey(o["properties"]["Name"])] = created("orgs").get(o["properties"]["Source ID"])
    people_c = created("people") if kind == "engagements" else {}

    def org_id(ref):
        if not ref:
            return None
        if ref.startswith("new-org:"):
            oid = org_by_name.get(ref.split(":", 1)[1])
            if not oid:
                raise SystemExit(f"organisation not created yet: {ref}")
            return oid
        return ref

    pages = []
    if kind == "orgs":
        pages = json.load(open(OUT / "orgs_new.json"))
    elif kind == "people":
        for x in json.load(open(OUT / "people_new.json")):
            props = dict(x["properties"])
            oid = org_id(x["org"])
            if oid:
                props["Organisation"] = [oid]
            pages.append({"properties": props})
    elif kind == "engagements":
        for x in json.load(open(OUT / "engagements_new.json")):
            props = dict(x["properties"])
            g = x["guest"]
            gid = people_c.get(g.split(":", 1)[1]) if g.startswith("new-person:") else g
            if not gid:
                raise SystemExit(f"guest not created yet: {g}")
            props["Guest"] = [gid]
            props["Show"] = [UN_SHOW]
            oid = org_id(x["org"])
            if oid:
                props["Organisation"] = [oid]
            pages.append({"properties": props, "content": x["content"]})
    d = OUT / "batches"
    d.mkdir(exist_ok=True)
    for old in d.glob(f"{kind}_*.json"):
        old.unlink()
    for i in range(0, len(pages), size):
        json.dump(pages[i:i + size], open(d / f"{kind}_{i // size + 1:02d}.json", "w"), ensure_ascii=False)
    print(f"{kind}: {len(pages)} pages in {(len(pages) + size - 1) // size} batches of {size}")


def write_updates():
    """update-page payloads: People gaps, then existing un# Engagements (properties, then a note appended to the body)."""
    orgs = created("orgs")
    org_by_name = {ckey(o["properties"]["Name"]): orgs.get(o["properties"]["Source ID"])
                   for o in json.load(open(OUT / "orgs_new.json"))}
    out = []
    for x in json.load(open(OUT / "people_update.json")):
        props = {k: v for k, v in x["properties"].items() if k != "org"}
        ref = x["properties"].get("org")
        if ref:
            props["Organisation"] = [org_by_name[ref.split(":", 1)[1]] if ref.startswith("new-org:") else ref]
        if props:
            out.append({"page_id": x["page_id"], "properties": props})
    for x in json.load(open(OUT / "engagements_update.json")):
        out.append({"page_id": x["page_id"], "properties": x["properties"], "append": x["content"]})
    json.dump(out, open(OUT / "batches" / "updates.json", "w"), ensure_ascii=False, indent=0)
    print(f"updates: {len(out)} pages")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "sql":
        print(match_sql(int(sys.argv[2])))
    elif cmd == "orgsql":
        print(org_sql(int(sys.argv[2])))
    elif cmd == "plan":
        plan()
    elif cmd == "batches":
        write_batches(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 50)
    elif cmd == "updates":
        write_updates()
