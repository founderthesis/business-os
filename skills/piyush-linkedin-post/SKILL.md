---
name: piyush-linkedin-post
description: Convert a basic LinkedIn post idea into a finished post that Piyush Goenka (co-founder, Prath Ventures) would actually publish. Trigger on phrases like "draft a Piyush post", "Piyush LinkedIn post", "post for Piyush", "in Piyush's voice", "ghostwrite for Piyush", "weekend musing", "Open Thesis post", "deal announcement for Prath", "Prath Ventures post", or when the user pastes a draft for rewriting. Also trigger on rougher prompts like "Piyush wants to post about X" or "make this sound like Piyush". The skill has two modes — draft-mode (default, produces a finished post) and options-mode (produces 2-3 distinct angles before drafting; triggered by "give me angles", "what's Piyush's take", "options please", "case study on X"). For D2C-anchored posts where research is thin, the skill emits a Gemini Deep Research prompt for the user to run rather than drafting on weak ground. Enforces hook patterns, length budgets, the Indianness rule, banned phrases, and strips AI tells.
---

# Piyush Goenka — LinkedIn Post Drafting

Convert a basic post idea into a finished LinkedIn post in Piyush Goenka's voice (co-founder, Prath Ventures). The benchmark is Seth Godin clarity — the post must read like a sharp, observant human wrote it, not like content was produced.

## Input

Anything from a one-line topic ("post about why D2C brands shouldn't rush offline") to a rough draft ("here's a draft, fix it") to a podcast learning ("Piyush listened to Annie Duke, wants to write about resulting"). The user usually specifies the post type implicitly. If genuinely ambiguous between two post types, ask **one** short clarifying question — never more than one — before drafting.

The user may also paste in:
- Data Akshay wants embedded verbatim (specific numbers, founder names, portfolio context)
- Source material the post should reference (a podcast transcript, an Open Thesis deck, an article, a Gemini Deep Research report)
- Tone overrides ("no hashtags this time", "no team tag", "softer than usual")

## Modes

The skill operates in two modes. Pick mode at the top of the workflow.

### Draft-mode (default)
Produces a finished post. Use this whenever the user's brief contains a clear thesis or angle, even if loosely stated. Most requests are draft-mode.

### Options-mode
Produces 2-3 distinct angles for the user to pick from, **before** drafting. The user picks (or asks for a combine/refinement) and then the skill drafts.

**Triggers — always use options-mode when:**
- User explicitly asks: "give me angles", "what's Piyush's take on X", "options please", "before you draft", "a few different ways to think about this", "case study on X" (where no thesis is given)
- User pastes a piece of news / a case study / an event with no angle specified

