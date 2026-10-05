# Statuses and pipelines

Proposal, 5 Oct 2026, second draft after Mamatha's feedback. Built from every status value in the FT Pipeline sheet (counts in `data/out/ft_pipeline_statuses.md`, not committed) and the PaaS lead fields already migrated. Nothing is changed in Notion until Akshay approves.

## The one idea

A row is one conversation. Mamatha's conversation with a guest is one row, whether the guest ends up free or sponsored. Akshay's sale of podcast production to a company is a different conversation, usually with a different person and usually after the episode, so it is a different row in a different table.

So:

- **Engagements** stays the guest table. One row per person per show. Mamatha lives here.
- **Deals** is new: one row per company we are selling production to (PaaS). Akshay and Chaandini live here. The 788 PaaS rows move out of Engagements into it.
- A sponsored appearance is not a deal. It stays on the guest row with a Payment column, because it is the same person, the same thread and the same owner.

## Engagements: the guest table

### Status (one column, in journey order)

| Status | Means | Inbound | Outbound | Sponsored route |
|---|---|---|---|---|
| New | Pitch received, or target approved for outreach | yes | yes | |
| Contacted | Invite sent, chasing a reply | | yes | |
| Interested | They replied yes, eval next | | yes | |
| Decision pending | Eval done, Akshay to decide. Also after a precall | yes | yes | |
| Precall requested | Precall offered, chasing for a slot | yes | yes | |
| Precall done | Precall happened, back to Decision pending. For sponsored guests this is the planning call | yes | yes | yes |
| Sponsored offered | Commercials shared, waiting on them | yes | yes | yes |
| Booking | Yes to record, no date yet. For sponsored, agreed and awaiting first payment | yes | yes | yes |
| Booked | Recording date set. Next date = recording | yes | yes | yes |
| Recorded | Done, form sent to guest, form chasers run | yes | yes | yes |
| Form filled | FT form in (pics, designation, links). Last active status; Episode carries release | yes | yes | yes |
| LT chase | Still want them, not now: a timing reason, or no reply to the precall request or invite. Revisit on Next date | yes | yes | |
| Parked | Akshay has lost interest. Mamatha stops following up. Akshay only. Counts as closed | yes | yes | yes |
| They declined | Said no to organic or sponsored | yes | yes | yes |
| We declined | Akshay or host said no | yes | yes | yes |
| Unresponsive | Chase ladder exhausted, silence | yes | yes | yes |

The sponsored path in order: Sponsored offered, Booking (agreed), Precall done (planning call), Booked, Recorded, Form filled. The money runs alongside in Payment.

"Add to outbound" is a move, not a status: the PR agency dropped out, so Direction flips to Outbound, Status to New, and the history stays in Activities.

"Released" is not a guest status. It lives on the Episode (Status = Published).

### The other columns Mamatha sees

| Column | Options | Who sets | Why |
|---|---|---|---|
| Direction | Inbound, Outbound | Agent on creation, Mamatha | Inbound = pitched to us. Outbound = we reached out. Separate tabs |
| Tier | Tier 1, Tier 1.5, Tier 2 | Akshay | Importance to us: how hard we chase, which slot they get |
| Route | Sponsored, Organic | Akshay | Sponsored = the guest pays; Payment and Amount apply. Replaces Decision and Tier = Sponsored (decision 66) |
| Call type, Call link | Precall, Recording, Planning call; URL | Calendar sync | What Next date is when it is a call, and the Zencastr, Riverside or Meet link |
| Payment | Not started, GST received, Invoice 1 sent, Payment 1 received, Invoice 2 sent, Payment 2 received, Settled | Mamatha, agent from mail | Sponsored guests only. Hidden otherwise |
| Amount | number | Mamatha | Sponsored fee |
| Next action | one line | Mamatha, agent | What happens next |
| Next date | date | Mamatha, agent | When. Drives chasers, reminders and the recording |
| Chase step | 0 to 5 | Agent | Where on the follow-up ladder |
| Eval verdict | Book immediately, Strong consider, Evaluate after call, Decline | Agent | Hidden by default; the eval is a link away |
| Eval link, Dossier link | url | Agent | |
| Guest, Stakeholders, Via, Organisation, Episode | relations | Agent | Who, the PR people, who brought it, the company, the episode |

