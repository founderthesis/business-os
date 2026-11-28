---
name: ft-newsletter
description: "Turn a Founder Thesis episode transcript into a LinkedIn newsletter in Akshay Datt's voice that an ordinary reader enjoys and understands. Trigger on \"/ft-newsletter\", \"FT newsletter\", \"Founder Thesis newsletter\", \"LI newsletter\", \"deep dive for this episode\", \"make a newsletter from this episode\", or whenever a Founder Thesis transcript is supplied with newsletter intent. Proposes 3-4 themes and STOPS for Ranjita to pick one; then, in one pass, picks the voice, opens on a relatable everyday hook, tells the episode as a story in plain words with one short \"For the curious\" business section, uses Tracxn figures (cited \"Source: Tracxn\"), gives 5 simple titles, checks every number, and adds thumbnail lines and promo plugs. Inside a copy doc it writes into the LI newsletter tab. Say \"step by step\" for extra stops at voice and outline."
---

# Founder Thesis newsletter

Turn one Founder Thesis episode into a LinkedIn newsletter for Akshay's newsletter that a common reader opens, understands and finishes. The host is **Akshay Datt**. The reader is **not a founder or an investor by default**: think an urban Indian professional, ambitious, curious about business, who has never heard of this guest or this industry.

Three things decide whether the piece works:
1. **The hook.** The first two lines must pull in someone who doesn't care about the industry yet.
2. **The story.** It must read like a story with people, a problem and a turn, never like a report or a list.
3. **Plain words.** A reader with no business background understands every sentence on the first read.

And one thing it never does: **invent a number, a quote or a fact.**

## Inputs

Read these in full before writing. Never ask for something you can find yourself.
- The episode **transcript**, complete. If there's a revised transcript, it wins. Watch for transcription errors in names and figures, and leave out anything you can't confirm.
- The **dossier** and, inside a copy doc, the **Overview tab** (Company research, LinkedIn read, themes).
- **Tracxn.** Always pull the company's Tracxn figures (funding rounds, total raised, investors, revenue, profit or loss, headcount) with the Tracxn connector, or take them from the Overview tab if they're already there. Use them freely in the newsletter, cited "Source: Tracxn" (decision 532). If the Tracxn connector can't be reached, say so in the output and carry on.
- The Engagement's **guest restrictions and edit notes**. A cut segment or anything marked unpublished never appears.
- **Akshay's own newsletter voice.** Read `references/akshay-voice.md` before drafting.

If something genuinely isn't there or can't be opened (a dossier that returns "permission denied", say), note it at the top of the output and carry on with what you have. Never stop the run for a missing source.

## Modes

- **Default: one stop, for the theme.** Ranjita selects the theme. Propose 3 to 4 themes (Step 1), then STOP and wait for her pick. Once she picks (or combines two, or gives her own), do everything else in one pass with no more stops: choose the voice, write the hooks, titles and draft, and run the checks.
- **Step by step (only when asked).** Also stop after the voice options and after the outline.
- **"Skip" or a theme given up front.** If Ranjita names the theme in her request, or says "skip", take that theme and go straight to the draft.

## Where the output goes

- **Inside a copy doc:** the LI newsletter tab. Keep "Your deep dive" at the top blank for Ranjita and never overwrite anything a person wrote.
  - First run: write the theme options under a heading "Pick a theme", then stop and ask Ranjita in chat to pick.
  - After her pick, add below, in this order: the theme picked and the voice chosen (two lines), the 3 hooks tried, 5 titles, the draft, the number check, thumbnail lines, promo plugs. Leave the theme options in place.
  - Headings bold and coloured like the rest of the doc (teal for sections and the recommended pick, purple for alternates).
- **Elsewhere (no copy doc):** in chat or a markdown file `ft-newsletter-<slug>.md`, with the same order and plain `##` headings: Theme and voice, Hooks, Titles, Newsletter, Number check, Thumbnail lines, Promo plugs.

---

## Step 1: Theme options (STOP for Ranjita)

Read everything, then for each possible theme answer these four questions:
- **Who is the person**, and what did they want?
- **What got in the way?** The struggle, the bet, the moment it nearly failed.
- **What's the turn?** The surprising thing they did or understood that others didn't.
- **Why should an ordinary reader care?** Connect it to something in their own life: their phone, their commute, their kitchen, their salary, their kid's school.

