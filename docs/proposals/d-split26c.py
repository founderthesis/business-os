"""Split fixes from the SLOW dry run of 26 Oct (docs/proposals/split-dryruns/slow.md). Edits routines/zoya/parts.
1/ seq-origin keys had no defined raised time: it is the step's due date (the date the previous step set) at T00:00:00+09:00.
2/ Release mail 1 asked for a "confirmed date" the data doesn't hold, so every planned release went on Akshay's list.
   A date is confirmed once Akshay states it in writing or the episode link exists; a planned date alone is a hold
   that rechecks, and only 2 days before Planned release does the missing date go on his list.
3/ STEP 0b read Akshay's guest-facing replies with Zoya in To as feedback. Feedback is his message about your mail.
4/ Holds with no first day (cold outreach, an Akshay hold with no date) couldn't meet the hold rule.
5/ Decision 352's Mamatha swap would put cold-outreach rows in Zoya's queue: it applies to steps Zoya runs.
6/ Bounces and edit notes older than 72 hours fell out unprocessed (Ruchita, Ez): the window is 7 days, deduped by Activity.
   A bounced address on no People row (a typo) tags nobody.
Usage: python3 d-split26c.py (repo root)"""
import os
D = "routines/zoya/parts"
MAM = ("Nothing waits on Mamatha (decision 352): on any row you touch, replace her in Waiting on with Zoya and rewrite "
       "her step as yours.")
MAM2 = ("Nothing waits on Mamatha (decision 352): on any row you touch, replace her in Waiting on with Zoya and rewrite "
        "her step as yours when it is a step you run; a cold-outreach step is never yours, so leave that row as found "
        "and list it in the report.")
EDITS = [
 ("actions.txt",
  "A Claude note date with no time keys as <date>T00:00:00+09:00.",
  "A Claude note date with no time keys as <date>T00:00:00+09:00. A seq origin's raised time is that step's due date "
  "(the date the previous step set, else the row's Next date when the step was written) at T00:00:00+09:00, never the "
  "day you pick it up."),
 ("followups.txt",
  "Missing data (no confirmed date, no episode link, no post options) or a link not yet approved: send nothing and put "
  "\"Akshay: <what's missing> for <guest>'s release mail\" on his list.",
  "A release date is confirmed once Akshay states it in writing or the episode link exists; Planned release alone is "
  "not. Missing data (no confirmed date, no episode link, no post options) or a link not yet approved: send nothing. "
  "More than 2 days before Planned release it is a hold (\"held: release date not confirmed\", recheck 2 days before "
  "Planned release); from then on put \"Akshay: <what's missing> for <guest>'s release mail\" on his list, once per row."),
 ("followups.txt",
  "moves Next date to the first day it may go and writes \"held: <rule> (<what>), recheck <D Mon>\" in the Claude note;",
  "moves Next date to the first day it may go and writes \"held: <rule> (<what>), recheck <D Mon>\" in the Claude note "
  "(a hold with no first day: a cold-outreach hold takes Zoya off Waiting on and leaves Next date to the row's owner; "
  "an Akshay hold with no date puts the row on Waiting on Akshay and rechecks in 7 days);"),
 ("feedback.txt",
  "b. Akshay's replies to you (from ad@thepodium.in, on \"[Zoya test NN]\" threads or any mail you sent) are feedback on "
  "your mail (decision 315).",
  "b. Akshay's replies to you (from ad@thepodium.in, on \"[Zoya test NN]\" threads or any mail you sent) are feedback on "
  "your mail (decision 315) when they speak to you about that mail (its wording, tone, recipients, timing or facts). "
  "His reply written to the guest or their side, with you in To or Cc, is a thread message, not feedback."),
 ("bounces.txt",
  "Check both inboxes for delivery failures in the last 72 hours (mailer-daemon, \"Address not found\").",
  "Check each inbox on its own (cross-inbox search fails) for delivery failures in the last 7 days (mailer-daemon, "
  "\"Address not found\"); skip a bounce whose Activity already exists."),
 ("bounces.txt",
  "For each address you are sure of: tag the person \"Email bounced\" in People,",
  "For each address you are sure of: tag the person \"Email bounced\" in People if a People row holds that address (a "
  "typo variant on no row tags nobody and only changes Via if Via used it),"),
 ("editnotes.txt",
  "read the Activities from the last 72 hours on in-scope rows:",
  "read the Activities from the last 7 days on in-scope rows:"),
 ("queue-slow.txt", MAM, MAM2),
 ("queue-fast.txt", MAM, MAM2),
]
for f, a, b in EDITS:
    p = os.path.join(D, f)
    s = open(p, encoding="utf-8").read()
    assert s.count(a) == 1, (f, a[:50], s.count(a))
    open(p, "w", encoding="utf-8").write(s.replace(a, b))
    print("edited", f)
