#!/usr/bin/env python3
# Generate The Complete FDM Troubleshooting Guide PDF
# Output: C:/Users/Administrator/ko-fi-products/fdm-troubleshooting-guide.pdf

import os
import sys
import requests
import tempfile
from pathlib import Path

# ── ReportLab imports ──────────────────────────────────────────────────────────
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image, HRFlowable, KeepTogether
)
from reportlab.platypus.flowables import Flowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Colour palette ─────────────────────────────────────────────────────────────
NAVY        = colors.HexColor('#1a1a2e')
ORANGE      = colors.HexColor('#e85d04')
WHITE       = colors.white
LIGHT_GREY  = colors.HexColor('#f5f5f5')
MID_GREY    = colors.HexColor('#e0e0e0')
DARK_GREY   = colors.HexColor('#555555')
TABLE_HDR   = NAVY
TABLE_ALT   = colors.HexColor('#f0f0f5')
FOOTER_CLR  = colors.HexColor('#999999')

# ── Page geometry ──────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4          # 595.27 x 841.89 pts
MARGIN_L = 20 * mm
MARGIN_R = 20 * mm
MARGIN_T = 22 * mm
MARGIN_B = 22 * mm
BODY_W   = PAGE_W - MARGIN_L - MARGIN_R

# ── Output path ────────────────────────────────────────────────────────────────
OUTPUT_DIR  = Path(r"C:\Users\Administrator\ko-fi-products")
OUTPUT_PATH = OUTPUT_DIR / "fdm-troubleshooting-guide.pdf"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Image download ─────────────────────────────────────────────────────────────
IMAGE_URLS = [
    # Unsplash direct image links — verified working
    "https://images.unsplash.com/photo-1581091012184-7e0cdfbb6797?w=900&auto=format&fit=crop&q=80",   # filament / 3D printing
    "https://images.unsplash.com/photo-1617791160536-598cf32026fb?w=900&auto=format&fit=crop&q=80",   # 3D printer
    "https://images.unsplash.com/photo-1564069114553-7215e1ff1890?w=900&auto=format&fit=crop&q=80",   # printed parts
    "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=900&auto=format&fit=crop&q=80",      # fdm printing process
]

_tmp_images = []   # keep temp file handles alive

def download_image(url: str, idx: int):
    """Download an image and return the local temp path, or None on failure."""
    try:
        print(f"  Downloading image {idx+1}: {url[:60]}...")
        r = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        suffix = ".jpg"
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        tmp.write(r.content)
        tmp.close()
        _tmp_images.append(tmp.name)
        print(f"    -> saved to {tmp.name} ({len(r.content)//1024} KB)")
        return tmp.name
    except Exception as e:
        print(f"    -> FAILED: {e}")
        return None


def cleanup_images():
    for p in _tmp_images:
        try:
            os.unlink(p)
        except Exception:
            pass


