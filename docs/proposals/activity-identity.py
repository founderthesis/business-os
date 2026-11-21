"""Activity identity (CTO, 21 Oct, from the first-hourly-day report: the inbox re-logged 24 message ids, 29 extra rows).
One Activity per message id, ever; caps and the 7-day rule count unique message ids.
Composes on the Cut 1 outputs. Usage: python3 activity-identity.py <cut-1 out dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
EDITS = {
 "trig_0189eZvAD8x4357cfevgZ3No": [  # inbox
  ("For each remaining message, check Activities for Source ID = the Gmail message id. If it exists, skip the message. Otherwise create one Activity:",
   "IDENTITY: one Activity per message, ever. Before creating anything, query Activities once for all candidate ids (SQL, \"Source ID\" IN (...), 50 at a time; the MCP Emails id for Zoya's inbox). An id that comes back already has its Activity: create nothing, and never change its Kind, Summary or author (only add a missing link). The same mail read again, by a later run or from the other inbox, makes zero rows. Kind follows the From header. Otherwise create one Activity:"),
 ],
 "trig_01UPT8LDrBDL5JQqW91Awgbo": [  # zoya
  ("counted as today's (JST) Activities whose Summary starts \"Zoya sent\" or \"Agent sent\", loop-ins excluded (decision 207).",
   "counted as today's (JST) Activities whose Summary starts \"Zoya sent\" or \"Agent sent\", loop-ins excluded (decision 207), one per unique Source ID."),
  ("At most one mail from our side to a person per 7 days, whoever sent it.",
   "At most one mail from our side to a person per 7 days, whoever sent it, counted by unique message id (two Activities with one Source ID are one mail)."),
 ],
}
for tid, R in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    for o, n in R:
        assert s.count(o) == 1, (tid, o[:60])
        s = s.replace(o, n)
    assert "—" not in s.replace("Independent review — latest checkpoint", "")
    b = s.encode()
    assert len(b) <= 65536 - 200, (tid, len(b))
    open(os.path.join(out, f"{tid}.txt"), "w", encoding="utf-8").write(s)
    print(tid, len(b), hashlib.sha256(b).hexdigest()[:16])
