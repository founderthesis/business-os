---
name: meeting-intel
description: "Turn a meeting or call transcript into an intelligence note that tests what was said against existing project research and external sources. Trigger on /meeting-intel or when a transcript is supplied with intent to extract findings rather than minutes."
---

# Meeting intelligence note

Turns a transcript into a document that answers one question: what do we now know that we did not know before, and what did we believe that turns out to be wrong.

This is not minutes. Minutes record what happened. This tests what was said against what the project already holds and against the public record, and reports where the three disagree.

Trigger on `/meeting-intel`, "intelligence note", "what did we learn from this call", "write this call up", or a transcript supplied with intent to extract findings.

---

## Before starting, ask two things

Ask both in one message, then wait.

1. **Who else will read this?** The answer governs the curation pass in Phase 2. Naming the people matters: a note that the counterparty or the person who made the introduction may see is edited differently from one that stays internal.
2. **Is the transcript complete?** Recording tools often capture only one side. If only one speaker is present, everything attributed to the other party is reconstructed from the first speaker's restatements, and the user's own recollection becomes a source. Ask them to fill the gaps from memory now, while it is fresh.

Do not ask anything else. If they supply a name or a company with no transcript, ask for the transcript once.

---

## Phase 1: the findings map, then STOP

### Search project knowledge before anything else

Run `project_search` on the main subjects in the transcript before any external research. Read the documents that come back. The existing research is the baseline every finding is measured against, and quoting it is what separates this document from a summary.

### Sort every substantive claim

Five buckets:

- **Validates.** The transcript confirms something the research asserted. Strongest when a live operator's number lands inside a band the research derived from published sources.
- **Disputes.** The transcript contradicts a stated finding. These are the most valuable and the most dangerous, because a single source can be wrong or self-serving.
- **Complicates.** Both are true of different things, or the disagreement is about how normal something is rather than whether it happens.
- **New.** Closes a question the research explicitly left open, or introduces something it never contemplated.
- **Corrects the file.** The transcript shows a project document is factually wrong. This gets its own callout, because stale knowledge poisons every downstream decision.

### Present the map and stop

Output a compact list: one line per finding, bucketed, with the project document it bears on. No prose, no research yet, under 400 words.

Then **STOP** and ask which findings to build out. Do not start Phase 2 until they answer.

---

## Phase 2: verify, then write

### Verify before reporting

Every checkable factual claim gets searched. Do not repeat what the person said as though saying it made it true.

**The pattern to look for: right on the fact, wrong on the cause.** People in a market know what happened and often attribute it wrongly. Someone may say a government shut a sector down when the sector actually exhausted a published quota. Both mean the sector is shut, but one is arbitrary and unplannable while the other is measurable and predictable. The corrected version is always the more useful finding, so spend the research effort.

**Numbers that do not fit get researched, not reported.** If a figure seems off by an order of magnitude or inconsistent with the role described, go and find real market data, then reconcile. State the reconciliation plainly rather than hedging about what was recalled.

**Anchor economics on the median, state the top as upside.** A model built on the best case only works if every case is the best case. Lead with what a typical instance earns or costs, then give the upper end in a separate sentence. Name the market average as the one comparator so the reader can see where the figure sits.

**Where a claim is competitively convenient for the person making it, say so once, neutrally.** "Worth a second source before it carries weight" is enough. Do not editorialise about motive, particularly when someone else made the introduction.

### Label inference separately

Anything concluded rather than stated gets marked as such: "Our inference, not his words." Never let a conclusion drift into the document as reported fact.

### Do not speculate beyond what was discussed

If the counterparty did not raise a capability, do not write about whether that capability would help. Speculating about the reader's own assets in a document about someone else's business reads as wishful thinking and it is the fastest way to lose the reader's trust in the rest.

### The curation pass

Run this against the readership answer from the start. Cut:

- Business failures, ventures closed, moments of doubt, and anything else said candidly in a private call that would embarrass the counterparty if the document travelled
- Compliments exchanged, warm exchanges, and anything about how the conversation went rather than what was in it
- Travel details, scheduling, interruptions, small talk
- Any framing that implies a colleague's earlier judgement was wrong. Correct the document, not the person: "worth correcting in the file" rather than "the premise this was built on was mistaken"

Keep the counterparty's operating logic and cut the personal framing around it. "He is uncomfortable with this model" becomes the reason the model is hard to run.

---

## Structure of the document

Target 1,500 to 2,000 words. Every section leads with a bolded phrase so it reads on a scroll.

1. **Title and one line** naming who was spoken to, when, and who made the introduction if relevant.
2. **In short.** Five bullets maximum, each a finding rather than a topic. This is what gets read. Write it last.
3. **The person, briefly.** Two or three paragraphs. Enough to establish standing, nothing more.
4. **What the business actually is.** Correct the project's picture of it here if the picture is wrong. Numbered list for business lines.
5. **The substance**, in whatever order the findings demand. Economics usually deserves its own section.
6. **Where this cuts against our thesis.** Disputes, each with the verification underneath it as short bullets with dates.
7. **Still to verify.** Bolded lead-in per item, saying why it matters and who can close it.
8. **Sources.** Live links, described so the reader knows what each one settles. The single-source caveat lives here, not at the top.

### What not to include

- Tables, unless the data genuinely has two dimensions. Three numbers in a sentence beat a three-row table.
- A sourcing caveat before the findings. It delays the payload and the Sources section already carries it.
- Benchmark lists as supporting evidence. Pick the one comparator that makes the figure land.
- Confidence markers on every line. Reserve them for the handful of claims that genuinely rest on one unverified source.

---

## Voice

Prose and lists. Short varied paragraphs, contractions, specifics over generalities. Sentence case headers. No em-dashes, no rule-of-three, no puffery, no "it's not X, it's Y" constructions. Quote yen, dollars or the local currency as primary and give rupee equivalents with the rate noted.

Never invent a number. If a figure is not in a source, say so.

---

## Output

Write a markdown file, deliver it with `SendUserFile`, and save it to project knowledge with `project_write` at `claude/<subject>-note.md` so the next session builds on it rather than rediscovering it.

Expect corrections on the finished draft rather than approval of an outline. When a correction lands, apply it, restage the file, rewrite to the project, and say in two lines what changed.