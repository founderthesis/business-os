#!/usr/bin/env python3
"""Apply fix5.py to fresh page copies: python3 fix637_apply.py <before_dir> <after_dir>.

Reuses apply_notion.py (anchors must match once, plans written per page) and adds the
MUST_GO check: every stale date-owner phrase must be gone from the new text.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import notion_edits as ne  # noqa: E402
import apply_notion  # noqa: E402
import fix5 as fix637  # noqa: E402

ne.EDITS, ne.PAGES, ne.MUST_KEEP = fix637.EDITS, fix637.PAGES, fix637.MUST_KEEP
apply_notion.main()
dst = sys.argv[2]
for name, phrases in fix637.MUST_GO.items():
    text = open(os.path.join(dst, name + ".md"), encoding="utf-8").read()
    left = [p for p in phrases if p in text]
    if left:
        raise SystemExit(f"{name}: still has {left}")
print("MUST_GO: clean")
