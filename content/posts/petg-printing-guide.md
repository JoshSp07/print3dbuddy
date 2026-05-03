# PETG Printing Guide: Settings, Stringing, and Bed Adhesion

PETG sits in a sweet spot between PLA and ABS. It is stronger and more heat-resistant than PLA, easier to print than ABS, and has good chemical resistance. It is a natural choice for functional parts that need to handle some stress or warmth.

The catch is that PETG has a few specific quirks. It strings more than PLA, it sticks to some build surfaces almost too well, and it likes slightly different settings than what works for PLA. Once you know what to expect, it is a very capable material.

---

## Why PETG Behaves Differently

PETG is hygroscopic (it absorbs moisture from the air), it has a higher printing temperature than PLA, and it flows differently - it is stickier and more viscous when melted. These properties mean it grips build surfaces aggressively, tends to string between parts, and benefits from minimal cooling compared to PLA.

---

## Recommended Settings

**Nozzle temperature:** 230-250C. Start at 235C and adjust. Higher temperatures improve layer adhesion but increase stringing.

**Bed temperature:** 70-85C. PETG adheres best to a warm bed. Start at 75C.

**Part cooling fan:** 30-50%. PETG needs less cooling than PLA - too much fan reduces layer adhesion and can cause delamination. Too little causes stringing and drooping on overhangs.

**Print speed:** 40-60mm/s. PETG generally prints better slightly slower than PLA. The stickier melt needs a little more time to bond correctly.

**Retraction:**
- Direct drive: 1-2mm
- Bowden: 4-6mm

PETG is prone to stringing, so retraction is important - but too much retraction causes grinding and clogs. Start conservative and increase in small steps.

Use the [print settings cheat sheet](https://tools.print3dbuddy.com/tools/print-settings) for a full settings reference.

---

## Bed Adhesion - The Tricky Part

PETG can stick so aggressively to some surfaces that it pulls the surface coating off when you try to remove the print. This is especially common with:

- Textured PEI at high temperatures
- Bare glass
- Bare metal build plates

**Best approach:**
- **Smooth PEI + a thin layer of glue stick as a release agent** - the glue prevents the PETG from bonding directly to the PEI
- **Textured PEI at 70-75C bed temperature** (lower end) - less aggressive grip
- **Let the bed cool to 30-40C before removing** - PETG releases much more easily when cold

If a print is well and truly stuck, put the build plate in the freezer for 10 minutes. The differential thermal contraction usually pops it free.

Do not use hairspray or other adhesives intended to increase grip - PETG does not need them and you will make the problem worse.

---

## Fixing Stringing

PETG strings more than PLA by nature, but it is controllable. The main levers are:

**Temperature:** Try dropping nozzle temperature by 5-10C. A lower temperature means less oozing between moves.

**Retraction:** Increase retraction distance in 0.5mm steps until stringing improves, but stop before you get grinding or clogs.

**Travel speed:** Increase the travel (non-printing movement) speed. The faster the nozzle moves between parts, the less time plastic has to drip.

**Combing / avoid crossing perimeters:** Enable this in your slicer. It routes travel moves through the inside of the model rather than across open air, eliminating most stringing without touching retraction.

See the full [stringing fix guide](/posts/how-to-fix-3d-printer-stringing/) for a complete walkthrough.

---

## Layer Adhesion and Delamination

If your PETG prints are delaminating or layers are separating, the most common causes are:

- **Too much part cooling** - reduce fan speed
- **Print speed too high** - slow down to give layers time to bond
- **Temperature too low** - try 5-10C higher
- **Wet filament** - PETG absorbs moisture and wet PETG delaminates easily; dry before printing if stored unsealed. See the [wet filament guide](/posts/how-to-fix-wet-filament/) for drying instructions.

---

## Moisture and Storage

PETG absorbs moisture more readily than PLA. After a few weeks of open storage in a humid environment, you will notice:

- More stringing than usual
- Rough surface texture
- Slight crackling sounds at the nozzle
- Weaker layer adhesion

If you notice these symptoms, dry the spool at 65C for 4-6 hours in a filament dryer or food dehydrator before printing. Store in a sealed bag with desiccant between uses.

---

## When to Use PETG vs PLA

**Choose PETG when:**
- The part will be exposed to heat (car interior, near electronics, direct sunlight)
- You need a more impact-resistant or flexible part than PLA provides
- Chemical resistance matters (PETG resists many common household chemicals)
- Printing parts that need to bend slightly without snapping

**Stick with PLA when:**
- Print quality and surface detail are the priority
- Ease of printing matters more than material properties
- The part does not need to withstand heat or stress

See the [PLA vs PETG vs ABS comparison](/posts/pla-vs-petg-vs-abs-which-filament-for-beginners/) for a full breakdown.

---

## PETG for Outdoor Use

PETG handles outdoor use significantly better than PLA. PLA degrades noticeably in direct sunlight over months and starts to soften at fairly low temperatures. PETG is more UV-stable and holds its shape in higher heat.

That said, PETG isn't the best outdoor material either. It slowly yellows with prolonged sun exposure and has a heat deflection temperature of around 70-80°C, meaning it will deform in a hot car interior, direct summer sun in a south-facing window, or near heat sources. For parts that genuinely need long-term outdoor performance, ASA is the better choice. It's formulated specifically for UV and weather resistance and outperforms PETG over months of outdoor exposure.

If PETG is what you have and outdoor performance matters, a UV-resistant clear coat spray extends the part's life noticeably.

---

## Brand Differences With PETG

PETG is a material where brand quality matters more than with basic PLA. The spread between good and bad PETG is wider.

Established brands like Polymaker, eSUN, and Bambu Lab print consistently and hit close to their stated temperature ranges. Their diameter tolerances are tighter, which means less flow variation mid-print.

Budget PETG from unknown brands can have wider diameter inconsistencies, inconsistent flow, and sometimes needs significantly different temperatures than the label says. If you've tuned carefully and are still having repeated problems with PETG that don't respond to settings changes, switching to a more consistent brand is a legitimate troubleshooting step, not just a luxury.

---

## PETG vs PETG-CF

Carbon fibre reinforced PETG (PETG-CF) has short chopped carbon fibres mixed into the base material. This makes it noticeably stiffer and reduces flex, which is useful for structural parts.

The trade-offs: PETG-CF requires a hardened steel nozzle. The carbon particles are abrasive and will wear a brass nozzle down within a few hundred grams of printing. Surface finish is rougher than standard PETG, and the material tends to be more brittle at impact than unfilled PETG.

For parts that need stiffness and rigidity, the upgrade is worth it. For general-purpose use where you want some flex and a decent surface finish, standard PETG is the right choice.

---

## Related Guides

- [How to Fix 3D Printer Stringing](/posts/how-to-fix-3d-printer-stringing/) - retraction, temperature, and travel settings
- [How to Fix Wet Filament](/posts/how-to-fix-wet-filament/) - identifying and drying moisture-affected filament
- [3D Printing Layer Adhesion Problems](/posts/3d-printing-layer-adhesion-problems-fixes/) - delamination and weak layers
- [Best Filament for Outdoor Use](/posts/best-filament-for-outdoor-use/) - PETG vs ASA for outdoor applications
- [Nozzle Size Recommender](https://tools.print3dbuddy.com/tools/nozzle-recommender) - check nozzle choice for PETG
