# How to Fix 3D Print Warping: The Complete Guide

Warping is a thermal problem. Plastic contracts as it cools. If different parts of your print cool at different rates, the uneven contraction pulls the base off the bed - corners lift first, then the whole print peels away.

The fix depends entirely on the material. PLA warps rarely and is usually fixed with basic bed prep. ABS without an enclosure is fighting physics - no amount of glue stick will reliably fix what is fundamentally a heat management problem.

---

## Fix 1: Clean the Bed and Check Z Offset

Before anything else, clean the bed with isopropyl alcohol. Skin oils from handling the surface cut adhesion significantly. This alone fixes more warping problems than people expect, because what looks like a warping issue is often just poor first layer adhesion.

Then check your Z offset. A first layer that is not properly squished onto the bed will lift the moment thermal forces start pulling. You want the first layer lines slightly flattened and fused to the surface, not sitting round on top of it.

---

## Fix 2: Bed Temperature

A cold bed is one of the most common causes of warping. More importantly, make sure the bed is at temperature before the print starts - not reaching temperature at the start. Let it soak for a couple of minutes after hitting the target.

| Material | Bed Temperature |
|---|---|
| PLA | 55 - 65°C |
| PETG | 70 - 85°C |
| ABS | 100 - 110°C |
| ASA | 100 - 110°C |
| TPU | 30 - 60°C |

---

## Fix 3: Use the Right Bed Surface

The stock bed surface on most printers is not optimised for all materials.

| Surface | Best For | Notes |
|---|---|---|
| Textured PEI sheet | PLA, PETG, ABS | Best all-rounder. Parts release cleanly when cool. |
| Smooth PEI | PLA, PETG | Better bottom surface finish |
| Glass | PLA | Consistent and cheap. Parts release when cold. |
| Garolite / FR4 | Nylon | Nylon bonds exceptionally well to this |

A textured PEI spring steel sheet is the first hardware upgrade worth making on almost any printer. Parts bond well when hot and pop off when cool with no tools required.

PETG bonds aggressively to bare glass and smooth PEI - it can rip chunks out of the surface when you remove the print. If you are printing PETG on glass, use a thin layer of glue stick as a release agent, not as an adhesion aid.

---

## Fix 4: Add a Brim

A brim adds flat perimeters around the base of your model, increasing the bonded surface area and resisting the pulling force from contraction.

Enable in your slicer - 5-10mm width for most prints, 10-15mm for ABS/ASA or anything with a small contact area at the base. You snap or cut it off after printing.

Use a brim on:
- Any ABS or ASA print
- Anything with a small footprint or thin base
- Tall prints with narrow bases
- Anything you cannot afford to fail halfway through

---

## Fix 5: Enclosure for ABS and ASA

If you are printing ABS or ASA without an enclosure and getting warping, the enclosure is not optional. There is no other fix that works reliably.

The problem is the temperature differential between the hot bed and the cooler air around the print. An enclosure traps heat and keeps the ambient temperature elevated, which slows and evens out cooling across the whole print. Without it, the top layers are cooling in open air while the bottom layers are sitting on a 105 degree bed - the differential causes warping regardless of what else you do.

Target internal temperature of 40-50 degrees for ABS and ASA. A cheap thermometer inside lets you monitor it.

Budget options that work:
- A cardboard box placed over the printer (free and surprisingly effective for testing)
- A purpose-built enclosure like the Creality tent (~£30)
- Printed enclosure panels - many free designs on Printables

**Important:** do not print PLA in an enclosure above about 30 degrees ambient. PLA softens at relatively low temperatures and heat creep becomes a problem. If you share an enclosure between materials, turn it off or open it for PLA.

---

## Fix 6: Part Cooling Fan Settings

Cooling fans accelerate warping in temperature-sensitive materials.

**ABS and ASA:** turn part cooling off entirely, or no more than 15-20%. The whole point is to cool slowly and evenly.

**PETG:** 20-30% maximum. Too much cooling causes layer delamination, which shows up as weak prints even if adhesion looks fine.

**PLA:** 50-100% is fine. PLA does not warp significantly and benefits from good cooling for detail quality.

---

## Fix 7: Model Orientation and Geometry

Large flat surfaces printed parallel to the bed give more adhesion area and distribute thermal stress better. Orient your model to put the largest flat face on the bed where possible.

A thicker first layer (0.3mm instead of 0.2mm) bonds better. Slowing the first layer to 20-25mm/s also improves adhesion.

If you are designing the model yourself, chamfering the base edges at 45 degrees makes a real difference. Sharp 90-degree corners concentrate thermal stress and are where warping almost always starts.

---

## Fix 8: Adhesion Aids (Use as a Last Resort)

Glue stick, hairspray, and purpose-made adhesion sprays like Magigoo can help in stubborn cases. But they are treating the symptom, not the problem. If you need adhesion aids for every print of a particular material, something else is wrong - the bed temperature, the surface, the enclosure.

The exception is PETG on glass, where a thin layer of glue stick is used as a release agent to prevent over-bonding rather than to increase adhesion.

---

## Material-Specific Checklist

### PLA
- Bed cleaned with IPA?
- Bed at 60°C, soaked before printing?
- Z offset giving slight squish on first layer?
- First layer speed at 20-25mm/s?

### PETG
- Bed at 75-85°C?
- Fan at 20-30% maximum?
- Not printing on bare glass without a release agent?

### ABS / ASA
- Enclosure in use?
- Bed at 105-110°C?
- Part cooling off or below 20%?
- Brim of 10-15mm enabled?
- Drafts eliminated - doors and windows closed?

---

## Summary

PLA warping: clean the bed, check Z offset and bed temperature. Fixed in most cases.

PETG warping: right bed temperature, minimal fan, right bed surface.

ABS and ASA warping: get an enclosure. Everything else is secondary.

Start with the simplest thing. Adhesion sprays and special coatings are not the answer - correct fundamentals are.
