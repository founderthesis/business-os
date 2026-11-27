---
name: guest-note
description: >-
  Generate the guest-facing note for a podcast: the one or two page document
  sent to a prospective guest to make them say yes. Covers the opening hook,
  what the show is, what we talk about, why come on (including reach and
  early guests where they are real), format and logistics, meet the host, and
  the closing call. Trigger on "/guest-note", "guest note for [show]", "make
  a guest note", "note to send prospective guests", "guest-facing one pager",
  or after a new show's positioning is settled, even without the word
  "skill". Ask for the show's format facts, host bio and reach figures if not
  supplied, and ALWAYS confirm two things before building: the real audience
  numbers, and whether the guest gets edit or approval rights, since both are
  promises the document makes on the host's behalf. Distinct from
  concept-note, which is the client-facing commercial proposal with pricing;
  this one has no pricing and is written to be forwarded to a stranger.
---

# Guest note

**un# only (decision 688):** for un#, the editorial direction below overrides this skill's un# notes.

## un# editorial direction (decision 688, Akshay for Sri, 27 Nov 2026). Read first: it overrides anything below.

un# is a show about onchain finance: traditional finance embracing new rails. aarnâ is moving in a regulated direction and un# supports that journey, so nothing Sri puts out on un# should make a regulator uncomfortable.

- **Words we never write** in anything published or read on air (titles, thumbnails, captions, posts, newsletters, show notes, trailers, intros, VO, dossier questions): "crypto", "DeFi", "Web3", "altcoin", "memecoin", "degen", "token launch". "DeFi" has a different vibe from where the show is going, so it goes too.
- **Words we use:** onchain finance, tokenization, real-world assets (RWAs), stablecoins, digital assets, onchain capital markets, programmable finance, settlement infrastructure. A named asset or protocol (Bitcoin, a stablecoin, a tokenized fund) can be named as a fact when the episode is about it.
- **The frame:** TradFi embracing onchain rails. Institutions, regulated products, market structure, compliance, capital formation. Not crypto insiders talking to crypto insiders.
- **Nothing a regulator would flinch at:** no price predictions or targets, no token promotion, no yield claims, nothing that reads as investment advice, no hype for unregistered products. A guest's market view is reported as theirs, never endorsed.
- **When a guest says "crypto" or "DeFi" on tape:** prefer bites and quotes that don't use the words; keep them only inside a verbatim quote whose point needs them; never carry them into a title, thumbnail, caption, overlay or summary line. Paraphrase in onchain terms.
- **Test before anything ships:** would a SEBI, RBI or MAS officer reading or hearing this be comfortable? If not, rewrite it.


The document a prospective guest reads before deciding whether to give up ninety
minutes. It is not a description of the show. It is an argument for being on it,
written so the guest can forward it to whoever asks them why they said yes.

Reference notes for what "good" looks like, all four finalised and in use:

- **Breakthrough Thesis** (Ankit Anand, Riceberg Ventures). The new-show case: no
  audience yet, so the host's credibility and the guest set carry everything.
- **Built to Share** (Satish Mugulavalli, Hissa Fund). Named early guests as
  social proof, and the strongest "what this episode is worth to you" section.
- **Human by Design** (Dr Arjun Jain, Fast Code AI). Numbered Next Steps, and
  the tightest host-credential block.
- **Playbooks by Prath** (Piyush Goenka, Prath Ventures). On-location format as
  the differentiator, and the fullest list of what gets published.

See `references/structure-and-examples.md` for the section-by-section spec with
the openings from all four.

## Phase 1: gather

Search project knowledge and any supplied transcripts for the show's positioning
before asking the user anything. What is needed:

- Show name, host name, host's day job, and what the show is about
- The host's credibility claim: the thing that makes them not a journalist
- Guest groups, and how they are qualified
- Themes, in the guest's language
- Format facts: recording length, published length, remote or in person, the
  platform used, cadence
- What the guest receives: video, clips, transcript, anything else
- Reach figures, if the show has any
- Named early or upcoming guests, if any
- Contact details and links

Ask only for what is genuinely missing after searching.

## Phase 2: confirm the two promises (HARD STOP)

The note makes two commitments on the host's behalf. Both get confirmed in chat
before anything is built, and neither is ever assumed.

1. **The reach figure.** Post what you have and ask the user to confirm it.
   Never invent, round up, or carry a number across from another show's note.
   If the show is new and has no audience, say so and confirm the note will omit
   the reach block entirely rather than soften it.

