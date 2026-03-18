# TPU Flexible Filament: A Beginner's Guide

TPU (Thermoplastic Polyurethane) is the material that makes 3D printing genuinely useful for a whole category of things other plastics can't touch - phone cases, gaskets, wheels, grips, wearables, and anything that needs to flex or absorb impact.

It's also one of the trickier filaments to print well. Here's everything you need to know.

---

## What Is TPU?

TPU is a flexible, rubber-like plastic. It ranges from very soft and stretchy (Shore 85A - similar to a rubber band) to relatively firm and only slightly flexible (Shore 98A - similar to a hard rubber sole).

For beginners, **95A hardness** is the sweet spot - flexible enough for most applications, firm enough to print reliably.

**Popular TPU filaments:**
- [eSUN TPU 95A](https://www.amazon.com/s?k=eSUN+TPU+95A+filament+1.75mm) - consistent, affordable, widely available
- [Polymaker PolyFlex TPU95](https://www.amazon.com/s?k=Polymaker+PolyFlex+TPU95) - excellent quality, slightly easier to print
- [SainSmart TPU](https://www.amazon.com/s?k=SainSmart+TPU+filament+flexible) - budget option, good results

---

## TPU Print Settings

| Setting | Recommended Value |
|---|---|
| Nozzle temperature | 220-235°C |
| Bed temperature | 30-60°C |
| Print speed | 20-30mm/s |
| Retraction | 0-2mm (direct drive) / Minimal (Bowden) |
| Cooling | Moderate (30-50%) |
| Infill | 20-40% for flexibility, 60%+ for rigidity |

**Slow down.** TPU does not respond well to speed. 25mm/s is a safe starting point - you can push to 40mm/s once you understand how your printer handles it, but anything faster risks bunching and jams.

---

## Direct Drive vs Bowden: This Actually Matters for TPU

This is the most important thing to know about printing TPU:

**Direct drive printers** (extruder motor on the toolhead) handle TPU well. The short, direct path from extruder to nozzle gives the flexible filament no room to buckle or bunch.

**Bowden printers** (motor on the frame, long PTFE tube to hotend) struggle badly with TPU. The flexible filament compresses and buckles in the long tube, causing massive under-extrusion, jams, and inconsistent flow.

If you have a Bowden printer like an older Ender 3 (non-SE/V3), TPU is possible but frustrating. Slow way down (15-20mm/s) and reduce retraction to near zero.

If you have a direct drive printer (Ender 3 V3 SE, Bambu Lab, Prusa MK4, etc.), TPU prints reasonably well with the settings above.

---

## Retraction Settings for TPU

This trips up most beginners.

Too much retraction with flexible filament causes the extruder to grind against the soft material or cause the filament to buckle in the drive path.

**Direct drive:** Start with 0-2mm retraction at slow speed (20mm/s). Many TPU prints work better with retraction off entirely.

**Bowden:** Retraction should be 0-1mm maximum, or disabled. Counter-intuitive, but less retraction usually means fewer jams with TPU.

---

## Why TPU Jams (and How to Avoid It)

The most common TPU problem is the filament bunching up between the extruder gear and the hotend entry. This happens because:

1. **Speed too high** - TPU can't keep up and buckles
2. **Too much retraction** - pulls the soft filament back into the extruder mechanism where it jams
3. **Bowden tube gap** - any gap between the PTFE tube and nozzle gives TPU room to bunch

Prevention:
- Slow print speed (25mm/s)
- Minimal or no retraction
- Make sure your PTFE tube seats fully against the nozzle
- Use a [Capricorn PTFE tube](https://www.amazon.com/s?k=Capricorn+PTFE+tube+1.75mm) with its tighter 1.9mm inner diameter

---

## Bed Adhesion for TPU

TPU sticks well to most surfaces - sometimes too well.

- **PEI textured sheet** - excellent adhesion, but parts can be hard to remove. Let the bed cool fully before removal.
- **Glass with glue stick** - good adhesion and easier removal
- **Blue painter's tape** - works well, parts release easily

If parts stick too aggressively to your PEI sheet, try a thin layer of hairspray or glue stick on top of it as a release agent.

---

## Useful Things to Print in TPU

TPU really shines for functional, everyday items:

- **Phone cases** - custom-fitted, shock-absorbing
- **Cable ties and clips** - flexible and reusable
- **Gaskets and seals** - custom shapes for enclosures and projects
- **Wheels and tyres** for RC cars and robots
- **Grips and handles** - tool handles, jar openers
- **Watch straps** - surprisingly good quality
- **Shoe insoles** - with the right infill settings
- **Ear tips** for earphones
- **Vibration dampeners** for printers and electronics

Find TPU designs at [Printables.com](https://www.printables.com/search/models?q=tpu&ctx=models) and [Thingiverse](https://www.thingiverse.com/search?q=tpu&type=things).

---

## TPU Storage

TPU is highly hygroscopic - it absorbs moisture quickly and prints worse when wet. Signs of wet TPU: popping sounds, surface bubbles, weaker parts.

Store in an airtight container with [silica gel desiccant](https://www.amazon.com/s?k=silica+gel+desiccant+packets). Dry at 45-50°C for 4-6 hours in a [filament dryer](https://www.amazon.com/s?k=filament+dryer+box+3d+printing) if prints are coming out poorly.

---

## Summary

TPU is rewarding once dialled in. The key rules:

1. **Slow down** - 25mm/s, no exceptions until you know your setup
2. **Minimal retraction** - 0-2mm direct drive, 0-1mm Bowden
3. **Direct drive printer** is much easier than Bowden
4. **Keep it dry** - store with desiccant

Start with a simple test print - a small cube or a phone case - before attempting anything complex. Once you've got clean TPU prints, you'll wonder how you managed without it.
