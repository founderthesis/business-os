---
name: podcast-intro-voiceover
description: >-
  Generate a spoken intro voiceover for any of the 4 podcasts in the network:
  Founder Thesis (hosted by Akshay Datt), un# (Sri Misra), Built to
  Share (Satish Mugulavalli), or Human by Design (Arjun Jain). Trigger on
  phrases like intro vo, intro voiceover, episode intro, opening line,
  voiceover for the episode, pre-interview teaser, recording intro before
  the interview, or any podcast-name-specific cue. Supports two modes:
  post-recording (default, transcript-based, tease references specific
  moments) and pre-interview (dossier-only, tease references topic
  territory). The skill asks which podcast and which mode if either is
  unclear, then loads that podcast's reference file and outputs 5
  variations plus a recommended pick. Reads aloud, so no em-dashes, no
  buzzwords without unpacking, no markdown.
---

# Podcast Intro Voiceover

Generate a short spoken intro that the host reads at the start of an episode. The intro plays before the conversation begins and is reused in episode promotion on LinkedIn. This skill is shared across 4 podcasts in the network, each with a different host, audience, and structure.

## Step 1: Identify the podcast AND the mode

### Podcast

The 4 podcasts in the network:

| Podcast | Host | Topic | Reference file |
|---|---|---|---|
| Founder Thesis | Akshay Datt | Indian startup founders | `references/founder-thesis.md` |
| un# | Sri Misra | Crypto, DeFi, CeFi, Web3 | `references/unhashed.md` |
| Built to Share | Satish Mugulavalli | Talent wars, team building | `references/built-to-share.md` |
| Human by Design | Arjun Jain | AI builders and production reality | `references/human-by-design.md` |

Before doing anything else, identify which podcast this is for:

- The user may state it explicitly ("intro for Built to Share", "Sri's show", "un# intro").
- Context may make it obvious: a transcript about DeFi or stablecoins → un#; about hiring, ESOPs, attrition → Built to Share; about computer vision, model training, edge AI → Human by Design; about Indian startup scale stories → Founder Thesis.
- If unclear, ask once with the 4 options. Do not guess.

### Mode

Two modes are supported:

- **Post-recording mode (default).** The interview has happened. A transcript exists. The episode tease references specific moments, decisions, numbers, or framings the guest actually said.
- **Pre-interview mode.** The interview has not happened yet, or the host wants to record the intro VO before listening back. Only a dossier exists. The tease references topic territory the conversation is *expected* to cover, not specific reveals.

Detect the mode:

- **Pre-interview signals:** "pre-interview", "before the interview", "no transcript yet", "haven't recorded yet", "draft from the dossier", "teaser", "for the trailer", or the user provides only a dossier when a transcript would normally be expected.
- **Post-recording signals (default):** user provides a transcript, references quotes or moments from the conversation, says "draft an intro for this episode", or attaches a transcript file.
- **Ambiguous:** if the user names a guest and asks for an intro without attaching a transcript or saying "post-recording", **ask once**: "Has the interview been recorded yet? If so, share the transcript. If not, I'll draft a pre-interview version from the dossier — flagging that the tease will reference topic territory rather than specific moments."

Do not guess on mode. Generating a post-recording intro with no transcript will produce fabricated moments, which is a serious failure mode.

## Step 2: Read the matching reference file

Once the podcast is identified, **read the matching reference file in `references/`**. Each reference file is self-contained and contains everything specific to that podcast: audience, structure, target word count, scale-signal guidance, hook library, worked example, and any voice quirks. Each reference file also has a **"Pre-interview mode" section** at the bottom that adjusts the tease language and hook angles for that podcast.

The reference file overrides any defaults in this SKILL.md when they conflict.

## Step 3: Input

The required input depends on mode:

**Post-recording mode (default) requires both:**

1. **The episode transcript** — usually a 60-90 minute interview. Use this for: dramatic moments, specific decisions, contrarian framings, mechanics, mental models, and stories that will tease the episode.
2. **A research dossier on the guest and company** — typically a PDF with scale numbers, funding, sector context, technical credentials. Use this for: credibility signals like capital raised, AUM, users, deployments, lab pedigree.

**Pre-interview mode requires only:**

1. **The research dossier** — same as above. This carries the full weight of credibility (parts 1 and 2 of the intro) and informs predicted conversation territory (part 3).

