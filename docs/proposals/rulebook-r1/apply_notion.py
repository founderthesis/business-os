#!/usr/bin/env python3
"""Apply notion_edits.py to fetched page text and write the new page text.

Usage: python3 apply_notion.py <before_dir> <after_dir>
<before_dir> holds <short-name>.md, each the <content> of a fresh notion-fetch
(first line may be an HTML comment). Fetch again right before cutover: the
edits fail loudly if the page moved under them. Output goes to <after_dir>,
which should be git-ignored (pages carry mailto links). Prints sizes.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import notion_edits as ne  # noqa: E402


def once(text, s, what):
    n = text.count(s)
    if n != 1:
        raise SystemExit(f"{what}: found {n} times: {s[:90]!r}")
    return text.index(s)


CHILD = re.compile(r'<(?:page|database)[^>]*?url="([^"]+)"')


def apply(name, text, plan=None):
    plan = [] if plan is None else plan
    for op in ne.EDITS.get(name, []):
        kind, subj = op[0], op[1]
        tag = f"{name} {subj} {kind}"
        if kind == "replace":
            once(text, op[2], tag)
            plan.append({"op": "update_content", "old_str": op[2], "new_str": op[3], "subject": subj})
            text = text.replace(op[2], op[3])
        elif kind == "between":
            a = once(text, op[2], tag + " start")
            b = text.find(op[3], a)
            if b < 0 or text.count(op[3], a) != 1:
                raise SystemExit(f"{tag}: end not found once after start: {op[3][:90]!r}")
            plan.append({"op": "update_content", "old_str": text[a:b + len(op[3])], "new_str": op[4], "subject": subj})
            text = text[:a] + op[4] + text[b + len(op[3]):]
        elif kind == "whole":
            plan.append({"op": "replace_content", "new_str": op[2], "subject": subj})
            text = op[2]
        elif kind == "replace_all":
            n = text.count(op[2])
            if n < 1:
                raise SystemExit(f"{tag}: not found: {op[2][:90]!r}")
            plan.append({"op": "update_content", "old_str": op[2], "new_str": op[3], "replace_all_matches": True, "subject": subj})
            text = text.replace(op[2], op[3])
            print(f"  {name}: replaced {n} x {op[2][:50]!r}")
        elif kind == "drop_toggles":
            pat = re.compile(r"<toggle[^>]*>.*?</toggle>\n?", re.S)
            hits = [m for m in pat.finditer(text) if op[2] in m.group(0)]
            if not hits:
                raise SystemExit(f"{tag}: no toggle holds {op[2]!r}")
            for m in reversed(hits):
                plan.append({"op": "update_content", "old_str": m.group(0), "new_str": "", "subject": subj})
                text = text[:m.start()] + text[m.end():]
            print(f"  {name}: dropped {len(hits)} toggles with {op[2]!r}")
        elif kind == "drop_section":
            h = "## " + op[2]
            a = once(text, h, tag)
            nxt = text.find("\n## ", a + len(h))
            span = text[a:nxt + 1] if nxt >= 0 else text[a:]
            plan.append({"op": "update_content", "old_str": span, "new_str": "", "subject": subj})
            text = text[:a] + (text[nxt + 1:] if nxt >= 0 else "")
        else:
            raise SystemExit(f"unknown op {kind}")
    if "—" in text:
        print(f"  warning: {name} still has an em dash")
    return text


def fill_ids(text):
    """Group chat ids live outside git: data/rulebook-r1/ids.json (git-ignored)."""
    p = os.path.join(HERE, "..", "..", "..", "data", "rulebook-r1", "ids.json")
    ids = json.load(open(p)) if os.path.exists(p) else {}
    for k, v in ids.items():
        text = text.replace("{" + k + "}", v)
    left = re.findall(r"\{[A-Z_]+_ID\}", text)
    if left:
        raise SystemExit(f"unfilled ids {left}: create data/rulebook-r1/ids.json from the live routines/zoya-day.md")
    return text


def main():
    src, dst = sys.argv[1], sys.argv[2]
    os.makedirs(dst, exist_ok=True)
    for name in ne.EDITS:
        raw = open(os.path.join(src, name + ".md"), encoding="utf-8").read()
        body = re.sub(r"\A<!--.*?-->\n", "", raw, flags=re.S)
        plan = []
        new = fill_ids(apply(name, body, plan))
        for p in plan:
            for k in ("old_str", "new_str"):
                if k in p:
                    p[k] = fill_ids(p[k]) if "_ID}" in p[k] else p[k]
        lost = set(CHILD.findall(body)) - set(CHILD.findall(new))
        if lost:
            raise SystemExit(f"{name}: would drop child pages or databases {sorted(lost)}: move them first or keep their blocks")
        json.dump({"page_id": ne.PAGES[name], "ops": plan}, open(os.path.join(dst, name + ".plan.json"), "w"), indent=1, ensure_ascii=False)
        open(os.path.join(dst, name + ".md"), "w", encoding="utf-8").write(new)
        print(f"{name:16} {ne.PAGES[name]}  {len(body):>7} -> {len(new):>7} chars")


if __name__ == "__main__":
    main()
