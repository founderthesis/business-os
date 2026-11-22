# Rulebook r1: edits to the Notion rule pages, applied to a fresh fetch at cutover.
# Ops (all anchors are address-free, so this file carries no email addresses):
#   ("replace", subject, old, new)                 old must occur exactly once
#   ("between", subject, start, end, new)          replace start..end inclusive; each once, end after start
#   ("replace_all", subject, old, new)             old must occur at least once
#   ("drop_toggles", subject, marker)              remove every <toggle ...>...</toggle> whose text holds marker
#   ("drop_section", subject, heading)             remove "## heading" up to the next "## " heading or the end
# apply_notion.py applies them in order and fails on any miss.

PAGES = {
    "rules-for-zoya": "3f719a301a7f81a09de3ee3ad6ad98a3",
    "cadences": "3ff19a301a7f8143aa95cd89bd6519ec",
    "follow-ups": "40b19a301a7f81999c1acd8350d59a54",
    "wording": "3fa19a301a7f81b6a807d0f01847dae7",
    "routines": "3fb19a301a7f813b949cf28cc0993541",
    "client-show-mails": "3fc19a301a7f817588e2d081af825f8a",
    "fu-1-sponsored": "3fa19a301a7f81b0a80dc0c75102b60e",
    "fu-2-precall": "3fa19a301a7f8197be92d74c8f8e0660",
    "fu-3-recording": "3fa19a301a7f814086fdd272fb6f6b86",
    "fu-6-release": "3fa19a301a7f814da20ae36f6aaee724",
    "fu-8-revival": "3fa19a301a7f81008e72f23ebc526327",
    "calendar-rules": "3fa19a301a7f816c9a53fe80557d0046",
}

RELEASE_TABLE = """<callout icon="📅" color="blue_bg">
<b>Release dates: what may be said, and when</b> (decisions 427, 514, 575, 582, 601, 628, 638). Controls.

Sarika sets Planned release on every show (decision 514). A Planned release nobody has confirmed is a draft.

| Show | Before Sarika or Akshay confirms the date | After they confirm it in Zoya <> Team |
| --- | --- | --- |
| Founder Thesis and FT Tier 3 Spotlight | On the post-recording thread, the tentative week only, in "Release date (post-recording)" (decision 575). A release-date ask gets "Next steps and release date". | FT Release v2 (decisions 601, 628): Mail 1 is Akshay's draft, Mails 2 to 6 Zoya's. |
| un# | No date. A release-date ask gets "Next steps and release date". | Release v3 (decision 638): Mail 1 is Akshay's draft, Mails 2 to 5 Zoya's, no WhatsApps. |
| Built to Share, Human by Design | No date. A release-date ask gets "Next steps and release date". | Release mail stays Akshay's own (the pre-release ask drafted for him) until Release v3 starts on that show, once its short link is confirmed. |
| Pathfinders | Pre-launch: no release mail until its pitch sheet's release lines are confirmed (decision 626). | Same |
</callout>"""

SPONSORED_TABLE = """## 5c. Sponsored offers and pauses: one table (decisions 227, 237, 367, 422, 573, 618, 625, 656)

<b>Controls.</b> Every sponsored chase on every show follows this table. Intervals are on Cadences.

| | Founder Thesis | un# |
| --- | --- | --- |
| The offer | podm.in/sponsored, no price in the first mail | unhashed.co/sponsored, no price in the first mail |
| Price, only when asked | INR 1,00,000 + GST (podm.in/why-sponsor) | USD 1,500 |
| Before any follow-up | They must show interest in the sponsored option: ask about fees, deliverables or timing, say they are considering it, or ask for details. Silent or noncommittal: no follow-up at all. | Same |
| Silent or noncommittal 7 days after the offer, no interest shown | No mail. The row goes on the weekly Park proposals for Akshay (decisions 618, 656) | No mail. Status Unresponsive (decisions 422, 618) |
| After interest | Answer what they asked from the wording page, then at most 2 follow-ups on the Cadences days | Same; a yes, a negotiation, terms or a call go to Akshay |
| What counts toward the 2 | Every chase already sent on the thread, by anyone (Zoya, ad@, the team). Loop-ins and answers to their questions don't. A template change, deploy or Chase step reset never adds more. | Same |
| Negotiation | Zoya holds the price, makes the value case, offers The Spotlight Podcast at INR 30,000 + GST, fully upfront. A custom package or a call goes to Akshay. | Akshay |
| Stop: their no | A decline, "not our client" or words to that effect: the close note (with the influencer line), Status They declined | Any hint of disinterest: one short thank-you, no counter-pitch, Status They declined |
| Stop: no reply after the last follow-up | Send nothing more. Status stays; the row goes on the weekly Park proposals for Akshay. No nurture. | Send nothing more, Status Unresponsive. No nurture, no revival, no last check |
| Parked | Only on Akshay's word (decision 656) | Same |

<b>Pauses on their word</b> (every routine, sponsored included):

| They say | We do |
| --- | --- |
| They'll reach out when ready ("as and when", "we'll get back", "will revert once") | Nothing for 30 days from that mail, then at most one short warm check-in on the primary thread, then nothing unless they write. The row goes on the Park proposals. (decision 625) |
| It seems difficult, or not the right time | "totally understand, hope it is ok if I check in after a couple of months", then one check-in 3 months out, Status LT chase (decision 550) |
| Waiting for internal approval | "any update on the approval? let me know a timeline and I will check in with you then", then their date (decision 551) |
| A date | That date wins over every schedule |

A pause covers every chase on that row, the Tier 1 recording chase included."""

