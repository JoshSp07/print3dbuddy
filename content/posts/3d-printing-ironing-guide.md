# 3D Printing Ironing: How to Get Glass-Smooth Top Surfaces

If you've ever looked at a finished print and thought the top surface looks rough and lined compared to the sides  -  ironing fixes that. It's a post-processing pass the slicer adds after the final top layer, and when it's set up correctly, it turns a textured surface into something that looks almost injection-moulded.

It's one of those features that sounds fiddly but takes about two minutes to set up, and the results speak for themselves.

---

## What Is Ironing?

Ironing is an extra pass the printhead makes over the top surface after it finishes the final layer. The nozzle moves slowly back and forth across the surface, either extruding a very small amount of filament or nothing at all, remelting and smoothing the top layer as it goes.

The effect: instead of parallel ridged lines from the last top layer, you get a flat, smooth, slightly glossy surface.

---

## When Ironing Is Worth Using

Ironing works best on:
- Flat horizontal top surfaces
- Decorative prints where appearance matters
- Prints with large exposed top areas (coasters, plaques, cases, tiles)
- Models where a clean surface finish is part of the design

It's less useful on:
- Curved top surfaces (the nozzle can't follow complex curves cleanly)
- Functional prints where you don't care about aesthetics
- Very small flat areas (the ironing pass is short and makes little difference)

---

## How to Enable Ironing in Your Slicer

### OrcaSlicer / BambuStudio
Quality settings > Ironing > Enable ironing. Set to "Top surfaces only" to start.

### PrusaSlicer
Print settings > Infill > Ironing > Enable ironing.

### Cura
Search "ironing" in settings (make sure All settings are shown). Enable "Iron top surface".

---

## Ironing Settings Explained

### Ironing Flow Rate
The percentage of normal extrusion used during the ironing pass. Lower flow means the nozzle is mostly just remelting existing plastic rather than adding new material.

- Too low: the surface still looks textured, not enough heat transfer
- Too high: you're depositing extra plastic, causing raised lines or blobbing
- **Typical starting point: 10-15% for PLA, 15-20% for PETG**

### Ironing Speed
How fast the nozzle moves during the ironing pass. Slower means more time for heat to transfer and flatten the surface.

- **Typical starting point: 50% of your normal print speed**
- If results are inconsistent, slow it down further

### Ironing Line Spacing
How far apart the ironing passes are. Wider spacing is faster but leaves more texture. Tighter spacing is slower but smoother.

- **Typical starting point: 0.1-0.15mm** (most slicers default to around 0.1mm)

### Ironing Pattern
Most slicers offer concentric or linear options. Linear (back and forth) is the most common and works well for most shapes. Concentric follows the outer edge of the surface inward, which can look good on circular parts.

---

## Finding Your Ideal Settings

The best way is to print all four settings side by side using the [Ironing Test at tools.print3dbuddy.com](https://tools.print3dbuddy.com/test-prints). It prints four flat tiles  -  one with no ironing as a baseline, then 10%, 15%, and 20% flow  -  so you can see the difference directly.

Otherwise, start at 15% flow and 50% speed, run a quick test tile, and adjust from there.

---

## Common Ironing Problems and Fixes

**Still looks rough after ironing**
- Flow too low  -  increase by 5%
- Speed too fast  -  reduce to 40% of print speed
- Nozzle temp too low  -  try adding 5-10°C for the ironing layer

**Visible ridges or raised lines on the surface**
- Flow too high  -  reduce by 5%
- Line spacing too wide  -  tighten to 0.08-0.10mm

**Blobs or zits on the ironed surface**
- Retraction not triggering during ironing passes  -  check slicer settings
- Filament moisture  -  dry your filament before printing

**Ironing takes forever**
- Normal  -  ironing adds 20-40% to print time on large flat surfaces
- Reduce to "top surfaces only" if you have it set to all layers
- Increase line spacing slightly (0.15mm instead of 0.10mm)

---

## Does Ironing Work With All Filaments?

- **PLA:** Works extremely well. Most consistent results.
- **PETG:** Works well but needs slightly higher flow and is more prone to stringing during the pass. Make sure your retraction is dialled in.
- **ABS/ASA:** Works, but the surface tends to have more variation. Enclosure helps.
- **TPU:** Not useful  -  soft surfaces don't respond to ironing in a meaningful way.

---

## Is Ironing Worth It?

For decorative prints, yes. The difference between an ironed and unironed flat top is immediately visible and gives prints a much more finished look.

For functional prints, it's usually not worth the time. A bracket or a tool holder doesn't need a polished top face.

The one thing to be aware of: ironing adds print time, sometimes significantly on large flat areas. Run it on the prints where it counts.

---

## Try It Yourself

The [Ironing Test at tools.print3dbuddy.com](https://tools.print3dbuddy.com/test-prints) gives you all 4 tiles in one STL  -  no ironing, 10%, 15%, and 20% flow. Print them all at once, compare the tops, and you'll have your ideal setting in under 30 minutes.
