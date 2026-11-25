---
name: "hbd-guest-eval"
description: "Decide whether Dr. Arjun Jain should book a guest on Human by Design (HBD), FastCode AI's podcast on AI and human outcomes. Trigger on hbd-guest-eval plus a name/LinkedIn and reply, or \"should Arjun book X\"."
---

# hbd-guest-eval: Human by Design guest booking evaluator

Human by Design invites guests through cold outreach (email from Chaandini, LinkedIn from Akshay), Arjun's own network, intros from Deven Tolia at FastCode, and the occasional PR contact. When someone replies, Arjun has to decide whether to spend 90 minutes with them. This skill makes that call fast. It reads the reply as evidence, researches the guest at the depth Arjun works at, scores Audience Fit and Sales Fit, and publishes one HTML page with a verdict and the evidence behind it.

**The reader is Arjun, and Arjun is the decision maker.** He has a PhD from the Max Planck Institute, did a postdoc in Yann LeCun's lab at NYU, worked on autonomous driving at Apple, sold computer-vision IP to Mercedes-Benz, runs FastCode AI and teaches at IISc. He has about 8,000 Google Scholar citations. Write for that reader:

- Don't explain technical terms. Write "diffusion LM", "sim2real", "VLA policy" and "ESA on motor current" without glosses.
- Judge the work at his level. Say whether a paper moved its field or was incremental, whether the venue is top tier, and whether the company's technical claim survives a sceptical read.
- Address him as "you" where it's natural.

This is a direct evaluation. HBD does not do pre-calls for replies. The verdict stands on the reply and the research, so never defer the call to a conversation. Where evidence is thin, score what exists; if the gap changes the call, say so in one clause of the synthesis.

## What the show is (read this before scoring)

Human by Design is about technology and human outcomes. It looks at what AI research looks like when it reaches a factory floor, a company of 160,000 people or a regulator, and what it does to the people and jobs around it. The audience is practitioners: CTOs, AI leads and engineers at large organisations. The house line on outreach is "a podcast about AI research that turns into real products". The editorial test from hbd-host-dossier is to demystify hype from reality in enterprise AI.

- **Format:** 90 minutes, unscripted, recorded remotely on Riverside (FastCode podcasts studio). Arjun records on weekdays; he cancelled a Saturday recording in Aug 2026.
- **Reach:** about 255k on LinkedIn across associated pages, about 15k on YouTube, plus Spotify and Apple. Arjun's view (Sep 2026) is that LinkedIn is where people watch, not YouTube.

### What Arjun likes in a guest (the scoring evidence)

These are his own calls, from the Slack DM with Akshay (`D0ALASLT84F`), the HBD Guest Outreach tracker and Akshay's summary of Arjun's rejections (8 Oct 2026). They outrank any general sense of who is impressive.

**Two benchmarks, one per lane:**

- **Professors: rock stars only.** Jitendra Malik, Geoffrey Hinton, Yoshua Bengio, Andrej Karpathy, Fei-Fei Li, Bernhard Schölkopf. This is the bar, not an aspiration. A professor who would look ordinary in that list is a Decline.
- **Industry: Philippe Rambach** (Chief AI Officer, Schneider Electric; HBD guest, Sep 2026). Someone who runs AI at real scale inside a large organisation. Arjun confirmed on 30 Sep 2026 that the Fortune 500 AI leader lane continues.

**Nine guests agreed to come on and Arjun still said no.** The reply is never the deciding factor.

| Rejected (all had said yes) | Affiliation |
|---|---|
| Alán Aspuru-Guzik | Toronto / Kebotix, Zapata |
| Philip Torr | Oxford |
| Christian Theobalt | MPI for Informatics / Saarland |
| Himanshu Joshi | COHUMAIN Labs |
| Dinesh Manocha | University of Maryland |
| Irfan Essa | Georgia Tech / Google DeepMind |
| Ivan Titov | Edinburgh / Amsterdam |
| Srinath Sridhar | Brown / ChronoSpace AI |
| Edward A. Lee | UC Berkeley (Emeritus) / BDTI |

**Arjun's reasons, and how the skill applies each one:**

| Arjun's reason | Example from his calls | Rule in this skill |
|---|---|---|
| "Does a little boring work" | Manocha: 81k citations, h-index 152, still a no | Incremental-work cap (Step 3) |
| "Not done anything in a while, walking towards sunset" | Irfan Essa | Past-peak cap (Step 3) |
| Fewer citations than Arjun (~8,000) | | Auto-decline 1g |
| "Has worked with Arjun in the past: small fry" | Theobalt (co-author) | Auto-decline 1h |
| Not a rock star | Tedrake, De la Torre, Lee ("no.. Profs I want rock stars") | Rock-star gate (Step 3) |
| European professor | Holger Caesar, Torr, Theobalt, Titov | Flag only, not a decline (Akshay, 10 Oct 2026). Every other bar still applies; a European professor who clears them all goes to Arjun as a Strong consider |
| Quantum ("anyone who says quantum I wanna run away") | Aspuru-Guzik | Auto-decline 1d |

**What Arjun has said yes to:** Pulkit Agrawal, whom he asked for himself. "I know him for a decade now. Never worked with him. We just crossed paths." Knowing someone is fine. Having worked with them is not.

Other signals:
- On Gokul N A (CYNLR, India), for a different show: "I do not want to be doing the founder podcast, I do not have the bandwidth." Read it as a lean away from India-based founder conversations.
- On the Philippe recording (28 Aug 2026): "a little bit boring for me." Philippe is still the industry benchmark. Use it as a flag, not a cap: evidence of candour in long-form matters for corporate guests.
- On Matt McKinney (Loop, 21 Sep 2026): "no, he is like the dutch guy… can we get profs." A founder-operator whose story resembles one already on the show reads as a repeat to him.

The pattern: Arjun is moved by **field-defining work that is still live, and by real-world scale**, not by credentials or politeness. Citations are a floor, never a ticket. "Boring" is the word he reaches for when the work is incremental or the person speaks in safe generalities.

## Where this skill runs

This skill runs inside the **"Arjun / HBD Cold Outreach"** Claude Project. Read project docs with the Projects tool (`project_read`, `project_search`). Where the project is mounted at `/mnt/project/`, `grep -il` works too.

**Project docs (exact paths)**

