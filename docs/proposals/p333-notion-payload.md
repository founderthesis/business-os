# p333 Stage B: paired Notion payload (exact before and after)

The texts are as fetched on 18 Oct:
- Rules for Zoya (3f719a301a7f81a09de3ee3ad6ad98a3), last edited 17 Oct 16:01Z
- Mail and WhatsApp wording (3fa19a301a7f81b6a807d0f01847dae7)
- the Templates row "Sponsored turned down: close the thread" (3f719a301a7f8190ad7fc25529cbb809), last edited 15 Oct

Each "Before" is an exact substring for notion-update-page update_content. Notion's escapes (\{ \} \< \>) are omitted here for reading and are restored at apply time. Main applies everything in the same window as the Stage B prompt push, then fetches both pages and checks every "After" is present and every "Before" is gone. Rollback is Notion page history.

## A. Rules for Zoya

### A1. Section 1, "Akshay's automation" paragraph
Before:
> **Akshay's automation** (ad@thepodium.in): agents send in Akshay's name only what needs the host. Since decision 235 (Akshay, 16 Oct) that's only short mails with no link and no attachment: the holding reply ("adding @Zoya"), acknowledgements and close notes on a no. The no-show note is Zoya's (decision 236). Anything with a link or an attachment goes from Zoya, including his decision on a pitch, offers, the day-before note, release mail 1 and the patron ask. The thank-you is the exception for now: the calendar run drafts it in Akshay's Gmail and he attaches the transcript and sends it by hand (decision 300; client shows, decision 308). Akshay replies by hand where he wants to. Signed "Regards, Akshay".

