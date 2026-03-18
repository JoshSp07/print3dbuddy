# How to Reduce 3D Print Time Without Ruining Quality

A print that takes 8 hours doesn't have to. Most prints can be cut to 3-4 hours with the right slicer settings - without meaningfully affecting how the finished part looks or performs.

Here's how to print faster without sacrificing what matters.

---

## 1. Increase Layer Height

Layer height has the biggest single impact on print time. Doubling layer height roughly halves print time.

| Layer Height | Quality | Time |
|---|---|---|
| 0.1mm | Very high detail | Very slow |
| 0.2mm | Standard | Standard |
| 0.25mm | Good | ~20% faster |
| 0.3mm | Functional | ~35% faster |

**For functional parts** where surface finish isn't critical, 0.3mm is often the right call. **For visible display pieces**, stay at 0.2mm.

---

## 2. Reduce Infill

Most prints don't need more than 15-20% infill. Reducing infill from 40% to 20% cuts print time noticeably while keeping the part functional for most purposes.

**Rule:** Use the minimum infill that meets your strength requirements. Check our [infill guide](/posts/3d-printing-infill-patterns-guide/) for recommendations.

Also switch to **lightning infill** for purely decorative items - it's the fastest pattern available.

---

## 3. Increase Print Speed (Carefully)

Modern printers can print significantly faster than their defaults suggest. The key is understanding what you can push without degrading quality.

**What you can usually speed up:**
- **Infill:** Push to 100-150mm/s without visible quality loss
- **Travel moves:** 150-200mm/s is generally fine
- **Inner walls:** 80-100mm/s

**What to keep slower:**
- **Outer walls:** Keep at 40-60mm/s - this is what you see
- **First layer:** Always 20-25mm/s

A practical approach: set your overall speed to 80-100mm/s and manually reduce outer wall speed to 50mm/s. You get fast prints that still look good.

---

## 4. Increase Nozzle Size

Swapping from 0.4mm to 0.6mm nozzle dramatically increases flow rate, allowing faster printing or thicker layer heights without under-extrusion.

A 0.6mm nozzle at 0.3mm layer height produces prints that are:
- Much faster (often 50-60% less time)
- Slightly coarser in appearance
- Often stronger (thicker layers bond differently)

[0.6mm nozzle for Ender 3 / MK8](https://www.amazon.com/s?k=0.6mm+MK8+brass+nozzle) costs a few pounds and is one of the best speed upgrades available.

---

## 5. Reduce Perimeter/Wall Count

More walls = stronger print but longer print time. For decorative items that won't be stressed, 2 walls is plenty. For functional parts, 3 walls is usually sufficient - you rarely need more than 4.

---

## 6. Optimise Support Settings

Supports are slow to print and slow to remove. Minimise them where possible:

- **Reorient the model** to reduce overhangs - sometimes rotating 90 degrees eliminates supports entirely
- **Use support enforcers/blockers** to add supports only where truly needed
- **Reduce support density** - 10-15% is usually enough
- **Use tree supports** (in PrusaSlicer or Bambu Studio) - faster to print and easier to remove than grid supports

---

## 7. Use Adaptive Layer Heights

PrusaSlicer and Bambu Studio both support variable/adaptive layer heights - thick layers on simple geometry, thin layers only where detail matters.

Enable it under **Layer Height > Variable Layer Height**. The result: detail where it counts, speed everywhere else.

---

## 8. Reduce Top and Bottom Layers

Default top/bottom layer counts are often conservative. For non-functional parts:
- **Bottom layers:** 2-3 is usually enough
- **Top layers:** 3-4 is enough for most infill percentages

Reducing from 5 top layers to 3 won't affect appearance much but saves meaningful time on flat-topped models.

---

## 9. Combine Settings for Maximum Impact

The biggest gains come from combining settings. Example transformation:

**Original settings:**
- 0.2mm layer height
- 20% infill (grid)
- 50mm/s print speed
- 4 walls, 5 top/bottom layers

**Optimised for speed (functional part):**
- 0.3mm layer height
- 15% infill (lightning)
- 80mm/s print speed (outer walls at 50mm/s)
- 3 walls, 3 top/bottom layers

**Result:** Often 50-60% faster with little visible quality difference for everyday parts.

---

## 10. Enable Arachne Perimeter Generator

Arachne (available in PrusaSlicer and Cura) produces more efficient wall paths than the classic perimeter generator. It's particularly effective for thin features and reduces redundant moves.

Enable under **Perimeters > Perimeter generator > Arachne** in PrusaSlicer.

---

## When NOT to Optimise for Speed

Some situations where you should print slower and with more care:

- **Miniatures and detailed models** - detail is the point
- **First prints on a new filament** - understand the material before pushing it
- **Parts under significant mechanical stress** - more walls and infill matter
- **Overhangs and bridges** - slow down in these areas to avoid drooping

---

## Summary: Quick Wins in Order

1. **Layer height to 0.3mm** - biggest single time saving
2. **Infill to 15-20%** if strength allows
3. **Increase infill speed** to 100mm/s, keep outer walls at 50mm/s
4. **Lightning infill** for decorative items
5. **0.6mm nozzle** if you print large functional parts regularly

Making just the first two changes will cut most prints by 30-40% without any visible quality difference.

---

## See the Impact Before You Print

Wondering how much time and filament you'll actually save by bumping infill down or switching to a larger nozzle? Our free [STL Filament Estimator](https://tools.print3dbuddy.com) lets you upload your model and instantly compare filament usage across different settings. It's the fastest way to find the right balance between speed and material cost. [Try it free at tools.print3dbuddy.com](https://tools.print3dbuddy.com).