# ── Style helpers ──────────────────────────────────────────────────────────────
def make_styles():
    base = getSampleStyleSheet()

    styles = {
        "cover_title": ParagraphStyle(
            "cover_title",
            fontName="Helvetica-Bold",
            fontSize=32,
            leading=38,
            textColor=NAVY,
            alignment=TA_CENTER,
            spaceAfter=10,
        ),
        "cover_subtitle": ParagraphStyle(
            "cover_subtitle",
            fontName="Helvetica",
            fontSize=14,
            leading=20,
            textColor=DARK_GREY,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "cover_edition": ParagraphStyle(
            "cover_edition",
            fontName="Helvetica",
            fontSize=10,
            textColor=FOOTER_CLR,
            alignment=TA_CENTER,
        ),
        "section_heading": ParagraphStyle(
            "section_heading",
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=18,
            textColor=NAVY,
            spaceBefore=8,
            spaceAfter=4,
        ),
        "sub_heading": ParagraphStyle(
            "sub_heading",
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=13,
            textColor=ORANGE,
            spaceBefore=6,
            spaceAfter=2,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="Helvetica",
            fontSize=8.5,
            leading=12,
            textColor=colors.black,
            spaceAfter=3,
        ),
        "body_italic": ParagraphStyle(
            "body_italic",
            fontName="Helvetica-Oblique",
            fontSize=8.5,
            leading=12,
            textColor=DARK_GREY,
            spaceAfter=4,
        ),
        "note": ParagraphStyle(
            "note",
            fontName="Helvetica-Oblique",
            fontSize=7.5,
            leading=10,
            textColor=DARK_GREY,
            spaceAfter=4,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName="Helvetica",
            fontSize=8.5,
            leading=12,
            leftIndent=12,
            firstLineIndent=-12,
            spaceAfter=2,
        ),
        "toc_entry": ParagraphStyle(
            "toc_entry",
            fontName="Helvetica",
            fontSize=9,
            leading=14,
            textColor=DARK_GREY,
        ),
    }
    return styles


# ── Reusable table style builders ──────────────────────────────────────────────
def std_table_style(col_widths=None, alt_rows=True, hdr_rows=1):
    """Return a TableStyle for the standard reference tables."""
    cmds = [
        ("BACKGROUND",  (0, 0), (-1, hdr_rows - 1), TABLE_HDR),
        ("TEXTCOLOR",   (0, 0), (-1, hdr_rows - 1), WHITE),
        ("FONTNAME",    (0, 0), (-1, hdr_rows - 1), "Helvetica-Bold"),
        ("FONTSIZE",    (0, 0), (-1, hdr_rows - 1), 8),
        ("ALIGN",       (0, 0), (-1, hdr_rows - 1), "CENTER"),
        ("VALIGN",      (0, 0), (-1, -1),            "TOP"),
        ("FONTNAME",    (0, hdr_rows), (-1, -1),     "Helvetica"),
        ("FONTSIZE",    (0, hdr_rows), (-1, -1),     7.5),
        ("GRID",        (0, 0), (-1, -1), 0.4,       colors.HexColor('#cccccc')),
        ("ROWBACKGROUND",(0, 0), (-1, -1), [WHITE, WHITE]),  # default
        ("LEFTPADDING",  (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING",   (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 4),
        ("LINEABOVE",   (0, 0), (-1, 0), 0.5, NAVY),
        ("LINEBELOW",   (0, hdr_rows - 1), (-1, hdr_rows - 1), 1, ORANGE),
    ]
    return TableStyle(cmds)


def apply_alt_rows(style_cmds, data_start, num_rows):
    """Append alternating row background commands to a TableStyle command list."""
    for i in range(num_rows):
        row = data_start + i
        bg = TABLE_ALT if i % 2 == 0 else WHITE
        style_cmds.append(("BACKGROUND", (0, row), (-1, row), bg))


def make_table(data, col_widths, alt_start=1, span_cmds=None):
    """Build a Table with the standard style + alternating rows."""
    cmds = [
        ("BACKGROUND",  (0, 0), (-1, 0), TABLE_HDR),
        ("TEXTCOLOR",   (0, 0), (-1, 0), WHITE),
        ("FONTNAME",    (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",    (0, 0), (-1, 0), 8),
        ("ALIGN",       (0, 0), (-1, 0), "CENTER"),
        ("VALIGN",      (0, 0), (-1, -1), "TOP"),
        ("FONTNAME",    (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",    (0, 1), (-1, -1), 7.5),
        ("GRID",        (0, 0), (-1, -1), 0.4, colors.HexColor('#cccccc')),
        ("LEFTPADDING",  (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING",   (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 4),
        ("LINEBELOW",   (0, 0), (-1, 0), 1, ORANGE),
    ]
    apply_alt_rows(cmds, alt_start, len(data) - alt_start)
    if span_cmds:
        cmds.extend(span_cmds)
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle(cmds))
    return t


# ── Custom flowable: orange accent rule ───────────────────────────────────────
class AccentRule(Flowable):
    def __init__(self, width, thickness=2.5):
        Flowable.__init__(self)
        self.width = width
        self.thickness = thickness
        self.height = thickness + 1

    def draw(self):
        self.canv.setFillColor(ORANGE)
        self.canv.rect(0, 0, self.width, self.thickness, fill=1, stroke=0)


# ── Page template callbacks ────────────────────────────────────────────────────
def on_page(canvas, doc):
    """Draw footer on every page."""
    canvas.saveState()
    page_num = canvas.getPageNumber()

    # thin top rule
    canvas.setStrokeColor(NAVY)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN_L, PAGE_H - 14 * mm, PAGE_W - MARGIN_R, PAGE_H - 14 * mm)

    # page number centred
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(FOOTER_CLR)
    canvas.drawCentredString(PAGE_W / 2, 12 * mm, str(page_num))

    # Print3DBuddy right-aligned, small and subtle
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(FOOTER_CLR)
    canvas.drawRightString(PAGE_W - MARGIN_R, 12 * mm, "Print3DBuddy")

    # thin bottom rule
    canvas.setStrokeColor(NAVY)
    canvas.line(MARGIN_L, 18 * mm, PAGE_W - MARGIN_R, 18 * mm)

    canvas.restoreState()


def on_page_cover(canvas, doc):
    """Cover page: no header rule, just footer branding."""
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(FOOTER_CLR)
    canvas.drawRightString(PAGE_W - MARGIN_R, 12 * mm, "Print3DBuddy")
    canvas.restoreState()


# ── Section heading helper ─────────────────────────────────────────────────────
def section_heading(text, styles):
    elems = []
    elems.append(Spacer(1, 6))
    elems.append(Paragraph(text, styles["section_heading"]))
    elems.append(AccentRule(BODY_W))
    elems.append(Spacer(1, 4))
    return elems


def sub_heading(text, styles):
    return [Paragraph(text, styles["sub_heading"])]


def bullet_list(items, styles, prefix="• "):
    return [Paragraph(prefix + item, styles["bullet"]) for item in items]


def checkbox_list(items, styles):
    return [Paragraph("☐  " + item, styles["bullet"]) for item in items]


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE BUILDERS
# ══════════════════════════════════════════════════════════════════════════════

def build_cover(styles, img_path):
    elems = []
    elems.append(Spacer(1, 30 * mm))

    # optional image
    if img_path:
        try:
            img = Image(img_path, width=BODY_W * 0.72, height=72 * mm)
            img.hAlign = "CENTER"
            elems.append(img)
            elems.append(Spacer(1, 12 * mm))
        except Exception as e:
            print(f"  Cover image error: {e}")
            elems.append(Spacer(1, 12 * mm))
    else:
        elems.append(Spacer(1, 20 * mm))

    elems.append(Paragraph("The Complete FDM<br/>Troubleshooting Guide", styles["cover_title"]))
    elems.append(Spacer(1, 6))
    elems.append(Paragraph("Quick-reference guide for FDM 3D printing problems", styles["cover_subtitle"]))
    elems.append(Spacer(1, 8))
    elems.append(AccentRule(BODY_W * 0.5))  # centered visually – centred via table
    elems.append(Spacer(1, 10))
    elems.append(Paragraph("2025 Edition", styles["cover_edition"]))
    elems.append(PageBreak())
    return elems


def build_quick_reference(styles):
    elems = []
    elems += section_heading("Quick Reference Table", styles)
    elems.append(Paragraph(
        "Identify your issue below, then jump to the dedicated section for a full diagnosis.",
        styles["body_italic"]
    ))
    elems.append(Spacer(1, 5))

    hdr = ["PROBLEM", "MOST LIKELY CAUSE", "QUICK FIX"]
    rows = [
        ["Stringing between parts",         "Retraction too low",              "Increase retraction 0.5 mm at a time"],
        ["Blobs / ooze on walls",            "Too much retraction or heat",     "Lower temp 5 °C, tune retraction"],
        ["Part lifts off bed",               "Poor bed adhesion",               "Clean bed, increase first layer temp"],
        ["Corners warping up",               "Thermal contraction",             "Enclosure, brim, higher bed temp"],
        ["Under-extrusion (gaps in walls)",  "Partial clog or low temp",        "Cold pull, increase temp 5 °C"],
        ["Layer lines separating",           "Too fast or too cold",            "Slow print 10 mm/s, raise temp 5 °C"],
        ["First layer not sticking",         "Z offset too high",               "Lower nozzle (decrease Z offset)"],
        ["First layer too squished/scarred", "Z offset too low",                "Raise nozzle (increase Z offset)"],
        ["Nozzle clog (no extrusion)",        "Burned material or debris",       "Cold pull ×3, then manual clear"],
        ["Spaghetti / print failure",        "Layer shift or detachment",       "Check belt tension, clean bed"],
        ["Ringing / ghosting on walls",      "Vibration / too fast",            "Reduce speed, check belt tension"],
        ["Elephant foot (flared base)",      "First layer too squished",        "Raise Z offset 0.05 mm increments"],
        ["Pillowing on top surface",         "Too few top layers or cooling",   "Add 1–2 top layers, reduce fan"],
        ["Gaps in top surface",              "Under-extrusion",                 "Increase flow 2–3 %, check clog"],
        ["Overhangs drooping",               "Insufficient cooling",            "Increase fan, reduce speed"],
        ["Supports won't remove cleanly",    "Interface distance too small",    "Increase Z gap to 0.2 mm"],
        ["Cracks between layers (tall)",     "Ambient cold / ABS",              "Enclose printer, raise temp 5 °C"],
        ["Grinding / clicking extruder",     "Partial clog, too fast",          "Reduce speed, cold pull"],
        ["Layer shifts (horizontal)",        "Loose belt or too fast",          "Tighten belts, reduce acceleration"],
        ["Wet / bubbling filament",          "Moisture in filament",            "Dry filament 4–6 h at correct temp"],
    ]

    col_w = [BODY_W * 0.35, BODY_W * 0.30, BODY_W * 0.35]
    data = [hdr] + rows
    t = make_table(data, col_w)
    elems.append(t)
    elems.append(Spacer(1, 5))
    elems.append(Paragraph(
        "All settings adjustments assume a baseline properly calibrated printer. "
        "Always change one variable at a time.",
        styles["note"]
    ))
    elems.append(PageBreak())
    return elems


def build_stringing(styles, img_path=None):
    elems = []
    elems += section_heading("Section 2 — Stringing and Oozing", styles)
    elems.append(Paragraph(
        "Thin hairs or strings stretch between separate parts of a print; blobs or zits appear on outer walls.",
        styles["body_italic"]
    ))
    elems.append(Spacer(1, 4))

    if img_path:
        try:
            img = Image(img_path, width=BODY_W * 0.45, height=52 * mm)
            img.hAlign = "RIGHT"
            elems.append(img)
        except Exception:
            pass

    elems += sub_heading("Root Causes", styles)
    elems += bullet_list([
        "Retraction distance too low or too high",
        "Print temperature too high (lowers viscosity, promotes ooze)",
        "Travel speed too slow — nozzle lingers over gaps",
        "Combing / avoid-crossing-perimeters disabled",
        "Wet filament",
    ], styles)
    elems.append(Spacer(1, 4))

    elems += sub_heading("Settings Fix Table", styles)
    hdr = ["SETTING", "START VALUE", "ADJUST IF…", "NOTES"]
    rows = [
        ["Retraction distance",  "1 mm (direct)\n4–6 mm (Bowden)",   "Still stringing: +0.5 mm steps",     "Bowden: start 4–6 mm\nOver 7 mm risks jamming"],
        ["Retraction speed",     "25–45 mm/s",                        "Blobs after retract: −5 mm/s",        "Too fast = grinding"],
        ["Print temperature",    "Per material",                      "Lots of stringing still: −5 °C",      "Lower 5 °C, test, repeat"],
        ["Travel speed",         "150–200 mm/s",                      "Strings on travel",                   "Faster = less ooze time"],
        ["Combing mode",         "Within infill",                     "Stringing through infill areas",       "Enable 'within infill' or 'not in skin'"],
        ["Wipe on retract",      "On",                                "Blobs at seam",                       "Enables nozzle wipe move"],
        ["Coasting",             "0.1–0.2 mm",                        "Blobs at end of perimeters",           "Stops extrusion slightly early"],
    ]
    col_w = [BODY_W * 0.22, BODY_W * 0.20, BODY_W * 0.28, BODY_W * 0.30]
    elems.append(make_table([hdr] + rows, col_w))
    elems.append(Spacer(1, 5))

    elems += sub_heading("Material-Specific Notes", styles)
    elems += bullet_list([
        "PLA: Usually solves with retraction 1–2 mm (direct drive), temp 190–210 °C",
        "PETG: Notorious stringer — retraction 0.8–1.5 mm (direct), temp as low as 220 °C, slower travel helps",
        "TPU: Disable retraction almost entirely (0–1 mm) — retraction causes jams",
        "ABS/ASA: Higher temps mean more ooze — rely on combing + enclosure to manage",
    ], styles)
    return elems


def build_warping(styles):
    elems = []
    elems += section_heading("Section 3 — Warping and Bed Adhesion", styles)
    elems.append(Paragraph(
        "Corners or edges lift off the bed during printing, or the part fully detaches.",
        styles["body_italic"]
    ))
    elems.append(Spacer(1, 4))

    elems += sub_heading("Root Causes", styles)
    elems += bullet_list([
        "Bed surface not clean (oils, dust, hairspray residue)",
        "Z offset not dialled in — first layer not squished enough",
        "Bed temperature too low for the material",
        "Drafts or cooling air hitting the part",
        "Large flat parts with no brim",
    ], styles)
    elems.append(Spacer(1, 4))

    elems += sub_heading("Material-Specific Warping Table", styles)
    hdr = ["MATERIAL", "BED TEMP", "BEST SURFACE", "BRIM NEEDED?", "EXTRA TIPS"]
    rows = [
        ["PLA",   "55–65 °C",   "PEI, glass",          "Rarely",    "Drafts cause issues"],
        ["PETG",  "70–85 °C",   "PEI (textured)",       "Sometimes", "Too hot = sticks too hard, damages PEI"],
        ["ABS",   "100–110 °C", "PEI + glue stick",     "Always",    "Must enclose, no fan"],
        ["ASA",   "100–110 °C", "PEI + glue stick",     "Always",    "Even more draft-sensitive than ABS"],
        ["TPU",   "40–60 °C",   "PEI, glass",           "Rarely",    "Slow first layer helps"],
        ["Nylon", "70–90 °C",   "PEI + glue stick",     "Always",    "Dry filament thoroughly first"],
    ]
    col_w = [BODY_W * 0.13, BODY_W * 0.15, BODY_W * 0.22, BODY_W * 0.17, BODY_W * 0.33]
    elems.append(make_table([hdr] + rows, col_w))
    elems.append(Spacer(1, 5))

    elems += sub_heading("Adhesion Improvement — Order of Preference", styles)
    elems += bullet_list([
        "Fix Z offset — most warping is caused by insufficient first-layer squish",
        "Clean the build surface with IPA (90 %+)",
        "Increase bed temperature 5–10 °C",
        "Add a brim (4–8 mm width) in slicer",
        "Use a glue stick on glass or PEI for ABS/ASA",
        "Enclose the printer to maintain ambient temperature",
    ], styles, prefix="")

    elems.append(PageBreak())
    return elems


def build_under_extrusion(styles):
    elems = []
    elems += section_heading("Section 4 — Under-Extrusion", styles)
    elems.append(Paragraph(
        "Gaps between lines in walls and top surfaces; thin weak walls; "
        "inconsistent surface texture; clicking from the extruder.",
        styles["body_italic"]
    ))
    elems.append(Spacer(1, 4))

    elems += sub_heading("Root Causes (in order of likelihood)", styles)
    causes = [
        "Partial nozzle clog",
        "Print temperature too low for the filament",
        "Print speed too high for the hotend's melt capacity",
        "Extruder tension too low — filament slipping",
        "PTFE tube gap at the nozzle (creates clog zone)",
        "Worn or stripped extruder gear",
        "Flow rate calibration off",
    ]
    for i, c in enumerate(causes, 1):
        elems.append(Paragraph(f"{i}.  {c}", styles["bullet"]))
    elems.append(Spacer(1, 4))

    elems += sub_heading("Common Fixes", styles)
    hdr = ["CAUSE", "FIX"]
    rows = [
        ["Partial clog",       "Cold pull ×3–5 (see Nozzle Clogs section)"],
        ["Temp too low",       "Raise 5 °C at a time, stay within material max"],
        ["Speed too high",     "Reduce by 20 %, check wall quality"],
        ["Flow rate off",      "Calibrate e-steps and flow %"],
        ["PTFE gap",           "Tighten nozzle hot, re-seat PTFE tube"],
        ["Extruder slipping",  "Adjust tension, inspect gear teeth"],
        ["Wet filament",       "Dry 4–8 h — see material settings table"],
    ]
    col_w = [BODY_W * 0.35, BODY_W * 0.65]
    elems.append(make_table([hdr] + rows, col_w))
    elems.append(Spacer(1, 5))

    elems += sub_heading("E-Steps Calibration (Quick Method)", styles)
    esteps = [
        "Mark filament 100 mm and 120 mm from extruder entrance",
        "Extrude 100 mm via printer menu / terminal",
        "Measure remaining distance to the first mark",
        "If it extruded 95 mm instead of 100 mm: new e-steps = current × (100 / 95)",
        "Update e-steps in firmware or EEPROM",
        "Repeat until within 1 mm accuracy",
    ]
    for i, s in enumerate(esteps, 1):
        elems.append(Paragraph(f"{i}.  {s}", styles["bullet"]))

    elems.append(PageBreak())
    return elems


def build_layer_adhesion(styles):
    elems = []
    elems += section_heading("Section 5 — Layer Adhesion Problems", styles)
    elems.append(Paragraph(
        "Layers split apart when flexing or dropping the part; visible gaps between "
        "layers from the side; print breaks cleanly along a layer line.",
        styles["body_italic"]
    ))
    elems.append(Spacer(1, 4))

    elems += sub_heading("Critical Layer Height Rule", styles)
    elems.append(Paragraph(
        "<b>Maximum layer height = 75–80 % of nozzle diameter.</b><br/>"
        "0.4 mm nozzle → max 0.28–0.32 mm  |  "
        "0.6 mm nozzle → max 0.45–0.48 mm  |  "
        "0.8 mm nozzle → max 0.60–0.64 mm",
        styles["body"]
    ))
    elems.append(Spacer(1, 4))

    elems += sub_heading("Temperature vs Layer Adhesion", styles)
    hdr = ["MATERIAL", "MIN TEMP", "MAX TEMP", "NOTES"]
    rows = [
        ["PLA",   "195 °C", "220 °C", "Higher = stronger but more stringing"],
        ["PETG",  "230 °C", "250 °C", "240 °C+ for strength-critical parts"],
        ["ABS",   "230 °C", "250 °C", "Enclose for best layer bonding"],
        ["ASA",   "240 °C", "260 °C", "Same as ABS rules"],
        ["TPU",   "220 °C", "240 °C", "Slow + hot = best adhesion"],
        ["Nylon", "240 °C", "270 °C", "Dry filament is critical"],
    ]
    col_w = [BODY_W * 0.15, BODY_W * 0.15, BODY_W * 0.15, BODY_W * 0.55]
    elems.append(make_table([hdr] + rows, col_w))
    elems.append(Spacer(1, 5))

    elems += sub_heading("Fixes in Order of Impact", styles)
    fixes = [
        "Raise nozzle temperature 5–10 °C",
        "Reduce print speed by 20–30 % (especially wall speed)",
        "Reduce layer height (try 0.2 mm on 0.4 mm nozzle for strength-critical parts)",
        "Reduce part cooling fan speed (ABS/ASA: use 0–20 %)",
        "Increase number of perimeters/walls (3–4 walls dramatically improves strength)",
        "Check for under-extrusion and fix first (see Section 4)",
        "Dry filament if other fixes don't work",
    ]
    for i, f in enumerate(fixes, 1):
        elems.append(Paragraph(f"{i}.  {f}", styles["bullet"]))

    return elems


def build_first_layer(styles, img_path=None):
    elems = []
    elems += section_heading("Section 6 — First Layer Issues", styles)
    elems.append(Paragraph(
        "The first layer is the foundation of every print. Incorrect Z offset is the #1 cause of "
        "failed prints. Dial this in before adjusting anything else.",
        styles["body_italic"]
    ))
    elems.append(Spacer(1, 5))

    if img_path:
        try:
            img = Image(img_path, width=BODY_W * 0.42, height=48 * mm)
            img.hAlign = "RIGHT"
            elems.append(img)
        except Exception:
            pass

    elems += sub_heading("Z Offset Reference Table", styles)
    hdr = ["WHAT YOU SEE", "WHAT IT MEANS", "WHAT TO DO"]
    rows = [
        ["Lines not connected",       "Nozzle too high",                "Lower Z offset (more negative)"],
        ["Filament not sticking",     "Nozzle too high",                "Lower Z offset 0.05 mm steps"],
        ["Nozzle scraping bed",       "Nozzle too low",                 "Raise Z offset"],
        ["Squished flat, no texture", "Nozzle too low",                 "Raise Z offset 0.05 mm steps"],
        ["Transparent / thin lines",  "Nozzle too high",                "Lower Z offset"],
        ["Nice round lines, bonded",  "Correct Z offset",               "No change needed"],
        ["Elephant foot on base",     "Slightly too low",               "Raise 0.02–0.05 mm"],
        ["Lines lifting mid-layer",   "Z correct but bed not clean",    "IPA clean, re-level"],
    ]
    col_w = [BODY_W * 0.30, BODY_W * 0.30, BODY_W * 0.40]
    elems.append(make_table([hdr] + rows, col_w))
    elems.append(Spacer(1, 5))

    elems += sub_heading("First Layer Recommended Settings", styles)
    elems += bullet_list([
        "First layer height: 0.2–0.3 mm (regardless of other layer heights)",
        "First layer speed: 20–30 mm/s",
        "First layer flow: 100–105 %",
        "First layer fan: OFF for all materials",
        "First layer line width: 120–150 % of nozzle diameter",
    ], styles)

    elems.append(PageBreak())
    return elems


def build_nozzle_clogs(styles):
    elems = []
    elems += section_heading("Section 7 — Nozzle Clogs", styles)
    elems.append(Paragraph(
        "Most clogs are soft (carbonised material) and clear with a cold pull. "
        "Hard clogs may require nozzle replacement.",
        styles["body_italic"]
    ))
    elems.append(Spacer(1, 4))

    elems += sub_heading("Cold Pull Procedure", styles)
    steps = [
        "Heat nozzle to printing temperature for current material",
        "Manually push filament through until clean material emerges",
        "Lower temperature — PLA: 90 °C  |  PETG: 110 °C  |  ABS/ASA: 120 °C",
        "When target temp is reached, firmly but slowly pull filament straight out",
        "Inspect the tip — black residue = partial clog was present",
        "Reheat and repeat until pulled tip comes out clean and light-coloured",
        "Perform 3–5 cold pulls minimum for a stubborn clog",
    ]
    for i, s in enumerate(steps, 1):
        elems.append(Paragraph(f"{i}.  {s}", styles["bullet"]))
    elems.append(Spacer(1, 5))

    elems += sub_heading("When to Replace the Nozzle", styles)
    hdr = ["REPLACE NOZZLE WHEN…", "NOTES"]
    rows = [
        ["Cold pulls don't clear the clog",      "Hard clogs are not worth fighting"],
        ["Nozzle bore is visibly worn / oval",    "Common with abrasive filaments"],
        ["Printing abrasive > 500 hours",         "CF, GF, glow-in-dark, metallic fills"],
        ["Quality degraded despite tuning",       "Worn bore causes inconsistent flow"],
        ["Switching from abrasive to PLA",        "Wear affects precision prints"],
    ]
    col_w = [BODY_W * 0.45, BODY_W * 0.55]
    elems.append(make_table([hdr] + rows, col_w))
    elems.append(Spacer(1, 5))

    elems += sub_heading("Nozzle Material Guide", styles)
    elems += bullet_list([
        "Brass — best for PLA, PETG, ABS; cheap, great thermal conductivity",
        "Hardened Steel — use for carbon fibre, glass fibre, glow, metallic fills",
        "Stainless Steel — food-safe applications; slightly lower conductivity",
        "Ruby / Nozzle X — abrasive + long life; expensive but lasts years",
    ], styles)

    elems.append(PageBreak())
    return elems


def build_material_settings(styles):
    elems = []
    elems += section_heading("Section 8 — Material Settings Reference", styles)
    elems.append(Paragraph(
        "Starting-point ranges only. Your specific printer, filament brand, and hotend design will affect "
        "ideal settings. Always run a temp tower for new filament.",
        styles["body_italic"]
    ))
    elems.append(Spacer(1, 5))

    hdr = ["MATERIAL", "NOZZLE\nTEMP", "BED\nTEMP", "ENCLOSURE", "PART\nFAN", "SPEED", "RETRACTION\n(DD / Bowden)", "DRY AT"]
    rows = [
        ["PLA",      "190–220 °C", "55–65 °C",   "Not needed",   "100 %",    "40–80 mm/s",  "1–2 mm / 4–6 mm",   "45 °C / 4 h"],
        ["PLA+",     "200–230 °C", "60–65 °C",   "Optional",     "100 %",    "40–70 mm/s",  "1–2 mm / 4–6 mm",   "45 °C / 4 h"],
        ["PETG",     "230–250 °C", "70–90 °C",   "Optional",     "30–60 %",  "30–60 mm/s",  "0.8–1.5 mm / 4–5 mm","65 °C / 4 h"],
        ["ABS",      "230–250 °C", "100–110 °C", "Required",     "0–20 %",   "40–60 mm/s",  "1–2 mm / 4–6 mm",   "80 °C / 4 h"],
        ["ASA",      "240–260 °C", "100–110 °C", "Required",     "0–20 %",   "40–60 mm/s",  "1–2 mm / 4–6 mm",   "80 °C / 4 h"],
        ["TPU 95A",  "220–240 °C", "40–60 °C",   "Not needed",   "30–50 %",  "15–35 mm/s",  "0–1 mm / N/A",      "65 °C / 4 h"],
        ["TPU 85A",  "215–235 °C", "40–60 °C",   "Not needed",   "20–40 %",  "10–20 mm/s",  "0 mm / N/A",        "65 °C / 4 h"],
        ["Nylon",    "240–270 °C", "70–90 °C",   "Recommended",  "10–30 %",  "30–50 mm/s",  "1–2 mm / 4–5 mm",   "80 °C / 8 h"],
        ["PC",       "260–310 °C", "100–120 °C", "Required",     "0–20 %",   "25–50 mm/s",  "1–2 mm / 4–5 mm",   "80 °C / 6 h"],
    ]
    col_w = [
        BODY_W * 0.11,
        BODY_W * 0.11,
        BODY_W * 0.10,
        BODY_W * 0.12,
        BODY_W * 0.09,
        BODY_W * 0.12,
        BODY_W * 0.20,
        BODY_W * 0.15,
    ]
    elems.append(make_table([hdr] + rows, col_w))
    elems.append(Spacer(1, 4))
    elems.append(Paragraph("DD = Direct Drive  |  Bowden values are approximate — tube length affects ideal retraction.", styles["note"]))
    elems.append(Spacer(1, 6))

    elems += sub_heading("Filament Drying Reference", styles)
    hdr2 = ["MATERIAL", "DRY TEMP", "DRY TIME"]
    rows2 = [
        ["PLA",      "40–45 °C", "4–6 hours"],
        ["PETG",     "60–65 °C", "4–6 hours"],
        ["ABS/ASA",  "70–80 °C", "4–6 hours"],
        ["TPU",      "55–65 °C", "4–8 hours"],
        ["Nylon",    "75–80 °C", "8–12 hours"],
        ["PC",       "80–85 °C", "6–8 hours"],
    ]
    col_w2 = [BODY_W * 0.25, BODY_W * 0.25, BODY_W * 0.50]
    elems.append(make_table([hdr2] + rows2, col_w2))

    elems.append(PageBreak())
    return elems


def build_calibration_checklist(styles, img_path=None):
    elems = []
    elems += section_heading("Section 9 — Calibration Checklist", styles)
    elems.append(Paragraph(
        "Work through this checklist in order. Each step assumes the previous one is complete. "
        "A printer that is not calibrated cannot be tuned — fix fundamentals first.",
        styles["body_italic"]
    ))
    elems.append(Spacer(1, 5))

    if img_path:
        try:
            img = Image(img_path, width=BODY_W * 0.40, height=45 * mm)
            img.hAlign = "RIGHT"
            elems.append(img)
        except Exception:
            pass

    sections = [
        ("1.  Frame & Mechanical Checks", [
            "Frame is square and all bolts are tight — check all extrusion joints",
            "Build plate firmly attached — no wobble when pushed",
            "All grub screws on pulleys and couplers tight (especially Z couplers)",
            "Belts tensioned correctly — low guitar-string tone when plucked (35–50 Hz)",
            "Linear rods / rails clean and lightly lubricated",
            "Lead screws clean and lubricated with PTFE-based grease (not WD-40)",
            "No grinding or binding when axes moved by hand",
            "Extruder arm tension correct — filament held firm but not crushed",
        ]),
        ("2.  Electrical & Firmware Checks", [
            "Endstops trigger reliably (test via printer menu)",
            "Hotend thermistor reads room temperature within 3–5 °C of ambient",
            "Bed thermistor reads room temperature accurately",
            "Fans spin at correct speeds and in correct directions",
            "No loose wires in drag chain (wiggle test while monitoring temps)",
        ]),
        ("3.  E-Steps Calibration", [
            "Mark filament 100 mm and 120 mm above extruder inlet",
            "Command extrusion of 100 mm through terminal/menu",
            "Measure actual distance moved",
            "Calculate: New E-steps = Current E-steps × (100 ÷ actual mm moved)",
            "Update E-steps in EEPROM (M92 E[value] then M500 on Marlin)",
            "Repeat until within 1 mm accuracy (1 % error)",
        ]),
        ("4.  Bed Levelling", [
            "Run full mesh bed levelling at print temperature",
            "Minimum 3×3 mesh — recommend 5×5 or 9×9",
            "Save mesh to EEPROM (G29 S1 on many firmware versions)",
            "Confirm mesh loading is called in start G-code",
        ]),
        ("5.  Z Offset & First Layer", [
            "Set initial Z offset using paper method (0.1 mm resistance)",
            "Print first layer test — large flat square, single layer",
            "Lines should be slightly squished and touching — no gaps, not flat",
            "Adjust in 0.02–0.05 mm increments until correct",
            "Save Z offset to EEPROM",
        ]),
        ("6.  Temperature Calibration", [
            "Print a temperature tower for each new filament brand/colour",
            "Select best layer: best surface finish, no stringing, no gaps",
            "Record temperature per brand/colour for future use",
        ]),
        ("7.  Flow Rate / Extrusion Multiplier", [
            "Print single-wall cube (1 perimeter, no infill, 0 % top/bottom)",
            "Measure actual wall thickness with calipers",
            "Ideal = nozzle diameter (e.g. 0.4 mm)",
            "Adjust: New Flow % = Current Flow % × (nozzle diam. ÷ measured thickness)",
            "Typical result: 95–105 % is normal; outside this suggests a hardware issue",
        ]),
        ("8.  Retraction Calibration", [
            "Print retraction tower for specific material",
            "Start: 1 mm (direct drive) or 4 mm (Bowden)",
            "Increase 0.5 mm per step until stringing stops",
            "If still stringing at 3 mm+ (direct) or 7 mm+ (Bowden) — check for clog",
        ]),
        ("9.  Speed Calibration", [
            "Print calibration cube at baseline 50 mm/s",
            "Check for ringing/ghosting on walls",
            "If ringing: reduce acceleration (try 500–1500 mm/s²)",
            "Optionally run Input Shaper (Klipper) or Resonance Compensation (Marlin 2.x)",
        ]),
        ("10.  Final Validation Print", [
            "Print a 20 mm × 20 mm × 20 mm calibration cube",
            "Measure X, Y, Z — should be within 0.2 mm of 20 mm",
            "Inspect walls: smooth, no layer separation, no blobs",
            "Inspect top surface: closed, smooth, no pillowing",
            "Inspect bottom: no elephant foot, flat corners",
        ]),
    ]

    for title, items in sections:
        elems.append(Paragraph(title, styles["sub_heading"]))
        elems += checkbox_list(items, styles)
        elems.append(Spacer(1, 3))

    return elems


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════════
def main():
    print("=== FDM Troubleshooting Guide PDF Generator ===")
    print(f"Output: {OUTPUT_PATH}\n")

    # Download images
    print("Downloading images from Unsplash...")
    img_paths = [download_image(url, i) for i, url in enumerate(IMAGE_URLS)]
    cover_img     = img_paths[0]   # 3D printer
    stringing_img = img_paths[1]   # close-up
    firstlayer_img= img_paths[2]   # filament
    calib_img     = img_paths[3]   # printed parts

    styles = make_styles()

    # Track which page is cover vs interior
    _page_state = {"is_cover": True}

    def on_page_dispatch(canvas, doc):
        if _page_state["is_cover"]:
            on_page_cover(canvas, doc)
            _page_state["is_cover"] = False
        else:
            on_page(canvas, doc)

    doc = SimpleDocTemplate(
        str(OUTPUT_PATH),
        pagesize=A4,
        leftMargin=MARGIN_L,
        rightMargin=MARGIN_R,
        topMargin=MARGIN_T,
        bottomMargin=MARGIN_B,
        title="The Complete FDM Troubleshooting Guide",
        author="Print3DBuddy",
    )

    story = []

    # Page 1 — Cover
    story += build_cover(styles, cover_img)

    # Page 2 — Quick Reference Table
    story += build_quick_reference(styles)

    # Pages 3–4 — Stringing, Warping, Under-extrusion
    story += build_stringing(styles, stringing_img)
    story += build_warping(styles)
    story += build_under_extrusion(styles)

    # Pages 5–6 — Layer adhesion, First layer, Nozzle clogs
    story += build_layer_adhesion(styles)
    story.append(PageBreak())
    story += build_first_layer(styles, firstlayer_img)
    story += build_nozzle_clogs(styles)

    # Page 7 — Material Settings Reference
    story += build_material_settings(styles)

    # Page 8 — Calibration Checklist
    story += build_calibration_checklist(styles, calib_img)

    print("Building PDF...")
    doc.build(story, onFirstPage=on_page_cover, onLaterPages=on_page)
    print(f"\nDone! PDF saved to: {OUTPUT_PATH}")

    cleanup_images()


if __name__ == "__main__":
    main()
