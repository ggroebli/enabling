# AMBER Enablement – Planning Document

**Erstellt:** 12. Februar 2026
**Basierend auf:** Strategie-Brainstorming vom 04. Februar 2026 (Florian, Graig, Kai, Fynn)
**Status:** Konzeptphase – iterative Bearbeitung in Sessions

---

## 1. Das Problem

AMBER will auf 20.000 Deals und 1 Mio. Nutzer skalieren. Das bedeutet, dass zunehmend **unerfahrene User** auf die Plattform kommen – Unternehmer, die noch nie ein Unternehmen verkauft haben, und Kaufinteressenten ohne M&A-Erfahrung.

**Kernfragen:**
- Wie machen wir einen Erstverkäufer "exit-ready", der keine Ahnung von M&A hat?
- Wie machen wir einen Erstkäufer "acquisition-ready", der noch nie akquiriert hat?
- Wie begleiten wir beide Seiten durch den gesamten Prozess – nicht nur am Anfang, sondern bei jedem Schritt?
- Wie verhindern wir, dass unvorbereitete Nutzer Deals scheitern lassen (und damit die Plattform-Reputation gefährden)?

**Wer ist betroffen:**
- **Verkäufer (SME-Inhaber):** Kein M&A-Wissen, kein Berater, inserieren oft ohne Exit-Readiness
- **Käufer (Erstakquisiteure):** Wissen nicht, wie sie sich präsentieren, finanzieren oder verhandeln sollen
- **Plattform selbst:** Scheiternde Deals = schlechte Conversion, schlechter Ruf, Churn

---

## 2. Die Produktvision – Drei Ebenen

Im Meeting wurden drei integrierte Enablement-Ebenen definiert:

### Ebene 1: Readiness Academy
**Wann:** Nach der Registrierung, VOR einem konkreten Deal
**Ziel:** Nutzer vorbereiten, bevor sie in einen Deal eintreten

#### Käufer-Readiness
- [ ] **Profilvervollständigung** – Readiness Score basierend auf ausgefülltem Profil
- [ ] **Selbsttest: Persönliche Eignung** – Bin ich als Käufer geeignet? Welche Targets passen zu mir?
- [ ] **Finanzierungsvorbereitung** – Eigenkapitalnachweis, Hausbank-Kontakt, Finanzierungsbereitschaft
- [ ] **Suchstrategie definieren** – Branche, Größe, Region, Kaufgründe
- [ ] **Vorlagen-Paket Käufer** – Liquiditätsplanung, Bankpräsentation, Käuferprofil-Vorlage
- [ ] **Wissensmodule** – Was ist ein LOI? Was ist Due Diligence? Wie verhandelt man?

#### Verkäufer-Readiness
- [ ] **Selbsttest: Ist mein Unternehmen verkäuflich?** – Kundenabhängigkeiten, Personenabhängigkeiten, Dokumentenlage
- [ ] **Readiness Score Verkäufer** – Wie "exit-ready" bin ich?
- [ ] **Dokumentenvorbereitung** – Welche Unterlagen muss ich vorbereiten? (Jahresabschlüsse, BWA, Steuererklärungen)
- [ ] **Vorlagen-Paket Verkäufer** – Teaser-Vorlage, Unterlagencheckliste
- [ ] **Bewertungsbandbreite** – Automatisierte Ersteinschätzung basierend auf Nutzerdaten
- [ ] **Wissensmodule** – Was ist mein Unternehmen wert? Wie läuft ein Verkaufsprozess? Was kostet ein Berater?

#### Format & Content
- KI-generierte Videos und Texte (Verantwortlich: Kai & Anja)
- Interaktive Selbsttests mit Score-Berechnung
- Downloadbare Templates (PDF/Excel)
- SEO-optimierte Artikel als "Abfallprodukt" (Glossar, Wissensartikel)

---

### Ebene 2: In-Flow Guidance
**Wann:** Während eines aktiven Deals, getriggert durch Prozessfortschritt
**Ziel:** Zur richtigen Zeit die richtigen Informationen bereitstellen

#### Trigger-basierte Prozesskette
Die aktuelle Ember-Prozesskette muss deutlich **granularer** werden. Für jeden Schritt:

