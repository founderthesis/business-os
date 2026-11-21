"""Parse the 'Founder Thesis whatsapp group' Google Doc export into one JSON row per person.

Usage: python3 -I migration/whatsapp_blurbs.py <drive_json_path> <out_json_path>
Re-runnable. Strips phone numbers, emails, WhatsApp handles and invite links.
"""
import json, re, sys
from collections import Counter

src, out = sys.argv[1], sys.argv[2]
doc = json.load(open(src))
text = doc["fileContent"]

# ---------- scrubbing ----------
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE = re.compile(r"(?<![\w/])\+?\d[\d \-]{8,}\d(?![\w/])")
WA_LINK = re.compile(r"https?://(?:chat\.whatsapp\.com|wa\.me)/\S+|wa\.me/\d+")
MAILTO = re.compile(r"\(mailto:[^)]*\)")

def unescape(s):
    s = re.sub(r"\\([!~&#*_\[\]()<>.\-+`|{}])", r"\1", s)
    return s

def scrub(s):
    if s is None:
        return None
    s = MAILTO.sub("", s)
    s = WA_LINK.sub("[whatsapp link removed]", s)
    s = EMAIL.sub("[email removed]", s)
    # long digit runs that are not money/years
    s = PHONE.sub(lambda m: m.group(0) if re.search(r"[₹$]", s[max(0, m.start()-2):m.start()]) else "[number removed]", s)
    s = s.replace("@{WhatsApp handle}", "")
    return s

def strip_handles(s):
    """Remove WhatsApp mention handles: '@name' -> 'name', bare '@' dropped."""
    s = re.sub(r"@\{WhatsApp handle\}", "", s)
    s = re.sub(r"@\s?([A-Za-z][\w.]*)", r"\1", s)
    s = re.sub(r"(?<=[\s(,])@(?=[\s),])", "", s)
    return s

def clean(s):
    return re.sub(r"\s+", " ", strip_handles(scrub(unescape(s)))).strip()

# ---------- sectioning ----------
lines = text.split("\n")
paras, cur, cur_start = [], [], 0
for i, l in enumerate(lines):
    if l.strip() == "":
        if cur:
            paras.append((cur_start, "\n".join(cur)))
            cur = []
    else:
        if not cur:
            cur_start = i
        cur.append(l)
if cur:
    paras.append((cur_start, "\n".join(cur)))

SECTION_HEADS = {
    "## Non-joiners": "non_joiners", "## To be Added:": "to_be_added", "# Added": "added",
    "# Intros": "intros", "## Warm Welcomes": "warm_welcomes", "# templates": "templates",
    "# Hissa Outreach": "outreach_hissa", "# Prath Outreach": "outreach_prath", "# HBD Outreach": "outreach_hbd",
}
section = "preamble"
tagged = []
for idx, (ln, p) in enumerate(paras):
    head = p.strip().split("\n")[0].strip()
    for h, name in SECTION_HEADS.items():
        if head.rstrip() == h:
            section = name
            break
    else:
        if head.startswith("#"):
            section = "preamble"
    tagged.append((idx, ln, section, p))

# ---------- status lists ----------
LIST_ITEM = re.compile(r"^(?:\s*-\s*)?\**(?P<name>[A-Z][\w.’' ]*?)\s*@\s*(?P<company>[^<\-*\n]+?)\s*(?:\**\s*-?\s*\**)?\s*(?:<?(?P<url>https://claude\.ai/chat/[^\s>\\]+))?\**\s*$")

def parse_list_item(raw):
    s = unescape(raw).replace("**", "").strip().lstrip("-").strip()
    url = None
    m = re.search(r"https://claude\.ai/chat/[^\s>)\\]+", s)
    if m:
        url = m.group(0)
        s = s[:m.start()]
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = s.strip(" -<>")
    if "@" in s:
        name, company = [x.strip(" -") for x in s.split("@", 1)]
    else:
        name, company = s, None
    return name, company, url