Removed from Engagements: Stage, Outcome, Whose move, Heat, Pitch link, Rank, Host verdict for FT (kept for un#, B2S, HBD where the host is not Akshay). Type collapses into Direction once PaaS moves to Deals; Sponsor, Partner, Vendor rows go to Deals too.

Tier here is pre-recording importance. The Episode keeps its own production tier tag (Tier 1, Tier 2, Tier 3 Spotlight), set by the one tap after recording and defaulting from this Tier.

### Mamatha's tabs on Engagements

Three tabs, no more:

- **FT: Pipeline**: every open row, inbound and outbound, chasing and parked, recorded and form pending. Sorted by Next date. Status column does the separating.
- **FT: Outbound**: Direction = Outbound, open. Her cold-outreach list on its own.
- **FT: Sponsored**: Route = Sponsored, open, with Payment and Amount showing.

Open means Status is not They declined, We declined, Unresponsive or Form filled. History is a filter away on the Pipeline tab (clear the filter), so there is no separate "all guests" tab.

Each tab shows Name, Status, Tier, Next action, Next date, Route, Eval link, Guest, Stakeholders, and nothing else unless the tab needs it.

## Deals: the sales table (new)

One row per company we are selling production to. Every deal is warm or cold (decision 63):

| Warm or cold | How it starts | Today's source |
|---|---|---|
| Warm | Through an FT guest, a recording or an introduction | PAAS - FT tab (93 rows), the PaaS leads table |
| Cold outreach | Straight pitch by mail, LinkedIn or X | PAAS - Direct (1,434), PAAS new (104), US VC (774), HK/SG |

| Column | Options | Notes |
|---|---|---|
| Company | title | |
| Organisation, Contacts | relations | The people on the deal |
| From engagement | relation → Engagements | The FT guest row it grew out of, if any |
| Warm or cold | Warm, Cold outreach | Two tabs: Warm, Cold outreach |
| Stage | New, Contacted, Interested, In conversation, Proposal sent, Won, Parked, Declined, Unresponsive | Same shape as the guest ladder, so one mental model |
| Heat | Hot, Warm, Cold | Akshay's read |
| Proposal link | url | The short link to the PaaS proposal, standalone as asked |
| Pitch note | url | The full proposal page with pricing (artifact or Doc) |
| Guest note, Chat link | url | Guest-facing note for the client show; the Claude chat where the pitch was built |
| Fit rank | number | Cold list ranking, 1 first |
| Budget read | text | From the US VC enrichment |
| Amount | number | Monthly or total, once quoted |
| Next action, Next date, Chase step | | Same as Engagements |
| Tags | Has podcast, Priority A/B/C, No email | |
| Activities | relation | Every mail and call |

Later, the same table takes show sponsors and partner deals, with a Kind column (PaaS, Sponsor, Partner). Not needed now.

## Where today's sheet values land

| Raw (count) | Status | Also |
|---|---|---|
| TBD (108), "Akshay has to decide" | Decision pending | |
| Precall Scheduled (2), route "Preliminary call", "Asked for pre call" | Precall requested | Decision = Precall |
| "Precall done", "Planning call done" | Precall done | |
| Sponsored (53), route "Sponsored", "Commercials shared" | Sponsored offered | Tier = Sponsored, Decision = Sponsored |
| Paid (7), Paid tab rows | Booking, Booked or Recorded by milestone | Tier = Sponsored, Payment from the checkboxes, Amount |
| To be Scheduled (14) | Booking | Decision = Book |
| Scheduled (13) | Booked | Next date = recording |
| Recorded (2) | Recorded | |
| Form Filled (89) | Form filled | |
| P1 (62) on Inbound | Status from the matching P1 row, else Decision pending | |
| P2 (47), Maybe Later (4), Later (1) | Parked | Next date from the sheet, else 90 days out |
| LT Chase (17) | LT chase | |
| Chase (16), Interested (4) | Status they were chasing from; outbound Interested | Chase step from the follow-up columns |
| Add to outbound (13), Approved (154 cold leads) | New, Direction = Outbound | |
| Declined (288) | They declined, or We declined where the note says Akshay or "Decline by Akshay" | |
| Unresponsive (136), Bounced (8) | Unresponsive | Bounced also tags the email invalid |
| Propsed Alt (11) | They declined | The substitute becomes a New row |
| Tier 1, Tier 2 in the eval column | Tier | |
| PAAS tabs, PaaS leads, US VC, HK/SG | Deals, not Engagements | Stage from Cold = New, Emailed = Contacted, warm = Interested, In discussion = In conversation |

The eval column maps to Eval verdict where it is a label and to Eval link where it is a URL. Doc titles (173 rows) get neither; the enrichment routine looks them up later.

## What changes in Notion, in order

1. Create Deals. Move the 788 PaaS rows and the 1 Client row across with their fields. Repoint the Queue and Activities relations.
2. On Engagements: add Status, Direction, Tier, Payment; fill them from Stage, Outcome, Type and Decision for the 227 existing guest rows (all Recorded or Form filled, since they came from Blue).
3. Remove Stage, Outcome, Whose move, Heat, Pitch link, Rank, Type.
4. Rebuild Mamatha's tabs.
5. Migrate the FT Pipeline sheet's open rows (about 350) into Engagements with the mapping above, duplicates to a review list.
6. Update the inbox agent to write Status, Direction, Tier and Decision from the mail (done: capture-only agent, decision 62).
