# What to Do When a 3D Print Fails Mid-Print

You come back to the printer expecting a finished part and find a tangled mess of spaghetti, a shifted print, or just a naked build plate with a pile of plastic next to it. Mid-print failures are frustrating, but they are almost always diagnosable and preventable once you understand what caused them.

This guide covers the five most common mid-print failure types, what to do immediately when you spot a failure, how to read the evidence, whether resuming is worth trying, and how to prevent each type from happening again.

---

## What to Do Immediately When You Notice a Failure

Before diagnosing anything, take these steps as soon as you spot a failed print.

**Stop the print.** Press pause or cancel on the printer's screen or in your slicer's monitoring software. Do not leave a failed print running. A print that has already failed will not self-correct, and continuing just wastes filament and can cause further problems (a clog worsened by continued extrusion, or a spaghetti mass wrapping around the hotend).

**Do not move the printhead manually yet.** If the print has shifted or partially separated, moving the head before you have assessed the situation can knock the remaining print off the bed or make the diagnosis harder.

**Note the layer number and print time if you can.** Your slicer or printer screen may show the current layer. This is useful for understanding how far into the print the failure occurred and whether a partial recovery is possible.

**Photograph the failure before clearing it.** A photo of the failed state takes two seconds and gives you a reference when you are trying to diagnose the cause later. The evidence on the bed and around the printer is often clearer in the immediate aftermath than after you have cleaned up.

**Save your slicer settings and gcode if you made any changes since the last print.** If you are diagnosing a settings-related failure, you want to be able to compare the failing settings to working ones.

---

## Layer Shift

### What It Looks Like

The print is intact up to a certain height, then everything above that point is offset to one side by a fixed amount. The layers above the shift are still printing correctly relative to each other, but they are displaced horizontally from the layers below.

### Diagnosing It

Look at the print from the side. If the shift is in one direction only, note which axis it is on (left-right is X, front-back is Y on most printers).

**Common causes:**

**Print speed too high** - the stepper motors are skipping steps because they cannot keep up with the commanded movement, especially on fast direction changes. This is the most common cause.

**Loose or slipping belt** - a belt that has stretched, slipped on a pulley, or is too loose will skip when the axis changes direction. Check whether the belt gives more than a few mm of slack when you press it.

**Something physical obstructing the axis** - a cable caught on the frame, a clip that moved, or dried filament on a rod. Check the full travel of the affected axis by hand with the printer powered down.

**Stepper motor driver running too hot** - in enclosed printers with poor cooling, the stepper drivers can thermally throttle and drop steps. This is less common but worth checking if shifts happen after the printer has been running for a long time.

### Resume or Restart?

A layer-shifted print is almost never worth resuming. The shifted section cannot be aligned back with the original base, and any attempt to resume will just continue printing from the shifted position. Restart the print after fixing the cause.

### Prevention

Reduce print speed, particularly travel speed and acceleration, by 20 to 30%. Check and tighten belts (they should twang like a guitar string with moderate tension, not be floppy or so tight they will not deflect at all). Check for cable or filament obstructions on each axis before long prints.

---

## Print Detached from Bed

### What It Looks Like

The print has peeled off the bed partially or fully. You may find the print sitting loose on the bed, curled up at corners, or knocked off entirely. The printer may continue printing into thin air, depositing plastic that goes nowhere useful.

### Diagnosing It

Look at the underside of the print and at the bed surface.

**Common causes:**

**Dirty bed** - skin oils from handling the bed dramatically reduce adhesion. This is the most frequent cause of prints that stuck fine before but suddenly will not adhere.

**Z-offset too high** - the nozzle was not close enough to press the first layer into the bed surface properly. Look at the underside of the print. If the first layer lines have gaps between them or look rounded rather than squashed, z-offset is too high.

**Incorrect bed temperature** - too low for the material, or the bed cooled mid-print due to a sensor issue or slicer error.

**Draught or temperature change in the room** - especially with ABS and ASA, a cold draught can cause the print to contract rapidly and peel up. This is why enclosures are recommended for those materials.

**Warping-prone material without brim** - large flat prints in PLA or PETG can warp up at corners without a brim or adhesion aid.

### Resume or Restart?

If the print detached early, restart after fixing the bed. If it detached at 80% completion and the detached portion is largely intact, it may be worth attempting to reattach it with a dot of glue stick or hairspray and resuming, but the result is rarely clean. For functional parts, restart.

### Prevention

Clean the bed with IPA before every print. Check z-offset calibration after any bed removal or maintenance. Use a brim for prints with small footprints or in warping-prone materials. Use an enclosure for ABS and ASA.

---

## Spaghetti

### What It Looks Like

A tangled mass of loose filament strands covers the build plate and print, often wrapped around the hotend or deposited in chaotic loops. The print itself may have collapsed or detached at some point, and the printer continued extruding with nothing to deposit onto.

### Diagnosing It

Spaghetti is almost always a **consequence of another failure** rather than a direct cause. The usual root cause is the print detaching from the bed or collapsing mid-print, after which the printer continues extruding with the nozzle printing into thin air or into an unstable mass.

