// Tolerance / Fit Test
// Print once to find the right clearance for press fits, sliding joints, and snap fits.
// Generates 5 peg-and-hole pairs with clearances from 0.1mm to 0.5mm.
// Label is embossed on each pair so results are readable without notes.
//
// Recommended print settings:
//   Layer height: 0.2mm
//   Walls: 3
//   Infill: 20%
//   No supports needed

$fn = 60;

peg_diameter  = 8;    // nominal peg diameter (mm)
peg_height    = 12;   // peg height
base_h        = 2.5;  // base plate thickness
base_w        = 18;   // width of each pair block
base_d        = 22;   // depth of each pair block
hole_depth    = 14;   // depth of the receiving hole
spacing       = 2;    // gap between blocks
clearances    = [0.1, 0.2, 0.3, 0.4, 0.5];
label_strings = ["0.1", "0.2", "0.3", "0.4", "0.5"];

total_width = len(clearances) * (base_w + spacing) - spacing;

// -- Base row of peg blocks --
for (i = [0 : len(clearances) - 1]) {
    cl = clearances[i];
    x = i * (base_w + spacing);

    translate([x, 0, 0]) {
        // Peg block
        difference() {
            cube([base_w, base_d / 2, base_h + peg_height]);
            // Label recess
            translate([1, base_d / 2 - 2, base_h + peg_height - 1.5])
                linear_extrude(2)
                    text(label_strings[i], size = 3, halign = "left", font = "Liberation Sans");
        }
        // Peg
        translate([base_w / 2, base_d / 4, base_h])
            cylinder(d = peg_diameter, h = peg_height);
    }
}

// -- Base row of hole blocks --
for (i = [0 : len(clearances) - 1]) {
    cl = clearances[i];
    x = i * (base_w + spacing);
    hole_d = peg_diameter + cl * 2;

    translate([x, base_d / 2 + spacing, 0]) {
        difference() {
            cube([base_w, base_d / 2, base_h + hole_depth]);
            // Hole
            translate([base_w / 2, base_d / 4, base_h])
                cylinder(d = hole_d, h = hole_depth + 1);
            // Label recess
            translate([1, base_d / 2 - 2, base_h + hole_depth - 1.5])
                linear_extrude(2)
                    text(label_strings[i], size = 3, halign = "left", font = "Liberation Sans");
        }
    }
}
