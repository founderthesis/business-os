---
name: ft-substack-thumbnail
description: >-
  Take the Founder Thesis thumbnail prompt that the ft-substack-article skill just
  produced, run it in ChatGPT's image generator with the guest's photo attached, check
  the rendered text is spelled correctly, and hand back the finished PNG. Use this
  right after an FT article has been drafted, when the user says "make the thumbnail",
  "generate the thumbnail", "run the thumbnail prompt", "create the FT thumbnail", or
  "do the thumbnail in ChatGPT". Requires Claude in Chrome with the user logged into
  chatgpt.com, and the guest's photo available as a local file. It drives ChatGPT only
  — it never publishes anything.
---

# Founder Thesis — thumbnail generator

You run the FT thumbnail prompt in **ChatGPT image generation** through the browser,
then **verify the text** before handing the image over. Image models misspell text,
and this card is text-heavy — so the check is not optional, it is the point of this
skill.

## Before you start

1. **Browser control + login.** Confirm you have Claude in Chrome and the user is
   logged into **chatgpt.com**. If not, say so and stop.
2. **The prompt.** Take the ready-to-paste thumbnail prompt from this conversation
   (the ft-substack-article output). If it isn't here, ask the user to paste it, or
   rebuild it from `ft-substack-article/references/thumbnail.md`. Never invent a
   different design.
3. **The guest's photo.** You need a local image file of the guest. If the user hasn't
   given one, ask for the path. Do **not** substitute a stock photo or generate a
   likeness — it must be the real person.
4. **Record the exact strings** the image must contain, from the prompt:
   - `FOUNDER THESIS ✕ {GUEST NAME}`
   - the pill: `{COMPANY} · {CATEGORY}`
   - the headline
   - the subtitle
   - `founderthesis.com`
   You will check the render against these letter for letter.

## The steps

**Anti-loop rule.** Never repeat an action more than twice. Image generation takes
30–60 seconds — wait patiently in a few long waits, do not poll in a tight loop. If
something hasn't worked after two attempts, stop and hand back to the user with what
you have.

1. **Open a fresh ChatGPT chat.** Go to `chatgpt.com` and start a **new** chat, so no
   earlier context bleeds into the image. Don't touch any existing conversation.

2. **Attach the guest's photo.** Use the attach/upload control and select the local
   photo file. Confirm the thumbnail of the attachment appears in the composer before
   continuing.

3. **Paste the prompt and send.** Paste the full prompt verbatim — do not paraphrase,
   shorten, or "improve" it. Send.

4. **Wait for the image.** Give it a long wait (~30s), then check; if it's still
   generating, wait again (~30s) and check once more. Image generation is slow; that
   is normal, not a failure.

5. **Verify the text — the important step.** Zoom into the generated image and read
   every text element. Compare against the exact strings you recorded. Check:
   - Guest name spelled correctly, company and category correct
   - Headline exact (this is where models most often slip)
   - `founderthesis.com` correct — not "founderthesis.com" variants, no missing letters
   - No invented extra words, no duplicated/garbled letterforms

   Also sanity-check the design: dark oxblood background (**never white/light**),
   guest facing forward on the right, nothing cropped off the top of their head, the
   text within the middle ~70% vertically.

6. **If anything is wrong, correct it once — precisely.** Reply in the same ChatGPT
   chat naming the exact fix, e.g.
   *"Fix the text to read exactly: COMMISSION-FREE INVESTING. Keep everything else
   identical."*
   Then re-verify (step 5). **Allow at most two correction rounds.** If the text is
   still wrong after that, stop and hand back to the user — say plainly which text is
   wrong rather than passing off a broken card.

7. **Save the image.** Download the generated image (ChatGPT's download control). It
   lands in the browser's default download folder. Note the filename and tell the user
   where it is, so the publish step can pick it up.

## Deliver

Tell the user:
- The thumbnail is generated and **what you verified** — list the text you checked and
  confirm it matches.
- Where the file is (folder + filename).
- Anything still off that you couldn't fix in two rounds, stated plainly.
- That it's ready to hand to `ft-substack-publish`, which uploads it to the Substack
  draft (7:5 / 1260×900, upload as-is, don't crop).

## Never

- Never accept an image with misspelled text and call it done — flag it instead.
- Never generate or alter the guest's likeness; use their real photo, and only change
  their orientation as the prompt specifies.
- Never send anything, post anything, or change settings in the user's ChatGPT
  account. Generate the image and leave.
- Never fall back to a white/light background — the FT design is dark.
