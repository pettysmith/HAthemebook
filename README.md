# Themebook

Companion themes for the card collection [Viewsta](https://github.com/pettysmith/HAviewsta). Version 0.7.0.

Without a Viewsta theme (for example with Frosted Glass in your profile) the Viewsta cards follow your dashboard theme: glass, blur, border, corners and font come from that theme. Needs Viewsta 0.11.0.

Every theme has a light and a dark version and is meant to be chosen in your profile. Light or dark follows the mode chosen below the theme (or your device). Nachtrot is dark only.

`Viewsta <palette>` sets the palette of the Viewsta cards and the colors of Home Assistant (background, cards, text, primary and accent color, buttons, active states).

Palettes: Gelb · Silber, Rosa · Blau, Limette · Tanne, Orange · Creme, Mint · Marine, Rot · Rosé, Lila · Gelb, Pfirsich · Bordeaux, Blau · Eis, Grün · Pink, Silber · Schwarz, Marine · Creme, Himmel · Nachtblau, Zitrone · Graphit, Salbei · Tanne, Koralle · Petrol, Flieder · Tinte, and Nachtrot (dark only, everything red on black).

## Looks

Four themes that set shape and font as well as colors.

| Theme | Look |
| --- | --- |
| `Viewsta Duet` | Rounded colorful tiles in the style of a bedside clock, palette Pfirsich · Bordeaux, no borders |
| `Viewsta Metro · klassisch` | Square single-color tiles, no corners, narrow gaps (6 px), Home Assistant font, cobalt blue on black |
| `Viewsta Magazin` | Paper, black and red, headline font Archivo Black |

### Sets

Four themes with a light and a dark version in which every card type has its own fixed color, so a dashboard looks varied without setting colors card by card. Sliders and switches use a contrast color.

| Theme | Look |
| --- | --- |
| `Viewsta Metro Present` | Square tiles in electric blue, stone, coral, lime, lavender, graphite and dark green, lime sliders, square controls |
| `Viewsta Metro Mono` | Square tiles in light grey and graphite, one orange and one yellow tile, orange sliders, square controls |
| `Viewsta Duet Blue` | Rounded tiles in light grey, ultramarine and near black, acid green for running timers and as slider color |
| `Viewsta Duet Orange` | Rounded tiles in light grey, orange and graphite, orange sliders |

Needs Viewsta 0.10.0 or newer. A palette chosen on a card still wins.

For a photo behind a view, use Home Assistant's own setting: Edit dashboard → pencil next to the view name → **Background** → upload an image and set its opacity. The Magazin look is made for black-and-white photos there.

In every look you can give a single Viewsta card its own color with the option `palette`, for example several colors side by side for a mosaic in Metro. The palette on the card always wins.

## Installation

1. Make sure `configuration.yaml` loads themes from the `themes` folder:

   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```

2. Settings → Marketplace → **Add from link** → `pettysmith/HAthemebook` → install.
3. Reload themes (Developer tools → YAML → Reload themes).

## Use

Profile → Theme → pick a Viewsta theme, then choose light, dark or automatic below it.

A palette set on a single card with the option `palette` always wins.

## Contrast

The build script checks every theme and stops if a pair is too weak: text on background and cards at least 7:1 (Nachtrot 4.5:1), secondary text 4.5:1, primary color as text 4.5:1, text on primary and accent color 4.5:1, accent and active states against cards 3:1. In the light version bright accents such as yellow are darkened for text and buttons; the Viewsta cards keep the original colors.

## Build

`palettes.json` holds the colors, `python3 scripts/build_themes.py` writes `themes/themebook.yaml`.

## License and credits

MIT, see `LICENSE`. Sources: `CREDITS.md`.
