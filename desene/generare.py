import math
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 700, 440
FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/TTF/DejaVuSans.ttf",
]


def load_font(size):
    for path in FONT_PATHS:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size=size)


ATOM_FONT = load_font(26)
TITLE_FONT = load_font(22)
NOTE_FONT = load_font(18)


def label(d, x, y, text):
    box = d.textbbox((x, y), text, font=ATOM_FONT, anchor="mm")
    d.rectangle([box[0] - 4, box[1] - 2, box[2] + 4, box[3] + 2], fill="white")
    d.text((x, y), text, font=ATOM_FONT, fill="black", anchor="mm")


def bond(d, p, q, order=1):
    (x1, y1), (x2, y2) = p, q
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    nx, ny = -dy / length, dx / length
    offsets = {1: [0], 2: [-5, 5], 3: [-8, 0, 8]}[order]
    for o in offsets:
        d.line(
            [(x1 + nx * o, y1 + ny * o), (x2 + nx * o, y2 + ny * o)],
            fill="black",
            width=3,
        )


def figure(number, title, note, atoms, bonds):
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    for a, b, order in bonds:
        bond(d, atoms[a][:2], atoms[b][:2], order)
    for x, y, text in atoms.values():
        label(d, x, y, text)
    d.text((W / 2, 28), title, font=TITLE_FONT, fill="black", anchor="mm")
    d.text((W / 2, H - 28), note, font=NOTE_FONT, fill="black", anchor="mm")
    name = f"fig{number:02d}.png"
    img.save(os.path.join(HERE, name))
    return name


def hexagon(d, cx, cy, r):
    pts = [
        (cx + r * math.cos(math.radians(30 + 60 * k)), cy + r * math.sin(math.radians(30 + 60 * k)))
        for k in range(6)
    ]
    d.line(pts + [pts[0]], fill="black", width=3)


def ring_figure(number, title, note, centers, r, connect=None):
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    for cx, cy in centers:
        hexagon(d, cx, cy, r)
    if connect:
        d.line(connect, fill="black", width=3)
    d.text((W / 2, 28), title, font=TITLE_FONT, fill="black", anchor="mm")
    d.text((W / 2, H - 28), note, font=NOTE_FONT, fill="black", anchor="mm")
    name = f"fig{number:02d}.png"
    img.save(os.path.join(HERE, name))
    return name


