"""Split fixes from the FAST dry run of 26 Oct (docs/proposals/split-dryruns/fast-b.md). Edits routines/zoya/parts.
1/ Keying deadlock: only FAST keyed old-format steps and SLOW acted only on keyed ones, so SLOW would never send the ~150
   old-format follow-ups. Each run now keys the old-format steps of its own types, only on rows it acts on this run.
2/ Old-format key time: a Claude note date with no time becomes <date>T00:00:00+09:00.
3/ Message-ID: MCP Emails email_read returns In-Reply-To and References but not the message's own Message-ID; read it
   from action original (decoded in Bash) or by Gmail rfc822msgid lookup.
4/ Threading method: in MCP Emails each message is its own thread_id, so "the original thread's latest message" is the
   latest message whose References or In-Reply-To holds the original's Message-ID.
5/ Decision 404 (bare emoji reply to a no-ask update) had no owner in the split: it is a FAST reply action.
6/ FAST's SENDING pointed to "STEP 0c", which only SLOW has (build.py VARIANT).
Usage: python3 d-split26b.py (repo root)"""
import os
D = "routines/zoya/parts"
EDITS = [
 ("actions.txt",
  "Only FAST keys old-format steps; SLOW acts only on keyed segments and leaves an unkeyed one for FAST's next run, so two "
  "runs never key one step two ways.",
  "Each run keys only the old-format steps of its own types (the type the wording implies decides the run), and only on "
  "rows it acts on this run, so two runs never key one step two ways. A Claude note date with no time keys as "
  "<date>T00:00:00+09:00."),
 ("actions.txt",
  "Not owed: auto-replies, out-of-office, bounces, thanks or acknowledgements only, loop-ins, incidental Cc.",
  "Not owed: auto-replies, out-of-office, bounces, thanks or acknowledgements only, loop-ins, incidental Cc. An update "
  "with no ask gets only decision 404's bare emoji reply (Rules for Zoya), a FAST reply action, once per thread per 7 days."),
 ("sending.txt",
  "so its In-Reply-To and References come from that message;",
  "so its In-Reply-To and References come from that message (in MCP Emails each message has its own thread_id: the "
  "thread's latest message is the latest whose References or In-Reply-To holds the original's Message-ID);"),
 ("identity.txt",
  "A mail's identity is its RFC Message-ID header, the same in both mailboxes.",
  "A mail's identity is its RFC Message-ID header, the same in both mailboxes. MCP Emails email_read shows In-Reply-To "
  "and References but not the message's own Message-ID: read it with action original (decode it in Bash, keep only that "
  "line) or by Gmail search rfc822msgid."),
]
for f, a, b in EDITS:
    p = os.path.join(D, f)
    s = open(p, encoding="utf-8").read()
    assert s.count(a) == 1, (f, a[:40], s.count(a))
    open(p, "w", encoding="utf-8").write(s.replace(a, b))
    print("edited", f)
# FAST variant: SENDING's bounce pointer
bp = "routines/zoya/build.py"
b = open(bp, encoding="utf-8").read()
anchor = ' "fast": [\n'
add = ' "fast": [\n  ("sending", "(STEP 0c)", "(SLOW\'s bounce scan)"),\n'
if '"(SLOW\'s bounce scan)"' not in b:
    assert b.count(anchor) == 1
    open(bp, "w", encoding="utf-8").write(b.replace(anchor, add))
    print("edited build.py")
