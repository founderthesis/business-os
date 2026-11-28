---
name: "paas-eval"
description: "Check if a company and contact are a good fit for Unnati's podcast-as-a-service pitch. Trigger on /paas-eval or 'PAAS Eval' with a company name or LinkedIn URL."
---

# PAAS Eval

Akshay gives a company name or a LinkedIn URL. Research it, score it against the checklist below, and publish the result as an HTML artifact (format at the end). Plain, simple English. No em-dashes.

## What we sell

Unnati runs a podcast for a company. The founder hosts. The guests are the people the company wants to sell to. Each episode is an hour with a senior buyer who would ignore a cold email. The company owns the channel. Standard cost is about Rs 12 to 13 lakh for 12 episodes over 6 months.

Our proof:
- Founder Thesis (Akshay Datt). 500+ episodes, 2M+ views. The show is how Unnati gets its own clients.
- Built to Share (Satish Mugulavalli, Hissa). Seed-stage ESOP company, about 38 people, Rs 4 Cr revenue.
- Human by Design (Dr. Arjun Jain, Fast Code AI). Bootstrapped AI services firm, about 60 people, Rs 4.8 Cr revenue.
- un# (Sri Misra, aarna). Small DeFi startup, about $1.5M raised. Non-compete: never pitch DeFi or crypto companies.
- FieldAssist (Divir Tiwari), our newest client. Bootstrapped CPG sales SaaS, Gurugram, about 450 people, Rs 66 Cr revenue, sells in 32+ countries. Came in as a Founder Thesis guest. Show: Pathfinders, presented by FieldAssist.

## What the data says (Deals database, Oct 2026)

- Warm leads convert. Almost every deal at Proposal sent or Won started as a Founder Thesis guest who was pitched after the recording (Bicycle AI, SecurEyes, Bluehill, Cygnet, Josh, Wissen, Assiduus, SilverX, Alligator, Codewave, Damsun, FieldAssist).
- Cold outreach to US startups mostly fails. About 50 went No reply and 13 said No. The few cold leads that turned Interested (Nexla, Sorcero, Gather AI, Lema) came through the FT-guest-first route.
- The sweet spot is a founder-led Indian B2B company, Rs 20 to 500 Cr revenue or Series A to C, 50 to 3,000 people, selling high-ticket deals to senior buyers, often abroad.
- A podcast that stopped is a plus. Damsun ran 2 episodes and quit. Nexla ran 10 and went quiet. They already want a show and know they can't run it alone.
- Weak fits: consumer or low-ticket businesses (GyanDhan), funds waiting on a close (SilverX stalled), very large firms where the deal moves to a marketing team (Cygnet slowed).
- A past FT guest whose PR agency pitches them again for FT is a production-pitch opening. Decline the repeat FT slot and offer the show instead (QubeHealth, Oct 2026).

## The checklist (score out of 10)

1. **Warm path (0 to 3).** 3 = already a Founder Thesis guest or a personal intro. 2 = India connection, so the FT guest invite can come first. 0 = cold, no India link.
2. **Sells high-ticket B2B to senior buyers (0 to 2).** 2 = enterprise deals, buyers are CXOs, bank heads, plant owners, LPs. 1 = mid-ticket. 0 = consumer or self-serve.
3. **Can pay (0 to 2).** 2 = Rs 20 Cr+ revenue or Series A+ funding, 50+ people. 1 = smaller but profitable or seed with a clear budget. 0 = pre-seed, tiny, or cash-strapped.
4. **Founder can host (0 to 1).** 1 = sitting founder-CEO who is visible (talks, LinkedIn, past podcast guest spots). 0 = hired exec, departed founder, or very private.
5. **Podcast status (0 to 1).** 1 = no show, or a show that stopped. 0 = an active show they run well.
6. **Growth moment (0 to 1).** 1 = new market, new product, fresh funding, new fund. 0 = nothing moving.

**Verdict:** 7 to 10 = Pitch. 5 to 6 = Maybe. 0 to 4 = Skip.

**Automatic Skip:** DeFi or crypto (un# non-compete), consumer low-ticket, pre-seed, clinical biotech or medical devices, acquired company, founder already left.

## Best person to pitch

- Default: the founder-CEO. They host, they sign.
- Two founders: pitch the one who is more public, and say both can host (Codewave did two series).
- 1,000+ people: still pitch the founder, but name the marketing head who will run it day to day.
- Fund: the managing partner who meets founders and LPs.

## How to run it

1. **Check our own records first.** Search the Notion Deals database (collection://1a981c5a-912a-4972-b3fc-8c9f2abb329a) by company name. If it's already there, note its Stage and Result. Also check whether the person has been a Founder Thesis guest (Engagements database collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5, Episodes, Activities, and project memory). A past FT guest is the warmest lead for this pitch. If an inbound PR pitch for the same person is sitting in Activities, say so: it's the route in.
2. **Learn from results.** Read the Result column (Yes, No, No reply). Where Result is empty, read Stage: Won = Yes, Declined = No, Unresponsive = No reply. Find the 2 or 3 past deals most like this company (size, sector, warm or cold, region). If they mostly went No reply, lower the score by 1 and say so. If they mostly said Yes, raise it by 1. As more results come in, update the "What the data says" section of this skill.
3. **Research.** WebSearch and WebFetch: what they sell and to whom, HQ and markets, headcount, funding or revenue, founder name and title, co-founders, India connection, any podcast or YouTube interview series (episode count, last date). Check the company's own leadership page; Crunchbase, GetLatka and Tracxn are often stale. Mark estimates "est.".
4. **Score** each checklist line, with a one-line reason per line. The reasons go on the page.
5. **Build and publish** the artifact below. Load the artifact-design skill first.

## Output: HTML artifact

Every eval is published as its own artifact. Don't put the full eval in chat.

- File: `<company-slug>-paas-eval.html` in the scratchpad. One file per company. Re-running the same company republishes the same file.
- `<title>`: `<Company> PaaS Eval`. Icon: `scorecard`. Description: one sentence naming the contact, company and verdict.

Page sections, top to bottom:

1. **Header.** Eyebrow `PaaS eval · <date>`, the company name as H1, one line on what they do and who pays.
2. **Records flag** (only if it applies). An amber callout: already in Deals (Stage and Result), past FT guest (episode number and title), or an inbound PR pitch on file. Say what that means for the route in.
3. **Verdict band.** Big score `X/10` beside a pill (Pitch / Maybe / Skip) and two sentences on why and what to do next. Pill colour: teal for Pitch, amber for Maybe, muted grey for Skip.
4. **Scorecard.** The six checklist lines as rows: name, `points / max` in mono on the right, a segmented bar (one segment per point; filled = earned, amber = docked), and the one-line reason under it. If the deal-history adjustment (+1 / -1) applied, add it as a seventh row.
5. **The pitch.** A label/value list: Pitch to (name, title, why them; name the co-founder or marketing head if relevant), Angle (the show and who it gets them in a room with), Route in (how the first message reaches them: post-recording, PR agency reply, FT invite first, etc.).
6. **Sources.** Short linked list, plus the Notion rows used.

Design: clean single-column brief, max width about 760px. Bricolage Grotesque for display, IBM Plex Sans for body, IBM Plex Mono for labels and points. Cool off-white ground with a teal accent and amber for flags; full dark-mode tokens. Works at phone width.

After publishing, reply in chat with one line: the verdict and score, and that the page has the scorecard, pitch and sources. No email drafts unless asked.