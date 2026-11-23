"""Rulebook r1, fix 4 (23 Nov): decisions 660 and 661 on the source pages.

660: after interest, up to 5 sponsored follow-ups, 7 days apart, earlier sends counted.
661: the free founderthesis.com feature offer replaces parking for Founder Thesis
sponsored leads, and sponsored revival uses it; a free-feature "we'll get back" gets a
7-day check-in. un# keeps decision 422 (2 follow-ups, then Unresponsive).
New wording goes on the wording page as PROPOSED for Akshay; nothing unapproved is sent.
Run: python3 fix4_apply.py <before_dir> <after_dir>.
"""

PAGES = {
    "follow-ups": "40b19a301a7f81999c1acd8350d59a54",
    "fu-1-sponsored": "3fa19a301a7f81b0a80dc0c75102b60e",
    "fu-8-revival": "3fa19a301a7f81008e72f23ebc526327",
    "cadences": "3ff19a301a7f8143aa95cd89bd6519ec",
    "wording": "3fa19a301a7f81b6a807d0f01847dae7",
    "routines": "3fb19a301a7f813b949cf28cc0993541",
}

FREE = ("the free feature offer (decision 661): a written feature on founderthesis.com, free, "
        "built from a 30-minute call with Akshay")

EDITS = {
    "routines": [
        ("replace", "E18-upkeep-row",
         "BD episodes, flags, billing forwards to Jaya, guest forms | Weekdays, first wake at or after 13:00 | upkeep.txt | the day chat's | Nothing (drafts and one allowed ad@ forward) |",
         "BD episodes, flags, billing forwards to Jaya, guest forms, People LinkedIn enrichment through Reach (read only, up to 35 reads a day across all agents, decision 662) | Weekdays, first wake at or after 13:00 | upkeep.txt | the day chat's | Nothing (drafts and one allowed ad@ forward) |"),
    ],
    "follow-ups": [
        ("replace", "E1-routine-table",
         "Section 5c: interest first, at most 2 follow-ups, no nurture",
         "Section 5c: interest first, up to 5 follow-ups (Founder Thesis), then the free feature offer; no nurture"),
        ("replace", "E2-5c-heading",
         "## 5c. Sponsored offers and pauses: one table (decisions 227, 237, 367, 422, 573, 618, 625, 656)",
         "## 5c. Sponsored offers and pauses: one table (decisions 227, 237, 367, 422, 573, 618, 625, 656, 660, 661)"),
        ("replace", "E3-silent",
         "| Silent or noncommittal 7 days after the offer, no interest shown | No mail. The row goes on the weekly Park proposals for Akshay (decisions 618, 656) |",
         "| Silent or noncommittal 7 days after the offer, no interest shown | No sponsored follow-up. Instead, once, " + FREE + " (wording page: \"Free feature offer: silent sponsored lead (FT)\"). Never on the Park proposals |"),
        ("replace", "E4-after-interest",
         "| After interest | Answer what they asked from the wording page, then at most 2 follow-ups on the Cadences days | Same; a yes, a negotiation, terms or a call go to Akshay |",
         "| After interest | Answer what they asked from the wording page, then up to 5 follow-ups, 7 days apart, counted from our last answer (decision 660) | Answer, then at most 2 follow-ups on the Cadences days (decision 422); a yes, a negotiation, terms or a call go to Akshay |"),
        ("replace", "E5-counts",
         "| What counts toward the 2 |",
         "| What counts toward the limit (5 on Founder Thesis, 2 on un#) |"),
        ("replace", "E6-stop-noreply",
         "| Stop: no reply after the last follow-up | Send nothing more. Status stays; the row goes on the weekly Park proposals for Akshay. No nurture. |",
         "| Stop: no reply after the fifth follow-up | No more sponsored mail. Once, the free feature offer (decision 661), as for a silent lead. Status stays; never the Park proposals. No nurture. |"),
        ("replace", "E7-free-row",
         "| Parked | Only on Akshay's word (decision 656) | Same |",
         "| The free feature offer | Sent once per lead, only in the wording page's approved text; a toggle still marked PROPOSED is never sent (the step waits as \"Zoya: free feature offer to <name> (wording awaiting Akshay)\"). A yes: \"Feature interest: book the call with Akshay\". No reply: no chase. They say they'll get back on it: one check-in 7 days after that mail. | Not used |\n| Parked | Only on Akshay's word (decision 656) | Same |"),
        ("replace", "E8-pause-row",
         "| They'll reach out when ready (\"as and when\", \"we'll get back\", \"will revert once\") | Nothing for 30 days from that mail, then at most one short warm check-in on the primary thread, then nothing unless they write. The row goes on the Park proposals. (decision 625) |",
         "| They'll reach out when ready (\"as and when\", \"we'll get back\", \"will revert once\") | What's pending decides (decision 661). Money (a sponsored appearance, a payment): nothing for 30 days from that mail, then at most one short warm check-in on the primary thread, then nothing unless they write (decision 625); a Founder Thesis sponsored lead then gets the free feature offer once, any other row goes on the Park proposals. The free feature: one check-in 7 days after that mail, then nothing unless they write. |"),
    ],
    "fu-1-sponsored": [
        ("replace", "E9-top",
         "then at most 2 follow-ups, counting every chase already sent on the thread; no nurture, no revival; only Akshay parks (decision 656).",
         "then up to 5 follow-ups on Founder Thesis, 7 days apart (decision 660), and at most 2 on un# (decision 422), counting every chase already sent on the thread; no nurture. A Founder Thesis lead silent 7 days after the offer, or after the fifth follow-up, gets the free feature offer once (decision 661); only Akshay parks (decision 656)."),
        ("replace", "E10-revival",
         "Routine 8 may later write to a founder who wrote to us directly and whose no was to the price (decision 355).",
         "Routine 8 may later offer the free feature to a founder who wrote to us directly and whose no was to the price (decisions 355, 661)."),
        ("replace", "E11-links",
         "at most one per mail: [podm.in/sponsored](http://podm.in/sponsored) in mail 1, [podm.in/why-sponsor](http://podm.in/why-sponsor) for questions.",
         "at most one per mail: [podm.in/sponsored](http://podm.in/sponsored) in mail 1, [podm.in/why-sponsor](http://podm.in/why-sponsor) in mails 3 and 4 and for questions, [podm.in/guest-list](http://podm.in/guest-list) in mail 5."),
        ("replace", "E12-mails-3-5",
         "Use it only as written here.",
         "Use it only as written here.\n\n### Mail 3: access\n\n> Hi \\{PR\\},\n\n>\n\n> A sponsored appearance on the pod puts \\{guest\\} in front of founders, CXOs and VCs. That's the main reason founders do it. Guest profiles on [founderthesis.com](http://founderthesis.com) got 860k+ impressions from Google search alone in the last 3 months. The numbers are here: [podm.in/why-sponsor](https://podm.in/why-sponsor). Open to it?\n\n>\n\n> best,\n\n> Zoya ✨\n\n### Mail 4: questions\n\n> Hi \\{PR\\},\n\n>\n\n> Does \\{guest\\} have any questions about it? Happy to answer them, or [podm.in/why-sponsor](https://podm.in/why-sponsor) has the details.\n\n>\n\n> best,\n\n> Zoya ✨\n\n### Mail 5: who's been on\n\n> Hi \\{PR\\},\n\n>\n\n> Here's who Akshay has sat down with so far: [podm.in/guest-list](https://podm.in/guest-list). \\{guest\\} would be in good company. Open to it?\n\n>\n\n> best,\n\n> Zoya ✨\n\nMails 3 to 5 are the follow-up chains v2 wording (approved 21 Oct, decision 365), restored for decision 660. After mail 5 with no reply: the free feature offer (section 5c)."),
    ],
    "fu-8-revival": [
        ("between", "E13-mails",
         "## The mails\n",
         "Angle C only with real news from the last 60 days, checked against a second source.",
         "## The mail\n\nThe free feature offer (decision 661), from Zoya on the original thread, once per revival: the wording page toggle \"Free feature offer: sponsored revival (FT)\". While that toggle is PROPOSED, no revival mail goes. A later revival needs a new reason to write (a milestone, peers, real news from the last 60 days checked against a second source), at most one a quarter."),
    ],
    "cadences": [
        ("replace", "E14-ft-row",
         "| Sponsored offer (Founder Thesis) | Only after they show interest (Rules for Zoya: follow-ups, 5c) | At most 2 follow-ups: days 7 and 14, counting every chase already sent on the thread. None while they are silent. No nurture | A no, \"not our client\" or a yes. After the second with no reply: Park proposals for you. Below INR 30k goes to you |",
         "| Sponsored offer (Founder Thesis) | Only after they show interest (Rules for Zoya: follow-ups, 5c) | Up to 5 follow-ups, 7 days apart, counted from our last answer and counting every chase already sent on the thread (decision 660). None while they are silent. No nurture | A no, \"not our client\" or a yes. Silent 7 days after the offer, or after the fifth: the free feature offer once (decision 661). Below INR 30k goes to you |"),
        ("replace", "E15-revival-row",
         "| 1 mail a quarter, at most 5 a week from the backlog. From Fri 23 Oct, only when the no was to the price (decision 355) |",
         "| The free feature offer (decision 661), at most 1 mail a quarter, at most 5 a week from the backlog. Only when the no was to the price (decision 355) |"),
        ("replace", "E16-free-checkin",
         "| A promise or ask (misc chase) |",
         "| Free feature pending, they'll get back | Their mail | One check-in 7 days after it (decision 661) | Their reply |\n| A promise or ask (misc chase) |"),
    ],
    "wording": [
        ("replace", "E17-proposed-toggles",
         "<toggle heading=\"h3\">\nWhy not organic (they ask)",
         "<toggle heading=\"h3\">\nPROPOSED: Free feature offer: silent sponsored lead (FT)\n\n<b>From:</b> Zoya, on the sponsored thread, To whoever's move it is, Akshay in Cc. <b>When:</b> a Founder Thesis lead silent 7 days after the sponsored offer, or after the fifth follow-up (decisions 660, 661). Once per lead. <b>Status:</b> PROPOSED, waiting on Akshay's ok; never sent while PROPOSED.\n\n\\[A yes leads to \"Feature interest: book the call with Akshay\". They'll get back: one check-in 7 days later. No reply: no chase.\\]\n\nhi \\{first name\\},\n\nno worries if a sponsored appearance isn't the right fit for \\{guest first name\\} right now. we've started publishing written features on [founderthesis.com](http://founderthesis.com) (\\~300k monthly search impressions), and we would be happy to write one on \\{guest first name\\}, free, built from a 30-minute call with Akshay. ok to go ahead?\n\nbest,<br />Zoya ✨\n</toggle>\n\n<toggle heading=\"h3\">\nPROPOSED: Free feature offer: sponsored revival (FT)\n\n<b>From:</b> Zoya, on the original thread with the founder. <b>When:</b> routine 8, a founder who wrote to us directly and whose no was to the sponsored price (decisions 355, 661). <b>Status:</b> PROPOSED, waiting on Akshay's ok; never sent while PROPOSED.\n\n\\[A yes leads to \"Feature interest: book the call with Akshay\". No reply: no chase.\\]\n\nhey \\{first name\\},\n\nhope you're well. we've since started publishing written features on [founderthesis.com](http://founderthesis.com) (\\~300k monthly search impressions), and we would be happy to write one on you, free, built from a 30-minute call with Akshay. ok to go ahead?\n\nbest,<br />Zoya ✨\n</toggle>\n\n<toggle heading=\"h3\">\nPROPOSED: Free feature check-in (7 days)\n\n<b>From:</b> Zoya, on the same thread. <b>When:</b> they said they'd get back on the free feature offer, 7 days after that mail (decision 661). Once. <b>Status:</b> PROPOSED, waiting on Akshay's ok; never sent while PROPOSED.\n\nhi \\{first name\\},\n\nchecking in on the free written feature for \\{guest first name\\}. happy to set up the 30-minute call with Akshay whenever it suits.\n\nbest,<br />Zoya ✨\n</toggle>\n\n<toggle heading=\"h3\">\nWhy not organic (they ask)"),
    ],
}

MUST_GO = {
    "routines": [],
    "follow-ups": ["at most 2 follow-ups, no nurture", "The row goes on the weekly Park proposals for Akshay (decisions 618, 656)",
                   "the row goes on the weekly Park proposals for Akshay. No nurture.", "The row goes on the Park proposals. (decision 625)"],
    "fu-1-sponsored": ["then at most 2 follow-ups, counting every chase"],
    "fu-8-revival": ["### Angle A", "podm.in/sponsored"],
    "cadences": ["After the second with no reply: Park proposals for you"],
    "wording": [],
}
MUST_KEEP = {
    "routines": ["## One page per routine"],
    "follow-ups": ["## The nine routine pages", "<b>Pauses on their word</b>", "| Parked | Only on Akshay's word (decision 656) | Same |"],
    "fu-1-sponsored": ["### Mail 1", "### Mail 2", "### Mail 5: who's been on"],
    "fu-8-revival": ["## Who gets it", "## The mail"],
    "cadences": ["## Limits that apply to all of the above"],
    "wording": ["Why not organic (they ask)", "One-time: free feature offer to repeat guests",
                "PROPOSED: Free feature offer: silent sponsored lead (FT)"],
}
