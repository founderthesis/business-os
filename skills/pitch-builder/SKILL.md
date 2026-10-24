---
name: "pitch-builder"
description: "Build the client-facing podcast-production pitch for any prospect, whether they have already bought the idea or still need convincing. Produces a published interactive HTML pitch page (with its own Word export) where the client picks working show names and guests and configures the budget in one live Investment table, plus the covering email. Trigger on /pitch-builder, \"build a pitch\", \"pitch for [company]\", \"concept note for [company]\", \"proposal doc for [company]\", or a prospect transcript pasted with pitch intent."
---

# Pitch builder

The one skill for every client-facing podcast-production document. It replaces the
old split between pitch-builder and concept-note, because those were the same
document at two moments in a deal.

**Rebuilt October 2026 from Akshay's review of the Drizz pitch.** The short version
of what changed, each one detailed where it applies below:

- The opener is four short paragraphs with one pitch: the podcast opens doors, and it
  builds the client's name because guests share their episode. Host named by name in
  the first line. The three-beat on-ramp and the pull-quote opener are gone.
- No cover strip under the title. No preamble above the roadmap.
- No themes section. "Working names" is a main heading, names carry their taglines.
- "What an episode is" is a broad conversation with the guest, never one number.
- Only Phase 1 names people. Phase 2 is guest profiles at mid-market companies and
  startups. Marquee names go in a Phase 3 dream list.
- "How we measure it" has no intro paragraph and no "titles are current" line.
- Investment and the estimator are one table with a live Estimate column.
- Why us opens on the numbers, then the origin paragraph, then show cards that
  name-drop guest companies in ⬩-separated phrases with a "Featuring..." label.
- Rate card: guest sourcing ₹15,000, content ops ₹15,000 a month, offline recording is
  post-production only, a new crew and studio rental line at actuals, the studio
  consult applies to remote hosts and we only introduce the consultant.
- Review gate after six published episodes, not four.

**Two deliverables: the page, and the email that carries it.**

An HTML page, published with the Artifact tool. The working show names and the
guests are pickable, each list with a box for the client to add their own. The
Investment section is one table: tick a line in or out and its Estimate column and
the subtotals update live. One button exports the whole pitch as a Word file carrying what
they chose and the budget they configured.

**Do not build a standalone Word document unless the user asks for one.** The page
was shipping alongside a separately built docx, and across a six-round run that docx
was rebuilt six times and never used. The page's own export is strictly better: it
carries the guests the client kept and the budget they configured, which a statically
built file cannot. `build_concept_note.js` stays in the references for the case where
a forwardable file is needed before the client has touched the page, and that case is
rare enough to be a decision rather than a default.

The typical workflow: call with the prospect, upload the transcript to a new chat,
run this skill, send both links. What changes between deals is how hard the
document has to argue for the idea before it reaches the price.

## The files

| File | What it is | When to read it |
|---|---|---|
| `references/pricing-defaults.md` | The rate card. The only source of pricing | Phase 3, always |
| `references/editorial-rules.md` | Editorial rules, the opener, what an episode is, naming, voice, design tokens, the HTML spec, the checklist | Phase 5, before writing, and again before presenting |
| `references/build_concept_note.js` | The standalone Word build. Optional, off by default | Only when the user asks for a separate docx |
| `references/build_pitch_page.html` | The canonical HTML page build, rebuilt from the Drizz pitch (October 2026). A complete HTML document; its PITCH object carries Drizz as the worked example | Phase 5 |
| `references/credentials.md` | The body of work: the four shows, the verified stats, the guest names. The only source for all three credibility placements | Phase 5, always |
| `references/naming.md` | How to name the show. The four tests, the shapes that work, the shapes rejected in live pitches, and the generation procedure | Phase 5, before writing any working name |
| `references/benchmark-ixr-pitch.md` | A real approved pitch, kept for voice only. Its structure is out of date and the file says so | Phase 5, optional |

This file carries the process and the section order. Everything about how the
writing and the design have to behave lives in `editorial-rules.md`. Do not
reconstruct a rule from memory when the file is right there.

## What the user gives you

- A transcript of a conversation with the prospect: a discovery or sales call, or a
  recorded guest interview where the pitch came up.
- Sometimes also their website, deck, or numbers they shared.
- Sometimes an earlier pitch document, for this client or another one, handed over
  as the design to follow. See **Working from a supplied reference file** below.

If no transcript is present in the conversation, uploads or project, go and look for
one per Phase 0 before asking. Do not invent what a client said.

## How it runs

Six phases and three hard stops: the subject, pricing, and the guest gate. Do not
skip a stop because the answer seems obvious. The subject stop is the newest and the
most expensive to skip: a run that reached a finished six-page document three times
on a subject the client had not agreed to is what put it there.

---

### Phase 0. Stage and sources

Ask three questions before anything else, with AskUserQuestion. They decide the
shape of the whole document.