Occasionally, spaghetti can result from a specific failure of tall, narrow prints (called **spaghettification due to part toppling**). A tall, narrow print rocks from the nozzle impacts at height until it knocks loose or snaps at the base.

### Resume or Restart?

Do not attempt to resume from spaghetti. Restart entirely after diagnosing and fixing the root cause (which is usually bed adhesion or a stability problem).

### Prevention

Fix bed adhesion issues (see above). For tall or narrow prints, add a brim to widen the footprint. Slow the print speed for tall prints at height (some slicers allow a speed-by-height curve). Monitor long prints more actively during the first few layers.

---

## Clog

### What It Looks Like

Extrusion stops or becomes very thin and inconsistent mid-print. The printer may click repeatedly (the extruder motor skipping as it tries to push filament against the blockage). The print continues to move but plastic either stops coming out or becomes a thin trickle. The result is layers that are missing or severely under-extruded above a certain point.

You may also hear a regular ticking or clicking sound, which is the extruder gear slipping against the filament.

### Diagnosing It

**Common causes:**

**Heat creep** - heat travels up the hotend into the cold zone, causing filament to soften too early and jam in the heatbreak. More common in all-metal hotends and in printers without adequate cooling on the heatsink.

**Filament quality issue** - inconsistent filament diameter can jam in the nozzle. Filament that has absorbed moisture creates steam bubbles in the melt zone, which can cause inconsistent flow and jams.

**Partial blockage from a previous print** - a small amount of carbonised filament, debris, or a fragment of a previous jam still in the nozzle.

**Running at too low a temperature** - if nozzle temperature drops slightly (draft, sensor variation, or an incorrectly low temperature setting for a different material) the filament may not melt fast enough and backs up.

### Resume or Restart?

Clear the clog first. Most clogs can be cleared with a **cold pull**: heat the nozzle to print temperature, push a length of filament in by hand until it flows, then allow the nozzle to cool to around 90°C (for PLA) or 140°C (for PETG) while keeping gentle forward pressure on the filament, then pull it sharply out. Repeat until the pulled filament comes out clean.

Once the clog is clear, resuming at the correct layer is sometimes possible if the print is still on the bed and structurally sound. Check whether the print height matches the layer you are resuming from and test extrusion before resuming. For important functional prints, restarting is safer.

### Prevention

Ensure heatsink cooling fans are working and unobstructed. Check filament diameter consistency and store filament dry. Do not leave the printer at printing temperature with no movement for extended periods. Run a temperature tower calibration for each new filament brand to confirm the correct print temperature.

---

## Power Cut

### What It Looks Like

The printer is off, mid-print, with a partial part on the bed. The print may be cold but intact, or the filament may have solidified and bonded to the nozzle during the power loss.

### Diagnosing It

Check the print for quality up to the point the power cut. If the print quality was good and the part is still adhered to the bed, a resume attempt may be worthwhile. If the nozzle has cooled with filament bonded to the print, carefully heat the nozzle to print temperature to release it before moving the head.

### Resume or Restart?

**Power loss resume** is a feature on many modern printers (Creality, Bambu, Prusa, and others). If your printer supports it, it will prompt you to resume from the last saved position when power is restored.

However, the quality of power loss recovery varies. There will almost always be a slight visual seam at the layer where the print stopped and resumed. For functional parts, this is acceptable. For cosmetic parts, it may not be.

If your printer does not support power loss recovery, or if significant time has passed and the print has cooled fully (which can cause adhesion issues), restarting is the safer option.

### Prevention

A **UPS (uninterruptible power supply)** is the most reliable prevention. Even a small UPS rated for a few minutes of runtime will keep the printer running through short power interruptions and give you time to properly cancel a print during an extended outage.

---

## When to Do a Maintenance Check Before Reprinting

Not every failed print requires a maintenance check, but certain failure patterns are a signal that you should check the printer before starting the next job rather than just pressing print again.

**Check before reprinting if:**

- You had a layer shift (check belts, lubrication, and axis travel).
- You had a clog (clear the clog fully and check hotend and PTFE tube condition).
- The print detached and the printer continued running into nothing for a long time (check the nozzle for carbonised plastic buildup, and check whether any plastic got into the cooling fan or under the print carriage).
- The extruder made grinding or clicking noises (inspect the extruder gear for wear and confirm it is gripping filament correctly).
- The printer has been running for more than 200 hours since the last general check (lubricate rods, check all bolts and screws for looseness, inspect PTFE tube ends for wear).

Taking five minutes to check the printer before a three-hour job is much better than finding out something is wrong three hours in.

---

## Related Guides

- [How to Fix Layer Shifting](/posts/how-to-fix-layer-shifting/)
- [How to Fix 3D Printer Grinding Noise](/posts/how-to-fix-3d-printer-grinding-noise/)
- [How to Maintain Your 3D Printer](/posts/how-to-maintain-3d-printer/)