LINKS = """- <b>Approved links</b> (decisions 168, 222, 230, 237, 306, 332, 445, 462, 497, 553, 576, 587, 640). Only these, each for its job, never copied from a calendar title or booking page:
  - podm.in/30min: a 30-minute planning call with Akshay (precalls, intros, rebooking any call with him), always named that way (decision 569).
  - podm.in/book: a 2-hour recording slot.
  - podm.in/sponsored: Founder Thesis sponsored features, the first sponsored link a lead sees. podm.in/why-sponsor: the sales page with the full data, for sponsored follow-ups and questions.
  - podm.in/guest-list: the founders Akshay has interviewed. podm.in/community: the FT Community directory. podm.in/note: our audience and distribution. podm.in/pitch-to-us: vendor pitches. podm.in/thank-you: the guest form after a recording.
  - Any other podm.in/... link (decision 576), except podm.in/founders (retired) and podm.in/ad, which is Akshay's LinkedIn profile and never a booking link.
  - youtube.com/@spotlight-pod: only in the negotiation reply and the sponsored-vs-Spotlight answer. youtube.com/@founderthesis: the "where it's published" answer. founderthesis.com: the show site and guests' written profiles.
  - Client shows, each only on its own show: unhashed.co/sponsored and unhashed.co/precall (un#); built2share.in/note (Built to Share); fscd.ai/note (Human by Design). Recording links, recordings only: unhashed.co/studio (every un# recording: the invite's location and body, no Meet, no Zencastr room), built2share.in/studio, fscd.ai/studio.
  - zencastr.app.link/<room> or zencastr.com/record/<room>: a Founder Thesis guest's room from Ranjita, only in that guest's recording-link mail and invite.
  - f.io/... or frame.io/... links the edit team shares for an episode's assets: only in that episode's release mails.
  A link not on this list waits for Akshay."""

EDITS = {}

EDITS["rules-for-zoya"] = [
    ("between", "S9-release",
     '<callout icon="⛔" color="red_bg">\n<b>HOLD on release dates',
     "dates go out the week of 2 Nov at the earliest.\n</callout>",
     RELEASE_TABLE),
    ("replace", "S4-ranjita",
     "- Mamatha is never in Cc, and nothing waits on her, on any show (decisions 260, 352).",
     "- Mamatha is on a long break (decision 646): she is never in To or Cc and nothing waits on her. Ranjita does her room and transcript work (section 5)."),
    ("between", "S5-senders",
     "- Zoya's mail goes through MCP Emails from her inbox. Akshay's automated mail goes through the Gmail connector",
     "or an attachment. Format either way:",
     "- Which mailbox, which action, which tool: the sender table in section 1. Format either way:"),
    ("replace", "S1-parking",
     "- <b>PR says they no longer represent the guest:</b> Tier 1, find a direct route; anyone else, Park with the reason (decision 366).",
     "- <b>PR says they no longer represent the guest:</b> Tier 1, find a direct route; anyone else, stop the chase and put the row on the Park proposals with the reason (decisions 366, 656)."),
    ("replace", "S2-sponsored",
     "- <b>Sponsored stops only on their no:</b> a decline, or \"not our client\" or words to that effect. An eval Decline or silence never stops it (decision 367).",
     "- <b>Sponsored:</b> the table in Rules for Zoya: follow-ups, section 5c. An eval Decline never stops a sponsored conversation; their no does (decision 367)."),
    ("between", "S4-ranjita",
     "- <b>Zencastr link and transcript from Mamatha</b> (decision 439",
     "\"Akshay: no Zencastr link yet for \\<guest> (\\<D Mon>)\" on his list.",
     "- <b>Zencastr rooms and transcripts are Ranjita's</b> (decisions 445, 558, 644, 646). Founder Thesis rooms: as soon as a row reaches Booking, Zoya WhatsApps Ranjita one message listing every Booking or Booked row without a room, soonest first, and puts \"Ranjita: create \\<guest>'s Zencastr room and send Zoya the link (recording \\<D Mon>)\" on each row with Ranjita in Waiting on. One reminder after 2 days. A recording under 48 hours away with no link: Akshay's list, once. Her link (mail, WhatsApp or the Zoya <> Team group) goes on the row and the recording invite, and Zoya sends the guest the recording-link mail. Transcripts: after each recording, \"Ranjita: download \\<guest>'s Zencastr transcript and attach it to the Episode's Transcript file\" with one WhatsApp to her; one chase after 2 days, then Akshay's list. un# uses unhashed.co/studio and has no room ask."),
    ("replace", "S1-parking",
     "  - We declined (33) and Parked (34): Akshay's call; agents never touch them.",
     "  - Parked: Akshay's call; agents never set it (decision 656). We declined: Akshay's call, or a client-show host's no on their board. A live ask on such a row reopens it to Decision pending for him (decision 621)."),
    ("replace", "S4-ranjita",
     "She's added the way Mamatha always was: \"thanks Sujeet, adding @Zoya to coordinate\" (decision 199).",
     "She's added the way a colleague is: \"thanks Sujeet, adding @Zoya to coordinate\" (decision 199)."),
    ("replace", "S4-ranjita",
     "Our side wrote last (a chase from Mamatha, say): just \"adding @Zoya to coordinate further\", no thanks.",
     "Our side wrote last (a chase from the team, say): just \"adding @Zoya to coordinate further\", no thanks."),
    ("between", "S5-senders",
     "The one other allowed send is the billing forward to Jaya (decision 423",
     "also through MCP Emails.",
     "Two forwards are also allowed: billing documents received in ad@ forwarded to Jaya (decision 423), and the Gemini notes mail forwarded to Saurabh Garg when he was on the call (decision 574), both through MCP Emails.\n\n<b>Sender table</b> (decisions 235, 420, 423, 435, 574, 658). Controls.\n\n| Mailbox | Who | Action | Tool | Approval |\n| --- | --- | --- | --- | --- |\n| Zoya's inbox | Zoya (the day chat sends; composers only draft) | Every routine mail, follow-up and reply | MCP Emails: a reply is draft reply, update, read back, send; a new mail is email_compose | The rules on this page |\n| ad@thepodium.in | Routines and the day chat | Read only, never marked read | MCP Emails | None |\n| ad@thepodium.in | The day chat | The loop-in reply | MCP Emails email_compose reply, To and Cc passed explicitly; never the MCP Emails draft tool on ad@ | Standing |\n| ad@thepodium.in | The day chat | Billing forward to Jaya; Gemini notes forward to Saurabh | MCP Emails forward | Standing |\n| ad@thepodium.in | The day chat and chat sessions | Drafts of Akshay's own mail (release Mail 1, thank-you, day-before notes on client shows) for him to send | Gmail connector create_draft | He sends by hand |\n| ad@thepodium.in | CTO and other chat sessions | Mail Akshay approved in chat | Gmail connector reply, links written as plain text with the first dot broken | Akshay, per mail |\n\nNothing else goes from ad@thepodium.in."),
    ("between", "S9-release",
     "| Release mail 1 (the full ask) and the patron ask 7 days after release |",
     "| Release mails 2 to 4 | Zoya | Routine 6 |",
     "| Release mail 1 (Founder Thesis) | Akshay: drafted in his Gmail for him to send (decision 589) | A new mail that starts the release thread |\n| Release mails 2 to 6, the patron ask | Zoya, on the release thread | FT Release v2 on the wording page |"),
    ("replace", "C-privacy",
     "## 6. WhatsApp\n",
     "## 6. WhatsApp\n\n- <b>Group chat ids</b> (Blueticks): Zoya <> Team {ZOYA_TEAM_GROUP_ID}; The Founder Thesis Community {FT_COMMUNITY_GROUP_ID}. Kept here, not in the repo.\n"),
    ("replace", "S4-ranjita",
     "- <b>Agents send only to Akshay's own chat, the Zoya group, Jaya and Sarika.</b>",
     "- <b>Agents send only to Akshay's own chat, the Zoya group, the Zoya <> Team group, Jaya, Sarika and Ranjita.</b>"),
]

