# Resin 3D Printing: Complete Beginner's Guide

Resin 3D printing produces detail that FDM (filament) printers simply can't match - smooth surfaces, sharp edges, and fine features that look almost injection-moulded straight off the build plate. The tradeoff is more setup, messier post-processing, and a few safety precautions you genuinely need to follow. This guide covers everything you need to get started: how it works, what to buy, how to set it up, and how to get good results from your first print.

---

## How Resin Printing Works

Resin printers (MSLA printers, specifically) use an LCD screen to project UV light upward through a clear FEP film at the bottom of a resin vat. The UV-sensitive liquid resin sitting above the film hardens wherever the light hits it - one thin layer at a time. The build plate starts at the bottom of the vat, lifts slightly between each layer, and slowly pulls your print upward as it forms.

Because each layer is exposed all at once (not drawn point-to-point like FDM), resin printers can produce extremely fine detail regardless of model complexity. A detailed miniature takes the same time as a simple cube, as long as they're the same height.

**Key differences from FDM:**
- Much higher detail - 0.05mm layers vs 0.1-0.3mm on FDM
- Prints require washing in IPA and UV curing after printing
- Resin is a skin and eye irritant - gloves and ventilation are non-negotiable
- Prints are more brittle than FDM unless you use engineering resins
- Supports are often needed even for simple shapes

---

## Safety First

Uncured resin is a skin sensitiser. Repeated skin contact without protection can cause allergic reactions that get worse over time. This isn't scare-mongering - it's something you need to take seriously from your first print.

**Minimum safety requirements:**
- **Nitrile gloves** - always, whenever handling liquid resin or uncured prints
- **Safety glasses** - resin splashes, especially when removing the FEP or draining the vat
- **Ventilation** - resin fumes are unpleasant and potentially harmful with prolonged exposure. Print near an open window, in a garage, or with a carbon filter enclosure

