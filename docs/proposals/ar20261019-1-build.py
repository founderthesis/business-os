"""AR-20261019-1: persistent nurture, Tier 1 revival, 5-working-day PR coordination, one ask per person across shows.
Applied after Stage B v5, AR-8, AR-2 and simplification part 1. Run: python3 -I par19.py <root>"""
import sys, os, re
ROOT = sys.argv[1]

NURTURE = ('NURTURE (AR-20261019-1, Akshay, 19 Oct; Rules for Zoya section 5a is the master copy). Silence never ends a relationship. '
 'An approved pursuit is a row at Precall requested, Sponsored offered, Booking or LT chase, or with Tier 1, or one Akshay asked to nurture. '
 'GUARD, before any move to nurture by any routine: re-read the row, its calendar events and its thread. A precall or recording on the calendar stops that chase: Status stays (Booked), no new booking ask. A decision Akshay or Jaya holds on this pursuit (a verdict after a precall, a price, an offer, a no-show) keeps the row as it is. Only the chase segment of Next action changes; other " | " segments, their owners in Waiting on, and independent asks stay (AR-20261018-2). '
 'When a routine runs out (last step, span over, 60 silent days on sponsored, our last mail a close-out, 3 unanswered chases) and the GUARD passes, move it to nurture instead of closing it: '
 'Status LT chase, Zoya added to Waiting on, Chase step 0, Next date 30 days after our last mail on the thread, the chase segment of Next action "Zoya: nurture <recipient>: <the open ask> (since <D Mon YYYY>)", Claude note "YYYY-MM-DD: nurture started (<why>)". '
 'Nurture state comes from what happened, never from a typed counter: the start date is that Claude note line (for a row already at LT chase before 20 Oct 2026, the date it first went to LT chase in the Claude note or Activities, else 20 Oct 2026); n = the number of "Zoya sent: nurture" Activities since the start. After nurture mail n is sent, the next one is due that many days after its send date: n=1: 60, n=2: 90, then 120, and 180 once the start is 2 years old. Only a send moves n or the anchor; a run that sends nothing (cap, deferral, failure) leaves them and changes only Next date, with a reason. '
 'Nurture mails use routine 7\'s angles (sponsored rows: routine 8\'s, to whoever owns the thread); the close-out mails (sponsored 14, precall A14, B8 and C4) are not sent. '
 'A reply, a date they volunteer or a real new opening (their verified news, an episode on their topic) puts the row back on its active routine or on their date, and ends that nurture spell. '
 'Stops, which send nothing: a clear decline (They declined, with the close note), a no-contact request (from that person, anywhere: the "## Standing" section, Claude note, Your call or thread; Status Parked; it stops every row of that person), Akshay\'s decline or park, a no-show gate, and a dated host or show hold (Standing, Claude note, Your call or the thread: it stops only that show\'s row, revisit on its date). An old Unresponsive label or our own close-out mail is not a decline.\n'
 'PR COORDINATION (Akshay, 19 Oct): while a PR or agency person on Via is coordinating a precall or recording that isn\'t booked yet and their side wrote in the last 30 days, the next mail goes 5 working days after the last substantive ask or exchange (a loop-in, a thanks or an out-of-office doesn\'t count; weekdays only, never Diwali week), unless they asked for a hold (their date wins). After 30 quiet days the page\'s schedule takes over. Guest travel or busyness alone doesn\'t stop a check with the coordinator.\n'
 'ONE PERSON, ONE ASK: before any follow-up, nurture or revival mail, read the recipient\'s other Engagements on every show (People) and their Activities. Hold this mail only for: a mail to them from any row in the last 7 days (14 for nurture or revival); an active Salesblink sequence to them (Waiting on Chaandini or a Salesblink Activity in 14 days; recheck on its next step or end); or the same ask already open on another row. When two rows are due for the same person the same day, send the more urgent one (booked-call logistics, then PR coordination, then an active routine, then nurture); the other waits 7 days after that send. A Recorded or finished row elsewhere is context, never a reason to wait. Every hold writes Next date and the reason in the row\'s Claude note: "deferred: <other row or Salesblink>, <why>, recheck <D Mon>"; a deferral never changes nurture n. A show hold is never worked round through another show.\n'
 'REVIVAL: a closed row (Unresponsive, or LT chase gone silent) is followed up again only after the daily sweep moved it to nurture from a "revival checked <date> (cleanup): eligible" line in its Claude note. Never a row we or Akshay declined or parked, a no-contact or held row, a target that never wrote back to us (cold outreach stays with its owner), or a guest who already recorded (routine 9 only). '
 'At most 10 nurture and revival mails a run, within the daily cap. Each fits its thread, gives one clear next step and a true reason to write, never invents news or urgency, and never repeats an earlier mail\'s angle to the same person.\n')

