---
name: carousel
description: >-
  Build a LinkedIn quotes carousel from a podcast guest interview. Mines
  10-14 verbatim quotes from the transcript, pairs each with a context
  paragraph, and delivers an interactive HTML artifact where the user
  selects quotes, reorders them, and exports the final copy deck.
  Works for any podcast in the network: Founder Thesis (Akshay Datt),
  un# (Sri Misra), Built to Share (Satish Mugulavalli), or Human
  by Design (Arjun Jain). Trigger on "carousel", "quotes carousel",
  "make a carousel from this episode", "guest quotes for a carousel",
  "pull quotes for slides", "swipeable slides from this transcript",
  or the slash command "/carousel". Also trigger when the user pastes
  or references a transcript and asks for carousel content, quote
  cards, or LinkedIn slides from a guest interview.
---

# Carousel

Extract a podcast guest's strongest verbatim quotes from a transcript, pair each with a context paragraph, and deliver an interactive HTML picker where the user assembles the final carousel.

## What this skill produces

One self-contained HTML file. The user opens it, sees 10-14 candidate quote cards, ticks the ones they want (target: 4-6), drags them into order, and exports a copy deck. The skill does the editorial mining and writing. The user does the selection and sequencing.

## Inputs

1. **Transcript** (required). Read it fully. Every quote must be verbatim.
2. **Dossier** (optional). Hard numbers, career context, credibility markers for the cover slide.
3. **Theme direction** (optional). "About talent," "about capital," etc. Filters extraction.

## Step 1: Identify the podcast

| Podcast | Host | Episode link format |
|---|---|---|
| Founder Thesis | Akshay Datt | founderthesis.com/[guest] |
| un# | Sri Misra | TBD |
| Built to Share | Satish Mugulavalli | built2share.in/[guest-slug] |
| Human by Design | Arjun Jain | TBD |

If unclear which show, ask once.

## Step 2: Mine the transcript

Read the full transcript. Extract 10-14 candidate quotes from the guest.

### What makes a carousel quote

- **Standalone.** Makes sense without the host's setup question. If it needs context to land, it's not a carousel quote.
- **Weight.** A founder would pause, screenshot, or forward this. Not a generic observation. A line with conviction, experience, or an unexpected angle.
- **Proof point nearby.** Somewhere in the transcript, the guest backs this with a story, number, or example. That feeds the context paragraph.
- **Concise enough for large text.** Best at 10-25 words. If a passage has a great line buried in it, extract the punchiest sentence.

### What to reject

- Factual statements with no opinion or conviction behind them.
- Setup lines that only make sense as part of a longer argument.
- Quotes longer than ~35 words (they shrink on the slide and lose impact).
- Anything that reads like a motivational poster without a receipt.
- Industry truisms everyone already agrees with.

### Tagging

Tag each candidate quote with:
- **Theme** (1-2 words: talent, culture, capital, hiring, retention, execution, etc.)
- **Strength** (Strong / Good / Borderline). Be honest. The user wants to see your editorial judgment.
- **Suggested position** (Opener / Mid / Closer). Opener = most provocative, earns the swipe. Closer = most resonant, earns the share. Mid = everything else.

## Step 3: Write context paragraphs

Write one context paragraph (3-5 sentences) for each of the 10-14 candidates. Yes, even the ones tagged Borderline. The user might keep one you'd cut.

### Context paragraph rules

- **Third person.** Reference the guest by first name. "Ravi has been a tough, target-driven boss for 30 years." Never first person.
- **Don't restate the quote.** The reader just read it in huge text. Add what the quote doesn't contain: backstory, proof point, implication.
- **End with the sharpest sentence.** Build toward a punchy closer. "That's the culture manual nobody writes but everyone reads" is sharp. "And that's a lesson every founder should remember" is preachy.
- **3-5 sentences.** A paragraph, not a one-liner. Not an essay.
- **No "In other words..." or "What he means is..."** The reader understands the quote. Expand, don't translate.

## Step 4: Write the cover slide copy

The cover slide establishes who the guest is and why the reader should swipe.

### Cover slide elements

1. **Guest name.** Large, bold.
2. **Title and role.** Current first. Former if it adds credibility.
3. **Credibility block.** 2-3 lines of hard stats. Numbers, not adjectives. "Built Sodexo India to 28,000 people on $5M" beats "Experienced business leader."
4. **Hook.** One surprising line, a curiosity gap. "His 22-person leadership team? Not one of them came from his industry."
5. **Promise line.** "[N] lessons on [topic], from [N] years of [building/scaling/leading]." N is a placeholder; it updates based on how many quotes the user selects.
6. **Photo note.** Flag for designer: needs high-res headshot from episode assets.

Source the credibility block from the dossier (or transcript if no dossier).

## Step 5: Write the CTA slide copy

1. **Heading.** "The full conversation goes deeper." or similar.
2. **Topic list.** Major topics the episode covers BEYOND the carousel's theme. Use middot (·) separators. Signal there's more to discover.
3. **Episode URL.**
4. **Show branding.** Show name + "WITH [HOST NAME]".

