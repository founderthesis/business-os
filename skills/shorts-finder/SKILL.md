---
name: shorts-finder
description: >-
  Find the shorts in a podcast transcript and deliver them as a reviewable
  menu. Works for any podcast in the network: Founder Thesis (Akshay Datt),
  un# (Sri Misra), Built to Share (Satish Mugulavalli), or Human by
  Design (Arjun Jain). Proposes two formats: single-moment shorts (one
  contiguous verbatim range) and listicle compilations (4-6 spliced sound
  bites on one spine). Trigger on "/shorts", "shorts finder", "find the
  shorts", "identify shorts in this transcript", "what shorts can we cut
  from this", "clip options for this episode", "reels from this episode",
  "shorts for [guest]", or whenever a transcript is pasted with intent to
  pull short-form video from it. Takes a transcript with timestamps,
  optionally a dossier. Produces ONE interactive HTML artifact where every
  field has its own copy button, the reviewer ticks the shorts they want,
  and the selected set exports as a cut sheet. Every spoken word is
  verbatim.
---

# Shorts Finder

Read a full episode transcript and hand back the shorts worth cutting, as a menu the host or producer can review in one pass and pick from. The skill does the mining and the judgment. The reviewer does the picking.

Output feeds two people: whoever picks the shorts, and whoever cuts them. So every candidate has to be **findable in the audio** (real timestamps, verbatim words) and **decidable in five seconds** (a headline and a reason, not a paragraph).

## What this skill produces

ONE self-contained HTML artifact. It shows 8-12 single-moment candidates plus 2-3 listicle compilations, each as a card with a copy button on every field, a keep checkbox, and a live counter. The reviewer ticks the ones they want and exports the selected set as a cut sheet.

If the environment writes files (`present_files`), write the `.html` to the outputs directory. Otherwise render it as an artifact.

## Inputs

1. **Transcript** (required). With timestamps. Read it end to end before proposing anything.
2. **Dossier or episode notes** (optional). Use to spot which claims are the episode's real payload.
3. **Direction** (optional). "Only the AI stuff", "shorts for LinkedIn", a target count. Filters extraction.

## Step 1: Identify the show and what travels

| Podcast | Host | What travels as a short |
|---|---|---|
| Founder Thesis | Akshay Datt | Operator mechanics with a number in them. The hard decision, the unit economics, the thing that sounds expensive to have learned. |
| un# | Sri Misra | The contrarian structural take. A claim about where crypto or institutions actually go, stated flatly. |
| Built to Share | Satish Mugulavalli | The ownership or people decision. What a founder gave up, who they bet on, what it cost. |
| Human by Design | Arjun Jain | The distinctive research claim and its implication for a normal person. |

If it is unclear which show, ask once and stop.

## Step 2: Walk the transcript and find single-moment candidates

Go end to end. Flag every stretch that could stand alone as a video. Aim for **8-12 candidates** on a full episode. Be generous here; the reviewer wants a real menu, not three safe picks.

### What makes a short

- **The first line is the hook.** The range must open on a line that earns the next three seconds by itself. If the strongest line is 20 seconds in, the range starts too early. Move the start.
- **One idea.** A short answers exactly one question. Two ideas in one clip means two shorts, or a weaker one.
- **Self-contained.** It lands without the previous ten minutes. If it needs a setup the viewer never heard, reject it or start the range at the host question that supplies the setup.
- **A payoff, not a preamble.** Something resolves: a number lands, a decision gets named, a belief gets contradicted.
- **Concrete.** Names, numbers, prices, dates, a specific company, a specific mistake. Abstract advice does not travel.
- **Ends on a beat.** The last line should feel like a full stop, not a trailing "so, yeah". Trim to the real ending.

### Duration

Target **15-90 seconds** of speech, which matches what the editor tool accepts. The sweet spot is **30-60 seconds**, roughly 3-8 sentences. Under 15 seconds gets rejected downstream; over 90 needs a reason.

### What to reject

- Host monologue or a question with no answer attached.
- Anything that needs a chart, a screen share, or a "as I showed you earlier".
- Industry truisms with no receipt behind them.
- Sections where the transcript is visibly garbled or the speaker attribution is wrong. Do not propose a range you cannot vouch for word for word. Flag it in chat instead.
- Anything the guest asked to cut, or off-air talk.
- Near-duplicates. If two ranges make the same point, propose the tighter one only.

### Speakers

A short is usually the guest. Include a host line **only** when it is inside the contiguous range and it is the setup the payoff needs. Never open a short on a long host wind-up.