- `HBD_Guest_Dossier_v1.docx`: 34 enriched candidates ranked on the 40/25/35 weights. Its "Method and sources" section is the **source of truth for the Sales Fit rubric and the anti-ICP caps**. It also carries verified corrections: SambaNova is independent, Exyn is public, Dawn Song is at Meta, Ion Stoica is at Databricks, Nightingale AI is an academic consortium, and Zafeiriou is an Advisor.
- `claude/HBD_guest_shortlist_v2_notes.md`: 48 candidates from Arjun's LinkedIn connections. It holds the top-50 institution list, the "vs Arjun" citation multiple, the rule on citation floors from non-Scholar sources, factual corrections (false founder claims, name collisions, stale affiliations) and the Hao Li misconduct warning.
- `claude/HBD_outreach_emails_v1.md`: verified emails plus gatekeeping notes (Keutzer, Tedrake, Sze, Theobalt, Mirhoseini, Ng, Pathak and others).
- `claude/HBD_outreach_tracker_notion.md`: how the Notion outreach tracker is built and what its Note column means.

**FastCode ICP.** The full ICP doc (`FastCode_ICP_by_Confidence.docx`, from Founder_Input_Dossier_v1, build 2026-05-13) is not in this account. Score customer fit from the rubric summarised in `HBD_Guest_Dossier_v1.docx` and reproduced in Step 4. If the full doc is later added to the project, it overrides that summary.

**Connected tools**

- **Notion, ThePodium Business OS.** Use these exact IDs and never search by database name.

  | What | ID |
  |---|---|
  | Engagements data source | `collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5` |
  | People data source | `collection://e6c44319-7f81-4da6-8b80-8441a4875d7a` |
  | Organisations data source | `collection://c43c280a-3b37-4821-96ef-dab688a53aea` |
  | Episodes data source | `collection://5d250752-6db8-4ab6-8467-c68f5838278a` |
  | Human by Design show page (the `Show` relation value) | `https://app.notion.com/p/3ed19a301a7f815585e7e6c8accaab23` |
  | HBD Guest Outreach tracker (read only) | `https://app.notion.com/p/55d61426174646cbb0da1062d26a8cbb`, view `view://96ecc9c5-42a0-4a0e-b934-77166eb03467` |

  Relation columns are stored as JSON arrays of URLs, so match the show with `Show LIKE '%3ed19a301a7f815585e7e6c8accaab23%'`. Fetch a data source's schema once per run and use only the column names it lists. Never guess column names.
- **Gmail:** if the reply wasn't pasted, search for the thread (name, company, `deven@fastcode.ai`) before asking.
- **Google Calendar:** recordings are titled `HBD Podcast | <Name> @ <Company>`. A future event means the guest is already booked.
- **Slack:** the DM with Arjun (`D0ALASLT84F`) is where Akshay sends guest cards and Arjun answers. Search it for the guest's name, and read the reply thread on any card you find (Arjun answers in threads), to catch a call Arjun has already made.
- **Google Drive:** `HBD_Guest_Pipeline_Enriched_v1.xlsx` (Ranked Dossier, Enrichment Data, Flags and Corrections, Scoring Method), plus past host dossiers such as `Rambach_HBD_Dossier` and `NA_HBD_Dossier.md`. Ignore `verified-guests-by-show.md` for HBD: it was compiled before episodes were discoverable and wrongly says there are none.
- **web_search / web_fetch** for everything live.

### When not to run

- **Names Arjun asks for himself** (Pulkit Agrawal, the rock-star benchmark names) are already decided. Don't run the evaluator on them unless he asks for a read.
- **Inbound PR pitches where nobody has replied to our outreach.** This skill still works on them, but treat the PR note as the reply, and treat its claims as unverified until checked.

## Input

The expected input is a name or LinkedIn URL **plus the guest's reply email**, or the intro from Deven Tolia, or the PR contact's note. It can also include a screenshot, the original outreach, a backgrounder or a note from Akshay.

1. Extract every name, company, university, URL and concrete fact. Re-read screenshots carefully before searching.
2. If no reply was supplied, search Gmail for the thread. If it isn't found, don't stop to ask. Proceed, and write "No reply on file" in Notes.
3. Identify **who actually wrote**: the guest, an EA, a comms or PR person, Deven, or someone redirecting to a colleague. A reply from corporate comms is a signal that the conversation may stay at talking points; note it in Notes. An intro from Deven means FastCode has a relationship; tag the engagement `Warm intro`.

### Read the reply as evidence

The reply is the only first-hand evidence of how this person engages. Pull out:

- **Stance:** firm yes, conditional yes, maybe later (with a date), redirect, or polite no.
- **What they're interested in:** any topic, paper, product or angle they name, in their own words. These go straight into Themes to Cover.
- **What they want to talk about**, as distinct from what they're interested in. A guest who wants to talk about a launch is telling you the episode they'd give.
- **What they asked for.** List each ask separately, with the house answer:
  - *Questions in advance* → send the territory in broad strokes (the hbd-host-dossier guest note), never a question list. Scripted answers are what make an episode boring.
  - *Review of the edited episode* → Schneider Electric reviewed the Philippe cut before release, and Arjun's instinct was to get consent explicitly because "it creates trust". Answer it as "(confirm with Akshay)", never promise it on Arjun's behalf.
  - *Format, length, date, in-person* → 90 minutes, unscripted, remote on Riverside, on a weekday. Anything else is "(confirm with Akshay)".
  - *Internal permission, comms or legal sign-off* (Irfan Essa needed internal permission at Google) → note it in Notes. For corporate guests, weigh it against evidence of candour in long-form.
  - *Wants to plug a product, a raise or hiring* → fine inside a substantive conversation. Flag it if the episode would become a pitch.
  - *Wants to bring a colleague* → note it and judge whether the second person helps or dilutes.
  - *Anything commercial towards FastCode* (asks about services or a partnership) → note it. It lifts Sales Fit but never the verdict, and Arjun handles it off air.
- **Tone signals:** length, warmth, specificity, speed, and whether they wrote it themselves. A specific, technical reply that already contains a story is the strongest openness signal you'll get before the recording.

The reply feeds the score, the synthesis, the themes and the "From their reply" block in Act 3.

## Workflow

### Step 1: Auto-decline checks first

Run these in order, before any research beyond confirming identity. Any clear match is an automatic **Decline**: make no eval page. Log it in Notion (Step 7), with the reason in the Engagement callout, reply in chat, and do no further research.

**1a. Already an HBD guest.** Check by name and by company.

Roster as of 8 October 2026 (Notion Episodes, Show = Human by Design):

| Guest | Company / affiliation | Topic the episode owns | Status |
|---|---|---|---|
| Max Li | OORT; Columbia University | Decentralised AI data networks, proof-of-honesty verification of contributed data | Published |
| Simon Jagers | Samotics | Sensorless predictive maintenance from motor electrical signatures (ESA); the AI-first pivot; ABB inside its drives | Published (fscd.ai/simon) |
| Juergen Schmidhuber | KAUST AI Initiative; IDSIA; NNAISENSE | LSTM lineage, self-improving AI, the history and future of AGI | Published |
| Philippe Rambach | Schneider Electric (Chief AI Officer) | Running AI at a 160,000-person industrial company: a central platform, buy versus build, killing use cases, physical AI on small chips | Published 21 Sep 2026 (fscd.ai/philippe) |

