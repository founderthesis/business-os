# B1 (calendar) and decision 424

**Built so far:** `calendar_b1.py` on the d420 batch calendar.
- Output 57,968 B / f6d140196f3b75b4. Cleanup accepted it (759daf4) as the calendar to deploy.
- Its 424 text: the booker attaches only on evidence naming the guest, and a FOLD rule.

## Next follow-up for Cleanup: CX-20261029-03 (Codex)

Until this is built, **no routine retires a duplicate**:
- a duplicate a routine finds stays as it is;
- the routine reports it, naming both rows and why it thinks they're the same.

That holds for the calendar, the inbox (d420 round 7) and Zoya (decision 424 text in zoya-one). The FOLD clauses already deployed or accepted change to "report, don't fold" until the five points below are in, so they're never run in their current form.

The fold is built only when all five hold:

1. **A deterministic survivor.** Rank the two rows, in this order:
   - open before closed;
   - further along the guest ladder (Booked > Booking > Precall done > Precall requested > Decision pending > Interested > Contacted > New);
   - a Guest that is the guest themselves, not a contact;
   - more Activities;
   - older Captured;
   - lower page id.

   The first rule that separates them decides, and the report names that rule.
2. **A valid eval carries over.** If the survivor has no Eval link, or one that isn't claude.ai, and the duplicate has a claude.ai Eval link, copy the duplicate's link along with Eval verdict, Eval date and its "## Eval (" sections. A survivor's own valid eval is never overwritten. Two valid evals: the newer stays in Eval link, and the other goes in a Claude note line with its date.
3. **Conflicting evidence is kept, not resolved:**
   - different Status, Tier, verdict, Your call or decision lines;
   - different Scheduling lines;
   - a call on each row.

   Each of the duplicate's values goes into the survivor's page body under "## Folded from <duplicate name> (<date>)", word for word. The survivor's fields stay as they were. If both rows hold a decision of Akshay's, nothing folds and it's reported (as decision 424 says).
4. **Every relation is moved, not just Activities.** Each relation on the duplicate moves to the survivor. People relations (Guest, Via, Stakeholders) all become survivor Stakeholders, except the survivor's own Guest. That covers:
   - Activities;
   - Episode;
   - Deal;
   - Organisation;
   - For engagement on Task rows that point at the duplicate;
   - Eval slots rows that point at it;
   - Guest, Via and Stakeholders;
   - any other relation property on its schema.

   The routine fetches the Engagements schema at run time and moves every relation property it finds, not a fixed list. It also moves the back-relations: rows elsewhere whose relation points at the duplicate.
5. **Nothing left, read back.** Re-fetch the duplicate. Trash it (decision 416) only when every relation property is empty and no row elsewhere points at it. Otherwise leave it, with a Claude note line "fold incomplete: <relation> still set", and report it. Re-fetch the survivor and check that each moved item is there.

**Tests (offline replay, twice):**
- a survivor chosen by each rule;
- a blank survivor that gains the eval;
- two valid evals;
- different Status on each row, with both kept;
- an Episode and a Deal on the duplicate, both moved;
- a Task row's For engagement repointed;
- one relation that won't clear, so no trash;
- a decision of Akshay's on each row, so no fold and a report.

**Size:**
- The calendar has about 7.3 KB of room.
- Zoya's FAST prompt has room.
- The inbox has 3 bytes. The inbox fold rule gets one pointer instead of the full text: "FOLD: report a duplicate, never retire it (CX-20261029-03)". The calendar is the only routine that folds, until a sweep step takes it over.
