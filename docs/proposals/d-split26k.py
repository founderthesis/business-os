"""Release cut: bring zoya-slow under 62,300 bytes (3,236 under the 65,536 cap) by removing repetition and history only.
No rule changes. What goes: dated attributions and rationales ("(Codex, 22 Oct)", "(Akshay, 16 Oct)", "CTO 22 Oct", stories of
what went wrong), decision numbers that only attribute (multi-number lists, and single ones whose rule reads whole without them
or that are cited elsewhere), rules stated in full twice (one full statement kept, the other a pointer), and wordy phrasing said
again in fewer words. Every safeguard, cap, hold, limit, recipient rule, link, id, placeholder and key format stays; a number goes
only where it repeated one stated in full elsewhere (AFTER SEND's gap numbers, PR COORDINATION keeps them). Line-by-line reasons and the before/after checks: split-dryruns/release-cut.md.
Usage: python3 d-split26k.py (repo root), once, on parts that already carry d-split26j."""
import os
D = "routines/zoya/parts"
E = [
 # intro-slow
 ("intro-slow.txt", "in your SLOW run (decision 394: the FAST/SLOW trial).", "in your SLOW run (decision 394)."),
 ("intro-slow.txt", "This run does the follow-up chains (routines 1 to 8), nurture and revival, team work (transcripts, edit notes, "
  "WhatsApps to Jaya and Sarika), payments, snoozes, bounces, vendor forms, Akshay's feedback, the owner mail and the scorecard, and "
  "it reconciles FAST.", "This run does SLOW ORDER's work: follow-up chains (routines 1 to 8), nurture, team work, payments, snoozes, "
  "STEP 0 and RECONCILE."),
 # rules-common, rules-routines
 ("rules-common.txt", " (the un# pitch sheet and the client templates C1 to C19: the words of every un# mail, decisions 305, 306)",
  " (the un# pitch sheet and the client templates C1 to C19: the words of every un# mail)"),
 ("rules-routines.txt", " All eight are live (Akshay, 16 Oct).", " All eight are live."),
 # notion-data
 ("notion-data.txt", "an Engagement with Kind Task is a work item (an internal task, reminder, builder action or other commitment), "
  "never a guest", "an Engagement with Kind Task is a work item, never a guest"),
 ("notion-data.txt", "PERSON STEPS GO ON THEIR ROW (decision 385, Akshay, 21 Oct):", "PERSON STEPS GO ON THEIR ROW (decision 385):"),
 # scope
 ("scope.txt", "SCOPE (decisions 205, 225, 307, 323). Yours:", "SCOPE. Yours:"),
 ("scope.txt", "Akshay still decides un# guests (decisions 263, 301); Sri picks", "Akshay still decides un# guests; Sri picks"),
 ("scope.txt", "Cold outreach stays Chaandini's (C1 and C2): an Outbound row at New or Contacted waits on no one, and you pick "
  "it up once their side replies.", "Cold outreach stays Chaandini's (C1 and C2); Outbound rows as on un#."),
 # actions
 ("actions.txt", "ACTIONS (decision 394, the FAST/SLOW trial; spec docs/proposals/zoya-split.md).", "ACTIONS (decision 394)."),
 ("actions.txt", " and write it back onto that segment before acting, so the same obligation always gets the same key.",
  " and write it back onto that segment before acting."),
 ("actions.txt", "Every other old-format segment is keyed once, before launch, by the keying migration; one still unkeyed (a later "
  "writer's) is FAST's to key", "Any other old-format segment still unkeyed is FAST's to key"),
 # queue-slow
 ("queue-slow.txt", " Reply, decision and hold actions are FAST's (RECONCILE).", ""),
 # internal
 ("internal.txt", "INTERNAL TASKS (decision 376, Akshay, 21 Oct; Rules for Zoya,", "INTERNAL TASKS (Rules for Zoya,"),
 # editnotes
 ("editnotes.txt", "once one is in the chat (Codex, 22 Oct) (guest,", "once one is in the chat (guest,"),
 # snoozed
 ("snoozed.txt", "SNOOZED ASKS (decision 302, Akshay, 17 Oct).", "SNOOZED ASKS."),
 ("snoozed.txt", "he has put off (AR-20261020-1).", "he has put off."),
 ("snoozed.txt", "never sets the row's Next date (rev 2c).", "never sets the row's Next date."),
 # voice
 ("voice.txt", "VOICE (decisions 199, 201, 204, 206, 345).", "VOICE."),
 # sending
 ("sending.txt", "podm.in/why-sponsor (sponsored follow-ups and questions, decision 218)",
  "podm.in/why-sponsor (sponsored follow-ups and questions)"),
 ("sending.txt", "founderthesis.com (the show site and guests' written profiles, decision 332)",
  "founderthesis.com (the show site and guests' written profiles)"),
 ("sending.txt", "Never pass include_attachments on a reply (MCP Emails rejects it; replies never carry",
  "Never pass include_attachments on a reply (replies never carry"),
 ("sending.txt", 'THREADING (Codex, 25 Oct: follow-ups went out as new threads with a "Re:" subject and no In-Reply-To). Every '
  "mail that continues a conversation is a draft action reply, read back (To, Cc, thread) and then sent, on the original thread's "
  "latest message in your inbox, so its In-Reply-To and References come from that message (in MCP Emails each message has its own "
  "thread_id: the thread's latest message is the latest whose References or In-Reply-To holds the original's Message-ID); "
  'reply_all false, To and Cc set explicitly. Never action send with a "Re:" subject or a fresh mail to continue a thread, and '
  "never pick a thread by subject. MCP Emails' reply puts the thread's last sender in To, so on any thread where the team wrote "
  "last (Akshay, you or anyone tagged Team), build the reply as a draft, set To and Cc from the thread (the people outside the team "
  "in To, Akshay in Cc), read the draft back (To, Cc and that it is a reply on that thread), then send it; any edit is read back "
  "again; a retry checks Sent first and reuses that row's unsent draft, never a second draft (CTO, 22 Oct).",
  "THREADING. Every mail that continues a conversation is a draft action reply on the original thread's latest message in your "
  "inbox, so its In-Reply-To and References come from that message (in MCP Emails each message has its own thread_id: the "
  "thread's latest message is the latest whose References or In-Reply-To holds the original's Message-ID); reply_all false, To "
  "and Cc set explicitly from the thread (MCP Emails' reply puts the thread's last sender in To; where the team wrote last, "
  "Akshay, you or anyone tagged Team, the people outside the team go in To, Akshay in Cc); read the draft back (To, Cc and that "
  "it is a reply on that thread), then send it; any edit is read back again; a retry checks Sent first and reuses that row's "
  'unsent draft, never a second draft. Never action send with a "Re:" subject or a fresh mail to continue a thread, and never '
  "pick a thread by subject."),
 ("sending.txt", "To: whoever's move it is (the person you're asking), so it shows prominently; move everyone else to Cc",
  "To: whoever's move it is (the person you're asking); move everyone else to Cc"),
 ("sending.txt", "never his other addresses in To or Cc (Codex, 25 Oct): rebuild", "never his other addresses in To or Cc: rebuild"),
 ("sending.txt", "idempotency_key: the action key (ACTIONS; its SHA-256 hex if longer than 200 characters), never the run date. "
  "When a send may have gone without being logged (no Activity, but a failure after sending), check your Sent and the thread "
  "first; if it went, log it with its message id and send nothing.",
  "idempotency_key: the action key (ACTIONS), never the run date; a send that may have gone unlogged: ACTIONS' check first."),
 ("sending.txt", "send nothing and put it on Akshay's list as before.", "send nothing and put it on Akshay's list."),
 # teamwa
 ("teamwa.txt", "TEAM WHATSAPP (Akshay, 16 Oct).", "TEAM WHATSAPP."),
 ("teamwa.txt", "(e.g. Ranjita for transcripts; chat by People Phone)", "(e.g. Ranjita for transcripts)"),
 # limits
 ("limits.txt", "(decision 346, Akshay, 20 Oct)", "(decision 346)"),
 ("limits.txt", " never start or reset the clock; a mail with a real ask counts even if it also loops someone in.",
  " never start or reset the clock."),
 ("limits.txt", "Classify by content, never by label (Codex, 22 Oct):", "Classify by content, never by label:"),
 ("limits.txt", "(weekdays, runs inside the follow-up window on Cadences, decision 393:", "(weekdays, decision 393:"),
 ("limits.txt", "quiet hours and the caps still do (CTO, 21 Oct).", "quiet hours and the caps still do."),
 # onemail, identity, runrecord
 ("onemail.txt", "ONE THREAD, ONE CONVERSATION (Codex, 25 Oct: Findoc's and Scalar Field's asks went in one mail):",
  "ONE THREAD, ONE CONVERSATION:"),
 ("identity.txt", "MESSAGE IDENTITY (Codex, 22 Oct).", "MESSAGE IDENTITY."),
 ("runrecord.txt", "RUN RECORD (AR-20261018-8).", "RUN RECORD."),
 ("runrecord.txt", "(this prompt's version, CTO 22 Oct)", "(this prompt's version)"),
 # feedback
 ("feedback.txt", " is live at once, because the routines read those pages every run.", " is live at once."),
 # ownermail, scorecard, payments, invites
 ("ownermail.txt", "STEP 0f. OWNER MAIL (decisions 315, 329; email is how Akshay takes decisions).", "STEP 0f. OWNER MAIL."),
 ("ownermail.txt", "Collect (decisions 351, 385):", "Collect:"),
 ("scorecard.txt", "STEP 0g. MONDAY SCORECARD (roadmap item 5).", "STEP 0g. MONDAY SCORECARD."),
 ("payments.txt", "STEP 1b. PAYMENTS (sponsored, Akshay, 16 Oct)", "STEP 1b. PAYMENTS (sponsored)"),
 ("invites.txt", "INVITES (decisions 400, 403, 406; detail on", "INVITES (detail on"),
 # followups
 ("followups.txt", "SELECT BY STATUS AND DATE (Codex, 23 Oct).", "SELECT BY STATUS AND DATE."),
 ("followups.txt", "DATED SEGMENTS (Codex, 26 Oct):", "DATED SEGMENTS:"),
 ("followups.txt", " doesn't stop a due step of yours on another obligation (AR-20261018-2).",
  " doesn't stop a due step of yours on another obligation."),
 ("followups.txt", "NURTURE (AR-20261019-1; Rules for Zoya 5a is the master). Silence never ends a relationship. Approved",
  "NURTURE (Rules for Zoya 5a is the master). Approved"),
 ("followups.txt", "Only the chase segment changes; other segments, owners and asks stay (AR-20261018-2).",
  "Only the chase segment changes (WRITE PATH)."),
 ("followups.txt", "PR COORDINATION (Akshay, 19 Oct):", "PR COORDINATION:"),
 ("followups.txt", "(retired 19 Oct, so this ends 2 Nov;", "(this hold ends 2 Nov;"),
 ("followups.txt", ", one per sent message, so a retry or a run that sends nothing uses none, within the daily cap.",
  ", one per sent message, within the daily cap."),
 ("followups.txt", "whatever Next action says (AR-20261020-1; a plan written as", "whatever Next action says (a plan written as"),
 ("followups.txt", ', or a row with Tags "No revival" (the no came through a PR or agency; decision 379).',
  ', or a row with Tags "No revival".'),
 ("followups.txt", "; a block (missing data, bounce, a decision someone else holds; an undated Akshay hold or cold outreach is a "
  "hold, never a block) names", "; a block (missing data, bounce, a decision someone else holds) names"),
 ("followups.txt", "AFTER SEND (AR-20261019-1).", "AFTER SEND."),
 # hard
 ("hard.txt", "OUTSIDE MAIL (Cleanup, 21 Oct):", "OUTSIDE MAIL:"),
 ("hard.txt", "OWNERS (AR-20261020-1):", "OWNERS:"),
 # second pass: rules stated twice, kept once
 ("notion-data.txt", 'Next action segment "<owner>: <step>" after " | " (other segments kept), add',
  'Next action segment "<owner>: <step>" after " | ", add'),
 ("scope.txt", "Never podm.in links, never podm.in/book.", "Never podm.in links."),
 ("queue-slow.txt", 'YOUR QUEUE (decision 223). "Zoya" is a Waiting on option, and a Zoya segment of Next action is one of your '
  "actions (ACTIONS). This run takes followup, nurture and team actions:",
  'YOUR QUEUE ("Zoya" is a Waiting on option). This run takes followup, nurture and team actions (ACTIONS):'),
 ("internal.txt", "TAKING THE FILE (decision 377):", "TAKING THE FILE:"),
 ("snoozed.txt", "Any segment of Next action, wherever it sits, reading", "Any segment of Next action reading"),
 ("snoozed.txt", "write that into Last activity and the Claude note and put the ask back reflecting it. Then rewrite only that "
  'segment as "Akshay: <ask>" (updated by what you read), add Akshay to Waiting on, drop "(held for Akshay\'s snooze)" from the '
  "steps that waited on it, keep every other segment and owner, set Next date to the earliest date still open on the row, Claude "
  "note line", "write that into Last activity and the Claude note. Then rewrite only that segment as \"Akshay: <ask>\" (updated "
  'by what you read), add Akshay to Waiting on, drop "(held for Akshay\'s snooze)" from the steps that waited on it, Next date per '
  "WRITE PATH, Claude note line"),
 ("sending.txt", "; on un# only unhashed.co/sponsored and unhashed.co/precall.", "; client show links: SCOPE."),
 ("feedback.txt", " The main Claude session builds and deploys it.", ""),
 ("bounces.txt", "Check each inbox on its own (cross-inbox search fails)", "Check each inbox on its own"),
 ("vendor.txt", "Find the person in People by Email (Email or Other emails), else create them",
  "Find the person (PEOPLE MATCH), else create them"),
 ("followups.txt", "In-scope Engagements only. ", ""),
 ("followups.txt", "(weekdays only; under PR COORDINATION its gap, 3 working days for Tier 1 inbound in its first month, 2 for un# "
  "Booking rows)", "(weekdays only; PR COORDINATION's gap where it applies)"),
 # third pass
 ("scope.txt", "Where the FT routine pages set timing, follow them; the words come from the un# templates.",
  "Where the FT routine pages set timing, follow them."),
 ("internal.txt", "LOOK BEFORE ASKING: first search for", "LOOK BEFORE ASKING: search for"),
 ("report-slow.txt", 'Also the run record\'s page body (RUN RECORD, Summary "Run zoya SLOW <start> JST: <status>")',
  "Also the run record's page body (RUN RECORD)"),
 ("followups.txt", " Next date is always the earliest date still open on the row.", ""),
 ("followups.txt", "(LIMITS, decision 346; a PR person per guest thread)", "(LIMITS; a PR person per guest thread)"),
 ("followups.txt", "rows at Status Sponsored offered whose Next date is today or earlier, whatever Next action says",
  "rows at Status Sponsored offered, whatever Next action says"),
 ("followups.txt", ' A row with no "## Next sponsored mail" plans it from the thread and podm.in/why-sponsor first. The planned mail '
  'is in the page body section "## Next sponsored mail": send it',
  ' The planned mail is in the page body section "## Next sponsored mail" (none: plan it from the thread and podm.in/why-sponsor '
  "first): send it"),
 ("followups.txt", "On un#, every 2 working days (PR COORDINATION, decision 382).", "On un#, every 2 working days (PR COORDINATION)."),
 ("followups.txt", ' Akshay, Next action "Ask Akshay: no form from <guest> after <n> chasers. Chase another way, nurture, or close?". '
  "The row never closes on silence.",
  ' Akshay, Next action "Ask Akshay: no form from <guest> after <n> chasers. Chase another way, nurture, or close?".'),
 ("followups.txt", "- 7 Long-term chase: Status LT chase, Next date today or earlier, nurture rows included",
  "- 7 Long-term chase: Status LT chase, nurture rows included"),
 ("followups.txt", ' <n+1> on <D Mon>" (a hold changes only "on <D Mon>", never the key); Claude', ' <n+1> on <D Mon>"; Claude'),
 # fourth pass: decision numbers that only attribute (the rule text is complete without them, or the number is cited elsewhere)
 ("rules-common.txt", "THE RULES ARE IN NOTION (decision 194).", "THE RULES ARE IN NOTION."),
 ("sending.txt", "SENDING (decision 184).", "SENDING."),
 ("bounces.txt", "STEP 0c. BOUNCES (decision 217).", "STEP 0c. BOUNCES."),
 ("vendor.txt", "STEP 0d. VENDOR FORMS (decision 239).", "STEP 0d. VENDOR FORMS."),
 ("voice.txt", "CONTEXT CHECK before every send (decision 216):", "CONTEXT CHECK before every send:"),
 ("voice.txt", ' or "great question(s)" (decision 208).', ' or "great question(s)".'),
 ("voice.txt", "by up to about 40% (decision 152),", "by up to about 40%,"),
 ("voice.txt", "for a call that didn't happen (decision 198).", "for a call that didn't happen."),
 ("feedback.txt", "create a Task row in Engagements (decision 329):", "create a Task row in Engagements:"),
 ("feedback.txt", "are feedback on your mail (decision 315) when", "are feedback on your mail when"),
 ("sending.txt", "never Mamatha (decision 352);", "never Mamatha;"),
 ("sending.txt", "reaches the guest's side directly (decision 373):", "reaches the guest's side directly:"),
 ("sending.txt", "permanently until he says otherwise (decision 262);", "permanently until he says otherwise;"),
 ("followups.txt", "Release mail 1 is yours too (decision 235):", "Release mail 1 is yours too:"),
 ("followups.txt", 'an approved "Patron ask (FT)" (decision 238);', 'an approved "Patron ask (FT)";'),
 ("followups.txt", "- 8 Sponsored revival (decision 355):", "- 8 Sponsored revival:"),
 ("followups.txt", "their own date wins (decision 375).", "their own date wins."),
 ("followups.txt", "signed as you (decision 379), once:", "signed as you, once:"),
 ("scope.txt", "BUILT TO SHARE AND HUMAN BY DESIGN (decision 323).", "BUILT TO SHARE AND HUMAN BY DESIGN."),
 ("scope.txt", "UN# (decision 307).", "UN#."),
 ("scope.txt", "USD 1,500 per feature (unhashed.co/sponsored).", "USD 1,500 per feature."),
 ("notion-data.txt", "PEOPLE MATCH (decision 383),", "PEOPLE MATCH,"),
 ("notion-data.txt", "AKSHAY'S LIST IS A DECISION INBOX (decision 325):", "AKSHAY'S LIST IS A DECISION INBOX:"),
 ("internal.txt", "a. TRANSCRIPT ROWS (decision 377, every show):", "a. TRANSCRIPT ROWS (every show):"),
 ("editnotes.txt", "EDIT NOTES TO SARIKA (decision 226; Sarika", "EDIT NOTES TO SARIKA (Sarika"),
]
for f, a, b in E:
    p = os.path.join(D, f)
    s = open(p, encoding="utf-8").read()
    assert s.count(a) == 1, (f, a[:50], s.count(a))
    open(p, "w", encoding="utf-8").write(s.replace(a, b))
print("edited", len(E))