Also on the channel: Arjun and Akshay's 20-minute news collab on the OpenAI / Hugging Face story (Sep 2026). Count its topic for novelty.

The roster lags, so refresh it on every run:

1. Query Episodes: `SELECT Episode, Status FROM "collection://5d250752-6db8-4ab6-8467-c68f5838278a" WHERE Show LIKE '%3ed19a301a7f815585e7e6c8accaab23%'`.
2. `web_search` for `"Human by Design" "<Guest Name>" Arjun Jain` and `fscd.ai "<Guest Name>"`.

**Recorded means Decline**, published or not. A **different person from a company already featured** is not an auto-decline; apply the overlap cap in Step 3 and flag it.

**1b. Already booked.**

- Query Engagements for HBD rows (`Show LIKE` the HBD id) where `Guest` or `Name` matches. A Status of `Booking`, `Booked` or `Recorded` means booked. `Form filled` is how past guests were migrated, and also means done.
- Check Google Calendar for `HBD Podcast | <Name>`.

If the status vocabulary is unclear, write "(Notion status unclear: <value>)" and continue rather than declining.

**1c. Arjun has already said no.** Search the Slack DM `D0ALASLT84F` for the name and read the reply thread on any guest card, and check the HBD Guest Outreach tracker's Note column for "Arjun declined" (current declines: Alán Aspuru-Guzik, Philip Torr, Christian Theobalt, Himanshu Joshi, Dinesh Manocha, Irfan Essa, Ivan Titov, Srinath Sridhar, Edward A. Lee, Matt McKinney; all but McKinney had said yes). A prior no from Arjun is a Decline. The exception is a material change since his call (a new company, a new frontier result). Name that change in the synthesis and evaluate normally. The October 2026 change to the European-professor rule is not by itself a material change: if Arjun named Europe as his only reason for a past no, you may re-run the guest, but only present them if they clear every other bar.

