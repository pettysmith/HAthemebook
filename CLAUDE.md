# Arbeitsanweisung für Claude Code

Projekt: Begleit-Themes für die Karten des Repos Viewsta. Öffentliches Theme-Repository für den Marketplace von Home Assistant. Je Palette gibt es zwei Themes: ein vollständiges mit heller und dunkler Fassung für die Auswahl im Profil und eines mit dem Zusatz „nur Karten“, das nur die Variable `viewsta-palette` setzt und sonst nichts an Home Assistant verändert.

Persönliche Arbeitsregeln des Projektinhabers und alle privaten Angaben stehen in einer Ergänzung, die nicht im Repo liegt:
@~/.claude/standby-privat.md
Fehlt die Datei, arbeite mit den Regeln unten weiter und frage nach, statt zu raten.

## Stand
`palettes.json`, `scripts/build_themes.py`, `themes/themebook.yaml` (40 Themes: 18 Paletten vollständig und „nur Karten“, dazu die Looks Duet, Metro zeitgemäß und klassisch, Magazin), `hacs.json`, `README.md`, `LICENSE`, `CREDITS.md`. Entscheidung des Projektinhabers (0.2.0): Die Themes sollen im Profil stimmig aussehen, deshalb setzen die vollständigen Themes wieder Farben von Home Assistant, jetzt mit heller und dunkler Fassung und geprüften Kontrasten. Wer ein anderes Theme wie Frosted Glass behalten will, nimmt die Fassung „nur Karten“ pro Ansicht.

## Erst lesen
ROADMAP.md, CREDITS.md, palettes.json, README.md

## Regeln
- Kurz antworten. Erst die gestellte Frage beantworten.
- Änderungen nur nach ausdrücklichem Auftrag. Vorher zeigen, welche Dateien sich ändern und mit welchem Inhalt, und die Freigabe abwarten. Commit und Push nur nach ausdrücklicher Freigabe, denn das Repo ist öffentlich.
- Nichts erfinden. Annahmen als offene Frage kennzeichnen.
- Die Themes „nur Karten“ setzen ausschließlich Variablen mit dem Präfix `viewsta-`. Die vollständigen Themes setzen nur Variablen, die im Quelltext des Home-Assistant-Frontends nachgelesen wurden, und jede Farbkombination muss die Kontrastprüfung des Skripts bestehen.

## Technik
- HACS-Theme-Repository: `themes/<name>.yaml`, `hacs.json`, `README.md`, `LICENSE`, `CREDITS.md`. Pro Repository wird eine Theme-Datei verwaltet; die Paletten liegen als mehrere Themes in dieser einen Datei (Vorbild: iOS Themes, ein Standard-Repo mit allen Varianten in einer Datei). Eigene Repos installiert man im Marketplace über „Add from link“; dafür muss das Repo öffentlich sein und eine `hacs.json` haben. Ob der Marketplace die Mehrfach-Themes in einer Datei genauso annimmt, zeigt erst der erste Installationstest.
- Die Theme-Datei wird aus `palettes.json` durch das Skript erzeugt.
- Versionen: HAUPT.NEBEN.KORREKTUR, Veröffentlichung als Git-Tag mit Release.
- Prüfen: YAML lesbar, Themes laden in Home Assistant (`frontend.reload_themes`), Screenshots eines Test-Dashboards.


## Arbeitsregeln (festgelegt vom Projektinhaber)
- Sehr kurz antworten: Ergebnis zuerst, Stichpunkte, etwa ein Viertel der früher üblichen Länge.
- Eine Frage ist kein Auftrag. Gebaut wird erst nach ausdrücklicher Freigabe. Größere Vorhaben in Pakete teilen und einzeln vorlegen, iterativ arbeiten.
- Etablierte Standardlösungen und vorhandene Systeme von Home Assistant nutzen, möglichst wenig selbst bauen, wartungsarm, keine Insellösungen. Selbst gestaltet werden nur feste Elemente.
- Nichts erfinden: an der Quelle prüfen, Ungeprüftes als ungeprüft kennzeichnen.
- Raster: Innenabstand P = 16 px (Kacheln unter 140 px: 12 px), Außenradius R = 24 px, Innenradius r = R − P. Inhalte ankern am Abstand P, Grafiken füllen die Fläche mittig. Randlos nur Fotos, geteilte Uhr, Laufband.
- Texte nie abschneiden: einpassen oder weich ausblenden, Platz für Unterlängen.

## Quellen würdigen
Jede genutzte Ressource (Vorbild, Dokumentation, Code, Schrift, Icon) wird vor der Veröffentlichung in CREDITS.md eingetragen: Urheber, Lizenz mit genauer Bezeichnung, wie sie genannt wird, Status (an der Quelle geprüft oder offen). Nichts als geprüft markieren, was nicht an der Quelle nachgelesen wurde.

## Öffentliche Dateien
Alles in diesem Repo ist öffentlich. Nicht hineinschreiben: Klarnamen, Wohnort, Arbeitgeber, Adressen, IPs, Gerätetypen, Netz- und Zugangsdetails, Token, Passwörter, Kontaktdaten, private Pläne, Screenshots mit Konten oder Gerätenamen. Als Autor steht nur der GitHub-Name `pettysmith`. Vor jedem Commit alle geänderten Dateien danach durchsuchen und das Ergebnis zeigen.
