# WA-Blurb rename (decision 342): deploy steps for Main

Prepared by the misc session, 19 Oct 2026. Nothing below is live yet.

Why: Akshay renamed the FT Community WhatsApp intro to WA-Blurb so that "Blurb" alone means the new research profile on People (decision 342). The live WhatsApp and calendar routines find the intro by its Notion property names, so the Notion renames and the new prompts must go live in the same window.

## Already live (misc, 19 Oct)

- People: new Blurb, Guest tier, Research tags, Blurb evidence, Researched.
- Engagements: Blurb is now a rollup of the guest's People Blurb (it held no data).

These don't touch any routine's existing fields.

## To do together, in one window (Main)

1. Pause or wait out the WhatsApp (hourly) and calendar runs.
2. Rename in Notion:
   - FT Community: Blurb -> WA-Blurb; Blurb link -> WA-Blurb link.
   - People: Community blurb (rollup) -> WA-Blurb; Blurb (old copy, retired) -> Old WA-Blurb (retired).
3. Deploy routines/whatsapp.md (24,720 B) and routines/calendar.md (52,173 B) from this branch. Read back the live prompts and check they match.
4. Edit the Notion rule page "Blurb sources" (3fc19a301a7f81eb9bcfc36f3a1cd6a9): the field is WA-Blurb, and new page-body sections are headed "WA-Blurb, <date>". Old "Blurb, <date>" sections still count.
5. routines/community-directory.md only changes its never-copy list (WA-Blurb, Blurb). Deploy it with the rest or at the next touch.
6. Watch one WhatsApp run and one calendar run.

## What changed in the routine text

- Property names: Blurb -> WA-Blurb and Blurb link -> WA-Blurb link, on FT Community only.
- New page-body sections are headed "WA-Blurb, <date>". Older "Blurb, <date>" sections are still read.
- Next action labels now read "WA-Blurb: <page URL>".
- "Never write People's blurb fields" now names Blurb, WA-Blurb and Old WA-Blurb.

## Not changed

- Decision 331's sourcing rules.
- The founder-thesis-blurb skill. It writes text and never names the field.
