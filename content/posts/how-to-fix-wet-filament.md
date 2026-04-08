# Wet Filament: How to Identify, Dry, and Store Filament Properly

One of the most frustrating 3D printing problems to diagnose is wet filament. The symptoms look like a dozen different things - stringing, poor surface quality, blobs, brittle prints, crackling sounds - and people often spend hours tweaking slicer settings trying to fix something that is actually a materials storage problem.

This guide covers how to identify wet filament, how to dry it out, and how to store it so the problem does not come back.

---

## Why Moisture Ruins Filament

Most 3D printing filaments are hygroscopic - they absorb moisture from the air over time. When that moisture gets into the filament and you heat it to printing temperature, the water turns to steam inside the nozzle. That steam creates tiny bubbles and pressure spikes in the melt zone, causing a range of visible problems:

- Popping and crackling sounds while printing
- Bubbles and blobs on the surface
- Stringing worse than usual
- Weak layer adhesion - parts snap more easily
- Inconsistent extrusion and gaps

It is not a sign that your filament is ruined. In most cases, drying it properly will restore it to its original quality.

---

## Which Filaments Are Most Affected?

| Filament | Moisture Sensitivity | Storage Priority |
|---|---|---|
| Nylon (PA) | Extreme | Airtight + desiccant always |
| TPU / TPE | Very High | Airtight + desiccant always |
| PETG | High | Airtight storage recommended |
| ABS / ASA | Medium | Airtight storage recommended |
| PLA / PLA+ | Low-Medium | Airtight for long-term storage |

Nylon is the worst - it can absorb enough moisture to cause problems within hours of being left out in humid conditions.

---

## How to Tell If Your Filament Is Wet

**Sounds:**
- Crackling, popping, or hissing sounds while printing - this is the most reliable sign
- Clicking at the nozzle during extrusion

**Visual signs while printing:**
- Small wisps of steam or vapour from the nozzle
- Bubbles or foam visible in extruded filament
- Rough, inconsistent surface texture
- More stringing than usual from the same filament
- Random blobs or zits on the surface

**Signs in the finished print:**
- Rough, sandpaper-like surface
- Visible bubbles or voids in walls
- Prints that feel brittle or snap more easily than usual
- Poor layer adhesion that temperature and speed changes do not fix

When in doubt, listen. A dry spool should extrude almost silently. Crackling means moisture.

---

## How to Dry Filament

### Option 1: Dedicated Filament Dryer (Best)

A dedicated filament dryer (like the Sunlu S1 Plus or eSUN eBOX) is the easiest and safest method. Set the temperature, set a timer, done. Many models let you print directly from the dryer while it runs, which helps with long prints on sensitive materials.

See the [best filament dryers guide](/posts/best-filament-dryers-for-3d-printing/) for a comparison of popular options.

---

### Option 2: Food Dehydrator

A food dehydrator works well and is often cheaper than a dedicated dryer. Make sure it fits your spool and can reach the required temperature.

**Drying temperatures by material:**

| Filament | Temperature | Time |
|---|---|---|
| PLA | 45-50C | 4-6 hours |
| PETG | 65C | 4-6 hours |
| ABS / ASA | 70-80C | 4-6 hours |
| TPU | 45-50C | 4-6 hours |
| Nylon | 80-90C | 8-12 hours |

Do not exceed these temperatures. PLA will deform if dried too hot, and most spool plastic softens around 70-80C.

---

### Option 3: Oven

A kitchen oven works but requires care. Most ovens are inaccurate at low temperatures - the actual temperature can be 20-30C off the dial setting. Use an oven thermometer to verify before putting filament in. Leave the door slightly ajar to let moisture escape. Not recommended for PLA due to warping risk.

---

### Option 4: Airtight Box With Desiccant

This will not dry filament quickly, but placing a wet spool in an airtight box with plenty of fresh silica gel desiccant will slowly pull moisture out over several days. Lowest effort, slowest result.

---

## How to Store Filament

### The Basic Setup: Airtight Container + Desiccant

The minimum you need:
1. An airtight container - a large zip-lock bag works, but a sealed plastic storage box is better
2. Silica gel desiccant packets - absorb moisture inside the container

[Silica gel desiccant packs](https://www.amazon.co.uk/s?k=silica+gel+desiccant+packets+reusable&tag=print3dbuddy2-21) are cheap and reusable - bake at 120C for a few hours to regenerate when saturated. Colour-indicating silica gel changes colour when full, so you can see at a glance whether it needs regenerating.

### Dedicated Filament Dry Boxes

Purpose-built dry boxes are a step up from zip-lock bags:

- [eSUN eBOX Lite](https://www.amazon.co.uk/s?k=eSUN+eBOX+filament+dryer&tag=print3dbuddy2-21) - built-in heating and humidity display, keeps filament dry while printing
- [Sunlu FilaDryer S2](https://www.amazon.co.uk/s?k=Sunlu+FilaDryer+S2&tag=print3dbuddy2-21) - popular mid-range option with accurate temperature control
- DIY option: a large airtight food storage container with desiccant and a PTFE tube hole for feeding directly to the printer

### Vacuum Bags

[Vacuum storage bags](https://www.amazon.co.uk/s?k=vacuum+storage+bags+filament&tag=print3dbuddy2-21) remove air entirely. Excellent for long-term storage of spools you won't use for months.

---

## Practical Storage Tips

**Don't leave spools on the printer.** If you're not printing for more than a day, put the filament back in storage. This is the most common mistake beginners make.

**Store in a cool, dry place.** Avoid garages or sheds with temperature swings - condensation forms when temperatures change rapidly.

**Buy a cheap hygrometer.** A [digital hygrometer](https://www.amazon.co.uk/s?k=digital+hygrometer+thermometer&tag=print3dbuddy2-21) (~£5) inside your storage box shows the humidity level. Aim for below 15% RH.

**Label your desiccant.** Note the date you last regenerated it. Replace or regenerate every 3-6 months depending on your climate.

**For Nylon and TPU, dry before every long print** regardless of storage conditions. These materials absorb moisture fast enough that even well-stored spools benefit from a drying session before a long print.

---

## Quick Checklist

1. Hear crackling or popping while printing? Dry the filament before continuing
2. Identify the material - is it moisture-sensitive?
3. Dry at the correct temperature and time for your material (see table above)
4. Store in an airtight container with desiccant after drying
5. Keep filament off the printer between sessions

---

## Related Guides

- [Best Filament Dryers for 3D Printing](/posts/best-filament-dryers-for-3d-printing/) - dedicated dryers compared
- [How to Fix Under-Extrusion](/posts/how-to-fix-under-extrusion/) - wet filament can cause inconsistent extrusion
- [TPU Flexible Filament Guide](/posts/tpu-flexible-filament-beginners-guide/) - TPU-specific settings and storage tips
- [Print Settings Cheat Sheet](https://tools.print3dbuddy.com/tools/print-settings) - correct temperatures for your filament type