EDITS["rules-for-zoya"] += [
    ("replace", "S8-templates",
     "Every mail's text, one toggle per mail, with its owner. It replaces the Templates database, which is deleted at go-live.",
     "Every mail's text, one toggle per mail, with its owner."),
]

EDITS["rules-for-zoya"] += [
    ("between", "S0-links",
     "- Only the approved short links:",
     "is the fixed Built to Share recording link: recordings only, never a precall (Akshay, 21 Oct). Anything else waits for Akshay.",
     LINKS),
]

EDITS["rules-for-zoya"] += [
    ("between", "S15-history",
     "## System-audit corrections, 25 Oct 2026",
     "Zoya is live (since 2026-10-16 00:20 JST).",
     "## Standing checks\n\n- <b>Reach claims.</b> A figure that combines Akshay's and Unnati's channels says \"we have\" and names the channels and the dated source; never call it Founder Thesis's own following.\n- <b>Threading.</b> A follow-up replies on the original conversation, found by its RFC Message-ID, In-Reply-To and References across ad@ and Zoya's inbox; a matching subject or a typed Re: is not a reply. If Zoya is not on it, the ad@ loop-in adds her on that chain first. If the headers or the source can't be recovered, record a blocker on the row; never start a replacement thread.\n- <b>One company per conversation.</b> A shared PR contact never lets two companies share one mail (Rules for Zoya: follow-ups, 5a).\n- <b>Addresses.</b> Keep ad@thepodium.in in Cc and drop Akshay's other alias (never both); never remove anyone else's address by a name match.\n- <b>Team deliverables.</b> Check incoming mail and work WhatsApp before chasing a team member; 24 hours after the ask, one WhatsApp nudge in team hours replaces that cycle's mail chase (SLOW work, INTERNAL TASKS b).\n- <b>Verified completion closes only its own obligation.</b> A group join removes the add or invite ask (and Akshay from Waiting on only if nothing else of his is left); it never proves a list, an intro or another promise was sent.\n\nZoya is live (since 2026-10-16 00:20 JST)."),
    ("between", "S10-holding",
     "- <b>Holding reply when a PR person chases a row waiting",
     "Akshay's list item stays as it is.",
     "- <b>Holding reply when someone chases a row waiting on Akshay</b> (decisions 390, 418, 571). Zoya replies on that thread the same day with only \"hi \\<first name>, will get back to you on this\": never Akshay's name, never a date. At most one holding reply per thread per 7 days; it is a reply, not a chase, so the 7-day limit doesn't hold it. A question the wording page answers gets that answer instead (decision 585). Akshay's list item stays as it is."),
    ("between", "S4-ranjita",
     "<b>Internal ad-hoc tasks (decision 376, Akshay, 21 Oct).</b>",
     "goes to Akshay's list.",
     "<b>Asks of the team</b> (decisions 376, 385, 592, 646). A step for a team member about a guest is a \"<name>: <step>\" segment on that guest's Engagement with the person in Waiting on; only work with no guest row is a Kind Task row (Show Internal). Zoya asks on WhatsApp (team hours) or by mail with no Akshay in To or Cc, and chases every 2 working days (Ranjita: once, after 2 days). A date they give wins. A reply that it can't be done goes to Akshay's list."),
    ("between", "S4-ranjita",
     "<b>Transcript requests while Zencastr blocks standalone",
     "Stops when Akshay says Zencastr downloads work again.",
     "<b>Transcripts</b> are Ranjita's (section 5: Zencastr rooms and transcripts)."),
    ("replace", "S4-ranjita",
     "Only the team (Ranjita, Sarika, Jaya, Mamatha, Chaandini).",
     "Only the team (Ranjita, Sarika, Jaya, Chaandini)."),
    ("replace", "S15-history",
     "## More rules (decisions 373 to 382)",
     "## Guest-facing mail, team asks and replies"),
    ("between", "S15-history",
     "Sections 9 and 10 (one-time plans and go-live history)",
     "Akshay's open items live in his Engagements queue.",
     "Akshay's open items live in his Engagements queue."),
]

