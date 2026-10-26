# Routine prompts: where message wording and sending controls live

Read-only survey of the repo at branch `templates-consolidation` (clean, level with origin `claude/business-os-structure-k3sqo5`, head 3dfa2e4), 26 Oct 2026. Email addresses are written as "Akshay's mailbox" (ad@) and "Zoya's inbox". Literal text is quoted short; `<...>` are the prompt's own placeholders. "(sparkles)" stands for the emoji in Zoya's sign-off and group posts.

Notion pages named below, with ids:
- Mail and WhatsApp wording 3fa19a301a7f81b6a807d0f01847dae7 ("wording page")
- Rules for Zoya 3f719a301a7f81a09de3ee3ad6ad98a3
- Client show mails 3fc19a301a7f817588e2d081af825f8a (pitch sheets, C1 to C19)
- Cadences 3ff19a301a7f8143aa95cd89bd6519ec (caps, quiet hours, intervals)
- Inbox and Your call rules 3ff19a301a7f8148993ccea78fc66428 (Controls)
- Calendar rules 3fa19a301a7f816c9a53fe80557d0046
- Episode asset filing 3fe19a301a7f815c9925e8f16b94910b (Controls)
- Sales page "Founder Thesis: sponsored guest features" 3ea19a301a7f8109ac3ed03e82c9a9c0
- Zoya routine pages 1 to 8 (Sponsored offers, Precall requested, Recording slot, Misc chase, Guest form, Release, Long-term chase, Sponsored revival)
- FT community invite kit 3f919a301a7f8182809ede95a2cdae19

The Templates database (b2976a03-...) is read by no routine. Inbox, calendar and sweep each say "The Templates database is retired: never read it." No prompt mentions "Short templates", "Approved row" or a "Mode" column. CLAUDE.md still says the inbox and calendar routines read the Templates database; that sentence is stale.

---

## 1. Inbox (routines/inbox.md, "Inbox to Business OS", hourly at :02 JST)

Sends from Akshay's mailbox with the Gmail connector. Sends WhatsApp to Akshay's own chat with Blueticks.

### A. Sources read

| Step | Source | Quote | Messages it governs |
|---|---|---|---|
| WORDING (preamble) | Mail and WhatsApp wording | "the only mail you fill is Akshay's decision mail (STEP 6c), from its toggle on the Notion page "Mail and WhatsApp wording" ... use only a toggle marked approved" | Akshay's decision mail (filled here, sent by Zoya) |
| 6c a | wording page toggles | "Tier 1: keen, ask for a pre-call"; "Tier 1.5: alignment check call"; "Tier 2: alignment check call, organic undecided"; "Sponsored: founder wrote directly"; "Sponsored: no organic slot (via PR)" | Decision mail by tier |
| 6c c | wording page toggle | "{show credentials} = the toggle "Show credentials: <show name>"" | Credentials block inside the decision mail |
| 6c a0 | "the show's approved decline template" | no page named; implied wording page | Decline decision mail |
| YOUR CALL | Inbox and Your call rules (Controls) | "read it every run; it wins where it differs" | Loop-ins (6a), repeat-guest wording ("Sponsored for a repeat guest" on the wording page), snoozes, owners |
| CADENCES | Cadences | "every contact cadence and limit number (the daily cap, hold defaults ...)" | Daily cap, quiet hours |
| HARD RULES, 6c d0 | Client show mails | "SHOW CHECK ... show facts only from that show's pitch sheet"; "on un# the pitch sheet and SHOW CHECK apply" | Any un#, B2S, HBD send or draft |
| 3 (sponsored no) | wording page | "the close note, once, is Zoya's, in her voice from the wording page (decision 379)" | Sponsored close note (handed to Zoya) |
| 3 (chase step) | Rules for Zoya 5a | "One branch (Rules for Zoya 5a)" | Nurture routing, not wording |
| 6d | Episode asset filing (Controls) | "follow the Notion page "Episode asset filing"" | Filing only; no mail |

### B. Wording inside the prompt