**1. Where is this deal?**

- **Already sold on the idea.** They want a podcast and are choosing a producer, or
  the shape is agreed and this is the paperwork. Route A.
- **Still selling the idea.** They have not decided a podcast is worth doing, or
  someone floated it and nobody has run at it. Route B.

**2. What is this show about, and what does the client want it to do for them?**
Free text. Ask it even when a transcript is in hand, because a call rarely settles it
and research never does.

This is the most important question in the skill. The guest list is called the thing
that wins the deal, and it is, but the guest list is downstream: every angle under
every name is a function of the subject. In the run that produced this rule the guest
list was stable from the third version onward while the subject moved four times, and
each move meant rewriting twenty-one angles.

**The subject belongs to the guest's world, not the client's product.** This is the
single most important rule in the skill and the easiest one to break, because the
client will hand you the other answer. Full spec in `editorial-rules.md` under "What
the show is about". The short version:

- The show exists to get the client in the room with the people they sell to. That is
  the whole product. Not audience, not awareness, and above all not evangelism.
- So the subject is a question the ICP argues about among themselves, and it is worth
  an hour of a senior person's time whether or not the client exists.
- The client's product, category and worldview never set the agenda. A show that
  educates the market about the problem the client happens to solve is a webinar with
  better lighting, and the guests who matter can smell it in the invitation.

Take whatever the user gives you, even a rough sentence, then **test it against that
rule before writing it down.** Clients hand over a category brief almost every time,
because it is the obvious answer and it is what their marketing team would say. Where
the answer they give is about their own product, say so plainly in chat and offer two
subjects drawn from the ICP's world instead. If they do not know, offer two or three
from Phase 1 research and get one chosen.

**3. What are we working from?** Multi-select: a discovery or sales call transcript,
a recorded podcast interview with them, a website or deck, notes, nothing yet.

**Then go and find the transcripts yourself, before asking for them.** What the
prospect said on a call beats anything on their website, and there is usually a
transcript sitting in Drive that nobody remembers. Search Google Drive by both the
person and the company, because meeting notes get filed under either:

```
title contains '<person first name>' or title contains '<company>'
fullText contains '<person full name>' or fullText contains '<company>'
```

Run the title search first, then the fullText one, and widen with `modifiedTime >`
the last six months if the results are noisy. Meeting-notes files are usually named
for the call or carry "Notes by Gemini", "transcript", or "Meeting started". Check
the project docs too. Read what you find rather than skimming the file names.

Then ask, in one line, for the thing you cannot find yourself: **is there a podcast
interview with this person, on Founder Thesis or anyone else's show?** An hour of
them talking about their own business is the richest input this skill can get. It
gives you their own words on the buying problem, the objections they hear and the
people they name, and those quotes are what make the pitch sound like it was
written by someone who was in the room. Ask for the transcript or the episode link.

Say in chat what you found and what you are missing, then carry on. A pitch built
with no transcript at all is possible but weaker, and the user should know which one
they are getting.

If the stage is ambiguous, ask rather than guess. A Route A document sent to a
Route B prospect reads as presumptuous. A Route B document sent to a converted
client wastes two pages telling them what they already believe.

**The subject stop.** Before Phase 2a fans out a single subagent, write the subject
back in one sentence, in the shape the show would actually carry: who it is for, what
it is about, and what it does for the client. One line, not a paragraph. Then get a
yes.

> The show for people who run route-to-market in fragmented retail across India,
> South East Asia and Africa. It makes [Client] the company that convenes that room.

Note what that sentence does not contain: the client's product, their category, or
anything they would like the market to believe. It names a job other people do, and
the client's return is that they are the ones holding the microphone.

**Run the guest test on it before you send it.** Would a senior person in that world
agree to an hour on this subject if the client did not exist? Would they watch someone
else's episode? Two noes means the subject is a category brief wearing a disguise, and
the fix is to go back to what the ICP argues about among themselves rather than to
reword it.

Nothing downstream survives this being wrong, so it is cheaper to spend a message
here than to rewrite a guest list. If the user is not sure yet, propose two subjects
after the Phase 1 read-back and make them pick before the fan-out.

---

### Phase 1. Orientation research

Before any research prompt, spend four to six web searches working out what the
company actually sells and to whom. Get this wrong and everything downstream is
wrong.

Pull out:

- **What they sell, in plain words.** Not their marketing line. What the product
  does and what category it sits in. Check it against the transcript. If a founder
  says on tape "we are not X, we connect to X", that is load-bearing: a document
  that frames the show around X will be rejected outright.
- **The deal size or price point**, if it came up.
- **The ICP, named precisely.** University deans and medical directors. Heads of tax
  at multinationals. Revenue and data leaders at high-volume consumer businesses.
  This is the single most important extraction, because it drives the research, the
  guest list and the concept. This group is what "cohort" means everywhere in this
  skill except the pricing file, where it means a batch of episodes.
