/* ---------------------------------------------------------------------------
 * HOUSE PITCH / CONCEPT NOTE TEMPLATE
 *
 * The canonical Word build. Section order, design tokens and table structures
 * here match the rules in references/editorial-rules.md. If the two ever
 * disagree, the rules file wins and this file is stale: fix it.
 *
 * To use it for a new client:
 *
 *   1. Copy this file to /home/claude.
 *   2. Set ROUTE, CLIENT, SHOW, HOST and OUT below.
 *   3. Replace every block marked REPLACE with this client's material.
 *   4. Swap the pricing rows and tags for the values confirmed in Phase 3.
 *   5. Keep the section order, the design tokens, the helpers and the table
 *      structures exactly as they are.
 *   6. Build, convert to PDF, and look at every page before presenting.
 *
 * Section order, both routes:
 *   Cover, the on-ramp, Overview (carries the ownership line), [Route B only:
 *   the access opener], Who it is for, Potential themes, The roadmap (ending in
 *   how we measure it), What one recording becomes, What the sales team can use,
 *   Investment (setup is a ROW in the table), What we need from the client,
 *   Why us, closing line.
 *
 * Type sizes are deliberate: 11pt (size 22) minimum for all body text,
 * bullets and every table cell, because these get read on phones. Only the
 * RECOMMENDED / OPTIONAL tag labels go smaller.
 *
 * Every table sets columnWidths in twips at the Table level, with a matching
 * DXA width on every cell and FIXED layout. A percentage width with no column
 * widths collapses into slivers of vertical letters in Word while looking
 * fine in a PDF render.
 * ------------------------------------------------------------------------- */

const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  BorderStyle, AlignmentType, LevelFormat, convertInchesToTwip, VerticalAlign,
  ShadingType, TableLayoutType, ExternalHyperlink } = require('docx');
const fs = require('fs');

const INK = "20242B", HEAD = "17365D", MUTE = "5A5F68", RULE = "C9CED5", BAND = "EDF1F6";
const TAGR = "17365D", TAGO = "6E747C";
const F = "Calibri", SZ = 22;

// ---- REPLACE per client ----
const ROUTE = "A";                       // "A" = idea already sold, "B" = still selling it
const CLIENT = "Riceberg Ventures";
const SHOW = "Breakthrough Thesis";
const HOST = "Ankit";
const OUT = `/mnt/user-data/outputs/${SHOW.replace(/ /g, "-")}-${ROUTE === "A" ? "Concept" : "Pitch"}-Note.docx`;

const KICKER = ROUTE === "A" ? "CONCEPT NOTE" : "PITCH NOTE";
const TITLE = ROUTE === "A" ? `${SHOW} by ${CLIENT}` : `A podcast for ${CLIENT}`;

/* --- helpers ------------------------------------------------------------ */

const t = (x, o = {}) => new TextRun({ text: x, bold: !!o.b, italics: !!o.i,
  underline: o.u ? {} : undefined,
  size: o.size || SZ, color: o.color || INK, font: F });

/* A show name in Why us links to its YouTube channel, so a reader who wants to check
   is one click away. URLs in references/credentials.md. */
const link = (text, url) => new ExternalHyperlink({ link: url,
  children: [t(text, { b: true, color: HEAD, u: true })] });

const p = (children, o = {}) => new Paragraph({ children,
  spacing: { after: o.after === undefined ? 130 : o.after, line: 252 } });

const h1 = (x) => new Paragraph({
  children: [new TextRun({ text: x, bold: true, size: 30, color: HEAD, font: F })],
  spacing: { before: 300, after: 100 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 5 } },
});

const sub = (x) => new Paragraph({
  children: [new TextRun({ text: x, bold: true, italics: true, size: 23, color: INK, font: F })],
  spacing: { before: 180, after: 70 },
});

const mini = (x) => new Paragraph({
  children: [new TextRun({ text: x, bold: true, size: 20, color: MUTE, font: F })],
  spacing: { before: 110, after: 55 },
});

