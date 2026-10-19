# Source-page access for guest research (decisions 342, 343)

Misc session, 19 Oct 2026. Diagnosis only; nothing changed.

## What fails and why

- Web search works: it runs outside the session container.
- Opening a page does not. curl to techcrunch.com, inc42.com, en.wikipedia.org, businesswire.com, entrackr.com, browserstack.com and bloomberg.com: the egress gateway answers 403 to CONNECT ("policy denial"). pypi.org returns 200.
- WebFetch fails the same way: "getaddrinfo ENOTFOUND inc42.com".
- Cause: the environment's Limited network access allows package managers only. No source site is allowed, so numbers can be checked only against search-result snippets.

## Why "allow every cited domain" is not the fix

The 358 finished records cite 736 links across 323 domains. The top 40 domains cover only 52% of links, and 12% of links are aggregator estimates (Latka, Sacra, Tracxn-style sites) that should not back a number anyway.

## Minimum allow-list (keep Limited, add these under Allowed domains)

Twelve hosts:

- **Indian business press:** inc42.com, entrackr.com, yourstory.com, economictimes.indiatimes.com, livemint.com, www.business-standard.com
- **Global press and newswires:** techcrunch.com, www.reuters.com, www.businesswire.com, www.prnewswire.com
- **Filings:** nsearchives.nseindia.com, www.sec.gov

Optional, for identity and role only (never numbers): en.wikipedia.org.

Not worth adding: Bloomberg and Moneycontrol (paywalled or bot-blocked), Crunchbase (bot-blocked), and the aggregators.

These 12 already back 24% of today's links. Company press releases reach most of them through the newswires.

## How verification would work with the list

1. Each kept number (one to three per person) must cite one of the 12 hosts. If a worker's source is elsewhere, the verifier searches for the same fact restricted to these hosts.
2. The verifier opens that page and keeps the number only if the page states it with the same date, period and metric type. Otherwise the number is dropped.
3. Tier, tags and role do not depend on page access and are kept as they are. A tier that rested only on a dropped number is marked Needs research.
4. Expected work: about 350 verified people times 1 to 3 fetches. Fetches are not counted against the 200-search cap; re-sourcing searches are.

## Held until access works

No further bulk research, no bulk Notion write, no shortlist view. The 348 records (plus the 10 pilot rows already on People) are kept in the session scratchpad. No Kimi or other API is set up.
