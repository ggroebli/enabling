# Videos – DUB Academy

Sammelordner für alle KI-generierten Lehrvideos der Käufer-Akademie (und später Verkäufer-Akademie).
Skripte werden hier abgelegt, mit dem Tool-Workflow generiert und später in die jeweiligen `academy-modul-*.html` eingebettet.

## Workflow-Übersicht

Inspiriert von Nate Herks "Claude Code + HeyGen" Workflow (YouTube `EbJu9T30nfI`).
Drei Tools, orchestriert durch Claude Code:

| Schritt | Tool | Zweck | Status |
|---|---|---|---|
| 1. Skript schreiben | Claude Code | Voiceover-Text, Du-Form, ca. 6–7 Min pro Modul | manuell, fertig für Modul 1 |
| 2. Voice-Clone | ElevenLabs | Realistische deutsche Sprecher-Stimme aus Voice-Sample | offen |
| 3. Avatar-Video | HeyGen (Avatar 5) | Sprechender Avatar mit lippensynchroner Animation | offen |
| 4. Schnitt + Motion | Remotion | B-Roll, Bauchbinden, Übergänge, finales MP4 | offen |
| 5. Einbettung | HTML | Video-Tag im `academy-modul-*.html`, ersetzt Platzhalter | offen |

## Setup-Checkliste

### Accounts & Pricing (Stand 2026)

- [ ] **HeyGen** – `heygen.com`. Empfehlung: **Creator-Plan** (ca. 24 USD/Monat) oder Team-Plan, je nach Video-Volumen. Wichtig: Avatar 5 muss verfügbar sein (steckt im Creator+ und höher).
- [ ] **ElevenLabs** – `elevenlabs.io`. Für Voice-Cloning braucht es mindestens den **Starter-Plan** (ca. 5 USD/Monat) für Instant Voice Clone, besser **Creator-Plan** (ca. 22 USD/Monat) für Professional Voice Clone mit mehr Charakter.
- [ ] **Remotion** – `remotion.dev`. Open-Source, lokal. Optional **Remotion Pro** für Cloud-Rendering.

### Assets, die wir brauchen

#### Für den Avatar (HeyGen)
- [ ] **2–5 Min Video-Aufnahme** der Person, die als Avatar dienen soll – oder ein lizenzierter HeyGen-Stock-Avatar
  - Frontal, gutes Licht, ruhiger Hintergrund
  - Verschiedene Mimiken (lächeln, neutral, erklärend)
  - Während des Sprechens (Lippensynchronität wird daraus trainiert)
- [ ] **Consent-Formular** für HeyGen, falls echte Person als Avatar

#### Für die Stimme (ElevenLabs)
- [ ] **1–3 Min Audio-Sample**, deutsch, ruhige Umgebung
  - Lesetext: z.B. ein Abschnitt aus dem Suchstrategie-Skript
  - 44,1 kHz, keine Hintergrundgeräusche, kein Hall
- [ ] Sprecher:in festlegen (gleiche Person wie Avatar oder andere?)

#### Für die Motion Graphics (Remotion)
- [ ] DUB-Logo (SVG, weiß auf transparent)
- [ ] DUB-Farb-Codes (sind in `CLAUDE.md` dokumentiert)
- [ ] Schriftart Inter (Google Fonts, frei)
- [ ] Bauchbinden-Template-Skizze (z.B. unten links: Modul-Nummer + Titel)

### Offene Entscheidung: Avatar & Stimme

- **Avatar**: Eigene Aufnahme oder HeyGen-Stock-Avatar?
- **Stimme**: Eigene Stimme (via ElevenLabs Voice Clone) oder eine der ElevenLabs-Default-Stimmen?
- Wenn Avatar + Stimme dieselbe Person → höchste Authentizität, aber 2–5 Min sauberes Video + 1–3 Min sauberes Audio nötig.

### API-Keys (für die Claude-Code-Pipeline später)

- [ ] HeyGen API-Key (Dashboard → API → Generate Key)
- [ ] ElevenLabs API-Key (Profile → API Keys)
- [ ] Speichern in `.env` (nicht in Git committen, `.gitignore` prüfen)

## Skript-Konventionen

Damit alle Skripte konsistent klingen:

- **Du-Form**, lockerer DUB-Ton (siehe Modul 1 als Referenz)
- **Sprechdauer 6–7 Min** pro Modul (entspricht ca. 800–1.000 Wörtern)
- **Struktur**: Intro → 3 Abschnitte → Zusammenfassung
- **Keine Fake-Zahlen** (siehe Memory). Lieber "in der Regel rund 20%" statt "73% der Käufer..."
- **Berater-vs-Direktverkauf**: Wenn relevant, Unterscheidung explizit machen (Teaser/IM nur bei Berater-Prozessen)
- **Verlinkung zum Modul**: Hinweise auf interaktive Tools wie die Bierdeckelrechnung einbauen
- **Mathematische Sorgfalt**: Rechenbeispiele müssen konsistent sein (siehe letzten Commit `dfe6b8f`)

## Skript-Pipeline – nächste Module

In Reihenfolge der Akademie (Phase 1: Vorbereitung):

1. `video-skript-modul-01-suchstrategie.md` ✓ (fertig)
2. `video-skript-modul-02-dokumente.md`
3. `video-skript-modul-03-bewertung.md`
4. `video-skript-modul-04-finanzierung.md`
5. `video-skript-modul-05-transaktionsstrukturen.html` (entspricht academy-modul-transaktionsstrukturen.html)
6. `video-skript-modul-06-angebotsstrategie.md`
7. `video-skript-modul-07-due-diligence.md`
8. `video-skript-modul-08-kaufvertrag.md`
9. `video-skript-modul-09-100-tage-plan.md`

## Offene Entscheidungen

- Format-Verhältnis: 16:9 (Desktop-Embed in academy-modul-*.html) oder zusätzlich 9:16 für mögliche Social-Media-Schnipsel?
- Untertitel: Hardcoded ins Video oder als separate `.vtt`-Datei?
