---
name: satish-newsjacking
description: Run the Built to Share / Hissa newsjacking workflow for Satish Mugulavalli — find recent ESOP, secondary, employee-liquidity, equity-comp, and startup-talent news he can post a take on, dedup it against what he has already published, and build a prep sheet. Trigger on "/satishnewsjacking", "/satishnewsjaking", "newsjacking for Satish", "Satish newsjacking", "find news for Satish", "what can Satish post about", or "Hissa newsjacking". Three gated phases with hard STOPs. Phase 1 emits two ready-to-run research prompts (Grok and Perplexity) and stops. Phase 2 takes the pasted-back results, dedups every candidate against Satish's last ~50 posts using the OPEN/CONTESTED/COVERED system, ranks survivors, and stops for Akshay to pick. Phase 3 web-verifies the chosen story against primary sources and builds an HTML prep-sheet artifact with all source links, what is happening, and what Satish needs to know, angle left open for him to write. Use whenever Akshay starts a newsjacking cycle even if he does not say "skill".
---

# Satish Newsjacking

This skill runs the recurring newsjacking cycle for Satish Mugulavalli (founder of Hissa, host of Built to Share). Satish writes sharp, operator-voice LinkedIn posts that react to fresh news with a contrarian or non-obvious read. The job of this skill is to surface candidate news, make sure he has not already covered the angle, and hand him a clean prep sheet so his own take leads.

The single most important thing this skill does is **dedup before it recommends**. The fastest way to waste Satish's time is to hand him a story whose angle he posted last week. Phase 2 is the heart of the skill, not Phase 3.

## The three-phase workflow

Phases are sequential and gated. Never skip a phase. Never build the prep sheet before a story is finalized.

### Phase 1 — Emit the two research prompts

On trigger, read `references/research-prompts.md`. Output, with almost no preamble:

1. A one-line note that Grok is the stronger of the two because Satish catches most of this on X anyway, but both should be run so Perplexity can lock the filings and exact numbers.
2. The **Grok prompt** in its own code block, with today's date filled in.
3. The **Perplexity prompt** in its own code block, with today's date filled in.
4. A closing line telling Akshay to run both and paste the results back, and reminding him newsjacking runs Monday and Thursday with a minimum three-day gap.

Then **STOP**. Do not invent news yourself. Do not pre-guess what will come back. Wait for the pasted results.

### Phase 2 — Dedup and rank

Akshay has pasted back the Grok and/or Perplexity output. This is the editorial gate.

Read `references/beat-and-dedup.md` if not already loaded. Then, for **every** candidate item in the pasted results:

1. **Pull Satish's recent posts.** Use `project_knowledge_search` against the post archive (`satish-hissa-linkedin-posts.md` and `satish-hissa-linkedin-posts-51-100.md`). Search by the candidate's company name AND by its angle (e.g. "buyback former employees", "lock-in secondary block", "IPO secondaries liquidity"). The post document is the authoritative source for angle coverage — always reconcile there first, before the posting log or any search. Run a search per candidate; do not batch them into one vague query.

2. **Assign a status** using the system in the reference file:
   - **OPEN** — no logged coverage of this company or this angle. Clean to use.
   - **CONTESTED** — the company is new but the angle overlaps something he posted recently, or vice versa. Usable only with a genuinely different angle; flag the overlap explicitly with the date and post.
   - **COVERED** — he has posted this company or this exact angle recently, or it restates his standing thesis. Skip.

3. **Watch for the standing-thesis trap.** Several of Satish's core positions (secondaries beat IPOs for employee liquidity, partial sale signals confidence, large ESOP expense signals real ownership, legacy finance can't manufacture ownership) recur across his feed. A candidate that just restates one of these is COVERED even if the specific company is new. The reference file lists these.

Output a ranked verdict, best-first, in this shape per item:

```
**N. [Headline] → STATUS [✅ / ⚠️ / ❌]**
[1-2 lines: what it is, and the exact overlap if any — name the prior post and its date]
[1 line: recommendation — use / use only if reframed / skip]
```

Then a short bottom line: how many are genuinely usable, and which one or two you'd lead with. If the week is thin or the prompts returned angles he has already mined, say so plainly. Note any factual flags surfaced by the results (X-only claims with no primary source, unconfirmed figures).

Close with: "Which one do you want to run with?" Then **STOP**. Do not build the prep sheet yet. Do not draft a post — Satish writes his own takes.

### Phase 3 — Verify and build the prep sheet

Akshay has picked a story. Now produce the artifact.

1. **Verify against primary sources first.** Do not trust the X reposts the research prompts cited. Run `web_search`, then `web_fetch` the strongest source (prefer the filing, the company statement, then credible publications like Business Standard, Entrackr, ANI, Moneycontrol, ET). Confirm every load-bearing number. Flag anything you could not verify rather than passing it through.

2. **Read `references/prep-sheet-template.html` in full.** Copy its CSS verbatim and follow its structure element-for-element. The page has: a masthead (eyebrow, headline, standfirst, meta row), a "What the news shows" section of numbered thread cards with stat chips, an optional dark "scale/backdrop" strip, a "What to weigh before you write" section (lead line, an angle callout, an amber factual-flags callout, the dedup note from Phase 2), and a grouped "Sources" list, then a footer.

3. **Handle sensitive threads with the flagged treatment.** Anything involving a regulator, an investigation, a named individual's conduct, or unverified allegations gets the amber `flagged` card and the safe framing written in (e.g. "summoned, complied, nothing alleged"). Never imply wrongdoing about a named, listing-bound company or person. See the factual-discipline rules in `references/beat-and-dedup.md`.

4. **Leave the angle open.** The "What to weigh" section lays out the non-obvious territory and the questions, but never writes the take. Satish's view leads. Surfacing the herd read and the operator counter-read is fine; concluding for him is not.

Save to `/mnt/user-data/outputs/<slug>-newsjacking-prep.html` (slug is 2-4 lowercased words from the story, e.g. `zepto-newsjacking-prep.html`). Call `present_files`. Keep the closing message short: one or two lines on what's inside and the offer to verify final numbers against the source document before anything hits a thumbnail.

## What this skill never does

- **Never drafts the post.** Satish writes his own takes. This skill hands him the ground, not the words. If Akshay explicitly asks for a draft, that is a separate request — but the default deliverable is the prep sheet.
- **Never recommends a COVERED story** just because it has high traction. Dedup overrides traction.
- **Never passes an unverified number into the prep sheet body or a thumbnail.** Reported-but-unconfirmed figures are flagged as such.
- **Never implies guilt or wrongdoing** on a named company or person from an investigation, summons, or allegation.

## Reference files

- **`references/research-prompts.md`** — The two ready-to-run prompts (Grok and Perplexity). Read in Phase 1. Contains both prompts in full plus the date-handling note and the split-rationale line.
- **`references/beat-and-dedup.md`** — Satish's beat definition, the OPEN/CONTESTED/COVERED status system, the standing-thesis list, the factual-discipline and sensitive-topic rules, and the content/voice constraints (podcast link in comments, no quote cards, numbers-on-thumbnails verification). Read in Phase 2.
- **`references/prep-sheet-template.html`** — The canonical prep-sheet HTML (the Built to Share navy editorial one-pager). Read in Phase 3. Copy the CSS verbatim and follow the structure element-for-element.

## The standard, restated

Satish should be able to open the prep sheet on his phone, read what happened and what the non-obvious angle is, form his own view, and write the post. Every number in it survives a check against a primary source. Nothing in it repeats what he already published. And nothing in it puts words in his mouth.
