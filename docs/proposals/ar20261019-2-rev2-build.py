"""AR-20261019-2 rev 2 (decision 363): team asks in "All things FT" and @Zoya replies, composed on Cut 1.
Reuses the 19 Oct build's text (ar20261019-2-build.py, 8398b02, design accepted by Cleanup 19 Oct 16:50 JST) and fixes
its review findings:
 1. Outsiders who type @Zoya get only their own booked date and time, the show's approved links, or "with the team":
    nothing from Claude note, eval, Next action, Scheduling, fees, tier or other people.
 2. Replies to people outside the team go only Mon to Fri 09:30 to 19:00 IST; JST quiet hours stay for Akshay and the team.
 3. A teammate is recognised by name or phone against People rows tagged Team, never an id typed in the prompt.
Also: decision 363 counts a message only when its text starts with "@zoya"; the group is found by exact name and type
(no ids in the prompt, so nothing to fill at deploy). Personal chats stay unread: STEP 1's work-chat rule is unchanged.
Usage: python3 ar20261019-2-rev2-build.py <dir with cut-1 outputs trig_<id>.txt> <out dir>"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def sha(s): return hashlib.sha256(s.encode()).hexdigest()[:16]

g = {}
src = open(os.path.join(HERE, "ar20261019-2-build.py"), encoding="utf-8").read()
exec(src[src.index("T0T = '''"):src.index("for f, reps in R.items():")], g)
T0T, R, NOSHOW = g["T0T"], g["R"], g["NOSHOW"]

FIX = [
    ('GROUP CHECK before any post, every run: chats get <ATFT_GROUP_ID> must return the name exactly "All things FT" and chatType group.',
     'GROUP CHECK before any post, every run: chats search "All things FT" must return exactly one chat named exactly "All things FT" with chatType group; use its id.'),
    ("Messages not fromMe, from a participant whose People row is tagged Team,",
     "Messages not fromMe, from a teammate (the author's saved contact name equals the Name of a People row tagged Team, or the author's digits match that row's Phone),"),
    ("- A teammate (People tagged Team):", "- A teammate (recognised as in 0t b):"),
    ('- Anyone else (guest, PR, host): only what the row already says and approved links; else capture it on the row',
     '- Anyone else (guest, PR, host): only their own booked date and time (calendar or the row\'s Next date with Call type set), the approved short links for that row\'s show, or "it\'s with the team, we\'ll come back to you"; never anything from Claude note, eval, Next action, Scheduling, fees, tier or other people. Capture the ask on the row'),
    ("Quiet hours (23:00 to 07:00 JST) hold only for replies to people outside the team: those go at 08:00 JST or later.",
     "Replies to people outside the team go only Mon to Fri 09:30 to 19:00 IST; otherwise they wait for a run inside those hours. Replies to Akshay or the team: any time except 23:00 to 07:00 JST."),
]
for a, b in FIX:
    assert T0T.count(a) == 1, ("T0T", a[:60], T0T.count(a))
    T0T = T0T.replace(a, b)
i = T0T.index("WHICH COUNT:"); j = T0T.index("\n", i)
wc = T0T[i:j]
a = 'WHICH COUNT: "@zoya" in the message\'s own text (not only inside a quoted or forwarded message),'
assert wc.startswith(a), wc[:120]
T0T = T0T[:i] + 'WHICH COUNT (decision 363): the message\'s own text starts with "@zoya", any case (not a quoted or forwarded message),' + wc[len(a):] + T0T[j:]

CUT_PERM_A = 'and STEP 3c sends text messages to Akshay\'s own chat (its id is the "from" of any message of his with fromMe true; never typed). Nowhere else.'
CUT_PERM_B = ('STEP 3c sends text messages to Akshay\'s own chat (its id is the "from" of any message of his with fromMe true; never typed), '
              'STEP 0t posts team asks in "All things FT" (after its check), and STEP 0z replies once in the chat where a message asked @Zoya (AR-20261019-2). '
              'Nowhere else: never an unsolicited message to a guest, PR, host or any other group.')
wa = [(CUT_PERM_A, CUT_PERM_B), ("WHATSAPP IS READ-ONLY, with two exceptions:", "WHATSAPP IS READ-ONLY, with four exceptions:")]
for a, b in R["whatsapp"][1:]:
    if a.startswith("Plain and short, no em dashes, no phone numbers: rows completed in STEP 3d (name: LinkedIn, blurb);"):
        a, b = a.replace("(name: LinkedIn, blurb)", "(name: LinkedIn)"), b.replace("(name: LinkedIn, blurb)", "(name: LinkedIn)")
    if "STEP 0t" in b or "0t" in b:
        b = b.replace(g["T0T"], T0T)
    wa.append((a, b))
EDITS = {"trig_01MnmJYorWrd61K7b5BCqXr1": wa, "trig_01UPT8LDrBDL5JQqW91Awgbo": R["zoya"], "trig_0189eZvAD8x4357cfevgZ3No": R["inbox"]}

src_dir, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for tid, reps in EDITS.items():
    s = open(os.path.join(src_dir, f"{tid}.txt"), encoding="utf-8").read()
    n0 = len(s.encode())
    for a, b in reps:
        assert s.count(a) == 1, (tid, a[:70], s.count(a))
        s = s.replace(a, b)
    if tid == "trig_01MnmJYorWrd61K7b5BCqXr1":
        assert s.count(NOSHOW[0]) == 1; s = s.replace(NOSHOW[0], NOSHOW[1])
    assert len(s.encode()) <= 65536 and "—" not in s
    open(os.path.join(out, f"{tid}.txt"), "w", encoding="utf-8").write(s)
    print(tid, n0, "->", len(s.encode()), sha(s))
