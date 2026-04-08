# How to Fix Under-Extrusion in 3D Printing (Every Cause, Every Fix)

Under-extrusion looks different every time it shows up. Gaps between lines. Weak layers that snap if you look at them wrong. Prints that look almost right but fall apart when you try to use them. It is frustrating because the printer is clearly doing something - just not enough of it.

The first time I had a serious under-extrusion problem it took three days to diagnose. The extruder gear had stripped the filament so badly it could not grip anymore. Three days of tweaking temperatures and print speeds before I thought to actually look at the extruder. Once you know what to look for, you can usually identify the cause in ten minutes.

---

## How to Spot It

- Gaps between perimeter lines or infill
- Thin or missing top layers
- Prints feel lightweight and fragile compared to how they should feel
- Layer lines look separated rather than fused
- Clicking or grinding from the extruder while printing

That last one - the clicking - is the clearest indicator. It means the extruder motor is skipping because it cannot push filament fast enough. Do not ignore it and hope it goes away.

---

## Work Through These in Order

### 1. Check the Extruder First

Look at the filament path. If there is a flat section ground into the filament just above the extruder, the gear has been slipping. It chews a groove into the filament until it cannot grip at all.

Pull the filament out and look at it. If it looks chewed, that is your problem. Clean the debris out of the extruder gear teeth with a stiff brush, check the idler arm tension, and reload fresh filament from a clean section of the spool.

This takes two minutes and rules out the most common mechanical cause.

---

### 2. Raise Nozzle Temperature

If the filament is not hot enough it will not flow easily. The extruder has to work harder to push it through and eventually starts skipping.

Increase temperature by 5 degrees at a time and test. Most materials have a range - PLA runs well at 190-220, PETG at 230-250. If you are printing at the low end of the range for your material, try the middle first.

Also worth checking: if your printer has been running for a while, the thermistor can drift or partially fail. A thermistor reading 210 degrees when the actual temperature is 190 is a surprisingly common cause of unexplained under-extrusion. If raising the set temperature fixes it, that is a clue the thermistor needs attention.

---

### 3. Do a Cold Pull

A cold pull clears partial clogs that restrict flow without stopping it entirely. Partial clogs are sneaky because prints can look almost normal until you push speed or use a larger nozzle.

Heat to printing temperature, push filament through manually until it flows cleanly, then let it cool to around 90 degrees for PLA (higher for other materials - around 110 for PETG). Pull the filament out sharply. It should come out with a clean tip shaped like the inside of the nozzle. Dark specks, rough texture, or a deformed tip means debris came with it - repeat until you get a clean pull.

---

### 4. Reduce Print Speed

If the hotend cannot melt filament fast enough to keep up with the extruder, under-extrusion follows. This is volumetric flow limiting - the melt zone has a maximum throughput, and if you push past it the pressure builds and the extruder skips.

Drop print speed by 20-30% and see if the problem improves. If it does, either keep the slower speed or raise temperature slightly to increase melt rate.

---

### 5. Check the Bowden Tube (Bowden Printers Only)

On Bowden printers the PTFE tube runs from the extruder to the hotend. A gap between the tube and the nozzle causes filament to accumulate and create a partial blockage over time. Check that the tube is fully seated with no gap at the nozzle end.

If the tube is discoloured, cracked, or has lost shape at the ends, replace it. Capricorn tubing is worth the small premium - tighter tolerances mean less filament play and more consistent feeding.

---

### 6. Calibrate E-Steps

If your extruder has never been calibrated, it may think it is pushing 100mm of filament when it is actually pushing 90mm. Everything you print will be slightly under-extruded.

Mark 100mm on filament above the extruder, tell the printer to extrude 100mm, measure how much actually moved. If the numbers do not match, adjust E-steps accordingly. This is a one-time calibration that improves everything.

---

### 7. Check Filament Quality

Cheap filament often has significant diameter variation. A section that is 1.85mm instead of 1.75mm creates flow resistance. I had a spool of budget PETG once that printed fine for the first 200g then got progressively worse toward the end - the last third was clearly inconsistent diameter. Weighed the full spool before buying it and it was under spec too.

Measure filament at a few points with digital calipers. Variation above 0.05mm from 1.75mm is a quality problem, not a settings problem. Wet filament also produces under-extrusion symptoms alongside crackling sounds and surface bubbling.

---

## The Diagnostic Order

1. Look at the extruder - check for stripped filament and slipping gear
2. Raise temperature by 10 degrees - quick test, often fixes it immediately
3. Do a cold pull - rules out partial clog
4. Reduce print speed by 30% - if it improves, it is a flow rate issue
5. Calibrate E-steps if none of the above work

Most cases are solved by step one or two.

---

## Prevention

- Do not leave filament loaded in a hot nozzle when you are done printing - it degrades and causes clogs
- Store filament in sealed containers with desiccant
- Do a cold pull at the start of any long print session with a material you have not used recently
- Check the [Print Settings guide](https://tools.print3dbuddy.com/tools/print-settings) for correct starting temperatures - wrong starting temps cause more under-extrusion than anything else

---

Under-extrusion feels mysterious the first time. After you have fixed it a few times you develop an instinct - the clicking extruder is the gear slipping, the gradually worsening print is a partial clog building up, the under-extrusion on the first print with a new filament is temperature. Work through the list above and you will find it.
