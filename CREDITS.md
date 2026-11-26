# Quellen und Lizenzen

Stand: 0.4.0. Jeder neue Baustein wird hier eingetragen, bevor er veröffentlicht wird.

| Quelle | Wofür | Lizenz | Stand |
| --- | --- | --- | --- |
| Home Assistant Frontend (github.com/home-assistant/frontend, Stand 15. November 2026, Commit f2d0da0): `src/resources/theme/color/*.ts`, `src/common/dom/apply_themes_on_element.ts`, `src/data/ws-themes.ts` | Namen der Theme-Variablen, Schlüssel `modes` mit `light` und `dark`, Farbstufen `ha-color-primary-05` bis `-95` | Apache License 2.0; nur Variablennamen verwendet, kein Code und keine Farbwerte übernommen | an der Quelle gelesen |
| Home Assistant Frontend (github.com/home-assistant/frontend, Stand 25. November 2026, Commit 25307e4): `src/components/ha-card.ts`, `src/panels/lovelace/sections/hui-grid-section.ts`, `src/panels/lovelace/views/hui-sections-view.ts`, `src/panels/lovelace/cards/hui-tile-card.ts`, `src/resources/theme/typography.globals.ts`, `src/resources/roboto.ts` | Variablen der Looks: `ha-card-border-width`, `ha-section-grid-row-gap`, `ha-section-grid-column-gap`, `ha-section-border-radius`, `ha-tile-icon-border-radius`; Schrift Roboto ist im Frontend enthalten | Apache License 2.0; nur Variablennamen verwendet | an der Quelle gelesen |
| Archivo Black (The Archivo Black Project Authors, Omnibus-Type) | Titelschrift im Look Magazin; eingebettet in Viewsta, hier nur über `viewsta-font: archivo` gewählt | SIL Open Font License 1.1 | Lizenz in Viewsta geprüft (LICENSES.txt) |
| Apple StandBy | Gestalterisches Vorbild: Querformat, Schwarz, randlos | Marke der Apple Inc.; weder Code noch Bilder übernommen | geprüft |
| Farbwerte in `palettes.json` | Paletten | eigene Zusammenstellung des Autors | geprüft |
| Dieses Repository | Themes, Skript, Dokumentation | MIT License | geprüft |
