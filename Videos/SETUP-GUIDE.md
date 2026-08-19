# Setup-Guide: HeyGen + ElevenLabs + Remotion

Schritt-für-Schritt-Anleitung, um in ca. 1–2 Stunden produktionsbereit zu sein. Stand Mai 2026.

## Strategie: MVP zuerst, API später

Erstmal die **Web-UIs** der drei Tools nutzen (kein API-Zugang nötig). Damit kannst du in einer Stunde dein erstes Video produzieren. Die API-Pipeline (Claude Code als Orchestrator) bauen wir erst, wenn der manuelle Workflow funktioniert – das spart Geld und Frust.

**MVP-Kosten:** HeyGen Creator $24/Monat (jährlich) + ElevenLabs Creator $22/Monat = **ca. 46 USD/Monat**. Remotion ist kostenlos.

---

## 1. ElevenLabs (Stimme klonen) – ZUERST machen

Reihenfolge-Begründung: Du brauchst die geklonte Stimme als Audio-Datei, bevor du in HeyGen ein Video damit erzeugst.

### 1.1 Account anlegen

1. Öffne https://elevenlabs.io/sign-up
2. Sign-up mit Google oder Email
3. Sprache wählen: **English** (das Tool-UI ist auf Englisch, der Voice-Clone funktioniert trotzdem für Deutsch)

### 1.2 Plan wählen

1. Klick auf **My Plan** (oben rechts)
2. Wähle **Creator** ($22/Monat oder $198/Jahr = $16,50/Monat)
   - Beinhaltet: 100.000 Credits/Monat (ca. 100 Min Sprache), Professional Voice Cloning, kommerzielle Nutzung
3. Zahlmethode hinterlegen, abschließen

> **Warum nicht Starter ($5)?** Der hat nur "Instant Voice Cloning" – das klingt für 30 Sek nett, wird aber bei längeren Lehrvideos blechern und inkonsistent. Creator-Plan = "Professional Voice Cloning" = echte Studio-Qualität.

### 1.3 Voice Sample aufnehmen

**Anforderungen:**
- 30 Min sauberes Audio (mehr ist besser, max. 3h)
- Ruhiger Raum, kein Hall, kein Echo
- Konstante Lautstärke, normale Sprechgeschwindigkeit
- WAV oder MP3, 44,1 kHz oder höher

