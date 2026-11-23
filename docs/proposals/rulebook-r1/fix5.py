"""Rulebook r1, fix 5 (23 Nov): Akshay's answers on fix 4 (decision 661).

1. The three free feature toggles are approved, with "ok to go ahead?" replaced by
   "interested?" in drafts 1 and 2 ("ok to go ahead seems too eager"). Draft 3 unchanged.
2. The "wording awaiting Akshay" wait goes.
3. A Founder Thesis sponsored lead with no reply 30 days after the free feature offer goes on
   the Saturday Park proposals (CTO default, Akshay didn't object). Revival rows are already
   closed and are not parked.
Before text: data/rulebook-r1/fix4-live (fix 4 read back). Run: python3 fix5_apply.py <before_dir> <after_dir>.
"""

PAGES = {
    "follow-ups": "40b19a301a7f81999c1acd8350d59a54",
    "fu-8-revival": "3fa19a301a7f81008e72f23ebc526327",
    "cadences": "3ff19a301a7f8143aa95cd89bd6519ec",
    "wording": "3fa19a301a7f81b6a807d0f01847dae7",
}

PARK30 = "no reply 30 days after it: the Saturday Park proposals"
APPROVED = "<b>Status:</b> approved (decision 661, Akshay, 23 Nov)."

EDITS = {
    "follow-ups": [
        ("replace", "G1-silent-row",
         "(wording page: \"Free feature offer: silent sponsored lead (FT)\"). Never on the Park proposals |",
         "(wording page: \"Free feature offer: silent sponsored lead (FT)\"); " + PARK30 + " |"),
        ("replace", "G2-stop-row",
         "Status stays; never the Park proposals. No nurture.",
         "Status stays; " + PARK30 + ". No nurture."),
        ("replace", "G3-offer-row",
         "Sent once per lead, only in the wording page's approved text; a toggle still marked PROPOSED is never sent (the step waits as \"Zoya: free feature offer to \\<name> (wording awaiting Akshay)\"). A yes: \"Feature interest: book the call with Akshay\". No reply: no chase.",
         "Sent once per lead, only in the wording page's approved text (decision 661). A yes: \"Feature interest: book the call with Akshay\". No reply: no chase; 30 days after the offer with still no reply, the row goes on the Saturday Park proposals and Akshay decides."),
        ("replace", "G3b-offer-checkin",
         "They say they'll get back on it: one check-in 7 days after that mail. | Not used |",
         "They say they'll get back on it: one check-in 7 days after that mail; no reply 30 days after the check-in: the Saturday Park proposals. | Not used |"),
        ("replace", "G3c-pause-row",
         "The free feature: one check-in 7 days after that mail, then nothing unless they write. |",
         "The free feature: one check-in 7 days after that mail; no reply 30 days after the check-in: the Saturday Park proposals. |"),
    ],
    "fu-8-revival": [
        ("replace", "G4-no-wait",
         " While that toggle is PROPOSED, no revival mail goes.", ""),
    ],
    "cadences": [
        ("replace", "G5-ft-row",
         "Silent 7 days after the offer, or after the fifth: the free feature offer once (decision 661).",
         "Silent 7 days after the offer, or after the fifth: the free feature offer once (decision 661); no reply 30 days after it: Park proposals for you."),
        ("replace", "G5b-pending-row",
         "| Free feature pending, they'll get back | Their mail | One check-in 7 days after it (decision 661) | Their reply |",
         "| Free feature pending, they'll get back | Their mail | One check-in 7 days after it (decision 661) | Their reply. None 30 days after the check-in: Park proposals for you |"),
    ],
    "wording": [
        ("replace", "G6-title-1", "PROPOSED: Free feature offer: silent sponsored lead (FT)", "Free feature offer: silent sponsored lead (FT)"),
        ("replace", "G7-status-1",
         "Once per lead. <b>Status:</b> PROPOSED, waiting on Akshay's ok; never sent while PROPOSED.",
         "Once per lead. " + APPROVED),
        ("replace", "G8-note-1",
         "They'll get back: one check-in 7 days later. No reply: no chase.\\]",
         "They'll get back: one check-in 7 days later. No reply: no chase; 30 days on, the Saturday Park proposals.\\]"),
        ("replace", "G9-ask-1",
         "in the last 3 months. we would be happy to write one on \\{guest first name\\}, free, built from a 30-minute call with Akshay. ok to go ahead?",
         "in the last 3 months. we would be happy to write one on \\{guest first name\\}, free, built from a 30-minute call with Akshay. interested?"),
        ("replace", "G10-title-2", "PROPOSED: Free feature offer: sponsored revival (FT)", "Free feature offer: sponsored revival (FT)"),
        ("replace", "G11-status-2",
         "(decisions 355, 661). <b>Status:</b> PROPOSED, waiting on Akshay's ok; never sent while PROPOSED.",
         "(decisions 355, 661). " + APPROVED),
        ("replace", "G12-ask-2",
         "we would be happy to write one on you, free, built from a 30-minute call with Akshay. ok to go ahead?",
         "we would be happy to write one on you, free, built from a 30-minute call with Akshay. interested?"),
        ("replace", "G13-title-3", "PROPOSED: Free feature check-in (7 days)", "Free feature check-in (7 days)"),
        ("replace", "G14-status-3",
         "7 days after that mail (decision 661). Once. <b>Status:</b> PROPOSED, waiting on Akshay's ok; never sent while PROPOSED.",
         "7 days after that mail (decision 661). Once. " + APPROVED),
    ],
}

MUST_GO = {
    "follow-ups": ["wording awaiting Akshay", "never the Park proposals", "Never on the Park proposals"],
    "fu-8-revival": ["PROPOSED"],
    "cadences": [],
    "wording": ["PROPOSED: Free feature", "never sent while PROPOSED", "write one on you, free, built from a 30-minute call with Akshay. ok to go ahead?"],
}
MUST_KEEP = {
    "follow-ups": ["| Parked | Only on Akshay's word (decision 656) | Same |", "<b>Pauses on their word</b>"],
    "fu-8-revival": ["## The mail", "Free feature offer: sponsored revival (FT)"],
    "cadences": ["| Free feature pending, they'll get back |"],
    "wording": ["One-time: free feature offer to repeat guests", "Free feature check-in (7 days)",
                "checking in on the free written feature for \\{guest first name\\}."],
}
