"""AR-20261019-4 part 2, v2: reply owner, protected-status replies, source identity and dates
on Built to Share and Human by Design (Codex disposition of 420ca4f, 19 Oct 19:25 JST).

Bases are the installed prompts, read back 19 Oct:
  Salesblink sync 9,276 B / 6b94365084520118, Zoya 43,704 B / 7f71e2302f155d6f.
Usage: python3 ar20261019-4-replies-build.py <sync base> <zoya base> <sync out> <zoya out>
"""
import hashlib, sys

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]

def apply(s, R):
    for a, b in R:
        assert s.count(a) == 1, a[:70]
        s = s.replace(a, b)
    return s

sb_in, z_in, sb_out, z_out = sys.argv[1:5]
sb = open(sb_in).read()
z = open(z_in).read()
assert sha(sb) == "6b94365084520118", "sync base is not the installed prompt"
assert sha(z) == "7f71e2302f155d6f", "Zoya base is not the installed prompt"

REPLIES = (
    'REPLIES ON BUILT TO SHARE AND HUMAN BY DESIGN (decision 323: replies and follow-ups are Zoya\'s, and Chaandini keeps cold outreach until their side replies; decision 333; AR-20261019-4). This replaces c)\'s owners on both shows; c) still decides what the reply means. Work message by message: get_thread_messages on each thread from STEP 1. An inbound message is one whose "to" is our sending mailbox. Its source ID is "salesblink:<that message record\'s id>", never the thread\'s messageId, which every message in the thread shares.\n'
    '   1. Done already? Look for the Activity with that Source ID. If it exists and the row\'s Claude note has the line "handoff salesblink:<id>", change nothing. If the Activity exists without that line, a run stopped half way: go to 3 with that Activity and never create a second one. A message received before 20 Oct 2026 whose row already has a salesblink sync Claude note line dated on or after the day it arrived was handled under the old rule: record its Activity and the line "handoff salesblink:<id> (handled before 20 Oct)", and change nothing else.\n'
    '   2. Record it: one Activity, Kind Email in, Source Salesblink, Source ID salesblink:<id>, Engagement, People (the lead and anyone on the message\'s cc found in People by email; add the others to Stakeholders), Captured the received date (scheduled_time), Summary "<name> replied (Salesblink <sequence>): <gist>" with no addresses. Page body "## Source": sequence, thread messageId, received time in UTC, subject, the message\'s to and cc, our side\'s last message in that thread (date, to, cc), and the reply text with quoted history cut. Last line "Reply-to: verified <address>" only when Salesblink attributes the message to the lead and its sign-off is the lead\'s (the address is the lead\'s sequence address); otherwise "Reply-to: not verified (<why>, such as written by <name> whose address shows only in quoted text)".\n'
    '   3. Hand off in one update of the row, which also adds "YYYY-MM-DD: handoff salesblink:<id> to <owner> (salesblink sync)" at the top of the Claude note:\n'
    '      - yes, interested, details or a call: Status Interested, step "Zoya: answer <first name> (salesblink:<id>); eval, then Akshay decides on <Satish\'s or Arjun\'s> board (decision 326)", due today.\n'
    '      - later, after a date, not now: Status LT chase, step "Zoya: revisit <first name>: <what they said> (salesblink:<id>)", due their date, else 90 days from today.\n'
    '      - they name another person or address to write to: step "Zoya: write to <who> as <first name> asked (salesblink:<id>)", due today.\n'
    '      - a clear no: They declined as c) says, with the handoff line.\n'
    '      - left the company with nobody named, an out-of-office or an auto-reply: cold outreach, still Chaandini\'s. Human by Design: c) as written. Built to Share: note it only, no date and no owner, while the pause lasts.\n'
    '      Owners: add Zoya to Waiting on; everyone else stays, except Guest or PR on a row at New or Contacted. When the Activity says "Reply-to: not verified", also add Chaandini and put "Chaandini: confirm the address <name> wrote from (salesblink:<id>)" in front of Zoya\'s step.\n'
    '      A row already at a status in the never-move-backward list below: Status and Call type stay, and every other segment of Next action keeps its words, owner and date. The reply step goes in front. At They declined, We declined or Parked a reply reopens nothing: Akshay is added, with step "Akshay: <first name> wrote again on <date> after <status> (salesblink:<id>): <gist>", due today.\n'
    '      Built to Share only, a decision 328 row (Next action starts "On hold: Satish\'s approval rescinded", or its Claude note names decision 328): the hold stays in front, and nobody invites or follows up. Akshay is added, with "Akshay: <first name> replied <date> (salesblink:<id>, <gist>); approval rescinded 18 Oct: put on Satish\'s board?" after the hold note, due today. A clear no is still They declined.\n'
    '   4. Dates. Each segment of Next action carries its own due date as "(due D Mon)". Before adding a step, give every existing segment that has none the row\'s current Next date. The reply step replaces only an "On hold" cold note or Zoya\'s own chase or nurture segment for this same ask; every other segment, and its due date, stays as it was. Never change a calendar event, recording or delivery date. Next date = the earliest due date among the segments; when that is the row\'s existing Next date, keep it exactly, time included.\n'
)