**[Nitrile gloves (box of 100) on Amazon UK](https://www.amazon.co.uk/s?k=nitrile+gloves+100+box&tag=print3dbuddy2-21)**

Once your print is fully cured (hard, no longer tacky), it's safe to handle without gloves. The washing and curing stage is where most exposure happens - treat all wash liquid and uncured prints the same as the liquid resin itself.

---

## Choosing a Resin Printer

### Budget (under £200) - Elegoo Saturn 2 / Anycubic Photon Mono M5

For most beginners, the Elegoo Saturn 2 or the Anycubic Photon Mono M5 are the go-to recommendations. Both offer a large-ish build plate (around 218x123mm), a fast mono LCD screen, and well-established community support.

If you want the smallest footprint and lowest cost, the Elegoo Mars 4 Ultra is a solid choice with a smaller 153x77mm build plate - plenty for miniatures and small models.

**[Elegoo Mars 4 Ultra on Amazon UK](https://www.amazon.co.uk/s?k=elegoo+mars+4+ultra&tag=print3dbuddy2-21)**

**[Anycubic Photon Mono M5 on Amazon UK](https://www.amazon.co.uk/s?k=anycubic+photon+mono+m5&tag=print3dbuddy2-21)**

### What to look for

- **Mono LCD screen** - essential. Older RGB screens are much slower. All current printers use mono screens.
- **Build plate size** - larger means you can print more at once, but takes up more space
- **Resolution** - most modern printers are between 4K and 12K. Higher resolution = finer detail, though the difference is most visible on very small prints

---

## What Else You'll Need

### Wash and Cure Station

After printing, you wash parts in isopropyl alcohol (IPA) to remove uncured resin, then cure them under UV light to harden fully. You can do this with a glass jar of IPA and a UV nail lamp, but a dedicated wash and cure machine makes the process much less messy.

The Elegoo Mercury Plus is the most popular choice and works well with any printer brand.

**[Elegoo Mercury Plus Wash and Cure on Amazon UK](https://www.amazon.co.uk/s?k=elegoo+mercury+plus+wash+cure&tag=print3dbuddy2-21)**

### Isopropyl Alcohol (IPA)

You need 90%+ IPA for washing. Lower concentrations have too much water and don't clean resin effectively. Buy a litre or two to start - it goes faster than you expect.

**[Isopropyl Alcohol 99% on Amazon UK](https://www.amazon.co.uk/s?k=isopropyl+alcohol+99+percent+1+litre&tag=print3dbuddy2-21)**

### Resin

Start with a standard PLA-like resin from Elegoo or Anycubic. It's the easiest to work with, smells the least offensive, and produces good results out of the box.

- **Elegoo Standard Resin** - reliable, well-supported exposure settings
- **Anycubic Eco Resin** - slightly lower odour than most
- **Siraya Tech Blu** - tougher and less brittle than standard resin, popular for functional parts

---

## Resin Settings Explained

Unlike FDM where you adjust temperature and speed, resin printing is mainly about exposure time - how long the UV light stays on for each layer.

| Setting | What it does | Starting point |
|---------|-------------|----------------|
| Layer exposure time | How long each layer is cured | 2-3s for most mono screens |
| Bottom layers | First N layers, exposed longer to grip the plate | 4-6 layers |
| Bottom exposure time | Exposure for those first layers | 30-45s |
| Layer height | Thinner = more detail, slower print | 0.05mm detail, 0.1mm speed |
| Lift speed | How fast the plate lifts between layers | 2-3mm/s (slower = fewer failures) |

These starting values are for standard resins on modern mono screens. The best source for your specific printer/resin combination is the [Chitubox exposure finder](https://www.chitubox.com/en) community settings database - most common combinations are already there.

---

## Supports in Resin Printing

Almost everything in resin printing needs supports - not just overhangs. Because the model is being pulled upward off a sticky FEP film, large flat areas (islands) will tear away from the rest of the print if they're not supported from above.

Most slicers (Chitubox, Lychee Slicer) have auto-support that works reasonably well. For important prints, check for unsupported islands manually.

**Key support tips:**
- Tilt your model at 30-45 degrees when possible - reduces flat contact with the FEP and requires fewer supports
- Light supports are usually enough - you don't need heavy FDM-style supports
- Place supports on areas that won't show - hidden undersides, not visible surfaces

**Slicers to try:**
- **Chitubox** - most widely used, good auto-support
- **Lychee Slicer** - better island detection, slightly more complex

---

## Post-Processing: Wash and Cure

### Step 1 - Remove from build plate

Use a plastic scraper or the metal one that comes with most printers. Wear your gloves. Some prints pop off easily; others need firm pressure along the edge. Don't flex the build plate - you'll knock off your calibration.

### Step 2 - Wash

Submerge in IPA for 2-3 minutes. Agitate or use a wash station's spinning basket. Don't leave prints soaking for more than 5-6 minutes - resin can absorb IPA and become weak if over-washed.

### Step 3 - Dry

Let prints air dry for 5-10 minutes before curing. Curing wet prints traps IPA and can cause cloudiness on the surface.

### Step 4 - Cure

Expose to UV light until fully hardened. A dedicated cure station takes 2-4 minutes. Direct sunlight also works but takes longer and is weather-dependent. Fully cured resin should feel hard, not rubbery or tacky.

---

## Common Resin Problems

### Print detaches mid-print

The most common resin failure. Usually caused by:
- Bottom exposure too short - increase bottom exposure time by 5s at a time
- Lift speed too fast - reduce to 1.5-2mm/s
- Build plate not level or not adhesive enough - re-level and try a light sand of the plate

### Layer lines or banding

Usually caused by inconsistent FEP tension or a dirty FEP. Check the FEP for scratches, cloudiness, or debris. Replace it if damaged (they cost around £5 and are consumable).

### Supports breaking mid-print

- Increase support tip diameter slightly
- Add more contact points - resin supports are cheap (just a bit more resin)
- Slow down the lift speed

### Cloudy or white patches

Usually from over-washing or washing before fully drying. Pat dry before curing next time.

---

## Calibrating Exposure

If you're getting delamination, weak prints, or prints that won't stick, print an exposure calibration matrix (commonly called a "Resin XP2 Validation Matrix"). It's a quick print that shows you a range of exposure times simultaneously so you can find the sweet spot for your resin/printer combination in one print.

We'd also recommend a [first layer calibration print](https://tools.print3dbuddy.com/test-prints#first-layer-test) once you've got your exposure dialled in - a flat grid that shows quickly whether your plate is level and your z-offset is correct.

---

## Summary

Resin printing has a steeper setup curve than FDM but the results are genuinely impressive. The main things to get right:

1. **Safety** - gloves and ventilation, every time
2. **Levelling** - most failed prints trace back to this
3. **Exposure time** - use community settings for your specific printer and resin
4. **Supports** - don't skip them, tilt models when you can
5. **Wash and cure properly** - don't rush it

Once you've got those five things right, resin printing is surprisingly reliable.
