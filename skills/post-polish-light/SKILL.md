---
name: post-polish-light
description: Lightweight punch-up pass for a LinkedIn post or short-form piece that is foundationally sound (angle holds, structure is right, research is there) but isn't landing: soft hook, flat storytelling, AI tells, repetition, weak voice, lazy numbers, dated hooks, or too many Western references for an Indian audience. Trigger on "/post-polish-light" followed by a pasted draft. Also trigger on "this post needs more punch", "it's not landing", "tighten this up", "make it sharper", "the hook is soft", "this reads flat", or any request to sharpen a draft that is structurally fine. Two-step workflow: a numbered diagnostic flag list across seven punch areas (hook, storytelling, AI tells, repetition, voice, numbers, Indianness) plus a claim-risk check that flags load-bearing or easily-wrong factual claims for verification, then one tight rewrite on go-ahead (two variants only on request). Does NOT verify facts, research, or restructure; claim-risk flags route to fact-check, foundation and structural work to post-polish.
---

# post-polish-light

This skill is the lightweight sibling of post-polish. It assumes the post is foundationally correct — the angle holds, the structure matches the argument, the research is in place — and the only thing missing is punch.

Punch fails in seven common ways. A polished post can also ship a claim that is false or dated, which is worse than an unpolished one: a sharpened, confident sentence carries an error further. So alongside the seven punch areas, this skill runs one claim-risk check. It audits all seven punch areas plus claim risk in one pass, presents flags as a single numbered list, waits for the go-ahead, then delivers one tight rewrite (or two variants if the user asks for options).

No 8-pass sequence. No foundation gate. No per-pass back-and-forth. Two steps, done.

## When to use this skill

- The user has a draft that is structurally fine but doesn't land
- The user types "/post-polish-light" with a pasted draft
- The user says the post needs "more punch," "more bite," "more sharpness," or reads "flat"
- The user knows what the post is about and has the facts — they just want it to hit

## When NOT to use this skill

- The angle is broken, the central claim is wrong, or the research is thin — route to post-polish (which has a foundation gate) or back to drafting
- The user wants a structural rewrite or section reordering — route to post-polish Pass 3
- The user is at blank-page stage — route to the relevant drafting skill
- The user wants client-specific voice fit from scratch — route to the drafting skill for that client

## The two-step workflow

### Step 1 — Diagnostic (numbered flag list)

Read the post once. Then audit it across the seven punch areas below, plus the claim-risk check. Output a single numbered list of every flag found, in reading order through the post (not grouped by area). Each flag is one or two lines: what's flagged, why it's weak, and the area it falls under in brackets.

Example flag format:

> *3. "I've been thinking a lot about..." — throat-clearing first three words, no scroll-stop. [Hook]*
> *7. "What I find more interesting is..." — connective tissue that announces a transition instead of making one. [AI tells]*
> *12. "60% of revenue comes from international markets" — true but not load-bearing; the post doesn't use this number for anything. [Numbers]*
> *14. "the same water that runs through every tap" — load-bearing factual claim about what the product is; verify before publishing. [Claim risk]*

After the numbered list, append two lines:

> *Total flags: [N]. Hook severity: [low / medium / high]. Claim-risk flags: [N — verify before publishing, or none]. Recommend rewriting if hook severity is medium or higher.*
>
> *Want me to go ahead with the rewrite? (Say "options" if you want two distinct variants instead of one.)*

Then stop. Wait for the user.

### Step 2 — Rewrite (one tight variant by default)

After the user says go ahead (or specifies which flags to prioritise), output **one tight rewrite** that addresses the flags. This is the default. The user has usually already settled the angle by this point in the workflow; what they want is the sharpened post, not a menu.

**The rewrite must arrive tight, not loose-pending-trim.** Apply the compression check (area 4) to the rewrite itself before showing it, not just to the original. The most common failure of this skill is delivering a rewrite that fixes the flagged lines but still carries flab the user then has to point at one round at a time. Do the subtraction now.

Two concrete rules:
- **Cut toward a budget.** Unless the user names a length, aim to remove roughly 15-25% of the draft's word count, and never let a punch-up rewrite come back *longer* than the draft it sharpens. If the draft is already lean and cutting 15% would remove meaning, say so and cut less, but state the count.
- **Run the subtraction test on every sentence.** For each sentence in the rewrite, read it without its qualifiers, set-up clauses, and example lists. If the meaning survives the cut, the cut stays. Kill "simply / actually / just / really / very," restate-the-subject clauses, three-item lists that work as two, and proper-noun lists longer than the point needs.

State the rewrite's word count in the structural note so the user can see it landed tighter than the draft.

Below the rewrite, add a short note (two or three lines max) naming what was cut or changed at the structural level — not a line-by-line change-log, just the moves that matter (e.g. "removed the two not-X-but-Y scaffolds; collapsed the triple-stated category point; cut the channel-name list").