In pre-interview mode, **do not invent transcript content**. If you find yourself writing "Henry breaks down how DigiFT settles a tokenized T-bill" without a transcript to back it, you are fabricating. The correct framing is "we'll explore how DigiFT settles tokenized T-bills" or "expect a conversation about settlement mechanics, MAS regulation, and TradFi adoption".

The two sources (or one, in pre-interview mode) are enough. Do not ask for additional information.

## Step 4: Output

Return **5 variations**, each within the word count specified by the podcast's reference file, followed by a recommended pick. No preamble, no commentary about the process — start directly with `**Variation A`.

Format each variation like this:

```
**Variation A (Hook type):**
"[The voiceover, written as one flowing block for spoken delivery]"
```

After the 5 variations, end with:

```
My pick is **Variation X** because [one or two sentences on why this hook lands hardest for that podcast's audience].
```

## Universal style rules

These apply to every podcast regardless of reference file:

**Write for the ear:**
- Short sentences. Periods, not semicolons.
- Avoid parentheticals that interrupt flow.
- Read each draft mentally. If you'd stumble, rewrite.

**Do:**
- **Include the podcast name in the VO.** Every intro must contain the podcast's branded name at least once, spoken aloud. The default slot is the tease line ("In this episode of the Founder Thesis Podcast, Alok shares..."). Some podcasts also use an opening-line slot ("Steven Goldfeder joins us on the un# podcast..."). The exact canonical phrasing for each show is in its reference file. Do not abbreviate, do not paraphrase the name, do not skip it.
- Use concrete numbers ($500M, 55,000+, 240k followers, 2023, 30%).
- Name real brands, real people, real institutions (Swiggy, UPI, Polygon, Bitwise, Yann LeCun, Apple, Mercedes). They do credibility work that no adjective can.
- Reference specific years when teasing a story ("in 2023", "in September 2024") — signals the conversation has dates and details, not abstractions.
- Use plain language. State the fact, state the move, state the result.

**Don't:**
- **No em-dashes (—) or en-dashes (–).** Hard ban. They read as AI-generated and break spoken cadence. Use commas, periods, or colons. Hyphens in compound words ("AI-powered", "real-time") are fine.
- No buzzwords without unpacking: "agentic AI", "deep tech", "alternate data", "vertical SaaS", "TVL", "DeFi-native", "platform play". If you must use them, unpack with examples in the same sentence. (Each reference file specifies which terms can stay un-unpacked for that audience.)
- No hype words: "revolutionary", "groundbreaking", "disrupting", "game-changing", "trailblazing", "pioneering". "Pioneered" used once for a real first-mover claim is OK; otherwise cut.
- No generic teases: "masterclass", "shares his journey", "takes us behind the scenes", "deep dive into", "fascinating conversation about", "incredible insights". These promise nothing specific. Test: could this tease be pasted onto a different guest's intro? If yes, rewrite.
- No direct quotes from the guest. Paraphrase.
- No conversational filler from the transcript ("um", "right?", "you know").

## Pre-interview mode: what changes universally

Most of this skill is unchanged in pre-interview mode. The audience, host voice, structure, word count, currency rules, credibility signals, and style rules all stay the same. **Only the tease (final part of the intro) shifts.** Here is what changes universally; per-podcast nuance lives in each reference file's "Pre-interview mode" section.

**What changes in the tease:**

| Aspect | Post-recording (default) | Pre-interview |
|---|---|---|
| Tease basis | Specific moments from the transcript | Topic territory the dossier suggests |
| Framing verbs | "explains how", "breaks down", "shares why", "reveals" | "we'll explore", "expect a conversation about", "the questions I want to ask", "we're going deep on" |
| Specificity | Named decisions, dates, numbers from the transcript | Named topics from the dossier (sectors, debates, products, ventures) |
| Confidence | High — based on what was actually said | Anticipatory — framed as what's coming |

**Topic territory in pre-interview mode** still needs to be specific. The failure mode is going generic ("we'll explore his journey, lessons, and vision") — that violates the no-generic-tease rule just as badly in pre-interview mode as in post-recording. Use the dossier to surface real topics:

- Named ventures the guest has built or is building
- Sector debates the guest is publicly on a side of
- Recent events in the guest's domain (deals, regulatory shifts, technical releases)
- Specific tradeoffs visible in the guest's current work (e.g., "the tradeoff between on-chain transparency and institutional privacy")

