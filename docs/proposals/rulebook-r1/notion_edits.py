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
}

RELEASE_TABLE = """<callout icon="📅" color="blue_bg">
<b>Release dates: what may be said, and when</b> (decisions 427, 514, 575, 582, 601, 628, 638). Controls.

Sarika sets Planned release on every show (decision 514). A Planned release nobody has confirmed is a draft.

| Show | Before Sarika or Akshay confirms the date | After they confirm it in Zoya <> Team |
| --- | --- | --- |
| Founder Thesis and FT Tier 3 Spotlight | On the post-recording thread, the tentative week only, in "Release date (post-recording)" (decision 575). A release-date ask gets "Next steps and release date". | FT Release v2 (decisions 601, 628): Mail 1 is Akshay's draft, Mails 2 to 6 Zoya's. |
| un# | No date. A release-date ask gets "Next steps and release date". | Release v3 (decision 638): Mail 1 is Akshay's draft, Mails 2 to 5 Zoya's, no WhatsApps. |
| Built to Share, Human by Design, Pathfinders | No date. A release-date ask gets "Next steps and release date". | Release mail stays Akshay's own (the pre-release ask drafted for him) until Release v3 starts on that show, once its short link is confirmed. |
</callout>"""

SPONSORED_TABLE = """## 5c. Sponsored offers and pauses: one table (decisions 227, 237, 367, 422, 573, 618, 625, 656)

<b>Controls.</b> Every sponsored chase on every show follows this table. Intervals are on Cadences.

| | Founder Thesis | un# |
| --- | --- | --- |
| The offer | podm.in/sponsored, no price in the first mail | unhashed.co/sponsored, no price in the first mail |
| Price, only when asked | INR 1,00,000 + GST (podm.in/why-sponsor) | USD 1,500 |
| Before any follow-up | They must show interest in the sponsored option: ask about fees, deliverables or timing, say they are considering it, or ask for details. Silent or noncommittal: no follow-up at all. | Same |
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
     "  - We declined and Parked: Akshay's call; agents never set or change them (decision 656). A live ask on such a row reopens it to Decision pending for him (decision 621)."),
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
     "## Standing checks\n\n- <b>Reach claims.</b> A figure that combines Akshay's and Unnati's channels says \"we have\" and names the channels and the dated source; never call it Founder Thesis's own following.\n- <b>Verified completion closes only its own obligation.</b> A group join removes the add or invite ask (and Akshay from Waiting on only if nothing else of his is left); it never proves a list, an intro or another promise was sent.\n\nZoya is live (since 2026-10-16 00:20 JST)."),
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
     "- <b>Recipients</b> (decisions 144, 180, 188, 227, 229, 305, 586, 592, 643, 646, 647). Controls; every send and draft from either inbox follows it, and the prompts check it in code before every send.\n  1. Reply on a thread with anyone outside the team: everyone on its latest message (From, To, Cc), less only Zoya's own address, People tagged \"Email bounced\", People whose Role starts \"Ex-employee (mailbox dead)\", Akshay's addresses other than ad@thepodium.in, and Mamatha (on a long break). Everyone else stays, whether or not they wrote: team members, Sri, client-show hosts, PR, comms, EAs.\n  2. Then add whoever is missing of: Akshay (ad@thepodium.in) in Cc; Zoya in Cc on mail from ad@thepodium.in; Chaandini on Built to Share and Human by Design; Divir and Ankita Joshi on Pathfinders; Jaya and Sarika on revenue mail (sponsored from their yes on: next steps, billing, invoices, payments; never expenses); the guest or a company-side contact on guest-facing mail (day-before note, prep note, recording link, reschedule, thank-you).\n  3. A new mail to someone outside the team: their side from the row and the step, plus the same additions; a new thread someone outside the team starts with Zoya gets Akshay in Cc.\n  4. Team-only mail: the team members only, never Akshay (decision 592), never Mamatha.\n  5. Never added on our own: Sri or a host to a thread they are not on, Mamatha, Saurabh Garg (except decision 517 below).\n  6. To is whoever's move it is, everyone else Cc; ad@thepodium.in is never in To; no team address is in To on outside mail."),
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
    ("drop_section", "S8-templates", "Retired: do not send"),
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
     "## Runtime inventory\n\n<b>Describes.</b> Who runs what, when, and from which source. The CTO updates this table in the same release as any schedule or prompt change, and reads each scheduled task back before marking it live. Cadences owns how often people are contacted.\n\n| Worker | Job | When (JST) | Reads | Model | Sends |\n| --- | --- | --- | --- | --- | --- |\n| Zoya day chat | Runs inbox actions, Zoya FAST, WhatsApp and calendar, and the OUTBOX | Weekdays every 2 hours 07:38 to 23:38; weekends 08:38, 12:38, 16:38, 20:38 | routines/zoya-day.md, the release prompts, Rules for Zoya and its subpages, Cadences, Client show mails | as its seed sets | Every mail, WhatsApp and invite |\n| Capture composer | Logs mail (inbox capture) | Start of every wake | composer seed, inbox-capture.txt | claude-sonnet-5-5 | Nothing |\n| SLOW composer | Follow-ups, nurture, team work, payments | Weekdays 11:08 and 17:08 | composer seed, zoya-slow.txt and its work file | claude-opus-5-5 | Nothing: drafts only |\n| Engagement chats | Evals, dossiers, blurbs for one guest | When the day chat sends a step | docs/engagement-chat-seed.md, the show's skills | claude-opus-5-5 | Nothing |\n| Blurb chats | One community blurb | On request | docs/blurb-chat-seed.md, skills/ft-community-blurb | as started | Nothing |\n| On Akshay's Mac | Zencastr transcripts | His schedule | routines/mac | n/a | Nothing |\n\nThe daily sweep, the hourly routines' own scheduled tasks, the evals and dossier schedules are retired; see Retired routines."),
]
