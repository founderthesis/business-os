"""Decisions 411 and 412 (as amended) in the calendar and daily sweep prompts (decision 412 names the calendar; the CTO's
411 order names Sweep STEP 3a). Usage: python3 docs/proposals/d-411-412-cal-sweep.py <live calendar> <live sweep> <out dir>.
Input: the ACTION KEYS outputs of d394-keys.py on the 26 Oct live prompts (calendar 56,155 / dc6a547ff748ee6e, sweep
35,078 / 676ed2404e424127); the anchors also apply to the live prompts alone.
1/ Calendar STEP 4 a (FT, no Zencastr audio 6 hours after the recording): the note-only rule (decision 321) becomes Akshay's
   queue ask on the Engagement (411): "Akshay: did the <D Mon> recording with <guest> happen? Write yes or no in Your call".
2/ Calendar STEP 4c: the FT thank-you draft is a standalone new mail To the guests, Cc the PR, every other stakeholder and the
   house copies, never a reply on the PR thread; no transcript; Akshay's ask reads "(draft ready)" (412).
3/ Calendar STEP 4d: client-show thank-you drafts go without the transcript too (Akshay, 26 Oct: "For the time being - thank
   you drafts to go out without transcript"); the transcript line is left out.
4/ Sweep STEP 3a: an old note about whether a recording happened never becomes "Zoya: confirm with <PR>"; it becomes the 411
   queue ask, and no rewrite ever puts an ask for Akshay on WhatsApp."""
import sys, os, hashlib
cal, swp, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
def edit(src, dst, pairs):
    s = open(src, encoding="utf-8").read()
    for a, b, n in pairs:
        assert s.count(a) == n, (a[:60], s.count(a))
        s = s.replace(a, b)
    assert s.count(chr(0x2014)) == open(src, encoding="utf-8").read().count(chr(0x2014)) and len(s.encode()) <= 65536 - 200
    open(dst, "w", encoding="utf-8").write(s)
    b = s.encode()
    print(os.path.basename(dst), len(b), hashlib.sha256(b).hexdigest()[:16])
edit(cal, os.path.join(out, "calendar.txt"), [
 ("leave Waiting on and Next action alone (decision 321), Claude note line \"YYYY-MM-DD: recorded <date>? no Zencastr audio in Drive\" "
  "(once; don't repeat it on later runs) and a report line. Akshay sets Recorded himself, or pings Zoya, if it happened.",
  "it is still unclear (decision 411: settled from our side only; never ask the guest or PR): once, add Akshay to Waiting on and "
  "the Next action segment \"Akshay: did the <D Mon> recording with <guest> happen? Write yes or no in Your call\", Claude note line "
  "\"YYYY-MM-DD: recorded <date>? no Zencastr audio in Drive, asked Akshay\" and a report line. Never on WhatsApp.", 1),
 ("a reply on the latest thread with the guest or PR, else a new mail", "always a standalone new mail, never a reply on the PR thread (decision 412)", 1),
 ("To: the guest and the main PR contact (Via). Cc: every other Stakeholder and the house copies.",
  "To: the guests. Cc: the PR (Via), every other Stakeholder and the house copies. No transcript, and don't wait for one (decision 412).", 1),
 ("(in your Gmail Drafts; attach the transcript)", "(draft ready)", 2),
 ("the PR block only when a PR is on the To line", "the PR block only when a PR is on the mail", 1),
 ("the transcript line kept so Akshay attaches it", "the transcript line left out (decision 412: no transcript for now)", 1),
])
edit(swp, os.path.join(out, "sweep.txt"), [
 ("\"Remind Akshay\" -> \"Ask Akshay: <what about>\";",
  "\"Remind Akshay\" -> \"Ask Akshay: <what about>\"; a note about whether a recording happened -> Akshay in Waiting on, \"Akshay: did "
  "the <D Mon> recording with <guest> happen? Write yes or no in Your call\" (decision 411: never \"Zoya: confirm with <PR>\", never "
  "the guest or PR, never WhatsApp);", 1),
])
