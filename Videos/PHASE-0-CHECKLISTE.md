# Phase 0: Gratis-Smoke-Test

**Ziel:** In 2 Stunden für $0 wissen, ob der KI-Video-Workflow für DUB funktioniert.
**Was du danach weißt:** Ob ElevenLabs deine Stimme + deutsche Fachbegriffe gut klont und ob HeyGen-Lippensync mit dem Audio überzeugend wirkt. Erst wenn beides klar "ja" ist, gibst du Geld aus.

---

## Vorbereitung (5 Min, vor den 10 Schritten)

- [ ] Ruhigen Raum für Voice-Aufnahme finden (kein Echo, keine Lüfter, kein Verkehrslärm)
- [ ] Smartphone oder Headset-Mikro bereitlegen
- [ ] Smartphone laden (für Avatar-Test-Video)

---

## Die 10 Schritte

### 1. ElevenLabs Free-Account anlegen (5 Min)
- Öffne https://elevenlabs.io/sign-up
- Sign-up mit Google oder Email
- Plan: **Free** (nicht zahlen!)
- Email bestätigen

### 2. Voice-Sample für Free-Tier-Test aufnehmen (15 Min)
- Smartphone Voice Memos öffnen (iPhone) oder Audacity (Windows: https://www.audacityteam.org/)
- **2–3 Min** den Test-Text aus `PHASE-0-TEST-SKRIPT.md` (siehe unten) ruhig vorlesen
- Sprich normal, nicht künstlich langsam
- Speichern als MP3 oder WAV

### 3. Instant Voice Clone in ElevenLabs anlegen (10 Min)
- Im Dashboard: **Voices** (linke Sidebar) → **Add a New Voice**
- Wähle **Instant Voice Clone** (das ist das, was im Free-Tier geht – nicht Professional)
- Datei hochladen
- Name: "Graig Test"
- Labels: Language = German, Accent = German
- **Add Voice** → ist sofort verfügbar (kein langes Warten wie bei Professional)

### 4. Voice-Test mit deutschem Fachvokabular (5 Min)
- Dashboard → **Voices** → "Graig Test" → **Use voice**
- Im **Text-to-Speech**-Fenster diesen Test-Text einfügen (kritische M&A-Fachbegriffe):

```
Hallo und willkommen zum ersten Modul der DUB Academy.
Heute geht es um deine Suchstrategie und dein Käuferprofil.
Wir sprechen über EBIT, EBITDA, Multiples und Earn-Out-Klauseln.
Du brauchst in der Regel rund 20 Prozent des Kaufpreises als Eigenkapital.
Den Rest finanzierst du über Bankdarlehen oder ein Verkäuferdarlehen.
```

- Modell: **eleven_multilingual_v2**
- Stability 50%, Similarity 75%
- **Generate** → MP3 wird erzeugt
- **KRITISCH ANHÖREN:**
  - Klingt es nach dir?
  - Werden "EBIT", "EBITDA", "Earn-Out" verständlich ausgesprochen?
  - Werden Zahlen ("20 Prozent") sauber gesagt?

> **Entscheidungspunkt 1:** Wenn die Stimme schon hier blechern klingt oder Fachbegriffe katastrophal ausgesprochen werden – **STOP**. Wir müssen den Skript-Workflow anpassen (Fachbegriffe ausschreiben, Phonetik-Hints) oder eine ElevenLabs-Default-Stimme nutzen statt Custom Voice Clone. Schick mir das MP3 und ich höre rein.

### 5. HeyGen Free-Account anlegen (5 Min)
- Öffne https://www.heygen.com/signup
- Sign-up mit Google oder Email
- Plan: **Free** (3 Min/Monat mit Wasserzeichen)
- Email bestätigen

### 6. Stock-Avatar auswählen (5 Min)
- Dashboard → **Create Video** → **Avatar Video**
- Im Avatar-Karussell einen **männlichen, professionell wirkenden Stock-Avatar** wählen (z.B. "Daniel" oder "Edward")
- Nicht dein eigenes Avatar – das kommt erst in Phase 1

### 7. ElevenLabs-Audio in HeyGen importieren (5 Min)
- Im HeyGen-Editor: **Voice** → **Upload Audio**
- Die MP3 aus Schritt 4 hochladen
- Video-Größe: **1920×1080 (16:9)**
- Hintergrund: einfach lassen (egal welcher)
- **Submit** → Render dauert 3–10 Min

### 8. Render anschauen und Lippensync prüfen (10 Min)
- Wenn fertig: Video herunterladen oder im Browser ansehen
- **KRITISCH PRÜFEN:**
  - Sind die Lippen synchron zum Audio?
  - Passen die Mundbewegungen zu deutschen Lauten?
  - Wirkt der Avatar lebendig oder mechanisch?

> **Entscheidungspunkt 2:** Wenn Lippensync schlecht ist, brauchen wir Avatar IV/V – das gibt's nur ab Creator-Plan. Wenn auch das nicht klappt (was selten ist bei DUB-Sprechstil), müsste man den Workflow grundlegend überdenken.

### 9. Eigenes Avatar-Test-Video aufnehmen (15 Min – schon Vorbereitung für Phase 1)
- Smartphone frontal in Augenhöhe positionieren (am besten an Wand lehnen oder Stativ)
- Gutes Tageslicht ins Gesicht (nicht Fenster im Rücken!)
- 2–3 Min sprechen, abwechselnd:
  - 30 Sek lächeln und Skript-Text vorlesen
  - 30 Sek neutral, erklärend
  - 30 Sek leicht ernst (für Warn-Hinweise)
  - 30 Sek über etwas Persönliches erzählen (für Sprach-Vielfalt)
- Speichern – noch nicht hochladen, das kommt erst nach Phase-0-Entscheidung

### 10. Phase-0-Auswertung (10 Min)
Beantworte ehrlich:

- [ ] Stimme klingt wie ich? **Ja / Nein**
- [ ] Fachbegriffe verständlich ausgesprochen? **Ja / Nein**
- [ ] Lippensync ist akzeptabel? **Ja / Nein**
- [ ] Stock-Avatar wirkt natürlich genug, um daraus zu lernen? **Ja / Nein**

> **Wenn 3 von 4 = Ja:** Wir gehen in Phase 1 (Creator-Plans abschließen, eigener Avatar trainieren).
> **Wenn weniger als 3 = Ja:** Wir sprechen über Workarounds, bevor du Geld ausgibst.

---

## Nach Phase 0

Wenn alles passt:
1. HeyGen Creator-Plan abschließen ($29/Monat, monatlich nicht jährlich)
2. ElevenLabs Creator-Plan abschließen ($22/Monat)
3. Eigenes Avatar-Video (Schritt 9) bei HeyGen Studio Avatar hochladen
4. Professional Voice Clone bei ElevenLabs mit längerem Audio (30+ Min) trainieren
5. Ich baue parallel den Orchestrator und schreibe weitere Skripte

---

## Was du mich danach fragen kannst

- "Hier ist das MP3, klingt das gut?" → ich höre rein und gebe ehrliches Feedback
- "Lippensync hier ist 200ms versetzt – fixbar?" → ja, das kann an Audio-Encoding liegen
- "EBITDA klingt wie 'I bid Tee Da' – was tun?" → wir schreiben es phonetisch im Skript

Erst danach geht es ans Bezahlen.