## Step 6: Build the interactive HTML artifact

Deliver ONE self-contained HTML file with all CSS and JS inline. No external dependencies. No localStorage (not supported in Claude artifacts).

### HTML artifact structure

The artifact has three sections:

**Section 1: Cover slide preview**
- Shows the cover slide copy (guest name, title, credibility, hook, promise line)
- The promise line auto-updates its count as the user selects quotes below
- Not editable in the artifact (edits happen in chat if needed)

**Section 2: Quote picker**
- Each candidate quote rendered as a card:
  - A **keep checkbox** (unchecked by default)
  - The **verbatim quote** in large text
  - The **context paragraph** in smaller text below
  - A **theme tag** (e.g. "Culture", "Hiring", "Capital")
  - A **strength badge** (Strong / Good / Borderline)
  - A **position tag** (Opener / Mid / Closer)
- Cards are visually distinct when selected (e.g. highlighted border, accent colour)
- A **live counter** at the top: "4 of 12 selected" updating in real time
- A guidance note: "Select 4-6 quotes. Drag to reorder below."

**Section 3: Build tray**
- Selected quotes appear here automatically as draggable rows
- User can **drag to reorder** the sequence
- Each row shows: position number, the quote (truncated to first ~60 chars), theme tag
- The cover slide appears as a fixed first row (not draggable)
- The CTA slide appears as a fixed last row (not draggable)
- Visual preview of the carousel order: Cover → selected quotes in drag order → CTA

**Export button**
- Generates the final copy deck as a downloadable `.docx` file containing:
  - Cover slide copy (all elements)
  - Each selected quote in order: verbatim quote + context paragraph + attribution
  - CTA slide copy
  - Production notes (slide count, design system reference)
- Also include a **copy-as-text fallback** that copies the full deck to clipboard as plain text
- The `.docx` must be a valid file (proper ZIP structure, correct CRC-32). Test before shipping.

### Design system reference (include in the artifact as a collapsible section)

- Background: deep navy across all slides
- Quote text: large, bold, cream/off-white
- Quote marks: large decorative, orange/red accent
- Context text: smaller weight, warm grey
- Accent colour: orange/red (quote marks, show name, SWIPE, URL)
- Attribution: guest name bold + show name in accent, below thin divider
- Persistent: show logo (top left), slide counter (top right), SWIPE >>> (bottom right except last)
- Cover: guest photo right side, no quote marks
- CTA: no quote marks, no attribution, show branding footer
- No illustrations. Text-only format.

## Self-audit checklist

Run before delivering. Fix violations silently.

### Verbatim check (hard rule)
Is every quote an exact string from the transcript? Did you tidy grammar, merge sentences, or paraphrase? If so, revert to the real spoken words. Any non-verbatim quote is a failure.

### Quote count check
Are there 10-14 candidates? Fewer than 10 doesn't give enough choice. More than 14 overwhelms.

### Strength honesty check
Are the strength tags honest? If everything is tagged "Strong," you're not being editorial. A good menu has 5-7 Strong, 3-5 Good, 1-3 Borderline.

### Context paragraph check
Does every context paragraph avoid restating the quote? Does every one end on a sharp sentence, not a preachy moral? Is every one in third person?

### Cover credibility check
Does the cover slide use hard numbers, not adjectives?

### Theme diversity check
Do the 10-14 candidates span at least 3 different themes? If they cluster on one theme, mine harder for others.

### Em-dash check (hard rule)
String-search the entire output for — and –. Replace with commas, periods, or rewrite.

### AI tells check
String-search for: "In today's fast-paced world," "It's worth noting," "This underscores," "At the end of the day," "It goes without saying." Rewrite.

### Artifact integrity check
Is the HTML self-contained (inline CSS/JS, no external requests, no localStorage)? Does the keep checkbox toggle card highlighting? Does the live counter update? Does the build tray accept drag-to-reorder? Does the export produce a valid .docx? Does copy-to-clipboard work?

## Process summary

1. Identify the podcast. Read transcript (and dossier if available).
2. Mine 10-14 verbatim candidate quotes. Tag each with theme, strength, position.
3. Write a context paragraph for every candidate.
4. Write the cover slide copy (name, title, credibility, hook, promise line).
5. Write the CTA slide copy (heading, topic list, URL, branding).
6. Build ONE interactive HTML artifact: cover preview, quote picker with cards, build tray with drag-to-reorder, export button (.docx + copy-to-clipboard).
7. Self-audit. Fix violations.
8. Deliver the HTML file with `present_files`. Chat message: name the strongest opener, the strongest closer, and the combination you'd run if it were your carousel. No preamble, no restating the menu.

## Constraints (non-negotiable)

- Zero em-dashes anywhere
- Zero hashtags
- Quotes are verbatim from the transcript, never paraphrased
- Context paragraphs are original writing, never pulled from transcript
- Cover credibility uses hard numbers
- No AI tells
- No tidy moral announcements
- HTML artifact must be self-contained, no localStorage, no external deps
- Export must produce a valid .docx (test the ZIP structure)
