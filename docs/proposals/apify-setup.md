# Apify setup: what Akshay needs to decide (tab 11, items 20 and 21)

Akshay prefers Apify for two jobs:
- **LinkedIn lookups** (item 20), such as the 1,762 People rows with no LinkedIn.
- **X research in un# dossiers** (item 21).

No session has an Apify connector or token yet. Nothing is built until he agrees to the setup below.

## What's needed

1. **An Apify account** on Akshay's or ThePodium's billing. Apify bills per result, so the cost is pay-as-you-go.
2. **The connector.** Apify runs an official hosted MCP server at `https://mcp.apify.com`. There are two ways to connect it:
   - **Preferred: a claude.ai custom connector with OAuth.** Akshay adds it once in claude.ai connector settings and signs in to Apify in the browser. The token never appears in any prompt or file, and routines and Cowork tasks get the connector the same way they get Notion.
   - **Fallback: an API token** from Apify Console > Settings > Integrations, sent as `Authorization: Bearer <token>`. It goes only in the environment's secrets, never in a prompt, the repo or Notion (CLAUDE.md: no credentials in committed files).
3. **Which environment gets it:**
   - The Cowork environment that runs the un# dossier skill (item 21).
   - The builder environment, for a one-off LinkedIn enrichment run (item 20).
   - Not the hourly routines: neither job is hourly.
4. **A spending cap** set in Apify's billing, say USD 20 a month to start, so one misbehaving run can't run up the bill.

## Cost per 100 lookups

Prices come from community-built scrapers (Apify calls them Actors) on the Apify Store. They change, so these are listing-page figures from 28 Oct, not quotes.

| Job | Typical listed price | Per 100 |
|---|---|---|
| LinkedIn profile, no login, basic fields (name, headline, location) | USD 1.2 to 2 per 1,000 | USD 0.12 to 0.20 |
| LinkedIn profile with experience and education | USD 3 to 8 per 1,000 | USD 0.30 to 0.80 |
| LinkedIn profile plus email search | about USD 9 per 1,000 | about USD 0.90 |
| X posts (tweets) | USD 0.15 to 0.40 per 1,000 posts | USD 0.02 to 0.04 per 100 posts |

**Rough totals:**
- **Item 20:** 1,762 profiles with experience is about USD 5 to 14, one-off.
- **Item 21:** a un# dossier reads maybe 200 to 500 posts, so a few cents each. One tested comparison found an Actor billing far above its listed rate on small runs, so check the first run's real cost.

## Risks to put to Akshay

- **Third-party Actors:** these are community scrapers, not Apify's own. The "no cookies, no ban risk" claims are the developers' marketing. We'd never give one his LinkedIn login.
- **Data rules:** found LinkedIn URLs and profile facts go on People rows with provenance (Source Apify, the Actor name, the date). Emails from an email-search Actor stay off unless he asks for them.
- **The un# dossier skill:** Akshay updated it himself. Before any change, skills/un-dossier is re-synced from his live copy.

## The ask

1. Yes or no to an Apify account and a monthly cap. Which card, and what cap?
2. OAuth connector (preferred) or a token in the environment's secrets?
3. For item 20: basic fields only (cheapest), or experience too?
