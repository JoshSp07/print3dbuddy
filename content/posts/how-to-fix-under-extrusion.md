# How to Fix Under-Extrusion in 3D Printing (Every Cause, Every Fix)

Under-extrusion is one of those problems that looks different every time it shows up. Gaps between lines. Weak layers that snap if you look at them wrong. Prints that look almost right but fall apart when you try to use them. It's frustrating because the printer is clearly doing *something* — just not enough of it.

I've been through this more times than I'd like to admit. My first serious under-extrusion problem took me three days to diagnose. Turns out my extruder gear had stripped the filament so badly it couldn't grip it anymore. Three days of tweaking temperatures and speeds before I thought to actually look at the extruder. Once you know what to look for, you can usually fix it in an hour.

---

## What Under-Extrusion Actually Is

Your printer expects a precise amount of filament to come out of the nozzle. Under-extrusion means less filament is coming out than expected — either because the extruder isn't pushing enough, the nozzle is partially blocked, or the filament path has a problem somewhere.

The result: gaps, weak layers, surfaces that look like they're missing material, and prints that fail mid-way through tall sections where the problem compounds.

---

## How to Spot It

- Gaps between perimeter lines or infill
- Thin or missing top layers
- Prints feel lightweight and fragile
- Layer lines that look separated rather than fused
- Clicking or grinding sound from the extruder

If you hear clicking from the extruder while printing, that's the extruder motor skipping — a sure sign the filament isn't moving as fast as it should be.

---

## My Under-Extrusion Story

The worst case I had was with a spool of cheap PETG I bought to save a few pounds. The extrusion was fine for the first 200g, then started getting progressively worse. I blamed everything — the temperature, the retraction, the print speed — before eventually weighing the remaining filament and realising it was labelled wrong. The spool was listed as 1kg but was actually closer to 700g, and the last third was clearly poor quality with inconsistent diameter. The filament itself was the problem.

Since then I weigh every spool before I buy and check the diameter consistency on anything that matters. Cheap filament costs more in wasted prints than it saves on the spool.

---

## The Causes (Work Through These in Order)

### 1. Nozzle Temperature Too Low

The most common cause. If the filament isn't hot enough, it won't flow easily and the extruder has to work harder to push it through.

**Fix:** Increase nozzle temperature by 5°C at a time. Most materials have a range — PLA 190-220°C, PETG 230-250°C. If you're at the bottom of the range, move up. Also check that your thermistor is reading accurately — a faulty thermistor can make the printer think it's at 210°C when it's actually at 190°C.

### 2. Print Speed Too High

Fast printing requires more filament per second. If the hotend can't melt plastic fast enough to keep up, under-extrusion follows.

**Fix:** Drop print speed by 20-30% and see if the problem improves. If it does, either keep the slower speed or raise the temperature slightly to increase melt rate.

### 3. Partial Nozzle Clog

A partial clog doesn't stop printing entirely — it just restricts flow. This is sneaky because prints can look almost normal until you try a faster or larger print.

**Fix:** Do a cold pull. Heat the nozzle to printing temperature, push filament through manually until it flows clean, then let it cool to around 90°C (for PLA) and pull the filament out sharply. This pulls debris out with it. Repeat until the pulled filament comes out clean with no dark specks or rough texture. For stubborn clogs, use an acupuncture needle or cleaning filament.

### 4. Extruder Gear Slipping or Stripped Filament

The extruder gear grips the filament and pushes it forward. If the gear is worn, loose, or if the filament surface has been chewed up by repeated slipping, it can't get a proper grip.

**Fix:** Look at the filament coming out of the extruder — if it has a flat section ground into it, the gear has been slipping. Open the extruder and check the gear for wear. Tighten the idler arm tension if it seems loose. Clean debris out of the gear teeth with a brush.

### 5. Bowden Tube Issues

On Bowden printers (where the extruder is separate from the hotend), gaps or damage in the PTFE tube cause filament drag and inconsistent feeding.

**Fix:** Check that the tube is fully seated against the nozzle with no gap. A gap here causes filament to accumulate and create blockages. If the tube is discoloured, cracked, or has lost its shape at the ends, replace it. Capricorn tubing is a worthwhile upgrade — tighter tolerances mean less play in the filament path.

### 6. Flow Rate / E-Steps Not Calibrated

If your extruder hasn't been calibrated, it may think it's pushing 100mm of filament when it's actually pushing 90mm. Over time this under-extrudes everything you print.

**Fix:** Mark 100mm on a piece of filament above the extruder, tell the printer to extrude 100mm, and measure how much actually moved. If it's not 100mm, adjust your E-steps (steps per mm) accordingly. This is a one-time calibration that makes everything more accurate.

### 7. Filament Diameter Inconsistency or Moisture

Cheap filament can have significant diameter variation — sections that are 1.85mm instead of 1.75mm create flow resistance. Wet filament also doesn't flow as smoothly and can produce under-extrusion alongside other symptoms like bubbling or stringing.

**Fix:** Measure filament diameter at multiple points with digital calipers. If variance is more than ±0.05mm, the filament quality is the problem. For moisture, dry the spool in a food dehydrator or oven at 45-65°C (material-dependent) for 4-8 hours.

---

## The Diagnostic Order

If you're not sure where to start:

1. **Check the extruder** for clicking and stripped filament first — it's visible and rules out a big category
2. **Raise temperature** by 10°C — quick test, often fixes it immediately
3. **Do a cold pull** to rule out a partial clog
4. **Reduce print speed** by 30% — if it improves, you know it's a flow rate issue
5. **Check E-steps** if none of the above work

Most cases are solved by step 1-3.

---

## Prevention

- Don't leave filament loaded in a hot nozzle when not printing — it degrades and causes clogs
- Store filament in sealed bags or boxes with desiccant
- Do a cold pull at the start of any long print session with a material you haven't used recently
- Use the [Print Settings Cheat Sheet at tools.print3dbuddy.com](https://tools.print3dbuddy.com) to make sure your starting temperatures are correct for your specific material — wrong starting temps are the number one cause of under-extrusion in my experience

---

Under-extrusion feels mysterious until you've fixed it a few times. After that you develop an intuition for which symptom points to which cause. The clicking extruder is the extruder gear. The gradually worsening print is a partial clog. The inconsistent layers on the first print with a new filament is usually temperature. Work through the list, fix one thing at a time, and you'll find it.
