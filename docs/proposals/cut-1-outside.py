"""Cut 1, Cleanup's two fixes (verdict 21 Oct 00:51 UTC, via the CTO): quiet hours from the Cadences row, and explicit To and Cc
with Akshay never in To, on every mail to anyone outside the team. Applied to inbox, calendar and Zoya after their Cut 1 part."""
RULE = ("- OUTSIDE MAIL (Cleanup, 21 Oct): nothing goes to anyone outside the team in the quiet hours on Cadences "
        "(23:00 to 10:00 JST); it waits for the first run after 10:00. Set To and Cc explicitly: To is whoever's move it is, "
        "Cc the house copies; Akshay is never in To.\n")
HEAD = {"inbox": "HARD RULES\n", "calendar": "HARD RULES\n", "zoya": "HARD RULES (always hold, whatever a page says)\n"}

def edit(name, s):
    h = HEAD[name]
    assert s.count(h) == 1, (name, "head")
    s = s.replace(h, h + RULE)
    if name == "zoya":
        o = ("runs starting 10:00 to 23:00 JST, decisions 362 and Akshay 21 Oct; never Diwali week). Quiet hours: no mail to anyone "
             "outside the team from 23:00 to 10:00 JST, replies included; it waits for 10:00")
        assert s.count(o) == 1, "zoya window"
        s = s.replace(o, "runs starting 10:00 to 23:00 JST, decision 362, Akshay 21 Oct; never Diwali week; quiet hours: OUTSIDE MAIL)")
        o = "Replies and queue steps go any run inside those hours; mail to the team or WhatsApp to Akshay is not held."
        assert s.count(o) == 1, "zoya replies"
        s = s.replace(o, "Replies and queue steps go any run outside quiet hours; mail to the team and WhatsApp to Akshay are never held.")
    return s
