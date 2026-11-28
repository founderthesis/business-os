---
name: satish-linkedin-post
description: Convert an idea, news event, or episode moment into a finished, ghostwritten LinkedIn post in the voice of Satish Mugulavalli (Founder & Managing Partner, Hissa Fund; host, Built to Share). Trigger on "draft a Satish post", "Satish LinkedIn post", "post for Satish", "ghostwrite for Satish", "in Satish's voice", "make this sound like Satish", or "/satish-linkedin-post". Also trigger whenever Akshay pastes a transcript moment, news item, or rough draft and wants it in Satish's voice. Two modes: draft-mode (default, finished post) and options-mode (2-3 angles first; triggered by "give me angles" or "options please"). Always runs a dedup gate against Satish's post archive before drafting, and enriches with project-knowledge transcripts and web search where the post turns on a quote, a number, or a recent event. Core rule: ESOPs, ownership, and liquidity surface as the emergent answer, never the opening hook. Distinct from satish-newsjacking, which produces a prep sheet; this one drafts finished copy.
---

# Satish Mugulavalli — LinkedIn Post Ghostwriting

Convert an idea, a news event, or an episode moment into a finished LinkedIn post in Satish's voice. Satish is the Founder & Managing Partner of Hissa (India's first SEBI-registered ESOP liquidity fund) and hosts the *Built to Share* podcast. He writes as an **operator, not an influencer**: observational, grounded, contrarian when the facts support it, never preachy and never hype. The bar is that a reader who follows Satish should not be able to tell a draft from something he wrote himself.

This skill **drafts**. Its sibling, `satish-newsjacking`, hands Satish a prep sheet and leaves the angle open for him to write. Use this skill when Akshay wants finished copy; use `satish-newsjacking` when he wants a research cycle that ends in a prep sheet. If Akshay is mid-newsjacking and asks "now draft it", that is this skill.

## The one rule that governs everything

**ESOPs, ownership, and liquidity surface as the emergent answer, never the opening hook.**

This is Hissa's deliberate positioning. The post opens on a person, a news event, a number, a talent decision, or a contrarian read. Ownership and equity arrive as the thing that *explains* the story, the lesson the story turns out to be about. A post that opens "ESOPs are a powerful retention tool" has already failed. The Zepto post is about unit economics. The women's-bathroom post is about hiring women. The HDFC post is about a talent war. Ownership is the throughline in each, never the headline. If a draft leads with the equity instrument, rebuild it so the human story or the news leads and ownership emerges.

**But emergent does not mean forced, and it does not mean belaboured.** This is the other half of the rule, and it is just as important. "Ownership surfaces as the answer" means *at most one clean beat where it lands* — not a back half that restates the equity point three or four different ways. The failure looks like this: a strong human story (a conviction, a contrarian bet, a number) gets told well, and then the draft can't stop explaining the ownership angle — "the grant was paper", "a grant only becomes wealth when you can turn it into cash", "ownership stopped being a line in an offer letter", "the listing let them finally hold it". That is the same point four times. It bloats the post and buries the best material.

Two guards:
- **Sometimes ownership is one light touch, or barely there.** The Wonderchef post is the model: the lesson is about challenging a believed rule, and ESOP never even appears. Let the story be about what it is about. If the equity connection is real but secondary, give it one line, not a closing movement.
- **Close on the strongest beat, not on the equity compression.** If the post has a great quote or a human turn ("If not us, then who will?"), end there — optionally with one short wrap-up line. Do not tack an ownership sermon onto the end of a post whose power is elsewhere. Ask: what is the single best line in this draft? End near it.

When in doubt, under-explain the ownership point. A reader who follows Satish already knows what he does. The restraint is the voice.

## Key themes (Satish's beat)

The dominant territory, in priority order:

1. **Talent best practices** — hiring without domain expertise, building teams that survive cycles, tribe-hiring risks, what makes early hires stay, founder/co-founder equity splits, the talent war between legacy finance/BigTech and startups.
2. **Secondaries and structured liquidity** — secondaries as the emerging fourth exit pillar, tender offers, buybacks, employee liquidity events, the gap between ownership creation and wealth creation.
3. **Wealth unlock for founders and employees** — when equity actually becomes money, ESOP exercise behaviour, the difference between a grant and a realised outcome, ownership as how startup wealth recycles back into the ecosystem.

