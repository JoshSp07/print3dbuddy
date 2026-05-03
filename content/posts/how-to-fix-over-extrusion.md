# How to Fix Over-Extrusion in 3D Printing

Over-extrusion is less dramatic than a spaghetti failure but it quietly ruins print quality and makes functional parts useless. Walls that bow outward, blobs on the surface, holes that come out too small to fit a bolt through - all of these can trace back to too much plastic being pushed out.

It is also one of the easier problems to fix once you know what to look for.

---

## What Over-Extrusion Looks Like

- Walls that bow outward slightly
- Blobs or zits dotted across the outer surface
- Corners that look rounded or filled in rather than sharp
- First layer spreading wider than the model (this specific issue is elephant foot - covered in the [elephant foot guide](/posts/how-to-fix-elephant-foot/))
- Dimensional inaccuracy - holes too small, parts that do not fit together
- Excess filament building up on top surfaces, leaving a rough finish

---

## Fix 1: Calibrate Flow Rate (Extrusion Multiplier)

The most common cause. Flow rate - also called extrusion multiplier or extrusion factor depending on the slicer - defaults to 100% but every printer and filament combination is slightly different. Running at 105% when you need 100% is enough to cause visible over-extrusion on detailed parts.

Print a single-wall box: no top layers, no bottom layers, no infill, one perimeter. Measure the wall thickness with digital calipers. It should match the line width set in your slicer - typically 0.4-0.45mm for a 0.4mm nozzle. If the walls are thicker than that, reduce flow rate in 2-3% increments and reprint until they match.

This is the calibration I do on every new filament spool before running anything that needs to fit precisely. Budget filament in particular often needs adjusting - the diameter can run slightly wide and push the effective flow rate up.

---

## Fix 2: Check E-Steps

E-steps tell the printer how many motor steps equal 1mm of filament movement. If these are set too high, more filament is physically pushed than the printer accounts for.

Mark 100mm and 120mm on filament above the extruder. Command the printer to extrude exactly 100mm (with the hotend at temperature). Measure how much actually moved. If it moved more than 100mm, e-steps are too high.

New e-steps = (current e-steps x 100) / actual mm extruded

This is a one-time calibration per machine. Once set, it does not drift unless you change the extruder hardware.

---

## Fix 3: Lower Print Temperature

The hotter the filament, the more it flows and the harder it is to control precisely. Printing 10-15°C hotter than needed produces blobs, stringing, and slight over-extrusion. I have seen machines printing PLA at 225°C that cleaned up completely at 205°C - same spool, same settings otherwise.

Try dropping temperature in 5°C steps:
- PLA: 200-215°C
- PETG: 230-245°C
- ABS/ASA: 235-250°C

If reducing temperature causes under-extrusion or layer adhesion problems, the temperature was correct and the problem lies elsewhere.

---

## Fix 4: Check for a Partial Nozzle Blockage

A partial blockage causes irregular pressure inside the hotend. Molten filament accumulates behind the blockage until pressure builds enough to force a surge through - the surge looks like over-extrusion in patches, but with under-extruded areas around it.

Signs this is the cause: over-extrusion that appears randomly rather than consistently, combined with some under-extruded patches in the same print. Consistent over-extrusion everywhere is a flow rate or temperature problem, not a blockage.

Fix: cold pull. Heat to printing temperature, push filament through manually, cool to around 90°C and pull sharply. Repeat until the pulled tip comes out clean with no brown or black discolouration. The [nozzle guide](/posts/complete-nozzle-guide-3d-printing/) has full cold pull instructions.

---

## Fix 5: Check the Extruder Gear Set Screw

The extruder gear has a small set screw that holds it to the motor shaft. If it's even slightly loose, the gear slips intermittently under load, causing inconsistent extrusion that shows up as patches of over-extrusion between normal-looking sections.

Check this if the over-extrusion is inconsistent rather than uniform. With the motor off, grip the extruder gear and try to twist it relative to the shaft. Any play means the screw needs tightening. It's usually a 1.5mm or 2mm hex key.

While you're looking at it: worn or clogged gear teeth from printing abrasive filaments can't grip filament reliably and cause erratic extrusion in both directions.

---

## What Looks Like Over-Extrusion But Isn't

**First-layer squish:** A first layer that looks flat and wide is usually intentional. Printers squash the first layer for adhesion. If the first two layers look squashed but everything above them looks normal in width, that's correct first-layer behaviour, not over-extrusion. The test is always to measure a layer a few millimetres up, not right at the base.

**Seam buildup:** Every print has a seam where each layer starts and ends. A small raised spot at the seam is normal. If blobs appear in multiple locations around the perimeter, or if the full outer perimeter has a ridge running its length, that's actual over-extrusion.

---

## Why It's Worth Fixing Properly

Mild over-extrusion is easy to ignore, but it has practical consequences that add up:

Holes and openings print undersized. An M3 bolt hole designed at 3.2mm prints at 2.9mm, which means drilling out every single print that needs hardware inserted.

Mating parts don't fit. Brackets, enclosures, snap fits, anything that has to slot into something else will fail if each wall face is 0.1-0.2mm wider than designed. This is consistent and predictable once you know what's causing it.

Top surfaces stay rough regardless of other settings. Over-extruded perimeters pile up slightly at the edges, and the top surface layers then bridge over a raised lip rather than lying flat.

A five-minute flow rate calibration fixes all three at once.

---

## Checklist

1. Print a single-wall box and measure - adjust flow rate to match target line width
2. Calibrate e-steps if never done on this machine
3. Drop temperature 5-10°C and test
4. If only the first layer is affected, see the [elephant foot guide](/posts/how-to-fix-elephant-foot/)
5. If over-extrusion is inconsistent, do a cold pull to clear a partial clog
6. Check extruder gear set screw if issue is intermittent and non-uniform
