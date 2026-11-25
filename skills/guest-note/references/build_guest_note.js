/* ---------------------------------------------------------------------------
 * HOUSE GUEST NOTE TEMPLATE
 *
 * Filled with the Breakthrough Thesis (Riceberg Ventures) example, which is the
 * new-show case: no reach block, host credibility carrying the note.
 *
 * To use for another show:
 *   1. Copy this file to /home/claude.
 *   2. Set SHOW, BANNER, PHOTO and OUT below.
 *   3. Replace every block marked REPLACE.
 *   4. Add the reach block and the named-guest block ONLY if Phase 2 confirmed
 *      real numbers and agreed names. Delete them otherwise.
 *   5. Build, convert to PDF, and look at every page before presenting.
 *
 * 11pt (size 22) minimum everywhere. These get read on phones.
 * Banner appears once at the top, never as a repeating page header.
 * ------------------------------------------------------------------------- */

const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  BorderStyle, AlignmentType, LevelFormat, ImageRun, convertInchesToTwip,
  VerticalAlign, ShadingType } = require('docx');
const fs = require('fs');

const INK = "20242B", HEAD = "17365D", MUTE = "5A5F68", RULE = "C9CED5";
const F = "Calibri", SZ = 22;

// ---- REPLACE per show ----
const SHOW = "Breakthrough Thesis";
const BANNER = "/home/claude/assets/banner.png";   // crop to ~6:1 first
const PHOTO = "/home/claude/assets/host.png";      // portrait, ~4:5
const OUT = `/mnt/user-data/outputs/${SHOW.replace(/ /g, "-")}-Guest-Note.docx`;

const t = (x, o = {}) => new TextRun({ text: x, bold: !!o.b, italics: !!o.i,
  size: o.size || SZ, color: o.color || INK, font: F });

const p = (children, o = {}) => new Paragraph({ children,
  spacing: { after: o.after === undefined ? 96 : o.after, line: 242 } });

const h1 = (x) => new Paragraph({
  children: [new TextRun({ text: x, bold: true, size: 26, color: HEAD, font: F })],
  spacing: { before: 150, after: 60 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 5 } },
});

const bullet = (runs) => new Paragraph({ children: runs,
  numbering: { reference: "gn", level: 0 }, spacing: { after: 46, line: 242 } });

const noBorders = {
  top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
  left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
  insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE },
};

// Host photo beside the bio. Borderless two-column table, never a floated image.
const hostBlock = (bioParas) => new Table({
  width: { size: 100, type: WidthType.PERCENTAGE },
  columnWidths: [2400, 7440],
  borders: noBorders,
  rows: [new TableRow({ children: [
    new TableCell({ borders: noBorders, margins: { right: 220, top: 30 },
      children: [new Paragraph({ children: [new ImageRun({
        data: fs.readFileSync(PHOTO), transformation: { width: 128, height: 156 },
      })] })] }),
    new TableCell({ borders: noBorders, verticalAlign: VerticalAlign.TOP, children: bioParas }),
  ] })],
});

