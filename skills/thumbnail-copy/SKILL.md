---
name: "thumbnail-copy"
description: "Build the thumbnail brief for a podcast episode as a published HTML artifact: thumbnail + episode title combos shown at real browse size, a legibility strip, collapsed context, colour-coded guardrails, and a pick-and-export flow that saves the designer's chosen combos as a Word (.docx) file. Trigger on /thumb."
---

# Thumbnail Brief

Build the brief a designer works from to make a thumbnail **without having watched the episode**. The designer is not the bottleneck; the missing context is. This skill manufactures that context from the transcript, then hands her a menu wide enough to have a real opinion about.

**Every option is a combo: thumbnail copy plus the episode title it ships with.** The two are judged together because the viewer sees them together. The title carries the who and the search terms; the thumbnail carries the claim.

**The copy is for the viewer; the card is for the designer.** A 3 or 4 word line compresses an idea, and on its own it gives her nothing to draw. So every card spells out the full idea behind the line and a concrete visual concept for showing it. She never has to reverse-engineer a picture from four words, and the copy never gets longer just to brief her. This came from the designer on the KAST episode: "Bigger than crypto exchanges?" was the right copy, but it left her nothing to visualise, while the longer "How neobanks will beat exchanges" had at least given her a neobank-versus-exchange picture.

**The deliverable is a published HTML artifact, never chat markdown.** The reader is visual and busy. A wall of text in a chat window is the failure mode this skill exists to avoid. She should see every option at the size it will actually appear, spot the ones that die at browse size, tick the ones she likes, and export her picks as a Word file in about two minutes. Detail sits behind collapsed sections she opens only when she wants them.

She picks. The brief does not pick for her. It shows what each choice costs and what it would teach.

The designer already has host and guest portraits. She does not need a video still and should not wait on one.

