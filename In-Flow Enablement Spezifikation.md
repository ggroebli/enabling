# In-Flow Enablement – Technische Spezifikation

**Erstellt:** 24. März 2026
**Zweck:** Deterministische Referenz für das Tech-Team. Beschreibt exakt, welche Inhalte je nach Perspektive (Käufer/Verkäufer) und Deal-Phase angezeigt werden müssen.
**Basierend auf:** Mockups im Projektordner, Enablement Planning Document, Academy-Module

---

## Inhaltsverzeichnis

1. [Prozesskette (DUB-Phasen)](#1-prozesskette)
2. [Käufer: Empfohlene Schritte pro Phase](#2-käufer-empfohlene-schritte)
3. [Käufer: Sidebar-Content pro Phase](#3-käufer-sidebar-content)
4. [Käufer: Chat-Widget Quick Actions pro Phase](#4-käufer-chat-widget)
5. [Käufer: Mitteilungen pro Phasenwechsel](#5-käufer-mitteilungen)
6. [Käufer: Transaktionsübersicht (Enablement-Bar)](#6-käufer-transaktionsübersicht)
7. [Verkäufer: Empfohlene Schritte pro Phase](#7-verkäufer-empfohlene-schritte)
8. [Verkäufer: Sidebar-Content pro Phase](#8-verkäufer-sidebar-content)
9. [Verkäufer: Chat-Widget Quick Actions pro Phase](#9-verkäufer-chat-widget)
10. [Academy-Modul-Zuordnung](#10-academy-modul-zuordnung)
11. [Downloads/Dokumente pro Phase](#11-downloads-pro-phase)
12. [Phasenwechsel-Trigger & Berechtigungen](#12-phasenwechsel-trigger)
13. [Checklisten: Persistenz & Lifecycle](#13-checklisten-persistenz)
14. [Toast-Banner: Auslöser & Verhalten](#14-toast-banner)
15. [Mitteilungen: Lifecycle & Gelesen-Status](#15-mitteilungen-lifecycle)
16. [Verkäufer: Multi-Käufer-Logik](#16-multi-käufer-logik)
17. [Download-Bibliothek & Dateiverwaltung](#17-download-bibliothek)
18. [KI-Assistent: Architektur & Antwortlogik](#18-ki-assistent-architektur)
19. [Berater-Box: Darstellungsvarianten](#19-berater-box)
20. [Navigation: Perspektivwechsel Käufer/Verkäufer](#20-navigation-perspektivwechsel)
21. [Deal-Attraktivität: Käufer-Bewertungsfeld](#21-deal-attraktivität)
22. [Edge Cases & Sonderfälle](#22-edge-cases)

---

## 1. Prozesskette

Die DUB-Prozesskette hat **9 Phasen**, die für Käufer und Verkäufer identisch sind (aber aus unterschiedlichen Perspektiven erlebt werden):

| # | Phase | Beschreibung |
|---|-------|-------------|
| 1 | **Interessensbekundung** | Käufer bekundet Interesse an einem Inserat |
| 2 | **Match** | Beide Seiten haben Interesse bestätigt |
| 3 | **NDA unterzeichnet** | Vertraulichkeitserklärung liegt vor |
| 4 | **Persönliches Treffen** | Erstes persönliches Kennenlernen |
| 5 | **LOI vorgelegt** | Letter of Intent wurde eingereicht |
| 6 | **LOI unterzeichnet** | LOI wurde von beiden Seiten unterschrieben |
| 7 | **Notartermin** | Notartermin ist vereinbart |
| 8 | **Signing** | Kaufvertrag ist unterschrieben |
| 9 | **Closing** | Transaktion ist vollständig abgeschlossen |

**Timeline-Darstellung:** Horizontaler Stepper mit Dots und Verbindungslinien.
- Abgeschlossene Phasen: Grüner Dot mit Häkchen (`#10B981`)
- Aktuelle Phase: Blauer Dot mit Puls-Animation (`#2563EB`)
- Zukünftige Phasen: Grauer Dot (`#E5E7EB`)

---

## 2. Käufer: Empfohlene Schritte pro Phase

> **Darstellung:** Interaktive Checkliste auf der Deal-Detailseite (Hauptbereich). Items sind abhakbar. Der erste Schritt ist bei Phaseneintritt bereits als "erledigt" markiert (= der Trigger-Event der Phase selbst).

### Phase 1: Interessensbekundung

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | Interessensbekundung abgesendet | ✅ Erledigt |
| 2 | Inserat-Details sorgfältig prüfen (Branche, Größe, Standort) | ☐ Offen |
| 3 | Eigene Finanzierungsmöglichkeiten grob einschätzen | ☐ Offen |
| 4 | Käuferprofil vervollständigen (erhöht Match-Chancen) | ☐ Offen |
| 5 | Auf Antwort des Verkäufers warten | ☐ Offen |

**Phasenbeschreibung (Fließtext):**
"Deine Interessensbekundung wurde an den Verkäufer übermittelt. Wenn beide Seiten Interesse haben, wird ein Match erzeugt und du erhältst eine NDA zur Unterzeichnung. Nutze die Wartezeit, um dein Käuferprofil zu vervollständigen – das erhöht deine Chancen."

---

### Phase 2: Match

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | Match bestätigt | ✅ Erledigt |
| 2 | NDA sorgfältig lesen (Checkliste nutzen) | ☐ Offen |
| 3 | NDA unterzeichnen und zurücksenden | ☐ Offen |
| 4 | Fragenkatalog für das Erstgespräch vorbereiten | ☐ Offen |
| 5 | Frühzeitig Finanzierung klären (KfW-Förderprogramme prüfen) | ☐ Offen |

**Phasenbeschreibung:**
"Beide Seiten haben Interesse bekundet – ihr seid jetzt ein Match! Als Nächstes wird die NDA unterzeichnet. Bereite dich parallel schon auf das Kennenlerngespräch vor und kläre frühzeitig deine Finanzierung."

---

### Phase 3: NDA unterzeichnet

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | NDA sorgfältig lesen und unterschreiben | ✅ Erledigt |
| 2 | Jahresabschlüsse und BWA vom Verkäufer anfordern | ☐ Offen |
| 3 | Unterlagen mit der Checkliste "IM bewerten" systematisch prüfen | ☐ Offen |
| 4 | Erste Bewertung durchrechnen (Bewertungs-Template nutzen) | ☐ Offen |
| 5 | Fragenkatalog für das persönliche Treffen vorbereiten | ☐ Offen |

**Phasenbeschreibung:**
"Die Vertraulichkeitserklärung (NDA) ist unterzeichnet. Damit können jetzt vertrauliche Unternehmensinformationen ausgetauscht werden. Bei einem Direktverkauf erhältst du in der Regel die Jahresabschlüsse und eine BWA – nutze die Checkliste, um die Unterlagen systematisch auszuwerten. Der nächste Meilenstein ist das persönliche Kennenlernen mit dem Verkäufer."

**Hinweis Direktverkauf vs. Berater:**
- Bei beratergestützten Prozessen: Käufer erhält ein Informationsmemorandum (IM)
- Bei Direktverkäufen (<2M EUR): Käufer erhält Jahresabschlüsse, BWA, ggf. Kundenliste

---

### Phase 4: Persönliches Treffen

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | Notizen vom Treffen auswerten und offene Fragen notieren | ✅ Erledigt |
| 2 | Unternehmensbewertung durchrechnen (Bewertungs-Template nutzen) | ☐ Offen |
| 3 | Deal-Struktur festlegen: Share Deal oder Asset Deal? | ☐ Offen |
| 4 | LOI-Entwurf vorbereiten (LOI-Mustervorlage anpassen) | ☐ Offen |
| 5 | Finanzierung klären: Eigenkapital, Bankgespräch, Fördermittel | ☐ Offen |

**Phasenbeschreibung:**
"Das persönliche Treffen mit dem Verkaufsberater hat stattgefunden. Jetzt geht es darum, deine Eindrücke auszuwerten und zu entscheiden, ob du ein verbindliches Angebot in Form eines Letter of Intent (LOI) formulieren möchtest. Nutze die Zeit, um offene Fragen zu klären und deine Bewertung zu schärfen."

---

### Phase 5: LOI vorgelegt

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | LOI-Entwurf beim Verkäufer eingereicht | ✅ Erledigt |
| 2 | Auf Rückmeldung des Verkäufers warten | ☐ Offen |
| 3 | Eventuelle Nachverhandlungen führen (Kaufpreis, Exklusivität, Bedingungen) | ☐ Offen |
| 4 | Finanzierungszusage einholen (falls noch nicht geschehen) | ☐ Offen |
| 5 | Due-Diligence-Team zusammenstellen (Steuerberater, Anwalt) | ☐ Offen |

**Phasenbeschreibung:**
"Dein LOI ist beim Verkäufer eingegangen. Jetzt beginnt die Verhandlungsphase – der Verkäufer wird dein Angebot prüfen und möglicherweise Anpassungen vorschlagen. Nutze die Zeit, um deine Finanzierung abzusichern und dein DD-Team vorzubereiten."

---

### Phase 6: LOI unterzeichnet

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | LOI von beiden Seiten unterschrieben | ✅ Erledigt |
| 2 | Due-Diligence-Checkliste vorbereiten | ☐ Offen |
| 3 | Datenraum-Zugang beantragen und Dokumente systematisch prüfen | ☐ Offen |
| 4 | Finanzierung finalisieren (Bankgespräch, Kreditvertrag) | ☐ Offen |
| 5 | Kaufvertragsentwurf mit Anwalt vorbereiten | ☐ Offen |

**Phasenbeschreibung:**
"Der LOI ist von beiden Seiten unterschrieben – jetzt starten Due Diligence und Finanzierung parallel. Du hast in der Regel eine Exklusivitätsphase (typisch 3–4 Monate), in der du das Unternehmen detailliert prüfen kannst. Nutze die DD-Checkliste, um nichts zu übersehen."

---

### Phase 7: Notartermin

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | Notartermin vereinbart | ✅ Erledigt |
| 2 | Kaufvertragsentwurf final prüfen (mit Anwalt) | ☐ Offen |
| 3 | Checkliste Vertragsklauseln durchgehen | ☐ Offen |
| 4 | Finanzierung final bestätigen lassen | ☐ Offen |
| 5 | Closing-Checkliste vorbereiten | ☐ Offen |

**Phasenbeschreibung:**
"Der Notartermin steht – du bist fast am Ziel. Prüfe den Kaufvertragsentwurf sorgfältig mit deinem Anwalt und stelle sicher, dass alle Bedingungen aus dem LOI umgesetzt wurden. Bereite die Closing-Unterlagen vor."

---

### Phase 8: Signing

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | Kaufvertrag beim Notar unterschrieben | ✅ Erledigt |
| 2 | Closing-Bedingungen prüfen und erfüllen | ☐ Offen |
| 3 | Kaufpreiszahlung vorbereiten / auslösen | ☐ Offen |
| 4 | Übernahmeplanung starten (100-Tage-Plan) | ☐ Offen |
| 5 | Kommunikationsplan für Mitarbeiter und Kunden vorbereiten | ☐ Offen |

**Phasenbeschreibung:**
"Der Kaufvertrag ist unterschrieben – Glückwunsch! Zwischen Signing und Closing müssen noch die vereinbarten Closing-Bedingungen erfüllt werden (z.B. Kaufpreiszahlung, behördliche Genehmigungen). Nutze die Zeit, um deinen 100-Tage-Plan vorzubereiten."

---

### Phase 9: Closing

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | Transaktion vollständig abgeschlossen | ✅ Erledigt |
| 2 | 100-Tage-Plan starten | ☐ Offen |
| 3 | Übergabegespräche mit dem Verkäufer führen | ☐ Offen |
| 4 | Mitarbeiter und Kunden informieren | ☐ Offen |
| 5 | Erste Quick Wins identifizieren und umsetzen | ☐ Offen |

**Phasenbeschreibung:**
"Herzlichen Glückwunsch – du bist jetzt Unternehmer! Die Übergabe beginnt. Starte strukturiert mit deinem 100-Tage-Plan: Erst zuhören und verstehen, dann optimieren. Die ersten 100 Tage entscheiden über den langfristigen Erfolg."

---

## 3. Käufer: Sidebar-Content pro Phase

> **Darstellung:** Rechte Sidebar (320px, sticky) auf der Deal-Detailseite. Enthält 4 Blöcke: "Dein nächster Schritt", "Passende Downloads", "Berater empfohlen", "M&A-Assistent".

### Block A: "Dein nächster Schritt"

| Phase | Tipp-Text | Academy-Modul (CTA) |
|-------|-----------|---------------------|
| 1 – Interessensbekundung | "Während du auf die Antwort wartest: Vervollständige dein Käuferprofil – das zeigt dem Verkäufer, dass du ein ernsthafter Kandidat bist." | Suchstrategie & Käuferprofil |
| 2 – Match | "Ihr seid ein Match! Lies die NDA sorgfältig und bereite dich auf das Erstgespräch vor. Unser Modul zeigt dir, worauf du achten musst." | Dokumente im M&A-Prozess |
| 3 – NDA unterzeichnet | "Die NDA ist unterschrieben – jetzt bekommst du Zugang zu den Unternehmensunterlagen. Unser Modul zeigt dir, worauf du bei den Dokumenten achten musst und wie du die Zahlen richtig einordnest." | Dokumente im M&A-Prozess |
| 4 – Pers. Treffen | "Das Treffen war positiv? Dann ist jetzt der richtige Zeitpunkt, dein Angebot zu formulieren. Unser LOI-Modul zeigt dir Schritt für Schritt, wie du einen überzeugenden Letter of Intent erstellst." | Angebotsstrategie & LOI |
| 5 – LOI vorgelegt | "Dein LOI ist raus – jetzt heißt es warten und parallel die DD vorbereiten. Unser Modul erklärt dir, wie du die Due Diligence strukturiert angehst." | Due Diligence meistern |
| 6 – LOI unterzeichnet | "LOI steht – jetzt Due Diligence und Finanzierung parallel starten. Unser Modul hilft dir, den Datenraum systematisch zu prüfen und nichts zu übersehen." | Due Diligence meistern |
| 7 – Notartermin | "Notartermin steht – prüfe den Kaufvertrag sorgfältig mit deinem Anwalt. Unser Modul zeigt dir die wichtigsten Vertragsklauseln." | Kaufvertrag & Closing |
| 8 – Signing | "Vertrag unterschrieben – bereite jetzt die Übernahme vor. Der 100-Tage-Plan hilft dir, strukturiert zu starten." | 100-Tage-Plan |
| 9 – Closing | "Herzlichen Glückwunsch! Du bist jetzt Unternehmer. Starte mit dem 100-Tage-Plan – die ersten Wochen entscheiden über den langfristigen Erfolg." | 100-Tage-Plan |

### Block B: "Passende Downloads"

→ Siehe [Abschnitt 11: Downloads pro Phase](#11-downloads-pro-phase)

### Block C: "Berater empfohlen"

| Phase | Anzeigen? | Text |
|-------|-----------|------|
| 1–3 | Ja (dezent) | "Viele Käufer ziehen spätestens ab der Due-Diligence-Phase einen Berater hinzu. Noch ist es früh – aber wenn du die Unterlagen ausgewertet hast und weitergehen willst, kann ein erfahrener Steuerberater oder M&A-Berater helfen." |
| 4–5 | Ja (prominent) | "Die meisten Käufer holen sich in dieser Phase professionelle Unterstützung. Ein M&A-Berater hilft dir bei der Bewertung, LOI-Verhandlung und Due Diligence – besonders wertvoll ab der Angebotsphase." |
| 6–8 | Ja (prominent) | "Für die Due Diligence und Vertragsverhandlung sind Steuerberater und Anwalt fast immer sinnvoll. Bei kleinen Deals (<2M EUR) reicht oft ein erfahrener Steuerberater + Anwalt statt eines spezialisierten M&A-Beraters." |
| 9 | Nein | — |

### Block D: "M&A-Assistent"

Auf jeder Phase identisch:
- Text: "Fragen zu diesem Deal oder zum nächsten Schritt? Dein KI-Assistent kennt alle Academy-Inhalte und hilft dir weiter."
- CTA: "Chat starten" → öffnet Chat-Widget

---

## 4. Käufer: Chat-Widget Quick Actions pro Phase

> **Darstellung:** Floating Button (unten rechts, lila `#7C3AED`). Klick öffnet 400px breites Chat-Panel. 3 Quick-Action-Chips passen sich der aktuellen Phase an.

| Phase | Quick Action 1 | Quick Action 2 | Quick Action 3 |
|-------|---------------|---------------|---------------|
| 1 – Interessensbekundung | "Was passiert nach meiner Interessensbekundung?" | "Wie verbessere ich mein Käuferprofil?" | "Was ist ein Teaser?" |
| 2 – Match | "Was ist eine NDA?" | "Wie bereite ich mich auf das Erstgespräch vor?" | "Brauche ich einen Berater?" |
| 3 – NDA unterzeichnet | "Was steht in einem IM?" | "Worauf bei der BWA achten?" | "Wie berechne ich den Unternehmenswert?" |
| 4 – Pers. Treffen | "Was bedeutet ein Earn-Out?" | "LOI: Worauf achten?" | "Brauche ich einen Berater?" |
| 5 – LOI vorgelegt | "Wie lange dauert die LOI-Verhandlung?" | "Was ist eine faire Exklusivität?" | "Was passiert nach dem LOI?" |
| 6 – LOI unterzeichnet | "Wie läuft eine Due Diligence ab?" | "Welche Dokumente brauche ich im Datenraum?" | "Wie finanziere ich die Übernahme?" |
| 7 – Notartermin | "Worauf muss ich im Kaufvertrag achten?" | "Was sind typische Vertragsklauseln?" | "Was passiert zwischen Signing und Closing?" |
| 8 – Signing | "Was sind Closing-Bedingungen?" | "Wie plane ich die Übernahme?" | "Wann informiere ich die Mitarbeiter?" |
| 9 – Closing | "Was ist ein 100-Tage-Plan?" | "Wie führe ich die Übergabegespräche?" | "Welche Quick Wins gibt es?" |

**Chat-Eröffnung (dynamisch):**
"Hallo! Ich bin dein M&A-Assistent. Ich kenne alle Inhalte der DUB Academy und helfe dir bei Fragen rund um Unternehmenskäufe. Du bist gerade in der Phase **"{Phasenname}"** bei {Projektname}. Wie kann ich dir helfen?"

---

## 5. Käufer: Mitteilungen pro Phasenwechsel

> **Darstellung:** Eine Mitteilung pro Phasenwechsel auf der Seite "Mitteilungen". Enthält: Titel, Beschreibung, Inline-Downloads (max. 2), Academy-Modul-Link, optionaler Tipp, CTA "Deal ansehen".

| Phase | Titel | Beschreibung | Downloads | Academy-Modul | Tipp |
|-------|-------|-------------|-----------|--------------|------|
| 1 → 2 | "Match bestätigt – bereite dich auf das Erstgespräch vor" | "Beide Seiten haben Interesse bekundet – ihr seid jetzt ein Match! Als Nächstes wird die NDA unterzeichnet." | NDA-Checkliste, Teaser-Checkliste | Dokumente im M&A-Prozess | "Kläre frühzeitig deine Finanzierung – die KfW bietet Förderprogramme speziell für Unternehmensübernahmen an." |
| 2 → 3 | "NDA unterzeichnet – Zugang zum Unternehmensexposé" | "Die Vertraulichkeitserklärung ist unterzeichnet. Du erhältst jetzt Zugang zum Informationsmemorandum (IM). Nutze die Checkliste, um es systematisch auszuwerten." | Checkliste IM bewerten | Dokumente im M&A-Prozess | — |
| 3 → 4 | "Persönliches Treffen absolviert – nächster Schritt: Angebot vorbereiten" | "Das Treffen hat stattgefunden. Wenn du ein Angebot machen möchtest, bereite jetzt deinen Letter of Intent (LOI) vor. Kläre parallel deine Finanzierung." | LOI-Mustervorlage, Bewertungs-Template | Angebotsstrategie & LOI | "Die meisten Käufer auf DUB verhandeln eine Exklusivitätsklausel in ihrem ersten LOI – das gibt dir Planungssicherheit." |
| 4 → 5 | "LOI vorgelegt – dein Angebot ist beim Verkäufer" | "Dein Letter of Intent wurde übermittelt. Der Verkäufer wird dein Angebot prüfen. Bereite dich parallel auf die Due Diligence vor." | DD-Checkliste | Due Diligence meistern | — |
| 5 → 6 | "LOI unterzeichnet – Due Diligence und Finanzierung starten" | "Der LOI ist von beiden Seiten unterschrieben. Jetzt beginnt die Due Diligence – du hast Zugang zum Datenraum." | DD-Checkliste, DD-Doku-Liste | Due Diligence meistern | "Stelle dein DD-Team zusammen: Steuerberater für die Zahlen, Anwalt für den Kaufvertrag." |
| 6 → 7 | "Notartermin vereinbart – Kaufvertrag prüfen" | "Der Notartermin steht. Prüfe den Kaufvertragsentwurf sorgfältig mit deinem Anwalt." | Checkliste Vertragsklauseln, Closing-Checkliste | Kaufvertrag & Closing | — |
| 7 → 8 | "Kaufvertrag unterschrieben – Closing vorbereiten" | "Der Kaufvertrag ist beim Notar unterschrieben. Erfülle die Closing-Bedingungen und bereite die Übernahme vor." | Closing-Checkliste | Kaufvertrag & Closing | — |
| 8 → 9 | "Closing abgeschlossen – Glückwunsch, du bist Unternehmer!" | "Die Transaktion ist vollständig abgeschlossen. Starte jetzt mit deinem 100-Tage-Plan." | 100-Tage-Plan Template | 100-Tage-Plan | "Die ersten 100 Tage entscheiden über den langfristigen Erfolg. Erst zuhören, dann optimieren." |

---

## 6. Käufer: Transaktionsübersicht (Enablement-Bar)

> **Darstellung:** Auf der Seite "Meine Transaktionen" → Tab "Matches". Jede Match-Karte zeigt eine Enablement-Bar am unteren Rand.

| Phase | Bar-Text | Download-Link | Modul-Link |
|-------|----------|--------------|------------|
| 1 – Interessensbekundung | "Nächster Schritt: Warte auf die Antwort des Verkäufers" | — | — |
| 2 – Match | "Nächster Schritt: NDA prüfen und unterzeichnen" | NDA-Checkliste | Dokumente im M&A-Prozess |
| 3 – NDA unterzeichnet | "Nächster Schritt: Unternehmensexposé auswerten" | Checkliste IM | Dokumente im M&A-Prozess |
| 4 – Pers. Treffen | "Nächster Schritt: Angebot vorbereiten – erstelle deinen LOI" | LOI-Vorlage | Angebotsstrategie & LOI |
| 5 – LOI vorgelegt | "Nächster Schritt: Due Diligence vorbereiten" | DD-Checkliste | Due Diligence meistern |
| 6 – LOI unterzeichnet | "Nächster Schritt: Datenraum prüfen und Finanzierung finalisieren" | DD-Doku-Liste | Due Diligence meistern |
| 7 – Notartermin | "Nächster Schritt: Kaufvertrag mit Anwalt prüfen" | Checkliste Vertragsklauseln | Kaufvertrag & Closing |
| 8 – Signing | "Nächster Schritt: Closing-Bedingungen erfüllen" | Closing-Checkliste | Kaufvertrag & Closing |
| 9 – Closing | "Geschafft! Starte deinen 100-Tage-Plan" | 100-Tage-Plan Template | 100-Tage-Plan |

**Zusätzlich:** Jede Match-Karte zeigt ein **Phase-Badge** (farbiger Chip) mit dem aktuellen Phasennamen.

---

## 7. Verkäufer: Empfohlene Schritte pro Phase

> **Kontext:** Der Verkäufer sieht eine Übersicht aller Interessenten/Käufer. Jeder Käufer hat eine eigene Phase. Die empfohlenen Schritte beziehen sich auf den jeweiligen Käufer.

### Phase 1: Interessensbekundung erhalten

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | Neue Interessensbekundung erhalten | ✅ Erledigt |
| 2 | Käuferprofil ansehen und prüfen | ☐ Offen |
| 3 | Profil mit deinen Kriterien abgleichen (Branche, Erfahrung, Kaufkraft) | ☐ Offen |
| 4 | Kaufkraft und Finanzierungsfähigkeit einschätzen | ☐ Offen |
| 5 | Match bestätigen oder freundlich ablehnen | ☐ Offen |

**Phasenbeschreibung:**
"Du hast eine neue Interessensbekundung erhalten. Prüfe das Käuferprofil sorgfältig – passt der Interessent zu deinem Unternehmen? Nutze die Screening-Checkliste, um systematisch zu bewerten."

---

### Phase 2: Match

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | Match bestätigt – beidseitiges Interesse | ✅ Erledigt |
| 2 | NDA zur Unterzeichnung an den Käufer senden | ☐ Offen |
| 3 | Erstgespräch vorbereiten (Gesprächsleitfaden nutzen) | ☐ Offen |
| 4 | Unterlagen zusammenstellen (Jahresabschlüsse, BWA) | ☐ Offen |
| 5 | Gesprächstermin vereinbaren | ☐ Offen |

**Phasenbeschreibung:**
"Match bestätigt – der Käufer hat sein Interesse bestätigt. Sende jetzt die NDA und bereite das Erstgespräch vor. Unser Leitfaden hilft dir, das Gespräch strukturiert zu führen."

---

### Phase 3: NDA unterzeichnet

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | NDA unterzeichnet | ✅ Erledigt |
| 2 | Käuferprofil mit Screening-Checkliste prüfen | ☐ Offen |
| 3 | Unterlagen (Jahresabschlüsse, BWA) bereitstellen | ☐ Offen |
| 4 | Persönliches Kennenlernen vorbereiten (Gesprächsleitfaden) | ☐ Offen |

**Phasenbeschreibung:**
"Die NDA ist unterzeichnet. Du kannst jetzt vertrauliche Unterlagen teilen – Jahresabschlüsse, BWA und Kundenlisten. Nutze die Screening-Checkliste, um den Käufer vorab einzuschätzen, und bereite das persönliche Kennenlernen vor."

---

### Phase 4: Persönliches Treffen

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | Persönliches Treffen durchgeführt | ✅ Erledigt |
| 2 | Käufer mit Bewertungsmatrix systematisch einschätzen | ☐ Offen |
| 3 | Referenzen und Finanzierungsnachweis anfragen | ☐ Offen |
| 4 | Entscheidung: Weitermachen oder freundlich absagen? | ☐ Offen |

**Phasenbeschreibung:**
"Das persönliche Treffen hat stattgefunden. Bewerte den Käufer systematisch – passt er als Nachfolger zu deinem Unternehmen? Nutze die Bewertungsmatrix, um deine Eindrücke zu strukturieren."

---

### Phase 5: LOI vorgelegt

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | LOI erhalten und gelesen | ✅ Erledigt |
| 2 | Wesentliche Punkte prüfen: Kaufpreis, Deal-Struktur, Exklusivität | ☐ Offen |
| 3 | Rückfragen mit dem Käufer klären | ☐ Offen |
| 4 | Mit Berater/Anwalt durchsprechen | ☐ Offen |
| 5 | LOI unterschreiben oder Gegenvorschlag formulieren | ☐ Offen |

**Phasenbeschreibung:**
"Du hast einen Letter of Intent (LOI) erhalten. Prüfe das Angebot sorgfältig – insbesondere Kaufpreis, Exklusivitätsklausel und Bedingungen. Halte die Exklusivität so kurz wie möglich (max. 3–4 Monate) und bevorzuge wenn möglich die mildere Abschlussexklusivität."

---

### Phase 6: LOI unterzeichnet

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | LOI von beiden Seiten unterschrieben | ✅ Erledigt |
| 2 | Datenraum für die Due Diligence vorbereiten | ☐ Offen |
| 3 | Dokumente strukturiert hochladen (Datenraum-Vorlage nutzen) | ☐ Offen |
| 4 | Mitarbeiter und Schlüsselpersonen informieren (falls nötig) | ☐ Offen |
| 5 | Steuerberater/Anwalt für Kaufvertragsverhandlung einbinden | ☐ Offen |

**Phasenbeschreibung:**
"Der LOI ist unterschrieben – jetzt beginnt die Due Diligence. Bereite den Datenraum vor und stelle alle relevanten Dokumente strukturiert bereit. Die DD-Vorbereitungs-Checkliste hilft dir, nichts zu vergessen."

---

### Phase 7: Notartermin

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | Notartermin vereinbart | ✅ Erledigt |
| 2 | Kaufvertragsentwurf mit Anwalt prüfen | ☐ Offen |
| 3 | Closing-Checkliste durchgehen | ☐ Offen |
| 4 | Übergabeplanung starten | ☐ Offen |

**Phasenbeschreibung:**
"Der Notartermin steht. Prüfe den Kaufvertragsentwurf sorgfältig mit deinem Anwalt und bereite die Closing-Unterlagen vor."

---

### Phase 8: Signing

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | Kaufvertrag unterschrieben | ✅ Erledigt |
| 2 | Closing-Bedingungen erfüllen | ☐ Offen |
| 3 | Übergabeplan mit dem Käufer abstimmen | ☐ Offen |
| 4 | Mitarbeiter und Kunden über den Eigentümerwechsel informieren | ☐ Offen |

**Phasenbeschreibung:**
"Der Kaufvertrag ist unterschrieben. Jetzt müssen die Closing-Bedingungen erfüllt werden. Beginne parallel mit der Übergabeplanung."

---

### Phase 9: Closing

| # | Schritt | Status bei Eintritt |
|---|---------|-------------------|
| 1 | Transaktion vollständig abgeschlossen | ✅ Erledigt |
| 2 | Strukturierte Übergabe starten (Übergabe-Checkliste) | ☐ Offen |
| 3 | Wissenstransfer-Plan mit dem Käufer umsetzen | ☐ Offen |
| 4 | Kunden- und Lieferantenbeziehungen übergeben | ☐ Offen |
| 5 | Eigenes nächstes Kapitel planen | ☐ Offen |

**Phasenbeschreibung:**
"Der Verkauf ist abgeschlossen – Glückwunsch! Starte jetzt die strukturierte Übergabe. Ein guter Wissenstransfer sichert den Erfolg deines Lebenswerks auch nach dem Eigentümerwechsel."

---

## 8. Verkäufer: Sidebar-Content pro Phase

### Block A: "Dein nächster Schritt"

| Phase | Tipp-Text | Academy-Modul (CTA) |
|-------|-----------|---------------------|
| 1 – IB erhalten | "Neuer Interessent! Prüfe sein Profil sorgfältig. Unser Screening-Modul zeigt dir, worauf du achten musst." | Käufer-Screening |
| 2 – Match | "Match bestätigt – bereite das Erstgespräch vor. Unser Modul gibt dir einen Gesprächsleitfaden." | Kennenlernen |
| 3 – NDA unterzeichnet | "NDA steht – jetzt kannst du offen sprechen. Bereite die Unterlagen vor und plane das Kennenlernen." | Kennenlernen |
| 4 – Pers. Treffen | "Das Treffen war gut? Bewerte den Käufer systematisch mit der Bewertungsmatrix." | Käufer-Screening |
| 5 – LOI vorgelegt | "LOI erhalten – prüfe das Angebot sorgfältig. Unser Modul zeigt dir die wichtigsten Punkte." | LOI verhandeln |
| 6 – LOI unterzeichnet | "LOI steht – bereite den Datenraum für die Due Diligence vor." | DD & Closing |
| 7 – Notartermin | "Notartermin steht – prüfe den Kaufvertrag und bereite das Closing vor." | DD & Closing |
| 8 – Signing | "Vertrag unterschrieben – letzte Schritte bis zum Closing." | DD & Closing |
| 9 – Closing | "Verkauf abgeschlossen! Starte die Übergabe strukturiert." | Übergabe |

### Block B: "Berater empfohlen"

| Phase | Anzeigen? | Text |
|-------|-----------|------|
| 1–3 | Ja (dezent) | "Viele Verkäufer mandatieren einen M&A-Berater, der den gesamten Prozess begleitet. Besonders bei der Käufersuche und Verhandlung kann das wertvoll sein." |
| 4–6 | Ja (prominent) | "Ab der LOI-Phase ist ein erfahrener Berater besonders wertvoll – für die Vertragsverhandlung und den Datenraum." |
| 7–8 | Ja (prominent) | "Für die Kaufvertragsverhandlung ist ein spezialisierter M&A-Anwalt unerlässlich." |
| 9 | Nein | — |

---

## 9. Verkäufer: Chat-Widget Quick Actions pro Phase

| Phase | Quick Action 1 | Quick Action 2 | Quick Action 3 |
|-------|---------------|---------------|---------------|
| 1 – IB erhalten | "Wie prüfe ich einen Interessenten?" | "Was ist ein gutes Käuferprofil?" | "Wann lehne ich ab?" |
| 2 – Match | "Wie bereite ich das Erstgespräch vor?" | "Was darf ich vor der NDA verraten?" | "Brauche ich einen Berater?" |
| 3 – NDA unterzeichnet | "Welche Unterlagen muss ich teilen?" | "Was gehört in ein IM?" | "Wie schütze ich vertrauliche Infos?" |
| 4 – Pers. Treffen | "Wie bewerte ich den Käufer?" | "Worauf achten beim Kennenlernen?" | "Was sind Red Flags bei Käufern?" |
| 5 – LOI vorgelegt | "Wie prüfe ich den LOI?" | "Was ist eine faire Exklusivität?" | "Wie bereite ich den Datenraum vor?" |
| 6 – LOI unterzeichnet | "Was gehört in den Datenraum?" | "Wie läuft die Due Diligence ab?" | "Was prüft der Käufer?" |
| 7 – Notartermin | "Worauf beim Kaufvertrag achten?" | "Was sind typische Klauseln?" | "Was passiert beim Notar?" |
| 8 – Signing | "Was sind Closing-Bedingungen?" | "Wann informiere ich meine Mitarbeiter?" | "Wie plane ich die Übergabe?" |
| 9 – Closing | "Wie gestalte ich die Übergabe?" | "Wie lange dauert der Wissenstransfer?" | "Was kommt nach dem Verkauf?" |

---

## 10. Academy-Modul-Zuordnung

### Käufer-Academy (9 Module)

| Modul | Datei | Relevante Phasen | Dauer |
|-------|-------|-----------------|-------|
| Suchstrategie & Käuferprofil | `academy-modul-suchstrategie.html` | Pre-Deal, Phase 1 | 15 Min. |
| Transaktionsablauf und Deal-Strukturen | `academy-modul-transaktionsstrukturen.html` | Pre-Deal, Phase 4 | 15 Min. |
| Bewertung & Preisfindung | `academy-modul-bewertung.html` | Phase 3–4 | 12 Min. |
| Dokumente im M&A-Prozess | `academy-modul-dokumente.html` | Phase 2–3 | 12 Min. |
| Angebotsstrategie & LOI | `academy-modul-angebotsstrategie.html` | Phase 4–5 | 12 Min. |
| Due Diligence meistern | `academy-modul-due-diligence.html` | Phase 5–6 | 15 Min. |
| Akquisitionsfinanzierung | `academy-modul-finanzierung.html` | Phase 3–6 | 15 Min. |
| Kaufvertrag & Closing | `academy-modul-kaufvertrag.html` | Phase 7–8 | 12 Min. |
| 100-Tage-Plan | `academy-modul-100-tage-plan.html` | Phase 8–9 | 15 Min. |

### Verkäufer-Academy (10 Module)

| Modul | Datei | Relevante Phasen | Dauer |
|-------|-------|-----------------|-------|
| Exit-Readiness | `seller-academy-modul-exit-readiness.html` | Pre-Deal | 15 Min. |
| Verkaufsberater mandatieren | `seller-academy-modul-verkaufsberater.html` | Pre-Deal | 12 Min. |
| Verkaufsprozess verstehen | `seller-academy-modul-verkaufsprozess.html` | Pre-Deal | 15 Min. |
| Unternehmensbewertung | `seller-academy-modul-bewertung.html` | Pre-Deal, Phase 5 | 12 Min. |
| Unterlagen vorbereiten | `seller-academy-modul-unterlagen.html` | Pre-Deal, Phase 3 | 15 Min. |
| Käufer-Screening | `seller-academy-modul-kaeufer-screening.html` | Phase 1, Phase 4 | 12 Min. |
| Kennenlernen | `seller-academy-modul-kennenlernen.html` | Phase 2–3 | 12 Min. |
| LOI verhandeln | `seller-academy-modul-loi.html` | Phase 5 | 15 Min. |
| DD & Closing | `seller-academy-modul-dd-closing.html` | Phase 6–8 | 15 Min. |
| Übergabe | `seller-academy-modul-uebergabe.html` | Phase 9 | 12 Min. |

---

## 11. Downloads pro Phase

### Käufer-Downloads

| Phase | Download 1 | Download 2 | Download 3 | Download 4 |
|-------|-----------|-----------|-----------|-----------|
| 1 – Interessensbekundung | Käuferprofil-Vorlage (PDF) | Dokumenten-Checkliste (PDF) | — | — |
| 2 – Match | NDA-Checkliste (PDF) | Checkliste Teaser bewerten (PDF) | — | — |
| 3 – NDA unterzeichnet | Checkliste IM bewerten (PDF) | NDA-Checkliste (PDF) | Bewertungs-Template (Excel) | — |
| 4 – Pers. Treffen | LOI-Mustervorlage (PDF) | Bewertungs-Template (Excel) | Share Deal vs. Asset Deal (PDF) | Finanzierungsplan-Vorlage (Excel) |
| 5 – LOI vorgelegt | DD-Checkliste (PDF) | Finanzierungsplan-Vorlage (Excel) | — | — |
| 6 – LOI unterzeichnet | DD-Checkliste (PDF) | DD-Doku-Liste (PDF) | Finanzierungsplan (Excel) | Checkliste Bankgespräch (PDF) |
| 7 – Notartermin | Checkliste Vertragsklauseln (PDF) | Closing-Checkliste (PDF) | — | — |
| 8 – Signing | Closing-Checkliste (PDF) | 100-Tage-Plan Template (PDF) | — | — |
| 9 – Closing | 100-Tage-Plan Template (PDF) | — | — | — |

### Verkäufer-Downloads

| Phase | Download 1 | Download 2 | Download 3 | Download 4 |
|-------|-----------|-----------|-----------|-----------|
| 1 – IB erhalten | Käufer-Screening-Checkliste (PDF) | Käufer-Bewertungsmatrix (Excel) | — | — |
| 2 – Match | Gesprächsleitfaden Erstgespräch (PDF) | NDA-Vorlage (PDF) | — | — |
| 3 – NDA unterzeichnet | Käufer-Screening-Checkliste (PDF) | Gesprächsleitfaden (PDF) | Unterlagen-Checkliste (PDF) | — |
| 4 – Pers. Treffen | Käufer-Bewertungsmatrix (Excel) | Referenz-Checkliste (PDF) | — | — |
| 5 – LOI vorgelegt | LOI-Checkliste für Verkäufer (PDF) | Exklusivitäts-Merkblatt (PDF) | — | — |
| 6 – LOI unterzeichnet | DD-Vorbereitungs-Checkliste (PDF) | Datenraum-Vorlage (Excel) | — | — |
| 7 – Notartermin | Closing-Day-Checkliste (PDF) | Kaufvertrags-Checkliste (PDF) | — | — |
| 8 – Signing | Closing-Day-Checkliste (PDF) | Übergabe-Checkliste (PDF) | — | — |
| 9 – Closing | Übergabe-Checkliste (PDF) | Wissenstransfer-Plan (PDF) | — | — |



---

## 12. Phasenwechsel-Trigger & Berechtigungen

> **Kernfrage:** Wer oder was löst den Übergang von Phase X nach Phase X+1 aus?

| Übergang | Trigger-Typ | Auslöser | Wer darf auslösen? |
|----------|-------------|----------|-------------------|
| → Phase 1 (IB) | **User-Aktion** | Käufer klickt "Interesse bekunden" auf Listing-Seite | Käufer |
| 1 → 2 (Match) | **System** | Verkäufer bestätigt die Interessensbekundung | Verkäufer (Bestätigung) → System erzeugt Match |
| 2 → 3 (NDA) | **System** | NDA-Dokument wird von beiden Seiten digital unterzeichnet (E-Signatur) | System erkennt beide Unterschriften |
| 3 → 4 (Treffen) | **User-Aktion** | Entweder Käufer oder Verkäufer markiert "Treffen hat stattgefunden" | Beide Seiten können bestätigen; idealerweise bestätigen beide |
| 4 → 5 (LOI vorgelegt) | **System** | Käufer lädt LOI-Dokument hoch oder sendet LOI über die Plattform | Käufer |
| 5 → 6 (LOI unterzeichnet) | **System** | LOI wird von beiden Seiten digital unterzeichnet | System erkennt beide Unterschriften |
| 6 → 7 (Notartermin) | **User-Aktion** | Käufer oder Verkäufer trägt Notartermin-Datum ein | Beide Seiten können eintragen |
| 7 → 8 (Signing) | **User-Aktion** | Käufer oder Verkäufer bestätigt "Kaufvertrag unterschrieben" | Beide Seiten bestätigen |
| 8 → 9 (Closing) | **User-Aktion** | Käufer oder Verkäufer bestätigt "Closing abgeschlossen" | Beide Seiten bestätigen |

### Regeln

- **Phasen können nicht übersprungen werden.** Der Übergang ist strikt sequenziell (1 → 2 → 3 → ... → 9).
- **Rücksprünge sind nicht möglich.** Eine Phase kann nicht rückgängig gemacht werden. Bei Abbruch → Status wechselt auf "Ausgeschieden" (eigener Status, keine Phase).
- **Bei Bestätigung durch beide Seiten:** Phase wechselt erst, wenn mindestens eine Seite bestätigt. Optional: Warnung an die andere Seite, wenn nur eine bestätigt hat ("Käufer hat das Treffen als stattgefunden markiert – bestätigst du das?").
- **Timestamp:** Jeder Phasenwechsel wird mit Datum + Uhrzeit gespeichert. Dieses Datum erscheint in der Timeline und in der Phasen-Historie.

### Sonderfall: Ausscheiden

| Auslöser | Wer darf? | Folge |
|----------|-----------|-------|
| Käufer zieht sich zurück | Käufer | Deal-Status → "Ausgeschieden (Käufer)" |
| Verkäufer lehnt ab | Verkäufer | Deal-Status → "Ausgeschieden (Verkäufer)" |
| Interessensbekundung abgelehnt | Verkäufer (in Phase 1) | Kein Match → Deal-Status → "Abgelehnt" |

Bei "Ausgeschieden" wird kein Enablement-Content mehr angezeigt. Die Deal-Karte zeigt einen grauen Status-Badge "Ausgeschieden" mit dem Datum.

---

## 13. Checklisten: Persistenz & Lifecycle

### Datenspeicherung

- Jeder Checklist-Eintrag wird als **Datenbankobjekt** gespeichert mit:
  - `deal_id` (FK zum Deal)
  - `user_id` (FK zum User – Käufer oder Verkäufer)
  - `phase` (Integer 1–9)
  - `step_index` (Integer 1–5, Position in der Checkliste)
  - `checked` (Boolean, Default: false)
  - `checked_at` (Timestamp, nullable)

### Verhalten bei Phasenwechsel

- **Alte Checkliste bleibt gespeichert**, ist aber nicht mehr sichtbar auf der Deal-Detailseite.
- Die Deal-Detailseite zeigt **immer nur die Checkliste der aktuellen Phase**.
- In der **Phasen-Historie** (vertikale Timeline) können abgeschlossene Phasen aufgeklappt werden, um die Checkliste dieser Phase nachträglich einzusehen (read-only).
- Bei Phaseneintritt wird Schritt 1 automatisch auf `checked: true` gesetzt (= der Trigger-Event).

### Vorausgefüllte Steps

- Die Checklist-Items werden **nicht vom User erstellt**, sondern kommen aus der Konfiguration (§2 / §7 dieser Spec).
- Das System rendert beim Laden der Deal-Detailseite die Items anhand von `phase` + `perspektive (Käufer/Verkäufer)`.
- Der User kann die Reihenfolge nicht ändern und keine eigenen Items hinzufügen.

### Fortschrittsanzeige

- Optional: Prozentanzeige oder Balken unterhalb des Phase-Titels ("3 von 5 Schritten erledigt").
- Die Empfehlung ist, dies einzubauen – es gibt dem User ein Gefühl von Fortschritt und Kontrolle.

---

## 14. Toast-Banner: Auslöser & Verhalten

### Wann wird der Toast angezeigt?

| Bedingung | Wert |
|-----------|------|
| **Trigger** | User öffnet die Seite "Meine Transaktionen" UND es gibt mindestens einen Deal, bei dem seit dem letzten Besuch ein Phasenwechsel stattgefunden hat |
| **Welcher Deal?** | Der Deal mit dem **jüngsten** Phasenwechsel. Bei mehreren gleichzeitigen Phasenwechseln: der Deal mit der **höchsten Phase** (= am weitesten fortgeschritten) |
| **Nur einmal pro Phasenwechsel** | Der Toast wird als "gesehen" markiert nach dem ersten Anzeigen. Beim nächsten Laden der Seite erscheint er nicht erneut (gespeichert in `user_toast_seen` mit `deal_id` + `phase`) |
| **Maximale Anzeige** | 1 Toast gleichzeitig. Kein Stapeln |

### Verhalten

| Eigenschaft | Wert |
|-------------|------|
| **Position** | Fixed, oben mittig, 16px unter der Nav (72px + 16px = 88px von oben) |
| **Animation** | Slide-in von oben (300ms ease-out) |
| **Auto-Dismiss** | Nach 12 Sekunden (Slide-out nach oben, 300ms) |
| **Manuelles Schließen** | X-Button oben rechts im Toast |
| **CTAs** | "Deal ansehen" → Deal-Detailseite, "Mitteilungen" → mitteilungen.html |
| **Inhalt** | Dynamisch: Titel = Phasen-Titel aus §5 (Mitteilungen), Subtitle = "{Projektname} · {Inserat-Titel} · vor {Zeitdauer}" |

### Edge Case: Mehrere Phasenwechsel

Wenn der User die Plattform länger nicht besucht hat und bei 3 Deals Phasenwechsel stattfanden:
- Toast zeigt nur den **relevantesten** Deal (höchste Phase)
- Die anderen Phasenwechsel sind in "Mitteilungen" sichtbar (Badge-Counter auf dem Mitteilungen-Reiter)
- Der Mitteilungen-Counter im Nav zeigt die Anzahl ungelesener Mitteilungen (roter Dot mit Zahl)

---

## 15. Mitteilungen: Lifecycle & Gelesen-Status

### Erstellung

- Pro Phasenwechsel wird **automatisch eine Mitteilung erstellt** (System-generiert, nicht vom User).
- Der Inhalt kommt aus §5 (Käufer) bzw. einem analogen Mapping für Verkäufer.
- Mitteilungen werden **für beide Seiten** erstellt (Käufer UND Verkäufer erhalten jeweils eine phasenwechsel-spezifische Mitteilung).

### Gelesen-Status

| Status | Darstellung | Auslöser |
|--------|------------|----------|
| **Ungelesen** | Grüner linker Rand (3px solid `#10B981`) + Badge "Neu" (grün) | Default bei Erstellung |
| **Gelesen** | Kein grüner Rand, kein Badge | User klickt irgendwo auf die Mitteilungskarte ODER öffnet die Mitteilungen-Seite und die Karte ist im Viewport für ≥2 Sekunden |

### Sortierung

- **Neueste zuerst** (nach `created_at` DESC)
- Ungelesene Mitteilungen erscheinen immer vor gelesenen (pinned to top)

### Archivierung

- Mitteilungen werden **nicht gelöscht**, auch nicht nach Abschluss eines Deals.
- Optional: "Alle als gelesen markieren"-Button oben rechts auf der Mitteilungen-Seite.

### Nav-Counter

- Der Reiter "Mitteilungen" in der Nav zeigt einen **roten Zähler** (Dot mit Zahl) wenn ungelesene Mitteilungen vorhanden sind.
- Format: Roter Kreis (18px) mit weißer Zahl. Bei >9: "9+".
- Counter zählt nur **ungelesene** Mitteilungen.

---

## 16. Verkäufer: Multi-Käufer-Logik

### Grundprinzip

Ein Verkäufer hat **ein Inserat** und potenziell **mehrere Käufer** in verschiedenen Phasen. Die Verkäufer-Deal-Detailseite (`transaktion-detail-verkaeufer.html`) zeigt alle Käufer als **expandierbare Karten**.

### Darstellung

| Element | Logik |
|---------|-------|
| **Übersicht (Stats-Bar)** | Zeigt aggregierte Zahlen: "X Aktive Interessenten", "X LOI", "X Matches", "X Gesamt-IB" |
| **Käufer-Karten** | Sortiert nach Phase (höchste zuerst), dann nach Datum (neueste zuerst) |
| **Default-Zustand** | Der Käufer mit der **höchsten Phase** ist ausgeklappt, alle anderen eingeklappt |
| **Expandieren/Kollabieren** | Klick auf die Käufer-Card-Header klappt auf/zu. Mehrere können gleichzeitig offen sein |

### Sidebar-Logik bei mehreren Käufern

| Situation | Sidebar zeigt |
|-----------|--------------|
| **Ein Käufer ausgeklappt** | Content der Phase dieses Käufers (aus §8) |
| **Mehrere Käufer ausgeklappt** | Content der Phase des **zuletzt ausgeklappten** Käufers |
| **Alle eingeklappt** | Content der Phase des **am weitesten fortgeschrittenen** Käufers |

### Checkliste bei mehreren Käufern

- Jeder Käufer hat seine **eigene** Checkliste.
- Die Checkliste ist **innerhalb der Käufer-Card** sichtbar (nicht in der Sidebar).
- Abhaken eines Items bei Käufer A hat keinen Einfluss auf Käufer B.

### Mini-Timeline pro Käufer

- Jede Käufer-Card zeigt eine **kompakte horizontale Mini-Timeline** (Dots ohne Labels).
- Hover auf einen Dot zeigt den Phasennamen als Tooltip.
- Klick auf die Mini-Timeline öffnet keine Detail-Ansicht (die Timeline ist rein informativ).

---

## 17. Download-Bibliothek & Dateiverwaltung

### Speicherung

- Alle Downloads sind **statische Dateien** (PDF, Excel), die zentral auf dem Server/CDN liegen.
- Pfad-Konvention: `/downloads/{perspektive}/{dateiname}` (z.B. `/downloads/kaeufer/loi-mustervorlage.pdf`)
- **Keine dynamische Generierung** – alle Vorlagen sind vorab erstellt und hochgeladen.

### Download-Katalog (vollständige Liste)

#### Käufer-Downloads

| ID | Dateiname | Format | Beschreibung |
|----|-----------|--------|-------------|
| K-01 | `kaeufer-profil-vorlage.pdf` | PDF | Vorlage für ein aussagekräftiges Käuferprofil |
| K-02 | `dokumenten-checkliste.pdf` | PDF | Übersicht aller Dokumente im M&A-Prozess |
| K-03 | `nda-checkliste.pdf` | PDF | Prüfpunkte für die NDA-Prüfung |
| K-04 | `checkliste-teaser-bewerten.pdf` | PDF | Kriterien zur Teaser-Bewertung |
| K-05 | `checkliste-im-bewerten.pdf` | PDF | Systematische Auswertung des IM |
| K-06 | `bewertungs-template.xlsx` | Excel | Multiple-Bewertung, DCF-Ansatz, Szenarioanalyse |
| K-07 | `loi-mustervorlage.pdf` | PDF | LOI-Template mit Erläuterungen |
| K-08 | `share-deal-vs-asset-deal.pdf` | PDF | Vergleich der Dealstrukturen |
| K-09 | `finanzierungsplan-vorlage.xlsx` | Excel | Kalkulation EK/FK-Mix, Kapitaldienstfähigkeit |
| K-10 | `dd-checkliste.pdf` | PDF | Vollständige DD-Prüfungsliste |
| K-11 | `dd-doku-liste.pdf` | PDF | Welche Dokumente im Datenraum angefordert werden |
| K-12 | `checkliste-bankgespraech.pdf` | PDF | Vorbereitung auf das Finanzierungsgespräch |
| K-13 | `checkliste-vertragsklauseln.pdf` | PDF | Wichtigste Klauseln im Kaufvertrag |
| K-14 | `closing-checkliste.pdf` | PDF | Alle Schritte zwischen Signing und Closing |
| K-15 | `100-tage-plan-template.pdf` | PDF | Strukturierte Übernahmeplanung |

#### Verkäufer-Downloads

| ID | Dateiname | Format | Beschreibung |
|----|-----------|--------|-------------|
| V-01 | `kaeufer-screening-checkliste.pdf` | PDF | Systematische Käuferbewertung |
| V-02 | `kaeufer-bewertungsmatrix.xlsx` | Excel | Scoring-Matrix für Käufervergleich |
| V-03 | `gespraechsleitfaden-erstgespraech.pdf` | PDF | Struktur für das Kennenlerngespräch |
| V-04 | `nda-vorlage.pdf` | PDF | NDA-Template für Verkäufer |
| V-05 | `unterlagen-checkliste.pdf` | PDF | Welche Dokumente vorbereitet werden müssen |
| V-06 | `referenz-checkliste.pdf` | PDF | Prüfpunkte für Käufer-Referenzen |
| V-07 | `loi-checkliste-verkaeufer.pdf` | PDF | LOI-Prüfpunkte aus Verkäufersicht |
| V-08 | `exklusivitaets-merkblatt.pdf` | PDF | Verhandlungs- und Abschlussexklusivität erklärt |
| V-09 | `dd-vorbereitungs-checkliste.pdf` | PDF | Datenraum-Vorbereitung |
| V-10 | `datenraum-vorlage.xlsx` | Excel | Ordnerstruktur und Dokumentenliste für den Datenraum |
| V-11 | `closing-day-checkliste.pdf` | PDF | Alle Schritte am Closing-Tag |
| V-12 | `kaufvertrags-checkliste.pdf` | PDF | Wichtigste Klauseln aus Verkäufersicht |
| V-13 | `uebergabe-checkliste.pdf` | PDF | Strukturierte Übergabe nach Closing |
| V-14 | `wissenstransfer-plan.pdf` | PDF | Template für den Wissenstransfer-Zeitplan |

### Referenzierung in §11

Die Download-Tabellen in §11 referenzieren die Downloads über den **Kurznamen** (z.B. "LOI-Mustervorlage"). Die exakte Datei-ID findet sich in der Tabelle oben.

---

## 18. KI-Assistent: Architektur & Antwortlogik

### MVP (Phase 1): Hardcoded Antworten

Für den Plattform-Launch empfehlen wir **hardcoded Antwort-Paare** pro Quick-Action-Chip:

| Eigenschaft | Wert |
|-------------|------|
| **Anzahl Antworten** | 3 pro Phase × 9 Phasen × 2 Perspektiven = **54 Antwort-Paare** |
| **Format** | JSON-Objekt: `{ phase: int, perspective: "kaeufer" | "verkaeufer", question: string, answer: string, sources: [{ label: string, url: string }] }` |
| **Quick-Action-Chips** | Werden aus der Konfiguration geladen (§4 / §9). Klick auf einen Chip sendet die Frage als User-Message und zeigt die hinterlegte Antwort als Bot-Message |
| **Freitext-Eingabe** | Im MVP deaktiviert oder mit Hinweis: "Freitext-Antworten kommen bald. Nutze die vorgeschlagenen Fragen oben." |
| **Quellen-Links** | Jede Antwort enthält 1–2 Links zu Academy-Modulen (am Ende der Antwort, als klickbare CTA) |

### Zukünftig (Phase 2): LLM-basiert

| Eigenschaft | Wert |
|-------------|------|
| **Modell** | Claude (oder gleichwertig) via API |
| **System-Prompt** | Enthält: (1) Rolle ("Du bist ein M&A-Berater-Assistent für DUB"), (2) aktuelle Phase + Deal-Kontext, (3) Academy-Inhalte als Retrieval-Kontext |
| **Retrieval** | Academy-Modul-Texte werden als RAG-Kontext mitgegeben. Pro Frage wird das relevanteste Modul identifiziert (basierend auf Phase-Mapping aus §10) |
| **Antwort-Regeln** | (1) Keine Rechts-/Steuerberatung – bei sensiblen Themen: "Sprich mit einem Berater/Anwalt". (2) Quellen-Transparenz: Jede Antwort referenziert das Academy-Modul. (3) Kein Zugriff auf vertrauliche Deal-Daten (Finanzzahlen, Dokumente) ohne explizite Freigabe |
| **Freitext** | Aktiviert – User kann beliebige Fragen stellen |
| **Fallback** | Wenn keine Antwort möglich: "Das kann ich leider nicht beantworten. Wende dich an deinen M&A-Berater oder kontaktiere den DUB-Support." |

### Chat-UI-Spezifikation

| Element | Wert |
|---------|------|
| **Floating Button** | Kreis, 56px Durchmesser, Position: fixed bottom-right (24px Abstand), Farbe: Lila Gradient (`#7C3AED` → `#6D28D9`), Icon: Chat-Bubble (Font Awesome `fa-comments`) |
| **Panel** | 400px breit, von rechts einfahrend (Slide-in 300ms), volle Höhe minus Nav (72px), z-index: 1000 |
| **Header** | Lila Gradient-Header, Titel "DUB M&A-Assistent", Untertitel "Dein persönlicher Berater", X-Close-Button |
| **Bot-Avatar** | Lila Kreis mit Roboter-Icon |
| **User-Avatar** | Grauer Kreis mit User-Icon |
| **Quick-Action-Chips** | Lila Border, rounded, klickbar. Verschwinden nach dem ersten Klick (werden durch die Frage/Antwort ersetzt) |
| **Input-Feld** | Unten fixiert, Placeholder: "Schreibe eine Nachricht...", Send-Button (Pfeil-Icon) |
| **Scrolling** | Chat-Verlauf scrollbar, neue Nachrichten auto-scroll nach unten |
| **Kontextuelle Eröffnung** | Beim Öffnen zeigt der Bot eine phasenabhängige Begrüßung (§4 Chat-Eröffnung) |

---

## 19. Berater-Box: Darstellungsvarianten

### Variante "dezent" (Phase 1–3 Käufer / Phase 1–3 Verkäufer)

| Eigenschaft | Wert |
|-------------|------|
| **Hintergrund** | `#F9FAFB` (sehr helles Grau) |
| **Border** | `1px solid #E5E7EB` |
| **Icon** | `fa-user-tie` in Grau (`#9CA3AF`) |
| **Text-Farbe** | `#6B7280` (mittelgrau) |
| **CTA** | Text-Link "Berater finden →" (kein Button) |
| **Position** | Unterster Block in der Sidebar (unter "M&A-Assistent") |

### Variante "prominent" (Phase 4–8 Käufer / Phase 4–8 Verkäufer)

| Eigenschaft | Wert |
|-------------|------|
| **Hintergrund** | Enablement-Gradient (`linear-gradient(135deg, #F0FDF4 0%, #F0FDFA 50%, #F5F3FF 100%)`) |
| **Border** | `1px solid #E0E7FF` |
| **Icon** | `fa-user-tie` in Lila (`#7C3AED`), größer (24px) |
| **Text-Farbe** | `#1A1A1A` (schwarz) |
| **Statistik-Zeile** | Fettgedruckt, oberhalb des Textes |
| **CTA** | Grüner Button (CTA-Gradient) "Berater finden →" |
| **Position** | Dritter Block in der Sidebar (unter "Passende Downloads", über "M&A-Assistent") |

---

## 20. Navigation: Perspektivwechsel Käufer/Verkäufer

### Grundprinzip

Jeder User kann sowohl Käufer als auch Verkäufer sein. Die Perspektive wird über die **Focus-Group** (Avatar-Dropdown oben rechts) gewechselt.

### Nav-Struktur pro Perspektive

| Nav-Element | Käufer-Perspektive | Verkäufer-Perspektive |
|-------------|-------------------|----------------------|
| Link 1 | Suche → `suche.html` | Mein Inserat → `inserat.html` |
| Link 2 | Suchaufträge → `suchauftraege.html` | Interessenten → `transaktion-detail-verkaeufer.html` |
| Link 3 | Mitteilungen → `mitteilungen.html` | Mitteilungen → `mitteilungen.html` |
| Link 4 | Postfach → `postfach.html` | Postfach → `postfach.html` |
| Link 5 | Meine Transaktionen → `transaktionen.html` | Meine Transaktionen → `transaktionen.html` |
| Link 6 | Academy → `academy.html` | Academy → `verkaufer-academy.html` |

### Focus-Group Dropdown

| Käufer-Perspektive | Verkäufer-Perspektive |
|-------------------|----------------------|
| **Zur Verkäuferansicht** → Verkäufer-Startseite | **Zur Käuferansicht** → Käufer-Startseite |
| Käuferprofil → `kauferprofil.html` | Mein Inserat bearbeiten |
| Kontoeinstellungen | Kontoeinstellungen |
| DUB-Professional | DUB-Professional |
| Abmelden | Abmelden |

### Perspektiv-Erkennung

- Die aktuelle Perspektive wird **serverseitig** als User-Preference gespeichert.
- Beim Login wird die **zuletzt genutzte Perspektive** geladen.
- Der Wechsel über die Focus-Group speichert die neue Perspektive und leitet auf die Startseite der gewählten Perspektive weiter.

---

## 21. Deal-Attraktivität: Käufer-Bewertungsfeld

### Beschreibung

Auf der Käufer-Deal-Detailseite kann der Käufer seine subjektive Einschätzung der Deal-Attraktivität auf einer Skala von 1 bis 5 eintragen.

### Darstellung

| Wert | Label | Farbe (Hintergrund) | Farbe (Text) |
|------|-------|-------------------|-------------|
| 1 | Sehr attraktiv | `#065F46` (Dunkelgrün) | `#FFFFFF` |
| 2 | Attraktiv | `#10B981` (Grün) | `#FFFFFF` |
| 3 | Neutral | `#F59E0B` (Gelb/Amber) | `#FFFFFF` |
| 4 | Weniger attraktiv | `#F97316` (Orange) | `#FFFFFF` |
| 5 | Unattraktiv | `#EF4444` (Rot) | `#FFFFFF` |

### Verhalten

| Eigenschaft | Wert |
|-------------|------|
| **Position** | Deal-Info-Box, oben rechts (neben Branche/Umsatz/EBITDA) |
| **Default** | Kein Wert ausgewählt (Platzhalter: "Bewerte diesen Deal") |
| **Interaktion** | Klick auf Zahl 1–5 setzt den Wert. Erneuter Klick ändert den Wert. |
| **Persistenz** | Wird pro User pro Deal gespeichert |
| **Sichtbarkeit** | Nur für den Käufer sichtbar (nicht für den Verkäufer) |
| **Sortierung** | Optional: Auf "Meine Transaktionen" können Deals nach Attraktivität sortiert werden |

### Hinweis: Kein Feld für Verkäufer

Das Feld "Deal-Attraktivität" existiert **nur in der Käufer-Perspektive**. In der Verkäufer-Perspektive gibt es kein Äquivalent – der Verkäufer bewertet Käufer über die Bewertungsmatrix (Download V-02).

---

## 22. Edge Cases & Sonderfälle

### 22.1 Deal wird abgebrochen

| Situation | Verhalten |
|-----------|----------|
| Käufer bricht ab (Phase 1–8) | Deal-Status → "Ausgeschieden". Kein Enablement-Content mehr. Grauer Badge auf Deal-Karte. Mitteilung an Verkäufer: "Käufer hat sich zurückgezogen." |
| Verkäufer lehnt ab (Phase 1) | Interessensbekundung → "Abgelehnt". Mitteilung an Käufer: "Der Verkäufer hat deine Interessensbekundung nicht angenommen." |
| Verkäufer bricht ab (Phase 2–8) | Deal-Status → "Ausgeschieden". Mitteilung an Käufer: "Der Verkäufer hat den Prozess beendet." |

### 22.2 Käufer hat mehrere aktive Deals

- Jeder Deal hat seine **eigene** Checkliste, Phase, Attraktivität und Chat-Kontext.
- Auf "Meine Transaktionen" sieht der Käufer alle Deals mit ihren jeweiligen Phasen-Badges.
- Der KI-Assistent ist **deal-spezifisch**: Beim Öffnen auf einer Deal-Detailseite kennt er den Deal-Kontext. Auf "Meine Transaktionen" ist der Chat generisch (ohne Deal-Kontext).

### 22.3 Verkäufer hat kein Inserat

- Wenn ein Verkäufer noch kein Inserat erstellt hat, zeigt die Verkäufer-Startseite einen CTA: "Erstelle dein Inserat – wir begleiten dich Schritt für Schritt."
- Academy-Module der Pre-Deal-Phase sind trotzdem zugänglich.
- Keine Deal-Detailseite, keine Checklisten, keine Mitteilungen.

### 22.4 Käufer hat Readiness Score < 30%

- Auf der Suche-Seite sind Listings **geblurrt/gesperrt** (bestehendes Feature, siehe `suche.html`).
- Auf der Deal-Detailseite wird ein zusätzlicher Hinweis angezeigt: "Dein Käuferprofil ist noch unvollständig (Score: X%). Vervollständige es, um deine Chancen zu erhöhen." → CTA: "Profil verbessern" → `kauferprofil.html`
- Der Hinweis erscheint als Banner oberhalb der Deal-Info-Box (gelber Hintergrund `#FEF3C7`, amber Border).

### 22.5 Phase ohne Aktion (Wartezeit)

In manchen Phasen wartet eine Seite auf die andere (z.B. Käufer wartet auf LOI-Antwort in Phase 5). In diesem Fall:

- Checkliste zeigt "Auf Rückmeldung des Verkäufers warten" als offenen Schritt.
- Sidebar-Tipp passt sich an: "Nutze die Wartezeit für..." mit sinnvoller Vorbereitung.
- **Kein Timer oder Countdown** – nur informativer Hinweis.

### 22.6 Direktverkauf vs. Berater-gestützter Verkauf

| Aspekt | Direktverkauf (<2M EUR) | Berater-gestützt |
|--------|------------------------|-----------------|
| Phase 3: Unterlagen | Jahresabschlüsse, BWA, ggf. Kundenliste | Informationsmemorandum (IM) |
| Phase 3: Checkliste | "Jahresabschlüsse und BWA anfordern" | "IM anfordern und auswerten" |
| Phase 3: Download | "Checkliste IM bewerten" (funktioniert für beide) | "Checkliste IM bewerten" |
| Phase 4: Treffen | Oft die wichtigste Informationsquelle | Ergänzend zum IM |

**Technische Umsetzung:** Das Inserat enthält ein Boolean-Feld `has_advisor` (hat der Verkäufer einen Berater mandatiert?). Basierend darauf wird in Phase 3 die passende Checklisten-Variante geladen.

### 22.7 Zeitliche Reihenfolge der Mitteilungen

Mitteilungen werden strikt nach `created_at` sortiert, **nicht** nach Phase. Beispiel:

```
24.03. – Deal B: NDA unterzeichnet (Phase 3)
23.03. – Deal A: LOI vorgelegt (Phase 5)
21.03. – Deal B: Match bestätigt (Phase 2)
```

Jede Mitteilung enthält den Deal-Namen, sodass der User die Zuordnung erkennt.

### 22.8 Academy-Modul noch nicht abgeschlossen

Wenn in der Sidebar "Dein nächster Schritt" auf ein Academy-Modul verlinkt wird, das der User noch nicht abgeschlossen hat:
- CTA-Text: **"Modul starten"**

Wenn das Modul bereits abgeschlossen ist:
- CTA-Text: **"Modul wiederholen"**
- Optional: Grünes Häkchen neben dem Modul-Namen

Der Abschluss-Status wird über das Academy-Fortschrittssystem verwaltet (bestehende Logik aus `academy.html` / Readiness Score).
---

## Anhang: Design-Referenzen

Alle visuellen Design-Details (Farben, Abstände, Komponenten) sind in der `CLAUDE.md` im Projektordner dokumentiert. Die folgenden Mockup-Dateien dienen als visuelle Referenz:

| Mockup-Datei | Zeigt |
|---|---|
| `transaktion-detail.html` | Käufer, Phase 4 (Pers. Treffen) |
| `transaktion-detail-galabau.html` | Käufer, Phase 3 (NDA unterzeichnet) |
| `transaktion-detail-verkaeufer.html` | Verkäufer, 3 Käufer auf Phase 1/3/5 |
| `mitteilungen.html` | Enablement-Mitteilungen für Phase 1–4 |
| `transaktionen.html` | Enablement-Bars + Toast-Banner |
