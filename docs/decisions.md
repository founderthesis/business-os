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

## Open

- Field-level spec: draft 3 approved 2 Oct; tables created (see `docs/notion.md`).
- Release cadence: not fixed; the planner proposes dates each time.
- Which templates exist per show, and approval of each.
- Backlog clean-up for the existing unread inbox.

## Overrides

None yet.
