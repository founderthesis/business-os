"""Phase A of the Blue legacy transfer: gap inventory, conflicts and video manifest. Read-only.

Usage: python migration/blue_legacy_phase_a.py

Reads (all git-ignored, extracted read-only on 9 Nov 2026):
  data/blue_legacy/export/*.csv             Blue record CSV exports, one per workspace
  data/blue_legacy/files/*.tsv              Blue file lists (id, name, size) for mp4s, Hissa, FastCode
  data/blue_legacy/files/type_counts.json   file counts by type per workspace
  data/blue_legacy/comments_*.json          comment text per record
  data/blue_legacy/docs/index.json          Blue docs
  data/blue_legacy/notion/*.json            Notion Engagements, Episodes and guest People snapshots
  data/blue_legacy/people_unmatched_emails.txt  Blue emails with no People row (exact, Email or Other emails)
Writes:
  data/blue_legacy/inventory.json           counts the plan quotes
  data/blue_legacy/records_<workspace>.json one JSON per workspace: every record, mapped, with its Notion match
  data/blue_conflicts.csv                   Blue value differs from a non-empty Notion value
  data/blue_video_manifest.csv              mp4s that stay in Blue
  data/blue_legacy/not_in_notion.csv        Blue records with no Notion row (name match shown, never used)
Never writes to Notion or Blue. Re-run safely.
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data/blue_legacy"
BATCH = "blue-legacy-2026-11-09"
EM = re.compile(r"[A-Za-z0-9._%+'-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
LIMIT = 20 * 1024 * 1024  # Notion MCP single-part upload limit (20 MiB)

WS = {  # export file -> (workspace, show)
    "ft.csv": ("FT & Spotlight", "FT"), "un.csv": ("alpha un#", "AU"), "hissa.csv": ("Hissa Podcast", "B2S"),
    "fastcode.csv": ("FastCode Podcast", "HBD"), "ei.csv": ("Episodes Inventory", "FT"),
    "ij.csv": ("Inner Journeys", None), "vproj.csv": ("Vanshika Projects", None),
    "prompts.csv": ("Prompts", None), "vanshika.csv": ("Vanshika", None)}

# Blue column -> (target, how). Targets: EP Episodes, EN Engagements, PE guest People, OR Organisations,
# GF Guest forms row (FT form submissions), ACT Activities, BODY Episode page body "From Blue", MANIFEST, DROP.
COMMON = {
    "Todo ID": ("PROV", "Source ID blue:<id>"), "Title": ("EP", "Episode (new rows only)"),
    "List": ("EP", "Status (new rows only; else BODY line)"), "Start Date": ("BODY", "Blue start date"),
    "Due Date": ("BODY", "Blue due date (meaning unconfirmed)"), "Tags": ("EP", "Tags for tiers; rest BODY"),
    "Description": ("BODY", "card description"), "Assignees": ("BODY", "Blue assignees"),
    "Completed": ("BODY", "done flag"), "Created At": ("BODY", "created in Blue"), "Updated At": ("DROP", "system"),
    "Completed At": ("BODY", "done date"), "Created By": ("PROV", "form vs staff"), "Color": ("DROP", "empty"),
    "Project": ("DROP", "workspace name"), "Checklists": ("DROP", "automation noise, 0 ticked (audit)"),
}
MAP = {
    "FT & Spotlight": {
        "Dossier": ("EN", "Dossier link"), "Guest Name": ("PE", "Name"),
        "Guest Organisation Name": ("OR", "Name via Engagement Organisation; GF Company"),
        "Guest Email ID": ("PE", "Email; GF Guest email"),
        "Email ID (1) of PR/ Communication/ Marketing team member": ("PE", "PR contact + EN Stakeholders"),
        "Email ID (2) of PR/ Communication/ Marketing team member": ("PE", "PR contact + EN Stakeholders"),
        "Email ID (3) of PR/ Communication/ Marketing team member": ("PE", "PR contact + EN Stakeholders"),
        "Email ID (4) of PR/ Communication/ Marketing team member": ("PE", "PR contact + EN Stakeholders"),
        "Would you like to spend on Google ads to promote the episode on YouTube?": ("BODY", "Engagement page body line"),
        "Organisation Linkedin Page Link": ("NEW", "Organisations.LinkedIn (url); GF Company LinkedIn"),
        "Date of recording": ("EP", "Recording date"), "Formal Designation of the guest": ("PE", "Role; GF Designation"),
        "Guest LinkedIn Profile Link": ("PE", "LinkedIn; GF Guest LinkedIn"),
        "Episode Title": ("BODY", "Copy from Blue"), "Show Notes": ("BODY", "Copy from Blue"),
        "Thumbnail Copy": ("BODY", "Copy from Blue"), "LinkedIn Release post copy": ("BODY", "Copy from Blue"),
        "Unlisted Video": ("BODY", "link"), "Link to working doc": ("EP", "Copywriting doc"),
        "Hi Res Image of the Guest": ("GF", "Photo (file)"), "Upload the Logo(s) of the company": ("GF", "Logo (file)"),
        "Spotify thumbnail": ("NEW", "Episodes.Assets (file)"), "YT Thumbnail (+LinkedIn Newsletter)": ("NEW", "Episodes.Assets (file)"),
        "Substack Thumbnail (420x300)": ("NEW", "Episodes.Assets (file)"), "Quote Cards": ("NEW", "Episodes.Assets (file)"),
        "Episode Out Now Thumbnail": ("NEW", "Episodes.Assets (file)"), "Deep Dive Thumbnail": ("NEW", "Episodes.Assets (file)"),
        "Intro Reel": ("MANIFEST", "mp4 stays in Blue"), "Training Data": ("EP", "Transcript file"),
        "Audio File": ("DRIVE", "audio over the upload limit, Drive folder"), "Uncut version": ("DROP", "empty"),
        "Youtube Link": ("EP", "YouTube"), "podm.in Short Link": ("EP", "Short link"), "Spotify Link": ("EP", "Spotify"),
        "Amazon Music Link": ("EP", "Amazon Music"), "Apple Podcast": ("EP", "Apple"),
        "Substack Published Page": ("EP", "Substack"), "LI Announcement Post": ("EP", "LinkedIn"),
        "Linkedin Newsletter": ("BODY", "Other links"),
    },
    "alpha un#": {
        "short link": ("EP", "Short link"), "Guest Name": ("PE", "Name"), "Guest Title": ("PE", "Role"),
        "Co Name": ("OR", "Name"), "Guest Linkedin Profile": ("PE", "LinkedIn"), "Guest Email ID": ("PE", "Email"),
        "Other Email IDs": ("PE", "PR contact + EN Stakeholders"), "Dossier": ("EN", "Dossier link"),
        "Co LinkedIn Page": ("NEW", "Organisations.LinkedIn (url)"), "Co Website": ("OR", "Website"),
        "Guest X Link": ("BODY", "People page body: Links from Blue"), "Co X Link": ("BODY", "Organisation page body"),
        "Episode Number": ("BODY", "Episode number"), "YouTube Link": ("EP", "YouTube"),
        "Link to Working Doc": ("EP", "Copywriting doc"), "Link to Guest Assets": ("BODY", "Other links"),
        "Opus Shorts Project": ("BODY", "Other links"), "creators.spotify Landing Page": ("BODY", "Other links"),
        "Spotify Link": ("EP", "Spotify"), "Amazon Music Link": ("EP", "Amazon Music"), "Pocket Casts Link": ("BODY", "Other links"),
        "Apple Podcast Link": ("EP", "Apple"), "Sri's LI Announcement": ("EP", "LinkedIn"),
        "Sri's X announcement": ("BODY", "Other links"), "Published Newsletter Link": ("EP", "Substack"),
        "Thumbnail for YT": ("NEW", "Episodes.Assets (file)"), "Thumbnail for Spotify": ("NEW", "Episodes.Assets (file)"),
        "Audio File": ("DRIVE", "audio, Drive folder"), "Episode Out Now": ("NEW", "Episodes.Assets (file)"),
        "Deep Dive Thumbnail": ("NEW", "Episodes.Assets (file)"), "Guest Pic": ("NEW", "Episodes.Assets (file)"),
        "infographics etc": ("NEW", "Episodes.Assets (file)"), "Shorts/ Reels": ("MANIFEST", "mp4 stays in Blue"),
        "Source data (transcripts/ dossiers/ LI)": ("EP", "Transcript file (txt); Assets (pdf)"),
        "Gemini Chat Link": ("DROP", "empty"), "Claude Project": ("DROP", "empty"), "ChatGPT Chat Link": ("DROP", "empty"),
    },
    "Hissa Podcast": {
        "short link": ("EP", "Short link"), "Guest Name": ("PE", "Name"), "Guest Title": ("PE", "Role"),
        "Co Name": ("OR", "Name"), "Guest Linkedin Profile": ("PE", "LinkedIn"), "Guest Email ID": ("PE", "Email"),
        "Other Email IDs": ("PE", "PR contact + EN Stakeholders"), "Dossier": ("EN", "Dossier link"),
        "Co LinkedIn Page": ("NEW", "Organisations.LinkedIn (url)"), "http://www.cashify.in": ("OR", "Website"),
        "Guest X Link": ("DROP", "empty"), "Co X Link": ("DROP", "empty"), "Episode Number": ("BODY", "Episode number"),
        "Episode Title": ("DROP", "empty"), "Thumbnail Copy": ("DROP", "empty"), "Uncut video v1": ("DROP", "empty"),
        "YouTube Link": ("EP", "YouTube"), "Link to Working Doc": ("EP", "Copywriting doc"),
        "Link to Guest Assets": ("DROP", "empty"), "Opus Shorts Project": ("DROP", "empty"),
        "creators.spotify Landing Page": ("DROP", "empty"), "Spotify Link": ("EP", "Spotify"),
        "Amazon Music Link": ("EP", "Amazon Music"), "Pocket Casts Link": ("DROP", "empty"), "Apple Podcast Link": ("EP", "Apple"),
        "Satish's LI Announcement": ("DROP", "empty"), "Satish's X announcement": ("DROP", "empty"),
        "Published Newsletter Link": ("EP", "Substack"), "Thumbnail for YT": ("DROP", "empty"),
        "Thumbnail for Spotify": ("DROP", "empty"), "Episode Out Now": ("DROP", "empty"),
        "Deep Dive Thumbnail": ("NEW", "Episodes.Assets (file)"), "Guest Pic": ("NEW", "Episodes.Assets (file)"),
        "infographics etc": ("DROP", "empty"), "Shorts/Reels": ("DROP", "empty"),
        "Source data (transcripts/ dossiers/ LI)": ("EP", "Transcript file (txt); Assets (other)"),
    },
    "FastCode Podcast": {
        "Training Data": ("EP", "Transcript file"), "You Tube Link": ("EP", "YouTube"), "Amazon Music": ("EP", "Amazon Music"),
        "Spotify Link": ("EP", "Spotify"), "Apple Podcast": ("EP", "Apple"), "Link to working doc": ("EP", "Copywriting doc"),
        "Shortlink": ("EP", "Short link"), "Dossier": ("EN", "Dossier link"), "Guest Name": ("PE", "Name"),
        "Guest Title": ("PE", "Role"), "Company Name": ("OR", "Name"), "Guest Email ID": ("PE", "Email"),
        "Other Email ID": ("PE", "PR contact + EN Stakeholders"), "Guest LinkedIn profile": ("PE", "LinkedIn"),
        "Co LinkedIn Profile": ("NEW", "Organisations.LinkedIn (url)"), "Co Website": ("OR", "Website"),
        "Guest Pic": ("NEW", "Episodes.Assets (file)"),
    },
    "Episodes Inventory": {
        "Guest Name": ("PE", "Name"), "Org Name": ("OR", "Name"), "Guest Linkedin Profile": ("PE", "LinkedIn"),
        "Org Website": ("OR", "Website"), "YouTube Link": ("EP", "YouTube"), "Spofity Link": ("EP", "Spotify"),
        "Amazon Music Link": ("EP", "Amazon Music"), "Apple Podcast Link": ("EP", "Apple"), "Substack Link": ("EP", "Substack"),
        "YouTube Cleanup": ("BODY", "rework flag"), "Themes": ("EP", "Sector (9 sector values); rest BODY"),
        "Link to working Doc": ("EP", "Copywriting doc"), "LI Newsletter": ("BODY", "Other links"),
        "Transcript": ("EP", "Transcript file"), "Shorts": ("DROP", "empty"), "Quote Cards": ("NEW", "Episodes.Assets (file)"),
        "Thumbnail for YT": ("NEW", "Episodes.Assets (file)"), "Thumbnail for Spotify": ("NEW", "Episodes.Assets (file)"),
        "Thumbnail for Substack": ("NEW", "Episodes.Assets (file)"),
        "Checklists": ("BODY", "Re-Publish checklist state (the one checklist that was used)"),
    },
}
EP_COMPARE = {  # Blue column -> Notion Episodes column, for conflict detection
    "Youtube Link": "YouTube", "YouTube Link": "YouTube", "You Tube Link": "YouTube",
    "Spotify Link": "Spotify", "Spofity Link": "Spotify", "Apple Podcast": "Apple", "Apple Podcast Link": "Apple",
    "Amazon Music Link": "Amazon Music", "Amazon Music": "Amazon Music",
    "Substack Published Page": "Substack", "Substack Link": "Substack", "Published Newsletter Link": "Substack",
    "podm.in Short Link": "Short link", "short link": "Short link", "Shortlink": "Short link",
    "Link to working doc": "Copywriting doc", "Link to Working Doc": "Copywriting doc", "Link to working Doc": "Copywriting doc",
    "LI Announcement Post": "LinkedIn", "Sri's LI Announcement": "LinkedIn", "Date of recording": "rec",
}
SECTORS = {"Fintech", "SaaS", "D2C", "Marketplace", "Deeptech", "Edtech", "Healthtech", "Services", "Gaming"}
FILE_COLS = {"Hi Res Image of the Guest", "Upload the Logo(s) of the company", "Spotify thumbnail",
             "YT Thumbnail (+LinkedIn Newsletter)", "Substack Thumbnail (420x300)", "Quote Cards", "Episode Out Now Thumbnail",
             "Deep Dive Thumbnail", "Intro Reel", "Training Data", "Audio File", "Thumbnail for YT", "Thumbnail for Spotify",
             "Episode Out Now", "Guest Pic", "infographics etc", "Shorts/ Reels", "Source data (transcripts/ dossiers/ LI)",
             "Transcript", "Quote Cards", "Thumbnail for Substack"}


def read_csv(path):
    rows = list(csv.reader(open(path, encoding="utf-8")))
    head = rows[0]
    out = []
    for r in rows[1:]:
        rec = {}
        for i, h in enumerate(head):  # duplicate column names (HBD "Dossier" twice) get a suffix
            k = h if h not in rec else f"{h}#2"
            rec[k] = r[i].strip() if i < len(r) else ""
        out.append(rec)
    return head, out


def norm_url(u):
    u = (u or "").strip().rstrip(",").lower()
    u = re.sub(r"^https?://(www\.)?", "", u)
    u = u.split("?")[0].split("#")[0].rstrip("/")
    return u


def yt_id(u):
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/live/|/embed/)([A-Za-z0-9_-]{11})", str(u or ""))
    return m.group(1) if m else None


def link_key(prop, u):
    """Compare platform links by the id inside them, not the URL spelling."""
    u = (u or "").strip().rstrip(",")
    if prop == "Apple":
        m = re.search(r"[?&]i=(\d+)", u)
        return m.group(1) if m else norm_url(u)
    if prop == "Spotify":
        m = re.search(r"/episode/([A-Za-z0-9]+)", u)
        return m.group(1) if m else norm_url(u)
    if prop == "Substack":
        m = re.search(r"/p/([^/?#]+)", u)
        return m.group(1).lower() if m else norm_url(u)
    if prop == "Copywriting doc":
        m = re.search(r"/d/([A-Za-z0-9_-]+)", u)
        return m.group(1) if m else norm_url(u)
    return norm_url(u)


def name_key(s):
    return re.sub(r"[^a-z ]", "", (s or "").lower()).strip()


def files_in(v):
    return [f.strip() for f in re.split(r",\s*(?=[^,]*\.[A-Za-z0-9]{2,5}(?:,|$))", v) if f.strip()] if v else []


def main():
    eng = {r["Source ID"].split(" ", 1)[1]: r for r in json.load(open(D / "notion/engagements_blue.json"))}
    engp = {r["sid"].split(" ", 1)[1]: r for r in json.load(open(D / "notion/engagements_people.json"))}
    eps_all = json.load(open(D / "notion/episodes_all.json"))
    linked = {e["url"]: e for e in json.load(open(D / "notion/episodes_blue_linked.json"))}
    for e in eps_all:
        e.setdefault("Guest form in", (linked.get(e["url"]) or {}).get("Guest form in"))
        e.setdefault("rec", (linked.get(e["url"]) or {}).get("rec"))
    eps_by_url = {e["url"]: e for e in eps_all}
    eps_by_sid = {e["Source ID"].split(" ", 1)[1]: e for e in eps_all if (e.get("Source ID") or "").startswith("Blue ")}
    eps_by_yt = defaultdict(list)
    for e in eps_all:
        if yt_id(e.get("YouTube")):
            eps_by_yt[yt_id(e["YouTube"])].append(e)
    eps_by_sp = defaultdict(list)
    for e in eps_all:
        if e.get("Spotify"):
            eps_by_sp[link_key("Spotify", e["Spotify"])].append(e)
    unmatched_emails = set(open(D / "people_unmatched_emails.txt").read().split())
    comments = json.load(open(D / "comments_ft.json")) + json.load(open(D / "comments_un.json"))
    com_by_rec = defaultdict(list)
    for c in comments:
        com_by_rec[c["record"]].append(c)

    inv, conflicts, missing = {}, [], []
    for fname, (ws, show) in WS.items():
        p = D / "export" / fname
        if not p.exists():
            inv[ws] = {"exported": False}
            continue
        head, recs = read_csv(p)
        cmap = {**COMMON, **MAP.get(ws, {})}
        out, stat = [], Counter()
        field_fill = Counter()
        for r in recs:
            rid = r["Todo ID"]
            for k, v in r.items():
                if v:
                    field_fill[k] += 1
            # Notion match: Source ID first (Engagement or Episode), then YouTube id for the inventory
            e = eng.get(rid)
            ep = None
            how = None
            if e and e.get("Episode"):
                ep = eps_by_url.get(json.loads(e["Episode"])[0])
                how = "engagement Source ID"
            if not ep and rid in eps_by_sid:
                ep, how = eps_by_sid[rid], "episode Source ID"
            yt = yt_id(r.get("Youtube Link") or r.get("YouTube Link") or r.get("You Tube Link"))
            if not ep and ws == "Episodes Inventory" and yt and len(eps_by_yt.get(yt, [])) == 1:
                ep, how = eps_by_yt[yt][0], "YouTube id"
            sp = link_key("Spotify", r.get("Spofity Link"))
            if not ep and ws == "Episodes Inventory" and sp and len(eps_by_sp.get(sp, [])) == 1:
                ep, how = eps_by_sp[sp][0], "Spotify id"
            in_notion = bool(e or ep)
            if ws in ("Inner Journeys", "Vanshika Projects", "Prompts", "Vanshika"):
                in_notion = None  # archive pages, not row matches
            if in_notion is False:
                guest = r.get("Guest Name") or r["Title"].split("@")[0]
                cand = [x["Episode"] for x in eps_all if name_key(guest) and name_key(guest) in name_key(x.get("Episode"))]
                missing.append({"workspace": ws, "blue_id": rid, "title": r["Title"], "list": r.get("List"),
                                "created": r.get("Created At"), "name_match_report_only": " | ".join(cand[:3])})
            stat["in_notion" if in_notion else ("archive" if in_notion is None else "missing")] += 1
            # conflicts: Blue value vs non-empty Notion value, never overwritten
            if ep:
                for col, ncol in EP_COMPARE.items():
                    bv = r.get(col, "").rstrip(",").strip()
                    nv = ep.get(ncol)
                    if bv and not nv:
                        stat[f"fill_Episodes.{'Recording date' if ncol == 'rec' else ncol}"] += 1
                    if not bv or not nv:
                        continue
                    if ncol == "rec":  # Blue export times are UTC; Notion dates are IST days
                        try:
                            from datetime import datetime, timedelta
                            bd = (datetime.strptime(bv[:16], "%Y-%m-%d %H:%M") + timedelta(hours=5, minutes=30)).date()
                            same = bd.isoformat() == nv[:10] or bv[:10] == nv[:10]
                        except ValueError:
                            same = bv[:10] == nv[:10]
                    elif ncol == "YouTube":
                        same = yt_id(bv) == yt_id(nv)
                    else:
                        same = link_key(ncol, bv) == link_key(ncol, nv)
                    if not same:
                        conflicts.append({"workspace": ws, "blue_id": rid, "blue_title": r["Title"], "target": "Episodes",
                                          "notion_url": ep["url"], "property": "Recording date" if ncol == "rec" else ncol,
                                          "blue_value": bv, "notion_value": nv})
            ed = engp.get(rid)
            if ed and r.get("Dossier") and not ed.get("dossier"):
                stat["fill_Engagements.Dossier link"] += 1
            tcol = next((c for c in ("Training Data", "Transcript", "Source data (transcripts/ dossiers/ LI)") if r.get(c)), None)
            if ep and tcol and ".txt" in r[tcol].lower():
                stat["transcript_in_blue"] += 1
                if (not ep.get("Transcript file") or ep.get("Transcript file") == "[]") and not ep.get("Transcript"):
                    stat["fill_Episodes.Transcript file"] += 1
            if ed and r.get("Dossier") and ed.get("dossier") and norm_url(r["Dossier"]) != norm_url(ed["dossier"]):
                conflicts.append({"workspace": ws, "blue_id": rid, "blue_title": r["Title"], "target": "Engagements",
                                  "notion_url": ed["eng"], "property": "Dossier link", "blue_value": r["Dossier"],
                                  "notion_value": ed["dossier"]})
            # guest People gaps and conflicts (first linked guest only)
            if ed and ed.get("guests"):
                g = ed["guests"].split(" ;; ")[0].split("|")
                purl, pname, pmail, pli, prole = (g + [""] * 6)[:5]
                bmail = (r.get("Guest Email ID") or "").lower()
                bli = r.get("Guest LinkedIn Profile Link") or r.get("Guest Linkedin Profile") or r.get("Guest LinkedIn profile")
                brole = r.get("Formal Designation of the guest") or r.get("Guest Title")
                for prop, bv, nv, cmp in [("Email", bmail, pmail, lambda a, b: a.lower() == b.lower()),
                                          ("LinkedIn", bli, pli, lambda a, b: norm_url(a) == norm_url(b)),
                                          ("Role", brole, prole, lambda a, b: a.strip().lower() == b.strip().lower())]:
                    if bv and nv and not cmp(bv, nv) and not (prop == "Email" and bv in (g[5] if len(g) > 5 else "").lower()):
                        conflicts.append({"workspace": ws, "blue_id": rid, "blue_title": r["Title"], "target": "People",
                                          "notion_url": purl, "property": prop, "blue_value": bv, "notion_value": nv})
                    elif bv and not nv:
                        stat[f"people_gap_{prop}"] += 1
            # PR contacts and stakeholder links
            pr = set()
            for k, v in r.items():
                if k.startswith("Email ID (") or k.startswith("Other Email ID"):
                    pr.update(x.lower() for x in EM.findall(v))
            stake = (ed or {}).get("stake") or ""
            linked = {x for x in pr if x in stake.lower()}
            stat["pr_emails"] += len(pr)
            stat["pr_linked"] += len(linked)
            stat["pr_unlinked_existing_person"] += len([x for x in pr - linked if x not in unmatched_emails])
            stat["pr_no_person"] += len([x for x in pr if x in unmatched_emails])
            files = {k: files_in(v) for k, v in r.items() if k in FILE_COLS and v}
            out.append({"blue_id": rid, "workspace": ws, "show": show, "fields": r, "files": files,
                        "comments": com_by_rec.get(rid, []),
                        "form_submission": ws == "FT & Spotlight" and not r.get("Created By"),
                        "notion": {"match": how, "engagement": (e or {}).get("url"), "episode": (ep or {}).get("url"),
                                   "episode_guest_form_in": (ep or {}).get("Guest form in")},
                        "provenance": {"Source": "Migration", "Source ID": f"blue:{rid}", "Migration batch": BATCH}})
        # field gaps: columns with values whose target is not an existing property
        gaps = {k: {"records": field_fill.get(k, 0), "target": cmap.get(k, ("UNMAPPED", ""))[0],
                    "property": cmap.get(k, ("UNMAPPED", ""))[1]} for k in head if field_fill.get(k)}
        if "#2" in "".join(r_k for r_k in field_fill):  # second Dossier column on HBD
            gaps["Dossier#2"] = {"records": field_fill["Dossier#2"], "target": "EN", "property": "Dossier link (2nd)"}
        form = [o for o in out if o["form_submission"]]
        inv[ws] = {"records": len(recs), "lists": dict(Counter(r.get("List") for r in recs)), **stat,
                   "form_submissions": len(form),
                   "form_in_notion": sum(1 for o in form if o["notion"]["engagement"]),
                   "form_guest_form_in_ticked": sum(1 for o in form if o["notion"]["episode_guest_form_in"] == "__YES__"),
                   "comments": sum(len(o["comments"]) for o in out),
                   "records_with_comments": sum(1 for o in out if o["comments"]),
                   "fields": gaps}
        slug = re.sub(r"[^a-z0-9]+", "_", ws.lower()).strip("_")
        json.dump(out, open(D / f"records_{slug}.json", "w"), indent=1, ensure_ascii=False)

    # video manifest: mp4s stay in Blue; record id/title from export file names (several names repeat)
    name_to_rec = defaultdict(list)
    for fname, (ws, _) in WS.items():
        p = D / "export" / fname
        if p.exists():
            for r in read_csv(p)[1]:
                for k, v in r.items():
                    for f in files_in(v):
                        if f.lower().endswith(".mp4"):
                            name_to_rec[(ws, f)].append((r["Todo ID"], r["Title"]))
    man = []
    for tsv, ws in [("mp4_ft.tsv", "FT & Spotlight"), ("mp4_un.tsv", "alpha un#"), ("mp4_ij.tsv", "Inner Journeys")]:
        for line in open(D / "files" / tsv):
            fid, name, size = line.rstrip("\n").split("\t")
            recs = name_to_rec.get((ws, name), [])
            man.append({"workspace": ws, "record_id": ";".join(x[0] for x in recs) or "",
                        "record_title": ";".join(x[1] for x in recs) or "(comment or record attachment, not in a field)",
                        "file_id": fid, "filename": name, "size_bytes": int(size)})
    with open(ROOT / "data/blue_video_manifest.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(man[0]))
        w.writeheader()
        w.writerows(man)
    with open(ROOT / "data/blue_conflicts.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["workspace", "blue_id", "blue_title", "target", "notion_url", "property",
                                          "blue_value", "notion_value"])
        w.writeheader()
        w.writerows(conflicts)
    with open(D / "not_in_notion.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["workspace", "blue_id", "title", "list", "created", "name_match_report_only"])
        w.writeheader()
        w.writerows(missing)
    inv["_video_manifest"] = {"files": len(man), "bytes": sum(m["size_bytes"] for m in man),
                              "active_files": sum(1 for m in man if m["workspace"] != "Inner Journeys"),
                              "active_bytes": sum(m["size_bytes"] for m in man if m["workspace"] != "Inner Journeys"),
                              "unmapped_to_record": sum(1 for m in man if not m["record_id"])}
    inv["_conflicts"] = dict(Counter(f"{c['target']}.{c['property']}" for c in conflicts).most_common())
    inv["_conflicts_total"] = len(conflicts)
    inv["_generated"] = date.today().isoformat()
    json.dump(inv, open(D / "inventory.json", "w"), indent=1, ensure_ascii=False, default=str)
    for ws, v in inv.items():
        if not ws.startswith("_") and v.get("records"):
            print(ws, {k: v[k] for k in v if k not in ("fields", "lists")})
    print("conflicts", len(conflicts), inv["_conflicts"])
    print("manifest", inv["_video_manifest"])
    print("missing", Counter(m["workspace"] for m in missing))


if __name__ == "__main__":
    sys.exit(main())
