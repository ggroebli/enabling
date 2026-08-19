# DUB-Rebrand & Verkäufer-Downloads – Produktionsplan

> Blueprint für zwei zusammenhängende Arbeitspakete:
> **(A)** Umbenennung/Umfärbung AMBER → DUB über das gesamte Projekt und
> **(B)** Produktion der herunterladbaren Dokumente der Verkäufer-Academy.
> Stand: 19.08.2026

---

## 0. Fixierte Entscheidungen

| Thema | Entscheidung |
|---|---|
| Plattform | Academy erscheint auf **DUB (www.dub.de)**, nicht auf AMBER |
| Markenname | **AMBER → DUB** überall (Text, Logo, Domain) |
| Logo | Text `/AMBER` → **DUB-Navy-Badge** (weißes „DUB" auf Navy, abgerundet; CSS, kein Bild) |
| Support-Mail | `support@amber.deals` → **info@dub.de** |
| Farb-CI | **Volles Recolor** auf DUB-Navy/Blau (CTA-Grün + Academy-Lila werden ersetzt) |
| Ansprache | **„du" bleibt** (kein Rewrite auf „Sie", trotz dub.de-Konvention) |
| Download-Format | **Hybrid**: Checklisten/Leitfäden/Vorlagen = PDF (aus HTML), Rechner = echtes `.xlsx` |
| Inhaltstiefe | **Voll ausformuliert**, direkt nutzbar |
| Content-Regel | Inhalt **kongruent zu den Academy-Modultexten**, Details aus der **Wissensdatenbank** (Single Source of Truth) |
| Reihenfolge | **Verkäufer zuerst** (17 Dokumente), Käufer später (15) |

---

## A. DUB-Rebrand & Recolor

### A.1 Text-Rebrand (case-sensitive, damit Farbe „Amber" unangetastet bleibt)

