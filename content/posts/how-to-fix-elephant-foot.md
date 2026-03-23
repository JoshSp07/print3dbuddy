# How to Fix Elephant Foot in 3D Printing

Elephant foot is one of the most common first-layer problems in FDM printing. The base of the print flares out wider than the rest, giving it a splayed, chunky-looking bottom that ruins dimensional accuracy and makes flat-bottomed prints impossible to use as intended.

The good news is that every cause of elephant foot has a straightforward fix, and in most cases you will solve it with a single small adjustment.

---

## What Elephant Foot Is

**Elephant foot** is when the first one to three layers of a print are squashed wider than the designed dimensions. Viewed from the side, the base of the print looks like it is spreading outward, resembling the wide, flat foot of an elephant.

The width of the spreading varies. Mild elephant foot might be 0.1 to 0.3mm wider than intended on each side. Severe elephant foot can splay 1mm or more, leaving a visible skirt around the entire base of the part.

For decorative prints, elephant foot is mainly an aesthetic issue. For functional parts, anything that needs to fit inside a housing, slide into a slot, or mate with another component will not fit correctly if the base is wider than designed.

---

## Why Elephant Foot Happens

There are four main causes, and they can occur individually or in combination.

### Z-Offset Too Low

**Z-offset** is the distance between the nozzle and the bed at the start of a print. When the z-offset is too low, the nozzle is closer to the bed than it should be, which squashes the first layer plastic outward in all directions. The plastic has no room to go upward, so it spreads sideways.

This is the most common cause of elephant foot and the first thing to check.

### Bed Temperature Too High

The build plate temperature affects how quickly the first layer of plastic solidifies after being deposited. If the bed is too hot, the first layer stays soft and partially molten for long enough that the weight of the subsequent layers pressing down squashes it wider. It is effectively being compressed by the layers above before it has had time to solidify into its correct shape.

### First Layer Flow Rate Too High

**Flow rate** (also called extrusion multiplier) controls how much plastic is extruded relative to what the slicer calculates. If your first layer flow rate or general flow rate is set higher than 100%, more plastic is coming out than the layer volume requires. The excess plastic has nowhere to go except outward, causing the base to splay.

Some slicers also have a separate **first layer line width** setting. If this is set above 100%, it causes the same problem.

### No Elephant Foot Compensation

Most modern slicers include an **elephant foot compensation** setting specifically to counteract this effect. This setting instructs the slicer to slightly reduce the width of the first layer or first few layers in the model to pre-compensate for the expected spread.

If this setting is at zero and your printer has any tendency to produce elephant foot, the base will splay regardless of how well everything else is dialled in.

---

## How to Fix Elephant Foot: Step by Step

Work through these fixes in order, checking the result after each adjustment before moving on.

### Fix 1: Adjust Z-Offset

Start here. Adjust your z-offset **upward** (moving the nozzle slightly further from the bed) in **0.05mm increments**.

In most slicer and printer firmware interfaces, a more positive (or less negative) z-offset value moves the nozzle further from the bed. If your current z-offset is -1.20mm, try -1.15mm, then print a small test object (a 20mm cube or a short cylinder works well) and check the base.

**One 0.05mm increment at a time.** It is easy to overcorrect and end up with poor bed adhesion, which is a worse problem. Raise the z-offset until elephant foot disappears, but stop before the first layer becomes under-extruded or starts peeling up.

A correctly set z-offset will produce a first layer where lines are squashed together slightly but not spread wide. The surface of the first layer should look smooth and flat with no visible gaps between lines, and the base of the print should be the same width as the rest.

### Fix 2: Reduce Bed Temperature

If adjusting the z-offset by 0.1 to 0.15mm has not resolved the problem, try reducing bed temperature.

Reduce bed temp in **5°C increments** and reprint the test object after each change.

Common ranges to aim for if you have been running too hot:

- **PLA**: 55 to 65°C is typical. If you are running at 70°C or above, bring it down.
- **PETG**: 70 to 80°C. Running at 85°C or higher can cause elephant foot.
- **ABS/ASA**: 100 to 110°C. These materials genuinely need high bed temps, so reduce cautiously and prioritise the z-offset fix first.

Do not reduce bed temperature so far that the print stops adhering. There is a balance between adhesion and avoiding elephant foot, and the z-offset fix usually resolves most of the problem without needing a large temperature change.

### Fix 3: Reduce First Layer Flow Rate

In your slicer settings, look for **first layer flow rate** or **initial layer line width**. If either of these is set above 100%, reduce it to 100% and reprint.

If you have made general flow rate adjustments for over-extrusion that are above 100%, this will also contribute to elephant foot. Check your general flow rate or extrusion multiplier and confirm it is at or below 100%.

Some slicers (PrusaSlicer, Bambu Studio, Orca Slicer) have explicit flow calibration tools. If you suspect overall over-extrusion, run a flow calibration before continuing with elephant foot troubleshooting, as an incorrect global flow rate will affect everything else.

### Fix 4: Use Elephant Foot Compensation

In your slicer, search for **elephant foot compensation** (PrusaSlicer, Orca Slicer) or **initial layer horizontal expansion** (Cura). These settings apply a negative horizontal offset to the first layer or first few layers.

A value of **0.1 to 0.2mm** is a typical starting point. This instructs the slicer to print the base of each wall 0.1 to 0.2mm narrower than the model, which compensates for the expected spread.

This fix is best used in combination with the other adjustments rather than as a substitute for them. If your z-offset is wildly wrong, no amount of slicer compensation will fully correct it. Get the hardware setting roughly right first, then use slicer compensation to fine-tune.

---

## How to Check If Elephant Foot Is Fixed

Print a **20mm calibration cube** and measure the base with digital calipers.

Measure the X and Y dimensions at the very bottom of the first layer, then measure the same dimensions 5mm up from the base. If elephant foot is present, the bottom measurement will be noticeably larger (0.2mm or more) than the measurement taken higher up.

When fixed, both measurements should be within 0.1mm of each other and within 0.2mm of the designed dimension (20mm in this case).

Visually, the fixed print will have a base that looks flush with the sides of the object rather than flared outward. Looking directly at the bottom corner from the side, you should see a 90-degree angle rather than a curved or splayed edge.

---

## When Is It Actually the Correct Z-Offset?

This is worth understanding because it trips up many people.

A well-set z-offset should produce a first layer that looks squashed. The lines of the first layer should be visibly flattened compared to the layers above, with no gaps between them. This is correct and desirable. It is the squash that creates adhesion.

**Elephant foot is different from a squashed-looking first layer.** The distinction is:

- **Correctly squashed first layer**: the first layer is slightly flatter than subsequent layers, but the footprint of the print matches the model dimensions.
- **Elephant foot**: the footprint of the print is wider than the model dimensions.

If your first layer looks flat and well-adhered but the base width is correct when you measure it, your z-offset is fine. The visual appearance of a compressed first layer is expected, not a problem.

If you raise your z-offset to the point where the first layer looks normal height (matching subsequent layers exactly), you have probably gone too far. The first layer should always look slightly more compressed than the rest.

The test is the measurement, not the visual appearance of layer height.

---

## Related Guides

- [3D Printing First Layer Problems and Fixes](/posts/3d-printing-first-layer-problems-fixes/)
- [How to Fix Over Extrusion](/posts/how-to-fix-over-extrusion/)
