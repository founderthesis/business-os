# People knowledge audit

Read-only audit, run 30 Sep 2026. Goal: find where per-person knowledge already lives so the new Notion People database can carry Location, Blurb and Research history (guest evals, dossiers, prep notes, BD evals). Nothing was edited in Slack, Gmail, Drive, Notion, Blue or Apollo. No Apollo credits were spent.

Privacy: this file holds counts, formats and anonymised descriptions only. No guest names, email addresses, phone numbers or eval text.

Related audits already in Notion (Business OS): Sheets audit, Blue audit, Notion audit, Inbox audit. This file does not repeat their field maps; it adds the per-person research layer.

## Summary

- **Blurbs are small and clean.** Slack #ft-blurbs holds 35 community blurbs for 26 distinct FT guests (10 May to 18 Sep 2026). 25 of 26 carry the guest's LinkedIn URL inline, so they match People by LinkedIn slug with no human help.
- **A second blurb type exists:** about 21 short "prospect blurbs" (Name @ Company, LinkedIn, Blurb) posted to hosts in Slack DMs and show channels for HBD and un#, May to Sep 2026. All but one carry a LinkedIn URL.
- **Guest evals are the biggest research asset.** 524 Gmail threads in the last 12 months mention "guest eval". About 325 link to claude.ai, about 177 to Perplexity, 6 to both, and about 16 to neither (Google Docs, ChatGPT shares, or inline LinkedIn plus text). Rough estimate: 350 to 500 distinct people.
- **The tool shifted over the year:** ChatGPT shares and Google Docs (Oct to Nov 2025), Perplexity (Nov 2025 to Apr 2026), public claude.ai artifacts (Apr to Sep 2026), private claude.ai/artifact links (from mid Sep 2026).
- **Evals are machine-readable going forward.** The Artifact tool read one private eval link as raw HTML with stable sections: verdict banner, name, a role line of the form "Title, Company (City)", two 1-10 scorecards, and a Links section that includes the guest's LinkedIn URL. Perplexity, ChatGPT and claude.ai/chat links are not readable by our tools.
- **Dossiers and prep notes are scattered:** about 82 Gmail threads mention "dossier", about 50 dossier-titled Drive files (roughly 27 distinct guests, many versions), about 50 Gmail threads since Jun 2026 carry guest prep note links, plus Gemini call notes forwarded with "make dossier" instructions (50 in the last six weeks alone).
- **Location is almost nowhere at person level.** Members Master List (682 people), Blue and the FT and un# pipeline sheets have no location field. Location exists only in a handful of prospect shortlists (Country or City columns), the B2S Notion lists (Country), and inside eval artifacts (city in the role line).
- **Apollo is available but unused:** 0 saved contacts, 180 lead credits per monthly cycle, 0 consumed this cycle (15 Sep to 15 Oct). A person match returns city, state and country. At that allowance, locating all 682 Members takes about 4 cycles unless more credits are bought.

## Where blurbs live

### 1. FT community blurbs (founder-thesis-blurb skill)

| Item | Finding |
|---|---|
| Source | Slack public channel #ft-blurbs, created 10 May 2026. Only Akshay posts; every message ends "Sent using Claude" |
| Count | 35 messages, 26 distinct people |
| Duplicates | 9 extra drafts for 3 people, all posted 13 May 2026 (iterations of the same blurb, 2 to 5 per person). Newest message per person should win |
| Date range | 10 May 2026 to 18 Sep 2026 |
| Format | One paragraph, about 100 to 250 words. Opens with "Full Name (LinkedIn URL - @{WhatsApp handle}) is the <role> of <Company>". The WhatsApp handle placeholder is never filled |
| Names person and company | Yes in every message, in the first sentence |
| LinkedIn URL | 25 of 26 people. 2 messages use a "{LinkedIn URL}" placeholder; one of those people has a later message with the real URL, the other (a VC) has none |
| Matchability | Automatic. Parse the first URL, normalise (strip in./www., trailing slash, query string), match People.LinkedIn. Fallback: first-sentence name plus company |
| Not found elsewhere | No copies in DMs or other channels. Blurbs written before 10 May 2026 are not in Slack; older ones went straight to WhatsApp |

