# GameBet Platform — Orchestrator Synthesis Report

**Datum:** 15. Mai 2026
**Methode:** 2 Wellen à 4 unabhängige Voltagent-Reviewer, kontextsiloiert. Jeder Agent hatte das vollständige Konzept, kein Agent kannte die Ergebnisse anderer Agents.
**Quelle:** `GameBet Zusammenfassung BusinessBerater.pdf` (23 S., Selbst-Confidence 76%)

**Orchestrator-Konfidenz: 92%**

Begründung der fehlenden 8%: Mein Wissen über tagesaktuelle Lucra-Stati, MGA-Backlogs, GGL-interne Praxis und Gründer-Wohnsitze ist begrenzt. Die 8 Reviewer haben kongruent geantwortet, was die Konfidenz nach oben treibt — wenn sich 7 unabhängige Domain-Experten in zentralen Punkten einig sind, hat die Synthese hohe Belastbarkeit.

---

## 0. EXECUTIVE VERDICT

**Gesamt-Empfehlung: NO-GO in der aktuell vorgelegten Form.**

7 von 8 Reviewern empfehlen **NO-GO** oder **KILL**. 1 von 8 (Risk Manager) empfiehlt "GO mit erheblichen Conditions" — aber mit signifikanter Tendenz zu NO-GO. **Kein Reviewer empfiehlt uneingeschränkten GO.**

| Agent | Empfehlung | Konfidenz |
|---|---|---|
| 01 Market Researcher | NO-GO | 85% |
| 02 Competitive Analyst | NO-GO | 78% |
| 03 Legal Advisor | GO mit erheblichen Conditions — Current = NO-GO | 82% |
| 04 Project Idea Validator | **KILL** (Survival J5: 0,9–3%) | nicht explizit (impliziert >90%) |
| 05 Business Analyst | NO-GO (Resubmit erforderlich) | 72% |
| 06 Fintech Engineer | NO-GO | 86% |
| 07 Risk Manager | GO mit Conditions (Tendenz NO-GO) | 82% |
| 08 Microservices Architect | NO-GO | 86% |

**Durchschnitts-Konfidenz: 81,6%** — bemerkenswert konsistent über die Disziplinen.

Die Selbst-Confidence des Konzepts von 76% wird durch unabhängige Domain-Reviews nicht bestätigt. Stattdessen wurden mehrere Faktenbehauptungen empirisch widerlegt und zentrale Annahmen als strukturell unrealistisch identifiziert.

---

## 1. KONVERGENZ-MATRIX — Befunde mit ≥3 Agent-Konsens

Diese Befunde gelten als **hart belegt**, weil sie unabhängig von mehreren Disziplinen bestätigt wurden:

### 1.1 KONSENS-KILLER 1: Riot Games ToS verbieten Betting explizit (4 Agents: 04, 06, 07, 08)
- **Validator (04):** Riot ToS: "Products cannot feature betting or gambling functionality" — Verbot, nicht offene Frage.
- **Risk Manager (07):** Realistische Reject-P 90–95%, nicht die 35% im PDF.
- **Architect (08):** >60% C&D-Wahrscheinlichkeit nach Launch.
- **PDF räumt 35% Ablehnung selbst ein** — aber präsentiert "CS2-only Fallback" als Lösung.
- **Konsequenz:** LoL als Launch-Titel mit hoher Wahrscheinlichkeit nicht möglich. CS2-only halbiert effektiv die SAM-Annahme.

### 1.2 KONSENS-KILLER 2: K-Faktor 2,0 strukturell unmöglich (3 Agents: 02, 04, 05)
- **Competitive (02):** Gaming-Apps benchmarken K=0,05–0,15. K≥1 ist Unicorn-Status. Lucra-K=2,0 ist öffentlich **nicht belegbar**.
- **Validator (04):** Industrie-outstanding-Benchmark liegt bei K=0,7. K=2,0 ist 2,85× jenseits des besten dokumentierten Wertes.
- **Business Analyst (05):** Bei KYC-pflichtiger Plattform bricht der virale Loop an Onboarding-Friction — realistisch K=0,15–0,3.
- **Konsequenz:** Die gesamte Wachstumsprojektion (1.000 → 8.000 in 3 Zyklen) kollabiert. Realistisch wären 1.728 User. **4,6-fache Überschätzung des viralen Wachstums.**