def build():
    entries = []

    entries.append((
        "Atom de C nular (metan, CH4)",
        "Tipuri de atomi de carbon > Nular",
        figure(1, "Atom nular - metan (CH4)", "C: 0 vecini de C, 4 cu H",
               {"C": (350, 220, "C"), "H1": (350, 100, "H"), "H2": (350, 340, "H"),
                "H3": (150, 220, "H"), "H4": (550, 220, "H")},
               [("C", "H1", 1), ("C", "H2", 1), ("C", "H3", 1), ("C", "H4", 1)]),
    ))

    entries.append((
        "Atom de C primar (etan, C2H6)",
        "Tipuri de atomi de carbon > Primar",
        figure(2, "Atom primar - etan (C2H6)", "C: 1 vecin de C -> primar",
               {"C1": (250, 220, "C"), "C2": (450, 220, "C"),
                "a": (250, 100, "H"), "b": (250, 340, "H"), "c": (80, 220, "H"),
                "d": (450, 100, "H"), "e": (450, 340, "H"), "f": (620, 220, "H")},
               [("C1", "C2", 1), ("C1", "a", 1), ("C1", "b", 1), ("C1", "c", 1),
                ("C2", "d", 1), ("C2", "e", 1), ("C2", "f", 1)]),
    ))

    entries.append((
        "Atom de C secundar (propan, C3H8)",
        "Tipuri de atomi de carbon > Secundar",
        figure(3, "Atom secundar - propan (C3H8)", "C2: 2 vecini de C -> secundar",
               {"C1": (190, 220, "C"), "C2": (350, 220, "C"), "C3": (510, 220, "C"),
                "a": (190, 100, "H"), "b": (190, 340, "H"), "c": (40, 220, "H"),
                "d": (350, 100, "H"), "e": (350, 340, "H"),
                "f": (510, 100, "H"), "g": (510, 340, "H"), "h": (660, 220, "H")},
               [("C1", "C2", 1), ("C2", "C3", 1), ("C1", "a", 1), ("C1", "b", 1), ("C1", "c", 1),
                ("C2", "d", 1), ("C2", "e", 1), ("C3", "f", 1), ("C3", "g", 1), ("C3", "h", 1)]),
    ))

    entries.append((
        "Atom de C terțiar (2-metilbutan, C5H12)",
        "Tipuri de atomi de carbon > Terțiar",
        figure(4, "Atom terțiar - 2-metilbutan (C5H12)", "C2 (CH): 3 vecini de C -> terțiar",
               {"C1": (90, 220, "CH3"), "C2": (240, 220, "CH"), "C3": (390, 220, "CH2"),
                "C4": (540, 220, "CH3"), "C5": (240, 360, "CH3"), "H": (240, 100, "H")},
               [("C1", "C2", 1), ("C2", "C3", 1), ("C3", "C4", 1), ("C2", "C5", 1), ("C2", "H", 1)]),
    ))

    entries.append((
        "Atom de C cuaternar (3,3-dimetilbut-1-ină, C6H10)",
        "Tipuri de atomi de carbon > Cuaternar",
        figure(5, "Atom cuaternar - 3,3-dimetilbut-1-ina (C6H10)", "C3: 4 vecini de C -> cuaternar",
               {"H": (60, 220, "H"), "C1": (170, 220, "C"), "C2": (320, 220, "C"),
                "C3": (470, 220, "C"), "M1": (470, 90, "CH3"), "M2": (470, 350, "CH3"),
                "M3": (630, 220, "CH3")},
               [("H", "C1", 1), ("C1", "C2", 3), ("C2", "C3", 1),
                ("C3", "M1", 1), ("C3", "M2", 1), ("C3", "M3", 1)]),
    ))

    entries.append((
        "Formula structurală plană cu linii de valență (3-metilpent-1-ină, C6H10)",
        "Formule > Formula structurală > a) cu linii de valență",
        figure(6, "Formula structurala plana cu linii de valenta", "3-metilpent-1-ina, C6H10",
               {"H0": (50, 220, "H"), "C1": (130, 220, "C"), "C2": (240, 220, "C"),
                "C3": (350, 220, "C"), "C4": (460, 220, "C"), "C5": (570, 220, "C"),
                "H3": (350, 100, "H"), "CH3": (350, 350, "CH3"),
                "H4a": (460, 100, "H"), "H4b": (460, 340, "H"),
                "H5a": (570, 100, "H"), "H5b": (570, 340, "H"), "H5c": (650, 220, "H")},
               [("H0", "C1", 1), ("C1", "C2", 3), ("C2", "C3", 1), ("C3", "C4", 1),
                ("C4", "C5", 1), ("C3", "H3", 1), ("C3", "CH3", 1), ("C4", "H4a", 1),
                ("C4", "H4b", 1), ("C5", "H5a", 1), ("C5", "H5b", 1), ("C5", "H5c", 1)]),
    ))

    entries.append((
        "Formula de poziție plană rezumată (3-metilpent-1-ină)",
        "Formule > Formula structurală > b) de poziție plană rezumată",
        figure(7, "Formula de pozitie plana rezumata", "CH#C-CH(CH3)-CH2-CH3",
               {"C1": (90, 220, "CH"), "C2": (210, 220, "C"), "C3": (330, 220, "CH"),
                "C4": (450, 220, "CH2"), "C5": (575, 220, "CH3"), "M": (330, 360, "CH3")},
               [("C1", "C2", 3), ("C2", "C3", 1), ("C3", "C4", 1), ("C4", "C5", 1), ("C3", "M", 1)]),
    ))

    skeleton_bonds = [("C1", "C2", 3), ("C2", "C3", 1), ("C3", "C4", 1),
                      ("C4", "C5", 2), ("C5", "C6", 1)]

    entries.append((
        "Scheletul catenei (se dă)",
        "Aplicație > Se dă scheletul catenei",
        figure(8, "Scheletul catenei", "C#C-C-C=C-C, cu ramificatii",
               {"C1": (90, 220, "C"), "C2": (190, 220, "C"), "C3": (290, 220, "C"),
                "C4": (390, 220, "C"), "C5": (490, 220, "C"), "C6": (590, 220, "C"),
                "T": (390, 100, "C"), "B": (290, 340, "C")},
               skeleton_bonds + [("C4", "T", 1), ("C3", "B", 1)]),
    ))

    entries.append((
        "Completarea cu H a catenei",
        "Aplicație > a) Completarea cu H",
        figure(9, "Catena completata cu H", "C8H12",
               {"C1": (90, 220, "C"), "C2": (190, 220, "C"), "C3": (290, 220, "C"),
                "C4": (390, 220, "C"), "C5": (490, 220, "C"), "C6": (590, 220, "CH3"),
                "Hc1": (30, 220, "H"), "Hc3": (290, 100, "H"), "Hc5": (490, 100, "H"),
                "T": (390, 100, "CH3"), "B": (290, 340, "CH3")},
               skeleton_bonds + [("C1", "Hc1", 1), ("C3", "Hc3", 1), ("C5", "Hc5", 1),
                                 ("C4", "T", 1), ("C3", "B", 1)]),
    ))

    entries.append((
        "Naftalina (inele condensate, C10H8)",
        "Hidrocarburi aromatice > Polinucleare > a) cu inele condensate",
        ring_figure(10, "Naftalina (inele condensate)", "C10H8",
                    [(240, 220), (240 + math.sqrt(3) * 70, 220)], 70),
    ))

    entries.append((
        "Bifenil (inele izolate, C12H10)",
        "Hidrocarburi aromatice > Polinucleare > b) cu inele izolate",
        ring_figure(11, "Bifenil (inele izolate)", "C12H10",
                    [(200, 220), (500, 220)], 70,
                    connect=[(200 + 70 * math.cos(math.radians(0)), 220),
                             (500 - 70 * math.cos(math.radians(0)), 220)]),
    ))

    lines = ["# Index figuri", "", "Imaginile sunt în acest folder (fig01.png ... fig11.png).", ""]
    for i, (name, section, fname) in enumerate(entries, start=1):
        lines.append(f"## Fig {i}: {name}")
        lines.append(f"Secțiune: {section}")
        lines.append("")
        lines.append(f"![Fig {i}]({fname})")
        lines.append("")
    with open(os.path.join(HERE, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    build()