list_rows = []
for idx, ln, sec, p in tagged:
    if sec not in ("non_joiners", "to_be_added", "added"):
        continue
    for raw in p.split("\n"):
        r = raw.strip()
        if not r or r.startswith("#") or re.fullmatch(r"[-*\s]*", r.replace("**", "")):
            continue
        if r.startswith("<https://claude.ai") and list_rows:   # url on its own line
            list_rows[-1]["claude_chat_url"] = re.search(r"https://claude\.ai/chat/[^\s>\\]+", r).group(0)
            continue
        name, company, url = parse_list_item(r)
        if not name:
            continue
        list_rows.append(dict(name=name, company=company, claude_chat_url=url, list_section=sec, raw_line=ln + 1))

# Pending invites (strikethrough = done) and Not Joined Yet, inside intros area
pending_rows = []
mode = None
for idx, ln, sec, p in tagged:
    s = p.strip()
    if s.startswith("Pending Invites"):
        mode = "pending_invites"; continue
    if s.startswith("Pending Thank yous") or s.startswith("**Video Intros"):
        mode = None; continue
    if s.startswith("Not Joined Yet"):
        mode = "not_joined_yet"; continue
    if sec == "templates":
        mode = None
    if mode == "pending_invites":
        for raw in p.split("\n"):
            r = raw.strip().lstrip("-").strip()
            if not r:
                continue
            struck = "~~" in r
            r2 = unescape(r).replace("~", "")
            r2 = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", r2).strip()
            if not r2:
                continue
            nm, _, co = r2.partition(" - ")
            pending_rows.append(dict(name=nm.strip(), company=co.strip() or None, list_section="pending_invites",
                                     struck_through=struck, raw_line=ln + 1))
    elif mode == "not_joined_yet":
        nm = unescape(s).strip()
        if nm and "\n" not in nm and len(nm) < 40:
            pending_rows.append(dict(name=nm, company=None, list_section="not_joined_yet", struck_through=False, raw_line=ln + 1))

# ---------- blurbs ----------
ROLE_WORDS = r"(founder|co-?founder|cofounder|ceo|partner|managing|promoter|president|md\b|cto|coo|chairman|director|investor|head|vc|entrepreneur|veteran|banker|filmmaker|podcaster|scion|journalist|doctor|specialist)"
NAME = r"(?:Dr\.? |Md\.? )?[A-Z][A-Za-z.’'\-]*(?: (?:[A-Z][A-Za-z.’'\-]*|van der|aka)){0,4}"
HANDLE_PAREN = r"\s*\*{0,2}\s*\((?:[^()]|\([^()]*\))*?\)"
lead_patterns = [
    # Name (handle/linkedin) ...
    re.compile(rf"^(?:A (?:warm|delayed[^,]*?|highly delayed[^,]*?) (?:welcome|Welcome) to (?:the community )?)?\*{{0,2}}(?P<name>{NAME})\*{{0,2}}{HANDLE_PAREN}"),
    # Welcome to the community Job (@)!
    re.compile(rf"^Welcome to the community (?P<name>{NAME}){HANDLE_PAREN}"),
    # Name is/was ... (no handle)
    re.compile(rf"^(?:A (?:warm|delayed[^,]*?) welcome to |It’s an honor to welcome |A warm welcome to )?\*{{0,2}}(?P<name>{NAME})\*{{0,2}}(?:,| -| is | was | has | had | started | took | spent | belongs | calls )"),
]
hook_pattern = re.compile(rf"(?P<name>{NAME})\s*\*{{0,2}}\s*\((?:(?:[^()]*?)(?:linkedin|@)[^()]*?|\s*_?\s*|@)\)")
pair_pattern = re.compile(rf"^(?P<a>{NAME})\s*(?:\((?:[^()]*)\))?\s*(?:and|&)\s*(?P<b>{NAME})\s*\((?:[^()]*)\)")
pair_pattern2 = re.compile(r"^(?P<a>[A-Z][a-z]+) and (?P<b>[A-Z][a-z]+) (?P<last>[A-Z][a-z]+) \(")

WELCOME = re.compile(r"(join me in (?:welcoming|extending)|warm welcome to|welcome to (?:the|our)|welcoming)", re.I)