EDITS["rules-for-zoya"] += [
    ("between", "S3-recipients",
     "- Zoya is in Cc on every mail from",
     "- Every stakeholder on the thread stays on it: PR, company comms, EA, intern, co-founder. A new mail copies everyone who was on the original (decision 144).",
     "- <b>Recipients</b> (decisions 144, 180, 188, 227, 229, 305, 586, 592, 643, 646, 647). Controls; every send and draft from either inbox follows it, and the prompts check it in code before every send.\n  1. Reply on a thread with anyone outside the team: everyone on its latest message (From, To, Cc), less only Zoya's own address, anyone who handed over (8), People tagged \"Email bounced\", People whose Role starts \"Ex-employee (mailbox dead)\", Akshay's addresses other than ad@thepodium.in, and Mamatha (on a long break). Everyone else stays, whether or not they wrote: team members, Sri, client-show hosts, PR, comms, EAs.\n  2. Then add whoever is missing of: Akshay (ad@thepodium.in) in Cc; Zoya in Cc on mail from ad@thepodium.in; Chaandini on Built to Share and Human by Design; Divir and Ankita Joshi on Pathfinders; Jaya and Sarika on revenue mail (sponsored from their yes on: next steps, billing, invoices, payments; never expenses); the guest or a company-side contact on guest-facing mail (day-before note, prep note, recording link, reschedule, thank-you).\n  3. A new mail to someone outside the team: their side from the row and the step, plus the same additions; a new thread someone outside the team starts with Zoya gets Akshay in Cc.\n  4. Team-only mail: the team members only, never Akshay (decision 592), never Mamatha.\n  5. Never added on our own: Sri or a host to a thread they are not on, Mamatha, Saurabh Garg (except decision 517 below).\n  6. To is whoever's move it is, everyone else Cc; ad@thepodium.in is never in To; no team address is in To on outside mail.\n  7. The ad@thepodium.in loop-in: ad@ is the sender, so it is never in To or Cc. To the person whose move it is; Cc everyone else on the message it replies on, less the removals in 1, plus Zoya. Nothing else is added.\n  8. Someone who handed over on the thread (a message saying a new contact takes over) is removed, and the new contact takes their place."),
]

EDITS["rules-for-zoya"] += [
    ("between", "C6-senders",
     " Nothing else goes from his account: no acknowledgements, close notes, decision mails or follow-ups.",
     "Signed \"Regards, Akshay\".",
     " What Zoya can send goes from her inbox once she's on the thread; anything only Akshay can send goes on his list, drafted in his Gmail when it carries a link (the thank-you without the transcript: decisions 300, 308, 412). The no-show note is Zoya's (decision 236). Agents read ad@thepodium.in through MCP Emails and never mark it read. Akshay's own mails are signed \"Regards, Akshay\"."),
]

EDITS["cadences"] = [
    ("replace", "S2-sponsored",
     "| Sponsored offer (Founder Thesis) | 7 days after the offer | 2 follow-ups: days 7 and 14, then Parked, no nurture (decision 573, 13 Nov). More only if they ask for details or fees. Silent for 60 days: moves to nurture | A no, \"not our client\" (decision 367), or a yes. Below INR 30k goes to you |",
     "| Sponsored offer (Founder Thesis) | Only after they show interest (Rules for Zoya: follow-ups, 5c) | At most 2 follow-ups: days 7 and 14, counting every chase already sent on the thread. None while they are silent. No nurture | A no, \"not our client\" or a yes. After the second with no reply: Park proposals for you. Below INR 30k goes to you |"),
    ("between", "S2-sponsored",
     "| Sponsored offer (un#) | 7 days after the offer |",
     "Closing ends this sponsored pursuit only, never the person or their other rows |",
     "| Sponsored offer (un#) | Only after they show interest (Rules for Zoya: follow-ups, 5c) | At most 2 follow-ups: days 7 and 21, counting every chase already sent on the thread by anyone. No nurture, no revival, no last check (decision 422) | Any hint they're not interested: one short thank-you, then stop. A yes, a negotiation or terms go to you. After the second with no reply: Unresponsive. Closing ends this sponsored pursuit only |"),
    ("drop_section", "S6-sweep", "Historical system timings, pending scheduler reconciliation"),
    ("replace", "S6-sweep",
     "How often Zoya contacts anyone, in one place. Comment on any row (select the text, then Comment) and the CTO applies it. Live behaviour as of 20 Oct 2026. The CTO maintains this page. From Fri 23 Oct it becomes the master copy that Zoya reads; until then it mirrors her live rules.",
     "How often Zoya contacts anyone, in one place: contact intervals and limits only. When each worker runs is on Routines. Comment on any row (select the text, then Comment) and the CTO applies it."),
]

EDITS["follow-ups"] = [
    ("replace", "C8-nurture", "a no-contact request from that person, anywhere (\"## Standing\", Claude note, Your call or the thread; Status Parked).", "a no-contact request from that person, anywhere (\"## Standing\", Claude note, Your call or the thread; Status They declined with the no-contact note)."),
    ("replace", "S6-sweep",
     "Zoya's SLOW work (the 10:38 and 16:38 weekday runs) reads this page every run, with the same authority as the parent page.",
     "Zoya SLOW reads this page every run, with the same authority as the parent page."),
    ("replace", "S2-sponsored",
     "See Cadences. Silent leads move to nurture (section 5a)",
     "Section 5c: interest first, at most 2 follow-ups, no nurture"),
    ("replace", "S2-sponsored",
     "A decline stops it. \"Give us time\" doesn't. Silent past the limit on Cadences: nurture (section 5a), never Unresponsive. No fresh restart of old offers (decision 230)",
     "Section 5c. No fresh restart of old offers (decision 230)"),
    ("replace", "S2-sponsored",
     "| The routine has run out (last step, span over, a sponsored offer silent past the limit on Cadences, our last mail a close-out, or 3 unanswered chases) |",
     "| The routine has run out (last step, span over, our last mail a close-out, or 3 unanswered chases; never a sponsored offer, which follows 5c) |"),
    ("replace", "S1-parking",
     "- <b>Start:</b> the daily sweep starts nurture on each marked row (daily limit on Cadences).",
     "- <b>Start:</b> Zoya SLOW starts nurture on each marked row (daily limit on Cadences)."),
    ("replace", "S2-sponsored",
     "<b>Approved pursuit:</b> a row at Precall requested, Sponsored offered, Booking or LT chase, or with Tier 1, or one Akshay asked to nurture.",
     "<b>Approved pursuit:</b> a row at Precall requested, Booking or LT chase, or with Tier 1, or one Akshay asked to nurture. A sponsored offer is never a nurture pursuit (5c)."),
    ("between", "S9-release",
     "<b>Release week (decisions 580, 582). Controls.</b>",
     "No post-recording thread: report it, send nothing.",
     "<b>Release mail</b> follows the release-date table on Rules for Zoya and the release workflow in the Zoya day instructions."),
    ("between", "S2-sponsored",
     "## The nine routine pages",
     "## The nine routine pages",
     SPONSORED_TABLE + "\n\n## The nine routine pages"),
]

