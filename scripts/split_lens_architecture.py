#!/usr/bin/env python3
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CANON = ROOT / "docs/architecture/v2025-08/LENS_Architecture_v2025-08-15.md"
OUTDIR = CANON.parent

SECTIONS = [
    ("01-opening-cinematic.md", r"^## Opening Cinematic:"),
    ("02-lens-equation.md", r"^## The LENS Equation:"),
    ("03-core-gameplay-loop.md", r"^## Core Gameplay Loop:"),
    ("04-mechanics-and-systems.md", r"^## Mechanics & Systems:"),
    ("05-meta-narrative-and-lore.md", r"^## Meta-Narrative & Lore:"),
    ("06-real-world-impact-bridge.md", r"^## Real-World Impact Bridge:"),
    ("07-technology-and-infrastructure.md", r"^## Technology & Infrastructure:"),
    ("08-growth-and-adoption.md", r"^## Growth & Adoption"),
    ("09-impact-and-market.md", r"^## Impact & Market"),
    ("10-call-to-adventure.md", r"^## Call to Adventure:"),
    ("11-technical-implementation-roadmap.md", r"^### Technical Implementation Roadmap"),
]

def main():
    text = CANON.read_text(encoding="utf-8").splitlines()
    def find(pat):
        rx = re.compile(pat)
        for i,l in enumerate(text):
            if rx.match(l.strip()):
                return i
        return None
    anchors=[]
    for fname, pat in SECTIONS:
        s = find(pat)
        anchors.append((fname, s))
    for j,(fname, start) in enumerate(anchors):
        if start is None: 
            print(f"[WARN] missing: {fname}")
            continue
        nexts = [s for _,s in anchors[j+1:] if s is not None]
        end = min(nexts) if nexts else len(text)
        body = "\n".join(text[start:end]).rstrip()+"\n"
        (OUTDIR/fname).write_text(body, encoding="utf-8")
        print("Wrote", OUTDIR/fname)
if __name__=="__main__":
    main()
