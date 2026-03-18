# 3D Printing Layer Adhesion Problems: Causes and Fixes

Layer adhesion is the bond between each horizontal slice of your print. When it's good, your parts are strong and consistent. When it's bad, layers split apart, parts snap along layer lines, and surfaces look rough and separated.

Here's why it happens and exactly how to fix it.

---

## Signs of Poor Layer Adhesion

- Parts split or delaminate when handled
- Visible gaps between layers on the surface
- Prints snap easily along horizontal lines
- Rough, grainy surface texture
- Layers visibly separating during printing

---

## Cause 1: Print Temperature Too Low

The most common cause. If your nozzle temperature is too low, the filament doesn't fully melt and bond to the previous layer.

**Fix:** Increase nozzle temperature in 5°C increments until adhesion improves.

Typical temperature ranges:
| Material | Min | Recommended | Max |
|---|---|---|---|
| PLA | 180°C | 200-215°C | 230°C |
| PETG | 220°C | 235-245°C | 260°C |
| ABS | 220°C | 235-250°C | 260°C |
| TPU | 210°C | 220-235°C | 250°C |

Different filament brands behave differently even within the same material type. A temperature tower test (printing at multiple temperatures in one go) finds your specific filament's sweet spot quickly. Download a free temperature tower from [Printables](https://www.printables.com/search/models?q=temperature+tower).

---

## Cause 2: Print Speed Too High

Printing too fast doesn't give each layer enough time to bond to the previous one. The molten filament needs a moment to fuse - too fast and it just sits on top without properly bonding.

**Fix:** Reduce print speed by 20-30% and test. For critical structural parts, slower is always better.

Try:
- **Walls:** 40-60mm/s
- **Infill:** 60-80mm/s
- **First layer:** 20-30mm/s always

---

## Cause 3: Cooling Too Aggressive

Part cooling is a double-edged sword. Good cooling improves surface finish and detail - but too much cooling chills the layer before the next one bonds to it, especially with materials that need high temperatures to fuse properly.

**Material-specific cooling settings:**

| Material | Fan Speed |
|---|---|
| PLA | 50-100% (after first layers) |
| PETG | 20-40% maximum |
| ABS | 0-10% maximum |
| ASA | 0-10% maximum |
| Nylon | 0% (no cooling) |

If you're printing PETG or ABS with high cooling and getting delamination, reduce your fan speed first.

---

## Cause 4: Layer Height Too Large

Each layer needs to be compressed into the previous one to bond properly. If your layer height is too large relative to your nozzle diameter, there isn't enough overlap for good adhesion.

**Rule:** Layer height should be no more than 75-80% of your nozzle diameter.

For a 0.4mm nozzle: maximum 0.3mm layer height. 0.2mm is the standard and gives excellent adhesion.

If you're using 0.3mm layers and getting adhesion issues, drop to 0.2mm.

---

## Cause 5: Wet Filament

Moisture in filament turns to steam during printing, creating micro-bubbles between layers that destroy adhesion. If your prints sound like popcorn or have a rough, bubbly texture, wet filament is likely the cause.

**Fix:** Dry your filament in a [filament dryer](https://www.amazon.com/s?k=filament+dryer+box+3d+printing) or [food dehydrator](https://www.amazon.com/s?k=food+dehydrator+filament) before printing.

Drying temperatures:
- PLA: 45°C for 4-6 hours
- PETG: 65°C for 4-6 hours
- ABS/ASA: 65°C for 4-6 hours
- Nylon: 80°C for 8-12 hours

---

## Cause 6: Under-Extrusion

If your printer isn't pushing out enough filament, each layer is thinner than intended and doesn't bond properly to the layer below.

**How to check:** Print a single-wall cube (no infill, no top layers, 1 perimeter) and measure the wall with [digital calipers](https://www.amazon.com/s?k=digital+calipers+3d+printing). It should match your set line width (typically 0.4-0.45mm for a 0.4mm nozzle).

**Fix:** Increase flow rate / extrusion multiplier in your slicer by 2-5% increments until the wall matches target thickness.

Also check:
- Extruder grip - is the filament being gripped firmly?
- Partial clog - run a few cold pulls to clear any debris
- PTFE tube gap - any gap near the nozzle causes ooze and inconsistency

---

## Cause 7: Z-Hop Causing Poor Layer Contact

Z-hop lifts the nozzle between travel moves to avoid hitting the print. If set too high, it can cool the previous layer too much before the next is deposited.

**Fix:** Reduce or disable Z-hop if you're experiencing layer adhesion issues. Most prints don't need it.

---

## ABS-Specific: Delamination and Cracking

ABS is especially prone to delamination - not just poor bonding, but layers physically splitting apart mid-print or after. This is almost always caused by:

1. **No enclosure** - the print cools too rapidly, causing thermal stress that splits layers
2. **Too much cooling** - any part cooling fan above 10% will cause delamination in tall ABS prints
3. **Cold environment** - ambient temperature below 15°C makes ABS very difficult

**Fix for ABS delamination:** Enclosed printer, zero part cooling, bed at 105-110°C, and keep the enclosure sealed throughout the print.

---

## How to Test Layer Adhesion

The best test is a simple pull test:

1. Print a 20x20x40mm block
2. Try to snap it along the layer lines (bend it across the middle)
3. A well-bonded print should require significant force to break

Compare breaks across different temperature settings using the same model to find your optimal temperature quickly.

---

## Summary Checklist

- [ ] Temperature high enough for the material?
- [ ] Fan speed appropriate for the material?
- [ ] Layer height within 75% of nozzle diameter?
- [ ] Filament dry?
- [ ] Extrusion multiplier calibrated?
- [ ] Print speed reasonable (under 80mm/s for walls)?

Work through this list in order - temperature and cooling fix the majority of layer adhesion problems.
