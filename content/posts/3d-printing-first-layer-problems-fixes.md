# 3D Printing First Layer Problems: Every Issue and How to Fix It

The first layer is the foundation of every print. Get it right and everything else has a chance of working. Get it wrong and no amount of other tuning will save the print.

Here are every common first layer problem, what causes it, and exactly how to fix it.

---

## Problem 1: Filament Not Sticking to the Bed

The most common beginner problem. The filament comes out fine but just won't stay on the bed.

**Causes and fixes:**

**Dirty bed** - skin oils from handling the bed dramatically reduce adhesion. Clean with isopropyl alcohol (IPA 70%+) before every print. This fixes more "not sticking" problems than any other single thing.

**Z offset too high** - the nozzle is too far from the bed, so the filament just gets pushed around rather than squishing down and bonding. Reduce your Z offset (move the nozzle closer) in 0.05mm increments.

**Bed temperature too low** - check recommended bed temps: PLA 55-65°C, PETG 70-85°C, ABS 100-110°C. Make sure the bed has reached temperature and soaked for a few minutes before printing.

**Wrong bed surface for the material** - glass beds can be poor for PETG (sticks too well and rips chunks) and poor for ABS (doesn't stick well enough). A [textured PEI sheet](https://www.amazon.co.uk/s?k=textured+PEI+spring+steel+sheet&tag=print3dbuddy2-21) works for almost everything.

**First layer speed too fast** - slow your first layer to 20-25mm/s in your slicer settings.

---

## Problem 2: Filament Dragging Instead of Laying Flat

The nozzle is too close to the bed. The filament has nowhere to go and gets pushed ahead of the nozzle.

**Fix:** Increase your Z offset in 0.05mm increments. You want the filament slightly squished, not scraped.

Signs the Z offset is correct: lines are flat and slightly wider than round, adjacent lines fuse together slightly, no gaps between lines.

---

## Problem 3: First Layer Looks Uneven Across the Bed

One corner sticks well, another has gaps, another is scraped. Classic unlevelled bed.

**Fix:**

If you have **auto bed levelling** - re-run the bed mesh levelling routine from your printer menu. Make sure your Z offset is also set correctly after re-levelling.

If you have **manual levelling** - relevel the bed at printing temperature (the bed expands slightly when hot). Adjust each corner with a sheet of paper until you get consistent light drag across all four corners and the centre.

Run through manual levelling at least twice in a row - adjusting one corner affects the others slightly.

---

## Problem 4: First Layer Lines Have Gaps Between Them

The lines are being placed but they're not fusing together - you can see gaps between each pass.

**Causes:**

- **Z offset too high** - nozzle not close enough for lines to squish together
- **Under-extrusion** - not enough filament coming out
- **Line width set too narrow** in slicer - check your first layer line width (should be 100-150% of nozzle diameter)

**Fix:** Adjust Z offset slightly lower first. If that doesn't help, check your extrusion multiplier.

---

## Problem 5: First Layer Lines Are Squished Together and Rough

The opposite problem - lines are merging into a rough, uneven mass.

**Fix:** Z offset too low. Increase in 0.05mm increments until lines are separate but still slightly flattened and bonded.

---

## Problem 6: First Layer Looks Fine But Lifts at Corners (Warping)

The print starts well but corners begin lifting during or after the first layer.

**Causes:**
- Bed temperature too low
- Ambient temperature too cold
- No brim
- Material prone to warping (ABS, ASA)

**Fixes:**
- Increase bed temperature
- Add a brim (5-10mm wide) in your slicer
- Clean the bed with IPA
- For ABS/ASA: use an enclosure and turn off part cooling

---

## Problem 7: Blobbing at the Start of the First Layer

A large blob or blob trail at the start of the print, usually where the nozzle starts moving.

**Causes:**
- Ooze before print starts - nozzle has been sitting hot and leaking
- Start G-code not purging properly

**Fixes:**
- Add a purge line to your start G-code (most slicers include this by default)
- Use a skirt (a printed outline around the print that purges the nozzle before the actual print starts)
- Reduce ooze with slight retraction improvements or a lower standby temperature

---

## Problem 8: First Layer Has a "Scar" or Scrape Mark

A groove or scar running across the first layer.

**Cause:** The nozzle is dragging through already-deposited material on a travel move. Usually caused by Z offset being slightly too low, causing the nozzle to hit previous lines.

**Fix:** Slightly increase Z offset. Also check if Z-hop is enabled in your slicer (lifts the nozzle during travel moves).

---

## Problem 9: First Layer Looks Perfect But Print Still Fails Later

If the first layer looks great but the print still fails (detaches, warps, or falls over), the problem is elsewhere:

- **Warping:** bed temperature dropping, drafts, material sensitivity - see our [warping guide](/posts/how-to-fix-3d-print-warping/)
- **Tall prints falling over:** centre of gravity, print speed too fast for the geometry
- **Layer adhesion failure:** temperature or cooling issues - see our [layer adhesion guide](/posts/3d-printing-layer-adhesion-problems-fixes/)

---

## The Perfect First Layer: What to Look For

A correct first layer:
- Lines are slightly flattened (not round, not completely squished)
- Adjacent lines are touching and slightly fusing at edges
- No gaps between lines
- No scraping or rough patches
- Corners are flat and bonded
- Surface looks smooth and uniform from above

The best way to calibrate this is to use our [first layer calibration test print](https://tools.print3dbuddy.com/test-prints#first-layer-test)  -  a 60×60mm grid square that makes Z offset reading straightforward. Adjust Z offset until it looks right, then note the value and use it consistently.

---

## Tools That Help

- [Digital calipers](https://www.amazon.co.uk/s?k=digital+calipers+3d+printing&tag=print3dbuddy2-21) - measuring first layer thickness
- [Textured PEI sheet](https://www.amazon.co.uk/s?k=textured+PEI+spring+steel+sheet&tag=print3dbuddy2-21) - the best all-round bed surface for first layer adhesion
- [Isopropyl alcohol (IPA)](https://www.amazon.co.uk/s?k=isopropyl+alcohol+70+percent+cleaning&tag=print3dbuddy2-21) - clean the bed before every print

---

## Summary

First layer problems almost always come down to three things:
1. Z offset (nozzle height)
2. Bed levelness
3. Bed cleanliness

Start with cleaning the bed with IPA. Then check your Z offset. Then check bed level. In that order. This sequence resolves the vast majority of first layer issues without changing anything else.
