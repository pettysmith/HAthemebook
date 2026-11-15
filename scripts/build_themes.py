#!/usr/bin/env python3
"""Erzeugt themes/themebook.yaml aus palettes.json.

Je Palette entstehen zwei Themes:
- "Viewsta <Palette>": vollständiges Theme mit heller und dunkler Fassung
  (Schlüssel `modes`). Setzt die Palette der Viewsta-Karten und die Farben
  von Home Assistant. Gedacht für die Auswahl im Profil.
- "Viewsta <Palette> · nur Karten": setzt nur `viewsta-palette`. Gedacht für
  eine einzelne Ansicht über einem anderen Theme, das unverändert bleiben soll.

Das Skript prüft die Kontraste (WCAG) und bricht ab, wenn ein Paar zu schwach ist.
Variablennamen: Quelltext des Home-Assistant-Frontends (siehe CREDITS.md).
"""
import colorsys, json, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
pal = json.loads((ROOT / "palettes.json").read_text(encoding="utf-8"))
SCALE = {"05": .006, "10": .015, "20": .03, "30": .07, "40": .16, "50": .26,
         "60": .38, "70": .52, "80": .68, "90": .84, "95": .92}


def slug(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def rgb(h):
    return [int(h[i:i + 2], 16) for i in (1, 3, 5)]


def hexc(c):
    return "#" + "".join(f"{max(0, min(255, round(v))):02x}" for v in c)


def lum(h):
    c = [(v / 255 / 12.92 if v / 255 <= .03928 else ((v / 255 + .055) / 1.055) ** 2.4) for v in rgb(h)]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]


def contrast(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True)
    return (x + .05) / (y + .05)


def mix(a, b, t):
    """t Anteile a, Rest b."""
    return hexc([x * t + y * (1 - t) for x, y in zip(rgb(a), rgb(b))])


def bw(bg):
    return "#000000" if contrast(bg, "#000000") >= contrast(bg, "#ffffff") else "#ffffff"


def sat(h):
    r, g, b = (v / 255 for v in rgb(h))
    return colorsys.rgb_to_hls(r, g, b)[2]


def tone(h, target):
    """Gleicher Farbton, auf die Ziel-Helligkeit (relative Luminanz) gebracht."""
    other = "#000000" if lum(h) > target else "#ffffff"
    lo, hi = 0.0, 1.0
    for _ in range(40):
        mid = (lo + hi) / 2
        c = mix(h, other, mid)
        if (lum(c) > target) == (other == "#000000"):
            hi = mid
        else:
            lo = mid
    return mix(h, other, (lo + hi) / 2)


def reach(h, bg, need):
    """Farbe so weit abdunkeln oder aufhellen, bis sie auf bg den Kontrast erreicht."""
    if contrast(h, bg) >= need:
        return h
    other = "#000000" if lum(bg) > .4 else "#ffffff"
    for i in range(1, 101):
        c = mix(other, h, i / 100)
        if contrast(c, bg) >= need:
            return c
    return other


problems = []


def check(name, mode, what, fg, bg, need):
    c = contrast(fg, bg)
    if c < need:
        problems.append(f"{name} ({mode}): {what} {fg} auf {bg} = {c:.2f}, nötig {need}")


