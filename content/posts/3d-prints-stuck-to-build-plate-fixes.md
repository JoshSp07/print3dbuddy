# Prints Stuck to the Build Plate: Causes and Fixes

A print fusing itself to the bed is one of the more frustrating problems in 3D printing. What should take five seconds - lift the print off, done - turns into ten minutes of prying, scraping, and hoping you do not gouge the surface.

The irony is that good bed adhesion is exactly what you spent time calibrating. The fix is not less adhesion, it is more controlled adhesion - firm during the print, clean release once cooled.

---

## Why Prints Stick Too Hard

The main causes:

- Bed still hot - most surfaces release much more easily once fully cooled
- Z-offset too low - first layer pressed too hard into the bed texture
- PETG on smooth PEI - PETG bonds chemically with PEI at high temperatures
- Bed temperature too high for the material
- Adhesive build-up - old glue stick layers stacking up and creating a bond rather than a release

---

## Fix 1: Let It Cool Completely

The most commonly skipped step. PLA on a textured PEI sheet goes from "stuck solid" to "lifts with a light push" somewhere around 30-35°C bed temperature.

Wait until the bed is fully at room temperature before trying to remove the print. On a heated bed that means 10-15 minutes after the print ends - longer if you have a thick glass or aluminium plate, which holds heat longer. Trying to remove the print at 50°C and then wondering why it won't come off is one of those things everyone does once.

If you need it faster, a brief blast of compressed air across the base of the print helps the surface cool and contract away from the bed texture.

---

## Fix 2: Use a Thin Flexible Spatula

Do not pry with a thick metal scraper - you will gouge the bed and stress the print. A thin flexible spatula lets you work under the edge of the print without force.

The technique: hold the spatula nearly flat against the bed, edge-on, and slide it under the brim or first layer perimeter. Work around the outside gradually rather than levering from one spot. Once the edge is free the print usually lifts easily.

If you have a magnetic spring steel PEI sheet, flex the sheet itself. A slight bow pops most prints off with no tools at all - this is one of the main reasons spring steel sheets are worth having.

---

## Fix 3: Raise Z-Offset

If prints are consistently stuck even after full cooling, the first layer is being squashed too hard into the bed texture. Too low a Z-offset presses filament into every groove and pore of the surface, creating a mechanical lock.

What the first layer should look like: flat ribbons, slightly wider than the filament diameter, but with visible ridges between passes and some height to them. Not a completely transparent, solid sheet with no texture at all.

Raise Z-offset in 0.05mm increments and test. Stop when prints release cleanly but still adhere solidly during printing - the margin is usually 0.1-0.15mm.

---

## Fix 4: Lower Bed Temperature

Reducing bed temperature by 5-10°C while keeping everything else the same is often enough to shift from stuck to releasing cleanly.

| Material | Common bed temp | Try reducing to |
|---|---|---|
| PLA | 60°C | 50-55°C |
| PETG | 70-80°C | 65°C |
| ABS | 100-110°C | 95-100°C |
| ASA | 100-110°C | 95°C |

Lower temperature means slightly less adhesion, so watch the first layer carefully. If corners start lifting you have gone too far.

---

## Fix 5: PETG on PEI

PETG is the worst offender for over-bonding. On smooth PEI at high temperatures, it can chemically fuse to the surface and rip chunks out when you remove the print.

A company I worked with had this happen repeatedly on a batch of smooth PEI sheets they had bought. Three sheets damaged in a week before we identified the cause. The fix was straightforward once we understood what was happening.

For PETG on PEI:

- Switch to textured PEI - the reduced contact area means PETG grips well during printing but releases cleanly once cool
- Apply a thin layer of glue stick between the PETG and the bed as a release layer - it prevents direct contact between the two materials
- Drop bed temperature to 65-70°C - high enough to print, low enough to reduce the chemical bonding

Do not let PETG prints cool fully on smooth PEI - they can actually get harder to remove the cooler they get once they have bonded at temperature.

---

## Fix 6: Clean the Build Surface

A dirty bed behaves unpredictably - sometimes gripping too hard, sometimes not adhering at all.

For PEI: wipe with 90%+ IPA on a lint-free cloth before every few prints. This removes skin oils that contaminate the surface. Do not use acetone on PEI - it degrades the surface over time.

For glass: warm soapy water removes adhesive residue. Dry thoroughly before heating.

Old glue stick layers build up over time and change how the surface behaves. If you have been using glue stick regularly, wash it off completely with warm water, dry the sheet, and retest.

---

## When to Replace the Surface

If your PEI sheet has deep gouges, peeling edges, or patches where behaviour is unpredictable regardless of cleaning, replace it. PEI sheets wear out after hundreds of prints and a worn sheet causes adhesion problems that no amount of settings adjustment will fix. Replacement sheets are inexpensive and most fit any magnetic bed system.

---

## Summary

| Cause | Fix |
|---|---|
| Print still warm | Wait until bed is at room temperature |
| Z-offset too low | Raise 0.05mm at a time |
| Bed temp too high | Drop 5-10°C |
| PETG on smooth PEI | Switch to textured PEI or use glue stick as release |
| Dirty surface | IPA for PEI, soapy water for glass |
| Worn surface | Replace the sheet |

For most setups, the fix is cooling time or Z-offset. Sort those first before changing anything else.