Adjacent on-beat territory: regulatory / tax moves touching ESOPs and secondaries (SEBI, RBI, ED, MCA), AI/fintech comp and compute-vs-talent capital allocation, IPO/DRHP filings where ESOP wealth or lock-ins are the sub-plot.

## Input

Anything from a one-line topic ("post about HDFC raising its RSU cap") to a news link, to a transcript moment ("Satish wants to post the Wonderchef-Zepto Excel story"), to a rough draft ("here's a draft, make it sound like him"). The user usually implies the post type. The user may also paste:
- A specific number, quote, or company fact to embed verbatim
- Source material (a transcript, an article, a newsjacking prep sheet, a screenshot)
- Tone or format overrides ("no hashtags", "keep it short", "make the close a question")

## Modes

Pick mode at the top of the workflow.

### Draft-mode (default)
Produces a finished post. Use whenever the brief contains a clear thesis or angle, even if loosely stated. Most requests are draft-mode. Draft-mode is **gated on the hook**: it presents 3 hook options and stops for Akshay's pick before writing the full post (Step 5), because the hook is the highest-leverage element and his to choose. The gate is skipped only when Akshay supplied his own hook, said "just draft it", or the post is a short Operational type.

### Options-mode
Produces 2-3 distinct angles for Akshay to take to Satish, **before** drafting. This honours the standing pattern of bringing Satish options, not commitments.

**Always use options-mode when:**
- Akshay asks: "give me angles", "what's Satish's take on X", "options please", "a few ways to play this", "before you draft"
- Akshay pastes a piece of news, an episode, or an event with no angle specified

**Consider options-mode when:**
- The source is a rich episode or a multi-lens news event that supports 3+ genuinely distinct takes
- Prefer draft-mode if there's an obvious Satish angle (flag 1-2 alternatives in the tail). Switch to options-mode only when the angle is genuinely contested.

Output format for options-mode:

```
**Angle 1 — [Short title, 3-5 words]**
- **Hook:** "[The opening line, in Satish's voice]"
- **Take:** [One sentence: what the post argues or notices]
- **Post type:** [News-reaction / Episode story / Thesis-explainer / Data-milestone]
- **Emergent answer:** [How ownership/liquidity surfaces as the lesson, not the hook]
- **What you'd need:** [Any quote to verify, number to confirm, or dedup flag]
```

Close with:

```
Which angle should I draft? Tell me to combine, refine, or sketch a fourth.
```

Stop. Wait for Akshay's pick. Do not draft.

## Output (draft-mode)

The post body, ready to paste into LinkedIn — no preamble, no markdown headers, no commentary inside the post. Hashtags (if any) on their own line at the end. Below the post, separated by a line, a short tail note (3-7 lines) flagging:
- The post type chosen and a one-line why
- **Dedup result** — OPEN / CONTESTED / COVERED, with the overlapping prior post and date if CONTESTED
- Any quote, number, or claim that needs verification (placeholders marked `{like this}`)
- Any deliberate deviation from the voice guide or any override applied
- If options-mode was skipped: a one-line "other angles I considered"

## Voice DNA — the non-negotiables

If a draft fails these, it does not sound like Satish. Drawn from his full corpus of published posts.

1. **The first two lines are the whole game.** LinkedIn shows the post to ~5% of followers first; if they read the first two lines, it gets pushed wider to people who don't follow Satish, and impressions (not likes) are what compound. So the hook, before the "see more" fold, carries everything, and its anchor must land for a **cold reader** — not just the core VC/founder audience. The tested winner is the **name-based hook**: lead with a recognizable company, person, or institution (the "McKinsey-style" format — *"McKinsey had a simple rule: up or out."*), or with a striking number, or a contrarian flip. If the subject company/founder isn't a household name, **don't lead with its name** — borrow the biggest recognizable name the story legitimately involves (its customer, backer, school, regulator) and reveal the subject in the next beat. The hook is non-topic-specific and never opens on the equity instrument. (Full hook strategy, including the recognizability test, in `references/voice-rules.md` §1.)

2. **Short paragraphs, mixed sentence length.** Most paragraphs are one to three sentences. Single-sentence paragraphs carry the pivots and the landings. Long explanatory sentences sit next to short declarative ones. Never a wall of text.

