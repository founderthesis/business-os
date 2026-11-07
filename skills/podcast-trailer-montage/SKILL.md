---
name: podcast-trailer-montage
description: >-
  Build an intro trailer (montage) for any podcast in the network: Founder
  Thesis (Akshay Datt), un# (Sri Misra), Built to Share (Satish
  Mugulavalli), or Human by Design (Arjun Jain). A trailer is NOT a host-read
  intro line (that is the podcast-intro-voiceover skill); it is a montage of
  verbatim guest/host soundbites clipped from the episode audio, with one
  host-voiced VO, plus an editor pull-sheet of exact timestamps. Trigger on
  phrases like trailer, montage, sizzle, teaser cut, soundbite reel, cold open,
  "cut a trailer for this episode", "pull soundbites", or any request to
  assemble episode audio clips into a promo. Takes a transcript and optionally a
  dossier. Outputs an interactive HTML artifact with three menus the user
  assembles from: a tagged menu of 12-18 verbatim soundbites (flagged by role,
  speaker, and flow), a voice-over menu, and suggested combinations.
  The user ticks clips, drags them into order, and exports a Word doc for the
  editor. The VO reads aloud, so no em-dashes or buzzwords.
---

# Podcast Trailer Montage

Assemble an episode trailer from **verbatim audio soundbites** plus **one host-voiced VO**. The trailer plays as a promo (LinkedIn, YouTube intro, social cut) and as the cold open before the episode proper. This skill is shared across the 4 podcasts in the network.

## What this skill is NOT

This is the trailer/montage skill. It is a **sibling** to `podcast-intro-voiceover`, not a replacement.

- `podcast-intro-voiceover` → a single spoken intro line the host reads. No clips. No timestamps.
- `podcast-trailer-montage` (this skill) → a montage of **clipped episode audio** (verbatim soundbites) with **one VO in the middle** and an **editor pull-sheet of timestamps**.

If the user wants only a spoken intro with no clips, route to `podcast-intro-voiceover`. If the user wants clips assembled into a promo, this is the right skill.

## The output shape (what we are building)

The output is a **menu the user assembles from**, not a set of finished trailers. The user picks soundbites to include or exclude and orders them into their own cut. The deliverable is three menus, delivered as one artifact:

1. **A soundbite menu** — a single table of 12-18 verbatim, selectable clips. Each row is tagged so the user can see at a glance what job it does: whether it works as an **opener**, as a **cliffhanger ender**, as a mid-montage line, who speaks it (host/guest), and which earlier soundbite it **flows from** (a link cue) versus standing alone as a clean **cold start**. The user includes or excludes rows freely.
2. **A voice-over menu** — 3-4 alternative VO blocks the user can pick one from (or none). Each is host-voiced, names the podcast, and teases a slightly different territory, so the choice of VO can re-angle the whole trailer.
3. **A combinations menu** — 3-4 suggested ready-to-run assemblies, each naming a specific subset of soundbite rows by number plus one VO, in cut order. These are starting points; the user is free to ignore them and build from the raw menu.

The trailer still plays on the same proven spine when assembled (an attention-grabbing open, a VO that frames, a cliffhanger out), but the VO does **not** have to sit in the valley — see rule 5. The skill hands over the parts and a few suggested assemblies, not pre-packaged theme-options.

### The five assembly rules (encode these in the menu tags)

These are the rules the menu must make easy to follow. Tag and order the menu so the user can obey them without guessing.

1. **The opener grabs attention.** The starting byte must earn the next five seconds: counter-intuitive, a bold claim, a big number, or an emotional moment, and **short**. Two kinds qualify, and the menu should mark both:
   - **Standalone opener** — arresting on its own ("We're not playing power law").
   - **Setup opener** — a quieter line that only lands because a **front-loaded VO pays it off seconds later** ("our best performers are manufacturing companies" → VO: "Most VCs avoid factories. Rajeev does the opposite"). A setup opener is only valid when paired with an early VO; do not pair one with a valley VO that arrives too late to rescue it. Tag setup openers `Opener (needs early VO)` so the dependency is explicit.
   A long or throat-clearing line is not an opener either way.
