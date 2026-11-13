#!/usr/bin/env python3
"""Erzeugt themes/themebook.yaml aus palettes.json.

Jedes Theme setzt nur eine Variable: viewsta-palette. Die Viewsta-Karten lesen sie aus.
"""
import json, re, pathlib, unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
pal = json.loads((ROOT / "palettes.json").read_text(encoding="utf-8"))

def slug(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

names = [p["name"] for p in pal["palettes"]] + [pal["night"]["name"]]
out = ["# Erzeugt von scripts/build_themes.py aus palettes.json. Nicht von Hand ändern.",
       "# Diese Themes setzen nur Variablen für die Viewsta-Karten und verändern sonst nichts an Home Assistant."]
for n in names:
    out.append(f'"Viewsta {n}":')
    out.append(f'  viewsta-palette: "{slug(n)}"')
(ROOT / "themes").mkdir(exist_ok=True)
(ROOT / "themes" / "themebook.yaml").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"{len(names)} Themes geschrieben.")