CO_TOK = r"[A-Z0-9][\w&’'\-]*(?:\.[A-Za-z0-9]+)*"
COMPANY = rf"{CO_TOK}(?:\s+(?:(?:of|and|&|for)\s+)?{CO_TOK})*"
DESC_NOUN = r"(?:brand|startup|company|platform|fund|chain|unicorn|app|exchange|firm|agency|marketplace|group|player|business|venture|bank|NBFC|lab|school|network)"
ROLE = r"(?:co-?founder|cofounder|[Ff]ounder|CEO|[Pp]artner|MD|President|promoter(?: director)?|COO|CTO|[Hh]ead|[Cc]hairman|[Dd]irector)"
CO_STOP = {"The","This","Think","Many","After","Under","Some","Starting","At","He","She","They","His","Her","India","Today","Their","It","In","With","Some"}
CO_BAD = {"D2C","UK","US","Mumbai","India’s","India's","HR","NFT","B2B","EV","Inverter","HRTech","India","Saas","SaaS","B2B Saas","B2B Travel","EV Battery","91"}

def _tidy(c):
    if not c:
        return None
    c = re.split(r"\.\s", c)[0]
    toks = c.split()
    while toks and (toks[-1] in CO_STOP | {"of", "and", "&"} or toks[-1].isdigit()):
        toks.pop()
    c = " ".join(toks).strip(" .,-*’'")
    if not c or c in CO_BAD or len(c) < 2:
        return None
    return c

def company_from(blurb):
    b = blurb.replace("**", "")
    pats = [
        # founder of the D2C mattress brand - The Sleep Company / founder of the edtech startup - Adda247
        rf"{ROLE}(?: (?:and|&) [A-Za-z]+)?(?: & [A-Z]{{2,4}})?\s+(?:of|at)\s+(?:the\s+)?[^.;()]{{0,60}}?{DESC_NOUN}\s*[-–]\s*(?P<c>{COMPANY})",
        # founder of the D2C brand Troo Good
        rf"{ROLE}\s+(?:of|at)\s+(?:the\s+)?[A-Za-z0-9/\- ]{{0,40}}?{DESC_NOUN}\s+(?P<c>{COMPANY})",
        # founder of X
        rf"{ROLE}(?: (?:and|&) [A-Za-z]+)?(?: & [A-Z]{{2,4}})?\s+(?:of|at|for)\s+(?:the\s+)?(?:unicorn\s*-\s*)?(?P<c>{COMPANY})",
        rf"(?:founded|started|built|runs|building|co-founded)\s+(?P<c>{COMPANY})",
    ]
    best = None
    for pat in pats:
        for m in re.finditer(pat, b):
            c = _tidy(m.group("c"))
            if c:
                if best is None or m.start() < best[0]:
                    best = (m.start(), c)
                break
    return best[1] if best else None

def short_desc_from(blurb, company):
    if not company:
        return None
    i = blurb.find(company)
    if i < 0:
        return None
    tail = blurb[i + len(company):]
    m = re.match(r"\s*(?:\([^)]*\))?\s*(?:,|-|–|—)\s*(?:which is |which |that )?(?:basically )?(?P<d>(?:an?|the|India’s|India's)\s[^.,;]{3,120})", tail)
    if not m:
        m = re.match(r"\s*(?:,|-|–|—)?\s*(?:which|that)\s+(?:is\s+)?(?P<d>[^.,;]{3,120})", tail)
    if not m:
        return None
    words = m.group("d").split()
    return " ".join(words[:14]).rstrip(" -–")

INVESTOR = re.compile(r"\b(VC|venture capital|fund\b|Fund\b|Capital\b|Ventures\b|Partners\b|general partner|GP\b|managing partner|founding partner|angel network|angel investor|private equity|PE investor|family office|investing arm)", re.I)
FOUNDER = re.compile(r"\b(founder|co-?founder|cofounder|promoter|CEO|MD of)\b", re.I)

def role_guess(blurb, company):
    lead = blurb[:260]
    inv = bool(INVESTOR.search(lead)) and re.search(r"(partner|fund|VC|investor|Capital|Ventures|Angels|private equity)", lead)
    if inv and re.search(r"(fund|VC|venture capital|investor|Angels|private equity|angel network|deep-tech VC|micro-VC|venture debt)", lead, re.I):
        return "investor"
    if FOUNDER.search(lead):
        return "founder"
    return "other"

