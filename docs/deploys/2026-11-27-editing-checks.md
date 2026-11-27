# Deploy: editing checks, 27 Nov 2026

- Source: routines/editing-checks.txt at e93f7eb (claude/business-os-structure-k3sqo5), 9,464 bytes, sha256 babe3703b0e19ce5eab5613558755bbb94426d99c986837b90ea5627496344f8.
- Changes from the live prompt (5bbd48c): decision 684 (un# leaves out the cinematic title tab and numbers the later tabs on); decision 687 (tab 6 adds 3 recommended 30-second trailers, FT pattern 2 or 3 bites, short VO, about 2 bites, cliffhanger); tab 1 line now says "the Thumbnail options tab" instead of "tab 8".
- Deployed by the Episode editor chat (session_019pwcV3jbCtwb56pcVB3o6J), 27 Nov 2026 08:48 UTC, with update_trigger (prompt only).
- Byte check of each update_trigger result against the file:
  - trig_01SXrnWJb2iz5Q3zts34VZu4 (13:15 IST): EQUAL, 9,464 bytes
  - trig_0177CBiFc4zP8SGCaVip97Gc (15:47, 22:47 IST): EQUAL, 9,464 bytes
  - trig_01AU4fQevmq39TDZX6LvC4cq (11:17, 12:17, 18:17 IST): EQUAL, 9,464 bytes
- Rollback: 5bbd48c (9,124 bytes, sha256 37c310bea05512925fec2238422c679d0c4bf7ab936ceaf7f209b5ad458928de).

## Second deploy, 27 Nov 2026, 09:38 UTC

- File: routines/editing-checks.txt at e6cf0fa, 9,812 bytes, sha256 043519846bec44be97f7abc5f0c247d79b56f2d64582a5823a7b481cc8185a43, no trailing newline.
- Change: decision 688, Part C tab 6 only. un# trailers have the same shape as Founder Thesis but no written VO; they use pieces of Sri's recorded intro VO split between the bites. Every un# tab uses onchain finance, tokenization, RWAs and stablecoins, never "crypto" or "DeFi" in titles, thumbnails, show notes, lower thirds or trailers, and nothing a regulator would be uncomfortable with. Every other line is identical to e93f7eb.
- Tasks: trig_01SXrnWJb2iz5Q3zts34VZu4, trig_0177CBiFc4zP8SGCaVip97Gc and trig_01AU4fQevmq39TDZX6LvC4cq, prompt only.
- Verify: each update_trigger result's prompt compared with the file byte for byte; all three EQUAL on the first deploy.
- Deployed by: Episode editor session (session_019pwcV3jbCtwb56pcVB3o6J).
- Rollback: e93f7eb (9,464 bytes, sha256 babe3703b0e19ce5eab5613558755bbb94426d99c986837b90ea5627496344f8).