SB = [
    ('- People: collection://e6c44319-7f81-4da6-8b80-8441a4875d7a\n',
     '- People: collection://e6c44319-7f81-4da6-8b80-8441a4875d7a\n- Activities: collection://290f715d-fd45-4203-ade6-3642c2326c6c (Summary, Kind, Source, Source ID, Engagement, People, Captured): Source "Salesblink" for replies (REPLIES)\n'),
    ('Everything else applies as written: b) bounces, e) new rows (state as a) above), g), h) connect safety, and c) every reply in full.',
     'b) records a bounce (Claude note, and "Bounced <date>: find a new email when outreach restarts" after the On hold note) with no Next date and no Waiting on. Everything else applies as written: e) new rows (state as a) above), g), h) connect safety, and every reply as REPLIES says.'),
    ('A reply is never cold: its Status, owner and dated next step follow c), its step replaces',
     'A reply is never cold: its Status, owners and dated next step follow REPLIES, its step replaces'),
    ('so a reply on such a row follows c) and asks Satish afresh, and',
     'so a reply on such a row goes to Akshay as REPLIES says, never straight to an invite, and'),
    ('Human by Design: a) to h) as written.\nNever move a row backward:',
     'Human by Design: a) to h) as written.\n' + REPLIES + 'Never move a row backward:'),
    ('except to append a Claude note when a new reply arrives.\na) MAILED',
     'except to append a Claude note when a new reply arrives (on Built to Share and Human by Design the reply also gets its handoff, as REPLIES says). On both shows LT chase is protected too: a) and d) never touch it, and c) still moves it forward.\na) MAILED'),
]

Z = [
    ('A thread in neither inbox: skip it and say so in the report.',
     'A thread in neither inbox: skip it and say so in the report, except a Salesblink reply handed to you (decision 333, AR-20261019-4): your step names "salesblink:<id>" and the Activity with that Source ID holds the reply. Reconcile first: a mail in your Sent with idempotency_key "zoya-<engagement page id>-salesblink-<id>", or from you to that person after the reply\'s received time, means it went: log it if it isn\'t logged and send nothing. If your inbox holds a newer message from that person, reply on it as usual. Otherwise, only when the Activity ends "Reply-to: verified <address>", send one new mail from your inbox: To that address; Cc everyone outside the team on the reply\'s cc and on our side\'s last message in that thread, Akshay, and Chaandini (house copy on these shows); subject "Re: <the thread\'s subject>"; written as the next message after the Activity\'s reply text (CONTEXT CHECK, SHOW CHECK, LEAK CHECK and the show\'s C templates, as for any reply); that idempotency_key. From then the thread is in your inbox. Not verified, no Activity, or no template that fits: send nothing, keep your step and put the exact blocker in front, "Chaandini: <blocker> (salesblink:<id>)" with Chaandini in Waiting on (an address to confirm, a missing source), or on Akshay\'s list when only he can settle it. After the send: Activity "Zoya sent: reply to <name> (salesblink:<id>)" with the sent message id, then drop only your segment; other owners and segments stay, and Next date becomes the earliest "(due D Mon)" left in Next action, else your next step\'s date.'),
]

sb2 = apply(sb, SB)
z2 = apply(z, Z)
open(sb_out, "w").write(sb2)
open(z_out, "w").write(z2)
for name, s in (("sync", sb2), ("zoya", z2)):
    print(name, len(s.encode()), sha(s))