**What does NOT change:** parts 1 and 2 of the intro (founder line, scale/credibility, why-they-matter). These come from the dossier in both modes, so they're identical.

**Founder Thesis takeaways section in pre-interview mode:** the takeaways become "questions we're exploring" — still 2-3 specific things, but framed as topics the host wants to dig into, not as reveals.

**Refusal condition:** if the dossier is thin (a one-paragraph bio, no specifics on ventures or views), do not generate a pre-interview intro. Ask the user for a richer dossier. A pre-interview intro built on a thin dossier will either be generic (fails the specificity test) or fabricated (fails the honesty test).

## Process

1. **Identify the podcast and mode.** Read the matching reference file in `references/`.
2. **Scan the dossier.** Identify: guest name, company name, the most impressive credibility signal, sector. In pre-interview mode, also extract: named ventures, public positions, recent events, visible tradeoffs.
3. **In post-recording mode: scan the transcript for tease material.** Look for: decisions tied to a date, contrarian moves, counterintuitive insights, dramatic moments, mental models the guest articulates, specific mechanics. **Skip this step in pre-interview mode.**
4. **Apply the reference file's structure.** Each podcast has its own structure — follow it. Use the reference file's hook library for tease angles. In pre-interview mode, also read that file's "Pre-interview mode" section for adjusted phrasing.
5. **Draft 5 variations** with different tease angles.
6. **Self-audit each variation** against the checklist below. Rewrite violations silently. Do not show the user the audit.
7. **Output:** 5 variations + recommendation. No preamble. Start directly with `**Variation A`. In pre-interview mode, add a one-line note above the variations: *"Pre-interview draft — tease references expected topic territory, not transcript moments."*

## Self-audit checklist

Run each variation through these. For every violation, rewrite — do not just flag.

### Podcast branding check
Does the variation include the podcast's branded name spoken aloud at least once? Use the exact canonical phrasing from the reference file ("Founder Thesis Podcast", "un# podcast", "Built to Share", "Human by Design"). If missing, add it. The default slot is the tease line ("In this episode of [podcast]..."); some podcasts also use an opening slot.

### Em-dash check (hard rule)
String-search for `—` and `–`. If any appear, replace with commas, periods, or colons. Hyphens in compound words are fine.

### Banned phrases check
String-search for: "masterclass", "shares his journey", "takes us behind the scenes", "deep dive", "fascinating conversation", "incredible insights", "revolutionary", "groundbreaking", "disrupting", "game-changing", "trailblazing", "passionate about", "thought leader". Rewrite in plain language.

### Unpacking check
Does the variation use a technical or industry term that the audience for THIS podcast wouldn't grasp instantly? Check the reference file's audience profile to know what's allowed. If unpacking is needed, add 2-3 concrete examples with named brands or specific actions.

### Credibility signal check
Is there exactly ONE primary credibility signal (scale number, technical pedigree, etc.)? Two or more stacked signals dilute impact. Cut to the strongest one, possibly paired with one humanizing secondary metric.

### Currency check
Is the scale signal in the right currency for this podcast's audience? Check the reference file. Convert if needed.

### Tease specificity check
Is the tease generic? Apply the test: could it be cut and pasted onto a different guest's intro? If yes, rewrite. In post-recording mode, the fix is a specific date, decision, number, or moment from the transcript. In pre-interview mode, the fix is a named venture, sector debate, or recent event from the dossier — *not* a fabricated moment.

### Fabrication check (pre-interview mode only)
Is the variation claiming something the guest said, decided, or did during the conversation? If yes, rewrite. In pre-interview mode, the tease must use anticipatory framing ("we'll explore", "expect a conversation about", "the questions I want to ask") not transcript framing ("breaks down", "explains how", "shares why"). Hard rule: no fabricated moments.

### Length check
Is each variation within the word count specified by the reference file? Trim or expand.

### Spoken-cadence check
Read each variation mentally. Are there points where you'd stumble? Long parentheticals, semicolons, or comma-stuffed sentences break spoken delivery. Break into shorter sentences.

### Output check
Did you start with any preamble ("Here are five options", "I've drafted these", "Let me know what you think")? Cut. Start directly with `**Variation A`. In pre-interview mode, the one-line note above the variations is allowed and expected.