NAME_STOP = {"This","Many","If","And","I","It","Here","Like","Grip","Anyone","You","Not","Please","Founders","My","Welcome","Happy","Folks","Hey","So","The","Hi","Sir","Hello","Last"}

def fix_name(n, flat):
    n = n.replace("**", "").strip()
    n = re.sub(r"^(Please meet|Meet|meet|Similarly|And last but not least -?|Last but not least -?) ", "", n).strip()
    parts = n.split(". ")
    if len(parts) > 1 and not re.fullmatch(r"(Dr|Md|[A-Z](?:\.[A-Z])*)", parts[-2].split()[-1]):
        n = parts[-1]
    n = re.sub(r"[’']s$", "", n).strip()
    n = re.sub(r"^HK/ ", "", n)
    # prefer a longer form of the same first name that appears early in the paragraph
    first = n.split()[0] if n.split() else n
    if len(n.split()) == 1:
        m = re.search(rf"\b{re.escape(first)}((?: (?:van der|[A-Z][a-z]+)){{1,3}}) (?:is|was|has)\b", flat[:300])
        if m:
            n = first + m.group(1)
    return n

def rebuild_parens(t):
    """Replace handle/linkedin parentheticals with just the LinkedIn URL (or nothing)."""
    def rep(m):
        inner = m.group(0)
        li = re.search(r"(?:https?://)?(?:[a-z]{2,3}\.)?linkedin\.com/in/[\w\-%]+/?", inner)
        return f"({li.group(0)})" if li else ""
    t = re.sub(r"\((?:[^()]|\([^()]*\))*?linkedin(?:[^()]|\([^()]*\))*?\)", rep, t)
    t = re.sub(r"\(\s*\*{0,2}@[^()]*\)", rep, t)
    t = re.sub(r"\(\s*_?\s*\)", "", t)
    t = re.sub(r"\(\s*[a-z][\w.]*\s*\)", rep, t)
    return re.sub(r" +([,.!])", r"\1", t)

blurbs = []
batch_no, batch_greeting = 0, None
last_blurb = None
for idx, ln, sec, p in tagged:
    if sec not in ("intros", "warm_welcomes"):
        continue
    s = unescape(p.strip())
    flat = re.sub(r"\s+", " ", s)
    if flat.startswith("#") or flat.startswith("-----") or flat.startswith("—") or flat.startswith("–"):
        if flat.startswith("-----") or flat.startswith("—") or flat.startswith("–"):
            batch_no += 1; batch_greeting = None
        continue
    is_welcome_line = bool(WELCOME.search(flat)) and len(flat) < 260 and not re.search(r"\bis (?:the|a|an)\b", flat)
    if is_welcome_line:
        batch_no += 1
        batch_greeting = clean(flat)
        last_blurb = None
        continue
    names = []
    m2 = pair_pattern2.match(flat)
    pm = pair_pattern.match(flat)
    if m2:
        names = [f"{m2.group('a')} {m2.group('last')}", f"{m2.group('b')} {m2.group('last')}"]
    elif pm and re.search(r"\bare\b", flat[:200]):
        names = [pm.group("a"), pm.group("b")]
    else:
        nm = None
        for pat in lead_patterns:
            mm = pat.match(flat)
            if mm:
                nm = mm.group("name"); break
        if not nm and len(flat) > 300:
            hm = hook_pattern.search(flat)
            if hm:
                nm = hm.group("name")
        if nm:
            names = [nm]
    names = [fix_name(n, flat) for n in names]
    names = [n for n in names if n and n.split()[0] not in NAME_STOP]
    if not names and len(flat) > 200:
        hm = hook_pattern.search(flat)
        if hm:
            nm = fix_name(hm.group("name"), flat)
            if nm.split()[0] not in NAME_STOP:
                names = [nm]
    if re.match(r"^(Many here would probably know|This Diwali)", flat):
        names = []
    # a paragraph that starts with the previous person's first name is a continuation
    if names and last_blurb is not None and len(names) == 1 and \
            names[0].split()[0] == last_blurb["name"].split()[0] and \
            not re.search(r"\(\s*[@_]?\s*\)|\(@|linkedin", flat[:120]):
        last_blurb["extra_paragraphs"].append(clean(flat))
        continue
    # require a role word and some length to count as a blurb
    if names and len(flat) > 140 and re.search(ROLE_WORDS, flat, re.I):
        company = company_from(flat)
        b = clean(rebuild_parens(flat))
        li = re.search(r"(?:https?://)?(?:[a-z]{2,3}\.)?linkedin\.com/in/[\w\-%]+/?", flat)
        group_id = f"b{len(blurbs)}"
        for n in names:
            blurbs.append(dict(name=clean(n).replace("**", ""), company=clean(company) if company else None,
                               blurb=b, short_desc=short_desc_from(b, clean(company)) if company else None,
                               linkedin=li.group(0) if li else None, section=sec, batch_no=batch_no,
                               batch_greeting=batch_greeting, shared_blurb_id=group_id if len(names) > 1 else None,
                               raw_line=ln + 1, extra_paragraphs=[]))
        last_blurb = blurbs[-1]
    else:
        if last_blurb is not None and sec in ("intros", "warm_welcomes"):
            last_blurb["extra_paragraphs"].append(clean(flat))

