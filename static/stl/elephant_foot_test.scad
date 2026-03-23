// Elephant Foot Calibration Test
// Print this to measure and eliminate elephant foot (base flare) on FDM printers.
//
// How to use:
//   1. Print with your current Z offset and first layer settings.
//   2. Measure the disc diameter and the cylinder diameter with calipers.
//   3. If the disc is wider than the nominal diameter (50mm), you have elephant foot.
//      The difference on each side = your elephant foot amount.
//   4. Raise Z offset by 0.05mm steps and reprint until disc and cylinder are even.
//
// Nominal disc diameter:     50mm
// Nominal cylinder diameter: 20mm
// Cylinder height:           10mm (tall enough to show sidewall quality)
//
// Recommended print settings:
//   Layer height: 0.2mm
//   Walls: 3
//   Infill: 20%
//   No supports needed

$fn = 120;

disc_d    = 50;
disc_h    = 1.2;   // 6 layers at 0.2mm - thin enough to show flare clearly
cyl_d     = 20;
cyl_h     = 10;
label_h   = 0.4;   // one layer emboss depth

// Disc base
cylinder(d = disc_d, h = disc_h);

// Central cylinder
translate([0, 0, disc_h])
    cylinder(d = cyl_d, h = cyl_h);

// Embossed diameter label on disc surface
translate([0, -3, disc_h - label_h])
    linear_extrude(label_h + 0.01)
        text("D50 / C20", size = 4, halign = "center", valign = "center", font = "Liberation Sans");

// Tick marks at 0, 90, 180, 270 degrees to help measure concentricity
for (a = [0, 90, 180, 270]) {
    rotate([0, 0, a])
        translate([disc_d / 2 - 3, -0.4, disc_h - label_h])
            cube([3, 0.8, label_h + 0.01]);
}
