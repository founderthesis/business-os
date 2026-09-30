# Spreadsheet audit: guest and pipeline sheets

Audit date: 2026-09-30. Read-only. Input to the Notion Business OS migration.
Reproduce with `python migration/profile_sheets.py data/raw --json stats.json --as-of 2026-09-30`
(raw exports live outside git; `--private-dir` writes person-level CSVs that must never be committed).

Sources audited:

| # | Source | Kind | Owner | Last modified |
|---|---|---|---|---|
| 1 | B2S_Guest_list.xlsx (7 tabs) | Uploaded xlsx (generated file, no owner metadata) | AD account holds earlier Drive versions | copies on Drive dated 2026-07-13 |
| 2 | HBD_new.xlsx (3 tabs) | Uploaded xlsx (generated file) | AD account holds an earlier "HBD_Guest_Pipeline_Enriched_v1" | Drive predecessor 2026-08-20 |
| 3 | FT Pipeline (10 tabs) | Google Sheet | Mamatha | 2026-09-30 (edited today) |
| 4 | un# Pipeline (10 tabs) | Google Sheet | Akshay | 2026-09-30 (edited today) |

## Summary

- **30 tabs, 4,061 non-empty data rows, 4,030 named rows** (3,970 guest or prospect rows plus 60 podcast-host rows in un# "Podcast Leads" and "pod Campaign"; FT "Sheet2" is a chase-cadence template, not data).
- **About 3,450 to 3,490 unique people** behind 4,025 person mentions: matching on email removes 258, LinkedIn a further 73, normalised name plus company a further 206. Name-only matching would remove 53 more, but some of those are common-name false positives.
- **Tabs are used as pipeline stages.** Rows are copied forward (Inbound to P1, N2 to N3, Pipeline v2 to CRM) and the old row is never closed: 471 people sit in 2+ tabs and 99 of them carry contradictory statuses. The four shows barely overlap (only 9 people appear in more than one workbook).
- **Identity keys are thin.** 56% of mentions carry a LinkedIn URL (almost always hidden as a hyperlink behind the name text, so CSV export loses it), 45% carry an email, 24% carry neither.
- **74 distinct status strings** across 17 status columns mix five different concepts: pipeline stage, outcome, host decision, commercial deal type and chase step. Plus 9 verification flags and 13 contact-plan values that are not statuses at all.
- **Decisions live in the wrong columns**: host verdicts in follow-up date cells ("Arjun rejected"), eval verdicts as hyperlink display text (in FT P1, 91% of verdict cells show only a document title), payment milestones as 7 checkboxes, PR contacts in "Via".
- **Follow-ups are 3,086 date cells in 1 to 6 columns per tab**, 449 of them dated in the future (planned, not sent), plus 53 free-text cells ("check later", "Next yr (2027)", "Arjun rejected", dates typed as text).
- **PR contacts are a real entity**: 546 distinct names in Via / PR Contact, 154 recur 2+ times (covering 460 rows), 20 recur 5+ times, 76 appear in both FT and un# tabs.

## Inventory

Rows = non-empty data rows below the real header. Header = row number of the real header.

| Source | Tab | Rows | Named | Header | Name format | Status col | FU cols |
|---|---|---|---|---|---|---|---|
| B2S | India | 46 | 45 | 1 | Name @ Company (+LinkedIn link) | Status 39% | 6 |
| B2S | Global known in India | 21 | 21 | 2 | Name @ Company | Status 90% | 5 |
| B2S | NEW | 49 | 49 | 1 | Name @ Company, header "Column 1" | Status 8% | 5 |
| B2S | N2 | 291 | 291 | 1 | Split Name / Company | S (flags) 100%, Status 0.3% | 5 |
| B2S | N3 (6) | 294 | 294 | 3 | Name@Company (no spaces) | Status 20% | 5 |
| B2S | Outliers | 33 | 33 | 1 | Split Name / Company | none | 5 |
| B2S | Global p3 | 40 | 40 | 2 | Split (header says "Founder / Company") | Status 0% | 0 |
| HBD | Sheet1 | 34 | 34 | 2 | Split Name / Company (domain in brackets) | Status 24% | 4 |
| HBD | V2 | 28 | 28 | 1 | Name only, affiliation in unlabelled col | Status 25% | 4 |
| HBD | V3 | 48 | 48 | 2 | Name @ Company, 2 unlabelled cols | Status 10% | 4 |
| FT | Paid | 12 | 12 | 1 | Split Guest / Co Name | 7 checkbox milestones | 1 |
| FT | Inbound | 661 | 659 | 1 | Name @ Company, 46 free-text "Name, Title, Co" | Status 100% | 1 |
| FT | P1 | 208 | 208 | 1 | LinkedIn page title "Name - Co \| LinkedIn" (131) | Status 100% | 1 |
| FT | PAAS - FT | 93 | 93 | 1 | Name @ Company | Status 83% | 2 |
| FT | PAAS - Direct | 1,434 | 1,434 | 1 | Name @ Company | Status 6% | 6 |
| FT | PAAS new | 104 | 104 | 1 | Name @ Company | Status 1% | 4 |
| FT | VC Intros | 41 | 34 | 1 | Name - Fund | Status 63% | 1 (empty) |
| FT | Sheet2 | 14 | 0 | n/a | Cadence template | n/a | n/a |
| FT | FT Cold Lead | 154 | 154 | 1 | Split First / Last | two "Status" columns | 0 |
| FT | Post Release | 9 | 9 | 1 | Name only | none | 0 |
| un# | Pipeline v2 | 191 | 191 | 1 | Name @ Co or LinkedIn title, header "Linkedin Link" | Status 100% | 1 |
| un# | Sponsored | 18 | 18 | 2 | Name @ Company | Status 100% | 1 |
| un# | Post Release | 3 | 3 | 1 | Name only | none | 0 |
| un# | Podcast Leads | 56 | 40 | 1 | Podcast + Host Name (not guests) | Contact Status 46% | 2 (text) |
| un# | pod Campaign | 20 | 20 | 1 | Podcast + split First / Last | none | 0 |
| un# | YAP Clients | 34 | 34 | 1 | Name @ Company | Recommendation 100% | 0 |
| un# | Theprgenius Client | 14 | 14 | 1 | Name @ Co; 2nd sub-table at row 17 | Guest eval 79% | 0 |
| un# | Old Pipeline | 23 | 23 | 1 | Split; 2nd sub-table at row 28 | Status 96% | 0 |
| un# | CRM | 49 | 49 | 1 | Split Guest Name / Co Name | none | 0 |
| un# | Defillama 49 Lead | 53 | 48 | 1 | Split Founder(s) / Protocol | 2 unlabelled flag cols | 0 |

Name formats across all tabs: "Name @ Company" 2,696 cells; name-only with company elsewhere 647; "Name@Company" without spaces 296 (collides with the email regex, 3 cells parse as fake emails); pasted LinkedIn page titles 242; split first/last 174; "Name - Company" 164; free text "Name, Title, Company" 60; parenthetical nicknames or roles 56; two or more people in one cell 54; ALL CAPS 9.

## Per-source detail

### 1. B2S_Guest_list.xlsx (Built to Share)

- **Headers are not on row 1** in 3 of 7 tabs (row 2 in "Global known in India" and "Global p3", row 3 in "N3 (6)"). "NEW" calls its name column "Column 1". Several tabs have a Follow Up 5 column with no header.
- **India / Global known in India**: name cell carries the LinkedIn URL as a hyperlink (65 of 66 rows). "Connect" (Akshay 5, Cold 34) is the warm-intro path. "Outreach channel" mixes channel, commentary ("LinkedIn / PR, cagey", "Rippling lawsuit") and, in India, 28 email addresses. "OR" = channel used (BOTH 19, MAIL 14, LI 1). Status: Unresponsive 28, Declined 6, Chasing 2, Maybe later 1. Follow-ups: 142 dates, 3 text cells ("check later", a date typed as text with "(v)", a reputational note about a founder).
- **NEW** (49): Country column contains "November" once. Follow Up 1 to 5 filled 92% to 27%; text "CHRO" (2, meaning the contact is the HR head) and "Next yr (2027)".
- **N2** (291): column "S" is a verification flag, not a status: CURRENT 203, TITLE_MISMATCH 49, DEPARTED 25, DOMAIN_CHANGED 6, ACQUIRED 3, COMPANY_DEAD 2, UNCLEAR 1, DISTRESSED 1, BAD_ROW 1. "Email in list" holds "(none)" 34 times. Real Status used once. 44 rows have 4 pre-scheduled follow-up dates, all in the future.
- **N3 (6)** (294): 259 of its people are also in N2; it is a re-bucketed copy (Bucket: More of the Same 220, Outliers 45, IPO / Pre-IPO 20, Big Global Founders 7, Recently IPOd 2). Name cell hyperlinks go to LinkedIn *search* pages, not profiles. Notes column holds the bucket rationale and 32 email addresses. Status: Started 58, Unresponsive 1 (dropdown also offers "Not yet").
- **Outliers** (33): 100% email fill but 7 academic, 6 personal freemail, 2 role inboxes (press@), 4 cells with two emails.
- **Global p3** (40): email only; 10 emails carry a dagger meaning "this is someone else's address" (a co-founder, investor relations or another executive), 1 is ir@. Status and Connect columns are empty.

### 2. HBD_new.xlsx (Human by Design)

- Academic-heavy: 70 of 110 emails are university or research-institute addresses; 11 carry "(verified)" in the cell text.
- **Sheet1** (34): Company column embeds the domain "(company.ai)". Status: Unresponsive 4, Maybe later 3, Approved 1. Follow-up text: "Reachout in 2027" (2), "Arjun rejected" (1).
- **V2** (28): affiliation and title sit in an unlabelled 3rd column (96% filled). Status: Approved 4, Declined 2, Chasing 1. "Arjun rejected" appears 3 times in follow-up cells; 6 Follow Up 4 dates are in 2027 (probable year typo).
- **V3** (48): two unlabelled columns (institution, title). Status: Approved 5. "Arjun rejected / Rejected" 3 times in Follow Up 1.
- The host verdict for HBD therefore exists only as text inside follow-up date columns.

### 3. FT Pipeline (Founder Thesis)

- **Paid** (12 real rows, 13 more rows are only unticked checkboxes): PR Contact 100%, Comment (free text stage), Nxt FU Date, and 7 checkboxes that form a payment and production checklist: GST details 7, Invoice sent 7, First payment 5, Planning call 4, Recording scheduled 3, Final payment 3, Released 1. One unlabelled cell holds an amount paid.
- **Inbound** (661): the main PR-pitch log. Status: Declined 267, Unresponsive 118, TBD 111, P1 61, Sponsored 48, P2 33, Propsed Alt 10, Paid 7, Interested 4, Precall Scheduled 2. Via 100% (PR person). "Next Action - mamatha" is really a stage log (Sponsored 112, Preliminary call 88+, Commercials shared 73+, 386 commercial or sponsorship mentions in total). "Next action - AD" (4%) holds host decisions ("Not looking for paid sponsorship", "Dont chase", "Akshay need to confirm"). "Dossier/ guest eval" 69% filled: verdict text in 357 cells (Decline 156, Evaluate after call 98, Strong consider 77, Book immediately 26, some cells list two verdicts for two people), 97 cells show only a link or doc title; 422 hyperlinks, mostly claude.ai shares, then Perplexity. One date column (FU/ Rec Date) is used for both next follow-up and recording date.
- **P1** (208): status values Form Filled 85 (post-recording: next action says thank-you sent, blurb added), Declined 18, LT Chase 16, To be Scheduled 16, P2 15, Add to outbound 13, Chase 13, Scheduled 13, Unresponsive 12, Recorded 4, Maybe Later 3. "Verdict" is 82% filled but only 16 cells show a verdict; 154 show a document title ("Guest Eval: ...") with the verdict inside the linked doc (claude.ai, Google Docs, Perplexity, ChatGPT). "Column 1" holds more eval and prep links. Via mixes "Cold Lead", "Referred by X @ Fund" (13), PR names and one phone number.
- **PAAS - FT** (93, podcast-as-a-service sales to past FT guests): Status Cold 52, warm 9, Emailed 5, Declined 5, Chase 3. Email cell holds 17 multi-address cells, 14 role inboxes (ir@, contact@, media) and 3 PR emails written as "founder / PR - pr@agency". "FD" column = "No reply" 13 (final follow-up done).
- **PAAS - Direct** (1,434, cold sales prospects): only 49% have email, 6% status (Unresponsive 76, Reject 5, Later 1), 12% have any outreach dates; a 6th unlabelled follow-up column holds 94 dates. One date typed as "25/18/2026".
- **PAAS new** (104): 100% email, X handle 43%, 3 scheduled follow-ups each (57 future-dated), Status used once.
- **VC Intros** (34 VCs): the intro targets sit in "Connects 1..5" (hyperlinked founders) and the *row below* each VC holds the eval verdicts for those founders (Strong consider 13, Book immediately 3, Decline 1). Status P2 24, Unresponsive 2; the dropdown (Contacted, Responded, Follow Up, Introduced) is never used.
- **FT Cold Lead** (154): two columns named "Status": the first is list approval (Approved 143, "Indian Investors,Approved" 11), the second is outcome free text (Bounced 6, Bounce - Block 2, 13 unique sentences about pre-calls). Email column contains "Bounced" as a value twice.
- **Post Release** (9): name, LinkedIn post URL, date. The only record of "Live".
- **Sheet2**: a 15-day chase cadence (Day 1 email, Day 3 WhatsApp, Day 7 email, Day 9 WhatsApp, Day 13 email, Day 15 WhatsApp). Useful as the Chase step definition.

### 4. un# Pipeline (alpha un#)

- **Pipeline v2** (191): name lives in a column headed "Linkedin Link" (display text is the name, 165 cells hyperlink to LinkedIn, 3 to X). Status (17 values): Recorded 31, Unresponsive 30, P2 28, Declined 27, Inbound 23, LT Chase 22, Sponsored 6, Approval Pending 5, others 1 to 3. "Sri Approval" is the host verdict (Yes 68, No 44, Ask 13, Sponsored 1). "AD Review" checkbox ticked 8. "Guest Eval" verdict text in 87 cells (Strong consider 39, Book immediately 34, Decline 10, Evaluate after call 5, Pre-call needed 1), 65 cells show only a title or link; "Guest Eval 2" and "Column 2" hold more. "follow up needed" (91%) is a mixed action and decision log ("Declined by Ravi", "Need update from Sri", "Offered Sponsored", "PR person - [name]"). The follow-up date column is headed "23-Jun". About 875 trailing rows contain only unticked checkboxes.
- **Sponsored** (18): header on row 2. Status Inbound 10, Declined 5, Unresponsive 3; Via 100%; "Next Action - mamatha" tracks commercial steps.
- **Post Release** (3): one says "No post done".
- **Podcast Leads** (56) and **pod Campaign** (20): outreach to *other* podcasts to place the host as a guest. Different entity (podcast + host), 23 role inboxes, "Contact Status" is a contact plan (Send Email+X DM+LinkedIn), rows 56 to 58 are notes ("Subscribers", "Youtube Link required").
- **YAP Clients** (34) and **Theprgenius Client** (14): guests offered by two PR agencies. Recommendation / Guest eval = eval verdict (100% filled). Theprgenius has a second sub-table (Guest Name, Designation, Recommendation, Blurb) starting at row 17, shifted one column right.
- **Old Pipeline** (23): legacy statuses (Proposed/ chasing 7, Proposed/ Interested 4, Inbound 3, Recorded 3, Sri to connect 3); a second sub-table header at row 28; 6 threaded comments hold channel notes ("LI + Mail", "guest eval, no connect").
- **CRM** (49): recorded or booked guests with title, email, Telegram (6), WhatsApp numbers (9), "Other Email IDs" (65%, mostly assistants and PR agency staff), LinkedIn, dossier, website, X. One row's email is a copy of another guest's email. Highest-sensitivity tab.
- **Defillama 49 Lead** (53): protocol founders; two unlabelled columns hold "Added / Exist" (21) and account-activity notes (13); "Not disclosed" used as a founder name.

## Cross-sheet identity results

Method: split multi-person cells, normalise names (accents folded, brackets and titles removed, first + last token) and companies (legal words and TLDs removed), then union-find on: (1) personal email, excluding role inboxes, dagger emails, PR emails and "Other Email IDs"; (2) LinkedIn profile slug from hyperlinks or text; (3) normalised name + company.

| Measure | Count |
|---|---|
| Named rows (guest and prospect tabs) | 3,970 |
| Person mentions after splitting 50 multi-person cells | 4,025 |
| Unique after email | 3,767 |
| Unique after email + LinkedIn | 3,694 |
| Unique after email + LinkedIn + name & company | **3,488** |
| Lower bound if identical full names also merge | 3,435 |
| Mentions with a LinkedIn URL / any email / neither | 2,247 / 1,818 / 950 |
| People in 2+ tabs | 471 |
| People in 2+ workbooks (shows) | 9 |
| Max tabs for one person | 3 |
| People duplicated inside the same tab | 29 (19 inside FT Inbound) |
| People with 2+ different personal emails | 30 |
| Email addresses shared by 2+ different names | 12 |
| Multi-tab people with contradictory status | 99 |

Largest tab overlaps: N2 and N3 (6) 259; FT Inbound and P1 61; Global p3 and N3 30; un# CRM and Pipeline v2 27; N3 and NEW 23; FT Cold Lead and P1 19; Global p3 and NEW 16; P1 and PAAS - FT 10. Of the 99 status conflicts, 52 are Inbound vs P1 and 17 are FT Cold Lead vs P1: a person promoted to the next tab keeps their old status on the old tab.

Tricky matches (anonymised):

1. Founder of an AI voice company: firstname.lastname@ on one B2S tab, firstname@ on another; no LinkedIn on the second row. Matched only by name + company.
2. Founder of a crypto exchange: on B2S India, FT P1 and un# Pipeline v2 with three statuses (Chasing, Declined, Unresponsive) and no email anywhere; LinkedIn links two rows, name + company the third.
3. Founder of an autonomous-driving company: on B2S N2, B2S N3 and HBD V2 (same email); in HBD the affiliation column just says "[company]'s CEO". The only B2S/HBD cross-show person.
4. Crypto founder spelled with a double consonant in un# Pipeline v2 and single in Old Pipeline and CRM; only the LinkedIn slug joins them.
5. Blockchain founder written with Serbian spelling in Old Pipeline and English transliteration in CRM; joined by LinkedIn.
6. DeFi founder entered as first name + surname initial in Old Pipeline and full name in CRM; LinkedIn is the only key.
7. Listed internet-company founder: full name on B2S India, first name only with the company written as one word on FT VC Intros, ALL CAPS without company on B2S NEW. LinkedIn joins two; the third needs a name-only match.
8. VC fund founder listed twice inside FT Cold Lead with two different addresses on the same domain, and again on P1 and VC Intros.
9. HR-tech founder on FT P1 with a nickname in brackets and a .com address, on PAAS - FT with a .ai address. Name normalisation plus company joins them.
10. Two different crypto guests in un# CRM share one email because a row was copy-pasted; a naive email match merges two people. Same risk from two consumer-brand co-founders who share role inboxes on PAAS - FT, and a B2S Global p3 row whose dagger email belongs to the co-founder listed on another tab.

## Status mapping

All status-like values actually used (count). Proposed target fields: **Stage** (Identified, Contacted, In conversation, Agreed), **Outcome** (Live, Done, Declined, No response, Dropped out), **Host verdict**, **Eval verdict**, **Commercial** (Free guest, Sponsored, Paid, Client), **Chase step**. Blank = leave unset.

| Raw value (count) | Where | Stage | Outcome | Other field |
|---|---|---|---|---|
| Declined (334) | most tabs | keep last known | Declined | |
| Unresponsive (275), Proposed/ unresponsive (1) | most tabs | Contacted | No response | Chase step = last FU sent |
| uncontactable (1), Bounced (6), Bounce - Block (2) | un#, FT Cold Lead | Contacted | No response | flag email invalid |
| Approved (153) | FT Cold Lead | Identified | | Host verdict = Approved to pitch |
| Indian Investors,Approved (11) | FT Cold Lead | Identified | | Host verdict = Approved; tag Investor |
| Approved (10) | HBD V2/V3/Sheet1 | open question | | Host verdict = Approved (probable) |
| Cold (52), Cold Lead (3), Add to outbound (13) | PAAS - FT, un#, P1 | Identified | | |
| Inbound (36) | un# | Identified | | Source = Inbound pitch |
| Started (58), Emailed (5) | B2S N3, PAAS - FT | Contacted | | Chase step 1 |
| Chase (16), Chasing (7), Proposed/ chasing (7) | FT, B2S, HBD, un# | Contacted | | Chase step active |
| LT Chase (39) | FT P1, un# | Contacted | | Chase step = Long-term (snooze) |
| Maybe later / Maybe Later (11), Later (1) | many | Contacted | | Chase step = Snoozed, next date |
| warm (9), Interested (5), Proposed/ Interested (4) | PAAS - FT, FT, un# | In conversation | | |
| TBD (111) | FT Inbound | In conversation | | Host verdict = Pending |
| Approval Pending (5), Sri to connect (3) | un# | In conversation / Identified | | Host verdict = Pending |
| P1 (61) | FT Inbound | In conversation | | Host verdict = Priority |
| P2 (100) | FT, un#, VC Intros | keep | | Host verdict = Low priority / parked |
| Precall Scheduled (3), PreCall Done (3) | FT, un# | In conversation | | |
| To be Scheduled (19), Scheduled (14) | P1, un# | Agreed | | |
| Recorded (38) | P1, un# | Agreed | Done | |
| Form Filled (85) | P1 | Agreed | Done | post-recording form received |
| Released (Post Release rows, Paid checkbox) | FT, un# | Agreed | Live | |
| Propsed Alt / proposed alt (12) | FT Inbound, un# | keep | Dropped out | link to alternate person |
| Reject (6) | PAAS | keep | Declined (open question) | |
| Sponsored (54) | FT Inbound, un# | In conversation | | Commercial = Sponsored |
| Paid (7) | FT Inbound | In conversation | | Commercial = Paid |
| FT Cold Lead 2nd Status (13 sentences) | FT Cold Lead | parse: pre-call wording = In conversation, "not interested" = Declined, "next year" = snoozed | | |
| CURRENT, TITLE_MISMATCH, DEPARTED, DOMAIN_CHANGED, ACQUIRED, COMPANY_DEAD, UNCLEAR, DISTRESSED, BAD_ROW (291) | B2S N2 | | | Data-quality flag, not a status |
| Send Email+X DM(+LinkedIn), LinkedIn, Twitter, etc. (26) | Podcast Leads | | | Contact plan (non-guest entity) |

Other decision fields:

- **Host verdict** sources: un# "Sri Approval" (Yes 68, No 44, Ask 13, Sponsored 1) and "AD Review" (8 ticked); HBD "Arjun rejected" text in follow-up cells (7); FT P1/P2 statuses, "Next action - AD" and phrases like "Decline by Akshay", "Akshay has to decide", "Dont chase" (about 53 host-decision phrases in note columns); B2S "Connect" = Akshay (warm path) vs Cold; FT Cold Lead "Approved".
- **Eval verdict** vocabulary: Book immediately, Strong consider, Evaluate after call, Pre-call needed, Decline, plus Tier 1 / Tier 2 (P1 only) and combined cells ("Decline and Strong consider" for two people). Readable in cell text: Inbound 357, Pipeline v2 87, YAP 34, Theprgenius 14, VC Intros 17, P1 16. Hidden behind a link or doc title: P1 154, Inbound 97, Pipeline v2 65.
- **Commercial**: Sponsored = Inbound status, un# Sponsored tab, "Sponsored feature / Commercials shared" notes; Paid = FT Paid tab (7 milestone checkboxes, which become a Deal record) and status Paid; Client = PAAS tabs (sales prospects for podcast production, 1,631 rows); everything else Free guest. "YAP Clients" and "Theprgenius Client" are PR-agency clients, i.e. free guests via a PR contact, not ThePodium clients.
- **Chase step**: derive from the count of follow-up dates on or before today (0 to 6), with Sheet2 cadence as the template (email, WhatsApp, email, WhatsApp, email, WhatsApp over 15 days); LT Chase and Maybe later become a snooze date; "FD = No reply" means final step done.

## Via / PR contacts

- Columns: FT Inbound "Via" (100%), FT P1 "Via" (89%), un# Sponsored "Via" (100%), FT Paid "PR Contact" (100%). Also embedded in un# "follow up needed" ("PR person - ..."), CRM "Other Email IDs" and PAAS - FT email cells.
- 877 non-empty cells: 841 named contacts, 21 "Cold lead", 13 "Referred by X @ Fund" (these are introducers, often VCs, not PR), 2 "Inbound".
- **546 distinct contact names; 154 recur 2+ times and cover 460 rows; 20 recur 5+ times; the busiest contact appears 11 times.** 76 contacts appear in more than one tab (FT and un#). 29 are first-name only; a few cells carry a phone number, an email fragment or a company name instead of a person.
- Implication: a PR Contacts database (person + agency) is worth it; about a third of pitches come from a repeat contact. Agency is not recorded anywhere and would need backfilling from email domains.

## Data problems the migration must handle

1. **Header position varies** (row 1, 2 or 3); two tabs have a second sub-table mid-sheet (Old Pipeline row 28, Theprgenius row 17, shifted one column); VC Intros uses the row *below* a VC for verdicts.
2. **Unlabelled columns with data** (Follow Up 5, HBD affiliation and title, Defillama flags, PAAS - Direct 6th follow-up): 263 cells. Duplicate header names (two "Status" in FT Cold Lead). Headers that are data ("23-Jun", "Column 1", "Linkedin Link" holding names).
3. **Hyperlinks carry the data**: 3,910 hyperlinks. LinkedIn URLs sit behind name text; eval verdicts sit behind doc titles. Export must use xlsx or the Sheets API, never CSV.
4. **Name parsing**: 12 formats (see Inventory). "Name@Company" looks like an email. Titles and roles appended to names ("... Co-Founder", "CPO @ Company"). Multi-person cells (50) must split into separate people linked to one conversation.
5. **Email hygiene**: markers inside the value ("(verified)" 11, dagger 10), placeholders ("(none)" 34, "Bounced", "No", "Not found", "N/A", "Contact form on website"), multiple addresses in one cell (45), role inboxes (58), PR addresses in guest cells (3), emails stored in Outreach channel (28) and Notes (32) columns, trailing spaces, 17 personal freemail and 77 academic addresses. Store as Email (primary) + Other emails + Email status.
6. **Duplicates and conflicts**: 471 multi-tab people, 29 in-tab duplicates, 99 contradictory statuses. Rule needed: the most advanced stage wins, the latest dated row wins for notes.
7. **Status vocabulary drift**: case variants (Maybe later / Maybe Later, Chase / Chasing), typos (Propsed Alt, Perliminary, Commericials), multi-value cells ("Indian Investors,Approved"), dropdown values defined but never used (Contacted, Responded, Introduced, Accepted, Not yet, Precall pending).
8. **Dates**: 449 follow-up dates in the future (planned, not done), a date typed as "25/18/2026" (invalid), "19/08/2026 (v)", six HBD Follow Up 4 dates in 2027 (likely typo), one numeric date in P1, one column used for both follow-up and recording date.
9. **Decisions in free text**: "Next Action" columns are stage logs; host verdicts sit in follow-up and note cells; payment progress in checkboxes. Needs a rules-based parser plus human review for about 300 rows.
10. **Phantom rows**: about 890 rows with only unticked checkboxes (un# Pipeline v2, FT Paid); note rows in Podcast Leads; "Not disclosed" as a founder name.
11. **Copy-paste errors**: one CRM row carries another guest's email; one B2S Global p3 row has another founder's email (dagger); country "November".
12. **Sensitive data**: WhatsApp numbers, Telegram handles and assistant emails in un# CRM; a phone number in a P1 Via cell; reputational notes about founders in follow-up cells. Needs restricted fields in Notion.
13. **Non-guest entities in guest workbooks**: podcast hosts (Podcast Leads, pod Campaign), sales prospects (PAAS, 1,631 rows), VCs as introducers (VC Intros), outreach templates (Sheet2).

## Other sheets found in Drive (inventory only)

Owner shown by account name only. Not audited.

| Title | Owner | Last modified | Likely role |
|---|---|---|---|
| Founder_Thesis_Master_People_List (3 copies) | AD | 2026-09-07 to 09-08 | Possible existing master people list; check before migrating |
| founderlinkedinlist | AD | 2026-09-07 | LinkedIn list |
| PAAS_Leads | AD | 2026-09-02 | PAAS prospects |
| BTS_Guest_Shortlist_46 | AD | 2026-09-01 | B2S shortlist |
| BuiltToShare_Guest_Shortlist_Aug2026 | AD | 2026-08-13 | B2S shortlist |
| B2S_Guest_list, B2S_Guest_list__with_emails | AD | 2026-07-13 | Earlier versions of source 1 |
| HBD_Guest_Pipeline_Enriched_v1.xlsx | AD | 2026-08-20 | Earlier version of source 2 |
| Un# Scheduling | Mamatha | 2026-09-25 | Active recording scheduling tracker |
| HK/SG Guest - Un# | Mamatha | 2026-07-02 | un# regional guest list |
| alhpa Un# Podcast Pitch | Mamatha | 2025-08-19 | Early un# pitch list |
| FT Cold Lead | Mamatha | 2025-09-08 | Original of the FT Cold Lead tab |
| FT 2 Tracxn sheet.xlsx | Mamatha | 2026-01-07 | Company data export |
| Fast Code Podcast Pipeline | Mamatha | 2026-07-13 | Client podcast pipeline |
| Podcast Lead sheet | Deven (Fast Code) | 2026-05-14 | Client podcast leads |
| Podcast_Guest_Shortlist_Top20.xlsx, apollo-contacts.xlsx | Sanjay (Fast Code) | 2026-03 | Client guest shortlist, Apollo export |
| FT_guest_Shark | Chaandini | 2026-08-18 | FT guest idea list |
| PAAS US Outreach | founderthesis Gmail account | 2026-08-12 | PAAS outreach |
| US B2B Companies for PAAS Pitch; US_B2B_Companies_-_Scored (2 copies) | AD | 2026-07-02 | PAAS target companies (large) |
| PodcastGTM_Pitch_List__85_Verified_Prospects | AD | 2026-07-10 | Prospect list |
| Next_Horizon_Guest_Shortlist_v2 / v4 | AD | 2026-07-23 | Guest shortlist (another show) |
| Playbooks Guestlist v5; Playbooks_by_Prath_Longlist v3 to v6 (6 files) | AD | 2026-06-10 to 07-02 | Guest lists for another client show |
| Hissa Guests | AD | 2025-11-09 | B2S-related guest list |
| Founder Cohorts | Akshay | 2026-01-19 | Founder grouping |
| TracxnExport files (3) | AD | 2025-07 to 2026-06 | Company data exports |
| Unnati Rate Card (2 files), Unnati Run Rate | AD | 2026-07 to 09-30 | Pricing and finance reference |

Also matched but out of scope: post-idea and post trackers (Piyush, Satish, aarna), finance reports (TDS, GSTR, debtors, bank), hiring and application forms.

## Open questions

1. Is Founder_Thesis_Master_People_List already a consolidated people list, and should it be a fifth source or the seed?
2. Which B2S tab is canonical: N2 or N3 (6)? N3 looks like a re-bucketed superset.
3. What exactly are P1 and P2: host priority, or stage? (Inbound P1 rows are copied to the P1 tab.)
4. HBD and B2S "Approved": host approved the target, or guest agreed to record?
5. PAAS "Reject": did the prospect decline, or did we drop them?
6. "Propsed Alt": should the alternate spokesperson become a new person linked to the original conversation?
7. Are follow-up date columns planned dates or sent dates? 449 are in the future, so at least some are plans.
8. Should eval verdicts hidden inside linked docs (about 316 rows) be backfilled by reading the docs?
9. Should podcast-host outreach (un# Podcast Leads) and PAAS sales prospects live in the same People database with a Type field, or separately?
10. "Client" in Commercial: PAAS customers only, or also PR-agency clients pitched as guests?
11. Where should WhatsApp and Telegram details live, and who may see them?
12. The B2S and HBD uploads are generated files with no owner; who owns them going forward, and are the Drive versions older or newer?
