# -*- coding: utf-8 -*-
"""
DUB Kaeufer-Academy - Bewertungs-Template (Modul 3)
Erzeugt Downloads/Kaeufer/bewertungs-template.xlsx

Gegenstueck zum Verkaeufer-Template (Downloads/Verkaeufer/_build-bewertungs-template.py),
gleiche Mechanik und gleiches Layout, Inhalt aus Kaeufersicht.

Aufbau je Blatt:
  1 Zahlen des Zielunternehmens   -> EBITDA laut Jahresabschluss
  2 Bereinigungen pruefen         -> Bereinigtes EBITDA
  3 Gewichtung der Jahre          -> Bewertungsbasis
  4 Multiple-Szenarien            -> konservativ / realistisch / optimistisch
  5 Unternehmenswert              -> cash and debt free
  6 Preisbruecke                  -> dein Kaufpreisband
  7 Plausibilitaetspruefung
"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.pagebreak import Break

# ---------------------------------------------------------------- CI-Tokens
NAVY       = "0F2744"
ORANGE     = "EE7A1E"
ORANGE_LT  = "FDEBD8"
INK        = "1A1A1A"
GREY       = "666666"
GREY_LT    = "8A94A6"
LINE       = "E5E7EB"
PAPER      = "EEF1F5"
INPUT_BG   = "FFF8EF"
INPUT_FG   = "B35C0F"
WHITE      = "FFFFFF"
NAVY_TEXT  = "C7D0DE"

FONT = "Calibri"

EUR  = '#,##0 "€";[Red]-#,##0 "€"'
EURC = '#,##0 "€";[Red]-#,##0 "€";""'
PCT  = '0 %'
MUL  = '0.0"×"'
YR   = '0'


def f(sz=10.5, b=False, color=INK, italic=False):
    return Font(name=FONT, size=sz, bold=b, color=color, italic=italic)


def fill(c):
    return PatternFill("solid", fgColor=c)


def side(color=LINE, style="thin"):
    return Side(style=style, color=color)


LEFT   = Alignment(horizontal="left",   vertical="center", wrap_text=False)
LEFTW  = Alignment(horizontal="left",   vertical="top",    wrap_text=True)
RIGHT  = Alignment(horizontal="right",  vertical="center")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
LABELW = Alignment(horizontal="left",   vertical="center", wrap_text=True)

COLS    = ["C", "D", "E", "F"]       # die vier Jahresspalten
SZENCOL = ["D", "E", "F"]            # konservativ / realistisch / optimistisch
SZEN    = ["Konservativ", "Realistisch", "Optimistisch"]


# ---------------------------------------------------------------- Beispiel
# Die Zahlen sind so gewaehlt, dass sie die Beispielrechnung aus Modul 3
# exakt reproduzieren: bereinigtes EBITDA 200.000 €, Multiples 3/4/5,
# Unternehmenswert 600k/800k/1.000k, Kaufpreisband 550k-950k.
BEISPIEL = {
    "jahre":          [2024, 2025, 2026, 2027],
    "umsatz":         [1150000, 1240000, 1310000, 1390000],
    "gesamtleistung": [1160000, 1250000, 1320000, 1400000],
    "egt":            [105000, 162000, 166000, 190000],
    "finanzergebnis": [-8000, -7000, -6000, -5000],
    "afa":            [42000, 44000, 46000, 48000],
    "ber_gehalt":     [-20000, -20000, -20000, -20000],
    "ber_privat":     [12000, 12000, 12000, 12000],
    "ber_aufwand":    [18000, 0, 0, 0],
    "ber_ertrag":     [0, -15000, 0, 0],
    "ber_miete":      [0, 0, 0, 0],
    "ber_frei":       [0, 0, 0, 0],
    "multiples":      [3.0, 4.0, 5.0],
    "brueck_schulden": -100000,
    "brueck_cash":     50000,
    "brueck_wc":       0,
    "brueck_capex":    0,
}

LEER = {k: ([None] * 4 if isinstance(v, list) else None) for k, v in BEISPIEL.items()}
LEER["jahre"] = [2024, 2025, 2026, 2027]
LEER["multiples"] = [None] * 3


PRUEFPUNKTE = [
    ("Ertragskraft",
     "Oberes Szenario: Umsatz und bereinigtes Ergebnis sind über mehrere Jahre gestiegen, die Marge liegt über dem "
     "Branchenschnitt.   Unteres Szenario: Schwankende oder rückläufige Zahlen, Marge unter Branchenschnitt."),
    ("Inhaberabhängigkeit",
     "Oberes Szenario: Das Tagesgeschäft läuft ohne den Inhaber, Prozesse sind dokumentiert, Kunden hängen am Team.   "
     "Unteres Szenario: Fachwissen, Entscheidungen und Kundenkontakte liegen allein beim Inhaber."),
    ("Kundenstruktur",
     "Oberes Szenario: Viele Kunden, kein einzelner dominiert, wiederkehrende Erlöse aus Wartung oder Rahmenverträgen.   "
     "Unteres Szenario: Ein einzelner Kunde macht einen erheblichen Teil des Umsatzes aus."),
    ("Marktposition und Zukunftsaussichten",
     "Oberes Szenario: Wachsender Markt, erkennbares Alleinstellungsmerkmal, unterlegte Planung.   "
     "Unteres Szenario: Schrumpfender Markt, austauschbares Angebot, Planung ohne Auftragsbasis."),
    ("Belegbarkeit der Zahlen",
     "Oberes Szenario: Testierte oder vom Steuerberater erstellte Abschlüsse, Bereinigungen sind belegt.   "
     "Unteres Szenario: Nur BWA oder Angaben des Verkäufers, Bereinigungen ohne Nachweis."),
    ("Verträge und Ausstattung",
     "Oberes Szenario: Langfristige Kunden-, Liefer- und Mietverträge, gepflegte Maschinen und Software.   "
     "Unteres Szenario: Kurzfristig kündbare Verträge, Investitionsstau, ungeklärte Rechtsfragen."),
]


class Sheet:
    """Schreibt das Modell zeilenweise und merkt sich die Zeilennummern."""

    def __init__(self, ws, data, beispiel=False):
        self.ws = ws
        self.d = data
        self.beispiel = beispiel
        self.r = 1
        self.ref = {}

    # -- Bausteine ------------------------------------------------
    def row_h(self, h):
        self.ws.row_dimensions[self.r].height = h

    def band(self, h):
        for col in "ABCDEFG":
            self.ws[f"{col}{self.r}"].fill = fill(NAVY)
        self.row_h(h)
        self.r += 1

    def section(self, nr, titel):
        ws = self.ws
        self.row_h(7)
        self.r += 1
        ws.merge_cells(f"B{self.r}:F{self.r}")
        c = ws[f"B{self.r}"]
        c.value = f"  {nr}   {titel.upper()}"
        c.font = f(11, True, WHITE)
        c.alignment = LEFT
        for col in "BCDEF":
            ws[f"{col}{self.r}"].fill = fill(NAVY)
        ws[f"A{self.r}"].fill = fill(ORANGE)
        self.row_h(24)
        self.r += 1

    def note(self, text, color=GREY, size=9.5, height=None, italic=False):
        ws = self.ws
        ws.merge_cells(f"B{self.r}:F{self.r}")
        c = ws[f"B{self.r}"]
        c.value = text
        c.font = f(size, False, color, italic)
        c.alignment = LEFTW
        self.row_h(14)
        self.r += 1

    def input_row(self, label, key, fmt=EUR, indent=False, height=17):
        ws = self.ws
        c = ws[f"B{self.r}"]
        c.value = ("      " if indent else "") + label
        c.font = f(10.5)
        c.alignment = LABELW
        c.border = Border(bottom=side(LINE))
        vals = self.d.get(key) or [None] * 4
        for i, col in enumerate(COLS):
            cell = ws[f"{col}{self.r}"]
            cell.value = vals[i]
            cell.number_format = fmt
            cell.font = f(10.5, False, INPUT_FG)
            cell.fill = fill(INPUT_BG)
            cell.alignment = RIGHT
            cell.border = Border(bottom=side(LINE), left=side(WHITE, "thin"))
        self.row_h(height)
        row = self.r
        self.r += 1
        return row

    def calc_row(self, label, formula_tpl, fmt=EURC, accent=False, size=10.5, height=19):
        ws = self.ws
        bg = ORANGE_LT if accent else PAPER
        c = ws[f"B{self.r}"]
        c.value = label
        if isinstance(label, str) and label.startswith("="):
            c.data_type = "s"
        c.font = f(size, True, NAVY if accent else INK)
        c.alignment = LABELW
        c.fill = fill(bg)
        c.border = Border(top=side(NAVY if accent else GREY_LT), bottom=side(LINE))
        for col in COLS:
            cell = ws[f"{col}{self.r}"]
            cell.value = formula_tpl.format(c=col)
            cell.number_format = fmt
            cell.font = f(size, True, NAVY if accent else INK)
            cell.fill = fill(bg)
            cell.alignment = RIGHT
            cell.border = Border(top=side(NAVY if accent else GREY_LT), bottom=side(LINE))
        self.row_h(height)
        row = self.r
        self.r += 1
        return row

    def szen_heads(self):
        for col, h in zip(SZENCOL, SZEN):
            c = self.ws[f"{col}{self.r}"]
            c.value = h
            c.font = f(9.5, True, NAVY)
            c.alignment = CENTER
        self.row_h(18)
        self.r += 1

    def bruecke_row(self, label, key, hint=""):
        """Einzelwert der Preisbruecke: Label B:E, Betrag in F."""
        ws = self.ws
        ws.merge_cells(f"B{self.r}:E{self.r}")
        c = ws[f"B{self.r}"]
        c.value = label + ((": " + hint) if hint else "")
        c.font = f(10.5)
        c.alignment = LABELW
        for col in "BCDE":
            ws[f"{col}{self.r}"].border = Border(bottom=side(LINE))
        cell = ws[f"F{self.r}"]
        cell.value = self.d.get(key)
        cell.number_format = EUR
        cell.font = f(10.5, False, INPUT_FG)
        cell.fill = fill(INPUT_BG)
        cell.alignment = RIGHT
        cell.border = Border(bottom=side(LINE), left=side(WHITE, "thin"))
        row = self.r
        self.row_h(17)
        self.r += 1
        return row

    def spacer(self, h=8):
        self.row_h(h)
        self.r += 1

    # -- Abschnitte -----------------------------------------------
    def kopf(self):
        ws = self.ws
        self.band(6)
        ws[f"B{self.r}"] = "DUB  ·  KÄUFER-ACADEMY"
        ws[f"B{self.r}"].font = f(10, True, NAVY_TEXT)
        ws[f"B{self.r}"].alignment = LEFT
        ws.merge_cells(f"D{self.r}:F{self.r}")
        ws[f"D{self.r}"] = "MODUL 3 · BEWERTUNG UND PREISFINDUNG"
        ws[f"D{self.r}"].font = f(10, True, ORANGE)
        ws[f"D{self.r}"].alignment = RIGHT
        self.band(18)

        ws.merge_cells(f"B{self.r}:F{self.r}")
        ws[f"B{self.r}"] = "Bewertungs-Template" + ("  –  ausgefülltes Beispiel" if self.beispiel else "")
        ws[f"B{self.r}"].font = f(20, True, WHITE)
        ws[f"B{self.r}"].alignment = LEFT
        self.band(30)

        ws.merge_cells(f"B{self.r}:F{self.r}")
        ws[f"B{self.r}"] = "Bereinigtes EBITDA × Multiple = Unternehmenswert. Preisbrücke = dein Kaufpreisband."
        ws[f"B{self.r}"].font = f(11, False, NAVY_TEXT)
        ws[f"B{self.r}"].alignment = LEFT
        self.band(19)
        self.band(8)
        self.spacer(10)

    def anleitung(self):
        if self.beispiel:
            self.ws.merge_cells(f"B{self.r}:F{self.r}")
            c = self.ws[f"B{self.r}"]
            c.value = ("Dieses Blatt zeigt das Modell mit den Beispielzahlen aus Modul 3: bereinigtes EBITDA 200.000 €, "
                       "Multiples 3× / 4× / 5×, Kaufpreisband 550.000 – 950.000 €. Es dient nur der Veranschaulichung – "
                       "arbeite im Blatt „Bewertung“ mit den Zahlen deines Zielunternehmens.")
            c.font = f(10, False, NAVY)
            c.fill = fill(ORANGE_LT)
            c.alignment = LEFTW
            for col in "BCDEF":
                self.ws[f"{col}{self.r}"].fill = fill(ORANGE_LT)
            self.row_h(30)
            self.r += 1
            self.spacer(10)
            return

        self.section("▶", "So gehst du vor")
        for t in [
            "1.  Trage in Abschnitt 1 die Zahlen des Zielunternehmens ein – aus den Jahresabschlüssen oder aus dem "
            "Unternehmensexposé (IM). Was du dafür anfordern solltest, steht in Modul 4.",
            "2.  Prüfe in Abschnitt 2 die Bereinigungen. Der Verkäufer rechnet sie dir vor – deine Aufgabe ist, sie zu "
            "hinterfragen und belegen zu lassen.",
            "3.  Wähle in Abschnitt 4 drei Multiples: konservativ, realistisch und optimistisch. Branchenwerte findest "
            "du in den DUB KMU-Multiples auf www.dub.de.",
            "4.  Abschnitt 5 zeigt den Unternehmenswert, Abschnitt 6 rechnet ihn über die Preisbrücke in dein "
            "Kaufpreisband um. Abschnitt 7 hilft dir einzuordnen, welches Szenario realistisch ist.",
        ]:
            self.note(t, INK, 10, 15)
        self.note("Die orange hinterlegten Felder sind Eingabefelder. Alle übrigen Werte berechnen sich automatisch.",
                  GREY_LT, 9.5, 16, italic=True)
        self.spacer(10)

    def abschnitt_1(self):
        ws = self.ws
        self.section("1", "Zahlen des Zielunternehmens")
        self.note("Nimm die Zahlen aus den Jahresabschlüssen oder dem Unternehmensexposé. Fehlt dir das Folgejahr, "
                  "lass die Spalte leer – das Modell rechnet dann ohne sie weiter.", INK, 10, 15)
        heads = ["Zwei Jahre zurück\n(abgeschlossen)", "Letztes Jahr\n(abgeschlossen)",
                 "Laufendes Jahr\n(Hochrechnung)", "Folgejahr\n(Planung des Verkäufers)"]
        ws[f"B{self.r}"] = "Position · alle Beträge in Euro"
        ws[f"B{self.r}"].font = f(9.5, True, GREY)
        ws[f"B{self.r}"].alignment = Alignment(horizontal="left", vertical="bottom")
        for col, h in zip(COLS, heads):
            c = ws[f"{col}{self.r}"]
            c.value = h
            c.font = f(9, True, NAVY)
            c.alignment = Alignment(horizontal="center", vertical="bottom", wrap_text=True)
        self.row_h(30)
        self.r += 1

        self.ref["jahr"] = self.input_row("Geschäftsjahr", "jahre", YR)
        self.input_row("Umsatzerlöse", "umsatz")
        self.input_row("Gesamtleistung (Umsatz ± Bestandsveränderung + aktivierte Eigenleistungen)", "gesamtleistung")
        self.ref["gl"] = self.r - 1
        self.input_row("Ergebnis der gewöhnlichen Geschäftstätigkeit (EGT)", "egt")
        self.ref["egt"] = self.r - 1
        self.input_row("Finanzergebnis (Zinserträge − Zinsaufwendungen, meist negativ)", "finanzergebnis")
        self.ref["fe"] = self.r - 1
        self.input_row("Abschreibungen auf Sachanlagen und immaterielle Vermögensgegenstände", "afa")
        self.ref["afa"] = self.r - 1

        self.ref["ebitda"] = self.calc_row(
            "= EBITDA laut Jahresabschluss",
            "={{c}}{egt}-{{c}}{fe}+{{c}}{afa}".format(**self.ref))
        self.note("EBITDA = EGT abzüglich Finanzergebnis zuzüglich Abschreibungen. Weist die GuV kein EGT aus, "
                  "nimm stattdessen: Jahresüberschuss + Steuern vom Einkommen und Ertrag.", GREY_LT, 9.5, 15, italic=True)
        self.note("Das EBITDA blendet die Abschreibungen aus. Investiert das Unternehmen laufend in Maschinen, "
                  "Fahrzeuge oder Ausstattung, treffen dich diese Beträge nach der Übernahme trotzdem. Dafür gibt es "
                  "zwei Stellen im Modell: Was der Verkäufer aufgeschoben hat, trägst du in Abschnitt 6 als "
                  "Investitionsstau ein. Einen dauerhaft hohen Investitionsbedarf bildest du ab, indem du in "
                  "Abschnitt 4 ein vorsichtigeres Multiple wählst.", GREY, 9.5, 34)
        self.spacer(10)

    def abschnitt_2(self):
        self.ref["break2"] = self.r
        self.section("2", "Bereinigungen prüfen")
        self.note("Bei inhabergeführten Unternehmen spiegelt das EBITDA laut Jahresabschluss selten die Ertragskraft "
                  "nach der Übernahme. Trage die Bereinigungen ein, die der Verkäufer ansetzt: Alles, was das Ergebnis "
                  "erhöht, positiv – alles Mindernde mit Minuszeichen.", INK, 10, 28)
        start = self.r
        self.input_row("Inhabergehalt: Differenz zu einem marktüblichen Geschäftsführergehalt", "ber_gehalt", indent=True)
        self.input_row("Private Ausgaben über das Unternehmen (z. B. privat genutzter Firmenwagen)", "ber_privat", indent=True)
        self.input_row("Einmalige Aufwendungen (z. B. Rechtsstreit, Umzug, Abfindung)", "ber_aufwand", indent=True)
        self.input_row("Einmalige Erträge (z. B. Versicherungsleistung, Anlagenverkauf) – negativ eintragen", "ber_ertrag", indent=True)
        self.input_row("Miete an die Verkäuferseite: Differenz zur marktüblichen Miete", "ber_miete", indent=True)
        self.input_row("Weitere Bereinigung (frei)", "ber_frei", indent=True)
        ende = self.r - 1

        self.ref["summe_ber"] = self.calc_row(
            "= Summe Bereinigungen", "=SUM({{c}}{a}:{{c}}{b})".format(a=start, b=ende))
        self.ref["ber_ebitda"] = self.calc_row(
            "= BEREINIGTES EBITDA",
            "={{c}}{e}+{{c}}{s}".format(e=self.ref["ebitda"], s=self.ref["summe_ber"]),
            accent=True, size=12, height=24)
        self.calc_row("Bereinigte EBITDA-Marge (auf Gesamtleistung)",
                      '=IFERROR({{c}}{b}/{{c}}{g},"")'.format(b=self.ref["ber_ebitda"], g=self.ref["gl"]),
                      fmt=PCT, size=10, height=17)
        self.note("Lass dir jede Bereinigung belegen. Ein marktübliches Geschäftsführergehalt, das der Verkäufer "
                  "bisher nicht gezahlt hat, mindert das bereinigte EBITDA – auch wenn es in seiner Rechnung fehlt. "
                  "Bereinigungen ohne Nachweis gehören nicht ins Modell.", GREY_LT, 9.5, 28, italic=True)
        self.spacer(10)

    def abschnitt_3(self):
        ws = self.ws
        self.section("3", "Gewichtung der Jahre")
        self.note("Nicht jedes Jahr wiegt gleich schwer. Das letzte abgeschlossene und das laufende Jahr sagen am "
                  "meisten über die Ertragskraft aus, die du übernimmst. Die Planung des Verkäufers wiegt am "
                  "wenigsten, solange sie nicht mit Aufträgen unterlegt ist. Du kannst die Gewichtung anpassen, in "
                  "Summe muss sie 100 % ergeben.", INK, 10, 28)
        gew = [0.15, 0.35, 0.35, 0.15]
        c = ws[f"B{self.r}"]
        c.value = "Gewichtung"
        c.font = f(10.5)
        c.alignment = LABELW
        c.border = Border(bottom=side(LINE))
        for col, g in zip(COLS, gew):
            cell = ws[f"{col}{self.r}"]
            cell.value = g
            cell.number_format = PCT
            cell.font = f(10.5, True, INPUT_FG)
            cell.fill = fill(INPUT_BG)
            cell.alignment = RIGHT
            cell.border = Border(bottom=side(LINE), left=side(WHITE, "thin"))
        self.ref["gew"] = self.r
        self.row_h(19)
        self.r += 1

        ws.merge_cells(f"B{self.r}:F{self.r}")
        chk = ws[f"B{self.r}"]
        chk.value = ('=IF(SUM(C{g}:F{g})=1,"Gewichtung ergibt 100 % – passt.",'
                     '"Achtung: Die Gewichtung ergibt "&TEXT(SUM(C{g}:F{g}),"0 %")&". Bitte auf 100 % anpassen.")'
                     ).format(g=self.ref["gew"])
        chk.font = f(9.5, False, GREY_LT, True)
        chk.alignment = LEFTW
        self.row_h(15)
        self.r += 1
        self.spacer(4)

        ws.merge_cells(f"B{self.r}:D{self.r}")
        lab = ws[f"B{self.r}"]
        lab.value = "= GEWICHTETES BEREINIGTES EBITDA  ·  deine Bewertungsbasis"
        lab.data_type = "s"
        lab.font = f(12, True, NAVY)
        lab.alignment = LEFT
        ws.merge_cells(f"E{self.r}:F{self.r}")
        val = ws[f"E{self.r}"]
        val.value = "=SUMPRODUCT(C{b}:F{b},C{g}:F{g})".format(b=self.ref["ber_ebitda"], g=self.ref["gew"])
        val.number_format = EURC
        val.font = f(13, True, NAVY)
        val.alignment = RIGHT
        for col in "BCDEF":
            ws[f"{col}{self.r}"].fill = fill(ORANGE_LT)
            ws[f"{col}{self.r}"].border = Border(top=side(NAVY), bottom=side(NAVY))
        self.ref["basis"] = self.r
        self.row_h(26)
        self.r += 1
        self.spacer(10)

    def abschnitt_4(self):
        ws = self.ws
        self.ref["break4"] = self.r
        self.section("4", "Multiple-Szenarien")
        self.note("Rechne nicht mit einem Multiple, sondern mit dreien. Sieh dir dafür die KMU-Multiples für die "
                  "Branche des Zielunternehmens auf www.dub.de an – Multiples unterscheiden sich von Branche zu "
                  "Branche erheblich.", INK, 10, 15)
        self.note("Dort stehen EBITDA- und EBIT-Multiples nebeneinander. Multiple und Bezugsgröße müssen "
                  "zusammenpassen: Dieses Template rechnet mit dem bereinigten EBITDA, trage hier also den "
                  "EBITDA-Multiple ein. Der EBIT-Multiple ist immer der höhere von beiden – auf ein EBITDA "
                  "angewendet ergibt er einen zu hohen Unternehmenswert.", INK, 10, 28)
        self.note("Als grobe Orientierung, wenn dir für die Branche keine Werte vorliegen: hohe Inhaberabhängigkeit "
                  "2–3×, stabiles Unternehmen 3–5×, wachsend mit geringer Abhängigkeit 4–6×, starke Marke mit "
                  "wiederkehrenden Umsätzen 5–8×.", GREY, 9.5, 15)
        self.szen_heads()

        c = ws[f"B{self.r}"]
        c.value = "Multiple für die Branche des Zielunternehmens"
        c.font = f(10.5)
        c.alignment = LABELW
        c.border = Border(bottom=side(LINE))
        ws[f"C{self.r}"].border = Border(bottom=side(LINE))
        for col, v in zip(SZENCOL, self.d["multiples"]):
            cell = ws[f"{col}{self.r}"]
            cell.value = v
            cell.number_format = MUL
            cell.font = f(11, True, INPUT_FG)
            cell.fill = fill(INPUT_BG)
            cell.alignment = RIGHT
            cell.border = Border(bottom=side(LINE), left=side(WHITE, "thin"))
        self.ref["mult"] = self.r
        self.row_h(21)
        self.r += 1
        self.spacer(10)

    def abschnitt_5(self):
        ws = self.ws
        self.section("5", "Unternehmenswert")
        self.szen_heads()

        ws.merge_cells(f"B{self.r}:C{self.r}")
        c = ws[f"B{self.r}"]
        c.value = "UNTERNEHMENSWERT"
        c.font = f(13, True, WHITE)
        c.alignment = LEFT
        for col in SZENCOL:
            cell = ws[f"{col}{self.r}"]
            cell.value = "=$E${b}*{m}{r}".format(b=self.ref["basis"], m=col, r=self.ref["mult"])
            cell.number_format = EURC
            cell.font = f(13, True, WHITE)
            cell.alignment = RIGHT
        for col in "BCDEF":
            ws[f"{col}{self.r}"].fill = fill(NAVY)
        ws[f"A{self.r}"].fill = fill(ORANGE)
        self.ref["uw"] = self.r
        self.row_h(32)
        self.r += 1

        self.note("Das ist der Unternehmenswert, nicht der Kaufpreis. Er ist schulden- und liquiditätsfrei gerechnet "
                  "(im Fachjargon „cash and debt free“): Schulden, überschüssiges Bargeld, das im Tagesgeschäft "
                  "gebundene Kapital und ein Investitionsstau kommen erst über die Preisbrücke in Abschnitt 6 dazu "
                  "oder gehen ab.", GREY, 9.5, 28)
        self.note("Betriebsnotwendige Maschinen, Ausstattung und Warenbestand sind in diesem Wert bereits enthalten – "
                  "ohne sie gäbe es das Ergebnis nicht, auf dem er beruht. Schlägt der Verkäufer sie zusätzlich auf, "
                  "ist das doppelt gerechnet. Nur nicht betriebsnotwendige Werte, etwa eine vermietete Immobilie oder "
                  "ein ungenutztes Grundstück, dürfen separat hinzukommen.", GREY, 9.5, 34)
        self.spacer(10)

    def abschnitt_6(self):
        ws = self.ws
        self.ref["break6"] = self.r
        self.section("6", "Preisbrücke: vom Unternehmenswert zum Kaufpreis")
        self.note("Diese vier Positionen gelten für alle drei Szenarien. Das Vorzeichen steht jeweils dahinter. Die "
                  "Werte stammen aus der letzten Bilanz und werden zum Übergabetag final gemessen.", INK, 10, 15)
        self.note("Zum gebundenen Kapital, im Fachjargon Working Capital: In jedem Betrieb steckt Geld im Umlauf – "
                  "in offenen Kundenrechnungen und "
                  "im Warenlager, gegengerechnet mit dem, was der Betrieb selbst noch an Lieferanten schuldet. "
                  "Käufer und Verkäufer einigen sich auf einen Normalwert, meist den Durchschnitt der letzten zwölf "
                  "Monate. Liegt der Stand am Übergabetag darunter, weil der Verkäufer vorher das Lager abgebaut oder "
                  "Forderungen eingezogen hat, sinkt der Kaufpreis um die Differenz – liegt er darüber, steigt er.",
                  INK, 10, 34)

        ws[f"F{self.r}"] = "Betrag"
        ws[f"F{self.r}"].font = f(9.5, True, NAVY)
        ws[f"F{self.r}"].alignment = CENTER
        self.row_h(18)
        self.r += 1

        start = self.r
        self.bruecke_row("Finanzverbindlichkeiten", "brueck_schulden",
                         "Bankdarlehen, Gesellschafterdarlehen, Leasing (negativ eintragen)")
        self.bruecke_row("Überschüssiges Cash", "brueck_cash",
                         "Kassenbestand und Bankguthaben über dem betriebsnotwendigen Niveau (positiv eintragen)")
        self.bruecke_row("Im Tagesgeschäft gebundenes Kapital", "brueck_wc",
                         "Abweichung vom vereinbarten Normalwert (positiv oder negativ)")
        self.bruecke_row("Investitionsstau", "brueck_capex",
                         "Notwendige Investitionen, die der Verkäufer nicht getätigt hat (negativ eintragen)")
        ende = self.r - 1

        ws.merge_cells(f"B{self.r}:E{self.r}")
        c = ws[f"B{self.r}"]
        c.value = "= Summe Preisbrücke"
        c.data_type = "s"
        c.font = f(10.5, True, INK)
        c.alignment = LABELW
        cell = ws[f"F{self.r}"]
        cell.value = "=SUM(F{a}:F{b})".format(a=start, b=ende)
        cell.number_format = EURC
        cell.font = f(10.5, True, INK)
        cell.alignment = RIGHT
        for col in "BCDEF":
            ws[f"{col}{self.r}"].fill = fill(PAPER)
            ws[f"{col}{self.r}"].border = Border(top=side(GREY_LT), bottom=side(LINE))
        self.ref["bruecke"] = self.r
        self.row_h(19)
        self.r += 1
        self.spacer(8)

        self.szen_heads()
        ws.merge_cells(f"B{self.r}:C{self.r}")
        c = ws[f"B{self.r}"]
        c.value = "KAUFPREISBAND"
        c.font = f(13, True, WHITE)
        c.alignment = LEFT
        for col in SZENCOL:
            cell = ws[f"{col}{self.r}"]
            cell.value = '=IF({m}{u}="","",{m}{u}+$F${b})'.format(m=col, u=self.ref["uw"], b=self.ref["bruecke"])
            cell.number_format = EURC
            cell.font = f(13, True, WHITE)
            cell.alignment = RIGHT
        for col in "BCDEF":
            ws[f"{col}{self.r}"].fill = fill(NAVY)
        ws[f"A{self.r}"].fill = fill(ORANGE)
        self.row_h(32)
        self.r += 1

        self.note("Verhandle mit dieser Rechnung, nicht mit einer Zahl. „Der bereinigte EBITDA beträgt X, ein Multiple "
                  "von Y ist branchenüblich, abzüglich Schulden ergibt das Z“ überzeugt einen Verkäufer eher als ein "
                  "Gebot ohne Herleitung.", GREY, 9.5, 28)
        self.spacer(10)

    def abschnitt_7(self):
        ws = self.ws
        self.ref["break7"] = self.r
        self.section("7", "Welches Szenario ist realistisch?")
        ws.merge_cells(f"B{self.r}:F{self.r}")
        c = ws[f"B{self.r}"]
        c.value = ("Die drei Szenarien sind kein Verhandlungsspielraum, sondern eine Einschätzung. Ob dein "
                   "Zielunternehmen eher am unteren oder am oberen Rand liegt, entscheidet sich an den folgenden "
                   "Punkten. Prüfe sie, bevor du dich auf ein Szenario festlegst – und prüfe sie nach der Due "
                   "Diligence erneut.")
        c.font = f(11, True, NAVY)
        c.alignment = LEFTW
        for col in "BCDEF":
            ws[f"{col}{self.r}"].fill = fill(ORANGE_LT)
        self.row_h(46)
        self.r += 1
        self.spacer(6)

        for name, text in PRUEFPUNKTE:
            b = ws[f"B{self.r}"]
            b.value = name
            b.font = f(10, True, NAVY)
            b.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
            b.border = Border(top=side(LINE))
            ws.merge_cells(f"C{self.r}:F{self.r}")
            t = ws[f"C{self.r}"]
            t.value = text
            t.font = f(9.5, False, INK)
            t.alignment = LEFTW
            for col in "CDEF":
                ws[f"{col}{self.r}"].border = Border(top=side(LINE))
            self.row_h(30)
            self.r += 1
        self.spacer(6)
        self.note("Ein hoher Kaufpreis nützt nichts, wenn er nicht finanzierbar ist. Prüfe dein Kaufpreisband gegen "
                  "dein Eigenkapital, den möglichen Bankkredit und ein mögliches Verkäuferdarlehen – siehe Modul 7, "
                  "Akquisitionsfinanzierung.", GREY, 9.5, 28)
        self.spacer(10)

    def fuss(self):
        ws = self.ws
        ws.merge_cells(f"B{self.r}:F{self.r}")
        c = ws[f"B{self.r}"]
        c.value = ("Dieses Template dient der Orientierung und ersetzt keine Rechts-, Steuer- oder Finanzberatung.    "
                   "DUB · info@dub.de · www.dub.de    © 2026 Deutsche Unternehmerbörse DUB.de GmbH")
        c.font = f(9, False, GREY_LT)
        c.alignment = LEFTW
        for col in "BCDEF":
            ws[f"{col}{self.r}"].border = Border(top=side(LINE))
        self.row_h(24)
        self.r += 1

    def layout(self):
        ws = self.ws
        ws.sheet_view.showGridLines = False
        ws.sheet_properties.tabColor = NAVY
        widths = {"A": 2.2, "B": 74, "C": 16, "D": 16, "E": 16, "F": 16, "G": 2.2}
        for col, w in widths.items():
            ws.column_dimensions[col].width = w
        ws.page_setup.orientation = "landscape"
        ws.page_setup.paperSize = ws.PAPERSIZE_A4
        ws.page_setup.fitToWidth = 1
        ws.page_setup.fitToHeight = 0
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        ws.print_options.horizontalCentered = True
        ws.page_margins.left = ws.page_margins.right = 0.4
        ws.page_margins.top = ws.page_margins.bottom = 0.4

    def build(self):
        self.layout()
        self.kopf()
        self.anleitung()
        self.abschnitt_1()
        self.abschnitt_2()
        self.abschnitt_3()
        self.abschnitt_4()
        self.abschnitt_5()
        self.abschnitt_6()
        self.abschnitt_7()
        self.fuss()
        # Unternehmenswert/Preisbruecke und die Einordnung starten je auf neuer Seite,
        # damit kein Abschnitt vom Seitenfuss abgeschnitten wird
        self.ws.row_breaks.append(Break(id=self.ref["break2"]))
        self.ws.row_breaks.append(Break(id=self.ref["break4"]))
        self.ws.row_breaks.append(Break(id=self.ref["break6"]))
        self.ws.row_breaks.append(Break(id=self.ref["break7"]))


# ------------------------------------------------------------------ AutoFit
# Excel misst die noetigen Zeilenhoehen selbst. Verbundene Zellen ignoriert
# Excels AutoFit, deshalb wird ihr Text in eine Hilfsspalte gleicher Breite
# gespiegelt und die Zeile darueber gemessen.
AUTOFIT_PS = r"""
param([string]$Path)
$xl = New-Object -ComObject Excel.Application
$xl.Visible = $false; $xl.DisplayAlerts = $false
$wb = $xl.Workbooks.Open($Path)
$HELP = 26
foreach ($ws in $wb.Worksheets) {
    $used = $ws.UsedRange
    $last = $used.Row + $used.Rows.Count - 1
    $minH = @{}
    for ($r = 1; $r -le $last; $r++) { $minH[$r] = $ws.Rows.Item($r).RowHeight }
    for ($r = 1; $r -le $last; $r++) {
        $text = $null; $fromCol = 0; $span = 0
        for ($c = 2; $c -le 6; $c++) {
            $cell = $ws.Cells.Item($r, $c)
            if ($cell.MergeCells -and $cell.WrapText) {
                $ma = $cell.MergeArea
                if ($ma.Rows.Count -eq 1 -and $ma.Row -eq $r) {
                    $tl = $ws.Cells.Item($r, $ma.Column)
                    if ($tl.Value2 -is [string] -and $tl.Value2.Length -gt 0) {
                        $text = $tl.Value2; $fromCol = $ma.Column; $span = $ma.Columns.Count
                    }
                }
                break
            }
        }
        if ($null -ne $text) {
            $w = 0
            for ($k = 0; $k -lt $span; $k++) { $w += $ws.Columns.Item($fromCol + $k).ColumnWidth }
            $h = $ws.Cells.Item($r, $fromCol)
            $ws.Columns.Item($HELP).ColumnWidth = $w
            $probe = $ws.Cells.Item($r, $HELP)
            $probe.Font.Name = $h.Font.Name; $probe.Font.Size = $h.Font.Size
            $probe.Font.Bold = $h.Font.Bold; $probe.WrapText = $true
            $probe.Value2 = $text
        }
        $fit = ($null -ne $text)
        if (-not $fit) {
            for ($c = 2; $c -le 6; $c++) {
                $cell = $ws.Cells.Item($r, $c)
                if ((-not $cell.MergeCells) -and $cell.WrapText -and $null -ne $cell.Value2) { $fit = $true; break }
            }
        }
        if ($fit) {
            $ws.Rows.Item($r).AutoFit() | Out-Null
            $ws.Rows.Item($r).RowHeight = [Math]::Max($ws.Rows.Item($r).RowHeight + 3, $minH[$r])
            if ($null -ne $text) { $ws.Cells.Item($r, $HELP).Clear() | Out-Null }
        }
    }
    $ws.Columns.Item($HELP).ColumnWidth = 8.43
}
$wb.Worksheets.Item(1).Activate()
$wb.Save(); $wb.Close($true); $xl.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($xl) | Out-Null
"""


def autofit(path):
    """Zeilenhoehen von Excel messen lassen (nur Windows mit installiertem Excel)."""
    import subprocess, tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".ps1", delete=False, encoding="utf-8") as fh:
        fh.write(AUTOFIT_PS)
        script = fh.name
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass",
                            "-File", script, "-Path", os.path.abspath(path)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print("AutoFit uebersprungen (kein Excel?):", (r.stderr or "").strip()[:200])
        else:
            print("Zeilenhoehen von Excel gemessen.")
    finally:
        os.unlink(script)


def main():
    wb = Workbook()
    ws1 = wb.active
    ws1.title = "Bewertung"
    Sheet(ws1, LEER, beispiel=False).build()

    ws2 = wb.create_sheet("Beispiel")
    Sheet(ws2, BEISPIEL, beispiel=True).build()
    ws2.sheet_properties.tabColor = ORANGE

    wb.properties.title = "DUB Bewertungs-Template"
    wb.properties.creator = "Deutsche Unternehmerbörse DUB.de GmbH"
    wb.properties.description = "Käufer-Academy, Modul 3: Bewertung und Preisfindung"

    out = os.path.join("Downloads", "Kaeufer", "bewertungs-template.xlsx")
    wb.save(out)
    print("geschrieben:", out)
    autofit(out)


if __name__ == "__main__":
    main()
