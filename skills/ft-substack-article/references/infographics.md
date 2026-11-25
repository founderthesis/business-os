# Infographics — decide, then generate

The article can carry FT-themed infographics, but **only where its own content
supports one.** This file is the decision logic and the templates. Read it during
the writing pass, decide honestly, and generate 0–2 charts per article.

## The bar: when does the article warrant an infographic?

Make one only if ALL of these are true for the data in question:

1. **The numbers are real and verified** — from the transcript or cited research,
   the same standard as the body. Never chart an estimate as if it were fact; if a
   figure is a third-party estimate, don't build a chart around it.
2. **There are enough data points to be worth a picture** — a single vague number
   is a sentence, not a chart. See each template's minimum below.
3. **It carries the story** — the visual should make the article's core point land
   faster (the growth, the arc, the scale, the contrast). If it just decorates,
   skip it.

If the data doesn't clear the bar, **make no infographic.** A weak chart is worse
than none. Most articles get one; some get two; some get zero. That is correct.

## Which template for which data

| The article contains… | Use | Minimum |
| --- | --- | --- |
| A number series over time or across categories (revenue by year, funding rounds, users growing) | **Bar chart** | 3+ real values |
| A dated sequence of milestones (founded → pivot → raise → exit) | **Timeline** | 3+ dated events |
| One dominant, impressive figure (a $1B valuation, a ₹144cr exit, 65M users) | **Stat card** | 1 hero number that clears the $10M / ~₹80cr bar (or a huge non-money figure like users/GMV) |
| Two comparable things with numbers (company vs competitor, before vs after, India vs China share) | **Comparison bars** | 2–4 values that are genuinely comparable |

Pick the ONE that best carries the story; add a second only if it shows something
different. Never chart the same data two ways.

## The $10M rule applies to stat cards

A **stat card** exists to make one number feel big — so its number must clear the
$10M / ~₹80cr bar (money), or be a genuinely large non-money figure (millions of
users, large GMV). A stat card built around a $2M seed undercuts the brand; if the
hero number is small, use a different template (a bar chart of the *growth* is fine,
because there the story is the climb, not the absolute figure).

## FT theme (all templates)

- Background ink `#14101b`; text white `#ffffff`; muted `#9a95a3`; gridline `#2e2a36`
- Brand red `#d81e26` (bars, accents); darker `#b0161d` for gradient bottoms
- Headline / big numbers: heavy **sans** — `-apple-system,"Helvetica Neue",Arial,sans-serif`, weight 800, letter-spacing -0.5px
- Labels / body: same sans, normal/medium weight
- Card 1200px wide; height 760–900px depending on template
- Footer on every chart: the logo (via the `{{FT_LOGO}}` token) bottom-left, a
  "Source: …" note bottom-right

## How to generate + render

1. Write the filled template HTML to a file (data baked in as inline styles/values
   — no client-side JS; the renderer blocks scripts). Use the `{{FT_LOGO}}` token
   for the logo `src`.
2. Render to PNG: `scripts/render.sh <file.html> <out.png> <width> <height>`.
   The script injects the logo and produces a retina PNG ready to upload to
   Substack. (Render needs Chrome, so it runs wherever Chrome is — see SKILL.md.)
3. Deliver the PNG alongside the article, noting where it goes in the body.