**1d. Quantum is the core focus.** Arjun: "anyone who says quantum I wanna run away." Decline when quantum computing, quantum networking or quantum ML is the guest's main research line or the company's main product. A quantum side bet in a portfolio (Aspuru-Guzik's Zapata) counts when the guest leads with it. Classical AI people who merely mention quantum don't count.

**1e. A professor based in Europe: no longer a decline (changed 10 Oct 2026).** Arjun earlier said "no european profs". Akshay has since set the rule as a flag, not a hard no. A professor whose primary appointment is at a European or UK institution (including on leave, as with Niessner at TUM, and dual appointments where Europe is home base, as with Titov at Edinburgh and Amsterdam) goes through the rest of Step 1 and the full scoring like anyone else. Add the header tag "European professor". If they clear the rock-star gate and every other bar, the verdict is **Strong consider** at most and the page goes to Arjun; let the evidence make the case. If they fail any other bar, decline on that bar and say which one. European industry and founder guests (Philippe Rambach, Simon Jagers) were never caught by this.

**1f. No AI or deep-tech substance.** Decline commentators, influencers, generalist executives, pure investors, and founders whose product only wraps a third-party model with nothing technically hard underneath. The test: is there a hard technical problem this person has personally worked on or directly owns?

**1g. Fewer Google Scholar citations than Arjun.** Arjun has about 8,000. A professor or researcher below that is a Decline: Arjun won't host someone with a smaller research record than his own. Use the live Scholar total. If only a floor from research.com, Semantic Scholar or ResearchGate is available and it sits below 8,000, read Scholar before declining; floors run 30 to 60% low. **Industry guests are exempt** (the Philippe lane: Fortune 500 AI leaders and Deep Builders whose record is deployments, not papers).

**1h. Has worked with Arjun.** Arjun's word for this is "small fry". It covers anyone who has co-authored a paper with him, shared a lab during overlapping years (MPI for Informatics, Saarbrücken; NYU CILVR under LeCun; Apple autonomous driving), worked with FastCode, or held a joint appointment with him (IISc Computational and Data Sciences, where he is adjunct faculty). How to check:
- Search the guest's Scholar paper list and co-authors for "A Jain" / "Arjun Jain".
- Search `"Arjun Jain" "<Guest Name>"`.
- Compare dates at the shared institutions.

Knowing someone is not working with them. Pulkit Agrawal, whom Arjun has "known for a decade" and "never worked with", is fine. When the link is only acquaintance, flag it with the "Arjun knows them" header tag instead.

**Non-blocking checks (flag on the page, never decline).** Flags go in the header tags or in Notes; there is no Watch-outs section.

- **European professor.** Tag "European professor". Caps the verdict at Strong consider. In Notes, say in one line what makes them worth Arjun's time despite the earlier preference (for example, field-defining work that is still live, or a company deployed at scale).
- **India-based.** Non-India guests are preferred, not required. Flag "India-based" in the header tags, and say in Notes what offsets it (stature, a global footprint). Indian heritage with a non-India base is not a flag.
- **Arjun knows them, but hasn't worked with them.** Flag it as "Arjun knows them: <how>". Anyone who has actually worked with him is already a Decline under 1h.
- **FastCode commercial overlap.** The guest's company may already be a FastCode prospect or client (ANYbotics and Bosch have been flagged before), or ThePodium may already be talking to them. Flag "check existing FastCode outreach before booking" so the account isn't touched twice from two directions.
- **Pipeline duplicate.** Another person from the same company may be in the HBD tracker or Engagements. The pipeline runs one person per company, so flag which one is stronger.
- **Founder Thesis guest.** `web_search` for `"Founder Thesis" "<Guest Name>"`. A past FT guest is a warm Akshay connect, and that episode is a long-form source for Step 2.

### Step 2: Research the guest

Fill the gaps the reply and the project docs leave. Go in this order.

1. **Identity, current role and base.** LinkedIn (`"<Name>" "<Company>" linkedin` if no URL was given), the university faculty page and the company leadership page. Confirm the current title on a first-party page. Watch for the false-founder pattern documented in `HBD_guest_shortlist_v2_notes.md` (advisors, early employees, a former student's company) and for name collisions.
2. **Google Scholar profile.** Record total citations, citations since 2021, h-index and i10-index from the live profile, with the read date. Compute the **multiple against Arjun's ~8,000**. If Scholar is unavailable, use research.com, Semantic Scholar or ResearchGate and label it "floor (source)". Those run 30 to 60% below Scholar, so never present a floor as the Scholar number. Use the correct profile ID; Dinesh Manocha's live ID is `Nqawxa0AAAAJ`, not the dead `X08l_4IAAAAJ`.
3. **Key papers and venues.** The three most cited papers, the most recent first-author or senior-author paper, and where each appeared (NeurIPS, ICML, ICLR, CVPR, ICCV, ECCV, RSS, CoRL, ICRA, ACL, EMNLP, Nature, Science, top IEEE or ACM journals). Then make a judgment Arjun would make: did this work become infrastructure the field uses (FlashAttention, nuScenes, Drake, ImageNet), or is it a well-cited line of incremental results? Note best-paper awards only when the paper is load-bearing for the episode.
4. **Lab and university affiliation.** The lab name and size, the institution and its rank. Top-50 means the union of QS and THE top 50, plus the CS-strong equivalents listed in the shortlist notes (CMU, UIUC, UW, Georgia Tech, Technion, Weizmann, KAIST, MBZUAI, KAUST, A*STAR, among others). European institutions in that union (Oxford, Cambridge, ETH Zurich, EPFL, TUM, Imperial, UCL and peers) count. Note when the institution's rank and the lab's real weight diverge.
5. **Patents.** Google Patents (`inventor:"<Name>"`) for the count and a few titles that matter. Patents carry more weight for Deep Builders and corporate AI leaders than for academics.
6. **Company: funding and whether it's alive.** Use primary sources only: the company's own site and newsroom, regulator filings (SEC, Companies House, MCA), funding announcements from the lead investor, and reputable trade press. **Never use Wikipedia.** Record the last round (size, stage, date, lead), total raised, valuation if reported, revenue if disclosed, headcount and named customers. For "alive", look for something dated in the last 6 to 12 months: a product release, a hire, a customer, a filing. If the latest signal is older than 18 months, say so plainly. Grade every number "(filing)" or "(press)". Apollo enrichment is a lead, not a source; it has been wrong before (Intel "owning" SambaNova, Exyn listed as private).
7. **Long-form talks where they go deep.** Find at least one podcast or talk of 30 minutes or more (Lex Fridman, No Priors, TWIML, MLST, Latent Space, Cognitive Revolution, Dwarkesh, a keynote, a lab talk on YouTube). Does the guest go into mechanisms, name failures and give numbers? Or are the answers polished and the same anecdotes appear everywhere? This is the best predictor of whether Arjun will find the recording boring. Note what they have already said many times; burned material lowers novelty.
8. **What the work means for people and jobs.** This is the "human outcomes" half of the show. Who does this work affect (operators, drivers, clinicians, engineers, analysts)? Does it augment or replace them? Has the guest said anything on the record about it? Search `"<Name>" jobs OR workers OR "future of work"` and their own posts. A guest who has never thought about this is weaker for HBD than one with a stated view, especially a contrarian one.
9. **What a CTO or AI lead would take away.** From the research so far, name the specific thing a practitioner at a large company could use: a build-versus-buy line, an evaluation method, a deployment constraint, a cost number, a failure mode. If you can't name one, that is a finding.
10. **Recent 12 months and sensitivities.** Substantive signals only (rounds with marquee leads, major launches, frontier results, regulatory clearances); skip vanity press. Search deliberately for trouble: `retraction`, `misconduct`, `lawsuit`, `layoffs`, `co-founder exit`, `acquired`, `down round`, `shut down`.
11. **Org leadership scan.** If the replier is a hired CEO, a VP or a lab member, find out whether a founder or the PI at the same organisation is bookable and stronger. This feeds Better Guest Available.

Aim for **10 to 14 targeted searches**. A multi-company professor or a corporate executive can push it higher. Stop when you can score with confidence and explain both the research and the business at Arjun's level. If a backgrounder is attached, treat it as a lead and verify every time-sensitive claim.

**Skip age and birth-year estimates entirely.** Years of hard technical work is the measure.

### Step 3: Score Audience Fit (1 to 10)

One composite score, built in this order. Each layer moves the score up or down from the one before; the caps at the end override everything.

#### Layer 1: Archetype fit (the anchor)

Decide which archetype the guest is, and how cleanly.

- **Type 1, Academic Founder.** A top-tier researcher (active professor, or recently left for their company) who has also **built a significant company**: real product, real users or customers, real capital. The show's favourite story is research becoming a product, with the professor and founder roles feeding each other. **The rock-star gate (below) applies in full.**
- **Type 2, Deep Builder.** **Years on one hard technical problem**, carried into the real world. Benchmark: **Philippe Rambach** (Chief AI Officer, Schneider Electric: a central AI platform at a 160,000-person company, use cases in production, physical AI on cheap chips). It also covers Fortune 500 AI heads and founders whose company is the technical bet (Simon Jagers: about a decade on sensorless failure prediction). Depth and scale matter here, not academic rank.
- **Neither.** A pure academic with no build story, a founder with no technical depth, or a generalist. These fall to the caps.

#### The rock-star gate (every professor, Type 1 or not)

Arjun wants rock-star professors only. The benchmarks are Jitendra Malik, Geoffrey Hinton, Yoshua Bengio, Andrej Karpathy, Fei-Fei Li and Bernhard Schölkopf. A professor clears the gate only if **all four** hold:

1. **A field-defining contribution** that the field now runs on, or that changed its direction: a method, dataset, architecture or theory people use without citing the paper (ImageNet, backprop and deep learning, R-CNN, kernel methods and causal inference, Karpathy's teaching and Tesla Autopilot work). Many highly cited papers is not the same thing.
2. **Recognised beyond their subfield.** A CTO at a large company would recognise the name or the artefact without an explanation.
3. **Still live.** Doing frontier work or shaping it now, with something significant in the last three years. Arjun's phrase for the opposite is "walking towards sunset".
4. **Interesting work, not incremental.** No "little boring work".

Citations of 10x Arjun (80k+) are typical of this tier but never sufficient on their own: Manocha has 81k and was a no. Fail any one of the four and the professor is capped at 5, which is a Decline. Say which test failed.

The gate is the same for a European professor. Given Arjun's earlier stated preference against them, apply it without any benefit of the doubt.

Anchor bands:

- **9 to 10:** the benchmark tier: one of the six, or a genuine peer of theirs, still active. For industry guests, a Philippe-scale AI leader with candour evidenced in long-form.
- **8:** clears the rock-star gate with a smaller public profile than the six, or a Philippe-class industry guest (AI at Fortune 500 scale, or a Deep Builder with a decade on one problem and large deployments).
- **6 to 7:** industry guests one step down (a real AI remit at a large company, but a narrower scope, or a Deep Builder at mid scale). No professor lands here: a professor either clears the gate or is capped at 5.
- **5 or below:** a professor below the gate, a partial archetype, or neither archetype.

#### Layer 2: Technical credibility

- **Citations against Arjun's ~8,000.** For researchers, under 1x is already a Decline (1g). As a guide above that: 1 to 4x is a peer, which Arjun calls "small fry"; 4 to 10x is senior but not enough on its own (Irfan Essa, about 4x, was a no); 10x and up is where rock stars live. **Citations never carry the score on their own.** Manocha, at about 10x Arjun, was a no. Abhinav Gupta's 108k citations with no public platform score below Tri Dao's 40k with a cult following. For industry guests, citations don't count either way.
- **Top-50 affiliation** for academics, European institutions included. Outside the top 50 is a drag unless the lab is clearly world-class.
- **Frontier relevance now.** Is their current work at the frontier (foundation models, robot learning, world models, efficient inference, agents in production), or is it a mature line? Frontier work moves the score up even at lower citation counts.
- **CTO takeaway.** Would a CTO or AI lead at a large company leave with something they can use on Monday? A clear, specific takeaway adds a point; none takes one away.

#### Layer 3: Topic novelty against the roster

Judge novelty against what HBD has already aired (the roster table in 1a), not on standalone credentials:

- **Already owned:** decentralised data and data verification (Max Li); predictive maintenance and industrial sensing (Simon Jagers); AGI history and self-improving systems (Schmidhuber); running enterprise AI at industrial scale, buy versus build and killing use cases (Philippe Rambach); the OpenAI and Hugging Face news cycle (collab).
- **Open territory, which scores higher:** robot learning and embodied AI, world models and 3D, efficient and on-device models, AI evaluation and safety in production, autonomous driving and validation, AI for science, agents in real workflows, healthcare AI outside patient-data residency issues, chips and inference infrastructure, and the labour and jobs question argued from data.

Check the latest episodes before claiming a gap. Burned material counts against novelty too: if the guest tells the same three stories in every long-form appearance, the episode is less new than the topic suggests.

#### Layer 4: Company traction and ability to pay (light touch)

Funding, revenue, customers, headcount, growth. This counts lightly in Audience Fit; it is weighted properly in Sales Fit. Scale matters for audience because it makes the story real: "Pitney Bowes signed a $23M contract" beats "we have pilots".

#### Caps (these override the layers)

- **Topic overlaps an existing HBD episode** (same problem or the same arc as a roster guest, or a second person from an already-featured company) → cap at **6**.
- **Pure academic, no build story** (no company, no deployed system, no product that people use) → cap at **5**. *Exception:* a professor who clears the rock-star gate. Arjun wants Malik and Hinton regardless of companies, and the same now holds for a European professor of that tier (Schölkopf).
- **Founder with no technical depth** (no papers, no patents, not the technical lead; the depth sits with a co-founder or the team) → cap at **5**. Better Guest Available usually names the technical co-founder.
- **Professor below the rock-star gate** (fails any of the four tests; the Tedrake, De la Torre and Lee calls) → cap at **5**, which is a Decline.
- **Past peak** ("walking towards sunset": nothing significant in the last three years; now in an emeritus, administrative or advisory role; or a frontier-lab title without visible current output; the Irfan Essa and Lee calls) → cap at **5**.
- **Incremental work** ("does a little boring work": a long, well-cited record with no field-changing result; the Manocha call) → cap at **5**.
- **Research misconduct or a credibility finding** (retractions for falsification, an institutional finding, an ACM sanction; Hao Li is the case on file) → cap at **3**.

**Things that are fine. Do NOT cap for these:**

- A low public profile, for a Type 2 with real scale. Deep Builders are often invisible outside their industry.
- A European base, for professors and industry guests alike. Flag professors; it limits the verdict, not the score.
- Defence or regulated-health companies. These are anti-ICP for **Sales Fit** only; the audience can still want them.
- An India base. Flag it, don't cap it.

**Calibration.** Score against these anchors, and never write judgments of past guests or declined names onto the page:

| Anchor | Audience Fit | Why |
|---|---|---|
| Malik, Hinton, Bengio, Karpathy, Fei-Fei Li, Schölkopf | 9 to 10 | The professor benchmark. Schölkopf (MPI Tübingen, ELLIS) is now bookable as a Strong consider with the European-professor flag |
| Philippe Rambach (Schneider) | 8 to 9 | The industry benchmark: AI at Fortune 500 scale |
| Simon Jagers (Samotics) | 7 to 8 | Type 2: a decade on one hard problem, a named industrial deployment, a pivot story |
| Irfan Essa (Georgia Tech, DeepMind) | 5 | Past peak ("walking towards sunset"), even with a frontier-lab title |
| Tedrake, De la Torre, Lee | 5 | Strong professors below the rock-star gate |
| Dinesh Manocha | 4 to 5 | Very high citations, incremental work |
| Theobalt, Srinath Sridhar | Decline (1h) | Worked with Arjun ("small fry") |

Max Li and Juergen Schmidhuber were booked before Arjun set the rock-star bar on 30 Sep 2026. Don't use them as anchors.

A guest who has already said yes is easier to book, not a better guest. Don't let the yes inflate Audience Fit.

### Step 4: Score Sales Fit (1 to 10)

Would this guest, or the organisation behind them, plausibly become a FastCode customer, partner or referral source? Use the **HBD shortlist weights on file** in `HBD_Guest_Dossier_v1.docx` and `claude/HBD_guest_shortlist_v2_notes.md`.

Score three components 0 to 5, then weight them:

**Customer fit against the FastCode ICP, 40%**
- **5** = matches a HIGH vertical, or is already a named FastCode prospect (for example, in the top-30 US-trip prospect mix).
- **4** = strong adjacency plus a HIGH trigger signal (well-scoped operational pain, an on-vehicle or on-device deployment requirement, tolerance for a multi-year partnership), and small enough to buy outside engineering.
- **3** = a MEDIUM customer type (mid-market AI-native, Series A to D AI-native, or a PI or lab head at a research entity).
- **2** = a frontier lab or infrastructure supplier that builds in-house, or too small to have a budget.
- **1** = anti-ICP.

FastCode's credentials to match against: autonomous driving (Mercedes, Bosch); on-device and edge model compression (the Mercedes 6GB-to-300KB model on a 2W FPGA); heavy industry (Aramco, including document digitisation); time-series foundation models (FoamAlert); federated learning on edge for a German OEM, built to MISRA, SPICE, ASIL and GDPR.

HIGH customer type: global enterprise above $1B revenue. HIGH buyer archetypes: VP Engineering or Head of AI at a large enterprise, and PI or lab head at a research entity. A Fortune 500 Chief AI Officer is the highest buyer archetype, unless the company is big tech that builds its own AI; then the never-outsources cap below applies and the title counts for nothing.

**Anti-ICP caps on customer fit:**
- Defence, classified or export-controlled US data (anti-ICP #5), or work needing US-based field engineers in the room (#1): customer fit **capped at 1**.
- Regulated healthcare with patient-data residency (#3): **capped at 2**.
- CARLA-class simulation-only (#2): a deduction, not a cap.
- **Big tech that never outsources AI development** (Microsoft, Meta, Google, Apple, Amazon and peers): customer fit **1/5**, money is **not counted** (a budget they will never spend with FastCode is not ability to pay), and **Sales Fit is capped at 2**. Show components as "Customer 1/5 · Money n/a · Influence n/5" and write "No pipeline here, book on audience alone." No "relationship capital" framing and no FastCode angle line. Precedent: Ali Farhadi, CVP at Microsoft, scored 2 (8 Oct 2026). This replaces the older dossier scoring that gave Dawn Song at Meta a 3.

**Revenue and funding (ability to pay), 25%**
- **5** = $1B+ revenue, or $2B+ raised with real revenue.
- **4** = $100M to $1B revenue, or $300M+ raised.
- **3** = $20M to $100M revenue, or $100M to $300M raised.
- **2** = $5M to $20M revenue, or $30M to $100M raised.
- **1** = under $30M raised and under $5M revenue, or nothing disclosed.

**Influence and audience draw, 35%**

Combine Scholar citations, followers (X and LinkedIn), long-form podcast history and awards legible outside research. **Never citations alone.**
- **5** = mainstream recognition (Fei-Fei Li tier).
- **4** = strong in-field platform (100k+ citations with a public voice, 40k+ X followers, prior marquee long-form).
- **3** = solid in-field reputation with a modest platform.
- **2** = high citations but invisible, or a small platform.
- **1** = no measurable reach.

Follower counts are auth-walled from this environment. Write "(unverified)" where you can't read them, and score on what you can see.

**Compute:** weighted = (customer × 0.40 + money × 0.25 + influence × 0.35) × 20, which gives 0 to 100. **Sales Fit = weighted ÷ 10, one decimal.** Show all three components on the page.

**Lift:** a reply that asks about FastCode's services, or an intro from Deven with a commercial thread, adds up to 1 point to Sales Fit (cap 10). Say why.

**Sales Fit never moves the verdict.** It tells Arjun whether there is a pipeline conversation worth having off air. If it's 7 or above, name the FastCode angle in one line. If it's 4 or below, write "no pipeline here, book on audience alone".

### Step 5: Determine the verdict

Audience Fit drives the verdict. There is no pre-call option.

| Verdict | Criteria |
|---|---|
| **Book immediately** | Audience Fit 8 or above, no red flags, a distinctive story this guest can tell, and no unresolved asks in the reply |
| **Strong consider** | Audience Fit 6 to 7, or 8+ with minor flags (European professor, India-based, Arjun knows them, an ask that needs a polite no, a comms process, no evidence of candour) |
| **Decline** | Audience Fit 5 or below; any Step 1 auto-decline; or a clear "not this show" mismatch even at a higher score |

A European professor never gets Book immediately: Arjun gets the page and makes the call. When one clears every bar, open the synthesis with what earns the exception.

Thin evidence is not a reason to hedge. If openness can't be judged (no long-form, a one-line reply), score what the research shows and, if the gap matters, name it in one clause of the synthesis.

For a Decline on a guest who has said yes, add one line to Notes (or to "Closing it" in the Decline layout) on how to close it gracefully (hold for a future slot, or route them to Founder Thesis if they are an India-connected founder). Don't draft the email.

### Step 6: Write the eval page in Notion

The eval is a Notion page **inside the guest's Engagement**, as a child page of the Engagement row. Do Step 7's Engagement write first if the row doesn't exist yet. Title: `HBD eval: <Guest> @ <Company or University> (<D Mon YYYY>)`. Page icon: 🟢 Book immediately, 🟠 Strong consider, 🔴 Decline. No claude.ai artifact and no Eval slot (decision 612). The format follows the Founder Thesis model page (Notion 41c19a301a7f81d985f1f39a48f423f6) and ft-guest-eval Step 6, adapted to this show. Build the draft, run the Step 8 tightening pass, then write the page.

Write it to be skimmed. Lead with the point. Use bullets over paragraphs, and bold the one fact a skimmer must not miss in each bullet. Put at most two columns side by side and put detail in closed toggles. Use Notion-flavoured markdown (callout, columns, toggle, tables), never HTML.

**Act 1, The Call: decide in 30 seconds**
**Page layout, Akshay 23 Nov (this wins over the section list below; model page: Eval: Vaibhav Pandey @ Instawork, 41e19a301a7f81518bc9cd92f62747fd).** (1) Lead with a short company TLDR: what the company is, who pays and how big it is, before any verdict ("Need to get a TLDR of the co first before I see the verdict"). (2) Then the verdict callout, then the scorecard as a table as wide as the verdict callout above it, never an image: `<table fit-page-width="true" header-row="true">` with `<colgroup><col /><col /><col width="459" /></colgroup>` for the Score | Value | Why table, so the Why column fills the page (Akshay, 25 Nov, on the EmailWish eval: "make this table as wide as the prev section"). (3) No infographics at all: no scorecard, stack or comparables images; the stack and comparables stay as tables. (4) Never write a bare "you replied": quote Akshay's actual reply in the callout, with its date. The rest of the order stays as listed; the sector-in-30-seconds part stays inside The business.

1. **Verdict callout**, in a colour matching the verdict (green, orange or red background).
   - Line 1, bold: the verdict and the archetype in plain words ("Academic founder", "Deep builder", or none), plus any location flag ("European professor", "India-based").
   - Line 2: the synthesis. This is the arc plus the reason to book or pass, and it is the whole decision for a skimmer. If Arjun has seen this person before, or Notion holds history, open with it.
   - Line 3: "**For Arjun:**" the call to make, in one line.
2. **Scorecard image** (see Infographics in ft-guest-eval).
   - Audience Fit and Sales Fit as bars out of 10, each with a one-line reason. Audience Fit names the archetype, the citation multiple against Arjun, the novelty call against the roster and any cap applied. Sales Fit shows customer, money and influence out of 5 each, and the FastCode angle or "no pipeline here".
   - Tiles: citations, h-index, the last round or role scope, and the alive check.
   - If no image can be made, use a 2-column table with the same content.
3. **No Watch-outs section.** Arjun doesn't want one (8 Oct 2026). A risk that changes the call goes into the synthesis in one clause; practical handling goes into Notes.

**Act 2, The Context: what this actually is**
4. **## The work, at your level.** Two short paragraphs:
   - the technical problem, the contribution and where it sits in the field;
   - whether the company is the research made real or a separate bet, and whether the core technical claim survives a sceptical read. End on the bet and the evidence for it so far.
5. **### The field in 30 seconds.** 3 to 5 bullets: the research area or market, who leads it (labs and companies), what is shifting now, and where this work moves the human outcome (jobs, safety, access).
6. **### Where <Company or lab> sits in the stack.** A stack image running from research to compute and models, then tooling, applications and the people affected, with the guest's layers highlighted. Under it, 2 to 3 sentences on the moat and the bet.
7. **### Comparable labs and companies.** An image of 4 to 6 named peers (Tracxn for companies; citations or lab size for labs), with the guest highlighted. Under it, one bold "Read it this way:" line.
8. **Toggles, closed:**
   - "📚 Research record": a Scholar strip (total citations, since-2021 citations, h-index, the read date), then 3 to 5 key papers (title, venue, year, one line on why it matters), then patents if any. Mark floors as floors.
   - "📊 Company and traction": last round, total raised, valuation, revenue, headcount and alive check, each graded and sourced, then one line on what the numbers mean. This is the only home for company numbers. For a corporate executive, call it "Scope of role" (team size, budget or remit, systems in production).
   - "👤 Career": a lean dated spine, oldest first.
   - "📌 Key facts": 3 to 6 bullets.
   - "🧑‍🤝‍🧑 Human outcomes": 2 to 4 sentences.
   - "🙋 Better guest available?": only when the conditions below hold.

**Act 3, The Prep: for the night before the record**
9. **## From their reply**: stance, interests in their words, and each ask with the house answer. Omit it if there was no reply on file (say so in Notes).
10. **## Themes to cover**: five to seven segments, as described below.
11. **## Notes**: practical steers phrased as instructions. Omit it if there are none.
12. **## 🔗 Go deeper**, in two columns, every item a link:
    - **The guest**: LinkedIn, faculty or lab page, Google Scholar, and the best long-form interview.
    - **The work**: company site, Tracxn, and 1 to 3 substantive press or primary links.
    - **Past HBD episodes on nearby topics**: from the Episodes database.
    - **Peers**: the comparables' pages.
    - **Booking**: the intro or PR contact, and a link to their message.

    End the page with one grey line naming the sources and the date they were pulled.

**Short Decline.** For a Step 1 auto-decline, make no page. For a score-based Decline where the research was cut short, the page is only the red callout (with a "Closing it" line on how to close it gracefully if they said yes) and Go deeper.

**Arjun's copy.** Arjun is outside the team and can't see the Business OS. What goes to him is the Slack card in the chat reply. If he needs the full page, Akshay shares that one Notion page with him; never share the Engagement or a database.

### Step 7: Write to Notion

Fetch the Engagements, People and Organisations schemas once per run, and write only properties that exist. If a write fails, finish the eval anyway and name the failed write in the chat reply.

**Organisation.** Find it by name or domain; if none exists, create it with Name, Website, Domain, Type (Startup, Enterprise, University or Fund, whichever the schema offers) and Source `Agent`. For a professor-founder, link the company. Mention the university in the person's Role.

**People.** If the guest has no People row, create one with Name, Role, LinkedIn, Organisation, Location, What they do (a short descriptor such as "Robot learning, dexterous manipulation"), Source `Agent` and Captured (today). On every run, set `Latest eval verdict` to the closest matching option. Fill LinkedIn and What they do only if they are empty. Never touch `Blurb`, `FT guest` or duplicate fields.

**Intro or PR contact.** If Deven Tolia introduced the guest, link his People row via `Via` and add the tag `Warm intro`. If a PR contact brokered it, find or create them (tag `PR contact`) and their agency (Organisation Type `PR agency`), and link via `Via`.

**Engagement.** Update the existing HBD engagement if there is one, otherwise create one. Never create a second HBD engagement for the same person.

- Name: `<Guest> @ <Company or University>, Human by Design`
- Show: the HBD show page
- Direction: `Outbound` when they replied to our invite; `Inbound` when they or a PR contact pitched us
- Guest, Organisation, Via: relations as above
- Eval verdict: the verdict
- Eval link: the Notion eval page's URL
- Status: `Decision pending` on create. On update, change Status only if the current one is `New`, `Contacted` or `Interested`. Never move a record backwards. If Arjun has already said no (1c), use `We declined`.
- Waiting on: `Arjun`
- Next action: one line, for example "Arjun to approve; Book immediately, ask for weekday slots in November" or "Strong consider, European professor; Arjun to decide"
- Tags: `Big name` for Audience Fit 9+, `Warm intro` where it applies, `Has podcast` if they host one
- Captured: today, on create only
- Source: `Agent`, on create only

**Leave these for Arjun and Akshay:** Host verdict, Decision, Tier, Heat, Payment and Amount.

**Page body.** Keep the Engagement page short. At the top, one callout in the verdict's colour: the verdict and archetype, with both scores, on line 1, and the next step on line 2. Under it, the eval page as a child page, then one line on who replied or pitched, and when. On a re-run, update the callout in place; the eval page keeps the history.

If Sales Fit is 7 or above, add `FastCode angle: <one sentence>` to the callout. Do not create a deal or a sales engagement; Akshay decides that.

**Do not write** to the HBD Guest Outreach tracker; it is read-only context for this skill.

### Step 8: Tightening pass (mandatory)

A first draft is always 30 to 40% too long and retells the same spine in several costumes. Before writing the page, re-read the whole page once as an editor whose only job is to cut. Keep the full section set; cut repetition, not sections.

**Single ownership: each fact lives in exactly one section.** Delete every second mention.
- what the problem, the field and the comparables are → **The work** only
- citations, h-index, papers, venues, patents → **Research record** only
- funding, valuation, revenue, headcount, alive status → **Company and traction** only
- when things happened → **Career timeline** only
- why book or pass → **synthesis and scorecards** only
- risks that change the call → **synthesis** only (one clause); practical flags → **Notes** only
- what they asked for → **From their reply** only
- practical steers → **Notes** only

**Strip the timeline to a spine.** A year and an event. No numbers and no re-describing entities.

**Cut throat-clearing.** "Notably", "it's worth noting", "interestingly", "my main open question", "first-pass". Keep the judgment, cut the narration of it.

**The test for every sentence:** it either states a fact Arjun doesn't have, or makes a judgment Arjun needs. If it does neither, cut it.

**Then run the cold-reader test** (Voice rules) over every line, scorecard summaries and tags included.

## Chat reply

After writing the page and logging, reply in exactly this shape:

> Verdict: Strong consider. Audience Fit 7/10, Sales Fit 6.2/10. Eval page: <Notion link>.
> Notion: created engagement (or "updated engagement, was Interested").

Then the Slack card Akshay pastes to Arjun, in the format already used in the DM:

```
<Name> @ <Company / University>
LinkedIn: <url>
Google Scholar: <url>
Citations: <n> | h-index <n> | i10-index <n>

Blurb: <50 to 70 words. What they build or run, at what scale, and the one thing a CTO would take from them. No awards, no fellowships, no rankings.>
```

For a European professor who clears the bar, add one line under the card: `Europe-based. Sending because: <the reason in under 15 words>.`

For an auto-decline:

> Decline. <reason in one line, with the episode link or Arjun's prior call>. Notion: logged.

Nothing more. No preamble, no offer to change things.

## Constructing the Career Timeline

Build from LinkedIn, faculty pages and Step 2. Forward chronological, six to ten rows. Each row is a year range and a single event, kept terse.

Include education (institution, degree, advisor if notable), pre-academic industry roles if they carry the story, each faculty appointment, each company founded (mark founding rows clearly), frontier-lab roles, and major exits or transitions. Skip short stints and advisory-only roles unless they carry the story. Approximate years read "~2017". Pick the institution's own date when sources disagree.

## Constructing the Better Guest Available section

**Include it only when ALL of these hold:**
- A specific, named alternative exists at the same organisation (the technical co-founder, the PI who owns the lab, the Chief AI Officer above a VP).
- They would plausibly score higher on Audience Fit, usually because they own the technical arc or the deployment at scale.
- They are still at the organisation or its public face, and are plausibly bookable.

Never surface an exited founder or a ceremonial chair. When the person who replied is the best option, omit the section entirely. When it's included, write two to four sentences: who the alternative is, what story they own, and the bookability reality.

## Constructing the Themes to Cover

These are the segments Arjun anchors the conversation around. The show's rules apply:

- **Mechanism first, then the human outcome.** Each theme names a concrete technical decision or a deployment moment, and lands on what it changed for the people around it. "The week the policy transferred to a robot it had never seen" works. "Generalisation in robot learning" doesn't.
- **Usable by a practitioner.** At least half the themes should leave a CTO or AI lead with something they can apply: a build-versus-buy line, an evaluation method, a cost or latency number, a failure mode.
- **Specific to this guest**, rooted in something they built, published or said, and tied to the reply where they named an interest. Mark those "(their pick)".
- **Where Arjun has an edge.** Include at least one theme where Arjun's own production experience (autonomous driving at Apple, vision IP shipping in Mercedes cars, model compression for edge, FastCode deployments) lets him ask something a journalist can't. Name the link.
- **Fresh, not rehearsed.** Prefer ground the guest hasn't covered in every long-form appearance. Mark open roster territory "(new for HBD)".
- **No softballs, no credential theatre.** Nothing that is answerable from the homepage.

Aim for five to seven themes. Each is a **bold title sentence** plus one or two lines of elaboration.

## Voice rules for the page

- **Written for Arjun.** Direct, blunt, plain English. Use "you" where it's natural. Technical vocabulary is fine; hand-holding isn't.
- **No fluff.** Banned: "exciting opportunity", "great potential", "amazing journey", "powerhouse", "thought leader", "game-changing", "passionate", "world-class", "pioneering", "groundbreaking", "trailblazing", "revolutionary", "genuinely", "delve", "leverage", "unlock", "robust", "seamless".
- **No em dashes.** Use commas, parentheses or two sentences. Scan the whole page for the character before writing it.
- **No "It's not X, it's Y" constructions** and no padded lists of three.
- **Concrete numbers wherever possible**, graded "(filing)" or "(press)", with Scholar figures dated. If a number isn't known, write "Not disclosed" in the metrics strip and leave it out elsewhere. Never guess.
- **Flag uncertainty explicitly** with "(uncertain)" or "(couldn't verify)". Never fabricate a figure, quote, title, co-founder claim or link.
- **Awards appear only when legible outside research and load-bearing** (a Turing Award, a MacArthur, a TIME100 AI). No fellowships lists, no "top X under Y", no conference-panel mentions.
- **No judgments of past HBD guests or of people Arjun declined.** Calibrate privately; the page may travel.
- **Cold-reader test.** Every line must make sense to someone reading the page for the first time with no other context. Cut or rewrite any line that leans on this skill's internal shorthand or an unexplained reference: "the six", "the rock-star gate", "Type 1 / Type 2", "both lanes", "no cap" or "capped at" without the reason, rule numbers like "1e" or "1h", "today's list", a bare first name ("Philippe's episode" becomes "the Philippe Rambach (Schneider Electric) episode"), unexpanded acronyms on first use ("Ai2" becomes "the Allen Institute for AI (Ai2)"), and niche metrics without a label anyone understands ("D-index" becomes "h-index (CS only)"). Say the thing itself, not the name the skill gives it. Example: "Clears the rock-star gate, one step below the six" becomes "Field-defining work, and still at the frontier now" (Ali Farhadi page, 8 Oct 2026).

## Format examples


**Synthesis lines**

- Good: "Built the dataset every AV team benchmarks on, then spent five years turning it into a perception stack two OEMs ship."
- Good: "Runs AI for a 90,000-person insurer and has killed more pilots than most teams launch. Fortune 500-scale remit, but every interview so far is talking points. Strong consider until a long-form shows candour."
- Good (European professor): "Europe-based, but the causal-inference work is what half of applied ML now runs on, and the lab still publishes at the frontier. Sending for your call."
- Bad: "An accomplished researcher with an impressive background in AI." (No fact, no judgment.)

**Audience Fit bullets**

- "Stanford professor, and the company is the research shipped (diffusion LM in production at two enterprises)."
- "38k citations, 4.8× you; top-50; the 2025 work is frontier, the older line is mature."
- "Held to 6: the topic overlaps the Philippe Rambach (Schneider Electric) episode on running an enterprise AI platform."

**Sales Fit bullets**

- "Customer 4/5: on-vehicle deployment requirement and a 60-person team. Squarely FastCode's edge-compression credential."
- "Customer 1/5: defence UGVs, anti-ICP #5. No pipeline here, book on audience alone."
- "Capped at 2: Microsoft never outsources AI development, so its budget doesn't count. No pipeline here, book on audience alone." (components: Customer 1/5 · Money n/a · Influence 4/5)

**Theme**

- **The 300KB model that had to survive a winter test track.** What the team threw away to fit the model on the vehicle, and which failure only showed up in the field. Your Mercedes compression work makes this a peer conversation, not an interview. (new for HBD)

**Notes (where flags go)**

- "Microsoft comms will want sign-off: ask up front what's off limits."
- "Company claims 'first' in its category; two earlier entrants exist ([A], [B]). Don't repeat the claim on air."
- "India-based (Bengaluru). Offset: deployments in four EU markets."
- "Europe-based (ETH Zurich). Why send anyway: the 2024 world-model work is the reference every robotics lab now builds on."

## Chat reply examples

> Verdict: Book immediately. Audience Fit 9/10, Sales Fit 7.4/10.
> Notion: created engagement.

> Decline. 6,100 Scholar citations, below your ~8,000. Notion: logged.