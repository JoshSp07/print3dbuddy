# How to Calibrate Your First 3D Printer: Step-by-Step Guide

Getting your first 3D printer set up properly is the single most important thing you can do for print quality. A poorly calibrated printer produces warped bases, bad layer adhesion, blobs, gaps, and endless frustration. A well-calibrated printer produces clean, consistent prints every time.

**This guide covers everything you need to calibrate a new 3D printer**, in the order you should actually do it. Follow these steps and you'll avoid the most common beginner pitfalls.

---

## Why Calibration Matters

Calibration isn't just a one-time setup step  -  it's an ongoing process, especially in the early days with a new machine. Think of it like tuning a musical instrument: even a great guitar sounds off if it hasn't been set up properly.

The good news is that most calibration steps only need to be done once (or after major maintenance). And modern printers like the Bambu Lab series handle much of this automatically. But understanding what each step does will help you troubleshoot problems down the line, whatever printer you're using.

---

## Step 1: Level the Bed (or Check Auto-Levelling)

Bed levelling is the foundation of everything. If your bed isn't level, your first layer won't adhere correctly, and a bad first layer means a failed print.

### Manual Bed Levelling

If your printer has manual bed levelling (common on budget Creality machines):

1. Heat your bed to printing temperature first (surfaces expand slightly when hot)
2. Home all axes
3. Disable steppers so you can move the print head by hand
4. Move the nozzle to each corner of the bed
5. Slide a piece of paper under the nozzle  -  you want slight friction, not tight resistance
6. Adjust the bed knobs until the paper drags consistently at all four corners
7. Check the centre last

**Repeat this process 2 - 3 times**, because adjusting one corner affects the others slightly.

### Auto Bed Levelling (ABL)

Many modern printers include automatic bed levelling using a probe (BLTouch, CRTouch, or built-in inductive sensors). With ABL:

- Run the bed mesh levelling routine from your printer's menu
- The printer maps the height variations across the bed and compensates during printing
- You still need to set your Z offset correctly (see Step 2)

