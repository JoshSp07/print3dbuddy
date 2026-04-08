# 3D Printing Supports: When to Use Them, How to Set Them Up, How to Remove Them

Supports are one of those things that every 3D printer owner has a complicated relationship with. You need them for certain prints. They take extra time and filament. And removing them - especially on detailed models - is satisfying when it goes well and infuriating when it does not.

I spent about six months avoiding them entirely: designing around overhangs, tilting models at odd angles, splitting things in half, convincing myself it was fine. Eventually I printed something that just needed supports, used them, and discovered they were not nearly as bad as I had built them up to be. Now I use them without thinking twice. The trick is knowing when to use them and how to set them up so they actually come off cleanly.

---

## Why Supports Exist

FDM printing builds objects layer by layer from the bottom up. Each layer needs something beneath it. When a feature hangs in mid-air - an overhang, a bridge, an arch - there is nothing underneath for the filament to land on and it sags or fails.

Supports are printed structures that fill that gap. They hold up the overhanging geometry during printing and get removed afterwards.

---

## The 45-Degree Rule

Most printers handle overhangs up to about 45-50 degrees without supports. Beyond that, each new layer is too far from the previous one and unsupported filament starts to sag.

The exact threshold depends on your printer, material, and part cooling. PLA with good cooling can often manage 50-55 degrees. PETG is less tolerant and may start struggling at 40 degrees. ABS benefits from an enclosure but still has trouble with steep overhangs.

The best way to find your actual limit is to print an overhang test at various angles and see where your specific setup starts to struggle. The [overhang test print](https://tools.print3dbuddy.com/test-prints#overhang-test) at tools.print3dbuddy.com is a quick way to do this - worth running once when you get a new printer or switch materials.

---

## Types of Supports

### Normal Supports

Straight columns or grids going from the build plate up to the overhang. Standard option in every slicer. Reliable, uses more material than tree supports, and can be harder to remove from surfaces you care about.

### Tree Supports

Branches that grow from the build plate and reach up to touch the model at specific points only. Uses significantly less material than normal supports and leaves a better surface finish because it contacts the model at small points rather than across a whole area.

Tree supports are better for organic shapes - figurines, characters, curved geometry. Normal supports are often better for mechanical parts where you need firm backing across a flat surface.

### Support Enforcers and Blockers

Most slicers let you paint or place support enforcers (force a support here) and blockers (never put a support here) on specific parts of the model. Automatic detection is not always right - it puts supports where you do not need them, or misses areas that need them.

Manual placement takes a few minutes but saves time on removal and improves surface finish in the areas that matter. Worth learning once you are past the basics.

---

## The Settings That Matter

### Support Density

How dense the support structure is. Higher density means stronger support but more material and harder removal. For most models, 10-20% is enough. Only go higher if you are supporting a large flat area that needs firm backing.

### Z Distance (Gap)

The vertical gap between the top of the support and the bottom of the model surface. Too small and the support fuses to the model - hard to remove and damages the surface. Too large and the overhang sags into the gap.

For PLA on PLA, 0.2mm (one layer height) is a good starting point. For PETG, which bonds more aggressively, increase to 0.3mm. Getting this right makes more difference to support removal than anything else.

### Interface Layers

A denser layer printed between the support and the model. Makes the supported surface smoother and the support easier to remove. Turn this on for anything where surface finish matters. The material and Z distance settings for the interface layer specifically are often adjustable separately from the rest of the support.

### Support Placement

"Touching build plate only" - supports only grow from the floor. Simpler, less material, easier removal, but won't help features that overhang other parts of the model.

"Everywhere" - supports anywhere they are needed, including on top of the model itself. Required for complex geometry but generates more supports to remove.

---

## When to Use Supports vs. When to Redesign

**Use supports when:**
- Overhangs exceed 45-50 degrees
- Bridges are longer than about 50-60mm (shorter bridges usually print fine without support)
- The model has horizontal holes (like a hole through a wall)
- The underside surface finish matters for how the part will be used

**Redesign or reorient instead when:**
- You can split the model into two pieces and glue them together
- Rotating the model eliminates the overhang without creating worse problems elsewhere
- The overhang is under 45 degrees and the underside surface does not matter
- The geometry is functional and support removal might damage critical features

---

## Removing Supports Without Damaging the Print

The first time I printed a figurine with tree supports in Cura, I removed them with a craft knife and sliced through the model instead of the support. Ruined a 14-hour print. The support had fused to the surface because I had not set a proper interface layer or Z gap - same material, same nozzle temperature, and it had basically become part of the print.

After that I adjusted Z gap and enabled interface layers. Removal became straightforward.

**Let it cool completely** before attempting removal. Warm prints are softer - easier to accidentally snap thin features or bend geometry while levering supports off.

**Use the right tools.** Needle-nose pliers for gripping and twisting supports away from the model. Flush cutters for snipping support columns at the base. A craft knife for cleaning up the surface after. Not your fingers for anything other than test-pulls.

**Work from the outside in.** Snap or cut supports away from the outer edges first, then work toward the model. This stops you using the model itself as a lever and breaking features in the process.

**For stubborn supports:** A brief soak in warm water softens PLA slightly and can make removal easier. PVA supports dissolve completely in warm water - no removal needed at all.

---

## Dual Extrusion and Dissolvable Supports

If you have a dual-extrusion printer, using a different material for supports changes things significantly.

**PVA** dissolves in warm water and leaves a clean surface. Expensive, absorbs moisture quickly and needs dry storage, but worth it for detailed models where surface finish matters.

**HIPS** dissolves in limonene and is used alongside ABS. Less common than PVA.

**Breakaway filament** is designed to separate cleanly from the model surface without dissolving. Easier removal than same-material supports without needing a chemical process.

For single-material printing, interface layer settings and Z distance are the main levers. Get those right and same-material support removal is manageable for most prints - just not as clean as dissolvable.

---

## A Note on PETG and TPU with Supports

Both materials bond more aggressively than PLA and need larger Z gaps to remove cleanly. PETG at 0.3mm and TPU at 0.3-0.4mm. If you use the default PLA Z gap settings on PETG, you will be cutting supports off rather than pulling them.

The [print settings tool at tools.print3dbuddy.com](https://tools.print3dbuddy.com) covers support settings per material if you want a starting point.

Supports are not the enemy. Once you know how to set them up properly, they open up models you simply cannot print any other way.
