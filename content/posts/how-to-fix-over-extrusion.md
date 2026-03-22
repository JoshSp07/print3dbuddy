# How to Fix Over-Extrusion in 3D Printing

Over-extrusion is the opposite of under-extrusion, but it causes just as many problems. Too much plastic, bulging walls, blobs on the surface, and prints that come out slightly larger than they should be. It is less dramatic than a spaghetti failure, but it quietly ruins print quality and makes functional parts fit badly.

Here is every cause and how to fix each one.

---

## What Does Over-Extrusion Look Like?

- Walls that bow outwards slightly
- Blobs or zits on the outer surface
- Corners that are slightly rounded or filled in
- First layer that squishes out and spreads wider than expected (this specific issue is called elephant foot - more on that below)
- Dimensional inaccuracy - holes too small, parts that do not fit together correctly
- Excess filament building up on top surfaces

---

## Fix 1: Calibrate Your Flow Rate (Extrusion Multiplier)

The most common cause of over-extrusion is a flow rate that is set too high. Your slicer has a setting called flow rate, extrusion multiplier, or extrusion factor - they all mean the same thing. The default is usually 100% (or 1.0), but every printer and filament combination is slightly different.

**How to calibrate it:** Print a single-wall cube (no top, no bottom, just walls) and measure the wall thickness with digital calipers. It should match your slicer's line width setting (usually 0.4-0.45mm for a 0.4mm nozzle). If the walls are thicker than expected, reduce the flow rate by 2-3% at a time and reprint until they match.

Our [filament cost calculator](https://tools.print3dbuddy.com/tools/filament-cost) can help you understand how flow rate changes affect material use - but for calibration, the [flow rate test print](https://tools.print3dbuddy.com/test-prints) is the most direct tool.

---

## Fix 2: Check Your E-Steps (Extruder Steps Per Millimetre)

E-steps tell your printer how many motor steps equal 1mm of filament movement. If this is set too high, your printer physically pushes more filament than it thinks it is.

**How to check:** Mark 100mm and 120mm on a piece of filament above the extruder. Tell the printer to extrude exactly 100mm through the terminal or printer menu. Measure how much filament actually moved. If it moved more than 100mm, your E-steps are too high.

New E-steps = (current E-steps x 100) / actual mm extruded

E-steps are saved in your printer's EEPROM and will persist across prints once updated. You only need to calibrate them once per machine - they should not drift unless you change your extruder hardware.

---

## Fix 3: Lower Your Print Temperature

The hotter the filament, the more it flows and the harder it is to control. Printing even 5-10C hotter than needed can cause slight over-extrusion, blobs, and stringing.

**Recommended starting temperatures:**
- PLA: 200-215C
- PETG: 220-235C
- ABS/ASA: 235-250C

Try dropping your temperature in 5C steps. Use the [print settings cheat sheet](https://tools.print3dbuddy.com/tools/print-settings) for recommended starting points for your specific filament.

If reducing temperature causes under-extrusion or layer adhesion issues, your temperature was correct and the problem lies elsewhere.

---

## Fix 4: Elephant Foot (First Layer Only)

Elephant foot is a specific type of over-extrusion that only affects the first layer. The bottom of the print is wider than the rest, creating a flared edge that makes the part look like it has feet.

It is caused by the first layer being printed too close to the bed and being squashed flat, or by the first layer flow rate being set too high.

**Fix:**
- Increase your Z offset slightly (raise the nozzle a fraction away from the bed)
- Reduce your first layer flow rate to 90-95% in your slicer
- Some slicers have a specific elephant foot compensation setting - use it if available

---

## Fix 5: Check for a Partial Nozzle Blockage

This sounds like the opposite of over-extrusion, but a partial blockage can cause irregular flow that sometimes looks like over-extrusion in patches. Burned filament creates a narrowing inside the nozzle, and pressure builds up until it forces a surge of plastic out.

**Signs this is the cause:** Over-extrusion that appears randomly rather than consistently, combined with some under-extruded patches in the same print.

**Fix:** Do a cold pull - heat the nozzle to printing temperature, push filament through manually, then cool to around 90C and pull the filament out sharply. Repeat until the pulled filament tip comes out clean with no brown or black residue. See the [complete nozzle guide](/posts/complete-nozzle-guide-3d-printing/) for full cold pull instructions.

---

## Quick Checklist

1. Print a single-wall test cube and measure wall thickness - adjust flow rate to match target
2. Calibrate E-steps if you have never done so
3. Check print temperature - try 5-10C lower
4. If only the first layer is affected, adjust Z offset and first layer flow rate
5. Do a cold pull if over-extrusion appears inconsistent or patchy

---

## Related Guides

- [How to Fix Under-Extrusion](/posts/how-to-fix-under-extrusion/) - the opposite problem, equally common
- [Complete Nozzle Guide](/posts/complete-nozzle-guide-3d-printing/) - cold pull instructions and nozzle maintenance
- [How to Calibrate Your First 3D Printer](/posts/how-to-calibrate-your-first-3d-printer/) - full calibration walkthrough including E-steps and flow rate
- [Nozzle Size Recommender](https://tools.print3dbuddy.com/tools/nozzle-recommender) - check if you are using the right nozzle for your material