# headers like **Rohit @ Biz2x** in Warm Welcomes: use as short label for the next blurb
for idx, ln, sec, p in tagged:
    s = unescape(p.strip()).replace("**", "")
    if sec == "warm_welcomes" and re.fullmatch(r"[A-Z][a-z]+ @ [\w. ]+", s):
        nxt = [b for b in blurbs if b["raw_line"] > ln + 1]
        if nxt:
            nxt[0]["header_label"] = s
            nxt[0]["extra_paragraphs"] = [e for e in nxt[0]["extra_paragraphs"]]
# drop header label paragraphs that got attached as extras
for b in blurbs:
    b["extra_paragraphs"] = [e for e in b["extra_paragraphs"] if not re.fullmatch(r"[A-Z][a-z]+ @ [\w. ]+", e)]

# ---------- merge statuses ----------
def norm(n):
    n = re.sub(r"^(dr\.?|md\.?)\s+", "", n.lower())
    return re.sub(r"[^a-z ]", "", n).strip()

def match(row, blist):
    n = norm(row["name"])
    co = (row.get("company") or "").lower()
    co_key = re.sub(r"[^a-z0-9]", "", co)[:5]
    def co_ok(b):
        hay = re.sub(r"[^a-z0-9]", "", ((b.get("company") or "") + " " + (b.get("blurb") or "")).lower())
        return co_key and co_key in hay
    if len(n.split()) >= 2:
        full = [b for b in blist if norm(b["name"]) == n]
        if full:
            return full
    first = n.split()[0] if n else ""
    if first and co_key:
        return [b for b in blist if norm(b["name"]).split()[:1] == [first] and co_ok(b)]
    return []

entries = []
for b in blurbs:
    b.update(added=True, added_basis="introduced in group (blurb in Intros)", list_status=None, claude_chat_url=None)

unmatched_lists = []
for row in list_rows + pending_rows:
    hits = match(row, blurbs)
    status_map = {
        "added": (True, "listed under # Added"),
        "to_be_added": (False, "listed under To be Added"),
        "non_joiners": (False, "listed under Non-joiners (declined / did not join)"),
        "not_joined_yet": (False, "listed under Not Joined Yet"),
        "pending_invites": (True, "Pending Invites, struck through (done)") if row.get("struck_through") else (False, "Pending Invites, not struck through"),
    }
    added, basis = status_map[row["list_section"]]
    if hits:
        for h in hits:
            if row["list_section"] == "pending_invites" and not row.get("struck_through"):
                h["status_conflict"] = "on old Pending Invites list (not struck) but has an intro blurb"
                h["list_status"] = row["list_section"]
                continue
            h["added"], h["added_basis"], h["list_status"] = added, basis, row["list_section"]
            if row.get("claude_chat_url"):
                h["claude_chat_url"] = row["claude_chat_url"]
    else:
        unmatched_lists.append(dict(name=row["name"], company=row.get("company"), blurb=None, short_desc=None,
                                    linkedin=None, section=row["list_section"], batch_no=None, batch_greeting=None,
                                    shared_blurb_id=None, raw_line=row["raw_line"], extra_paragraphs=[],
                                    added=added, added_basis=basis, list_status=row["list_section"],
                                    claude_chat_url=row.get("claude_chat_url")))

