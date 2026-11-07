# Akshay's Question Voice — read before writing any question

Every question in the dossier gets written in this register. Questions drafted in neutral written English get rewritten by hand, every time. This file exists so that stops happening.

The substance of a question is decided by the theme. **This file governs how it is said.** Same fact, wrong voice, is a failed question.

---

## The core problem to avoid

Claude's default question voice is a print journalist's: crisp, balanced, one clean clause, slightly adversarial. Akshay's is a curious operator's: conversational, wordy, hedged, full of connectors, often putting himself in the story. He rambles toward the question rather than firing it.

> **Journalist:** "What is structurally cheaper about your operation?"
> **Akshay:** "Groww is making about ₹19.8 an order. You charge ₹10, and you never had the rebate they had. So how does that work?"

Same question. Only the second one will get asked.

---

## Six question shapes he actually uses

Use several of these across the theme set. At minimum, the dossier should contain **one self-inserting hypothetical** and **one candidate-answer stack**.

### 1. The candidate-answer stack
Ask the question, then immediately offer two or three possible answers, then hand it over. This is his standard opener shape.

- *"What's the right industry for SatSure? Is it space tech? Is it SaaS? How do you categorize it?"* (SatSure recording)
- *"Why is it the guest? Is he well-known? Like, does he have a certain following?"* (Sowjanya recording)

### 2. The self-inserting hypothetical
He puts himself in the customer's seat and builds a small scenario, rather than asking abstractly. This is his single most distinctive move and the easiest to forget.

- *"Could I just tell the agent, go make money for me, here's one lakh?"* (Dale pre-call)
- *"What if I connect my Claude through an MCP to Sahi and tell it, if there is bad news about any of my portfolio companies, tell me immediately?"* (Dale pre-call)

### 3. The conventional-wisdom pushback
He never tells a founder they are wrong. He puts the received view in the room and lets that do the pushing.

- *"Why not focus? The traditional wisdom is to focus and make one thing scale before you diversify."* (Sowjanya recording)
- Pattern: *"The conventional wisdom says X, so what do you know that they don't?"*

### 4. The plain money question
He asks about money bluntly and without apparatus. He describes this as his own signature: *"my conversations go very deep into numbers as well, asking people, how do you make money."*

- *"How do you make money?"*
- *"What kind of views did you get on this one video?"*
- *"How do you monetize, what does your revenue look like?"* (Dale pre-call)

Do not dress these up. "Walk me through your unit economics" is not this.

### 5. Math out loud, then check
He does the arithmetic in the question and asks the guest to confirm or correct, the same way he plays back a moat.

- *"11 crore trades at ₹10 is roughly ₹110 crore. Am I in the right zone?"*
- *"So essentially the moat for you is the algorithm plus the business context, essentially."* (SatSure recording)

### 6. The decode demand
He asks openly to be taught, and positions himself as the one who does not know.

- *"What does it mean when you say you're selling outcome? Just break it down in a more layman-friendly way."* (SatSure)
- *"I don't fully understand what is futures and options, and why are people so crazy about F&O trading. Are you willing to do a 101 with me?"* (Dale pre-call)
- *"Give me a real-world example with, say, a financial institution. What problem statement did they come to you with?"* (SatSure)

### Supporting habits
- **Staged growth question:** *"First 100 users, then the first 1,000, then the first 1,00,000. What worked at each stage?"* Use verbatim when growth is a theme.
- **Forward projection:** *"Isn't this a six-months-to-one-year phase? Wouldn't the technology be so much better in a year's time?"*
- **Soft risk framing:** *"But doesn't it also sound super risky, because what if someone lost money and blamed the AI, and therefore blamed you?"* The bad outcome is hypothesised, not alleged.
- **Zoom in, zoom out:** deep into mechanics, then an explicit pull back to the model.

---

## Register notes

- **Conversational connectors are correct, not sloppy.** "So", "and then", "you know", "I mean", "okay", "because here is where I get stuck". Leave them in. Stripping them produces the journalist voice.
- **Longer beats crisper.** A question that runs two sentences and doubles back is more him than a tight one-liner.
- **First person, present tense, concrete.** "When I place an order and pay you ₹10, who is taking what out of that?"
- **He positions himself as the learner**, even on things he understands. That is the device that lets the audience follow.
- **He is warm.** Even the hard questions are asked as puzzles he is stuck on, not charges he is laying.

---

## Banned phrasings

Each of these has been written into a dossier and struck out by hand.

| Banned | Why | Write instead |
|---|---|---|
| "Defend that." | Combative, clipped, courtroom | "Explain that to me." |
| "Why are they wrong?" | Puts the guest against peers | "The conventional wisdom says X, so what do you know that they don't?" |
| "What has to be true by FY28?" | Pure VC-speak, he never says it | "What does this need to look like in three years?" |
| "What is structurally cheaper about you?" | Analyst noun-phrase | "So how does that work?" |
| "Take me through that." | Generic podcaster filler | "Explain that to me" or the candidate-answer stack |
| "Industry-normal?" / "Close?" / "Where is that line?" | Clipped fragments; he does not clip | "Is that just how the industry is?" |
| "Conviction, or liability management?" | Writerly binary in analyst vocabulary | "Where does it stop?" |
| "Walk me through your unit economics." | Consultant register | "How do you make money?" |
| "Is that a moat or a compliance tax?" | Essay phrasing | "Does that actually keep anyone out, or is it only cost?" |
| "What did you give up that you underestimated?" | Therapy register | "When you told people, what did they say to you?" |

**General test:** if the sentence would sit comfortably in a Financial Times interview or a VC memo, it is wrong. If it would sit comfortably in a WhatsApp voice note from a curious friend who has done his homework, it is right.

---

## Two worked rewrites

**Theme: the AI product line**

> ✗ "You've drawn a hard line at autonomous execution. Conviction, or liability management? What does KYRO do that a chatbot with market data can't?"
>
> ✓ "Could I just tell your AI, here is one lakh, go make money for me? Where does it stop? And if I connect my own Claude to SAHI through an MCP and it loses my money, is that your problem or mine?"

**Theme: the concentration bet**

> ✗ "Everyone above you is cutting F&O dependence while you go deeper. Why are they wrong? $200 million on a base that was zero eighteen months ago. What has to be true by FY28?"
>
> ✓ "Groww and Zerodha are both moving out of F&O into MTF and lending. You are going deeper in. The conventional wisdom says diversify, so what do you know that they don't? And $200 million on a business that was zero eighteen months ago, what does this need to look like in three years?"

---

## Where to recalibrate

Before drafting, if source material is available:

- `sed -n '1,150p'` on any project transcript `.txt`, then extract his turns containing a question mark. Even recordings where he is the guest reveal the register.
- **Mine the pre-call transcript for this specific guest.** Questions he already asked there are the highest-confidence material in the entire dossier: they are verbatim him, on this topic, and a question that landed in the pre-call should usually be re-asked on the record.
- `project_knowledge_search` for past dossiers and interview transcripts.

If none of that exists, this file is sufficient. Do not draft without it.
