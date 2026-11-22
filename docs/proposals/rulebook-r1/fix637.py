"""Rulebook r1, fix 1 (23 Nov): date ownership (decision 637) and two leftover one-off lines.

Auditor CX-20261123T0800 finding 2 on CTOA-03. Zoya's own chase steps write Zoya date;
Next date holds only people's steps and is never moved by a send, hold, deferral,
failed send or cap. Ops use the notion_edits op format; run fix637_apply.py.
"""

PAGES = {
    "follow-ups": "40b19a301a7f81999c1acd8350d59a54",
    "fu-7-nurture": "3fa19a301a7f8151b310e102839d630f",
    "rules-for-zoya": "3f719a301a7f81a09de3ee3ad6ad98a3",
}

EDITS = {
    "follow-ups": [
        ("replace", "D1-precedence",
         "Comment in the last column, as before. Your 15 Oct comments are applied to the cells and the pages below. Since 19 Oct, where a comment or a page's \"Your notes\" says to close a silent row as Unresponsive, section 5a governs instead (AR-20261019-1); the comments stay as written, for history.",
         "Comment in the last column. AD comments keeps Akshay's 15 Oct notes as he wrote them; the other columns and sections 5a to 5c are the rules that run."),
        ("replace", "D2-preserve",
         "Nothing on the row changes: Status, Call type, Waiting on, Next action and Next date stay.",
         "Nothing on the row changes: Status, Call type, Waiting on, Next action, Next date and Zoya date stay."),
        ("replace", "D3-nosend",
         "A run that sends nothing (a deferral, a failure) changes only Next date, with a reason; a cap is never a hold and changes nothing.",
         "A run that sends nothing (a deferral, a failure) changes only Zoya date, with a reason; a cap is never a hold and changes nothing."),
        ("replace", "D4-rowshape",
         "- Next date = the next contact.",
         "- Zoya date = the next contact (decision 637). Next date holds only people's steps (Akshay's decision, their side's move, a call) and no chase, hold or send ever moves it."),
        ("replace", "D5-scheduled",
         "scheduled (Waiting on Zoya with a Next date)",
         "scheduled (Waiting on Zoya with a Zoya date)"),
        ("replace", "D6-ordinary",
         "Chase step n, Next date the next step's date.",
         "Chase step n, Zoya date the next step's date."),
        ("replace", "D7-nurture",
         "Chase step 0, Next date the send date plus the interval for n.",
         "Chase step 0, Zoya date the send date plus the interval for n."),
        ("replace", "D8-nothing",
         "A hold or deferral moves the step's date and Next date; a failed send moves only Next date, with the reason; a cap changes nothing.",
         "A hold or deferral moves the step's date and Zoya date; a failed send moves only Zoya date, with the reason; a cap changes nothing. Next date is never touched by any of these."),
        ("replace", "D9-hold",
         "Every hold writes a recheck Next date and the reason",
         "Every hold writes a recheck Zoya date and the reason"),
        ("replace", "D10-550",
         "then set Next date 3 months out, Status LT chase,",
         "then set Zoya date 3 months out, Status LT chase,"),
    ],
    "fu-7-nurture": [
        ("replace", "D11-start",
         "- <b>Starts:</b> on the revisit date (Next date).",
         "- <b>Starts:</b> on the revisit date (Zoya date, decision 637)."),
    ],
    "rules-for-zoya": [
        ("replace", "D12-routines-live",
         "<b>Live for Founder Thesis from 16 Oct (decision 207). All 8 routines are live (decision 230).</b> ",
         ""),
        ("replace", "D13-oneoff",
         "; Akshay still decides un# guests and Sri picks slots; a one-time loop-in of open un# threads in her 16:30 JST run that day.",
         "; Akshay still decides un# guests and Sri picks slots."),
    ],
}

# Strings that must be gone from the new text (checked by fix637_apply.py).
MUST_GO = {
    "follow-ups": ["Next date = the next contact", "governs instead", "changes only Next date",
                   "Next date the next step's date", "Next date the send date", "moves only Next date",
                   "recheck Next date", "set Next date 3 months"],
    "fu-7-nurture": ["(Next date)"],
    "rules-for-zoya": ["All 8 routines are live", "one-time loop-in"],
}
MUST_KEEP = {
    "follow-ups": ["## 5c. Sponsored offers and pauses", "<b>Pauses on their word</b>", "## The nine routine pages",
                   "<page url=\"https://app.notion.com/p/3fa19a301a7f8151b310e102839d630f\">"],
    "fu-7-nurture": ["### Angle C: their news"],
    "rules-for-zoya": ["<b>Recipients</b>", "<b>Sender table</b>", "## Standing checks"],
}