**Only produce two variants if the user explicitly asks** — via "options", "give me two", "two variants", "show me a couple of angles", or similar. When they do, the two must take a *genuinely different angle on the hook or storytelling spine*, not two cosmetic line-edits of the same approach.

Examples of variant pairs that earn their distinction (use only when options are requested):
- Variant A opens with a number; Variant B opens with a scene
- Variant A is biographical narrative; Variant B is a contrarian claim with proof
- Variant A leads with the tension; Variant B leads with the resolution and reveals the tension underneath
- Variant A is first-person stake-led; Variant B is third-person observation

If the user asks for options but two genuinely distinct angles aren't available (the post's content only supports one approach), say so and deliver one rewrite plus a short note on why a second angle would be forced.

When producing two variants, add a one-line tag under each describing its approach: *"Variant A: number-led hook, biographical spine. Variant B: contrarian claim, proof-led."*

---

## The seven punch areas

These are what the diagnostic pass checks for. Do not output them as section headers in the diagnostic — they are the lens, not the format. Use them as the bracketed tag at the end of each flag.

### 1. Hook

The first two sentences are the entire reason anyone reads the next two hundred.

Flags:
- Vague openers ("In today's market...", "Innovation is at an all-time high...")
- Throat-clearing ("I've been thinking about...", "Now,", "So,", "Honestly,")
- Abstract claims instead of concrete scene, number, or named character
- Second sentence that continues the same register without adding force
- Three or more numbers crowding the opener
- A year or date stamped on a fact that is still true now, which makes a current reality read as old news ("...was valued at $1.4 billion in 2024", read in 2026). If the fact still holds, cut the date and use the present tense ("...is worth $1.4 billion"). Timing that genuinely matters can move to where the post uses it; it should not blunt the opener.
- A hook built on an event the reader will register as stale (an old acquisition, a funding round from years back) when a present-tense standing fact would land harder.

A dated or stale-sounding hook is at least **medium** hook severity, because it costs the scroll-stop even when every word is true.

### 2. Storytelling

A post with facts but no narrative pull reads as a brief.

Flags:
- No named character anchoring the story (a founder, a customer, a specific moment)
- Events presented as a list of facts instead of a sequence with stakes
- No tension named explicitly — the reader has to construct the stakes themselves
- The "what changed" beat is missing — the post lists what is, never what shifted
- Time is flat — no before/after structure when the underlying story has one

### 3. AI tells & connective tissue

The places where AI writing announces itself.

Flags (from post-polish Pass 4):
- Connective tissue: "What I find more interesting is...", "I keep coming back to...", "This is where...", "Let's turn to..."
- Self-import: "What most people miss is...", "More than people are noticing", "A rare/unusual/distinctive thing about..."
- Restating what the reader just inferred: "This shows that...", "The point is..."
- Marketing abstractions: "authentic advocacy," "operational excellence," "strategic alignment," "holistic approach"
- Hedging before the point: "Each of these is impressive," "Of course, the obvious point is..."
- Telegraphed contrast: "But here's the thing...", "Here's where it gets interesting...", "The plot twist is..."
- Throat-clearing first words: "Now," "So," "Well," "Honestly," "Frankly"

### 4. Compression (repetition, redundancy & flab)

The post says the same thing twice, or uses more words than the meaning needs. This is the area that decides whether the post reads tight. Flag aggressively here — under-flagging compression is the single most common reason a "polished" post still reads loose.

Repetition flags:
- A sentence whose claim was already made one paragraph earlier
- A summary line at the end of a paragraph that restates the paragraph
- Two adjectives where one would do ("genuine, authentic engagement")
- The same idea stated two or three ways inside one paragraph (state it once, in its sharpest form)

Flab flags (the cuts a writer would otherwise have to ask for by hand):
- Three short fragments or a three-item list doing the work of one or two ("Two SKUs. One sachet. One ritual." → often two beats, sometimes one)
- An explanatory clause doing work the next sentence already does on its own
- A hedge or set-up sentence before a real claim that could just sit alone
- Connective tissue between two sentences that could simply sit next to each other
- A list of proper nouns or examples longer than the point needs (three channel names where "online" carries it)
- Any qualifier the sentence survives without ("simply," "actually," "really," "just," "very," "quite")
- A clause that restates the subject the reader is already holding ("the buyer the aisle had been ignoring" right after naming that buyer)

The test for each: read the sentence without the flagged words. If the meaning survives, the words go.

### 5. Voice / first-person presence

Thought leadership requires the writer in the post.

Flags:
- Pure third-person analysis with no first-person beat — reads as journalism, not POV
- No "I would back this" or "the question I keep asking" or "I have not seen" — no stake
- Closing line is observational, not personal — anyone could have written it
- Inverse failure: every other sentence starting with "I think" or "In my view" — over-presence dilutes authority
- Hedges ("perhaps," "arguably," "it may be the case") softening the post to vanishing

### 6. Number discipline

Numbers should earn their position, not just decorate.

Flags:
- More than two numbers in the hook
- A number that doesn't change the reader's understanding if removed
- Three or more numbers crowded in one sentence
- "Exactly 47.3%" when "roughly half" would read more naturally
- A precise-sounding number used for flavour rather than evidence

