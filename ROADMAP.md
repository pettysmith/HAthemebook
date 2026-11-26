# Roadmap

Entscheidung des Projektinhabers (0.2.0): Die Themes sollen auch im Profil stimmig aussehen. Deshalb gibt es je Palette ein vollständiges Theme mit heller und dunkler Fassung und daneben eine Fassung „nur Karten“, die andere Gestaltungen (etwa Frosted Glass) nicht überschreibt.

## 0.5.0
Drei Sets mit heller und dunkler Fassung: Metro Mono, Duet Blue, Duet Orange. Jede Kartenart hat eine feste Farbe (Variablen `viewsta-<kartenart>-accent`, `-on`, `-surface`), Regler eine Kontrastfarbe (`viewsta-control`), Metro Mono mit eckigen Reglern. 43 Themes, alle Kontrastprüfungen bestanden. Benötigt Viewsta 0.10.0. Offen: Ansicht in einem laufenden Home Assistant.

## 0.4.0
Vier Looks als dunkle Themes für das Profil: Duet (runde farbige Kacheln, Pfirsich · Bordeaux), Metro zeitgemäß und klassisch (quadratisch, ohne Rand, enge Fugen, Schrift von Home Assistant), Magazin (Papier, Schwarz, Rot, Archivo Black; Foto über den Hintergrund-Editor der Ansicht). Neue Variablen aus dem Frontend-Quelltext: Kartenrahmen, Abstände und Ecken der Abschnitte-Ansicht, Ecken der Symbole in Kacheln. 40 Themes, alle Kontrastprüfungen bestanden. Benötigt Viewsta 0.9.1 (Palette an der Karte hat Vorrang vor den Farben des Looks). Offen: Ansicht in einem laufenden Home Assistant.

## 0.3.0
36 Themes: fünf neue Paletten (Himmel · Nachtblau, Zitrone · Graphit, Salbei · Tanne, Koralle · Petrol, Flieder · Tinte), je vollständig mit heller und dunkler Fassung und als „nur Karten“. Paletten gleich wie in Viewsta 0.9.0. Alle Kontrastprüfungen bestanden. Offen: Ansicht in einem laufenden Home Assistant.

## 0.2.0 (vorbereitet)
26 Themes: 13 vollständige (12 mit heller und dunkler Fassung, Nachtrot nur dunkel) und 13 „nur Karten“. Kontrastprüfung im Build-Skript. Variablennamen aus dem Quelltext des Home-Assistant-Frontends. Geprüft mit einer nachgebauten Oberfläche im Browser. Offen: Ansicht in einem laufenden Home Assistant, besonders Schaltflächen, Schalter, Diagramme und Dialoge.

Hinweis zum Umstieg: Die Namen `Viewsta <Palette>` sind jetzt die vollständigen Themes. Wer sie bisher pro Ansicht über einem anderen Theme genutzt hat, wählt dort künftig `Viewsta <Palette> · nur Karten`.

## 0.1.0
13 Themes, die nur `viewsta-palette` setzen. Nach Screenshots des Projektinhabers in Home Assistant installiert und in der Ansicht wählbar.

## Später
- Themes mit zusätzlicher Schriftwahl.
- Eigene Farben für Diagramme und weitere Zustände, falls gewünscht.
