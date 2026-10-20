"""Cut 1, WhatsApp part. Removes: Akshay's phone number and the community group id from the prompt (no phone numbers in
committed files; both are found at run time), the stale STEP 3d line, the retired blurb step's long text, Mamatha.
Adds: decision 360's one line in the Zoya group, and closing the FT Community add Task row when the guest joins."""

def edit(s):
    R = [
        ("and STEP 3c sends text messages to Akshay's own chat 919560085085@c.us. Nowhere else.",
         "and STEP 3c sends text messages to Akshay's own chat (its id is the \"from\" of any message of his with fromMe true; never typed). Nowhere else."),
        ("list_messages on 919560085085-1592905303@g.us since the start of the previous JST day.",
         "list_messages on the group named \"The Founder Thesis Community\" (chats search, chatType group) since the start of the previous JST day."),
        ("Then the count check: chats get on 919560085085-1592905303@g.us gives the member count;", "Then the count check: chats get on that group gives the member count;"),
        ("send Akshay the full invite set in his own chat (919560085085@c.us, the only chat you may send to),", "send Akshay the full invite set in his own chat (the only chat you may send to),"),
        ("Never set Waiting on Mamatha on a Founder Thesis row (decision 167).", "Never set Waiting on Mamatha (decision 352)."),
        ("0b. BLURBS: retired (decision 347, Akshay, 20 Oct: \"kill this process\"). Never post a blurb to this group and never rerun the blurb skill from here. Blurbs are drafted by the calendar routine and edited in each recording's own editing chat, linked under its \"Blurb, <date>\" section. Old blurb posts and their Activities stay as they are.",
         "0b. PRECALL PROMISES (decision 360): for each precall whose Task rows (Source ID \"precall:<event id>:<n>\") are new since your last post, once (dedupe: an Activity with Source ID \"promises:<event id>\"): post \"Zoya ✨ from the <guest> precall I noted:\" then one \"- <owner>: <promise>\" line each, then \"anything else you promised?\". His answer comes back as any message (0a). Blurbs are never posted here (decision 347)."),
        ("with a Claude note line \"YYYY-MM-DD: joined the FT Community per WhatsApp\".",
         "with a Claude note line \"YYYY-MM-DD: joined the FT Community per WhatsApp\", and set Task state Done on their open Task row for the community add (decision 360)."),
    ]
    i = s.index('- Blurb empty, or holding "{" or "}": find the person'); j = s.index("STEP 4. PUBLIC DIRECTORY MIRROR", i)
    s = s[:i] + "- Blurb and Blurb link are not yours: the calendar run writes the Blurb (decision 331) and Blurb link holds only the guest's editing chat (decision 359).\n" + s[j:]
    R.append(("rows completed in STEP 3d (name: LinkedIn, blurb)", "rows completed in STEP 3d (name: LinkedIn)"))
    for a, b in R:
        assert s.count(a) == 1, (a[:70], s.count(a))
        s = s.replace(a, b)
    return s