2. **The ender is a cliffhanger.** The closing byte leaves the audience hungry. Two strong forms, and you should surface several of each:
   - **Clipped guest line** cut off mid-thought, before the payoff (give the exact out-point).
   - **Host question with no answer attached** — this is prime cliffhanger material and the show's most natural hook ("would you have invested in Raw Pressery?", "what's an example of a company catering to the top 10% that's really broken out?"). Mine host questions deliberately as enders, not just as setups. The menu must surface **at least 2-3 host-question closers**.
3. **Intersperse host bytes, never two in a row.** Host lines must be present (see host ratio below), but two host bytes back to back is a defect. The combinations menu must never place two host rows consecutively, and the soundbite menu should flag host rows clearly so the user avoids it too.
4. **Make the montage flow.** A byte that links to the previous byte (answers its question, completes its thought, picks up its word) is preferred over a jump cut. For each row, note in a **flow** column what it links from, or mark it **cold start** if it stands alone. The combinations menu should chain linked rows where possible.
5. **VO placement is a variable, not the valley by default.** The VO can sit in three places, and the combinations menu should show more than one:
   - **Front-loaded** (after the opener, near the top) — the VO frames the whole montage early, then the soundbites deliver evidence. **This is often the strongest choice, and it is required when the trailer opens on a setup opener** (rule 1), because the setup needs the VO to pay it off fast.
   - **Valley** (in the middle) — the classic split between an opening run and a closing run.
   - **Split** (two short VO fragments) — rare, only if the reference file allows it.
   Pick placement per combination and state it. Do not hard-code the valley.

## CRITICAL: the host must be present (no two in a row)

The host is the through-line across every episode; a menu the user could assemble into an all-guest supercut erases the show's host. In practice, the cuts that play best run **about a third host** — host questions open and close the strongest montages. So the **soundbite menu must contain enough host lines that any sensible assembly lands at 25-35% host** (pull at least 5-6 strong host candidates into the menu, including several host *questions* usable as openers or enders), and **every suggested combination must itself be 25-35% host** (the VO does not count; it is fresh-read, not a clip).

But host lines are setups and punctuation, not a block. **Never place two host bytes consecutively** in a suggested combination, and flag host rows in the menu so the user keeps them interleaved: a host question that sets up the guest's payoff, the guest landing it, the host pushing back or punctuating the next guest line. That interleaving is what makes the cut play as a conversation rather than a supercut.

## CRITICAL: verbatim audio only

The soundbites are **clipped from the real episode audio**. The editor can only cut what was actually said. Therefore:

- **Every soundbite must be a verbatim string from the transcript.** Do not tidy grammar, merge two sentences, or smooth a run-on. If the clean line you want does not exist as spoken, you cannot use it — find the nearest verbatim line that exists, or pull a clean clause.
- **Quote the exact spoken words**, including the speaker's actual phrasing even if slightly awkward. The editor matches your text against the audio.
- **Give the transcript timestamp** for every soundbite so the editor can locate it.
- If the idea you want only exists mid-run-on (joined to other content), say so explicitly and give the editor the boundary, or pick a cleaner fragment.
- The **VO is the only place fresh-written prose is allowed.** It is recorded by the host, not clipped. Everything in the soundbite tables is constrained to what exists in the audio.

A trailer that proposes a soundbite the guest never said verbatim is a hard failure — it sends the editor hunting for audio that does not exist.

## Step 1: Identify the podcast

The 4 podcasts in the network:

| Podcast | Host | Topic | Reference file |
|---|---|---|---|
| Founder Thesis | Akshay Datt | Indian startup founders | `references/founder-thesis.md` |
| un# | Sri Misra | Crypto, DeFi, CeFi, Web3 | `references/unhashed.md` |
| Built to Share | Satish Mugulavalli | Talent wars, team building | `references/built-to-share.md` |
| Human by Design | Arjun Jain | AI builders and production reality | `references/human-by-design.md` |

Identify which podcast this is for:

