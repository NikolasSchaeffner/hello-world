# Wave 2 / Agent 05 — Business Analyst Report

**Konfidenz: 72%**

Begründung der Lücken: Kein direkter Zugriff auf das Original-PDF und die zugrundeliegenden Excel-Modelle. Gearbeitet wird ausschliesslich mit dem strukturierten Datenauszug. Keine Founder-Q&A, keine Peer-Reviews (isolierter Auftrag). Branchen-Benchmarks zu Gambling-CAC/Churn stammen aus Wissensstand bis August 2025, nicht aus aktuellem Marktreport. Die drei grossen Fragezeichen (Korrektheit der P&L-Detailzahlen, Marketing-Budget-Breakdown, Steuer-Substanz-Dokumentation) sind nicht auflösbar ohne Primärquellen.

---

## 1. Interne Konsistenz P&L (€3,1M vs. €9,52M Widerspruch)

**Befund: Kritischer Fehler — die beiden Zahlen schliessen sich gegenseitig aus.**

Die P&L-Tabelle zeigt 2031: Rake €7,49M + Tournament+Premium €2,03M = **€9,52M Total Revenue**. Das Mittelszenario-Statement behauptet dagegen **€3,1M Revenue J5** bei 80k MAU.

Reverse-Engineering der €3,1M Variante:
- €3,1M / 80.000 MAU = **€38,75 ARPU pro Jahr** — das ist ein Drittel des behaupteten ARPU von €186.
- Alternativ: €3,1M / €119 ARPU = **26.050 MAU** — das entspricht 2029, nicht 2031.

Reverse-Engineering der P&L-Tabelle:
- €9,52M / 80.000 MAU = **€119 ARPU** (Jahresbasis 2031). Aber Unit Economics behaupten €186 ARPU für J5. Das ist ein dritter Widerspruch.

Zusammenfassung der P&L-Inkonsistenzen:
1. Mittelszenario-Narrativ (€3,1M) vs. P&L-Tabelle (€9,52M) = Faktor 3,1
2. P&L-Tabelle ARPU implizit (€119) vs. Unit Economics ARPU behauptet (€186) = Faktor 1,56
3. EBITDA-Marge in Unit Economics ("~34% in J5") vs. P&L impliziert €6,30M / €9,52M = **66% EBITDA-Marge** in 2031 — ein Faktor 2 Überschätzung der Profitabilität oder Unterbewertung der Kostenbasis.

Wahrscheinlichste Erklärung: Das Mittelszenario-Statement und die P&L-Tabelle stammen aus verschiedenen Modell-Versionen und wurden nicht synchronisiert. Die P&L-Tabelle scheint näher am "Optimistischen Szenario" zu liegen (180k MAU, €8,2M Revenue), aber mit 80k MAU gelabelt. Das macht das gesamte 5-Jahres-Modell nicht verwertbar ohne Neuaufbau.

---

## 2. MAU-Wachstum-Realismus

**Befund: Wachstumsziel erreichbar, aber Budget-Lücke ist existenzkritisch.**

Wachstumspfad: 4k → 18k → 38k → 58k → 80k MAU. Das entspricht:
- 2027 → 2028: +14.000 neue aktive User (netto)
- 2028 → 2029: +20.000 netto
- 2029 → 2030: +20.000 netto
- 2030 → 2031: +22.000 netto

Bei 8% monatlichem Churn = 63% Jahres-Churn. Um 80.000 MAU stationär zu halten, müssen jährlich **50.400 Gross-Acquisitions** erfolgen — also 4.200 pro Monat nur für Churn-Replacement. Dazu kommt das Wachstum.

Kumulative Gross-Acquisition-Berechnung (vereinfacht, Churn-Replacement eingerechnet):

| Jahr | Benötigte Gross Akquis. | CAC | CAC-Kosten |
|---|---|---|---|
| 2028 | ~25.000 | €33 | €825k |
| 2029 | ~42.000 | ~€30 | €1,26M |
| 2030 | ~50.000 | ~€28 | €1,40M |
| 2031 | ~55.000 | €27 | €1,49M |
| **Kumulativ 2028–2031** | | | **~€4,97M** |

Das Marketing-Budget in der Kostenplanung ist nicht explizit ausgewiesen, aber der Gesamt-Kostenpfad (€1,05M → €3,22M) lässt bei üblichen Kostenstruktur-Splits (25–30% Marketing) nur €262k–€966k Marketing-Budget in 2028–2031 zu — drastisch unter den berechneten €4,97M Akquisitionskosten. Das Startkapital allokiert €35k Marketing für Phase 1, was 833 Ersterakquisitionen zu €42 CAC deckt. Das liegt Faktor 60–100 unter dem kumulierten Bedarf.

Dies ist der grösste quantifizierbare Finanzierungsfehler im Plan.

