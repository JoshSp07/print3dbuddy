# How to Fix 3D Printer Stringing: 7 Settings to Adjust

If your 3D prints look like they've been attacked by a spider, you're dealing with stringing  -  one of the most common problems beginners run into. The good news? It's almost always fixable with a few slicer tweaks. This guide walks you through the 7 most effective settings to adjust to get clean, string-free prints.

---

## What Is 3D Printer Stringing?

Stringing (sometimes called "oozing" or "hairy prints") happens when your printer nozzle drags molten filament across open gaps in your print, leaving thin threads of plastic behind. It looks messy, it's a pain to clean up, and it's a sign that your printer settings aren't quite dialled in.

The root cause is almost always excess molten plastic leaking from the nozzle while the print head moves between two points. The fix involves either pulling that plastic back (retraction), reducing how much oozes out in the first place (temperature), or moving faster so there's less time for plastic to drip.

---

## 7 Settings to Fix Stringing

### 1. Increase Retraction Distance

Retraction is the single most important setting for stringing. When the print head moves between two parts of your model, the printer pulls the filament backwards slightly to reduce pressure in the nozzle, so it doesn't ooze.

**What to try:**
- For direct drive extruders (like those on the Bambu Lab P1S or Prusa MK4): start at 0.5 - 1mm
- For Bowden setups (like many Creality Enders): start at 4 - 6mm and work up to 7 - 8mm if needed

Increase retraction in 0.5mm increments and test with a stringing test model (there are plenty of free ones on Printables and Thingiverse).

**Too much retraction** causes under-extrusion and clogs  -  so don't go overboard.

---

### 2. Increase Retraction Speed

It's not just how far you retract  -  it's how fast. A slow retraction gives molten plastic more time to ooze before it's pulled back.

**What to try:** Most printers do well between 25 - 45mm/s. Push direct drive setups toward the faster end. If you're getting grinding or skipping sounds, dial it back.

---

### 3. Lower Your Print Temperature

Hotter filament is more liquid, which means it drips and strings more easily. Dropping your nozzle temperature by 5 - 10°C can make a surprising difference.

**What to try:**
- PLA typically prints well between 190 - 220°C. If you're at 215°C and getting stringing, try 205°C.
- PETG is trickier  -  it needs higher temps but also strings more. Try 230°C before going higher.

Always do a temperature tower test when dialling in a new filament brand  -  it'll show you exactly where stringing starts.

---

### 4. Enable or Increase "Avoid Crossing Perimeters" / "Combing"

Most slicers (Bambu Studio, Cura, PrusaSlicer) have a setting that forces the print head to travel over already-printed areas rather than crossing open gaps. Less open-air travel means less stringing.

- In **Cura**: look for "Combing Mode"  -  set it to "All" or "Not in Skin"
- In **PrusaSlicer/BambuStudio**: look for "Avoid crossing perimeters"

This setting alone can dramatically reduce stringing without changing any temperatures.

---

### 5. Increase Travel Speed

The faster the nozzle moves between points, the less time molten plastic has to drip. This is a simple win.

**What to try:** Most printers can handle 150 - 200mm/s for travel moves. Increase your travel speed in your slicer's speed settings. This won't affect print quality since no plastic is being extruded during travel.

---

### 6. Enable "Wipe Before Retract" or "Coast at End"

These are small but useful features:

- **Wipe before retract** (Cura): The nozzle wipes along the outer edge of the print before retracting, cleaning off excess filament.
- **Coast at end** (Simplify3D / some slicers): The printer stops extruding slightly before the end of a line, using residual pressure to finish  -  reducing ooze at travel start points.

Not every slicer has both options, but enable whichever ones you have access to.

---

### 7. Lower Your Minimum Travel Distance for Retraction

If your slicer is set to only retract when moving more than 5mm, short hops between nearby features won't trigger retraction at all  -  and those are often the ones causing strings.

**What to try:** Lower your "minimum travel for retraction" to 1 - 2mm. This means retraction kicks in more often, which helps with detailed models that have lots of small features.

---

## Still Stringing? Check These Too

If you've adjusted all the settings above and still have issues:

- **Wet filament** strings badly. PLA and PETG both absorb moisture from the air. Try drying your filament in a food dehydrator (https://www.amazon.com/s?k=food+dehydrator+filament+drying) or a filament dryer box (https://www.amazon.com/s?k=filament+dryer+box+3d+printing) for 4 - 6 hours.
- **Worn nozzle**: A partially blocked or worn brass nozzle can cause inconsistent flow and stringing. Replacement nozzles are cheap  -  grab a pack (https://www.amazon.com/s?k=replacement+brass+nozzle+0.4mm+3d+printer).
- **Calibrate your extruder**: If your e-steps are off, you may be over-extruding consistently, which makes stringing much worse.

---

## Best Printers for Low-Stringing Out of the Box

Some printers are better tuned for stringing from the factory than others. The **Bambu Lab A1 Mini** (https://bambulab.com/en/bambu-lab/a1-mini) and **Bambu Lab P1S** (https://bambulab.com/en/bambu-lab/p1s) are well-regarded for minimal stringing thanks to their direct drive systems and well-tuned default profiles. If you're still shopping for a printer, that's worth considering.

The **Creality Ender 3 V3** (https://www.amazon.com/s?k=Creality+Ender+3+V3) is a great budget option but uses a Bowden setup, so you'll likely spend a bit more time tuning retraction.

---

## Quick Reference: Anti-Stringing Settings Cheatsheet

| Setting | Bowden | Direct Drive |
|---|---|---|
| Retraction Distance | 4 - 7mm | 0.5 - 1.5mm |
| Retraction Speed | 40 - 60mm/s | 25 - 45mm/s |
| Print Temperature | Reduce by 5 - 10°C | Reduce by 5 - 10°C |
| Travel Speed | 150 - 200mm/s | 150 - 200mm/s |
| Combing/Avoid Crossing | Enable | Enable |

---

## Final Thoughts

Stringing is frustrating, but it's one of those problems that clicks once you understand what's causing it. Work through these 7 settings one at a time  -  change one thing, run a test print, and compare. Changing multiple things at once makes it impossible to know what actually worked.

If you want to speed up your testing, print a dedicated stringing test model (free on Printables)  -  it only takes 10 - 15 minutes and gives you clear results.

Ready to upgrade your setup? Check the current price on Amazon for a quality filament dryer (https://www.amazon.com/s?k=filament+dryer+box+3d+printing)  -  it's one of the best investments you can make for consistent prints.
