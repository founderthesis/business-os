"""CTOA-20261025-03 phase 3, mail threading and recipients (card 40519a301a7f811696baec7fd01d3541; Codex audit 25 Oct
findings 1, 2 and notes 3 to 8). Evidence: Zoya's 23 Oct MaxVolt and Findoc follow-ups went out as new messages with a
"Re:" subject and no In-Reply-To or References (detached threads), and ONE MAIL PER PERSON PER RUN put Findoc's and
Scalar Field's asks in one mail.
1/ Every follow-up is an MCP Emails reply (email_compose reply, or draft reply then send) on the original thread's
   latest message, so In-Reply-To and References come from it. Never action send with a "Re:" subject, never a fresh
   mail to continue a conversation, never a subject match.
2/ A thread not in Zoya's inbox: Akshay's ad@ loops her in on the original thread (the short follow-up that SENDING
   already allows, or "<first name>, adding @Zoya to coordinate <the ask in a few words>"), Cc Zoya; her mail follows as
   a reply once the thread is in her inbox. Replaces decision 380's fresh-mail branch.
3/ ONE MAIL PER PERSON PER RUN is deleted. Each row's mail stays on its own thread. Two guests share one mail only when
   they are on the same thread (same company, e.g. MaxVolt's Vishal and Mukesh); otherwise the contact caps defer the
   second. Decision 354's "one mail covers both" is limited the same way.
4/ Akshay's addresses: ad@thepodium.in in Cc, never his other aliases in To or Cc (a reply's derived recipients are
   rebuilt). Final read-back of To, Cc and the reply thread before every send (Codex CX-20261026-02).
5/ One receipt: no holding reply when the real answer goes in the same run; at most one per inbound message.
No replay: nothing here resends MOHH, KNAM, Sukant or Divir; CONTEXT CHECK and the existing Sent checks hold.
Zoya on the live prompt (65,160 / bdc550a275e6957d). Usage: python3 d-thread26.py <live dir> <out dir>"""
import sys, os, re, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
ZOYA = "trig_01UPT8LDrBDL5JQqW91Awgbo"
BASE = (65160, "bdc550a275e6957d")
EDITS = [
 # 1/ threading
 ("Reply on the existing thread (action reply, reply_all false, To and Cc set explicitly, on its latest message in your "
  "inbox).",
  "THREADING (Codex, 25 Oct: follow-ups went out as new threads with a \"Re:\" subject and no In-Reply-To). Every mail "
  "that continues a conversation is a reply (email_compose action reply, or draft action reply then send) on the "
  "original thread's latest message in your inbox, so its In-Reply-To and References come from that message; reply_all "
  "false, To and Cc set explicitly. Never action send with a \"Re:\" subject or a fresh mail to continue a thread, and "
  "never pick a thread by subject."),
 # 4/ read-back and aliases
 ("read the draft back, then send it;",
  "read the draft back (To, Cc and that it is a reply on that thread), then send it; any edit is read back again;"),
 ("Cc: Akshay (ad@thepodium.in) on every mail you send, permanently until he says otherwise (decision 262);",
  "Cc: Akshay (ad@thepodium.in) on every mail you send, permanently until he says otherwise (decision 262); never his "
  "other addresses in To or Cc (Codex, 25 Oct): rebuild a reply's recipients without them;"),
 # 2/ loop-in on the original thread instead of a fresh mail
 ("If we wrote last (decision 380): send a fresh mail from your inbox to the current contact (read the thread and any "
  "later mail from that agency for a handover; a PR who left is replaced by whoever took over), Cc the rest of their "
  "side and Akshay, one opening line picking up the earlier conversation, then the approved wording; never on a closed "
  "or declined row.",
  "If we wrote last: from ad@thepodium.in, reply on the original thread's latest message to the current contact (read "
  "the thread and any later mail from that agency for a handover; a PR who left is replaced by whoever took over), Cc "
  "you: \"<first name>, adding @Zoya to coordinate <the ask in a few words>\" (a loop-in; never on a closed or declined "
  "row); your mail follows as a reply once the thread is in your inbox."),
 # 3/ PR people: only a shared thread is combined
 ("and when two of their guests are due the same day, one mail covers both.",
  "and when two of their guests are due the same day, one mail covers both only if both are on one thread (one "
  "company); else each goes on its own thread and the weekly limit defers the second."),
 # 5/ one receipt
 ("Then the holding reply (decision 390, Akshay, 22 Oct), this run, from your inbox on that thread, unless one went on "
  "it in the last 7 days:",
  "Then the holding reply (decision 390, Akshay, 22 Oct), this run, from your inbox on that thread, unless one went on "
  "it in the last 7 days or the real answer goes on it this run (one receipt at most):"),
]
s = open(os.path.join(src, f"{ZOYA}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == BASE, (len(s.encode()), sha(s.encode()))
dashes = s.count("—")
for a, b in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, b)
# 3/ delete ONE MAIL PER PERSON PER RUN (one LIMITS bullet)
m = re.search(r"- ONE MAIL PER PERSON PER RUN \(CTO, 22 Oct\)\..*?\n", s)
assert m and s.count("ONE MAIL PER PERSON PER RUN") == 1
s = s[:m.start()] + ("- ONE THREAD, ONE CONVERSATION (Codex, 25 Oct: Findoc's and Scalar Field's asks went in one mail): "
                     "each row's mail goes on its own thread; never combine rows by To address. Rows on one shared thread "
                     "(one company) may share one mail; otherwise the limits above defer the second.\n") + s[m.end():]
assert "covered by msgid" not in s
b = s.encode()
assert len(b) <= 65536 - 200 and s.count("—") == dashes, len(b)
open(os.path.join(out, f"{ZOYA}.txt"), "wb").write(b)
print(ZOYA, len(b), sha(b), "headroom", 65336 - len(b))
