"""Cut 1, inbox part (CTO plan 20 Oct, roadmap item 2): the inbox goes back to capture-only.

Failure it prevents: two senders for one step (inbox and Zoya both send close notes, admin and asset replies),
rules the inbox enforces for shows it no longer runs, and a 65 KB prompt where every change is byte surgery.
Removes: every send except the holding reply, the Saurabh thanks, the vendor redirect and WhatsApp to Akshay;
the Templates database (retired: the decision mail fills from the wording page); every Mamatha step (decision 352);
date-gated un#/B2S/HBD switch-over text (all past). Adds: one Cadences pointer.
"""

CADENCES = ('CADENCES (CTO, 20 Oct): every contact cadence and limit number (the daily cap, hold defaults, chase counts, '
            'nurture intervals) is on the Notion page "Cadences" (3ff19a301a7f8143aa95cd89bd6519ec, Controls); where a number '
            'here differs, Cadences wins.\n')

def region(s, start, end, new, keep_end=True):
    i = s.index(start); j = s.index(end, i)
    assert s.count(start) == 1, start[:50]
    return s[:i] + new + (s[j:] if keep_end else s[j + len(end):])

def edit(s):
    R = []  # (old, new) exact replacements
    # Templates retired
    s = region(s, "TEMPLATES (decision 98): collection://", "LINKS (decision 135):",
        'WORDING (decisions 98, 194): the only mail you fill is Akshay\'s decision mail (STEP 6c), from its toggle on the Notion page "Mail and WhatsApp wording" (3fa19a301a7f81b6a807d0f01847dae7): fill the {placeholders}, keep its line breaks, drop bracketed instructions, adapt up to about 40% to the thread (decision 152) but never a fact, price, term, link or the ask, and use only a toggle marked approved. The Templates database is retired: never read it. ')
    s = region(s, "TEMPLATE MODES AND LOGGING (decision 102).", "HOUSE COPIES (", "")
    s = region(s, "HOUSE COPIES (decisions 132, 180, 225, 260).", "ZOYA LIVE (",
        'HOUSE COPIES (decisions 180, 305, 352). Every mail you send from ad@thepodium.in to anyone outside the team has Zoya in Cc, plus Chaandini on Built to Share and Human by Design, unless already on To or Cc; addresses from People rows. Never Mamatha. ALL SHOWS ON ZOYA (decisions 207, 307, 323): Founder Thesis, un#, Built to Share and Human by Design follow ZOYA LIVE alike; guest decisions stay with Akshay and the host boards, the hosts pick slots (Sri, Satish, Arjun), and Chaandini keeps cold outreach until their side replies.\n')
    s = region(s, "ZOYA LIVE (decisions 207, 223; from 16 Oct 2026", "Fetch each data source once",
        'ZOYA LIVE (decisions 207, 223, 307, 323; capture-only, CTO 21 Oct). You send only the STEP 6 holding reply, STEP 6a, STEP 6b and WHATSAPP TO AKSHAY. Every other mail on every show (Akshay\'s decision mail, the sponsored close note, edit-notes, acknowledgement, admin, asset and routine replies, an approved proposal) is Zoya\'s: set Waiting on Zoya with "Zoya: <step>" first in Next action and log nothing as sent. When Akshay\'s own mail hands a thread to Zoya ("@Zoya will take you through the next steps"), take Akshay off, set Waiting on Zoya and put the step he handed over in Next action.\n' + CADENCES)
    s = region(s, "TEAM ROLES (decisions 154, 211, 223).", "YOUR CALL (",
        'TEAM ROLES (decisions 154, 223, 352). Nothing waits on Mamatha: never set Waiting on Mamatha or write "Mamatha:" on any row. Waiting on holds Akshay (a decision only he can make: "Akshay: <step>"), Zoya (every routine mail step: "Zoya: <step>"), a host, or Guest or PR. Outbound rows at New wait on no one (decision 167). "Fix:" flags are data problems for you (decision 90): fix them from the thread and People, else list them in the report.\n')
    R += [
        ('"ok" or "yes" approves the proposal in Next action as written (send the drafted mail in the page body or the template it names; on Founder Thesis a decision mail goes as in STEP 6c and any routine follow-on is "Zoya: <step>", Waiting on Zoya; on a Vendor show row send nothing yourself: Waiting on Zoya, Next action "Zoya: <his instruction>", decision 239;',
         '"ok" or "yes" approves the proposal in Next action as written (a decision mail goes as in STEP 6c; any other mail it approves, including a draft in the page body, is Zoya\'s: Waiting on Zoya, "Zoya: send the approved <what> to <who>"; on a Vendor show row: Waiting on Zoya, Next action "Zoya: <his instruction>", decision 239;'),
        ("- Mail actions allowed: only the sends, drafts, draft deletions, RSVP archiving, invite cancellations and WhatsApp messages the steps below describe, limited on Founder Thesis by ZOYA LIVE. Nothing else: no other sends, replies, forwards, drafts, labels or trash.",
         "- Mail actions allowed: only the sends, draft deletions, RSVP archiving, invite cancellations and WhatsApp messages the steps below describe, limited by ZOYA LIVE. Nothing else: no other sends, replies, forwards, drafts, labels or trash."),
        ("(multi-select: team first names such as Akshay, Mamatha, Sarika; client hosts", "(multi-select: Akshay, Zoya, Sarika, Jaya; client hosts"),
        ('"Mamatha: reply to Rhea with a recording slot", "Ask Akshay', '"Zoya: reply to Rhea with a recording slot", "Ask Akshay'),
        (" Don't link Template on the Email out Activity; the draft already counts.", ""),
        ("b. Written by hand: if the mail does the job of one Templates row (same Purpose and show: thank-you, precall invite, chaser, decline, sponsored offer, release mail, and so on), link that Template on the Email out Activity and leave Edit size empty. If none fits, leave Template empty.\nc. A Draft Activity", "b. A Draft Activity"),
        ("\nd. His mail answers his ask (decision 316", "\nc. His mail answers his ask (decision 316"),
        ("Next date = next working day, Waiting on Mamatha (empty on Founder Thesis: the evals routine sets it), Source Agent,",
         "Next date = next working day, Waiting on empty (Founder Thesis and un#: the evals routine sets it; Built to Share and Human by Design: STEP 5), Source Agent,"),
        ("Then send, never draft (decision 164), a reply-all on that thread from the Templates row \"Edit notes: noted with thanks\" (if the row is missing, send nothing and say so; greet anyone newly looped in by first name in one short line), keeping everyone on the thread plus the house copies in Cc (send_message with replyThreadId and the thread's people as To and Cc, so earlier internal mails are not quoted), within the daily cap. Log it as \"Zoya sent: noted with thanks to <name>\" and link the Template; do not put the row on Akshay's list for it.",
         "The reply is Zoya's: Waiting on Zoya, \"Zoya: noted-with-thanks reply to <name> (edit notes)\"; not Akshay's list."),
        (" The row comes back to Mamatha on that date.", ""),
        ('- A guest, PR person or stakeholder wrote and the thread now waits on us: Mamatha, "Mamatha: reply to <who>: <what they want>".',
         '- A guest, PR person or stakeholder wrote and the thread now waits on us: Zoya, "Zoya: reply to <who>: <what they want>".'),
        ('- Akshay decided (STEP 3): the next step for Mamatha. Book -> "Mamatha: ask <PR or guest> for recording slots"; precall -> "Mamatha: send the precall invite"; sponsored -> "Mamatha: send the sponsored commercials"; decline -> "Mamatha: send the decline" unless it has gone out already.',
         '- Akshay decided (STEP 3): the next step is Zoya\'s. Book -> "Zoya: ask <PR or guest> for recording slots"; precall -> "Zoya: send the precall invite"; sponsored -> "Zoya: send the sponsored commercials"; decline -> "Zoya: send the decline" unless it has gone out already.'),
        ('- A pitch for un#, Built to Share or Human by Design: Mamatha, "Mamatha: new <show> pitch via <PR>, reply or decline". Founder Thesis pitches go to the evals routine.',
         '- A pitch for Built to Share or Human by Design: Akshay, "Akshay: new <show> pitch via <PR>: put it on <host>\'s board, decline or park?". Founder Thesis and un# pitches go to the evals routine.'),
        ('- Sponsored money moved: Mamatha, "Mamatha: <next payment step>".\n', ""),
        ("Mamatha (or anyone tagged Team) sent the mail a row was waiting on Akshay for", "Zoya or anyone tagged Team sent the mail a row was waiting on Akshay for"),
        ("from her own address or ad@thepodium.in.", "from their own address or ad@thepodium.in."),
        ('Daily cap (decision 317): 150 sends across all routines (today\'s JST Activities whose Summary starts "Zoya sent" or "Agent sent", loop-ins excluded).',
         'Daily cap: the number on Cadences, counted as today\'s (JST) Activities whose Summary starts "Zoya sent", loop-ins excluded.'),
        ('body from the Templates row "Vendor or service pitch redirect" (if missing, the STEP 6b one-liner);', "body: the STEP 6b one-liner;"),
        ("No match, or more than one candidate: set Merge status Needs review, Merge note = what you tried and what came close, and list it in the report (the daily sweep mails Mamatha the forms waiting for review). Then move on.",
         "No match, or more than one candidate: set Merge status Needs review, Merge note = what you tried and what came close, and list it in the report. Then move on."),
        ('Other shows: Waiting on Mamatha, Next action "Mamatha: form in, send the likely release date"', 'Other shows: Waiting on Zoya, Next action "Zoya: form in, send the likely release date"'),
        ("- Pitch replies sent (guest names; Saurabh forwards thanked). Drafts created and sent drafts matched (template: edit size).",
         "- Pitch replies sent (guest names; Saurabh forwards thanked). Sent drafts matched (edit size). Steps handed to Zoya (count by type)."),
        ("team members are tagged Team, e.g. Mamatha, Sarika)", "team members are tagged Team, e.g. Sarika, Jaya)"),
        ("their decision or instruction there (Akshay, Chaandini, Mamatha, a host)", "their decision or instruction there (Akshay, a host)"),
        ('Example: "Rhea (Value360) to Mamatha: offers', 'Example: "Rhea (Value360) to Zoya: offers'),
        ("his reply to the PR or guest, a mail to Mamatha)", "his reply to the PR or guest, a mail to Zoya)"),
    ]
    for a, b in R:
        assert s.count(a) == 1, (a[:70], s.count(a))
        s = s.replace(a, b)
    # Sponsored close note: hand to Zoya
    s = region(s, "Then the close note, once: it has gone only if", "Repair, every run,",
        "Then the close note, once, is Zoya's: unless a message from our side since their no already is that close note or Akshay's own reply settling it (one found but not logged: log it with its message id), set Waiting on Zoya and put \"Zoya: send Akshay's sponsored close note to <name>\" first in Next action. ")
    # Mamatha eval bullet (dead since decision 154)
    s = region(s, "- Mamatha sends Akshay a guest evaluation:", "- Akshay decides: his decision", "")
    # STEP 6c: queue only
    s = region(s, "STEP 6c. AKSHAY DECIDED ON THE ROW: SEND THE REPLY (decisions 112, 131, 157, 263)", "a0. ",
        "STEP 6c. AKSHAY DECIDED ON THE ROW: QUEUE HIS DECISION MAIL FOR ZOYA (decisions 112, 157, 263, 313)\nAkshay decides new Founder Thesis and un# guests in Your call (YOUR CALL hands it here) or by setting Tier on a row at Decision pending; text in Next action is never his instruction (decision 263), and Tier on any other Status is not a decision. For each such Engagement with no decision mail from our side on the pitch thread since he decided:\n")
    s = region(s, "a. Pick the Templates row:", "c. Fill the template:",
        'a. Pick the toggle: Tier 1 -> "Tier 1: keen, ask for a pre-call"; Tier 1.5 -> "Tier 1.5: alignment check call"; Tier 2 -> "Tier 2: alignment check call, organic undecided"; Sponsored -> "Sponsored: founder wrote directly" when the pitch came from the guest\'s own address with no PR or agency on the thread (Via empty), else "Sponsored: no organic slot (via PR)".\n')
    R2 = [
        ('{show credentials} (decision 130) = the page body of the Templates row "Show credentials: <show name>" ("Show credentials: Founder Thesis" for FT), pasted', '{show credentials} (decision 130) = the toggle "Show credentials: <show name>", pasted'),
        ("d0. Founder Thesis, and un# from 19 Oct 2026 08:00 JST (decisions 313, P2r; before then un# uses d.): you never send this mail; Zoya does, from her inbox.", "d0. You never send this mail; Zoya does, from her inbox (decisions 313, P2r)."),
        ("6c ends here: e. does not run, Status and Proposed mail stay as they are, and Zoya's STEP 0e moves the row on after a confirmed send.", "Status stays as it is; Zoya's STEP 0e moves the row on after a confirmed send."),
        ("Fill the template as in c. (on un# the pitch sheet", "Fill the toggle as in c. (on un# the pitch sheet"),
    ]
    for a, b in R2:
        assert s.count(a) == 1, (a[:70], s.count(a))
        s = s.replace(a, b)
    s = region(s, "d. Send it, never a draft (decision 131:", "At most 15 per run.", "")
    s = s.replace("At most 15 per run. Founder Thesis and un# only; B2S and HBD have their own process.", "At most 15 per run.", 1)
    # STEP 6d: hand to Zoya
    s = region(s, "STEP 6d. ADMIN AND LOGISTICS ASKS: ANSWER THEM (decision 133)", "Assets for an episode",
        'STEP 6d. ADMIN AND LOGISTICS ASKS (decision 133)\nA message in the last 72 hours that only asks us to confirm a fact (did Akshay get the invite, is the time still fine, did the link or file arrive), with no reply from our side since: check the fact first. It checks out: Waiting on Zoya, "Zoya: admin confirmation to <name>: <the fact, with day, date and time in their time zone>". It doesn\'t (no invite on the calendar): Waiting on Akshay, "Akshay: <who> asks <what>, not found on <where>". Never agree a new date or time, accept or move an invite, or touch fees, terms or a booking decision.\n')
    s = region(s, "THE REPLY, only to a guest, PR or company with no reply from our side since:", "Edit notes (cuts and corrections) are not assets",
        'THE REPLY, only to a guest, PR or company with no reply from our side since, is Zoya\'s: Waiting on Zoya, "Zoya: assets received reply to <name> (<what they sent>)", Claude note line "YYYY-MM-DD: assets received from <name>". ')
    s = region(s, "Edit notes (cuts and corrections) are not assets: STEP 3 handles those.", "\n\nSTEP 6e.", "Edit notes (cuts and corrections) are not assets: STEP 3 handles those.")
    # STEP 6e: classify, hand to Zoya
    R3 = [
        ('On Founder Thesis (ZOYA LIVE) buckets A and B send nothing and log no "Zoya sent": set Waiting on Zoya, Next action "Zoya: <reply type> to <who>: <what they asked>". A plain cancel request on FT still cancels the event as below, then hands the reply to Zoya ("invite cancelled").',
         'Buckets A and B send nothing (ZOYA LIVE): set Waiting on Zoya, Next action "Zoya: <reply type> to <who>: <what they asked>". A plain cancel request still cancels the event as below, then hands the reply to Zoya ("invite cancelled").'),
        ('a file or update shared. Reply-all from ad@thepodium.in, Cc the house copies, a few words only: "thanks <first name>" or "noted, thanks <first name>". Never acknowledge a mail that is itself only thanks or "noted" to us, an out-of-office or auto-reply, a newsletter, or a cc where a team member is the addressee. Log "Zoya sent: acknowledgement to <name>".',
         'a file or update shared: "Zoya: acknowledgement to <name>". Never for a mail that is itself only thanks or "noted" to us, an out-of-office or auto-reply, a newsletter, or a cc where a team member is the addressee.'),
        ("B. Routine, we know the answer: send the reply, never a draft, on the thread from ad@thepodium.in, To the sender, Cc everyone else on it plus the house copies, within the daily cap, using the Templates row named (fill it from the Engagement, keep its line breaks, LINKS rules apply):",
         "B. Routine, we know the answer (Zoya's reply, by type):"),
        ("   - Price asks: Zoya's on FT, and on un# from 19 Oct 2026 08:00 JST (decision 307); before then a un# price ask is bucket C.\n   - A lower-price or discount ask on a Founder Thesis sponsored row: Zoya's, as in STEP 3 (decision 237); beyond STEP 3's test it is C.",
         "   - Price asks, and a lower-price or discount ask on a Founder Thesis sponsored row (decision 237; beyond STEP 3's test it is C)."),
        ('   - Guest cancels or asks to move a recording with no new time agreed. Other shows: no link; we book by hand, so set Waiting on the show\'s coordinator to line up slots and send them to the guest to confirm, after any cancel below. Founder Thesis: "Reschedule after guest cancels" (podm.in/book), adapted to say the invite is cancelled.',
         '   - Guest cancels or asks to move a recording with no new time agreed: "Zoya: rebook <guest> after their cancel" (podm.in/book on Founder Thesis; on the other shows the host picks the slots).'),
        ('Then send "Admin ask: noted, added before release".', '"Zoya: admin ask noted for <name> (added before release)".'),
        ("Reply with only what they asked: the recording link", "Zoya replies with only what they asked: the recording link"),
        ('   Then: Activity "Zoya sent: <template name> to <name>", move Status, Waiting on and Next action on as the template implies (usually Waiting on Guest or PR), Claude note line "YYYY-MM-DD: routine reply sent (<template name>)".',
         '   Then move Status as the reply implies, Claude note line "YYYY-MM-DD: routine reply handed to Zoya (<type>)".'),
        ("Mail that is Mamatha's to act on (PR sends slots, a form, a document on a thread she runs) goes on her list as in STEP 5.\n", ""),
        ("set Membership To invite unless it is already Added, Blurb link = the Engagement's page URL unless it holds an editing-chat link (decision 347), and leave Blurb",
         "set Membership To invite unless it is already Added, leave Blurb link as it is (only the guest's editing chat goes there, decision 359), and leave Blurb"),
        ('Waiting on Guest or PR, Next action "Waiting on <who>: new recording date for <guest> (<date> cancelled at their request; podm.in/book sent <D Mon>)".',
         'Waiting on Zoya, Next action "Zoya: rebook <guest> (<date> cancelled at their request)".'),
    ]
    for a, b in R3:
        assert s.count(a) == 1, (a[:70], s.count(a))
        s = s.replace(a, b)
    return s
