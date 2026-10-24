# Perplexity Deep Research prompt template (Phase 1c)

Fill the bracketed slots from Phase 1a. Emit in a single clean code block, then the STOP text from SKILL.md. Nothing after it.

```
Deep research brief: [GUEST], [ROLE], [COMPANY].
Purpose: interview preparation for a podcast recording on [DATE]. Host is a technical
AI practitioner; guest is [DIAL DESCRIPTION]. I need unreported material, not a summary
of the public repertoire.

CONTEXT: I have already mapped the public set across [OUTLETS]. Do NOT return: [LIST
THE BURNED ITEMS VERBATIM]. All exhausted.

FIND THE FOLLOWING:

1. VENDOR DEPENDENCY. Every named third-party technology under [COMPANY]'s AI stack.
Which [COMPANY]-branded products are built on someone else's infrastructure, and has
anyone there publicly addressed concentration risk or lock-in? Quote verbatim, with
source and date. Check the vendors' own customer-story pages.

2. [THE SPECIFIC RECENT EVENT OR SITE VISIT]. Primary sourcing for every figure and
named person in it. What event produced the coverage, and what did [COMPANY] itself
publish about it?

3. THE UNCOMFORTABLE QUESTION. Every instance where [GUEST] has been asked about
[THE TENSION IN THEIR POSITION]. Has anyone pressed them on the gap between
[STATED POSITION] and [COMMERCIAL REALITY]?

4. DEPLOYMENT COUNTS. Every publicly stated figure for [COMPANY] AI use cases in
production, with date and source, from [YEAR] to now. Flag conflicts.

5. HEADCOUNT. Every publicly stated figure for the AI team, with date and source.

6. [THE NEWEST PRODUCT]. What is it, when did it launch, what is underneath it, and
has it shipped to customers or only been announced?

7. THE VERIFICATION SWEEP. For each of the following, tell me whether it appears
ANYWHERE in the public record, and if so give source and exact wording. If genuinely
absent, say so explicitly:
   (a) [INTERNAL-ONLY CLAIM 1]
   (b) [INTERNAL-ONLY CLAIM 2]
   (c) ...

8. CONTRADICTIONS. Any place where [GUEST] has given two incompatible accounts of the
same thing across different outlets or dates. Quote both with dates.

9. WHERE THEY HAVE BEEN CONTRADICTED. Any journalist, analyst, competitor or former
employee disputing a [COMPANY] claim. Any project that underperformed, was withdrawn,
or was quietly dropped.

10. COMPETITOR COMPARABLE. How [PEERS] have structured the same function, and any
public claim that contrasts.

OUTPUT RULES: Every claim carries a source URL and a date. Distinguish clearly between
what [GUEST] said and what a journalist wrote about [COMPANY]. Where sources conflict,
print both and flag it rather than picking one. Where you find nothing, say "no sources
found" rather than inferring. Prioritise the last 18 months. Include non-English sources
where the company is not US-headquartered.
```

## Notes
- Item 7 is the highest-value block. It converts internal-only material into a defensible "genuinely unreported" claim, which is what justifies the episode.
- Item 8 exists because contradictions are themes, not problems.
- Item 1 tells you to check vendor customer-story pages. Executives say things about dependency there that they never say in an interview.
