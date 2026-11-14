"""Cut 1, daily sweep part (base: the due-versus-done build, 35,703 B / 91b93ab03268f60b). Removes: Templates (3e template
review and 6b template mail go with the database; 3d drafts read the wording pages), every Mamatha step (352), dated show
switch-over text. Adds: the Cadences pointer for the cap."""

def region(s, start, end, new):
    assert s.count(start) == 1, start[:60]
    i = s.index(start); j = s.index(end, i)
    return s[:i] + new + s[j:]

def edit(s):
    R = [
        (' Mamatha has no FT tasks and works "Mamatha: waiting on me" (Waiting on contains Mamatha) for the other shows she still runs.', ""),
        ("- In this prompt, \"flag\" means: set Waiting on (multi-select: Akshay, Zoya, Mamatha, Sarika,", "- In this prompt, \"flag\" means: set Waiting on (multi-select: Akshay, Zoya, Sarika,"),
        ("- Never send mail other than STEP 6b and STEP 6c (billing forwards to Jaya), within the daily cap of 150 sends across all routines (decision 317, JST); every Founder Thesis send is Zoya's (ZOYA LIVE). Create drafts only in STEP 3d and per TEMPLATES (a bigger rewrite for Akshay).",
         "- Never send mail other than STEP 6c (billing forwards to Jaya), within the daily cap on the Notion page \"Cadences\" (3ff19a301a7f8143aa95cd89bd6519ec; decision 317, JST); every guest send is Zoya's (ZOYA LIVE). Create drafts only in STEP 3d."),
        ("Search since the row's last Activity for the guest's name and company: his sent mail (in:sent), replies on the PR thread, the \"Eval ready\" mail, and mails from Mamatha saying what Akshay decided.",
         "Search since the row's last Activity for the guest's name and company: his sent mail (in:sent) and replies on the PR thread."),
        ('else flag "Zoya: send the sponsored commercials" (Waiting on Zoya; "Mamatha:" on other shows);', 'else flag "Zoya: send the sponsored commercials" (Waiting on Zoya);'),
        ('A reply from their side that waits on us -> on FT, flag "Zoya: reply to <who>: <what they want>" (Waiting on Zoya),', 'A reply from their side that waits on us -> flag "Zoya: reply to <who>: <what they want>" (Waiting on Zoya),'),
        ('; on other shows "Mamatha: reply to <who>: <what they want>". Our reply sent', '. Our reply sent'),
        ('- Read Gmail for Akshay\'s decision. Found: apply it, and flag the next step, on FT with Waiting on Zoya (book -> "Zoya: ask <PR or guest> for recording slots"; precall -> "Zoya: send the precall invite"; decline not yet sent -> "Zoya: send the decline"); on other shows the same steps go to Mamatha as "Mamatha: ...".',
         '- Read Gmail for Akshay\'s decision. Found: apply it, and flag the next step with Waiting on Zoya (book -> "Zoya: ask <PR or guest> for recording slots"; precall -> "Zoya: send the precall invite"; decline not yet sent -> "Zoya: send the decline").'),
        ('flag "Zoya: ask <PR or guest> for recording slots (eval: book immediately)" with Waiting on Zoya on FT; "Mamatha: ..." on other shows.', 'flag "Zoya: ask <PR or guest> for recording slots (eval: book immediately)" with Waiting on Zoya.'),
        ("Otherwise leave the flag as it is (on FT it waits on Zoya or Akshay, never Mamatha).", "Otherwise leave the flag as it is."),
        ('with Waiting on Zoya on FT ("Mamatha:" on other shows).\n- Promise lapsed', 'with Waiting on Zoya.\n- Promise lapsed'),
        ('Next action "Zoya: chase <who> for <what> (promised by <D Mon>)" on FT (Mamatha and "Mamatha:" on other shows).', 'Next action "Zoya: chase <who> for <what> (promised by <D Mon>)".'),
        ('"Zoya: recorded <date>, send the form reminder" with Waiting on Zoya on FT ("Mamatha:" on other shows).', '"Zoya: recorded <date>, send the form reminder" with Waiting on Zoya.'),
        ('"Zoya: send GST and invoice details" with Waiting on Zoya on FT ("Mamatha:" on other shows).', '"Zoya: send GST and invoice details" with Waiting on Zoya.'),
        ("- On Founder Thesis, skip any row whose Waiting on includes Zoya or whose Next action already starts \"Zoya:\": her routines own its follow-ups (decision 223).", "- Skip any row whose Waiting on includes Zoya or whose Next action already starts \"Zoya:\": her routines own its follow-ups (decision 223)."),
        (" Zoya mails Akshay his items (her STEP 0f); a Notion row never wakes the main session, so Builder items wait until he starts one.", " Zoya mails Akshay his items (her STEP 0f); the CTO reads the Builder queue itself."),
        ("old notes rewritten (STEP 3a); rows changed from Gmail", "old notes rewritten (STEP 3a); owners removed (STEP 3a2); rows changed from Gmail"),
    ]
    for a, b in R:
        assert s.count(a) == 1, (a[:70], s.count(a))
        s = s.replace(a, b)
    s = region(s, "TEMPLATES (decision 98): collection://", "LINKS (decisions 135, 168, 218):",
        'WORDING (decisions 98, 194): drafts (STEP 3d) take their words from the toggle named there on the Notion page "Client show mails" (3fc19a301a7f817588e2d081af825f8a): fill the {placeholders}, keep its line breaks, drop bracketed instructions, never change a fact, price, term, link or the ask. The Templates database is retired: never read it. ')
    s = region(s, "TEAM ROLES (decision 154, Akshay, 12 Oct:", "BEFORE ANY SEND (decisions 216, 217).",
        'TEAM ROLES (decisions 154, 211, 223, 352). Nothing waits on Mamatha: never set Waiting on Mamatha or write "Mamatha:" on any row; a row you touch that waits on her moves to Zoya (a routine step) or Akshay (a decision). On every show Waiting on holds Akshay ("Akshay: <step>", a decision only he can make), Zoya ("Zoya: <step>", every routine mail step), a host, or Guest or PR. Outbound rows at New wait on no one (decision 167). An open row with Waiting on empty, other than Outbound at New and Form filled, gets Guest or PR. "Fix:" flags are data problems for you (decision 90): fix them from the Gmail thread and People, else leave the "Fix:" text and list the row in the report.\nLOGGING. Every draft you create: an Activity Kind Draft, Summary "Zoya drafted: <what> for <guest>", Draft ID, Source Gmail, Link, Engagement and Episode, Captured today, and the drafted subject and body in the page body.\nHOUSE COPIES (decisions 180, 305, 352): every mail or draft from ad@thepodium.in to anyone outside the team has Zoya in Cc, plus Chaandini on Built to Share and Human by Design, unless already on To or Cc; addresses from People rows; never Mamatha. Guest decisions stay with Akshay and the host boards; the hosts pick slots.\nZOYA LIVE (decisions 207, 307, 323): Zoya\'s routine sends every guest follow-up and routine reply on every show: never send one yourself; leave the step on the row as Waiting on Zoya, Next action "Zoya: <step>".\n')
    s = s.replace('a. Take the show\'s Templates row "Pre-release ask (FT)", "(un#)", "(B2S)" or "(HBD)". Skip if Mode is Off.', 'a. Take the show\'s pre-release toggle on "Client show mails" (its pitch sheet and SHOW CHECK apply). No approved toggle for the show: skip and say so.', 1)
    s = s.replace("(team domain only; never Mamatha on Founder Thesis). Subject from the template's Subject with", "(team domain only; never Mamatha). Subject from the toggle's subject line with", 1)
    s = s.replace("c. Log it per TEMPLATE MODES AND LOGGING, and flag the Engagement:", "c. Log it per LOGGING, and flag the Engagement:", 1)
    s = region(s, "STEP 3e. TEMPLATE REVIEW (Fridays only)", "STEP 3g. FOUNDER THESIS GUESTS LIST", "")
    s = region(s, "STEP 6b. TEMPLATE REVIEW MAIL (Fridays only", "STEP 6c. BILLING", "")
    return s
