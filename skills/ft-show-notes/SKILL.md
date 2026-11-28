---
name: ft-show-notes
description: >-
  Write the YouTube description for a Founder Thesis episode: hook, overview
  paragraph, key highlights, chapters with timestamps, and hashtags, in the
  exact published order and ready to paste into YouTube. Trigger on
  "/ft-shownotes", "show notes", "YouTube description", "episode description",
  "chapters and hashtags", or whenever an FT transcript is supplied and the
  ask is the description that ships with the video. Needs a timestamped
  transcript for chapters. Distinct from ft-substack-article, which writes
  the long-form written piece.
---

# Founder Thesis — show notes

The YouTube description. It does two jobs at once: convince a first-time visitor to press play, and carry the search terms that bring them there in the first place.

## Inputs

- **Transcript with timestamps** (required — chapters cannot be faked)
- **Guest name and company**, **host name** (Akshay Datt)
- **Primary SEO keyword** — one phrase. If not supplied, propose one and say so
- **Secondary keywords** — 3 to 5. Propose if not supplied
- **Selected theme** (optional) from `ft-episode-themes`

## Output, in this exact order

Ship it as continuous text with **no section headers and no labels**. The structure below is how you build it, not how it appears.

### 1. Hook — 2 sentences maximum

Curiosity-driven, aimed at someone who has never heard of this founder.

- Lead with a tension, a contradiction, or a surprising outcome
- **Do not open with the guest's name or company name as the first word**
- Work the primary keyword in naturally
- Banned openers: "In this episode", "Join us as"

> Good: *Most founders pitch VCs without knowing the math that decides their fate. In this conversation, Pranav Pai of 3one4 Capital breaks down the fund economics, portfolio construction, and the bets that built Licious and Darwinbox.*
> Bad: *Pranav Pai is a leading VC at 3one4 Capital. In this episode, we dive deep into his journey.*

### 2. Overview — 120 to 150 words, one paragraph

A magazine feature blurb. Specific, vivid, value-forward. No bullets.

Must contain: the guest's background and what makes it credible and unusual; the company's mission, current scale, and the precise problem it solves; two or three of the most specific or contrarian insights in the transcript; why this is timely against a real market trend; and Akshay woven in naturally rather than as his own sentence.

### 3. Key highlights — 5 to 6 bullets

Each a complete sentence opening with **How**, **Why**, **What**, or a direct verb. Specific: names, numbers, companies from the transcript. Never a generic bullet like "Founder insights on competition" — replace it with the actual insight.

The final bullet is the CTA:

> Subscribe to Founder Thesis for weekly founder conversations and follow Akshay Datt on LinkedIn [URL] for daily insights.

### 4. Chapters

Format exactly, no extra punctuation:

```
00:00 - Chapter Title
12:34 - Chapter Title
```

- **7 words or fewer** per title
- Each carries a keyword or a high search-intent phrase
- Curiosity or a clear benefit, never a dry summary
- Use real timestamps from the transcript

**On how many:** the house prompt says 6 to 10, but the published FT standard is far more granular — the Eggoz episode shipped with 24, one per genuine topic shift. Default to comprehensive coverage, because chapters are navigation as much as SEO. Say which you did.

### 5. Hashtags — 15 to 20, one line

Built from: guest name, company, sector, host, podcast, plus 8 to 10 long-tail search phrases. Mix broad (`#IndiaStartups`) with specific (`#Eggoz #AbhishekNegi`). At least three must match how a non-subscriber would actually search this topic. No spaces inside a tag.

## Hard rules

- **No em dashes anywhere.** Commas or simple dashes.
- **No section headers in the delivered text.**
- **Every number appears in the transcript.**
- Never keyword-stuff. If a keyword does not fit the sentence, leave it out.
