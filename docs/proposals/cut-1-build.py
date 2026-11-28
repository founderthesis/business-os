"""Cut 1 (CTO week plan, roadmap items 2 and 5; decisions 352, 354, 355, 359, 360). Composes the five parts on the live
bases. The sweep base is the due-versus-done build (due-vs-done-build.py) on the live sweep, so both compose.
Usage: python3 cut-1-build.py <dir with trig_<id>.txt live bases> <out dir>
Every output must be smaller than its live base."""
import hashlib, importlib.util, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
def sha(s): return hashlib.sha256(s.encode()).hexdigest()[:16]
def part(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, f"cut-1-{name}.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

BASES = {  # routine: (trigger id, live bytes, live sha16)
    "inbox": ("trig_0189eZvAD8x4357cfevgZ3No", 65324, "d09f63ec081186de"),
    "zoya": ("trig_01UPT8LDrBDL5JQqW91Awgbo", 49048, "487ebbf6feef8db7"),
    "calendar": ("trig_01Voiz5YsK2SnVf2STF8PoSH", 56059, "5576c67e1181d79e"),
    "sweep": ("trig_01MdfUFg2qrebDWgiHwncgnd", 35943, "b0888b6624e6848f"),
    "whatsapp": ("trig_01MnmJYorWrd61K7b5BCqXr1", 21846, "80c9f92041f3b548"),
}
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for name, (tid, n, h) in BASES.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s)) == (n, h), (name, len(s.encode()), sha(s))
    if name == "sweep":
        tmp = os.path.join(out, "sweep-dvd.txt")
        subprocess.run([sys.executable, os.path.join(HERE, "due-vs-done-build.py"), os.path.join(src, f"{tid}.txt"), tmp], check=True, capture_output=True)
        s = open(tmp, encoding="utf-8").read(); os.remove(tmp)
    if name == "calendar":  # the orphan fix (93b24de + guard) deploys with Cut 1
        tmp = os.path.join(out, "cal-orph.txt")
        subprocess.run([sys.executable, os.path.join(HERE, "calendar-orphan-fix.py"), os.path.join(src, f"{tid}.txt"), tmp], check=True, capture_output=True)
        s = open(tmp, encoding="utf-8").read(); os.remove(tmp)
    o = part(name).edit(s)
    if name in ("inbox", "calendar", "zoya"):
        o = part("outside").edit(name, o)
    assert len(o.encode()) < n, (name, len(o.encode()), n)
    assert "—" not in o.replace("Independent review — latest checkpoint", ""), name
    open(os.path.join(out, f"{tid}.txt"), "w", encoding="utf-8").write(o)
    print(f"{name:9s} {n:6d} -> {len(o.encode()):6d}  {sha(o)}")