| Step | Message | Literal text |
|---|---|---|
| 6 (and 3 repeat pitch) | Loop-in on a new FT or un# pitch | "thanks <sender's first name>, adding @Zoya to coordinate" (lowercase, nothing else) |
| 6a | Thanks to Saurabh for a guest-pitch forward | "Thanks for sharing, SG." then "Thanks & Regards," / "Akshay Datt" |
| 6a | Thanks to Saurabh for a vendor forward | "Thanks for sharing, SG. I've asked <first name> to fill out podm.in/pitch-to-us." + same sign-off |
| 6b (and 6a vendor) | Vendor redirect | "thanks <first name>, pls could you fill out this form for us to evaluate your offering: podm.in/pitch-to-us" |
| 6c c | Decision-mail fills | {community link} = " (see who's in: podm.in/community)"; {community sentence} = " It also comes with access to the Founder Thesis community of 500+ founders and investors: podm.in/community."; "600+" followed by "(podm.in/guest-list)" |
| WHATSAPP TO AKSHAY | Contact card to Akshay's own chat | "zoya here: <topic> <emoji>", then 2 to 4 context lines, signed "Zoya, Akshay's AI Chief of Staff" |
| 4 | Brand or paid-article reply (proposal in page body, never sent until ok) | Not literal, but the prices are in the prompt: "USD 750 base, about INR 60k + GST ... +50% ... +USD 400" |
| 6e B | Recording logistics reply (Zoya's) | Content spec only: laptop raised to eye level, no background blur, AirPods fine, quiet room; "nothing needs preparing, it is a free-flowing conversation". The inbox no longer sends this (ZOYA LIVE), so this wording is not read by the sender |
| Your call | Proposal line written into Next action | "Write ok, not ok or a change in Your call." |

### C. Controls inside the prompt

| Step | Message | Control |
|---|---|---|
| ZOYA LIVE | All | Inbox sends only the STEP 6 loop-in, 6a, 6b and WHATSAPP TO AKSHAY. Everything else (decision mail, close note, edit-notes reply, acknowledgement, admin, assets, routine replies) is "Waiting on Zoya ... log nothing as sent" |
| HOUSE COPIES | Every mail from Akshay's mailbox to outsiders | Zoya in Cc; Chaandini on B2S and HBD; never Mamatha |
| HARD RULES, OUTSIDE MAIL | All outside mail | Quiet hours from Cadences (00:30 to 07:30 JST); To = whoever's move it is; Akshay never in To |
| LINKS / FORMAT | All mail | Gmail redirects links, so links are unlinked text with the first dot broken by an empty span; never an `<a>` tag; htmlBody with one `<p>` per paragraph; own approved-link list (no founderthesis.com, podm.in/ad, youtube) |
| CONTEXT CHECK, BOUNCES | All mail | get_thread first; drop "Email bounced" addresses; never include_attachments |
| 6 | Loop-in | FT and un# only, pitch under 72 h, nobody from our side on thread, send never draft, To the sender, Cc others except Saurabh; skip repeat, vendor, closed rows; within daily cap; logged as loop-in |
| 6a | Saurabh thanks | Reply to Saurabh only, Cc house copies; Saurabh never on guest-facing mail; daily cap counted from "Zoya sent" Activities, loop-ins excluded |
| 6b | Vendor redirect | Send never draft, To the sender, Cc house copies, at most 20 per run, daily cap |
| 6c d0 | Decision mail | Never sent here. Filled text goes into "## Decision mail (<id>)" in the page body; Next action "Zoya: send Akshay's decision mail (<template>)"; at most 15 per run |
| 6e | Buckets A, B | Send nothing; queue "Zoya: <reply type>"; bucket C queues "Zoya: holding reply to <who> (decision 390)" unless one went in 7 days |
| WHATSAPP TO AKSHAY | WhatsApp | Akshay's own chat only, id from a fromMe message, two lowercase messages |
| 7 | RSVP archive | Never mark read (decision 199) |

---

## 2. Calendar (routines/calendar.md, "Calendar sync")

Header says hourly at :35; the prompt says "SIX RUNS A DAY (CTO, 26 Oct)". Sends through MCP Emails from both inboxes; drafts through Gmail create_draft.

### A. Sources read

| Step | Source | Quote | Messages |
|---|---|---|---|
| WORDING (preamble) | wording page; Client show mails for client shows | "the wording of every mail and draft is the toggle named below on the Notion page "Mail and WhatsApp wording" ... use only a toggle marked approved" | All its mails and drafts |
| DAILY CAP, HARD RULES | Cadences | "DAILY CAP: the number on the Notion page "Cadences""; quiet hours | All sends |
| 1b | Calendar rules | "read it each run, and if it disagrees with this step, the page wins" | Audit, double-booking check |
| 1b rule 1 | Rules for Zoya + wording page | "the "Double booking check" mail (Rules for Zoya, Mail and WhatsApp wording)"; "her sign-off from the wording page" | Double booking check (Zoya) |
| 3b | wording page toggle | "Recording tomorrow: looking forward, prep note" | Day-before note, FT (sent) and client shows (draft) |
| 3b | Prep note Notion page (per guest) | "fetch the Notion page whose id is the last 32 hex characters of the Prep note link and paste its content in full" | Body of day-before note |
| 4c | wording page toggle | "Rules for Zoya, Mail and WhatsApp wording, "FT thank-you after recording" ... read fresh each run and used exactly" | FT thank-you draft |
| 4d | Client show mails C13 + pitch sheet | "Wording: C13 on Client show mails, its theme from the show's pitch sheet (SHOW CHECK)" | Client thank-you draft |
| HARD RULES | Client show mails | SHOW CHECK | Any client-show send or draft |

### B. Wording inside the prompt

| Step | Message | Literal text |
|---|---|---|
| 1b rule 1 | Double booking check subject | "<guest name>: two calls on <D Mon>?" |
| 3b | Day-before fills | {conversation} = "your conversation with Akshay" (FT, Zoya's voice, Akshay in third person); "our conversation" for FT and "your conversation with <host first name>" in the client-show fill list (the two FT values conflict) ; client draft "signed Akshay" |
| 4c | FT thank-you subject | "Next Steps \| <Guest full name> @ <Company> <> Founder Thesis" |
| 4d | Client thank-you subject | "Thank You <guest first name>!" |
| 4d | Client thank-you host line | "I'm CCing <host first name> so that you two can be directly connected." or "You are already in touch with <host first name>, he mailed you directly." |
| 3 | Host "Podcast prep" invite (to the host, notification ALL) | Summary "Podcast prep: <Guest> @ <Company>"; description "Dossier: <link>", "Recording link: <studio>" |
| 1b rule 4 | Studio link added to a guest invite (notification ALL) | "Recording link: <link>" appended to the description |
| 2, 4a, 4c, 4f | Steps queued for Zoya or Akshay | "Zoya: <recording\|precall> on <date> cancelled, send the reschedule mail"; "...get new slots for <host> to pick (no podm.in links)"; "Zoya: ask <who> if the <D Mon> <recording\|call> is still on, <Guest> declined the invite"; "Zoya: ask Ranjita for the transcript (decision 376)" (step text, not mail text) |

### C. Controls inside the prompt

| Step | Message | Control |
|---|---|---|
| ZOYA LIVE, HARD RULES | All | Sends only the double-booking check (1b) and the FT day-before note (3b), both from Zoya's inbox. Thank-yous and client-show day-before notes are drafts for Akshay. Everything else is "Waiting on Zoya" |
| MAIL FORMAT | All | MCP Emails email_compose from the right inbox, include_signature false, html_body one `<p>` per paragraph, real `<a href>` links, plain-text copy; reply on latest message, reply_all false, To and Cc explicit; drafts via Gmail create_draft; own approved-link list (no podm.in/note, pitch-to-us, founderthesis.com) |
| HOUSE COPIES | Mail or draft from Akshay's mailbox | Zoya in Cc; Chaandini on B2S, HBD; never Mamatha |
| BEFORE EVERY SEND | All | Context check, bounces, else "Akshay: <mail> for <guest> held: <why>" |
| OUTSIDE MAIL | All | Quiet hours from Cadences; Akshay never in To |
| DAILY CAP | All | Count "Zoya sent" or "Agent sent" today, loop-ins out |
| 1b rule 1 | Double booking check | FT precalls and recordings only; send never draft; from Zoya's inbox, new mail; Cc the others on the invites and Akshay (decision 229); within cap; only when "likely an accident"; cancel the duplicate only after they name the slot to keep |
| 3b | FT day-before note | Sent from Zoya's inbox, Akshay in Cc, only if event unchanged, starts 3 h or more ahead, no Akshay hold, none sent; expiry deletes stale drafts. Prep note link empty: send nothing, ask Akshay |
| 3b | Client-show day-before | Always a draft in Akshay's mailbox (decision 313); To the guest, Cc Via, Stakeholders, house copies; never Saurabh; "Ask Akshay to send the day-before mail" |
| 4c | FT thank-you | Draft in Akshay's mailbox (Gmail create_draft), reply on the latest thread with guest or PR, else new; To guest + Via; Cc Stakeholders + house copies; Next action "Akshay: send the thank-you draft ... (attach the transcript)" |
| 4d | Client thank-you | Draft, always a NEW mail; To guest; Cc PR, Zoya, house copies, host by default |

---

## 3. Daily sweep (routines/daily-sweep.md, "Daily sweep")

Header says weekdays 13:10 JST; the prompt runs in two parts (A before 14:00, B after).

### A. Sources read

| Step | Source | Quote | Messages |
|---|---|---|---|
| WORDING (preamble), 3d a | Client show mails | "drafts (STEP 3d) take their words from the toggle named there on the Notion page "Client show mails""; "Take the show's pre-release toggle" | Client-show pre-release draft (subject and body) |
| HARD RULES | Cadences | "within the daily cap on the Notion page "Cadences"" | Billing forwards |
| 3, 3r | Rules for Zoya 5a | "take exactly one branch (Rules for Zoya section 5a)" | Nurture routing only |
| 3h | OS Audit page 3fc19a301a7f8171b1e2ef19ded7c239 | handoffs to Task rows | No mail |

### B. Wording inside the prompt

| Step | Message | Literal text |
|---|---|---|
| 6c | Billing forward to Jaya | forwardText "For the tax records: <vendor or client>, <what it is>, <amount if shown>." |
| 2, 4 | Steps queued for Zoya | "Zoya: send the sponsored commercials", "Zoya: quiet since <date>, chase or update the status", "Zoya: recorded <date>, send the form reminder", "Zoya: send GST and invoice details", "Zoya: chase <who> for <what> (promised by <D Mon>)" (step text only) |

### C. Controls inside the prompt

| Step | Message | Control |
|---|---|---|
| HARD RULES | All | Only STEP 6c sends; drafts only in 3d; every guest send is Zoya's (ZOYA LIVE) |
| LINKS | All outside mail | Unlinked span-broken text; approved list includes podm.in/ad and founderthesis.com; "Always pass the mail text as htmlBody (plain lines joined with <br>)": this contradicts CLAUDE.md, the inbox and the calendar (one `<p>` per paragraph, never `<br>` blocks) |
| HOUSE COPIES, BEFORE ANY SEND | All | Zoya Cc, Chaandini on B2S, HBD, never Mamatha; bounces; context check |
| 3d | Client pre-release draft | un#, B2S, HBD only (FT release mail 1 is Zoya's); 7-day window; draft never sent; To guest + Via; Cc Stakeholders, house copies and team members Akshay's last pre-release mail copied; "Ask Akshay to send the pre-release mail" |
| 6c | Billing forward | To Jaya from her People row; Gmail forward; exclusion list (alerts, OTPs, finance list, personal); once per message id; counts toward daily cap |

---

## 4. Zoya (routines/zoya.md, hourly at :30 JST) and the split build (routines/zoya/)

**Which is the source.** `routines/zoya.md` is the live single prompt (65,210 B, deployed in e922498). It is not generated from the parts. `routines/zoya/build.py` builds the two trial prompts, `zoya-fast.txt` and `zoya-slow.txt`, from `routines/zoya/parts/*.txt` (manifests FAST and SLOW plus a VARIANT list of per-prompt rewrites); zoya.md is only an optional second argument for a coverage check. So: zoya.md is the source for production; parts are the source for FAST/SLOW, which are not accepted (see section 13).

### A. Sources read (zoya.md)

| Step | Source | Quote | Messages |
|---|---|---|---|
| THE RULES ARE IN NOTION | Rules for Zoya | "who sends what, copies, voice, limits, replies, never-followed-up, the loop-in" | All |
| same | wording page | "the words of every one-off mail" | All one-off mails |
| same | Cadences | "it is the master: where a routine page or this prompt gives another number, Cadences wins" | Caps, intervals, windows |
| same | Client show mails | "the un# pitch sheet and the client templates C1 to C19" | All un#, B2S, HBD mail |
| same | Routine pages 1 to 8 | "Those pages decide who gets which mail, when, and in what words. Where a page and this prompt differ, the page wins, except for the HARD RULES" | Every follow-up step |
| NOTION DATA | Sales page | "Numbers in any mail come only from it, as it reads today" | Sponsored numbers, fee, steps |
| NOTION DATA | FT guests database | "peers for name-drops" | Follow-up angles |
| UN#, B2S/HBD | pitch sheets, C templates | "the words come from the un# templates. A un# mail no template covers goes on Akshay's list unsent"; C1, C2 (Chaandini), C5, C7, C8, C16, C17 named | Client-show mails |
| INTERNAL TASKS | Rules for Zoya, "Internal ad-hoc tasks" and "Transcript requests" | "has the wording" | Transcript request to Ranjita, internal follow-ups |
| INTERNAL c(4) | wording page | "approved "FT thank-you after recording" wording in Akshay's voice" | FT thank-you draft (when transcript arrives) |
| VOICE | Rules for Zoya, Plain English | "follow the Plain English rule on Rules for Zoya" | All |
| 0e | wording page | "uses only "Sponsored for a repeat guest" from the wording page" | Repeat-guest decision mail |
| 0e | Engagement page body | "## Decision mail (<decision id>)" holds the filled template (filled earlier by the inbox from the wording page) | Akshay's decision mail |
| 1b | Rules for Zoya section 4 + wording page | "Answer it per Rules for Zoya section 4, with the wording page"; toggles "Sponsored commercials (FT)", "Sponsored yes: next steps", "Price negotiation: hold the price, offer The Spotlight Podcast" | Replies |
| 1c | Rules for Zoya sections 4 and 7 | what is not routine | Holding reply routing |
| STEP 2 routine 1 | Engagement page body + podm.in/why-sponsor | "The planned mail is in the page body section "## Next sponsored mail": send it in your voice"; "plans it from the thread and podm.in/why-sponsor" | Sponsored follow-ups |
| STEP 2 routine 1 | wording page | "the sponsored close note from the wording page" | Sponsored close note |
| STEP 2 routine 6 | wording page | "Pre-release ask (FT)"; "Patron ask (FT)" once approved | Release mails 1 and patron |
| STEP 2 | Routine pages' fallback angle | "with neither, use the page's fallback angle" | Follow-ups |
| INVITES | Rules for Zoya, Calendar rules | "detail on Rules for Zoya and Calendar rules" | Invite and confirmation |
| NURTURE | Rules for Zoya 5a | "the master copy"; routine 7 and 8 angles | Nurture mails |
| HARD RULES | wording page, sales page, Client show mails | "Never a price, discount, term or deadline that isn't on the wording page or the sales page"; SHOW CHECK | All |

### B. Wording inside the prompt (zoya.md)

| Step | Message | Literal text |
|---|---|---|
| VOICE | Every mail | Opens "hey <first name>,"; signs "best," then "Zoya (sparkles)"; style rules and banned words |
| VOICE | Release mail 2 | Opens "Zoya here, I work with Akshay on the Founder Thesis podcast." |
| UN# | un# price answer | "a sponsored appearance on un# is USD 1,500, details at unhashed.co/sponsored" (price lives in the prompt) |
| SENDING | Follow-up from Akshay's mailbox on a thread Zoya is not on | e.g. "Sreerag, any update from Trishank on the precall? adding @Zoya to coordinate" |
| SENDING | Loop-in when their side wrote last | "thanks <first name>, adding @Zoya to coordinate" |
| SENDING | Loop-in when we wrote last | "<first name>, adding @Zoya to coordinate <the ask in a few words>" |
| TEAM WHATSAPP | WhatsApp to Jaya, Sarika | first message opens "hi <name>, zoya here."; last signed "Zoya, Akshay's AI Chief of Staff" |
| 0b step 5 | Reply to Akshay's feedback | "done, live now: <what changed>, <scope>" or "written, not live yet: <what>. I'll tell you when it's live." |
| 0f | Owner mail to Akshay | subject "Zoya: <n> for you, <D Mon>"; close "Reply with the number and your answer."; reply "noted: <n> updated" |
| 0g | Monday scorecard to Akshay | subject "Zoya: last week (<D Mon> to <D Mon>)"; five lines "1/ follow-ups: <due> due, <sent> sent" ... "5/ next: ..." |
| 1b | Edit-notes reply | "Edit notes: noted with thanks" (looks like a toggle name used as text) |
| 1b | Cancel request | Content only: "reply that it's cancelled with the rebook link" / "taking it off the calendar and ask for a fresh slot" |
| 1c | Holding reply | "hi <first name>, checking with akshay, will come back by <weekday, 3 working days out>." |
| 1d | New pitch sent to Zoya | "thanks <first name>! looping in Akshay" |
| 1b (payments) | Payment thanks, Jaya WhatsApp | Content spec only: one-line thanks; WhatsApp names guest, company, invoice 1 or 2, amount |
| 0e | Repeat-guest rule | ends "lmk if interested" (also on the wording page) |

### C. Controls inside the prompt (zoya.md)

| Step | Message | Control |
|---|---|---|
| SCOPE, UN#, B2S/HBD | All | Shows in scope; host never mailed or in Cc; Chaandini Cc on B2S, HBD; links per show; no sponsored offer on B2S, HBD; un# negotiation to Akshay |
| SENDING | All | MCP Emails, include_signature false, html_body `<p>` per paragraph, real links; approved link list; THREADING: replies as a draft, read back, then send; To = whoever's move it is; Cc Akshay always (decision 262), never his other addresses, never Mamatha, never Saurabh; Jaya and Sarika on revenue mail; idempotency_key format; Sent check before retry |
| SENDING | Fallback from Akshay's mailbox | Only short link-free follow-ups or loop-ins; a mail with link or attachment never goes from there |
| TEAM WHATSAPP | WhatsApp | Only Jaya and Sarika; chat by People Phone or named chat; logged |
| LIMITS | All | Daily and per-run caps from Cadences; 7-day one-mail-per-person; PR weekly limit (354); one thread per row; follow-up window and weekdays; never Diwali week; hand-written pause 4 working days; replies exempt from 7-day rule |
| HARD RULES | All | Quiet hours; LEAK CHECK; SHOW CHECK; never introduce self except release mail 2; never pose as Akshay |
| 0e | Decision mail | Superseded check, delivery check, then send To the pitcher, Cc thread + Akshay; status moves only on a message id |
| 0e2 | Approved day-before draft | Send exact draft only if event unchanged, 3 h ahead, no hold, none sent; else delete |
| 0f, 0g | Owner mail, scorecard | Once a day after 09:00; Monday after 08:00; to Akshay only |
| 1c | Holding reply | Once per 7 days per thread; reply, not a chase; quiet hours apply |
| 1d | New thread from outsider | Akshay in Cc; none if Akshay already on it |
| 1b, payments | Revenue | Jaya, Sarika, Akshay Cc; reminders on Cadences days; un# negotiation to Akshay; counter below INR 30,000 + GST to Akshay |
| RUN ORDER, STEP 2 | Follow-ups | Queue first; routine 7 and nurture capped at 10 a run; nurture moves at most 20 a day; revival only from sweep's cleanup line |
| ONE PERSON, ONE ASK | Follow-ups | Hold rules with 7 and 14 days; Salesblink hold until 2 Nov |
| INTERNAL | Transcript request | To Ranjita, Cc Akshay; quiet hours and 7-day rule do not apply; counts to cap |

### Split build deltas (parts only, not live)

| Part | Change vs zoya.md |
|---|---|
| actions.txt | New message: "decision 404's bare emoji reply (Rules for Zoya)" to an update with no ask, FAST only, under 48 h, once per thread per 7 days |
| reconcile.txt (SLOW) | New WhatsApp post in group "Zoya": "Zoya (sparkles) stuck: <row name>: <action, short> since <time>", once per action key, with pending and posted markers |
| mail.txt | Holding line goes inside another mail on the same thread instead of a second mail |
| internal.txt | Decision 412: the FT thank-you never waits for or carries a transcript; standalone NEW mail, never a reply on the PR thread; subject "Next Steps \| <guests> @ <company> <> Founder Thesis"; internal follow-ups first try one WhatsApp nudge to the team member |
| VARIANT (FAST) | Strips the release mail 2 exception, WhatsApp, follow-ups and vendor text from FAST |

---

## 5. WhatsApp (routines/whatsapp.md, hourly)

### A. Sources read

| Step | Source | Quote | Messages |
|---|---|---|---|
| 0d | Rules for Zoya (voice) | "in Zoya's voice (Rules for Zoya, decision 345: short, direct ...)" | Replies to team "@zoya" questions |
| 3c | FT community invite kit page | "Set A messages 1 to 6 from the page (message 5 is the member list ...)", "Set B messages 1 to 3" | Invite set sent to Akshay's own chat |

No read of the wording page, Cadences or Client show mails.

### B. Wording inside the prompt

| Step | Message | Literal text |
|---|---|---|
| 0 | Every group post | First line "Zoya (sparkles) <what this is>"; "- " lists |
| 0a a | Capture ack | "Zoya (sparkles) captured" + "<row name>: handed to the inbox, next run <time> JST" |
| 0a e0 | Community invite ack | "Zoya (sparkles) noted: <name> is on your invite list" |
| 0a e | Blurb ack | "Zoya (sparkles) noted for <guest>'s blurb. Edit it in its chat: <link>" or "...its editing chat isn't set up yet" |
| 0a f | Clarifying question | "Zoya (sparkles) quick check: is this about <best guess>?" |
| 0a2 | Done reports | "Zoya (sparkles) done: <row>: <what>"; "<owner> has: <ask>"; "Zoya (sparkles) handed over: ..."; "Zoya (sparkles) done by hand: ..."; "Zoya (sparkles) still open: <row name>: the inbox has not acted yet" |
| 0b | Precall promises | "Zoya (sparkles) from the <guest> precall I noted:" ... "anything else you promised?" |
| 0c | Briefs and digest | "Zoya (sparkles) <morning\|evening> brief" with fixed line set; "- <name>: invite to the community? reply 'invite <first name>'"; digest header "Zoya (sparkles) since <HH:MM>" |
| 0d | Team replies | Open "zoya here", signed "Zoya, Akshay's AI Chief of Staff"; group redirect "zoya here: sent you the details directly"; "zoya here: noted, <owner> has it"; booking description "Booked by Zoya for <member> (WhatsApp, <D Mon>)" |
| 3c | Invite set to Akshay | "fresh FT invite set: <n> new (<first names>), <total> members"; "set B, only if a direct add is blocked:"; kit header "group members, alphabetically, with company" |

### C. Controls inside the prompt

| Step | Message | Control |
|---|---|---|
| WHATSAPP IS READ-ONLY | All | Sends only to group "Zoya", Akshay's own chat, and team "@zoya" replies; no polls, media, reactions, mark_read |
| 0c | Briefs | Morning after 08:00, evening after 21:00; one digest per run; quiet hours 23:00 to 07:00 JST post only replies (its own window, not Cadences) |
| 0d | Team replies | Sender must be tagged Team; group replies only if every member is Team; no fees, contacts or notes in groups; booking slots 10:00 to 22:00 JST, standing approval (decision 378) |
| 3c | Invite set | Akshay's own chat only, one message per send, lowercase start |

---

## 6. Host boards (routines/host-boards.md)

A: none. B: none (writes Next action steps such as "<Host>: pick a slot for <guest> on your board (<the slots>)" and "Akshay: Sri says <Yes|No> on <guest> ... Your call?"). C: "Never send mail or messages." Stale control: the pre-307 path still sets "Waiting on Mamatha (Chaandini for B2S and HBD)" and "<team member>: send the decline (<Host> said no)", which contradicts decision 352 (nothing waits on Mamatha).

## 7. Cowork evals (routines/cowork-evals.md, whole file is the prompt)

A: none for wording (skills write the eval page). B: queued step "Zoya: ask <PR or guest first name> for a recording slot (podm.in/book), eval says book immediately"; replacement rows end "Write ok, not ok or a change in Your call." C: "NO MAIL (decisions 154, 207, 333): this task never sends mail, to anyone"; Gmail read only. The link choice (podm.in/book) for Zoya's slot ask is set here, not on the wording page.

## 8. Tasks (routines/tasks.md)

Not a prompt: a task-type table (owners, due dates). Mentions "Release emails and posts" (Ranjita) and "Reels email" (Sarika) as task names, with no wording or controls. No ```text block.

## 9. Community directory (routines/community-directory.md, Saturdays 09:47 JST)

No messages. Apollo search plus a mirror of FT Community to the public database. A, B, C: none.

## 10. Feedback call (routines/feedback-call.md)

Not a prompt: five-line procedure. Turns action items into Tasks "or Queue items for Akshay" (the Queue is retired; stale). No messages.

## 11. Mac transcripts (routines/mac/transcripts.md, Mac desktop task)

### A. Sources read
| Step | Source | Quote | Messages |
|---|---|---|---|
| NOTION list, 7g | wording page | "toggle "FT thank-you after recording". Use its text exactly; fill only the {placeholders}" | FT thank-you draft |

### B. Wording inside the prompt
| Step | Message | Literal text |
|---|---|---|
| 7g | FT thank-you subject | "Next Steps \| <Guest full name> @ <Company> <> Founder Thesis" |
| 7g | Sign-off | "Regards," then "Akshay" |
| 7 | Transcript line dropped when there is none | "The transcript of the episode is attached for your reference." |
| TEST MODE | Test draft | subject starting "[TEST] " |
| 7e, 7g | Next action text | "transcript attached" in place of "attach the transcript"; "Akshay: send the thank-you draft to <guest first name> (in your Gmail Drafts, transcript attached)" |

### C. Controls inside the prompt
| Step | Message | Control |
|---|---|---|
| MAIL RULES | All | Sends no mail ever; never sends or deletes a draft; only creates FT thank-you drafts; gate "draft attach probe passed" |
| 7g | FT thank-you | MCP Emails draft in Akshay's mailbox, reply on the latest thread with guest or PR (else new); To guest + Via; Cc Stakeholders, every outside address seen on threads and invites, and Zoya; patron paragraphs dropped only for Sponsored; html_body `<p>`, podm.in/thank-you as real link; transcript attached; read back |
| 7a to 7f | Client thank-you | Attach transcript to the calendar's draft only; never alter body or recipients |

## 12. Zencastr links (routines/mac/zencastr-mac.md)

No messages: "It sends no mail and never edits a calendar." A, B, C: none.

---

## 13. In-flight builds that change these prompts

| Build | Where | Status | Effect on wording or controls |
|---|---|---|---|
| Zoya FAST/SLOW split (decision 394) | routines/zoya/build.py + parts/, docs/proposals/zoya-split*.md, d-split26*.py, split-dryruns/ | Not accepted (f0f003a, 3dfa2e4): no lock (split-blocker.md; Akshay decided no lock in prompts); SLOW 65,312 B is 24 B under the build ceiling and 2,776 B over the 3,000 B size gate; round 4 R1, R2, L3, I2b fail | New messages (404 emoji reply, stuck alert), thank-you per decision 412. There is no inbox FAST/SLOW split; the split is Zoya's only |
| ACTION KEYS delta for inbox, calendar, sweep | docs/proposals/d394-keys.py | Deploys with the split, never before | Adds action keys to queued steps; grows those prompts |
| Release build frozen (8e64140, decisions 411 to 413) | d-411-412-cal-sweep.py on the ACTION KEYS outputs | Frozen, not deployed: inbox 63,536 B, calendar 56,272 B, sweep 35,319 B | Thank-you as standalone mail without transcript (412); recording status internal (411); Akshay's actions in his Notion queue, never WhatsApp. Live calendar 4c and Mac 7g still reply on the thread and attach the transcript |
| Consolidation 1 (sponsored obligations as Task rows) | docs/proposals/consolidation-1-sponsored-pilot.md, branch claude/consolidation-1-pilot | Proposal, nothing built | Moves "## Next sponsored mail" from the Engagement body to Task rows |
| Post-recording v2 (decision 374) | post-recording-v2.md | Partly live (one thank-you template) | Single "FT thank-you after recording" toggle with optional PR block |

---

## 14. Cross-routine table

"WP" = Mail and WhatsApp wording page; "CSM" = Client show mails; "RfZ" = Rules for Zoya.

| Message | Routines that send or draft it | Where each gets wording | Where each gets controls |
|---|---|---|---|
| Loop-in "thanks <name>, adding @Zoya to coordinate" | Inbox 6 (new pitch); Zoya SENDING (fallback, two variants) | Prompt literal in both (3 variants) | Inbox prompt (72 h, FT/un#, closed rows, cap) + Inbox and Your call rules (skip if Zoya already on it); Zoya prompt + RfZ ("the loop-in") |
| Thanks to Saurabh (guest and vendor forward) | Inbox 6a | Prompt literal, signed "Thanks & Regards, Akshay Datt" | Inbox prompt + Cadences cap |
| Vendor redirect | Inbox 6a, 6b | Prompt literal | Inbox prompt (20 per run, cap) |
| Akshay's decision mail (Tier 1, 1.5, 2, Sponsored x2, decline, repeat guest) | Inbox 6c fills; Zoya 0e sends | Inbox: WP toggles + "Show credentials" toggle + prompt fills ({community link} etc.) + CSM on un#; Zoya: page-body snapshot "## Decision mail", rewritten in her voice; repeat guest from WP | Inbox prompt (queue only, 15 per run); Zoya prompt (superseded and delivery checks, To pitcher, Cc Akshay); Inbox and Your call rules (repeat guest) |
| Holding reply "checking with akshay..." | Zoya 1c (inbox queues it) | Zoya prompt literal | Zoya prompt (7 days, quiet hours); inbox prompt queues it |
| New pitch to Zoya "thanks <name>! looping in Akshay" | Zoya 1d | Zoya prompt literal | Zoya prompt + RfZ (decision 188) |
| Acknowledgement, routine replies (booking, cancel, admin, assets, logistics, "any update?") | Zoya 1b (inbox 6d, 6e queue them) | RfZ section 4 + WP; inbox carries its own logistics content spec that Zoya does not read | Zoya prompt + RfZ; inbox decides routing |
| Sponsored commercials, yes next steps, price negotiation | Zoya 1b | WP toggles "Sponsored commercials (FT)", "Sponsored yes: next steps", "Price negotiation: hold the price, offer The Spotlight Podcast"; sales page for numbers | Zoya prompt (Jaya and Sarika Cc, INR 30,000 floor, un# to Akshay); inbox and sweep route |
| un# price answer | Zoya | Zoya prompt literal (USD 1,500) | Zoya prompt |
| Sponsored follow-ups (routine 1) | Zoya STEP 2 | Engagement "## Next sponsored mail" (written by Zoya from podm.in/why-sponsor and routine page 1) | Routine page 1 + Cadences + Zoya prompt |
| Sponsored close note | Zoya STEP 2 routine 1 (inbox queues) | WP | Zoya prompt; inbox 3 routing |
| Precall, recording-slot, misc, form, long-term chase (routines 2 to 5, 7) and nurture | Zoya STEP 2 | Routine pages 2 to 5, 7 (+ fallback angle), RfZ 5a; CSM C7 etc. on client shows | Routine pages + Cadences + Zoya prompt (LIMITS, NURTURE, ONE PERSON) ; sweep moves rows to nurture |
| Sponsored revival (routine 8) | Zoya STEP 2 | Routine page 8 | Routine page 8 + Cadences |
| Release mail 1 (pre-release ask), 2, 3, 4, patron | Zoya STEP 2 routine 6 (FT); sweep 3d drafts client-show pre-release | Zoya: WP "Pre-release ask (FT)", "Patron ask (FT)", routine page 6, prompt literal opener for mail 2; Sweep: CSM pre-release toggle | Zoya prompt + routine 6 + Cadences; sweep prompt (draft only, recipients) |
| Day-before note | Calendar 3b (FT send, client draft); Zoya 0e2 (sends an approved draft) | Calendar: WP "Recording tomorrow: looking forward, prep note" + Prep note page + prompt fills; Zoya: the draft as written | Calendar prompt (3 h, no hold, expiry); Zoya prompt 0e2 |
| Double booking check | Calendar 1b | WP "Double booking check" + RfZ; subject literal in prompt | Calendar prompt + Calendar rules |
| FT thank-you | Calendar 4c draft; Mac transcripts 7g draft; Zoya INTERNAL c(4) draft; split internal.txt draft | WP "FT thank-you after recording" in all four; subject literal in calendar, Mac and split; Mac adds sign-off and transcript line literals | Four different controls: calendar (Gmail draft, reply on latest thread, "attach the transcript"); Mac (MCP draft, reply, transcript attached, Zoya Cc); zoya.md (attach transcript to draft); split (standalone new mail, no transcript, decision 412) |
| Client thank-you | Calendar 4d draft; Mac attaches transcript | CSM C13 + pitch sheet; host line and subject literal in prompt | Calendar prompt (new mail, host Cc) |
| Client-show pre-release | Sweep 3d draft | CSM pre-release toggle | Sweep prompt |
| Transcript request to Ranjita | Zoya INTERNAL a | RfZ "Transcript requests" | Zoya prompt |
| Internal follow-ups to team | Zoya INTERNAL b | RfZ "Internal ad-hoc tasks" (split adds WhatsApp nudge) | Zoya prompt |
| Billing forward to Jaya | Sweep 6c | Prompt literal forwardText | Sweep prompt + Cadences cap |
| WhatsApp to Jaya (invoice, payment) and Sarika (edit notes) | Zoya TEAM WHATSAPP, 1b, EDIT NOTES | Prompt frame literal; content spec in prompt | Zoya prompt |
| WhatsApp to Akshay (contact card) | Inbox WHATSAPP TO AKSHAY | Prompt literal | Inbox prompt |
| Zoya group posts (acks, briefs, digests, done reports) | WhatsApp STEP 0 | Prompt literals | WhatsApp prompt (own quiet hours 23:00 to 07:00) |
| Team "@zoya" replies | WhatsApp 0d | Prompt literals + RfZ voice | WhatsApp prompt |
| Invite set to Akshay | WhatsApp 3c | Invite kit page + prompt literal header | WhatsApp prompt |
| Owner mail, Monday scorecard, feedback replies to Akshay | Zoya 0b, 0f, 0g | Prompt literals (subjects, closing lines, five-line format) | Zoya prompt |
| Stuck alert, emoji reply | Split only (SLOW RECONCILE, FAST ACTIONS) | Parts literal; emoji reply from RfZ (decision 404) | Parts |

---

## 15. Prompt sizes and headroom (cap 65,536 bytes for a scheduled task prompt)

Measured as UTF-8 bytes between the ```text fences (whole file where there is no fence).

| Prompt | Bytes | Headroom to 65,536 | Note |
|---|---|---|---|
| zoya.md (live) | 65,210 | 326 | Tightest. build.py's own ceiling is 65,336 (cap less 200) |
| inbox.md | 61,957 | 3,579 | Frozen release build would be 63,536 (2,000 headroom) |
| calendar.md | 54,901 | 10,635 | Frozen release build 56,272 (9,264) |
| daily-sweep.md | 33,824 | 31,712 | Frozen release build 35,319 (30,217) |
| whatsapp.md | 26,007 | 39,529 | |
| cowork-evals.md (whole file) | 14,795 | 50,741 | |
| host-boards.md | 8,474 | 57,062 | |
| community-directory.md | 4,168 | 61,368 | |
| mac/transcripts.md | 20,669 | 44,867 | Mac desktop task; cap may not apply the same way |
| mac/zencastr-mac.md | 5,365 | 60,171 | Mac desktop task |
| split zoya-fast (built today) | 38,248 | 27,288 | 12,648 B over the spec's 25 KB target |
| split zoya-slow (built today) | 65,312 | 224 (24 to the 65,336 build ceiling) | Fails the 3,000 B size gate by 2,776 B |

What moving wording out would free (rough, from the literals above): Zoya's literal mails (owner mail, scorecard, feedback replies, holding reply, loop-ins, un# price, release opener, team WhatsApp frame) are a few hundred bytes of text, but the surrounding per-message control prose is several KB; the inbox's LINKS block, 6a/6b literals, 6c placeholder fills and the 6e logistics spec Zoya never reads are about 3 KB; the calendar's thank-you and day-before control paragraphs about 4 KB. Shared preamble blocks repeated across inbox, calendar, sweep, Zoya and WhatsApp (PEOPLE MATCH, AKSHAY'S LIST, KIND, PERSON STEPS, HOUSE COPIES, SHOW CHECK, OUTSIDE MAIL) are about 2.5 to 3 KB each prompt.

## 16. Inconsistencies found along the way

1. Link format splits by sender: inbox and sweep (Gmail connector) write links as span-broken plain text; calendar and Zoya (MCP Emails) send real `<a>` links. Sweep also says "plain lines joined with <br>", against CLAUDE.md and every other prompt.
2. Four approved-link lists differ (inbox lacks founderthesis.com, podm.in/ad; calendar lacks podm.in/note, pitch-to-us, founderthesis.com; sweep includes podm.in/ad; Zoya includes youtube and unhashed.co/precall).
3. FT thank-you has four writers with conflicting controls (calendar 4c, Mac 7g, zoya.md INTERNAL c(4), split internal.txt). Only the split follows decision 412.
4. Calendar 3b gives two values for {conversation} on Founder Thesis.
5. Prices in prompts, not on pages: un# USD 1,500 (Zoya), paid-article rates (inbox STEP 4), INR 30,000 + GST floor (inbox, sweep, Zoya).
6. Headers disagree with prompts on timing: calendar (hourly vs six runs), sweep (one run vs parts A and B).
7. Stale: CLAUDE.md says inbox and calendar read the Templates database; host-boards still routes to Mamatha on the pre-307 path; feedback-call.md mentions Queue items.
8. Inbox 6e B still carries the recording-logistics reply content although the reply is Zoya's and she reads RfZ section 4 instead.
