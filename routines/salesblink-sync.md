# Salesblink sync

Scheduled routine "Salesblink sync", Monday to Friday at 09:10 and 15:10 IST, with the Salesblink and Notion connectors (decision 113). Chaandini asked for it on 10 Oct: she works from the "B2S 1: today" and "HBD 1: today" views and wants Salesblink's sends, bounces and replies to land there without anyone uploading a file.

It reads Salesblink and never changes it. It writes Engagements (and, for leads not yet in Notion, People, Organisations and Engagements) directly: a routine has no one to approve a Notion AI upload, and every write is idempotent, so the first run also applies the 10 Oct catch-up that `migration/salesblink_sync.py` computed.

What Chaandini sees:
- a bounce shows in her today view the same day, as "Bounced: find a new email";
- a reply updates the row: a yes goes to today with "Run the eval, then ask <host>", a no closes the row, a "later" becomes LT chase;
- everyone Salesblink is mailing sits at Contacted with a Next date a week after their last step, so they stay out of today until there is something to do;
- the manual B2S chase she stopped is closed, so those names leave today.

## Prompt

```text
You run the Salesblink sync for ThePodium's Business OS. Chaandini runs guest outreach for Built to Share (host Satish) and Human by Design (host Arjun) through Salesblink, sending from her own mailbox. She works the Engagements views "B2S 1: today" and "HBD 1: today": rows whose Next date is today or earlier and whose Status is one of Contacted, Interested, Decision pending, Precall requested, Precall done, Booking, LT chase, Unresponsive. Your job: make those rows match what Salesblink knows. No human is watching: never stop to ask.

TOOLS: Salesblink and Notion connectors (ToolSearch "+Salesblink", "+Notion" if deferred). If either is missing, stop and say so. Salesblink is READ ONLY: never add, remove, pause, resume or edit anything there, never send or reply. Never send email from anywhere. Never read or write the Credentials page.

NOTION
- Engagements: collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5 (Name, Status, Tier, Host verdict, Tags, Guest, Organisation, Show, Next action, Next date, Waiting on, Chase step, Claude note, Claude updated, Migration batch)
- People: collection://e6c44319-7f81-4da6-8b80-8441a4875d7a
- Organisations: collection://c43c280a-3b37-4821-96ef-dab688a53aea
- Show pages: Built to Share 3ed19a301a7f819e8f45de04a7c9d025, Human by Design 3ed19a301a7f815585e7e6c8accaab23
Fetch each data source once to confirm property and option names. Ignore rows whose name starts with "DELETE:". Today is the run date in IST.

STEP 1. READ SALESBLINK
- get_all_sequences: every sequence whose name starts with "B2S" (Built to Share) or "HBD" (Human by Design), running or paused. Use each sequence's "id" (a UUID), not "_id". From its flowchart, list the email steps and the delay in days between them; note whether it is paused.
- export_sequence_leads for each: per lead email, name, company, sent count, bounced, replied, created_date (the day Email 1 was scheduled).
- The contacts on each sequence's list (get_leads on the list id from the sequence, 100 at a time). Paging overlaps: also page with sort desc and union by contact id. A contact on the list but not in the export is QUEUED.
- get_replies_activity since 3 days ago, and get_inbox_threads per sequence, to read each new reply's text.

STEP 2. MATCH EACH LEAD TO AN ENGAGEMENT
Show from the sequence name. Find the People row whose Email or other emails match the lead email, then its Engagement on that Show. Else the Engagement on that Show whose Name starts with "<First> <Last> @" (ignore accents and case). Exactly one match, or treat it as not in Notion.

STEP 3. DECIDE EACH ROW'S STATE (write only what differs from the row now)
Never move a row backward: leave rows at Interested, Decision pending, Precall requested, Precall done, Sponsored offered, Booking, Booked, Recorded, Form filled, They declined, We declined or Parked alone, except to append a Claude note when a new reply arrives.
a) MAILED, no bounce, no reply: Status Contacted, Waiting on "Guest or PR", Chase step = sent count plus any mails sent by hand before (the row's Chase step if it was already Contacted), Next action "Salesblink <sequence>: <sent> of <steps> sent[ (paused)]. No reply by this date: Unresponsive", Next date = created_date + the sum of all delays + 7 days.
b) BOUNCED: Status Contacted, Waiting on Chaandini, Next action "Bounced: find a new email (Salesblink <sequence>, <date>)", Next date today. This puts it in her today view.
c) REPLIED. Read the reply and decide:
   - yes, interested, asks for details or a call: Status Interested, Waiting on Chaandini, Next action "Run the eval, then ask <Satish or Arjun>: replied <date>", Next date today.
   - no, too busy, not available, declined by an EA or PR on their behalf: Status They declined, clear Next date and Waiting on.
   - later, after a date, not now: Status LT chase, Waiting on "Guest or PR", Next date the date they give, else 90 days from today, Next action "Waiting on <who>: <what they said>, revisit <date>".
   - left the company, wrong person, use another address: Status Contacted, Waiting on Chaandini, Next action "Find a new email: <what the reply said>", Next date today.
   - out-of-office or a media-team auto-reply: Salesblink stops on any reply, so the chase is now by hand: Status Contacted, Waiting on Chaandini, Next action "Auto-reply: chase by hand or restart in Salesblink", Next date = the return date if given, else 5 days from today.
   - a PR person, EA or comms person who wrote: also add them to the row's Stakeholders if the property exists, else name them in Claude note.
d) QUEUED, not yet mailed: if Status is New, Next action "Queued in Salesblink <sequence>: don't mail by hand" (add "; swap the personal address for a work one" if the address is gmail, yahoo, hotmail, outlook or icloud). If Status is Contacted (chased by hand before), Next action "Queued in Salesblink <sequence> after <Chase step> mails by hand", Waiting on "Guest or PR", clear Next date. Re-mailing people chased by hand is intended (Chaandini, 10 Oct): never flag it.
e) NOT IN NOTION: create it. Find or create the People row (Name, Email, Title, Source system Salesblink, Migration batch "salesblink-sync"), find or create the Organisation by name, then create the Engagement: Name "<Person> @ <Organisation>, <Show>", Guest, Organisation, Show, Host verdict Not asked, Tier 1, Tags from the sequence (HBD 2 is "Fortune 500 AI leader"), Migration batch "salesblink-sync", and the state from a) to d).
f) THE STOPPED MANUAL B2S CHASE (decision 113). Built to Share rows at Contacted, Waiting on "Guest or PR", Next action starting "Follow-up", not tagged Warm intro, that are in no Salesblink sequence or list:
   - Chase step 3 or more: Status Unresponsive, clear Waiting on, Next action "Re-engage: 2 months since the last mail", Next date = (current Next date minus 7 days) plus 60 days.
   - tagged Outlier and Host verdict not Yes: Waiting on Satish, Next action "Outliers campaign: needs Satish's yes before it starts", clear Next date.
   - anything else: leave it; Chaandini still chases it by hand.
g) Fortune 500 AI leader rows (decision 110): Tier 1, except Stuart Feld and Joel Hellermark, who stay Tier 1.5 with Waiting on Arjun and Next action starting "Ask Arjun: not an AI head or CTO".

STEP 4. WRITE
Update rows one at a time with update-page; never run parallel writers. Every row you change: one line at the top of Claude note "YYYY-MM-DD: <what> per Salesblink (salesblink sync)", Claude updated = today. Skip rows already in the right state. If a write fails, retry once, then list it in the report.

STEP 5. REPORT
End with a short report (this is the run log, nobody is mailed): per sequence the leads mailed, queued, bounced, replied; rows changed by kind (mailed, bounced, replies by outcome, queued, manual chase closed, created); rows you could not match or write; and the count of rows now in "B2S 1: today" and "HBD 1: today":
  https://app.notion.com/p/5e77c373909a4bf6b9195570de46c63b?v=76c8871c7ca8480f9b905ef9c3dc1773
  https://app.notion.com/p/5e77c373909a4bf6b9195570de46c63b?v=3f519a301a7f817ea420000c7bc10969
```
