# Nylon 3D Printing Guide: Settings, Tips, and Common Problems

Nylon is one of the most capable FDM filaments available - strong, flexible, abrasion-resistant, and genuinely useful for functional parts. It is also one of the harder materials to print reliably. This guide covers everything you need to get good Nylon prints consistently.

---

## Why Print in Nylon?

Nylon makes sense when you need:

- **Strength and flexibility together** - Nylon bends without snapping, unlike PLA or ABS
- **Abrasion resistance** - gears, bushings, and wear parts last much longer in Nylon than other materials
- **Heat resistance** - Nylon holds its shape up to around 80 - 120°C depending on the type, well above PLA's limit
- **Impact resistance** - parts that take repeated knocks or stress

Common applications include mechanical components, clips, hinges, cable ties, and any part that needs to flex repeatedly without breaking.

If your part does not need these properties, PLA or PETG are easier to work with. But if you need a tough functional part, Nylon is hard to beat.

---

## Types of Nylon Filament

**Nylon 6 (PA6):** The most widely used type. Good all-round properties, moderate price. Hygroscopic - absorbs moisture aggressively.

**Nylon 12 (PA12):** More flexible than PA6, lower moisture absorption, slightly easier to print. More expensive.

**Nylon + Carbon Fibre (PA-CF):** Stiff, very strong, lightweight. Requires a hardened steel nozzle - carbon fibre eats through brass nozzles quickly. See the [complete nozzle guide](/posts/complete-nozzle-guide-3d-printing/) for hardened steel options.

**Nylon + Glass Fibre (PA-GF):** Similar to CF but less stiff, lower weight gain. Also requires a hardened nozzle.

