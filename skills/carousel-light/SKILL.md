---
name: carousel-light
description: >-
  Convert a podcast transcript into a ready-to-post LinkedIn PDF carousel
  in the Editorial Navy quote-card format: cover with guest photo and stat
  hook, 4 big-quote cards each with a supporting message, and a CTA card
  with episode link. Theme routing per show: Built to Share carousels are
  about talent, ESOPs, and org building; un# about DeFi and crypto;
  Founder Thesis about scaling up; Human by Design about AI. Trigger on
  "/carousel-light", "carousel light", "make a carousel from this episode",
  "quote carousel", "carousel PDF", "Editorial Navy carousel", or whenever
  the user supplies a transcript and wants a finished, designed carousel
  file rather than a copy deck. Output is a rendered PDF of 1080x1080
  cards, not a markdown brief. For illustration-based playbook copy decks
  handed to a designer, use playbook-carousel; carousel-light is the
  ship-it-yourself path.
---

# Carousel Light

Turn an episode transcript into a finished Editorial Navy PDF carousel. The reference standard is the Ravi Saxena deck: navy cards, orange accent, big cream quotes, grey supporting message, hissa/show chrome, SWIPE chevrons.

## Inputs

1. **Transcript** (required). The only legitimate source for quotes. Read it fully.
2. **Show** (required). Built to Share, un#, Founder Thesis, or Human by Design. Infer from host name in the transcript or project context; ask if ambiguous.
3. **Dossier** (optional). For verifying numbers and cover-hook stats.
4. **Guest photo** (optional). If the user provides an image file, pass its path as `cover.photo`. If not, the cover renders a placeholder frame; flag it in the handoff.

## Step 1: Load the show profile

Read `references/show-profiles.md` and pick the matching show. The profile gives:

- **Theme territory.** Extract quotes ONLY from this space. A great quote off-theme is still off-theme. Built to Share wants talent and ownership; un# wants DeFi; Founder Thesis wants scaling; Human by Design wants AI.
- **Brand chrome JSON** (logo, wordmark, attribution, colors).
- **CTA link pattern and label.** Never invent an episode URL; if the profile says ask, ask.

## Step 2: Mine the transcript for quotes

Find 6-8 candidates inside the show's theme territory, then cut to the best 4. A qualifying quote:

- Is the guest's own words, verbatim or minimally cleaned (fillers and false starts removed, meaning untouched, no invented words).
- Is 10-22 words after cleaning. It must read as one complete punchy thought at 55px across 3-5 lines.
- Picks a fight or inverts a default. "Pedestals drag you more than they lead you" beats "hiring is important."
- Has a receipt elsewhere in the transcript or dossier (a number, a decision, an outcome) that the support text can carry.

Selection cuts, in order: no fight, cut. No receipt, cut. Overlapping territory with a stronger quote, cut. Sequence so the most provocative quote is card 2 and the most resonant is the last quote card.

## Step 3: Write the copy JSON

Build the spec for `scripts/build_carousel.py` (the docstring at the top of the script shows the full JSON shape). Copy rules:

**Cover card**
- `name_html`: guest name in caps, line break between first and last name.
- `hook`: 2-3 lines, stat-led, the most impressive verifiable arc ("He built Sodexo India to 28,000 people on $5M. Then Wonderchef to ₹500 Cr.").
- `subhook_html`: 1-2 lines, the twist that earns the swipe.
- `lessons`: the show profile's lessons-line pattern with real numbers.

**Quote cards**
- `quote`: the cleaned verbatim quote. No attribution inside the quote; the footer carries it.
- `support_html`: 3-5 rendered lines (roughly 35-55 words). Converts the quote into a message: context, the receipt, why it matters. Bold exactly one key phrase with `<b>`. Never restate the quote. For un#, this is where jargon gets unpacked for a non-crypto reader.

**CTA card**
- `headline`: "The full conversation goes deeper." (default; vary only if asked)
- `topics_html`: 4-5 episode topics separated by `&middot;`, drawn from material NOT used on the quote cards.
- `link`: per show profile, confirmed or flagged.

**Hard constraints**
- Zero em dashes in copy (the BUILT —2— SHARE wordmark is brand, exempt). Zero hashtags. No hyperbole the transcript can't back.
- Every number verified against transcript or dossier. When they conflict, the guest's own number wins (e.g. Ankit said 93%, dossier said 94.2%: use 93%).
- HTML-escape ampersands and special characters in copy fields.

## Step 4: Render, review, fix

```bash
pip install img2pdf --break-system-packages -q   # if not installed
python3 scripts/build_carousel.py copy.json /home/claude/carousel_build
```

The script renders each card as an exact 1080x1080 PNG via wkhtmltoimage (deterministic; do NOT swap in wkhtmltopdf, its page scaling is unreliable), builds `sheet.png`, and binds the PDF.

**Mandatory:** open `sheet.png` with the view tool and check every card before shipping:
- No text overlapping the footer rule or running off-card.
- Quote fits in 3-5 lines; if it spills to 6+, trim the quote or shorten the support.
- Cover left column ends above the footer; photo frame doesn't touch it.
- Page numbers sequential, chrome consistent.

If anything overflows, edit the copy (shorter is the fix, not smaller fonts) and rerun.

## Step 5: Ship

Copy the PDF to `/mnt/user-data/outputs/` and present it. Handoff message covers, briefly: the quote lineup, anything needing confirmation (photo drop-in, episode link slug), and the strongest benched quotes in case the user wants a swap. No postamble beyond that.

## Defaults and variations

- Default deck: 6 cards (cover + 4 quotes + CTA). The user can ask for 5-7 quotes; the script handles any count, page numbers adjust automatically.
- Fonts are Poppins (body/headlines) and Lora (serif logo, quote mark); both ship in the container's google-fonts directory. If missing, install `fonts-lora` via apt or download from github.com/rsms or google/fonts.
- The user may override palette, title, or quote selection at any point; their instruction beats this skill.
