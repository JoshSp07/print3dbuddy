# PETG on PEI: Common Problems and How to Fix Them

PETG and PEI sheets are a popular combination - but they come with a catch. Print too cold or too dry and nothing sticks. Print too hot or with the wrong settings and your print fuses to the bed permanently. This guide covers every common PETG-on-PEI problem and exactly how to fix it.

---

## Why PETG and PEI Is a Tricky Combination

PEI (polyetherimide) is one of the best general-purpose build surfaces for 3D printing. It grips PLA well, releases cleanly when cool, and lasts for hundreds of prints. With PETG, it works brilliantly - but the margin for error is narrower.

PETG is slightly adhesive by nature. At the right temperature and with the right first layer settings, it sticks well and releases when the plate cools. Too much heat, too much squish, or a surface that is too clean and you can end up with prints that are genuinely difficult to remove - or that tear chunks out of your PEI sheet.

---

## Problem 1: PETG Sticking Too Well (Impossible to Remove)

This is the most common complaint, and it is almost always caused by one or more of these:

**Bed temperature too high.** PETG on PEI works well at 70 - 80°C. If you are running 85°C or above, PETG bonds very aggressively to the surface. Drop the bed temp by 5°C at a time until prints release cleanly when cool.

**First layer squish too much.** PETG does not need to be flattened into the bed the way PLA does. A slightly raised first layer (0.1 - 0.2mm gap rather than the maximum squish some people aim for) sticks reliably without welding itself to the surface.

**Print temperature too high.** Higher nozzle temps make PETG more fluid and more adhesive. Try dropping nozzle temp by 5 - 10°C.

**A light release agent helps.** A very thin coat of glue stick (Pritt Stick or similar) applied to the PEI sheet creates a slight barrier between the PETG and the surface. It still grips well enough for printing but releases much more cleanly. Wipe off with water between prints.

**Wait for the bed to cool fully.** PETG releases significantly better at room temperature than at 40 - 50°C. If you are trying to remove prints while the bed is still warm, wait another 5 - 10 minutes.

---

## Problem 2: PETG Not Sticking at All

If PETG is lifting off the PEI mid-print or not bonding on the first layer:

**Clean the PEI surface.** Oils from your hands prevent PETG from bonding. Wipe the surface with isopropyl alcohol (90%+ IPA) before every print. Do not touch the print area after cleaning.

**Increase bed temperature.** If you are running below 70°C, try 75 - 80°C. PETG needs a warmer bed than PLA to bond reliably.

**Increase nozzle temperature.** PETG typically needs 230 - 250°C. If you are printing below 230°C, the first layer may not bond properly.

**Improve first layer adhesion settings.** Try:
- Slow the first layer speed to 20 - 30mm/s
- Increase first layer line width to 110 - 120%
- Add a brim (3 - 5mm) for parts with small footprints

**Check your Z offset.** If the nozzle is too far from the bed, the filament will not press into the surface properly. Lower the Z offset until you see a slight squish on the first layer - not flattened, but making contact.

Run a [first layer calibration test](https://tools.print3dbuddy.com/test-prints#first-layer-test) to dial this in visually before printing your actual part.

---

## Problem 3: PETG Stringing More Than Usual

PETG strings more than PLA by nature - it is a stickier material. But excessive stringing is still avoidable.

**Lower print temperature.** Try dropping nozzle temp to 230°C if you are currently running hotter. Every 5°C makes a noticeable difference to stringing.

**Increase retraction.** PETG needs more retraction than PLA in most setups:
- Direct drive: 1 - 2mm at 35 - 45mm/s
- Bowden: 5 - 7mm at 40 - 60mm/s

Use the [retraction calculator](https://tools.print3dbuddy.com/retraction-calculator) to get a starting point, then test with a retraction tower.

**Enable combing.** In Cura, set combing mode to "Not in Skin" or "All." In PrusaSlicer and Bambu Studio, enable "Avoid crossing perimeters." This keeps the nozzle over printed areas during travel moves and dramatically reduces stringing.

**Do not over-retract.** Too much retraction with PETG causes heat creep and clogs because the soft filament gets pulled into the heat zone and jams. If you start seeing under-extrusion after fixing stringing, you have gone too far.

See the full [stringing fix guide](/posts/how-to-fix-3d-printer-stringing/) for more detail.

---

## Problem 4: PETG Looks Rough or Bubbly on the Surface

A rough, bubbly, or foamy-looking surface almost always means **wet filament.**

PETG absorbs moisture from the air faster than PLA. Even a roll that has been open for a few days in a humid environment can start printing badly. Symptoms include:

- Popping or crackling sounds while printing
- Rough, foamy surface texture
- Inconsistent extrusion
- More stringing than usual

**Fix:** Dry your filament before printing. 65°C for 4 - 6 hours in a [filament dryer](https://www.amazon.co.uk/s?k=filament+dryer+box+3d+printing&tag=print3dbuddy2-21) or food dehydrator resolves moisture issues. See the [wet filament guide](/posts/how-to-fix-wet-filament/) for full drying instructions and how to test if moisture is the cause.

---

## Problem 5: PETG Layers Splitting or Poor Layer Adhesion

If your PETG prints are weak, snapping easily, or showing gaps between layers:

**Increase nozzle temperature.** Layer bonding in PETG improves significantly at higher temperatures. Try 240 - 250°C. The material bonds to itself much better when it is fluid enough to flow into the previous layer.

**Slow down.** Higher speeds reduce the time each layer has to bond. Drop your print speed by 20 - 30% and check whether layer adhesion improves.

**Check cooling.** PETG does not want aggressive cooling. Too much fan can cause layers to solidify before bonding properly. Reduce your fan to 30 - 50% (or even off for the first few layers) and see if strength improves.

See the [layer adhesion guide](/posts/3d-printing-layer-adhesion-problems-fixes/) for a deeper dive.

---

## PETG on PEI Settings Reference

| Setting | Recommended Range |
|---|---|
| Bed temperature | 70 - 80°C |
| Nozzle temperature | 230 - 250°C |
| First layer speed | 20 - 30mm/s |
| Retraction (direct drive) | 1 - 2mm |
| Retraction (Bowden) | 5 - 7mm |
| Part cooling fan | 30 - 50% |
| Release aid | Thin glue stick coat |

---

## Related Guides

- [PETG Printing Guide](/posts/petg-printing-guide/) - full PETG settings from scratch
- [How to Fix Stringing](/posts/how-to-fix-3d-printer-stringing/) - retraction, temperature, and travel settings
- [How to Fix Wet Filament](/posts/how-to-fix-wet-filament/) - drying and storage
- [First Layer Problems and Fixes](/posts/3d-printing-first-layer-problems-fixes/) - bed levelling and Z offset
- [Layer Adhesion Problems](/posts/3d-printing-layer-adhesion-problems-fixes/) - temperature, speed, and cooling
