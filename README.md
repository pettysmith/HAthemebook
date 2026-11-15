# Themebook

Companion themes for the card collection [Viewsta](https://github.com/pettysmith/HAviewsta). Version 0.2.0.

Every palette comes as two themes:

| Theme | What it does | Where to choose it |
| --- | --- | --- |
| `Viewsta <palette>` | Complete theme with a light and a dark version. Sets the palette of the Viewsta cards and the colors of Home Assistant (background, cards, text, primary and accent color, buttons, active states). | In your profile |
| `Viewsta <palette> · nur Karten` | Only sets the palette of the Viewsta cards. Changes nothing else, so it works on top of any theme such as Frosted Glass. | Per view |

Palettes: Gelb · Silber, Rosa · Blau, Limette · Tanne, Orange · Creme, Mint · Marine, Rot · Rosé, Lila · Gelb, Pfirsich · Bordeaux, Blau · Eis, Grün · Pink, Silber · Schwarz, Marine · Creme, and Nachtrot (dark only, everything red on black).

## Installation

1. Make sure `configuration.yaml` loads themes from the `themes` folder:

   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```

2. Settings → Marketplace → **Add from link** → `pettysmith/HAthemebook` → install.
3. Reload themes (Developer tools → YAML → Reload themes).

## Use

- **Whole interface:** profile → Theme → `Viewsta <palette>`. Light or dark follows the mode chosen below the theme (or your device).
- **One view only, keeping your own theme:** Edit dashboard → pencil next to the view name → Theme → `Viewsta <palette> · nur Karten`.

A palette set on a single card with the option `palette` always wins.

## Contrast

The build script checks every theme and stops if a pair is too weak: text on background and cards at least 7:1 (Nachtrot 4.5:1), secondary text 4.5:1, primary color as text 4.5:1, text on primary and accent color 4.5:1, accent and active states against cards 3:1. In the light version bright accents such as yellow are darkened for text and buttons; the Viewsta cards keep the original colors.

## Build

`palettes.json` holds the colors, `python3 scripts/build_themes.py` writes `themes/themebook.yaml`.

## License and credits

MIT, see `LICENSE`. Sources: `CREDITS.md`.
