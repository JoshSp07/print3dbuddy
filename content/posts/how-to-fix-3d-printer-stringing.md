# How to Fix 3D Printer Stringing: What Actually Works

Stringing is one of those problems people overcomplicate. They spend an hour tweaking retraction when the real fix was dropping the temperature by 10 degrees. This guide cuts straight to what actually matters.

---

## What Stringing Actually Is

Stringing happens when molten filament leaks from the nozzle during travel moves - the non-printing movements between parts of your model. The nozzle crosses open air, leaves a thin thread behind, and you end up with what looks like a spider web across your print.

The root cause is almost always one of three things: too much heat, not enough retraction, or slow travel speed. In that order of likelihood.

---

## Start Here: Temperature

Before touching retraction, drop your nozzle temperature by 5-10 degrees and run a test print.

Most people print PLA at 210-215 degrees out of habit. That is often higher than necessary. At 200-205 degrees the filament is less liquid, oozes less between moves, and strings significantly less. It is the lowest-effort fix and works more often than people expect.

PETG is the exception. It needs higher temperatures to print well, which means it strings more. With PETG, temperature is still the first variable to tune - but you are looking for the lowest temperature that still gives you good layer adhesion, not just the lowest temperature full stop. Start at 230 degrees and only go higher if you see poor bonding.

**PLA:** try 200-210 before going higher  
**PETG:** 230-240, tune down from there  
**ABS:** 235-245, stringing is less common with ABS

---

## Retraction: The Settings That Matter

Retraction pulls filament back into the nozzle before a travel move to release the pressure. Get it wrong in either direction and you have problems - too little and it strings, too much and you get clogs or under-extrusion.

**Starting points by extruder type:**

| Extruder Type | Retraction Distance | Retraction Speed |
|---|---|---|
| Direct drive | 0.5 - 1.5mm | 25 - 45mm/s |
| Bowden | 4 - 6mm | 40 - 60mm/s |

Direct drive setups need far less retraction than Bowden because there is no tube between the gear and the nozzle. If you are on a direct drive printer and stringing persists past 2mm retraction, retraction is not the issue - go back to temperature.

On Bowden printers, 6-7mm is a common sweet spot. Going above 8mm rarely helps and increases the chance of the filament pulling out of the hotend entirely.

Increase in 0.5mm increments and test each time. The [retraction test print](https://tools.print3dbuddy.com/test-prints#retraction-test) at tools.print3dbuddy.com makes this quick - seven towers, results visible in 15 minutes.

---

## The Setting Most People Miss: Combing

Every major slicer has a setting that routes travel moves over already-printed areas rather than crossing open gaps. In Cura it is called Combing Mode. In PrusaSlicer and Bambu Studio it is called Avoid Crossing Perimeters.

Enable it. It does not affect print quality at all and it dramatically reduces stringing on detailed models by eliminating open-air travel moves entirely.

- **Cura:** Combing Mode - set to "All" or "Not in Skin"  
- **PrusaSlicer / Bambu Studio:** Avoid crossing perimeters - enable

This is the most underused anti-stringing setting. Most people go straight to retraction without enabling this first.

---

## Travel Speed

Faster travel means less time for filament to drip. Most printers handle 150-200mm/s for travel moves without any issues since no plastic is being deposited.

If your travel speed is set to 80-100mm/s, raise it to 150mm/s minimum. This is a quick win.

---

## If You Have Still Not Fixed It

At this point the issue is usually one of these:

**Wet filament** - moisture-affected filament strings badly regardless of settings. If you hear crackling or popping while printing, dry the spool before doing anything else. See the [wet filament guide](/posts/how-to-fix-wet-filament/).

**Worn or partial-clog nozzle** - inconsistent flow causes inconsistent pressure, which causes inconsistent stringing. If this printer has had a lot of use, try a fresh nozzle. They are cheap.

**Extruder calibration** - if your e-steps are off and you are over-extruding, you are starting every travel move with more pressure than you need. Calibrate your extruder first, then revisit stringing.

---

## Quick Reference

| Setting | Bowden | Direct Drive |
|---|---|---|
| Retraction distance | 4 - 6mm | 0.5 - 1.5mm |
| Retraction speed | 40 - 60mm/s | 25 - 45mm/s |
| Print temperature | Lower by 5-10 degrees | Lower by 5-10 degrees |
| Travel speed | 150mm/s minimum | 150mm/s minimum |
| Combing / avoid crossing | Enable | Enable |

Work through temperature first, then combing, then retraction. That order solves the problem faster than going straight for retraction settings.