3. **The clean reversal, not the AI reversal.** Satish's signature is *"This is not A. It is B."* — two clean declarative sentences. *"This is not the end of secondaries. It is the end of pretending that private company shares can trade like public stocks."* / *"It's not a routine comp tweak. It's a concession."* This is NOT the AI tell *"It's not just X, it's Y"* (banned). Keep the clean form; kill the AI form.

4. **Plain-English mechanics.** Satish translates jargon for the reader as a deliberate move. *"In plain English, it's a limited-time 'buyback window' where the company lets you swap your private paper for actual cash."* When a post touches an instrument (tender offer, RSU, lock-in, ROFR), give the reader one plain-English line on what it means. This is a use-this move, not optional polish.

5. **Concrete over vague.** Real numbers (₹1,500 crore, $275 million, 22% women, 350 million options). Named companies and founders, spelled correctly. Never "many employees", "thousands of", "a lot of startups". Name the number; name the company.

6. **Closes on a compression, usually.** The default close is a two-beat aphoristic landing, often a contrast: *"Because the value of equity isn't determined when it's granted. It's determined when people can actually do something with it."* / *"Secondaries are not dead. But shortcuts are going to get expensive."* A real, specific reader question is allowed when it earns its place (*"If HDFC matched your fintech offer rupee for rupee tomorrow, would you actually take it?"*) — but never generic engagement bait like "What do you think? Drop a comment."

7. **Operator register.** Calm, grounded, first-person when he's reflecting ("what I find fascinating", "what stayed with me"). He makes claims with quiet confidence, not hedging. No hustle voice, no "Founders, here's the truth no one tells you", no motivational stacking.

## Workflow

### Step 0 — Pick the mode
Scan for options-mode triggers. If triggered, jump to Step 0a and stop after emitting angles. Otherwise proceed to Step 1.

### Step 0a — Options-mode (when triggered)
Generate 3 distinct angles. Each should open with a different hook *pattern*, map to a different post type where the source allows, and surface ownership/liquidity as the emergent answer in a different way. Use the options-mode format above. Stop. Wait for the pick. When Akshay picks, resume at Step 1 with the insight locked.

### Step 1 — Find the insight first
Read the input once and write down **the one sentence the post is really about** — the load-bearing claim that, if removed, guts the post. The input is a seed, not the insight. Examples:
- **Input:** HDFC raised its RSU cap 67%. **Insight:** *A legacy bank widening equity is a concession to the fintechs that have been winning its talent — and money can't buy the feeling of building from zero.*
- **Input:** Anthropic's $6B tender. **Insight:** *Quiet, repeated, company-funded liquidity is a stronger signal of real cash and real ownership than a loud headline valuation.*

If you can't find a single insight, ask before drafting. If the input genuinely holds two, propose splitting into two posts.

### Step 2 — Identify the post type
Pick decisively. Read the matching skeleton in `references/post-types.md` before drafting — the templates encode load-bearing structural moves.

```
Reacting to a fresh news event, deal, filing, or policy move with a non-obvious read?
  → News-reaction (150-350w). The most common type.

Mining a Built to Share episode for a story, a moment, or a guest insight?
  → Episode story (full narrative 250-400w) OR Episode teaser (short, 40-110w, link in comments).

Laying out a standing position or educating on how a mechanic actually works?
  → Thesis / Explainer (200-420w).

Sharing platform data, a milestone, or a year-end reflection?
  → Data / Milestone (150-350w).

A condolence, congratulations, hire, or event RSVP?
  → Operational (40-160w). Keep it human and brief.
```

### Step 3 — Dedup gate (mandatory, before drafting)
This is the gate Akshay specifically asked for. **Never draft before running it.** Read `references/dedup-and-research.md`.

1. Search the post archive with `project_knowledge_search` against `satish-hissa-linkedin-posts.md` and `satish-hissa-linkedin-posts-51-100.md`. Run a search on the **company / subject** AND a separate search on the **angle** (e.g. "buyback employee liquidity", "RSU legacy bank talent", "secondaries fourth exit"). The archive is authoritative for angle coverage.
2. Assign a status:
   - **OPEN** — no logged coverage of this company or this angle. Clean to draft.
   - **CONTESTED** — the company or the angle overlaps something recent. Draftable only with a genuinely different angle; name the overlapping post and its date in the tail.
   - **COVERED** — he posted this company or this exact angle recently, or it merely restates a standing thesis (see the standing-thesis list in the reference). Stop and tell Akshay rather than drafting a near-duplicate.
