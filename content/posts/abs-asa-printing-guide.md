# ABS and ASA Printing Guide: Settings, Warping, and Getting Reliable Results

ABS and ASA are the two materials most beginners are warned away from. That reputation is mostly deserved - they are genuinely harder to print than PLA or PETG. But they have real advantages for functional parts: heat resistance, better impact strength, and (for ASA specifically) excellent UV and weather resistance.

This guide covers everything you need to print ABS and ASA reliably.

---

## ABS vs ASA - Which Should You Use?

**ABS** is the older of the two. It has been around since the beginning of desktop 3D printing and is widely available. It machines and sands well and bonds strongly with acetone, which lets you smooth prints or glue parts together cleanly.

**ASA** is essentially an improved ABS. It has similar strength and heat resistance but with much better UV resistance - ASA parts left outdoors will not fade or become brittle the way ABS does. It is also slightly easier to print than ABS, with less warping.

For most people, ASA is the better choice unless you specifically need the acetone-smoothing properties of ABS or already have ABS filament to use up.

---

## Why ABS and ASA Are Harder to Print

Both materials shrink significantly as they cool. If one part of the print cools faster than another, the differential shrinkage pulls the print apart - causing warping, layer splitting, and cracks. The fixes all come down to controlling the cooling environment.

---

## The Most Important Requirement: An Enclosure

Printing ABS or ASA without an enclosure is possible, but it is fighting against the material. An enclosure traps heat around the print and keeps the ambient temperature stable, dramatically reducing warping and layer cracking.

You do not need an expensive enclosure. A fabric tent enclosure or even a cardboard box placed over the printer during printing can make a noticeable difference. See the [best 3D printer enclosures guide](/posts/best-3d-printer-enclosures/) for options at different budgets.

If you do not have an enclosure, you can still try printing ABS or ASA with these mitigations:
- Turn off or reduce part cooling fan entirely
- Use a brim (5-10 lines) to help adhesion and slow edge cooling
- Print in a warm, draught-free room
- Use a heated bed at the high end of the recommended range

---

## Recommended Settings

**Nozzle temperature:**
- ABS: 230-250C (start at 240C and adjust)
- ASA: 235-255C (start at 245C and adjust)

**Bed temperature:**
- ABS: 100-110C
- ASA: 90-100C

**Part cooling fan:**
- Set to 0% for the first 3-5 layers at minimum
- Many people print ABS and ASA with 0% cooling for the entire print
- If surface quality is a priority, try 10-20% fan for overhangs only

**Enclosure temperature:** Aim for 40-50C ambient inside the enclosure. Too hot and your filament will soften before it reaches the nozzle; too cold and warping returns.

Use the [print settings cheat sheet](https://tools.print3dbuddy.com/tools/print-settings) to get starting points for your exact printer setup.

---

## Bed Adhesion

ABS and ASA need good bed adhesion because the parts want to warp and peel.

**Best surfaces for ABS/ASA:**
- Smooth PEI - works well at temperature, releases when cool
- Garolite / FR4 sheet - excellent for both materials, especially ABS
- Glass with ABS juice or hairspray

**PEI note:** Textured PEI can grip ASA very strongly at temperature. If parts are sticking too hard and pulling up the PEI surface, try smooth PEI or let the bed cool to 40-50C before removing.

**Glue stick on any smooth surface** works as a release agent for ABS specifically - it prevents over-adhesion rather than improving it.

---

## Dealing With Warping

If warping is a persistent problem, work through this checklist:

1. Increase enclosure temperature or add one if you do not have it
2. Increase bed temperature by 5-10C
3. Add or increase brim width (8-15 lines)
4. Reduce part cooling fan to 0%
5. Check for draughts - open windows or nearby vents will cause cold air to hit the print
6. For very large flat parts, consider splitting the model into smaller sections

See the [how to fix warping guide](/posts/how-to-fix-3d-print-warping/) for more detail on each fix.

---

## Fumes and Ventilation

ABS produces styrene fumes when printing. ASA produces similar compounds. Both should be printed in a ventilated area or with an enclosure that has HEPA and activated carbon filtration. Do not print in a closed bedroom or office for long periods without ventilation.

ASA is somewhat better than ABS in this regard but the same precautions apply.

---

## Acetone Finishing (ABS Only)

One of ABS's unique properties is that it dissolves in acetone. This lets you:
- **Smooth prints** by brushing acetone onto the surface or using an acetone vapour chamber
- **Bond parts** by applying a tiny amount of acetone to the joint and pressing together - it creates a molecular bond stronger than most adhesives

ASA does not dissolve as readily in acetone, so this technique is mainly for ABS.

---

## Related Guides

- [How to Fix 3D Print Warping](/posts/how-to-fix-3d-print-warping/) - detailed warping fixes
- [Best 3D Printer Enclosures](/posts/best-3d-printer-enclosures/) - enclosure options at every budget
- [PLA vs PETG vs ABS - Which Filament?](/posts/pla-vs-petg-vs-abs-which-filament-for-beginners/) - material comparison
- [Best Filament for Outdoor Use](/posts/best-filament-for-outdoor-use/) - ASA compared to other weather-resistant options
- [Print Settings Cheat Sheet](https://tools.print3dbuddy.com/tools/print-settings) - temperature and speed settings for ABS and ASA
