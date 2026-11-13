# Arbeitsanweisung für Claude Code

Projekt: Begleit-Themes für die Karten des Repos Viewsta. Öffentliches Theme-Repository für den Marketplace von Home Assistant. Jedes Theme setzt nur die Variable `viewsta-palette` und verändert sonst nichts an Home Assistant.

Persönliche Arbeitsregeln des Projektinhabers und alle privaten Angaben stehen in einer Ergänzung, die nicht im Repo liegt:
@~/.claude/standby-privat.md
Fehlt die Datei, arbeite mit den Regeln unten weiter und frage nach, statt zu raten.

## Stand
Vorbereitet: `palettes.json`, `scripts/build_themes.py`, `themes/themebook.yaml` (13 Themes), `hacs.json`, `README.md`, `LICENSE`, `CREDITS.md`. Die frühere Fassung mit globalen Variablen (Hintergrund, Karten, Seitenleiste) wurde verworfen, weil sie andere Themes wie Frosted Glass überschrieb.

## Erst lesen
ROADMAP.md, CREDITS.md, palettes.json, README.md

## Regeln
- Kurz antworten. Erst die gestellte Frage beantworten.
- Änderungen nur nach ausdrücklichem Auftrag. Vorher zeigen, welche Dateien sich ändern und mit welchem Inhalt, und die Freigabe abwarten. Commit und Push nur nach ausdrücklicher Freigabe, denn das Repo ist öffentlich.
- Nichts erfinden. Annahmen als offene Frage kennzeichnen.
- Keine globalen Home-Assistant-Variablen setzen. Nur Variablen mit dem Präfix `viewsta-`.

## Technik
- HACS-Theme-Repository: `themes/<name>.yaml`, `hacs.json`, `README.md`, `LICENSE`, `CREDITS.md`. Pro Repository wird eine Theme-Datei verwaltet; die Paletten liegen als mehrere Themes in dieser einen Datei (Vorbild: iOS Themes, ein Standard-Repo mit allen Varianten in einer Datei). Eigene Repos installiert man im Marketplace über „Add from link“; dafür muss das Repo öffentlich sein und eine `hacs.json` haben. Ob der Marketplace die Mehrfach-Themes in einer Datei genauso annimmt, zeigt erst der erste Installationstest.
- Die Theme-Datei wird aus `palettes.json` durch das Skript erzeugt.
- Versionen: HAUPT.NEBEN.KORREKTUR, Veröffentlichung als Git-Tag mit Release.
- Prüfen: YAML lesbar, Themes laden in Home Assistant (`frontend.reload_themes`), Screenshots eines Test-Dashboards.

## Quellen würdigen
Jede genutzte Ressource (Vorbild, Dokumentation, Code, Schrift, Icon) wird vor der Veröffentlichung in CREDITS.md eingetragen: Urheber, Lizenz mit genauer Bezeichnung, wie sie genannt wird, Status (an der Quelle geprüft oder offen). Nichts als geprüft markieren, was nicht an der Quelle nachgelesen wurde.

## Öffentliche Dateien
Alles in diesem Repo ist öffentlich. Nicht hineinschreiben: Klarnamen, Wohnort, Arbeitgeber, Adressen, IPs, Gerätetypen, Netz- und Zugangsdetails, Token, Passwörter, Kontaktdaten, private Pläne, Screenshots mit Konten oder Gerätenamen. Als Autor steht nur der GitHub-Name `pettysmith`. Vor jedem Commit alle geänderten Dateien danach durchsuchen und das Ergebnis zeigen.