def mode_vars(name, p, dark, night=False):
    A = p["accent"]
    if night:
        bg, card, sbg = "#000000", "#0d0201", "#1a0503"
        text = "#ff3b30"
        sec = reach("#d9453a", card, 4.5)
        dis = "#7a1d17"
        primary = "#ff3b30"
        accent = "#ff3b30"
    elif dark:
        bg, card, sbg = mix(A, "#0b0b0d", .05), mix(A, "#1c1c1e", .05), mix(A, "#2a2a2d", .07)
        text, sec, dis = "#f4f4f6", "#a6a6ab", "#6f6f74"
        primary = reach(p["accentInk"], card, 4.5)
        cand = p.get("contrast", A)
        accent = cand if sat(cand) > .15 and contrast(cand, card) >= 3 else primary
    else:
        bg, card, sbg = mix(A, "#f5f5f7", .07), "#ffffff", mix(A, "#e9e9ee", .09)
        text, sec, dis = "#141a1c", "#5a5f64", "#a8a8ad"
        primary = None
        for c in (A, p["onAccent"], p["secondary"]):
            if sat(c) > .15 and contrast(c, card) >= 4.5 and contrast(c, bg) >= 4.5:
                primary = c
                break
        if primary is None:
            primary = reach(A if sat(A) > .15 else "#3a3a3c", bg, 4.5)
        accent = reach(A, card, 3) if sat(A) > .15 else primary
    scale = {k: tone(primary, y) for k, y in SCALE.items()}
    active = accent if contrast(accent, card) >= 3 else primary
    v = {
        "primary-color": primary,
        "text-primary-color": bw(primary),
        "light-primary-color": scale["80"],
        "text-light-primary-color": bw(scale["80"]),
        "dark-primary-color": scale["30"],
        "darker-primary-color": scale["20"],
        "accent-color": accent,
        "text-accent-color": bw(accent),
        "primary-background-color": bg,
        "secondary-background-color": sbg,
        "card-background-color": card,
        "clear-background-color": bg,
        "primary-text-color": text,
        "secondary-text-color": sec,
        "disabled-text-color": dis,
        "app-header-background-color": bg,
        "app-header-text-color": text,
        "state-icon-color": sec if not night else text,
        "state-active-color": active,
        "state-light-active-color": active,
        "state-switch-active-color": active,
        "ha-color-on-primary-loud": bw(scale["40"]),
    }
    for k, c in scale.items():
        v[f"ha-color-primary-{k}"] = c
    mode = "Nacht" if night else ("dunkel" if dark else "hell")
    strong = 4.5 if night else 7
    check(name, mode, "Text auf Hintergrund", text, bg, strong)
    check(name, mode, "Text auf Karte", text, card, strong)
    check(name, mode, "Nebentext auf Karte", sec, card, 4.5)
    check(name, mode, "Nebentext auf Hintergrund", sec, bg, 4.5)
    check(name, mode, "Primärfarbe als Schrift auf Karte", primary, card, 4.5)
    check(name, mode, "Primärfarbe als Schrift auf Hintergrund", primary, bg, 4.5)
    check(name, mode, "Schrift auf Primärfarbe", v["text-primary-color"], primary, 4.5)
    check(name, mode, "Akzent auf Karte", accent, card, 3)
    check(name, mode, "Schrift auf Akzent", v["text-accent-color"], accent, 4.5)
    check(name, mode, "Schrift auf Schaltfläche", v["ha-color-on-primary-loud"], scale["40"], 4.5)
    check(name, mode, "Aktive Zustände auf Karte", active, card, 3)
    return v


def emit(out, d, indent):
    for k, val in d.items():
        out.append(f'{" " * indent}{k}: "{val}"')


out = ["# Erzeugt von scripts/build_themes.py aus palettes.json. Nicht von Hand ändern.",
       "# 'Viewsta <Palette>': vollständiges Theme mit heller und dunkler Fassung, für die Auswahl im Profil.",
       "# 'Viewsta <Palette> · nur Karten': setzt nur die Palette der Viewsta-Karten, für eine Ansicht über einem anderen Theme."]
items = [(p["name"], p, False) for p in pal["palettes"]] + [(pal["night"]["name"], pal["night"], True)]
for n, p, night in items:
    out.append(f'"Viewsta {n}":')
    out.append(f'  viewsta-palette: "{slug(n)}"')
    out.append('  ha-card-border-radius: "24px"')
    out.append('  ha-card-box-shadow: "none"')
    if night:
        emit(out, mode_vars(n, p, True, True), 2)
    else:
        out.append("  modes:")
        out.append("    light:")
        emit(out, mode_vars(n, p, False), 6)
        out.append("    dark:")
        emit(out, mode_vars(n, p, True), 6)
for n, p, night in items:
    out += [f'"Viewsta {n} · nur Karten":', f'  viewsta-palette: "{slug(n)}"']

if problems:
    print("Kontrast zu schwach:")
    for x in problems:
        print(" -", x)
    sys.exit(1)
(ROOT / "themes").mkdir(exist_ok=True)
(ROOT / "themes" / "themebook.yaml").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"{2 * len(items)} Themes geschrieben, alle Kontraste bestanden.")
