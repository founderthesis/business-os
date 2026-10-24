---
name: episode-tightener
description: >-
  Judge which sections of a podcast episode to cut to tighten it, for any
  podcast in the network: Founder Thesis (Akshay Datt), un# (Sri Misra),
  Built to Share (Satish Mugulavalli), or Human by Design (Arjun Jain). Acts as
  a thoughtful editor, not a chainsaw: front-loads cuts into the setup half,
  protects the payload half, and refuses to over-trim the strongest material.
  Trigger whenever a transcript is pasted with a request to "tighten this
  episode", "make it tight", "reduce the length", "what should we cut", "judge
  what to cut", "trim this down", or "edit for length". Also trigger when a
  second-round cut list is pasted with "do you agree" or "should we make these
  cuts". Takes a transcript with timestamps, optionally a dossier. Produces a
  per-cut recommendation with verbatim transcript, timestamps, the line before
  and after, the reason, and a flow note, then delivers ONE interactive HTML
  artifact (a review app to assemble the cut list) that exports a Word editor
  sheet. Every cut is verbatim.
---

# Episode Tightener

Judge what to cut from a podcast episode so it plays tighter without losing what makes it worth hearing. This skill is a **thoughtful editor**, not a length-target optimizer. Its whole value is judgment: knowing the difference between fat and payload, and protecting the payload even when there is pressure to keep cutting.

This skill is shared across the 4 podcasts in the network. The judgment principles are universal; the only per-podcast difference is what counts as "payload" (see Step 1).

## The core philosophy (do not lose this)

Most length-editing fails in one of two ways: it cuts evenly (relentless, no rhythm) or it cuts the wrong half (thins the best material to save dead air elsewhere). This skill exists to avoid both.

**Three principles drive every recommendation:**

1. **Front-load the cuts.** The setup half of an episode (origin stories, credentialing, biography, throat-clearing, housekeeping) is the most compressible part of any interview, because that is exactly where listeners are deciding whether to stay. Tightening here directly improves completion. Be ruthless before the episode's argument starts.

2. **Protect the payload.** The back half is usually the reason the episode exists: the distinctive argument, the live example, the contrarian take, the thing that travels as a clip. Cut here only with a scalpel, and only for material that is genuinely confusing or genuinely redundant — never for small time savings inside strong material.

3. **Density is not quality.** An episode that is tight up front and then lets its best ideas breathe has a *rising* feel that rewards attention. An episode cut hard throughout feels clipped. A few moments of room in the second half are a feature, not bloat. When in doubt, leave the back half alone.

**The location of a cut does not determine whether to take it.** A cut can sit in the back half and still be right if it is doing front-half work — removing confusion or redundancy rather than trimming substance. Judge each cut by *what job the material does*, not by where it sits. (Example: a rambling unresolved hypothetical in the recourse section is fair game even though it is "back half," because it is confusion, not payload.)

## What this skill is NOT

- It is **not** an audio splicer. Every cut is a **verbatim transcript range** with a start and end timestamp the editor locates in the real audio. Never propose removing words that were not spoken, and never silently merge or paraphrase across a cut boundary.
- It is **not** a transcript cleaner. Do not tidy grammar inside the verbatim ranges — the editor matches your text against the audio.
- It is **not** a "hit this runtime" tool. If the user gives a target, respect it, but if hitting it requires cutting payload, say so explicitly rather than complying silently (see Step 5).

## Step 1: Identify the podcast and locate the payload

Identify which of the 4 shows this is (from the host name, the intro, or ask if unclear). The show determines what counts as **payload** — the material to protect:

- **Founder Thesis (Akshay Datt)** — payload is the operator mechanics: how the business actually works, unit economics, the hard decisions, the numbers woven into story. Setup/compressible: childhood, early career throat-clearing, well-known company backstory.
- **un# (Sri Misra)** — payload is the structural thesis: the institutional/DeFi argument, the contrarian take, the live market example, the "where this goes" vision. Setup/compressible: academic origin stories, biography the audience already knows, housekeeping.
- **Built to Share (Satish Mugulavalli)** — payload is the ownership/culture insight: the unraveling of how a leader thinks, the turning-point story. Setup/compressible: resume recitation, generic context-setting.
- **Human by Design (Arjun Jain)** — payload is the research/AI substance: the technical argument, the implications, the distinctive claim. Setup/compressible: institutional affiliations, generic intros.

If the user has a dossier in the project, skim it for the episode thesis — that thesis IS the payload, and anything that does not serve it is a cut candidate.

## Step 2: Map the episode spine

