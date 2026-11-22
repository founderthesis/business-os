#!/usr/bin/env python3
"""Rulebook r1 build: pinned prompt bytes + edits.py -> prompts/ + manifest.json.

Re-runnable. Reads the pinned sources with git show, never the working tree.
Every edit's old text must occur exactly once, or the build fails.
Usage: python3 docs/proposals/rulebook-r1/build.py [--check]
  --check  build in memory and compare with prompts/ (exit 1 on drift)
"""
import hashlib, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import edits  # noqa: E402

SOURCES = {
    # output file: (pinned commit, repo path)
    "calendar.txt": ("83e8fb0", "docs/proposals/zoya-day/prompts/calendar.txt"),
    "inbox-actions.txt": ("83e8fb0", "docs/proposals/zoya-day/prompts/inbox-actions.txt"),
    "inbox-capture.txt": ("83e8fb0", "docs/proposals/zoya-day/prompts/inbox-capture.txt"),
    "whatsapp.txt": ("83e8fb0", "docs/proposals/zoya-day/prompts/whatsapp.txt"),
    "zoya-fast.txt": ("83e8fb0", "docs/proposals/zoya-day/prompts/zoya-fast.txt"),
    "zoya-slow.txt": ("83e8fb0", "docs/proposals/zoya-day/prompts/zoya-slow.txt"),
    "zoya-slow-work.txt": ("63d63ec", "routines/zoya/release/zoya-slow-work.txt"),
}
# daily-sweep.txt is retired (decision 657): not rebuilt. Its live obligations are
# accounted for in change-map.md (S6).


def pinned(commit, path):
    return subprocess.run(["git", "show", f"{commit}:{path}"], check=True,
                          capture_output=True, cwd=HERE).stdout.decode("utf-8")


def build():
    out, report = {}, []
    for name, (commit, path) in SOURCES.items():
        text = pinned(commit, path)
        before = len(text.encode())
        for subj, old, new in edits.EDITS.get(name, []):
            if old is None:
                continue
            n = text.count(old)
            if n != 1:
                raise SystemExit(f"{name}: {subj}: old text found {n} times: {old[:90]!r}")
            text = text.replace(old, new)
        for subj, prefix in edits.REMOVE_LINES.get(name, []):
            lines = text.split("\n")
            hits = [i for i, l in enumerate(lines) if l.startswith(prefix)]
            if len(hits) != 1:
                raise SystemExit(f"{name}: {subj}: line prefix found {len(hits)} times: {prefix!r}")
            del lines[hits[0]]
            text = "\n".join(lines)
        if "—" in text and "—" not in pinned(commit, path):
            raise SystemExit(f"{name}: an edit added an em dash")
        out[name] = text
        report.append({
            "file": name, "source": f"{commit}:{path}",
            "source_sha256": hashlib.sha256(pinned(commit, path).encode()).hexdigest(),
            "bytes_before": before, "bytes_after": len(text.encode()),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "edits": sum(1 for e in edits.EDITS.get(name, []) if e[1] is not None)
                     + len(edits.REMOVE_LINES.get(name, [])),
        })
    # upkeep.txt from the retired sweep (change-map S6).
    sweep = pinned("83e8fb0", "docs/proposals/zoya-day/prompts/daily-sweep.txt").split("\n")
    keep = sorted(set(edits.UPKEEP_LINES))
    up = edits.UPKEEP_INTRO + "\n\n" + "\n".join(sweep[i - 1] for i in keep)
    for subj, old, new in edits.UPKEEP_EDITS:
        n = up.count(old)
        if n != 1:
            raise SystemExit(f"upkeep.txt: {subj}: old text found {n} times: {old[:90]!r}")
        up = up.replace(old, new)
    out["upkeep.txt"] = up
    report.append({"file": "upkeep.txt", "source": "83e8fb0:docs/proposals/zoya-day/prompts/daily-sweep.txt (lines kept: %d)" % len(keep),
                   "source_sha256": hashlib.sha256("\n".join(sweep).encode()).hexdigest(),
                   "bytes_before": 0, "bytes_after": len(up.encode()),
                   "sha256": hashlib.sha256(up.encode()).hexdigest(), "edits": len(edits.UPKEEP_EDITS)})

    # Stamp the SLOW prompt with its work file's release (release.json, written at cutover
    # after the work file is committed). Without it the placeholders stay and --release fails.
    work = out["zoya-slow-work.txt"]
    rel = {}
    rp = os.path.join(HERE, "release.json")
    if os.path.exists(rp):
        rel = json.load(open(rp))
    stamps = {"{SLOW_WORK_SHA16}": hashlib.sha256(work.encode()).hexdigest()[:16],
              "{SLOW_WORK_CHARS}": f"{len(work):,}"}
    if rel.get("slow_work_commit"):
        stamps["{SLOW_WORK_COMMIT}"] = rel["slow_work_commit"]
    for k, v in stamps.items():
        out["zoya-slow.txt"] = out["zoya-slow.txt"].replace(k, v)
    for r in report:
        if r["file"] == "zoya-slow.txt":
            r["bytes_after"] = len(out["zoya-slow.txt"].encode())
            r["sha256"] = hashlib.sha256(out["zoya-slow.txt"].encode()).hexdigest()
    if "--release" in sys.argv and "{SLOW_WORK_COMMIT}" in out["zoya-slow.txt"]:
        raise SystemExit("release.json has no slow_work_commit: commit the work file first, then stamp")
    return out, report


def main():
    out, report = build()
    pdir = os.path.join(HERE, "prompts")
    if "--check" in sys.argv:
        drift = [n for n, t in out.items()
                 if not os.path.exists(os.path.join(pdir, n))
                 or open(os.path.join(pdir, n), encoding="utf-8").read() != t]
        print("drift:" if drift else "no drift", *drift)
        sys.exit(1 if drift else 0)
    os.makedirs(pdir, exist_ok=True)
    for n, t in out.items():
        with open(os.path.join(pdir, n), "w", encoding="utf-8") as f:
            f.write(t)
    with open(os.path.join(HERE, "manifest.json"), "w") as f:
        json.dump(report, f, indent=1)
        f.write("\n")
    for r in report:
        print(f"{r['file']:22} {r['bytes_before']:>7} -> {r['bytes_after']:>7}  edits {r['edits']:>2}  {r['sha256'][:16]}")


if __name__ == "__main__":
    main()
