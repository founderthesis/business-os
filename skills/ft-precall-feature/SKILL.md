---
name: ft-precall-feature
description: "Write a free founderthesis.com written feature from a Founder Thesis precall transcript, for a founder who did not get a video episode (decision 636). Trigger on /ft-precall-feature or ft-precall-feature followed by a guest name, Engagement link or Gemini notes doc, or on \"write the feature for X\", \"founderthesis.com feature from the precall\", \"turn this precall into an article\", \"written feature for X\", \"feature call write-up\". Input is the Gemini notes and transcript of a 30 to 50 minute call between Akshay Datt and the founder (a precall or a dedicated feature call). Never written from questions, decks, press notes or anything the founder's team sends. Output is one Markdown feature (SEO title, standfirst, 600 to 900 words in sections, an About box) plus a SOURCES list that backs every claim with a timestamped transcript quote or a URL, and a GAPS list. Nothing is published: Ranjita publishes after review."
---

# ft-precall-feature

Founder Thesis has a bar for video episodes. A founder who talked to Akshay but did not make that bar (or turned down a sponsored episode) can still get a written feature on founderthesis.com, free (decision 636, 20 Nov 2026). The feature is written **only** from a 30-minute call between Akshay and the founder: a precall, or a dedicated feature call booked for this.

This skill turns that call into a draft feature. It does not publish, post, mail or write to Notion. Ranjita reviews and publishes it.

The reader is a founder, operator or investor in India who found the page through Google or LinkedIn. They want the story and the specifics: what the company does, how it got here, what it chose, how the money works. The feature is editorial, not a press release.

## Hard rules (check every one before you hand over)