# roster lines in templates: "Abhinav Jain Shop101 (acquired by inmobi)"
roster = []
for idx, ln, sec, p in tagged:
    if sec != "templates":
        continue
    for raw in p.split("\n"):
        r = unescape(raw).strip()
        m = re.fullmatch(r"(?P<head>[A-Z][\w. ’'/]+?)\s*\((?P<desc>[^()]+)\)", r)
        if m and len(r) < 120:
            roster.append((m.group("head"), m.group("desc"), ln + 1))
for b in blurbs:
    toks = b["name"].split()
    for head, desc, rln in roster:
        h = head.lower()
        if not toks or not h.startswith(toks[0].lower()):
            continue
        if b["company"] and re.sub(r"[^a-z0-9]", "", b["company"].lower())[:5] in re.sub(r"[^a-z0-9]", "", h):
            b["roster_desc"] = desc
            if len(toks) == 1:
                cut = h.find(re.sub(r"[^a-z0-9 ]", "", b["company"].lower())[:4])
                guess = head[:cut].strip() if cut > 0 else None
                if guess and len(guess.split()) >= 2:
                    b["name_full_from_roster"] = guess
            break
# fill first-name-only entries from the batch greeting ("welcome to Kunal Jain, Tarun Matta, ...")
for b in blurbs:
    if len(b["name"].split()) == 1 and b.get("batch_greeting"):
        m = re.search(rf"\b{re.escape(b['name'])} ((?:[A-Z][a-z]+ ?){{1,2}})(?=,| and|!|\.|$)", b["batch_greeting"])
        if m:
            b["name_full_from_greeting"] = f"{b['name']} {m.group(1).strip()}"
for b in blurbs:
    b["name_as_written"] = b["name"]
    b["name"] = b.get("name_full_from_greeting") or b.get("name_full_from_roster") or b["name"]
    b["short_desc"] = b.get("roster_desc") or b.get("short_desc")
    b["short_desc_source"] = "templates roster line" if b.get("roster_desc") else ("derived from blurb" if b.get("short_desc") else None)

entries = blurbs + unmatched_lists
seen = Counter(norm(e["name"]) for e in entries if len(norm(e["name"]).split()) >= 2)
first_idx = {}
for i, e in enumerate(entries):
    k = norm(e["name"])
    e["raw_index"] = i
    e["duplicate_of"] = first_idx.get(k) if seen.get(k, 0) > 1 else None
    first_idx.setdefault(k, i)
    e["role_guess"] = role_guess(e["blurb"], e["company"]) if e["blurb"] else None
    e["group"] = "Founder Thesis community (single group; founders and VCs together)"
    e["date_added"] = None
    e["source"] = {"system": "google_doc", "doc_title": doc["title"], "doc_id": "1duGZC9l3Th8e3njjgy7MBs6qBG2HcYsSG3qiMvC-7NI",
                   "line": e["raw_line"], "captured": "2026-10-08"}
    for k2 in ("name", "company", "blurb", "short_desc", "batch_greeting"):
        if e.get(k2):
            e[k2] = clean(e[k2])
    e["extra_paragraphs"] = [clean(x) for x in e["extra_paragraphs"]]

# final safety pass: no emails / phones / wa links anywhere
dump = json.dumps(entries, ensure_ascii=False)
assert not EMAIL.search(dump), "email leaked"
assert "chat.whatsapp.com" not in dump and "wa.me" not in dump
assert "{WhatsApp handle}" not in dump

json.dump(entries, open(out, "w"), ensure_ascii=False, indent=1)
print("written", len(entries))
