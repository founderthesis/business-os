# Thumbnail — the ChatGPT image prompt (dark red FT style)

The FT thumbnail is generated in **ChatGPT (image generation)** from the guest's
photo. So the skill's job is to **output one ready-to-paste ChatGPT prompt** that
produces the FT look, plus the candidate hook lines. The user attaches the founder
photo and runs the prompt.

**The look is DARK, not white.** Deep oxblood/near-black background with a soft red
bokeh glow, a `FOUNDER THESIS ✕ GUEST` lockup, a red category pill, a big condensed
white all-caps headline, a one-line subtitle, `founderthesis.com` bottom-left, and
the guest's cut-out on the right. (This replaces the old light-grey-background
prompt — never spec a white/light background.)

**Fonts (what we decided):** the headline is a **heavy condensed sans-serif, all
caps** (Anton / Druk style); supporting text is a **clean sans-serif**. Never serif.
Name the font style in the prompt so ChatGPT gets close.

## What the skill delivers

- The **5 thumbnail hook lines** (short, 2–5 words, punchy, one emotional/category
  punch). The **$10M rule** applies: a number headlines the thumbnail only if it
  clears $10M / ~₹80cr.
- **One ready-to-paste ChatGPT prompt** built around the strongest hook, with the
  `COMPANY · CATEGORY` pill and subtitle filled. Any of the 5 hooks can be swapped
  into the `{HEADLINE}` slot.

## The prompt template (fill the slots, output verbatim for pasting)

> Create a podcast episode thumbnail with a **7:5 landscape aspect ratio, rendered at 1260 × 900 px**,
> in a dark, premium, high-contrast style, using the attached photo of
> **{FOUNDER NAME}**.
>
> **Background:** deep near-black oxblood (very dark red-black, around #1a0406) with
> a soft, out-of-focus **red bokeh glow** toward the right — blurred circular red
> lights, cinematic and subtle. No texture, no noise, no gradient banding.
>
> **The photo:** cut **{FOUNDER NAME}** out cleanly and place them on the **right
> third** of the frame, head and shoulders, **facing forward toward the viewer**,
> fully inside the frame with **nothing cropped at the top of the head**. **If the
> source photo has them in a specific or awkward pose — side profile, looking away,
> head tilted, or turned to one side — reorient them to a clean, natural
> front-facing head-and-shoulders pose.** Keep their real face and likeness exactly
> — do not change their features, age, or expression, only their orientation. Blend
> the cut-out edge softly into the dark background.
>
> **On the left,** stacked top-to-bottom with generous margins:
> - A small line at the top, white, uppercase, letter-spaced: **FOUNDER THESIS ✕
>   {GUEST NAME}** — render the "✕" in red (#d81e26).
> - A small **red rounded-rectangle pill** (#d81e26) with white uppercase bold text:
>   **{COMPANY} · {CATEGORY}**.
> - A large headline in a **heavy condensed sans-serif (Anton / Druk style), ALL
>   CAPS**, white, left-aligned, very tight line spacing, 2–3 lines:
>   **"{HEADLINE HOOK}"**.
> - A one-line subtitle below, clean medium-weight sans-serif, light grey-white:
>   **{SUBTITLE}**.
> - At the very bottom-left, small white bold text: **founderthesis.com**.
>
> **Safe area:** keep the headline, the guest's face and the `founderthesis.com` line
> within the middle ~70% of the height, with generous empty margin top and bottom.
> (Substack's social-preview slot is a wider 1.91:1 crop of this same image, so
> anything near the top or bottom edge gets cut off when the link is shared.)
>
> Modern startup-media style: bold, minimal, high-contrast. No borders, no drop
> shadows on the text, no extra icons or logos, no watermark. Crisp, legible type.

Then add, on its own line after the prompt, for the user:

> *Attach the founder's photo before sending. Substack's thumbnail slot is **420 × 300**
> (7:5) — generate at **1260 × 900** (same ratio, 3× for retina) and let Substack
> downscale, so it stays sharp. It's text-heavy, so if ChatGPT misspells any word,
> reply "fix the text to read exactly: …" and keep the rest.*

## Worked example (Upstox / Raghu Kumar)

> Create a podcast episode thumbnail, 7:5 landscape rendered at 1260 × 900 px, in
> a dark, premium, high-contrast style, using the attached photo of **Raghu Kumar**.
> Background: deep near-black oxblood (around #1a0406) with a soft out-of-focus red
> bokeh glow toward the right. Cut Raghu Kumar out cleanly and place him on the right
> third, head and shoulders, **facing forward toward the viewer** (reorient to a
> clean front-facing pose if the source photo has him in a side or awkward pose),
> nothing cropped at the top of the head; keep his real face and likeness exactly.
> On the left, top to bottom: a small white
> uppercase line **FOUNDER THESIS ✕ RAGHU KUMAR** (the ✕ in red #d81e26); a red
> rounded pill (#d81e26) reading **UPSTOX · FINTECH** in white uppercase bold; a
> large heavy condensed all-caps white headline (Anton/Druk style), tight leading,
> **"COMMISSION-FREE INVESTING"**; a one-line light-grey subtitle **Building India's
> commission-free investing app**; and **founderthesis.com** small and white at the
> bottom-left. Modern startup-media style, bold and minimal, no borders, no shadows,
> no extra logos. *(attach Raghu's photo)*

## Notes

- Keep the thumbnail hook different-but-consistent with the article title — punchier
  and shorter than the SEO title.
- One or two words of the headline may go red (#d81e26) for punch if it helps, but
  the reference look is an all-white headline against the red-lit dark — default to
  white.
- It's a legitimate promotional thumbnail of a consenting podcast guest; use the
  real photo, don't invent a likeness.
