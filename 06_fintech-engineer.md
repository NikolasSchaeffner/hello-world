# Wave 2 / Agent 06 — Fintech Engineer Report

**Konfidenz: 86%**

Begründung der fehlenden 14%:
- Keine Einsicht in den vollen Business-Plan und das tatsächliche Kapitaltabellen-Setup (cap table, founder-equity-für-Substanz, geplante Director-Residencies).
- Keine Sicht auf bereits geführte PSP-Vorgespräche / NDAs / Term Sheets — Bewertung erfolgt anhand öffentlicher Marktstandards für 2024–2026 (Nuvei iGaming, Paysafe Gambling).
- MGA-Gebührentabellen & FIAU Implementing Procedures Part II wurden seit 2023 mehrfach revidiert; meine Quellenbasis ist überwiegend Q3 2024 / 2025-Stände. Ich halte Beträge daher in Bandbreiten.
- Litauische EMI-Lizenz: Bank of Lithuania hat 2024 den "fast-track"-Pfad faktisch entschärft (post-Wirecard / post-Foris / post-Payrnet) — meine Zeit/Kosten-Schätzungen sind eher konservativ als optimistisch.
- "Jumio FAR <0,1%" ist ohne Angabe der genau gemessenen Methodik (NIST FRVT? iBeta PAD Level 2?) nicht zuverlässig zu falsifizieren — ich bewerte plausibility, nicht den exakten Zahlenwert.

---

## 1. PSP-Setup-Realismus (3 PSPs parallel)

**Verdikt: Unrealistisch in 2026 für ein €200k-Startup ohne MGA-Lizenz in der Hand. Maximal 1 PSP + 1 Wallet/Alternative am Start.**

### Marktrealität iGaming-PSP 2026

Nuvei und Paysafe gehören zu den ~6 Tier-1 Acquirern, die echtes Gambling-MCC (7995) für lizenzierte Operatoren unterstützen. Beide verlangen vor Vertragsschluss durchweg:

| Anforderung | Nuvei (iGaming-Vertical) | Paysafe (Gaming Solutions) |
|---|---|---|
| Lizenz im Hand (MGA/UKGC/Curaçao) | Pflicht — kein PoC ohne | Pflicht |
| Mindest-Settlement-Volumen für Tier-1-Pricing | ~€500k/Monat | ~€300–500k/Monat |
| Onboarding-Dauer realistic | 8–14 Wochen | 10–16 Wochen |
| Rolling Reserve | 5–10% / 180 Tage | 5–15% / 180 Tage |
| Integrations-Aufwand (Dev-Tage) | 25–45 (Cashier + Webhooks + 3DS2 + Reconciliation) | 20–40 |
| Setup-Fee | €5–15k (oft "waived" bei Volumen-Commitment) | €5–10k |
| Discount Rate (MDR) iGaming non-EEA cards | 2,8–4,5% + €0,20–0,35/Tx | 2,9–4,8% |
| Chargeback-Fee | €15–25 | €15–30 |

### Konkrete Probleme für GameBet

1. **Henne-Ei-Problem:** Beide PSPs unterzeichnen NICHT ohne MGA-Lizenz. MGA-Lizenz kommt aber laut Plan erst Monat 8–14. Also frühestens Q4-2026 echte PSP-Verträge — nicht "Day 1".
2. **Drei parallel = Anti-Pattern:** Selbst Tier-1-Operatoren (LeoVegas, Kindred zu deren Frühphase) starteten mit 1 Acquirer + 1 APM-Aggregator. Drei parallele PSP-Stacks bedeuten:
   - 3× KYC-of-Merchant (jeder PSP screened den Operator separat → 3× Underwriting-Friction).
   - 3× Reconciliation-Pipelines (verschiedene Settlement-Files, Cycle-Times, Chargeback-APIs) — bei 3–5 Devs nicht leistbar.
   - 3× Compliance-Reports (PCI-DSS Eingangsfragen, AML-Walkthroughs pro PSP, jährliche Re-Underwriting-Reviews).
   - Verhandlungsmacht sinkt, weil keiner der drei das Gefühl bekommt, "primary" zu sein — Pricing wird schlechter, nicht besser.
3. **Backup-PSP-Mythos:** Backup-PSP funktioniert nur, wenn er live mit Volumen läuft (sonst friert er ein, Risk-Profile veraltet, MID kalt). Ein "schlafender" Backup-PSP fällt nach 90 Tagen ohne Transaktion oft aus dem Active-Status raus.
4. **Verhandlungsmacht eines €200k-Startups:** Im iGaming-Acquiring 2026 ist <€500k/Monat Settlement schlicht Tier-3-Pricing. Erwartete reale MDR: 4,5–5,5% + Volume-Reserve 10–15%. Das frisst die Marge.

