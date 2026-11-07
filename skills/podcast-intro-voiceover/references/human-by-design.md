# Human by Design (Arjun Jain)

## Host

Dr. Arjun Jain, founder of Fast Code AI (scaled from 6 to 45 people, serving Mercedes, Bosch, Volkswagen, Saudi Aramco). Before Fast Code: NYU Courant Institute under Yann LeCun, Max Planck Institute for Informatics, Apple's Project Titan autonomous driving team, Weta Digital (motion capture for *The Adventures of Tintin*), and sold computer vision IP to Mercedes-Benz North America (now in the MBUX system).

The voice: someone who has actually shipped production AI systems and knows the difference between a benchmark improvement and a system that works under real-world constraints. The intro should sound like a builder talking to other builders — not a media host introducing an expert, and not a hype-merchant celebrating an "AI visionary".

## Audience

AI decision-makers, CTOs, AI startup founders, applied researchers transitioning to industry, technical leaders deploying AI systems. ~240k LinkedIn followers. They open episodes because they're evaluating an AI investment, debugging a production model, deciding open vs closed strategy, or trying to scale a research team into an engineering org.

Assume they:
- Know the AI landscape (transformers, LLMs, RAG, fine-tuning, RLHF, agents).
- Know the major labs and companies (OpenAI, Anthropic, Google DeepMind, Meta FAIR, Mistral, xAI, Cohere).
- Know the production stack (PyTorch, JAX, TensorRT, vLLM, Kubernetes, Triton).
- Can handle technical depth — they're not casual observers.
- Will be put off by hype language, marketing copy, or anything that sounds like it was written for a non-technical audience.

## Target word count

**55-75 words.** Reads in about 25-35 seconds.

## Currency preference

**USD native.** Global technical audience, USD is the default for any financial figure (ARR, fundraise, contract size, compute spend).

## Structure (3 parts, in this order)

The defining feature of a Human by Design intro is that **credibility is established through technical pedigree and shipped systems, not headline metrics**. The audience doesn't care that the company raised $50M; they care what model it deployed and where.

### 1. Guest with technical credentials (research + production combo)
Open with the guest, role, and a credibility line that pairs **research depth** with **production reality** — the show's defining axis.

Pattern: `[Name] [role at company], where [shipped production thing].` Or: `[Name] is the founder of [company], building [specific technical thing]. Before that, [research credential at named lab] and [production credential at named company].`

Strong credibility signals for this audience:
- Named lab pedigree (FAIR, DeepMind, Google Brain, OpenAI, NYU/CMU/Stanford CS departments, Max Planck)
- Named advisor / collaborator (Yann LeCun, Geoff Hinton, Yoshua Bengio)
- Shipped at a recognizable place (Apple, Tesla Autopilot, Waymo, Anthropic, Mercedes MBUX)
- Built a specific technical artifact people would know (the original BERT paper, the Llama RLHF pipeline, a recognized open-source library)
- Production scale that implies real engineering ("deployed across 2 million vehicles", "serves 50B inference calls a month")

Avoid scale signals that sound corporate without technical content. "Raised $50M from a16z" alone is weak; "raised $50M from a16z to scale their inference infrastructure to 50B calls/month" works because the second clause adds technical content.

### 2. Why this guest matters as a builder
After credentials, surface **what specifically this guest has done that the audience would want to learn from**. This is the technical hook — what real problem did they solve, what real system did they ship, what real tradeoff did they navigate.

Pattern: **specific shipped system or technical decision that the audience would face.**

Examples:
- "His team shipped the first on-device computer vision model running under 5W in a production vehicle."
- "Built and open-sourced the inference engine now powering three frontier labs."
- "Made the call to abandon transformers for state-space models 18 months before Mamba dropped, and shipped a 7B model that beats Llama 2 on long-context benchmarks at a third the inference cost."
- "Took a research idea on federated learning out of FAIR and turned it into a deployed system across 200M phones."

Avoid: "leading the AI revolution", "pioneering AI-driven X", "transforming industry Y with AI". These say nothing about what was actually built.

### 3. Episode tease — the "In this episode..." line
End with a tease that promises **technical depth and a real decision**, not a generic AI conversation.

