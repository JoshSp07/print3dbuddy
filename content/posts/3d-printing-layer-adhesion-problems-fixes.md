# 3D Printing Layer Adhesion Problems: Causes and Fixes

Layer adhesion problems are one of the most common issues across all printer types and skill levels. The print looks fine on the outside but snaps along a layer line when you flex it, or layers visibly separate during printing, or the surface has a rough grainy texture that should not be there.

In most cases the root cause is one of three things: temperature too low, cooling too aggressive for the material, or wet filament. Work through those first before looking elsewhere.

---

## Signs of Poor Layer Adhesion

- Parts split or delaminate when handled - snap cleanly along a layer line with minimal force
- Visible gaps between layers on the surface
- Rough, grainy texture that looks like sand
- Layers visibly separating during printing
- Prints feel lightweight and hollow compared to how they should feel

---

## Cause 1: Print Temperature Too Low

The most common cause. If the nozzle temperature is too low, the filament does not fully melt and bond to the previous layer. I have seen this repeatedly on machines where the stock temperature profiles are conservative - the printer ships tuned to avoid blobs and stringing at the cost of adhesion.

Increase nozzle temperature in 5°C increments and test. The change in adhesion is usually obvious within a couple of layers.

| Material | Minimum | Recommended | Maximum |
|---|---|---|---|
| PLA | 180°C | 200-215°C | 230°C |
| PETG | 220°C | 235-245°C | 260°C |
| ABS | 220°C | 235-250°C | 260°C |
| TPU | 210°C | 220-235°C | 250°C |

These ranges vary by brand. A temperature tower - one print that tests multiple temperatures in a single run - finds the sweet spot for a specific filament much faster than printing individual test pieces at each temperature. The [temperature tower on our Test Prints page](https://tools.print3dbuddy.com/test-prints#temp-tower) includes a guide for reading the results.

---

## Cause 2: Cooling Too Aggressive

Part cooling and layer adhesion are in direct tension with each other. Cooling improves surface finish and detail, but too much cools the previous layer before the next one can fuse to it. This is especially destructive with materials that need high temperatures to bond properly.

A print farm that I worked with had six PETG machines all producing weak parts that failed at the layer lines under minimal stress. Every printer was running the same cooling profile that had been set up for PLA and never adjusted. Dropping from 60% fan to 25% fan on all six machines fixed the problem across the board.

| Material | Fan Speed |
|---|---|
| PLA | 50-100% |
| PETG | 20-40% maximum |
| ABS | 0-10% maximum |
| ASA | 0-10% maximum |
| Nylon | 0% |

If you are printing PETG or ABS with high fan speeds and seeing delamination, reduce cooling before touching anything else.

---

## Cause 3: Print Speed Too High

Printing too fast means each layer has less time at the deposition point to bond to the previous one. There is less heat transfer, less fusion, and weaker bonds.

The effect is more pronounced on materials that need higher temperatures. ABS at 80mm/s can show adhesion problems that disappear completely at 50mm/s without changing anything else.

Reduce speed by 20-30% and test. For structural parts, slower is nearly always stronger.

Starting points for wall speed:
- Outer walls: 40-60mm/s
- Inner walls: 60-80mm/s
- First layer: 20-30mm/s

---

## Cause 4: Layer Height Too Large

Each layer must compress into the previous one to bond properly. If layer height is too large relative to nozzle diameter, there is not enough overlap for good fusion.

Layer height should be no more than 75-80% of nozzle diameter. For a standard 0.4mm nozzle, that means a maximum of 0.3mm. 0.2mm is the standard and gives excellent adhesion. If you are using 0.3mm layers and seeing adhesion problems, drop to 0.2mm and test.

---

## Cause 5: Wet Filament

Moisture in filament turns to steam during printing, creating micro-bubbles between layers. The result is poor adhesion, rough surface texture, and sometimes visible bubbling on the print surface. If there is a crackling or popping sound during printing, the filament is wet.

Dry the filament before printing. See the [wet filament guide](/posts/how-to-fix-wet-filament/) for drying times and temperatures by material. Drying takes a few hours but fixes the problem immediately.

PETG and Nylon absorb moisture significantly faster than PLA. A spool of PETG left open in a humid room for 48 hours can produce noticeably degraded prints - not just aesthetically but in layer adhesion and final part strength.

---

## Cause 6: Under-Extrusion

If not enough filament is coming out, each layer is thinner than designed and does not bond properly to the layer below.

Check by printing a single-wall box (no infill, no top layers, one perimeter) and measuring the wall with digital calipers. It should match your set line width - typically 0.4-0.45mm for a 0.4mm nozzle. If it is short, increase extrusion multiplier in 2-3% increments.

Also check:
- Extruder grip (look for stripped filament just above the drive gear)
- Cold pull to clear partial clogs
- Bowden tube seated fully with no gap at the nozzle end

---

## ABS Specifically: Delamination and Cracking

ABS delamination is its own category. Layers physically splitting apart mid-print or cooling to a cracked part is almost always caused by an enclosure problem, not a temperature problem.

Without an enclosure, the top layers of an ABS print cool in open air while the lower layers sit on a 105°C bed. The temperature differential creates thermal stress that physically tears layers apart. No temperature increase compensates for this.

For ABS: enclosed printer, no part cooling, bed at 105-110°C, enclosure sealed throughout. That is the baseline - without it, delamination is expected, not a fault.

---

## Testing Adhesion

Print a 20x20x40mm block and try to snap it along the layer lines. A well-bonded print requires significant force. Run the same test at different temperatures to find where adhesion noticeably improves - this is faster and more useful than surface inspection alone.

---

## Summary Checklist

- Temperature correct for the material and brand?
- Fan speed appropriate - not too high for PETG/ABS?
- Layer height within 75% of nozzle diameter?
- Filament dry?
- Extrusion multiplier calibrated?
- Print speed reasonable for the material?

Temperature and cooling resolve the majority of layer adhesion problems.
