# Käufer-Academy – Download-Dokumente: Produktionsplan

> Fortsetzung von `DUB-Rebrand-und-Downloads-Produktionsplan.md` §B.
> Die Verkäuferseite ist seit 14.09.2026 abgeschlossen (17 Dokumente).
> Dieses Dokument plant die **15 Käufer-Dokumente** über **9 Module** und **5 Phasen**.
> Stand: 14.09.2026

---

## 1. Ausgangslage

Das Download-Center auf `academy.html` listet bereits **15 Dokumente** mit Titel, Beschreibung und Dateityp. Die Modul-Sidebars verweisen ebenfalls darauf. Verlinkt ist noch nichts, es existiert keine einzige Datei.

**Ordner:** `Downloads/Kaeufer/` (neu anzulegen, analog zu `Downloads/Verkaeufer/`)

---

## 2. Inventar: 15 Dokumente nach Modul

| # | Dokument | Typ | Modul | Phase | Detail-Quelle |
|---|---|---|---|---|---|
| **Phase 1 – Vorbereitung** |||||
| 1 | Käuferprofil-Vorlage | PDF | suchstrategie | 1 | Modultext |
| 2 | Checkliste: Deine Unterlagen als Kaufinteressent | PDF | suchstrategie | 1 | Modultext |
| 3 | Share Deal vs. Asset Deal | PDF | transaktionsstrukturen | 1 | Modultext |
| 4 | Bewertungs-Template | **Excel** | bewertung | 1 | „Quick Guide LBO Model" |
| **Phase 2 – Suche & Analyse** |||||
| 5 | Checkliste: Teaser bewerten | PDF | dokumente | 2 | „How to create a teaser", SAMPLE Teaser |
| 6 | Checkliste: Vertraulichkeitsvereinbarung/NDA prüfen | PDF | dokumente | 2 | „Best practices – NDA" |
| 7 | Checkliste: Unternehmensunterlagen bewerten | PDF | dokumente | 2 | „How to create an IM", TEMPLATE IM |
| 8 | LOI-Mustervorlage | PDF | angebotsstrategie | 2 | „DealCircle LOI Best Practice Guide" |
| **Phase 3 – Prüfung & Finanzierung** |||||
| 9 | DD-Checkliste | **Excel** | due-diligence | 3 | DueDiligence-Checkliste.xlsx, Guide 6 |
| 10 | DD-Dokumentenanforderungsliste | PDF | due-diligence | 3 | DueDiligence-Checkliste.xlsx |
| 11 | Finanzierungsplan-Vorlage | **Excel** | finanzierung | 3 | Modultext |
| 12 | Checkliste Bankgespräch | PDF | finanzierung | 3 | Modultext |
| **Phase 4 – Abschluss** |||||
| 13 | Checkliste Vertragsklauseln | PDF | kaufvertrag | 4 | Modultext |
| 14 | Closing-Checkliste | PDF | kaufvertrag | 4 | Modultext |
| **Phase 5 – Nach dem Deal** |||||
| 15 | 100-Tage-Plan Template | PDF | 100-tage-plan | 5 | Modultext |

→ **12 PDF + 3 Excel**

**Verteilung je Modul:** dokumente 3 · suchstrategie 2 · due-diligence 2 · finanzierung 2 · kaufvertrag 2 · transaktionsstrukturen 1 · bewertung 1 · angebotsstrategie 1 · 100-tage-plan 1

---

## 3. Gegenstücke auf der Verkäuferseite

**8 der 15 Dokumente haben ein fertiges Pendant.** Das beschleunigt die Produktion und erzeugt zugleich eine Pflicht: Die beiden Seiten dürfen sich nicht widersprechen, weil Käufer und Verkäufer denselben Prozess aus zwei Richtungen beschrieben bekommen.

| Käufer-Dokument | Verkäufer-Pendant | Verhältnis |
|---|---|---|
| Checkliste: Vertraulichkeitsvereinbarung/NDA prüfen | Muster-Vertraulichkeitserklärung (kurz/ausführlich) | gleiche Quelle, andere Rolle: prüfen statt vorlegen |
| Checkliste: Teaser bewerten | Inserat-Vorlage | Verkäufer erstellt, Käufer bewertet |
| Checkliste: Unternehmensunterlagen bewerten | Unterlagen-Checkliste | Verkäufer stellt zusammen, Käufer prüft |
| LOI-Mustervorlage | LOI-Checkliste für Verkäufer | gleiche Quelle, Käufer formuliert, Verkäufer prüft |
| DD-Checkliste + DD-Doku-Anforderungsliste | Käuferprüfung-Schwerpunkte + Datenraum-Struktur-Vorlage | dieselbe Prüfung von beiden Seiten |
| Bewertungs-Template | Bewertungs-Template (Verkäufer) | dieselbe Methodik, Käufersicht auf den Preis |
| Closing-Checkliste | Checkliste: Vollzug des Verkaufs | derselbe Termin, andere Pflichten |
| 100-Tage-Plan Template | Wissenstransfer-Plan + Übergabe-Checkliste | Übergeber und Übernehmer |

