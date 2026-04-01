# 3D Printer Fire Safety: Thermal Runaway, Smoke Detectors, and Safe Printing Habits

3D printers involve high temperatures, long unattended print runs, and electrical components that can fail. House fires caused by 3D printers are rare but real. Most are preventable with the right setup and habits. This guide covers the actual risks, what to do about them, and how to print with confidence.

---

## The Real Risks

Understanding where the risk actually comes from helps you address the right things.

**Thermal runaway.** The most common cause of 3D printer fires. If the thermistor (temperature sensor) fails or disconnects, the printer can continue heating the hot end indefinitely with no way to know the temperature is dangerously high. Without thermal runaway protection, the heater runs unchecked until something catches fire. Modern printers have this protection by default - older or budget printers sometimes do not.

**Heated bed electrical faults.** The heated bed draws significant current. A loose connector, damaged wiring, or a bed that has been modified without proper insulation can arc or overheat. Bed fires tend to smoulder rather than ignite quickly, but they are still dangerous.

**PSU faults.** A failing or undersized power supply unit can overheat or fail in ways that generate heat and sparks. Budget PSUs are more prone to this.

**Filament near hot components.** A failed print that dumps filament onto the hot end area can cause a smouldering situation. PETG and ABS are less flammable than some materials, but any organic material can burn.

**Resin and wash stations.** Resin is flammable. Isopropyl alcohol used for washing resin prints is highly flammable. These are the highest fire risk in the average 3D printing setup.

---

## Step 1: Check Thermal Runaway Protection Is Enabled

This is the single most important safety measure for FDM printers.

**Bambu Lab printers:** Thermal runaway protection is enabled by default and cannot be disabled. Safe.

**Prusa printers:** Thermal runaway protection is enabled by default in Prusa firmware. Safe.

**Creality and other Marlin-based printers:** Thermal runaway protection should be enabled, but some older firmware versions or clones had it disabled. To check:
1. Disconnect the thermistor from the hot end (or simply unplug it while the printer is off, then attempt to heat)
2. If the printer throws an error and refuses to heat, thermal runaway is active
3. If the printer heats without a thermistor connected, it is not protected - update the firmware immediately

The Creality firmware available on their official website has thermal runaway enabled. If you are on very old firmware, update it.

---

## Step 2: Fit a Smoke Detector

Place a smoke detector in the same room as your printer if there is not already one. Mount it on the ceiling directly above or near the printer.

A [10-year sealed battery smoke detector](https://www.amazon.co.uk/s?k=10+year+smoke+detector+sealed+battery&tag=print3dbuddy2-21) requires no maintenance beyond testing it monthly. Get one - they cost under £15 and provide early warning that nothing else will.

For enclosed printers or garage setups, a [heat detector](https://www.amazon.co.uk/s?k=heat+detector+alarm&tag=print3dbuddy2-21) is sometimes preferred over a smoke detector because it is not triggered by normal fume emissions from ABS or resin. Both types are worth having.

---

## Step 3: Never Leave a New or Untested Printer Unattended

For the first several print runs on a new printer or after significant changes (new firmware, new hot end, modified bed wiring), stay nearby and check on it regularly.

Once you have verified that:
- Thermal runaway protection is active
- The printer completes a full print without any unusual smells, sounds, or temperature errors
- All wiring and connectors look undamaged

...then leaving the printer unattended for known-good print jobs is a reasonable choice.

---

## Step 4: Inspect Wiring Regularly

Check these regularly as part of your maintenance routine:
- Hotend wiring: the cable bundle that moves with the print head flexes thousands of times. Look for cracked insulation, fraying near connectors, or any wires that have worked loose from their terminals.
- Heated bed cable: moves constantly as the bed travels. The cable should have a strain relief and enough slack that it is never pulled taut.
- PSU connections: the input and output terminals should be tight and show no signs of heat discolouration.

See the [printer maintenance guide](/posts/how-to-maintain-3d-printer/) for a full maintenance schedule.

---

## Step 5: Use a Smart Plug or Camera for Remote Monitoring

A [smart plug with power monitoring](https://www.amazon.co.uk/s?k=smart+plug+power+monitor&tag=print3dbuddy2-21) lets you:
- Cut power to the printer remotely if something looks wrong
- Monitor power consumption - a sudden spike or drop can indicate a component failure
- Turn the printer off automatically after a print if your printer does not do this itself

A [webcam or IP camera](https://www.amazon.co.uk/s?k=IP+camera+home+monitoring&tag=print3dbuddy2-21) lets you check on long prints remotely. Klipper users can use Mainsail or Fluidd with a camera stream. Bambu users have this built into the Bambu app.

---

## Step 6: Fire Extinguisher in the Print Room

A [dry powder or CO2 fire extinguisher](https://www.amazon.co.uk/s?k=CO2+fire+extinguisher+1kg&tag=print3dbuddy2-21) in the same room as your printer costs around £20 - £30 and could prevent a small electrical fire from becoming a house fire.

**For enclosed printers:** Automatic fire suppression canisters designed for enclosed electronics (sometimes called "fire suppression balls" or "aerosol fire suppressants") can be mounted inside an enclosure. They activate automatically on contact with flame and put out small fires without human intervention. These are increasingly popular with serious 3D printing enthusiasts.

---

## Resin Printing: Extra Precautions

Resin and IPA are both flammable. Specific precautions for resin setups:

- Store resin bottles away from heat sources and direct sunlight
- Store IPA in small quantities and keep it sealed when not in use
- Cure resin prints fully before handling - uncured resin is a skin irritant and potentially toxic
- Dispose of contaminated IPA properly - do not pour it down the drain. Let it cure in sunlight (in a sealable container) until solid, then dispose of as solid waste
- Never use IPA near an open flame or sparks

See the [resin 3D printing safety guide](/posts/resin-3d-printing-safety/) for full resin handling precautions.

---

## Safe Printing Habit Checklist

| Habit | Frequency |
|---|---|
| Check thermal runaway is active | Once on setup |
| Inspect wiring for damage | Monthly |
| Test smoke detector | Monthly |
| Clean filament debris from around hot end | After every print |
| Check for unusual smells during printing | Every print |
| Never leave a brand-new printer fully unattended | First 5 - 10 prints |

---

## Related Guides

- [3D Printing Emissions and Indoor Safety](/posts/3d-printing-emissions-indoor-safety/) - fumes, particles, and ventilation
- [Resin 3D Printing Safety](/posts/resin-3d-printing-safety/) - handling resin, IPA, and UV curing safely
- [How to Maintain Your 3D Printer](/posts/how-to-maintain-3d-printer/) - wiring inspection and maintenance schedule
- [Best 3D Printer Enclosures](/posts/best-3d-printer-enclosures/) - enclosures that contain heat and contain any fire