[The **Bambu Lab A1 Mini**](https://www.amazon.co.uk/s?k=Bambu+Lab+A1+Mini&tag=print3dbuddy2-21) [and **P1S**](https://www.amazon.co.uk/s?k=Bambu+Lab+P1S&tag=print3dbuddy2-21) use multi-point automatic levelling that's exceptionally accurate out of the box  -  one of the reasons they're so popular with beginners.

---

## Step 2: Set Your Z Offset (First Layer Height)

Your Z offset is the gap between the nozzle and the bed when printing starts. Get this wrong and your first layer either won't stick (too high) or will be smashed flat and cause a clog (too low).

**What a good first layer looks like:** slightly squished, with lines that bond together but don't overlap excessively. You should be able to see individual lines, but they should fuse at the edges.

### How to Set Z Offset

1. Start a first-layer calibration print (most slicers include one, or print a single-layer square)
2. Watch the first layer carefully
3. If the filament isn't sticking or is coming out as a rounded blob, the nozzle is too high  -  reduce your Z offset (move nozzle closer to bed)
4. If the nozzle is dragging through what it just laid down, or the filament looks squashed flat with rough edges, you're too low  -  increase your Z offset

Adjust in 0.05mm increments and reprint until it looks right. This step is worth taking your time on.

---

## Step 3: Calibrate Your Extruder (E-Steps)

E-steps (extruder steps per millimetre) tell your printer how many motor steps are needed to push 1mm of filament through the extruder. If this is wrong, you'll either over-extrude (blobs, rough surfaces, stringing) or under-extrude (gaps, weak layers, poor adhesion).

### How to Calibrate E-Steps

1. Mark your filament 100mm and 120mm from the entry point of your extruder
2. Command your printer to extrude exactly 100mm of filament (via the control menu or a terminal)
3. Measure how much filament actually moved
4. If it extruded 95mm instead of 100mm, your e-steps are too low  -  calculate the correction:

**New E-steps = (Current E-steps × 100) ÷ Actual mm extruded**

5. Update the value in your printer's firmware settings and save

**Note:** Many modern printers come factory-calibrated for e-steps. Check if yours needs this step before diving in  -  Bambu Lab printers, for example, handle this automatically.

---

## Step 4: Run a Temperature Tower Test

Different filament brands and even different colours of the same brand can behave differently at various temperatures. A temperature tower is a single print that tests multiple temperatures in one go.

1. Download a temperature tower model from Printables (free)  -  [search "temp tower"]
2. Use your slicer's "change filament at height" or custom G-code feature to step the temperature down every 5mm or so
3. Test from 230°C down to 190°C for PLA (adjust range for other materials)
4. Look at each section: where does stringing stop? Where does surface quality peak? Where do overhangs start drooping?

The temperature range that gives you the cleanest results is your sweet spot. Note it down for each filament brand you use.

---

## Step 5: Calibrate Flow Rate / Extrusion Multiplier

Even with correct e-steps, flow rate can be slightly off due to filament diameter variations between brands. Calibrating flow rate ensures you're extruding exactly the right amount of plastic.

### Simple Flow Rate Test

1. Print a single-wall cube (20mm × 20mm × 20mm, 0 infill, 0 top layers, 1 perimeter)
2. [Measure the wall thickness with digital calipers](https://www.amazon.co.uk/s?k=digital+calipers+3d+printing&tag=print3dbuddy2-21)
3. Your slicer's set line width is what you're aiming for (usually 0.4 - 0.45mm for a 0.4mm nozzle)
4. If your wall is 0.48mm thick, you're over-extruding  -  reduce flow rate proportionally
5. If it's 0.37mm, you're under-extruding  -  increase flow rate

Adjust in 2 - 3% increments. A good set of [digital calipers is essential for this step  -  check the current price on Amazon](https://www.amazon.co.uk/s?k=Creality+Ender+3+V3+SE&tag=print3dbuddy2-21).

---

## Step 6: Test Retraction Settings

Retraction controls how much filament is pulled back when the nozzle travels between two parts of a print. Incorrect retraction causes stringing or gaps.

1. Print a retraction test model (available free on Printables)
2. Start with recommended values for your printer type (see our stringing guide for specifics)
3. Adjust retraction distance and speed based on what you see

---

## Step 7: Print a Calibration Cube

Once you've worked through the steps above, print a 20mm calibration cube. This is the classic final test.

**What to check:**
- Dimensions: measure with calipers  -  should be within 0.2mm of 20mm on all sides
- Top surface: should be smooth with no gaps or blobs
- Corners: should be sharp, not rounded or blobby
- Walls: should be smooth, no visible layer lines wobbling or shifting

If something's off, you now know what each setting controls, so you can go back and adjust.

---

## Calibration Tools Worth Having

- [**Digital calipers**  -  essential for measuring prints accurately](https://www.amazon.co.uk/s?k=digital+calipers+3d+printing&tag=print3dbuddy2-21)
- [**Filament dryer**  -  wet filament causes all kinds of calibration headaches](https://www.amazon.co.uk/s?k=filament+dryer+box+3d+printing&tag=print3dbuddy2-21)
- **Bed adhesi[on spray or PEI sheet**  -  consistent bed adhesion makes calibration much easier](https://www.amazon.co.uk/s?k=PEI+sheet+3d+printer&tag=print3dbuddy2-21)
- **Good lighting**  -  being able to see your first layer clearly makes a huge difference

---

## How Often Do You Need to Calibrate?

- **Bed level**: Check whenever prints start failing at the first layer, or after moving the printer
- **Z offset**: Only when you change nozzles or the bed surface
- **E-steps**: Once, and again after any extruder hardware changes
- **Flow rate**: Once per filament brand/type
- **Temperature**: Once per filament brand/type

---

## Final Thoughts

Calibration sounds daunting, but work through it step by step and you'll build a solid understanding of how your printer behaves. Most of these steps take 30 - 60 minutes total, and once done, you'll be getting clean prints consistently.

If you're still choosing a printe[r and want something that minimises calibration effort, the **Bambu Lab A1 Mini**](https://www.amazon.co.uk/s?k=Bambu+Lab+A1+Mini&tag=print3dbuddy2-21) automates most of these steps. For a h[ands-on learning experience with a budget machine, the **Creality Ender 3 V3 SE**](https://www.amazon.co.uk/s?k=Creality+Ender+3+V3+SE&tag=print3dbuddy2-21) [is a classic choice  -  check the current price on Amazon](https://www.amazon.co.uk/s?k=Creality+Ender+3+V3+SE&tag=print3dbuddy2-21).

---

## Recommended Settings for Every Material

Once you're calibrated, the next question is always "what temperature and speed should I use for this filament?" Our free [Print Settings Cheat Sheet](https://tools.print3dbuddy.com) covers 15 materials including PLA, PETG, ABS, ASA, TPU, Nylon, and PC - with nozzle temperature, bed temperature, retraction, cooling, and first layer speed, adjusted for your extruder type. [Look up your filament at tools.print3dbuddy.com](https://tools.print3dbuddy.com).
