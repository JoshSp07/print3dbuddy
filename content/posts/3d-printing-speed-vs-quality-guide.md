# 3D Printing Speed vs Quality: How to Find the Right Balance

Modern printers advertise 500mm/s or higher. The marketing implies that faster is always better. In practice, printing at the maximum rated speed produces worse results on most machines, and the relationship between speed and quality is more nuanced than a single slider.

This guide covers what speed actually does, what limits it, and how to dial in the right settings for what you are trying to achieve.

---

## Why Speed and Quality Trade Off

**Under-extrusion at high speed.** Every hotend has a maximum rate at which it can melt and push filament. Exceed that rate and you get gaps, weak layer adhesion, and rough surface finish. This is volumetric flow limiting - the melt zone simply cannot keep up.

**Ringing (ghosting).** Rapid direction changes at high speed vibrate the frame. These vibrations show up as wavy artefacts on the surface near sharp corners and edges. The print is structurally fine but looks wrong.

**Corner rounding.** At high speed, the print head cannot change direction instantaneously. Corners get slightly rounded as the head overshoots.

**Weaker layer adhesion.** Less time at each deposition point means less heat transfer to the previous layer and weaker bonds.

Modern firmware features - input shaping and pressure advance - reduce some of these problems significantly, but do not eliminate them.

---

## The Speed Settings That Actually Matter

Most slicers break speed into several separate values, not one global setting. Understanding which is which matters more than the headline number.

**Print speed** - the overall speed while depositing filament. The number most people focus on.

**Outer wall speed** - speed for the outer perimeters. This is what you actually see. Keep it lower than everything else for better surface quality. Most slicers default outer walls to 50-60% of print speed.

**Inner wall / infill speed** - infill is invisible in the finished print. Run it faster. 80-100% of print speed is typical and costs nothing in visible quality.

**First layer speed** - always slow, regardless of everything else. 20-30mm/s. A failed first layer wastes the entire print.

**Travel speed** - movement without depositing filament. Can be much higher than print speed. 150-250mm/s is common and does not affect quality directly.

**Bridge speed** - printing in air across a gap needs a specific speed. Fast enough that the filament pulls taut, slow enough not to sag. 40-60mm/s is a common starting point.

---

## What Actually Limits Your Speed

### Volumetric Flow Rate

Every hotend has a maximum throughput in mm³/s. Exceed it and you under-extrude regardless of other settings.

| Hotend type | Approximate max flow |
|---|---|
| Standard brass nozzle | 10-15 mm³/s |
| High-flow hotend (Bambu, Rapido, etc.) | 30-35 mm³/s |
| Volcano / CHT nozzle | 20-25 mm³/s |

At 0.2mm layer height with a 0.4mm nozzle, 15mm³/s is roughly 190mm/s print speed. Above that, a standard hotend cannot keep up.

A company I worked with was running a set of printers for rapid prototyping and wanted to push speeds up significantly. The problem was they were on standard hotends. Cutting the layer height from 0.2mm to 0.15mm - which they assumed would be slower - actually let them increase speed without exceeding the flow rate limit, because each layer is thinner and requires less filament per second. Counter-intuitive but the maths works out.

### Printer Rigidity

A wobbly frame vibrates more at speed. CoreXY printers (Bambu, Voron, etc.) are inherently stiffer and faster than bed-slinger designs (Ender 3, etc.) because only the toolhead moves. A bed-slinger moving the whole bed in Y has more inertia and more flex in the system.

Asking an Ender 3 to print at 300mm/s because a Bambu A1 can print at 300mm/s is comparing two completely different mechanical systems.

### Input Shaping / Resonance Compensation

Klipper firmware and Bambu printers support input shaping - the printer measures its own resonant frequencies and applies corrections during printing. The effect is significant: without input shaping, practical quality limits on most printers are around 100-150mm/s. With input shaping on a rigid machine, 300-400mm/s becomes viable.

### Pressure Advance / Linear Advance

Controls how the extruder reacts to speed changes - prevents blobs at corners and gaps on outlines when the head decelerates and accelerates. Klipper calls it pressure advance. Marlin calls it linear advance. Bambu handles it automatically. Getting this right makes a noticeable difference at higher speeds.

---

## Speed Profiles for Different Goals

### High Quality (Figurines, display pieces, visible surfaces)

- Print speed: 40-60mm/s
- Outer wall speed: 30-40mm/s
- Layer height: 0.12-0.15mm
- Cooling: maximum for PLA

Slow the outer walls. Everything internal can run faster. The layer height reduction costs time but dramatically improves surface detail.

### Balanced (Most everyday prints)

- Print speed: 80-120mm/s
- Outer wall speed: 50-70mm/s
- Layer height: 0.2mm

The right default for most home printing. Good results, reasonable time.

### Fast / Functional (Test fits, internal parts, time-sensitive prints)

- Print speed: 150-250mm/s (hardware depending)
- Outer wall speed: 100-150mm/s
- Layer height: 0.25-0.3mm

Accept some surface quality reduction in exchange for speed. Fine for parts that are not visible or do not need fine detail.

### Maximum Speed (CoreXY with input shaping)

- Print speed: 300-500mm/s
- Outer wall speed: 150-250mm/s
- Requires: input shaping, pressure advance, high-flow hotend, rigid frame

Only relevant on a Bambu, Voron, or heavily modified Klipper setup. Not achievable on a standard bed-slinger regardless of settings.

---

## Practical Rules

**Calibrate extrusion first.** Before increasing speed, make sure your extrusion multiplier is correct. Print a single-wall box and measure the wall thickness. Speed problems compound extrusion problems.

**Outer walls slow, infill fast.** The outer walls are what you see. Keep those conservative. Infill is never visible - push it as fast as you can without quality problems.

**Increase gradually.** Add 20mm/s at a time, run a test, check quality. Jumping from 60 to 200 and wondering why it is bad makes the cause impossible to identify.

**Do not compare to manufacturer benchmarks.** A Bambu doing 500mm/s is not the same as your printer doing 500mm/s. The hardware, firmware, and frame design are fundamentally different.

---

The best speed is the fastest you can go before quality visibly degrades. Find that through testing. For most home printing on a standard printer, 60-100mm/s with a 0.2mm layer height produces excellent results - fast enough to be practical, slow enough to not fight the machine's limits.