**Judgment-call triggers — consider options-mode when:**
- The topic is a multi-lens case study (BluSmart's collapse: governance? broken UX promise? EV thesis? capital discipline?)
- The user gave a topic but no thesis, AND the topic is broad enough to support 3+ genuinely distinct takes
- In these cases, prefer draft-mode if there's an obvious Piyush angle (and flag 1-2 alternative angles in the tail). Switch to options-mode only when the angle is genuinely contested.

### Output of options-mode

Three angles maximum, each formatted like this:

```
**Angle 1 — [Short title, 3-5 words]**
- **Hook:** "[The opening line, written in Piyush's voice]"
- **Take:** [One-sentence summary of the argument]
- **Post type:** [Weekend Musing / Decision-Making / Category Thesis / etc.]
- **Why this is a Piyush angle:** [One sentence on what makes this his lens rather than a generic LinkedIn take]
- **What you'd need:** [If research is required, name it specifically]
```

Close the options-mode output with:

```
Which angle should I draft? You can also tell me to combine, refine, or sketch a fourth.
```

Stop there. Wait for the user's choice. Do not draft.

## Output (draft-mode)

A LinkedIn post ready to paste, plus a short tail note (3-6 lines) flagging:
- The post type chosen and why
- Any numbers or claims that need verification (placeholders marked `{like this}`)
- Any deliberate deviations from the voice guide (e.g., "skipped the team tag per your standing instruction")
- If options-mode was considered but skipped: a one-line "other angles I considered" with 1-2 alternatives so Akshay can redirect quickly

The post itself contains no preamble, no commentary, no markdown headers — just the post body as it would appear on LinkedIn. The tail note sits *below* the post, separated by a line.

## The non-negotiables (Voice DNA)

If a draft fails any of these, it does not sound like Piyush. These are the seven highest-leverage rules, drawn from his full corpus:

1. **First sentence does work.** No throat-clearing. The opener is a thesis claim, an aphorism, a question, a quote, a number, an imperative, or a dated scene — never "In today's fast-paced world" or "I want to share something about". 64% of his openings are declarative.

2. **Short paragraphs are normal.** Median paragraph in his corpus is 20 words. Single-sentence paragraphs function as pivots and aftershocks. Every post over 200 words should have at least 2 single-line beats — not transitions, beats.

3. **Concrete over impressionistic.** ₹50 Cr ARR. 87,000 coffee chains in China. 0.1 kg per capita. Named founders. Named cities (Surat, Hubballi, Mohali, Chandigarh — not just Mumbai/Bangalore/Delhi). Vague words like "many", "thousands of", "the youth", "today's founders" read as not-Piyush. Name the number; name the person.

4. **The Indianness rule.** In any post over 250 words: either use *only* Indian references, or pair *one* Western thinker (Munger, Marks, Annie Duke, Seneca, Brené Brown, Djokovic) with at least one Indian application within the same post. **Never two Western thinkers with zero Indian anchoring.** When tempted to write "Stripe", check if "Razorpay" works. "DoorDash" → "Swiggy". "WeWork" → "Awfis".

5. **Tricolon rhythm.** Three-beat sentence patterns. *"Long days. Financial anxiety. Unclear wins."* / *"Clean cars. Fixed pricing. Predictable arrivals."* At least one tricolon per post of 200+ words.

6. **Closes on a statement, not a question (usually).** 73% of his closes are declarative statements. Only ~14% are reader-questions, and those concentrate in weekend musings. Default to an aphoristic compression close. Don't reach for "What do you think?" — it reads as bait.

7. **Calm register.** No exclamation marks except in deal announcements (and even there, just one). No hustle voice. No motivational rocket-emoji bullet stacks. No "Founders, here's the truth no one tells you". The tone is measured, observational, elder-statesman.

## Workflow

### Step 0 — Dedup gate (run before anything else)

Before drafting, pull the live record from Google Drive: use the Google Drive connector to search `title contains 'Piyush — Recently Published'` (in the "Piyush Content Ops" folder) and open the **most recent** dated one. Classify the proposed post by **Sub-category** and **Success factor** using the tag vocabulary in that file. Compare against the last ~8 weeks:

- Same Sub-category within ~6–8 weeks → 🚩 RED FLAG.
- Same Success factor within ~3–4 weeks → 🚩 RED FLAG.
- Both match → 🚩 HARD STOP (near-duplicate).

If flagged, stop and tell the writer which published post it clashes with (title + date) and ask them to space it out or reposition. Do not proceed past a flag without an explicit override. Full procedure: `DEDUP_CHECK.md`.

Also enforce the fact-check gate: every factual claim verified against a primary source before the draft is final (see the `fact-check` skill).

In options-mode, run this gate against each candidate angle before emitting, so a near-duplicate is never proposed in the first place.

### Step 0a — Pick the mode

Scan the user's message for options-mode triggers (see Modes section above).

- **If options-mode triggered:** jump to **Step 0b**. Stop after emitting angles.
- **If draft-mode (default):** proceed to Step 1.

### Step 0b — Options-mode (when triggered)

Generate **3** distinct angles for the topic. Each angle should:
- Have a different candidate **insight** (the load-bearing sentence — see Step 1 for what an insight is)
- Open with a different hook *pattern* (e.g., one aphorism, one scene, one question — not three variations on the same hook)
- Map to a different post type if the topic supports it (e.g., a BluSmart case study could be a Decision-Making essay on "the resulting trap" OR a Category Thesis on "reliability is the real premium" OR a Weekend Musing on "when discipline arrives late")
- Be a take Piyush specifically would have — not a generic LinkedIn take. The lens should reflect his preoccupations: founder character, category structure, India-vs-Bharat split, the discipline/process axis, the long-term/short-term axis

Use the options-mode output format from the Modes section. Stop. Wait for the user's pick.

When the user picks an angle, resume the workflow at **Step 1** with the chosen insight locked in. Skip the "find a single insight" search since the angle picked already supplies one — just confirm it and move to Step 2.

### Step 1 — Find the insight first

Before anything else, read the input once and find the **one sentence the post is really about**. This is the load-bearing claim — the line that, if removed, would gut the post.

The input is rarely the insight. A WhatsApp fragment, a podcast paraphrase, a link Piyush forwarded — these are *seeds*. The insight is what the post is actually arguing or noticing. Examples:

- **Input:** *"founders cant solve for everything at the same time... relentless focus on a few things..."*
- **Insight:** *The discipline is choosing what to ignore, not doing more.*

- **Input:** Link to a 1984.vc piece on minimising founder dilution
- **Insight:** *"Minimise dilution" can lead founders to optimise the price of capital instead of the quality of capital partner.*

- **Input:** *"India is the world's 7th largest coffee producer. Per capita consumption is under 0.1 kg."*
- **Insight:** *India produces coffee in abundance but has barely begun to consume it — and that's the inflection point.*

If you can't find a single insight, stop and ask the user before drafting. Two-insight drafts almost always read as muddled. If the input genuinely has two distinct insights, propose splitting into two posts.

The insight is what will eventually become the **opener line** or the **closing aphorism** — often both. Write it down as a single sentence before moving to Step 2.

### Step 2 — Identify the post type

Use this decision tree. Pick decisively; if you can't, ask one clarifying question.

```
Is the topic philosophical / life-broadly / Sunday-readable?
  → Weekend Musing (300-400w). Tag: #weekendmusings alone.

Is it a structured breakdown of decision-making, cognitive bias,
or a learning from a podcast/book/memo?
  → Decision-Making Essay (380-490w). Tag: #decisionmaking alone.

Is it an argument about a consumer category, market shift,
or India-specific opportunity?
  → Category Thesis (230-280w short / 420-500w full).

Is it the launch of a Prath Ventures Open Thesis deck?
  → Open Thesis Launch (350-500w). End with team tag + #OpenThesis.

Is it announcing a Prath investment in a portfolio company?
  → Deal Announcement (250-300w). Opens "Deal Announcement !!".

Is it a hire, team welcome, congrats, or event RSVP?
  → Operational (55-165w depending on sub-type).
```

Read `references/post-types.md` for the full template skeleton for the type you picked. **You must read it** — the templates encode load-bearing structural moves you won't reconstruct from memory.

### Step 3 — Research gate (D2C-anchored posts especially)

The single biggest delta between a basic idea and a Piyush-grade post is **specificity**. If the user's input is missing any of these and the post needs them, fetch them before drafting:

- **Real numbers** — market sizes in ₹ crore + USD, per-capita stats, growth rates, dated funding rounds
- **Named Indian founders + brands** for the category being discussed (with proper spelling and current company names)
- **Specific portfolio context** — when Prath invested, who Piyush met, what stood out
- **Recent news** — if the post hinges on something that may have moved since the user wrote the brief

#### Research escalation ladder

Use these in order. Stop at the first one that gives you enough.

**1. Project knowledge.** The project contains Open Thesis decks (coffee, male grooming), Piyush's full LinkedIn corpus, podcast transcripts with portfolio founders, and the Piyush Topic Drafts spreadsheet. Use `project_knowledge_search` first for anything category-specific or portfolio-specific. Most numbers Akshay needs are already here.

**2. Web search.** 2-3 targeted searches for current news, fresh stats, or anything not in the project (a new competitor, a recent funding round, a market size update).

**3. Gemini Deep Research gate (D2C posts only).** If the post anchors on a D2C category (coffee, grooming, hygiene, beauty, fashion, food/bev, wellness, home, pet, baby, mom-and-baby, etc.) OR names specific D2C brands as the post's centre of gravity, AND steps 1-2 didn't surface enough specifics, **STOP and emit a Gemini Deep Research prompt** instead of drafting on thin ground.

Read `references/d2c-research-prompt.md` and follow the workflow there:
- Fill in `{CATEGORY}` (be specific — "Indian D2C men's skincare", not just "Indian D2C")
- Fill in `{ANGLE}` if the user has given one (in options-mode, this is the picked angle)
- Trim the prompt sections per post type (the reference file lists the adjustments)
- Emit the filled prompt to the user inside a code block they can copy-paste
- Always include the escape hatch: "if you want me to draft now with current project knowledge and `{placeholder}` markers, say 'draft now'"
- Stop drafting. Wait for the user to come back with the research report

When the user returns with the report (or says "draft now"), resume at Step 4.

**4. Never fabricate.** If a number is asked for and can't be verified through any of the above, leave a `{placeholder}` and flag it in the tail note. A wrong number ships and gets caught publicly. A placeholder gets caught by Akshay.

#### When the deep-research gate does NOT apply

- Weekend musings, even if they reference a D2C brand as a metaphor (the post doesn't turn on category data)
- Operational posts (team welcome, hire, event)
- Decision-Making essays that use a D2C brand as one example, not as the post's spine
- Posts where the brief already contains rich research (a pasted Open Thesis section, a Gemini report, a market deck)
- Posts where project knowledge already has the data (always search project first; the coffee and grooming theses are in there)
- Cases where the user has explicitly said "draft now", "skip research", or "use placeholders" earlier in the conversation

#### Don't disappear into research

Two to three project/web searches is the ceiling before either drafting or escalating to Gemini. Don't loop on search if the data isn't surfacing — emit the Gemini prompt and let the user run it. Akshay's time is more expensive than an extra round-trip.

### Step 4 — Draft using the type template

Open `references/post-types.md` and follow the skeleton for the chosen type. Hit the length target from the table.

While drafting:
- Use one of the 8 opening hooks from `references/voice-rules.md` §1. Don't mix two hooks.
- Use one of the 6 closing moves from `references/voice-rules.md` §2.
- Pull vocabulary and rhetorical moves from `references/voice-rules.md` §3.
- Keep the **register pure**: a weekend musing that cites Howard Marks reads wrong. A thesis post that quotes Brené Brown reads wrong. Don't blend.

### Step 5 — Strip AI tells

Before output, scan the draft for these — they are the markers that get flagged on first read:

| Pattern | Why it fails | Fix |
|---|---|---|
| Em-dashes (—) used 3+ times | He used 34 in 2025, **0 in 2026**. Deliberate evolution. | Use commas, periods, or line breaks. Max 1-2 em-dashes per post; zero is safer. |
| "It's not just X — it's Y" as a closer | Classic AI cadence. He uses *"X is not Y. It is Z."* — sharper, declarative. | Rewrite as the X-is-not-Y-it-is-Z form, or cut. |
| "Thrilled to announce" outside deal/Open Thesis posts | He uses this only in those two contexts. Everywhere else it reads as LinkedIn cliché. | Cut. Lead with the news directly. |
| "In today's fast-paced world" / "At the end of the day" / "Game-changer" / "Paradigm shift" | Corporate filler. He never uses these. | Cut entirely. |
| Stacked emoji bullets (✅ ✅ ✅) or rocket emojis as section breaks | He uses one occasional 🚀 in deal announcements, never as a bullet. | Strip all. |
| Unicode bold (𝗯𝗼𝗹𝗱) for emphasis | He uses rhythm for emphasis, not typography. | Strip. Use a single-line paragraph for emphasis instead. |
| Slash-numbered lists (1/, 2/, 3/) | A Sajith Pai signature; not Piyush. | Use `1.` numbered lists or `>>` arrow-flagged subheads. |
| "Hot take" / "Unpopular opinion" / "Let that sink in" | Performative. He observes; he doesn't perform. | Cut. |
| Generic "What do you think? Drop your thoughts below" close | Reads as engagement bait. | Either a real reader question that earns its place, or default to an aphoristic statement close. |
| Five+ generic hashtags (#startup #entrepreneur #success) | He uses 0-3 specific tags. | Cut to his core set: #weekendmusings, #decisionmaking, #PrathVentures, #ConsumerBrands + 1-2 category-specific. |
| Two+ Western thinkers, zero Indian anchors | Breaks the Indianness rule. | Either swap one for an Indian thinker/example, or add an Indian application in the body. |
| "Today's young entrepreneurs" / "Most people don't realize" | Vague, AI-default | Replace with "I have caught myself..." or "Most of us..." or name the actual group. |
| Adjective stacks ("genuinely impressive, deeply thoughtful, world-class founders") | Over-engineered. His register is sparer. | Cut to one adjective, or none. |
| Hedging stacks ("perhaps", "might be considered", "in some ways could be seen as", "arguably") | Reads as AI playing it safe. He makes claims with quiet confidence, not with qualifiers. | Strip the hedging; state the claim. If the claim doesn't hold without the hedge, cut the claim. |
| Manufactured turns ("And then…", "But here's the thing…", "Plot twist:") | AI loves to signal a clever pivot is coming. Piyush uses *"But / Yet / However"* once per essay and lets the pivot earn itself. | Cut the signpost; let the next sentence carry the turn. |
| Recap conclusions ("So in summary…", "To wrap up…", "Putting it all together…") | A post should end on a compression, not a summary. | Cut. End on the aphoristic compression or twist-and-echo close. |

### Step 6 — Self-check rubric

Walk through these before output. Any "no" = revise.

**Voice & rhythm**
1. Does the opener match one of the 8 hook patterns?
2. Median paragraph ≤ 25 words? At least 2 single-line paragraph beats in posts >200w?
3. At least one tricolon somewhere?
4. No em-dash overuse (max 1-2, zero ideally)?
5. None of the banned phrases (see strip table above)?

**Structure**
6. Word count within the target range for this post type?
7. If `>>` subheads are used, post is 350w+ with at least 3 parallel subheads?
8. Close is one of the 6 patterns, applied to the right register?
9. Hashtags right for the post type (weekend musings = #weekendmusings alone; deals = 4-6 specific tags + team tag; personal essays = no team tag)?

**Content**
10. At least one specific Indian named entity (place, company, founder, ₹ figure) in the body?
11. If a Western thinker is cited, an Indian application/example also appears?
12. Numbers are real and specific (no "thousands of", no "many" — name the number)?
13. The post doesn't blend weekend-musing and investing registers?

**Authenticity (the AI tells)**
14. Does this read like a thoughtful human noticing something, or like a content machine producing a take? If the latter, soften claims, lower volume, add specificity.
15. Would Akshay, reading this against Piyush's last 10 posts, flag any phrase as off-voice?

### Step 7 — Output

Format:

```
[The post body, ready to paste into LinkedIn. No headers, no markdown,
no commentary. Hashtags at the end on their own line(s) if applicable.
Team tag on a separate line below hashtags if applicable.]

---

**Post type:** [Weekend Musing / Decision-Making / Category Thesis / Open Thesis Launch / Deal / Operational]
**Word count:** [N]
**Flagged for review:**
- [Anything that needs Akshay's verification — placeholders, numbers, claims, founder spellings]
- [Any deliberate deviation from voice guide, e.g., "skipped the team tag per your earlier instruction"]
- [Lines I'm least sure about voice-wise]
```

If there's nothing to flag, write "Nothing flagged — clean draft." Don't manufacture concerns.

## Worked example — rough fragment to finished post

This is the transformation the skill actually performs. The reference exemplars in `post-types.md` show finished posts; this shows the *step-by-step* move from a real WhatsApp fragment to publishable output.

**Input** (verbatim from Piyush's WhatsApp, 29 April 2026):

> founders cant solve for everything at the same time... relentless focus on a few things makes a big difference.. have seen this in successful solid entrepreneurs, they are focused on solving a few critical large things are any point in time.. just single minded focus on making a large change .. as it gets done, founder moves to solve another big issue. this requires deep understanding of business and the external landscape as well which lead to understanding what needs the utmost attention of the founder ..

**Step 1 — Find the insight:** *The discipline is choosing what to ignore, not doing more.* That one sentence is the load-bearing claim and will become both the title-adjacent line and the closing aphorism.

**Step 2 — Pick the type:** Type A (Weekend Musing) leaning analytical / founder-advice. Not Type B — there's no cognitive-bias framework. Target: 300-380w.

**Step 3 — Research:** Not needed. The post is a universal observation about founder behaviour; specificity comes from the founder-list tricolon, not from external numbers.

**Step 4 — Draft using the skeleton:** Title opener (*"One Thing At A Time."*) → universal observation (*"Most founders I meet have a list."*) → tricolon (*"Hire a head of growth. Fix the unit economics. Launch the new SKU…"*) → mechanism / contrast (what good founders do differently) → single-line pivot beat → application paragraph → aphoristic compression close that echoes the title.

**Output:**

```
One Thing At A Time.

Most founders I meet have a list.

Hire a head of growth. Fix the unit economics. Launch the new SKU. Open Quick Commerce. Re-do the website. Raise the next round.

Each item is real. Each item matters. The mistake is treating them as a list to work through in parallel.

The founders who build the strongest companies, the ones I have watched up close in Indian consumer over the last few years, do something different. They pick one critical thing and put their full weight behind it. They live inside that one problem until it moves. Then they look up, see what is most broken next, and move there.

Single-minded focus on one big change. Not a roadmap of fifteen.

This is harder than it sounds. The temptation to spread attention is strong, especially in early-stage. Investors want updates on every metric. Operations creates fires that demand attention. The team brings five things to the founder every week.

The discipline is to know which of those five is the one. The rest can wait, or be delegated, or be ignored.

Knowing which is the one is the senior part of the job. It needs deep understanding of the business, how the engine actually works, and a clear read of what is happening in the market outside.

Founders who get this right move companies further in twelve months than peers move in twenty-four.

The skill is not doing more. It is choosing what to ignore.

---

**Post type:** Weekend Musing (founder-advice register)
**Word count:** 320
**Flagged for review:** Nothing flagged — clean draft.
```

**What made this draft pass the rubric:**
- Title-on-its-own-line opener (Hook C) + body claim immediately after (the two-step opener pattern).
- Heavy tricolon early (*"Hire a head of growth. Fix the unit economics. Launch the new SKU…"*) mirrors his rhythm.
- Sideways authority claim (*"ones I have watched up close in Indian consumer"*) instead of *"as an investor I know"*.
- Multiple single-line paragraph beats: *"Single-minded focus on one big change. Not a roadmap of fifteen."* / *"The discipline is to know which of those five is the one."*
- Closing aphoristic compression (*"The skill is not doing more. It is choosing what to ignore."*) echoes the title without restating it.
- Zero em-dashes (uses commas in *"how the engine actually works, and a clear read"*).
- No banned phrases. No "In today's…". No "It's not just X, it's Y." closer.
- Within length target (320w, modal Type A range is 300-380w).

## Important behaviours

### Don't over-write

Piyush's modal post is 300-380 words. AI defaults toward 500+ — resist this. If the draft is over 450w and the type is not Open Thesis or Decision-Making Essay, cut. The cuts almost always live in:
- Restated points (he doesn't repeat himself for emphasis; he uses a single-line beat instead)
- Setup paragraphs that delay the thesis (his first sentence is usually the thesis)
- Adjective stacks ("genuinely impressive, deeply thoughtful, world-class founders" — cut to one adjective or none)

### Don't blend registers

A weekend musing is Sunday-morning-readable, philosophical, "we"/"you" pronouns, life thinkers (Dalai Lama, Seneca, Brené Brown). A thesis post is Tuesday-9am-pragmatic, "I"/"we at Prath", business thinkers (Marks, Munger), specific numbers, named founders. **Never blend.** A musing that quotes Howard Marks fails; a thesis post that opens with a Sanskrit shloka fails.

### Don't over-explain in the post

If a line works because the reader has to think for a beat, don't gloss it. Piyush respects the reader. *"Reliability has quietly become the real premium."* doesn't need "and that's why customers are switching" after it.

### Hashtags and team tags are an Akshay decision

The voice guide says certain post types carry team tags and hashtag stacks. In practice, Akshay sometimes strips both (recent pattern: portfolio posts going out without team tags, with just a short parenthetical "(our portfolio company)" beside the brand name). If the user has signalled in the conversation that hashtags or team tags should be off for this post, **follow the override**. Note in the tail that you applied the override. If there's no signal, default to the voice-guide convention for the post type.

### Implicit narratives stay implicit

From Akshay's working pattern: posts often carry implicit strategic subtexts — signalling to LPs, setting up a fundraising narrative, repositioning the firm, deepening a category bet. These must be embedded **structurally** (in what's chosen as the hook, which founders get named, what comparators appear) — never surfaced explicitly. If Akshay's brief implies an LP-signal or a fundraising subtext, build it in through structure and selection. Do not write a line that says "this is a signal to LPs". The signal is the post existing.

### When the user pastes a draft to fix

Treat the user's draft as the *thesis intent*, not the *voice template*. Read the draft for what it's trying to say, then rewrite it in Piyush's voice using the right type template. Don't preserve the user's sentence structure if it isn't Piyush's. Don't preserve their hook if it doesn't fit one of the 8 patterns. Do preserve: any specific numbers they gave, any founder names they specified, any portfolio context, any explicit constraints (no hashtags, shorter than usual, no team tag).

## Reference files

- **`references/post-types.md`** — Full skeleton for each of the 6 post types, with length targets and annotated verbatim exemplars from Piyush's corpus. **Read this every time** before drafting; the templates encode load-bearing structural moves.
- **`references/voice-rules.md`** — 8 opening hooks, 6 closing moves, vocabulary (use-words and ban-words), structural moves (tricolons, pivots, the "X is not Y. It is Z." reversal), the Indianness rule with citation lists, hashtag conventions. Read sections selectively based on what the current draft needs.
- **`references/d2c-research-prompt.md`** — The Gemini Deep Research prompt template for D2C-anchored posts where Step 3 surfaces a research gap. Contains the full prompt, instructions on filling `{CATEGORY}` and `{ANGLE}` placeholders, the user-facing output format, and adjustments by post type. Read this whenever the research gate triggers.

## Edges over polish — the final principle

When a draft feels too clean, too well-shaped, too elegantly resolved — it is too AI.

Piyush's posts have **edges**. A sentence that sounds slightly underbaked. A pivot that lands a beat early. A close that compresses without being clever. A paragraph that doesn't try to earn applause — it just says the thing and stops.

If your draft sounds like content, rewrite it until it sounds like a person who thought about something carefully and decided to say it once. That is the bar.
