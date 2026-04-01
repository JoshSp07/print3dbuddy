# Input Shaper and Resonance Compensation: A Practical Guide

Ghosting and ringing - the faint echoes and ripples that appear on vertical surfaces after a sharp corner - are caused by vibration in the printer frame. Input shaper (also called resonance compensation) measures those vibrations and filters them out in the motion system. This guide explains what it is, how to set it up, and what to expect.

---

## What Is Input Shaper?

When a print head changes direction quickly, the frame vibrates slightly from the sudden force. Those vibrations travel through the print head and leave visible artefacts on the print surface - wavy lines parallel to corners, faint echoes of features, or a general soft look on what should be sharp edges.

Input shaper works by measuring the natural resonant frequency of your printer's X and Y axes, then actively counteracting vibrations at those frequencies in the motion planning. The result is sharper corners, cleaner surfaces, and the ability to print faster without artefacts appearing.

Input shaper is a firmware feature, available on:
- **Klipper firmware** (any printer running Klipper)
- **Bambu Lab printers** (all current models, called "vibration compensation")
- **Prusa printers** (MK4, XL, Mini via built-in calibration)
- **Some Marlin-based printers** (limited implementation, not as effective)

If your printer runs stock Creality firmware, input shaper is not available without a firmware change or upgrade to Klipper.

---

## Before You Start: Check the Basics

Input shaper fixes vibration-caused artefacts. It will not fix:

- Loose belts (fix belt tension first - see the [belt tensioning guide](/posts/how-to-tension-3d-printer-belts/))
- Loose frame screws or pulley grub screws
- Z-axis wobble
- Layer shifting

If you have ghosting or ringing, check and tighten belts before anything else. Input shaper on top of loose belts will not fully resolve the problem.

---

## Setting Up Input Shaper on Klipper

Klipper's input shaper is the most powerful and widely used implementation. There are two ways to measure resonant frequencies: with an accelerometer, or manually.

### Method 1: With an ADXL345 Accelerometer (Recommended)

This is the accurate method. An [ADXL345 accelerometer module](https://www.amazon.co.uk/s?k=ADXL345+accelerometer+module&tag=print3dbuddy2-21) mounts to the print head and measures actual vibration frequencies while the printer runs a test pattern.

**Setup steps:**
1. Wire the ADXL345 to your Klipper host (Raspberry Pi or similar) via SPI
2. Add the ADXL345 config section to your printer.cfg (Klipper documentation has the exact wiring and config)
3. Home the printer and run `TEST_RESONANCES AXIS=X` then `TEST_RESONANCES AXIS=Y`
4. Klipper generates resonance graphs showing the peak frequencies
5. Run `SHAPER_CALIBRATE` to automatically pick the best shaper type and frequency
6. Save the config with `SAVE_CONFIG`

The whole process takes about 20 minutes once the accelerometer is wired. The result is precise, automatic calibration rather than a manual guess.

### Method 2: Manual Tuning (No Accelerometer)

If you do not have an accelerometer, you can tune input shaper manually by printing ringing test models and adjusting settings by eye.

1. In printer.cfg, add or uncomment the `[input_shaper]` section
2. Set `shaper_type: mzv` as a starting point (MZV is a good general-purpose shaper)
3. Set `shaper_freq_x` and `shaper_freq_y` to an initial estimate (typically 30 - 60Hz for most printers)
4. Print a ringing calibration tower (available free on Printables)
5. Identify the layer height where ringing disappears and read off the corresponding frequency
6. Update your config with that frequency and save

Manual tuning takes longer and is less precise than accelerometer calibration, but it works and costs nothing extra.

---

## Setting Up Resonance Compensation on Bambu Lab Printers

Bambu handles this automatically. The process is:

1. Open Bambu Studio or the printer touchscreen
2. Go to Calibration
3. Run "Vibration Compensation" (the printer moves through a test routine and calibrates itself)
4. The printer stores the result - no user intervention needed beyond starting the calibration

Re-run this calibration if you:
- Move the printer to a different location or surface
- Replace any motion components (belts, rails, carriages)
- Add significant weight to the printer (toolhead swaps, camera mounts, etc.)

---

## Setting Up on Prusa MK4 and Mini

Prusa's built-in input shaper calibration is accessible from the printer's menu:

1. Go to Settings > Calibration > Input Shaper
2. The printer runs its own test routine and sets resonance compensation automatically
3. The calibration is stored in the printer - no slicer changes needed

Re-run after belt replacements or significant printer moves.

---

## What to Expect After Calibration

After input shaper is calibrated and enabled:

**Print quality:** Ghosting and ringing on vertical surfaces should be significantly reduced or eliminated. Corners should be sharper and cleaner.

**Print speed:** Input shaper allows higher acceleration settings without introducing artefacts. You can often increase acceleration by 2 - 4x compared to pre-input-shaper settings while maintaining the same print quality. This means faster prints without quality loss.

**The trade-off:** Some input shaper algorithms (particularly EI and 2HUMP_EI) can slightly reduce maximum extrusion speed at high accelerations. MZV is the safest starting point - good vibration suppression with minimal speed impact.

---

## Recommended Shaper Types

| Shaper | Best For | Trade-off |
|---|---|---|
| MZV | Most printers, good all-rounder | Moderate vibration reduction |
| EI | Printers with higher resonance frequencies | Can limit max speed slightly |
| 2HUMP_EI | Printers with very broad resonance peaks | Reduces max speed more |
| ZV | Very simple, least reduction | Only for very rigid frames |

Start with MZV unless the automatic calibration recommends otherwise.

---

## Frequently Asked Questions

**Do I need to recalibrate if I change filament?** No. Input shaper is about the printer's mechanical properties, not the filament.

**Will input shaper fix layer shifting?** No. Layer shifting is caused by belts, grub screws, or overheating drivers - not vibration. Input shaper only addresses print surface artefacts.

**Can I run input shaper on an Ender 3 without Klipper?** Not effectively on stock firmware. You would need to install Klipper or a third-party firmware that supports it.

**Does input shaper wear out?** No, but calibration can drift if mechanical components change. Re-run calibration after any maintenance that affects the motion system.

---

## Related Guides

- [How to Fix Ghosting and Ringing](/posts/how-to-fix-ghosting-ringing/) - other causes of surface artefacts
- [How to Tension 3D Printer Belts](/posts/how-to-tension-3d-printer-belts/) - fix belt issues before calibrating input shaper
- [3D Printing Speed vs Quality Guide](/posts/3d-printing-speed-vs-quality-guide/) - using higher speeds after input shaper calibration
- [How to Calibrate Pressure Advance](/posts/how-to-calibrate-pressure-advance/) - the other major Klipper calibration for print quality
