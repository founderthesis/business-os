---
name: "sow-builder"
description: "Build the client-facing scope of work / agreement document for a podcast production engagement, ready to sign. Trigger on /sow, \"scope of work for X\", \"agreement for X\", \"turn the pitch into an SOW\", or after a pitch is verbally accepted."
---

# Scope of work builder

Produces the signable `.docx` that converts a verbally agreed podcast production deal into a document the client routes through procurement. This is the step AFTER the pitch is won, not a selling document.

The canonical example is `Pathfinders, presented by FieldAssist` (Sep 2026). Match its structure exactly unless the engagement genuinely differs.

## Before you build

Pull the deal facts from call transcripts, the pitch note and project docs first. Do not ask the user for anything you can find yourself. Then confirm only what you genuinely cannot source:

1. **Both legal entities.** The client's registered name and trading name, and which of Akshay's entities is contracting. Never invent a registered name; if you cannot confirm it, put the client's trading name in and flag it.
2. **Show name**, exactly as settled, including any "presented by" construction.
3. **Season length** and release cadence.
4. **What is waived** for this first season and what the standing rate is. The waiver is leverage, so it must be visible as a struck-through figure, never silently absent.
5. **Who the host is**, and whether Akshay appears on the recordings.

## The twelve clauses, in this order

Never renumber, never reorder, never add a clause the deal does not need.

1. **The engagement.** Bullets: who hosts, where it publishes, season length and cadence, the settled show name, any crossover episode, and one line naming what the client said the show is FOR, quoting the call date.
2. **What we deliver for each episode.** A two-column table, asset against where it goes. The house set is: episode trailer (40 to 80 seconds, high energy, motion graphics, built to impress), full episode (video for YouTube, audio elsewhere), thumbnails (YouTube and audio apps, to the style guide), clips (LinkedIn), vertical shorts (Instagram, WhatsApp, YouTube Shorts), carousel (LinkedIn and YouTube), quote cards (LinkedIn and YouTube), SEO article (the episode page), newsletter issue (LinkedIn), thought leadership posts (written for the host, in their voice, from what the guest said).
3. **One-time setup.** Three sub-headings. *Brand and asset kit*: show logo, cover art, YouTube banner and avatar, LinkedIn banner, newsletter banner, thumbnail style guide, lower-third template, carousel template, quote card template. *Channel and distribution*: YouTube channel created or rebranded, LinkedIn page for the show alongside the host's personal profile, audio host and RSS feed with submission to Spotify, Apple Podcasts, YouTube Music, Amazon Music and the rest, LinkedIn newsletter. *Guest note*: the one-pager that books guests, written before the first invite goes out.
4. **Guest sourcing and outreach.** We run it end to end. The client introduces where the relationship is theirs, we carry the thread from that point. Name the shortlist size. State when cold outreach opens.
5. **Recording.** Session length, remote by default with all fees assuming remote, the in-person surcharge per episode, and what is waived.
6. **Investment.** Three tables. See the rate card below.
7. **Paid to third parties.** Everything the client pays directly, each with who holds the account. Ad spend gets its own bullet stating the single purpose and the subscriber goal.
8. **What the client provides.** Host time for recording and pre-interview calls, brand assets and a named creative approver, access to any channel being rebranded, and guest introductions.
9. **Sequence.** Four phases, no dates. Phase 1 on signature: paperwork, brand work, channel setup, guest note. Phase 2: guest outreach, guests briefed and prepped, host prepped through a mock recording. Phase 3: recording, with the opener recorded first and held until three are in the can. Phase 4: launch and repeat, with cold outreach and ads switching on after two or three episodes are live.
10. **Review and continuation.** The review point, the agreed proofs, and a per-episode rate card for what follows.
11. **Ownership.** Client owns the published episodes and all assets. Unnati may reference the work in its portfolio. Note any crossover arrangement.
12. **Agreed.** Two-column signature block, Name / Signature / Date in each.

## The house rate card

Defaults, to be overridden by what the deal actually settled:

| Line | Amount |
|---|---|
| Setup, one-time | Rs 75,000 |
| Post-production | Rs 60,000 per episode |
| Content amplification | Rs 20,000 per episode |
| Guest sourcing | Rs 10,000 per episode, where we source cold |
| Akshay on the recording | Rs 10,000 per episode |
| In-person recording | Rs 10,000 per episode |

So a standard episode is **Rs 80,000** with both optional lines waived, and **Rs 90,000 to Rs 1,10,000** once they apply.

Clause 6 carries three tables:

- **First season.** Every line with its amount and who it is paid to. Waived lines show the struck-through original. A shaded subtotal row for what is payable to Unnati, then third-party lines, then a shaded total engagement value.
- **Add-ons.** Three columns: add-on, per episode, when it applies. Mark anything waived for the first season.
- **Payment terms.** Billing runs on a monthly cycle, invoicing for episodes published in that month. Setup fee on signature, then per-episode monthly. Close with a small-print line: amounts exclusive of taxes, billing begins after signature and vendor registration.

## Building the file

Read the `docx` skill's SKILL.md, then write a Node script using the `docx` npm package. It is preinstalled, so require it directly.

House styling that matches the Pathfinders document:

- US Letter: `page: { size: { width: 12240, height: 15840 }, margin: { top: 1200, bottom: 1100, left: 1440, right: 1440 } }`
- Content width 9360 DXA. Every table needs `columnWidths` summing to that AND a `width` on every cell, both `WidthType.DXA`.
- Palette: ink `1A1A1A`, muted `555555`, accent red `C0182B`, table header band `F1E7D5`, rule `D8CDBA`. Shading must be `ShadingType.CLEAR`.
- Calibri throughout. Body 20 half-points, small print 18, h2 21, h1 26, title 34.
- A red uppercase `SCOPE OF WORK` kicker above the title, then the show name as title, a one-line descriptor, the date, then a paragraph bottom-border as a rule.
- Bullets via a `numbering` config with `LevelFormat.BULLET`. Never type a bullet character.
- Amounts right-aligned with the rupee sign as a literal character, not an escape.

Write the finished file to `/mnt/user-data/outputs/<Show>-Scope-of-Work.docx`.

## Verify before delivering

Render it and look at every page:

```bash
python3 <docx-skill>/scripts/office/soffice.py --headless --convert-to pdf --outdir . out.docx
pdftoppm -jpeg -r 90 out.pdf page
```

Then Read the images. Check the tables are not overflowing, the shaded rows are shaded, and the signature block is intact on the last page.

## Voice

Apply Akshay's writing rules: no em-dashes, short varied sentences, contractions, specifics over generalities, sentence case headers, no puffery. A scope of work is still writing someone reads.

State assumptions rather than hiding them. If the payment schedule was never agreed, write the proposed one and tell Akshay in the reply that it is a proposal.

## What this document is not

No termination clause, liability cap, confidentiality or payment-terms-in-days. This is a scope of work, not a contract. If the client is expecting one document that does both, say so in the reply and suggest it goes past someone who does contracts.

## Keep the plan in step

The SOW is usually built from a launch plan or pitch artifact. Once the client edits and signs the SOW, the signed version becomes the source of truth. Offer to update the artifact to match, and name the specific drifts rather than asking a vague question.