const bullet = (runs) => new Paragraph({ children: runs,
  numbering: { reference: "cn", level: 0 }, spacing: { after: 70, line: 252 } });

const cell = (children, o = {}) => new TableCell({
  width: { size: o.w || 1000, type: WidthType.DXA },
  margins: { top: 100, bottom: 100, left: 140, right: 140 },
  shading: o.shade ? { type: ShadingType.CLEAR, fill: o.shade } : undefined,
  verticalAlign: VerticalAlign.TOP,
  columnSpan: o.span,
  children,
});

const borders = {
  top: { style: BorderStyle.SINGLE, size: 3, color: RULE },
  bottom: { style: BorderStyle.SINGLE, size: 3, color: RULE },
  left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
  insideHorizontal: { style: BorderStyle.SINGLE, size: 3, color: RULE },
  insideVertical: { style: BorderStyle.NONE },
};

// Every table goes through this so columnWidths, DXA cell widths and FIXED
// layout can never drift apart.
const table = (columnWidths, rows, o = {}) => new Table({
  width: { size: 100, type: WidthType.PERCENTAGE },
  layout: TableLayoutType.FIXED,
  columnWidths,
  borders: o.borders || borders,
  rows,
});

const gap = (after = 70) => new Paragraph({ children: [], spacing: { after } });

/* --- guest line --------------------------------------------------------- */
/* Name and role on one line with the region in brackets, the episode angle
 * underneath. Same four fields as the HTML page, so the two cannot drift.
 * Where there is no verified name, pass null and write the slot honestly in
 * `role`. No verification dates against individual names. */

const guest = (name, role, why, region) => {
  const reg = region ? ` (${region})` : "";
  return [
    new Paragraph({
      children: name
        ? [t(name, { b: true }), t(", " + role + reg, { color: MUTE })]
        : [t(role + reg, { i: true, color: MUTE })],
      spacing: { before: 90, after: 20, line: 252 },
    }),
    new Paragraph({ children: [t(why, { color: INK })],
      spacing: { after: 60, line: 252 } }),
  ];
};

/* --- a named block: bold label, then one line under it ------------------- */
/* Used by the themes and the working names, so each one is a demarcated
 * item rather than a line of running prose. The page renders the same two
 * fields as a card the client can tick, cross or add to. */

const block = (label, line, url) => [
  new Paragraph({
    children: [url ? link(label, url) : t(label, { b: true, color: HEAD })],
    spacing: { before: 120, after: 20, line: 252 },
  }),
  new Paragraph({ children: [t(line, { color: INK })],
    spacing: { after: 60, line: 252 } }),
];

/* --- the stats band: four figures across, used once in Why us ----------- */

const bandCell = (fig, cap) => new TableCell({
  width: { size: 2460, type: WidthType.DXA },
  margins: { top: 130, bottom: 130, left: 100, right: 100 },
  shading: { type: ShadingType.CLEAR, fill: BAND },
  verticalAlign: VerticalAlign.CENTER,
  children: [
    new Paragraph({ alignment: AlignmentType.CENTER,
      children: [t(fig, { b: true, size: 30, color: HEAD })], spacing: { after: 20 } }),
    new Paragraph({ alignment: AlignmentType.CENTER,
      children: [t(cap, { size: 18, color: MUTE })], spacing: { after: 0 } }),
  ],
});

// REPLACE the figures from references/credentials.md. Never estimate one.
const statsBand = table([2460, 2460, 2460, 2460], [
  new TableRow({ children: [
    bandCell("2M+", "YouTube views"),
    bandCell("150K+", "Subscribers"),
    bandCell("270K", "LinkedIn followers"),
    bandCell("1,000+", "Hours recorded"),
  ] }),
], { borders: {
  top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
  left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
  insideHorizontal: { style: BorderStyle.SINGLE, size: 10, color: "FFFFFF" },
  insideVertical: { style: BorderStyle.SINGLE, size: 10, color: "FFFFFF" },
} });

/* --- Phase 0 setup table ------------------------------------------------ */

