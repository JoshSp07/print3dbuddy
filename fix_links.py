"""
Replace [AMAZON_LINK] and [BAMBU_LINK] placeholders in markdown posts
with real product URLs based on surrounding context.
"""

import re
from pathlib import Path

POSTS_DIR = Path("content/posts")

# Each entry: (file, line_fragment_to_match, old_text, new_text)
REPLACEMENTS = [

    # ── pla-vs-petg-vs-abs ───────────────────────────────────────────────────
    ("pla-vs-petg-vs-abs-which-filament-for-beginners.md",
     "Bambu Lab PLA Basic",
     "Bambu Lab PLA Basic ([BAMBU_LINK])",
     "Bambu Lab PLA Basic (https://bambulab.com/en/filament/pla-basic)"),

    ("pla-vs-petg-vs-abs-which-filament-for-beginners.md",
     "Hatchbox PLA ([AMAZON_LINK]) — reliable",
     "Hatchbox PLA ([AMAZON_LINK]) — reliable",
     "Hatchbox PLA (https://www.amazon.com/s?k=Hatchbox+PLA+1.75mm) — reliable"),

    ("pla-vs-petg-vs-abs-which-filament-for-beginners.md",
     "eSUN PLA+ ([AMAZON_LINK]) — slightly",
     "eSUN PLA+ ([AMAZON_LINK]) — slightly",
     "eSUN PLA+ (https://www.amazon.com/s?k=eSUN+PLA+Plus+1.75mm) — slightly"),

    ("pla-vs-petg-vs-abs-which-filament-for-beginners.md",
     "Bambu Lab PETG HF",
     "Bambu Lab PETG HF ([BAMBU_LINK])",
     "Bambu Lab PETG HF (https://bambulab.com/en/filament/petg-hf)"),

    ("pla-vs-petg-vs-abs-which-filament-for-beginners.md",
     "Polymaker PolyLite PETG",
     "Polymaker PolyLite PETG ([AMAZON_LINK])",
     "Polymaker PolyLite PETG (https://www.amazon.com/s?k=Polymaker+PolyLite+PETG)"),

    ("pla-vs-petg-vs-abs-which-filament-for-beginners.md",
     "Overture PETG",
     "Overture PETG ([AMAZON_LINK])",
     "Overture PETG (https://www.amazon.com/s?k=Overture+PETG+filament)"),

    ("pla-vs-petg-vs-abs-which-filament-for-beginners.md",
     "eSUN ABS+",
     "eSUN ABS+ ([AMAZON_LINK])",
     "eSUN ABS+ (https://www.amazon.com/s?k=eSUN+ABS+Plus+filament)"),

    ("pla-vs-petg-vs-abs-which-filament-for-beginners.md",
     "Bambu Lab ABS",
     "Bambu Lab ABS ([BAMBU_LINK])",
     "Bambu Lab ABS (https://bambulab.com/en/filament/abs)"),

    ("pla-vs-petg-vs-abs-which-filament-for-beginners.md",
     "Bambu Lab A1 Mini",
     "**Bambu Lab A1 Mini** ([BAMBU_LINK])",
     "**Bambu Lab A1 Mini** (https://bambulab.com/en/bambu-lab/a1-mini)"),

    ("pla-vs-petg-vs-abs-which-filament-for-beginners.md",
     "Creality Ender 3 V3 SE",
     "**Creality Ender 3 V3 SE** ([AMAZON_LINK])",
     "**Creality Ender 3 V3 SE** (https://www.amazon.com/s?k=Creality+Ender+3+V3+SE)"),

    ("pla-vs-petg-vs-abs-which-filament-for-beginners.md",
     "Hatchbox PLA ([AMAZON_LINK]) or",
     "Hatchbox PLA ([AMAZON_LINK]) or",
     "Hatchbox PLA (https://www.amazon.com/s?k=Hatchbox+PLA+1.75mm) or"),

    ("pla-vs-petg-vs-abs-which-filament-for-beginners.md",
     "eSUN PLA+ ([AMAZON_LINK]) and get",
     "eSUN PLA+ ([AMAZON_LINK]) and get",
     "eSUN PLA+ (https://www.amazon.com/s?k=eSUN+PLA+Plus+1.75mm) and get"),

    # ── best-filament-for-outdoor-use ────────────────────────────────────────
    ("best-filament-for-outdoor-use.md",
     "Polymaker PolyLite ASA",
     "Polymaker PolyLite ASA ([AMAZON_LINK])",
     "Polymaker PolyLite ASA (https://www.amazon.com/s?k=Polymaker+PolyLite+ASA)"),

    ("best-filament-for-outdoor-use.md",
     "Bambu Lab ASA",
     "Bambu Lab ASA ([BAMBU_LINK])",
     "Bambu Lab ASA (https://bambulab.com/en/filament/asa)"),

    ("best-filament-for-outdoor-use.md",
     "eSUN ASA",
     "eSUN ASA ([AMAZON_LINK])",
     "eSUN ASA (https://www.amazon.com/s?k=eSUN+ASA+filament)"),

    ("best-filament-for-outdoor-use.md",
     "Polymaker PolyLite PETG ([AMAZON_LINK])",
     "Polymaker PolyLite PETG ([AMAZON_LINK])",
     "Polymaker PolyLite PETG (https://www.amazon.com/s?k=Polymaker+PolyLite+PETG)"),

    ("best-filament-for-outdoor-use.md",
     "Bambu Lab PETG HF",
     "Bambu Lab PETG HF ([BAMBU_LINK])",
     "Bambu Lab PETG HF (https://bambulab.com/en/filament/petg-hf)"),

    ("best-filament-for-outdoor-use.md",
     "Overture PETG ([AMAZON_LINK])",
     "Overture PETG ([AMAZON_LINK])",
     "Overture PETG (https://www.amazon.com/s?k=Overture+PETG+filament)"),

    ("best-filament-for-outdoor-use.md",
     "Bambu Lab PA6-CF",
     "Bambu Lab PA6-CF ([BAMBU_LINK])",
     "Bambu Lab PA6-CF (https://bambulab.com/en/filament/pa6-cf)"),

    ("best-filament-for-outdoor-use.md",
     "hardened nozzles on Amazon",
     "hardened nozzles on Amazon ([AMAZON_LINK])",
     "hardened nozzles on Amazon (https://www.amazon.com/s?k=hardened+steel+nozzle+3d+printer)"),

    ("best-filament-for-outdoor-use.md",
     "UV-blocking clear coats",
     "UV-blocking clear coats ([AMAZON_LINK])",
     "UV-blocking clear coats (https://www.amazon.com/s?k=UV+resistant+clear+coat+spray)"),

    ("best-filament-for-outdoor-use.md",
     "Bambu Lab P1S",
     "**Bambu Lab P1S** ([BAMBU_LINK])",
     "**Bambu Lab P1S** (https://bambulab.com/en/bambu-lab/p1s)"),

    ("best-filament-for-outdoor-use.md",
     "Buy Polymaker PolyLite ASA",
     "**Buy Polymaker PolyLite ASA** ([AMAZON_LINK])",
     "**Buy Polymaker PolyLite ASA** (https://www.amazon.com/s?k=Polymaker+PolyLite+ASA)"),

    ("best-filament-for-outdoor-use.md",
     "Use PETG** ([AMAZON_LINK])",
     "**Use PETG** ([AMAZON_LINK])",
     "**Use PETG** (https://www.amazon.com/s?k=Polymaker+PolyLite+PETG)"),

    # ── how-to-fix-3d-printer-stringing ──────────────────────────────────────
    ("how-to-fix-3d-printer-stringing.md",
     "food dehydrator",
     "food dehydrator ([AMAZON_LINK])",
     "food dehydrator (https://www.amazon.com/s?k=food+dehydrator+filament+drying)"),

    ("how-to-fix-3d-printer-stringing.md",
     "filament dryer box",
     "filament dryer box ([AMAZON_LINK])",
     "filament dryer box (https://www.amazon.com/s?k=filament+dryer+box+3d+printing)"),

    ("how-to-fix-3d-printer-stringing.md",
     "grab a pack",
     "grab a pack ([AMAZON_LINK])",
     "grab a pack (https://www.amazon.com/s?k=replacement+brass+nozzle+0.4mm+3d+printer)"),

    ("how-to-fix-3d-printer-stringing.md",
     "Bambu Lab A1 Mini** ([BAMBU_LINK]) and **Bambu Lab P1S",
     "**Bambu Lab A1 Mini** ([BAMBU_LINK]) and **Bambu Lab P1S** ([BAMBU_LINK])",
     "**Bambu Lab A1 Mini** (https://bambulab.com/en/bambu-lab/a1-mini) and **Bambu Lab P1S** (https://bambulab.com/en/bambu-lab/p1s)"),

    ("how-to-fix-3d-printer-stringing.md",
     "Creality Ender 3 V3",
     "**Creality Ender 3 V3** ([AMAZON_LINK])",
     "**Creality Ender 3 V3** (https://www.amazon.com/s?k=Creality+Ender+3+V3)"),

    ("how-to-fix-3d-printer-stringing.md",
     "quality filament dryer",
     "quality filament dryer ([AMAZON_LINK])",
     "quality filament dryer (https://www.amazon.com/s?k=filament+dryer+box+3d+printing)"),

    # ── how-to-calibrate-your-first-3d-printer ───────────────────────────────
    ("how-to-calibrate-your-first-3d-printer.md",
     "Bambu Lab A1 Mini** ([BAMBU_LINK]) and **P1S",
     "**Bambu Lab A1 Mini** ([BAMBU_LINK]) and **P1S** ([BAMBU_LINK])",
     "**Bambu Lab A1 Mini** (https://bambulab.com/en/bambu-lab/a1-mini) and **P1S** (https://bambulab.com/en/bambu-lab/p1s)"),

    ("how-to-calibrate-your-first-3d-printer.md",
     "Measure the wall thickness with digital calipers",
     "Measure the wall thickness with digital calipers ([AMAZON_LINK])",
     "Measure the wall thickness with digital calipers (https://www.amazon.com/s?k=digital+calipers+3d+printing)"),

    ("how-to-calibrate-your-first-3d-printer.md",
     "current price on Amazon ([AMAZON_LINK]).\n\nAdjust",
     "current price on Amazon ([AMAZON_LINK]).\n\nAdjust",
     "current price on Amazon (https://www.amazon.com/s?k=digital+calipers+3d+printing).\n\nAdjust"),

    ("how-to-calibrate-your-first-3d-printer.md",
     "**Digital calipers**",
     "**Digital calipers** — essential for measuring prints accurately ([AMAZON_LINK])",
     "**Digital calipers** — essential for measuring prints accurately (https://www.amazon.com/s?k=digital+calipers+3d+printing)"),

    ("how-to-calibrate-your-first-3d-printer.md",
     "**Filament dryer**",
     "**Filament dryer** — wet filament causes all kinds of calibration headaches ([AMAZON_LINK])",
     "**Filament dryer** — wet filament causes all kinds of calibration headaches (https://www.amazon.com/s?k=filament+dryer+box+3d+printing)"),

    ("how-to-calibrate-your-first-3d-printer.md",
     "**Bed adhesion spray or PEI sheet**",
     "**Bed adhesion spray or PEI sheet** — consistent bed adhesion makes calibration much easier ([AMAZON_LINK])",
     "**Bed adhesion spray or PEI sheet** — consistent bed adhesion makes calibration much easier (https://www.amazon.com/s?k=PEI+sheet+3d+printer)"),

    ("how-to-calibrate-your-first-3d-printer.md",
     "Bambu Lab A1 Mini** ([BAMBU_LINK]) automates",
     "**Bambu Lab A1 Mini** ([BAMBU_LINK]) automates",
     "**Bambu Lab A1 Mini** (https://bambulab.com/en/bambu-lab/a1-mini) automates"),

    ("how-to-calibrate-your-first-3d-printer.md",
     "Creality Ender 3 V3 SE** ([AMAZON_LINK]) is a classic",
     "**Creality Ender 3 V3 SE** ([AMAZON_LINK]) is a classic",
     "**Creality Ender 3 V3 SE** (https://www.amazon.com/s?k=Creality+Ender+3+V3+SE) is a classic"),

    ("how-to-calibrate-your-first-3d-printer.md",
     "current price on Amazon ([AMAZON_LINK]).",
     "current price on Amazon ([AMAZON_LINK]).",
     "current price on Amazon (https://www.amazon.com/s?k=Creality+Ender+3+V3+SE)."),

    # ── 10-useful-things ─────────────────────────────────────────────────────
    ("10-useful-things-to-3d-print-for-your-home.md",
     "608 bearings",
     "on Amazon ([AMAZON_LINK])",
     "on Amazon (https://www.amazon.com/s?k=608+bearings+pack)"),

    ("10-useful-things-to-3d-print-for-your-home.md",
     "Bambu Lab website ([BAMBU_LINK])",
     "**Bambu Lab A1 Mini** ([BAMBU_LINK]) is an outstanding beginner machine",
     "**Bambu Lab A1 Mini** (https://bambulab.com/en/bambu-lab/a1-mini) is an outstanding beginner machine"),

    ("10-useful-things-to-3d-print-for-your-home.md",
     "Bambu Lab website ([BAMBU_LINK]).",
     "Check the current price on the Bambu Lab website ([BAMBU_LINK]).",
     "Check the current price on the Bambu Lab website (https://bambulab.com/en/bambu-lab/a1-mini)."),

    ("10-useful-things-to-3d-print-for-your-home.md",
     "Creality Ender 3 V3 SE** ([AMAZON_LINK]) is one",
     "**Creality Ender 3 V3 SE** ([AMAZON_LINK]) is one",
     "**Creality Ender 3 V3 SE** (https://www.amazon.com/s?k=Creality+Ender+3+V3+SE) is one"),

    ("10-useful-things-to-3d-print-for-your-home.md",
     "current price on Amazon ([AMAZON_LINK]).\n\nAnd",
     "current price on Amazon ([AMAZON_LINK]).\n\nAnd",
     "current price on Amazon (https://www.amazon.com/s?k=Creality+Ender+3+V3+SE).\n\nAnd"),

    ("10-useful-things-to-3d-print-for-your-home.md",
     "Hatchbox ([AMAZON_LINK])",
     "Hatchbox ([AMAZON_LINK])",
     "Hatchbox (https://www.amazon.com/s?k=Hatchbox+PLA+1.75mm)"),

    ("10-useful-things-to-3d-print-for-your-home.md",
     "eSUN PLA+ ([AMAZON_LINK]) are",
     "eSUN PLA+ ([AMAZON_LINK]) are",
     "eSUN PLA+ (https://www.amazon.com/s?k=eSUN+PLA+Plus+1.75mm) are"),
]


def apply_replacements():
    counts = {}
    for fname, context_hint, old, new in REPLACEMENTS:
        fpath = POSTS_DIR / fname
        if not fpath.exists():
            print(f"  SKIP (not found): {fname}")
            continue
        text = fpath.read_text(encoding='utf-8')
        if old in text:
            text = text.replace(old, new, 1)
            fpath.write_text(text, encoding='utf-8')
            counts[fname] = counts.get(fname, 0) + 1
        else:
            print(f"  WARN: could not find in {fname}: {repr(old[:60])}")

    print("\nResults:")
    for fname, n in counts.items():
        print(f"  {fname}: {n} replacements")

    # Check for any remaining placeholders
    remaining = []
    for md in POSTS_DIR.glob("*.md"):
        text = md.read_text(encoding='utf-8')
        if '[AMAZON_LINK]' in text or '[BAMBU_LINK]' in text:
            remaining.append(md.name)
    if remaining:
        print(f"\n  Still has placeholders: {remaining}")
    else:
        print("\n  All placeholders replaced.")


if __name__ == '__main__':
    import os
    os.chdir(Path(__file__).parent)
    apply_replacements()
