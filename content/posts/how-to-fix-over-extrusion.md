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

## Checklist

1. Print a single-wall box and measure - adjust flow rate to match target line width
2. Calibrate e-steps if never done on this machine
3. Drop temperature 5-10°C and test
4. If only the first layer is affected, see the [elephant foot guide](/posts/how-to-fix-elephant-foot/)
5. If over-extrusion is inconsistent, do a cold pull to clear a partial clog
