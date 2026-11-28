"""Inbox headroom trim (AR-20261019-1 release condition). Behaviour-preserving: each cut removes a restatement of a rule
the same prompt states in full elsewhere (named per cut), or a rationale clause that gives no instruction.
Applies to live, to live + nurture, and to the end of the pending chain. Run: python3 -I ptrim.py <root>"""
import sys, os, re
ROOT = sys.argv[1]
CUTS = [
 # T1: STEP 5 restates STEP 3's sponsored negotiation rule (STEP 3 "Sponsored money on FT is Zoya's" keeps it in full).
 ("(except a lower-price or discount ask on a Founder Thesis sponsored Engagement that meets STEP 3's test, which is Zoya's, decision 237 (a counter-offer below INR 30,000 + GST, any other term, a custom package or a call still goes to Akshay; on un# every negotiation does, decision 307))",
  "(except the Founder Thesis lower-price ask STEP 3 gives Zoya, decision 237)"),
 # T2: STEP 6e B restates the same STEP 3 rule; bucket C still names the exception.
 ("   - A lower-price or discount ask on a Founder Thesis sponsored row (decision 237): Zoya's, \"Zoya: price negotiation reply to <who>\". A counter-offer below INR 30,000 + GST, any other term, a custom package or a call is C; so is every un# negotiation (decision 307).",
  "   - A lower-price or discount ask on a Founder Thesis sponsored row: Zoya's, as in STEP 3 (decision 237); beyond STEP 3's test it is C."),
 # T3: rationale only; the instruction (read the whole chain with get_thread) stays.
 ("read the whole chain with get_thread (search previews show only the oldest messages and miss later Cc's) and collect",
  "read the whole chain with get_thread and collect"),
 # T4: description of the views, no instruction.
 (" Each person works from a view filtered on their name.", ""),
 # T5: STEP 6c c. already sets {show name} = "Founder Thesis" two sentences earlier.
 ("On FT, {show name} is \"Founder Thesis\" and the credentials'", "On FT, the credentials'"),
 # T6: rationale only; YOUR CALL states the same rule (decision 263).
 ("Text in Next action is never his instruction (decision 263): agents and the old sheets write there.",
  "Text in Next action is never his instruction (decision 263)."),
 # T7: the release-date paragraph right below states decision 155 in full.
 (" (a mail that only asks the release date is still bucket C, decision 155)", ""),
]
p = os.path.join(ROOT, 'routines', 'inbox.md')
s = open(p, encoding='utf-8').read()
for a, b in CUTS:
    assert s.count(a) == 1, (s.count(a), a[:70])
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8', newline='').write(s)
t = re.search(r'```text\n(.*?)\n```', s, re.S).group(1)
print('inbox', len(t.encode()))
