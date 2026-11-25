---
name: ft-substack-newsjack
description: >-
  Turn breaking news about a past Founder Thesis guest or their company into a fast,
  publishable Substack article that rides the search spike — built around the one
  asset no other outlet has: FT's own long interview with that founder. Use this when
  the user says "newsjack this", "X is in the news", "write a newsjack on [company]",
  "[founder] just raised / shut down / got acquired / died / went on Shark Tank", or
  pastes a news link about a founder FT has interviewed. Produces the title, subtitle,
  body with verbatim interview quotes, internal links, sources, tags and embeds —
  everything except hitting publish.
---

# Founder Thesis — newsjack writer

When a founder FT has interviewed lands in the news, a search spike opens for a few
days. Every outlet covering it is working from the **same press release**. FT has
something none of them have: **the founder, at length, in their own words**, recorded
before the news happened.

That asymmetry is the entire strategy. A newsjack is not a news report — FT will never
beat Inc42 or ET on speed or scoops. It is **the news event, explained through the
founder's own account of how they built the thing.** Write it that way.

Read `references/structure.md` for the proven section-by-section template and a full
worked example.

## Speed matters, but accuracy decides

Newsjacks are time-sensitive — the search spike lasts days, not weeks. Move fast, but
**never trade accuracy for speed**. A wrong number in a piece about a live news event
is far more damaging than a piece published a day later. If a fact can't be verified,
leave it out.

## Step 1 — The hook: is this worth newsjacking?

Establish exactly what happened, when, and why anyone is searching. Then judge it.

**Strong hooks** (these reliably draw search):
- Funding, secondary sale, acquisition, IPO/listing
- **Shutdown, layoffs, insolvency, fraud or controversy**
- **Death or departure of a founder**
- Shark Tank / mainstream TV appearance
- Big pivot, rebrand, or a celebrity/marquee investor angle
- The company crossing a milestone with a real number attached

**Weak hooks — skip these:** routine hires, small partnerships, award lists, generic
"trend" pieces, funding under the $10M / ~₹80cr bar with no other angle.

If the news is weak, say so and stop. A thin newsjack burns the archive link for
nothing.

## Step 2 — Match the archive (this is the gate)

Search the Notion **"Episode Inventory"** for the founder and the company. You need:
- the **episode** (title, YouTube URL, Spotify URL, Substack URL if an article exists)
- the **transcript** (Transcript URL / Transcript file)

**If FT has interviewed them → this is a strong newsjack.** The interview is the
differentiator; build the whole piece around it.

**If FT has NOT interviewed them → say so and check for the next best thing:** an
adjacent episode in the same category, or a cluster of related FT articles you can
legitimately link. If there's no real connection, recommend skipping — without the
interview, FT is just another outlet rewriting a press release, and that neither ranks
nor earns anything.

## Step 3 — Research the news

Get the facts straight from **multiple** current sources (Inc42, ET, YourStory,
Moneycontrol, company statements, filings). Capture:
- The **exact date** and what precisely happened
- Every **name and number** involved — who bought, who sold, how much, what stake
- Official quotes from the company/CEO
- The company's **current** financials: revenue, losses, growth, headcount, funding
  raised to date

Every number must trace to a source you'll cite. Never estimate and present it as fact.

## Step 4 — Mine the transcript for the founder's own words

This is the part no competitor can replicate. Read the transcript and pull:
- **2–4 verbatim quotes** that speak to whatever the news is about (if the news is a
  shutdown, find where they described the risk; if it's an exit, find why they built
  it that way)
- The **origin story**, the **failure or pivot**, and the **operating principle** that
  explains their decisions
- Their own framing of the thing now in the news

Quotes must be **exactly** as spoken — never tidied into something they didn't say.
These come from YouTube auto-captions, so flag any quote whose wording you're unsure
of for an audio check before publishing.

## Step 5 — Write it

Follow the structure in `references/structure.md`. In short:

1. **Open on the news** — dated, specific, framed as a question the news raises
2. **Unpack the news facts** — names, numbers, who did what
3. **Pivot to the archive** — an explicit line that the best answer on record is the
   founder's own
4. **Who the founder is** — background and the numbers, with **internal links to 3+
   related FT articles** woven in naturally
5. **The story from the interview** — the verbatim quotes and what they explain
6. **Where the business stands now** — current, verified financials
7. **"The one source no other outlet has"** — state plainly that everyone else is
   working from the same press release, and FT has the founder's own account
8. **The CTAs** — watch the episode (YouTube embed) + read the full article
9. **A closing line** that returns to the opening frame

Length: **900–1,500 words.** Tighter than a standard FT dossier — this is a news piece
with depth, not a full biography.

## Editorial stance: accurate but generous — and careful

Same house rule as the article skill: **factually accurate, never unkind.** Newsjacks
strain this more than anything else, because the news is often bad.

- **Deaths:** write with dignity, no morbid framing, no speculation about cause.
  Centre the legacy and the work.
- **Shutdowns, fraud, layoffs, controversy:** report exactly what is on record, cite
  it, and stop. **Never speculate on motive, and never pile on.** State the facts and
  let the reader judge.
- Never repeat a claim you've verified as false, and never editorialise real numbers
  into a verdict.
- FT hosted these founders. The piece should be one they'd find fair even on their
  worst week.

**The $10M rule:** no sub-$10M / ~₹80cr figure headlines a title or thumbnail (body
numbers are fine).

## Step 6 — Deliver

Run this checklist, then hand over:

- [ ] News hook is strong, exact date and facts verified across multiple sources
- [ ] FT episode identified — YouTube URL, Spotify URL (from Episode Inventory)
- [ ] 2–4 **verbatim** interview quotes, any uncertain wording flagged for audio check
- [ ] "The one source no other outlet has" section present and explicit
- [ ] 3+ internal FT links to related articles
- [ ] 900–1,500 words
- [ ] Every number traceable to a cited source; nothing invented
- [ ] Sources section with outbound authoritative links
- [ ] $10M rule respected in the title
- [ ] 1–3 tags from the fixed taxonomy: Fintech · D2C · SaaS · Deeptech · Healthtech ·
      Edtech · Consumer Internet · Mobility & EV · ClimateTech · VC & Investing
- [ ] Handled with dignity if the news is a death, shutdown or controversy

Deliver: the **title**, **subtitle**, **body**, **5 title options**, **tags**, the
**YouTube + Spotify embed URLs**, the **Sources** list, and a **facts-to-verify** note.

End with the meta line, as in the worked example:
`Tags: … · Publish with no email · Embed YouTube + Spotify (<url>)`

**Publish with no email.** Newsjacks are extra posts, not the weekly episode — they go
to the web without emailing subscribers. Then hand to `ft-substack-publish`.