For most people starting with Nylon, standard PA6 from a reputable brand is the right starting point. [Prusament Nylon](https://www.amazon.co.uk/s?k=prusament+nylon+filament&tag=print3dbuddy2-21) and [Polymaker PA6](https://www.amazon.co.uk/s?k=polymaker+nylon+filament+PA6&tag=print3dbuddy2-21) are well-regarded options.

---

## What You Need Before You Start

### An Enclosure

Nylon warps badly in open-air printing environments. An enclosure traps heat and keeps the print chamber temperature stable, which dramatically reduces warping and layer splitting. You do not need an expensive dedicated enclosure - a [simple snap-together enclosure](https://www.amazon.co.uk/s?k=3d+printer+enclosure&tag=print3dbuddy2-21) works fine.

See [best 3D printer enclosures](/posts/best-3d-printer-enclosures/) for options at different price points.

### Dry Filament

Nylon is extremely hygroscopic - it absorbs moisture from the air faster than almost any other common filament. Wet Nylon prints poorly: rough surfaces, weak layers, bubbling, and inconsistent extrusion. Always dry Nylon before printing, even if the roll is freshly opened.

Dry at 70 - 80°C for 6 - 12 hours in a [filament dryer](https://www.amazon.co.uk/s?k=filament+dryer+box+3d+printing&tag=print3dbuddy2-21) or food dehydrator. Store in a sealed container with desiccant when not in use. See the [wet filament guide](/posts/how-to-fix-wet-filament/) for more on drying and storage.

### A Suitable Build Surface

Nylon adhesion is famously difficult. It does not stick reliably to glass, PEI, or bare metal without help. The best options:

- **PEI with glue stick** - apply a thin coat of Pritt Stick to the PEI sheet before printing
- **Garolite (G10)** - the best dedicated surface for Nylon, bonds extremely well
- **Glass with hairspray** - hairspray creates a tacky layer that Nylon grips

A heated bed at 70 - 90°C is required.

---

## Recommended Print Settings

| Setting | Range |
|---|---|
| Nozzle temperature | 240 - 270°C |
| Bed temperature | 70 - 90°C |
| Print speed | 30 - 50mm/s |
| Part cooling fan | 0 - 20% |
| Enclosure | Strongly recommended |
| Nozzle material | Hardened steel for CF/GF variants |

**Start conservative.** Print at 250°C nozzle, 80°C bed, 40mm/s with the fan off or at 10% and adjust from there. Nylon benefits from slow, hot printing with minimal cooling.

---

## Common Problems and Fixes

### Warping and Lifting Corners

The most common Nylon problem. Nylon shrinks as it cools, and without containment the edges of the print lift off the bed.

**Fix:**
- Use an enclosure - this is the single biggest factor
- Apply glue stick or hairspray to your build surface
- Add a brim (5 - 10mm) to anchor the edges
- Raise bed temperature to 85 - 90°C
- Reduce part cooling fan to 0 - 10%
- Slow first layer speed to 20mm/s

### Layer Splitting or Delamination

Nylon layers that are not hot enough or cool too fast will not bond properly, leaving weak, separating layers.

**Fix:**
- Increase nozzle temperature by 5 - 10°C
- Reduce or eliminate part cooling fan
- Use an enclosure to keep the chamber warm
- Slow print speed

### Rough, Foamy Surface

Almost always wet filament. Nylon that has absorbed moisture will crackle, foam, and produce rough, inconsistent surfaces.

**Fix:** Dry the filament at 70 - 80°C for at least 8 hours. If you can hear popping or crackling from the nozzle during printing, stop and dry the filament before continuing.

### Stringing

Nylon strings more than PLA. Retraction settings help, but do not over-retract as this can cause jams.

**Fix:**
- Direct drive: 1 - 2mm retraction at 40mm/s
- Bowden: 5 - 7mm retraction
- Increase travel speed to 150mm/s+
- Enable combing in your slicer

Use the [retraction calculator](https://tools.print3dbuddy.com/retraction-calculator) to get a sensible starting point.

---

## Part Design Tips for Nylon

Nylon's flexibility is a feature, but it changes how you should design parts:

- **Avoid very thin walls** - Nylon flex can cause thin features to distort under load rather than breaking cleanly
- **Increase infill** - 40 - 60% infill for structural parts (higher than you would use for PLA)
- **Rectilinear or gyroid infill** - distributes stress well for flexible materials
- **Chamfer instead of fillet** - internal corners with chamfers print cleaner and are less likely to crack under stress

---

## Is Nylon Right for Your Printer?

Not every printer can handle Nylon reliably. You need:

- A hotend capable of 250°C+ (most modern printers manage this)
- A heated bed (essential)
- An enclosure or at least the ability to make one
- A PTFE-free hotend for extended printing above 240°C - standard PTFE-lined hotends can off-gas at these temperatures. All-metal hotends (like the Revo series) are the safer choice for regular Nylon printing

The [Bambu Lab P1S](https://www.amazon.co.uk/s?k=Bambu+Lab+P1S&tag=print3dbuddy2-21) comes with a built-in enclosure and AMS system that makes Nylon printing straightforward. The [Prusa MK4](https://www.amazon.co.uk/s?k=Prusa+MK4&tag=print3dbuddy2-21) handles Nylon well with an enclosure added. Budget printers like the Ender 3 series can print Nylon but require more setup and an aftermarket enclosure.

---

## Related Guides

- [ABS and ASA Printing Guide](/posts/abs-asa-printing-guide/) - other engineering materials with similar setup requirements
- [How to Fix Wet Filament](/posts/how-to-fix-wet-filament/) - drying and storage for moisture-sensitive filaments
- [Complete Nozzle Guide](/posts/complete-nozzle-guide-3d-printing/) - hardened steel nozzles for abrasive filaments
- [Best 3D Printer Enclosures](/posts/best-3d-printer-enclosures/) - what to look for and top picks
- [PLA vs PETG vs ABS - Which Filament?](/posts/pla-vs-petg-vs-abs-which-filament-for-beginners/) - choosing the right material for your project
