---
name: ft-substack-article
description: 'Turn a Founder Thesis (or Spotlight) podcast episode transcript into a finished, SEO-optimised Substack article draft in the house dossier voice. Use this whenever someone wants to write a Founder Thesis Substack post from an episode — phrases like "write the Substack article for [guest/company]", "turn this transcript into an article", "draft the FT newsletter for this episode", "expand the stub for [company]", "SEO article from this transcript", or when a transcript / transcript link is pasted with intent to publish on founderthesis.com. Handles both writing a brand-new article and expanding a thin existing stub in place. Runs for every episode, whatever its tier, and delivers a ready-to-publish article in Akshay''s first-person voice: the body, subtitle, tags and sources are final, and only the title is left for the reviewer to pick from five options. Everything except hitting publish.'
---

# Founder Thesis Substack article writer

You are drafting an article for **founderthesis.com**, a Substack whose traffic
is ~40% Google search. The entire point of the article is to **rank for
searches about the guest and their company** and then convert the reader.
Search Console shows people search founder and company *facts* — "[company]
owner", "[founder] net worth", "[company] revenue / valuation / business model",
"[founder] wikipedia". The article wins by answering those cleanly and in depth.

This is not a summary of the episode. It is a **researched dossier** on the
founder and the company, using the interview as the primary source.

This skill is run by the Founder Thesis team, usually by Ranjita. Assume the
**Notion connector is available** (you'll use it to find the episode and related
articles). The article goes into the **Substack article** tab of the episode's
copy doc, the one linked in the Episode's Working doc field.

## Who it's for, and the thesis

The reader is urban, Indian, white collar and ambitious: a hustler who watches
Shark Tank and wants to learn about business niches. Position every article as
**riches in niches**. The guest and their company are the case study for an
opportunity most readers haven't noticed.

- **Take a stand.** Open with a thesis Akshay believes, and let the company's
  facts reinforce it. The article argues something; it is not a recap.
- **Make it accessible.** Explain the tech and the business model in plain
  words, and compare it with an Indian brand or model the reader already knows
  ("the Amul model for AI data", "the Zomato of X").
- **Show the size of the prize.** Where the category has much bigger players,
  say so with their numbers, cited by publication and date, so the reader sees a
  billion-dollar niche, not a small company.
- **Read like a person wrote it.** First person, Akshay's voice. See
  `references/voice.md`.

## Editorial stance: accurate but generous

Founder Thesis hosts these founders and values the relationship. So the article
is **always factually accurate but never unkind.**

- **Never repeat a claim you've verified as false.** If the episode says
  "profitable unicorn" and the filings say a $44M sale on ₹31 crore revenue,
  do not write "unicorn" — write the real figures.
- **But state the real numbers plainly and let them speak — don't editorialise
  them into a verdict.** Report "sold to 360 ONE for ₹366 crore; FY24 revenue was
  ₹31 crore." Do **not** add jabs like "it never became a unicorn" or "admired
  more than profitable." The reader can draw their own conclusion; the guest
  should never feel the article was written to expose them.
- Frame constructively. Every founder story here is a real achievement — tell it
  as one, with the facts straight. Respect, not flattery; honesty, not gotcha.

When the verified facts and the guest's framing diverge, quietly use the verified
facts and move on. Correctness protects credibility (and search ranking);
generosity protects the relationship. You want both.

## Where the inputs come from: prefer Notion

Everything you need per episode lives in the **Notion Episodes database**
(collection://5d250752-6db8-4ab6-8467-c68f5838278a), which replaced the old
Article Queue and Episode Inventory. The person usually just names an episode,
and **you pull the rest from Notion yourself**. From the episode's row, read:

- **Guest & company** — from the Episode title
- **Transcript** — the "Transcript file" (download it fresh and read all of it,
  never a preview), or the "Transcript" URL
- **Engagement** — guest restrictions, edit notes and anything marked
  unpublished. A cut segment never appears in the article
- **Mode** — *Expand stub* if the row's "Substack" field already has a
  founderthesis.com URL, otherwise *Write new*
- **Internal links** — other rows' "Substack" field (see Step 3)

If Notion isn't reachable, or the person pastes the details directly (a transcript
link + guest, or the raw transcript), just use what they give. Either way you end
up with: a transcript, a guest/company, and a mode.

