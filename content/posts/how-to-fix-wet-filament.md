# How to Fix Wet Filament: Identifying, Drying, and Preventing Moisture Problems

One of the most frustrating 3D printing problems to diagnose is wet filament. The symptoms look like a dozen different things - stringing, poor surface quality, blobs, brittle prints, crackling sounds - and people often spend hours tweaking slicer settings trying to fix something that is actually a materials storage problem.

This guide covers how to identify wet filament, how to dry it out, and how to store it so it does not happen again.

---

## What Is Wet Filament?

Most 3D printing filaments are hygroscopic - they absorb moisture from the air over time. When that moisture gets into the filament and you heat it to printing temperature, the water turns to steam inside the nozzle. That steam creates tiny bubbles and pressure spikes in the melt zone, which causes a range of visible problems.

It is not a sign that your filament is ruined. In most cases, drying the filament properly will restore it to its original quality.

---

## How to Tell If Your Filament Is Wet

**Sounds:**
- Crackling, popping, or hissing sounds while printing (this is the most obvious sign)
- Clicking at the nozzle during extrusion

**Visual signs while printing:**
- Small wisps of steam or vapour coming from the nozzle
- Bubbles or foam visible in extruded filament
- Rough, inconsistent surface texture
- More stringing than usual
- Random blobs or zits on the surface

**Signs in the finished print:**
- Rough, sandpaper-like surface texture
- Visible bubbles or voids in walls
- Prints that feel brittle or snap more easily than usual
- Poor layer adhesion that you cannot fix with temperature or speed changes

If you hear crackling while printing, stop and dry your filament before continuing. Wet filament can also contribute to partial clogs over time, as moisture-affected material burns inside the nozzle.

---

## Which Filaments Are Most Affected?

Not all filaments absorb moisture at the same rate:

**Very sensitive (dry before every print, store carefully):**
- Nylon - absorbs moisture extremely quickly, can become unusable in hours in humid conditions
- PVA / BVOH (water-soluble support materials) - absorbs moisture even faster than Nylon
- TPU / flexible filaments - noticeably worse quality when wet

**Moderately sensitive (store with desiccant, dry if stored open):**
- PETG - absorbs moisture more slowly than Nylon but is still noticeably affected
- ABS / ASA - less sensitive than PETG but can be affected by long-term open storage

**Least sensitive:**
- PLA - relatively resistant to moisture compared to other filaments, but can still degrade after months of open storage in humid conditions

---

## How to Dry Filament

### Option 1: Dedicated Filament Dryer (Best)

A dedicated filament dryer (like the Sunlu S1 Plus or similar) is the easiest and safest method. You put the spool in, set the temperature, set a timer, and it handles the rest. Most can also dry filament while you print from it, which helps with long prints on sensitive materials.

See the [best filament dryers guide](/posts/best-filament-dryers-for-3d-printing/) for a comparison of the most popular options.

---

### Option 2: Food Dehydrator

A food dehydrator works well and is often cheaper than a dedicated filament dryer. Make sure it fits your spool and can reach the right temperature.

**Drying temperatures by material:**
- PLA: 45-50C for 4-6 hours
- PETG: 65C for 4-6 hours
- ABS / ASA: 70-80C for 4-6 hours
- TPU: 45-50C for 4-6 hours
- Nylon: 80-90C for 8-12 hours

Do not exceed these temperatures. PLA will deform if dried too hot, and many spools use plastic that softens around 70-80C.

---

### Option 3: Oven

A kitchen oven works but requires care. Most ovens are not accurate at low temperatures - the actual temperature can be 20-30C higher or lower than the dial setting. Use an oven thermometer to verify the actual temperature before putting filament in.

Set the oven to its lowest setting and use a thermometer to measure the actual temperature inside. For PLA especially, exceeding 60C for long periods can cause the spool to warp or the filament to fuse together on the spool.

Leave the oven door slightly ajar to allow moisture to escape.

---

### Option 4: Airtight Box With Desiccant

This will not dry filament quickly, but placing a wet spool in an airtight box with plenty of fresh silica gel desiccant will slowly pull moisture out over several days. It is the lowest-effort method but the slowest.

---

## How to Store Filament to Prevent Moisture Problems

- Keep unused spools in resealable zip bags or airtight containers (vacuum-sealed bags are even better)
- Include silica gel desiccant packets and replace or regenerate them periodically
- Store in a cool, dry place - avoid basements, garages, or anywhere with temperature swings that cause condensation
- Colour-indicating silica gel changes colour when saturated - once it changes, dry the desiccant in the oven at 120C for an hour before reusing it
- For very sensitive materials (Nylon, TPU), dry the filament just before printing even if stored well

The [how to store filament properly](/posts/how-to-store-filament-properly/) guide covers storage options and containers in more detail.

---

## Quick Checklist

1. Listen for crackling or popping while printing - if you hear it, dry the filament before continuing
2. Identify the material - is it a moisture-sensitive filament?
3. Dry at the correct temperature for your material (see table above)
4. Store all filament in airtight bags or containers with desiccant after drying
5. For Nylon and TPU, dry before every long print regardless of storage conditions

---

## Related Guides

- [How to Store Filament Properly](/posts/how-to-store-filament-properly/) - long-term storage methods and containers
- [Best Filament Dryers for 3D Printing](/posts/best-filament-dryers-for-3d-printing/) - dedicated dryers compared
- [How to Fix Under-Extrusion](/posts/how-to-fix-under-extrusion/) - wet filament can cause inconsistent extrusion
- [TPU Flexible Filament Guide](/posts/tpu-flexible-filament-beginners-guide/) - TPU-specific settings and storage tips
- [Print Settings Cheat Sheet](https://tools.print3dbuddy.com/tools/print-settings) - correct temperatures for your filament type