- The user may state it explicitly ("trailer for Human by Design", "Sri's show", "cut a montage for Founder Thesis").
- Context may make it obvious from the transcript subject: DeFi/stablecoins → un#; hiring/ESOPs/attrition → Built to Share; model training/edge AI/computer vision → Human by Design; Indian startup scale stories → Founder Thesis.
- If unclear, ask once with the 4 options. Do not guess.

Read the matching reference file in `references/`. It carries the podcast's audience, host voice, the canonical branded name, currency preference, and a **trailer-specific section** covering how soundbite clusters and the VO should feel for that show.

## Step 2: Input

**Required: the episode transcript with timestamps.** This is non-negotiable — without timestamps mapped to spoken text, there is no pull-sheet and no skill. The transcript is the source of every soundbite.

**Optional but recommended: a research dossier.** Used only to inform the VO (credibility signal, scale number, what the guest is known for). The dossier never supplies soundbites — soundbites come only from the transcript.

If the user provides no transcript (or a transcript with no timestamps), **stop and ask for it**. Explain that a montage is built from clipped audio, so verbatim lines and their timestamps are required. Do not generate a trailer from a dossier alone — that is the pre-interview case, which this skill does not cover (it would produce fabricated soundbites).

## Step 3: Mine the transcript for soundbites

Read the full transcript and mark candidate clips. A good trailer soundbite is:

- **Short.** One sentence or a clean clause. Long enough to land, short enough to cut cleanly.
- **Self-contained.** Makes sense without the surrounding paragraph. Avoid lines starting with "and then", "so", "but that", or a pronoun whose referent is offscreen — unless paired with a setup line.
- **Verbatim and clean at the boundaries.** The editor needs clean in/out points. A clip joined to other content mid-breath is harder; flag it.
- **One of these flavors:**
  - **Provocation** — the most arresting, contrarian, or quotable thing the guest says. These make the strongest openers.
  - **Setup / pushback line (host)** — a short host question, framing, or challenge that sets up or punctuates a guest payoff. **Mine these deliberately, not as an afterthought.** Look for: the question that triggered the best guest answer, a sharp one-line reframe ("So you're saying X?"), a moment of genuine pushback or surprise, or a crisp summary the host lands. These are what make the montage feel like a conversation. You need host candidates to fill 25-35% of every option, so pull at least 5-6 strong host lines, and treat host *questions* as doing double duty (they also open and close cuts).
  - **Mechanic / insight** — a crisp articulation of how something works or a mental model.
  - **Origin / stakes** — a line about why the guest started, what is at risk, or what they are chasing.
  - **Payoff / forward-look** — a line that points ahead, ending the trailer on momentum.
  - **Cliffhanger** — leaves the audience hungry. Two forms: (a) a guest line clipped right before the payoff ("the real reason is..." then a hard out), or (b) **a host question with no answer attached** ("would you have invested in Raw Pressery?", "what's broken out in the top 10%?"). Host questions are the most reliable closers the show produces — mark every strong one and ensure at least 2-3 reach the menu.

Mine generously: the menu surfaces **12-18 soundbites**, so pull 18-22 candidates and keep the best. Of those, make sure at least 5-6 are host lines — track them separately so they do not get crowded out when you select for the guest's best moments. You also need a healthy supply of two scarce flavors, because the menu must offer real choice for the open and the close:

