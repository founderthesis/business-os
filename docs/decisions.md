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
| 23 | alpha un# evals: Akshay approves first; the agent then sends Akshay a Slack reminder with the blurb and eval link to pass to Sri. | Akshay, 30 Sep |
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
| 45 | HK/SG Guest - Un# Sheet1 migrates as alpha un# targets (Identified, recommendation as tag, blurb and research link on the person). Sheet2 and the alpha un# podcast pitch list stay out. | Akshay, 2 Oct |
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
| 57 | Dashboard order: the To decide table first (decisions, actions and due reminders, with an FYI tab for heads-up), then Today (calendar, releases, hot PaaS), then pipeline views; settings, help and run log at the bottom. Every decision card carries the links needed to decide (Eval, LinkedIn, Website, Other link) so the mail doesn't need opening. | Akshay, 3 Oct |

## Open

- Field-level spec: draft 3 approved 2 Oct; tables created (see `docs/notion.md`).
- Release cadence: not fixed; the planner proposes dates each time.
- Which templates exist per show, and approval of each.
- Backlog clean-up for the existing unread inbox.

## Overrides

None yet.
