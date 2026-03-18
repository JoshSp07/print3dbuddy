# How to Fix 3D Print Warping: The Complete Guide

Warping is one of the most frustrating problems in 3D printing  -  your print starts fine, then the corners lift off the bed, the base curves up, and the whole thing peels away mid-print.

The good news is that warping is almost always fixable. Here's why it happens and exactly how to stop it.

---

## Why Warping Happens

Warping is a thermal problem. When plastic cools, it contracts. If different parts of your print cool at different rates, the uneven contraction pulls the base off the bed.

This is especially bad with:
- **ABS and ASA**  -  high coefficient of thermal expansion, warp badly without an enclosure
- **Large flat prints**  -  more surface area = more contraction force
- **Thin bases**  -  less mass to anchor the print to the bed
- **Cold environments**  -  ambient temperature affects cooling rates significantly

PLA warps less, but it still warps under the wrong conditions.

---

## Fix 1: Sort Your Bed Adhesion First

Before anything else, make sure your first layer is actually sticking properly.

### Clean the bed
Oils from your fingers reduce adhesion significantly. Clean the print surface with isopropyl alcohol (IPA, 70%+) before every print. This alone fixes many warping problems.

### Check your Z offset
If your nozzle is too far from the bed, the first layer won't squish down properly and won't bond. You want slight "squish"  -  the filament should be slightly flattened, not round and separate.

### Check bed temperature
| Material | Bed Temperature |
|---|---|
| PLA | 55 - 65°C |
| PETG | 70 - 85°C |
| ABS | 100 - 110°C |
| ASA | 100 - 110°C |
| TPU | 30 - 60°C |

A cold bed is a major cause of warping. Make sure your bed is up to temperature *before* the print starts  -  let it soak for a few minutes after reaching temperature.

---

## Fix 2: Use the Right Bed Surface

Not all bed surfaces hold all materials equally.

| Surface | Best For | Notes |
|---|---|---|
| PEI sheet (textured) | PLA, PETG, ABS | Best all-rounder. Parts release when cool. |
| PEI sheet (smooth) | PLA, PETG | Better surface finish on bottom |
| Glass (bare) | PLA | Cheap, consistent, parts release cleanly |
| BuildTak | PLA, PETG | Good adhesion, harder to remove parts |
| Garolite / FR4 | Nylon | Nylon bonds exceptionally well |

If you're still on the stock glass or magnetic bed your printer shipped with, a textured PEI sheet (~£15-25) is one of the best upgrades you can make.

---

## Fix 3: Add a Brim

A brim is a flat ring of extra perimeters added around the base of your print. It massively increases the surface area bonded to the bed, resisting the pulling force from thermal contraction.

Enable in your slicer: **Brim width: 5-10mm** for most prints, 10-15mm for ABS/ASA or large prints.

The brim prints attached to your model  -  you snap or cut it off after printing. Takes about 30 seconds.

**When to use a brim:**
- Any ABS or ASA print
- Any print with small contact area at the base
- Large prints with thin walls
- Anything you really can't afford to fail

---

## Fix 4: Use an Enclosure for ABS and ASA

If you're printing ABS or ASA and still getting warping after fixing bed adhesion, you almost certainly need an enclosure.

An enclosure traps heat, keeping the ambient temperature around the print elevated. This slows and evens out the cooling rate, preventing the differential contraction that causes warping.

**Budget enclosure options:**
- DIY cardboard box (free, surprisingly effective)
- Creality enclosure tent (~£30)  -  fits most printers
- Proper printed enclosures  -  many free designs on Printables/Thingiverse

Target internal temperature: 40-50°C for ABS/ASA. A cheap thermometer inside lets you monitor this.

**Important:** PLA should NOT be printed in an enclosure above ~30°C ambient  -  it can cause heat creep and clogs. Turn off or open the enclosure for PLA.

---

## Fix 5: Adjust Fan Cooling

Part cooling fans accelerate warping in materials that are sensitive to it.

**For ABS and ASA:** Turn part cooling off entirely, or use a maximum of 20%. The whole point is to cool slowly and evenly.

**For PETG:** Minimal cooling  -  20-30% maximum. Too much cooling causes layer delamination.

**For PLA:** Generous cooling is fine  -  50-100%. PLA doesn't warp much and benefits from good cooling for detail.

In your slicer, this is usually in **Cooling** settings. You can also set per-layer fan speeds (useful for ramping up after the first few layers).

---

## Fix 6: Adjust Model Orientation and First Layers

### Increase first layer thickness
A thicker first layer (0.3mm instead of 0.2mm) bonds better. Many slicers default to this.

### Slow down first layer
Printing too fast on the first layer reduces adhesion. 20-30mm/s for the first layer is common  -  your slicer may already handle this.

### Orient the model to minimise thermal stress
Large flat surfaces parallel to the bed = more surface area = better adhesion + less contraction stress. If your model has a large flat face, orient it down.

### Chamfer the base edges in your model
Sharp 90-degree corners are warp hotspots. A small chamfer (45°, 1mm) on the base edges significantly reduces the stress concentration that starts warping.

---

## Fix 7: Bed Adhesion Aids

When all else fails, adhesion aids help:

- **Glue stick (Pritt Stick / UHU):** Apply thin layer, let dry before printing. Works well for PLA on glass. Easy to clean with water.
- **Hairspray:** Similar effect. AquaNet is the classic hobbyist choice.
- **Magigoo / 3DLac:** Purpose-made adhesion sprays. More consistent than hairspray.
- **Kapton tape:** Used for ABS on glass  -  creates a slightly rough surface.

These are last resorts. If you need them for every print, fix the underlying problem (Z offset, bed temp, bed surface).

---

## Material-Specific Checklist

### PLA Warping
- [ ] Bed cleaned with IPA?
- [ ] Bed at 60°C?
- [ ] Z offset correct (slight squish)?
- [ ] First layer speed slow?

### PETG Warping
- [ ] Bed at 80°C?
- [ ] Fan at 20-30% max?
- [ ] Not printing too fast (stringing causes false positives)?

### ABS / ASA Warping
- [ ] Enclosure in use?
- [ ] Bed at 105-110°C?
- [ ] Part cooling off or <20%?
- [ ] Brim enabled (8-15mm)?
- [ ] Draft shield in slicer?

---

## Summary

Most warping comes down to three things: dirty bed, wrong bed temperature, or insufficient enclosure for heat-sensitive materials. Start with cleaning the bed and checking your Z offset  -  this solves 80% of cases.

If you're printing ABS and still warping: get an enclosure. There's no substitute.
