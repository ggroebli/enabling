# AMBER Enablement – Projekt-Kontext für Claude Code

## Quick Start (für neue Teammitglieder)

1. **Mockups anschauen:** Einfach die `.html`-Dateien im Browser öffnen (Doppelklick). Starte mit `academy.html` und `listing.html` – dort sind die meisten Enablement-Features sichtbar.
2. **Konzept lesen:** `Enablement Planning Document.md` enthält die vollständige Produktvision, Priorisierung und offene Fragen.
3. **Weiterarbeiten mit Claude Code:** Dieses Projekt ist darauf ausgelegt, mit Claude Code weiterentwickelt zu werden. Claude kennt durch diese Datei den vollen Kontext. Einfach sagen, was als nächstes gemockupt werden soll (z.B. "Lass uns den KI-Assistenten als Chat-Widget designen" oder "Bau die Verkäuferseite").
4. **Offene Aufgaben:** Siehe Abschnitt "Was noch offen ist" weiter unten – dort steht, was als nächstes dran ist.

## Was ist das hier?

Statische HTML-Mockups für das **Enablement-Produkt** der AMBER M&A-Plattform (Käuferseite). AMBER ist ein Marktplatz für Unternehmenskäufe/-verkäufe im deutschen Mittelstand (SME M&A). Das Enablement-Produkt soll unerfahrene Käufer und Verkäufer durch den gesamten M&A-Prozess begleiten.

Die Mockups dienen als **Konzeptgrundlage für das Team** (nicht als Production Code). Sie werden in Bubble.io umgesetzt.

## Team & Rollen

| Person | Rolle |
|---|---|
| **Florian (Fynn)** | Product / Mockups – erstellt die Mockups mit Claude Code |
| **Graig** | Strategy / Content – inhaltliche Konzeption |
| **Kai** | Strategy / Content – Academy-Module, Content |
| **Anja** | Content – KI-generierte Videos und Texte |

## Konzept-Dokument

Die vollständige Produktvision steht in **`Enablement Planning Document.md`**. Dort sind die drei Ebenen des Enablement-Produkts beschrieben, die Priorisierung, offene Fragen und der Session-Plan.

## Dateien im Projekt

### HTML-Mockups (Käuferseite)
| Datei | Seite | Enablement-Features |
|---|---|---|
| `suche.html` | Suchseite mit Listing-Karten | Gating: Listings mit niedrigem Readiness Score sind geblurrt/gesperrt mit Overlay |
| `listing.html` | Listing-Detailseite | KI-Analyse (Match-Score, Chancen/Risiken), Interest-Modal mit Verkäufer-Fragen |
| `suchauftraege.html` | Suchaufträge (Alerts) | Per-Alert Competition-Daten, Ergebnis/Gesperrt-Badges mit Tooltips, Locked-Summary CTA, Academy-Tip |
| `transaktionen.html` | Meine Transaktionen (3 Tabs) | Kontextuelle Academy-Cards pro Tab (Merkliste, Interessensbekundungen, Matches) |
| `kauferprofil.html` | Käuferprofil | Readiness Score Banner (45%, SVG Ring), Missing-Field Hints mit Academy-Links |
| `academy.html` | Academy Startseite | Hero mit Score-Ring, 3 Phasen (Vorbereitung/Im Deal/Nach dem Deal), 12 Module, Berater-CTA |
| `mitteilungen.html` | Mitteilungen/Notifications | Keine Enablement-Features (noch) |
| `postfach.html` | Postfach/Chat | Keine Enablement-Features (noch) |

### Referenz-Dateien
| Datei | Beschreibung |
|---|---|
| `Enablement Planning Document.md` | Vollständige Produktvision, 3 Ebenen, Priorisierung, offene Fragen |
| `Meetings/` | Meeting-Transkript und Summary vom Brainstorming (04. Feb 2026) |
| `*.png` | Screenshots der Original-Plattform (vor Enablement) als Referenz |
| `*.txt` | HTML-Quellcode der Original-Plattform (exportiert, als Vorlage benutzt) |

## Design-System

### Grundregeln
- **Layout:** 1440px fixed width, kein Responsive
- **Font:** Inter (Google Fonts CDN), Weights: 300, 400, 500, 600, 700, 800
- **Icons:** Font Awesome 6 Free (CDN)
- **Styling:** Inline `<style>` Blöcke pro Seite (kein externes CSS)
- **Nav:** Fixed top, 72px Höhe, mit Focus-Group-Dropdown (Avatar-Klick)
- **Alle Seiten** haben identische Nav-Struktur mit Links: Suche, Suchaufträge, Mitteilungen, Postfach, Meine Transaktionen, Academy

### CSS-Variablen
```css
--font-main: 'Inter', 'Helvetica Neue', Arial, sans-serif;
--black: #1A1A1A;
--grey-dark: #666666;
--grey-light: #CCCCCC;
--white: #FFFFFF;
--gradient-cta: linear-gradient(85.13deg, #9EFCEF 0%, #CCFDBA 96.11%);
```