### 7. Indianness (for Indian-audience posts)

If the post is for an Indian audience, Western proper nouns should not outnumber Indian ones unless the post is specifically about a Western company or figure.

Flags:
- More than two or three Western proper nouns where Indian equivalents exist (Tesla → Ola/Ather, Apple → boAt/Nothing, Buffett → Premji/Damani, Messi → Dhoni, Disney → YRF, Stanford → IIT Bombay)
- Western cultural touchstones used as anchors when the audience would land harder on Indian ones
- Statistics from Western markets used to make a claim about Indian behaviour
- A founder/company story Indian readers would already know, told as if novel

If the post is explicitly about a Western company or figure, this area is not a flag — the West is the subject, not the lens.

---

## The claim-risk check (flag, never verify)

This sits alongside the seven punch areas. It exists because a punch-up pass makes claims *more* confident, and a sharpened false claim travels further than a clumsy one. The check does **not** verify anything. It reads the post for assertions that are load-bearing or easy to get wrong, and raises them as `[Claim risk]` flags with a "verify before publishing" note. Verification belongs to the `fact-check` / `piyush-fact-check` skills; this check only makes sure such claims do not slip through a polish pass unexamined.

What to flag:
- **What the product is or is made of / where it comes from.** Claims about composition, source, or origin stated as fact ("the same water that runs through every tap", "sourced from the Himalayas", "the first plant-based..."). These are the highest-risk class — the tap-water error lived here. A product claim that also contradicts the brand's own positioning is a double flag, because it is both likely wrong and self-defeating for the argument.
- **Superlatives and firsts.** "first", "only", "largest", "fastest-growing", "the most X in Y". Each is a claim someone can falsify.
- **Founder / origin / attribution claims.** Who started it, who said what, what year it began. Names and dates stated with confidence.
- **Any claim the post's spine leans on.** If the hook, the central argument, or the close depends on a fact, that fact is load-bearing. Flag it even if it looks right — load-bearing position is the trigger, not suspicion.
- **A confident number with no visible provenance** that the rewrite is about to make more prominent.

How to flag (do not verify, do not rewrite the fact):
> *9. "the first canned water brand in the US" — load-bearing superlative in the hook; verify before publishing. [Claim risk]*

Then surface the count in the summary line ("Claim-risk flags: 2 — verify before publishing"). If the user has a fact-check skill in their toolkit, name it as the next step. Never silently fix a factual claim inside the rewrite on your own knowledge; if you happen to know a claim is wrong, flag it and say so plainly, but the verification pass is a separate skill.

A clean post here gets "Claim-risk flags: none." Do not manufacture risk on claims that are plainly safe (common knowledge, the user's own portfolio facts, numbers the user supplied as given).

---

## Operating principles

**1. Tight is the job.** "Punch-up" means the rewrite comes back shorter and sharper than the draft, not the same length with better lines. If the user has to ask for a tighter version after the rewrite, the skill underdelivered. Every rewrite is held to the compression check (area 4) and the word-budget rule in Step 2 before it is shown. When in doubt, cut.

**2. Default to fewer flags, sharper flags.** Twenty flags drown the signal. Eight to twelve well-chosen flags is the sweet spot for a 300–500 word post. Claim-risk flags are exempt from this ceiling — raise every load-bearing factual claim even if it pushes the count up, because a missed false claim is costlier than a noisy list.

**3. Read the post twice before writing flags.** First read for what it's trying to do. Second read for where it isn't doing it. Flags written from one read tend to be cosmetic.

**4. The diagnostic does not rewrite.** Step 1 is flagging only. Do not embed rewrites inside flag descriptions. The user reads the flags, decides what to prioritise, then asks for the rewrite.

**5. One tight variant by default; two only on request.** The default output is a single sharpened rewrite. Produce two variants only when the user explicitly asks for options, and when you do, two variants that share the same hook approach and differ only in word choice are one variant pretending to be two. If you can't find two distinct angles, deliver one and say why.

**6. Voice-agnostic.** Do not impose voice preferences. If the user has standing constraints (em-dash policy, banned phrases, length budget), they will name them. If they don't, default to universal craft.

**7. No process commentary in the rewrite.** The user wants the rewritten post, not paragraphs of explanation. A short structural note (what was cut or changed, plus the word count) is the whole change-log; when producing two variants, one line per variant tagging its approach.

---

## What this skill does not do

- Does not do foundation checks (angle, structure, central claim) — route to post-polish
- Does not verify claims or do research — the claim-risk check flags load-bearing or easily-wrong factual assertions and routes them to fact-check / piyush-fact-check; it never verifies them itself
- Does not draft from scratch — route to the relevant drafting skill
- Does not run an 8-pass sequence — for that depth, route to post-polish
- Does not auto-publish or schedule — output is text for the user to use

For the full polish workflow with foundation gate and 8-pass depth, use post-polish.