EDITS["wording"] = [
    ("replace_all", "S9-release", "PROPOSED: Release v3", "Release v3"),
    ("replace_all", "S9-release", "<b>Status:</b> PROPOSED", "<b>Status:</b> approved (decisions 601, 638)"),
    ("replace", "S9-release", " \\[approved 19 Nov, with \"we\" for Zoya\\]", ""),
    ("replace", "S9-release", " \\[approved 19 Nov, 3/ reworded\\]", ""),
    ("replace", "S9-release", "Mail 2: confirmed (day before) \\[approved 19 Nov\\]", "Mail 2: confirmed (day before)"),
    ("between", "S9-release",
     "<b>Status: LIVE for un# from 20 Nov (decision 638",
     "Until he approves them, Founder Thesis keeps FT Release v2 and the client shows keep their current release mails.",
     "<b>Status:</b> live on un# (decision 638): Mails 1 to 5, no WhatsApps. Founder Thesis runs FT Release v2, which this set matches word for word. Built to Share, Human by Design and Pathfinders start once their short links are confirmed; until then they keep the pre-release ask and the release-day mails below."),
    ("drop_toggles", "S9-release", "un# Episode Planned release is 7 days away or less and no pre-release mail yet"),
    ("drop_toggles", "C7-release", "Release v3, WhatsApps (from Akshay's WhatsApp, unsigned)"),
    ("replace", "S8-templates", "## Retired: do not send\n\nKept only so nobody rewrites them by accident. Each is replaced by the routine named.\n\n", ""),
    ("drop_toggles", "S8-templates", "<b>Status:</b> retired"),
    ("drop_toggles", "S8-templates", "Kept for reference; do not send."),
    ("between", "S8-templates",
     " The inbox and calendar routines still read the Templates database",
     "(Rules for Zoya, section 10).",
     ""),
    ("drop_toggles", "S6-sweep", "Mamatha's daily list"),
    ("replace", "S8-templates",
     "This page replaces the Templates database.",
     "Agents take every mail and WhatsApp wording from this page; the Templates database is retired."),
]

EDITS["routines"] = [
    ("between", "S6-sweep",
     "## 25 Oct audit: runtime ownership and deployment status",
     "| Community sync | Member cities, public directory mirror | Sat 09:47 | Nothing |",
     "## Runtime inventory\n\n<b>Describes.</b> Who runs what, when, and from which source. The CTO updates this table in the same release as any schedule or prompt change, and reads each scheduled task back before marking it live. Cadences owns how often people are contacted.\n\n| Worker | Job | When (JST) | Reads | Model | Sends |\n| --- | --- | --- | --- | --- | --- |\n| Zoya day chat | Runs inbox actions, Zoya FAST, WhatsApp and calendar, and the OUTBOX | Weekdays every 2 hours 07:38 to 23:38; weekends 08:38, 12:38, 16:38, 20:38 | routines/zoya-day.md, the release prompts, Rules for Zoya and its subpages, Cadences, Client show mails | as its seed sets | Every mail, WhatsApp and invite |\n| Capture composer | Logs mail (inbox capture) | Start of every wake | composer seed, inbox-capture.txt | claude-sonnet-5-5 | Nothing |\n| SLOW composer | Follow-ups, nurture, team work, payments | Weekdays 11:08 and 17:08 | composer seed, zoya-slow.txt and its work file | claude-opus-5-5 | Nothing: drafts only |\n| Engagement chats | Evals, dossiers, blurbs for one guest | When the day chat sends a step | docs/engagement-chat-seed.md, the show's skills | claude-opus-5-5 | Nothing |\n| Blurb chats | One community blurb | On request | docs/blurb-chat-seed.md, skills/ft-community-blurb | as started | Nothing |\n| Upkeep (in the day chat) | The retired sweep's live steps: client pre-release drafts, guests list, community backstop, BD episodes, flags, billing forwards to Jaya, guest forms | Weekdays, first wake at or after 13:00 | upkeep.txt | the day chat's | Nothing (drafts and one allowed ad@ forward) |\n| Host boards | Keeps the un#, Built to Share and Human by Design host boards in step with Engagements | 08:15, 12:15, 16:15, 20:15 daily | its stored prompt (routines/host-boards.md) | claude-sonnet-5-5 | Nothing |\n| Sarika's editing asks | Sarika's asks on Episodes, hand-made task allocations, editing docs | Mon to Sat 11:17, 12:17, 13:15, 15:47, 18:17, 22:47 IST (three scheduled tasks, one session) | its stored prompt (routines/editing-checks.txt) | as its session | Team allocation mail and Zoya calendar blocks |\n| FT Community directory sync | Member cities and the public directory mirror | Saturdays 09:47 | its stored prompt (routines/community-directory.md) | claude-sonnet-5-5 | Nothing |\n| Zoya day monitor | Watches the day chat for stalls and tells Akshay | Weekdays hourly at :55; weekends 08:55, 12:55, 16:55, 20:55 | its own session | claude-sonnet-5-5 | Alerts only |\n| CTO coordination round | Checks every run by outcome, relays work to builders, handles blocked cancel deletes | 08:45 and 20:45 daily | its stored prompt (routines/cto-round.txt) | as its session | Nothing routine |\n| Codex review | Independent audit, CTO Audit page, summary mail from Zoya to Akshay | Daily 08:00 | Codex's own task | n/a | One summary mail |\n| Monday scorecard | Zoya's weekly scorecard for Akshay | Mondays, in the 11:08 SLOW run (STEP 0g) | SLOW work file | as SLOW | One mail to Akshay |\n| On Akshay's Mac | Zencastr transcripts | His schedule | routines/mac | n/a | Nothing |\n\nNo longer scheduled: the daily sweep (657), the standing evals session and the dossier schedule (593), and the old separate Zoya, inbox, calendar and WhatsApp tasks (the day chat runs them, 568); none is in the enabled list."),
]