### Realistische Empfehlung

- **Stufe 1 (Pre-Launch, 0–6 Mo.):** Wallet-Onboarding via Open-Banking PIS (TrueLayer / Tink / Volt) + ggf. 1 PSP mit "Soft-Lock" bis MGA da ist.
- **Stufe 2 (Launch, 6–14 Mo.):** 1 primärer Acquirer (entweder Nuvei ODER Paysafe — nicht beide) + 1 APM-Aggregator (Trustly, Skrill, Paysafecash) für Locale-Coverage.
- **Stufe 3 (Scale, 14–24 Mo.):** Zweiter Acquirer als echtes Redundanz-Setup einführen, sobald Settlement >€300k/Monat.

**Risiko-Tag: HIGH** — der Plan unterschätzt Onboarding-Zeit (Faktor 3–4×) und Verhandlungsposition fundamental.

---

## 2. Litauen UAB EMI-Lizenz — Sinn und Aufwand

**Verdikt: Overkill für GameBets Stadium. Falscher Hebel zum falschen Zeitpunkt.**

### Litauische EMI 2024–2026 — die Fakten

Bank of Lithuania (LB) hat nach Wirecard, Payrnet und der UAB-Wave 2018–2022 die Anforderungen massiv verschärft:

- **Eigenkapital:** Mindest-Initial-Capital für EMI: €350.000 (Art. 7 EU EMD2 / litauisches EMI-Gesetz). Für "Small EMI" (begrenztes Volumen, max. €5 Mio. Outstanding E-Money) reduziert auf ca. €125–200k, aber für Gambling-Wallet-Use-Case nicht praktikabel — Volumenwachstum würde sofort full-license erzwingen.
- **Safeguarding-Konto:** 100% des E-Geld-Saldos muss in einem ringgefenced Konto bei einer EU-Kreditinstitution liegen ODER in qualifizierten Liquid-Assets (deutsche/franz. Staatsanleihen etc.). Die Mittel dürfen nicht der Insolvenzmasse der EMI zugänglich sein.
- **Substanzanforderungen ab 2023 (post-Foris):** 
  - Mindestens 3 KMU-Direktoren, davon mind. 2 residence in Litauen
  - Mindestens 1 lokaler AML/MLRO mit Litauisch-Sprachkenntnissen ODER fluent EN + LB-anerkannt
  - Lokaler Compliance Officer, lokaler Internal-Auditor (kann outsourced sein, aber mit Litauen-Nexus)
  - Physisches Büro in Vilnius/Kaunas (nicht nur Maildrop)
  - Lokale IT-Infrastruktur ODER zertifizierte EU-Cloud mit dokumentierter Sovereignty
- **Lizenzdauer:** 2018–2020 waren 6 Monate möglich. 2024–2026: realistisch **9–18 Monate** End-to-End, mit Antrags-Pre-Phase + RFI-Loops + Onsite-Inspektion.
- **Kosten** (laufend, Jahr 1):
  - Setup (Legal, Audit, IT-Compliance-Penetration-Test, Outsourcing-Frameworks): €120–250k einmalig
  - Laufender Run-Rate (3 Direktoren + Compliance/MLRO + Audit + Lokales Büro): €350–600k p.a.
  - Eigenkapital-Lock (Pflichtkapital + Safeguarding-Liquidity-Cushion): €400k+ gebunden

### Warum trotzdem manche Gambling-Anbieter EMI-Setup machen

Stimmt: Eine eigene EMI erlaubt:
1. Wallet ohne externen E-Geld-Anbieter (kein Skrill/Neteller-Markup)
2. Eigene IBANs für Spieler (Pay-out-Beschleunigung)
3. Cross-PSP-Aggregation ohne Acquirer-Doppel-Margin

Aber **das lohnt sich erst ab ~€10 Mio./Monat Tx-Volumen** — und auch dann partnern die meisten lieber mit existierenden EMIs (Lemonway, Modulr, Praxis Cashier) als selbst zu betreiben.

### Konkrete Empfehlung für GameBet

**Litauische EMI ist für €200k Startkapital nicht finanzierbar und nicht risikoadäquat.** Wallet-Funktionalität soll als Software-Layer **über** einem regulierten EMI-Partner laufen (z.B. Praxis Cashier, Lemonway, oder MGA-konform Trustly Wallet). Eigene EMI frühestens Jahr 3 prüfen — und nur dann, wenn der Volumen-Case da ist.

