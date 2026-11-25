---
name: review-dashboard
description: Convert a social-media engagement export for any client on any platform (X, LinkedIn, Instagram, YouTube) into one self-contained HTML dashboard. Trigger on "/review-dashboard", "make an engagement dashboard", "dashboard from this data", "visualize these [platform] stats for [client]", "turn this social export into a dashboard", or when the user pastes/uploads per-post engagement data (Google Sheets HTML export, CSV, or a pasted table with metrics like likes, views, reactions, comments, retweets plus post links) and wants it charted. Parses row-level records, ignores embedded weekly/monthly subtotal rows, splits merged rows, buckets by week, computes weekly and overall totals plus the mean of the headline metric and a top-5 star list, then renders a bright Apple-system-font dashboard: dataset toggle (e.g. posts vs replies), stat cards, a mean card with an animated 3D flip-tile trend, a bar-and-curve chart with metric chips, a weekly table, and star lists. Metrics and client handle adapt per platform.
---

# Review Dashboard

Turn a messy social export into the locked dashboard design: bright, Apple-system-font, one self-contained HTML file.

## Inputs it accepts
One row per post (or reply/comment) with a date, one or more engagement metrics, and a post URL. Common forms:
- Google Sheets "download as web page" / published HTML (links live inside `<a>` tags in cells)
- CSV / TSV
- A pasted plaintext table

Exports usually also contain **week-header rows** ("Week of ..."), **weekly subtotal rows**, and a **monthly total row**. These are not data. Exclude them from row-level parsing and recompute totals yourself.

Platforms differ in metrics: X (retweets, likes, views), LinkedIn (reactions, comments, reposts, impressions), Instagram (likes, comments, saves, reach), YouTube (views, likes, comments). The skill is metric-agnostic; you define the metric set per job.

## Workflow — 3 phases

### Phase 1 — Read a preview, confirm config (STOP)
Open the file and read enough to see the columns and shape. Then confirm with the user, inferring defaults and asking only what's genuinely ambiguous (use `ask_user_input` for discrete choices, max 3 questions):
- **Client** display name and handle (e.g. `@srimisra`)
- **Platform** (X, LinkedIn, Instagram, YouTube...)
- **Datasets**: one, or several (e.g. Posts + Replies) — each becomes a segmented-control tab
- **Metrics present** and their friendly labels, left-to-right
- **Headline metric**: the hero number and the metric the mean, tiles, chart default, and star ranking use. Default to "Total engagement". If the export has no total column, compute it as the sum of the component metrics.

Do not proceed to a full build until the config is confirmed.

### Phase 2 — Parse and compute
Use `scripts/parse.py` as a starting toolkit and adapt the row-filter to the actual file. Non-negotiable rules:
- Keep only rows with a valid post URL and at least one numeric metric.
- Drop header, "Week of", "Total weekly", and "Total monthly" rows.
- Split merged rows — a row with two URLs is two records; slice the numeric run into per-record chunks.
- Bucket by explicit "Week of X" headers when present; otherwise derive the ISO-week label from the date column.
- **Compute weekly sums, overall totals, the headline mean per item, and the top-5 stars entirely from row-level data.** If the sheet's printed weekly/monthly totals don't reconcile with your computed numbers, trust the computed numbers and flag the discrepancy to the user in chat.
- Assemble the `DASH` object via `build_dataset()` + `build_dash()`, then `inject()` it into the template.

### Phase 3 — Build and present
Write the filled template to `/mnt/user-data/outputs/<handle>-<platform>-dashboard.html`, `present_files` it, and give a 2-3 line summary of what's in it plus any data caveats (date range, mixed handles, totals that didn't reconcile). Offer the offline option: the chart loads Chart.js from a CDN, so mention you can inline the library if they need it to work with no connection.

## Design (locked — match the reference, don't redesign)
- Background `#F5F5F7`, cards `#FFFFFF`, ink `#1D1D1F`, muted `#6E6E73`, lines `#E5E5EA`.
- Font: Apple system stack, no webfont. Numbers use tabular figures and thousands separators.
- Headline accent `#FF5D2E`. Other metrics draw from this palette in order: `#0A84FF` (blue), `#FF9F0A` (orange), `#30D158` (green), `#BF5AF2` (purple), `#FF2D55` (pink).
- Component order: header + dataset segmented toggle (hidden if one dataset) -> four stat cards (headline hero + up to three metrics) -> "Average per item" card = big mean number beside a row of 3D flip-tiles (one per week, height scaled to that week's headline value, staggered `rotateY` spin, front/back faces) -> "Weekly performance" bar-and-curve combo chart with metric chips, defaulting to the headline -> weekly table with a bold total row -> "Star posts/replies" top-5 with clickable links.

## Copy rules (avoid AI tells)
- Section headings only. No explainer sub-paragraphs under headings, no footer prose beyond a one-line source note.
- Use neutral "Star posts" / "Star replies" framing. Do **not** write narrative callouts like "one post carried the month".
- No median or mode. Mean only, shown as a plain number.

## Output
A single self-contained HTML artifact in `/mnt/user-data/outputs`. The only external dependency is the Chart.js CDN; everything else is inline.
