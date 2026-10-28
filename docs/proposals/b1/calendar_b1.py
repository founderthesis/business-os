"""B1, calendar (CTO 28 Oct): starts with decision 424. Input: the d420 batch's calendar output (56,348 / b6d381c24680e75a).
Usage: python3 calendar_b1.py <batch calendar.txt> <out.txt>. Further B1 items land here as more edits."""
import hashlib, os, sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "b6d381c24680e75a"
dashes = s.count(chr(0x2014))

def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)

# Decision 424: the booker is not assumed to be the guest (Sakshi Sukhlecha booked Anirudh Damani's precall on 15 Oct and got her own row).
rep("Then search Gmail for the address and the name to learn who they are (a PR pitch, a guest we asked to book, a sales lead, "
    "a friend). Create one Engagement:",
    "Then search Gmail for the address and the name to learn who they are (a PR pitch, a guest we asked to book, a sales lead, "
    "a friend). BOOKER (decision 424, amended): never assume the booker is the guest. Attach to an open Engagement only on "
    "evidence naming its guest: the guest is named in the invite title, description, thread or form; or the booker works at "
    "the guest's own company (not an agency) and that company has exactly one open row on that show. Organisation or email "
    "domain alone never attaches. Attached: add the person to that row's Stakeholders, link the event there, set Call type, "
    "Call link and Next date as STEP 2 does, add the Claude note line \"YYYY-MM-DD: <person> booked <event title> for <guest> "
    "(decision 424)\", and create no row. A booker who acts for someone else (PR, agency, EA, comms, or Via or a Stakeholder "
    "on another row) without that evidence, or with two candidate rows: attach nothing, create nothing, one report line for "
    "the CTO. Only someone booking for themselves with no match gets a new Engagement:")
rep("Family and personal rows go on AD Personal and are never named in a mail or to anyone but Akshay.",
    "Family and personal rows go on AD Personal and are never named in a mail or to anyone but Akshay. FOLD (decision 424): "
    "only a proven duplicate (the same guest on the same show, or a contact's row standing in for the guest's, shown by "
    "BOOKER's evidence, never by organisation or domain alone). Carry every Claude note line, every open Next action segment "
    "and commitment, Waiting on, all Activities, and the Call, Eval and Dossier links to the kept row; read the kept row back; "
    "then Trash the duplicate once no relations remain (decision 416) and list it in the report. Never merge People; both rows "
    "holding different decisions: report it, never Akshay's list.")

out = s.encode()
assert s.count(chr(0x2014)) == dashes and len(out) <= 65536 - 200, len(out)
open(dst, "wb").write(out)
print(os.path.basename(dst), len(out), hashlib.sha256(out).hexdigest()[:16], "headroom", 65536 - 200 - len(out))