const stageRow = (n, name, line, when, items) => new TableRow({ children: [
  cell([p([t(n, { b: true, size: 26, color: "B7BFC8" })], { after: 0 })], { w: 500 }),
  cell([p([t(name, { b: true, color: HEAD })], { after: 4 }), p([t(line, { i: true, color: MUTE })], { after: 0 })], { w: 2000 }),
  cell([p([t(when, { b: true, color: INK })], { after: 0 })], { w: 1750 }),
  cell([p([t(items)], { after: 0 })], { w: 5590 }),
] });

// REPLACE the four rows with this client's setup, keeping the four labels.
const stageTable = table([500, 2000, 1750, 5590], [
  new TableRow({ tableHeader: true, children: [
    cell([p([t("")], { after: 0 })], { w: 500, shade: BAND }),
    cell([p([t("Stage", { b: true })], { after: 0 })], { w: 2000, shade: BAND }),
    cell([p([t("When", { b: true })], { after: 0 })], { w: 1750, shade: BAND }),
    cell([p([t("What happens", { b: true })], { after: 0 })], { w: 5590, shade: BAND }),
  ] }),
  stageRow("1", "The theme", "We settle what the show is about.", "First fortnight",
    `Positioning, name and tagline, and the visual identity: logo, cover art, thumbnail system. Settled with ${HOST}, not handed to him.`),
  stageRow("2", "The set and format", "We make the recording easy.", "First fortnight",
    "Room, camera and audio spec, episode length and cadence, and a mock run so the format is settled before a guest is in the chair."),
  stageRow("3", "The outreach engine", "We build the list and the ask.", "From week two, then ongoing",
    "Target list research, the invitation, the follow-up sequence, and the tracking behind it. Relationship status on every target is logged before an invitation goes out."),
  stageRow("4", "The first bookings", "We get episodes in the diary.", "From week two",
    `The first six guests come from ${CLIENT}'s own network. On every booking, whoever sourced it, we research the guest, write the prep dossier, and handle the engagement either side of the recording.`),
]);

/* --- measurement: four numbered rows ------------------------------------ */

const measureRow = (n, line) => new TableRow({ children: [
  cell([p([t(n, { b: true, size: 26, color: "B7BFC8" })], { after: 0 })], { w: 600 }),
  cell([p([t(line)], { after: 0 })], { w: 9240 }),
] });

// Four rows, no more. Each one sentence. REPLACE the wording, keep the shape.
const measureTable = table([600, 9240], [
  measureRow("1", "Guests who turn into a commercial conversation within ninety days of the recording."),
  measureRow("2", "How people respond to the cold invitations: the accept rate, and who accepts."),
  measureRow("3", "How many further introductions the guests make."),
  measureRow("4", "Engagement on LinkedIn across the posts, the newsletter and the short videos, read as who is responding rather than as reach, because that is where the right people surface months before they reply to anything."),
]);

/* --- content engine: three by four grid --------------------------------- */

const chip = (label) => new TableCell({
  width: { size: 3280, type: WidthType.DXA },
  margins: { top: 130, bottom: 130, left: 140, right: 140 },
  shading: { type: ShadingType.CLEAR, fill: BAND },
  verticalAlign: VerticalAlign.CENTER,
  children: [new Paragraph({ alignment: AlignmentType.CENTER,
    children: [t(label, { color: HEAD })], spacing: { after: 0 } })],
});

const engineTable = table([3280, 3280, 3280], [
  ["Full episode on YouTube", "Spotify and Apple", "LinkedIn video"],
  ["4 vertical shorts", "2 horizontal clips", "Trailer and thumbnails"],
  ["Posts in your voice", "Company page posts", "A share kit for the guest"],
  ["Carousel or quote cards", "An SEO blog article", "A deep-dive newsletter"],
].map(r => new TableRow({ children: r.map(chip) })), {
  borders: {
    top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
    left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
    insideHorizontal: { style: BorderStyle.SINGLE, size: 10, color: "FFFFFF" },
    insideVertical: { style: BorderStyle.SINGLE, size: 10, color: "FFFFFF" },
  },
});

/* --- investment --------------------------------------------------------- */

