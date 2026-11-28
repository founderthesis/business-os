---
name: post-polish
description: Polish a LinkedIn post or similar short-form written piece from rough-draft state to ready-to-ship through a fixed 8-pass sequence. Trigger whenever the user has an existing draft and asks to polish, examine flow, cut redundancy, find AI tells, look for phrases that aren't doing their job, make it tighter, finalise, ship, publish, post, tighten, edit, critique, or do an editorial pass. Also trigger when the user pastes a draft and asks for thoughts, a review, or any phrase suggesting the post is heading to publication. Specifically fires on "ready to ship," "make this ready," "ship this," "polish this," "examine this," "is this ready," "cut this down," "what can we cut," "look for phrases not doing their job," "is the flow working." Voice-agnostic by design — client-specific voice rules (banned phrases, hook patterns, length budgets) are NOT part of this skill. For voice fit, route to the relevant client-specific drafting skill (e.g., piyush-linkedin-post) before or after polish.
---

# post-polish

This skill polishes an existing post draft into a shippable final version. It does not draft from scratch. It does not enforce client-specific voice rules. It enforces universal craft.

The whole skill is built around one observation from a real polish session: **posts get strong by subtraction, not addition.** Every pass below is biased toward cutting, sharpening, or making sentences earn their place. None of the passes add length.

## When to use this skill

- The user has a draft (their own or AI-generated) and wants it cleaned up for publication
- The user has pasted a post and asked for editorial review, critique, or polish
- The user is in late-stage editing — "is this ready," "what can we cut," "look at flow"
- The user has just received structural feedback from someone (client, editor) and needs to apply it

## When NOT to use this skill