| Prozessschritt | Beispiel-Trigger | Enablement-Aktion |
|---|---|---|
| Profil erstellt | Registrierung abgeschlossen | Onboarding-Guide, Readiness-Check starten |
| Inserat veröffentlicht (Verkäufer) | Inserat live | Checkliste "Was kommt als nächstes", Teaser-Tipps |
| Interesse bekundet (Käufer) | Interessensbekundung gesendet | Guide "Was passiert jetzt?", NDA-Erklärung |
| Match entstanden | Beidseitige Annahme | Checkliste erste Gespräche, Gesprächsleitfaden |
| LOI-Phase | LOI versendet/empfangen | LOI-Template, rechtliche Hinweise |
| Due Diligence | DD gestartet | DD-Checkliste, **Beraterempfehlung** (→ Beraterbörse) |
| Verhandlung | Preisverhandlung | Verhandlungstipps, Bewertungstools |
| Closing | Notartermin | Closing-Checkliste, rechtliche Schritte |
| Post-Deal (Käufer) | Übernahme abgeschlossen | PMI-Checkliste, Change-Management-Tipps |
| Post-Deal (Verkäufer) | Verkauf abgeschlossen | Vermögensverwaltungs-Hinweise, nächste Schritte |

#### Ausspielung
- **In-Plattform:** Mitteilungen, Tooltips, Banner auf relevanten Seiten
- **E-Mail:** Trigger-basierte Erinnerungen für Nutzer, die nicht täglich einloggen
- **Verlinkung:** Relevante Academy-Module + passende Berater aus der Beraterbörse

---

### Ebene 3: KI-Assistent ("Kai Avatar")
**Wann:** Jederzeit verfügbar, kontextabhängig
**Ziel:** Persönlicher M&A-Berater als Chatbot

- [ ] **Wissensbasis:** Trainiert auf Academy-Inhalten + allgemeinem M&A-Wissen
- [ ] **Deal-Kontext:** Kennt (mit Nutzer-Zustimmung) die konkreten Deal-Informationen
- [ ] **Anwendungsfälle:** "Was sollte ich als nächstes tun?", "Ist dieser Preis realistisch?", "Welche Unterlagen brauche ich für die DD?"
- [ ] **Datenschutz:** Explizite Nutzer-Zustimmung bevor Deal-Daten einbezogen werden
- [ ] **MVP-Version:** Auch ohne Deal-Kontext wertvoll – allgemeine M&A-Fragen beantworten

**Abhängigkeit:** Braucht Inhalte aus Ebene 1 & 2 als Trainingsbasis. Ein "dummer" Chatbot mit allgemeinem M&A-Wissen wäre aber auch schon ein Mehrwert beim Launch.

---

## 3. Integration: Beraterbörse × Enablement

Ein zentrales Thema im Meeting: Das Enablement-Produkt muss mit der **Beraterbörse** (Beraterverzeichnis/Directory) verzahnt werden.

**Idee:** An den Stellen, wo Self-Service Enablement an seine Grenzen stößt, werden kontextbezogen Berater empfohlen.

Beispiel:
> Nutzer ist im Schritt "Due Diligence". Die Plattform zeigt:
> 1. DD-Checkliste + Academy-Modul "Was ist Due Diligence?"
> 2. KI-Assistent beantwortet Fragen
> 3. **"Du brauchst Unterstützung? Hier sind 3 DD-Berater, die sich auf deine Branche spezialisiert haben."**

Das schafft einen natürlichen Übergang von kostenlosem Self-Service zu kostenpflichtigem Berater-Service – ohne dass es sich wie ein Hard-Sell anfühlt.

---

## 4. Was NICHT im Scope ist (vorerst)

- Vollständiger Datenraum (nur Checklisten + Hinweise, welche Dokumente benötigt werden)
- Persönlicher menschlicher Coach / Sparring-Partner (perspektivisch denkbar, nicht für MVP)
- PMI-Plattform (nur Checklisten und Hinweise, kein vollständiges PMI-Tool)
- Eigene Finanzierungslösung (evtl. später embedded via Nico)

---

## 5. Launch-Strategie & Priorisierung

### Phase 1: MVP (Bubble-Launch, ~1. Juli)
**Realistischer Umfang: ca. 10-20% der Gesamtvision**

Priorisierungsvorschlag (offen für Diskussion):