**Aufnahme-Quickstart:**
- iPhone: App "Voice Memos" reicht für den Anfang, aber Headset/USB-Mic ist besser
- Mac: QuickTime → File → New Audio Recording
- Windows: Audacity (kostenlos, https://www.audacityteam.org/)

**Was sprechen?**
- Lies das fertige Skript [video-skript-modul-01-suchstrategie.md](video-skript-modul-01-suchstrategie.md) komplett vor – das gibt dir gleich 6–7 Min direkt brauchbares Material
- Sprich zusätzlich einen freien Abschnitt (5 Min), erzähle z.B. wie dein Tag war – das gibt der KI mehr Sprachvarianz

### 1.4 Voice Clone trainieren

1. ElevenLabs Dashboard → **Voices** (linke Sidebar) → **Add a New Voice**
2. Wähle **Professional Voice Clone**
3. Audio-Dateien hochladen
4. Name: z.B. "Graig DE"
5. Labels: Language = German, Accent = German, Description = "M&A-Lehrvideo-Sprecher"
6. **Submit** → Training dauert 2–4 Stunden, du wirst per Email benachrichtigt

### 1.5 Erstes Voiceover generieren

1. Nach Training: Dashboard → **Voices** → deine Stimme → **Use voice**
2. **Text-to-Speech** öffnet sich
3. Modell wählen: **eleven_multilingual_v2** (das ist das Modell mit bester Deutsch-Unterstützung)
4. Settings:
   - **Stability**: 50% (mittlerer Wert = lebendig aber konsistent)
   - **Similarity**: 75% (hoch, damit es nach dir klingt)
   - **Style Exaggeration**: 0% (für Lehrvideos neutral)
5. Skript einfügen → **Generate** → MP3 downloaden

### 1.6 API-Key holen (für später)

1. Profil-Icon oben rechts → **Profile + API key**
2. **Create API Key** → kopieren, in `.env` speichern als `ELEVENLABS_API_KEY=...`

---

## 2. HeyGen (Avatar + Video) – DANACH

### 2.1 Account anlegen

1. Öffne https://www.heygen.com/signup
2. Sign-up mit Google oder Email
3. Email bestätigen

### 2.2 Plan wählen

1. https://www.heygen.com/pricing
2. **Creator-Plan**: $29/Monat oder $24/Monat (jährlich = $288/Jahr)
   - Beinhaltet: 15 Min Video/Monat, alle Avatar-Versionen inkl. Avatar IV (neuestes Modell, ehemals Avatar 5 benannt im Marketing), HD-Export, kommerzielle Nutzung, kein Wasserzeichen
3. Subscription abschließen

> **Wichtig zu wissen:** Die API ist eine **separate** Subscription (pay-as-you-go ab $5 Guthaben, ca. $1 pro Minute 1080p Video, Avatar IV $4/Min). Wir brauchen die API jetzt **nicht** – die Web-UI reicht für den MVP.

### 2.3 Eigenen Avatar erstellen (zwei Optionen)

#### Option A: Instant Avatar (schnell, weniger Qualität)
1. Dashboard → **Create Avatar** → **Instant Avatar**
2. Webcam-Aufnahme: 2 Min nach Anleitung (frontal, gut beleuchtet, verschiedene Mimiken)
3. Verarbeitung: ca. 15 Min

#### Option B: Studio Avatar (höchste Qualität, Avatar IV/5) – **empfohlen**
1. Dashboard → **Create Avatar** → **Studio Avatar**
2. Anleitung folgen: 5–10 Min sauberes Video aufnehmen
   - 4K wenn möglich (iPhone 11+, Sony, Canon)
   - Studio-Licht oder gleichmäßiges Tageslicht
   - Hintergrund: einfarbig oder dezent
   - Verschiedene Sätze in normaler Sprechgeschwindigkeit
3. Upload → Verarbeitung: 24–48 Stunden
4. Consent-Formular ausfüllen (HeyGen muss bestätigt sehen, dass du Inhaber des Gesichts bist)

> **Alternative:** Wenn du keinen eigenen Avatar willst, gibt es **Stock-Avatare** im Marketplace. Aber: DUB-Lehrvideos wirken authentischer mit einem echten "Gesicht" der Firma.

### 2.4 Voice in HeyGen einbinden

HeyGen bietet zwei Wege, die ElevenLabs-Stimme zu nutzen:

#### Weg 1: ElevenLabs-Audio als Datei hochladen
1. Im Video-Editor: **Add Audio** → MP3 aus ElevenLabs hochladen
2. Avatar wird per "Talking Photo" auf das Audio gelippt
3. **Vorteil:** Full control über Stimme, Nuancen, Pausen
4. **Nachteil:** Mehr manuelle Schritte

#### Weg 2: ElevenLabs als Voice-Provider verknüpfen (Premium)
1. HeyGen Settings → **Integrations** → **ElevenLabs**
2. ElevenLabs API-Key einfügen
3. Stimmen aus ElevenLabs werden direkt im HeyGen Voice-Dropdown angeboten
4. **Vorteil:** Ein Tool-UI statt zwei

Für den ersten Test: **Weg 1** ist robuster.

### 2.5 Erstes Avatar-Video erzeugen

1. Dashboard → **Create Video** → **Avatar Video**
2. Avatar auswählen (deiner)
3. Voice: **Upload Audio** → MP3 aus ElevenLabs
4. Hintergrund: einfarbig (z.B. DUB-Schwarz #1A1A1A) oder Greenscreen für späteren Schnitt
5. **Generate** → 5–15 Min
6. Download als MP4 (1080p, MP4-H264)

### 2.6 API-Key holen (für später, **optional**)

1. https://app.heygen.com/settings → **API**
2. **Pay-as-you-go-Subscription** abschließen (separat von Creator-Plan!)
3. API-Key erzeugen, in `.env` als `HEYGEN_API_KEY=...`

---

## 3. Remotion (Schnitt + Motion Graphics) – LOKAL

### 3.1 Voraussetzungen prüfen

```powershell
node --version  # muss >= 20 LTS sein (du brauchst min. 16, empfohlen 20)
npm --version
```

Falls Node fehlt: https://nodejs.org/ → LTS-Version installieren.

### 3.2 Remotion-Projekt anlegen

Im Projektordner:

```powershell
cd "c:/Users/GraigGröbli/OneDrive - DealCircle GmbH/Misc/Dokumente/Enablement VS Project/Videos"
npx create-video@latest --yes --blank amber-videos
cd amber-videos
npm install
```

### 3.3 Remotion Studio starten

```powershell
npm run dev
```

Browser öffnet `http://localhost:3000` → Remotion Studio läuft.

### 3.4 Erste Composition anlegen

Im Studio:
1. Sidebar links → **Compositions**
2. Neue Komposition: Name `amber-modul-01`, 1920x1080, 30 fps
3. In `src/Composition.tsx`: DUB-Branding einbauen (Logo, Bauchbinde, Outro-Card)
4. HeyGen-Video als `<Video>` einbetten
5. Preview: Spacebar = Play

### 3.5 Render zu MP4

```powershell
npx remotion render amber-modul-01 out/amber-modul-01.mp4
```

Render dauert je nach Länge 2–10 Min auf einem normalen Laptop.

### 3.6 Optional: Remotion Pro / Lambda

Wenn die Render-Zeiten lokal zu lang werden:
- **Remotion Lambda**: Cloud-Rendering via AWS, parallelisiert (10x schneller)
- Setup: https://www.remotion.dev/docs/lambda

Brauchst du jetzt **nicht** – lokal reicht für 9 Module locker.

### 3.7 Kein Account nötig

Remotion ist Open-Source (Apache 2.0). Lizenz für kommerzielle Nutzung kommt erst ab >3 Mitarbeitern in der Firma (https://www.remotion.dev/license). Bei dir = klar OK ohne Lizenz.

---

## Nach dem Setup: Smoke-Test

Wenn alle drei Tools laufen, **mach einen Smoke-Test** mit nur 30 Sekunden:

1. Nimm die ersten 3 Sätze aus Modul 1 (Intro-Block)
2. ElevenLabs → 20 Sek MP3
3. HeyGen → 20 Sek Avatar-Video
4. Remotion → kurzes Intro mit DUB-Logo + Avatar + Outro

So findest du in 20 Minuten alle Stolpersteine, bevor du das ganze 7-Minuten-Modul produzierst.

---

## Häufige Stolpersteine

| Problem | Lösung |
|---|---|
| ElevenLabs Stimme klingt zu monoton | Stability runter (auf 30–40%) |
| ElevenLabs sagt englische Wörter mit englischem Akzent | Im Skript ausschreiben: "Em und A" statt "M&A" |
| HeyGen Avatar wirkt steif | Studio Avatar (Option B) statt Instant Avatar nutzen |
| HeyGen Lippensync passt nicht | Avatar IV / V Modell wählen (Creator-Plan) |
| Remotion `npm install` Fehler | Node 20+ statt 16 nutzen |
| Render-Audio synchron, aber Bild abgehackt | `--concurrency=1` im Render-Befehl probieren |

---

## Quellen

- HeyGen Pricing: https://www.heygen.com/pricing
- HeyGen API Pricing: https://www.heygen.com/api-pricing
- ElevenLabs Pricing: https://elevenlabs.io/pricing
- ElevenLabs Voice Cloning Guide: https://elevenlabs.io/docs/product-guides/voices/voice-cloning
- Remotion Docs: https://www.remotion.dev/docs/
- Remotion License: https://www.remotion.dev/license