**Risiko-Tag: HIGH** — der Plan deutet auf ein fundamentales Missverständnis, was eine EMI-Lizenz strukturell ist und kostet.

---

## 3. Wallet-Segregation — MGA-Pflicht technisch

### Was MGA wirklich fordert (B2C-Lizenz, Player Funds Protection)

Player Funds Protection ist in der **MGA Player Protection Directive** (zuletzt rev. 2023, in Verbindung mit dem Gaming Act 2018) geregelt:

1. **Segregated Account (Pflicht):** Ein "Players' Account" bei einer Bank/EMI in MGA-anerkannter Jurisdiktion. Mittel der Spieler dürfen NICHT mit operationellen Mitteln vermischt werden. Kein Zugriff durch Gläubiger im Insolvenzfall.
2. **Schutzlevel (3 Optionen, der Operator wählt):**
   - **Basic Protection:** Reine Segregation, keine Garantie/Bürgschaft.
   - **Medium Protection:** Segregation + irrevocable bank guarantee oder trust.
   - **High Protection:** Trust mit unabhängigem Trustee + zusätzliche Sicherheit.
   - GameBet hat **keine Protection-Level-Angabe** im Konzept — das ist eine Lücke. MGA fragt im Antrag konkret danach.
3. **Reconciliation-Pflicht:** Tägliche Reconciliation Player-Liability (Summe aller Spieler-Wallet-Salden) vs. Bank-Saldo des Segregated Account. Differenzen >€5.000 oder >0,5% sofort meldepflichtig an Compliance.
4. **Reports:** Monthly Player Funds Report an MGA (PFR-Format). Auditor's confirmation jährlich.
5. **Bookkeeping-Trennung:** GL-Trennung von Player Liability (passivseitig) und Operational Cash (aktivseitig). Doppelte Buchführung mit eindeutigem Mapping.

### Technische Realität für 3–5-Dev-Team

Echte Wallet-Segregation Day 1 ist non-trivial:

| Komponente | Aufwand realistisch | Risiko bei DIY |
|---|---|---|
| Ledger-Service (double-entry, append-only) | 6–10 Dev-Wochen | Off-by-one, race-conditions, Settlement-Drift |
| Tägliche Reconciliation-Engine (Bank-Feed vs. internal ledger) | 3–5 Dev-Wochen | Bank-Statement-Format-Drift, Timezone-Issues |
| Audit-Trail (immutable, signed) | 2–3 Dev-Wochen | AWS S3 Object Lock allein reicht nicht — Hash-Chains nötig |
| Monthly PFR-Report-Generator | 1–2 Dev-Wochen | Format-Compliance MGA-Template |
| GL-Integration (Xero/Netsuite) | 2–4 Dev-Wochen | Mapping-Errors → Bilanz-Inkonsistenz |

**Total: 14–24 Dev-Wochen ≈ 3,5–6 Personen-Monate netto.** Bei 3–5 Devs, die parallel Backend, Frontend, Game-Logic, Risk-Engine und Compliance bauen müssen, ist das ein 6–9-Monatsblock NUR für Wallet-Infra — unrealistisch zu "Day 1".

### Praktikable Alternative

**Outsourcing an Cashier-Provider (Praxis Cashier, Cashflows, Lemonway, Pay4Fun).** Diese Anbieter haben Wallet-Segregation als Service inkl. MGA-PFR-Reports. Kosten: 0,3–0,8% on top auf Transactions, dafür eingesparter Dev-Aufwand + Compliance-Risikoübernahme.

**Risiko-Tag: HIGH** wenn DIY versucht wird, **MEDIUM** mit Cashier-Provider.

---

## 4. KYC-Provider (Jumio) Claims

### "FAR <0,1%" — was bedeutet das, und stimmt es?

FAR (False Acceptance Rate) bei Liveness/Biometric Verification wird üblicherweise gemessen entweder per:
- **NIST FRVT (Face Recognition Vendor Test):** Anbieter-Ranking, öffentlich. Jumio nimmt sporadisch teil; ihre Werte liegen typischerweise im oberen Mittelfeld, nicht Top-3.
- **iBeta PAD (Presentation Attack Detection) Level 1/2:** Jumio hat iBeta PAD Level 1 + Level 2 zertifiziert (öffentlich nachweisbar). Level 2 fordert APCER (Attack Presentation Classification Error Rate) <2% und BPCER (Bona Fide PCER) <1% auf definierten Attack-Vektoren.
- **Eigene Marketing-Benchmarks:** Jumio publiziert "Identity Verification" mit Genauigkeitswerten 99%+ — diese sind nicht direkt mit FAR vergleichbar.