Members Master List has LinkedIn on 631 of 682 rows (93%), so almost every blurb should land on an existing person.

### 2. Prospect blurbs sent to hosts

| Item | Finding |
|---|---|
| Source | Slack DM with Arjun (HBD), DM with Sri (un#), #unhashed_podcast (private), #founders-inperson-podcast (shared with Fast Code AI) |
| Count | About 21 distinct people: 12 in the Arjun DM, 5 in the Sri DM, 4 in #unhashed_podcast, 1 in #founders-inperson-podcast. Found by keyword search, so a few may be missed |
| Date range | 7 May 2026 to 29 Sep 2026 |
| Format | "Name @ Company" header, then "LinkedIn:" or "LI:" URL, sometimes Google Scholar or faculty page, then "Blurb:" one to three sentences. un# ones lead with TVL, funding and revenue numbers |
| Matchability | Automatic for about 20 of 21 via LinkedIn URL. One un# message has no name line or URL and needs a human |

### 3. Blurb-like columns in sheets and Notion

These are pitch lines, not community intros, but they are the only one-liners for most prospects.

| Source | Column | Rough filled rows |
|---|---|---|
| un# Pipeline sheet, Pipeline v2 | short pitch | about 149 of 193 |
| un# Pipeline sheet, YAP Clients | Blurb | about 32 of 34 |
| FT Pipeline sheet, PAAS - FT | Blurb | about 56 of 93 |
| FT Pipeline sheet, PAAS - Direct | Blurb | about 186 of 1,434 (BD prospect one-liners) |
| HK/SG Guest - Un# sheet | Short Guest Blurb | small list, with LinkedIn URLs |
| BTS_Guest_Shortlist_46, Next_Horizon shortlists | 1-Line Blurb, Blurb - why now | about 46 and about 40 |
| Notion Members Master List | What they do | 682 of 682, one line each |
| Notion WhatsApp Group Members (public copy) | one line per person | 505 |

Only un# CRM and un# Old Pipeline hold real LinkedIn URLs among the sheets (73 total). Everything else keys on "Name @ Company" text, so matching needs name normalisation.

## Where evals, dossiers and prep notes live

### Guest evals (Gmail)

Method: Gmail search "guest eval" after 30 Sep 2025, all pages saved and parsed; link type split by two further searches (perplexity, claude.ai); three threads without a preview hit opened to confirm they hold an eval.

| Item | Finding |
|---|---|
| Threads, last 12 months | 524 |
| By month (first message) | Oct 4, Nov 13, Dec 5, Jan 21, Feb 31, Mar 40, Apr 43, May 39, Jun 30, Jul 93, Aug 75, Sep 130 |
| Senders of eval lines | Mamatha about 72%, Akshay forwarding to hosts or team about 28% (sample of 199 parsed lines) |
| Standard line | "PFB guest eval for <Name> @ <Company>: <link> - Recommendation: <verdict>" |
| Verdicts seen | Book Immediately, Strong Consider, Evaluate after call, Decline (plus the skill's Pre-call needed inside artifacts) |
| Link type (threads) | claude.ai about 325, Perplexity about 177, both 6, neither about 16 |
| Link type by era (first eval per person, parsed sample of 154) | Oct 2025: ChatGPT share and Google Doc. Nov 2025 to Apr 2026: Perplexity. Apr to Sep 2026: public claude.ai artifacts. Sep 2026: 34 private claude.ai/artifact links. Jul to Sep 2026: about 14 un# batches pasted inline as LinkedIn URL plus text |
| Distinct people | 154 in the 199 parsed eval lines. Scaled to all threads, roughly 350 to 500 |
| Other shows | A minority of threads are HBD, un# and B2S evals routed to other team members |

Where evals are also referenced:
- FT Pipeline sheet: Inbound "Dossier/ guest eval" (68% of 661) and P1 "Verdict" (81% of 208). Mostly verdict labels and eval doc titles; the Sheets audit counts 202 doc titles and 81 URLs across all verdict columns. Titles follow "Guest Eval: Name - Company".
- un# Pipeline sheet: Guest Eval (78%), Guest Eval 2 (18%, doc titles and claude.ai links), YAP Guest eval (33 Perplexity URLs).
- Notion inbox triage databases (10 Sep and 28 Sep 2026): a "Guest eval" URL per pitch row.
- Drive: only 2 eval files (one un# eval as Google Doc plus RTF, Aug 2025).

Machine-readability test: one private claude.ai/artifact eval link (Sep 2026) was read with the Artifact tool. It came back as raw HTML owned by the user's account. Structure: verdict banner, h1 name, a role line "Title, Company (City)", Audience Fit and Sales Fit scores, business summary, career timeline, key facts, themes, watch-outs, links (LinkedIn first). So verdict, scores, LinkedIn URL and city are parseable. Not tested: public claude.ai/public/artifacts links (the read action documents only claude.ai/artifact and claude.ai/code/artifact URLs). Perplexity threads, ChatGPT shares and claude.ai/chat links are not reachable by our tools.

### Dossiers

| Source | Count and format |
|---|---|
| Gmail | About 82 threads mention "dossier" in 12 months. Many are Gemini notes forwarded to Mamatha with "make dossier". Replies carry Google Doc links (Oct 2025 to Feb 2026), then claude.ai/chat links (Aug to Sep 2026) |
| Drive | About 50 dossier-titled files, roughly 27 distinct guests. One HBD guest has 9 versions. Naming drifts: "Dossier - Name @ Company", "Guest Dossier: Name @ Company", "Name: Company Dossier", "<Surname>_HBD_Dossier", "un-dossier-<surname>", "un-dossier-<surname>-guest-prep.md", "HOST DOSSIER: NAME". Owners split between Akshay's and Mamatha's Drives. A few are prompt docs, not dossiers |
| Slack | Dossier links in #unhashed_podcast, #founders-inperson-podcast and the Arjun DM: Google Docs, public and private claude.ai artifacts. #assistant holds lists of "Name @ Company - claude.ai/chat" links used for dossiers and blurbs (not machine-readable) |
| Blue | Dossier URL field on FT, un#, Hissa and FastCode records. Blue audit notes several point at private claude.ai chats |

### Prep notes

- Gmail: about 50 threads from Jun to Sep 2026 match "prep note", "guest note" or "guest prep" (33 in Sep). Mamatha or Chaandini send "guest prep note" links to the guest's PR contact, mostly private claude.ai/artifact links since Sep 2026. Thread subject usually names the guest and company.
- Drive: 2 un# guest-prep markdown files.
- Notion: Guest note and Pitch note pages under Podcast-as-a-Service Leads (14 leads).

### Call notes and transcripts (supporting research)

- Gemini meeting notes: 50 notes in the last six weeks. Titles name the guest when the booking came through the podm.in link ("<Name> and Akshay Datt (podm.in/ad)" or "Preliminary call | <Name> @ <Company>"); others are generic "Meeting <date>" and need a calendar lookup.
- Drive "Zencastr Transcripts" folder: 100+ per-guest subfolders named "<First name> - <Company>" (first page only; likely several hundred). A separate "transcripts" folder holds dated markdown plus JSON with an index.jsonl.
- Notion Members Master List: Transcript Link on about 514 rows. Blue: transcript file fields on FT and un# records.

### BD evals

- The bd-eval skill is chat-only, so its output is not stored anywhere searchable.
- Proxies: FT Pipeline PAAS tabs (Blurb columns above), PAAS_Leads sheet (priority, budget read, pitch angle per lead), Notion Podcast-as-a-Service Leads (14 rows, Pitch note and Guest note links), Notion US VC Podcast Outreach (774 firms with Fit Rank and Budget Read; contacts flattened into Contact 1 to 3).
- Artifact evals score Sales Fit, so every FT eval is also a light BD eval.

## Location data available today

| Source | Field | Level | Rough coverage |
|---|---|---|---|
| claude.ai eval artifacts | "(City)" at the end of the role line | Person | Every eval since Apr 2026 if the template held (1 sample checked) |
| Notion B2S guest list and archive | Country (48 options) | Person or company, mixed | 90 live, 492 archive |
| BTS_Guest_Shortlist_46 | Country | Person | 46 |
| BuiltToShare_Guest_Shortlist_Aug2026 | Country (HQ) | Company | about 100 |
| Playbooks_by_Prath longlists v3 to v6, Playbooks Guestlist v5 | City | Person | a few dozen per version |
| Next_Horizon shortlists v2, v4 | Based, HQ | Person, company | about 40 |
| HK/SG Guest - Un# | Location | Person | small list |
| un# Old Pipeline | comments (mostly "Based in X") | Person | 24 |
| Tracxn exports (several) | Country, State, City | Company HQ only | thousands of companies |
| Members Master List, Blue, FT and un# pipelines, HBD Guest Outreach | none | | 0 |
| Apollo | person city, state, country on match | Person | 0 saved contacts today |

Apollo cost: 180 lead credits per cycle, 0 used; a people match typically costs 1 lead credit per matched person (confirm on a paid test of 1). 682 Members would need about 4 cycles at current allowance. The free people search endpoint was not tried; whether it returns location without spending credits is unverified.

Weak proxy: phone country code in Members (88% filled) gives country only. Use as a fallback, not a value.

LinkedIn: no LinkedIn data export of guest profiles was found. A LinkedIn connections export of Arjun's network was shared in #founders-inperson-podcast; standard connection exports do not include location.

## How to backfill People

Match key order: normalised LinkedIn slug, then email (Members has none yet), then normalised "Name @ Company".

| Field | Source | Automatic | Needs a human | Rough count |
|---|---|---|---|---|
| Blurb (community) | #ft-blurbs, newest per person | 25 | 1 (no URL) | 26 |
| Blurb (prospect) | Slack host DMs and channels | about 20 | about 1 | about 21 |
| Blurb (pitch line) | Sheet blurb columns, Members "What they do" | name match covers most; LinkedIn only on 73 sheet rows | ambiguous names, multi-person cells | several hundred |
| Research: evals | Gmail eval lines (link, verdict, date) | about 470 threads with a parseable line (name @ company + link) | about 50 threads with batches, inline lists or odd formats | 350 to 500 people |
| Research: eval content | Private and public claude.ai artifacts | readable via Artifact tool (private tested) | Perplexity and ChatGPT era evals stay as links only | about 325 claude.ai threads |
| Research: dossiers | Drive titles, Gmail replies, Blue Dossier field | titles with "Name @ Company" | surname-only titles (un#, HBD), version picking | about 27 Drive guests plus Gmail and Blue |
| Research: prep notes | Gmail threads since Jun 2026 | subject names the guest | threads about several guests | about 50 |
| Research: call notes | Gemini notes | titled notes | generic "Meeting <date>" titles | 50+ in six weeks |
| Location | Eval artifact role line | yes, for people with a claude.ai eval | verify parser on 10 samples first | up to about 300 |
| Location | Shortlist Country and City columns | name match | company-HQ vs person ambiguity | about 150 to 250 |
| Location | Apollo match by LinkedIn URL | yes | review low-confidence matches | 180 per month |

Suggested order: (1) blurbs from Slack by LinkedIn slug; (2) Gmail eval index (person, company, link, verdict, date) into a Research relation; (3) read private artifacts for LinkedIn URL and city; (4) shortlist Country and City; (5) Apollo for FT guests still missing a location, 180 per month.

## Open questions

1. Should People hold one Blurb (the community blurb) and keep pitch lines in a separate field, or merge them?
2. Is the city in the eval role line the person's base or the company's HQ? The skill template should say which.
3. Can public claude.ai/public/artifacts links be read with the Artifact tool, or do they need re-publishing as private artifacts? Test one before planning around them.
4. Perplexity-era evals (about 177 threads): keep as links only, or re-run evals for people who are still active prospects?
5. Should Research be a separate Notion table (one row per eval, dossier or note, related to People) rather than text on the person row?
6. Buy more Apollo credits for a one-time location backfill, or trickle 180 a month?
7. Should blurbs written before May 2026 (WhatsApp only) be recovered from the WhatsApp group export?
8. Several dossier and prep links point at claude.ai/chat conversations. Should the team switch to artifacts so they stay readable?
</content>
</invoke>
