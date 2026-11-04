# Capture r13b (4 Nov)

| File | Bytes / sha256 |
|---|---|
| `capture.txt` (r13b) | 47,384 / 4029933c61f5a975 |
| r13 (replaced) | 46,842 / 7482f2f1132bd2e6 |
| Base: live r12e (`../capture-r12/capture.txt`) | 46,565 / 9caf2cdb |

**Build:** `python3 patch.py ../capture-r12/capture.txt <out>`. It asserts the base 9caf2cdb, and each edit exactly once. Patched twice, byte-identical, no em dashes.

1. **Decision 457 (KEY):** a pitch from outside the team with ad@ on To or Cc is never left for Zoya. Capture logs it in the same run: MSGID FIND, then REF, then RAW by HEAD.
2. **Decision 463.7 (STEP 3):** a mail that names a new guest on an existing thread belongs to that guest, whatever the old row's Status: open, Parked or closed. That covers Thinking Balloon on the Parked CloudThat thread.
   - Capture finds the guest's own Engagement on that show, or creates one as the pitch bullet says, and links the mail there.
   - The old row gets only a Claude note line, never a Status or Next action change.

**Status:** built, not replayed. Ready for Cleanup. The CTO deploys.
