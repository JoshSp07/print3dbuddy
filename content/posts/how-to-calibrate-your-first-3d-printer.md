# How to Calibrate Your First 3D Printer: Step-by-Step Guide

Most new printer problems are calibration problems. Warped bases, bad adhesion, gaps in layers, blobbing on corners - these all trace back to settings that are slightly off from the start. Spending an hour on calibration when you first set up saves dozens of hours troubleshooting later.

This is the order to do it in, and what to actually look for at each step.

---

## Step 1: Level the Bed (or Check Auto-Levelling)

Everything depends on bed levelling. A first layer that is not evenly adhered across the whole bed will fail regardless of what else you do.

### Manual Bed Levelling

1. Heat the bed to printing temperature first - the surface expands slightly when hot and the readings will be different cold
2. Home all axes
3. Disable steppers so you can move the print head by hand
4. Move the nozzle to each corner of the bed
5. Slide a piece of paper under the nozzle - you want slight friction, not tight resistance and not free movement
6. Adjust the bed knobs until you get consistent drag at all four corners
7. Check the centre last

Go around twice. Adjusting one corner affects the others slightly, so a single pass is rarely enough.

### Auto Bed Levelling (ABL)

Run the bed mesh levelling routine from your printer's menu. The printer maps the height variations and compensates during printing. This is accurate and saves a lot of manual fiddling.

Important: auto bed levelling does not set your Z offset. It compensates for surface variation, but the baseline nozzle-to-bed gap is still set by you. Many people run ABL, assume everything is sorted, and then wonder why the first layer is still wrong. See Step 2.

---

## Step 2: Set Your Z Offset

Z offset is the gap between the nozzle and the bed at the start of a print. This is the single most important calibration step and the one most worth taking your time on.

**What a correct first layer looks like:** lines slightly flattened, adjacent lines touching and fusing at the edges, no gaps, no rough scraped surface.

**Too high:** filament comes out round, does not squish down, corners lift. Lower the Z offset (move the nozzle closer) in 0.05mm increments.

**Too low:** nozzle drags through what it just laid down, surface looks rough and squashed. Raise the Z offset in 0.05mm increments.

Print a single-layer square each time you adjust. A 60x60mm square is ideal - large enough to see variations across the bed, fast enough to iterate. The [first layer calibration test print](https://tools.print3dbuddy.com/test-prints#first-layer-test) at tools.print3dbuddy.com is designed for exactly this.

---

## Step 3: Calibrate E-Steps

E-steps tell the printer how many motor steps push 1mm of filament. If this is wrong, every print is either slightly over-extruded or slightly under-extruded.

Many printers come factory-calibrated and you will never need to touch this. But if you are on a budget machine or have replaced your extruder, it is worth checking.

**How to check:**

1. Mark your filament 100mm and 120mm from the extruder entry point
2. Command the printer to extrude 100mm (via the control menu or terminal - with the hotend at printing temperature)
3. Measure how much actually moved
4. If it moved 95mm instead of 100mm, calculate the correction:

**New E-steps = (Current E-steps x 100) / Actual mm extruded**

Update the value in firmware and save. This is a one-time step that improves everything downstream.

---

## Step 4: Run a Temperature Tower

Different filament brands behave differently at different temperatures. A temperature tower tests several temperatures in one print.

1. Download a [temperature tower from the Test Prints page](https://tools.print3dbuddy.com/test-prints#temp-tower) at tools.print3dbuddy.com
2. Use your slicer's "change filament at height" feature to step the temperature down every 5mm
3. For PLA, test from 230 down to 190. For PETG, 250 down to 220
4. Look at each section: where does stringing reduce? Where does surface quality peak? Where do overhangs start drooping?

The range that gives you clean overhangs, minimal stringing, and good surface finish is your sweet spot. Note it per brand - it varies more than people expect.

---

## Step 5: Calibrate Flow Rate

Even with correct E-steps, flow rate can be slightly off due to filament diameter variation between brands. This step catches that.

1. Print a single-wall box: 20x20x20mm, zero infill, zero top layers, one perimeter
2. Measure the wall thickness with digital calipers
3. Your target is the line width set in your slicer - usually 0.4-0.45mm for a 0.4mm nozzle
4. If the wall is 0.48mm, reduce flow rate proportionally. If it is 0.37mm, increase it

Adjust in 2-3% increments. This is per-filament - do it once for each brand you use regularly.

---

## Step 6: Check Retraction

Retraction pulls filament back before travel moves to stop oozing. Wrong settings cause stringing (too little) or gaps and clogs (too much).

If you are new to the printer and everything else is dialled in, print a retraction test first to see if you actually have a stringing problem before tuning. Many printers print cleanly at defaults. If you do have stringing, the [stringing guide](/posts/how-to-fix-3d-printer-stringing/) covers this in full.

Starting points:
- Direct drive: 0.5-1.5mm distance, 25-45mm/s speed
- Bowden: 4-6mm distance, 40-60mm/s speed

---

## Step 7: Print a Calibration Cube

Once you have worked through the steps above, print a 20mm calibration cube as a final check.

What to look for:
- Dimensions: within 0.2mm of 20mm on all sides when measured with calipers
- Top surface: smooth, no gaps or blobs
- Corners: sharp, not rounded or blobby
- Walls: smooth, no wobble or horizontal banding

If something is off, you now know which step controls it.

---

## How Often Do You Need to Calibrate?

- **Bed level:** check whenever first layer adhesion changes, or after moving the printer
- **Z offset:** only when you change nozzles or the bed surface
- **E-steps:** once, and after any extruder hardware changes
- **Flow rate:** once per filament brand
- **Temperature:** once per filament brand

Most of these are set once and then not touched for months. The exception is Z offset - it drifts slightly on printers without ABL and is worth verifying if prints start failing at the first layer.

---

The calibration process sounds like a lot. In practice it takes an hour or two, most of it waiting for prints. After that, you print and fix problems as they come rather than fighting the same ones repeatedly. It is worth doing properly at the start.
