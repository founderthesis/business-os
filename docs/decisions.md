# Decisions

Closed items stay closed unless Akshay reopens them. Add overrides at the bottom with a date.

## Decided (30 Sep 2026)

| # | Decision | Why |
|---|---|---|
| 1 | Design from first principles. Earlier drafts (context brief, CRM build plan, older audits) are context only. | Akshay's call |
| 2 | Notion is the store and the screens. Logic lives in this repo. | Small team, no front end to maintain |
| 3 | One Engagements table for guest, BD, sponsor, partner and client pursuits. | Same loop everywhere; one queue, one chase engine |
| 4 | Stage (Identified, Contacted, In conversation, Agreed) and Outcome are separate fields. | Keeps how far something got before it died |
| 5 | Episodes hold the working doc in the page body plus Final fields. No separate Outputs table. | Akshay's call; learning compares page sections with Finals |
| 6 | People carry location (LinkedIn), a blurb, and all research history. | Research belongs to the person, not the deal |
| 7 | Scope: owned shows, BD, client production. Ghostwriting later. | Akshay's call |
| 8 | All four goals in scope; order follows dependencies. | Akshay: "all 4" |
| 9 | Emails send after Akshay approves, with no second step. Send log, daily cap and kill switch. | Akshay's call |
| 10 | Standing approval per template per show for routine sends (thank-you, PR form). A template edit resets approval. | Thank-yous should not wait on a dashboard check |
| 11 | Agent rules are defaults, not locks. Akshay can override in chat; overrides are logged here. | Akshay's call |
| 12 | Every inbox email goes to the dashboard as Decision, Heads-up, Reminder, Action or Noise. Handled mail is marked read. | Akshay's call |
| 13 | No pings. Notion dashboard only, opened by the morning brief. | Akshay's call |
| 14 | Prep links go on a private calendar only Akshay sees, never on invites with guests. | Guest invites are shared with guests |
| 15 | Content pack: Claude automatic; Gemini and ChatGPT manual, pasted and tagged. | Picks will show if more models are worth automating |
| 16 | All email goes from ad@thepodium.in. | Akshay's call |
| 17 | Zencastr transcripts downloaded by Claude in Chrome from the invite link. | No Zencastr export API |
| 18 | Meet transcripts are switched on per call; the prep entry reminds Akshay. | Cannot default on |
| 19 | Access: core team in the main workspace; hosts and retainer clients get separate synced portals; PR agencies get email only. | Notion has no row-level security |
| 20 | WhatsApp: pasted into Slack or logged by a button; reminders come through the brief. | No clean capture route |
| 21 | Threads where Akshay is only cc'd and Mamatha is handling are Heads-up and auto-marked read. | Akshay, 30 Sep |
| 22 | When an eval says Decline, the decision card pre-selects Sponsored. | Akshay, 30 Sep (70% of past decisions) |
| 23 | un# evals: Akshay approves first; the agent then sends Akshay a Slack reminder with the blurb and eval link to pass to Sri. | Akshay, 30 Sep |
| 24 | People is the one master network list: every FT guest plus everyone in Akshay's founder and VC WhatsApp group (500+), most recent data, deduped. It is the asset Akshay shows when pitching clients. Fields: FT guest, Substack article link, In WhatsApp group. | Akshay, 30 Sep |
| 25 | The existing FT guest list in Notion that feeds the automated Substack articles must keep working through the migration. | Akshay, 30 Sep |
| 26 | Spotlight is a tag within Founder Thesis, not a separate show. Tier 3 FT episodes carry it, publish on the Spotlight YouTube channel and RSS feed, and still get a founderthesis.com feature. | Akshay, 30 Sep (revised same day) |
| 27 | Phone numbers stay in Notion. | Akshay, 30 Sep |
| 28 | From Blue, copy field data only. Videos, photos and other heavy files are dropped. | Akshay, 30 Sep |
| 29 | Every engagement captures all stakeholders (guest, PR agency people, company comms, EAs, interns). All of them are copied on guest emails such as the thank-you. | Akshay, 30 Sep |
| 30 | The Google Ads upsell on the old guest form is no longer offered; the new form drops it. | Akshay, 30 Sep |
| 31 | No Commercial field. Decision (Sponsored) and the show's Owned or Client flag already say whether money is involved; Amount and Paid appear only when it is. | Akshay, 30 Sep |
| 32 | No typed Final fields. The episode working doc lives in the Episode page in Notion; every option is a checkbox and the ticked one is final. Ticks and edits are the learning signal. Ticking a theme starts stage B. | Akshay, 30 Sep |
| 33 | Two-guest episodes: one Episode, one Engagement per guest. | 30 Sep |
| 34 | Copy tasks go to Ranjita, video tasks to Sarika, created automatically from episode status, due dates counted back from Planned release. | Akshay, 30 Sep |
| 35 | Release calendar: Episodes have Planned and Actual release. A planning task runs every other week, proposes dates for the month, Akshay approves. | Akshay, 30 Sep |
| 36 | Shows carry a guest note, recording guidelines, platform links (YouTube, Spotify, Apple, Amazon, RSS, website), cadence, and a wiki page. | Akshay, 30 Sep |
| 37 | Tags (free multi-select) on People, Organisations, Engagements, Episodes and Tasks. The episode tier is a tag. | Akshay, 30 Sep |
| 38 | The guest form is sent for Founder Thesis only. | Akshay, 30 Sep |
| 39 | Engagements carry a Dossier link. | Akshay, 30 Sep |
| 40 | All video and production tasks go to Sarika for now; she will add dashboards for Francis, Vinayak and Ajab. | Akshay, 2 Oct |
| 41 | Tier decides workload: Tier 1 gets the full content pack and task set, Tier 2 and Spotlight a light pack. Order of work: client, Tier 1, Tier 2, Tier 3. | 1 Oct release call, Akshay 2 Oct |
| 42 | Reels go to the guest and company on release day for their Instagram. | 1 Oct release call |
| 43 | Science and PhD guests review a rendered frame before release ("Guest review" tag, default on for HBD). | 1 Oct release call |
| 44 | The weekly release feedback call notes are parsed per episode and feed the skills' learning. The release-frequency test is reviewed around 1 Nov. | Akshay, 2 Oct |
| 45 | HK/SG Guest - Un# Sheet1 migrates as un# targets (Identified, recommendation as tag, blurb and research link on the person). Sheet2 and the un# podcast pitch list stay out. | Akshay, 2 Oct |
| 46 | PaaS (podcasting as a service: selling ThePodium's production service to get client shows) is an Engagement type. It replaces "BD". PaaS deals carry Heat, Pitch link and the Proposal sent stage. | Akshay, 2 Oct |
| 47 | US VC Podcast Outreach migrates in full as PaaS engagements: one per firm, tagged US VC and Priority A/B/C, ranked by Fit Rank. Every named contact becomes a person (first contact as the main contact, the rest as stakeholders). Firms become Organisations with the role inbox in General email and the fit research in the page body. Reverses the earlier "not migrating" call. | Akshay, 2 Oct |
| 48 | "No email" tag on any person, firm or engagement with no address to write to, so it can be filtered out. | Akshay, 2 Oct |
| 49 | PR contacts from Blue guest forms become People tagged PR contact and are linked as stakeholders on the guest's engagement. Names are guessed from the address and tagged "Name guessed"; shared inboxes are tagged "Role inbox". | Akshay, 2 Oct |
| 50 | Old Notion tables fold in without rebuilding any table: PaaS Leads and US VC into Engagements; B2S and HBD lists into Engagements; Vendor Pitches form routes to Engagements type Vendor; Meetings feeds Activities; Newsjack Log stays as its agent's log; Publishing Plan, Substack Posts Audit, inbox snapshots, Scout log, starter template and the DELETE page retire after checks. Episodes gain Sector, Article state, Article priority, YouTube views and Apple. | Akshay, 2 Oct |
| 51 | An episode is named "Guest @ Company - Show", never by its title. A guest recorded more than once gets V1, V2 in recording order; a split recording keeps "Part N". Titles change and differ between YouTube and Spotify, so they live in "YouTube title" and "Spotify title". | Akshay, 3 Oct |
| 52 | One recording is one episode however many times it was published. Re-uploads and republishes (Beyond Campus, rebranded to Spotlight, carried FT episodes as is) merge into one row; the other upload's link is kept on the page. | Akshay, 3 Oct |
| 53 | Duplicate People are checked online first; the pair is linked ("Duplicate of") with a one-line reason, and Akshay decides by comment or by Match status. Rows to remove are marked, never deleted by an agent. | Akshay, 3 Oct |
| 54 | The inbox agent runs at 07:00 and 18:00 JST; the 07:00 run writes the morning brief at the top of the dashboard. One card per Gmail thread. | Akshay, 3 Oct |
| 55 | The inbox agent starts in TEST mode (sorts and drafts, sends nothing, marks nothing read, writes a test log). Akshay switches it to LIVE on the dashboard after one or two good test runs. | Akshay, 3 Oct |
| 56 | Standing approval: a guest pitch sent straight to Akshay or to hello@, by a PR person or by the guest themselves, gets "Thanks for your mail, adding Mamatha to coordinate" with Mamatha cc'd, without asking. | Akshay, 3 Oct |
| 57 | Superseded by 61. Dashboard order: the To decide table first (decisions, actions and due reminders, with an FYI tab for heads-up), then Today (calendar, releases, hot PaaS), then pipeline views; settings, help and run log at the bottom. Every decision card carries the links needed to decide (Eval, LinkedIn, Website, Other link) so the mail doesn't need opening. | Akshay, 3 Oct |
| 58 | One Status ladder on Engagements for the guest journey (New to Form filled, plus LT chase, Parked, They declined, We declined, Unresponsive). Stage, Outcome, Whose move, Heat, Pitch link, Rank and Type retired. Tier (1, 1.5, 2, Sponsored) and Direction (Inbound, Outbound) added. Sponsored money tracked in a Payment column on the same row. Spec in docs/statuses.md. | Akshay with Mamatha, 5 Oct |
| 59 | Commercial pursuits (PaaS, clients, sponsors, partners) live in a separate Deals table. A sponsored guest appearance is not a deal; it stays on the guest row. | Akshay, 5 Oct |
| 60 | No person tagging on rows. Each person owns a show or a list; Mamatha owns all FT guests. Her tabs on Engagements: FT: Pipeline, FT: Outbound, FT: Sponsored. | Akshay, 5 Oct |
| 61 | The dashboard and the Decision Desk are dropped. Akshay reads his own mail. Decision surfaces will be tried again later with a different approach. Supersedes 54 to 57 for now. | Akshay, 5 Oct |
| 62 | The inbox agent is capture only: one Activity per email (Source ID = Gmail message id, so re-runs skip what is logged), plus Engagement and Deal updates that follow from the mail. It sends nothing, marks nothing read, makes no cards and asks nothing. Run by hand in a separate chat for now. Prompt in routines/inbox.md. | Akshay, 5 Oct |
| 63 | Deals are either Warm (Akshay already knows them: a guest who has recorded, or a personal intro) or Cold outreach (anyone the team is approaching, including FT-invite targets not yet recorded; refined 5 Oct after Gather AI, Sorcero and Lemma). The FT, US VC and HK/SG buckets are gone; the US VC list is all cold outreach. Priority A/B/C, Has podcast and No email tags stay. | Akshay, 5 Oct |
| 64 | The Queue holds only what still needs someone, and every card is linked to an Engagement (or a Deal for production sales); the card title leads with the guest or company. One board, grouped by Status (To do, Waiting, Done), shows the linked Engagement and its status so Akshay clicks through and updates the Engagement there. Facts and FYIs are not cards: they go on the Engagement and Activities. Internal work goes to Tasks. Done cards are cleared from the "To delete (done cards)" tab. | Akshay, 5 Oct |
| 65 | The inbox agent adds a Queue To do card in two cases only: a guest eval from Mamatha, or a mail that asks Akshay a direct question he has not answered. One card per thread, linked to the Engagement or Deal, closed by the agent once his reply shows in the thread. Everything else stays capture only (amends 62). Cards now go to Mamatha, see 67. | Akshay, 5 Oct |
| 66 | Engagement statuses rationalised. Decision renamed Route (Sponsored, Organic); Tier is importance only (Tier 1, 1.5, 2), so "Sponsored" no longer appears twice. Parked = Akshay has lost interest and Mamatha stops following up, set by Akshay only. LT chase = still want them, revisit on Next date (timing reasons go here). Parked counts as closed in every view. New fields Call link and Call type, filled from the calendar. | Akshay, 5 Oct |
| 67 | The Queue is Mamatha's worklist, not Akshay's (amends 64 and 65). Akshay does not read it. Three card types: Ask Akshay (only he can decide; Mamatha chases him and records the answer), Follow up (a guest or deal has gone quiet), Fix data (cleanup in Notion). Routines add and close cards; a daily upkeep run keeps up to 30 Follow up plus Fix data cards open (raised from 12 new a day and 25 open, Akshay 6 Oct), and mails Mamatha a summary. Thread ID is the dedupe key. | Akshay, 5 Oct |
| 68 | Automations live as four Claude routines: Inbox to Business OS (06:55, 14:55, 20:55 JST), FT guest evals (07:20, 15:20, 21:20), Calendar sync (07:35, 15:35, 21:35), Queue upkeep (13:10 JST Mon to Sat). Standing approvals: the pitch reply "Thanks for your mail, adding Mamatha to coordinate" with Mamatha in Cc (FT only), eval link mails and the daily queue mail to Mamatha, archiving calendar RSVP mail. Auto eval for FT only. Private prep entries (no guests) 30 minutes before each recording and precall, with the call link. After a recording: a thank-you draft (never sent by the agent) and a WhatsApp blurb, with an Ask Akshay card. Send cap 100 a day as a runaway guard, not a quota. Prompts in routines/. | Akshay, 5 Oct |
| 69 | The Founder Thesis guest form (podm.in/thank-you) moves from Blue to a Notion form on a new Guest forms table. Questions: guest name, company, designation, email, guest and company LinkedIn, photo, logo, guest and company Instagram (optional), PR and comms emails, filled by, anything to hold back before release. Google Ads upsell stays dropped (30). Each submission stays as the raw row with its photo and logo; the inbox routine matches it to the guest's Engagement, fills People and Organisation gaps, adds PR emails as Stakeholders, sets Form filled, ticks Guest form in on the Episode, logs an Activity, and gives Mamatha a card to send the likely release date. Unmatched rows go to Needs review with a Fix data card. | Akshay, 6 Oct |
| 70 | Every inbound pitch is processed: no skip for mass mailings, pitches that name another podcast, or pitches that name no show. A pitch that does not name one of our other shows is Founder Thesis, gets the "adding Mamatha" reply and an auto-eval. An existing Engagement for the guest (including outbound wish-list rows) is reused and turned Inbound. | Akshay, 6 Oct |
| 71 | un# moves off its Google Sheet ("un# Pipeline") onto Engagements, same Status ladder as FT (mapping in docs/statuses.md). Sri's approval lives in Host verdict. P2 and Maybe Later are LT chase. The YAP and The PR Genius client rosters and the Defillama target list come in as New rows so the whole un# funnel is in one place. Existing Form filled and agent rows keep their status. Tabs: un#: Pipeline, un#: Sponsored, un#: Closed. Notion is the record from here; nothing syncs back to the sheet. | Akshay, 6 Oct |
| 72 | un# decisions stay Ask Akshay cards: Sri's calls are routed through Akshay, who speaks to him directly. Of the 28 un# rows migrated at Decision pending, 22 were closed as We declined on 6 Oct (20 where the sheet had Sri at No and nothing moved since March to May, 2 old-tab rows never picked up), with no decline mails sent; the 6 still waiting on Sri (Karl Floersch, Sergej Kunz, Fred Hsu, Evan Cheng, Konstantin Shulga, Alexis Sirkia) stay open. | Akshay, 6 Oct |
| 73 | Prep entries on the calendar: recordings (2-hour slots) get a 30-minute prep block before the call; precalls get a private entry at the same time as the call, marked free, carrying the prep links, so no extra time is blocked (amends 68). | Akshay, 6 Oct |
| 74 | Sponsored moves back into Tier (Tier 1, 1.5, 2, Sponsored) and Route is removed, so Mamatha has one column to read (overrides the Route part of 66). All 404 Route = Sponsored rows carry Tier = Sponsored; Route Organic held no information. FT: Sponsored view retired in favour of the Tier quick filter. Routines and skills read Tier = Sponsored for the A2 and F3 queue checks and Akshay's "sponsored" reply. | Akshay with Mamatha, 6 Oct |
| 75 | Anyone on the team can change anything in the Business OS, in Notion directly or by asking Claude through the notion-business-os skill. The skill no longer reserves Parked, Tier, Amount or Payment for Akshay; it logs who asked on every change. The scheduled routines keep their own limits (they still never set Parked, Tier, Amount or Payment on their own). | Akshay, 6 Oct |
| 76 | The FT thank-you mail links to the Notion guest form's public link. The podm.in/thank-you short link is deleted (out of free short links until 10 Oct). The calendar routine puts the Notion link in every thank-you draft and never copies the old link. A podm.in short link can replace it later. | Akshay, 6 Oct |
| 77 | Every email Activity carries a 2 to 3 line summary of what was said and asked in its page body, so the Gmail link is optional reading. | Akshay, 6 Oct |
| 78 | No Ask Akshay cards for eval decisions. Akshay decides nearly everything from his inbox, so Decision pending is his list and the routines read his decision from Gmail (his reply on the eval mail, the PR thread, or a mail to Mamatha) and apply it. A Book immediately eval is not a decision: it goes straight to Booking with a Follow up card to get dates. The eval mail goes to Akshay and Mamatha. Queue upkeep fixes rows itself when Gmail shows what happened (replies, decisions, three unanswered chases over 30 days -> Unresponsive) and cards only what's left; closed Engagements close their cards. Amends 67. | Akshay, 7 Oct |
| 79 | The Queue is retired. Anything that needs a person is flagged on the Engagement (or Deal) itself: Next date = today and Next action = who does what ("Mamatha: ...", "Ask Akshay to approve: ...", "Fix: ..."). Mamatha works the Engagements view FT: Today (Next date today or earlier, oldest first) and clears it by doing the step and moving the date. New column Last activity shows the newest logged mail; a Due formula drives the view. Routines never push an open flag later unless the mail settles it; our reply with the ball in their court moves Next date 4 days out as "Waiting on". Queue upkeep becomes the Daily sweep. Decision pending rows are flagged "Ask Akshay to approve" (amends 78). Supersedes 67. | Akshay, 7 Oct |
| 80 | The show is un# in writing and Unhashed when spoken; the old name with "alpha" is gone from Notion, the repo, the routines and the skills. Voiceover and trailer skills say "the Unhashed podcast". The one place it stays is a key in migration/episodes.py that must match the retired Blue workspace's literal name. Also: un#: Today view, same rules as FT: Today, with un# decisions flagged "Ask Akshay to get Sri's call". | Akshay, 7 Oct |

## Open

- Field-level spec: draft 3 approved 2 Oct; tables created (see `docs/notion.md`).
- Release cadence: not fixed; the planner proposes dates each time.
- Which templates exist per show, and approval of each.
- Backlog clean-up for the existing unread inbox.

## Overrides

None yet.