1. **One source of story: the call.** Every fact about the founder or company comes from the call transcript (or Gemini's notes of that same call), or from a public page you opened and can link. Never from written answers, decks, press notes, mails or forms the founder or their PR sent. If they sent material, ignore it. If something only exists in that material, it goes in GAPS, not the feature.
2. **Never invent.** No number, date, customer, investor, quote, motive or scene that is not in a source. No rounding that changes meaning. If the transcript is garbled, quote what is there and flag it in GAPS; do not guess what was meant.
3. **Every claim has a source line.** Each number and each factual claim in the feature maps to an entry in SOURCES: a verbatim transcript quote with its timestamp (`[00:11:02]`), or a URL you opened. Gemini's summary tabs ("Quick notes", "Full notes") are an index, not a source: find the line in the Transcript tab and quote that. If only the summary has it, mark the source "Gemini summary only" and list it in GAPS.
4. **Quotes.** Paraphrase by default. A direct quote longer than a short phrase (about six words) must be clearly the founder's words: in quotation marks, attributed ("Jansen says"), verbatim from the transcript, with filler words ("uh", "like", repeats) removed and nothing else changed. At most three such quotes in the piece. Never quote Akshay as if he were a source of facts about the company.
5. **Off the record stays out.** Anything the founder marked as off the record, confidential, "don't put this out", "between us", or not yet public (an unannounced round, a client they asked not to name, a pending deal) is left out entirely and listed in GAPS as "withheld: off the record" with its timestamp, so the reviewer can see it was seen and dropped.
6. **Money numbers.** Revenue, ARR, profit, margins, valuation and funding go in only if the founder said them on the call in a way that reads as shareable, and they are not sensitive. Leave them out (and note it in GAPS) if the founder hedged ("roughly, don't quote me"), if the figure is a projection presented as fact, or if it is about a client's business. Never add a number from a database, Tracxn, or an old article unless you opened the page and cite it, and the founder's own figure does not contradict it.
7. **Not about us.** The call often covers Founder Thesis itself: Akshay's reach, sponsored pricing, a barter or partnership, why they were not booked. None of that goes in the feature. Never mention that the founder was declined, offered a paid slot, or that this is "instead of" an episode.
8. **Writing rules (CLAUDE.md).** No em dashes. Never use "delve", "leverage", "unlock", "robust", "seamless". No "it's not X, it's Y" constructions. Sentence case headers. Short, varied paragraphs; contractions; specifics over generalities. No sign-off, no call to action, no hype ("revolutionary", "game-changing", "disrupting"). Spell names exactly as the founder or the company's own site spells them; the transcript's spelling of a name is not proof.

## Inputs

- **Required:** the call. Usually a Gemini "Notes by Gemini" Google Doc (tabs: Quick notes, Full notes, Transcript). Find it from the Engagement row, the "Notes: ..." mail from gemini-notes@google.com, or the attachment on the call's calendar event. Read it with Google Docs `read_doc` and use the **Transcript** tab in full, start to end.
- **Optional:** the Engagement row (for the founder's name, company and role as we have them recorded) and the People row. Use these only to identify who is who, never as a source of facts in the piece.
- **Optional, checkable public sources:** the company's own website, the founder's LinkedIn profile, registry filings, reputable press. Open the page; cite the URL. If a page will not open, it is not a source.

If there is no transcript (notes only, or no recording), stop and say so: the feature needs the founder's own words. Suggest booking a 30-minute feature call with Akshay (podm.in/30min).

## Step 1: Read the whole call

Read the full Transcript tab, not just Gemini's notes. Build a working list as you go, each item with its timestamp:

- **Identity:** founder's name, role, company name, where based, when founded, team size.
- **What it does and for whom:** product, customer, the problem, price points.
- **Founding story:** what they did before, the turning point, early failures, how the first customers came.
- **Hard decisions:** a pivot, a market choice, what they said no to, a trade-off they explained.
- **How it works / business model:** how they deliver, how they charge, what makes customers pay.
- **Traction:** customers, volumes, revenue, growth, geography. Only what they said.
- **What's next:** plans, markets, hiring.
- **Off the record or sensitive:** anything per rules 5 and 6.
- **About Founder Thesis:** note it so you know to leave it out (rule 7).

Gemini mishears names, companies and numbers. Where the transcript and Gemini's notes disagree, the transcript wins, and the disagreement goes in GAPS.

## Step 2: Check what can be checked

Open the company website and, if reachable, the founder's LinkedIn. Use them to confirm spellings, location and founding year, and only to add a fact that the call does not cover if it is plainly public and harmless (for example, the city the company is based in). Every such fact gets a URL in SOURCES. If a public source contradicts the call, do not pick a winner silently: use the founder's own account in the text only if it is not a hard fact that the public record disputes, and list the conflict in GAPS.

## Step 3: Find the hook

Pick the single most interesting true thing from the call. Good hooks are specific and surprising: an unusual career turn, a number that reframes the business, a contrarian choice. The hook drives the title and the standfirst. It must be sourced like everything else.

## Step 4: Write the feature

Length: 600 to 900 words in the body (title, standfirst, About box, SOURCES and GAPS not counted). If the call does not support 600 honest words, write shorter and say so in GAPS. Never pad.

Structure:

```
# <Founder name>, <Company>: <the hook, in plain words>

<Standfirst: two lines. Who they are, what the company does, why it is worth reading.>

## <What the company does and for whom>
## <The founding story>
## <The hard decisions>
## <How it works / the business model>
## <Traction they shared>
## <What's next>

> **About <Company>**
> <3 to 4 lines: what it does, founded when and where, founder and role, team size, website. Only sourced facts.>
```

Section headers are sentence case and specific to this story ("Apple at 21, then a startup he hated", not "Background"). Merge or drop a section the call does not cover; do not fill it with generalities. Keep the hook in the first two paragraphs.

**Title:** founder name + company + the hook, under about 70 characters where possible, with the words a person would search ("cold email", "B2B lead generation", the city or sector). No clickbait, no question titles, no colon chains.

**Voice:** third person, present tense for the company, past tense for the story. Plain and concrete. Let numbers carry weight. One idea per paragraph, two to four sentences each, with the odd one-liner.

## Step 5: SOURCES and GAPS

After the feature, add:

```
---
## SOURCES
1. "<claim as written in the feature>": [00:11:02] Founder: "<verbatim transcript line>"
2. "<claim>": <URL> (opened <date>), "<the line on the page>"
...

## GAPS
- <what is missing or uncertain, and what would settle it>
- withheld: off the record, [hh:mm:ss], <one-line description, no detail>
- not used: <fact only in material their team sent / only in Gemini summary / hedged number>
```

Every number and every factual sentence in the feature has a numbered SOURCES entry. Claims about the founder's motives or feelings need a quote that states them. GAPS always lists at least: the spelling checks you could not complete, anything a reviewer should confirm with the founder before publishing, and anything deliberately left out.

## Step 6: Self-check before handing over

Go through this list and fix anything that fails. Report the result in one line under GAPS ("Self-check: passed" or what still fails).

- [ ] Every number in the feature appears in SOURCES with a timestamp or URL.
- [ ] No fact comes from the founder's team's written material.
- [ ] Nothing from the Founder Thesis side of the call (reach, pricing, barter, booking decision).
- [ ] No off the record or hedged item in the text.
- [ ] Direct quotes: verbatim, attributed, at most three, none longer than a short phrase unless marked as the founder's words.
- [ ] Zero em dashes (search for the character U+2014); none of: delve, leverage, unlock, robust, seamless; no "it's not X, it's Y".
- [ ] Headers in sentence case.
- [ ] Body word count between 600 and 900, or the shortfall explained in GAPS.
- [ ] Names spelled as the company spells them, or flagged in GAPS.

## Output

Return the Markdown (feature, then SOURCES, then GAPS) in chat or write it to the file path you were given. Do not publish it, upload it, post it, mail it, or write it to Notion; the person who ran the skill hands it to Ranjita, who publishes it on founderthesis.com after review. If the founder later asks for changes, Akshay decides; facts the founder adds by mail still need a source line saying where they came from, and new facts beyond corrections need a call.
