# Inbox and calendar audit (Akshay, thepodium.in mailbox)

Audit date: 2026-09-30. Read-only pass over Gmail and Google Calendar to size an inbox-driven Notion dashboard. Nothing was sent, labelled, archived or marked. Figures are measured on samples; the method section says how.

## Summary

- **Volume is about 50 inbox threads a day now** (about 66 on weekdays, 10 on weekends), up from a 90-day average of about 38. About 76% land in Primary. The inbox holds 21,679 threads, 8,386 unread, which matches the earlier audit.
- **Mamatha is the inbox.** She is the latest sender on 56% of sampled threads. Most of it is her talking to PR agencies with Akshay on cc. 52% of all inbox threads are cc-only for Akshay, and he replied on 12% of those.
- **He reads the cc traffic anyway.** Only 4% of cc-only threads are unread. Unread mail is almost all noise, finance@ group mail and Gemini notes. The real cost today is attention on Heads-up mail, not unread counts.
- **Class mix (thread-days):** Heads-up 61%, Decision 15%, Noise 14%, Action 9%, Personal 1%, explicit Reminder under 1%. At 50 a day that is roughly 30 Heads-up, 7 to 8 Decision, 7 Noise and 4 Action items.
- **Guest evals confirm the hypothesis, and the volume is higher.** At least 52 eval emails from Mamatha in September (about 1.7 a day, 2.4 per weekday). Akshay's reply is a median 3 words, 57% are 3 words or fewer. "sponsored" is 34% of verdicts and "invite to precall" 27%. Median reply lag is 7 hours, p90 is 44 hours.
- **Verdicts are predictable.** When Mamatha recommends Decline, Akshay says "sponsored" 70% of the time. When she says Strong consider, he picks precall 58% of the time. The dashboard can pre-fill the likely verdict.
- **He decides in batches.** In the sampled Sent week he fired 8 decisions in 21 minutes one afternoon and 7 in 12 minutes another morning. A once-a-day Decision queue fits how he already works.
- **About 70 to 75% of items could be auto-marked read** (Noise plus Mamatha's scheduling, nudges, acks, close-outs, declines, calendar RSVPs, finance notices). That leaves 10 to 14 items a day that need his eyes, of which 5 to 8 are real decisions.
- **Things drop in five places:** Gemini notes (67% never opened), deferred decisions with no reminder system, eval replies that stall past 40 hours, Zencastr post-production mails with no episode name, and show-owner drift (Ravi no longer on his myunnati mailbox).
- **Templates exist for FT and partly B2S.** HBD and un# have no thank-you template on record since April.

## Method and sample

**Inbox day sample.** 13 days across the 90 days from 2026-07-02 to 2026-09-29, one per week, rotating the weekday so every weekday appears (9 weekdays, 4 weekend days). For each day I pulled every thread in `in:inbox` with a message that day, paging to the end. That is 486 thread-days.

| Day | Weekday | Inbox threads | Est. non-Primary |
|---|---|---|---|
| 07-02 | Thu | 46 | 13 |
| 07-10 | Fri | 53 | 14 |
| 07-18 | Sat | 3 | 1 |
| 07-26 | Sun | 1 | 1 |
| 08-03 | Mon | 50 | 11 |
| 08-11 | Tue | 38 | 7 |
| 08-19 | Wed | 46 | 12 |
| 08-27 | Thu | 32 | 7 |
| 09-04 | Fri | 74 | 7 |
| 09-12 | Sat | 11 | 8 |
| 09-16 | Wed | 45 | 10 |
| 09-20 | Sun | 9 | 5 |
| 09-28 | Mon | 78 | 18 (measured) |

**Classification.** Rules on sender, whether Akshay is in To or only in Cc, subject and the snippet of the message that arrived that day. For 102 threads the preview did not include that day's message, so the latest visible message was used. Rules were spot-checked by reading the listings; expect a few percent of misfiles between neighbouring Heads-up sub-types.

**Primary vs other.** The Gmail API does not return category labels on messages, but `category:` search works. I measured one day directly (09-28: 60 of 78 Primary, 77%). For the rest, non-Primary is estimated from sender type (Gemini notes, Zencastr, finance@ promos, newsletters, bounces), which reproduces 09-28 within 3 threads.

**Archive check.** Non-inbox mail on sampled days was 1 to 8 threads, mostly calendar RSVPs that skip the inbox. So the inbox is close to everything received.

**Dedicated queries.**
- Guest evals: 200 threads from Mamatha containing "guest eval" since 07-02, giving 71 eval messages (Jul 21 to Sep 30) and Akshay's reply to each. July and August are undercounted because long threads only preview a few messages, so September (52) is the reliable month.
- One full Sent week (09-14 to 09-20): 82 of Akshay's messages.
- Thank-you and release-day sends over 90 days, BD sequence copies (September), sample Gemini and Zencastr messages read in full.
- Calendar: the thepodium.in work calendar, 237 events from 08-01 to 10-14. The legacy myunnati.com calendar, 12 events in the same window.

**Units.** Items are counted as threads active that day, not messages. The inbox averages about 2.1 messages per thread overall.

## Volume

| Measure | 90-day sample | Last ~30 days (5 sample days) |
|---|---|---|
| Inbox threads per day | 38 | 50 |
| Weekday average | 51 | 66 |
| Weekend average | 6 | 10 |
| Primary share | about 76% | about 76% |
| Unread at audit time | 21% of sampled threads | same |

- Mondays after a weekend are the peak (78 threads on 09-28).
- Aliases hello@, sp@, nk@ and rc@ all deliver into this inbox. They carry SaaS sign-up mail and duplicate cold pitches.
- The myunnati.com finance group address delivers here too. In the sample that was 21 vendor promos (all unread) and 10 transactional notices (GST filings, payment advice, invoices), 9 of them unread.
- Personal and household mail is about 1% of threads (6 in the sample). Counted only.

## Classification table

Share is of the 486 sampled thread-days. Per day uses the current rate of about 50 threads a day. "Replied" means an Akshay message visible after the item in the same thread.

| Class | Sub-type | Share | Per day | What Akshay does today | What the agent should do |
|---|---|---|---|---|---|
| Decision | Guest eval from Mamatha | 2% in sample; 52 in Sept by direct count | 1.7 | Replies to Mamatha in 1 to 3 words: "sponsored" 34%, "invite to precall" 27%, "go ahead / record" 10%, stop or decline 8%, other instruction 8%, no visible reply 8%. Median 7 h, p75 33 h, p90 44 h | Card with the eval link, show, recommendation and a pre-filled verdict. One tap posts the word in-thread to Mamatha. Escalate if open 24 h |
| Decision | Mamatha question or loop-in | 2.3% | 1.1 | "Kindly assist", "shall I offer sponsored?", "did this happen?". Replied 8 of 11, median 33 h | Show the question, a 3-line thread summary and 2 to 3 answer buttons |
| Decision | PR or guest writing to Akshay directly | 4.1% | 2.0 | Replied 13 of 20, median 9 h. Often just "adding @mamatha k to coordinate" | Default to route-to-Mamatha (Action) unless dates, money or a client is involved |
| Decision | New pitch sent straight to Akshay | 0.8% | 0.4 | "Thanks for your mail, adding @mamatha k to coordinate", median about 20 h | Standing rule: auto-route to Mamatha, log the person, no card |
| Decision | BD prospect, client or vendor | 5.3% | 2.7 | Replied 8 of 21, median 8 h. Pricing, launch dates, contracts, tool sales reps | Attach prospect or account context, draft reply, flag pricing questions |
| Decision | Team member asks Akshay | 0.6% | 0.3 | Replies within about 1 h | Pass through as-is |
| Heads-up | Mamatha scheduling precall or recording | 14.6% | 7.3 | Reads, replied 7 of 71 | Log as Activity on the person, auto-read. Surface only if a date clashes with his calendar |
| Heads-up | Follow-up nudge to PR ("just checking", "circling back") | 10.9% | 5.5 | Reads, replied 1 of 53 | Auto-read. Advance the ladder step on the person |
| Heads-up | Acks ("Noted and thanks for the update") | 9.5% | 4.7 | Reads, never replies | Auto-read, no item beyond the log |
| Heads-up | External reply inside a team thread (Akshay cc) | 9.1% | 4.5 | Replied 13 of 43 (30%), median 3 h | Keep as a light flag; auto-read after 24 h if nobody asks for him |
| Heads-up | Team to external, other staff (Chaandini, Sarika, Jaya) | 2.3% | 1.1 | Replied 1 of 10 | Auto-read |
| Heads-up | Calendar RSVPs (Accepted, Tentative) | 2.9% | 1.5 | Never opens replies | Update event attendance, auto-read |
| Heads-up | Decline sent, sponsored pricing sent, close-out | 5.4% | 2.7 | Never replies | Record outcome on the person and pitch, auto-read |
| Heads-up | Eval routed to another show owner | 1.2% | 0.6 | Replies with routing ("ask Ravi on WhatsApp") | Route to the right owner, flag owner changes |
| Heads-up | Finance notices (GST, payments, invoices) | 2.1% | 1.0 | Unread 9 of 10 | Summarise weekly for Jaya's side, auto-read |
| Heads-up | Bounces, security, release-day chatter | 1.8% | 0.9 | Ignores | Auto-read; alert only on real bounces |
| Action | Gemini meeting notes | 6.0% | 3.0 | 67% unread. Sometimes forwards with "make wa blurb" or "pls read through the notes, and take necessary action" | Pull the Doc link from HTML, match to calendar event and person, file as Activity, propose next step, auto-read |
| Action | Reply to thank-you mail (form filled, asset sent) | 1.2% | 0.6 | Replies to half | Check form status, update release checklist |
| Action | Drive share requests | 0.8% | 0.4 | Never acted on (4 of 4) | Card: grant or ignore |
| Action | Calendar invite or reschedule sent to Akshay | 0.6% | 0.3 | Replies himself when it hits him directly ("am in Japan time zone...") | Propose new slots from his calendar; ask before editing any event with guests |
| Action | Zencastr post-production ready | 0.2% | 0.1 | Downloads by hand | Match to the latest recording, start transcript step |
| Noise | Newsletters and SaaS promos | 8.0% | 4.0 | 90% unread | Auto-archive candidate |
| Noise | finance@ group vendor promos | 4.3% | 2.2 | All unread | Filter at the group or auto-archive |
| Noise | Own Substack issue, calendar reminders | 0.6% | 0.3 | Unread | Auto-archive |
| Noise | BD sequence copies (Mamatha outbound) | 0.6% | 0.3 | Ignores | Log to the prospect, auto-archive |
| Personal | Personal and household | 1.2% | 0.6 | Handles himself | Leave untouched, never on the dashboard |
| Reminder | Explicit ("do you want me to remind you? when?") | 0.2% | 0.1 | Answers ad hoc | Turn into a dated Reminder |

**Reminders mostly come out of decisions, not mail.** In the sampled week: "let's schedule in a couple of months", "we should ask him only after we release", "set it up in September", plus PR replies like "I'll circle back around mid-October". Expect 0.5 to 1 derived Reminder a day. The agent should create them when a Decision reply contains a deferral.

### What Akshay's Sent mail looks like (one week, 82 messages)

- About 37 go to Mamatha: verdicts and short instructions ("sponsored", "set up precall", "ask for the founder/CEO", "offer sponsored - 500 pounds", "don't follow up anymore").
- About 6 route a new PR pitch to Mamatha ("adding @mamatha k to coordinate").
- About 6 go to Chaandini (BD pitch prep, forwarded notes, loop-in corrections).
- 7 are templates (thank-you, release day, HBD release).
- About 26 are direct external replies (clients, prospects, guests rescheduling).

## Auto-mark-read candidates

Safe to mark read on arrival, after logging:
- Noise: newsletters, SaaS promos, finance@ vendor promos, own Substack issue, calendar reminders, BD sequence copies. About 14% of threads, 7 a day.
- Mamatha's cc traffic that carries no question for Akshay: scheduling, nudges, acks, close-outs, decline and pricing sends. About 42%, 21 a day.
- Calendar RSVPs and finance notices. About 5%, 2.5 a day.

Mark read after the agent finishes the job:
- Gemini notes once filed (3 a day), Zencastr notices once matched, thank-you replies once the form status is logged.

Keep unread until Akshay acts:
- All Decision items, external replies in team threads for 24 hours, Drive share requests, anything personal.

Net: about 33 of 50 daily threads can be auto-read on arrival (65%), rising to 70 to 75% once Action items clear. Open question below on whether Akshay wants to keep reading Mamatha's cc threads.

## Templates inventory

| Template | Sender | Trigger | Volume (90 days) | Shows covered | Notes |
|---|---|---|---|---|---|
| Thank you for coming on the podcast | Akshay | Recording done and transcript downloaded | 16 FT (Jul 23 to Sep 28), 2 B2S | FT, B2S | Subject "Thank you for coming on the Founder Thesis podcast!" (lately with "Guest @ Company"). To guest and PR, cc Sarika, Ranjita, Mamatha (B2S adds Satish and Chaandini). Four asks (personal post, company page post, employees engage, repost), "5x more views" line, **transcript attached as .txt** named after the calendar event, then a paragraph to the PR contact asking for the **podm.in/thank-you** form; release date promised after the form |
| Episode releasing | Akshay | Release scheduled (sent 1 to 7 days before, sometimes same day) | 8 FT, 3 B2S, plus HBD and un# variants seen | FT, B2S, HBD, un# | Subject "Episode releasing on {Day} 🎉 \| {Show} podcast". Three asks and "Do I have your buy in for this?". Same cc pattern. A go-live follow-up ("As discussed, the episode went live at...") comes from Mamatha or Akshay |
| Precall request | Mamatha | Verdict "invite to precall" | Several a week | FT mostly, adapted for un# | "Thanks for proposing X's profile... As part of our process we like to do an informal preliminary conversation..." plus booking link (podm.in/ad) |
| Sponsored decline | Mamatha | Verdict "sponsored" | About 1 a day | FT, un# | "Regrettably, we have limited slots..." plus paid-feature offer. Price INR 50,000 + GST in India, $600 no GST for non-India guests, one-off GBP quotes by Akshay |
| Follow-up ladder | Mamatha | No reply from PR | 5 a day of nudges | All | "Just checking, any dates for a preliminary call?" then "circling back" then "one final time" then "I am considering this closed. If you wish to explore a paid appearance...". Release-ETA answer: "usually around 8 to 10 weeks" |
| Route to Mamatha | Akshay | New pitch or PR mail sent to him | About 6 a week | All | "Thanks for your mail, adding @mamatha k to coordinate" |
| Booking links | Akshay, Mamatha | Scheduling | Daily | All | podm.in/ad (30-min Meet via zcal), podm.in/book (recording slot), podm.in/30min, podm.in/pi (intake form) |
| Recording invite body | Mamatha (on Akshay's calendar) | Recording booked | 38 events | FT, B2S, HBD, un# | Zencastr link, good-practice checklist, WhatsApp emergency contact |
| Guest prep note | Mamatha | Before recording | Per recording | FT seen | Link to a public Claude artifact sent to the PR contact |
| BD sequence | Mamatha-signed, automated | Prospect added | 3 sequences in Sept | BD | 4 steps a day apart at about 12:56 UTC: opener, "Sorry to bump", "One thought and then I'll leave you alone", "Last one from me, promise". Copies land in Akshay's inbox |
| BD pitch | Akshay | After a warm conversation | A few a month | BD | Subject "The {Company} podcast pitch", link podm.in/{company}-pitch, cc Chaandini |

**Gaps.** HBD and un# have no thank-you template on record (zero matches since April). B2S thank-you exists but is rare. Precall and decline wording says "Founder Thesis" and gets hand-edited for other shows. No template exists for rescheduling or for the post-precall "we'd like to record" step; both are written fresh each time.

## Meeting notes and transcripts

**Gemini notes**
- Sender is the Google "gemini-notes" address, to Akshay only ("sent to invited guests in your organization").
- Two subject formats:
  - `Notes: "<calendar event title>" <Mon D, YYYY>` when the call was a calendar event. About 55% in the sample. The title carries the guest name, so it matches the event.
  - `Notes: Meeting <Mon D, YYYY> at <h:mm AM/PM> <TZ>` for ad-hoc Meet calls. About 45%. No name; match by time only.
- Body has "Quick Notes" topic bullets and "Suggested next steps" tagged with an owner in brackets.
- **The Google Doc link is only in the HTML body** (the "Open meeting notes" button and a "Notes by Gemini" chip). The plain-text body loses the URL, so the agent must parse HTML.
- The same Doc is attached to the calendar event: 88 events in the window carry a "Notes by Gemini" attachment. That is the cleaner join.
- Failures arrive from the Google Meet no-reply address as "Problem with the notes: <title>". That call has no notes.
- Timezone in the subject moved from IST to JST around late July.
- Recordings on Zencastr produce no Gemini notes, only Meet calls do.

**Zencastr**
- Sender is Zencastr support, subject "Your Postproduction is complete". The body is a download button to an enterprise preview URL. **No episode or guest name anywhere.** The agent has to match on time (latest recording that finished before the mail).
- Transcripts reach guests as a .txt attachment named "<calendar event title>-transcript.txt", so the calendar title is the join key.
- Zencastr also sends product marketing and support threads (August had a transcription download error).

## Calendar patterns and prep-doc needs

**Calendars.** The thepodium.in calendar is the work calendar (Asia/Tokyo). The myunnati.com calendar is legacy: finance due-date reminders created by Jaya, webinar sign-ups, a couple of external meetings, and one unsolicited third-party "document signature" invite that looks like phishing. "Holidays in Japan" is subscribed. There is no separate prep calendar yet.

**Event types, 08-01 to 10-14 (237 events, 31 in the next 14 days)**

| Type | Count | Next 14 days | Title pattern | Guests attendees? | Link | Prep doc needed |
|---|---|---|---|---|---|---|
| Booking-page call | 71 | 6 | "<Name> and Akshay Datt (podm.in/ad)", 30 min (some 15) | Yes, external in 62 | Meet on all 71 | Precall: guest eval plus booking-form answers. BD: prospect research |
| Recording | 38 | 13 | FT: "FT Podcast Recording \| Name @ Company" (33). B2S: "Name @ Company on the B2S Podcast". HBD: "HBD Podcast \| Name @ Company". un#: "un# podcast >> Name @ Company" | Yes, guest and PR on all; Mamatha on 37 | Zencastr link in description (33), Riverside (3), Meet (1) | Host dossier for that show, precall notes, eval, guest prep note |
| Named precall | 3 | 1 | "FT Preliminary Call \| Name @ Company" (made by Mamatha when the guest will not self-book) | Yes | Meet | Guest eval |
| BD or client call | 13 | 0 | "Podcast for <Company>", "<Company> GTM", "<Partner> X Founder Thesis" | Yes, external in 11 | Meet | Prospect research (bd-eval), prior pitch page, notes history |
| Internal and 1:1 | about 15 | 0 | "FT Release Feedback Call" (weekly, 6), "B2S Review", "<Name> / Akshay", studio or video check | Team | Meet | Open queue items for that person, release pipeline |
| Busy and OOO blocks | 74 | 7 | "busy", "Out of office" | No | None | None |
| Personal and other | about 20 | 4 | Varied | Varies | Varies | None, keep off the dashboard |

**Booking-page details.** Booked through zcal. The description holds Organisation Name, Meeting Agenda, links to review, an optional attachment, and a reschedule link. Agenda splits: 44 say it is a preliminary call for the podcast, 18 are blank, 9 say "work" or "others". Team members also book through the same page, so "<Name> and Akshay Datt" does not always mean a guest. Classify by attendee domain first, agenda second.

**Recording details.** 120 minutes, mostly Tuesday to Friday (33 of 38). Guest and PR are attendees, the Zencastr joining link is in the description written by Mamatha.

**Prep load.** About 5 precalls and 4 recordings a week. Each precall needs the eval ready before the call. Each recording needs a dossier, which the skills produce per show (FT, B2S, HBD, un#). The match key is guest name plus company from the title; for booking-page events use attendee domain and the Organisation Name field.

## Where things drop

1. **Gemini notes go unread.** 18 of 27 sampled were never opened. Nearly half are untitled ad-hoc meetings that cannot be tied to a person by subject.
2. **Deferred decisions have no home.** Mamatha asks "do you want me to remind you? If yes, when?" and chases with "Any update on this? You said to wait" and "did this happen?". Akshay's deferrals ("in a couple of months") live only in thread text.
3. **Eval replies stall.** 8% get no visible reply; a quarter wait more than 33 hours. Akshay also had to tell Mamatha "don't forget to send me guest eval, even when I tell you or them directly", so evals get skipped when he decides on a call.
4. **Routing costs a round trip.** A pitch sent straight to Akshay waits about 20 hours for "adding @mamatha k to coordinate".
5. **Show-owner drift.** Ravi is no longer using his myunnati mailbox; un# evals cc'd there go nowhere ("ask Ravi on WhatsApp"). Chaandini was out of the loop on one outreach and Akshay had to correct it.
6. **Zencastr is a dead end in mail.** No episode name in the notice, transcripts downloaded by hand, one transcription-error support thread in August.
7. **Missing templates** for HBD and un# thank-you, and no reschedule template.
8. **Drive share requests** sit unanswered (4 of 4 in the sample), including one from the team.
9. **finance@ group mail** clutters the inbox: promos plus GST and payment notices that are 90% unread.
10. **Calendar hygiene.** A phishing-like invite on the legacy calendar, 18 booking-page events with no agenda, and "Problem with the notes" failures that leave calls with no record.

## Open questions

1. **Item grain.** One dashboard item per thread (updated on each new message) or per message? Per thread keeps it near 50 a day; per message roughly doubles it.
2. **Mamatha's cc threads.** Akshay reads 96% of them today. Does he want them auto-read and only logged, or a daily digest of her pipeline instead?
3. **Standing approvals.** Can the agent auto-route new PR pitches to Mamatha, and post a one-tap eval verdict in-thread, without per-item approval?
4. **un# ownership.** Who receives un# evals now that Ravi is off the myunnati mailbox?
5. **finance@ membership.** Should Akshay leave the finance@ group, or should a filter handle it?
6. **Prep calendar.** CLAUDE.md says agents add entries to Akshay's prep calendar. None exists. Create a secondary calendar, or use private events on the work calendar?
7. **Ad-hoc Meet calls.** Should calls always start from a calendar event so Gemini notes carry a name?
8. **Personal mail.** Exclude it from the dashboard entirely (current plan), or show a count only?
9. **Aliases.** Treat hello@, sp@, nk@ and rc@ as Noise by default, with a whitelist?
10. **Zencastr matching.** Is "latest finished recording before the notice" good enough, or should Sarika tag the episode when she triggers post-production?
