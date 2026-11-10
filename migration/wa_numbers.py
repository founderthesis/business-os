"""One-time WhatsApp number enrichment (decision 535, Akshay, 10 Nov: "Phone numbers come only from People; a one-time
enrichment fills them from his WhatsApp contacts and chats, with ambiguous matches reviewed").

Read-only and re-runnable: it reads saved snapshots, never Notion or WhatsApp, and writes a review CSV plus a plan of
the unambiguous writes, both under data/ (git-ignored). The CTO runs the writes only after review (one writer).

Usage:
  python3 migration/wa_numbers.py <people.json> <chats.json> <out dir>

Snapshots (save under data/wa/):
  people.json: SQL on People (collection://e6c44319-7f81-4da6-8b80-8441a4875d7a):
    SELECT url, "Name", "Phone", "Organisation" FROM <People>
    with Organisation resolved to the organisation names: [{"url", "Name", "Phone", "Org": ["<name>", ...]}].
  chats.json: Blueticks chats_read action list, kinds ["contact"], include_archive true, every page, saved as one list of
    {"id": "<digits>@c.us", "name": "<saved name>"}. Groups and channels are dropped here anyway.

Matching (no guess):
  - Only People with an empty Phone.
  - A chat matches a person when its saved name, normalised (case, accents, dots, hyphens and extra spaces ignored),
    equals the person's full name, or equals the full name followed by one of their organisation's names, either
    order ("Asha Rao", "Asha Rao Acme", "Acme Asha Rao").
  - Unique: exactly one chat matches, and its number isn't already on another People row and matches no other person.
  - Anything else is listed for review (two or more chats, a number another person has or also matches, no match).
Phones are written as "+<digits>" (the chat id's digits carry the country code).
"""
import sys, os, json, csv, re, unicodedata, hashlib


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[.\-_,'()|/]+", " ", s)
    return " ".join(s.split())


def digits(chat_id):
    m = re.fullmatch(r"(\d{8,15})@c\.us", chat_id or "")
    return m.group(1) if m else None


def keys_for(person):
    name = norm(person["Name"])
    ks = {name} if name else set()
    for org in person.get("Org") or []:
        o = norm(org)
        if o and name:
            ks |= {name + " " + o, o + " " + name}
    return ks


def main(people_p, chats_p, out):
    people = json.load(open(people_p))
    chats = [c for c in json.load(open(chats_p)) if digits(c.get("id"))]
    on_people = {re.sub(r"\D", "", p.get("Phone") or "").lstrip("0") for p in people if p.get("Phone")}
    by_key = {}
    for c in chats:
        by_key.setdefault(norm(c.get("name")), []).append(c)
    empty = [p for p in people if not (p.get("Phone") or "").strip() and norm(p.get("Name"))]
    cand = {}
    for p in empty:
        hits = {digits(c["id"]): c for k in keys_for(p) for c in by_key.get(k, [])}
        cand[p["url"]] = hits
    claimed = {}
    for u, hits in cand.items():
        for d in hits:
            claimed.setdefault(d, set()).add(u)
    rows, plan = [], []
    for p in empty:
        hits = cand[p["url"]]
        nums = sorted(hits)
        if not nums:
            status = "no match"
        elif len(nums) > 1:
            status = "review: %d chats match" % len(nums)
        elif nums[0].lstrip("0") in on_people or nums[0] in on_people:
            status = "review: number already on another People row"
        elif len(claimed[nums[0]]) > 1:
            status = "review: number matches %d people" % len(claimed[nums[0]])
        else:
            status = "unique"
            plan.append({"person": p["url"], "name": p["Name"], "Phone": "+" + nums[0],
                         "from_chat": hits[nums[0]].get("name")})
        rows.append({"person": p["url"], "name": p["Name"], "org": "; ".join(p.get("Org") or []), "status": status,
                     "chat_names": "; ".join(hits[d].get("name") or "" for d in nums),
                     "numbers": "; ".join("+" + d for d in nums)})
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "wa-numbers-review.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["person"])
        w.writeheader(); w.writerows(rows)
    b = json.dumps(plan, indent=1, ensure_ascii=False, sort_keys=True).encode()
    open(os.path.join(out, "wa-numbers-plan.json"), "wb").write(b)
    counts = {}
    for r in rows:
        counts[r["status"].split(":")[0]] = counts.get(r["status"].split(":")[0], 0) + 1
    print("people %d, empty phone %d, chats %d; unique %d, review %d, no match %d; plan sha256 %s"
          % (len(people), len(empty), len(chats), counts.get("unique", 0), counts.get("review", 0),
             counts.get("no match", 0), hashlib.sha256(b).hexdigest()[:16]))


if __name__ == "__main__":
    main(*sys.argv[1:4])
