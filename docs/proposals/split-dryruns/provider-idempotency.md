# Provider duplicate-send test, 26 Oct 17:31 JST (real send, self-addressed)

Zoya's inbox sent to Zoya's own address, so no person received anything. Two identical `email_compose` calls (action send, same to, subject and body, include_signature false) both used idempotency_key `split-launch-test-idem-20261026-1`.

1. The first call returned status sent, Message-ID `58c3f410-fc78-4b45-ad1f-d2a5206768d9@mcpemails.com`.
2. The second call returned `idempotent_replay: true`, with the same Message-ID and "No new email was sent."
3. Search afterwards found:
   - INBOX: one delivered copy (INBOX:461).
   - Sent: two filed copies (634 and 635), both from the single send, with the same date and Message-ID. This is the known double filing.

**PASS:** the provider sends once per key within 24 hours, and delivery is one message. A Sent count must therefore key on Message-ID, as ACTIONS says ("two Sent copies with one Message-ID are one send").

The provider only dedupes an identical call. A retry that rebuilds the draft or rewords the body isn't deduped by the key, so only the thread check catches it. The kill test covers that case.
