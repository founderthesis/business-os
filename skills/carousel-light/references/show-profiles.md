# Show Profiles

Per-podcast configuration for carousel-light. Pick the profile matching the episode's show, filter quote extraction to the show's theme territory, and use the brand chrome values in the copy JSON.

If the show is ambiguous from the transcript or user message, ask before extracting.

---

## Built to Share (host: Satish Mugulavalli)

**Theme territory (extract quotes ONLY from this space):** talent, hiring, ESOPs and equity design, wealth creation for employees, org building, culture, leadership, compensation philosophy, founder decisions about people.

**Lessons line pattern:** "N lessons on talent, from N years of building."

**Brand chrome (matches the Ravi Saxena reference deck exactly):**
```json
{
  "accent": "#f04f23",
  "bg": "#1a2742",
  "logo_html": "h<span class=\"dot\">i</span>ssa",
  "logo_serif": true,
  "attribution": "ON BUILT-2-SHARE",
  "wordmark_html": "BUILT <span class=\"two\">&#8212;2&#8212;</span> SHARE",
  "wordmark_sub": "WITH SATISH MUGULAVALLI"
}
```

**CTA link pattern:** `built2share.in/[guest-first-name-or-slug]` (e.g. built2share.in/ravi). Confirm the slug with the user before publishing; flag it in the handoff message.

**CTA label:** WATCH THE FULL EPISODE

---

## un# (host: Sri Misra)

**Theme territory:** DeFi and crypto. How on-chain finance runs mainstream finance better, protocol design, tokenomics, market structure, crypto adoption, regulation, institutional crypto. Audience is largely Indian and NOT crypto-native, so support text must educate: unpack jargon ("on-chain" means recorded on a public ledger anyone can verify) rather than assume it.

**Lessons line pattern:** "N takes on DeFi, from the un# conversation." (adapt naturally; "lessons on talent" is wrong here)

**Brand chrome:**
```json
{
  "accent": "#f04f23",
  "bg": "#12151f",
  "logo_html": "aarn&acirc;",
  "logo_serif": false,
  "attribution": "ON UN#",
  "wordmark_html": "un<span class=\"two\">#</span>",
  "wordmark_sub": "WITH SRI MISRA"
}
```
aarnâ branding uses a darker near-black background. If the user has exact aarnâ hex values or a different accent, take theirs.

**CTA link:** No confirmed URL pattern on file. Ask the user for the episode link. Do not invent one.

**CTA label:** LISTEN TO THE FULL EPISODE

---

## Founder Thesis (host: Akshay Datt)

**Theme territory:** scaling up. Zero-to-one to one-to-many, growth levers, fundraising, unit economics, distribution, hiring for scale, operational systems, pivots, category creation in India.

**Lessons line pattern:** "N lessons on scaling up, from N years of building."

**Brand chrome:**
```json
{
  "accent": "#f04f23",
  "bg": "#1a2742",
  "logo_html": "FT",
  "logo_serif": false,
  "attribution": "ON FOUNDER THESIS",
  "wordmark_html": "FOUNDER <span class=\"two\">THESIS</span>",
  "wordmark_sub": "WITH AKSHAY DATT"
}
```
No sponsor mark on file for Founder Thesis; "FT" monogram is a stand-in. Ask the user if there's a logo asset or preferred wordmark.

**CTA link:** No confirmed URL pattern on file. Ask the user.

**CTA label:** LISTEN TO THE FULL EPISODE

---

## Human by Design (host: Dr. Arjun Jain)

**Theme territory:** AI and the humans building it. Research breakthroughs explained plainly, AI founder journeys, academia-to-startup, what AI changes about work and society. (Theme default inferred from the show's guest bar: professor + AI researcher + founder. Confirm with the user if unsure.)

**Lessons line pattern:** "N ideas on AI, from the Human by Design conversation."

**Brand chrome:**
```json
{
  "accent": "#f04f23",
  "bg": "#1a2742",
  "logo_html": "HbD",
  "logo_serif": false,
  "attribution": "ON HUMAN BY DESIGN",
  "wordmark_html": "HUMAN <span class=\"two\">BY</span> DESIGN",
  "wordmark_sub": "WITH DR. ARJUN JAIN"
}
```
Placeholder chrome; confirm logo and wordmark with the user.

**CTA link:** No confirmed URL pattern on file. Ask the user.

**CTA label:** WATCH THE FULL EPISODE
