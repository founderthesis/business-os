# ft-substack-article: plain editorial headings (9 Nov)

Why: Akshay and Ranjita rejected question-style H2s on the InfoBay article as reading gamed for SEO. Zoya (copy) proposed these exact edits. They cover the heading rule only. The skill lives in Akshay's account, not in this repo, so Akshay applies them.

## Prompt to paste into a claude.ai chat that has the ft-substack-article skill

```
Use skill-creator to update my ft-substack-article skill. Make exactly these 7 edits, change nothing else, then give me the updated skill to install.

1) SKILL.md, Step 2. Replace:
- **Outline** — the H2 sections, each phrased as a **question people actually ask**
  ("How did X reach $Y?", "Why did the founder walk away?"). See
  `references/seo-aeo.md`.
with:
- **Outline** — the H2 sections as **plain editorial headings that name the
  entities** ("From EduGorilla to InfoBay.AI", "The founder who lost to Byju's").
  No search-phrase or question headings, unless the question is how a reader would
  really phrase it. SEO lives in the answer-first opening, the entity naming and each
  section's first sentence. See `references/seo-aeo.md`.

2) SKILL.md, Step 3. Replace:
3. **Question-shaped H2s** every 200–300 words.
with:
3. **Plain editorial H2s that name the entities** every 200–300 words. Each section's first sentence states the fact the section answers.

3) SKILL.md, Step 4. Replace:
- Are the H2s phrased as real questions people ask?
with:
- Do the H2s read as plain editorial headings that name the entities, with no search-phrase or question headings, and does each section's first sentence state its answer?

4) SKILL.md, Step 4. Replace:
opening, add the missing answer sentence, re-cut a heading into a question,
with:
opening, add the missing answer sentence, put the fact into a section's first sentence,

5) SKILL.md, Final checklist. Replace:
- [ ] H2 every 200–300 words, phrased as questions
with:
- [ ] H2 every 200–300 words: plain editorial headings that name the entities, no search-phrase or question headings; each section's first sentence states its answer

6) references/intent-report.md. Replace:
So a winner is: **~1,600 words, 6–7 question-shaped headings, a `Name: arc + number`
with:
So a winner is: **~1,600 words, 6–7 plain editorial headings that name the entities, a `Name: arc + number`

7) references/seo-aeo.md. Replace:
  - **Question-shaped H2s** — headings that match the questions people ask.
with:
  - **Editorial H2s that name the entities** — no search-phrase or question headings; the answer goes in each section's first sentence.

Leave the "primary keyword in at least one H2" lines as they are.
```

## Superseded the same day by v2 (9 Nov, 19:35 JST)

Ranjita asked Zoya (copy) to fold all of the InfoBay feedback into the skill, so the 7-edit prompt above is no longer used. Akshay installs ft-substack-article-v2.zip from the file card in the Episode copywriter chat. The skill was never kept in skills/ and isn't added now; these checksums identify the build:

- zip 665187e8f3f06f937cb0058f9dc9b295cb85ff671042bb0a4c9870e3022f686a
- SKILL.md 1c261f35ffe39e41f6fbf0901586a5152097849c8359a633c00bef3ee28684fd
- references/voice.md ae452057abaa2111e57bb7d4b255df75460a2af737aee71d5043b232b21216e5
- references/seo-aeo.md 50c7556ee6e537775eb4c889f107bebcc78f19d6b2bd6452e7c91cd144ec9fef
- references/intent-report.md e7f0ad9a8799e33779d3af65d4bf7a13a2eae755d81f45cc5c30b7a79f0055ad
- scripts/render.sh 5281e7a9ede91be1b209a5ec014c9add67a17645def83b05f9f51ceaf636ebaa
- unchanged: references/infographics.md, tags.md, thumbnail.md, assets/ft-logo.png

The 12 changes are listed on Akshay's task row (Source ID cto:2026-11-09:substack-headings). The decision is logged once he has installed it.