---

## 3. ARPU/Rake-Kalibrierung

**Befund: Rake-Mechanismus intern inkonsistent, behaupteter ARPU nicht erreichbar mit Lucra-Benchmark.**

Berechnungsweg Lucra-Basis:
- Ø Wettbetrag: $10
- Rake 3–10%, nehmen wir 6,5% Mitte: $0,65 Rake pro Match
- Ziel-ARPU 2031: €119 (aus P&L-Tabelle) oder €186 (Unit Economics)
- Benötigte Matches bei €119 ARPU: €119 / €0,65 / 12 Monate = **15,3 Matches pro User pro Monat**
- Benötigte Matches bei €186 ARPU: **23,8 Matches pro User pro Monat**

In P2P-Skill-Gaming-Plattformen (Lucra, Skillz) liegen **Median-User bei 2–5 Matches pro Monat**. Die Top-Quintile (20%) spielen 15–25 Matches. Das bedeutet: Der ARPU-Durchschnitt ist getrieben von Power-Usern und impliziert eine starke Power-Law-Verteilung.

Wenn Top-20% der User 80% des Revenue tragen, dann entspricht der "durchschnittliche" Revenue-Beitrag bei 80.000 MAU realistisch etwa:
- 16.000 Power-User × €600 ARPU = €9,6M Revenue (= P&L-Tabelle!)
- 64.000 Casual-User × €0 effektiv

Das heisst: Die €9,52M aus der Tabelle sind *erreichbar* — aber nur wenn 16.000 hochaktive Spieler im Modell existieren. Die Darstellung mit "Ø-ARPU €186" über alle 80k User ist methodisch falsch und irreführend.

---

## 4. CAC-Plausibilität in Gambling-Vertical

**Befund: CAC-Ausgangswert plausibel, Absinken auf €27 in J5 widerspricht Marktdynamik.**

€42 CAC für Esports/P2P-Gaming-Plattformen im 2027-Launch ist am unteren Ende aber vertretbar für:
- Organisches Community-Marketing über Twitch/Discord
- K-Faktor 2,0 (virales Wachstum) reduziert effektiven Paid-CAC erheblich

K-Faktor 2,0 bedeutet: 1 User akquiriert 2 weitere. Wenn dieser K-Faktor tatsächlich greift, dann halbiert er die bezahlten Akquisitionskosten — €42 effektiver CAC bei €84 paid CAC ist möglich. K=2,0 ist jedoch ein **aggressiver Wert**, den nur wenige Plattformen (WhatsApp, Clubhouse early stage) nachhaltig erreichen. Lucra selbst bestätigt diesen Wert — aber für eine unbekannte neue Plattform ohne etablierter Community ist das eine frühe Benchmark-Übernahme ohne Validierung.

CAC von €42 → €27 (−36%) über 5 Jahre:

In Gambling/Esports-Verticals gilt empirisch das Gegenteil:
- Google Ads/Meta CPMs in Gambling-Keywords sind 2023–2025 um 40–80% gestiegen (iGaming-Sektor)
- Apple ATT (App-Tracking Transparency) erhöht Mobile-CAC strukturell
- Bei wachsender Plattformgrösse steigen CACs weil die "easy" demografischen Segmente zuerst ausgeschöpft werden
- Nur bei starkem organischen Anteil (SEO, Word-of-Mouth, K>1,5 nachhaltig) wäre ein CAC-Rückgang denkbar

Der Plan setzt sinkenden CAC voraus und steigert gleichzeitig den Marketing-Spend — das ist widersprüchlich zur Marktdynamik. Realistisch wäre CAC-Stabilisierung bei €35–45 oder leichter Anstieg auf €50–60 in gesättigten Kampagnenphasen.

---

## 5. LTV-Berechnungsmethode (Average vs. Power-Law)

**Befund: Methodischer Grundfehler — Average-LTV überschätzt Planbarkeit und Profitabilität.**

LTV J5 = €279. Berechnung implizit: ARPU €186 / Churn 5% monatlich = **€186 / 0,60 (einjährige Verweildauer)** oder klassisch **ARPU × (1/monthly_churn) = €186 × (1/0,05) = €3.720**. Welche Methode liegt zugrunde, ist nicht dokumentiert.

Das Kernproblem: **Gambling-Revenue ist power-law-verteilt.**

Branchenbeobachtung aus iGaming/Skillz-Kontext:
- Top 5% der User generieren 60–80% des Revenue
- Bottom 50% der User generieren <5% des Revenue (spielen wenige Runden, churnen früh)

Wenn das LTV-Modell einen simplen ARPU-Durchschnitt verwendet, dann:
- Ist der Durchschnitt massiv von Power-Usern nach oben gezogen
- Der Median-LTV (für die "typische" Akquisition) liegt deutlich darunter
- Marketing-Kanäle, die überwiegend Casual-User akquirieren (z.B. Broad Social Media), liefern LTVs von €30–60, nicht €279
- CAC €42 × LTV €50 Median = LTV:CAC von 1,2x — deutlich unter dem als positiv geltenden 3:1