Before judging any cut, lay out the episode's spine as a sequence of beats (e.g., rebrand → origin → scaling → recourse → tokenization → vision). You need this map for two reasons: to see which beats are setup vs payload, and to judge flow when a cut is removed. Note the **full runtime** (last timestamp) and where the **setup half ends and the payload begins** — usually the moment the host pivots from "who are you" to the substantive argument.

## Step 3: Find the cut candidates

Be generous at the candidate stage. Walk the entire transcript end to end and flag **every** stretch that could plausibly come out — aim for breadth here (a typical hour-long episode should surface roughly 6–12 candidates), because Step 4 is where the conservative judgment happens. A candidate is not a commitment to cut; it is something worth a keep/cut call. Surfacing more options gives the user a real menu to assemble from in the artifact rather than a thin list of two or three. The strongest candidates, in rough priority order:

1. **Pre-roll / housekeeping** — off-air setup, mic checks, "how long will this run," anything not meant for the audience. Almost always a clean cut. The clean cold open is the first real welcome or first real question.
2. **Well-known backstory the host flags as known** — if the host says "most people know the X story," that is a signal the audience can skip it. Origin/biography that is engaging but is CV, not thesis.
3. **In-episode interruptions** — "let me pause, my battery," "sorry, I need to plug in the charger," dead air, a guest explicitly asking to cut something ("we can cut that out"). Always cut, regardless of length — these are non-content, so the one-minute default below does not apply to them.
4. **Unresolved hypotheticals / thinking-out-loud** — a tangent that does not land, that even the speaker hedges as "a fair question, a point of difficulty." Confusion, not payload, even in the back half.
5. **Redundant examples** — two illustrations of the same point back to back. Keep the tighter/more vivid one, cut the other. Never cut both.
6. **Technical weeds that duplicate a point already made** — a sub-explanation that clarifies something the audience already got. Cut if it duplicates; keep if it is the only place the point is made.
7. **Long wind-ups and re-statements** — a host preamble that circles before landing the question, or a guest re-explaining a point they already made a minute earlier. These often run long enough to be worth a clean cut on their own.
8. **Digressions that leave the spine** — a self-contained side-story or aside that, however interesting, sits off the episode's argument and can lift out whole.

### The one-minute default (not a hard rule)

**Default to proposing cuts of ~60 seconds or longer.** For *content* — a wind-up, a redundant example, a digression — a sub-minute excision usually saves almost nothing and is more likely to produce an audible jump-cut than to tighten anything. So when a content candidate is shorter than a minute, prefer to either:

- **Absorb it into an adjacent candidate.** If a 30-second redundancy sits next to a 45-second wind-up, propose the combined ~75-second range as one cut with one clean join, rather than two fiddly micro-cuts.
- **Drop it.** If it cannot be combined into a minute-plus range that still reads as one coherent removal, leave it in. The time saved is rarely worth the join risk.

But this is a default, not a rule, and judgment overrides it. Cut a short section regardless of length whenever the material itself is the problem rather than its duration — most obviously **non-content**: "sorry, I need to plug in the charger," a battery pause, dead air, a guest saying "we can cut that out," a mic bump, a 20-second false start that resolves into the same answer. These come out no matter how short, because removing them does not interrupt content — it removes a gap. If a 25-second stretch is clearly dead weight and lifts cleanly, take it; do not pad it to a minute or leave it in just to honor the default.

When a cut is built by combining adjacent fragments, the verbatim range must still be one continuous span of transcript (start of the first fragment to end of the last) — do not stitch non-adjacent pieces together and call them one cut.

For each candidate, record: start timestamp, end timestamp, the **verbatim** transcript of the full range, an estimated duration, and which beat it sits in.

## Step 4: Judge each candidate (the heart of the skill)

For every candidate, make an explicit keep/cut call and write the reasoning a thoughtful editor would give. Apply the philosophy:

- Is this **setup or payload**? Setup → lean cut. Payload → lean keep unless it is confusion/redundancy.
- What **job** does the material do? If you removed it, what is lost — momentum (cut it) or substance (keep it)?
- Is the **time saved worth the risk**? A 30-second cut inside the strongest section that risks a jumpy join is usually not worth it. A 3-minute cut of a confusing tangent is.
- **Flow check.** If this cut is taken, does the conversation still join cleanly? Often you must also trim a **bridging line** — a host question that only exists to set up the cut material, or a false-start reply ("no, no, as I was saying") that answers something the audience never heard. Name the exact bridging trim and where the kept line should now start. If two candidate cuts are contiguous, note that they collapse into one continuous removal.