- **Openers:** mark at least 3-4 candidates. Include both **standalone openers** (arresting alone) and **setup openers** (a quieter line a front-loaded VO will pay off). Tag setup openers so the VO dependency is visible.
- **Cliffhangers:** mark at least 3-4 candidates, and make sure **2-3 of them are host questions** with no answer attached (the show's most reliable closer), alongside any clean mid-thought guest cuts.

Apply the reference file's trailer section for what flavor leads best for that show (e.g., Human by Design leads on a technical provocation; Founder Thesis often leads on a scale reveal or origin stakes).

## Step 4: Build the three menus

### 4a. The soundbite menu (12-18 rows)

One table of selectable verbatim clips. This is the heart of the deliverable. Each row carries these columns:

- **#** — a stable ID the combinations menu and the user can refer to.
- **Speaker** — host or guest name.
- **Timestamp** — line-start, for the editor to locate the audio.
- **Verbatim line** — the exact spoken words (see the verbatim rule; never tidied).
- **Role** — what job the byte can do: `Opener`, `Opener (needs early VO)`, `Cliffhanger`, or `Mid`. A row can carry two tags (e.g. `Opener / Mid`) if it genuinely works in more than one slot. Tag `Opener` only if short and arresting on its own; tag `Opener (needs early VO)` for a setup line that needs a front-loaded VO to pay it off; tag `Cliffhanger` only if it ends hungry (a clipped guest line or an unanswered host question).
- **Flow** — either `Cold start` (stands alone, safe to open on or jump-cut to) or `From #N: <why>` (links to another row by answering its question, completing its thought, or picking up its word). This is what lets the user chain a flowing montage.

Order the menu roughly by where bytes tend to sit (openers near the top, cliffhangers near the bottom, mids in between) so the table reads as a usable spectrum, not a jumble. Keep at least 3-4 `Opener` rows (a mix of standalone and setup) and 3-4 `Cliffhanger` rows (including 2-3 host questions) so the user has a real choice at both ends. Keep host rows at a level where any sensible assembly can hit 25-35% host.

### 4b. The voice-over menu (3-4 VOs)

3-4 alternative VO blocks, each within the reference file's word count, each naming the podcast and guest and teasing **a different territory** so the pick re-angles the trailer (e.g. one leads on the contrarian thesis, one on the origin/scale number, one on the single biggest idea). Label each VO with a short tag for what it foregrounds. Favour the **short, blunt, slightly irreverent register** that plays best (see VO style rules): "Most VCs chase unicorns and avoid factories. Rajeev Kalambi does the opposite" beats a measured, subordinate-clause read. All VO style and honesty rules below apply to every one.

### 4c. The combinations menu (3-4 assemblies)

3-4 ready-to-run starting points. Each names, in cut order, a specific subset of soundbite rows by **#**, with **one VO** placed explicitly (front-loaded, valley, or split — see rule 5; do not default to the valley). Show more than one placement across the set. Each combination must:

- **Open** on an `Opener` row and **close** on a `Cliffhanger` row. If it opens on an `Opener (needs early VO)` row, the VO must be **front-loaded**, not in the valley.
- **Flow:** prefer chains where each byte links from the previous (`From #N`); cold starts are fine but do not string three unrelated jump-cuts in a row.
- **Host ratio:** land at 25-35% host across the clips, and **never place two host rows consecutively**.
- State the **VO placement** ("VO front-loaded after #1") and carry a one-line note on the through-line, so the user sees how it differs from the others.

## Step 5: Output as an interactive HTML artifact

Deliver all three menus as **one self-contained HTML artifact** (`.html` in the outputs directory, presented with `present_files`). It is not just a viewer — it is a small app: the user ticks clips, strikes rejects, picks a VO, drags the kept set into final order, and **exports a Word doc for the editor**. A flat Markdown table can do none of that. Build it as a single file (inline CSS and JS, no external requests, no localStorage — keep state in JS memory only). Read the `frontend-design` skill before writing it.

**Theme — light and readable (not dark).** Use a light, high-readability theme: a light background (off-white or very light grey) with dark text and clear contrast. Do **not** ship a dark/night theme. Speaker distinction and badges carry colour, but the surface stays light so the verbatim lines are easy to read.

**Layout — two panes, menu left, final cut right.** Lay the app out as two side-by-side panes, not a grid of cards over a bottom tray:
- **Left pane = the soundbite menu.** A single-column, scrollable list of every generated clip, with the Role/Speaker filters above it. This is the only place the full generated set lives. Never render the soundbites as a two- (or multi-) column card grid — one column, left side.
- **Right pane = the final cut.** The build tray, persistent on the right, where kept clips assemble in order with drag-to-reorder, the chosen VO row, and the live host-ratio / VO-placement readout. A clip appears here only once kept; the same soundbite is never shown in both panes' lists at once.
- On a narrow screen the two panes may stack (menu first, cut below), but on desktop they sit left/right.

Required UX:

- **Soundbite cards, not a raw table.** Each clip is a card showing: the verbatim line (largest element), speaker (host/guest visually distinct — e.g. a colour or a left-border accent), timestamp + source file, and its Role and Flow as small pills/badges (`Opener`, `Opener · needs early VO`, `Cliffhanger`, `Mid`, `Cold start`, `From #3`). The cards stack in a single column in the left pane; let the user filter by Role so openers and cliffhangers are findable.
- **A checkbox per card to keep, and a way to strike out a reject.** Ticking a reject visibly strikes the card through and dims it (kept cards stay crisp). This is the core ask: the user is curating by elimination as much as by selection.
- **Host/guest legend and a live host-ratio readout** of the currently-kept set, so the user can see if they have drifted out of the 25-35% band or stacked two host clips.
- **The VO menu as selectable cards**, one selectable at a time (radio-style), each tagged with what it foregrounds.
- **Combinations rendered as visual strips, not arrow text.** Each suggested combination is a horizontal sequence of mini-chips in cut order, with the chosen VO shown as a distinct chip sitting where it plays (front-loaded chip near the left, valley chip in the middle). Label the placement on the strip. Clicking a combination can highlight its member cards above so the user sees what it is made of. This replaces the hard-to-read `#1 → #4 → [VO2] → #7` notation.
- **A build tray (the right pane) that turns the kept set into a final cut.** As clips are kept, they drop into the right-pane tray the user can **drag to reorder**. The selected VO appears as a draggable row too, so the user positions it in the cut; show a live readout of where it lands (front-loaded / valley / tail) and the host % of the assembled cut. A per-row remove pulls a clip back out (returning it to the left menu).
- **An export button that downloads a Word `.docx`** of the assembled cut: numbered clips in the user's order (speaker, file, timestamp, verbatim line), the chosen VO marked where it plays, the host-mix, and the editor notes (cliffhanger out-points, run-on boundaries, scrub reminder). Offer a "copy as text" fallback too. This file is the durable hand-off to the editor — the whole app exists to produce it.
- **Editor notes** in a collapsible section at the bottom: run-on boundaries, leaned-on regions, exact cliffhanger out-points, and the scrub reminder.

**Generating the .docx in-browser (no libraries):** the artifact cannot import document libraries, so write a real Word file by hand. A `.docx` is a ZIP of three text parts — `[Content_Types].xml`, `_rels/.rels`, and `word/document.xml` (WordprocessingML). Build `document.xml` from the cut (one `<w:p>` per line, `<w:r><w:t>` runs, `xml:space="preserve"`, and escape `& < >`), then ZIP the three parts with a tiny inline **store-method** zipper (no compression) that computes a correct **CRC-32** per entry and writes local headers, the central directory, and the end-of-central-directory record. Trigger the download with a Blob URL and an `<a download>`. Test the byte layout before shipping — a malformed zip yields a file Word refuses to open, and the user has no way to debug it.

In the chat message accompanying the artifact, keep it to a sentence or two: name the strongest opener and the strongest cliffhanger, and point to the combination you would run if forced to pick one. Do not restate the menu in chat.

## Worked example (Human by Design — Jürgen Schmidhuber)

This shows the target menu shape, abbreviated. The transcript was a ~1h50m interview; every soundbite below is verbatim from it, with line-start timestamps. A real menu would carry 12-18 soundbite rows and 3-4 VOs; this is trimmed for illustration.

```
# Trailer soundbite menu — Jürgen Schmidhuber on Human by Design

## Soundbite menu
| # | Speaker | Timestamp | Verbatim line | Role | Flow |
|---|---------|-----------|---------------|------|------|
| 1 | JS    | 01:51:48 | "any other AI which is limited to what's happening behind the screen, that's not a real AI. That's more like a fancy text editor." | Opener | Cold start |
| 2 | JS    | 01:46:52 | "there is no AI outside of the screen in the real world and the physical world that can do what a plumber can do." | Opener / Mid | From #1: extends "behind the screen" |
| 3 | Arjun | 01:51:42 | "So essentially what people are calling embodied AI or physical AI." | Mid | From #2: names what JS is describing |
| 4 | JS    | 01:52:19 | "For that we need the real physical AIs, robots that by themselves can not only replicate themselves, but also improve themselves." | Mid | From #3: completes the thought |
| 5 | JS    | 46:33 | "the GANS, a special case of artificial curiosity of 1990 and closely related to predictable immunization of 1991." | Mid | Cold start |
| 6 | Arjun | 48:09 | "if GANs were really in your paper of 1990... why did GANs as a working technology have to be discovered again in 2014?" | Mid | From #5: pushes back on the claim |
| 7 | JS    | 48:35 | "but that has a very straightforward and obvious answer, which is computing power." | Mid | From #6: answers the question |
| 8 | JS    | 01:47:09 | "If you want to really make a dent, help to create real robots, real hardware, real factories." | Mid | Cold start |
| 9 | JS    | 01:50:08 | "which is going to be the start of an age of abundance." | Cliffhanger | From #8: the payoff, clipped before he elaborates |

## Voice-over menu
**VO1 — leads on the recognizable credential:**
> Jürgen Schmidhuber co-invented LSTM, the neural network behind Siri, Alexa, and Google Translate. He's spent decades building modern AI, and today he leads AI research at KAUST. He sits down with Arjun Jain on Human by Design to talk about why he thinks real intelligence lives outside the screen, and where it's all headed next.

**VO2 — leads on the provocation:**
> The most decorated name in deep learning thinks most of what we call AI today is a fancy text editor. Jürgen Schmidhuber sits down with Arjun Jain on Human by Design to explain what real AI looks like, why it has to leave the screen, and what happens when machines can build and improve themselves.

## Suggested combinations
**Combination A — "behind the screen is nothing"** (VO valley, after #3): #1 → #2 → #3 → [VO1] → #8 → #9
Leads on the sharpest standalone provocation, VO sits in the valley carrying the credential, ends on the "age of abundance" cliffhanger. Host appears once (#3), interleaved. ~17% host — below the 25-35% band, so swap a mid for a second host line before running.

**Combination B — "the credit dispute"** (VO front-loaded, after #1): #1 → [VO2] → #5 → #6 → #7 → #9
VO front-loaded so the provocation is the cold open and the frame lands early; the GANs exchange (#5-#7) plays as a real back-and-forth with Arjun pushing; cliffhanger out on #9. Host beats present, never two in a row.

## Editor notes
- Clips 1-4 live in one dense passage (01:46-01:52), so any combination drawn from them leans on that region; the GANs exchange (46:33-48:35) gives a second region to cut between for visual variety.
- #9 is a trimmed clause from a run-on at 01:50:08 ("then you have a new kind of life which can replicate itself without human ado which is going to be the start of an age of abundance"). Cliffhanger out: hard cut after "age of abundance". A clean in-point alternative is "then you have a new kind of life" at the same timestamp.
- Timestamps point to line start; scrub a few seconds either side for clean in/out points.
```

This example shows the menu **content** in plain text for readability; the actual deliverable renders this same content as the interactive HTML described in Step 5 (cards with keep/strike, live host ratio, combinations as visual strips). The tags let the user see which lines can open, which close hungry (#9, clipped before the elaboration), and which link to each other (#1→#2→#3 is a chain; #5→#6→#7 is the GANs exchange). The two combinations also show the two main VO placements: valley (A) and front-loaded (B).

## VO style rules (the only fresh-written element)

The VO is host-voiced and follows the same spoken-delivery rules as the intro skill:

**Write for the ear:**
- Short sentences. Periods, not semicolons.
- Read it mentally; if you stumble, rewrite.

**Do:**
- **Name the podcast aloud**, using the canonical phrasing from the reference file ("Founder Thesis Podcast", "Unhashed podcast", "Built to Share", "Human by Design"). The default slot is the sit-down line ("He sits down with Arjun Jain on Human by Design").
- Lead with the credibility signal that earns attention (the thing the audience will recognize), then the hook, then the tease.
- Use ONE primary credibility signal, optionally one humanizing secondary. Do not stack.
- Name real brands, people, institutions — they do credibility work no adjective can.
- Tease **retained episode territory** only (see honesty rule below).

**Register — short and blunt beats measured and literary:**
- The strongest reads are plain, declarative, and a little irreverent. "Most VCs chase unicorns and avoid factories. Rajeev Kalambi does the opposite." lands harder than a careful sentence with subordinate clauses.
- Lead with the contrast or the bold claim, then the name, then the tease. Two to four short sentences total.
- A concrete, slightly cheeky phrase ("skipping the AI gold rush") outperforms a neutral one ("focusing on applied AI"). Stay truthful, but do not sand off the edge.
- Founder Thesis exemplar (front-loaded, paying off a setup opener): *"Most VCs chase unicorns and avoid factories. Rajeev Kalambi does the opposite. He runs Cactus Partners, which comes in as the first institutional check at Series A. In this episode of the Founder Thesis podcast, he breaks down the anti-power-law playbook and why he is skipping the AI gold rush."*

**Don't:**
- **No em-dashes (—) or en-dashes (–).** Hard ban; they break spoken cadence and read as AI-generated. Use commas, periods, or colons. Compound-word hyphens ("AI-powered") are fine.
- No buzzwords left unpacked (check the reference file for what each audience grasps instantly).
- No hype words ("revolutionary", "groundbreaking", "game-changing").
- No generic teases ("masterclass", "shares his journey", "deep dive", "fascinating conversation"). Test: could it paste onto a different guest? If yes, rewrite with specifics.

## Honesty and edit-consistency rules

These protect the trailer from misrepresenting the episode:

- **Soundbites must be verbatim and real.** Never propose a clip the guest did not say. (Step "CRITICAL: verbatim audio only".)
- **The VO tease must point only to content that remains in the released episode.** If the user mentions that parts of the episode are being cut, edited, or scrubbed, do not build the trailer around removed material, and do not let the VO tease topics that the edit removes. A trailer that promises content the episode no longer contains misleads the audience. When the user has shared a cut list, cross-check soundbites and the VO against it and flag any conflict.
- **If asked to make a montage feel like unedited continuous conversation when it is actually stitched from distant timestamps**, that is normal trailer craft and fine — trailers are understood to be edited. The line not to cross is engineering a trailer (or VO) to make the audience believe the *episode* contains something it does not, or to hide that a guest's stated position was altered.
- The VO must not put words in the guest's mouth. It describes and frames; it does not quote or paraphrase the guest as having said something they did not.

## Self-audit checklist

Run the menus through these. Rewrite violations silently.

### Verbatim check (hard rule)
Is every soundbite an exact string from the transcript, with a timestamp? Did you tidy grammar or merge sentences? If so, revert to the real spoken words or pick a different clip. Any non-verbatim soundbite is a failure.

### Timestamp check
Does every soundbite row have a transcript timestamp? Missing timestamps make the pull-sheet useless to the editor.

### Menu coverage check
Does the soundbite menu carry 12-18 rows, with at least 3-4 rows tagged `Opener` and at least 2-3 tagged `Cliffhanger`? Without real choice at both ends the menu fails its purpose. Add candidates if either is thin.

### Opener quality check
Is every `Opener` row short and arresting on its own (bold claim, big number, counter-intuitive line, or emotional beat)? Is every `Opener (needs early VO)` row a genuine setup line that a front-loaded VO would pay off, and tagged with that dependency? A long or throat-clearing line tagged as either is mis-tagged; retag it `Mid`.

### Cliffhanger supply check
Does the menu carry 3-4 `Cliffhanger` rows, of which **at least 2-3 are host questions** with no answer attached? Host questions are the show's most reliable closer; a menu without them is thin at the most important end.

### Cliffhanger quality check
Does every `Cliffhanger` row end hungry (a clean mid-thought cut or a provocative question with no answer)? Is the exact out-point given in editor notes? A line that resolves fully is not a cliffhanger; retag it.

### Flow check
Does every row carry a `Flow` value (`Cold start` or `From #N: <why>`)? Are the `From #N` links real (the row genuinely answers, completes, or picks up the referenced row)? Bogus links mislead the assembly.

### Combination integrity check (hard rule)
For every suggested combination: does it open on an `Opener` (and if it opens on `Opener (needs early VO)`, is the VO **front-loaded**, not in the valley)? Does it close on a `Cliffhanger`? Is it 25-35% host? Does it ever place **two host rows consecutively**? Two-in-a-row is a defect; reorder or swap. Does it state its VO placement? Does it avoid stringing three unrelated cold starts in a row?

### VO placement check
Across the combinations, is more than one VO placement shown (not every one defaulting to the valley)? Is at least one front-loaded? Any combination opening on a setup opener must front-load its VO.

### Host presence check (hard rule)
Does the soundbite menu contain at least 5-6 host rows, including several host *questions* usable as openers/enders, so any sensible assembly can hit 25-35%? Are host rows clearly flagged so the user keeps them interleaved? A menu that can only be assembled into an all-guest supercut is a failure.

### Podcast branding check
Does every VO name the podcast aloud, using the reference file's canonical phrasing? If missing, add it.

### Em-dash check (hard rule)
String-search every VO for `—` and `–`. Replace with commas, periods, or colons.

### Banned phrases check
String-search every VO for: "masterclass", "shares his journey", "deep dive", "fascinating conversation", "incredible insights", "revolutionary", "groundbreaking", "game-changing". Rewrite in plain language.

### Tease specificity check
Could any VO tease paste onto a different guest? If yes, add specifics from the transcript/dossier.

### Edit-consistency check
If a cut list or scrubbing instruction was shared, does any soundbite or VO tease reference removed content? If yes, remove it and flag.

### Credibility signal check
Does each VO carry exactly one primary credibility signal (not a stack)? Trim to the strongest.

### Spoken-cadence check
Read each VO mentally. Stumbles, semicolons, comma-stuffed sentences? Break into shorter sentences.

### VO distinctness check
Do the 3-4 VOs foreground genuinely different territories, or are they reworded twins? If twins, re-angle one.

### Artifact check
Is the deliverable one self-contained HTML file (inline CSS/JS, no external requests, no localStorage), presented with `present_files`? Does it render soundbites as cards with a keep checkbox and a strike-out for rejects, a live host-ratio readout, a radio-style VO picker, and combinations as visual ordered strips (not arrow text) with VO placement shown? Does it include a **drag-to-reorder build tray** (with the VO as a draggable row) and an **export button that downloads a valid `.docx`** of the assembled cut plus a copy-as-text fallback? Did you test that the generated `.docx` actually opens (valid ZIP, correct CRC-32) before shipping? Is the chat message a sentence or two, not a restatement of the menu?

## Process summary

1. Identify the podcast; read its reference file (incl. trailer section).
2. Confirm a timestamped transcript exists. If not, ask for it. (Dossier is optional, VO-only.)
3. Mine the transcript for 18-22 verbatim candidates across the flavors, including at least 5-6 host lines (several of them questions), 3-4 openers (standalone and setup), and 3-4 cliffhangers (2-3 of them host questions), tracked separately.
4. Build the three menus: a 12-18 row soundbite menu (Role and Flow tags, including `Opener (needs early VO)`), a 3-4 VO menu in the short/blunt register, and a 3-4 combinations menu. Every combination opens on an opener, closes on a cliffhanger, sits at 25-35% host, never places two host rows back to back, states its VO placement (front-loaded / valley / split, not defaulting to valley), and chains linked rows where possible.
5. Self-audit every menu. Rewrite violations.
6. Output all three menus as one self-contained interactive HTML artifact (cards with keep/strike, live host ratio, radio VO picker, combinations as visual strips, a drag-to-reorder build tray, and a tested `.docx` export of the assembled cut), presented with present_files, plus a one-or-two-sentence chat note naming the strongest opener, the strongest cliffhanger, and the combination you would run. No preamble, no restating the menu in chat.
