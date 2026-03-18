# 3D Printing Infill: Patterns, Percentages, and When to Use Each

Infill is the internal structure of a 3D print - the lattice of plastic inside solid-looking parts. Choosing the right infill pattern and percentage has a bigger impact on strength, weight, and print time than most beginners realise.

---

## What Is Infill?

When your slicer processes a model, it creates:
- **Outer walls/perimeters** - the visible shell
- **Top and bottom layers** - solid flat surfaces
- **Infill** - the internal structure connecting everything

The infill percentage controls how densely packed this internal structure is. 0% infill = completely hollow (fragile). 100% infill = completely solid (strong but heavy and slow).

Most prints don't need 100% infill. A 20% infill with the right pattern is surprisingly strong.

---

## Infill Percentage Guide

| Percentage | Strength | Use Case |
|---|---|---|
| 0% | Very weak | Display models, decorative items you won't handle |
| 5-10% | Weak | Lightweight decorative items |
| 15-20% | Moderate | General household objects, display pieces |
| 25-40% | Good | Functional parts with moderate loads |
| 50-60% | Strong | Load-bearing parts, brackets, clips |
| 80-100% | Very strong | Maximum strength parts, impact-absorbing pieces |

**Default starting point:** 15-20% for decorative items, 40% for functional parts. You rarely need more than 40% unless the part will be under significant stress.

---

## Infill Patterns Explained

### Grid / Lines

The simplest pattern - two sets of lines crossing at 90 degrees. Fast to print and reasonably strong in the XY plane.

**Best for:** General use, fast printing. The default in most slicers.

### Gyroid

A complex three-dimensional wave pattern. Strong in all directions, good for flexible materials, and has an unusual aesthetic when visible through walls.

**Best for:** Parts that need strength in multiple directions, especially those under torsion or multi-axis loads. Popular choice for functional parts.

### Honeycomb

Hexagonal cells, similar to natural honeycomb structure. Excellent strength-to-weight ratio, though slower to print than grid.

**Best for:** Lightweight structural parts where strength matters.

### Cubic / 3D Honeycomb

A 3D version of honeycomb with diagonal bracing in all three planes. Very strong in all directions.

**Best for:** Parts under compression or multi-directional loading.

### Concentric

Follows the outline of the model inward in concentric rings. Weak structurally but produces beautiful top surfaces and is excellent for flexible prints.

**Best for:** Flexible parts (TPU), artistic pieces where top surface matters.

### Lightning

Minimal internal structure that just supports the top layers - not a traditional infill pattern. Produces the lightest prints possible.

**Best for:** Display items and decorative pieces where weight and material savings matter. Not suitable for functional parts.

### Rectilinear / Lines (Directional)

Lines printed in a single direction per layer. Very fast, less strong than grid in one axis.

**Best for:** Fast drafts and prototypes.

---

## How Infill Affects Print Time and Strength

Increasing infill from 15% to 40% roughly doubles print time for the infill layers, but doesn't double strength. The majority of a part's strength comes from:

1. **Perimeter/wall count** - more walls = more strength, often more effectively than more infill
2. **Top/bottom layer count** - affects surface quality and part integrity
3. **Print orientation** - direction of layers relative to load

For maximum strength with minimal print time increase: **increase wall count to 4-5 before increasing infill beyond 30%**. This is often more effective.

---

## Practical Recommendations

### Decorative / Display Items
- **Infill:** 10-15%
- **Pattern:** Grid or lightning
- **Walls:** 2-3
- **Result:** Light, fast, looks good

### General Functional Parts (Hooks, Brackets, Clips)
- **Infill:** 30-40%
- **Pattern:** Gyroid or cubic
- **Walls:** 3-4
- **Result:** Good strength, reasonable print time

### High-Stress Parts (Tool handles, load-bearing brackets)
- **Infill:** 50-60%
- **Pattern:** Gyroid or cubic
- **Walls:** 4-5
- **Result:** Strong and durable

### Flexible Parts (TPU gaskets, phone cases)
- **Infill:** 20-40%
- **Pattern:** Concentric or gyroid
- **Walls:** 3-4
- **Result:** Flexible with good durability

### Maximum Strength (Impact resistance, safety-critical)
- **Infill:** 80-100%
- **Pattern:** Rectilinear or cubic
- **Walls:** 5+
- **Result:** Very strong, heavy, slow to print

---

## Infill Overlap

Most slicers have an "infill overlap" setting - how much the infill overlaps with the inner wall. A value of 20-25% is typical and ensures good bonding between infill and walls.

If you're seeing separation between infill and walls, increase infill overlap slightly.

---

## Visual Infill (Seeing Through the Top)

If your top layers look bumpy or you can see the infill pattern through them, you need more top layers. Most slicers default to 3-4 top layers - increase to 5-6 for a smoother top surface, especially at low infill percentages.

---

## Summary

- **Default:** 15-20% gyroid or grid for most prints
- **Functional parts:** 40% gyroid with 4 walls
- **Increase wall count before increasing infill** for better strength
- **Lightning infill** for lightweight decorative pieces
- **Concentric** for flexible parts and aesthetic tops

Most of the time, changing the infill pattern matters less than the percentage and wall count. Gyroid is a solid default for anything functional - it's strong in all directions and the extra print time is minimal.

---

## Know Exactly How Much Filament You'll Use

Choosing your infill percentage is much easier when you can see the impact on filament usage before you print. Our free [STL Filament Estimator](https://tools.print3dbuddy.com) lets you upload your model and test different infill percentages, wall counts, and layer heights - instantly showing you the estimated weight, filament length, and cost. No guesswork, no wasted plastic. [Try it free at tools.print3dbuddy.com](https://tools.print3dbuddy.com).