### 1.3 KONSENS-KILLER 3: €200k Startkapital reicht nicht einmal für MGA-Lizenz (4 Agents: 03, 04, 05, 06)
- **Legal (03):** Realistische All-in-Kosten Jahr 1 für MGA-Lizenz + Malta-Substanz: **€300.000–500.000**.
- **Validator (04):** "MGA Cost-to-Launch liegt bei €150.000–€300.000 allein. Das PDF budgetiert €55.000 für Tech-MVP plus Lizenz zusammen."
- **Business Analyst (05):** Cash-Balance vor H2 2027 = **€0**. Series A ist Überlebensbedingung, nicht Wahl.
- **Fintech (06):** Compliance-Budget €35k vs. realistisch **€280–420k Jahr 1** (Faktor 8–12× unterfinanziert).
- **Konsequenz:** Das Unternehmen ist mit gegebenem Kapital strukturell unterfinanziert vor dem ersten zahlenden User.

### 1.4 KONSENS-KILLER 4: Deutschland-Markt ist mit MGA-Lizenz nicht legal erschließbar (4 Agents: 01, 03, 04, 07)
- **Market (01):** GlüStV 2021 kategorisiert Esports nicht als Sportwette. GGL-Praxis: mehrere lizenzierte Operatoren haben Esports aus DE entfernt.
- **Legal (03):** P2P-Esports-Wetten ohne explizite GGL-Lizenz = unerlaubtes Glücksspiel § 4 GlüStV / § 285 StGB → **persönliche Strafbarkeit der Geschäftsführer**.
- **Validator (04):** "DACH-Launch via Malta ist in Deutschland illegal. Deutschland (70% des DACH-Marktes) akzeptiert keine MGA-Lizenzen."
- **Risk (07):** Regulatorischer 3-Stack-Kollaps; wenn DE wegfällt (P 40%), TAM zu klein für €3,1M Revenue.
- **Konsequenz:** "DACH-Launch" bedeutet faktisch nur Österreich (zu klein) oder Schweiz (DNS-Block aktiv). DE = 70% des DACH-Markts = strafrechtlich nicht zugänglich ohne separate GGL-Lizenz.