const tag = (label, colour) => new Paragraph({
  children: [new TextRun({ text: label, bold: true, size: 16, color: colour, font: F, characterSpacing: 25 })],
  spacing: { before: 30, after: 0 },
});

const priceRow = (name, tagText, tagColour, rate, covers) => new TableRow({ children: [
  cell([p([t(name, { b: true })], { after: 0 }), ...(tagText ? [tag(tagText, tagColour)] : [])], { w: 2500 }),
  cell([p([t(rate)], { after: 0 })], { w: 1900 }),
  cell([p([t(covers)], { after: 0 })], { w: 5440 }),
] });

const sectionRow = (label) => new TableRow({ children: [
  cell([p([t(label, { b: true, color: HEAD })], { after: 0 })], { w: 9840, span: 3, shade: BAND }),
] });

// REPLACE rates and tags with what was confirmed in the Phase 3 pricing gate.
// Setup is a ROW here, never a section of its own. Setup and post-production
// are never tagged Optional. Every rate carries a period.
const priceTable = table([2500, 1900, 5440], [
  new TableRow({ tableHeader: true, children: [
    cell([p([t("Item", { b: true })], { after: 0 })], { w: 2500, shade: BAND }),
    cell([p([t("Rate", { b: true })], { after: 0 })], { w: 1900, shade: BAND }),
    cell([p([t("What it covers", { b: true })], { after: 0 })], { w: 5440, shade: BAND }),
  ] }),
  sectionRow("Run by us (Unnati)"),
  priceRow("Setup", null, null, "₹75,000 one-time",
    "Branding: the name, logo, cover art and the look of the show. Distribution set up across YouTube, Spotify and the audio apps. The show's social handles created. Host prep, including a mock run before the first real recording."),
  priceRow("Post-production", null, null, "₹60,000 / episode",
    "Multi-cam edit, on-screen jargon explainers, 4 vertical shorts, 2 horizontal clips, 1 trailer, up to 5 thumbnails."),
  priceRow("Guest sourcing", "OPTIONAL", TAGO, "₹10,000 / guest sourced",
    `Target list research, outreach, follow-ups, scheduling, guest prep and guest promotion at release. Charged only on guests we source. No fee on anyone ${CLIENT} introduces. Guest research, the prep dossier and the engagement either side of the recording are included on every booking, whoever sourced it.`),
  priceRow("Akshay on the recording", "OPTIONAL", TAGO, "₹10,000 / episode",
    "Sitting in on the session to keep it running smoothly. Remote recordings only. The first three recordings are free."),
  priceRow("Content amplification", "RECOMMENDED", TAGR, "₹20,000 / episode",
    "LinkedIn posts for host and company, guest kit, clip copy, a carousel or quote cards, an SEO blog and a deep-dive newsletter."),
  priceRow("Offline recording", "OPTIONAL", TAGO, "₹10,000 / episode recorded in person",
    "Crew and kit to a location for an in-person recording rather than a remote one. Charged only on the episodes actually recorded in person. Cut this line where the show records remotely."),
  priceRow("Content ops", "OPTIONAL", TAGO, "₹10,000 / month",
    "We log into your handles, publish the posts, and respond to comments."),
  sectionRow("Third party services, paid directly"),
  priceRow("Studio setup consult", "RECOMMENDED", TAGR, "₹50,000 one-time",
    "For a client building a professional recording space in their own office. A consultant specs the room and the kit: acoustic treatment, lighting, cameras, audio chain and the desk layout, sized to the room and the budget, with a buying list you purchase directly. We take no margin on the hardware. Drop this line entirely where the host has no fixed studio and no plan for one."),
  priceRow("Ad management agency", "OPTIONAL", TAGO, "₹75,000 one-time",
    "Only if you do not have an in-house team or an agency already."),
  priceRow("Google Ads", "RECOMMENDED", TAGR, "₹80,000 media spend over 3 to 4 months",
    "A targeted test to put episodes in front of the named cohort. Promotional credit from Google comes on top of the spend. Paid results are reported separately from organic, and are not a success metric."),
]);

