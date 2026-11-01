"""Tidy Next action (Akshay, 1 Nov, via the CTO): one line per open step, no action keys, history in the Claude note.
Usage: python3 patch.py <routine> <in.txt> <out.txt>, routine one of inbox, calendar, sweep, hostboards.
Inputs: inbox = the msgid patch output (65,334 / 2f3250ed1d45e7db); calendar = the B1 build (57,968 / f6d140196f3b75b4);
sweep = the accepted d420 sweep (35,047 / 06c4120b2cd48ef1); hostboards = live (8,474 / 5819ccf7528ca16f).
Zoya's FAST prompt and SLOW file carry the same rule through routines/zoya/parts (KEYS and NEXT ACTION in actions.txt)."""
import hashlib, os, sys
name, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
INPUT = {"inbox": "2f3250ed1d45e7db", "calendar": "f6d140196f3b75b4", "sweep": "06c4120b2cd48ef1", "hostboards": "5819ccf7528ca16f"}
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == INPUT[name], name
dashes = s.count(chr(0x2014))

def rep(a, b):
    global s
    assert s.count(a) == 1, (name, a[:70], s.count(a))
    s = s.replace(a, b)

RULE = ("NEXT ACTION (Akshay, 1 Nov): one line per open step, \"<owner>: <what>\", about 80 characters, joined by \" | \"; "
        "history, past message dates and reasons go in the Claude note, and action keys only in Action keys. Completing or "
        "superseding a step removes it in the same write; a write that moves Status forward or passes the call date drops the "
        "earlier stage's steps.")
SHORT = ("NEXT ACTION: one line per open step, \"<owner>: <what>\", about 80 characters, joined by \" | \"; "
         "history and reasons go in the Claude note; a step done or superseded leaves in the same write.")

def after_engagements_line(rule):
    """Insert the rule on its own line right after the NOTION list's Engagements line (and its indented detail line)."""
    global s
    i = s.index("collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5")
    j = s.index("\n", i)
    while s[j + 1:j + 3] == "  ":  # an indented detail line under it
        j = s.index("\n", j + 1)
    s = s[:j + 1] + rule + "\n" + s[j + 1:]

if name == "inbox":
    after_engagements_line(SHORT)
    # Room: three sentences that repeat rules stated just before them.
    rep(" The same mail read again, by a later run or from the other inbox, makes zero rows.", "")
    rep(" Kind follows the From header.", "")
    rep("HOURLY (AR-20261019-6): each run takes only new or unfinished work; the look-back windows are catch-up after a missed "
        "run, and more runs never mean more mails.", "HOURLY (AR-20261019-6): only new or unfinished work; more runs never mean more mails.")
elif name == "sweep":
    after_engagements_line(RULE)
    rep("PART A: STEPS 2, 3, 3r, 3a and 3a2.", "PART A: STEPS 2, 3, 3r, 3a, 3a2 and 3t.")
    rep("STEP 3b. LINK STRAY MAIL",
        "STEP 3t. TIDY NEXT ACTION (Akshay, 1 Nov). Open Engagements whose Next action has a step tied to a past stage or a "
        "settled ask, a segment over 120 characters, or a \"[...]\" action key: remove the step (and its Action keys line), "
        "shorten a long one to NEXT ACTION's form keeping its owner and ask, move a bracketed key to Action keys as \"<short "
        "name> = <key>\"; one Claude note line \"YYYY-MM-DD: Next action tidied: removed <what> (daily sweep)\". Never drop a "
        "step whose key is still open or that waits on a decision. At most 30 rows a run, oldest Claude updated first.\n\n"
        "STEP 3b. LINK STRAY MAIL")
else:
    after_engagements_line(RULE)

out = s.encode()
assert s.count(chr(0x2014)) == dashes and len(out) <= 65536 - 200, (name, len(out))
open(dst, "wb").write(out)
print(f"{name:10s} {len(out):6d} {hashlib.sha256(out).hexdigest()[:16]} headroom {65536 - 200 - len(out)}")