EDITS["client-show-mails"] = [
    ("replace", "S9-release",
     "<b>Status:</b> approved 17 Oct. Replaces the separate buy-in mail and kit mail.",
     "<b>Status:</b> approved 17 Oct, for Built to Share and Human by Design until Release v3 starts there. Not for un#: un# runs Release v3 (decision 638)."),
    ("between", "S9-release",
     "C16 Episode is live\n\n<b>From:</b> Zoya (Akshay in Cc), on release day. <b>Status:</b> approved 17 Oct",
     "C16 Episode is live\n\n<b>From:</b> Zoya (Akshay in Cc), on release day. <b>Status:</b> approved 17 Oct",
     "C16 Episode is live\n\n<b>From:</b> Zoya (Akshay in Cc), on release day. <b>Status:</b> approved 17 Oct, for Built to Share and Human by Design until Release v3 starts there; not for un# (decision 638)"),
    ("between", "S9-release",
     "C17 After release: company pages\n\n<b>From:</b> Zoya (Akshay in Cc), 2 working days after release. <b>Status:</b> approved 17 Oct",
     "C17 After release: company pages\n\n<b>From:</b> Zoya (Akshay in Cc), 2 working days after release. <b>Status:</b> approved 17 Oct",
     "C17 After release: company pages\n\n<b>From:</b> Zoya (Akshay in Cc), 2 working days after release. <b>Status:</b> approved 17 Oct, for Built to Share and Human by Design until Release v3 starts there; not for un# (decision 638)"),
]

FU1_PAGE = """<b>Status: live.</b> Owner: Zoya, from her inbox, in SLOW runs. Who, when and how many: the sponsored table, Rules for Zoya: follow-ups section 5c, and Cadences. In short: no follow-up unless their side shows interest in the sponsored option; then at most 2 follow-ups, counting every chase already sent on the thread; no nurture, no revival; only Akshay parks (decision 656).

<b>Plain English</b> (decision 392): many readers use English as a second language. Say "a sponsored appearance on the pod", never "sponsored feature", "sponsored route" or idioms like "circling back".

## Who gets it

Every open Founder Thesis Engagement at Sponsored offered, and un# rows with our sponsored offer on the thread (decision 307). On un# the facts and the link come from the un# pitch sheet (unhashed.co/sponsored only), the price (USD 1,500) is stated only when asked, and a yes, a negotiation or terms go to Akshay. Founder Thesis numbers, peers and links never go into a un# mail.

## What each reply gets

- <b>A price question:</b> the commercials, fee and ROI only (decision 197). <b>What's included:</b> 2 or 3 lines from podm.in/why-sponsor "What you get" plus the link (decision 549).
- <b>A yes at the standard price:</b> "Sponsored yes: next steps", Jaya and Sarika in Cc (decision 227).
- <b>A lower-price ask (Founder Thesis):</b> "Price negotiation": the price holds and Zoya offers The Spotlight Podcast at INR 30,000 + GST, fully payable upfront (decisions 237, 464). A counter-offer below that, any other term, a custom package or a call goes to Akshay.
- <b>A no, "not interested" or "not our client" (decision 367):</b> the close note on Founder Thesis (decision 145), one short thank-you on un# (decision 397); Status They declined. On "not our client", a Tier 1 row goes direct (decision 366). Routine 8 may later write to a founder who wrote to us directly and whose no was to the price (decision 355).
- <b>They'll come back, it's not the right time, or approval pending:</b> the pause table in section 5c.

## How every mail is written

- On the original thread, from Zoya, recipients as Rules for Zoya section 2 says. Signed "best," / "Zoya ✨".
- The mails below, adapted up to about 40% to fit the thread (decision 152), never a fact, price, link or the ask. No stats block, no price, no mail built on the lead's company details.
- <b>LinkedIn numbers</b> (decision 395): our following is Akshay's profile plus the company pages combined, never "Founder Thesis has". First person plural and rounded: "50k+ director level and above folks follow us on LinkedIn". Never the seniority breakdown or exact counts.
- <b>Links</b> (decision 218): at most one per mail: podm.in/sponsored in mail 1, podm.in/why-sponsor for questions.
- The next planned mail sits at the top of each Engagement page under "Next sponsored mail". Edit it there and Zoya sends your version.

## The mails

Things in \\{braces\\} are filled per lead.

### Mail 1

> Hi \\{PR\\},

>

> Has \\{guest\\} had a chance to look at our offer of a sponsored appearance on the pod? The details are here: [podm.in/sponsored](https://podm.in/sponsored)

>

> best,

> Zoya ✨

### Mail 2

> Hey \\{PR\\},

>

> Just following up - would \\{guest\\} like to come on the Founder Thesis podcast as a sponsored guest? Guest profiles on [founderthesis.com](http://founderthesis.com) got 860k+ impressions from Google search alone in the last 3 months.

>

> best,

> Zoya ✨

The impressions figure (decision 620) is the last 3 months of Google Search Console (Web), rounded down; Akshay refreshes it. Use it only as written here.
"""

FU6_PAGE = """<b>Status: live.</b> Owner: Zoya, with Mail 1 and the release WhatsApps from Akshay. What may be said when: the release-date table on Rules for Zoya. Who sends each step and when: the release duty in the Zoya day instructions. Every mail word for word: "FT Release v2" (Founder Thesis and Spotlight) and "Release v3" (un#) on Mail and WhatsApp wording. Built to Share, Human by Design and Pathfinders keep the pre-release ask drafted for Akshay (Client show mails C15 to C17) until Release v3 starts on that show.

Patron ask (Mail 6, Founder Thesis only) is skipped for sponsored guests, existing patrons, anyone who said no to the patron line, and any open complaint.
"""