### Enablement-Farbsystem
| Farbe | Verwendung |
|---|---|
| Grün `#10B981` | Positiv: erledigt, Ergebnisse, Chancen, Score-Ring |
| Amber `#F59E0B` / `#FEF3C7` | Warnung: fehlende Felder, gesperrte Inhalte |
| Rot `#DC2626` / `#EF4444` | Negativ: Wettbewerb-Highlights, Risiken |
| Lila `#7C3AED` / `#EDE9FE` | Academy/KI: Module, Tipps, AI-Badge |
| Blau `#2563EB` / `#DBEAFE` | Deal-Phase: Module im Deal |

### Enablement-Hintergrund (Academy-Gradient)
```css
background: linear-gradient(135deg, #F0FDF4 0%, #F0FDFA 50%, #F5F3FF 100%);
border: 1px solid #E0E7FF;
border-radius: 8px;
```

### Karten-Patterns
- **Shadow Cards:** `box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.15); border-radius: 8px;`
- **Module Cards (Academy):** `box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.08); border: 1px solid #F0F0F0; border-radius: 8px;`
- **Mini Cards (kontextuell):** `border: 1px solid #E5E7EB; border-radius: 8px;` mit Hover-Effekt

### Modul-Typ Badges
| Typ | Badge-Farben |
|---|---|
| Video | `#EDE9FE` bg / `#7C3AED` text |
| Guide | `#DBEAFE` bg / `#2563EB` text |
| Test | `#FEF3C7` bg / `#D97706` text |
| Template | `#D1FAE5` bg / `#059669` text |
| Checkliste | `#FEE2E2` bg / `#DC2626` text |

### SVG Readiness Ring
```css
/* Kreis-Fortschritt via stroke-dasharray/dashoffset */
stroke-dasharray: 314; /* Umfang bei r=50 */
stroke-dashoffset: 172; /* 314 - (314 * 0.45) = 172.7 → 45% */
```

## Git Save Point

Es gibt einen Git-Tag `pre-enablement` = Stand aller Seiten **BEVOR** Enablement-Features eingebaut wurden.

**Zurücksetzen auf Original:**
```bash
git checkout .
git clean -fd
git reset --hard pre-enablement
```

## Was wurde bereits umgesetzt (Käuferseite)

### Ebene 1: Readiness Academy
- [x] Käufer-Readiness-Score auf Käuferprofil (SVG Ring, 45%, fehlende Items)
- [x] Academy Startseite mit 3 Phasen und 12 Modulen
- [x] Academy-Link in Navigation aller Seiten
- [x] Missing-Field Hints im Käuferprofil (mit Academy-Links)

### Ebene 2: In-Flow Guidance
- [x] Gating auf Suchseite (Listings geblurrt bei niedrigem Score)
- [x] Suchaufträge: Competition-Daten, Gesperrt-Badges, Tooltips, CTA
- [x] Transaktionen: Kontextuelle Academy-Cards pro Tab
- [x] Listing: KI-Analyse (Match 82%, Chancen, Risiken)
- [x] Listing: Interest-Modal mit Verkäufer-/Berater-Fragen

### Ebene 3: KI-Assistent
- [ ] Chat-UI (noch nicht gemockupt)
- [ ] Einbettung in Seiten (noch nicht gemockupt)

## Was noch offen ist / Nächste Schritte

### Mockups Käuferseite (noch nicht gemacht)
- KI-Assistent (Chat-Widget, Floating Button, Beispieldialoge)
- Mitteilungen mit Enablement-Trigger-Notifications
- Academy Modul-Detailseite (einzelnes Modul geöffnet)
- Postfach: Kontextuelle Hilfe bei Erstgesprächen

### Mockups Verkäuferseite (komplett offen)
- Verkäufer-Readiness-Score + Selbsttest
- Verkäufer-Inserat erstellen (mit Enablement-Guidance)
- Verkäufer-Dashboard mit Interessenten-Übersicht
- Berater-Fragen konfigurieren (für Interest-Modal)

### Konzept-Fragen (siehe Planning Document §6)
- Zwang vs. Freiwilligkeit beim Readiness-Check
- Gamification-Elemente
- Granularität der Prozesskette
- Bubble-Machbarkeit bis Juli

## Arbeitsweise

- Mockups werden iterativ in Claude Code Sessions gebaut
- Florian gibt Feedback, Claude passt an
- Jede Seite ist eigenständig (kein Build-Prozess, einfach HTML öffnen)
- Neue Features werden als CSS+HTML direkt in die bestehenden Seiten eingefügt
- Kommentare im Code markieren Enablement-Sections: `<!-- ENABLEMENT: ... -->`
- CSS-Sections sind mit Kommentaren markiert: `/* ===== ENABLEMENT: ... ===== */`