Propose **3 to 4 genuinely different themes**. A theme is a claim with tension, not a topic ("India's biggest mental health company is an astrology app" beats "About mental health"). Show each like this:

```
Theme 1: [simple label, 3 to 6 words]
- The story: [1 to 2 plain sentences on what the newsletter would tell]
- Why an ordinary reader cares: [the everyday link]
- Hook idea: [one line on how it could open]
- Anchored in: [the transcript moment or quote, with timestamp]
```

Mark the one you'd pick with ★ and say why in one line. Close with: "Pick a theme, combine two, or give me your own. I'll write the full newsletter from there." Then **STOP**.

## Step 1b: Voice (no stop)

Once Ranjita picks, choose the voice from `references/voice-palette.md`. **Akshay's plain voice is the default**; use a named voice (Gladwell, Lewis and so on) only when it clearly fits the story. Say which and why in one line at the top of the output.

## Step 2: The hook

The hook is the most important part. Write **three different hooks**, pick the best, and show all three in the copy doc so Ranjita can swap.

A good hook:
- **Starts in the reader's everyday life**, not in the industry. A moment they recognise: a time of day, a place, an object, a small frustration.
- Uses **"you"** or a concrete person, a real time and a real thing. "It is 10:15 AM on a Tuesday. You have ₹1 lakh in your trading app." "The broccoli in your pasta tonight started somewhere you will never see." "Somewhere in India tonight, a person is in real distress. They are not scrolling an app store."
- **Opens a question** the reader wants answered, and the story answers it.
- Is **two to three short sentences**. No throat-clearing, no "In today's world", no definitions, no statistics dump.

A bad hook starts with the company, the guest's CV, the market size, or a big claim about the industry.

Types to try (use a different type for each of the three):
1. **Everyday scene:** the reader in a moment where this business quietly touches their life.
2. **Surprising fact, made human:** one figure, shown through a person or an object, never as a bare number.
3. **The guest's moment:** the night, the meeting, the phone call where everything changed.
4. **The question everyone has:** something the reader has wondered about without knowing who solves it.

## Step 3: Titles

Give **5 titles**, recommend one, and mark it ★.
- **Simple and relatable.** Everyday words a 15-year-old knows. No jargon, no acronyms, no "paradigm", "ecosystem", "disruption", "unlocking".
- **Under 10 words.** Curious, true and specific.
- Tie it to something the reader knows or feels. Good: "The Hidden Journey Behind Your Broccoli", "India's Biggest Mental Health Company Is An Astrology App", "Meet the Heroes Behind India's Modern Equity Markets". Bad: "How AgriTech Is Transforming Supply Chain Efficiency".
- No clickbait the piece can't pay off.

## Step 4: Write it as a story

**Length:** 700 to 1000 words. Hard ceiling 1000.

**Shape** (a story, not sections of a report):
1. **Hook** (from step 2).
2. **Why it matters to you:** one short paragraph linking the hook to the reader's life.
3. **Watch CTA, first time:** one line inviting them to watch the episode.
4. **The person and the problem:** introduce the guest through what they wanted and what stood in the way. Full name once, then first name only.
5. **The turn:** what they did differently, with the best quote.
6. **How it actually works:** the business explained as if to a friend over chai. One Indian comparison the reader already knows ("it works like a dabbawala route, but for data"). Bring in the Tracxn figures here where they help the story (how much was raised, from whom, how big the business is), cited "Source: Tracxn".
7. **For the curious:** one short section, 80 to 150 words, with the subhead "For the curious". It carries the sharpest business point in the episode, the one an operator or investor would screenshot: why rivals failed, the unit economics, the valuation logic, the hidden moat. Still in plain words: explain every term, use one number, and keep it to two or three short paragraphs. Pick the point from the transcript; Tracxn figures can support it.
8. **What it means:** Akshay's own take. A clear point of view, not a summary.
9. **Close:** come back to the hook's image or question, now answered. Then the watch CTA, second time, and one line inviting comments ("Would you trust an app with this? Tell me below.").

