# How to Calibrate Flow Rate (Extrusion Multiplier) on Any 3D Printer

Flow rate - also called extrusion multiplier - is one of those settings most beginners never touch, and it quietly ruins their prints the whole time. If your top surfaces look rough or gappy, if your prints feel slightly weak, or if dimensions are consistently off, flow rate is almost certainly the culprit.

The good news: it is one of the easiest calibrations to run, and you only need to do it once per filament brand.

---

## What Is Flow Rate?

Flow rate (or extrusion multiplier) is a percentage that scales how much filament your printer pushes out. At 100%, the printer extrudes exactly what the slicer calculated. At 95%, it extrudes 5% less. At 105%, 5% more.

The default is always 100% - but filament varies. Different brands, different colours, and even different spools of the same brand can have slight diameter inconsistencies or melt at slightly different rates. A flow rate that is even 5% off shows up as noticeable print quality problems.

---

## Signs Your Flow Rate Needs Adjusting

**Too low (under-extrusion):**
- Gaps between top surface lines
- Rough or porous top layers
- Perimeters that don't quite touch
- Parts feel lighter than expected

**Too high (over-extrusion):**
- Raised ridges on top surfaces
- Blobbing or bulging at corners
- Seam looks pronounced and raised
- Dimensions are slightly larger than designed

---

## How to Calibrate It

There are two methods. Use whichever you have tools for.

### Method 1: Visual Tile Test (Easiest)

This is what the [Flow Rate Test print at tools.print3dbuddy.com](https://tools.print3dbuddy.com/test-prints) is for.

1. Download the STL and import it into your slicer.
2. Split it into 5 individual objects (most slicers have a "split to parts" button).
3. Set each tile's flow rate to its label: 90%, 95%, 100%, 105%, 110%.
4. Print all 5 at once at your normal temperature and speed.
5. Compare the top surfaces. The smoothest one - no gaps, no ridges - is your correct setting.

Dial in to the nearest 1% if you want precision from there. Most filaments land between 95% and 100%.

### Method 2: Measure Single Wall Thickness (More Precise)

This method uses calipers and gives you an exact number.

1. Create or download a simple hollow single-wall cube (20x20x20mm, wall thickness equal to your nozzle diameter - usually 0.4mm).
2. Slice it with a single perimeter/wall only, no infill, no top or bottom layers.
3. Print it.
4. Measure the wall thickness with calipers at multiple points.
5. Calculate: **new flow rate = (expected wall / actual wall) x current flow rate**

Example: if your nozzle is 0.4mm and your walls measure 0.43mm, your flow is running high.

New flow = (0.4 / 0.43) x 1.00 = 0.93 - set flow to 93%.

---

## Where to Set Flow Rate in Your Slicer

- **OrcaSlicer / BambuStudio:** Filament settings > Flow ratio
- **PrusaSlicer:** Filament settings > Extrusion multiplier
- **Cura:** Material > Flow (under the material settings, not print settings)

Save it as part of your filament profile so it carries over to every print.

---

## How Often Do You Need to Do This?

Once per filament brand and colour. Different colours from the same brand can have slightly different pigment loadings that affect flow, so it is worth a quick check when switching to a new colour.

You don't need to redo it every print - once it's dialled in and saved in your slicer profile, it just works.

---

## Flow Rate vs E-Steps: What's the Difference?

E-steps (or rotation distance in Klipper) is a hardware calibration that tells the printer how many motor steps equal 1mm of filament movement. Flow rate is a software scaling factor on top of that.

The right order: calibrate e-steps first, then set flow rate per filament. If you skip e-steps and only use flow rate to compensate, you're masking a mechanical problem.

**E-steps:** calibrate once per printer (or after changing extruder hardware)
**Flow rate:** calibrate once per filament profile

---

## Quick Reference

| Flow setting | Typical result |
|---|---|
| 90% | Gappy tops, weak parts |
| 95% | Slightly under - fine for some filaments |
| 100% | Default starting point |
| 105% | Slightly over - watch for ridges |
| 110% | Over-extruding - blobs and raised seams |

Most PLA lands at 95-100%. PETG is often 97-100%. TPU may need tweaking depending on hardness.

---

## Try It Yourself

The [Flow Rate Test at tools.print3dbuddy.com](https://tools.print3dbuddy.com/test-prints) gives you all 5 tiles in one STL, ready to slice. Takes about 20 minutes to print and tells you exactly where your extrusion multiplier should be. Our free [Print Settings Calculator](https://tools.print3dbuddy.com) also gives you recommended starting settings for 14 common filaments.