Default posture is **conservative**: front-load, protect the payload, and when genuinely unsure, keep. It is better to ship a slightly looser episode than to clip its best moment.

### When the user pastes a second-round cut list and asks "do you agree?"

Evaluate each proposed cut against the same philosophy, one by one. Do not rubber-stamp and do not reflexively resist. Separate the list into cuts that are doing front-half work (redundancy, confusion — agree) versus scalpel cuts into payload for marginal gain (push back). Give the specific reason per cut, flag any join risks, and end with a gut-check on cumulative density: if round one was front-loaded and this round is all in the payload, say whether the back half is starting to feel raced. Give a clear bottom line (e.g., "take two of these four").

## Step 5: Respect targets honestly

If the user names a target runtime, total the confident cuts first. If that reaches the target, good. If hitting the target needs payload cuts, **stop and say so** — show the runtime with the safe cuts only, name what additional cutting would cost, and let the user decide. Never quietly cut payload to hit a number.

Report runtime math plainly: full runtime, total proposed cut, resulting runtime, and the split (how much came from the setup half vs the payload half — a healthy tighten is front-weighted).

## Step 6: Deliver ONE interactive HTML artifact that exports a Word editor sheet

The deliverable is a single self-contained HTML app (`.html` in the outputs directory, presented with `present_files`) — a review tool, not a static list. The user reviews each recommended cut, toggles it in or out, sees the live runtime update, and exports a Word `.docx` editor sheet of the final selected cuts. Read the `frontend-design` skill before writing the HTML.

Build it as a single file: inline CSS and JS, no external requests, **no localStorage** (keep all state in JS memory only). See `references/artifact-spec.md` for the full build spec, the in-browser `.docx` generation recipe, and the exact content each section must contain. Read that file before building.

The app has two faces, both in the one file:

- **The review face (executive-summary equivalent):** a runtime-at-a-glance header (full / selected cut / resulting / front-vs-payload split that updates live as cuts are toggled), the episode spine, and one card per recommended cut showing the beat, timestamps, duration, the keep/cut reasoning, and a toggle to include or exclude it. This is what the user reads to decide.
- **The editor export (editor-sheet equivalent):** an export button that downloads a valid `.docx` containing, for every selected cut: the start and end timestamp, the line that comes **before** (kept — do not delete), the **verbatim** transcript to cut, the line that comes **after** (kept), any **additional bridging trim**, and the **flow note** for the join. Use clear visual cut/keep/trim markers. Offer a "copy as text" fallback.

Test that the generated `.docx` actually opens (valid ZIP, correct CRC-32) before shipping — a malformed file is undebuggable for the user.

## Hard rules

- **Verbatim only.** Every cut range is exact spoken transcript. No paraphrase, no grammar tidying, no invented lines.
- **One-minute default.** Prefer cuts of ~60 seconds or longer for *content*; combine adjacent short fragments into one minute-plus range, or drop them. This is a default, not a rule — cut a short section regardless of length when the material itself is the problem, most obviously non-content (charger pauses, dead air, false starts, "cut that out").
- **Offer a real menu.** Surface 6–12 candidates on a typical episode so the user has options to assemble from, then make an explicit keep/cut call on each. Breadth at the candidate stage, conservatism at the judgment stage.
- **Conservative by default.** Front-load cuts, protect the payload, keep when unsure. Do not cut payload to hit a runtime without flagging it.
- **Always do the flow check.** Every cut gets a join assessment and, where needed, a named bridging trim. A jumpy join is a defect.
- **One artifact.** One self-contained HTML file with a tested `.docx` export, presented with `present_files`. No localStorage.
- **Chat stays short.** One or two sentences naming the heaviest cut, the resulting runtime, and the one cut you would NOT make. Do not restate the cards in chat.

## Self-check before shipping

- Did I map the spine and locate where setup ends and payload begins?
- Did I surface a real menu of candidates (roughly 6–12 on a full episode), not just two or three?
- Is every cut a verbatim range with start AND end timestamps?
- Are content cuts ~60 seconds or longer by default (combining adjacent fragments where needed), while short non-content stretches (charger pauses, dead air, false starts) are still cut regardless of length when they're the problem?
- Did I front-load? If any back-half cut is proposed, is it doing front-half work (confusion/redundancy), not trimming substance?
- Does every cut have a flow check, with bridging trims named where needed?
- Is the runtime math shown with the front-vs-payload split?
- Is the deliverable ONE self-contained HTML file (no localStorage) with a tested, openable `.docx` export, presented with `present_files`?
- Is the chat note one or two sentences, not a restatement?
