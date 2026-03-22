# How to Fix Ghosting and Ringing in 3D Prints

Ghosting (also called ringing or vibration artefacts) shows up as wavy or ripple-like patterns on the surface of your print, most visible near sharp corners, text, or any sudden change in direction. The print is structurally fine - it is a surface quality issue, but it makes prints look rough and can obscure fine detail.

It is especially noticeable on faster printers and on prints with a lot of sharp features.

---

## What Does Ghosting Look Like?

Ghosting appears as horizontal ripples or waves on the outer surface of a print. They are most obvious:
- Just after a sharp corner (the vibration "echoes" along the wall)
- On text or lettering on vertical surfaces
- On any flat vertical face near a sharp edge

It is caused by the printer frame vibrating when the print head changes direction quickly. The head (or bed) overshoots, bounces back, and the nozzle lays down slightly incorrect lines for a few millimetres until the vibration dampens out.

---

## Fix 1: Reduce Print Speed

This is the most effective single change. Slower movement means the print head changes direction with less force, and the vibration is much smaller.

Try reducing your outer wall (perimeter) speed by 30-50%. You do not need to slow down the whole print - infill and inner walls can stay faster. Most slicers let you set outer wall speed separately.

If the ghosting disappears at lower speed, you have confirmed that speed is the cause. You can then work on other fixes to allow faster printing without the artefacts.

See the [speed vs quality guide](/posts/3d-printing-speed-vs-quality-guide/) for help setting sensible speed profiles.

---

## Fix 2: Reduce Acceleration and Jerk

Acceleration is how quickly the print head reaches its target speed. Jerk (or junction deviation in some firmware) is how the printer handles the instant direction change at a corner. High values in either setting mean more force is applied to the frame in a short time, which causes more vibration.

**What to try:**
- Reduce acceleration by 30-40% (e.g. from 3000 mm/s2 to 1800-2000 mm/s2)
- Reduce jerk from the default (often 10-20 mm/s) to around 5-8 mm/s

These settings can often be changed in your slicer (look for printer acceleration settings or machine settings) or in the printer's firmware menu. Changes made in the slicer override firmware defaults for that print only.

---

## Fix 3: Check Belt Tension

Loose belts allow the print head to vibrate more freely after a direction change. A tight, correctly tensioned belt dampens vibration faster.

Check both X and Y belts. Each should feel firm when pressed - not floppy, not so tight it is under extreme tension. If a belt deflects more than a few millimetres under light finger pressure, tighten it using the built-in tensioner or by adjusting the belt clips.

This is one of the most commonly overlooked causes. It is worth checking even if your belts do not feel obviously loose.

---

## Fix 4: Check for Frame Wobble

If your printer's frame is not rigid, vibration will be worse regardless of your settings. On cartesian printers (like the Ender 3 series), the X-axis frame can sometimes wobble if the eccentric nuts or V-slot wheels are worn or not correctly adjusted.

**How to check:** With the printer off, try to physically wobble the print head or gantry by hand. There should be essentially no give. If you can feel movement, tighten the eccentric nuts on the carriage wheels until the play disappears (but not so tight the carriage moves stiffly).

On CoreXY printers, check that the frame screws are all tight and that the printer is sitting on a flat, stable surface.

---

## Fix 5: Input Shaper (Klipper Printers Only)

If your printer runs Klipper firmware, input shaper (also called resonance compensation) is by far the most effective fix. It measures the resonant frequencies of your printer using an accelerometer and then cancels out vibrations digitally.

The result is dramatically reduced ghosting at high speeds - printers like the Bambu Lab range use a version of this by default, which is part of why they can print fast without obvious ringing.

Setting up input shaper is beyond the scope of this article, but if you run Klipper it is worth the hour it takes to configure. The Klipper documentation covers the full process.

---

## Which Direction Are the Ripples?

- **Ripples on the X-facing walls** (left and right sides of the print): the Y axis is the likely culprit (the bed or gantry moving front and back)
- **Ripples on the Y-facing walls** (front and back of the print): the X axis is the likely culprit

This tells you which belt, motor, and axis to focus your attention on first.

---

## Quick Checklist

1. Reduce outer wall print speed by 30-50%
2. Reduce acceleration and jerk settings
3. Check and tighten both X and Y belts
4. Check for frame wobble - tighten eccentric nuts or carriage wheels
5. If running Klipper, configure input shaper

---

## Related Guides

- [Speed vs Quality Guide](/posts/3d-printing-speed-vs-quality-guide/) - the right speed settings for your printer and goals
- [How to Fix Layer Shifting](/posts/how-to-fix-layer-shifting/) - another problem caused by loose belts and high acceleration
- [Best 3D Printer Upgrades Under $50](/posts/best-3d-printer-upgrades-under-50/) - belt tensioners and other quality-of-life upgrades
