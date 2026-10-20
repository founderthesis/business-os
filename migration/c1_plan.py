#!/usr/bin/env python3
"""Consolidation 1 pilot planner: sponsored obligations move from an Engagement's Next action to Kind Task rows.

Input: an export JSON (list of {id, properties, sections}) taken right before migrating, and the mapping below.
Output: plan JSON (Task rows to create, Engagement edits) and a conservation check: every " | " segment of each
Engagement's Next action ends up in exactly one place (left on the Engagement, or on exactly one Task row).
A mismatch stops that row. Nothing here writes to Notion; the writer applies the plan with the Notion connector.
Usage: python3 -I c1_plan.py <export.json> <plan.json>
"""
import sys, json

# Per row: which segment indexes go to which obligation, and the obligation row's own date and owner.
# "call_check": the Engagement keeps Next date only if a future calendar event of this Call type exists (checked at migration).
MAP = {
 "3f019a301a7f810aaef8d6dfbbaff143": {"rows": [{"ob": "Sponsored chase", "segs": [0], "date": "after_call", "wait": ["Guest or PR"], "state": "Awaiting someone else"}], "call_check": "Precall"},
 "3f019a301a7f819c9730ccc8067f0927": {"rows": [{"ob": "Sponsored chase", "segs": [0], "date": "2026-10-26", "wait": ["Zoya"], "state": "Handed over"}], "call_check": "Precall", "move": ["Next sponsored mail"]},
 "3f019a301a7f81178bd4ea089dfa2cf2": {"rows": [{"ob": "Sponsored next steps", "segs": [0], "date": "2026-10-22", "wait": ["Zoya"], "state": "Handed over"}], "move": ["Next sponsored mail"]},
 "3f719a301a7f81a18038db4a0673aaee": {"rows": [{"ob": "Sponsored next steps", "segs": [0], "date": "2026-10-23", "wait": ["Guest or PR"], "state": "Awaiting someone else"}], "move": ["Next sponsored mail"]},
 "3f019a301a7f8177a804ed083e54f7a3": {"rows": [{"ob": "Sponsored chase", "segs": [0, 1], "date": "2026-10-27", "wait": ["Zoya", "Guest or PR"], "state": "Handed over"}], "move": ["Next sponsored mail"]},
 "3f719a301a7f81cb9bbaf1abb2d68ede": {"rows": [{"ob": "Sponsored chase", "segs": [0], "date": "2026-10-25", "wait": ["Guest or PR"], "state": "Awaiting someone else"}]},
 "3fa19a301a7f8118a06aea18fea5d7f9": {"rows": [{"ob": "Sponsored chase", "segs": [0], "date": "2026-10-25", "wait": ["Guest or PR"], "state": "Awaiting someone else"}]},
 "3f019a301a7f8111b5ebcc4d67721479": {"rows": [{"ob": "Sponsored chase", "segs": [0, 1], "date": "2026-10-20", "wait": ["Zoya", "Guest or PR"], "state": "Handed over"}], "move": ["Next sponsored mail"]},
 "3f019a301a7f813a841ecd974cdbc9b6": {"rows": [{"ob": "Sponsored chase", "segs": [0, 1], "date": "2026-10-20", "wait": ["Zoya", "Guest or PR"], "state": "Handed over"}], "move": ["Next sponsored mail"]},
 "3f919a301a7f8198b010e0a43ed836fc": {"rows": [{"ob": "Sponsored chase", "segs": [0], "date": "2026-10-25", "wait": ["Guest or PR"], "state": "Awaiting someone else"}]},
}
SLUG = {"Sponsored chase": "sponsored-chase", "Sponsored next steps": "sponsored-next-steps",
        "Payment reminder": "payment-reminder", "Payment confirmation": "payment-confirmation"}

def segs(na):
    na = (na or "").replace("\\|", "|")
    return [x.strip() for x in na.split(" | ") if x.strip()]

def main(exp_path, out_path):
    E = {r["id"]: r for r in json.load(open(exp_path))}
    plan, ok_all = [], True
    for pid, m in MAP.items():
        r = E[pid]; p = r["properties"]
        S = segs(p.get("Next action"))
        used = [i for row in m["rows"] for i in row["segs"]]
        keep = [i for i in range(len(S)) if i not in used]
        ok = sorted(used + keep) == list(range(len(S))) and len(used) == len(set(used))
        name = p.get("Name", "").split(",")[0]
        rows = []
        for row in m["rows"]:
            rows.append({
                "Name": f"{row['ob']}: {name}",
                "Kind": "Task", "Obligation": row["ob"],
                "For engagement": [pid], "Show": p.get("Show"),
                "Waiting on": row["wait"], "Task state": row["state"],
                "Next action": " | ".join(S[i] for i in row["segs"]),
                "Next date": row["date"], "Chase step": p.get("Chase step"),
                "Source ID": f"obl:{SLUG[row['ob']]}:{pid}", "Source": "Agent",
                "body_sections": {h: r["sections"][h] for h in m.get("move", []) if h in r["sections"]},
            })
        eng = {"Next action": " | ".join(S[i] for i in keep),
               "Waiting on": "owners of the kept segments only (empty if none)",
               "Next date": "booked call date if a future calendar event of Call type exists, else empty" if m.get("call_check") else "empty",
               "Chase step": "empty", "moved_sections": m.get("move", [])}
        plan.append({"engagement": pid, "name": name, "status": p.get("Status"), "before": {
            "Next action": S, "Next date": p.get("date:Next date:start"), "Waiting on": p.get("Waiting on"),
            "Chase step": p.get("Chase step"), "Call type": p.get("Call type")},
            "task_rows": rows, "engagement_after": eng, "conservation_ok": ok,
            "segments": {"total": len(S), "moved": len(used), "kept": len(keep)}})
        ok_all &= ok
        print(f"{name[:40]:40} segs {len(S)} moved {len(used)} kept {len(keep)} rows {len(rows)} {'OK' if ok else 'STOP'}")
    json.dump(plan, open(out_path, "w"), indent=1, ensure_ascii=False)
    print("rows", len(plan), "task rows", sum(len(x["task_rows"]) for x in plan), "all conserved" if ok_all else "MISMATCH")
    return 0 if ok_all else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
