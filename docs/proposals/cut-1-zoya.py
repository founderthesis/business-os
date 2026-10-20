"""Cut 1, Zoya part. Removes: dated switch-over text (19 Oct, past), the one-time loop-ins (ran 19 Oct), STEP 0a go-live,
Mamatha steps, Templates, duplicated limit numbers (Cadences is the master). Adds: decisions 354 and 355 live,
follow-up runs work until done (no early stop), the Monday scorecard (roadmap item 5)."""

def region(s, start, end, new):
    assert s.count(start) == 1, start[:60]
    i = s.index(start); j = s.index(end, i)
    return s[:i] + new + s[j:]

SCORECARD = ('STEP 0g. MONDAY SCORECARD (roadmap item 5). In the first run at or after 08:00 JST each Monday, unless an Activity with '
    'Source ID "scorecard:<that Monday, YYYY-MM-DD>" exists: one new mail from your inbox to Akshay only, subject "Zoya: last week '
    '(<D Mon> to <D Mon>)", in his voice, five numbered lines for last Monday 00:00 to Sunday 24:00 JST, counted only from Activities '
    'and Engagements, never estimated: 1/ follow-ups: <due> due, <sent> sent (the sums of last week\'s run records); 2/ sponsored: '
    '<n> conversations moved (a reply from their side or a Status change on a Sponsored offered row), <n> won (Payment 1 received '
    'or a yes), with names; 3/ tier 1: <n> booked (a precall or recording on the calendar), with names; 4/ stuck: up to 3 open rows '
    'whose Next date passed, as "<name>: <whose move>, since <D Mon>"; 5/ next: one line on the week ahead (recordings, releases). '
    'Log it: Kind Email out, Summary "Zoya sent: Monday scorecard <D Mon>", Source ID "scorecard:<that Monday>", the sent message id '
    'in the page body, Captured today.\n\n')

