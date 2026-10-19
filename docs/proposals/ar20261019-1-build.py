"""AR-20261019-1: persistent nurture, Tier 1 revival, 5-working-day PR coordination, one ask per person across shows.
Applied after Stage B v5, AR-8, AR-2 and simplification part 1. Run: python3 -I par19.py <root>"""
import sys, os, re
ROOT = sys.argv[1]

NURTURE = ('NURTURE (AR-20261019-1, Akshay, 19 Oct; Rules for Zoya section 5a is the master copy). Silence never ends a relationship. '
 'An approved pursuit is a row at Precall requested, Precall done, Sponsored offered, Booking, Booked or LT chase, or with Tier 1, or one Akshay asked to nurture. '
 'When its routine runs out (last step, span over, 60 silent days on sponsored, our last mail a close-out, 3 unanswered chases), move it to nurture instead of closing it: '
 'Status LT chase, Waiting on Zoya, Chase step 0, Next date 30 days after our last mail, Next action "Zoya: nurture <recipient>: <the open ask> (last contact <D Mon>, nurture <n>)". '
 'Nurture mails use routine 7\'s angles (sponsored rows: routine 8\'s, to whoever owns the thread) at 30, 60 and 90 days, then every 120 days, and every 180 days once the row has been in nurture 2 years; the close-out mails (sponsored 14, precall A14, B8 and C4) are not sent. '
 'A reply, a date they volunteer or a real new opening (their verified news, an episode on their topic) puts the row back on its active routine or on their date. '
 'Stops, which send nothing: a clear decline (They declined, with the close note), a no-contact request (a "## Standing" line "no contact <date>, <source>", Status Parked), Akshay\'s decline or park, a no-show gate, and a dated host or show hold in "## Standing" (revisit on its date). An old Unresponsive label or our own close-out mail is not a decline.\n'
 'PR COORDINATION (Akshay, 19 Oct): while a PR or agency person on Via is coordinating a precall or recording that isn\'t booked yet and their side wrote in the last 30 days, the next mail goes 5 working days after the last substantive ask or exchange (a loop-in, a thanks or an out-of-office doesn\'t count; weekdays only, never Diwali week), unless they asked for a hold (their date wins). After 30 quiet days the page\'s schedule takes over. Guest travel or busyness alone doesn\'t stop a check with the coordinator.\n'
 'ONE PERSON, ONE ASK: before any follow-up, nurture or revival mail, read the person\'s other Engagements on every show (People) and their Activities. If another row wrote to them in the last 7 days (14 for nurture or revival), has an unanswered ask, is in a Salesblink sequence (Waiting on Chaandini or a Salesblink Activity), or is Booking, Booked or Recorded on another show, send nothing and move this Next date past it. A hold on one show (a "## Standing" line) never activates through another.\n'
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
   'Next date = the next step\'s due date (weekdays only; 5 working days under PR COORDINATION);'),
  ('After the last step, close the row as the page says.',
   'After the last step, move the row to nurture (NURTURE).'),
  ('rows closed by the staleness gate (name: why),',
   'rows moved to nurture (name: why), rows stopped or held (name: which stop), rows deferred by ONE PERSON, ONE ASK (name: the other row),'),
 ],
 'daily-sweep': [
  ('Eval verdict Book immediately or Strong consider: Status LT chase, Next date 90 days from today, Chase step 0, Waiting on Guest or PR, Next action "Waiting on <who>: 3 chases unanswered (<dates>), keep chasing. Revisit <date>". Any lower verdict, or none: Status Unresponsive, Waiting on empty, Next action "Closed: 3 chases unanswered". An LT chase row stays LT chase while its eval is Strong consider or better; never move it to Unresponsive or to Akshay.',
   'An approved pursuit (AR-20261019-1: Precall requested, Precall done, Sponsored offered, Booking, Booked or LT chase, Tier 1, Eval verdict Book immediately or Strong consider, or one Akshay asked to nurture): Status LT chase, Next date 30 days from today, Chase step 0, Waiting on Zoya, Next action "Zoya: nurture <who>: <the open ask> (3 chases unanswered, <dates>)". Anything else: Status Unresponsive, Waiting on empty, Next action "Closed: 3 chases unanswered". Silence never moves an approved pursuit to Unresponsive or to Akshay; only a clear decline, a no-contact request, Akshay\'s decline or park, or a dated hold in "## Standing" stops it (Rules for Zoya section 5a).'),
  ('closing mail sent with no reply -> Status Unresponsive).',
   'closing mail sent with no reply -> nurture as in STEP 3 for an approved pursuit, else Status Unresponsive).'),
  ('Cap this step at 60 rows a run, oldest Next date first; say in the report how many were left.',
   'Cap this step at 60 rows a run, oldest Next date first; say in the report how many were left.\n'
   'STEP 3r. REVIVAL (AR-20261019-1; Rules for Zoya section 5a). For rows at Unresponsive or LT chase whose Claude note has "revival checked <date> (cleanup): eligible, <reason>" and no later "revival started" line: re-read the row and its "## Standing"; if it now has a decline, a no-contact line, a hold, Akshay\'s decline or park, or an open row for the same person on another show, add "revival skipped: <why>" and stop. Else set Status LT chase, Waiting on Zoya, Chase step 0, Next date = the date cleanup gave (else the next working day), Next action "Zoya: revival <who>: <cleanup\'s reason>", Claude note "YYYY-MM-DD: revival started (cleanup check <date>)". At most 5 a day. Never revive a row without that cleanup line.'),
 ],
 'inbox': [
  ('Eval verdict Book immediately or Strong consider: Status LT chase, Next date 90 days from today, Chase step 0, Waiting on Guest or PR, Next action "Waiting on <who>: 3 chases unanswered (<dates>), keep chasing. Revisit <date>". Any lower verdict, or none: Status Unresponsive, Waiting on empty, Next action "Closed: 3 chases unanswered". An LT chase row stays LT chase while its eval is Strong consider or better.',
   'An approved pursuit (Rules for Zoya 5a): Status LT chase, Next date 30 days out, Chase step 0, Waiting on Zoya, Next action "Zoya: nurture <who> (3 chases unanswered)". Else Status Unresponsive, Waiting on empty, Next action "Closed: 3 chases unanswered".'),
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