const doc = new Document({
  numbering: { config: [{ reference: "gn", levels: [{
    level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: convertInchesToTwip(0.24), hanging: convertInchesToTwip(0.16) } },
      run: { color: MUTE, font: F } } }] }] },
  styles: { default: { document: { run: { font: F, size: SZ, color: INK } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 },
      margin: { top: 660, bottom: 340, left: 1000, right: 1000 } } },
    children: [

      // ---- BANNER: once, at the top. Not a page header. ----
      new Paragraph({
        children: [new ImageRun({ data: fs.readFileSync(BANNER),
          transformation: { width: 624, height: 104 } })],
        spacing: { after: 120 },
      }),

      // ---- HOOK (REPLACE). Contrast or premise, never description. Write last. ----
      p([t("Every breakthrough technology spends years in a state where the science works and the product does not. Most never leave it, and the reasons are rarely scientific. They are cost, manufacturing, regulation, and whether anyone will be the first customer.")]),
      p([t("That conversation happens constantly in private, between the people building a technology and the people deciding whether to fund it. Almost never in public. This show is the private conversation, recorded.")]),

      // ---- WHAT THIS IS (REPLACE) ----
      p([
        t(SHOW, { b: true }),
        t(" is one guest and one unbroken conversation with host "),
        t("Ankit Anand", { b: true }),
        t(", running about an hour. No script, no questions sent in advance, and no dumbing down of the technical material."),
      ], { after: 20 }),

      // ---- WHO COMES ON (REPLACE). Groups, not a ranked sequence. ----
      h1("Who comes on"),
      p([t("People doing the work, not describing it:")], { after: 60 }),
      bullet([t("Building", { b: true }), t(": founders and technical leaders shipping hardware that did not previously exist")]),
      bullet([t("Researching", { b: true }), t(": academics and lab scientists whose work is at the point of leaving the lab")]),
      bullet([t("Scaling", { b: true }), t(": operators who have taken a breakthrough through manufacturing, regulation, and a first customer")]),
      p([t("Across AI, chip design, nuclear power, robotics and space.")], { after: 20 }),

      // ---- WHAT WE TALK ABOUT (REPLACE). Four to six. Close on posture. ----
      h1("What we talk about"),
      bullet([t("The technology itself", { b: true }), t(", at the level you would explain it to a colleague")]),
      bullet([t("Getting out of the lab", { b: true }), t(": what stayed behind, what got out, and what made the difference")]),
      bullet([t("Cheaper, faster, or safer", { b: true }), t(": where the step change is, how big it honestly is, and what breaks at scale")]),
      bullet([t("What the field gets wrong about itself", { b: true }), t(": the commercialisation story everyone repeats and you think is wrong")]),

      // ---- WHY COME ON ----
      // REACH BLOCK: include ONLY if Phase 2 confirmed real numbers. A new show
      // omits it entirely. Never hedge it. When included, always pair the
      // number with who those people are.
      h1("Why come on"),
      bullet([t("A conversation with someone who has been on both sides of the problem, not a promo lap")]),
      bullet([t("Clean video, short clips and the full transcript afterwards, yours to use however you want")]),
      bullet([t("A place among a small, deliberately curated set of people working at the frontier")]),

      // ---- MEET THE HOST (REPLACE) ----
      // Move this above "Why come on" when the host's name is the reason to say yes.
      h1("Meet the host"),
      hostBlock([
        p([
          t("Ankit Anand", { b: true }),
          t(" is a physicist turned deep-technology investor. He studied physics at ETH Zurich and worked on the LIGO-Virgo collaboration, the experiment that first detected gravitational waves. He then helped build "),
          t("Sleepiz", { b: true }),
          t(", an ETH Zurich spinout that developed the first contactless radar-based vital signs monitor, and took it through FDA clearance and European medical device approval."),
        ]),
        p([
          t("He is now a founding partner at "),
          t("Riceberg Ventures", { b: true }),
          t(", an early-stage fund backing breakthrough technologies across six countries, and co-founder of "),
          t("KickSky Space Lab", { b: true }),
          t(". He is not a journalist asking you to explain your work. He is someone who has had to decide, repeatedly, whether work like yours becomes a business."),
        ], { after: 0 }),
      ]),

      // ---- FORMAT AND LOGISTICS (REPLACE) ----
      // The control line must match what Phase 2 confirmed. Do not assume.
      h1("Format and logistics"),
      bullet([t("Wherever you are.", { b: true }), t(" In person if Ankit is in your city, remote on video if not")]),
      bullet([t("We block ninety minutes", { b: true }), t(", and the episode runs about an hour")]),
      bullet([t("Nothing to prepare.", { b: true }), t(" No script, no questions in advance")]),
      bullet([t("You get the assets", { b: true }), t(": video, short clips and the full transcript, unrestricted")]),
      bullet([t("You keep control.", { b: true }), t(" Anything you would rather not have published is cut before release")]),

      // ---- CLOSING LINE (REPLACE). One italic sentence that actually asks. ----
      new Paragraph({
        children: [t("Building or researching something at the edge of what is possible? Get in touch and we will find a time.")],
        spacing: { before: 110, after: 40, line: 242 },
        border: { top: { style: BorderStyle.SINGLE, size: 5, color: HEAD, space: 8 } },
      }),
      p([t("linkedin.com/in/anandvankit   \u00b7   riceberg.vc", { color: MUTE })], { after: 0 }),
    ],
  }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync(OUT, b);
  console.log('written:', OUT);
});