### Plausibility-Check

"FAR <0,1%" als pauschale Aussage ist marketing-tauglich, aber technisch **nicht ohne Threshold-Angabe verifizierbar**. Real-world FAR bei modernen Liveness+Match-Pipelines (Jumio, Onfido, Veriff, iProov) liegen je nach Threshold-Konfiguration zwischen **0,05% und 0,5%** — mit entsprechendem Trade-off auf FRR (False Rejection Rate, also legitime User abgewiesen).

Wenn man FAR auf 0,1% kalibriert, steigt FRR oft auf 5–15%. Das bedeutet: 5–15% legitime Spieler scheitern beim ersten KYC-Versuch und brauchen manuelle Nachprüfung. Das ist operational signifikant.

### Was im Konzept fehlt

- Welcher Threshold? (Liveness-Score-Cutoff)
- Welche Attack-Vektoren werden abgedeckt? (2D-Photo, 3D-Mask, Deepfake-Video, Replay-Attack)
- Welcher Fallback bei FRR? (Manual Review SLA, Re-Try-Limits)
- 2026-Realität: **Deepfake-Liveness-Bypässe** sind das aktuelle Wettrüsten. Jumio's KI-Detection-Layer ist gut, aber nicht "0,1%" gegen state-of-the-art generative Attacks. NIST und ENISA haben 2024–2025 mehrfach gewarnt.

### Kosten

Jumio iGaming-Pricing 2026: ~€1,80–3,50 pro vollständige Verification (Document + Liveness + Match). Bei 10.000 Onboardings/Monat: €18–35k/Monat allein an KYC-Vendor-Cost. Im €35k-Compliance-Budget nicht abgedeckt.

**Risiko-Tag: MEDIUM** — Claim ist marketing-plausibel, aber operationell unterspezifiziert.

---

## 5. AML Rule-Set Vollständigkeit (vs. FATF/MGA Standards)

### Vergleich gegen MGA Implementing Procedures Part II + FIAU + FATF Recommendations

GameBet listet 12 Rules. Das ist **eine Teilmenge** dessen, was MGA-Audit erwartet. Es fehlen mindestens:

| Pflicht-Element | Im Konzept? | MGA/FIAU-Anforderung |
|---|---|---|
| Sanctions Screening (OFAC, EU, UN, HMT, Swiss SECO) bei Onboarding + ongoing | **FEHLT** | Pflicht, daily refresh, Match-Disposition-Workflow |
| PEP-Screening + Listen-Update-Frequenz | Nur bei L4 EDD — **zu spät** | Best Practice: alle Konten ab Onboarding |
| Adverse Media Screening | **FEHLT** | FIAU empfohlen, MGA-Audit checks |
| Source of Wealth (vs. Source of Funds) | Vermischt — nicht sauber getrennt | SoF = woher kam dieser konkrete Betrag; SoW = Gesamt-Vermögensentstehung. Distinkt. |
| Beneficial Ownership Verification (für Corporate-Customers, B2B) | **FEHLT** | Nur relevant wenn B2B-Affiliates; sollte adressiert sein |
| Geographic Risk Scoring (FATF High-Risk Jurisdictions, EU AMLD List) | **FEHLT** | Pflicht — IP+Address-basiert + Rule-Tree |
| Industry Risk Scoring (Spieler-Profession-Match) | **FEHLT** | EDD-Trigger bei Risk-Industries |
| Bonus Abuse / Promo Abuse Detection | **FEHLT** als AML-Rule | Manchmal AML-relevant (Strukturierung via Bonus-Stacking) |
| Cumulative Transaction Aggregation (rolling 30/90/365 days) | Implizit in RULE_001 (24h), aber nicht 30/90/365 | Pflicht — Long-window Pattern Detection |
| Velocity by Device / IP / Payment Instrument | RULE_009 streift es | Tieferes Pattern-Layering nötig |
| Dormant Account Reactivation | **FEHLT** | FIAU Indikator |
| Cross-Border Risk (deposit-currency vs. residence-country mismatch) | **FEHLT** | Common Red Flag |
| First-Time-Withdrawal-to-New-IBAN | **FEHLT** | Klassisches Money-Laundering-Pattern |
| SAR-Workflow (Drafting, MLRO-Review, FIAU-Submission via goAML/FIAU-Portal) | RULE_007 + RULE_012 erwähnen es — Workflow nicht beschrieben | Pflicht: vollständiges Case-Management |
| Recordkeeping 5+ Jahre | Implizit über S3 Object Lock | Pflicht inkl. nach Customer-Ende |
| Risk-Based-Approach-Dokumentation | **FEHLT als Dokument** | Pflicht — schriftliche Business Risk Assessment (BRA) |
| Customer Risk Profile (CRP) Score | **FEHLT** | Pflicht — initial + ongoing recalculation |

