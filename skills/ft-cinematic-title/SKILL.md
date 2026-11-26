---
name: ft-cinematic-title
description: >-
  Write the cinematic title card that appears at the top of a Founder Thesis
  episode, right after the opening. Trigger on "/ft-cinematic", "cinematic
  title", "title card", "the card at the start of the episode", "opening
  title", or whenever an FT transcript is supplied and the ask is for the
  on-screen title rather than the YouTube title. Produces 20 diverse options
  of 8 words or fewer, each with an honest fit assessment, spread across
  grand-scale and narrow-niche framings. This is an on-screen card, not a
  search asset - the YouTube title is a different job handled by
  ft-episode-titles.
---

# Founder Thesis — cinematic title

The card that tells a viewer why the next hour is worth it. It appears seconds into the episode, on screen, in silence or under music. It has to do its work in one read.

## Inputs

- **Transcript** (required)
- **Selected theme** (optional) — if one has been chosen from `ft-episode-themes`, anchor the strongest options to it

## Output

**20 titles, maximum 8 words each.** Group them:

- **Grand scale / broad appeal** — the market, the national frame, the big number
- **Founder journey and strategy** — the arc, the pivot, the operating insight
- **Narrow and specific** — the ones that speak precisely to the people who will actually watch to the end

Under each title give a one-line **fit assessment**: how well it matches what is actually in the transcript, rated Excellent / Very good / Good / Moderate, plus the caveat where one exists. Be blunt. A title that overreaches is worse than a plain one, because the viewer who clicks on it leaves early and takes the episode's watch time with them.

House examples that worked:

> A peek into the brains building intelligent machines
> The American VC Fuelling India's Rural Growth
> The Truth about Blue-Collar Hiring
> The Inside Story of the Multi Billion Dollar E-commerce Aggregator

## It sits in the most expensive minute on the channel

Retention curves for Founder Thesis separate almost entirely between **second 30 and second 90**. At 30 seconds the best and worst episodes are indistinguishable; by 90 seconds the best holds 55% of viewers and the worst holds 15%. *(3-episode probe, Sep 2026 — see the FT Channel Rules page: https://app.notion.com/p/3d219a301a7f813fa919fe4b6c48a72f)*

Two consequences:

1. **Never stack packaging.** A trailer, then this card, then a spoken host intro spends the entire decisive window before the guest has said anything. Pick one opening device. If `ft-host-intro` is being used, this card should be brief or absent — flag the conflict rather than writing into it silently.
2. **Short beats complete.** Six words that land beat eight that explain.

## Claim, not category

The same split that governs thumbnail copy applies to anything a viewer reads on screen: **make a claim about a named subject; never label a category.**

- Works: `Fixing Supply Beats Creating Demand` · `Cracking India's Last Unbranded Staple`
- Fails: `The Climate AI Opportunity` · `The Future of Indian Manufacturing`

## Hard rules

- **8 words maximum.** No exceptions, and shorter is usually better.
- **No em dashes.**
- **Every claim supported by the transcript.** Where a title is instantly legible but slightly overreaches, say exactly that, as in: *"Good, with a caveat — the host raises the comparison and the guest complicates rather than accepts it."*
- Do not restate the YouTube title. The card and the title are seen by different people at different moments.

## Lessons
- 2026-11-26: "we dont need cinematic title un#" (Akshay, in the Ryan Louvar copy doc chat; decision 684). un# editing docs have no title card tab.