After:
> **Akshay's account** (ad@thepodium.in): agents send from it only the two lines in "Who sends" below: the reply adding Zoya and the reply putting her back (decision 333, replaces the send lists of decisions 200 and 235). Acknowledgements, close notes, vendor redirects, decision mails and every other routine mail come from Zoya. Mails in Akshay's own voice (the thank-you for now, decisions 300 and 308; a client show's day-before note, thank-you and pre-release ask, decision 313) are drafts he sends by hand. Akshay replies by hand where he wants to.

### A2. Section 1 table, two rows
Before (row): `Holding reply to a fresh pitch, adding Zoya | Akshay's automation | New (section 3)`
After (row): `Adding Zoya to a thread where their side wrote last | Akshay's account (decision 333) | Section 3 and "Who sends"`

Before (row): `Close note when they say no to sponsored | Akshay's automation | With the influencer line (decision 196)`
After (row): `Close note when they say no to sponsored | Zoya (decision 333) | With the influencer line, in her voice (decision 196)`

### A3. New section "Who sends", inserted between the section 1 table and "## 2. Rules for every mail"
After (new):
> ## Who sends (decision 333, Akshay, 18 Oct)
> Every routine reads this before any mail.
> Akshay's account (ad@thepodium.in) sends to anyone outside the team for three things only:
> 1. **The reply that adds Zoya**, where their side wrote last: "thanks \<first name\>, adding @Zoya to coordinate", Zoya in Cc, nothing else. Where we wrote last there is no loop-in (decision 216): Zoya sends her mail as a new mail from her inbox, To the person whose move it is, Akshay in Cc, subject "Re: \<thread subject\>".
> 2. **A personal reply Akshay writes himself.** Routines never send these: a mail in Akshay's voice is a draft in his Gmail.
> 3. **A short reply putting Zoya back** on a thread someone dropped her from: "adding @Zoya back to coordinate", Zoya in Cc, once per message, at most 20 a run (the rest wait for the next run), outside the daily cap.
>
> Everything else a routine sends to someone outside the team comes from Zoya, on the thread, with Akshay in Cc. That covers decision mails, acknowledgements, edit-notes replies, vendor redirects, admin confirmations, assets received, no-show and close notes, chases and every follow-up. When the step is only an acknowledgement and Zoya isn't on the thread yet, the loop-in is the acknowledgement; it never stands in for a decision mail, a redirect or an answer.
>
> **A reply addressed only to Akshay** (nobody else on To or Cc) **on a thread where Zoya was included in To or Cc on an earlier message stays his** (Akshay, 18 Oct): no restore, no Zoya step and no new mail from Zoya on it, and it completes nothing. He hands it back if he wants. On a thread Zoya never joined, the normal loop-in and new-mail routes apply.
>
> **Unchanged:** mail only to the team, show rollout dates (a show not yet hers keeps its coordinator), house copies, the daily cap, bounces, and the context, leak and show checks.

### A4. Section 2, Thread
Before: `- Reply on the existing thread, To the person whose move it is.`
After: `- Reply on the latest message in your own inbox from the person whose move it is (their messages only in Akshay's inbox are context, never the message you reply to), reply_all off, with Cc set yourself: everyone else who should stay on it, Akshay and the house copies. If your inbox has no message from them on the thread, send a new mail To them with the same Cc and subject "Re: <thread subject>". If neither works, send nothing and report "addressing blocked" (decision 333).`

### A5. Section 2, Format
Before: `- Zoya's mail goes through MCP Emails from her inbox. Akshay's automated mail goes through the Gmail connector from ad@thepodium.in (decision 235: MCP Emails files a second copy in his Sent folder), and never carries a link (Gmail turns links into google.com redirects with a warning page) or an attachment. Format either way:`
After: `- Zoya's mail goes through MCP Emails from her inbox. Akshay's account sends only the two lines in "Who sends", through the Gmail connector, never with a link or an attachment (decision 333). Format either way:`

### A6. Section 2, Voice, acknowledgements
Before: `- **Every mail from outside gets acknowledged** (decision 200), by Akshay or Zoya: an intro, a handover, "will revert" or a file shared gets "thanks <first name>" or "noted, thanks".`
After: `- **Every mail from outside gets acknowledged** (decision 200), by Zoya (decision 333): an intro, a handover, "will revert" or a file shared gets "thanks <first name>" or "noted, thanks". On a thread she isn't on yet, the loop-in is the acknowledgement; no second thanks.`

### A7. Section 3, item 2 lead
Before: `2. **Holding reply, the first inbox run after it arrives.** Akshay's automation sends it from ad@thepodium.in, on the original pitch message.`
After: `2. **Adding Zoya, the first inbox run after it arrives.** Akshay's account sends it ("Who sends", item 1) from ad@thepodium.in, on the original pitch message.`

### A8. Section 3, item 2.1
Before: `1. Saurabh forwards also get his one-line "Thanks for sharing, SG" on his own thread.`
After: `1. Saurabh forwards get "Thanks for sharing, SG" on his own thread as a draft Akshay sends (decision 333).`

### A9. Section 3, item 2.3
Before: `3. A vendor or service pitch gets Akshay's one-liner, not a holding reply, with Zoya in Cc. Zoya handles the vendor thread from there (decision 225). The one-liner: "thanks <first name>, pls could you fill out this form for us to evaluate your offering: podm.in/pitch-to-us". Live 15 Oct.`
After: `3. A vendor or service pitch gets the same reply adding Zoya ("Who sends", item 1), and Zoya sends the "Vendor or service pitch redirect" (wording page) from her inbox (decisions 225, 333). A vendor pitch Saurabh forwards gets a Vendor Engagement with the redirect as Zoya's step, and the later form links to it.`

### A10. Section 4, Acknowledge and the Cc bullet
Before: `- **Acknowledge:** an intro, a handover, "will revert", a file shared: "thanks <first name>" (decision 200, live). A thanks to us, an out of office or an auto-reply: nothing. Nothing is marked read.`
After: `- **Acknowledge:** an intro, a handover, "will revert", a file shared: "thanks <first name>" from Zoya (decisions 200, 333); on a thread she isn't on yet, the loop-in is the acknowledgement. A thanks to us, an out of office or an auto-reply: nothing. Nothing is marked read.`

Before: `- **Zoya goes in Cc on every reply here.** Most threads from the last 72 hours don't have her yet (live).`
After: `- **Every reply here comes from Zoya** (decision 333). Where she isn't on the thread yet, Akshay's account adds her first ("Who sends").`

### A11. Section 5, "For every routine", last bullet
Before: `- If Zoya isn't on the thread yet when her follow-up is due, that one mail goes from ad@thepodium.in in Akshay's terse voice, carrying the follow-up itself with Zoya added at the end, for example "Sreerag, any update from Trishank on the precall? adding @Zoya to coordinate". Never a bare "thanks <name>, adding @Zoya" on a thread where we wrote last (decision 216). After that, the mails come from her (section 9).`
After: `- If Zoya isn't on the thread yet when her follow-up is due: where their side wrote last, Akshay's account adds her ("Who sends", item 1) and she sends the follow-up from her inbox once the thread reaches her; where we wrote last, she sends it as a new mail from her inbox, To the person, Akshay in Cc, subject "Re: <thread subject>" (decisions 216, 333). No follow-up ever goes from ad@thepodium.in.`

### A12. Section 9, items 1 and 2
Before: `Threads where we wrote last are skipped; Zoya joins them with their next follow-up, which carries the ask (section 5).`
After: `Threads where we wrote last are skipped; Zoya joins them with her next follow-up, sent as a new mail from her inbox (section 5, decision 333).`

Before: `2. **Everything else joins lazily.** That's 76 FT Sponsored offered (the next nurture mail already carries Zoya, decision 180), 54 FT and 37 un# LT chase, and older Precall requested rows. Their next due follow-up goes once from ad@thepodium.in with Zoya added, then she takes over.`
After: `2. **Everything else joins as needed.** That's 76 FT Sponsored offered (the next nurture mail already carries Zoya, decision 180), 54 FT and 37 un# LT chase, and older Precall requested rows. Their next due follow-up comes from Zoya as section 5 says; nothing goes from ad@thepodium.in except the loop-in (decision 333).`

### A13. Section 10, the first "Live" line
Before: `- **Live (15 Oct):** the one-line holding reply, the vendor one-liner, acknowledgements, Zoya in Cc on every reply, and no read-marking.`
After: `- **Live (15 Oct):** the one-line holding reply, Zoya in Cc on every reply, and no read-marking. Since decision 333 the vendor redirect and acknowledgements come from Zoya.`

## B. Mail and WhatsApp wording

### B1. Intro paragraph, two sentences
Before: `The inbox and calendar routines still read the Templates database for the mails they send from ad@thepodium.in until it's retired (Rules for Zoya, section 10).`
After: `No routine sends template mail from ad@thepodium.in (decision 333); the inbox reads the Templates database only to fill drafts and Zoya's queued decision mail.`

Before: `**Since 16 Oct (decision 235), Akshay's account only sends the short, link-free lines in section 0**, through Gmail as replies inside the existing thread, so his inbox keeps the whole history.`
After: `**Since 18 Oct (decision 333), Akshay's account sends only the two loop-in lines at the top of section 0**, through Gmail inside the existing thread.`

### B2. Section 0 heading
Before: `## 0. From Akshay's account: short lines, no links (decision 235)`
After: `## 0. Adding Zoya, and Zoya's short replies (decision 333)`

### B3. Holding reply toggle, the When text
Before: `**When:** the first inbox run after a new guest pitch reaches us. **Status:** live from 15 Oct (decisions 195, 199).`
After: `**When:** the first inbox run after a new guest pitch reaches us, and any thread Zoya isn't on yet where their side wrote last; never where we wrote last (decisions 216, 333). **Status:** live from 15 Oct (decisions 195, 199).`

### B4. New toggle after the holding reply
After (new):
> ### Zoya restore (new) {toggle="true"}
> **From:** Akshay (ad@thepodium.in), reply-all on the message that dropped Zoya. **When:** a message from outside the team on a thread Zoya was on leaves her off To and Cc. Once per message, at most 20 a run. Never on a reply addressed only to Akshay (nobody else on To or Cc): that stays his (decision 333). **Status:** new; goes out once Akshay approves the [Zoya test] mail (decision 238).
> adding @Zoya back to coordinate

### B5. Close note toggle, re-voiced for Zoya
Before (heading): `### Sponsored turned down: close note with the influencer line (new)`
After (heading): `### Sponsored turned down: close note with the influencer line`

Before (body):
> **From:** Akshay (ad@thepodium.in), reply-all on the thread. **When:** the guest or PR says no to the sponsored route, or asks for organic only. **Status:** live from 15 Oct (decision 196): the Templates row "Sponsored turned down: close the thread" now carries this wording. Model: Akshay's reply to Howden India, 15 Oct; first sent to Capwise, 15 Oct.
> [A clear no to paying, or organic only: this note once, then stop the sequence. Never a price or a counter-offer here.]
> Hi {PR or guest first name},
> Sorry to hear that, and thanks for letting us know.
> Think of me as a B2B influencer: a sponsored feature is influencer marketing spend that puts {guest first name} in front of founders, CXOs and investors. It's also what lets us keep doing the work we love, sustainably.
> If plans change, do get in touch.
> Thanks & Regards,<br>Akshay

After (body):
> **From:** Zoya, on the thread, Akshay in Cc (decision 333; was Akshay). **When:** the guest or PR says no to the sponsored route, or asks for organic only. **Status:** re-voiced 18 Oct; goes out once Akshay approves the [Zoya test] mail (decision 238). Until then the step waits in Zoya's queue. Model: Akshay's reply to Howden India, 15 Oct.
> [A clear no to paying, or organic only: this note once, then stop the sequence. Never a price or a counter-offer here.]
> Hey {PR or guest first name},
> Sorry to hear that, and thanks for letting us know!
> Think of Akshay as a B2B influencer: a sponsored feature is influencer marketing spend that puts {guest first name} in front of founders, CXOs and investors. It's also what lets us keep doing the work we love, sustainably.
> If plans change, just give me a shout.
> Stay awesome ✨<br>Zoya

### B6. Acknowledgement toggle
Before:
> **From:** Akshay or Zoya. **When:** an intro, a handover, "will revert", a file shared (decision 200). **Status:** live from 15 Oct.
> thanks {first name}

After:
> **From:** Zoya (decision 333). On a thread she isn't on yet, Akshay's loop-in is the acknowledgement; no second thanks. **When:** an intro, a handover, "will revert", a file shared (decision 200). **Status:** live from 15 Oct; Zoya's sign-off added 18 Oct.
> thanks {first name}!
> Stay awesome ✨<br>Zoya

### B7. Two new toggles in section 3, after "Admin ask: noted, added before release"
These carry the inbox's current bodies (inbox STEP 6d, live), re-voiced for Zoya.
After (new):
> ### Assets received (new) {toggle="true"}
> **From:** Zoya, on the thread, Akshay in Cc (decision 333; was the inbox, decision 137). **When:** a guest, PR or company sends material for a recorded or booked episode (videos, photos, logos, b-roll, a file or folder link). The inbox logs the assets on the Episode. **Status:** new; goes out once Akshay approves the [Zoya test] mail (decision 238).
> Hi {first name},
> Thanks, received! We're passing {what they sent, a few words} to our editor for {guest first name}'s episode.
> Stay awesome ✨<br>Zoya

> ### Admin confirmation (new) {toggle="true"}
> **From:** Zoya, on the thread, Akshay in Cc (decision 333; was the inbox, decision 133). **When:** a message only asks us to confirm a fact (did Akshay get the invite, is the time still fine, did the link or file arrive, which address to send to) and the inbox has checked the fact. Never to agree a new date or time, accept or move an invite, or touch fees, terms or a booking decision. **Status:** new; goes out once Akshay approves the [Zoya test] mail (decision 238).
> [Two or three lines stating the fact, with day, date and time in their time zone (IST for India). No links.]
> Hi {first name},
> {The fact, e.g. "Yes, Akshay has the invite for Tue, 21 Oct, 3:00 pm IST."}
> Stay awesome ✨<br>Zoya

## C. Templates row "Sponsored turned down: close the thread"
- Body before: the Akshay version (identical to B5's "Before" body lines, "Thanks & Regards, Akshay").
- Body after: the same as B5's "After" body, from the bracketed instruction line to the sign-off.
- **Mode:** Send becomes **Off**. No routine sends this row after Stage B; Zoya sends the wording-page toggle.
- **Approved:** stays ticked; not changed.
- **Owner routine:** inbox becomes **none**.
- **Sender:** "Akshay (ad@thepodium.in), reply on the thread" becomes "Zoya, reply on the thread (decision 333)".
- **Notes:** "Reply-all on the thread, Mamatha in Cc. Status They declined. Wording from Akshay, 12 Oct." becomes "Zoya sends the wording-page toggle (decision 333); this row is kept for history. Status They declined."
- **Version:** 1 becomes 2.

## D. Owner action this creates
Four [Zoya test] mails to Akshay: Zoya restore, close note, Assets received and Admin confirmation (decision 238). The changed Acknowledgement only adds Zoya's sign-off to a live line and is listed for him to see.

Until he approves, those steps wait in Zoya's queue:
- nothing is sent from ad@ in their place;
- the restore line itself is not sent.