### Bewertung

12 Rules sind **maximal 40–50% dessen, was MGA + FIAU realistisch erwarten**. Ein MGA-Compliance-Audit (jährlich, durch FIAU + MGA Compliance-Audit-Unit) würde diese Lücken sofort identifizieren. Es fehlt insbesondere:

1. Sanctions Screening (kann allein zum Lizenzentzug führen)
2. Geographic Risk Scoring (FATF Grey List, EU High Risk Third Countries)
3. Schriftliche BRA + CRP-Methodologie
4. Vollständiger SAR-Workflow inkl. FIAU goAML-Anbindung

**Risiko-Tag: HIGH** — der Plan ist Material-only "halbfertig".

---

## 6. MLRO-Realismus

### Kann man einen MGA-Antrag ohne MLRO einreichen?

**Nein, nicht ernsthaft.** MGA verlangt für die B2C-Lizenz die Benennung von **Key Function Holders** (KFH), darunter:
- MLRO (Money Laundering Reporting Officer)
- Compliance Officer
- Key Person für Player Protection / Responsible Gaming
- Key Person für Anti-Fraud
- Key Person für IT / Information Security
- Key Person für Finance
- Key Person für Gaming

Jede dieser Personen muss ein **Personal Declaration Form (PDF/PQ)** + Fingerprint-PCC + Lebenslauf + Educational Records einreichen und vom MGA-Fit-and-Proper-Test bestätigt werden. Bei MLRO ist zusätzlich der **MLRO Approval Process via FIAU** durchzulaufen (separater Antrag bei der Financial Intelligence Analysis Unit).

Ohne benannten und MGA-approved MLRO wird die Lizenz **nicht** erteilt. Theoretisch kann man den Antrag einreichen mit "MLRO TBD" — aber er wird in der Issued-Phase blockiert. Realistisch verzögert das die Lizenz um 2–4 Monate.

### MLRO-Kosten Jahr 1 (Malta-Markt 2025–2026)

| Kostenposition | Range |
|---|---|
| Gehalt Senior MLRO (10+ Jahre, MGA-erprobt) | €70.000–€110.000 brutto p.a. + Boni |
| Recruitment-Fee (Headhunter, üblich 20–25%) | €15.000–€25.000 einmalig |
| FIAU Approval Process (Fees + Legal Begleitung) | €3.000–€8.000 |
| Berufshaftpflicht (Professional Indemnity, oft individuell beim MLRO) | €1.500–€4.000 p.a. (kann auch Firma tragen) |
| Pflicht-Trainings (anti-MLA, Sanctions-Update) | €2.000–€4.000 p.a. |
| **Total Jahr 1** | **€91.500–€151.000** |

### Outsourced MLRO als Übergangsoption

Malta hat einen Markt für "MLRO-as-a-Service" (CSB Group, KPMG Malta, BDO Malta, einige boutique-firms). Kosten: **€36.000–€72.000 p.a.** für ein Standardpaket (4–8h pro Woche, escalation incl.). MGA toleriert outsourced MLRO bei kleinen Operatoren — der MLRO muss aber dennoch resident sein (oder mindestens substantial-presence-erfüllen) und Fit-and-Proper-approved.

### Bewertung des "benannt, Malta, 11 Jahre" — aber nicht eingestellt

Das ist eine Red Flag. Eine Person, die "benannt" aber nicht "vertraglich gebunden" ist, kann den MGA-Approval-Prozess nicht durchlaufen — MGA verlangt employment-contract oder service-agreement als Anhang zum Personal Declaration Form. "Benannt aber nicht eingestellt" heißt operativ: **nicht da**.

**Risiko-Tag: HIGH** — Antragsblocker.

---

## 7. PEP/Sanctions-Screening Level 2+ — Threshold falsch gesetzt

### Best Practice und MGA-Erwartung

PEP und Sanctions-Screening sind in fast allen EU-AML-Regimen **risk-based** und **bei Onboarding für ALLE Kunden** Pflicht — nicht erst ab einem Volumen-Threshold. Der Hintergrund:

- **Sanctions:** Wer auf einer OFAC/EU/UN-Liste steht, darf gar nicht erst Kunde werden — unabhängig von €1 oder €1.000.000. Screening ab "€500/Monat" ist **regulatorisch unzulässig**.
- **PEP:** Risikobasiert. EU AMLD 5/6: Identifikation bei Onboarding ist Pflicht; **Enhanced Due Diligence (EDD)** wird angewendet, sobald PEP-Status festgestellt. Das ist eine Workflow-Eskalation, kein Volumen-Gate.

### Was im Konzept steht ist falsch

"PEP-Check ab Level 4 (>€1.000/Mo.)" bedeutet: Wenn ein PEP für €999/Monat spielt, wird er nicht gescreent. Das ist nicht haltbar — weder rechtlich (FIAU Implementing Procedures Part II, Section 4.4) noch operationell.

### Korrekte Konfiguration

| Maßnahme | Trigger |
|---|---|
| Sanctions Screening | **JEDER** Account bei Onboarding + daily ongoing |
| PEP Identification | **JEDER** Account bei Onboarding + ongoing on list-updates |
| EDD on PEP | Automatisch bei Identification, unabhängig vom Volumen |
| Source of Wealth | Risk-based: bei PEP-Status, bei HRT, bei Volumen >€2.000/Mo. |
| Source of Funds | Bei jeder größeren Einzahlung (typischerweise >€2.000 single) |

**Risiko-Tag: HIGH** — fundamentales Compliance-Missverständnis.

---

## 8. Responsible Gaming Integrationen (OASIS/GAMSTOP)

### OASIS DE (Bundesländer-Sperrsystem)

**OASIS** ist das zentrale Spielersperrsystem nach §8 GlüStV 2021, betrieben vom Regierungspräsidium Darmstadt (im Auftrag der GGL — Gemeinsame Glücksspielbehörde der Länder). Anbindung ist nur möglich für **Inhaber einer deutschen Glücksspiel-Erlaubnis** (Online-Casino / Virtuelle Automaten / Online-Poker / Sportwetten gemäß GlüStV 2021).

- **MGA-Lizenz reicht nicht.** Ohne deutsche Erlaubnis kein OASIS-Zugang und keine Pflicht zur Anbindung.
- **Aber:** Operator ohne deutsche Lizenz, der DE-Spieler annimmt, agiert ohnehin im Graubereich/Schwarzmarkt. Seit 1.7.2021 ist Online-Glücksspiel in DE ohne GGL-Lizenz unzulässig, Strafbarkeit nach §284 StGB bleibt im Raum.
- **GameBet-Plan:** Wenn DACH-Markt geplant ist OHNE deutsche Lizenz, ist die OASIS-Integration faktisch leere Markenpflege — und das Geschäft selbst ist in DE nicht legal.

### GAMSTOP UK

