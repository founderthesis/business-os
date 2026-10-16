# Email automation: draft, learn, then send (decision 102, built 9 Oct 2026)

Akshay's roadmap: now, agents send a few safe replies and pre-draft the rest; next two weeks, learn from his edits and his own mail and improve the templates; after that, he switches templates to agentic sending one at a time.

## Templates: one row per mail, with a mode

New fields on Templates (collection://b2976a03-9983-49e1-96cf-d237a395148d):

| Field | Type | What it does |
|---|---|---|
| Mode | Select: Off, Draft, Send | Off: nobody uses it. Draft: the routine puts a Gmail draft in ad@thepodium.in for Akshay to send. Send: the routine sends on a standing approval. Only Akshay moves a row to Send. |
| Trigger | Text | When it fires, in plain words ("FT recording ended", "new FT pitch, no reply in 72h", "episode Planned release in 7 days"). The routine that owns it reads this. |
| Owner routine | Select: inbox, calendar, evals, daily sweep, none | Which routine drafts or sends it. |
| Uses | Rollup | Count of Activities linked to the template. |
| Drafts sent | Rollup | Agent drafts that went out with Edit size set (sum of the Activities formula Draft sent). |
| Clean sends | Rollup | Drafts sent with Edit size None or Minor (sum of Clean send). |
| Ready to send | Formula | "Ready" when Drafts sent >= 8 and Clean sends >= 80% of them. Hand-written mails count in Uses only, so they never hold a template back. A signal for Akshay, never an automatic switch. |
| Proposed wording | Page section | The learning job writes a suggested new version under a "Proposed" heading in the page; Akshay accepts by moving it into the body and bumping Version. |

Approved and Version stay as they are.

## Activities: the learning record

New fields on Activities (collection://290f715d-fd45-4203-ade6-3642c2326c6c):

| Field | Type | What it does |
|---|---|---|
| Template | Relation to Templates | Which template a sent mail came from or matches. |
| Draft ID | Text | The Gmail draft id the routine created, so the sent mail can be compared with it. |
| Edit size | Select: None, Minor, Major, Rewritten | How much Akshay changed the draft before sending. |
| Edit note | Text | One line on what changed ("added the guest's company in the first line", "dropped the patron paragraph"). |

## The loop

1. Draft: the owning routine creates the Gmail draft from the template and logs an Activity (Kind Draft, Template, Draft ID, Engagement).
2. Capture: each night the inbox run finds mail Akshay or the team sent. If it came from a logged draft, it compares sent against drafted and fills Edit size and Edit note on that Activity. If it was written by hand but matches a template's purpose, it links the template too (so his own mail teaches the template as well).
3. Learn: once a week (daily sweep, Friday), for each template with edited sends that week, write a Proposed wording into the template page that folds in the repeated edits, and flag Akshay ("Templates: 3 proposed updates").
4. Graduate: after two weeks, templates showing Ready to send get listed for Akshay. He flips Mode to Send on the ones he trusts. Caps and the send log stay as today (100 a day, every send logged "Agent sent").

## Starting point

- Send now (already live): "Mamatha added to a new FT pitch", "Eval ready, in the pitch thread" (internal). Daily list to Mamatha (internal).
- Draft now: FT thank-you (live via the calendar routine), pre-release asks for all four shows (needs a trigger on Episodes: Planned release 7 days out), vendor pitch redirect.
- Off for now: anything Mamatha or Chaandini send from their own mailboxes (myunnati.com). The connector only reaches ad@thepodium.in, so the agents can't draft there; those templates still help as reference and for learning from what they CC to Akshay.