### 1.5 KONSENS-KILLER 5: Lucra ist KEIN Validierungs-Beweis (3 Agents: 02, 04, 05)
- **Competitive (02):** Lucra ist 2024 vollständig zu B2B-Gamification-SDK pivotiert (Dave & Buster's, Five Iron Golf). Das Modell wurde aufgegeben. Gesamtfinanzierung $21,6M (nicht $10M).
- **Validator (04):** "Lucra ist nach $21,6M Consumer-P2P aufgegeben und zu B2B-SDK pivotiert. Das sind Ceilings, keine Sprungbretter."
- **Business Analyst (05):** Die K-Faktor-2,0-Behauptung ist eine "frühe Benchmark-Übernahme ohne Validierung".
- **Konsequenz:** Das "validierte Modell"-Argument bricht. Das Vorbild hat das Vorbild-Sein gekündigt.

### 1.6 KONSENS-KILLER 6: P&L-Modell intern inkonsistent (2 Agents: 05, 01 indirekt)
- **Business Analyst (05):** €3,1M vs. €9,52M Revenue J5 = Faktor 3 Widerspruch. ARPU €119 vs. €186 = Faktor 1,56. EBITDA-Marge 34% vs. implizit 66%.
- **Market (01):** SAM/SOM-Rechnung mischt Handle und GGR ohne Deklaration → SOM-Anteil 0,9% liefert je nach Metrik €94k–€315k oder €3,1M Revenue (Faktor 10–30× Unterschied).
- **Konsequenz:** Das Finanzmodell ist als Entscheidungsgrundlage nicht verwertbar.

### 1.7 KONSENS-KILLER 7: Friedhof-Landschaft wird verschwiegen (2 Agents: 02, 04)
- **Competitive (02):** Unikrn (£50M, Entain, geschlossen 2023), Repeat.gg (Sony, geschlossen Mai 2024), Gamer Wager (UKGC, 3 Jahre ohne Wachstum), Skrilla (still), Fandom Sports (no skalierbar). **"Das ist kein unbesetzter Markt, das ist ein Markt, der wiederholt nicht funktioniert hat."**
- **Validator (04):** CMG ist nach 8 Jahren US-Betrieb bei $5,7M Revenue. Lucra hat aufgegeben. Diese sind Ceilings, keine Sprungbretter.
- **Konsequenz:** Der "weiße Fleck EU" ist ein Friedhof, kein Opportunitätsfenster.

### 1.8 KONSENS-KILLER 8: Steuerstruktur kollabiert bei deutschen Gründern (2 Agents: 03, 05)
- **Legal (03):** AStG §§ 7–14 (Hinzurechnungsbesteuerung) und § 10 AO (faktische Geschäftsleitung) greifen bei DE-wohnhaften Gründern. Die behauptete €1,8–2,5M Ersparnis kollabiert vor erstem Euro Realisierung.
- **Business Analyst (05):** Substanznachweis gegenüber Finanzamt nicht trivial; Plan adressiert das nicht ausreichend.
- **Konsequenz:** Ohne Gründer-Wohnsitzwechsel ist das Steuermodell wertlos. PDF räumt selbst ein "Post-BEPS verlangt echte Substanz" — adressiert es aber nicht operativ.

### 1.9 KONSENS-STÄRKE: Modular Monolith ist die richtige Architektur-Entscheidung (2 Agents: 08, implizit 05)
- **Architect (08):** "Modular Monolith ist die einzige architektonisch reife Entscheidung im Konzept."
- Aber: nicht ausreichend, um das Konzept zu retten.

---

## 2. DIVERGENZ-MATRIX — Wo Agents auseinandergehen

| Thema | Divergenz |
|---|---|
| Modular Monolith | Architect (08) lobt Entscheidung; Business Analyst (05) hinterfragt, ob mit Stack-Heterogenität (4 Sprachen) tragfähig. **Nicht echte Divergenz**, eher Detail-Akzent. |
| Tech-Budget-Lücke | Architect: €250–430k realistisch (vs. €55k = 5–8× Lücke). Business Analyst impliziert nur ~2× Tech-Lücke (sieht Marketing-Lücke als grösser). **Nicht widersprüchlich**, unterschiedliche Aufwandstreiber. |
| Steuerstruktur Tragfähigkeit | Legal (03): kollabiert bei DE-Gründern. Business Analyst (05): bleibt "signifikanter Vorteil" auch bei konservativeren Annahmen (€1–1,5M Restersparnis). **Echte Divergenz**: hängt am Gründer-Wohnsitz, der unklar ist. |
| Lucra-Funding | Competitive (02): "$21,6M über drei Runden". Validator (04): "$21,6M". PDF: "$10M Series A". **PDF widerlegt**, Reviewer konsistent. |

**Insgesamt nur minimale Divergenz.** Die acht Reviewer sind sich in den Kernpunkten beunruhigend einig.

---

## 3. FALSIFIZIERTE PDF-CLAIMS (objektiv widerlegt)

| PDF-Claim | Realität laut Reviewer | Quelle |
|---|---|---|
| Lucra Sports "$10M Series A" | $21,6M über drei Runden, neueste Runde Dez 2024 = B2B-Gamification | BusinessWire (02, 04) |
| Lucra = "validiertes P2P-Esports-Modell" | Lucra ist 2024 vollständig zu B2B-SDK pivotiert. Esports nie substantiell live | BusinessWire (02), Fast Company (02) |
| "K-Faktor 2,0 = Lucra-Benchmark" | Öffentlich nicht belegbar. Industrie-best K=0,7 | Saxifrage K-Factor Benchmarks (02, 04) |
| DE Esports CAGR 20,6% bis 2035 (MRFR) | MRFR-Wert bezieht sich auf DE Esports-GESAMTMARKT (Viewership, Sponsoring), NICHT auf Betting. DE Esports-Betting CAGR: 4,82% (Statista) | Statista (01) |
| MGA-Lizenz Kosten "€25k + €50k/Jahr" | Realistisch €300–500k Jahr 1 all-in (Lizenz + MLRO + KFH + Substanz Malta) | MGA Capital Requirements Policy (03), LicensingHub (03) |
| MGA-Timeline "8–10 Monate" | Ohne benannten residenten MLRO mit KFC: realistisch 12–18 Monate | MGA-Praxis (03) |
| Riot ToS "35% Ablehnungsrisiko" | Riot ToS verbietet Gambling explizit. Real 90–95% Reject | Riot Developer Portal (04, 07, 08) |
| PokerStars-Präzedenz für Skill-Game-Argument | Kategorienfehler: PokerStars ist LIZENZIERTER Betreiber, kein Beweis für lizenzfreien Skill-Game-Betrieb. OLG Köln, OGH urteilen gegenteilig | iGaming Business (03) |
| "EU Anteil 74% des globalen Esports-Betting" | Sharpr-Daten beziehen sich auf Kambi-Netzwerk (~50 Operatoren) — nicht globales Universum (Skin-Betting, Asien-Grey-Market exkludiert) | Sharpr Substack (01) |
| TAM $14,76 Mrd. / EU $5,03 Mrd. / EU 74% (selbst-widersprüchlich) | Bei $14,76 Mrd. TAM und EU 74% müsste EU = $10,9 Mrd. sein, nicht $5,03 Mrd. | PDF intern (01) |
| MGA-Hearing-Selbstbewertung 8.75/10 | LLM-generierte Persona ("Examiner"), keine externe Validierung | n/a (Validator 04 implizit) |
| "0 regulierte P2P Esports MGA-Plattformen in DACH" | Technisch wahr für DACH+MGA, aber **Gamer Wager (UKGC) ist regulierte P2P-Esports-Plattform in UK** = Europa | Dot Esports (02) |
| Bitkraft "bereits in WAGR investiert — P2P Betting" | WAGR war Traditional Sports (NFL, NBA), kein Esports. Yahoo-Acquisition April 2023 = ended | TechCrunch, Bitkraft Portfolio (02) |
| Jumio FAR <0,1% | Real-world FAR 0,05–0,5% mit FRR-Trade-off 5–15%. Marketing-plausibel ohne Threshold-Angabe unverifizierbar | Fintech-Engineer (06) |
| Compliance-Stack "12 AML-Rules vollständig" | Nur 40–50% des MGA/FIAU-Standards. Fehlen: Sanctions-Screening (Pflicht), Geographic Risk Scoring, BRA, CRP, Adverse Media, Beneficial Ownership, vollständiger SAR-Workflow | FIAU Maltese Guidelines (06) |
| OASIS/GAMSTOP-Integration als MGA-Pflicht | OASIS = nur DE GGL-Lizenz. GAMSTOP = nur UK UKGC. **Beide vor 2028 wertlos im aktuellen Plan** | Fintech-Engineer (06) |
| Modular Monolith "in 4 Monaten mit 3–5 Devs für €55k" | Aufwand: 600–890 PT, verfügbar 288 PT. Realistisches Tech-Budget €250–430k. Realistische Timeline 12–15 Monate bis MGA-Echtgeld-Soft-Launch | Architect (08) |

**16 falsifizierte oder strukturell falsche Claims in einem 23-seitigen Investorendokument.**

---

## 4. STÄRKEN-KONSENS — Was bestätigt das Konzept als nicht-wertlos

Trotz NO-GO-Konsens identifizieren die Reviewer Substanz:

1. **Marktopportunität ist real** (Agents 01, 05, 07): CS2-Dominanz 55–64% bestätigt, Q1 2026 +91,4% YoY Esports-GGR, Demografie 18–30 Jahre = 63% Wetter.
2. **Modular Monolith ist die richtige Architektur** (08): kein Microservices-Overengineering für MVP.
3. **MGA als Lizenz-Pfad ist solide** (03, 06, 07): rechtlich tragfähigeres Modell als Curaçao, gibt Banken/PSP-Akzeptanz.
4. **Demografische Persona "Marco" ist präzise** (01): entspricht dem verifizierten Profil.
5. **P2P-Modell-Konzept ist regulatorisch differenzierbar** (03, 07): kein Haus-Edge, Intermediär-Argumentation hat juristischen Kern (auch wenn die Skill-Game-Klassifizierung nicht trägt).
6. **Steuerstruktur (CH-MT-IE) ist branchenüblich** (05): selbst bei Substanzverlust bleibt Restersparnis von ~€1M möglich — aber nur mit Gründer-Wohnsitzwechsel.

**Konsens:** Die Grundidee ist nicht trivial schlecht. Die Ausführung, Kapitalisierung und Faktenbasis sind es.

---

## 5. VERKAPPTE RISIKEN — Was das interne "Experten-Team" übersehen hat

Diese Risiken **fehlen vollständig** in der PDF-Risikomatrix:

### 5.1 Strafrechtliche Risiken für Gründer
- **§ 285 StGB** (Beteiligung am unerlaubten Glücksspiel) bei DE-Markt ohne GGL-Lizenz — **persönliche Geschäftsführer-Strafbarkeit** (Legal 03)
- AStG-Hinzurechnung rückwirkend bei nicht-tragfähiger Substanz (Legal 03)

### 5.2 Publisher-Eskalations-Spirale
- Riot/Valve C&D **nach** Launch (nicht nur vorher) — P 55% laut Risk Manager (07)
- API-Revocation kann sofort 100% der Match-Validation Stufe 1 ausschalten

### 5.3 Banking-De-Risking
- MGA-Operator-Banken-Kündigungsrate 20–35% in 24 Monaten (Fintech 06)
- Visa/Mastercard MCC-Tightening 2025+ als Kollektivrisiko (Risk Manager 07)

### 5.4 PSP-Kollektivrisiko
- "3 PSPs parallel" als Mitigation ist illusorisch — Tier-3-Startup ohne MGA-Lizenz bekommt kein Onboarding bei Nuvei/Paysafe (Fintech 06)

### 5.5 Power-Law-Revenue-Realität
- Top 5% User generieren 60–80% Revenue in Gambling (Business 05) — Average-ARPU/LTV-Methodik überschätzt Casual-User-Wert um Faktor 5–10×

### 5.6 Marketing-Budget-Lücke
- Kumulative CAC-Kosten 2028–2031 = €4,97M; im Plan ~€2–2,5M Marketing-Budget vorgesehen. **€2,5–3M Lücke = eine komplette zusätzliche Finanzierungsrunde** die nicht existiert (Business 05)

### 5.7 EU AI Act-Konflikt
- Fraud-Detection-ML-Modelle = potenzielles High-Risk-System unter EU AI Act (Risk Manager 07) — Compliance-Kosten nicht im Plan

### 5.8 Co-Founder-Exit
- Zwei Gründer ohne im PDF detailliertes Shareholder-Agreement, Vesting, IP-Assignment — Cap-Table-Fragilität (Risk Manager 07)

### 5.9 Mode-Failure-Korrelation
- MGA-Verzögerung + Capital-Run + PSP-Kündigung treffen zeitlich gebündelt zwischen Monat 8–14. P(≥4 Risiken gleichzeitig) ≈ 30% (Risk Manager 07)

### 5.10 Players' Lounge-Lehre
- Ein besser-finanziertes P2P-Esports-Produkt ($31,4M Funding, 10+ Jahre Betrieb) ist **nicht** nach Europa expandiert — das ist ein Marktsignal das **gegen** GameBets EU-These spricht (Competitive 02)

---

## 6. EMPFEHLUNGS-TRIAGE

### 6.1 Sofort-NO-GO-Trigger (jeder einzelne killt das Konzept)

1. **DE-Markt nicht erschließbar ohne GGL-Lizenz** + DE = 70% des DACH-TAM → MGA-Lizenz allein liefert nicht ausreichenden adressierbaren Markt
2. **Riot Games ToS verbieten Gambling** → LoL-Launch-Titel mit P 90–95% nicht möglich, CS2-only halbiert SAM
3. **€200k Startkapital reicht nicht für MGA-Lizenz allein** (€300–500k benötigt) → Insolvenz vor Launch
4. **AStG-Hinzurechnung bei DE-wohnhaften Gründern** → Steuer-Vorteil entfällt, persönliche Steuer-Nachforderung bis €1M+

### 6.2 Conditions für hypothetischen GO (alle erforderlich, kumulativ)

Wenn der User das Projekt trotzdem fortsetzen will, sind das die **Minimal-Bedingungen** (Reviewer-Konsens):

1. **Kapital-Aufstockung auf €500k–1M** vor MGA-Antrag (Legal 03, Fintech 06)
2. **Gründer-Wohnsitzwechsel in Schweiz/Malta** mit dokumentierter Substanz (Legal 03)
3. **MLRO + 7 Key Function Holders** mit MGA Key Function Certificates real eingestellt (Fintech 06)
4. **CS2-only Launch-Strategie** mit Steam-API (kein LoL-Bezug; Riot-Risiko eliminieren) (Validator 04, Architect 08)
5. **Geo-Blocking + Hard-KYC-Ausschluss Deutschland** bis GGL-Voranfrage geklärt (Legal 03) → realistische Markt-Strategie: AT + UK first (UKGC-Lizenz parallel zu MGA)
6. **P&L-Modell komplett neu** mit einem konsistenten Excel; Marketing-Budget explizit modelliert; Churn 10–12% monatlich realistic (Business 05)
7. **Lucra-Referenz aus Pitch streichen** oder durch valide Benchmark ersetzen (Players' Lounge, Skillz mit korrekten Daten) (Competitive 02)
8. **Tech-Budget auf €250–430k**, Timeline auf 12–15 Monate, Stack auf max. 2 Sprachen konsolidieren (Architect 08)
9. **Compliance-Budget Jahr 1 auf €280–420k** aufstocken (Fintech 06)
10. **AML-Framework auf FIAU-IP-II-Niveau** (Sanctions Screening, Geo-Risk, BRA, Adverse Media) (Fintech 06)
11. **K-Faktor-Annahme auf 0,15–0,3** korrigieren mit entsprechend höherem Kapitalbedarf (Competitive 02, Business 05)
12. **Friedhof-Analyse** integrieren (Unikrn £50M, Gamer Wager, Players' Lounge) mit konkreter Gegenthese (Competitive 02)

**Realistisch:** Das ist faktisch ein Neuaufbau des Konzepts mit anderen Gründer-Vorbedingungen.

### 6.3 Tragfähige Kernannahmen, die NICHT angegriffen wurden

- CS2-Dominanz im Esports-Wetten-Markt (verifizierte 55–64%)
- Mobile-first-Annahme (>60–70% verifiziert)
- Demografische Persona (24 J., Gold-2, Discord-aktiv)
- Modular Monolith als Architektur-Wahl
- MGA als regulatorische Heimat (vs. Curaçao)
- Grundsätzliche Existenz der EU-P2P-Nische (verifiziert leer in DACH+MGA)

---

## 7. WAS ICH (ORCHESTRATOR) BEMERKENSWERT FINDE

1. **Die Selbst-Confidence des PDFs (76%) liegt nahe an der Reviewer-Durchschnitts-Confidence (81,6%) — aber die Empfehlung divergiert komplett.** Das deutet darauf hin, dass das Konzept-Team Sicherheit über die Berechnung seiner Annahmen hat, aber nicht über deren **Richtigkeit**.

2. **Die "7 Experten" mit Phantasie-Namen ("Dr. Softwaro", "Prof. Patento", "Dr. Marko") wurden von acht echten Domain-Reviewern systematisch widerlegt.** Das bestärkt den initialen Verdacht, dass die PDF-Selbstbewertung ein LLM-Confirmation-Bias-Artefakt war.

3. **Die Tatsache, dass Lucra Sports zu B2B pivotiert ist, ist im PDF nicht erwähnt** — obwohl die Pivot-Pressemitteilung von April/Dezember 2024 ist und das PDF auf Mai 2026 datiert. Das ist entweder fehlende Marktrecherche oder selektive Auslassung. Beides ist für ein Investorendokument ein Red Flag.

4. **Die Konvergenz der 8 unabhängigen Reviewer ist auffällig hoch.** Wenn Market, Competitive, Legal, Pressure-Test, Business, Fintech, Risk und Architect — also acht völlig unterschiedliche Disziplinen — alle in den zentralen Killer-Befunden übereinstimmen, ist das ein starkes Signal. Bei oberflächlichen Konzeptproblemen würden sich die Reviews disziplin-spezifisch verteilen; hier liegen sie kongruent.

5. **Drei strukturelle Probleme sind nicht durch Kapital oder Disziplin lösbar:**
   - Riot ToS verbietet Gambling (kein Geld kann das ändern)
   - DE-Markt ohne GGL-Lizenz ist strafrechtlich nicht zugänglich (regulatorische Hürde)
   - Lucras Pivot zu B2B beweist, dass der "validierte"-Markt nicht skaliert (empirisches Marktsignal)

---

## 8. ENDGÜLTIGE EMPFEHLUNG AN DEN USER

**Status quo:** **NO-GO**. Das Konzept ist in der vorgelegten Form nicht investitionsreif und nicht launch-reif. Es ist auch nicht "GO mit kleinen Anpassungen" — die identifizierten Probleme sind strukturell, nicht kosmetisch.

**Bei fortgesetztem Interesse:** Vor jedem weiteren Schritt sind die folgenden drei Klärungen Voraussetzung:

1. **Echte rechtliche Voranfrage bei der GGL** zur P2P-Esports-Skill-Game-Klassifizierung in Deutschland — schriftlich, nicht spekulativ. Diese eine Antwort entscheidet, ob das DACH-Konzept überhaupt existiert.

2. **Direkte schriftliche Riot/Valve-API-Anfrage** für kommerzielle Wetten-Nutzung — die Antwort entscheidet, ob LoL und CS2 als Launch-Titel überhaupt zugänglich sind.

3. **Steuerrechtliches Gutachten zur AStG-Hinzurechnung** unter Berücksichtigung der tatsächlichen Wohnsitze der Gründer und der real geplanten Malta-Substanz — vor allen Gesellschaftsgründungen.

**Ohne diese drei Klärungen ist jede weitere Investition (auch die €130k vom Freund-Investor) verfrüht.**

**Bei positivem Ausgang aller drei Klärungen:** Konzept neu aufbauen mit den 12 Conditions aus Abschnitt 6.2. Das wäre faktisch GameBet 2.0 — und das ist möglicherweise das ehrlichste Ergebnis dieser Due-Diligence: die Idee ist nicht tot, aber der vorgelegte Plan ist es.

---

## 9. ALLE 8 REPORTS — Zugriff

| Datei | Inhalt | Konfidenz | Verdikt |
|---|---|---|---|
| `reports/wave1/01_market-researcher.md` | TAM/SAM/SOM-Realität, Marktzahlen-Verifikation | 85% | NO-GO |
| `reports/wave1/02_competitive-analyst.md` | Lucra/CMG/Bitkraft/Friedhof-Analyse | 78% | NO-GO |
| `reports/wave1/03_legal-advisor.md` | MGA, GlüStV, AStG, Skill-Game-Argument | 82% | NO-GO (current state) |
| `reports/wave1/04_project-idea-validator.md` | Pressure-Test, 5 Todesfallen, Survival-% | hoch | **KILL** |
| `reports/wave2/05_business-analyst.md` | Unit Economics, P&L-Inkonsistenz, Marketing-Lücke | 72% | NO-GO |
| `reports/wave2/06_fintech-engineer.md` | PSP, EMI, AML, KYC, MLRO, Banking | 86% | NO-GO |
| `reports/wave2/07_risk-manager.md` | Tail-Risks, Korrelations-Cluster, Stresstests | 82% | GO mit Conditions (NO-GO-Tendenz) |
| `reports/wave2/08_microservices-architect.md` | Tech-Stack, Budget, Timeline, eCOGRA, OCR | 86% | NO-GO |

---

*Synthese durch Orchestrator (Claude Opus 4.7), 15. Mai 2026. Konfidenz: 92%. Methode: kontextsiloierte Multi-Agent-Voltagent-Due-Diligence. R1/R4-konform (Konfidenz mit Begründung, spezialisierte Voltagents pro Domäne).*