R = {
 'zoya': [
  ('Skip any row whose Waiting on includes Akshay or Jaya, any row closed (They declined, We declined, Unresponsive, Parked, Form filled) unless routine 8 covers it, and every row Rules for Zoya section 7 says is never followed up.',
   'Skip a row while Akshay or Jaya holds a decision on this pursuit (a verdict, an offer, a negotiation, a price, a no-show or a hold); an independent ask of theirs on the row (a community or WhatsApp add, sending a draft, an invoice) doesn\'t stop a due step of yours on another obligation (AR-20261018-2). Skip any row closed (They declined, We declined, Unresponsive, Parked, Form filled) unless routine 8 or a revival (NURTURE) covers it, and every row Rules for Zoya section 7 says is never followed up.\n' + NURTURE.rstrip('\n')),
  ('Close the row instead of mailing (Status Unresponsive, or LT chase with Next date 90 days out for Strong consider or better; Waiting on empty; Next action "Closed: <why>"; Claude note line) only when one holds: the routine\'s span is over,',
   'Move the row to nurture (NURTURE) instead of sending the routine\'s next step when one holds: the routine\'s span is over,'),
  ('Never close a row in the 14 days after a loop-in or any mail from Akshay, or where Akshay asked to keep nurturing it (Claude note, Your call or the thread). At most 10 closures a run; list each in the report with the reason so Akshay can reopen. Never restart a closed sponsored thread with a fresh mail (no step R; a row still planned as step R is closed instead).',
   'Never move a row in the 14 days after a loop-in or any mail from Akshay. At most 10 moves a run; list each in the report. Silence never closes a row: only a stop NURTURE names does. A sponsored thread gets no fresh restart (no step R; a row still planned as step R goes to nurture instead).'),
  ('- 7 Long-term chase: Status LT chase, Next date today or earlier. Akshay in Cc.',
   '- 7 Long-term chase: Status LT chase, Next date today or earlier, nurture rows included (NURTURE sets their cadence). Akshay in Cc.'),
  ('Next date = the next step\'s due date (weekdays only);',
   'Next date = the next step\'s due date (weekdays only; 5 working days under PR COORDINATION; for a nurture mail the NURTURE interval from this send, with Activity "Zoya sent: nurture <n> to <name>" and the chase segment kept as "Zoya: nurture <recipient>: <ask> (since <start>)");'),
  ('After the last step, close the row as the page says.',
   'After the last step, move the row to nurture (NURTURE).'),
  ('rows closed by the staleness gate (name: why),',
   'rows moved to nurture (name: why), rows stopped or held (name: which stop), rows deferred by ONE PERSON, ONE ASK (name: the other row),'),
 ],
 'daily-sweep': [
  ('Eval verdict Book immediately or Strong consider: Status LT chase, Next date 90 days from today, Chase step 0, Waiting on Guest or PR, Next action "Waiting on <who>: 3 chases unanswered (<dates>), keep chasing. Revisit <date>". Any lower verdict, or none: Status Unresponsive, Waiting on empty, Next action "Closed: 3 chases unanswered". An LT chase row stays LT chase while its eval is Strong consider or better; never move it to Unresponsive or to Akshay.',
   'First the GUARD (Rules for Zoya section 5a): re-read the row, its calendar and thread; a precall or recording on the calendar keeps the row Booked with no new ask, and a decision Akshay or Jaya holds on this pursuit (verdict, price, offer, no-show) leaves the row as it is. Then, for an approved pursuit (AR-20261019-1: Precall requested, Sponsored offered, Booking or LT chase, Tier 1, Eval verdict Book immediately or Strong consider, or one Akshay asked to nurture): Status LT chase, Zoya added to Waiting on, Chase step 0, Next date 30 days after our last mail on the thread, only the chase segment of Next action becomes "Zoya: nurture <who>: <the open ask> (since <D Mon YYYY>)" (other segments and owners stay), Claude note "YYYY-MM-DD: nurture started (3 chases unanswered, <dates>)". Anything else: Status Unresponsive, Waiting on empty, Next action "Closed: 3 chases unanswered". Silence never moves an approved pursuit to Unresponsive or to Akshay; only a 5a stop does.'),

  ('closing mail sent with no reply -> Status Unresponsive).',
   'closing mail sent with no reply -> nurture as in STEP 3 for an approved pursuit, else Status Unresponsive).'),
  ('Cap this step at 60 rows a run, oldest Next date first; say in the report how many were left.',
   'Cap this step at 60 rows a run, oldest Next date first; say in the report how many were left.\n'
   'STEP 3r. REVIVAL (AR-20261019-1; Rules for Zoya section 5a). For rows at Unresponsive or LT chase whose Claude note has "revival checked <date> (cleanup): eligible, <reason>" and no later "nurture started (revival" line: re-read the row and its "## Standing"; if it now has a decline, a no-contact request, a hold on this show, or Akshay\'s decline or park, add "revival skipped: <why>" and stop. Else set Status LT chase, Zoya added to Waiting on, Chase step 0, Next date = the date cleanup gave (else the next working day; if another row wrote to the person in the last 14 days, 14 days after that mail, noted "deferred: <row>"), Next action "Zoya: nurture <who>: <cleanup\'s reason> (since <D Mon YYYY>)", Claude note "YYYY-MM-DD: nurture started (revival, cleanup check <date>)". A Recorded row elsewhere is context, not a reason to skip. At most 5 a day. Never revive a row without that cleanup line.'),
 ],
 'inbox': [
  ('Eval verdict Book immediately or Strong consider: Status LT chase, Next date 90 days from today, Chase step 0, Waiting on Guest or PR, Next action "Waiting on <who>: 3 chases unanswered (<dates>), keep chasing. Revisit <date>". Any lower verdict, or none: Status Unresponsive, Waiting on empty, Next action "Closed: 3 chases unanswered". An LT chase row stays LT chase while its eval is Strong consider or better.',
   'An approved pursuit passing the GUARD (Rules for Zoya 5a: no booked call, no pending owner decision): Status LT chase, Zoya added to Waiting on, Next date 30 days after our last mail, Chase step 0, chase segment "Zoya: nurture <who>: <ask> (since <D Mon YYYY>)", Claude note "nurture started". Else Status Unresponsive, Waiting on empty, Next action "Closed: 3 chases unanswered".'),
 ],
}
for f, reps in R.items():
    p = os.path.join(ROOT, 'routines', f + '.md')
    s = open(p, encoding='utf-8').read()
    for a, b in reps:
        assert s.count(a) == 1, (f, s.count(a), a[:70])
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8', newline='').write(s)
    t = re.search(r'```text\n(.*?)\n```', s, re.S).group(1)
    print(f, len(t.encode()))