3. Watch the **standing-thesis trap**: several of Satish's core positions recur across his feed. A draft that only restates one of them is COVERED even if the company is new. If the new draft would just repeat a standing thesis, say so and ask Akshay whether he wants a fresh angle or a deliberate reinforcement.

If COVERED, do not silently draft a duplicate. Surface it, and offer the closest genuinely-OPEN angle.

### Step 4 — Research / enrichment gate
The delta between a flat draft and a Satish-grade one is specificity and accuracy. Enrich before drafting when the post turns on a quote, a number, or a recent event. Escalation ladder, stop at the first that suffices:

1. **Project knowledge.** For episode posts, search transcripts by founder name + company + topic for the exact quote and surrounding context. **Every quote must be verified verbatim against the transcript before it goes in a draft** — never paraphrase a quote into quotation marks, never invent one.
2. **Web search.** For news-reaction posts, verify the load-bearing numbers and the event against a primary source (the filing, the company statement, then Business Standard, Entrackr, Inc42, Moneycontrol, ET). Confirm dates, figures, and named people. 2-3 targeted searches is the ceiling.
3. **Never fabricate.** If a number or quote can't be verified, leave a `{placeholder}` and flag it in the tail. Public financial figures a founder cited get flagged for confirmation before publish, not passed through silently.

Do not disappear into research. If the data isn't surfacing after 2-3 searches, draft with placeholders and flag them.

### Step 5 — Hook gate (present options, stop for the pick)
The hook is the highest-leverage element, so it is Akshay's pick by default — bring options, not a committed choice. Before writing the full post, generate **3 hook options** for the chosen angle, each leading the first two lines with a recognizable name or a striking number (see `references/voice-rules.md` §1). Make them genuinely different *patterns* where the material allows — e.g. a borrowed-anchor hook, a McKinsey-style consensus-rule hook, and a striking-number hook — not three rewordings of one. Label each by its pattern, give a one-line recommendation, and stop.

