# Host rundown spec (Phase 2d)

A single self-contained HTML file. The reading surface before the record and the instrument during it. Two modes, because those are different jobs and one document serves neither.

## Constraints
- White background, dark text, **one** accent colour. Never a dark theme.
- Use weight, dimming and strikethrough for hierarchy instead of a second colour. Burned material is struck through and greyed, not red.
- **No localStorage, sessionStorage or any browser storage.** State is in-memory and session-only. That is the right trade for a 90-minute artifact.
- Phone-first. It will be read on a phone and used on a laptop propped next to a camera.
- Google Fonts with system fallbacks. Assume the studio wifi may be bad.
- Keyboard focus visible, reduced motion respected, print stylesheet that drops the chrome.

## Mode 1: Brief (default)
For reading before the record. Inverts the dossier's hierarchy deliberately.

1. **The hook**, as a pull quote.
2. **"Read these two first"**: the behavioural instruction and the framework to bring, as the only filled boxes on the page. This is the single most important UX decision: behaviour goes first, facts go into disclosure.
3. **Works / Fails** boxes.
4. **Nouns worth interrupting on**, listed.
5. **Reference**: everything factual as `<details>` cards under a line saying none of it needs memorising: who he is, the org, numbers, the architecture question, internal-call substance, fact flags, burned material, do-not-go-here.
6. **Before the record**: clickable links, triaged.

Target reading time: four minutes.

## Mode 2: Live
For use during the recording.

- **Sticky act clock.** Elapsed time, the act the host *should* be in, a segment bar that fills. Start, pause, reset.
- **Interrupt meter.** A tappable timer for the current answer. Past the guest's known answer-length threshold it changes state and tells the host what to do: pick a noun and interject. This exists because no static document can help with pace, and pace is usually the biggest risk. Only include when the interview-technique block identifies a pace problem.
- **Themes grouped by act**, each with the minutes budget shown.
- **Questions as tappable rows** that strike through when asked. Provenance and clearance caveats attach to the individual question, not to a separate section, so they surface at the moment of asking.
- **Mark covered** per theme; the theme dims.
- **Persistent footer** showing coverage: themes covered, questions asked. At minute 60 the host can see he has never touched Act 3.
- **"Don't ask" drawer**, one tap from anywhere, containing burned material, do-not-go-here, the recovery moves, and the interrupt nouns. Burned material is useless in an appendix and useful mid-question.

## What not to build
- No dark mode toggle.
- No second accent colour.
- No animation beyond state changes.
- Nothing that requires network access at record time except fonts.