Every chart: compute bar heights proportionally to the real values (tallest bar
≈ the template's max height; floor tiny bars at ~16px so they stay visible), and
label the source.

---

# Template blueprints

Fill the data, keep the structure. All share this `<head>`:

```html
<style>
  :root{--ink:#14101b;--red:#d81e26;--red2:#b0161d;--paper:#fff;--muted:#9a95a3;--grid:#2e2a36}
  *{margin:0;padding:0;box-sizing:border-box}
  html,body{background:#fff}
  .card{width:1200px;background:var(--ink);padding:60px 72px 52px;color:var(--paper);
    font-family:-apple-system,"Helvetica Neue",Arial,sans-serif;display:flex;flex-direction:column}
  .kicker{font-size:20px;letter-spacing:.14em;text-transform:uppercase;color:var(--red);font-weight:700}
  h1{font-weight:800;letter-spacing:-.5px;font-size:50px;line-height:1.08;margin-top:14px;max-width:1000px}
  .sub{font-size:22px;color:var(--muted);margin-top:14px}
  .foot{display:flex;justify-content:space-between;align-items:center;margin-top:28px;height:64px}
  .foot .logo{height:64px;width:64px;border-radius:12px;overflow:hidden}
  .foot .logo img{height:100%;width:100%;object-fit:cover;display:block}
  .srcnote{font-size:16px;color:var(--muted)}
</style>
```

Footer (identical on all four):
```html
<div class="foot">
  <span class="logo"><img src="{{FT_LOGO}}"></span>
  <div class="srcnote">Source: …</div>
</div>
```

### 1. Bar chart  (render 1200×860)
```html
<div class="card" style="height:860px">
  <div class="kicker">COMPANY · METRIC</div>
  <h1>One-line takeaway with the arc</h1>
  <div class="sub">What the axis is — one clarifying line</div>
  <div style="flex:1;display:flex;align-items:flex-end;gap:56px;margin-top:44px;padding-bottom:12px;border-bottom:2px solid var(--grid)">
    <!-- one .col per bar; height ∝ value, tallest ≈ 300px, floor 16px; use class "bar dim" for a down year -->
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%">
      <div style="font-weight:800;font-size:34px;margin-bottom:14px">VALUE</div>
      <div style="width:100%;border-radius:12px 12px 0 0;background:linear-gradient(180deg,var(--red),var(--red2));height:XXXpx"></div>
      <div style="margin-top:16px;font-size:23px;color:var(--muted);font-weight:600">LABEL</div>
    </div>
    <!-- …more cols… -->
  </div>
  <!-- footer -->
</div>
```
(A "down" bar uses `background:linear-gradient(180deg,#4a4550,#3a3640)` so red always = up.)

### 2. Timeline  (render 1200×820)
```html
<div class="card" style="height:820px">
  <div class="kicker">COMPANY · THE ARC</div>
  <h1>From X to Y</h1>
  <div style="flex:1;margin-top:48px;display:flex;flex-direction:column;justify-content:center;gap:0">
    <!-- one row per milestone: a red node + year + event -->
    <div style="display:flex;align-items:flex-start;gap:28px;padding:18px 0;border-left:3px solid var(--grid);margin-left:8px;padding-left:36px;position:relative">
      <span style="position:absolute;left:-11px;top:24px;width:19px;height:19px;border-radius:50%;background:var(--red)"></span>
      <div style="font-weight:800;font-size:30px;min-width:120px">YEAR</div>
      <div style="font-size:26px;line-height:1.3">EVENT — one line</div>
    </div>
    <!-- …more rows… -->
  </div>
  <!-- footer -->
</div>
```

### 3. Stat card  (render 1200×760)
```html
<div class="card" style="height:760px">
  <div class="kicker">COMPANY</div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <div style="font-weight:800;letter-spacing:-2px;font-size:200px;line-height:.9;color:var(--red)">₹144cr</div>
    <div style="font-size:38px;font-weight:800;margin-top:10px">what the number is</div>
    <div class="sub" style="font-size:24px;max-width:900px">one line of context that makes it land</div>
  </div>
  <!-- footer -->
</div>
```

### 4. Comparison bars  (render 1200×760)
```html
<div class="card" style="height:760px">
  <div class="kicker">COMPANY vs COMPANY  (or  BEFORE vs AFTER)</div>
  <h1>The contrast in one line</h1>
  <div style="flex:1;display:flex;align-items:flex-end;gap:120px;margin-top:44px;padding:0 60px 12px;border-bottom:2px solid var(--grid)">
    <!-- 2–4 cols, same bar mechanic as the bar chart; give the FT/hero side red, the other a muted grey -->
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%">
      <div style="font-weight:800;font-size:40px;margin-bottom:14px">VALUE</div>
      <div style="width:100%;border-radius:12px 12px 0 0;background:linear-gradient(180deg,var(--red),var(--red2));height:XXXpx"></div>
      <div style="margin-top:16px;font-size:24px;color:var(--muted);font-weight:600">LABEL</div>
    </div>
    <!-- the other side uses grey: background:linear-gradient(180deg,#4a4550,#3a3640) -->
  </div>
  <!-- footer -->
</div>
```