- **Where the ICP sits geographically.** A founder selling into the United States
  from Bangalore will describe an Indian cohort out of habit. Check the customer
  page, the careers page and the case studies for where the revenue actually is, and
  say in the read-back which regions the guest list should span. An all-India guest
  list for a company selling to American retail is the fastest way to lose the room.
  Every name in the list carries a region tag, so a lopsided list is visible at a
  glance rather than buried in the companies.
- **The buying committee, if it is more than one person.** Who wants it, who has the
  concerns, who carries the decision. Founders describe this vividly when asked why
  deals stall, and it is usually the sharpest thing in the transcript. Also ask who
  has actually championed a win: founders name those people, and they belong at the
  top of the guest list.
- **Their goals and frustrations, in their own words.** Quote them back later.
- **Whether they run a show now, ran one before, or own a show name.** All three
  matter and the last two are easy to miss. A currently running show turns the
  document into production-as-a-service rather than "start a podcast". A **lapsed**
  show is better than either: it makes this a relaunch with an archive behind it,
  which is a materially easier first ask for a guest, and its old episodes are a
  list of people who have already said yes to this company. A show name the client
  already owns settles the naming section in one line. Search their site for an
  interview series, a webinar series and a podcast page, including on old or
  alternate domains, not just the current marketing site.
- **Any names, numbers or peers they mention.**

**Then mine their public customer page.** This is mandatory and it is the highest
yield step in the whole skill. Fetch the prospect's customers, testimonials, case
studies, advisory and logo pages, plus the archive of any show they have run
themselves. These people already vouch for the product in public, so they are the
warmest possible guest list, and almost no prospect thinks of them that way.

**Mine it for companies, then find the person.** A name sitting in a vendor
testimonial is the warmest lead and the weakest source: testimonial bands go stale,
carry titles nobody re-checks, and in practice most of those names cannot be
confirmed against anything the person's own employer publishes. So take the company
from the testimonial and find the current senior executive on that company's own
leadership page. That swap is usually an upgrade in seniority as well as in accuracy:
a mid-level manager quoted in a testimonial becomes the company's actual chief
information and digital officer, confirmed on their own site. Note which of them are
technical leaders: those are usually the people who championed adoption inside their
own company, which is the story the show exists to tell. Keep the URL for every name:
it becomes the Source link on the page.

**Count what you actually found and do not round it up.** If the customer page names
five people and the roadmap wants six, the sixth is an honest placeholder, "one from
the founder's own network, named together before launch", not an invented name. A
single fabricated guest costs the whole list its credibility.

Give the user a short read-back: who the prospect is, what they sell, the cohort,
where that cohort sits, the committee shape, the goal, whether they run or have run
a show, and the named people found on their customer page and their own archive. A
few lines, so it can be corrected before research runs.

**Propose the guest buckets in the read-back, and derive them from this prospect.**
Three buckets, each named after what those people do inside a company that buys this
product, taken from the buying committee you just extracted. One line per bucket on
why that group is in the room for this specific sale. Then ask whether the buckets
are right before any subagent goes looking for names, because a search against the
wrong buckets wastes the whole of Phase 2a.

**Never carry buckets over from a previous client.** Revenue leaders, CTOs and heads
of data are the right answer for a company selling analytics to consumer businesses
and the wrong answer for almost everything else. A fund sells to founders, LPs and
co-investors. A compliance product sells to a head of tax, an internal audit lead
and a CFO. A training product sells to deans and heads of department. If the buckets
you are about to write are the ones from the last pitch you built, you have stopped
thinking about this prospect.

**Weight the buckets toward whoever the document calls the champion.** The list has
to agree with the argument above it. A pitch that names commercial leaders as the
people who champion the purchase, and then fills eleven of eighteen slots with
technology and data leaders, is arguing against itself in its own most persuasive
section. Roughly:

- **Sixty per cent, the champion function.** The people the document says carry the
  purchase internally. Nobody else is making a show for them, which is also why they
  say yes.
- **Twenty per cent, the function that holds the architecture or the veto.** Real
  buyers, and already drowning in vendor podcast invitations.
- **Twenty per cent, outside voices.** Academics, analysts, distributors, operators
  at adjacent companies, recently retired executives. They are what make it an
  industry show rather than a customer series, and they are the easiest yeses in the
  whole list.

Check the split before the fan-out and say it in the read-back. Getting it wrong is
not a research failure, it is a brief failure, and it costs a full round of names.

---

### Phase 2. Research

Research splits in two and both halves run the same way: your own subagents, fanned
out in parallel, no external round trip and no stop. Run 2a and 2b together. The
subject is already agreed by this point, which is what makes the angles worth
writing.

**2a. Guest names and profiles: run this yourself, with parallel subagents.**