/* --- document ----------------------------------------------------------- */

/* ---- the on-ramp ----
   First thing after the cover, above the opener, under 90 words all in.
   Route B: three beats, in this order, never merged into one paragraph.
     1. Their problem, in their own language. Two sentences about their business.
     2. Why the route they already use tops out. One sentence, name the real thing.
     3. The proposal, named plainly. The word podcast, who hosts it, what one episode is.
   Route A: ONE line, where this came from and what was agreed.
   Beats 1 and 2 are sourced from the transcript or verified research, never invented.
   No question opening, no statistic as the first line. Rules and worked examples in
   editorial-rules.md under "The on-ramp". REPLACE every line below. */
const onRamp = ROUTE === "B" ? [
  p([t(`${CLIENT} backs deep tech, which means the founders worth funding are the ones nobody has heard of yet, working on things that do not have a category.`)]),
  p([t(`Deal flow comes through the same fund network everyone else is in, and the best of those founders are not in it.`)]),
  p([t(`The proposal is a podcast ${HOST} hosts, where every episode is a long conversation with one of those founders, researchers or operators about the work itself.`)]),
] : [
  p([t(`You and Akshay settled the shape of this on the call in September. This is what it looks like built.`)]),
];

const accessOpener = ROUTE === "B" ? [
  // REPLACE: three short paragraphs, no heading. Access first, then the
  // episode, then ownership. No universal quantifiers.
  p([t(`The people who decide this are spread across three desks, and they do not agree with each other. Ordinary outreach rarely reaches them. An invitation to talk about their own work often does.`)]),
  p([t(`Every episode is a senior decision maker at a company ${CLIENT} wants, in a long conversation with ${HOST}, with no pitch in it. The relationship is the point, and the published conversation does its own work as the clearest explanation of what ${CLIENT} actually does.`)]),
  p([t(`The brand sits with ${CLIENT} and ${HOST} is its face. Channel, handles, raw recordings, edited masters and the ad account are yours.`)], { after: 40 }),
] : [];