- `AMBER` → `DUB` (trifft Logo `/AMBER`, `AMBER-Professional`, Fließtext „auf AMBER", „AMBER Directory", „AMBER-Plattform")
- `support@amber.deals` → `info@dub.de`
- **NICHT anfassen** (kein Marken-, sondern Farb-/Code-Bezug):
  `Amber` (Farbname `#F59E0B`), CSS-Variable `--amber`, Klassen `.badge-amber` / `.sk-hint-amber`, JS-Variable `amberTotal`

**Betroffen:** 39 HTML + 8 MD-Dateien (~307 Vorkommen HTML, ~28 MD).

### A.2 Logo-Badge (ersetzt Text-Logo)

```html
<a href="suche.html" class="nav-logo"><span class="dub-badge">DUB</span></a>
```
```css
.dub-badge {
  display:inline-flex; align-items:center; justify-content:center;
  background:#0F2744; color:#fff; font-weight:800; letter-spacing:.5px;
  padding:6px 12px; border-radius:8px; font-size:18px;
}
```
Footer-Logo analog (`.footer-logo` → Badge oder weißes „DUB" auf dunklem Footer).

### A.3 Farb-Mapping (DUB-CI)

| Rolle | Alt (AMBER) | Neu (DUB) |
|---|---|---|
| Marken-Navy (Logo, dunkle Flächen) | – | `#0F2744` |
| Primär-CTA / Akzent | Grün-Gradient `#9EFCEF→#CCFDBA` | DUB-Blau `#0066CC`, CTA-Text **weiß** |
| CTA-Gradient | `linear-gradient(85deg,#9EFCEF,#CCFDBA)` | `linear-gradient(120deg,#0066CC,#0F2744)` |
| Academy/KI-Akzent | Lila `#7C3AED` / `#EDE9FE` | DUB-Blau `#0066CC` / Hellblau `#E6F0FA` |
| Deal-Phase-Blau | `#2563EB` / `#DBEAFE` | vereinheitlichen auf DUB-Blau `#0066CC` / `#E6F0FA` |
| **Semantik – bleibt (trägt Bedeutung, keine Marke)** | | |
| Positiv/Erfolg | Grün `#10B981` | **unverändert** |
| Warnung | Amber `#F59E0B` / `#FEF3C7` | **unverändert** |
| Negativ/Risiko | Rot `#DC2626` / `#EF4444` | **unverändert** |

> ⚠️ **Wichtiger Prüfpunkt:** CTAs hatten dunklen Text auf hellem Grün. Auf Navy/Blau-CTA muss der Text **weiß** werden. Deshalb Recolor **erst als Prototyp auf einer Seite**, visuell prüfen, dann ausrollen.

### A.4 Vorgehen Recolor
1. DUB-Token-Block + Logo-Badge auf **verkaufer-academy.html** (Prototyp) → Freigabe.
2. Ausrollen auf alle übrigen 38 HTML (Tokens/Klassen zentral, Sonderfälle wie CTA-Textfarbe gezielt).
3. `.md`-Doku (CLAUDE.md, Planning Doc, Tech-Spec-Seiten, Video-Skripte) nachziehen.

---

## B. Verkäufer-Downloads – Produktion

### B.1 Inventar (17 Dokumente → Modul → KB-Quelle)

| # | Dokument | Typ | Modul-Sidebar | Detail-Quelle |
|---|---|---|---|---|
| **Phase 1 – Vorbereitung** ||||
| 1 | Exit-Readiness-Checkliste | PDF | exit-readiness | Modultext |
| 2 | Unterlagen-Checkliste | PDF | unterlagen | DD-Checkliste, IM-Guide |
| 3 | Inserat-Vorlage | PDF | unterlagen | „How to create a teaser" |
| 4 | Muster-Vertraulichkeitserklärung | PDF | unterlagen | „Best practices – NDA" |
| 5 | Bewertungs-Template | **Excel** | bewertung | „Quick Guide LBO Model" |
| 6 | Checkliste Beraterauswahl | PDF | verkaufsberater | Modultext |
| 7 | Vorlage Beratermandat | PDF | verkaufsberater | Modultext |
| 8 | Verkaufsprozess-Übersicht | PDF (1-Seiter) | verkaufsprozess | Modultext |
| **Phase 2 & 3 – Im Verkaufsprozess** ||||
| 9 | Gesprächsleitfaden Erstgespräch | PDF | kennenlernen | Modultext |
| 10 | Käufer-Screening-Checkliste | PDF | kaeufer-screening | Modultext |
| 11 | Käufer-Bewertungsmatrix | **Excel** | kaeufer-screening | Modultext |
| 12 | LOI-Checkliste für Verkäufer | PDF | loi | „DealCircle LOI Best Practice Guide" |
| 13 | DD-Vorbereitungs-Checkliste | PDF | dd-closing | „Due Diligence Checklist" |
| 14 | Datenraum-Struktur-Vorlage | PDF | dd-closing | DD-Checkliste |
| **Phase 4 – Abschluss & Übergabe** ||||
| 15 | Closing-Day-Checkliste | PDF | dd-closing | Modultext |
| 16 | Übergabe-Checkliste | PDF | uebergabe | Modultext |
| 17 | Wissenstransfer-Plan | PDF | uebergabe | Modultext |

→ **15 PDF + 2 Excel** über **10 Module**.

### B.2 Produktions-Pipelines
- **PDF:** gemeinsames `_template.html` (DUB-CI: Navy-Kopf mit DUB-Badge, Fußzeile mit info@dub.de + Compliance-Hinweis „Keine Rechts-/Steuerberatung") → Inhalt einsetzen → Browser „Als PDF speichern".
- **Excel:** echte `.xlsx` mit Formeln (Bewertungs-Template: EBIT-Multiple + Szenarien; Käufer-Bewertungsmatrix: gewichtetes Scoring), per Skript erzeugt.

### B.3 Ordnerstruktur
```
Downloads/
  Verkaeufer/
    _template.html
    exit-readiness-checkliste.html (+ .pdf)
    muster-vertraulichkeitserklaerung.html (+ .pdf)
    ...
    bewertungs-template.xlsx
    kaeufer-bewertungsmatrix.xlsx
  Kaeufer/   (später)
```

### B.4 Verdrahtung
- `href="#"` in **verkaufer-academy.html** (Download-Center) + in den **10 Modul-Sidebars** auf echte Dateien setzen.
- **Cleanup:** doppelte Sidebar-Einträge korrigieren in
  `dd-closing` (Datenraum-Struktur-Vorlage 2×), `kaeufer-screening` (Käufer-Bewertungsmatrix 2×),
  `uebergabe` (Wissenstransfer-Plan 2×), `verkaufsberater` (Vorlage Beratermandat 2×).

### B.5 Wellen
1. **Prototyp (3):** Exit-Readiness-Checkliste (PDF) · Muster-NDA (KB-basiert) · Bewertungs-Template (Excel) → Freigabe Design + Inhaltstiefe.
2. **Rest PDFs (12)** modulweise, Academy-Text-Abgleich.
3. **Excel #2** (Käufer-Bewertungsmatrix) + Verdrahtung + Sidebar-Cleanup.

---

## C. Reihenfolge der Umsetzung
1. ✅ Plan-Doku (dieses Dokument)
2. Recolor-Prototyp (verkaufer-academy.html) → **Freigabe**
3. Rebrand + Recolor Rollout (alle Seiten + Doku)
4. Download-Template + Prototyp-Dokumente (3) → **Freigabe**
5. Restliche Verkäufer-Downloads
6. Verdrahtung + Cleanup
7. (später) Käufer-Downloads analog