Die LTV:CAC-Ratio von 4,1x → 10,3x in Unit Economics basiert wahrscheinlich auf Power-User-Segmenten, nicht auf der Gesamtpopulation. Das ist analytisch zulässig als Segment-Steuerungsgrösse, aber **nicht als Fundament für Gesamt-P&L-Projektionen über 80.000 MAU**.

---

## 6. Churn-Realismus in Gambling/Esports

**Befund: Churn-Annahmen systematisch optimistisch um Faktor 1,5–2x.**

Umrechnung:
- 8% monatlich = 1 − (1 − 0,08)^12 = **63% Jahres-Churn** in J1
- 5% monatlich = 1 − (1 − 0,05)^12 = **46% Jahres-Churn** in J5

Branchen-Benchmarks für Gambling/Social Gaming Apps:
- Casual Mobile Games: 70–80% Jahres-Churn (gut etabliert, App-Store-Daten)
- Real-Money Gambling Apps: 75–90% Jahres-Churn (UK Gambling Commission, 2022–2024 Reports)
- P2P-Skill-Gaming (Lucra-ähnlich, spezifisch): keine öffentlichen Daten; schätzungsweise 60–75% Jahres-Churn in etablierter Phase

Der Plan behauptet 46% Jahres-Churn in J5 — das entspräche einer Retention, die besser als Netflix (15–20% Jahres-Churn) und vergleichbar mit Spotify ist. Das ist für eine Gambling-App unrealistisch ohne ausserordentliche Retention-Mechanismen (Turnier-Ligen, Soziales Netzwerk, Achievement-System), die im Konzept nicht detailliert beschrieben sind.

Ein realistischer Churn-Pfad wäre:
- J1: 10–12% monatlich (70–76% jährlich)
- J3: 8–9% monatlich (64–67% jährlich)
- J5: 6–7% monatlich (51–57% jährlich) — unter der Voraussetzung gelebter Retention-Features

---

## 7. Break-Even Timing & Cash-Burn

**Befund: Runway reicht mathematisch nicht — Series A ist keine Option, sondern Überlebensbedingung.**

Startkapital-Verwendung laut Plan:
- €30k Recht/Gründung + €35k MGA-Lizenz + €55k Tech-MVP + €35k Marketing + €10k Steuer/IP + €20k Betrieb + €15k Reserve = **€200k ausgegeben vor H2 2027**

Cash-Balance vor H2 2027: **€0** (±€15k Reserve).

H2 2027 EBITDA: **−€148k**. Dies setzt voraus, dass Revenue im H2 2027 €129k beträgt — also laufende Einnahmen bereits in Betrieb. Aber nach Verbrauch aller Mittel für Phase-1-Costs bleibt keine Cash-Reserve für die Betriebskosten von H2 2027.

Konkret: €278k Gesamtkosten 2027 − €129k Revenue = €149k Cash-Bedarf in H2 2027. Startkapital = €200k − (Aufbaukosten für H1 2027) = Null. Das Modell hat keine Gap-Finanzierung zwischen Phase-1-Ausschöpfung und dem Cashflow-Positivpunkt.

Series-A-Zeitplan: Q1 2027 — das bedeutet vor MGA-Lizenz-Abschluss, vor Public Launch, bei 0–5.000 MAU (Beta-Phase). Das ist strukturell notwendig, aber:
- Investoren sehen kein Revenue
- Keine valide MGA-Lizenz (noch in Beantragung)
- Kein bewiesenes Retention-Modell

Ohne Series A in Q1 2027 ist das Unternehmen in Q3 2027 zahlungsunfähig. **Das ist kein Risiko — das ist ein inhärenter Plan-Pfad.**

---

## 8. Series A bei 5.000 MAU pre-Launch — Realismus

**Befund: Zeitpunkt und Bewertungslogik sind beide problematisch.**

Ziel: €800k–1,5M bei €4–8M Valuation, begründet mit "5× Revenue-Multiple".

Problem 1 — Bewertungsmethodik:
Bei €0–50k Run-Rate Revenue in Q1 2027 ergibt 5× Revenue-Multiple = **€250k Valuation**, nicht €4–8M. Die €4–8M sind eine *team- und marktbasierte Frühphasen-Bewertung*, die üblicherweise mit "Comparable Transactions" oder "DCF auf Mittelszenario" begründet wird — nicht mit Revenue-Multiple auf Near-Zero-Revenue. Das Dokument nennt die falsche Methode für seine eigene Bewertung.