- The user is at blank-page stage with just an idea — route to drafting
- The post has no central claim, no hook, and reads as freeform notes — route to drafting
- The user wants client-specific voice fit (Piyush's hook patterns, banned phrases, etc.) — route to that client's drafting skill
- The user wants the post written in a specific voice from scratch — route to drafting

## Opening move (before Pass 1)

Before running any pass, do two things in a single short message:

1. **Confirm the draft is visible.** If the user pasted the draft, acknowledge it. If they referenced "the post above" or "this post," confirm which draft you're working with.

2. **Ask for client-specific constraints in one line.** Voice-agnostic doesn't mean constraint-blind. Ask:

   > *"Before I start: any client-specific constraints I should respect? Word count target, em-dash policy, hashtag policy, banned phrases, or formatting preferences (team tags, etc.)? If none, I'll polish to universal craft."*

If the user has standing constraints (e.g., "Piyush: no em-dashes, no hashtags, no team tag, ~400-word target"), hold those through all 8 passes. If the user says "none," proceed with universal polish.

Then move to Pass 1.

---

## The 8-Pass Sequence

Each pass has a fixed purpose, decision rule, and output format. Pass 1 is always interactive (because it has a stop/rewrite/continue branch). Passes 2–8 default to interactive but can be batched if the user asks for speed.

After each pass: present findings, ask the user which flags to fix, apply fixes, then move to the next pass.

---

### Pass 1 — Foundation Check (always interactive)

**Purpose:** Decide whether the draft is polishable at all, or whether the angle/structure is broken below the polish line.

**What to check:**

- **Central claim:** Can you state the post's central claim or observation in one sentence? If you struggle to, the foundation is shaky.
- **Angle defensibility:** Is the post making a claim that holds up under scrutiny? (e.g., "no Indian celebrity-led D2C has won" — broken, Wonderchef exists)
- **Structure-argument match:** Does the post's structure reflect its argument? Numbered lists imply parallel weight. Hierarchical arguments need hierarchical structure.
- **Central tension:** Is there an explicit tension the post is resolving? (e.g., "convenience is the easy half. Without compromise is the half where most brands fail.") A post without a named tension reads as a list of facts.
- **Research depth:** Are the facts thin? Does the post lean on one anecdote, one transcript, one data point? If yes, the research gate may need to be re-triggered.

**Decision rule — Option C branch:**

If any of the above is broken, do not proceed to polish silently. Stop and present:

> *"Before I polish, here's what I see at the foundation level: [brief diagnosis of what's broken — angle, structure, tension, or research depth]. Three paths from here:*
>
> *(1) Stop polish — go back to drafting/research to fix the foundation first.*
> *(2) Do a structural rewrite together now, then polish the rewritten version.*
> *(3) Continue with polish anyway and treat the foundation issue as a flag the user can address later."*

Default recommendation: (2) for fixable structural issues, (1) for missing research, (3) for borderline cases where the user just wants forward motion.

If the foundation is sound, say so in one line and move to Pass 2.

**Output format:** Freeform paragraph. No tables.

---

### Pass 2 — Hook Audit

**Purpose:** The first two sentences are the entire reason anyone reads the next two hundred. Audit whether they earn the scroll-stop.

**What to check:**

- **First sentence:** Does it stop the scroll on its own? A number, a scene, a contrarian claim, an aphorism, a named character — these stop scrolls. Vague openers ("In today's market..."), throat-clearing ("I've been thinking about..."), and abstract claims ("Innovation is at an all-time high...") do not.
- **Second sentence:** Does it earn the reader's investment by either (a) explaining the first sentence, (b) humanising it with a scene, or (c) raising the stakes? A second sentence that just continues the same register without adding force is wasted.
- **Two-stage hook:** Many strong posts use a two-beat hook — number + scene, claim + proof, scene + interpretation. Check whether both beats are pulling weight.
- **Hook integrity under image pairing:** If the post is publishing with an image, does the hook's text-image combination reinforce or compete?
- **Numbers in the hook:** One number is a hook. Three numbers is a press release. If the opener has multiple numbers, flag for compression.

**Output format:** Freeform analysis (3–6 sentences) plus 2–4 alternative opener options if the hook is flagged. Each alternative on its own line, labelled by what it's doing differently.

---

### Pass 3 — Hierarchy Audit

**Purpose:** Make sure the post's structure matches its argument. Most polish problems are actually hierarchy problems.

**What to check:**

- **What is the most important point?** Identify the single load-bearing claim of the post. Is it in the structurally important position (early in the body, given the most space, named explicitly)?
- **Are amplifiers correctly demoted?** If the post lists multiple factors, is the most important one given more weight, or are they all treated as parallel? Parallel structure (numbered lists, equal-length sections) implies parallel weight. When the underlying argument is hierarchical, parallel structure misleads the reader.
- **Is the central tension named explicitly?** Strong posts have a single sentence (or pair of sentences) that names the tension the rest of the post resolves. If the post has no such moment, the reader has to do the structural work themselves.
- **Are paragraph breaks doing structural work?** Each paragraph should advance the argument by one step. Paragraphs that restate, hedge, or transition without adding are flags.

**Output format:** Freeform analysis. If the hierarchy is broken, offer a restructured outline (just the section order and one-line description of each section) before any prose rewrite. Confirm the new structure with the user before drafting prose.

---

### Pass 4 — Phrase-by-Phrase Pass (the heaviest pass)

**Purpose:** Read every sentence and label what it's doing. Flag every phrase that isn't load-bearing.

**Method:** Go through the post paragraph by paragraph. For each phrase or sentence, ask:

1. *What is this phrase doing?*
2. *Is it doing it well?*
3. *Could the reader infer this without the phrase being there?*

Flag any phrase that hits one of the following patterns. Each is an AI tell or a writerly tic that weakens prose:

**Connective tissue — phrases that announce transitions instead of making them:**
- "What I find more interesting is..."
- "I keep coming back to..."
- "This is where..."
- "It is worth pausing on"
- "Let's turn to..."
- "Speaking of..."

**Self-import — phrases that insert the writer's own perceptiveness into the sentence:**
- "More than people are noticing"
- "What most people miss is..."
- "A rare/unusual/distinctive thing about..."
- "I've been thinking about..."

**Restating what the reader can already infer:**
- "That is the consumer insight the brand is built on" (after the consumer insight has just been demonstrated)
- "This shows that..." (after the showing has just happened)
- "The point is..." (after the point has just been made)

**Marketing-speak abstractions — abstract noun phrases that hide unspecific thought:**
- "Authentic advocacy"
- "Genuine engagement"
- "Operational excellence"
- "Strategic alignment"
- "Holistic approach"
- Any abstract noun phrase that could be replaced with a concrete behavioural contrast

**Hedging before the point:**
- "Each of these is impressive" (before the real claim)
- "While X is true, Y is more important" (the post should just make the Y claim)
- "Of course, the obvious point is..." (just make the point)

**Three fragments doing one job:**
- "Two SKUs. One sachet. One ritual." — three fragments all saying "compression." Pick one.
- Any time three short fragments are stacked and they're all expressing the same idea, two are redundant.

**Telegraphed contrast:**
- "But here's the thing..."
- "Here's where it gets interesting..."
- "The plot twist is..."
- A good contrast doesn't need to be announced. It just happens.

**Throat-clearing first words:**
- Paragraphs that start with "Now," "So," "Well," "Honestly," "Frankly" — usually deletable

**Output format:** A table per paragraph (or per section if paragraphs are short). Columns:

| Phrase | What it's doing | Verdict | Replacement if flagged |
|---|---|---|---|

Verdicts: ✓ (load-bearing), soft flag (could be cut without loss), hard flag (actively weakens the post). After the table, summarise: "X soft flags, Y hard flags. Recommend fixing all hard flags. Soft flags are your call."

Then ask: *"Which flags do you want to fix? You can say 'all hard flags,' 'all of them,' specific numbers, or describe the cuts you want."*

---

### Pass 5 — Voice Register Check

**Purpose:** Distinguish thought leadership from reporting. Make sure the writer's voice is present where the post needs it.

**What to check:**

- **First-person presence:** Is the writer in the post at all? Pure third-person analysis reads as journalism. Thought leadership requires at least one or two moments where the writer's perspective is visible. Look for sentences like "I have not seen..." or "The question I keep asking is..." or "What I would back is..."
- **Personal stake in the close:** The strongest closes carry the writer's stake. "The brand that does is the one I would back" is stronger than "This is a model worth watching." Check the closing line — is there personal weight, or is it an observation anyone could have made?
- **Over-presence:** The opposite failure mode is too much first-person. Every other sentence starting with "I think" or "In my view" weakens authority. One or two well-placed first-person beats is the right dosage for a 400-word post.
- **Confidence calibration:** Hedge words ("perhaps," "arguably," "it may be the case") are sometimes appropriate but often soften the post to vanishing. Check whether hedges are doing work or just lowering the writer's risk.

**Output format:** Freeform analysis (3–5 sentences). If the post lacks first-person beats where it needs them, suggest 1–2 specific places to add a personal stake line and offer phrasing options.

---

### Pass 6 — Number Discipline

**Purpose:** Every number in the post should earn its position. Specificity is not the same as load-bearing.

**What to check:**

- **Numbers in the hook:** Aim for one. Two is the maximum. Three or more in the opening crowds the line and dilutes the scroll-stop.
- **Earned specificity:** For each number, ask: if I removed this, would the reader's understanding change? If not, cut.
- **Crowded sentences:** Any sentence with three or more numbers in it is likely doing too much. Split or compress.
- **Round vs precise:** "Half" reads more naturally than "fifty percent" in most prose. "Roughly a hundred" is fine; "exactly 97" needs a reason.
- **Anchor numbers:** Some numbers earn their position by being so striking they carry weight ($100M in 11 months, 1,500 ads). Some are filler (sixty percent international revenue — true but not load-bearing).

**Output format:** A list of every number in the post with verdict (keep / move / cut). Group cuts and explain the reasoning briefly.

---

### Pass 7 — Subtraction Pass

**Purpose:** Final word-count compression. After all the above passes, do one more sweep with one question: *if I removed this sentence, would the reader miss anything?*

**Method:**

Go through the cleaned post sentence by sentence. For each sentence:

1. *Is this sentence's claim already made elsewhere?*
2. *Is this sentence setting up a sentence that could stand alone without it?*
3. *Is this sentence a hedge before a real claim?*
4. *Is this sentence connective tissue between two sentences that could just sit next to each other?*

If yes to any: candidate for cut.

**Compounding effect:** Cuts compound. The first sweep finds the easy cuts. The second sweep finds the cuts you missed because the first sweep changed the rhythm. Run this pass *after* the user has accepted earlier cuts, not in parallel.

**Output format:** A list of candidate cuts with word savings. Group by safety:
- **Safe cuts** (no essence lost): list them
- **Riskier cuts** (lose something but might be worth it): list with what's lost
- **Don't cut** (paying their rent): list with one-line justification

Then recommend: *"My recommendation is the safe cuts plus [specific riskier cuts]. This takes the post from X words to Y. Want me to lock these in?"*

---

### Pass 8 — Ship Checklist

**Purpose:** Final mechanical verification before the post is ready.

**What to check:**

- **Word count:** Within target (if specified at opening)
- **Em-dashes:** Count them. Most clients prefer zero. Use the opening intake to know the policy.
- **Hashtags:** Count and policy compliance.
- **Banned phrases:** Run the post against any banned-phrase list from opening intake.
- **Team tags / @mentions:** Policy compliance.
- **Foreign proper nouns:** For Indian-audience posts, count Western proper nouns. Two or three is fine if load-bearing. More than that may need trimming.
- **Image-text pairing:** If publishing with an image, does the hook line work with the image preview?
- **Closing line:** Is it declarative? Does it leave the reader with something specific?
- **No stranded references:** Any "as I mentioned earlier" or "see above" — flag for removal (LinkedIn posts are read linearly, not as documents).

**Output format:** A pass/fail checklist with one line per item. Conclude with: *"Ship-ready"* or *"Fix [X] before shipping."*

---

## Closing move — the final shippable version

After Pass 8, output the final clean version of the post in one continuous block, ready to copy-paste. Below it, list:

- **Word count:** [N]
- **Passes completed:** 8/8
- **Open flags the user chose not to fix:** [list, or "none"]
- **Image pairing notes:** [if applicable]
- **Ready to ship.**

Do not over-narrate. The user wants the cleaned post, not another paragraph of process commentary.

---

## Operating principles (apply across all passes)

These are not passes. They are the disposition the skill operates from.

**1. Subtraction beats addition.** Default to cuts. Suggest additions only when something is structurally missing (a missing tension, a missing first-person beat).

**2. The user's pushback usually points to a structural problem, not a line edit.** When the user flags a single line, ask whether the surrounding structure is what they're actually reacting to.

**3. Connective tissue is where AI writing shows.** When in doubt about a transition phrase, cut it. Strong prose changes scene without announcing the change.

**4. Concrete beats abstract every single time.** An abstract noun phrase ("ongoing authentic advocacy") can almost always be replaced with a concrete behavioural contrast ("owners speak about a company, ambassadors speak about a contract").

**5. Working sentences and load-bearing sentences are different things.** A grammatically correct sentence that conveys true information can still be cut if the reader doesn't need it. Polish is not error-finding. It is weight-checking.

**6. Five or more passes is the bar.** Two passes are not enough. The skill's eight-pass sequence is the floor, not the ceiling. If the user wants to go again on any pass after fixes have been applied, do it.

**7. The last 5% of cuts often do more work than the first 50%.** The instinct to stop is strongest near the end. Resist it. Run Pass 7 even when the post feels finished.

**8. Stay voice-agnostic.** Do not impose voice preferences. If the user wants a particular tone, hook style, or formatting convention, they will say so in the opening intake. If they don't, default to universal craft.

---

## What this skill does not do

- Does not draft posts from scratch
- Does not enforce client-specific voice rules (banned phrases, hook patterns, length budgets) unless the user names them in opening intake
- Does not do research or fact-checking — if facts are thin, flag and route back to research
- Does not generate variations (multiple versions of the same post) unless the user explicitly asks
- Does not auto-publish, schedule, or post anywhere — output is text for the user to use

For drafting from scratch with voice fit, route to the relevant drafting skill (e.g., piyush-linkedin-post).
For research, route to deep research tools.
For variations, the user can invoke this skill multiple times.