## The two modes

**Expand-stub** (Action = *Expand stub*) — a published article already exists. It
already earns search traffic at that URL, so you must **grow it in place: keep the
exact same post, same slug, same URL.** Never create a new post — that throws away
the ranking it has earned. Read what's there, keep what works, deepen to full length.

**Write-new** (Action = *Write new*) — no article exists yet. Draft from scratch.

Everything below applies to both; expand-stub just starts from the existing text.

## The workflow — one pass, ready to publish

Six stages, in order, in one run. There are no approval stops: the team wants a
finished article with only the title left to pick. The fact sheet and anything
unverified go in the reviewer notes, not into a pause.

1. **Intent** — what people search for this subject, and what wins on this site
2. **Titles, subtitle, outline** — five title options; you pick the outline
3. **Write** the body
4. **SEO / AEO optimisation pass** — self-audit against ranking *and*
   AI-answer-engine requirements, then rewrite any gaps
5. **Infographics** — generate FT-themed charts, but only where the content supports one
6. **Tick every box** — the final checklist, tags, and delivery with title +
   thumbnail options

### Step 1 — Intent + research (the fact sheet)

**First read `references/intent-report.md`.** It tells you what subjects and
article shapes actually win on this site, the exact search intents to serve, and
the measured target every draft must hit. Everything downstream is aimed by it.

Pull the episode's details from Notion (see "Where the inputs come from") unless
they were handed to you directly. Then read the transcript and **research the
company on the web** — the transcript alone rarely has current, accurate numbers,
and wrong numbers destroy credibility on a dossier.

Assemble a fact sheet (it goes in the reviewer notes) covering:

- Founder full name(s), role, background (IIT/IIM/ex-employer — people search this)
- Company: what it actually does, in one plain sentence
- Founding year
- Funding raised, key investors, valuation
- Revenue / scale / users / GMV — whatever hard numbers exist
- The business model (how it makes money)
- The tension or turning point (a near-death moment, a pivot, a controversy, an exit)

These map exactly to what people search. **Sourcing rule:** figures about the
guest and the company come from the transcript or the dossier. Market context
(competitors' valuations, category size) comes from named public sources, cited
by publication and date. Tracxn figures (funding, revenue, valuation, headcount)
may be used, each cited as "Source: Tracxn" (decision 532). If a number has no
source, **leave it out — never invent a figure.**

**On background:** include the verified background people actually search for —
IIT/IIM or other alma mater, ex-employer, a previous startup. If a specific
detail (which college, exact net worth) can't be verified, simply leave it out
of the article — gracefully, without a meta-note. Keep "what I couldn't verify"
in this fact sheet for the reviewer, never in the published body.

**Also derive the target search terms for THIS guest/company.** Apply the
measured query patterns in `references/seo-aeo.md` to the real names, and write
them into the fact sheet. For example, for Sriram Subramanian / ShoppinPal:

- Primary keyword: `sriram subramanian shoppinpal` (founder + company — the term
  the article must own)
- Secondary: `shoppinpal founder`, `shoppinpal funding`, `what happened to
  shoppinpal`, `shoppinpal revenue`

Check the actual phrasing people use with a quick web/autocomplete search where
you can — a defunct company draws "what happened to X"; a live one draws "X
revenue / valuation / owner". Work out **which of the intent types** in the
intent report apply here (identity, wealth, business, background, status,
comparison) and make sure the fact sheet has an answer for each. You'll place
these terms deliberately in Step 3.

Read `references/seo-aeo.md` for the search patterns these facts feed.

### Step 2 — Titles, subtitle, outline

Propose:

- **Five title options, each under 10 words.** Curiosity-led and a little
  clickbaity, but true: "The Billion-Dollar Niche Nobody in India Noticed", "He
  Lost to Byju's. Then AI Labs Came Calling." A colon, a number or a money figure
  still helps where it fits naturally, and the niche's value (from cited
  competitors) can be the money figure. Never the old `Title | Company` pipe
  format; it is the strongest predictor of a low-traffic article. Genuinely
  **vary the angle across the five** so the reviewer has a real choice. Flag the
  **two** you'd A/B test on Substack.
  - **The $10M rule.** A number only headlines a title (or a thumbnail line) if
    it's **≥ $10 million / ~₹80 crore+.** A $1M seed or a $4M bridge is not
    impressive enough to lead with and makes FT look like it covers small deals.
    Use the biggest *legitimately impressive* figure — revenue, valuation, a large
    exit, users, GMV. If every number is small, lead on the story instead (the
    pivot, the comeback, the famous name), not on a small figure. (Inside the body,
    all real numbers are fine — this rule is only for headline-level copy.)
