# How to Fix Ghosting and Ringing in 3D Prints

Ghosting (also called ringing or vibration artefacts) appears as wavy or ripple-like patterns on the surface of a print, most visible near sharp corners, text, or any sudden change in direction. The print is structurally fine - it is purely a surface quality issue - but it makes prints look rough and obscures fine detail.

It is especially noticeable on faster printers and on prints with a lot of sharp features. It also tends to get worse gradually on a machine that was previously printing cleanly, usually because belts have loosened or screws have worked free over time.

---

## What Ghosting Looks Like

Horizontal ripples or waves on the outer surface, most obvious:
- Just after a sharp corner - the vibration echoes along the wall for a few millimetres
- On text or lettering embossed on vertical surfaces
- On any flat vertical face near a sharp edge

The cause is the printer frame vibrating when the print head changes direction quickly. The head overshoots, bounces back, and the nozzle lays down slightly incorrect lines until the vibration dampens out.

---

## Which Axis Is Causing It

Before going further - identify which axis:

- **Ripples on the X-facing walls** (left and right sides of the print as oriented on the bed): the Y axis is the likely culprit - the bed or gantry moving front and back is vibrating
- **Ripples on the Y-facing walls** (front and back of the print): the X axis is likely - the head moving left and right

This tells you which belt, pulley, and motor to focus on first.

---

## Fix 1: Reduce Print Speed

The most effective single change. Slower movement means direction changes with less force and much smaller vibration.

Reduce outer wall speed by 30-50%. You do not need to slow down the whole print - infill and inner walls can stay faster. Most slicers let you set outer wall speed separately from overall print speed.

If the ghosting disappears at lower speed, speed is confirmed as the cause. You can then work on the other fixes to push speed back up without the artefacts returning.

---

## Fix 2: Reduce Acceleration and Jerk

Acceleration is how quickly the print head reaches its target speed. High acceleration means more force applied to the frame in a short time, which means more vibration.

I diagnosed ghosting on three Ender 3 machines at a school workshop that had all been updated to a high-speed community profile. The profile had set acceleration to 5000 mm/s² - well above what the frame could handle cleanly. Dropping to 1500 mm/s² on all three removed the ghosting entirely with no other changes.

- Reduce acceleration by 30-40% (e.g. from 3000 to 1800-2000 mm/s²)
- Reduce jerk from the default (often 10-20 mm/s) to around 5-8 mm/s

These settings can be changed in your slicer's machine settings or in the printer's firmware menu. Changes made in the slicer override firmware defaults for that print only.

---

## Fix 3: Check Belt Tension

Loose belts allow the print head to vibrate more freely after a direction change. A correctly tensioned belt dampens vibration faster and reduces the amplitude of the ripples.

Check both X and Y belts. Each should feel firm when pressed - not floppy, not under extreme tension. More than a few millimetres of deflection under light finger pressure means it needs tightening.

This is one of the most commonly overlooked causes on older machines. Belts stretch gradually over months of use, and the ghosting gets slowly worse. A machine that printed cleanly when new and now shows ringing has often just loosened over time.

---

## Fix 4: Check for Frame Wobble

A rigid frame is essential at higher speeds. On Cartesian printers (Ender 3 and similar), the X-axis gantry can wobble if eccentric nuts or V-slot wheels are worn or not correctly adjusted.

With the printer off, try to physically move the print head or gantry by hand. There should be essentially no give. If you can feel movement, tighten the eccentric nuts on the carriage wheels until the play disappears - but not so tight the carriage moves stiffly.

On CoreXY printers, check that all frame screws are tight and that the printer is sitting on a flat, stable surface. A printer on an uneven bench vibrates more than the same printer on a solid level surface.

---

## Fix 5: Input Shaper (Klipper Printers)

If your printer runs Klipper firmware, input shaper is by far the most effective fix for ghosting at speed. It measures the printer's resonant frequencies using an accelerometer and applies corrections digitally during printing - the ringing is cancelled out rather than reduced.

Printers like the Bambu range use a version of this by default, which is part of why they can print fast with clean surfaces. Setting up input shaper on Klipper takes an hour or two but the result is significant - speeds that previously caused obvious ghosting become printable with clean walls.

The Klipper documentation covers the full setup process. If you are on Klipper and getting ghosting, this is worth the time.

---

## Quick Checklist

1. Identify which axis - check which walls show ripples
2. Reduce outer wall speed by 30-50%
3. Reduce acceleration and jerk settings
4. Check and tighten both X and Y belts
5. Check for frame wobble - tighten eccentric nuts or carriage wheels
6. If running Klipper, configure input shaper

Steps 1 through 3 fix the majority of ghosting on standard printers. Steps 4 and 5 are worth checking regardless - loose belts and frame play often go unnoticed until a speed increase reveals them.
