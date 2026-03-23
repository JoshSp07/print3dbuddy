# How to Print TPU Hinges and Living Hinges

A hinge that flexes thousands of times without breaking, prints in a single piece, and needs no hardware. That is what a living hinge offers, and TPU is the material that makes it genuinely practical on a home 3D printer.

This guide covers everything from design principles to slicer settings and common problems.

---

## What Is a Living Hinge?

A **living hinge** is a thin, flexible section of material that connects two rigid parts and acts as the pivot point between them. Rather than using a pin, barrel, or mechanical joint, the material itself bends repeatedly without fracturing.

You see living hinges constantly in everyday life. The lid on a shampoo bottle is a classic example. The thin plastic strip connecting the cap to the body flexes every time you open it, often surviving hundreds of thousands of cycles before failing.

In 3D printing, a living hinge is usually a thin wall printed between two thicker bodies. When the print is flexed, that thin section absorbs the movement. With the right material and design, it will outlast the rest of the part.

---

## Why TPU Is the Ideal Material

**TPU (thermoplastic polyurethane)** is a flexible filament with a combination of properties that suits living hinges extremely well.

**Elasticity** - TPU stretches and returns to its original shape rather than cracking under repeated flexing. Rigid materials like PLA will fracture at a living hinge after very few cycles because they cannot absorb the strain.

**Layer adhesion** - TPU bonds well between layers, which is critical for a hinge that bends across its layer lines. Poor layer adhesion is one of the main failure points in printed hinges, and TPU holds up significantly better than brittle materials.

**Durability** - TPU resists abrasion, impact, and UV exposure better than most common filaments. A hinge that is going to be opened and closed regularly needs a material that does not degrade quickly.

**Shore hardness options** - TPU is available in different shore hardness ratings, typically between 85A and 98A. Softer grades (85A to 95A) are easier to flex and suit thin hinge designs. Stiffer grades (95A to 98A) are better for larger hinges or parts that need to hold a position.

For most living hinge applications, a **95A TPU** is a good starting point. It is soft enough to flex easily but firm enough to give the rest of the part some structural rigidity.

---

## Design Considerations

Getting the design right is more than half the battle. A hinge that is the wrong thickness, the wrong orientation, or the wrong shape will fail regardless of your print settings.

### Minimum Hinge Thickness

The hinge section itself needs to be thin enough to flex without effort, but not so thin that it tears. For TPU printed at 0.2mm layer height, a hinge thickness of **0.4mm to 0.8mm** works well. That is two to four layer heights.

Thinner than 0.4mm and the hinge may not print reliably. Thicker than 1mm and it will be stiff to open, which places more strain on the hinge when force is applied.

A **length of 3mm to 6mm** along the flex axis gives the hinge enough surface area to distribute strain. Very short hinges concentrate all the bending stress in one spot and fail faster.

### Hinge Orientation on the Bed

This is critical. **The hinge must flex perpendicular to the layer lines, not parallel to them.**

If the hinge bends in the same direction as your layers stack, you are relying on layer adhesion to hold everything together when the hinge opens. Layer adhesion is always the weakest bond in a printed part. The hinge will delaminate quickly.

The correct orientation is to print the part flat on the bed so that the hinge section runs vertically through the layers. When the hinge flexes, it is bending across the layer lines rather than trying to pull them apart. This takes full advantage of the material's strength within the layer rather than relying on the bond between layers.

If your part shape makes this impossible, consider rotating the print 90 degrees and using supports to hold it, or splitting the part into sub-assemblies that can each be oriented correctly.

### Print-in-Place vs Separate Parts

**Print-in-place** designs include the hinge in a single print job. The hinge connects both rigid panels in the same model. This is convenient and removes any need for assembly, but requires that the whole part is oriented correctly for the hinge to work.

**Separate parts with a post-print hinge** involves designing the hinge section as its own component that is then glued or clipped to two separate rigid panels. This approach gives you more freedom with orientation and lets you use different materials for the rigid sections (such as PETG or PLA) while only the hinge itself is TPU.

For most small to medium parts, print-in-place is the tidier option. For large assemblies or parts where the rigid sections need to be very stiff, the hybrid approach is worth the extra assembly time.

