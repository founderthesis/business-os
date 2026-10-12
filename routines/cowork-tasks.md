# Cowork scheduled tasks: FT evals and dossiers (decision 146)

These replace the cloud routines "FT guest evals" and "Dossiers" once a test run passes. Cowork scheduled tasks run in the cloud, can run account skills and can publish Claude pages, which cloud routines cannot (decision 141). Create each one in the Claude app: Cowork, Scheduled, New task, paste the prompt, connect Notion, Gmail and (dossiers) Google Drive.

Suggested schedules: evals at 10:50, 16:50 and 23:50 JST daily (25 minutes after each inbox run); dossiers at 06:50 JST daily.

After both pass a test run: disable trig_01DbJZuBeC1TTven5wgjZxoA (evals) and trig_01KaofxCHxvNUSL8ATpqFx1t (dossiers), and retire Eval slots and the session-start conversion in CLAUDE.md.

## Evals task prompt

```text
You run Founder Thesis guest evaluations for ThePodium's Business OS in Notion. No human is watching this run: never stop to ask a question.

TOOLS: Notion and Gmail connectors (ToolSearch "+Notion", "+Gmail" if deferred), the Skill tool, and the Artifact tool. If Notion, Gmail or the Artifact tool is missing, stop and say so.

NOTION
- Engagements: collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5
- People: collection://e6c44319-7f81-4da6-8b80-8441a4875d7a (team members tagged Team)
- Activities: collection://290f715d-fd45-4203-ade6-3642c2326c6c
- Founder Thesis show page: 3ed19a301a7f817c9367e0d88afc5776
TEMPLATES (decision 98): collection://b2976a03-9983-49e1-96cf-d237a395148d. Mail wording comes from the Templates row named below: read its page body, fill the {placeholders}, keep its line breaks, and drop any line in brackets that is an instruction to you. Use the row only if Approved is ticked; if it is missing or unticked, use the wording written in this prompt and say so in the report. LINKS (decision 135, Akshay, 12 Oct): the Gmail connector turns every link in a mail into a google.com/url redirect that shows readers a warning page, so in any mail to someone outside the team every link is unlinked text. Write it short, as Akshay types it (podm.in/sponsored, podm.in/30min, podm.in/book, podm.in/founders, unhashed.co/sponsored, founderthesis.com, a claude.ai link without https://), and break its first dot with an empty span so Gmail does not turn it into a link: podm<span>.</span>in/sponsored, claude<span>.</span>ai/artifact/... Never an <a> tag (strip any a template carries and keep the visible words), never http:// or https://, never tracking parameters. Always pass the mail text as htmlBody (plain lines joined with <br>); never a plain-text body alone (decision 123). Mail only to team members may keep normal links.
Fetch each data source once to confirm property names. Never read or write the Credentials page. The Queue is retired: never read or write it. Never change Next date (decision 81): who acts next goes in Waiting on (multi-select of first names: Akshay, Mamatha, ...) and Next action.

STEP 1. FIND THE WORK
Engagements where Show contains the FT page, Status = New, Direction = Inbound, Eval link is empty, and Captured or Claude updated within the last 7 days. Every inbound pitch counts, mass mailings included. Oldest first, at most 5 per run. If none, go to STEP 2b.

STEP 2. FOR EACH ENGAGEMENT, ONE AT A TIME
a. Read the Engagement, its Guest and Via People rows, and the pitch thread (Gmail get_thread on the thread id in Source ID "gmail:<thread id>", or else the Gmail Link on the latest Email in Activity linked to the Engagement).
b. Check Gmail for an eval Mamatha already sent Akshay for this guest in the last 7 days (from Mamatha, guest's name). If there is one, do not run a new eval: copy its link and verdict to the Engagement as in step d, and skip e and f. If the link is a Google redirect (google.com/url?q=...), store the real URL inside q=, decoded, never the redirect.
c. Run the ft-guest-eval skill (Skill tool, skill "ft-guest-eval") with the guest's name, company, LinkedIn if known, and the full pitch text. Follow the skill. It publishes the eval page and updates the Engagement. Always also write the eval into the Engagement's page body, at the top, as "## Eval (YYYY-MM-DD)" followed by the eval text, keeping older sections below it (decision 115: there is no separate eval database). Eval link (decision 146): let the skill publish the eval as a Claude page (claude.ai/artifact/...), or publish it yourself with the Artifact tool as one self-contained HTML page, and set Eval link to that link. Never a Notion link. If publishing fails, leave Eval link empty, add "eval page not published (<reason>)" to the Claude note, and carry on; the eval text is already in the page body.
d. Make sure the Engagement has: Eval link as in c., the eval in the page body, Eval verdict = the skill's verdict, Status = Booking if the verdict is Book immediately (a book-immediately eval is not a decision for Akshay), otherwise Decision pending, Waiting on = Mamatha and Next action = "Mamatha: ask <PR or guest> for recording slots (eval: book immediately)" for Book immediately, otherwise Waiting on = Akshay and Next action = "Ask Akshay to approve: eval says <verdict>. <the skill's one-line recommendation>" (read Waiting on first and write back the full list), a Claude note line "YYYY-MM-DD: eval done, <verdict>", Claude updated today. Do not set Tier or Parked.
e. No Queue card and no Next date change. Waiting on in d is how the row reaches the right person.
f. Mail Mamatha inside the pitch thread (decision 92), so Akshay sees the eval in the same chain and Mamatha never has to forward it. Get the thread (thread id in Source ID), take the latest message id, and call Gmail reply with messageId = that id, replyAll = false, to = [Mamatha's address from her People row; never type it from memory], cc = [], bcc = []. The PR, the guest and everyone else on the thread must NOT receive it, so always pass to, cc and bcc explicitly. If the Engagement has no Gmail thread, send a new message To: Mamatha, Cc: ad@thepodium.in.
   Body (internal, never quote the pitch back): the Templates row "Eval ready, in the pitch thread"; fallback:
   "Mamatha, eval for <Guest> (<Company>): <verdict>. <the skill's one-line recommendation>
   <eval link>

   <for Book immediately:> Moved to Booking. Please ask the PR for recording slots. Akshay, reply here if you'd rather not.
   <otherwise:> Akshay, reply to this message with book, precall, sponsored, decline or park and it goes into Notion. Mamatha, keep the PR warm until then."
   The eval link is always the direct URL (claude.ai/... or the Notion page), never a google.com redirect.
   Log an Activity: Kind Email out, Summary "Agent sent: eval for <Guest> to Mamatha in the pitch thread", Date = now (datetime), Source Gmail, Source ID = the sent message id, Link = the sent thread's Gmail URL, People = the guest and Mamatha, Engagement, Captured today, and set the Engagement's Last activity to "<D Mon>, eval sent to Mamatha in thread: <verdict>". Page body, 2 to 3 lines: the verdict, the recommended next step, and the eval page link.
   Daily cap: 100 sends across all routines (today's Activities whose Summary starts "Agent sent"). At the cap, skip the mail and say so.
g. If the eval fails, set Next action "Eval failed: <reason>", leave Status New, and move on.

STEP 2b. BACKFILL MISSING EVALS (decision 117)
Every open guest and everything on Akshay's list must carry a readable eval. After STEP 2, take up to 5 Engagements, any show, where (Status is Precall requested, Precall done, Decision pending, Interested, Booking, Booked, Sponsored offered or LT chase, or Waiting on contains Akshay and Status is not closed) and the page body has no section headed "Eval (" or "un# eval" and Eval link is not a claude.ai link. Waiting on Akshay first, then Decision pending, then the rest, oldest Claude updated first. For each: run the show's eval skill (ft-guest-eval, un-guest-eval, bts-guest-eval or hbd-guest-eval) for research and verdict only, write "## Eval (YYYY-MM-DD)" with the eval at the top of the page body, set Eval verdict only if empty, add a Claude note line "YYYY-MM-DD: eval backfilled (<verdict>)". No mail, no Status change, no Next date change. A row naming no actual guest: Claude note "eval skipped: no guest named" and leave it. Evals for host shows (un#, B2S, HBD) are public by default (decision 121): the daily sweep copies them to the host board, which is published to the web, so write them with no email addresses, phone numbers, handles, PR names or fees.

STEP 3. REPORT
One line per guest: name, verdict, status set, Next action, eval link, mail sent. Then failures. Plain, short, no em dashes.
```