EDITS["fu-1-sponsored"] = [("whole", "S2-sponsored", FU1_PAGE)]
EDITS["fu-6-release"] = [("whole", "S9-release", FU6_PAGE)]
EDITS["fu-2-precall"] = [
    ("replace_all", "S1-parking", "If they say no: Tier 1 goes direct, anyone else is Parked (decision 366).",
     "If they say no: Tier 1 goes direct; anyone else stops and goes on the Park proposals (decisions 366, 656)."),
]
EDITS["fu-3-recording"] = [
    ("between", "S2-sponsored",
     "<callout icon=\"🛑\">",
     "## Who gets it",
     "<b>Status: live.</b> Owner: Zoya, in SLOW runs, To the person whose move it is, recipients as Rules for Zoya section 2 says. Rows due are Waiting on Zoya with Next action \"Zoya: recording step \\<n> on \\<D Mon>\". On Founder Thesis only Tier 1 rows are chased, and a Sponsored row only after their yes to the sponsored appearance (decisions 594, 618). No Founder Thesis slot ask before a precall with Akshay has happened, unless he said in writing to skip it (decision 654). Silence never makes a row Unresponsive.\n\n## Who gets it"),
    ("between", "S2-sponsored",
     "<b>Since 17 Nov (decision 594",
     "Precall follow-ups (routine 2) are unchanged.",
     "Tier 1.5, Tier 2 and untiered Founder Thesis rows get no slot follow-up: Status stays Booking, Waiting on Guest or PR, and they book through podm.in/book when ready."),
]
EDITS["fu-8-revival"] = [
    ("replace", "S2-sponsored",
     "PR-routed leads get routine 1, then nurture while silent (Rules for Zoya section 5a). After a no, nothing.",
     "PR-routed leads get routine 1 only (section 5c: no nurture). After a no, nothing."),
]
EDITS["calendar-rules"] = [
    ("between", "S4-ranjita",
     "<b>Decision 433 (Akshay, 30 Oct).</b> Every recording invite on a Zencastr show",
     "<b>2 days out, still no link:</b> your list.",
     "<b>Zencastr rooms</b> (decisions 433, 445, 558, 646). Every Founder Thesis recording invite carries its Zencastr room link before the recording. Zoya asks Ranjita on WhatsApp as soon as the row reaches Booking (\"Ranjita: create \\<guest>'s Zencastr room and send Zoya the link\" on the row, Ranjita in Waiting on), reminds her once after 2 days, and adds the link to the invite's location and first description line when it arrives, guests notified, nothing else changed. Under 48 hours out with no link: your list. Transcripts: Ranjita downloads and attaches each one to the Episode (decision 646). un#, Built to Share and Human by Design use their fixed studio links and need no room."),
    ("replace", "S0-retired",
     "The evals routine then re-runs the eval and puts your final call on your list (decision 172)",
     "The guest's engagement chat then re-runs the eval and your final call goes on your list (decisions 172, 593)"),
    ("between", "S4-ranjita",
     "<b>Zencastr links (decision 433, owner changed by decision 439 on 1 Nov).</b>",
     "need no new link.",
     "<b>Zencastr rooms:</b> Ranjita creates them when Zoya asks, as soon as the row reaches Booking, and attaches transcripts to the Episode (decisions 558, 646). The calendar run puts the link on the invite. Shows with a fixed studio link (unhashed.co/studio, built2share.in/studio, fscd.ai/studio) need no room."),
    ("between", "S15-history",
     "## 3. Today's audit (15 Oct, next 30 days)",
     "Zoya\n</callout>\n",
     ""),
]

# Toggles and headings that must survive every run (apply_notion asserts them).
MUST_KEEP = {
    "wording": ["Recording link", "Release date (post-recording)", "FT Release v2, Mail 1", "Release v3, Mail 1",
                "Next steps and release date", "Sponsored: no organic slot (via PR)", "Feature interest: book the call with Akshay"],
    "rules-for-zoya": ["## 1. Who sends what", "## 2. Rules for every mail", "Sender table", "<b>Recipients</b>"],
    "follow-ups": ["## 5c. Sponsored offers and pauses", "## 5a. Nurture and revival"],
}

# ---------------------------------------------------------------------------
# Batch 4: Rules index child pages and Inbox and Your call rules
# ---------------------------------------------------------------------------
PAGES.update({
    "inbox-your-call": "3ff19a301a7f8148993ccea78fc66428",
    "rules-inbox": "3fb19a301a7f818ca72ff4c8fcaf3dce",
    "rules-notion-list": "3fb19a301a7f81dda506eae542190b59",
    "data-rules": "3fb19a301a7f8101a6aaf3f557b7a240",
    "links-limits": "3fb19a301a7f81248dfec97a4569bd48",
    "blurb-sources": "3fc19a301a7f81eb9bcfc36f3a1cd6a9",
})

EDITS["inbox-your-call"] = [
    ("replace", "B4-history",
     "<b>Controls</b> (agents read this every run). AR-20261020-1, deployed 20 Oct 2026. Source: docs/proposals/[ar20261020-1-inbox-controls.md](http://ar20261020-1-inbox-controls.md).",
     "<b>Controls</b> (agents read this every run)."),
    ("replace", "B4-zoya-date",
     "Next date = the earliest date still open on the row, not counting held steps, so another segment due sooner keeps its date.",
     "Zoya date = the earliest open Zoya segment date (the snooze's included), not counting held steps; Next date only from people's steps (decision 637)."),
    ("between", "B4-cancel",
     "If they ask us to cancel the invite, or say the guest can't make it (decision 165), first cancel",
     "cancel nothing and put it in bucket C.",
     "If they ask us to cancel the invite, or say the guest can't make it (decision 165): never call delete_event on it (decision 609). Match the one event for that guest on the date they name (the guest's name in the title, or an attendee from the thread), put \"Akshay: delete the \\<D Mon> \\<precall|recording> invite for \\<guest> (blocked: auto mode)\" on the row, and the CTO round deletes it (decision 488); if two events could match, or the mail is unclear, put it in bucket C."),
    ("replace", "B4-final-cut",
     "(seeing the cut or final episode, or any reel, collab or tag ask, is bucket C, decision 208)",
     "(a reel, collab or tag ask is bucket C, decision 208; seeing the cut or final episode gets \"Asks to see the video before release\" from Zoya, bucket C only for a guest who covered our cost, decision 600)"),
    ("replace", "B4-history",
     "Team messages keep Zoya's signature. The 15 Oct \"never pose as Akshay\" rule stands for them; decision 486 replaces it only for these guest chasers.",
     "Guest chasers go from Akshay's WhatsApp as him, unsigned, only after his tick (decision 486). Team messages are Zoya's, opening \"Zoya ✨\", and never pose as Akshay."),
]

