"""Phase B (prep) of the Blue legacy transfer: builds the write files. Read-only: no Notion or Blue calls.

Usage: python migration/blue_legacy_phase_b.py

Reads (all git-ignored):
  data/blue_legacy/records_*.json, notion/*.json, comments_*.json, docs/index.json   Phase A extract
  data/blue_legacy/reread/                                                           Phase B re-reads from Blue
  data/blue_legacy/write/live_*.json|txt, stakeholder_resolution.json               drift-check observations taken from Notion
                                                                                     on 9 Nov (last 10 hex chars of page ids)
Writes data/blue_legacy/write/:
  01_schema.json .. 10b_body_data_optional.json   one list of exact operations per step
  drift_skips.csv, unwritten_name_matches.csv, blue_internal_conflicts.csv, summary.md

Rules (CTO answers, decision 533): data only, no files; Notion wins, never overwrite a non-empty cell; Source ID
"Blue <id>"; batch blue-legacy-2026-11-09 in the page body where a database has no Migration batch field.
Operation shapes (the writer maps each to one Notion call):
  add_property   {data_source, property, type}
  update_page    {page_id, properties}            property names are Notion names; dates as "date:<Name>:start"
  create_pages   {data_source, pages:[{properties, content}]}   up to 100 per call
  create_page    {parent, title, content}         parent is a page id or "$ARCHIVE" (the archive page made in step 8)
  append_body    {page_id, markdown}              appended, never replacing
"""
import csv
import html
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data/blue_legacy"
W = D / "write"
BATCH = "blue-legacy-2026-11-09"
TODAY = "2026-11-09"
EM = re.compile(r"[A-Za-z0-9._%+'-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
DS = {"episodes": "collection://5d250752-6db8-4ab6-8467-c68f5838278a",
      "people": "collection://e6c44319-7f81-4da6-8b80-8441a4875d7a",
      "orgs": "collection://c43c280a-3b37-4821-96ef-dab688a53aea",
      "engagements": "collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5",
      "activities": "collection://290f715d-fd45-4203-ade6-3642c2326c6c",
      "guest_forms": "collection://c8e770a4-c7ae-4b8a-bafe-9abf526853b2"}
SHOW_PAGE = {"FT": "https://app.notion.com/p/3ed19a301a7f817c9367e0d88afc5776",
             "AU": "https://app.notion.com/p/3ed19a301a7f8111b5e4d46002a7afe1",
             "B2S": "https://app.notion.com/p/3ed19a301a7f819e8f45de04a7c9d025",
             "HBD": "https://app.notion.com/p/3ed19a301a7f815585e7e6c8accaab23"}
SHOW_NAME = {"FT": "Founder Thesis", "AU": "un#", "B2S": "Built to Share", "HBD": "Human by Design"}
DEVELOPER_PAGE = "3fb19a301a7f81739c08e18ccf61e903"
WS_FILES = ["ft_spotlight", "alpha_un", "hissa_podcast", "fastcode_podcast", "episodes_inventory"]
FILL_COLS = {  # Notion Episodes property -> Blue columns, first non-empty wins
    "YouTube": ["Youtube Link", "YouTube Link", "You Tube Link"],
    "Spotify": ["Spotify Link", "Spofity Link"],
    "Apple": ["Apple Podcast", "Apple Podcast Link"],
    "Amazon Music": ["Amazon Music Link", "Amazon Music"],
    "Substack": ["Substack Published Page", "Substack Link", "Published Newsletter Link"],
    "Short link": ["podm.in Short Link", "short link", "Shortlink"],
    "Copywriting doc": ["Link to working doc", "Link to Working Doc", "Link to working Doc"],
    "LinkedIn": ["LI Announcement Post", "Sri's LI Announcement"],
}
SECTORS = {"fintech": "Fintech", "saas": "SaaS", "d2c": "D2C", "marketplace": "Marketplace", "deeptech": "Deeptech",
           "edtech": "Edtech", "healthtech": "Healthtech", "services": "Services", "gaming": "Gaming"}
PR_KEYS = ("Email ID (", "Other Email ID")

drift, internal_conflicts, unwritten = [], [], []


def sid10(url):
    return url.rstrip("/")[-10:]


def pid(url):
    return url.rstrip("/").rsplit("/", 1)[-1]


def jl(p):
    return json.load(open(p))


def clean_url(v):
    v = (v or "").strip().rstrip(",").strip()
    if not v or " " in v:
        return None
    if re.match(r"^https?://", v, re.I):
        return v
    if re.match(r"^[\w.-]+\.[a-z]{2,}(/|$)", v, re.I):
        return "https://" + v
    return None


def norm_key(s):
    s = re.sub(r"\s*@\s*", "@", (s or "").lower())
    return re.sub(r"[^a-z0-9@]", "", s)


def tokens(s):
    return {t for t in re.split(r"[^a-z]+", (s or "").lower()) if len(t) > 1}


def fval(r, cols):
    for c in cols:
        if r["fields"].get(c, "").strip():
            return r["fields"][c].strip()
    return ""


def drift_skip(step, target, prop, value, why):
    drift.append({"step": step, "target": target, "property": prop, "blue_value": value, "reason": why})


def write(name, ops):
    json.dump(ops, open(W / name, "w"), indent=1, ensure_ascii=False)
    return ops


def md_para(items):
    return "\n".join(items)


def main():
    W.mkdir(exist_ok=True)
    # ---- inputs
    recs = {w: jl(D / f"records_{w}.json") for w in WS_FILES}
    all_recs = [r for w in WS_FILES for r in recs[w]]
    eps = {e["url"]: e for e in jl(D / "notion/episodes_all.json")}
    eps_by10 = {sid10(u): u for u in eps}
    engp = {r["sid"].split(" ", 1)[1]: r for r in jl(D / "notion/engagements_people.json")}
    engb = {r["Source ID"].split(" ", 1)[1]: r for r in jl(D / "notion/engagements_blue.json")}
    live_ep = jl(W / "live_episodes_nonempty.json")
    live_ep_sets = {k: set(live_ep[k].split(",")) for k in ("Amazon Music", "Short link")}
    live_ep_unchanged = live_ep["counts_other"]
    live_people = {k: set(v.split(",")) for k, v in jl(W / "live_people_empty.json").items() if k in ("Email", "Role", "LinkedIn")}
    live_eng = jl(W / "live_engagements.json")
    dossier_empty = set(live_eng["dossier_empty"].split(","))
    sector_empty = set(open(W / "live_sector_empty.txt").read().strip().split(","))
    comments = jl(D / "comments_ft.json") + jl(D / "comments_un.json")
    rec_by_id = {r["blue_id"]: r for r in all_recs}
    existing_forms = {norm_key(n) for n in live_eng["guest_forms_existing_names"]}
    touched = defaultdict(lambda: {"kind": "", "name": "", "fills": [], "blue": set()})  # page id -> info (for step 10)

    # ---- 1 schema
    s1 = write("01_schema.json", [{"op": "add_property", "data_source": DS["orgs"], "property": "LinkedIn", "type": "url",
                                   "note": "Only new property (decision 533). Empty on all rows, so no drift possible."}])

    # ---- 2 organisations: LinkedIn
    org_vals = defaultdict(lambda: defaultdict(set))
    for r in all_recs:
        e = engb.get(r["blue_id"])
        if not e or not e.get("Organisation"):
            continue
        orgs = json.loads(e["Organisation"])
        if len(orgs) != 1:
            continue
        v = clean_url(fval(r, ["Organisation Linkedin Page Link", "Co LinkedIn Page", "Co LinkedIn Profile"]))
        if v and "linkedin.com" in v.lower():
            org_vals[orgs[0]][re.sub(r"^https?://(www\.)?", "", v.lower()).split("?")[0].rstrip("/")].add((v, r["blue_id"]))
    s2 = []
    for ourl, variants in sorted(org_vals.items()):
        if len(variants) > 1:
            internal_conflicts.append({"step": 2, "target": ourl, "property": "LinkedIn",
                                       "values": " | ".join(sorted(next(iter(x))[0] for x in variants.values()))})
            continue
        v, bid = sorted(next(iter(variants.values())))[0]
        v = v.split("?")[0]
        s2.append({"op": "update_page", "page_id": pid(ourl), "properties": {"LinkedIn": v}})
        t = touched[pid(ourl)]
        t.update(kind="Organisations", name=ourl)
        t["fills"].append("LinkedIn")
        t["blue"].add(bid)
    write("02_organisations_linkedin.json", s2)

    # ---- 3 people
    pc = defaultdict(lambda: defaultdict(set))  # person -> prop -> {(value, blue id)}
    people_skips = Counter()
    for r in all_recs:
        ed = engp.get(r["blue_id"])
        if not ed or not ed.get("guests"):
            continue
        gs = ed["guests"].split(" ;; ")
        if len(gs) != 1:
            people_skips["two_guests_on_engagement"] += 1
            continue
        g = (gs[0].split("|") + [""] * 6)[:6]
        purl, pname = g[0], g[1]
        bname = r["fields"].get("Guest Name", "")
        if bname and not (tokens(bname) & tokens(pname)):
            people_skips["blue_guest_name_differs_from_person"] += 1
            continue
        pr = set()
        for k, v in r["fields"].items():
            if k.startswith(PR_KEYS):
                pr.update(x.lower() for x in EM.findall(v))
        stake_emails = {x.lower() for x in EM.findall(ed.get("stake") or "")}
        bem = (r["fields"].get("Guest Email ID") or "").strip().lower()
        if bem and EM.fullmatch(bem):
            if bem in pr or bem in stake_emails:
                people_skips["guest_email_is_also_a_pr_or_stakeholder_address"] += 1  # decision 424: booker is not the guest
            else:
                pc[purl]["Email"].add((bem, r["blue_id"]))
        role = fval(r, ["Formal Designation of the guest", "Guest Title"])
        if role:
            pc[purl]["Role"].add((role, r["blue_id"]))
        li = clean_url(fval(r, ["Guest LinkedIn Profile Link", "Guest Linkedin Profile", "Guest LinkedIn profile"]))
        if li and "linkedin.com/in/" in li.lower():
            pc[purl]["LinkedIn"].add((li.split("?")[0], r["blue_id"]))
    s3 = []
    for purl, props in sorted(pc.items()):
        upd, bids = {}, set()
        for prop, vals in props.items():
            snap_has = None
            if sid10(purl) not in live_people[prop]:
                # not empty in Notion now; if Phase A snapshot said empty it is drift
                gsnap = [e for e in engp.values() if e["guests"] and purl in e["guests"]]
                idx = {"Email": 2, "LinkedIn": 3, "Role": 4}[prop]
                snap_has = any((x.split("|") + [""] * 6)[idx] for e in gsnap for x in e["guests"].split(" ;; ") if x.startswith(purl))
                if not snap_has:
                    drift_skip(3, purl, prop, sorted(vals)[0][0], "non-empty in Notion now, empty in Phase A snapshot")
                continue
            distinct = {v.lower() if prop != "Role" else v.strip().lower() for v, _ in vals}
            if len(distinct) > 1:
                internal_conflicts.append({"step": 3, "target": purl, "property": prop, "values": " | ".join(sorted(v for v, _ in vals))})
                continue
            v, b = sorted(vals)[0]
            upd[prop] = v
            bids.add(b)
        if upd:
            s3.append({"op": "update_page", "page_id": pid(purl), "properties": upd})
            t = touched[pid(purl)]
            t.update(kind="People", name=purl)
            t["fills"] += sorted(upd)
            t["blue"] |= bids
    write("03_people.json", s3)

    # ---- 4 episodes
    ec = defaultdict(lambda: defaultdict(dict))  # episode url -> prop -> {normalised: (value, blue id)}
    ep_blue = defaultdict(list)
    for r in all_recs:
        u = r["notion"]["episode"]
        if not u:
            continue
        ep_blue[u].append(r)
        for prop, cols in FILL_COLS.items():
            raw = fval(r, cols)
            v = clean_url(raw)
            if not v:
                if raw:
                    internal_conflicts.append({"step": 4, "target": u, "property": prop, "values": "unusable value: " + raw[:80]})
                continue
            ec[u][prop].setdefault(re.sub(r"^https?://(www\.)?", "", v.lower()).rstrip("/"), (v, r["blue_id"]))
        if r["workspace"] == "Episodes Inventory":
            secs = []
            for t in re.split(r",\s*", r["fields"].get("Themes", "")):
                if t.strip().lower() in SECTORS:
                    secs.append(SECTORS[t.strip().lower()])
            if secs:
                ec[u]["Sector"].setdefault(",".join(sorted(secs)), (secs, r["blue_id"]))
    s4 = []
    for u, props in sorted(ec.items()):
        e = eps[u]
        upd, bids = {}, set()
        for prop, vals in props.items():
            if prop == "Sector":
                if sid10(u) not in sector_empty:
                    continue
                if len(vals) > 1:
                    internal_conflicts.append({"step": 4, "target": u, "property": prop, "values": " | ".join(vals)})
                    continue
                secs, b = next(iter(vals.values()))
                upd["Sector"] = json.dumps(secs)
                bids.add(b)
                continue
            snap = e.get(prop)
            if snap:
                continue  # already filled in Phase A snapshot: Notion wins (conflicts are in data/blue_conflicts.csv)
            if prop in live_ep_sets:
                if sid10(u) in live_ep_sets[prop]:
                    for v, b in vals.values():
                        drift_skip(4, u, prop, v, "filled in Notion since Phase A (CTO backfill)")
                    continue
            if len(vals) > 1:
                internal_conflicts.append({"step": 4, "target": u, "property": prop, "values": " | ".join(v for v, _ in vals.values())})
                continue
            v, b = next(iter(vals.values()))
            upd[prop] = v
            bids.add(b)
        if upd:
            s4.append({"op": "update_page", "page_id": pid(u), "properties": upd})
            t = touched[pid(u)]
            t.update(kind="Episodes", name=e["Episode"])
            t["fills"] += sorted(upd)
            t["blue"] |= bids
    n_fill_ops = len(s4)
    # 2 new Episodes. Arpit Chhabra already has an Episode (found at the drift check), so that create is gated.
    new_eps, gated_eps = [], []
    sg = rec_by_id["f69c3d3c7f8042a6a101eeef8485cea7"]
    ar = rec_by_id["cm5mc15cj00gws5tws23ukq1l"]
    sg_props = {"Episode": "Saurabh Garg @ C4E - Built to Share", "Status": "Recorded", "Source": "Migration",
                "Source ID": f"Blue {sg['blue_id']}", "Migration batch": BATCH, "date:Captured:start": TODAY,
                "Show": json.dumps([SHOW_PAGE["B2S"]]), "Guests": json.dumps(["https://app.notion.com/3ed19a301a7f81ad8e2fd15573bf1d1f"]),
                "Copywriting doc": None}
    sg_props.pop("Copywriting doc")
    sg_body = (f"Migration batch: {BATCH}. Created from Blue card {sg['blue_id']} (Hissa Podcast, list Recorded, created in Blue "
               f"{sg['fields']['Created At']} UTC by the Blue card creator). Dossier: {sg['fields']['Dossier']}. "
               f"Blue attachment left in Blue (no files moved): {sg['fields']['Source data (transcripts/ dossiers/ LI)']}.")
    new_eps.append({"properties": sg_props, "content": sg_body})
    ar_props = {"Episode": "Arpit Chhabra @ IOTfy - Founder Thesis", "Status": "Work started", "Source": "Migration",
                "Source ID": f"Blue {ar['blue_id']}", "Migration batch": BATCH, "date:Captured:start": TODAY,
                "Show": json.dumps([SHOW_PAGE["FT"]]), "Guests": json.dumps(["https://app.notion.com/3ed19a301a7f81a3919bee171571aca7"]),
                "Spotify": ar["fields"]["Spofity Link"], "Amazon Music": ar["fields"]["Amazon Music Link"],
                "Apple": ar["fields"]["Apple Podcast Link"], "Tags": json.dumps(["Tier 2"])}
    ar_body = (f"Migration batch: {BATCH}. Blue Episodes Inventory card {ar['blue_id']} (list In Progress; Blue tags: "
               f"{ar['fields']['Tags']}; created {ar['fields']['Created At']} UTC; Themes: {ar['fields']['Themes']}).")
    gated_eps.append({"properties": ar_props, "content": ar_body,
                      "gate": "DO NOT APPLY without CTO ok: Notion already has 'Arpit Chhabra @ IoTfy - Founder Thesis' "
                              "(Source ID 'Episode Inventory 3c519a30-1a7f-8130-baa8-f16f3906318f', page 3ed19a301a7f81a7a268d84ac1000aea). "
                              "A create would duplicate it."})
    s4.append({"op": "create_pages", "data_source": DS["episodes"], "pages": new_eps})
    write("04_episodes.json", s4)
    write("04b_episode_create_GATED_arpit.json", [{"op": "create_pages", "data_source": DS["episodes"], "pages": gated_eps}])

    # ---- 5 engagements
    s5 = []
    for r in all_recs:
        ed = engp.get(r["blue_id"])
        if not ed:
            continue
        d1 = clean_url(r["fields"].get("Dossier", "")) or clean_url(r["fields"].get("Dossier#2", ""))
        if not d1:
            continue
        if sid10(ed["eng"]) not in dossier_empty:
            if not ed.get("dossier"):
                drift_skip(5, ed["eng"], "Dossier link", d1, "non-empty in Notion now, empty in Phase A snapshot")
            continue
        s5.append({"op": "update_page", "page_id": pid(ed["eng"]), "properties": {"Dossier link": d1}})
        t = touched[pid(ed["eng"])]
        t.update(kind="Engagements", name=ed["ename"])
        t["fills"].append("Dossier link")
        t["blue"].add(r["blue_id"])
    stake = jl(W / "stakeholder_resolution.json")
    stake_adds = [x for x in stake["rows"] if x["status"] == "to_add"]
    for x in stake_adds:  # none today; kept so a re-run with new resolutions emits the append
        s5.append({"op": "append_relation", "page_id": x["eng"], "property": "Stakeholders", "add": ["https://app.notion.com/" + x["person"]]})
    write("05_engagements.json", s5)

    # ---- 5b Source ID: exact same-show name matches (gated: every target already has a non-empty Source ID)
    show_suffix = {" - founder thesis": "FT", " - built to share": "B2S", " - un#": "AU", " - human by design": "HBD"}
    ep_names = defaultdict(list)
    for u, e in eps.items():
        n = e["Episode"]
        low = n.lower()
        for suf, sh in show_suffix.items():
            if low.endswith(suf):
                ep_names[(norm_key(n[: -len(suf)]), sh)].append(u)
    miss = list(csv.DictReader(open(D / "not_in_notion.csv")))
    s5b, un_rows = [], []
    gm = {"xsww928znraets3jipymtii7": "3f019a301a7f817caccbced016c15f9b", "pyqeyy2id1q39v902ae6rs1m": "3f119a301a7f819f9a19f9f8a97ddb3e"}
    for m in miss:
        r = rec_by_id.get(m["blue_id"])
        show = r["show"]
        guest = r["fields"].get("Guest Name") or ""
        org = r["fields"].get("Guest Organisation Name") or r["fields"].get("Co Name") or r["fields"].get("Org Name") or ""
        cand_key = norm_key(f"{guest}@{org}") if r["workspace"] != "Episodes Inventory" else norm_key(r["fields"]["Title"])
        hits = ep_names.get((cand_key, show), [])
        row = {"workspace": m["workspace"], "blue_id": m["blue_id"], "title": m["title"], "show": show, "result": "", "notion_episode": ""}
        if m["blue_id"] == "b11681207810424c82bcc03684a7e9c6":
            row["result"] = "already keyed: the Wysa Engagement Source ID already holds this Blue id (Phase A matcher missed the '; FT Pipeline/P1/101' suffix). Nothing to write."
        elif m["blue_id"] == "h3x6snxxizy6htio3kvpwxew":
            row["result"] = "Notion Episode and Engagement already carry another Blue id for this guest (qkxkbj646xkzjij0eov3lfxe): a second Blue card for the same guest. Not written."
        elif m["blue_id"] == "f69c3d3c7f8042a6a101eeef8485cea7":
            row["result"] = "no Notion Episode exists: created as a new Episode in step 4 (Source ID Blue <id>)"
        elif len(hits) != 1:
            row["result"] = ("no exact same-show name match" if not hits else f"ambiguous: {len(hits)} Notion episodes match") + "; not written"
        else:
            ep = hits[0]
            row["notion_episode"] = ep
            cur = eps[ep].get("Source ID") or ""
            row["result"] = f"exact same-show name match; Source ID already '{cur}', so setting it would overwrite: gated append in 05b"
            s5b.append({"op": "append_text", "page_id": pid(ep), "property": "Source ID", "append": f"; Blue {m['blue_id']}",
                        "current_value_expected": cur, "gate": "needs CTO ok: appends to a non-empty Source ID (same '; ' convention as the Wysa row)"})
            t = touched[pid(ep)]
            t.update(kind="Episodes", name=eps[ep]["Episode"])
            t["blue"].add(m["blue_id"])
            t["fills"].append("(name match, Source ID append gated)")
            if m["blue_id"] in gm:
                s5b.append({"op": "append_text", "page_id": gm[m["blue_id"]], "property": "Source ID", "append": f"; Blue {m['blue_id']}",
                            "gate": "needs CTO ok: appends to a non-empty Source ID on the Engagement"})
        un_rows.append(row)
    write("05b_source_id_append_GATED.json", s5b)

    # ---- 6 guest forms
    s6, forms_skipped, forms_pr_email = [], [], []
    forms = [r for r in all_recs if r["form_submission"]]
    gf_pages = []
    for r in forms:
        f = r["fields"]
        gname = (f.get("Guest Name") or f["Title"]).strip()
        if norm_key(gname) in existing_forms:
            forms_skipped.append((r["blue_id"], gname, "a Guest forms row with this name already exists"))
            continue
        prs = sorted({x.lower() for k, v in f.items() if k.startswith(PR_KEYS) for x in EM.findall(v)})
        gem = (f.get("Guest Email ID") or "").strip()
        eng = r["notion"]["engagement"]
        props = {"Guest name": gname, "Company": f.get("Guest Organisation Name", ""), "Designation": f.get("Formal Designation of the guest", ""),
                 "Merge status": "Merged" if eng else "Needs review"}
        if gem and EM.fullmatch(gem):
            if gem.lower() in prs:  # the address on the form is also a PR/comms address: the booker is not the guest (decision 424)
                props["Filled by"] = gem
                forms_pr_email.append(r["blue_id"])
            else:
                props["Guest email"] = gem
        v = clean_url(f.get("Guest LinkedIn Profile Link", ""))
        if v:
            props["Guest LinkedIn"] = v
        v = clean_url(f.get("Organisation Linkedin Page Link", ""))
        if v:
            props["Company LinkedIn"] = v
        if prs:
            props["PR and comms emails"] = ", ".join(prs)
        if eng:
            props["Engagement"] = json.dumps([eng])
        props = {k: v for k, v in props.items() if v}
        note = (f"Blue {r['blue_id']} | {BATCH} | Blue submission {f.get('Created At', '')} UTC | "
                + ("merged on 2 Oct by the Blue migration" if eng else "no Engagement in Notion for this card: needs a human look"))
        props["Merge note"] = note
        files = [f"photo: {x}" for x in r["files"].get("Hi Res Image of the Guest", [])] + \
                [f"logo: {x}" for x in r["files"].get("Upload the Logo(s) of the company", [])]
        body = [f"Imported from Blue card {r['blue_id']} (FT & Spotlight, list {f.get('List', '')}). Source ID: Blue {r['blue_id']}.",
                f"Migration batch: {BATCH}",
                f"Blue submission time: {f.get('Created At', '')} UTC. Recording date on the form: {f.get('Date of recording', '') or 'not given'}.",
                f"Would you like to spend on Google ads: {f.get('Would you like to spend on Google ads to promote the episode on YouTube?', '') or 'no answer'} "
                "(the upsell stays dropped, decision 30)."]
        if files:
            body.append("Files left in Blue, not copied (decision 533): " + "; ".join(files))
        gf_pages.append({"properties": props, "content": "\n\n".join(body)})
    for i in range(0, len(gf_pages), 100):
        s6.append({"op": "create_pages", "data_source": DS["guest_forms"], "pages": gf_pages[i:i + 100]})
    write("06_guest_forms.json", s6)

    # ---- 7 activities
    acts = []
    for c in comments:
        if not c["text"].strip():
            continue
        r = rec_by_id.get(c["record"])
        if not r:
            continue
        ed = engp.get(r["blue_id"])
        props = {"Summary": f"Blue comment by {c['by']}: {c['text'].strip()[:140]}", "Kind": "Note", "Source": "Migration",
                 "Source ID": f"Blue comment {c['id']}", "date:Date:start": c["date"], "date:Captured:start": TODAY}
        if r["notion"]["engagement"]:
            props["Engagement"] = json.dumps([r["notion"]["engagement"]])
        if r["notion"]["episode"]:
            props["Episode"] = json.dumps([r["notion"]["episode"]])
        if ed and ed.get("guests") and len(ed["guests"].split(" ;; ")) == 1:
            props["People"] = json.dumps([ed["guests"].split("|")[0]])
        body = (f"{c['text'].strip()}\n\nBlue comment {c['id']} on card \"{c['title']}\" ({r['workspace']}), by {c['by']}. "
                f"The date is decoded from the comment id (Blue gives no timestamp). Migration batch: {BATCH}.")
        acts.append({"properties": props, "content": body})
    s7 = [{"op": "create_pages", "data_source": DS["activities"], "pages": acts[i:i + 100]} for i in range(0, len(acts), 100)]
    write("07_activities.json", s7)

    # ---- 8 docs
    idx = jl(D / "docs/index.json")
    s8 = [{"op": "create_page", "parent": DEVELOPER_PAGE, "title": "Blue legacy archive", "id_alias": "$ARCHIVE",
           "content": f"Read-only copy of what was left in Blue (the old project tool) before it is switched off. Migration batch: {BATCH}. "
                      "Data only: no files, no attachments, no logins. Docs, then the four archived Blue workspaces. Proposed under Business OS developer."}]
    redactions = []
    for dct in idx:
        src = D / "reread/docs" / f"{dct['id']}.md"
        if not src.exists():
            raise SystemExit(f"missing re-read doc {dct['id']}")
        body = src.read_text()
        if "Not copied" in body or "logins removed" in body or "removed" in body.lower():
            redactions.append(dct["title"] + " (" + dct["workspace"] + ")")
        s8.append({"op": "create_page", "parent": "$ARCHIVE", "title": f"{dct['title']} ({dct['workspace']})",
                   "content": f"Source ID: Blue doc {dct['id']}. Migration batch: {BATCH}. Not tied to a card, so it lives here.\n\n" + body})
    write("08_docs.json", s8)

    # ---- 9 archive pages
    rr = D / "reread"
    ij_rows = [l.rstrip("\n").split("\t") for l in open(D / "archived/inner_journeys_records.tsv")]
    ij_detail = jl(rr / "inner_journeys_cards.json")["read"]
    ij = [f"Inner Journeys was ThePodium's show hosted by Divakar Vijayasarathy. 24 guest cards in Blue (archived workspace). Source ID: Blue workspace cm65wyqdj0kff2lpqdus97crb. Migration batch: {BATCH}.",
          "| Card | List | Tag | Blue id |\n|---|---|---|---|"]
    ij += [f"| {a[1]} | {a[2]} | {(a[3] if len(a) > 3 else '')} | {a[0]} |" for a in ij_rows]
    ij.append("## Cards read in full (field text)\nThe other 21 cards were read as titles, lists and tags only (reading each costs about 8k tokens and the guests already exist as People).")
    for c in ij_detail:
        ij.append(f"### {c['title']} (episode {c.get('episode_no', 'n/a')}, {c['list']})\n" + (c.get("guest", "") + "\n" if c.get("guest") else "") +
                  "\n".join(f"- {k}: {v}" for k, v in c.get("links", {}).items()) + (c.get("note", "")))
    pr_first = json.loads(json.load(open(D / "archived/prompts_FT_e775fc59.json"))[0]["text"])
    pr = [f"LLM repurposing prompts for FT, un# and Inner Journeys (Blue workspace Prompts, 5 cards, archived). Superseded by skills/. Source ID: Blue workspace cm917ld1b0mb5r72lphxof0fp. Migration batch: {BATCH}.",
          "## FT (e775fc59e3fb4f1d809cb0e253ae3755)"]
    pr += [f"### {f['name']}\n{f['text'].strip()}" for f in pr_first["customFields"] if f.get("text", "").strip()]
    for c in jl(rr / "prompts_other_four.json"):
        pr.append(f"## {c['title']} ({c['id']})")
        pr += [f"### {k}\n{v}" for k, v in c["fields"].items()]
    vp = [l.rstrip("\n").split("\t") for l in open(rr / "vanshika_projects_titles.tsv")]
    lname = {"U": "Uploaded on Blue", "W": "WIP", "I": "Inbox"}
    vproj = [f"Vanshika Projects (Blue slug 'thumbnail', archived): the thumbnail design queue. 110 cards named after FT and un# guests, no files, docs or comments. Source ID: Blue workspace cm90znhql06alr72l00yejjmp. Migration batch: {BATCH}.",
             "| Card | List | Blue id |\n|---|---|---|"] + [f"| {a[1]} | {lname[a[2]]} | {a[0]} |" for a in vp]
    vcards = jl(rr / "vanshika_cards.json")
    vsh = [f"Vanshika (Blue, archived): design jobs for the Built to Share launch and episodes. 4 cards. Source ID: Blue workspace cmi5zq2a00gdtq31e2i8nd53j. Migration batch: {BATCH}."]
    vsh += [f"## {c['title']} ({c['list']}) [{c['id']}]\n{c['checklist']}" for c in vcards]
    s9 = [{"op": "create_page", "parent": "$ARCHIVE", "title": t, "content": "\n\n".join(c)}
          for t, c in [("Inner Journeys (archived Blue workspace)", ij), ("Prompts (archived Blue workspace)", pr),
                       ("Vanshika Projects (archived Blue workspace)", vproj), ("Vanshika (archived Blue workspace)", vsh)]]
    write("09_archive_pages.json", s9)

    # ---- 10 body lines
    def body_data(r):
        f = r["fields"]
        out = [f"Blue card {r['blue_id']} ({r['workspace']}): list {f.get('List', '')}; tags {f.get('Tags', '') or 'none'}; "
               f"start {f.get('Start Date', '') or 'none'}; due {f.get('Due Date', '') or 'none'} (meaning unconfirmed, decision 533 keeps it here only); "
               f"created {f.get('Created At', '')}; completed {f.get('Completed', '')}{' ' + f['Completed At'] if f.get('Completed At') else ''}; "
               f"assignees {f.get('Assignees', '') or 'none'}."]
        cp = [f"**{k}:** {f[k].strip()}" for k in ("Episode Title", "Show Notes", "Thumbnail Copy", "LinkedIn Release post copy") if f.get(k, "").strip()]
        if cp:
            out.append("Copy from Blue:\n" + "\n\n".join(cp))
        lk = [f"- {k}: {f[k].strip()}" for k in ("Unlisted Video", "Linkedin Newsletter", "LI Newsletter", "Pocket Casts Link", "creators.spotify Landing Page",
                                                 "Opus Shorts Project", "Link to Guest Assets", "Sri's X announcement", "Guest X Link", "Co X Link")
              if f.get(k, "").strip()]
        if lk:
            out.append("Links from Blue:\n" + "\n".join(lk))
        extra = [f"{k}: {f[k].strip()}" for k in ("Episode Number", "Themes", "YouTube Cleanup") if f.get(k, "").strip()]
        if extra:
            out.append("Other Blue fields: " + "; ".join(extra) + ".")
        if f.get("Description", "").strip() and not r["form_submission"]:
            out.append("Blue card description: " + re.sub(r"<[^>]+>", " ", html.unescape(f["Description"])).strip()[:1500])
        return out

    s10, s10b = [], []
    for pg, t in sorted(touched.items()):
        lines = [f"From Blue ({BATCH}): filled {', '.join(sorted(set(t['fills']))) or 'nothing'}. Blue record id(s): "
                 + ", ".join(f"Blue {b}" for b in sorted(t["blue"])) + ". Notion values were not overwritten."]
        if t["kind"] == "Episodes":
            for r in ep_blue.get(next((u for u in eps if pid(u) == pg), ""), []):
                lines += body_data(r)
        s10.append({"op": "append_body", "page_id": pg, "kind": t["kind"], "markdown": "\n\n".join(lines)})
    done = {x["page_id"] for x in s10}
    for u, rs in sorted(ep_blue.items()):
        if pid(u) in done:
            continue
        lines = [f"From Blue ({BATCH}): no property needed filling. Blue record id(s): " + ", ".join(f"Blue {r['blue_id']}" for r in rs) + "."]
        for r in rs:
            lines += body_data(r)
        s10b.append({"op": "append_body", "page_id": pid(u), "kind": "Episodes", "markdown": "\n\n".join(lines)})
    write("10_body_provenance.json", s10)
    write("10b_body_data_optional.json", s10b)

    # ---- csvs
    def wcsv(name, rows, fields):
        with open(W / name, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)

    wcsv("drift_skips.csv", drift, ["step", "target", "property", "blue_value", "reason"])
    wcsv("blue_internal_conflicts.csv", internal_conflicts, ["step", "target", "property", "values"])
    wcsv("unwritten_name_matches.csv", un_rows, ["workspace", "blue_id", "title", "show", "result", "notion_episode"])
    wcsv("guest_forms_skipped.csv", [dict(zip(["blue_id", "guest", "reason"], x)) for x in forms_skipped], ["blue_id", "guest", "reason"])

    # ---- summary numbers
    def n_updates(ops):
        return sum(1 for o in ops if o["op"] == "update_page")

    stats = {
        "1_schema": len(s1), "2_orgs": len(s2), "3_people": len(s3), "4_episode_updates": n_fill_ops, "4_new_episodes": len(new_eps),
        "5_engagements": len(s5), "5_stakeholder_adds": len(stake_adds), "5b_gated_appends": len(s5b),
        "6_forms": len(gf_pages), "6_forms_call": len(s6), "7_activities": len(acts), "7_call": len(s7),
        "8_docs": len(s8) - 1, "9_archive": len(s9), "10_appends": len(s10), "10b_optional_appends": len(s10b),
        "drift_skips": len(drift), "internal_conflicts": len(internal_conflicts), "people_skips": dict(people_skips),
        "forms_guest_email_was_pr_address": len(forms_pr_email), "forms_needs_review": sum(1 for p in gf_pages if p["properties"]["Merge status"] == "Needs review"),
        "redacted_docs": redactions,
        "fill_cells": {"orgs_LinkedIn": len(s2), "people": dict(Counter(p for o in s3 for p in o["properties"])),
                       "episodes": dict(Counter(p for o in s4 if o["op"] == "update_page" for p in o["properties"])),
                       "engagements": dict(Counter(p for o in s5 if o["op"] == "update_page" for p in o["properties"]))},
    }
    json.dump(stats, open(W / "stats.json", "w"), indent=1, ensure_ascii=False)
    # ---- summary.md
    drift_by = Counter(f"{d['property']}" for d in drift)
    upd = len(s2) + len(s3) + n_fill_ops + sum(1 for o in s5 if o["op"] == "update_page")
    creates = len(s6) + len(s7) + 1 + 1 + 1 + 1  # forms, activities, new episode, archive parent, children, schema
    calls_two = upd + len(s10) + len(s6) + len(s7) + 1 + 1 + 2 + 1  # schema, episode create, parent, children
    sample = [("2 Org", s2[0]["page_id"], "LinkedIn"), ("2 Org", s2[-1]["page_id"], "LinkedIn"), ("3 People", s3[0]["page_id"], "see properties"),
              ("3 People", s3[len(s3) // 2]["page_id"], "see properties"), ("4 Episode", s4[0]["page_id"], "Copywriting doc"),
              ("4 Episode", s4[len(s4) // 2]["page_id"], "see properties"), ("4 new Episode", "(Saurabh Garg @ C4E - Built to Share, find by Source ID)", "all properties, Show, Guests"),
              ("5 Engagement", s5[0]["page_id"], "Dossier link"), ("6 Guest form", "(first and last of the 136, find by Merge note 'Blue <id>')", "properties + Engagement relation"),
              ("7 Activity", "(find by Source ID 'Blue comment cmfl1907803xrrd1e4chnt8di')", "dates, relations"), ("8/9 Pages", "(Blue legacy archive and its 21 children)", "titles, no credentials")]
    L = [f"# Blue legacy transfer, Phase B prep summary (built {TODAY}, batch {BATCH})", "",
         "Read-only prep. Nothing written to Notion or Blue. All files in data/blue_legacy/write/, built by migration/blue_legacy_phase_b.py.", "",
         "## Operations per step", "", "| Step | File | Operations | Notion calls |", "|---|---|---|---|",
         f"| 1 schema | 01_schema.json | add Organisations.LinkedIn (url) | 1 |",
         f"| 2 organisations | 02_organisations_linkedin.json | {len(s2)} LinkedIn fills | {len(s2)} |",
         f"| 3 people | 03_people.json | {len(s3)} pages: {stats['fill_cells']['people']} | {len(s3)} |",
         f"| 4 episodes | 04_episodes.json | {n_fill_ops} pages: {stats['fill_cells']['episodes']}; plus 1 new Episode (Saurabh Garg) | {n_fill_ops + 1} |",
         f"| 4b | 04b_episode_create_GATED_arpit.json | GATED, do not apply: Arpit already has an Episode | 0 |",
         f"| 5 engagements | 05_engagements.json | {len(s5)} Dossier link fills; 0 Stakeholder adds (see below) | {len(s5)} |",
         f"| 5b | 05b_source_id_append_GATED.json | {len(s5b)} Source ID appends, GATED on a CTO ok | 0 until ok |",
         f"| 6 guest forms | 06_guest_forms.json | {len(gf_pages)} creates in {len(s6)} batches | {len(s6)} |",
         f"| 7 activities | 07_activities.json | {len(acts)} creates in {len(s7)} batch | {len(s7)} |",
         f"| 8 docs | 08_docs.json | 1 archive parent page + {len(s8) - 1} doc pages | 2 (parent, then 21 children with step 9) |",
         f"| 9 archive | 09_archive_pages.json | {len(s9)} pages | 0 extra (sent with the children above) |",
         f"| 10 body lines | 10_body_provenance.json | {len(s10)} appends, one per touched row | {len(s10)} |",
         f"| 10b optional | 10b_body_data_optional.json | {len(s10b)} appends of Blue data onto Episodes with no fill | {len(s10b)} if wanted |", "",
         f"**Expected Notion calls: about {calls_two}** ({upd} property updates + {len(s10)} body appends + 8 creates). If notion-update-page can set properties and append content in one call, merge each pair and the total drops by {len(s10)} to about {calls_two - len(s10)}. At 10 to 15 s per sequential call that is {calls_two*10/3600:.1f} to {calls_two*15/3600:.1f} hours.", "",
         "## Expected row counts after (for reconciliation)", "",
         "| Table | Now | After | Why |", "|---|---|---|---|",
         "| Episodes | 691 | 692 | + Saurabh Garg. 629 rows get fills, no other row count change |",
         f"| Guest forms | 8 | {8 + len(gf_pages)} | + {len(gf_pages)} historical submissions ({stats['forms_needs_review']} of them 'Needs review': no Engagement) |",
         "| Activities | 4,668 | 4,702 | + 34 comments; 0 Blue-sourced rows today |",
         "| People, Organisations, Engagements | unchanged | unchanged | fills only; 0 new People, 0 new Engagements |",
         "| Pages under Business OS developer | | + 22 | Blue legacy archive + 17 docs + 4 archived workspaces |",
         f"| Cells filled | | | Orgs LinkedIn {len(s2)}; People {stats['fill_cells']['people']}; Episodes {stats['fill_cells']['episodes']}; Engagements {stats['fill_cells']['engagements']} |", "",
         "## Drift check (done 9 Nov, from live Notion)", "",
         f"{len(drift)} planned fills dropped because the cell is now non-empty (data/blue_legacy/write/drift_skips.csv): {dict(drift_by)}. All are the CTO's Amazon Music / Short link backfill on Episodes. "
         "Amazon Music is non-empty on 156 Episodes now, so 458 Episodes with a Blue value are still empty and are in step 4 (mostly Episodes Inventory rows the backfill did not reach). "
         "Every other column was checked by count against the Phase A snapshot and is unchanged (Copywriting doc 111, YouTube 623, Spotify 619, Apple 626, Substack 462, LinkedIn 0). "
         "People and Engagements were checked per row against the live empty-cell lists. A count check cannot see a swap (one cell emptied, another filled); the writer should still not overwrite.", "",
         "## Findings that change the brief", "",
         "1. **Stakeholder links: 0 to add, not 9.** Phase A's 9 were 7 PR contacts already on the Engagement (Phase A had no Engagement for Wysa, Sorin, GyanDhan and Prashant Sachan B2S, because their Source IDs have a suffix or a different key) and 2 where the 'PR' address is the guest's own (Rajeev Mantri, Arthur Breitman). See stakeholder_resolution.json.",
         "2. **Source ID on the 13 name matches: not writable without overwriting.** Every matched Episode or Engagement already has a non-empty Source ID. Of the 13: Wysa is already keyed (Engagement 'Blue b116...; FT Pipeline/P1/101'); Sorin's Notion rows carry a different Blue id (a second Blue card for the same guest); Yulu (V1 and V2), Parthip (WeddingSutra.com vs WeddingSutra) and Arpit (Chabbra/IOTfy vs Chhabra/IoTfy) are not exact; 9 are exact and same show (GyanDhan, Prashant Sachan on B2S, 7 inventory cards). For those 9, 05b holds 11 appends (the Episode, plus the Engagement for GyanDhan and Prashant): appends of '; Blue <id>' (same convention as the Wysa row), gated on a yes. Listed in unwritten_name_matches.csv.",
         "3. **Arpit Chhabra already has an Episode** ('Arpit Chhabra @ IoTfy - Founder Thesis', Episode Inventory source). Creating one would duplicate it, so only Saurabh Garg is created. The Arpit create is in 04b, gated.",
         "4. **Guest forms has no Source ID, Source or Migration batch property.** With none added (answer 7), 'Blue <id> | batch | Blue submission time' sits in Merge note and the body. Guest forms has no People relation either; the guest is reachable through the Engagement. 4 forms had the PR address as 'guest email': it goes in Filled by, and Guest email stays empty (decision 424).",
         "5. **Credentials in Blue docs.** The Home docs of FT, un#, Built to Share, Human by Design and Inner Journeys hold plaintext usernames and passwords (Zencastr, LinkedIn, Spotify, Gmail, Riverside, Google Ads, X, Beehiiv and more, plus a phone number). They are NOT copied into the re-read files, the write files or the repo. Those passwords should be treated as exposed to anyone with Blue access and rotated when Blue is switched off.",
         "6. **Not in the CTO's step list, so not built:** Organisation Website fills (no fresh Organisations snapshot), Transcript file fills (files are out of scope), Episode Tags/tier changes. The plan's Episode body sections are in step 10 for rows that get a fill and in 10b (optional) for the other matched Episodes.",
         "7. **Inner Journeys archive page:** field text was read for 3 of 24 cards (about 8k tokens each, guests already People); the page lists all 24 by title, list and tag. Re-read the remaining 21 if their links matter.", "",
         "## Unwritten (name-only) matches", "", "See unwritten_name_matches.csv: 13 rows with the reason for each.", "",
         "## Read-back sample plan (10 rows, after each step's writes)", ""]
    L += [f"{i + 1}. {a}: {b} ({c})" for i, (a, b, c) in enumerate(sample)]
    L += ["", "For each: fetch the page, confirm the filled cell equals the file, an untouched non-empty cell still equals its drift-check value, the body ends with the provenance line, and the Source ID/Merge note holds the Blue id. Reconcile the counts table above at the end.", "",
          "## Other files", "", "drift_skips.csv, blue_internal_conflicts.csv (9 cells where two Blue cards disagree or hold several links, not written), unwritten_name_matches.csv, guest_forms_skipped.csv (empty), stats.json, reread/ (docs as markdown without credentials, prompts, Vanshika titles)."]
    (W / "summary.md").write_text("\n".join(L) + "\n")

    print(json.dumps(stats, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