def edit(s):
    R = [
        (" (the last three from 19 Oct 2026 08:00 JST)", ""),
        ("- Client show mails: 3fc19a301a7f817588e2d081af825f8a",
         "- Cadences: 3ff19a301a7f8143aa95cd89bd6519ec (every follow-up schedule and limit number; it is the master: where a routine page or this prompt gives another number, Cadences wins)\n- Client show mails: 3fc19a301a7f817588e2d081af825f8a"),
        ("- Rows Waiting on Mamatha on un# are yours: when you touch one, replace Mamatha with Zoya in Waiting on and rewrite her step as \"Zoya: <step>\". Mamatha is never in Cc on un# mail.\n", ""),
        ("BUILT TO SHARE AND HUMAN BY DESIGN (decision 323, Akshay, 18 Oct: \"Zoya needs to take over follow ups with guests for other shows also - humans miss follow ups\"). From 19 Oct 2026 08:00 JST the UN# rules above hold on both shows, with these differences:",
         "BUILT TO SHARE AND HUMAN BY DESIGN (decision 323, Akshay, 18 Oct: \"humans miss follow ups\"). The UN# rules above hold on both shows, with these differences:"),
        ("Chaandini is in Cc on every mail on these shows, with Akshay (and Mamatha, as HOUSE COPIES says).", "Chaandini is in Cc on every mail on these shows, with Akshay."),
        ("- Rows Waiting on Mamatha or Chaandini on these shows are yours when the step is a reply or follow-up: replace them with Zoya in Waiting on and rewrite the step as \"Zoya: <step>\". Cold outreach stays Chaandini's (C1 and C2; Salesblink is retired, AR-20261019-6):",
         "- Rows Waiting on Chaandini on these shows are yours when the step is a reply or follow-up: replace her with Zoya in Waiting on and rewrite the step as \"Zoya: <step>\". Cold outreach stays Chaandini's (C1 and C2):"),
        ("- One-time loop-in: as for un#, in the same first run on or after 19 Oct 2026 16:00 JST, on open Built to Share and Human by Design threads, up to 40 more, Cc Chaandini too.\n", ""),
        ("Rows waiting on Akshay are never yours to mail.", "Rows waiting on Akshay are never yours to mail. Nothing waits on Mamatha (decision 352): on any row you touch, replace her in Waiting on with Zoya and rewrite her step as yours."),
        ("never Mamatha (decision 260);", "never Mamatha (decision 352);"),
        ("- 8 Sponsored revival: founders who wrote to us directly, as the page says, including They declined rows (Akshay, 16 Oct). Rows closed before 16 Oct 2026 get their first revival mail no earlier than 14 Jan 2027, at most 5 a week.",
         "- 8 Sponsored revival (decision 355): founders who wrote to us directly whose no was to the sponsored price, at most one mail a quarter and only with a new reason to write; never a plain \"not interested\" or anyone who asked us to stop. Start dates and the weekly limit are on Cadences."),
        ("A decline gets Akshay's close note from ad@thepodium.in, unless an Activity \"Zoya sent: sponsored close\" or \"Agent sent: sponsored close\" is already on the row (the inbox sends it too).",
         "A decline gets Akshay's close note from ad@thepodium.in, once: not if the thread already shows it or a \"sponsored close\" Activity is on the row (the inbox hands these to you as \"Zoya: send Akshay's sponsored close note to <name>\")."),
        ("STEP 0e. AKSHAY'S DECISION MAIL (decisions 235, 313, P2r; Founder Thesis, and un# from 19 Oct 2026 08:00 JST).", "STEP 0e. AKSHAY'S DECISION MAIL (decisions 235, 313, P2r; Founder Thesis and un#)."),
        ("; Proposed mail = the matching Templates row, only if one exists (a wording-page mail has none: leave it)", ""),
        ("At most 20 nurture and revival mails a day (JST), counted from today's \"Zoya sent: nurture\" Activities, one per sent message, so a retry or a run that sends nothing uses none (was 10 in each of the two follow-up runs), within the daily cap.",
         "Nurture and revival mails a day: the number on Cadences, counted from today's (JST) \"Zoya sent: nurture\" Activities, one per sent message, so a retry or a run that sends nothing uses none, within the daily cap."),
        ("Plain and short, no em dashes: go-live line (yes or already), feedback handled,", "Plain and short, no em dashes: feedback handled,"),
        ("STEP 1. MAIL TO YOU, AND THREADS LEFT HANGING", SCORECARD.rstrip("\n") + "\n\nSTEP 1. MAIL TO YOU, AND THREADS LEFT HANGING"),
        ("rows skipped and why (cap, 7-day rule, missing data, bounce, context check), anything that failed.", "rows skipped and why (cap, 7-day rule, missing data, bounce, context check), the Monday scorecard (sent or not due), anything that failed."),
        ("After nurture mail n is sent, the next one is due that many days after its send date: n=1: 60, n=2: 90, then 120, and 180 once the start is 2 years old.",
         "After nurture mail n is sent, the next is due the Cadences interval for n after its send date."),
        ("At most 20 moves a day (JST), counted once per move from Claude note entries dated today whose text after the \"YYYY-MM-DD: \" date starts \"nurture started\" and ends \"(Zoya)\"; your own move entries end that way (see the start line above), so the daily sweep's nurture starts never count against you (was 10 in each of the two follow-up runs); list each in the report.",
         "At most 20 moves a day (JST), counted from today's Claude note lines \"nurture started ... (Zoya)\" (the sweep's never count); list each in the report."),
        ("remind on the invoice thread on working days 3, 7 and 14 after the invoice, Jaya, Sarika and Akshay in Cc; after the third,",
         "remind on the invoice thread on the working days Cadences gives, Jaya, Sarika and Akshay in Cc; after the last,"),
        ("When two rows are due for the same person the same day, send the more urgent one (booked-call logistics, then PR coordination, then an active routine, then nurture); the other waits 7 days after that send.",
         "When two rows are due for the same person the same day, send the more urgent one (booked-call logistics, then PR coordination, then an active routine, then nurture); the other waits the 7-day rule."),
        (' Builder items go in one line at the end: "Builder queue: <n> waiting. No routine can wake the builder; to start them, paste this into the main Claude session: Pick up the Engagements Task rows waiting on Builder." (only when n is above 0)', ""),
        ("; Mail issues that went Fixed and live or Observed working since the last owner mail; Kind Task rows Waiting on Builder for more than 24 hours.", "; Mail issues that went Fixed and live or Observed working since the last owner mail."),
    ]
    for a, b in R:
        assert s.count(a) == 1, (a[:70], s.count(a))
        s = s.replace(a, b)
    s = region(s, "SCOPE (decisions 205, 225, 307).", "UN# (decision 307,",
        "SCOPE (decisions 205, 225, 307, 323). Yours: threads linked to an Engagement whose Show is Founder Thesis, un# (3ed19a301a7f8111b5e4d46002a7afe1), Built to Share (3ed19a301a7f819e8f45de04a7c9d025) or Human by Design (3ed19a301a7f815585e7e6c8accaab23); vendor pitch threads and Engagements on the Vendor show page (3fc19a301a7f811b829ae03fa68e235b, STEP 0d); AD Personal threads for misc chase (routine 4). Anything else, or an Engagement with no Show: do nothing.\n")
    s = region(s, "- One-time loop-in (as Rules for Zoya section 9):", "BUILT TO SHARE AND HUMAN BY DESIGN", "")
    s = region(s, "STEP 0. GO-LIVE AND AKSHAY'S FEEDBACK\na. If Rules for Zoya", "b. Akshay's replies to you", "STEP 0. AKSHAY'S FEEDBACK\n")
    s = region(s, "LIMITS\n- Daily cap (decision 317):", "- At most one mail from our side",
        "LIMITS (the numbers are on Cadences)\n- The daily cap and the per-run cap as Cadences gives them, counted as today's (JST) Activities whose Summary starts \"Zoya sent\" or \"Agent sent\", loop-ins excluded (decision 207). Replies to people who wrote to us come first, then your queue, then follow-ups, oldest due first. Stop at the cap and say so.\n")
    s = region(s, "- Follow-ups only on weekdays (India) and only in the runs that start 16:00 to 22:00 JST", "- A hand-written mail",
        "- PR people (decision 354, from its start date on Cadences): for a PR or agency person the 7 days count per guest thread, within that person's weekly limit on Cadences across all their guests, and when two of their guests are due the same day, one mail covers both.\n- Follow-ups go only on the days and in the window Cadences gives (weekdays, runs starting 10:00 to 22:00 JST, decision 362; never Diwali week). A follow-up run works its due list oldest first until it is empty, the cap is reached or a hold applies; never stop early because the window is ending: the next run carries on. Replies and queue steps go any run.\n")
    return s