Problem 2 — Investoren-Präferenz in Gambling:
Gambling-/iGaming-Startups haben strukturell schwierigere Fundraising-Bedingungen als FinTech oder SaaS wegen:
- Regulatorischer Unsicherheit (besonders UK post-2023 Gambling Reform)
- ESG-Filtern bei institutionellen Fonds
- Noch fehlender MGA-Lizenz als harter Gate-Keeper

Bei 5.000 MAU (Beta), ohne Lizenz, ohne UK-Footprint, ist eine €4–8M Valuation **möglich bei Angel/Family-Office-Investoren** mit Nischenkenntnis, aber **unwahrscheinlich bei VC-Fonds** ohne Lead-Investor mit iGaming-Track-Record.

Der Plan behandelt Series A als sicheres Ereignis ("Ziel Q1 2027"). Es ist ein existenziell notwendiges Ereignis, das von externen Parteien abhängt.

---

## 9. Top-3 finanzielle Schwachstellen

**Schwachstelle 1 — P&L-Modell ist intern inkohärent und nicht investitions-ready.**

Der 3-fache Widerspruch (€3,1M vs. €9,52M Revenue J5, ARPU €119 vs. €186, EBITDA-Marge 34% vs. implizit 66%) macht das Finanzmodell als Entscheidungsgrundlage unbrauchbar.

**Schwachstelle 2 — Marketing-Budget ist um Faktor 10–50 unterfinanziert.**

Kumulative CAC-Kosten 2028–2031 betragen schätzungsweise €4,97M. Die gesamte Kostenbasis 2028–2031 beträgt €1,05M + €1,57M + €2,34M + €3,22M = €8,18M, wovon Marketing bei typischer Kostenstruktur maximal €2–2,5M ausmacht. Das Defizit liegt bei €2,5–3M — also eine komplette zusätzliche Finanzierungsrunde, die im Plan nicht existiert.

**Schwachstelle 3 — Series A ist einziger Überlebenspfad ohne Fallback.**

Das Unternehmen hat nach Verbrauch des Startkapitals für Phase-1-Aufbau null verbleibenden Puffer für den Betrieb von H2 2027. Die Series A in Q1 2027 ist keine Wachstumsoption, sondern die einzige Massnahme gegen Insolvenz.

---

## 10. Top-3 Stärken trotz allem

**Stärke 1 — Marktopportunität und Timing sind real.**

P2P-Skill-Gaming ist ein nachgewiesenes Modell. Der Esports-Markt wächst strukturell. Die MGA-Lizenz als regulatorische Grundlage gibt Akzeptanz bei Banken und Payment-Providern.

**Stärke 2 — CAC-Ausgangsniveau und K-Faktor-These sind valide angesetzt.**

€42 CAC für eine Community-getriebene Esports-Plattform mit organischem Wachstum über Twitch/Discord ist plausibel, wenn der K-Faktor von 2,0 auch nur halb erreicht wird.

**Stärke 3 — Steuerstruktur adressiert einen realen Cost-Driver.**

Das Kernproblem der DE-GmbH mit Vollbesteuerung ist für ein iGaming-Business mit Malta-Lizenz real. Die angestrebte Jurisdiktions-Struktur ist ein branchenübliches Setup.

---

## 11. Empfehlung: NO-GO in aktueller Form — Resubmit erforderlich

Das ist keine grundsätzliche Ablehnung des Geschäftsmodells, sondern eine Ablehnung des vorgelegten Finanzplans als Investitionsgrundlage.

**Resubmit-Bedingungen (priorisiert):**
1. Kompletter P&L-Neuaufbau aus einem einzigen konsistenten Excel-Modell
2. Marketing-Budget explizit modelliert mit Gross-Acquisition-Logik
3. Realistischer Churn-Ansatz: 10–12% monatlich in J1, nicht 8%
4. Series-A-Szenario mit Fallback
5. LTV-Berechnung transparent machen: Formel, Annahmen, Power-User vs. Casual-User

---

## 12. Konkrete Folgefragen

1. **P&L-Modell-Quelle:** Welche der beiden Revenue-Zahlen (€3,1M oder €9,52M in J5) stammt aus dem zugrundeliegenden Modell?
2. **Marketing-Budget-Breakdown:** Was ist der geplante monatliche Marketing-Spend in J2 (2028) aufgeschlüsselt nach Kanal?
3. **Churn-Validierung:** Liegt eine Retention-Analyse vor? Quelle für 8%-Churn?
4. **Series-A-Contingency:** Was ist der konkrete Minimal-Plan für Series-A-Verzögerung?
5. **Steuer-Substanz-Plan:** Wie viele Vollzeit-Mitarbeiter in Malta/Irland, ab wann? AStG-Rechtsgutachten?

---

*Erstellt im Rahmen Wave 2 — isolierte Due-Diligence. Datum: 2026-05-15.*
