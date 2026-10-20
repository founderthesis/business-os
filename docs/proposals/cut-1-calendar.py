"""Cut 1, calendar part. Removes: Templates (the wording page is the only wording source; the day-before note's live
Mode was Send, so Founder Thesis keeps sending it from Zoya's inbox and the unused draft path goes), Mamatha steps (352),
dated un#/B2S/HBD switch-over text, the ad@ declined-invite mail on client shows (Zoya's, decision 323).
Adds: decision 359 (a confirmed recording creates the guest's FT Community row; Blurb link never an Engagement URL)
and decision 360 as amended (each precall promise is its own Kind Task row)."""

def region(s, start, end, new):
    assert s.count(start) == 1, start[:60]
    i = s.index(start); j = s.index(end, i)
    return s[:i] + new + s[j:]

def edit(s):
    s = region(s, "ZOYA LIVE (decision 207, fail-closed):", "DRIVE (read only;",
        'ZOYA LIVE (decisions 207, 307, 323, 352). On every show you send only the double-booking check (STEP 1b, from Zoya\'s inbox) and the Founder Thesis day-before note (STEP 3b, from Zoya\'s inbox); thank-yous and client-show day-before notes are drafts for Akshay. Every other mail this prompt describes (a reschedule after a cancel, the declined-invite "is it still on?" question, slot asks, chases, rebooks, form or release mails) you do not send: set Waiting on Zoya with "Zoya: <step>" (e.g. "Zoya: ask Riya if the 21 Oct recording is still on, Arjun declined the invite"); her routine sends it. Decisions go to Akshay ("Akshay: <step>"). Never set Waiting on Mamatha or write "Mamatha:". When you update Next action on a row Waiting on Zoya, add your note after her step (" | "); never put text in front of "Zoya: ...".\n')
    s = region(s, "TEMPLATES (decision 98): collection://", "MAIL FORMAT (decision 184",
        'WORDING (decisions 98, 194): the wording of every mail and draft is the toggle named below on the Notion page "Mail and WhatsApp wording" (3fa19a301a7f81b6a807d0f01847dae7; client shows: Client show mails): fill the {placeholders}, keep its line breaks, drop bracketed instructions, adapt up to about 40% to the thread (decision 152) but never a fact, price, term, link or the ask, and use only a toggle marked approved. The Templates database is retired: never read it. ')
    s = region(s, "TEAM ROLES (decision 154, Akshay, 12 Oct:", "BEFORE EVERY SEND",
        'LOGGING. Every draft you create: an Activity Kind Draft, Summary "Zoya drafted: <what> for <guest>", Draft ID, Source Gmail, Link, Engagement and Episode, Captured today, the full drafted subject and body in the page body (the inbox compares it with what is sent). Every send: "Zoya sent: <what> to <name>" (old rows say "Agent"; wherever this prompt dedupes on a Summary, match both prefixes). DAILY CAP: the number on the Notion page "Cadences" (3ff19a301a7f8143aa95cd89bd6519ec), counted as today\'s Activities whose Summary starts "Zoya sent" or "Agent sent", loop-ins left out.\nHOUSE COPIES (decisions 180, 305, 352): every mail or draft from ad@thepodium.in to anyone outside the team has Zoya in Cc, plus Chaandini on Built to Share and Human by Design, unless already on To or Cc; addresses from People rows; never Mamatha. Guest decisions stay with Akshay and the host boards; the hosts pick slots (Sri, Satish, Arjun).\n')
    R = [
        ("Transcripts: a .txt whose title contains the guest's name and \"transcript\", in that recording's Zencastr folder or in \"Zencastr Transcripts\" (id 11XD5kDLIC4r89GHE7uK4cHiQD6I5Zrz5), put there by the Mac transcript task.",
         "Recording transcripts live only in the Episode's Transcript file (decision 364), put there by the Mac transcript task."),
        ("(multi-select of first names: Akshay, Zoya, Mamatha, Sarika, Sri, ...;", "(multi-select of first names: Akshay, Zoya, Sarika, Sri, ...;"),
        ("- Never send mail, except the Founder Thesis day-before mail in STEP 3b when its template Mode is Send (on client shows it is only ever a draft, decision 313), the declined-invite question to the PR in STEP 2 on shows other than FT (decision 163), and the double-booking check in STEP 1b on FT precalls and recordings (decision 209). Every other FT mail is Zoya's (ZOYA LIVE).",
         "- Never send mail, except the Founder Thesis day-before note in STEP 3b and the double-booking check in STEP 1b on FT precalls and recordings (decision 209), both from Zoya's inbox. Every other mail is Zoya's (ZOYA LIVE)."),
        (" (put it first and keep any other open ask after \" | \"), Waiting on Mamatha only if she still has a prep step (never on FT). Only write what changed.", " (put it first and keep any other open ask after \" | \"). Only write what changed."),
        ('un#, Built to Share and Human by Design (Akshay, 16 Oct: "we book manually, no links are sent: coordinate for slots and then send slots to the guest to get confirmation"): never send podm.in/book or podm.in/30min; Waiting on the show\'s coordinator (Mamatha unless the row names another), Next action "<name>: <recording|precall> on <date> cancelled, coordinate slots and send them to the guest to confirm". Skip if Next action already says so.',
         'un#, Built to Share and Human by Design (Akshay, 16 Oct: "we book manually, no links are sent"): Waiting on Zoya, Next action "Zoya: <recording|precall> on <date> cancelled, get new slots for <host> to pick (no podm.in links)". Skip if Next action already says so.'),
        ('other shows: Waiting on Mamatha, "Mamatha: booked for <date> but no invite on the calendar". Skip if Next action already says so.', 'other shows the same. Skip if the Claude note already says so.'),
        ("Log per TEMPLATE MODES AND LOGGING (Summary", "Log per LOGGING (Summary"),
        ('(Blurb, and Blurb link unless it holds an editing-chat link, on the row, Membership stays Invited)', '(Blurb on the row, Membership stays Invited; Blurb link holds only the guest\'s editing chat, decision 359: never write it)'),
        (', Blurb link = the Engagement\'s page URL (decision 120) unless it holds an editing-chat link (claude.ai/code/...), which stays (decision 347), and LinkedIn;', ', and LinkedIn; never write Blurb link (it holds only the guest\'s editing chat, decision 359);'),
        ('it happened: set Status Recorded, clear Call type, Claude note line "YYYY-MM-DD: recorded <date> (Zencastr audio in Drive)".',
         'it happened: set Status Recorded, clear Call type, Claude note line "YYYY-MM-DD: recorded <date> (Zencastr audio in Drive)", and make sure the guest has an FT Community row (decision 359): by Person, else exact name plus company; none: create it (Name, Company, Person, Source FT guest, Membership To invite, Captured today); one row per person, never a second, and never touch Blurb link.'),
    ]
    for a, b in R:
        assert s.count(a) == 1, (a[:70], s.count(a))
        s = s.replace(a, b)
    s = region(s, "Other shows: send, never draft, a short mail from ad@thepodium.in to the person who booked or pitched", "Either way leave the event, Next date and Status alone",
        "Other shows: the same, with \"Zoya:\" (decision 323). ")
    s = s.replace('- The guest attendee declined but the event still stands (decision 163, Akshay, 13 Oct: "this one invite in which the main star, the guest, has declined: in such cases we should ask PR if it is still on"): the guest is the attendee whose address is on the Guest\'s People row, else the one named in the title. Founder Thesis: send nothing;',
                  '- The guest attendee declined but the event still stands (decision 163): the guest is the attendee whose address is on the Guest\'s People row, else the one named in the title. Founder Thesis: send nothing;', 1)
    # Day-before: Mode retired; FT sends from Zoya with its checks (live Mode was Send), client shows draft
    s = region(s, '- Otherwise take the Templates row "Recording tomorrow: looking forward, prep note". Mode Draft:', "Send sends it from Zoya's inbox, Akshay in Cc, only if all hold:",
        '- Otherwise use the toggle "Recording tomorrow: looking forward, prep note". On un#, Built to Share and Human by Design it is always a draft (decision 313). Founder Thesis (P2r, decision 235): send it from Zoya\'s inbox, Akshay in Cc, only if all hold:')
    s = s.replace("only if all hold:Send sends it from Zoya's inbox, Akshay in Cc, only if all hold:", "only if all hold:", 1)
    a = 'add Akshay to Waiting on and put "Akshay: WhatsApp addition pending: add <guest first name> to the FT Community (invited in the <D Mon> precall). Blurb: <the Engagement\'s page URL>" in Next action (decision 300) (after any open verdict ask, joined with " | ").'
    assert s.count(a) == 1, "wa invite"
    s = s.replace(a, "the add itself is its own Task row (New actions, below; decision 360).")
    # Decision 360 (amended): each precall promise is its own Task row
    s = region(s, "New actions from the precall (decision 209,", "STEP 4. AFTER A RECORDING",
        'New actions from the precall (decisions 209, 360): once per precall (skip if Claude note has "precall <that date> actions checked"), read the Gemini notes and transcript for anything Akshay offered or promised, or the guest side owes: an intro, a deck, numbers, a date, a follow-up call, a group add. Each one is its own Task row in Engagements, never a segment of this row\'s Next action: Name "Task: <the promise> (<guest>, <D Mon> precall)", Kind Task, For engagement = this row, Show = this row\'s Show, Waiting on its owner (Akshay for what he said he would do, Guest or PR for what their side owes), Task state Handed over (Awaiting someone else for their side), Next action "<owner>: <the promise>", Next date the date named, else 7 days after the precall, Source Agent, Source ID "precall:<event id>:<n>" (reuse a row that has that key; never a second), Captured today. A group or community add also makes sure the FT Community row exists as To invite (Invited if Akshay already sent the invite). Write the notes\' key points in the page body under "## Precall notes (<date>)". The eval re-run is the evals routine\'s job once Status is Precall done (decision 172). Claude note line "YYYY-MM-DD: precall <date> actions checked, <n> Task rows".\n\n')
    return s