## Step 3: Build listicle compilations

The listicle is the stitched format: one spine, 4-6 sound bites, one line each, cut back to back. "Five things a founder learns after a down round." It is the only place splicing is allowed.

Propose **2-3** of these per episode. Build each one like this:

- **Find the spine first.** A single question the episode answers more than once. If you cannot name the spine in six words, there is no listicle.
- **4-6 beats.** Fewer than four is not a list. More than six loses people.
- **One line per beat.** Each beat is a short verbatim range, typically 4-12 seconds. Every beat needs its own start and end timestamp, because the editor is making a separate cut for each one.
- **Order for escalation.** Beat one is the most immediately gettable. The last beat is the one worth staying for. Do not open on the strongest line here, this format works on accumulation.
- **Beats must be non-overlapping** and must not reuse a range already proposed as a single-moment short.
- **Every beat is verbatim.** Splicing means reordering real spoken ranges, never writing a connective line. If the list needs a bridge, the bridge is on-screen text made of words the guest actually said.

Add a **join note** for each compilation: any beat where the cut in or out will sound abrupt, and where to trim to fix it.

## Step 4: Write the fields for every candidate

Every card carries these, and every one gets its own copy button:

1. **Theme.** 1-2 words. Pricing, hiring, fundraising, churn, regulation, culture.
2. **Headline.** The on-screen title. 60 characters or fewer, punchy, no clickbait phrasing the guest would disown. This is the thing that gets typed into the editor, so it must be usable as-is.
3. **The question it answers.** One line, phrased the way a viewer would actually ask it. "How much runway do you need before raising a Series A?" This is what tells the reviewer whether the short has an audience, and it doubles as the description copy.
4. **Timestamps.** `start - end`, in the transcript's own format, copied exactly as they appear so the editor can find them. For a compilation, list one pair per beat.
5. **Verbatim transcript.** The exact spoken words of the range. No grammar tidying, no merging, no ellipses standing in for words. For a compilation, the beats in cut order, each labelled with its timestamp.
6. **Strength.** Strong / Good / Borderline. Be honest. A menu where everything is Strong is not editorial judgment.
7. **Why it works.** One sentence. What the viewer gets and why they would send it to someone.

## Step 5: Build the HTML artifact

ONE self-contained file. Inline CSS and JS, no external requests, **no localStorage**. Read the `frontend-design` skill before writing it.

**Header:** episode title, guest, total candidates, and a live counter of how many are selected.

**Cards:** one per candidate, single-moment cards first, then compilations in their own clearly labelled section. Each card shows the seven fields as labelled rows. Each row has a small copy button at the end that copies just that value. A **copy-all** button on the card copies the whole candidate as plain text. Copy buttons confirm visually on click, so the reviewer knows it landed.

**Selection:** a keep checkbox per card, unchecked by default. Selected cards are visually distinct. The counter updates live.

**Filters:** by strength and by format (moment / compilation). Keep it to two filters, this is a review tool not a dashboard.

**Export:** one button that produces a cut sheet of the selected candidates only, containing every field in the order above. Download it as `.docx` if the environment supports it, and always include a copy-as-plain-text fallback. If you generate a `.docx`, verify it opens (valid ZIP, correct CRC-32) before shipping.

## Self-audit before delivering

- Is every spoken word verbatim from the transcript? String-match a few ranges to be sure.
- Does every single-moment candidate open on its hook line, not on a wind-up?
- Is every range 15-90 seconds, with most in the 30-60 band?
- Are there 8-12 moment candidates and 2-3 compilations?
- Does every compilation have a nameable spine, 4-6 beats, per-beat timestamps, and a join note?
- Are the strength tags honest, with a real spread?
- Is every headline 60 characters or fewer and usable as-is in the editor?
- Do the timestamps match the transcript's own format exactly?
- Does every field have a working copy button, and does copy-all work?
- Is the file self-contained with no localStorage?
- Did I flag, rather than propose, any range where the transcript is garbled?

## Hard rules

- **Verbatim only.** Exact spoken words. No tidying, no paraphrase, no invented on-screen copy.
- **Splicing only in compilations.** A single-moment short is one contiguous range with one start and one end.
- **Real timestamps.** Copied from the transcript, never estimated.
- **No overlap.** No candidate reuses a range from another candidate.
- **Zero em-dashes** anywhere in the output.
- **Chat stays short.** Two or three sentences: the one short you would cut first, the compilation you would run, and anything you refused to propose and why. Do not restate the menu in chat, it is already in the artifact.