What the page needs from this search changed in October 2026. **Named people are
needed for Phase 1** (people who already know the client) **and for the Phase 3 dream
list** (the marquee names). **Phase 2 shows guest profiles, not names**: a role at a
kind of company, with stage, sector and region ("Heads of mobile and VPs of
engineering at growth-stage US consumer apps, Series B to D"). Akshay's read on the
Drizz list: Uber and Capital One in episodes 7 to 14 is too ambitious, and a founder
who sees it stops believing the roadmap. Still run the name hunt for the Phase 2
buckets, because the verified names become the internal booking list and tell you
which profiles are real, but the names stay in chat and in the tracker, not on the
page. The biggest names you find move to the dream list.

Do not wait for a deep research round trip to produce the guest list. It comes back
slow, regionally lopsided, and with titles that are two jobs stale. Instead, fan out
general-purpose subagents, split by region rather than by role, and give each the
same brief: the ICP definition, the buckets confirmed in the read-back, how many
names per bucket, and the instruction to verify every current title against a primary source,
which means the company's own leadership page, the person's own profile, or a dated
press release.

A sensible split for a company selling globally is one agent for the Americas, one
for Europe, the United Kingdom, the Middle East and Africa, and one for India and
South East Asia. Ask each for more names than you need, because the verification
gate will kill some.

Ask each subagent for two more things per name: **the URL it verified the title
against**, which becomes the Source link on the page, and **a single sentence on the
episode angle**, meaning the specific thing that person could talk about for an hour
that serves the show's subject. Without the angle the list is a directory. With it,
the client can see the show rather than the seniority.

Tell each subagent to exclude anyone employed by a direct competitor, and to flag any
candidate who has already appeared on a competitor's own show. Booking someone second
is a weaker episode, and it is cheaper to learn that here than at the gate.

The deep research prompt asks for names too, in its section 6. **That is a pool of
leads, not a second opinion, and it is the weaker pool.** In practice those names
fail verification far more often than the subagents' do, and they fail in the ways
that are hardest to catch: right person, wrong employer; right title, wrong country;
a role that ended a year ago; a name whose only trace is a conference bio. Merge the
two lists, drop the duplicates, and keep the subagent's title wherever the two
disagree, because that one was verified against a primary source. Every name from
either pool still goes through the verification gate before it reaches the document,
and budget for most of the research tool's names not surviving it.

**2b. The cohort's world: same fan-out, no round trip.**

The rest of the research is about the world the cohort lives in, and it used to go
out as a nine-section prompt for an external deep research tool, followed by a hard
stop while it ran. That is gone. The names it returned were the weaker pool, the
round trip cost a session, and in the run that retired it the prompt was skipped
entirely with nothing lost: parallel agents covered the same ground with better
titles. Send the same questions to your own subagents alongside the name hunt, and
keep going.

Brief them on four things, in this order of value:

1. **The objections that stall this sale, in a buyer's own voice.** The standard
   reasons a buyer in this category says no or delays, and then real buyers and
   practitioners saying those things in their own words, from podcast transcripts,
   conference talks, forum threads, review sites and LinkedIn comments. Verbatim
   wording matters more than paraphrase: the sales team reuses these sentences, and a
   peer's phrasing carries weight a marketing summary does not. This is the single
   highest-value pull, and it feeds two sections.
2. **Competing and adjacent shows, and who appears on them.** Which podcasts already
   target this cohort, run by competitors, adjacent vendors or independently: the
   host, the format, the cadence, and any reported results. Then the guests from the
   last eighteen months, because those are proven willing podcast guests. Flag anyone
   whose employer is a competitor's publicly branded showcase customer.
3. **Test the cohort definition.** In this category, who actually signs, who holds
   the budget, and who can kill the deal? Say plainly if the founder's account of
   their own buyer looks wrong or incomplete, and what the evidence is. Expect this
   to widen the committee rather than replace it: the real internal champion is often
   a level below the person the founder named, and there is usually a finance or
   operations seat with a veto that never came up on the call. If it contradicts the
   founder, that goes to the user in chat as a question, never silently into the
   document.
4. **What the cohort actually consumes, and category precedent.** Beyond vendor
   shows: the podcasts, newsletters and events, and whose opinion moves them. Plus
   verifiable examples of B2B companies that defined a category, and what role owned
   media played.

Every fact comes back with a link. Nothing from this pool goes into the document
unsourced, and no name from it skips the guest gate.

---

### Phase 3. Pricing gate (HARD STOP)

Pricing is dynamic and is never assumed. Read `references/pricing-defaults.md`. That
file is the rate card. If it cannot be read, say so and ask the user to paste the
current rates. Never reconstruct pricing from meeting notes, internal call
transcripts, or a previous client's document. Meeting notes are a draft of a
decision, not the decision, and reconstructing from them has produced wrong figures
before.

**First, check whether the client already has numbers in hand.** Search the project,
the transcripts and the uploads for an earlier proposal, quote or costing sheet sent
to this prospect. On a Route A deal there usually is one, and the rate card will have
moved since. If one exists, put a second table in the gate listing every line where
the old quote and the current card disagree, in both directions, and say who has
already seen the old numbers. A client whose colleague reviewed and approved a figure
last month will notice a silent change, and the fix is a sentence in the covering note
rather than a discovered discrepancy. Say plainly whether the net effect on a
realistic episode batch is up, down or roughly neutral.

Post the current card in chat as a table with the default Recommended and Optional
tags, then ask the user to confirm or change, for this client:

- the rates and any tier changes,
- what the one-time setup covers,
- which lines are Recommended, which are Optional, which are core and untagged,
- whether any line should be dropped,
- how many episodes the estimator should default to, and how many guests the client
  expects to introduce.

Then STOP and wait. "Use standard" means proceed with the defaults.

**Drop lines that do not apply rather than reframing them.** The studio setup consult
is the exception: it applies to every show, remote hosts included, so it stays on
every pitch (October 2026). Crew, equipment and studio rental is a separate
third-party line at actuals, off by default, for in-person recordings only.

**Watch the tier.** The card carries a standard tier, and some deals price above it.
Large contract values, a cold guest list that needs real outreach, or a host in a
distant time zone are all reasons to raise the guest sourcing line and the setup
fee. Raise it in this gate, with the user, never silently in the document. A client
who has already reviewed an older quote is the one case where an uplift costs more
than it earns, so offer it and let the user decline.

The rest of the pricing rules, including how concessions are written and how
sourcing is computed, are in `pricing-defaults.md` under "Rules for applying the
card". Read them there rather than from memory.

---

### Phase 4. Verification and the guest gate (HARD STOP)

Two halves. Verify on your own, then put the list in front of the user and wait.

**4a. Verify.** Run this before writing a word of the document, and report the
result in chat. Research returns confident, stale titles, and a wrong title in a
guest list destroys the one thing the list exists to
prove, which is that you know this world. Fan the re-verification out to subagents
the same way Phase 2a did, one agent per group of names, so it costs a single round
trip rather than thirty searches.

- **Re-verify every named person** with a fresh search: current role, current
  company, and whether a merger, acquisition or move has changed the title. Check
  the person, not just the company, and check the company name too: renames and
  acquisitions mean the employer on the research note may no longer exist.
- **Keep the URL that confirmed each title.** It becomes the Source link on the page,
  and a list where every name links to the page that proves it is the strongest
  credibility signal in the document.
- **A company's own leadership page is necessary, not sufficient.** It is the best
  source available and it still goes stale in the most damaging direction: pages have
  listed an executive who retired weeks earlier, with no successor named. Where a
  name matters, look for a dated appointment or departure notice as well.
- **A page that contradicts itself is a hold, not a coin flip.** If a leadership page
  names two different people in the same role, or the title differs from the person's
  own profile, do not pick the likelier one. Say so in chat and either get it
  confirmed or drop the name. There is almost always a second person at that company
  who is cleaner and often a better guest.
- **Drop anyone you cannot confirm**, or demote them to a role description. A name
  whose only source is the client's own testimonial band, a data broker, or a
  conference bio older than eighteen months is not confirmed.
- **Report what changed** in chat, with counts: how many checked, how many killed,
  how many corrected, and the specific corrections. The corrections are the proof the
  gate did work, and they stop the user assuming it was a formality.
- **Check the geographic spread** against what Phase 1 found. If every name in a
  bucket is from one country and the cohort is global, the bucket is not finished.
- **Check the internal consistency of the guest list** against any rule the document
  plans to state. A list that contains a competitor under a blanket no-competitors
  rule is the kind of contradiction a client spots in thirty seconds and then
  distrusts the whole document for.
- **Flag competitor reference accounts to the user, in chat.** A guest can be
  personally clean while their employer is a competitor's publicly branded showcase
  customer. That is not a reason to cut the name, but it is the client's call to make
  knowingly rather than yours to make silently.
- **Where a bucket cannot be filled with verified names, say so and leave an honest
  placeholder.** Some regions and some functions are simply not published: data
  leaders outside the United States and Europe are the recurring example. One named
  placeholder in a bucket reads as rigour. One invented name costs the list.

**4b. The guest gate. Show the list, then STOP.**

Post the whole list in chat: Phase 1 names, the Phase 2 profiles per bucket (with
the verified names behind each profile listed underneath for the user's eyes only),
and the dream list. One line each: name or profile, role and company, region, and the
episode angle in a few words. Compact enough to read in
thirty seconds. Then ask four things and wait:

- Are these the right buckets for this prospect, or has the research moved them?
- Does anyone here not belong, and is anyone obvious missing?
- Is the regional spread right for where this company actually sells?
- Anyone the user knows personally, or knows is unreachable, which changes the phase
  they sit in.

**Why this stop exists.** The guest list is the most persuasive part of the document
and the easiest thing to get subtly wrong, because the names look plausible whether
or not they are the right names. Left alone, a run of this skill drifts toward the
shape of whichever pitch it saw last: the same three buckets, the same seniority
mix, the same regions. The user knows this market and can spot a wrong list in ten
seconds, which is cheaper than finding out from the client. So the list is a
proposal until they say otherwise, however well the research went.

Then STOP and wait. "Looks good" means proceed.

---

### Phase 5. Build

**Read `references/editorial-rules.md` first, in full.** It carries the rules, the
voice, the design tokens and the checklist, and the build file assumes it. The section
that governs everything else is **"What the show is about"**: the show belongs to the
guest's world rather than the client's product, because what the client is buying is
the room, not an audience and certainly not a platform for evangelism. If the subject,
the name or the episode framing drifted toward the client's category during
research, this is where it gets caught. Three more sections decide how the front half
reads: "The opener", because a long opener loses the reader before the pitch lands;
"One listener, one arena", because a show for four audiences is a show for none; and
"Naming the show", because a name that restates the client's positioning is the
fastest way to make the document sound like marketing.

Then read the research for five things: the objections in a buyer's own words, the
competing shows and who appears on them, the named guests and their angles, the
category precedent, and where the research disagreed with the founder.

**Read `references/credentials.md` too.** It carries the four shows, their verified
numbers, the guest companies for the show cards and the origin paragraph, and it is
the only source for the Why us section, now the only credibility placement. If a figure it wants is missing or marked stale, ask rather than estimating:
the section that proves we can be trusted with numbers is a poor place to guess one.
It also lists the guest names that get misspelled, which is the most expensive typo
in the document.

**Read `references/naming.md` before writing a single working name.** The show belongs
to the guest's profession, not to the client's product, and three consecutive pitches
shipped names that broke that rule. The file carries the four tests, the shapes that
work, and the names rejected in live pitches with the reasons.

Build order:

1. Write the copy in chat so the user can react.
2. Copy `references/build_pitch_page.html`, fill the content into the `PITCH` data
   object (it carries Drizz as the worked example: replace everything), and publish it
   with the Artifact tool. Call the Artifact tool with action "capabilities" first and
   declare `{"downloads": true}`. The file is a complete HTML document with a doctype,
   which publish requires. Do not hand-edit the markup: every section renders from `PITCH`, which
   is what keeps the page and its export from disagreeing.
3. Open the published page and check it before saying it is ready: every list marks
   and clears, the add-your-own boxes save, the Estimate column and subtotals move
   when a line is ticked or the introduces counter changes, and the export produces a file.
4. Write the covering email in chat, with the page link in it.

A standalone Word document is not part of this. If the user asks for one, copy
`references/build_concept_note.js`, fill it the same way, build, render the PDF and
look at every page. Do not write markdown and convert it with pandoc: the tables, the
shaded band rows and the tags will not survive.

**Then write the covering email.** The pitch never travels alone. Every run ends with
the email that carries the link, in chat, as plain text ready to paste into Gmail.
Six or seven short paragraphs, spec in `editorial-rules.md` under "The covering
email". The one piece of real work in it is the reference podcast, which comes from
the competing and adjacent shows found in Phase 2b and has to be a show aimed at this
prospect's own market. It is what makes a podcast feel like a normal thing companies
in their category already do.

Do not put pricing, guest names or the show's direction in the email. All three live behind the
link, and an email that summarises the document gives the reader a reason not to open
it.

If the user keeps a CRM row or a Notion board for the prospect, record the artifact
URL there.

**Discard what does not serve the argument.** Research wanders. Drop anything
off-target, and never use a vendor's own marketing case-study numbers however
conveniently they fit. If the research contradicts something the prospect claimed,
flag it to the user rather than repeating it in the document.

Run the checklist at the end of `editorial-rules.md` before presenting.

---

## Working from a supplied reference file

Sometimes the user hands over a previous pitch, usually an HTML page built for
another client, and says to use it. Treat that file as the design, not as a
suggestion: copy it and replace its content, rather than rebuilding from
`build_pitch_page.html` and approximating the look. They chose that file because they
have already sold from it.

Three things to get right when tailoring one:

- **Re-check the section set against the new deal.** A Route B file opens with the
  access argument and no Overview. Retargeted at a Route A client, that argues for
  something they already believe, so the opener becomes a short Overview and the
  kicker changes. Sections the old client did not need may now apply, and the
  reverse: a studio line belongs in the rate table only if this client has a studio.
- **Carry the editorial fixes across.** An older file predates rules that have since
  been written down. Sweep it for the ones that matter, especially any line that
  argues against part of what is being sold. Fix them while tailoring and say in chat
  which lines you changed and why, rather than porting them forward silently.
- **Test it in a browser before delivering.** A standalone file does not run inside
  the Artifact runtime, so a call to `claude.use("downloads")` fails silently. Wrap
  it so it tries the runtime first and falls back to an anchor download, then open
  the file and confirm the guest rows, the add-your-own boxes, the Investment totals
  and the console are all clean.

---

## The section order, and where the two routes differ

Both routes run the same sections in the same order. Only the first block changes.

1. **Cover.** Route A: title "[Show name] by [Client]", kicker "CONCEPT NOTE", a
   one-line italic subtitle carrying the show's promise. Route B: kicker "PITCH NOTE",
   title "A podcast for [Client]". Accent rule. **No credibility strip under the
   title** (cut October 2026).
2. **The opener.** Four short paragraphs, roughly 75 to 90 words: the proposal with
   the host named by name, it opens doors, it builds the client's name because guests
   share their episode, ownership. Spec and the Drizz worked example in
   `editorial-rules.md` under "The opener". Route A runs one line plus a short
   Overview instead.
3. **Who it is for.** Audience groups as boxes, one card per group, no ticks or
   crosses. Name the one listener first, say which group are the buyers. State that
   the client approves every guest.
4. **Working names.** A main section heading. Three names per `references/naming.md`,
   each with its tagline (the sub line) and one line on what it promises a listener,
   pickable, with an add-your-own box. Where the name is already settled, drop this
   section and carry one italic line that the name is a working title.
5. **What an episode is.** One line of framing, a short list of the ground a
   conversation covers (career path, what worked, mistakes, their take on the
   subject, how they have changed this year), then the prep-document line.
6. **The roadmap.** Opens straight on Phase 0, no preamble. Phase 0 (including
   episode zero), Phase 1 named, Phase 2 profiles, Phase 3 dream list, then "How we
   measure it" with no intro paragraph. See below.
7. **What one recording becomes.** The three-by-four grid.
8. **What the sales team can use.** Four bullets. Spec in `editorial-rules.md`.
9. **Investment.** ONE table: tick, item and tag, rate, what it covers, live Estimate
   with the working shown, a subtotal per group. Presets (6 and 12 months) above it,
   the introduces counter under Guest sourcing, the in-person counter under Offline
   recording. Then the out-of-scope line. No separate estimator section.
10. **What we need from [Client].** From the host, and from the team.
11. **Why us.** The five-figure numbers band, the origin paragraph, then four show
    cards, each a "Featuring..." label and a ⬩-separated line of guest companies, then
    the time commitment and the link. Spec in `editorial-rules.md`.
12. **Closing line.** One quiet italic sentence.

### Route A: the idea is already sold

Kicker "CONCEPT NOTE". One line on where this came from and what was agreed, then a
short Overview: what the show is, the commercial point, the ownership line. Sourced
from the transcript, never assumed.

### Route B: the idea still needs selling

Kicker "PITCH NOTE", no subtitle. The opener does the selling in four short
paragraphs and nothing more. The buying committee, why their current channel tops
out, and the comms-team argument are real and useful, but they belong in the
conversation, the sales section or the email, not stacked above the fold. The Drizz
draft opened with six paragraphs and about 270 words before the reader reached
anything to react to, and the review cut it to a third.

---

## Constructing the guest roadmap

Route B lives or dies here. A category description persuades nobody. Real people at
real companies make the whole thing concrete in ten seconds.

**Phases, not tiers.** An earlier version of this skill tiered the list by warmth and
led with the client's existing customers. That defeats the argument the pitch is
making. If the first tier is people who already know the client, the reader concludes
the show reaches nobody new, and the access promise collapses on its own first page.
Phases fix it by tying the same ordering to episode numbers, so the existing network
reads as a launch mechanism rather than as the audience.

- **Phase 0. Setup.** The first fortnight, as labelled rows: positioning and name,
  the set and format, **episode zero** (Akshay interviews the host about how the
  company was built, so the feed launches with an episode and every invitation has a
  format demo; a recent Founder Thesis episode with the founder can serve), the
  outreach engine, and the first bookings.
- **Phase 1. Episodes 1 to 6. People who already know [Client]. NAMED.** Named
  individuals from their customer, testimonial and case-study pages, the founders'
  former employers, and investors' networks. Six slots; where fewer verify, an honest
  "named with the founders before launch" slot. Frame it honestly: the fastest
  bookings, and what makes the cold list possible.
- **Phase 2. Episodes 7 to 14. The people [Client] wants to work with. PROFILES, NOT
  NAMES.** Three buckets named after what those people do inside a buying company,
  derived from this prospect's own committee. Each bucket carries two to five guest
  profiles: a role, a kind of company (stage, sector), a region pill, and one line on
  the episode angle. Aim at **mid-market companies and startups**, weighted to the
  regions agreed in Phase 1. Close the phase blurb with one line that names get drawn
  up with the client once the first six episodes are out. **Why:** in the Drizz
  review, Uber, Capital One and Airbnb in episodes 7 to 14 read as too ambitious. A
  show with six episodes books the director at a Series C app, not the principal
  engineer at Uber, and a list that claims otherwise costs the roadmap its
  credibility.
- **Phase 3. Episode 15 onward. The dream list. NAMED.** The marquee names:
  household-name companies, category authors, the people a founder would be proud to
  have on. Verified like every other name, each with an angle and a Source link. Say
  in the blurb that by this point guests introduce the next guests (the last beat of
  every episode is the guest naming the next one) and that the review gate sits
  behind this decision.
- **How we measure it.** Closes the roadmap, because a promise about the future
  belongs next to the numbers that test it. Four numbered rows, spec in
  `editorial-rules.md`.

Rules for the list:

- **Every name is verified at build time**, per the verification gate. No "titles
  are current as of..." line on the page (cut October 2026), and no verification date
  against each name.
- **Check every cold name for a warm path before calling it cold.** A target account
  is often already a customer, a partner, or named on the client's own logo wall, and
  a name presented as a cold conquest that turns out to be an existing account makes
  the whole list look unresearched. Run the Phase 2 names back against the customer
  page, the case studies and anything the founder listed, and move the hits into the
  phase they belong in.
- **The guest's comms team is a real gate on a vendor's show.** At a multinational, a
  senior executive's appearance gets screened, and "a podcast run by a vendor we buy
  from" is a fast no. Two things change that, and both belong in the document: the
  show is branded as an industry show presented by the client rather than the client's
  own show, and product stays off the air. Say the first in the opener and the second
  in what the host gets asked for.
- **Four fields per name.** The name, the role and company, a short region tag, and
  one sentence on why them, which is the episode angle from Phase 2a. On the page the
  region is a pill beside the name and the angle carries a Source link to the page the
  title was verified against. The optional Word build takes the same four fields, with
  the region in brackets after the role, so the two cannot drift.
- **The angle is a function of the subject, so it is the cheap thing to rewrite.**
  When the subject moves, the names usually survive and every angle has to change.
  Rewrite the angles, keep the list, and say in chat that is what you did. This is
  why the subject is settled in Phase 0: twenty-one angles is an afternoon, and it is
  an afternoon nobody should spend twice.
- **The page's guest rows are tri-state and start unmarked.** A tick and a cross on
  every row. Unmarked exports as kept, the cross removes the name, and a tick
  shortlists it: once any name in a bucket is ticked, the export carries only the
  ticked ones from that bucket. The working names and the Phase 2 profiles behave identically,
  because all three are the same component. The full spec is in
  `editorial-rules.md`.
- **Every bucket on the page ends with an add-your-own-names box**, and what the
  client types there exports as an extra name flagged as theirs. Say so in the roadmap
  intro, in one clause, so they know they can add to the list rather than only prune
  it.
- **Where there is no verified name, say so in the slot.** "One from the AppDynamics
  network, named with [founder] before launch, to confirm" is honest and costs
  nothing. An invented name costs the document. The build files take `null` for the
  name and render the slot in italics.
- **No blanket competitor ban.** Stating one and then listing a competitor is a
  self-inflicted contradiction, and the rule is unenforceable anyway. Write instead
  that the client signs off on every guest and that anyone with product overlap is
  their call.
- **Guests are never called clients.** Never "our clients", never "trusted by". They
  are people the client would invite. The client's own story is told separately.

---

## Three things that do not go in the document

All three come up in the call, all three feel like they belong, and all three are
worse on the page than in the conversation.

**A kill criterion.** Founders ask what the cut-off is for stopping, and they ask
because they have to defend the spend to a co-founder or a board. Answer it in chat,
fully and specifically. Do not write it into the pitch: a clause about when to
abandon the show reads as an exit clause in a document whose job is to start one, and
the client will strike it. The review gate after the first six published episodes is
already in the roadmap and carries the same meaning without the framing.

**A recital of the client's own business.** No stat strip of their numbers, no list of
their customers, no explanation of what their product does. They know. The space
belongs to what they still have to decide. Route B's opener describes their buying
problem, which is the opposite of this: it proves you listened.

**Pass marks on the review gate.** The gate after the first six published episodes
needs numbers behind it, and you should have them: the accept rate on cold invites to
target profiles, introductions made by the first six guests, inbound guest requests,
follow-ups the account owner opened, the share of engagement coming from target
accounts or roles, and how many sellers are sharing tracked links. Work them out and
give them to the user in chat, with a decision rule: most of them met, commission the
next block; about half, fix format or targeting and recheck at episode ten; almost
none, stop.

Keep all of it out of the pitch, for the same reason as the kill criterion. A table of
pass marks in a document whose job is to start something reads as the terms on which
it gets cancelled, and it commits to a bar before anyone knows what normal looks like
for this show. The document names the gate and says what gets measured. The numbers
belong in the conversation where they can be argued with.