**GAMSTOP** (https://www.gamstop.co.uk) ist das nationale Selbstausschluss-Register UK. Pflicht für **UKGC-lizenzierte** Operatoren (LCCP 3.5.5). Anbindung erfordert UKGC-Lizenzdaten als Vertragsgrundlage.

- Wenn UKGC erst Phase 2 (2028), dann ist GAMSTOP-Integration **vor 2028 wertlos** (man kann sich technisch anbinden, GAMSTOP würde aber keinen Live-Connector ohne UKGC-Lizenz freischalten).
- "Geplante GAMSTOP-Integration" für 2026 ist ein Konzept-Fehler.

### Was geht stattdessen für MGA-only Operator?

- **eIGA-Compliance** (Maltese Player Protection Directive) — Pflicht, intern umsetzbar.
- **Pan-EU-Selbstausschluss** ist KEINE harmonisierte Infrastruktur. Es gibt keine cross-jurisdictional self-exclusion-DB außerhalb von GAMSTOP/OASIS und einigen einzelländischen Systemen (ROFUS Dänemark, Spelpaus Schweden, ADM Italien, Cruks Niederlande, DGOJ Spanien — jeweils nur für eigene Lizenznehmer).
- **Internes Selbstausschluss-Register** Pflicht — das ist machbar und MGA-konform.

### Reality Check (alle 60 Min, nicht wegklickbar)

MGA-Player-Protection-Directive verlangt Reality-Checks, aber Frequenz ist nicht starr 60 Minuten. UKGC fordert 60 Minuten als Default; MGA empfiehlt "appropriate intervals". 60 Minuten ist konservativ ok, aber **muss konfigurierbar** sein, weil DE GlüStV andere Anforderungen hat (5-Sekunden-Mindestabstand bei Slots, Einzahlungslimit €1.000 cross-operator etc.) — was GameBet ohne DE-Lizenz nicht erfüllen muss, aber im DACH-Marketing klären müsste.

**Risiko-Tag: MEDIUM** — Konzept ist nicht falsch, aber zwei der drei genannten Integrationen sind in der Anfangsphase nicht aktivierbar. Marketing-Behauptung ohne operative Substanz.

---

## 9. Banken-Kündigung & De-Risking-Risiko

### Realität 2024–2026

MGA-lizenzierte Operatoren erleben weltweit hohe **De-Risking-Raten** durch klassische Banken. Hintergründe:

- EU-Banken (insbes. DE, FR, AT, IT) haben Gambling-MCC 7995 oft als "elevated risk" eingestuft. Korrespondenzbanken (USD-Clearing) lehnen Gambling-Operatoren häufig direkt ab.
- Maltesische Banken: Bank of Valletta + APS + HSBC Malta haben in den letzten 5 Jahren mehrfach Gambling-Konten massenhaft gekündigt (HSBC Malta hat 2017–2019 quasi alle iGaming-Konten ausgehebelt).
- Litauische Banken (Šiaulių Bankas, Citadele) sind selektiv offen, aber post-Wirecard skeptisch.
- Alternative: Schweizer Privatbanken, Liechtensteinische Banken, einige LATAM (gestaltbar, aber teuer und mit FATCA/CRS-Komplexität).
- Spezial-Banken: **Praxis Cashier**, **Lemonway**, **Cashflows**, **Banking Circle** — alle mit Gambling-Vertical-Akzeptanz, oft mit Premium-Pricing.

### Kündigungsrate empirisch

Branchen-Stats (informell, aber konsistent über mehrere iGaming-Verbände): **20–35% der MGA-Operatoren erleben in den ersten 24 Monaten mindestens eine Banking-Beziehung-Kündigung**. Bei kleinen Operatoren mit limitiertem Volumen ist die Quote sogar höher, weil sie aus Banking-Sicht "viel Risk, wenig Revenue" sind.

### Empfehlung

- **Multi-Banking Day 1**: Mindestens 2 Bankbeziehungen plus 1 EMI als Backup. Niemals single-banked.
- **Iberischer / Skandinavischer Mid-Tier-Bank-Pfad** zusätzlich zur Malta-Bank (Sabadell, Bankinter, Lansforsakringar, Nordnet — selektiv).
- **Reserve-Liquidität** für 60–90 Tage Operations halten, falls Konto über Nacht gekündigt wird (üblich: 30-Tage-Kündigungsfrist, gelegentlich sofort).

### Konkret für GameBet

Bei €200k Startkapital ist Multi-Banking-Setup eng. Lithuanian-EMI-Plan würde immerhin als "Banking-Backup" über die Safeguarding-Banking-Beziehung dienen — aber die EMI selbst hat das gleiche De-Risking-Problem auf der Korrespondenzbank-Ebene.

**Risiko-Tag: HIGH** — wahrscheinliche Banking-Kündigung in 12-24 Monaten, kein Backup-Plan dokumentiert.

---

## 10. Top-3 Payment/Compliance-Schwächen

### 1. MLRO + Key Function Holders nicht real besetzt → Antragsblocker

Ohne unterschriebene Verträge + Fit-and-Proper-fähige Personen für **alle 7 Key Function Roles** wird der MGA-Antrag nicht ausgegeben. €35k Compliance-Budget reicht für GENAU EINEN Senior MLRO 4–5 Monate brutto — und das ist 1 von 7 KFH. Das ist ein operatives K.O.

### 2. Litauische EMI-Lizenz im Plan = Kapitalvernichtung

EMI-Setup-Kosten + Run-Rate übersteigen das gesamte Startkapital um Faktor 3–5×. Das ist nicht "ambitioniert", das ist nicht finanzierbar. Wallet-Funktionalität muss via existierendem EMI-Partner (Cashier-as-a-Service) gelöst werden.

### 3. AML Rule-Set lückenhaft — Sanctions/Geo/BRA fehlen vollständig

Ohne Sanctions-Screening (Onboarding + daily) ist die Lizenz nicht zu halten. Der MGA-Audit (in den ersten 6 Monaten nach Lizenzerteilung — "Initial Compliance Visit") würde die Lücken markieren und potentiell zur Conditional License oder Suspension führen.

---

## 11. Empfehlung: GO / GO mit Conditions / NO-GO

**Verdikt: NO-GO im aktuellen Setup. Re-Plan erforderlich vor MGA-Antrag.**

Begründung:
- Compliance-Budget €35k ist um **Faktor 8–12× unterfinanziert** für den behaupteten Scope (MGA-Lizenz + EMI + 3 PSPs + 5-Level-KYC + 12 AML-Rules + Jumio + S3 Object Lock + HSM + eCOGRA).
- Realistisches Year-1-Compliance-Budget (ohne EMI): **€280.000–€420.000** (MLRO €100k + Compliance-Officer €70k + KYC-Tooling €30k + AML-Vendor €25k + MGA-Fees €25k + Auditor €25k + Legal-Retainer €40k + sonstiges €15–30k).
- Mit EMI-Plan additional: **+€500–750k im Year 1.**

### Conditions, unter denen das doch zu GO wird

1. **EMI-Lizenz-Plan streichen.** Wallet via Cashier-Provider (Praxis, Lemonway, Cashflows).
2. **Compliance-Budget realistisch auf €300k+ aufstocken** ODER **Phase-1-Modell mit Curaçao-Lizenz** (deutlich günstiger, dafür aber DACH-Markt-Problem) als Bridge.
3. **MLRO + Compliance-Officer real einstellen** bevor Antrag eingereicht wird (Verträge in der MGA-Application).
4. **AML Framework auf vollen FIAU-IP-II-Standard ausbauen** (Sanctions + PEP-für-alle + BRA + CRP + SoW/SoF-Distinktion + Geo-Risk).
5. **PSP-Strategie auf 1 Acquirer + 1 APM-Aggregator** zurückskalieren.
6. **OASIS/GAMSTOP-Marketing-Claim entfernen** oder explizit als "Phase 2 nach DE/UK-Lizenz" markieren.
7. **Banking-Plan: mindestens 2 Bankbeziehungen + 1 Cashier-EMI als Backup, dokumentierte De-Risking-Contingency**.

Wenn diese 7 Conditions erfüllt sind → **GO mit Conditions**. Aktuell jedoch: **NO-GO**.

---

## 12. Folgefragen

1. **MLRO-Status real:** Ist die genannte 11-Jahre-Person ein LOI oder ein signed Service Agreement? Hat die Person bereits eine FIAU-MLRO-Approval für andere Operatoren?
2. **Komplettes Key Function Holders Mapping** — wer ist Compliance Officer, RG Key Person, IT Security KFH, Finance KFH? Lebensläufe vorhanden?
3. **Protection Level Player Funds**: Basic / Medium / High? Ist eine Bank Guarantee oder ein Trust aufgesetzt?
4. **Cashier-Provider-Evaluation:** Wurde Praxis/Lemonway/Cashflows als Alternative zur Eigenwallet evaluiert?
5. **Sanctions-Screening-Vendor**: ComplyAdvantage / Refinitiv World-Check / Dow Jones — welcher, mit welchem List-Refresh-SLA?
6. **PSP-Term-Sheets**: Existieren bereits Letter of Intent von Nuvei und Paysafe? Mit welchen Rolling-Reserve-Konditionen und MDR?
7. **Business Risk Assessment (BRA)** als schriftliches Dokument: existiert, oder ist es ein Konzept-Item für später?
8. **DE-Marktstrategie:** GameBet zielt auf DACH ohne deutsche Lizenz — was ist der Plan? Geofencing-Strategie, B2B-only-Modell, oder Ignorier-Risiko und SOA?
9. **Korrespondenzbank-Kette**: Welche Korrespondenzbank wird die USD/EUR-Settlements clearen? Hat die Eigentums-Banking-Bank dies bereits bestätigt für iGaming-MCC?
10. **eCOGRA-Roadmap:** geplant heißt was — Q3 2026? 2027? eCOGRA-Audit kostet typischerweise €25–50k. Budgetiert?
11. **HSM-Strategie:** AWS CloudHSM, Thales Luna, oder Azure Dedicated HSM? Key-Ceremony-Plan? FIPS 140-2 Level 3 nötig (für PCI HSM)?
12. **PCI DSS Scope:** Volle PCI DSS Level 1 oder über SAQ-D + Tokenization (häufig via PSP)?

---

**Final Statement:** Das Konzept liest sich wie ein Compliance-Wunschzettel ohne Realitätsabgleich auf Budget, Zeit und Substanz. Die einzelnen Bausteine (MGA + EMI + 3 PSPs + 5-Level-KYC + 12 AML-Rules + Jumio + eCOGRA) sind alle in sich plausibel — aber **die Aggregation übersteigt €200k Startkapital um eine Größenordnung**. Realistische Re-Planung mit fokussiertem Scope-Cut (kein EMI Day 1, 1 PSP zum Launch, MLRO + AML komplett erst, dann erweitern) ist Voraussetzung für einen tragfähigen MGA-Antrag.
