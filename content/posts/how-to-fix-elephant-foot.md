# How to Fix Elephant Foot in 3D Printing

Elephant foot is when the base of a print flares out wider than the rest, giving it a splayed bottom edge. For decorative prints it is mainly cosmetic. For anything functional - a bracket, a housing, a part that needs to slot into something else - it means the print does not fit as designed.

Every cause of elephant foot has a direct fix, and in most cases one small adjustment sorts it.

---

## What It Is

The first one to three layers print wider than the designed dimensions. Viewed from the side, the base of the print spreads outward like the foot of an elephant - hence the name.

Mild elephant foot is 0.1-0.3mm wider than intended on each side. Severe cases can splay 1mm or more, leaving a visible flared skirt around the entire base.

The test is measurement, not appearance. A correctly set Z-offset will produce a first layer that looks visually squashed - that is expected and correct. Elephant foot is confirmed when the width measured at the base is larger than the width measured 5-10mm up.

---

## Cause 1: Z-Offset Too Low (Most Common)

When the nozzle is closer to the bed than it should be, the first layer gets squashed outward in all directions. The plastic has no room to go up, so it spreads sideways.

Fix: raise Z-offset in 0.05mm increments. In most slicer and firmware interfaces, a less negative value moves the nozzle further from the bed. Go one increment at a time - it is easy to overcorrect and end up with poor adhesion, which is a worse problem.

Stop when the base width measured with calipers matches the width higher up the print. The first layer will still look slightly compressed - that is correct. The footprint is what matters, not the visual layer height.

---

## Cause 2: Bed Temperature Too High

If the bed is too hot, the first layer stays soft long enough for the weight of subsequent layers pressing down to squash it wider. It is being compressed before it has had time to solidify into shape.

Fix: reduce bed temperature in 5°C increments and reprint.

Common targets if you have been running too hot:
- PLA: 55-65°C. If you are running at 70°C or above, bring it down.
- PETG: 70-80°C. Running above 85°C can cause elephant foot.
- ABS/ASA: 100-110°C. These genuinely need high bed temps - prioritise the Z-offset fix first before reducing temperature on these materials.

Do not reduce so far that the print stops adhering. The Z-offset fix usually handles most of the problem without needing a large temperature change.

---

## Cause 3: First Layer Flow Rate Too High

If your first layer flow rate or general extrusion multiplier is set above 100%, more plastic is coming out than the layer volume requires. The excess spreads outward.

Fix: in your slicer, check first layer flow rate and initial layer line width. If either is above 100%, bring it back to 100% and reprint. If your general flow rate is miscalibrated high, that will also contribute - run a single-wall box calibration (measure wall thickness with calipers, adjust until it matches your set line width) before continuing.

---

## Cause 4: No Elephant Foot Compensation

Most modern slicers have an elephant foot compensation setting. In PrusaSlicer and Orca Slicer it is called elephant foot compensation. In Cura it is called initial layer horizontal expansion.

A value of 0.1-0.2mm applies a negative horizontal offset to the first few layers, pre-compensating for the expected spread.

Use this in combination with the other fixes rather than instead of them. If the Z-offset is significantly wrong, slicer compensation alone will not fully correct it. Get the hardware setting roughly right first, then use this to fine-tune.

---

## How to Verify It Is Fixed

Print a 20mm calibration cube. Measure with digital calipers at the very bottom of the first layer, then again 5-10mm up from the base.

When fixed:
- Both measurements should be within 0.1mm of each other
- Both should be within 0.2mm of the designed 20mm dimension
- The base corner viewed from the side should look like a 90-degree angle, not a curve or flare

---

## Fix Order

1. Raise Z-offset 0.05mm - check base width
2. Reduce bed temperature 5°C if Z-offset adjustment alone was not enough
3. Check first layer flow rate and line width - set both to 100%
4. Add 0.1-0.2mm elephant foot compensation in slicer as a fine-tune
