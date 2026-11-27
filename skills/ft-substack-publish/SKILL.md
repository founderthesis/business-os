---
name: ft-substack-publish
description: >-
  Take a Founder Thesis article that's already been drafted in this chat and
  assemble it as a DRAFT in the Substack editor, driving the browser end to end —
  then stop at the Publish button for a human. Use this right after the
  ft-substack-article skill has produced an article, when the user says "publish
  this to Substack", "put this on Substack", "run the publish skill", "draft this
  in Substack", or "load this into Substack". Requires Claude in Chrome (or
  equivalent browser control) with the user logged into founderthesis.com's
  Substack. It formats the body, embeds YouTube and Spotify, adds the hyperlinks,
  sets the social-preview thumbnail, tags, and email setting — everything — and
  then hands off. It NEVER clicks Publish or sends email.
---

# Founder Thesis — Substack publisher

You drive the Substack editor with the browser tools to build a **draft** of the
article that's already in this conversation, then stop. This exists because
Substack has no publishing API — the only way to post is through the editor UI.

## Absolute rule: stop at the draft. Never publish.

Assemble everything, then **stop at the Publish button and hand back to the human.**
- **Never click "Publish now", "Send", "Schedule", or "Continue" past the point
  where the email would go out.** Publishing emails ~1,300 subscribers and cannot
  be undone.
- Your finish line is: a complete draft, saved, with every element in place, and a
  message telling the user it's ready for them to review and hit Publish.
- If at any point you're unsure whether an action publishes or emails, stop and
  ask rather than clicking.

## Before you start

- Confirm you have browser control and the user is **logged into the Substack
  publisher** for founderthesis.com. If not, say so and stop.
- Gather from this conversation (the ft-substack-article output): the **title**
  (the chosen one), **subtitle**, **body** (with block-quotes and the embed
  placeholders), the **YouTube URL**, the **guest name + LinkedIn**, **company +
  website**, the **tags**, the **thumbnail** image, and any **infographic** images.
  If the thumbnail or an infographic image isn't ready yet (they render outside
  chat), note it and leave that step for the user — don't invent an image.
- Then **resolve the podcast platform links** (next section) *before* you touch the
  editor, so Steps 6–7 have real URLs and never guess.

## Resolve the platform links first (do this before editing) — never ask the user to find a URL

**The links now live in Notion.** The "Episode Inventory" database has a
**`Spotify URL`** and an **`Apple URL`** column, filled for most episodes. Read them
from there first — that is the source of truth and needs no searching. **The user
should never have to go find a link.**

1. **Look up the episode's row in Notion "Episode Inventory"** (match on the
   **YouTube URL** — exact and reliable — or failing that the episode title). Take:
   - **`Spotify URL`** → the episode share link (`open.spotify.com/episode/<id>`)
   - **`Apple URL`** → the exact Apple episode link
   Coverage today: Spotify is filled for essentially all Founder Thesis episodes;
   Apple for roughly the 300 most recent across both shows. If a cell is filled, use
   it as-is and do no further searching.

2. **If `Apple URL` is empty**, resolve it from the public iTunes API (no login):
   `https://itunes.apple.com/lookup?id=1509981658&entity=podcastEpisode&limit=200`
   (`1509981658` = Founder Thesis; **The Spotlight** show is `1516229286`). Find the
   episode whose `trackName` contains the **guest or company name**, take
   `trackViewUrl`, strip any trailing `&uo=4`. No confident match → use the show link
   `https://podcasts.apple.com/us/podcast/founder-thesis/id1509981658` and flag it.

3. **If `Spotify URL` is empty**, use the Founder Thesis show link
   `https://open.spotify.com/show/4OWyibZXvObwJQNIN8zyTJ` and flag it for the user.
   Do **not** browse Spotify hunting for the episode — that is what used to fail and
   loop.

4. **Amazon Music** has no stored column and no usable API. Use the fixed show link
   `https://music.amazon.com/podcasts/87162f1d-3b37-4a9a-a8fa-fd10ee6b274a/founder-thesis`
   unless an episode-exact Amazon URL is already in this chat or the draft.

**Share link vs embed link — important.** Use the **share** form
(`open.spotify.com/episode/<id>`) everywhere in Substack: pasted on its own line it
auto-converts into a player. The `/embed/episode/<id>` form (also available in Notion
as the derived **`Spotify embed URL`** column) is only for hand-written `<iframe>`
HTML and will render as a dead link if pasted into the Substack editor. **Never paste
the embed URL into Substack.**

Record: **Apple episode URL**, **Spotify URL**, **Amazon URL**, plus anything you had
to fall back on. You'll use these in Step 6.

## The steps