EDITS["rules-for-zoya"] += [
    ("replace", "C5-opener", "opening \"hi \\<name>, zoya here.\" (decision 226)", "opening \"Zoya ✨\" (decision 226)"),
]

RULES_INBOX_PAGE = """<callout icon="📖" color="gray_bg">
<b>Describes</b> what happens to mail that reaches ad@thepodium.in. It controls nothing: the rules are in the inbox capture and inbox actions prompts, Rules for Zoya and Inbox and Your call rules.
</callout>

## The short version

- <b>Every mail is logged</b> as an Activity on the right person and Engagement. Personal mail is skipped. Nothing is ever marked read: you do that.
- <b>A new pitch gets one line from your account</b>, only when Zoya isn't on it yet: "thanks \\<name>, adding @Zoya to coordinate". Nothing else ever goes from ad@ except two forwards: billing to Jaya and Gemini notes to Saurabh.
- <b>Zoya answers everything she can</b> from her own inbox, with you in Cc: acknowledgements, routine replies, standard answers from the wording page, your decision once you make it.
- <b>Your list gets only what needs you</b>: a decision, a negotiation below the fixed price, a custom package, a call, an upset guest, press, a partnership, anything new. Zoya sends a one-line holding reply on the thread.
- <b>Your call</b> is how you answer. Write in it on the row; the next run acts on it, clears it and takes you off.
"""

LINKS_LIMITS_PAGE = """<callout icon="📖" color="gray_bg">
<b>Describes.</b> Nothing here controls a routine.
</callout>

- <b>Approved links:</b> the list in Rules for Zoya, section 2. A link not on it isn't sent until you approve it.
- <b>Limits</b> (daily cap, per-run cap, per-person gap, sending days, quiet hours, pauses): Cadences.
- <b>Writing style:</b> Rules for Zoya, Voice, and the Writing rules in CLAUDE.md.
"""

EDITS["rules-inbox"] = [("whole", "B4-describes", RULES_INBOX_PAGE)]
EDITS["links-limits"] = [("whole", "B4-describes", LINKS_LIMITS_PAGE)]

EDITS["rules-notion-list"] = [
    ("replace", "B4-describes",
     "- A Founder Thesis thank-you to send (decision 300): drafted in your Gmail; attach the transcript and send. The next calendar run sees it in Sent and moves the row on.",
     "- A Founder Thesis thank-you to send (decisions 300, 615): drafted in your Gmail, subject \"Gratitude! | ...\". The next calendar run sees it in Sent and moves the row on."),
    ("replace", "B4-describes",
     "- Three unanswered chases. The routine closes the row or moves it to the long-term chase.",
     "- Three unanswered chases. The row moves to the long-term chase (nurture), or onto the weekly Park proposals for sponsored offers; only you park a row (decision 656)."),
    ("replace", "B4-describes",
     "- Approvals are kept few: research first, write once; more than 10 rows go as one Notion AI upload (decision 91).",
     "- Approvals are kept few: research first, write once, in as few calls as possible (decisions 91, 341)."),
    ("replace", "B4-describes",
     "- To shelve a row without an instruction, set Status to Parked: it leaves your list at once and nobody follows it up.",
     "- To shelve a row without an instruction, set Status to Parked: it leaves your list at once and nobody follows it up. Only you park; rows a rule would park come to you once a week as Park proposals (decision 656)."),
]

EDITS["data-rules"] = [
    ("replace", "B4-history",
     " This owner instruction supersedes the no-show exception for Tasks in decision 329.",
     ""),
    ("replace", "B4-describes",
     "- Agents can't delete Notion rows: dedupe flags rows and a person deletes. Merging or deleting people needs your OK.",
     "- Agents move duplicate, test or asked-for rows to Trash themselves, after checking no relation is left, and report it (decision 416). Merging people or deleting a whole database needs your OK."),
]

EDITS["blurb-sources"] = [
    ("between", "B4-blurbs",
     "## Ownership override, 25 Oct 2026: Codex writes, Claude maintains records",
     "## Read before writing",
     "<b>Who writes blurbs</b> (decisions 524, 652, Akshay, 22 Nov). One blurb chat per guest writes the blurb with skills/ft-community-blurb, from the sources below, and hands DRAFT, SOURCES and NOTES FOR AKSHAY to the CTO, who checks every source before it reaches the page. A new blurb goes into the FT Community Blurb field and its section on Warm Welcomes only when Akshay asks or approves. Chats never write to Notion or send anything.\n\n## Read before writing"),
    ("replace", "B4-blurbs",
     "Write nothing, and put the gap on the Engagement: a Task row \"Blurb blocked: \\<guest>'s \\<D Mon> recording transcript not found (\\<where you looked>)\", Kind Task, Waiting on Builder.",
     "Write nothing, and put the gap on the Engagement as a segment, \"Ranjita: attach \\<guest>'s \\<D Mon> recording transcript to the Episode (blurb blocked; looked in \\<where>)\", with Ranjita in Waiting on (decisions 385, 646, 655)."),
]

MUST_KEEP["inbox-your-call"] = ["## 3. Your call snoozes", "## 6. Your call", "WHATSAPP CHASE"]
MUST_KEEP["blurb-sources"] = ["## Read before writing", "## Gaps", "## Writing and storing"]