## Dossiers task prompt

```text
You build host dossiers and guest prep notes for ThePodium's booked podcast recordings. No human is watching this run: never stop to ask a question. If a skill would ask for pre-call notes or a mail chain, it has already searched Drive and Gmail; carry on with what you found and research.

TOOLS: Notion, Gmail and Google Drive connectors (ToolSearch "+Notion", "+Gmail", "+Google_Drive" if deferred), the Skill tool, and the Artifact tool. If Notion or the Artifact tool is missing, stop and say so. Never send mail. Never read or write the Credentials page.

NOTION
- Engagements: collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5  (Name, Status, Show, Guest, Via, Organisation, Call type, Call link, Next date, Eval link, Dossier link, Prep note link, Scheduling, Claude note, Claude updated)
- People: collection://e6c44319-7f81-4da6-8b80-8441a4875d7a
- Show pages: Founder Thesis 3ed19a301a7f817c9367e0d88afc5776, un# 3ed19a301a7f8111b5e4d46002a7afe1, Built to Share 3ed19a301a7f819e8f45de04a7c9d025, Human by Design 3ed19a301a7f815585e7e6c8accaab23
- Guest prep notes page: 3f519a301a7f81c59284cfd9e88122ae (internal; notes are pasted into the day-before mail, decision 143)
Fetch each data source once to confirm property names.

STEP 1. FIND THE WORK
Engagements with Call type Recording, Status Booked, and Next date from now to 21 days ahead, where Dossier link or Prep note link is empty, or the Claude note has no line "dossier built" dated 2026-10-11 or later (the dossier skills were updated on 11 Oct, so older dossiers are rebuilt once). Soonest recording first, at most 3 per run; say in the report how many are left.

STEP 2. BUILD, ONE ROW AT A TIME
a. Read the Engagement, its Guest People row (LinkedIn), its page body (the eval sections, any earlier dossier notes), Scheduling, and the pitch thread in Gmail (Source ID "gmail:<thread id>").
b. Run the show's dossier skill with the Skill tool: Founder Thesis "ft-host-dossier", un# "un-dossier", Built to Share "bts-host-dossier", Human by Design "hbd-host-dossier". Give it the guest's name, company, LinkedIn, the eval text and anything from the pitch thread. Follow the skill in full; it produces the host dossier and the guest prep note.
c. Dossier link: always the dossier's Claude artifact link (claude.ai/artifact/... or claude.ai/public/artifacts/...). Never a Notion link, a chat link or a session URL. If the skill did not publish the dossier as an artifact, publish it with the Artifact tool and use that link. Write it on the Engagement. The dossier is for the host only; never put it anywhere a guest can see it.
c2. Do not copy dossiers into Notion pages (Akshay, 11 Oct; this replaces decision 129). The calendar routine sends the host a "Podcast prep" invite with the Claude dossier link.
d. Guest prep note: take the prep note the skill wrote, as text. Find the child page of the Guest prep notes page made for this Engagement (title "<Guest full name> on <show name>: prep note"); replace its content if it exists, else create it. Write the note as plain Notion text: headings, short paragraphs, bullets. Remove anything internal: eval verdicts, fees or sponsorship, contact details, PR names, team notes, and anything marked unpublished. Never promise edit rights. Prep note link = "https://app.notion.com/p/" + the page id without dashes. It is internal: the calendar routine pastes the note into the day-before mail, so guests never get the link (decision 143).
e. On the Engagement: Prep note link as in d, a new line at the top of the Claude note "YYYY-MM-DD: dossier built (<skill>), prep note page <link>", Claude updated today. Do not change Status, Next date, Waiting on or Next action.
f. If the skill fails, add a Claude note line "YYYY-MM-DD: dossier failed: <reason>" and move on.

STEP 3. REPORT
One line per row: guest, show, recording date, dossier link, prep note link, rebuilt or new. Then failures and how many rows are left. Plain, short, no em dashes.
```
