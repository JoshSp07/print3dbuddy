# How to Calibrate Pressure Advance (and Linear Advance)

Pressure advance is one of the most effective calibrations you can run for print quality. It cleans up blobs at corners, fixes the slight over-extrusion at the start of lines, and allows you to print faster without losing quality. If you have noticed that corners on your prints look slightly blobby or rounded, or that line starts look fatter than they should, pressure advance is the fix.

Pressure advance is the Klipper firmware term. Marlin calls the same feature Linear Advance (LA). They work identically - this guide covers both.

---

## What Is Pressure Advance?

When your printer pushes filament into a hot nozzle, the filament is slightly compressible. As the extruder motor pushes, pressure builds up in the hotend before plastic actually comes out. When the extruder slows or stops (at a corner, for example), that built-up pressure continues to push plastic out after the motor has stopped.

The result: blobs and zits at corners, rounded sharp edges, and slightly inconsistent line widths.

Pressure advance compensates for this by pushing filament slightly ahead of where it is needed (to pre-load pressure) and pulling back slightly when decelerating (to release pressure before it oozes out).

---

## Do You Need This Calibration?

Pressure advance is most impactful if you are seeing:

- Blobs or bulges at corners
- Rounded sharp corners that should be crisp
- First millimetre of lines that are fatter than the rest
- Artefacts near direction changes that do not go away with speed or temperature changes

If your prints already look clean, your firmware may have a reasonable default set, or the issue may lie elsewhere.

---

## Klipper: Calibrating Pressure Advance

Klipper's built-in pressure advance tuning print is the fastest method.

**Step 1:** Add this to your printer.cfg if it is not already there:
```
[extruder]
pressure_advance: 0.0
```

**Step 2:** Run the tuning tower. In your Klipper console (Mainsail or Fluidd), run:
```
SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=1 ACCEL=500
TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.005
```

Then start a print of a simple hollow square or box shape.

**Step 3:** Examine the result. The pressure advance value increases as you go up the print. Find the height where corners look cleanest and lines look most consistent, then calculate the value:

Pressure advance = height of best layer x 0.005

**Step 4:** Set the value in printer.cfg:
```
[extruder]
pressure_advance: 0.04  # replace with your measured value
```

Typical values: 0.02-0.08 for direct drive, 0.4-0.8 for Bowden setups.

---

## Marlin: Calibrating Linear Advance

Marlin's Linear Advance uses K-factor instead of PA value, but the concept is the same.

**Step 1:** Check that Linear Advance is enabled in your firmware. Many Marlin builds ship with it disabled. If `M900` commands in the terminal give an error, LA is not compiled in and you need a custom firmware build.

**Step 2:** Use the Marlin LA calibration pattern generator at `marlinfw.org/tools/lin_advance/`. Configure your printer dimensions, generate the G-code, and print it.

**Step 3:** The print produces a series of lines at different K values. Find the K value where lines are most consistent in width. Set it with:
```
M900 K0.15  # replace with your measured value
M500        # save to EEPROM
```

Typical K values: 0.05-0.25 for direct drive, 1.0-2.0 for Bowden.

---

## Bambu Lab and Other Closed-Firmware Printers

Bambu Lab printers run their own closed firmware that includes pressure advance tuned by the manufacturer. You cannot manually set the PA value in the same way. If you are seeing corner blobs on a Bambu printer, the issue is more likely a flow rate calibration problem - run the built-in flow calibration from the printer menu.

---

## After Calibrating

Once pressure advance is set, you may find you can:

- Print slightly faster without the quality dropping
- Reduce retraction slightly (pressure advance handles some of what retraction was covering for)
- Get sharper corners without any other changes

Re-run this calibration if you change your extruder hardware, switch between direct drive and Bowden, or install a new hotend - the physical characteristics of the filament path have changed.

---

## Related Guides

- [How to Fix Over-Extrusion](/posts/how-to-fix-over-extrusion/) - blobs and corner issues that pressure advance alone may not fix
- [How to Fix Ghosting and Ringing](/posts/how-to-fix-ghosting-ringing/) - another corner-quality issue, different cause
- [How to Calibrate Your First 3D Printer](/posts/how-to-calibrate-your-first-3d-printer/) - full calibration sequence including E-steps and flow rate
- [How to Calibrate Flow Rate](/posts/how-to-calibrate-flow-rate-extrusion-multiplier/) - calibrate flow before pressure advance for best results
- [Speed vs Quality Guide](/posts/3d-printing-speed-vs-quality-guide/) - how to make use of the speed gains from pressure advance