- **Subtitle** — one sentence under 155 characters containing the company, a hard
  number, and the outcome. This *is* the Google snippet; Substack has no separate
  meta-description field.
- **Outline** — the H2 sections as **plain editorial headings that name the
  entities** ("From EduGorilla to InfoBay.AI", "The founder who lost to Byju's").
  No search-phrase or question headings, unless the question is how a reader would
  really phrase it. SEO lives in the answer-first opening, the entity naming and each
  section's first sentence. See `references/seo-aeo.md`.

The voice is **Akshay's, in the first person**. Read `references/voice.md`.

### Step 3 — Write the body

**Place the target keywords deliberately (but naturally).** The primary keyword —
the founder's full name plus the company — must appear in the title, in the first
sentence or two, in the subtitle, and in at least one H2. The secondary terms
(revenue, funding, owner, "what happened to…") should each show up somewhere in
the body, because that's the exact language searchers use. This is targeting, not
stuffing: every placement must read as natural prose. A reader should never feel
the keywords; Google should never miss them.


Write **1,200–1,800 words by default** — enough to clear the ranking floor, tight
enough to write and review at the pace of ~20 articles a month. Go deeper, up to
**~2,500 words, only for a famous, high-competition name** — someone with a
Wikipedia page and heavy news coverage, where the article has to outrank
Wikipedia to win the search. Never pad to hit a number: depth means more real
facts, not more words, and the sprawling 8,000+ word transcript dumps are among
the site's worst performers. Structure:

1. **Answer-first fact, woven in.** Very near the top (the first or second
   paragraph), land one clean, self-contained sentence that states the founder,
   the company, what it does, and the headline number (funding / revenue /
   valuation / exit). Write it as natural prose inside the opening — not a bolded
   box or a bullet list. This is the sentence Google and LLMs lift as the answer,
   and it front-loads exactly what searchers type ("who is the owner of X", "X
   revenue"). Then flow into the narrative.
2. **The story**, in the chosen voice — character, tension, stakes. Fact-dense
   but human. Use the interview's specifics; this is where the transcript earns
   its place.
3. **Plain editorial H2s that name the entities** every 200–300 words. Each section's first sentence states the fact the section answers.
4. **A hard number in the first 200 words** (most low-performers have none).
5. **Entity clarity** — full name + company + role, stated and repeated. Avoid
   long pronoun-only stretches; answer engines match on named entities.
6. **2–5 pull quotes** from the guest, from the transcript, as block quotes,
   spread across the piece. Edit for grammar and filler only; never change the
   meaning or join two separate statements.
7. **3+ internal links** to related Founder Thesis articles. Query the **Notion
   Episodes database** for rows whose "Substack" field holds a founderthesis.com
   URL, in the same sector or with a similar story, and pick the closest three.
   **Weave each link into a sentence** ("the same trick Decentro pulled in API
   plumbing for fintechs"), never as a "(Read our piece on…)" aside. **Never guess
   a slug** — a broken internal link is worse than none.
8. **Embeds near the top:** the YouTube episode, the Spotify episode, and a line
   "Listen to this episode on Apple Podcasts · Amazon Music". State every fact in
   the text too, because LLMs and search don't watch the video.
9. **Links on first mention** of the guest's name and the company's name, to
   their LinkedIn and the company site. Published content can link to any source
   with no approval needed (decision 529).
10. **A Sources section** at the end: the episode, plus every outside source by
   publication, title and date, each linked to its URL.

### Step 4 — SEO / AEO optimisation pass

Now stop writing and **audit the draft you just wrote as a skeptic**, against two
goals at once: rank on Google, *and* get recommended by AI chatbots (ChatGPT,
Claude, Perplexity). Go through `references/seo-aeo.md` and check, honestly:

**Search ranking**
- Does the primary keyword (founder + company) sit in the title, the first
  sentence, the subtitle, and an H2 — reading naturally, not stuffed?
- Does the article answer every search intent you identified in Step 1
  (owner / net worth / revenue / valuation / business model / status)? Find the
  sentence that answers each. If one is missing, it's a gap.
- Do the H2s read as plain editorial headings that name the entities, with no search-phrase or question headings, and does each section's first sentence state its answer?

**AI answer engines (AEO)**
- Is there a clean, self-contained factual sentence near the top that a chatbot
  could quote as the whole answer to "who founded X" or "what does X do"?
- Is every load-bearing fact stated *in the text* (not only implied by the embed)?
- Is the entity named consistently throughout — no long pronoun-only stretches?
- Does the Sources section make the page look like a corroborated reference?

**If you find gaps, rewrite to close them** — don't just note them. Rework the
opening, add the missing answer sentence, put the fact into a section's first sentence,
tighten the entity naming. Loop until the draft passes both goals. This pass is
what turns a good article into a ranking one; treat it as real work, not a
rubber stamp.

### Step 5 — Infographics (only if the content supports them)

Look at the article you've written and decide, honestly, whether its **data**
warrants a visual — this is content-driven, not automatic. Read
`references/infographics.md` for the decision logic and templates. In short:

- A real number **series** (revenue by year, funding rounds) → **bar chart**
- A dated **sequence** of milestones → **timeline**
- One dominant **hero number** that clears the $10M / ~₹80cr bar → **stat card**
- Two genuinely **comparable** figures → **comparison bars**

**Default to a timeline** ("<Company> · The arc") whenever the story has 3 or more
dated milestones; most founder stories do. Generate **0–2** charts — only the ones the data truly supports. A weak or
decorative chart is worse than none; if the numbers are thin or unverified, make
none, and say so. Every figure in a chart must be verified (same standard as the
body); never chart an estimate as fact.

For each warranted chart: write the filled FT template HTML (from
`references/infographics.md`, using the `{{FT_LOGO}}` token), then render it to a
PNG with `scripts/render.sh <file.html> <out.png> <w> <h>`. The render needs
Chrome or Chromium (set `CHROME=` to its path; on Linux the script adds
`--no-sandbox`). Then **embed the PNG in the copy doc** where it sits in the
article, and hand the PNG over for the Substack upload.

### Step 6 — Tick every box: tags, checklist, deliver

Assign **1–3 tags** from the fixed taxonomy in `references/tags.md` — never invent
a tag.

**Write the thumbnail prompt.** Produce the 5 candidate hook lines, pick the
strongest, and output one ready-to-paste **ChatGPT image prompt** from
`references/thumbnail.md` — the **dark red FT design** (near-black oxblood + red
bokeh, `FOUNDER THESIS ✕ GUEST` lockup, red `COMPANY · CATEGORY` pill, big condensed
all-caps white headline, subtitle, `founderthesis.com`, guest cut-out on the right),
with the slots filled. The user runs it in ChatGPT with the founder's photo
attached. Never spec a white/light background.

Then run the final checklist below against the draft and fix anything still
missing. Every box must be ticked before you hand over.

## Final checklist (run before delivering)

- [ ] 5 title options, each under 10 words, curiosity-led and true, NOT `Title | Company`; 2 flagged for A/B
- [ ] Ready to publish in one pass: no approval stops; only the title is left to pick
- [ ] First person, Akshay's voice; opens on a thesis the company's facts reinforce; riches-in-niches framing with an Indian comparison
- [ ] $10M rule respected — no sub-$10M / sub-₹80cr figure headlines a title or thumbnail line
- [ ] SEO/AEO pass done — every Step-1 search intent has an answer sentence; a clean quotable answer sentence sits up top; gaps rewritten, not just noted
- [ ] Subtitle < 155 chars: company + number + outcome
- [ ] Answer-first fact sentence woven into the opening (founder, company, headline number)
- [ ] Primary keyword (founder full name + company) in the title, first sentence, subtitle, and an H2
- [ ] 1,200–1,800 words (up to ~2,500 only for a famous, high-competition name); no padding
- [ ] 5 thumbnail copy lines delivered
- [ ] Ready-to-paste ChatGPT thumbnail prompt delivered — the dark red FT design (never white bg), built around the chosen hook
- [ ] H2 every 200–300 words: plain editorial headings that name the entities, no search-phrase or question headings; each section's first sentence states its answer
- [ ] A hard number in the first 200 words
- [ ] Full name + company + role stated and repeated
- [ ] 2–5 guest pull quotes, edited for grammar only
- [ ] 3+ internal FT links from the Episodes database, woven into sentences
- [ ] YouTube and Spotify embeds plus the Apple Podcasts · Amazon Music line near the top; facts also in text
- [ ] Guest and company linked on first mention
- [ ] Sources section: the episode plus every outside source by publication and date
- [ ] 1–3 tags from the fixed taxonomy
- [ ] Infographic(s) generated only where the data warrants (0–2); none forced; every charted number verified
- [ ] Every number traceable to the transcript, the dossier or a cited public source; paid-database figures only when the guest's side has made them public — nothing invented

## Output format

Write it into the **Substack article** tab of the episode's copy doc, in this
order: **Pick a title** (the five options, two starred), the **subtitle**, the
**article** (embeds as bare URL lines, pull quotes, the timeline image in place,
the Sources list), then **Reviewer notes** containing:

- **5 title options** (the recommended one plus 4 alternates, with the 2 you'd
  A/B test flagged)
- **5 thumbnail copy lines** to choose from — short, punchy, each landing the hook
  (same $10M rule — a number only appears if it's ≥ $10M / ~₹80cr+)
- **A ready-to-paste ChatGPT thumbnail prompt** — the **dark red FT design**
  (`references/thumbnail.md`), built around the strongest hook with the
  `COMPANY · CATEGORY` pill and subtitle filled, for the user to paste into ChatGPT
  with the founder's photo attached. Substack's thumbnail slot is 420×300 (7:5) —
  generate at 1260×900 (same ratio, 3× for retina). Never a white background.
- the **tags** (1–3 from the taxonomy)
- the **fact sheet** and a **number check** (each figure with its transcript timestamp or source)
- any **paid-database figures left out** because the guest's side hasn't made them public
- any **facts to verify** (unverified details, and quotes to check against audio)
- any **infographics** generated (the PNG(s), or the filled template HTML to
  render), with a note on where each sits in the body — or a line saying the data
  didn't warrant one

Do not publish — the person picks the title and thumbnail line and publishes
themselves.

## Reference files

- `references/intent-report.md` — **read first.** What ranks on this site, the
  search-intent taxonomy, the measured winning article shape, and the $10M rule
- `references/voice.md` — Akshay's first-person voice, register, and exemplars to match
- `references/seo-aeo.md` — title/subtitle formula, the search-query patterns to
  target, and the AEO structure
- `references/tags.md` — the fixed 10-tag taxonomy and how to assign
- `references/infographics.md` — when the content warrants a chart, the 4 FT
  templates, and how to render them to PNG (`scripts/render.sh`)
- `references/thumbnail.md` — the ready-to-paste ChatGPT thumbnail prompt (the dark
  red FT design: oxblood + red bokeh, condensed white headline, guest cut-out, pill)

## Lessons

- 2026-11-27 (Akshay with Ranjita, call 27 Nov 20:10 JST): every title carries the founder's name and the company name (SEO). Add imagery: license-free images or an image prompt showing the product in real life (e.g. an EV auto with the Fyn Mobility logo), never a dry text-only post. The preview image must be the right size; to get one, give Claude a previous thumbnail as the example and ask for the prompt. Ranjita decides keep or cut on anything sensitive or off the record. No editing inputs from the guest before publishing (decision 645).