**Canonical podcast-name phrasing:** "Human by Design" (capital H, B, D, no "the", no "podcast" suffix — reads cleanly on its own). Use it in the tease line: "In this episode of Human by Design, Edul breaks down..." The opening slot ("Edul Patel joins us on Human by Design...") also works but the tease slot is the default.

**Bad (generic):**
- "In this episode, Arjun shares his thoughts on the future of AI."
- "In this episode, Arjun talks about building AI products."
- "In this episode, Arjun discusses open vs closed source AI."

**Good (specific, technical):**
- "In this episode, Arjun explains why his team trains on synthetic data for 80% of the pipeline, the failure modes that took eight months to debug, and the eval framework that finally caught them."
- "In this episode, Arjun breaks down the architectural decision to drop attention for the last six layers, the latency win that came from it, and the benchmark loss he was willing to accept."
- "In this episode, Arjun lays out why he thinks the inference cost curve is overrated and what actually bottlenecks production deployment at Fortune 500 scale."

Pattern: **specific technical decision + concrete mechanic + tradeoff or insight.** Technical specificity is the password into this audience. Vague AI talk gets skipped.

## Hook library — 5 tease angles

1. **Technical decision / architecture call (default)** — a specific engineering decision with tradeoffs. ("why his team dropped attention for the last six layers and accepted a 2-point benchmark loss")
2. **Production reality lesson** — what breaks between research and deployment. ("the eight-month debugging saga that turned a SOTA paper into a shipped product")
3. **Contrarian technical view** — a sharp view against the consensus. ("why he thinks the next breakthrough won't come from scale, and what his team is doing instead")
4. **Build-vs-buy / open-vs-closed call** — a strategic technical decision. ("why he chose to fine-tune Llama instead of paying GPT-4 API costs, the math behind it, and the inference setup that made it work")
5. **The unsexy infrastructure win** — the boring decision that produced the big result. ("the data pipeline rewrite that mattered more than the model architecture")
6. **Research-to-production translation** — taking a lab idea into the real world. ("how he turned a federated learning paper into a deployed system across 200M devices, and what the original paper got wrong")

Label each variation with its hook type (e.g., `Variation A (Technical decision / architecture call)`).

## What's allowed un-unpacked

This audience handles these without explanation:
- Transformers, attention, fine-tuning, RLHF, RAG, agents, MCP
- Open vs closed source, on-prem vs cloud, inference vs training
- Named models (GPT-4, Claude, Llama, Mistral, Gemini)
- Named labs and companies in the space
- Standard ML terminology (loss function, gradient, embeddings, tokens, parameters)
- Compute terms (FLOPs, GPU hours, H100, TPU)

These need a half-sentence unpack:
- Niche techniques (state-space models, MoE routing, speculative decoding, KV caching)
- Specific benchmarks (MMLU, HumanEval, GSM8K) when used as evidence
- Vertical-specific systems (MBUX, autonomous stack components)

## What this podcast is NOT

The intro should never sound like:
- A McKinsey AI report
- A LinkedIn AI thought-leadership post ("AI is transforming...")
- A hype celebration ("breakthrough", "revolutionary", "game-changing")
- A non-technical executive summary

It should sound like: **a senior engineer telling another senior engineer about a specific technical decision worth 60 minutes**.

## Recommendation guidance

Default to the **technical decision / architecture call** or the **production reality lesson** hook. The Human by Design audience presses play because they want technical depth that respects their intelligence. Anything that pattern-matches to AI marketing copy will get skipped in the first 10 words.

The contrarian-technical hook lands hard when the transcript has a real, defensible argument against consensus. Don't fake contrarianism — this audience will detect it instantly.

## Worked example

> "Edul Patel founded Mudrex, the crypto investment platform serving Indian retail investors, and built the recommendation engine that now allocates $50M+ in AUM across automated strategies. Before that, he led applied ML at Goldman Sachs, shipping execution algorithms that traded billions in daily volume. In this episode of Human by Design, Edul breaks down the architectural decision to abandon deep models for tree ensembles in execution, the latency math that drove it, and why he thinks LLMs are still the wrong tool for production trading."

**Word count:** ~85 words. Slightly over target — could trim to 75 by tightening clause two.

### Annotation

