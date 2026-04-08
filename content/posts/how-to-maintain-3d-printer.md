# How to Maintain Your 3D Printer: A Practical Guide

Most 3D printing problems that seem mysterious - inconsistent extrusion, sudden layer shifts, stringing that appears after months of clean prints - are maintenance problems. The printer has not broken randomly. Something has loosened, worn, or accumulated debris to the point where it affects printing.

The pattern I see most often when troubleshooting someone else's machine: the printer worked well for the first few months, then problems started creeping in gradually. By the time they ask for help, the belt is visibly slack, the lead screw has not been lubricated in a year, and the nozzle is half-clogged with carbonised filament. Each problem on its own might be manageable. Together they make the printer genuinely difficult to diagnose.

Routine maintenance takes about 30 minutes once you know what to do, and it prevents far more downtime than it costs.

---

## After Every Print

**Remove filament carefully.** Do not pull filament cold. Heat the nozzle first and retract or pull while the filament is still soft. Cold-pulling loaded filament can damage the extruder drive gear over time.

**Wipe the build surface.** IPA on a lint-free cloth removes skin oils and adhesive residue. Do this before every print if you can, or at minimum when adhesion starts degrading. Fingerprints on PEI cut adhesion more than most people expect.

**Clear blobs and strings from the nozzle.** Small bits of filament stuck to the outside of the nozzle or heater block will eventually fall onto the print mid-job. Remove them with tweezers while the nozzle is still warm.

---

## Every Week or Every 10-15 Prints

**Check belt tension.** Press each belt with a finger. It should feel firm and spring back, not floppy. Loose belts cause layer shifting and ghosting. On most modern printers there is a built-in tensioner wheel at the end of each axis - use it rather than adjusting the belt clips. See the [layer shifting guide](/posts/how-to-fix-layer-shifting/) for what to look for.

**Inspect the hotend area.** Look for filament buildup or burnt plastic around the nozzle and heater block. Small buildups can be cleared with a brass wire brush when the hotend is warm (around 100-120°C, not printing temperature). Keep fingers clear.

**Check the PTFE tube on Bowden printers.** The tube should be fully seated at both ends with no gap at the nozzle end. A small gap there causes filament to accumulate and partially block over time. This is one of the most common causes of mysterious clogs on Bowden machines.

---

## Every Month or Every 50-100 Prints

**Lubricate the lead screws and smooth rods.** The Z-axis lead screw needs periodic lubrication - wipe off the old grease first, then apply a PTFE-based lubricant or light machine oil along the threads. Smooth rods take a light oil or PTFE grease. Do not use WD-40 - it evaporates quickly and leaves residue that makes things worse.

**Lubricate linear rails if fitted.** CoreXY printers with MGN linear rails need a small amount of light machine oil or grease applied to the rail. Dry rails sound scratchy during fast moves and cause jerky motion that shows up as surface artefacts.

**Tighten all frame screws.** Vibration works screws loose over hundreds of hours of printing, especially on printers with a lot of moving mass. I have worked on machines where half the frame bolts had backed out to the point of being finger-loose. Check all accessible frame bolts and tighten anything that has moved. Pay particular attention to the gantry and print head carriage.

**Check eccentric nuts and V-slot wheels.** On Ender 3 series printers and similar V-slot designs, the wheels have eccentric nuts that control how tightly they grip the rail. Worn wheels develop flat spots and cause uneven movement. Spin each wheel by hand - it should roll smoothly with no rough patches. Replace wheels that have flat spots.

---

## Every Few Months or When Problems Appear

**Cold pull the nozzle.** Nozzles accumulate burnt filament over time, especially when switching between materials. A partial clog shows up as inconsistent extrusion, rough surface texture, or prints that gradually get worse over a session.

Heat to printing temperature, push filament through manually, cool to around 90°C for PLA (higher for other materials) and pull sharply. The pulled tip should come out clean with a shape that reflects the inside of the nozzle - no brown or black residue, no rough texture. Repeat until it comes out clean. Full instructions are in the [nozzle guide](/posts/complete-nozzle-guide-3d-printing/).

**Check and re-level the bed.** Bed levelling drifts as components settle and the printer accumulates vibration hours. If first layer adhesion has gradually gotten worse without any obvious cause, re-level before touching any other settings.

**Inspect all wiring.** Hotend and heated bed cables are high-movement cables that flex thousands of times over the life of the printer. Look for cracked insulation, fraying at connectors, or cables that have pulled loose. A loose thermistor connection causes temperature errors or thermal runaway - check connectors are seated firmly.

**Replace the nozzle if needed.** Brass nozzles wear after 3-6 months of regular printing, and accumulated residue eventually makes cold pulls less effective. A new nozzle costs very little and fixes a lot of printing problems that seem unrelated to the nozzle. If you print abrasive materials (carbon fibre, glow-in-the-dark, wood fill), the wear rate is much faster.

---

## Symptoms That Mean Maintenance Is Overdue

- Inconsistent extrusion or sudden under-extrusion - check nozzle, PTFE tube, extruder gear
- Layer shifting that was not there before - check belts and pulley grub screws
- Adhesion that has gotten steadily worse - clean the build plate with IPA
- Grinding or scratching from the Z-axis - lubricate the lead screw
- Ghosting or ringing that has gotten worse - check belt tension and frame screws
- Printer running louder than it used to - check for loose screws, dry bearings, worn wheels

These are not random failures. They all have a maintenance cause and a maintenance fix.