**Keep it easy to understand:**
- Short sentences. Mostly one idea per sentence. Short paragraphs of one to three sentences.
- Every technical word is explained in plain words the first time it appears, or replaced. If you can't explain it in one simple line, leave it out.
- Use **one** number per point, never a cluster. Make each number feel real with a comparison the reader knows, but only a comparison you have checked is true.
- Rupees for Indian figures, in crore or lakh.
- Two or three plain bold subheads at most, written as everyday phrases, so the piece is easy to scan on a phone, plus the "For the curious" subhead.

**Keep it from being boring:**
- Every paragraph either moves the story forward or makes the reader feel something. Cut any that does neither.
- End each section with a small pull into the next: a question, a twist, an "but that's not where it ended".
- Vary rhythm: a long sentence, then a short one. Let a single-line paragraph land the key moment.
- Show, don't tell: a scene or a specific detail beats an adjective.
- Real people, real places, real moments from the transcript. No generic "businesses today face challenges".

**Quotes:** 2 to 4 block quotes from the transcript, edited for grammar and length only. Never change the meaning, never merge two separate statements, never invent one. Each quote should sound like a person talking, not a press release.

**Voice:** Akshay, first person. Conversational and honest, like his own newsletter: he admits what he didn't know, uses everyday examples from his life, and asks the reader what they think. He has a view; the guest is the expert witness. Never critical of the guest.

## Step 5: Number check (mandatory)

Before the piece ships, list every figure, date, superlative ("first", "largest", "only") and named claim.
- Check each against the transcript, then Tracxn, then the dossier and Overview tab, then a web search for present-day facts.
- **When the guest and Tracxn disagree** on a company figure (funding, revenue, headcount), use the Tracxn figure, cited "Source: Tracxn", and show the guest's figure beside it in the number check. If the gap changes the story, mention it plainly in the text ("Vivek counts $42M; Tracxn records $46M across three rounds").
- Never give the guest credit for a figure that belongs to a competitor or the market.
- A projection or a claim only the guest makes is credited to the guest ("Vivek expects…"). If it sits far off the Tracxn figures (a forecast many times last year's revenue), either credit it clearly and set the Tracxn figure next to it, or leave it out. Never present it as fact.
- Don't round up careers or market shares. Contested stats are attributed or cut.
- Show a short table: claim, source, verdict, what changed.

## Step 6: Read it as a reader

Read the whole draft once as the common reader who knows nothing about this industry:
- Would you keep reading after the first two lines? If not, rewrite the hook.
- Is there any sentence you'd have to read twice? Simplify it.
- Is there any paragraph where your attention drops? Cut or tighten it.
- Does the end answer the question the hook asked?
- Strip AI tells: no "it's not X, it's Y", no dramatic three-fragment lists, no "Let that sink in", no "In a world where", no tidy rhetorical sign-off.

Revise, then deliver.

## Step 7: Extras

**Thumbnail lines, 5 options.** About 5 words each, simple and curious, for the image next to the guest's photo. Recommend one.

**Promo plugs, 5 options.** Two lines each for a LinkedIn post linking to the newsletter. Line 1 is a relatable, surprising line; line 2 opens a curiosity gap. No emojis, no tags, nothing that leans on a number the check flagged. Recommend one.

---

## House rules (never break)

1. No em dashes anywhere.
2. No brochure words: "game-changer", "revolutionary", "unlock", "leverage", "seamless", "robust", "delve", "ecosystem", "disrupt".
3. No negative framing of the guest.
4. First name for the guest after the first mention.
5. Sentence-case subheads.
6. Engagement over SEO. Never write for a search engine.
7. No invented numbers, quotes or facts. Tracxn figures used and cited "Source: Tracxn".
8. Honour every guest restriction and edit note.

## Ready when

- The hook pulls in someone who doesn't care about the industry, in two or three sentences.
- The title is simple, under 10 words, and uses words anyone knows.
- It reads as one story from hook to close, with a turn in the middle.
- A reader with no business background understands every sentence on first read.
- No flat patch; every section pulls into the next.
- 700 to 1000 words, 2 to 4 real quotes, one "For the curious" section, the watch CTA twice, a comment invite at the end.
- Ranjita picked the theme, and the Tracxn figures used are cited "Source: Tracxn".
- Every number survived the check and the table is shown.

## Reference files

- `references/akshay-voice.md`: how Akshay's own newsletter sounds, with hook and title examples. Read before drafting.
- `references/voice-palette.md`: Akshay's plain voice (the default) and the named voices for when a story suits one.