Work one step at a time. After each, do **one** read (page or screenshot) to confirm
it worked, then move on. Find controls by their visible label/role, not by fixed
coordinates — the editor layout shifts. If a control isn't where expected, read the
page and adapt.

**Anti-loop rule (important).** Never repeat the same step more than **twice**. If a
control, an embed, or a confirmation hasn't succeeded after two attempts, **leave
that one piece, note it for the handoff, and move to the next step.** Do not
re-read or re-click the same element waiting for a state that isn't changing, and
never poll for a "Saved"/success state in a loop — one check is enough. Getting
stuck repeating a step is a bug, not diligence.

1. **Open a new post.** Go to the Substack dashboard and start a new post
   (Posts → New post, or the publisher's new-post URL). Wait for the editor.

2. **Author = Akshay Datt.** If there's a byline/author control, set it to Akshay
   Datt. (It's usually already the default; verify.)

3. **Title and subtitle.** Put the chosen title in the title field and the
   subtitle in the subtitle field.

4. **Body.** Paste the article body into the editor. Then fix formatting:
   - **Quotes → block quotes.** For each pull-quote, select it and apply the
     block-quote style (the editor's quote button, or the `"` control).
   - Preserve the headings as H2s.

5. **Embed the YouTube episode.** At the top of the body (where the article marks
   the embed), paste the **full** YouTube URL on its own empty line and let
   Substack auto-convert it to an embedded player. A short link will NOT
   auto-embed — use the full `youtube.com/watch?v=…` URL. Confirm the player
   appears.

6. **Spotify player + "Listen on" links.**
   - **Embed Spotify.** If the `Spotify URL` from Notion is an **episode** link
     (`open.spotify.com/episode/<id>` — it will be, for almost every Founder Thesis
     episode), paste it **on its own empty line** where the article marks the Spotify
     embed and let Substack auto-convert it to a player. Confirm once; if it hasn't
     embedded after one retry, leave the bare URL and move on. Use the **share** URL,
     never the `/embed/` form — that renders as a dead link here.
     If you only have the **show** link, do *not* embed a show player: keep Spotify as
     a plain hyperlink on the "Listen on" line instead, and flag it.
   - **"Listen on" line.** Add the remaining links as hyperlinks — **Apple Podcasts**
     (exact episode) and **Amazon Music** (show link) — plus Spotify if it wasn't
     embedded above. Select the anchor text, use the link control, paste the URL.
   - Use the URLs you already resolved; do **not** go looking for any of them now.

7. **Guest & company hyperlinks.** In the body, link the **guest's name** to their
   LinkedIn profile and the **company name** to the company website.

8. **Infographics.** Insert each infographic PNG at the spot the article marks for
   it (upload image at that point in the body). Skip any image that isn't ready and
   note it.

9. **Thumbnail / social preview.** Go to the post settings (the "Continue" /
   settings step) and upload the thumbnail image. The FT thumbnail is produced at
   **1260 × 900 (7:5)** to fill Substack's **420 × 300** slot at 3× so it stays sharp
   after downscaling — upload it as-is, don't resize or crop it. If Substack offers a
   crop control, keep the whole frame (the design has text at the left edge and the
   guest at the right; cropping cuts one of them). Do **not** proceed past settings
   into publishing.

10. **Tags.** Add the 1–3 tags from the article (exactly as given).

11. **Audience & email.** Audience = **Everyone**. For the **email** setting: send
    as email **only if this is the one weekly Founder Thesis episode**; for
    back-catalogue / extra posts, set it to **no email** (publishing to web only).
    If unsure which this is, ask the user before setting it.

12. **Stop — the draft is done.** Substack **autosaves**, so there is nothing to
    click to save and **no "Saved" state to wait for.** Take **one** final
    screenshot of the draft, then **STOP.** Do not re-open the body, do not re-check
    earlier steps, do not poll for a save/success state, and never click Publish or
    Schedule. One screenshot, then hand off.

## When done

Tell the user, plainly:
- The draft is built and saved in Substack, with a link to it.
- A quick checklist of what you set (title, YouTube/Spotify embeds, Apple/Amazon
  links, thumbnail, tags, email on/off) and **anything you left for them** (a
  missing image, any platform link you couldn't resolve — Spotify/Apple/Amazon —
  the email toggle).
- That the last step — hitting **Publish** — is theirs.

Then stop and let them review.

## Lessons

- 2026-11-27 (Akshay with Ranjita, call 27 Nov 20:10 JST): every title carries the founder's name and the company name (SEO). Add imagery: license-free images or an image prompt showing the product in real life (e.g. an EV auto with the Fyn Mobility logo), never a dry text-only post. The preview image must be the right size; to get one, give Claude a previous thumbnail as the example and ask for the prompt. Ranjita decides keep or cut on anything sensitive or off the record. No editing inputs from the guest before publishing (decision 645).
