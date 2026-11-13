# Themebook

Companion themes for the card collection [Viewsta](https://github.com/pettysmith/HAviewsta). Each theme only sets the palette for the Viewsta cards. It changes nothing else in Home Assistant, so it works together with any theme such as Frosted Glass.

## Themes

Viewsta Gelb · Silber, Rosa · Blau, Limette · Tanne, Orange · Creme, Mint · Marine, Rot · Rosé, Lila · Gelb, Pfirsich · Bordeaux, Blau · Eis, Grün · Pink, Silber · Schwarz, Marine · Creme, and Nachtrot.

## Installation

1. Make sure `configuration.yaml` loads themes from the `themes` folder:

   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```

2. Settings → Marketplace → **Add from link** → `pettysmith/HAthemebook` → install.
3. Reload themes (Developer tools → YAML → Reload themes).

## Use

Do not choose these themes in your profile, that would replace your own theme. Choose one per view: Edit dashboard → pencil next to the view name → **Theme** dropdown → a Viewsta theme. Cards inside that view then use the palette. A palette set on a single card with the option `palette` always wins.

## Build

`palettes.json` holds the colors, `python3 scripts/build_themes.py` writes `themes/themebook.yaml`.

## License and credits

MIT, see `LICENSE`. Sources: `CREDITS.md`.
