# 3D Printing Speed vs Quality: How to Find the Right Balance

Modern printers advertise 500mm/s or even 700mm/s. Your first instinct might be to print as fast as possible  -  but blindly cranking up speed creates a mess of artefacts, weak parts, and failed prints.

This guide explains what speed actually does, what limits it, and how to dial in the right settings for your specific goal.

---

## Why Speed and Quality Trade Off

Faster printing introduces several problems:

**1. Under-extrusion at speed**
Your extruder can only push filament so fast. Exceed the flow rate limit and you get gaps, weak layer adhesion, and poor surface finish.

**2. Ringing (ghosting)**
The rapid direction changes at high speed create vibrations in the frame. These show up as wavy artefacts on the surface  -  especially visible near sharp corners.

**3. Corner rounding**
At high speed, the print head can't change direction instantaneously. Corners get slightly rounded as the head overshoots.

**4. Layer adhesion issues**
Less time at the deposition point = less heat transferred = weaker bonds between layers.

The good news: modern firmware features (input shaping, pressure advance) dramatically reduce these problems.

---

## The Key Speed Settings

### Print Speed
The overall speed the print head moves while depositing filament. The headline number.

### Travel Speed
Speed when moving between points *without* depositing filament. Can be much higher  -  150-300mm/s is common even on slower printers. Travel speed doesn't affect print quality directly.

### Perimeter / Wall Speed
Speed for the outer walls. This is what you actually see  -  keep it slower for better surface quality. Many slicers default outer walls to 50-60% of the overall print speed.

### Infill Speed
Speed for internal fill patterns. Infill quality matters less than walls, so infill can run faster. 80-100% of print speed is typical.

### First Layer Speed
Always slow this down  -  20-30mm/s regardless of your overall speed. A good first layer is the foundation of the whole print.

### Bridge Speed
Bridging (printing in air across a gap) needs a specific speed: fast enough that the filament pulls taut, slow enough to not sag. 40-60mm/s is a common starting point.

---

## What Actually Limits Your Speed

### 1. Maximum Volumetric Flow Rate
Every hotend has a maximum rate at which it can melt and push filament  -  measured in mm³/s. Exceed it and you get under-extrusion.

Typical limits:
| Hotend Type | Approx. Max Flow |
|---|---|
| Standard brass nozzle | 10-15 mm³/s |
| High-flow hotend (e.g. Bambu) | 30-35 mm³/s |
| Volcano / CHT nozzle | 20-25 mm³/s |

At 0.2mm layer height with a 0.4mm nozzle, 20mm³/s = roughly 250mm/s print speed. Above that you're under-extruding.

### 2. Printer Rigidity
A wobbly frame vibrates more at speed, creating ringing. CoreXY printers (Bambu, Voron, etc.) are inherently more rigid and faster than bed-slinger designs (Ender 3, etc.) because only the toolhead moves.

### 3. Input Shaping / Resonance Compensation
Klipper firmware and Bambu printers support input shaping  -  the printer measures its own resonant frequencies and cancels them out. This allows much higher speeds without ringing.

Without input shaping: practical speed limit around 100-150mm/s for good quality.
With input shaping: practical limit around 300-400mm/s on a rigid printer.

### 4. Pressure Advance / Linear Advance
Controls how the extruder reacts to speed changes  -  prevents blobs at corners and gaps on outlines. Enabled in Klipper (pressure advance) and Marlin (linear advance). Bambu handles this automatically.

---

## Speed Profiles for Different Goals

### High Quality (Figurines, display pieces, visible exterior parts)
- **Print speed:** 40-60mm/s
- **Outer wall speed:** 30-40mm/s
- **Layer height:** 0.12-0.15mm
- **Cooling:** Maximum for PLA

Slow down the outer walls and reduce layer height. The rest can be faster.

### Balanced (Most everyday prints)
- **Print speed:** 80-120mm/s
- **Outer wall speed:** 50-70mm/s
- **Layer height:** 0.2mm
- **Cooling:** Standard

The default starting point for most prints. Good results, reasonable time.

### Fast/Functional (Internal parts, test fits, time-sensitive prints)
- **Print speed:** 150-250mm/s (hardware depending)
- **Outer wall speed:** 100-150mm/s
- **Layer height:** 0.25-0.3mm
- **Cooling:** Adequate

Accept some surface quality reduction in exchange for speed. Fine for parts that aren't visible.

### Maximum Speed (Possible on CoreXY with input shaping)
- **Print speed:** 300-500mm/s
- **Outer wall speed:** 150-250mm/s
- **Layer height:** 0.2-0.25mm
- Requires: input shaping, pressure advance, high-flow hotend, rigid frame

Only relevant if you have a Bambu Lab printer, a Voron, or a heavily modified Klipper setup.

---

## Practical Tips

**Tune flow rate first.** Before increasing speed, make sure your extrusion multiplier is correct. Print a single-wall cube and measure the wall thickness  -  adjust until it matches your target.

**Lower outer wall speed, raise infill speed.** The outer walls are what you see. Keep those slow. Infill is invisible  -  run it fast.

**Enable acceleration limits.** High speed with aggressive acceleration is worse than moderate speed with smooth acceleration. In PrusaSlicer, check your acceleration settings.

**Don't compare to Bambu benchmarks without their hardware.** A Bambu A1 doing 500mm/s on Bambu hardware ≠ your Ender 3 doing 500mm/s. The hardware is fundamentally different.

**Increase speed gradually.** Add 20mm/s at a time, run a test, check quality. Don't jump from 60 to 200 and wonder why it's bad.

---

## Useful Test Prints

- **Benchy** (3DBenchy)  -  the standard quality benchmark. Prints in 15-20 minutes at normal speed. Check for ringing on the hull, stringing in the cabin, overhangs under the roof.
- **Cali dragon**  -  popular speed/quality benchmark on Printables
- **Single-wall cube**  -  for calibrating extrusion multiplier
- **Ringing tower**  -  specifically tests for ghosting at different speeds

---

## Summary

High speed is a bonus, not a requirement. For most home printing, 60-100mm/s with a 0.2mm layer height produces excellent results on any printer.

If you want to go faster: check your volumetric flow rate limit, enable input shaping if possible, and reduce outer wall speed even when increasing infill speed.

The best speed is the fastest you can go before quality visibly degrades  -  find that point through testing, not through benchmark marketing.