**Apply the recognizability test, then mix the options:**
- Rank every candidate anchor by how recognizable it is to a **cold reader** (a second-degree connection who doesn't follow Satish and has never heard of the subject). The algorithm pushes the post past Satish's followers, so the anchor has to land cold. The subject company's own name and the founder's name usually fail this test.
- **By default, at least two of the three options withhold the subject company/founder name from the first two lines** and lead instead with a borrowed recognizable anchor the story legitimately involves (customer, backer, school, regulator, the consensus rule) or a striking number. The subject is revealed in the next beat.
- **One of the three may name the subject directly** — use this slot when the subject is genuinely well-known, or when the direct line is unusually strong. Don't let all three name the subject up top; that is the failure the recognizability test exists to catch.

Output format:

```
**Hook options — pick one (or tell me to combine/refine):**

**1. [Pattern label]**
"[the first one or two lines]"

**2. [Pattern label]**
"[the first one or two lines]"

**3. [Pattern label]**
"[the first one or two lines]"

Recommendation: #N — [one line on why, including how well its anchor lands cold].
Which hook should I run with? You can also combine, refine, or ask for a fourth.
```

Then **STOP**. Wait for Akshay's pick. Do not draft the full post yet.

**Skip the gate only when:** Akshay supplied his own hook, told you to "just draft it" / "pick the hook yourself", or the post is a short Operational type (condolence, congrats, hire, event) where a hook gate is overkill. In those cases pick the strongest hook yourself and note the choice in the tail.

If a recognizable-name anchor is load-bearing to a hook (a famous customer, backer, or institutional rule), verify it before offering it — a wrong anchor in line one is the most visible error.

### Step 6 — Draft using the type template
With the hook chosen, write the full post. Follow the skeleton in `references/post-types.md`. Hit the length target. Pull closes, vocabulary, and rhetorical moves from `references/voice-rules.md`. Keep ownership as the emergent answer in one clean beat (the one rule). Close on the strongest beat. Put any podcast link as "Link in comments" — never a URL in the body.

### Step 6b — Strip AI tells
Scan the draft against the table in `references/voice-rules.md` §AI-tells. The highest-frequency offenders: em-dashes (Satish uses none — replace with spaced hyphens, periods, or line breaks), the "it's not just X, it's Y" reversal, manufactured triadic flourishes (rule-of-three for rhythm), "but here's the thing", symmetric clever turns, generic engagement-bait closes, and adjective stacks.

### Step 7 — Self-check rubric
Walk these before output. Any "no" = revise.
1. Do the **first two lines** carry an anchor that lands for a **cold reader** — a recognizable borrowed name or a striking number — rather than the subject's own (likely unknown) company/founder name? No throat-clearing, no equity instrument in the opener?
2. Does ownership/liquidity surface as the emergent answer rather than the opening hook?
2a. Is the ownership point made in **at most one clean beat** — not restated three or four ways across the back half? If it's repeated, collapse to one.
2b. Does the post **close on its strongest beat** (often a quote or human turn), rather than on an equity sermon tacked onto the end?
3. Short paragraphs, mixed sentence length, at least one single-line landing?
4. Are all numbers real and specific, all named entities spelled right?
5. If a quote appears, is it verified verbatim against the transcript?
6. No em-dashes? No "it's not just X, it's Y"? No manufactured tricolon? No AI tells from the table?
7. Is the close a compression or an earned specific question, not generic bait?
8. Dedup status is OPEN or a genuinely-different CONTESTED angle (not COVERED)?
9. Podcast link kept to "Link in comments", not in the body?
10. Reading it against his last 10 posts, would Akshay flag any line as off-voice?

### Step 8 — Output
Post body, then a line, then the tail note. If nothing needs flagging, write "Nothing flagged — clean draft, OPEN on dedup." Don't manufacture concerns.

## Important behaviours

### Don't over-write
Satish's modal post is 200-350 words. AI defaults toward 450+. Resist. Cut restated points (he uses a single-line beat instead of repeating), setup paragraphs that delay the thesis, and adjective stacks. The most common bloat in this skill specifically is the **forced, repeated ownership point** — the back half that explains the equity angle three or four times. Collapse it to one beat. If cutting the ownership restatements makes the post end on the human line or the quote, that is usually the better post.

### Keep the emergent-answer discipline even under pressure
If Akshay's brief names ESOP up front ("write a post about why ESOPs are great"), do not open on ESOP. Find the human story or the news that makes the point, lead with that, and let ownership emerge. That is the job.

### Borrowed authority must be anchored
A hook that leans on a famous name works only when anchored to a named guest, company, or real event ("Sequoia and Matrix offered him 8x the cash"). A floating celebrity name-drop with no anchor is off-voice. Cut it.

### Emoji are sparing and functional
Satish uses the occasional 👉 👇 ❤️ ♣️ 😁 — functionally (to point at a line, mark a card series, sign a light moment), never as bullet stacks or decoration. Default to none; add one only where his corpus would.

### Hashtags and name-tags default to OFF
Akshay's standing preference is clean posts: **no name-mentions** (don't tag the guest or Hissa at the foot of the post) and **no hashtags**, unless he asks for them on a specific post. Default to none. If a post clearly benefits from one tag or Akshay requests them, add them and note it in the tail. Do not append a "Guest · Hissa · #hashtags" footer by reflex — that is the thing he most often strips.

### The gated-name rule
Any post that would reference **Verismo, Revvx, or YourNest** needs Satish's direct sign-off. Do not surface those as angles or write them into a draft without flagging the gate explicitly in the tail.

### When Akshay pastes a draft to fix
Treat his draft as the *thesis intent*, not the voice template. Read it for what it's trying to say, then rebuild in Satish's voice. Preserve any specific numbers, named people, quotes, and explicit constraints. Don't preserve sentence structure that isn't Satish's.

## Reference files
- **`references/voice-rules.md`** — hook patterns, close patterns, structural moves (the clean reversal, plain-English mechanics, the emergent-answer rule), vocabulary use/ban lists, the full AI-tells strip table, emoji and hashtag conventions. Read selectively for what the draft needs.
- **`references/post-types.md`** — the skeleton for each post type with length targets and annotated verbatim exemplars from his corpus. Read the matching type every time before drafting.
- **`references/dedup-and-research.md`** — the OPEN/CONTESTED/COVERED dedup system, the standing-thesis list, the beat definition, factual-discipline and sensitive-topic rules, and the research escalation ladder. Read in Step 3.

## The standard
A finished draft reads like Satish noticed something, thought about it, and said it once — grounded, specific, calm, with ownership emerging as the lesson rather than announced as the topic. Every number survives a check. Every quote is verbatim. Nothing repeats what he already published.