Works for all four shows in the network (Founder Thesis, un#, Built to Share, Human by Design). Every measured figure below is from Founder Thesis. Treat it as a strong prior for the other three, not as proof.

## Trigger

Fire on `/thumb`, optionally followed by the show (`/thumb FT`). The show is only used to keep host and guest names straight.

## Inputs

1. **Transcript** (required). Read it fully before writing anything. The best copy is usually a phrase someone actually said.
2. **Episode title** (optional). If one is supplied, it becomes the title half of at least three combos, and the rest of the menu offers alternatives to it.
3. **Guest dossier** (optional). If an `ft-guest-eval` artifact or research dossier exists for this guest (check the project files), lift its business section rather than rewriting it.

No transcript means no brief. Stop and ask for it rather than working from a summary. Web search is allowed to fill gaps in the business explainer when the transcript assumes knowledge the viewer will not have.

## The evidence base

Nine concluded tests where the thumbnail overlay copy itself was read, with share of watch time. This is the training set. Every option card cites it.

| Episode | Winning copy | Share | Weakest copy | Share |
|---|---|---|---|---|
| Captain Fresh | India's most underrated $1B Founder | 67.2% | $1 BILLION / M&As to scale globally | 14.9% |
| Centricity | The uncomfortable truth about your wealth management | 64.6% | Inside India's wealth industry | 15.9% |
| SquadStack | the playbook for voice bots | 62.1% | AI CLONED OUR CALLERS (no face) | 5.1% |
| SuperGaming | HE RUNS PAC-MAN MOBILE | 49.1% | WHY NEW GAMES CAN'T WIN | 22.6% |
| Palantir | FUNDING INDIA'S PALANTIR? | 47.5% | CHINA COPIES CHIPS NOT MACHINES | 20.7% |
| Kazam | (identical copy, stronger image) | 46.2% | (identical copy, weaker image) | 25.6% |
| Felicity | HOW MOBILE GAMES MAKE MONEY | 40.3% | WHY Candy Crush WINS | 25.2% |
| ello.ai | Rent any intelligence you want | 40.3% | AI SPENDS OVER PAYROLL SPENDS? | 23.1% |
| Stellaris | Cold emails don't get funded | 39.6% | The dirty secrets of Venture Capital | 30.2% |

Four further tests varied titles only and point the same way: SatSure 55.9%, SilverX 50.5%, EtherealX 40.9%, Netcore 58.6%.

YouTube scores these on share of watch time, not click-through, so a winner earned the click **and** held the viewer.

## What wins

- **Second person, or a line that implicates the reader.** "your wealth management", "Rent any intelligence you want", "Cold emails don't get funded".
- **A reference point the viewer already holds.** Palantir, PAC-MAN. The known thing explains the unknown founder.
- **Plain money language and concrete deliverables.** "HOW MOBILE GAMES MAKE MONEY", "the playbook for voice bots".
- **A number inside a claim, never alone.** "India's most underrated $1B Founder" took 67.2%. Bare "$1 BILLION" took 14.9% in the same test.
- **Sentence case over all caps.** Identical words, 40.3% against 36.6%.

## What loses, every time it has been tested

These still appear in the menu when they are the obvious idea, badged **Avoid** with the number attached. She should see what was considered and why it was rejected, not be handed a pre-sanitised list.

- **"Inside <company>" and category labels.** "Inside India's wealth industry" 15.9%, the worst copy result on record. Also "Inside Silver X" at 30.7%.
- **Bare number shouting.** "$1 BILLION" 14.9%, "$600M fund" 30.3%.
- **Negative or abstract framings.** "WHY NEW GAMES CAN'T WIN" 22.6%.
- **Jargon comparisons.** "AI SPENDS OVER PAYROLL SPENDS?" 23.1%, "M&As to scale globally" 14.9%.
- **Copy about anyone other than the guest.** Candy Crush 25.2%, China and chips 20.7%, Trump 17.9%.
- **Analogies that need decoding.** "UPI MOMENT for electricity?" 28.2%.

## Akshay's review rules

These come from Akshay reviewing menus line by line, not from YouTube tests. They are his taste and they are binding: every line is screened against them before it enters the menu. A line that fails one is cut, or kept only as an **Avoid** card with the failed rule named. First recorded on the un# KAST episode (Raagulan Pathmanathan), September 2026.

1. **Short.** 3 to 4 words. Five only when every word is short. "Bigger than Coinbase by 2030?" and "Crypto's next giant: a money app?" both came back as too long, though he liked the idea behind the second; "Crypto's next giant?" is the cut-down form.
2. **Somebody is building something.** A line that only names a problem, a statistic or a macro trend reads like a social documentary, not a founder interview. Rejected: "$8B in fees. Every year.", "The 2030 neobank shock", "The dollar already won", "Exchanges were round one".
3. **Aspirational, never a gap.** Framing around what is missing reads as negative. Rejected: "The global Venmo nobody built".
4. **Globally known references only.** The network's audience is India and Asia first. US-only or Europe-only brands fail: Venmo, Revolut. AWS passed.
5. **A brand beside the guest's face reads as his employer.** "A JP Morgan on stablecoin rails" made it look like a JP Morgan executive was on the show. A brand works only when the line turns it into a category the guest belongs to: "The AWS of stablecoin banking" passed, as did "India's Palantir".
6. **Correct English on a literal read.** "Money that moves like WhatsApp" failed because WhatsApp doesn't move; messages do.
7. **A number must explain itself in one glance and give a reason to click.** "0.1% of $120T. For now." gave neither.

What passed on that episode, as a model for grand-vision guests: **"Bigger than crypto exchanges?"** (a bet on scale, phrased as a question), the idea behind **"Crypto's next giant?"**, and **"The AWS of stablecoin banking"**.

When the guest's pitch is a big vision, lead with the vision and put the product detail in the title.

8. **Make the viewer feel something.** Every line has to trigger fear, controversy, sadness, anger or curiosity in the viewer. A line that describes the product, or names a feeling without causing it, is "baseline" and gets sent back. Recorded on the Founder Thesis Gaurav Mishra (Proshort) episode, October 2026, over four rejected rounds:
   - Plain description, rejected: "Whisper the answer", "Your sales call copilot", "From spying to coaching".
   - Intrusive but still plain, rejected: "Who's whispering to your rep?", "Someone's on your call", "Stop spying. Start coaching."
   - Names an emotion without triggering it, rejected: "Stumped? AI whispers the answer", "Their reps have AI. Yours?", "Watched every call. Hated it.", "He dreamt of India's Google".
   - Strongest levers to reach for first: a buyer-side fear ("You won't know it's AI"), a real quote with conflict in it from someone on the episode ("That's not my problem"), a fight the industry is already having ("Did vibe coding just kill SaaS?"), a villain or a loss in the guest's story ("He took on Google and lost"). Pending Akshay's verdict.
9. **Sharpen the concept, don't swap it.** When Akshay asks for punchier copy, keep each card's idea and visual and rework only the wording. A round that drifted to new angles was rejected; "AI in every sales call?" is the model of a base worth sharpening.

Rule 3 and rule 8 pull against each other. Read rule 3 as applying to the guest's own story (don't frame the founder by what's missing); fear, anger and controversy aimed at the viewer's own situation are what rule 8 asks for. Flag any line that leans on both.

After every review where Akshay rejects lines with a reason, add the new rule or example here, in the same turn, and tell him it's been added.

## Routing

The old routing asked whether the episode had a big number and led with it when the answer was yes. That is contradicted: three variants carrying a big number lost to variants carrying none. Ask this instead.

> **What does the viewer get, and what do they already recognise?**

If the audience already holds a reference point, anchor to it, subject to review rules 4 and 5. If not, name the deliverable or the bet in plain words. A number is an ingredient either way and never carries the line alone.

Routing shapes which patterns dominate the menu. It does not narrow the menu to one.

## The context block

The half the designer cannot get anywhere else. Write it for someone who has never heard of the guest or the company. In the artifact the episode summary and the conversation beats sit open, near the top, as "The episode in brief"; Akshay flagged the brief as missing the summary when it was collapsed (Gaurav Mishra episode, October 2026). The business explainer and the takeaways stay collapsed.

**The business in plain terms** (150 to 200 words). Lead with the industry structure, not the company's self-description. Who does what in this value chain, where this company sits, how it makes money, and one or two comparables. The test: could she explain the company to a friend after reading it once.

**What happened in the conversation** (5 to 7 bullets with timestamps). The actual beats. Where the guest pushed back, where a number landed, where the story turned. Not a list of topics.

**What a viewer takes away** (3 to 5 bullets). The insights someone is glad they watched for, phrased as what they now know. This is what the thumbnail is selling, so every option must trace to one of these, and each card shows which.

## Building the menu

**Ten to twelve combos.** Spread across the winning patterns so there is genuine choice: known reference point, a bet on scale phrased as a question, second person, plain money, number-in-a-claim, verbatim guest line. Screen each against the review rules first. Include one or two **Avoid** cards for the obvious ideas that fail, so she sees why they were dropped.

Each combo carries:

- **Thumbnail copy**, in the case it should be set in, with `[VERBATIM, speaker, ts]` or `[FRESH, ts]`
- **Episode title**, see below
- **The idea**: one plain sentence stating the full claim the copy compresses, with its timestamp. Name who or what is being compared, or what is being built. Written so she could explain the line to someone who hasn't seen the episode. Example for "Bigger than crypto exchanges?": "Rags predicts that stablecoin money apps like KAST will grow bigger than crypto exchanges, which most people see as crypto's giants today (30:14)."
- **Visual concept**: two or three concrete sentences. The scene, the central contrast or metaphor that makes the idea visible, and where the guest sits in it. For a comparison line, name both sides and show which one wins. Specific to this line, never repeated across cards. Example: "Split frame. On the left, an exchange trading screen full of red and green candles, small and pushed to the edge. On the right, a phone with a clean money app towering over it. Rags stands on the app side."
- **Alternate visual**: one line, a second way to show the same idea. This is what the image-axis test uses.
- **Pattern badge**: `Proven` (matches a winning pattern), `Untested` (reasonable, no precedent), `Avoid` (matches a losing pattern or fails a review rule)
- **The note**: the pattern and its number, then any warning. Legibility risk, a claim that needs checking, or why it is an Avoid. Two lines maximum.
- **Traces to**: which viewer takeaway it sells
- **Pairs with**: the option number it makes a clean one-axis test against

## Writing the title half

- **The title carries the who.** Guest's full name and company in every title, usually after a pipe: `… | Raagulan Pathmanathan, KAST`. Add the host's credential hook only if it earns space (ex-Circle, ex-Flipkart).
- **One searchable topic phrase** a viewer would type: stablecoin neobank, cold chain seafood, voice AI. Use the spelling the market uses, not the transcript's (transcripts mangle names; check the dossier).
- **Around 60 to 75 characters.** Front-load the claim so it survives truncation on mobile.
- **The title may echo the thumbnail** when both stay specific. The Palantir winner ran title "India's Palantir: Inside the Defence Tech Startup Boom" with thumbnail "FUNDING INDIA'S PALANTIR?" and took 47.5%. The failure mode is an unspecific thumbnail, not an echoed one.
- **Where the thumbnail is a question or a bet, the title answers enough of it** to make the click feel safe: "Bigger than crypto exchanges?" pairs with "Why Stablecoin Neobanks Will Shock Everyone by 2030 | …".
- The same factual bar applies to titles as to thumbnails.

Search-optimised title sets for Founder Thesis remain `ft-episode-titles`. When that skill has already produced a title for this episode, reuse it in at least two combos.

## Pairing for the test

Name **two or three pairings worth running**, and for each say what a win would tell you.

- **Copy axis** (default). Same background, same portrait, two different lines.
- **Image axis.** Same line, two different visuals: the card's visual concept against its alternate visual. The Kazam test moved 20.6 points on this axis alone.

Never vary both, or the result explains nothing. Titles stay fixed during a thumbnail test. Two variants, not three, unless the episode is one you expect YouTube to push hard: below the channel's impression median a three-way split runs the full fourteen days and returns "not enough impressions". Seven of twenty tests died that way.

## Word budget

Target 3 to 4 words, 5 at most (review rule 1). Numerals and symbols survive small better than spelled-out words; say so in the note when it is the deciding factor.

Legibility is the real constraint, and the artifact settles it visually rather than by assertion. The line must read at 168px wide, the browse size on a phone.

## Visual direction

Stated once in the artifact header, not repeated on every card.

- **Visual concepts are described concretely.** "A red-lit data centre at night." "A Pac-Man maze." "A Gmail rejection screen." Not "something about deep tech." The Stellaris winner used a staged Gmail screen, an idea from the episode rather than a moment filmed in it, so a visual never requires footage.
- **The visual carries what the copy leaves out.** When the copy is a question or a bet ("Bigger than crypto exchanges?"), the image shows the two sides so the viewer gets the comparison before reading a word.
- **Cut-out portrait, not a video still.** The three highest shares on record (67.2%, 64.6%, 62.1%) all used one. The podcast-set look with two people and visible mics tops out around 49%. Within the Palantir test the two-shot took 31.8% and the single composited portrait took 47.5%.
- **The guest stays the largest single element.** Every tested variant that removed the guest or shrank him among other faces lost, four of five coming last.
- **No third face.** Borrowed celebrity has failed three of three: Trump 17.9%, an Ambani montage 19.5%, Modi and Xi 20.7%.

## The factual bar

Non-negotiable. Curiosity gaps are the job. Half-truths are not.

- A curiosity gap withholds something the episode actually delivers. Fair.
- A claim the episode does not support is banned, however well it would click.
- Every number must appear in the transcript or dossier. Never round up, never invent, never borrow from elsewhere. A number from the dossier that the guest never says on air is allowed but flagged in the note.
- A number the host says is the host's, not the guest's. Flag it, and never imply the guest's company is fixing something it isn't yet doing.
- Every claim carries the timestamp where it is said, so the designer can verify without watching.
- If a strong line needs a stretch, keep it in the menu badged **Avoid** with the gap named.

Hunt verbatim lines first. A line the guest actually said is already phrased the way a human would phrase it.

## The artifact

Write one self-contained HTML file and publish it with the Artifact tool, declaring `capabilities: {downloads: true}` on the first publish so the export works. New episode, new file path, so each brief keeps its own URL. Do not use the React artifact builder; a single hand-written HTML page is the right weight here.

Build it in this order, because the order is the point. The menu is the page; everything else is reference.

**1. Header.** Guest, company, show, episode date. One line on what the viewer gets. The standing visual direction as four short chips, not prose. A one-line note on the title split, and the correct spelling of any name the transcript mangles.

**2. The legibility strip.** Every thumbnail line rendered at 168px wide in a single scrollable row, in the type treatment it would use. This is the most useful thing on the page: she sees at a glance which lines survive browse size and which turn to mush. Tapping a tile jumps to its card. It sits above the cards.

**3. Combo cards, a responsive grid, two or three across.** Each card:
- A 16:9 preview tile with the copy set in position and a neutral silhouette block standing in for the cut-out portrait. Scale the tile's type with container query units (`cqw`) so the 168px strip tile is a true shrink of the card tile. A layout sketch that shows word count and balance, not a mockup of finished art.
- Directly under the tile, the **title** as it would appear under a YouTube thumbnail: two lines max, clamped, with a character count.
- **The idea** and **Show it** (the visual concept), stacked under the title with those labels, then the alternate visual as a smaller line. These sit above the badge and note because they are what she works from.
- The pattern badge, colour-coded: Proven green, Untested neutral, Avoid red. Colour is never the only signal, so the badge carries its word and a glyph.
- The note, two lines maximum.
- Footer chips: `Traces to <takeaway>`, `Pairs with #<n>`, `[VERBATIM 41:59]` or `[FRESH]`.
- Clicking a `Pairs with` chip scrolls to and highlights that card.
- **A Pick toggle** (a real checkbox with a visible label, not colour alone) and a small optional **note field** for her comment, both with stable ids. A picked card gets a visible selected state.

**4. Pick bar.** A sticky bar at the bottom of the viewport (`bottom: 0` plus `env(safe-area-inset-bottom, 0px)` in its padding) showing "N picked", a **Clear** button and an **Export to Word** button. It stays hidden until at least one card is picked. Picks and notes also persist in `localStorage` (wrapped in try/catch) as a per-viewer convenience so a reload doesn't lose them.

**5. Pairings worth running.** Two or three, each showing the two preview tiles side by side with the titles under them, the axis named, and what a win for each would tell you.

**6. Context.** "The episode in brief" sits open directly under the header: two short paragraphs on the episode, then the timestamped conversation beats. Further down, two `<details>` sections closed on load: the business in plain terms, and what a viewer takes away.

**7. Guardrails, collapsed.** Two `<details>`: claims you may make (each with its timestamp) and must not imply (each with why and its timestamp). Green and red headers with the words in the markup, not in CSS `content`.

**8. Pre-flight.** Real checkboxes at the foot of the page:
- Cut-out portrait, not a video still
- Guest is the largest single element in the frame
- Copy legible at 168px wide
- No third face competing with the guest
- 4 words or fewer, or the layout gives it a clean field
- Cover the copy: can you still tell this is a founder interview about a specific business

Build rules: responsive down to a phone, light and dark both handled through tokens, no colour used as the only carrier of meaning, no purple gradients or centred hero. Give the page wrapper's grid children `min-width: 0` so the scrolling strip can't widen the page. The page must be readable at rest without scrolling to trigger anything.

## The Word export

The export writes a real `.docx` in the browser and hands it to the viewer through the `downloads` capability. The page cannot trigger a download any other way.

**What goes in the file**, in this order:
1. Heading: `Thumbnail picks: <Guest>, <Company>` and a line with show, episode date and export date.
2. One block per picked combo, in menu order: `#n  <thumbnail copy>`, then `Title:`, `The idea:`, `Visual concept:`, `Alternate visual:`, `Badge:`, `Source:` (verbatim/fresh + timestamp), `Note:` (the brief's note), and `Designer note:` if she wrote one.
3. The pairing she should test, if both halves of a named pairing are picked.
4. Pre-flight: each item with ☑ or ☐ as ticked on the page.
5. Must-not-imply guardrails, as a short list, so they travel with the file.

Filename: `thumb-picks-<guest-slug>-<yyyy-mm-dd>.docx`.

**How to build it.** Load JSZip from cdnjs (`https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js`, before the inline script) and assemble a minimal WordprocessingML package. This builder has been checked to open in Word-compatible apps:

```js
function buildDocx(blocks){ // blocks: {kind:"h1"|"h2"|"h3"|"p", text} or {runs:[{text,bold}]}
  const x = s => String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
  const para = b => {
    const sz = {h1:36,h2:28,h3:24}[b.kind] || 21;
    const bold = b.kind && b.kind !== "p" ? "<w:b/>" : "";
    const runs = (b.runs || [{text:b.text}]).map(r =>
      `<w:r><w:rPr>${bold || (r.bold?"<w:b/>":"")}<w:sz w:val="${sz}"/></w:rPr><w:t xml:space="preserve">${x(r.text)}</w:t></w:r>`).join("");
    return `<w:p><w:pPr><w:spacing w:after="${b.kind==="h1"?200:120}"/></w:pPr>${runs}</w:p>`;
  };
  const zip = new JSZip();
  zip.file("[Content_Types].xml",`<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>`);
  zip.file("_rels/.rels",`<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>`);
  zip.file("word/document.xml",`<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>${blocks.map(para).join("")}<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="0" w:footer="0" w:gutter="0"/></w:sectPr></w:body></w:document>`);
  return zip.generateAsync({type:"blob"});
}
```

**How to hand it over.**

```js
let downloads = null;
claude.use("downloads").then(d => { downloads = d; exportBtn.hidden = !d; copyBtn.hidden = !!d; });
exportBtn.onclick = async () => {
  try { await downloads.save({ filename, data: await buildDocx(blocks) }); status("Saved"); }
  catch (e) {
    if (e?.code === "declined") return;                   // she said no; never retry
    if (e?.code === "rate_limited") return status("A save prompt is already open");
    status("Word export isn't available here. Use Copy picks instead.");
  }
};
```

`claude.use("downloads")` resolves `null` where saving can't run (some viewers, previews). Then hide Export and show **Copy picks**, which writes the same content as plain text with `navigator.clipboard.writeText` inside the click handler, falling back to selecting a `<textarea>` when the clipboard refuses. Never use `<a download>`; the viewer's frame blocks it.

**Before publishing**, run one check: build the same blocks in Node with the `jszip` package and open the result with `python-docx` or LibreOffice. Then syntax-check the page script once with `node --check`.

After publishing, say in one line what it is. Do not restate the menu in chat. The page is private until shared, so remind Akshay to share it with the designer.

## After the test concludes

Add a row to the evidence table: episode, winning copy, share, weakest copy, share. That is what keeps this skill grounded in the channel rather than in theory.

Then check the winner was actually applied in Studio. Three concluded tests are currently still running a losing variant, one by 29 points, because the reminder badge in the content list disappears the moment anyone opens the report.

## What this skill does not do

- No colour, font or brand-system decisions. Those stay with the designer.
- No full search-optimised title sets or descriptions. The title half of each combo is written here; full FT title sets are `ft-episode-titles`, descriptions are `ft-show-notes`.
- No analytics interpretation beyond the evidence table.
- No copy for shows outside the four in the network.