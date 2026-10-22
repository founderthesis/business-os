"""Codex audit fixes of 22 Oct (CTO checked them against the repo; bug fixes under existing decisions, no new process).
1/ Owner mail (STEP 0f, decision 351): collects every open Akshay ask over 3 days old, guest rows included (decision 385
   moved guest decisions onto Engagements), community adds grouped as one item; each ask mailed once, gone once answered.
2/ One message identity: the RFC Message-ID header is the key, so a mail read from both mailboxes logs once (four sends
   were logged twice, under the Gmail id and the MCP Emails id). A loop-in that carries an ask is that follow-up
   (Tanuj Shori, Mukund Jha, 21 Oct 21:38): logged and counted as the follow-up, closing its step.
3/ Edit notes to Sarika: a pending marker first, "sent" only on a send receipt; an uncertain result is checked in the chat
   and retried once.
4/ The LT chase and nurture cap (d390) is a processing cap, not a hold: unreached rows stay due with "last attempted",
   least recently attempted first.
Zoya and inbox, on the live prompts (d390 rev 3 + fix as deployed 22 Oct). Usage: python3 d-codex22.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX, ZOYA = "trig_0189eZvAD8x4357cfevgZ3No", "trig_01UPT8LDrBDL5JQqW91Awgbo"
BASE = {INBOX: (60397, "e5a2339a8fdbd848"), ZOYA: (60587, "f077b7c7e04fed68")}
KEY = ("MESSAGE IDENTITY (Codex, 22 Oct: four sends were logged twice, once per mailbox). A mail's identity is its RFC "
       "Message-ID header, the same in both mailboxes. Wherever this prompt sets an Activity's Source ID to a message id, use "
       "\"msgid:<Message-ID without angle brackets>\" (the provider's own id only when the header can't be read). Before creating "
       "a mail Activity, look up that key and the provider ids you hold for the message (Gmail id, MCP Emails id): any hit means "
       "it is logged, so add only a missing link.")
EDITS = {
 ZOYA: [
  ("RUN RECORD (AR-20261018-8).", KEY + "\n\nRUN RECORD (AR-20261018-8)."),
  ("Collect: Engagements with Kind Task, Waiting on Akshay and Task state not Done or On hold whose page body has no "
   "\"mailed\" line;",
   "Collect (decisions 351, 385): every open Akshay ask on any Engagement, guest rows and Kind Task rows alike: Waiting on "
   "Akshay, Status not They declined, We declined, Parked or Unresponsive, Task state not Done or On hold, the ask (its "
   "\"Akshay:\" or \"Ask Akshay\" segment) raised more than 3 days ago by its Claude note line, and no \"mailed\" line for "
   "that ask in the page body; every community add (invite or WhatsApp addition asks) together as one item;"),
  ("Add \"mailed <YYYY-MM-DD>\" to each item's page body.",
   "Add \"mailed <YYYY-MM-DD>: <the ask, short>\" to each item's page body (each row of a grouped item). An ask his answer "
   "or Your call has cleared is no longer open, so it drops out of the next mail."),
  ("First log \"Zoya sent: WhatsApp to Sarika: edit notes for <guest>\" with Source ID \"editnotes:<that Activity's id>\" "
   "(a retry never sends twice), then send it this run per TEAM WHATSAPP",
   "First log a pending marker, \"Zoya pending: WhatsApp to Sarika: edit notes for <guest>\" with Source ID "
   "\"editnotes:<that Activity's id>\", then send it this run per TEAM WHATSAPP; only when the send returns a message key, "
   "rename the marker \"Zoya sent: ...\" and add the key. A marker still pending on a later run: read Sarika's chat since "
   "the marker; the message is there: mark it sent; it isn't: send once more, then mark it sent, or \"failed\" with the step "
   "on Akshay's list. Never a second message once one is in the chat (Codex, 22 Oct)"),
  ("at most 10 of those a run; the rest move Next date to the next working day with \"held: LT chase cap\" in the Claude "
   "note.",
   "at most 10 of those a run; the rest stay due exactly as they are (Next date unchanged: a processing cap is not a hold, "
   "Codex 22 Oct) with a Claude note line \"last attempted <YYYY-MM-DD HH:MM> JST\", and each run takes the least recently "
   "attempted first."),
  ("e.g. \"Sreerag, any update from Trishank on the precall? adding @Zoya to coordinate\", Cc you.",
   "e.g. \"Sreerag, any update from Trishank on the precall? adding @Zoya to coordinate\", Cc you. It is that follow-up, "
   "not a loop-in: log it as the step it sends, and it closes that step."),
  ("Replies to a mail they just sent, and steps in your queue that answer them, are exempt.",
   "Replies to a mail they just sent, and steps in your queue that answer them, are exempt. Classify by content, never by "
   "label (Codex, 22 Oct: Tanuj Shori, Mukund Jha): a mail logged as a loop-in that also carries an ask or follow-up is that "
   "follow-up; it counts once toward these limits and closes the step it asked about."),
 ],
 INBOX: [
  ("IDENTITY: one Activity per message, ever. Before creating anything, query Activities once for all candidate ids (SQL, "
   "\"Source ID\" IN (...), 50 at a time; the MCP Emails id for Zoya's inbox).",
   "IDENTITY: one Activity per message, ever. " + KEY + " Before creating anything, query Activities once for all candidate "
   "keys and ids (SQL, \"Source ID\" IN (...), 50 at a time; the MCP Emails id for Zoya's inbox)."),
  ("- Source: Gmail. Source ID: the message id.", "- Source: Gmail. Source ID: the msgid: key (MESSAGE IDENTITY)."),
 ],
}
for tid, edits in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == BASE[tid], (tid, len(s.encode()), sha(s.encode()))
    dashes = s.count("—")
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, (tid, len(b))
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
