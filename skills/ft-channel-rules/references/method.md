# Method — assembling the data and setting the evidence bar

## Step 1: build the dataset

Work in a scratch directory. Aim for one table, one row per episode.

### a. Podcast RSS — title, publish datetime, duration

```
FT: https://feeds.zencastr.com/f/mbqvPYFP.rss     (~450 items)
```
**Founder Thesis only.** Do not pull the Spotlight feed — it is a different show and its
episodes must not enter this dataset.

Per `<item>`: `<title>`, `<pubDate>` (RFC-822, gives **day of week and hour**),
`<itunes:duration>` (seconds). This is the only reliable source of publish time — the
Notion `Published` column is empty on all 582 rows.

### b. YouTube — durations, titles, video IDs

One flat dump beats per-video calls, which get bot-walled fast:

```
yt-dlp --flat-playlist --ignore-errors --no-warnings \
  --print "%(id)s|%(duration)s|%(title)s" \
  "https://www.youtube.com/channel/UChwUqkuczHA_d-TV3n0LN9w/videos"
```

Shorts come back with no duration — that's how you tell them apart. Exclude anything under
20 minutes from performance analysis: they're clips, not episodes, and they distort everything.

### c. Notion Episode Inventory

`collection://6e563350-3261-4da5-89f8-4f4ec6d201ff`, filtered `WHERE "Show" = 'Founder Thesis'`
(460 rows) — take **Views** (Substack article views), **Guest**, **Company**, **Theme**,
**Article words**, **Article state**, **YouTube URL**.

Join Notion to the other sources on **YouTube video ID** (extract from the URL). This is
exact; title matching is not — don't use titles as the join key.

### d. Thumbnails, if testing thumbnail rules

`https://img.youtube.com/vi/<VIDEO_ID>/maxresdefault.jpg` — read the text off the image.
Record: word count, whether a number appears, face present, logo present.

### e. Tier 2 — the Studio CSV, if provided

Columns you want: Impressions, Impressions click-through rate, Average view duration,
Average percentage viewed. Join on video title or ID. **This is the only source of
impressions, CTR and retention.**

## Step 2: pick the metric, and be honest about it

Priority order:
1. **Studio CTR + average percentage viewed** — the real answer, if the export exists
2. **YouTube views** — decent proxy for reach
3. **Substack article views** — only measures the article, not the episode

Whichever you use, name it at the top of the output.

## Step 3: normalise for age

Older episodes have had longer to accumulate. Either:
- **Bucket by publish period** (e.g. per year) and compare within buckets, or
- Use **views per month since publish**

Say which you did. An un-normalised "older episodes do better" finding is an artefact, not
a rule, and it's the single easiest way to produce a confidently wrong document.

## Step 4: winners vs losers

Rank by the metric. Take the **top 20%** and the **bottom 20%**. For each feature, compute
its prevalence in each group.

Report as: feature, n in each group, median metric in each, and the ratio.

## Step 5: the bar a finding must clear to become a rule

All three:

1. **n ≥ 20** in each group for that feature — below that it's noise
2. **A gap worth acting on** — roughly ≥1.5× on a continuous metric, or ≥15 percentage
   points on a rate. A 6% difference is not an instruction.
3. **Survives the obvious confounder.** Before writing it, ask: what else explains this?
   - Famous guests get more views regardless of the title → check whether the title rule
     still holds *within* the non-famous group
   - Recent episodes have better thumbnails *and* better distribution → compare within period
   - Long episodes are usually the big-name guests → check length within guest tier

   If a confounder is plausible and you can't separate it, mark the rule **tentative** and
   say what would settle it.

## Step 6: write rules, not observations

Bad: *"There's a correlation between title length and views."*
Good: **"Keep titles under 60 characters."** Titles under 60 chars median 412 views vs 171
for longer ones (n=143 vs 96, 2.4×). Holds within both the famous and non-famous groups.

Every rule: an imperative, then the evidence, then its status.

## Step 7: the negative results

Keep a list of everything tested that showed **no** effect, with the numbers. This is not
filler — it's what stops the team relitigating "should we try question titles?" every
quarter. A tested-and-dead theory is a real deliverable.

## Step 8: diff against the previous run

Load the existing rules page first. For each prior rule, recompute and mark **CONFIRMED /
WEAKENED / OVERTURNED**, then add anything **NEW**.

Write the changelog entry in plain language:

> **4 Oct 2026** — "Numbers in titles win" OVERTURNED: gap fell from 2.1× to 1.1× as more
> episodes adopted them; the edge was novelty, not the number. New rule on publish slot
> (Tue 06:30 vs Sat) added, n=210.

That entry is often the most useful thing in the document.