const doc = new Document({
  numbering: { config: [{ reference: "cn", levels: [{
    level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: convertInchesToTwip(0.26), hanging: convertInchesToTwip(0.17) } },
      run: { color: MUTE, font: F } } }] }] },
  styles: { default: { document: { run: { font: F, size: SZ, color: INK } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 },
      margin: { top: 1080, bottom: 1000, left: 1200, right: 1200 } } },
    children: [

      /* ---- cover ---- */
      new Paragraph({
        children: [new TextRun({ text: KICKER, bold: true, size: 19, color: MUTE, font: F, characterSpacing: 50 })],
        spacing: { after: 90 },
      }),
      new Paragraph({
        children: [new TextRun({ text: TITLE, bold: true, size: 40, color: HEAD, font: F })],
        spacing: { after: ROUTE === "A" ? 70 : 60 },
        border: ROUTE === "B"
          ? { bottom: { style: BorderStyle.SINGLE, size: 6, color: HEAD, space: 10 } }
          : undefined,
      }),
      // Route A carries a one-line italic subtitle. Route B has none: it goes
      // straight into the argument.
      ...(ROUTE === "A" ? [new Paragraph({
        children: [new TextRun({ text: "A deep tech fund's owned brand asset, taking the conversation that happens in diligence and having it in public, with the people building technologies that do not exist yet.", italics: true, size: 23, color: MUTE, font: F })],
        spacing: { after: 60, line: 252 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: HEAD, space: 10 } },
      })] : []),

      /* ---- credibility strip. One grey line, three facts, BOTH routes. Furniture,
         not a paragraph: it never grows and never takes an adjective. ---- */
      new Paragraph({
        children: [new TextRun({ text: "Six years. Four shows. Two million views.", size: 19, color: MUTE, font: F, characterSpacing: 20 })],
        spacing: { after: 160 },
      }),

      ...onRamp,

      ...accessOpener,

      /* ---- overview (Route A) ---- */
      ...(ROUTE === "A" ? [
        h1("Overview"),
        p([t(`${SHOW} is a podcast ${HOST} hosts, about the gap between a technology working in a lab and existing as a product: chip design, nuclear power, robotics, space and AI, examined from the vantage point of someone who has crossed that gap himself and now funds people trying to.`)]),
        p([t(`Every conversation is also a real relationship with a founder, a researcher or an operator worth knowing. Ninety minutes of thinking hard about someone's own work is a materially different first contact from a meeting, and it compounds across a season.`)]),
        // The ownership line lives here, in the opener, not under the price table.
        p([t(`The brand sits with ${CLIENT} and ${HOST} is its face. Channel, handles, raw recordings, edited masters and the ad account are yours.`)], { after: 40 }),
      ] : []),

      /* ---- who it is for ---- */
      h1("Who it is for"),
      p([t("Who listens.", { b: true }), t(" Four groups.")], { after: 70 }),
      bullet([t("Founders and technical teams.", { b: true }), t(" They are building at the frontier and they are the fund's dealflow. These are the buyers, and the show is built for them.")]),
      bullet([t("Co-investors and corporate funds", { b: true }), t(" who underwrite the same categories.")]),
      bullet([t("Current and prospective LPs", { b: true }), t(`, who get to see how ${HOST} thinks before they see a deck.`)]),
      bullet([t("Potential hires and the wider deep tech ecosystem", { b: true }), t(", the people who decide where the good engineers and researchers go.")]),
      p([t(`The audience in deep tech is small and senior, which suits the format. ${CLIENT} approves every guest before an invitation goes out.`)], { after: 40 }),

      /* ---- themes ---- */
      h1("Potential themes of the show"),
      // REPLACE: THREE themes. Each is a block, not a bullet: the angle named in
      // a few words, then one line on what the show would chase and who it pulls
      // in. The same two fields the page renders as a card.
      p([t("Three directions the show could take. One leads and the other two run as recurring strands.")], { after: 60 }),
      ...block("Getting out of the lab", "What stayed behind, what got out, and what actually made the difference. Pulls in founders mid-commercialisation, which is the dealflow, and sits closest to the sale."),
      ...block("What breaks when it scales", "Where the step change really sits, how big it honestly is, and what falls over at volume. The engineers' episode, and the one that travels furthest on LinkedIn."),
      ...block("Who went first", "Procurement, regulation, and the person who signed before there was a reference customer. The most quotable, and the one that earns inbound."),
      mini("WORKING NAMES"),
      // REPLACE: TWO names, both short, each promising the listener something and
      // carrying a descriptor. Never a restatement of the company's positioning.
      // See the naming rules in editorial-rules.md.
      p([t("Two names that promise a listener something, rather than describe the company. Working titles, settled together in the first fortnight.")], { after: 60 }),
      ...block("First Customer: the deep tech show", "Promises the moment the science had to earn money, which is the part nobody writes up."),
      ...block("Nobody Funded This: backing what the market passed on", "Promises the story of the bet everyone else passed on. The louder of the two."),
      mini("WHAT AN EPISODE IS"),
      p([t("Each episode is built around one number that moved in the guest's business and what their team did about it. Category setters work the same ground across companies rather than inside one, so the spine flexes for them.")]),
      p([t(`${HOST} gets a prep document before every recording: who the guest is, where the interesting tension in their work sits, and the three or four places worth pushing. No homework, and nobody walks in cold.`)], { after: 40 }),

      /* ---- the roadmap ---- */
      h1("The roadmap"),
      /* The CREDIBILITY LINE. Sits where the reader doubts hardest, right before the
         list promises fifteen senior people will say yes. ALWAYS rewrite the second
         sentence for this client. These people are GUESTS on our shows, never our
         clients, and never "trusted by". From references/credentials.md. */
      p([t("The head of future of finance at Citi and the head of innovation at Franklin Templeton have both sat down for shows we produce. Imagine who says yes to yours.")], { after: 60 }),
      p([t("Episode ranges rather than dates: this is the shape we are aiming at, not a guarantee. The review gate sits after the first four published episodes.")], { after: 110 }),

      sub("Phase 0. Setup. The first fortnight."),
      stageTable,
      gap(),

      sub(`Phase 1. Episodes 1 to 6. People who already know ${CLIENT}.`),
      p([t(`Named individuals from your customer, testimonial, case-study and advisory pages, plus the people who championed a win. These are the fastest bookings, and they are what make the cold list possible: a show with six published episodes is a different ask.`)], { after: 60 }),
      // REPLACE with six verified names. Where there is no verified name, pass
      // null and write the slot honestly. Never invent one.
      ...guest("[Name]", "[Title], [Company]", "[One sentence on the episode angle: the specific thing this person could talk about for an hour.]", "India"),
      ...guest(null, `One from ${HOST}'s own network, named with you before launch`, "The slot is held for a founder in the portfolio who has taken a technology to a first paying customer.", "To confirm"),
      gap(110),

      sub(`Phase 2. Episodes 7 to 14. The people ${CLIENT} wants to meet.`),
      p([t("Three buckets, four names each, spread across the regions the buyers actually sit in. Every name here is a target account.")], { after: 60 }),
      mini("TECHNOLOGY LEADERS"),
      ...guest("[Name]", "[Title], [Company]", "[Episode angle.]", "US"),
      mini("REVENUE LEADERS"),
      ...guest("[Name]", "[Title], [Company]", "[Episode angle.]", "US"),
      mini("DATA AND ANALYTICS LEADERS"),
      ...guest("[Name]", "[Title], [Company]", "[Episode angle.]", "US"),
      gap(110),

      sub("Phase 3. Episode 15 onward. The category setters, and the flywheel."),
      p([t("Analysts, investors, authors and practitioners whose view of this category carries weight. By this point guests are introducing the next guests, and the review gate sits behind this decision.")], { after: 60 }),
      ...guest("[Name]", "[Title], [Company]", "[Episode angle.]", "US"),
      gap(110),

      sub("How we measure it"),
      p([t("A podcast appearance is not a lead. Relationship and opportunity status is logged before an invitation goes out, so the movement reported later is real. Four numbers:")], { after: 110 }),
      measureTable,
      gap(90),
      p([t("Views, retention and subscribers are tracked from the first episode and reported separately, alongside these four rather than in place of them. Titles in the list above are current as of this month and get reconfirmed at outreach.")], { after: 40 }),

      /* ---- content engine ---- */
      h1("What one recording becomes"),
      p([t(`${HOST} records for ninety minutes. That single conversation is turned into everything below, ready to publish.`)], { after: 110 }),
      engineTable,
      gap(),
      p([t("One recording, close to twenty finished assets, across every channel this audience actually reads. Nothing here asks for more of your time.")], { after: 40 }),

      /* ---- sales enablement ---- */
      h1("What the sales team can use"),
      p([t("The episodes do a second job that has nothing to do with the audience, because every conversation arms the people already selling.")], { after: 70 }),
      bullet([t("Names to drop.", { b: true }), t(" “When I was talking to the CTO of [peer company] about this” opens a conversation that a cold email does not, and every episode adds one more.")]),
      bullet([t("Objections in a buyer's own words.", { b: true }), t(" Guests say out loud why they hesitated. The team gets the counter-arguments from a peer rather than from marketing.")]),
      bullet([t("Proof without a case study.", { b: true }), t(" A clip of someone else describing the problem lands harder than a vendor describing the solution, and it is already being produced.")]),
      bullet([t("A reason to reach out.", { b: true }), t(" Sending a prospect the episode featuring their direct peer is a warm touch that asks for nothing.")]),

      /* ---- investment ---- */
      h1("Investment"),
      priceTable,
      gap(60),
      p([t("Anything outside this scope is charged at our standard rate card. Turnaround times, revision rounds, approval windows and cancellation terms are settled in the SOW.")], { after: 40 }),

      /* ---- what we need ---- */
      h1(`What we need from ${CLIENT}`),
      sub("From the host"),
      bullet([t("Four to six hours a month for prep and recording.")]),
      bullet([t("Introductions to the first six guests. A personal note is what gets a yes.")]),
      bullet([t("Sign-off on positioning and on every guest. Anyone with product overlap is your call.")]),
      bullet([t("A short fortnightly review to keep guest targeting sharp.")]),
      sub(`From the ${CLIENT} team`),
      bullet([t("Camera and room logistics for the in-person sessions, to a spec we provide in advance.")]),
      bullet([t("Warm introductions wherever a relationship already exists.")]),
      bullet([t("Cross-posting each episode on your own channels.")]),

      /* ---- why us ---- */
      // REPLACE from references/credentials.md: the THREE shows closest to this
      // prospect, the combined band once, and two or three guest names chosen for
      // this reader. Nothing estimated.
      /* ---- Why us. EVERYTHING from references/credentials.md, nothing estimated.
         The ORIGIN STORY leads, before any show and before any number: it is the
         one thing a competing producer cannot copy. ALL FOUR shows follow, every
         time, Founder Thesis first: the range across four unrelated arenas is the
         argument, and un# is the one wrongly cut for feeling off-topic. Plain verbs, short sentences,
         no "method", no "P&L", no three balanced clauses: an earlier draft had all
         three and was cut for sounding machine-written. Then THREE shows chosen for
         this prospect, with guest names chosen for this reader. Then the band, once.
         Then the time commitment and the link. No "we never invent numbers" line:
         it was drafted and cut, because a document that protests its own honesty
         invites the reader to go looking. ---- */
      h1("Why us"),
      p([t("We ran a hiring company and started Founder Thesis on the side. The founders Akshay interviewed kept turning into clients. After a while it was bringing in more business than anything else we did, so we started building shows for other people too.")], { after: 60 }),
      ...block("Founder Thesis, hosted by Akshay Datt", "The show the method was proved on. Manish Sabharwal of TeamLease, Sanjeev Bikhchandani of Info Edge, Dinesh Agarwal of IndiaMART and Rajendra S. Pawar of NIIT have all taken the chair. It built a community of India's most consequential founders and a business that grew out of the conversations.", "https://www.youtube.com/@founderthesis"),
      ...block("Built to Share, hosted by Satish Mugulavalli", "Category ownership. When founders think about ESOPs and employee equity, Satish is the name in the room, and the education his market needed became the authority his business runs on. Anurag Jain of CarDekho, Ankit Mehta of ideaForge, Vishal Bali of Asia Healthcare Holdings and Atul Shinghal of Scripbox have been on.", "https://www.youtube.com/@built2share"),
      ...block("Human by Design, hosted by Dr. Arjun Jain", "Enterprise doors. An hour with Jürgen Schmidhuber, whose work underpins modern AI, and another with Philippe Rambach, Chief AI Officer of Schneider Electric. The show built Arjun's voice in the field and put him across the table from the Fortune 500 leaders his company serves.", "https://www.youtube.com/@HumanByDesignPodcast"),
      ...block("un# (Unhashed), hosted by Sri Misra", "Access. Sandy Kaul, head of innovation at Franklin Templeton, Ronit Ghose, then running future of finance at Citi, and Matthew Hougan of Bitwise have all sat down with Sri. It gave him a direct line to the investors, builders and distribution partners his business runs on.", "https://www.youtube.com/@unhashedpodcast"),
      gap(110),
      statsBand,
      gap(),
      p([t("Your total commitment is three to six hours a month. The rest is ours. More at myunnati.com.")], { after: 40 }),

      /* ---- closing ---- */
      new Paragraph({
        children: [new TextRun({ text: `The aim through the first cohort of episodes is simple: a handful of conversations that people at the frontier want to be part of, published consistently, so the guest list becomes the fund's clearest asset.`, italics: true, size: 23, color: MUTE, font: F })],
        spacing: { before: 240, line: 252 },
        border: { top: { style: BorderStyle.SINGLE, size: 5, color: HEAD, space: 10 } },
      }),
    ],
  }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync(OUT, b);
  console.log('written:', OUT);
});
