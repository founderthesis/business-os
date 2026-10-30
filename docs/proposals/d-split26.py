"""Split carry-ins for launch (CTO, 26 Oct; CTOA-03 items 4 and 7). Edits routines/zoya/parts in place; build.py then
makes FAST and SLOW.
1/ 24-hour team nudge (audit observation 13): an internal Task row whose team owner hasn't answered our ask (mail or
   WhatsApp) within 24 hours gets one WhatsApp nudge in place of that cycle's follow-up mail; a date they give wins and a
   reply on either channel ends it. TEAM WHATSAPP gains the Task owner as a recipient for that nudge only (Ranjita for
   transcripts), found by People Phone, never a typed number.
2/ Schedules at launch: FAST CRON_TZ=Asia/Tokyo 38 7-23 * * * (the Zoya trigger), SLOW CRON_TZ=Asia/Tokyo 50 10,16 * * 1-5
   (new trigger, Zoya's connectors). Decisions 407 and 408 are not Zoya text: 407 is the inbox SLOT CHECK
   (d-slots407.py, base re-pointed by Cleanup) and 408 the WhatsApp routine's STEP 2c (d-slack408.py); they deploy in
   the same window. Usage: python3 d-split26.py   (run from the repo root; build.py's two "hard" variants changed the same way)"""
import os
D = "routines/zoya/parts"
EDITS = [
 ("internal.txt",
  "follow up on the thread of its last Email out Activity (none: a new mail), To that person, Cc Akshay, and set Next "
  "date 2 working days on,",
  "read their WhatsApp chat and mail since our last ask; no answer within 24 hours of it: one WhatsApp nudge to them per "
  "TEAM WHATSAPP (once per ask; log it), else follow up on the thread of its last Email out Activity (none: a new mail), "
  "To that person, Cc Akshay; either way set Next date 2 working days on,"),
 ("hard.txt", "- WhatsApp only to Jaya and Sarika, per TEAM WHATSAPP.", "- WhatsApp only to the team members TEAM WHATSAPP names."),
 ("teamwa.txt",
  "only to these team members: Jaya (invoices, payment confirmations) and Sarika (guest edit feedback).",
  "only to these team members: Jaya (invoices, payment confirmations), Sarika (guest edit feedback), and for the 24-hour "
  "nudge in INTERNAL TASKS b the team member whose Task it is (e.g. Ranjita for transcripts; chat by People Phone)."),
]
for f, a, b in EDITS:
    p = os.path.join(D, f)
    s = open(p, encoding="utf-8").read()
    assert s.count(a) == 1, (f, s.count(a))
    open(p, "w", encoding="utf-8").write(s.replace(a, b))
    print("edited", f)