---

## Slicer Settings for TPU Hinges

TPU is more sensitive to slicer settings than PLA or PETG. Small adjustments make a significant difference to the quality of the hinge.

### Layer Height

Use **0.15mm to 0.2mm** layer height for hinge sections. Thinner layers produce better bonding between layers, which helps the hinge survive repeated flexing. At 0.3mm layers the hinge section may not bond reliably enough.

### Print Speed

**Slow down significantly.** TPU does not behave well at high speeds. Print the entire part at **20 to 30mm/s** maximum. The hinge section specifically benefits from a slow, steady extrusion that gives the filament time to bond properly.

If your slicer allows you to set a per-feature speed, reduce the speed for outer walls and top/bottom layers even further, to around 15mm/s.

### Wall Count

Use a **wall count of 3 or more** for the rigid sections of the part. The hinge section itself will likely be too thin for multiple walls at its narrowest point, but the surrounding structure benefits from extra perimeters.

### Infill

For the rigid panels of a print-in-place hinge, **40 to 60% infill** gives a good balance of rigidity and weight. Rectilinear or gyroid infill patterns both work well with TPU.

### No Supports

Avoid supports inside or near the hinge wherever possible. Support material that contacts the hinge surface leaves marks and can cause the thin hinge to tear when you remove it. Design your model so the hinge overhangs do not require support, or angle the print slightly to avoid overhangs at the hinge section entirely.

### Retraction

TPU is prone to stringing and does not respond well to aggressive retraction. Reduce retraction distance to **1 to 2mm** for Bowden setups or **0.5 to 1mm** for direct drive. Reduce retraction speed to around **20 to 25mm/s**. Excessive retraction can strip or deform TPU and cause inconsistent extrusion at the critical hinge section.

---

## Common Problems and Fixes

### Delamination at the Hinge

**Symptom:** The hinge tears apart along layer lines after a small number of flex cycles.

**Cause:** The hinge is oriented so that flexing pulls the layers apart. This is almost always an orientation problem.

**Fix:** Re-orient the model so the hinge flexes across the layers rather than along them. If that is not possible with the current design, redesign the hinge geometry so it runs vertically in the print.

A secondary cause can be print speed. If you are printing too fast, layers do not bond as well. Slow down to 20mm/s and check whether adhesion improves.

### Hinge Too Stiff to Open Easily

**Symptom:** The hinge requires significant force to flex and does not return smoothly to a flat position.

**Cause:** The hinge section is too thick, the TPU shore hardness is too high, or the hinge geometry is too short.

**Fix:** Reduce hinge thickness in your model by 0.1mm to 0.2mm at a time and reprint to test. If you are using a 98A TPU, try a 95A or 87A grade. Lengthening the hinge section (the dimension along the flex axis) also distributes the bend over more material, making it feel softer to open.

### Stringing Through the Hinge

**Symptom:** Fine threads of TPU cross the open area of the hinge, or blob onto the surface.

**Cause:** TPU strings easily at high temperatures or with incorrect retraction settings.

**Fix:** Reduce print temperature by 5 degrees and check retraction settings are appropriate for TPU (see slicer settings section above). Ensure travel moves across the hinge are minimised in your slicer's travel path settings.

---

## Practical Use Cases

Living hinges in TPU are useful across a wide range of practical prints.

**Snap-fit cases and lids** - tool cases, pill organisers, and storage boxes with integral lids are much more useful when the lid stays attached.

**Cable management clips** - a hinged clip that snaps around cables does not require threading cables through a hole.

**Flexible phone stands and mounts** - adjustable stands that stay at any angle benefit from a TPU hinge that holds position under slight friction.

**Wearable parts** - bracelets, watch straps, and flexible costume accessories can use living hinges to add articulation without visible mechanical joins.

**Locking enclosures** - electronics cases with a latch on one side and a living hinge on the other are fully printable in a single piece.

---

## Related Guides

- [TPU Flexible Filament: A Beginner's Guide](/posts/tpu-flexible-filament-beginners-guide/)
- [How to Fix 3D Printer Stringing](/posts/how-to-fix-3d-printer-stringing/)