- **Part 1:** Name, company, specific shipped system (recommendation engine + AUM). Production credential first.
- **Part 2:** Prior credentials with named institution (Goldman) and named technical artifact (execution algorithms + scale). Research-to-production combo.
- **Part 3:** Three specific things — architectural call (deep models vs tree ensembles), the math behind it, and a contrarian view (LLMs wrong for production trading). All technical, all defensible, none generic.

## Style notes specific to Human by Design

- Technical precision matters more than dramatic phrasing. "Shipped a 7B model" is stronger than "built groundbreaking AI".
- Reference real systems and benchmarks where possible. Vague "AI capabilities" reads as marketing copy.
- It's fine — even good — to use technical terms (MoE, KV cache, speculative decoding) once if the transcript discusses them substantively. The audience will respect the unhidden depth.
- Arjun's voice carries weight from his Apple / Mercedes / Yann LeCun pedigree. Avoid intros that sound like he's interviewing a peer he doesn't respect — every guest should be presented as someone whose work he wanted to understand.
- Avoid the word "AI" as a noun when you can use a more specific term. "His computer vision system" is stronger than "his AI system". "The 7B language model" beats "the AI". This is a builder's show; builders are specific about what they build.

## Pre-interview mode

In pre-interview mode, only the dossier exists. Parts 1 (guest + credentials) and 2 (why this guest matters as a builder) are unchanged — both come from the dossier and are pure credibility content. Only part 3 (tease) shifts.

**Part 3 — tease shifts to anticipatory framing.** Replace transcript-based verbs ("breaks down", "explains how", "lays out") with anticipation verbs ("I want to understand", "we'll get into", "expect a conversation about", "we're going deep on").

The technical specificity requirement does not relax in pre-interview mode. The audience still expects named systems, real benchmarks, and actual tradeoffs. Pull these from the dossier rather than fabricating from imagined transcript moments.

Topic territory in Human by Design pre-interview mode draws from:
- The guest's named shipped systems and what they're built on
- Public technical positions (open-source releases, papers, conference talks)
- The technical debates the guest's work sits inside (open vs closed, attention vs SSM, scale vs efficiency)
- Recent technical releases in the guest's domain that they'll have a view on

### Worked example (pre-interview version)

> "Edul Patel founded Mudrex, the crypto investment platform serving Indian retail investors, and built the recommendation engine that now allocates $50M+ in AUM across automated strategies. Before that, he led applied ML at Goldman Sachs, shipping execution algorithms that traded billions in daily volume. In this conversation on Human by Design, expect a deep look at the architecture choices behind low-latency execution systems, where Edul sees the line between deep models and tree ensembles in production trading, and why he thinks LLMs are still the wrong tool for live execution."

**Word count:** ~90 words.

### Notes

- Parts 1 and 2 are identical to the post-recording version.
- The tease references real technical territory (execution architecture, deep vs tree ensembles, LLMs in trading) — all visible in the dossier or inferable from Edul's prior public positions.
- "Expect a deep look at" and "where Edul sees the line" replace transcript verbs without sacrificing specificity.

### Hook library adjustments

For pre-interview mode, the hook angles rephrase:

| Post-recording hook | Pre-interview equivalent |
|---|---|
| Technical decision ("why his team dropped attention for the last 6 layers") | Architecture territory ("the architecture decisions behind low-latency execution") |
| Production reality ("the 8-month debugging saga that turned a SOTA paper into a product") | Production territory ("what actually breaks between research and shipped systems") |
| Contrarian technical view ("why he thinks the next breakthrough won't come from scale") | Contrarian territory ("his view on where the next AI capability gains will come from") |
| Build-vs-buy ("why he chose to fine-tune Llama instead of paying GPT-4 API costs") | Strategy territory ("the inference cost math behind fine-tune vs API decisions") |

### Refusal condition for pre-interview mode

If the dossier is a thin bio with no named shipped systems, no public technical positions, and no clear domain debates the guest sits inside, **decline to draft pre-interview**. A pre-interview intro for Human by Design needs real technical hooks to land with this audience — and inventing them is a serious failure mode. Tell the user the dossier needs to include at least: named shipped systems, the technical stack involved, and at least one public position the guest has taken.
