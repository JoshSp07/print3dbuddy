# 3D Printing First Layer Problems: Every Issue and How to Fix It

The first layer is the foundation of every print. Get it right and everything else has a chance of working. Get it wrong and nothing you do later will fix it.

Most first layer problems come down to three things: a dirty bed, a wrong Z offset, or an unlevel bed. In that order of how often they are the actual cause. Start with the simplest thing first.

---

## Before Anything Else: Clean the Bed

Skin oils from handling the print surface reduce adhesion dramatically. A bed that looks clean is not necessarily clean. I clean my bed with isopropyl alcohol (70% or higher) before every single print without exception - it takes ten seconds and it solves more "filament not sticking" problems than any other single thing.

If you are troubleshooting a first layer problem and you have not cleaned the bed with IPA first, do that now before reading any further.

---

## Problem 1: Filament Not Sticking to the Bed

**Check bed cleanliness first.** If that is fine, work through these:

**Z offset too high** - the nozzle is too far from the bed. Filament gets pushed around instead of squishing down and bonding. Lower your Z offset in 0.05mm increments. You want the first layer lines to look slightly flattened, not round.

**Bed temperature too low** - check these temperatures and make sure your bed has soaked for a couple of minutes after reaching temp before you start printing:

| Material | Bed Temperature |
|---|---|
| PLA | 55 - 65°C |
| PETG | 70 - 85°C |
| ABS / ASA | 100 - 110°C |
| TPU | 30 - 60°C |

**Wrong bed surface** - glass beds work well for PLA but are poor for PETG (it bonds too aggressively and rips chunks out) and inconsistent for ABS. A textured PEI spring steel sheet works reliably for almost every material and is one of the best low-cost upgrades you can make.

**First layer speed too fast** - anything above 30mm/s for the first layer is pushing it. Set your slicer to 20-25mm/s for the first layer specifically.

---

## Problem 2: Filament Dragging Instead of Laying Flat

The nozzle is too close. The filament has nowhere to go and gets pushed ahead of the nozzle, dragging through the print.

Increase Z offset in 0.05mm increments. You want slight squish - lines slightly flattened and slightly wider than round, adjacent lines fusing together at the edges. Not scraped flat, not sitting round and separate.

---

## Problem 3: Uneven First Layer Across the Bed

One corner sticking well, another with gaps, another being scraped. This is almost always the bed level.

**If you have auto bed levelling** - re-run the mesh levelling routine. Make sure your Z offset is set correctly after re-levelling. Auto levelling corrects for surface variation but does not set Z offset - you still need to dial that in separately.

**If you have manual levelling** - level at printing temperature. The bed expands when hot and the readings will be different to cold. Use a sheet of paper and adjust each corner until you get consistent light drag across all four corners and the centre. Run through the process twice - adjusting one corner affects the others slightly.

---

## Problem 4: Lines Not Fusing Together (Gaps Between Lines)

The lines are placed but not bonding side to side.

**Z offset too high** is the most common cause - the nozzle is not close enough for lines to squish together. Lower it slightly.

**Under-extrusion** - not enough material coming out. Check your extrusion multiplier and nozzle temperature.

**Line width set too narrow in slicer** - first layer line width should be 100-150% of your nozzle diameter. On a 0.4mm nozzle, 0.4-0.6mm is the range. Check this in your slicer.

---

## Problem 5: Lines Squished Together, Rough Surface

The opposite - everything is merging into a rough uneven mass.

Z offset is too low. Increase in 0.05mm increments until lines are separate but still slightly flattened and touching at the edges.

---

## Problem 6: Corners Lifting During the First Layer

The first layer starts fine but corners peel up during or shortly after printing.

- Increase bed temperature
- Add a brim (5-10mm) in your slicer - this dramatically increases the surface area bonded to the bed
- Make sure the bed is fully up to temperature before printing, not just hitting temperature at the start
- For ABS and ASA specifically: you need an enclosure. There is no reliable fix for ABS warping without one.

---

## Problem 7: Blob at the Start of the Print

A large blob or blob trail where the nozzle starts moving. The nozzle has been sitting hot and oozing before the print starts.

Most slicers include a purge line in the start G-code by default - check that it is not disabled. Adding a skirt (a printed outline before the actual model starts) also purges the nozzle cleanly.

If this is a persistent problem, check your standby temperature. Keeping the nozzle at full printing temperature while waiting is harder on the filament than a slightly lower standby.

---

## Problem 8: Scar or Groove Across the First Layer

A line or groove running through the first layer.

The nozzle is dragging through already-deposited material on a travel move. Z offset is slightly too low. Raise it by 0.05mm. Also check if Z-hop is enabled in your slicer - this lifts the nozzle during travel moves and prevents this entirely.

---

## Problem 9: Perfect First Layer But Print Still Fails Later

If the first layer is fine and the print is failing higher up:

- **Warping and lifting** - see the [warping guide](/posts/how-to-fix-3d-print-warping/)
- **Layer adhesion failure** - temperature or cooling issue, see the [layer adhesion guide](/posts/3d-printing-layer-adhesion-problems-fixes/)
- **Tall print falling over** - print speed too fast for the geometry, or centre of gravity problem

---

## What a Correct First Layer Looks Like

- Lines slightly flattened (not round, not scraped flat)
- Adjacent lines touching and slightly fusing at the edges
- No gaps between lines
- No scraping, rough patches, or drag marks
- Corners flat and bonded

The [first layer calibration test print](https://tools.print3dbuddy.com/test-prints#first-layer-test) at tools.print3dbuddy.com is a 60x60mm grid square that makes Z offset easy to read. Print it, adjust Z offset until it looks right, and note the value.

---

## The Fix Order

1. Clean the bed with IPA
2. Check Z offset - lower it if filament is not bonding
3. Check bed temperature for your material
4. Re-run bed levelling if the problem varies across the bed

This sequence resolves the vast majority of first layer problems without changing anything else.