**Konsequenz für den Review:** Jedes dieser acht Dokumente wird gegen sein Pendant gelesen, nicht nur gegen das eigene Modul.

---

## 4. Entschieden am 14.09.2026 – Welle 0 erledigt

| Punkt | Entscheidung | Umsetzung |
|---|---|---|
| 4.1 Downloads-Block im 100-Tage-Plan | hinzufügen | Der Block existierte, nutzte aber als einziges Modul ein abweichendes Alt-Markup (`download-title`/`download-desc` statt `download-item`). Auf das einheitliche Muster gebracht, fehlende CSS-Regel ergänzt. |
| 4.2 Doppelte Sidebar-Einträge | aufräumen | Finanzierung und Transaktionsstrukturen hatten den Downloads-Block **doppelt und innerhalb der `next-module-card`** – die Verschachtelung war kaputt. Block herausgelöst, Dublette entfernt. Kaufvertrag: doppelte Zeile entfernt. |
| 4.3 EBIT vs. EBITDA | EBITDA | Das Modul war bereits durchgängig EBITDA-basiert, nur die Center-Beschreibung sagte „EBIT-Multiples". Korrigiert. **Zusätzlich gefunden:** Die Preisbrücke rechnete mit „5× EBITDA: 800.000 €", während das Modulbeispiel 200.000 € × 4,0 verwendet. Auf 4× korrigiert. |
| 4.4 Teaser und IM bei kleinen Deals | flexibel je nach Projektgröße verfassen | **Gilt für die Dokumente 5, 6, 7.** Jede der drei Checklisten deckt beide Wege ab: den beratergestützten Ablauf (Teaser → NDA → IM) und den Direktverkauf (Inserat → NDA + persönliches Gespräch → Jahresabschlüsse/BWA). Der Käufer muss erkennen können, welcher Fall bei ihm vorliegt und was dann an die Stelle des fehlenden Dokuments tritt. |
| 4.5 „Dokumenten-Checkliste" zweideutig | akzeptiert | Umbenannt in **„Checkliste: Deine Unterlagen als Kaufinteressent"**, in Download-Center und Sidebar. |

---

## 5. Produktions-Pipelines

Beide sind auf der Verkäuferseite erprobt und werden unverändert übernommen.

**PDF:** HTML gegen `Downloads/Verkaeufer/_dub-doc.css` bauen (Navy-Kopf, Fußzeile mit info@dub.de und Compliance-Hinweis), dann
```
chrome --headless=new --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=15000 --run-all-compositor-stages-before-draw \
  --print-to-pdf="<ziel>.pdf" "file:///<pfad>.html"
```
Das Zeitbudget ist zwingend, sonst druckt Chrome vor dem Laden der Schriften.

**Excel:** Generator-Skript nach dem Muster von `_build-bewertungs-template.py`. Festgelegt: Calibri statt Inter, Beschriftungen mit führendem `=` brauchen `data_type = "s"`, berechnete Zellen bekommen ein Zahlenformat mit leerem Null-Abschnitt, Zeilen für Texteingaben brauchen eine Mindesthöhe von 30. Jede Datei bekommt ein zweites Blatt mit durchgerechnetem Beispiel.

---

## 6. Reihenfolge

| Welle | Inhalt | Warum zuerst |
|---|---|---|
| ~~**0**~~ | ~~Sidebar-Cleanup, Klärung 4.3–4.5~~ | **erledigt am 14.09.2026** (siehe Abschnitt 4) |
| **1** | Modul „Dokumente" komplett: Nr. 5, 6, 7 | Drei Dokumente in einem Modul, gemeinsame Quellen, klärt gleich die Frage aus 4.4 |
| **2** | Phase 1: Nr. 1, 2, 3 | Reine Modultext-Dokumente, schnell |
| **3** | Die drei Excel: Nr. 4, 9, 11 | Aufwändigste Einzelstücke, Pipeline ist erprobt |
| **4** | Phase 3 Rest: Nr. 10, 12 | |
| **5** | Phase 4 und 5: Nr. 13, 14, 15 | |
| **6** | Verdrahtung, Zähler, Konsistenz-Audit gegen die Verkäuferseite | |

---

## 7. Review-Ablauf je Dokument

Unverändert gegenüber der Verkäuferseite:

1. Dokument gegen das zugehörige Modul lesen, bei den acht Pendants zusätzlich gegen das Verkäufer-Dokument. Nur Widersprüche und Brauchbarkeit als Arbeitsmittel prüfen, es ist keine Modul-Zusammenfassung.
2. Graig entscheidet, was umgesetzt wird.
3. Umsetzen, Seitenumbrüche prüfen (kein Kapitel am Seitenfuß). **Kein Commit.**
4. Graig liest den neuen Stand und gibt frei.
5. Erst mit der Freigabe: committen, verdrahten, auf Ansage pushen.

**Keine erfundenen Zahlen.** Testwerte nie in die Auslieferungsdatei tippen, der OneDrive-AutoSave macht sie dauerhaft – auf einer Kopie im Temp-Ordner arbeiten.