2. **Edit or approval rights.** Three positions exist across the network, and
   they contradict each other:
   - Founder Thesis: guests get no approval or editing rights, though they can
     suggest cuts
   - Built to Share: the guest reviews the edited episode before publication
   - Breakthrough Thesis: anything the guest would rather not have published is
     cut before release

   Ask which one applies. Getting this wrong creates a promise the host has to
   either honour or break.

Then stop and wait.

## Phase 3: build

Copy `references/build_guest_note.js` to /home/claude, fill it, run it, convert
to PDF, and look at every page before presenting.

## Document structure

1. **Banner**, full text width, once at the top. Never as a repeating page
   header: it prints on every page and eats the document.
2. **Title.** "[Show name]: Guest Note".
3. **The hook.** Two or three short paragraphs. See the opening rules below.
4. **What this is.** The show, the host, and who it is for. Two paragraphs.
5. **What we talk about.** The themes as bullets, in the guest's language, then
   one line on the posture: decisions rather than outcomes, no rigid script.
6. **Why come on.** The heart of the note. What the guest gets, made concrete.
   Include the reach block only if the numbers are real.
7. **Format and logistics.** Where, how long, on what platform, what to prepare,
   what they receive, and who controls the edit.
8. **Meet the host.** Photo beside text. The bio does one job: establish that
   this host is not a journalist and will understand the answer.
9. **Closing line.** One italic sentence, the actual call.

Order is not rigid. Put Meet the host before Why come on when the host's name is
the reason anyone would say yes.

## Opening rules

Every one of the four notes opens on a contrast or a premise, never a
description. That is the signature move and it is what stops the note reading
like a press release.

- "Most AI podcasts are hosted by journalists, investors, or founders who've
  never debugged a production model. This one isn't."
- "Most founders talk about their products, their funding rounds, and their
  growth metrics. The best founders talk about the people who made it all
  possible."
- "Playbooks aren't extracted in studios. So we come to you."
- "Every breakthrough technology spends years in a state where the science works
  and the product does not."

Write the hook last, once the rest of the note has told you what the show is
actually for.

## Editorial rules

- **Never invent reach.** No follower counts, download numbers, or audience
  figures that were not confirmed in Phase 2.
- **Never promise edit rights that were not confirmed.** Same for cross-promotion,
  turnaround times, or anything else the production team has to deliver.
- **A new show omits the reach block rather than hedging it.** "Growing audience"
  and "early but engaged" read as no audience, which is worse than silence.
  Lead on the host and the guest set instead.
- **Name early guests when they exist and have agreed.** It is the strongest
  social proof available to a show with no numbers, and it is what makes the
  fourth guest easier than the first.
- **Concrete over flattering.** "Clips optimized for LinkedIn, all yours to
  repurpose for recruiting" beats "great content for your brand".
- **No pricing, ever.** This document goes to guests. Pricing lives in the
  concept note.
- **Carry forward confidentiality constraints.** Check the discovery call and any
  recording transcript for figures the client asked to keep off the record.
  Standing example: Riceberg Ventures, where no AUM figure or fund target
  appears anywhere.
- **Describe what the host did, not the title they claim**, where the public
  record and the host's self-description disagree. Ankit describes himself as a
  Sleepiz co-founder; the public record lists him as VP of Software Engineering.
  The note says he helped build it and took it through FDA clearance, which is
  true either way and is the stronger claim.
- House voice: no em-dashes, no banned AI vocabulary, short varied paragraphs,
  contractions, specifics over generalities.

## Length

- **One page for a new show.** There is less to say and a stranger will read a
  page. Cut copy to fit rather than shrinking type.
- **Two pages once there is reach, a guest list, and a Next Steps block.**
- If the banner pushes it over, cut a line of copy. Do not shrink the banner
  into illegibility or drop the margins.

## Type and format

- 11pt minimum (docx `size: 22`) for body text, bullets and table cells. These
  get read on phones.
- Banner cropped to roughly 6:1. The supplied artwork usually has dead space
  above and below the type, and cropping it buys back half an inch.
- Host photo sits in a borderless two-column table beside the bio, not floated.

## Output

- One `.docx`, presented via `present_files`, plus a rendered PDF checked
  visually before presenting.
- Also deliver markdown when the note is going to be published as a web page.
  Three of the four live at a short URL: fscd.ai/note, unhashed.co/note,
  built2share.in/note.
