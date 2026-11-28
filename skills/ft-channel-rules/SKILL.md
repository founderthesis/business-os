---
name: ft-channel-rules
description: >-
  Analyse the full Founder Thesis history to work out what actually drives
  performance — title shapes, thumbnail copy, guest types, episode length, publish slots —
  and turn it into a living set of operating rules. Use this when the user says "what's
  working on the channel", "update the channel rules", "analyse our performance", "what
  titles work", "rerun the channel analysis", or asks why some episodes outperform others.
  Output is RULES the team can act on, never charts or dashboards. Re-run it monthly; each
  run updates the rules doc in place and records what changed.
---

# Founder Thesis — channel performance rules

You work out **what actually drives performance** across the whole Founder Thesis back
catalogue, and express it as **rules someone can follow**, not analysis someone has to
interpret.

**Scope: Founder Thesis only.** Exclude Spotlight entirely — it is a different show with a
different format and audience, and mixing the two muddies every rule. In Notion that means
filtering `Show = 'Founder Thesis'`; in the feeds it means the FT feed only.

The output is a living document. Every run updates it and records what changed — a rule
that stopped holding is as important as a new one.

Read `references/method.md` for the exact data assembly and the statistical bar.

## The one rule about output

**Rules, not charts.** Nobody wants a bar chart. Every finding must land as an instruction
with the evidence attached:

> **Put the guest's company in the title.** Episodes with the company name in the title
> average 2.4× the views of those without (n=189 vs 71, medians 412 vs 171).

Never produce a chart, a dashboard, or a "here are some interesting patterns" essay. If a
finding can't become an instruction, it isn't finished — keep working or drop it.

## Data: two tiers

**Tier 1 — always available, no exports.** Enough to run the whole analysis:
- **Podcast RSS** — the FT feed only, ~450 episodes: episode **title**, **publish date AND
  time**, **duration in seconds**. `https://feeds.zencastr.com/f/mbqvPYFP.rss`
- **YouTube channel dump** for video durations and titles:
  `yt-dlp --flat-playlist --print "%(id)s|%(duration)s|%(title)s" <channel>/videos`
- **Notion Episode Inventory** (`collection://6e563350-3261-4da5-89f8-4f4ec6d201ff`),
  filtered to `Show = 'Founder Thesis'` (460 rows): Substack **Views**, **Guest**,
  **Company**, **Theme**, **Article words**, **Article state**

**Tier 2 — needs a 2-minute export, and it's what unlocks the metrics people actually ask
about.** Impressions, CTR and retention are **YouTube Studio-only** — they are not public
and cannot be scraped. Ask the user to export:

> YouTube Studio → Analytics → Advanced mode → set the date range to "Lifetime" →
> Content tab → **Export → CSV**. That gives impressions, impressions CTR, average view
> duration and average percentage viewed, per video.

If the user provides that CSV, use it as the primary performance metric and say so. If they
don't, run on Tier 1 and **state plainly at the top of the output** that the analysis is on
views and Substack traffic, not impressions/CTR/retention.

**Never imply you measured impressions, CTR or retention when you only had views.**

## What to test

Work through these, and only report the ones that clear the evidence bar:

**Title shape** — company name present · guest name present · a number present · a money
figure · question form · "how/why" opener · colon vs pipe separator · character length ·
superlative or curiosity gap · category word ("D2C", "fintech")

**Thumbnail copy** — word count on the card · whether a number appears · whether the guest's
face is present · whether the company logo is present. (Fetch thumbnails via
`https://img.youtube.com/vi/<VIDEO_ID>/maxresdefault.jpg` and read the text off them.)

**Guest type** — founder vs VC vs operator · first-time vs repeat · company stage · whether
the company is a recognisable consumer brand

**Length** — duration banded (<30m, 30–45, 45–60, 60–75, 75–90, 90m+), against performance

**Publish slot** — day of week and hour, from the RSS `pubDate`

**Theme** — the Notion Theme tags, against performance

## Method, briefly

Full detail in `references/method.md`. In short: rank episodes by the performance metric,
compare the **top quintile against the bottom quintile**, and look for features that
separate them. A finding becomes a rule only if:

- **n ≥ 20** in each group for that feature, and
- the gap is **large enough to act on** (roughly 1.5× or more on the metric, or a 15+ point
  difference in a rate), and
- it **isn't explained by something else** — check the obvious confounder before claiming it

State the numbers behind every rule: both group sizes, both medians, the ratio.

**Beware the age trap.** Older episodes have had longer to accumulate views. Always compare
within similar publish periods, or normalise, and say which you did.

## Updating — this is the point

The rules live in a **Notion page** so they update in place and the other FT skills can read
them. On the first run, create a page called **"FT Channel Rules"** under the Substack Audit
Report and note its URL in your output. On later runs, find and update that page.

Every run:

1. Recompute all rules from current data
2. For each existing rule, mark it: **CONFIRMED** (still holds, update the numbers) ·
   **WEAKENED** (holds but the gap narrowed) · **OVERTURNED** (no longer true — say so
   loudly) · **NEW**
3. Rewrite the page with the current rules, each carrying its evidence and status
4. Append a dated entry to a **Changelog** section at the bottom: what changed and why

An overturned rule is the most valuable output a run can produce — it means the team has
been following something that stopped being true. Never quietly drop a rule; state that it
died and when.

## Output format

```
# FT Channel Rules — <date>
Based on <n> Founder Thesis episodes. Metric: <views | Studio impressions+CTR+retention>.
<one line on any data caveat>

## Titles
1. **<Rule as an instruction.>**
   <evidence: group sizes, medians, ratio>  [CONFIRMED since Mar 2026]

## Thumbnails
## Guests
## Length
## Publish slots
## Themes

## What we tried and found nothing
<features tested that showed no real effect — this stops the team re-litigating them>

## Changelog
- <date>: <what changed this run>
```

The "found nothing" section matters. A negative result stops someone wasting a month on a
theory the data already killed.

## Hard rules

- **Never invent a number.** Every figure traces to the data you actually loaded.
- **Never state a rule you can't back with group sizes.** "Shorter titles do better" is
  useless; "titles under 60 chars average 1.8× views (n=143 vs 96)" is a rule.
- **Say what you couldn't measure.** If there's no Studio export, say the retention and CTR
  rules are absent — don't quietly substitute views and call it the same thing.
- **Correlation is not instruction.** Before writing a rule, ask what else could explain it.
  If a confounder is plausible and you can't rule it out, mark the rule as tentative.
- Never publish anything or modify episode data. This skill reads and writes one rules page.