| Priorität | Feature | Ebene | Aufwand | Impact |
|---|---|---|---|---|
| P1 | Käufer-Readiness-Check (Selbsttest + Score) | 1 | Mittel | Hoch |
| P1 | Verkäufer-Readiness-Check (Selbsttest + Score) | 1 | Mittel | Hoch |
| P1 | Basis-Academy (5-10 Kernmodule mit KI-Content) | 1 | Mittel | Hoch |
| P1 | KI-Assistent (allgemeines M&A-Wissen) | 3 | Niedrig | Hoch |
| P2 | Templates/Vorlagen (Käufer + Verkäufer) | 1 | Niedrig | Mittel |
| P2 | Basis In-Flow Notifications (3-4 Key-Trigger) | 2 | Mittel | Mittel |
| P3 | Berater-Empfehlung an Prozesspunkten | 2+Börse | Hoch | Hoch |
| P3 | Automatisierte Bewertungsbandbreite | 1 | Hoch | Mittel |
| Later | Vollständige Prozesskette mit Triggern | 2 | Hoch | Hoch |
| Later | Deal-kontextueller KI-Assistent | 3 | Mittel | Hoch |
| Later | Einfacher Datenraum | - | Hoch | Mittel |
| Later | PMI-Checklisten | 1 | Niedrig | Niedrig |

### Phase 2: Neue Plattform (nach Merger)
- Vollständige Prozesskette mit allen Triggern
- KI-Assistent mit Deal-Kontext
- Tiefe Beraterbörsen-Integration
- Embedded-Finanzierung
- Bewertungstool
- Einfacher Datenraum

---

## 6. Offene Fragen & Brainstorming-Themen

Für die nächsten Sessions zu klären:

### Konzeptionell
1. **Wie viel Zwang vs. Freiwilligkeit?** – Muss man den Readiness-Check durchlaufen, bevor man inserieren/kontaktieren darf? Oder ist es nur eine Empfehlung?
2. **Gamification des Readiness Scores?** – Badges, Fortschrittsbalken, "Verified Buyer/Seller" Badge im Profil?
3. **Wie granular muss die Prozesskette sein?** – Wie viele Schritte? Wer aktualisiert den Status (Käufer, Verkäufer, System)?
4. **Content-Erstellung:** Wer erstellt welche Inhalte? Timeline für KI-generierte Videos?

### UX/UI
5. **Wo lebt die Academy?** – Eigener Menüpunkt? In den bestehenden Flow integriert? Beides?
6. **Wo lebt der KI-Assistent?** – Floating Widget? Eigene Seite? In-Context bei jedem Prozessschritt?
7. **Wie werden In-Flow-Hinweise dargestellt?** – Mitteilungen? Modale? Inline-Banner? Sidebar?

### Technisch
8. **Bubble-Machbarkeit:** Was davon ist realistisch in Bubble bis Juli?
9. **KI-Assistent Datenschutz:** Wie regeln wir die Zustimmung für Deal-kontextuelle Antworten?
10. **E-Mail-Trigger:** Welches E-Mail-System? Wie vermeiden wir Spam-Empfindung?

---

## 7. Session-Plan

Dieses Dokument wird in mehreren Sessions bearbeitet. Vorgeschlagene Struktur:

### Session 1 (aktuell): Problemverständnis & Strukturierung
- [x] Meeting-Inhalte strukturieren
- [ ] Gemeinsames Brainstorming zu offenen Fragen
- [ ] Priorisierung validieren

### Session 2: Käufer-Journey Mockup
- [ ] Käufer-Readiness-Flow durchdesignen
- [ ] Academy-Startseite + 1-2 Module mockupen
- [ ] Readiness Score UI-Konzept

### Session 3: Verkäufer-Journey Mockup
- [ ] Verkäufer-Readiness-Flow durchdesignen
- [ ] Selbsttest "Ist mein Unternehmen verkäuflich?" mockupen
- [ ] Bewertungsbandbreiten-UI (wenn im Scope)

### Session 4: In-Flow Guidance Mockup
- [ ] Prozesskette definieren (alle Schritte)
- [ ] Trigger-Notifications designen (Mitteilungen, E-Mail)
- [ ] Beraterbörsen-Integration mockupen

### Session 5: KI-Assistent Mockup
- [ ] Chat-UI designen
- [ ] Beispieldialoge definieren
- [ ] Einbettung in bestehende Seiten

### Session 6: Review & Finalisierung
- [ ] Alle Mockups verlinken
- [ ] Finales Konzeptpapier generieren
- [ ] Tech-Handoff vorbereiten

---

## 8. Teilnehmer & Verantwortlichkeiten

| Person | Rolle | Verantwortung |
|---|---|---|
| **Florian (Fynn)** | Product / Mockups | Mockup-Erstellung, technische Machbarkeit, Claude Code Sessions |
| **Graig** | Strategy / Content | Inhaltliche Konzeption, Prozessketten, Berater-Integration |
| **Kai** | Strategy / Content | Inhaltliche Konzeption, Academy-Module, Content-Erstellung |
| **Anja** | Content | Video- und Text-Content (KI-generiert) |

---

*Dieses Dokument wird iterativ in Sessions mit Claude Code weiterentwickelt.*
