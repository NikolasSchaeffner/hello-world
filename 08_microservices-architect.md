# Wave 2 / Agent 08 — Microservices Architect Report

**Konfidenz: 86%**

Begründung der fehlenden 14 %:
- Keine Einsicht in das tatsächliche Lasten-/Pflichtenheft, nur die im Briefing zusammengefassten Konzept-Fakten. Annahmen über Funktionsumfang basieren auf Branchenerfahrung.
- MGA-Zertifizierungsdetails (genauer eCOGRA-Scope für reine P2P-Skill-Wager-Plattform ohne RNG) variieren je nach Audit-Vertrag; ich extrapoliere aus aktuellen iGaming-Audits 2024–2025.
- DACH-Gehaltsannahmen sind Marktdurchschnitt 2025/26, individuelle Verträge können abweichen.
- Keine Verifikation der konkreten Riot/Valve/EA-ToS-Stände zum Datum 2026-05-15. Stand der Recherche im Bericht: Q4 2025 / Q1 2026 öffentlich bekannt.

Wo ich unter 95 % bin, sage ich es explizit. Wo ich >95 % bin, ist es ein hartes Architektur-Urteil.

---

## 1. Modular Monolith Realismus (4 Monate, 3–5 Devs, €55k)

**Verdikt: Unrealistisch in der präsentierten Form. Konfidenz 95 %.**

Der modulare Monolith ist als Architektur-Entscheidung für ein 3–5-Personen-Team **strategisch korrekt** — das ist die einzige Stelle, an der das Konzept architekturell schlüssig ist. Aber die Umsetzungs-Parameter passen nicht zueinander.

### Was in 4 Monaten mit 3–5 Devs realistisch baubar ist (Skill-Wager-MVP)

Realistisch (~600 Personentage Brutto, ~420 Netto nach Meetings/PRs/Sick/Onboarding):

| Modul | Aufwand (PT) | Bemerkung |
|---|---|---|
| Auth/Identity (KYC-Hooks, 2FA, Session) | 30–45 | Pflicht für MGA |
| Wallet/Ledger (double-entry, idempotent) | 60–80 | Allein eines der größten Module — Geldfluss-korrekt |
| Match-Lifecycle (create, accept, lock, settle) | 50–70 | Zustandsmaschine |
| Stake-Escrow + Pot/Rake-Engine | 30–40 | Inkl. Refund-Pfade |
| Steam/Riot-API-Adapter inkl. Resilience | 40–60 | Pro API einzeln, mit Retry/Caching |
| Screenshot-Upload + OCR-Adapter | 30–50 | Cloud-OCR wrap, kein eigenes Modell |
| Dispute-Workflow + Moderator-Cockpit | 50–80 | Inkl. SLA-Timer, Evidence-Storage |
| Payment-Provider-Integration (PSP) | 40–60 | Stripe/Mollie + SEPA + 3DS2 |
| KYC/AML-Adapter (Sumsub/Veriff/Onfido) | 25–40 | Adapter, nicht Eigenbau |
| Anti-Fraud-Hooks + Velocity-Rules | 30–50 | Regelbasiert, nicht ML |
| Audit-Log + S3 Object Lock | 15–25 | Append-only-Service |
| Admin-Backoffice (CRUD, Lookups, Refund) | 60–90 | Wird konsequent unterschätzt |
| Frontend Web (Lobby, Match, Wallet, KYC) | 80–120 | Reactive UI mit Live-State |
| Observability (Logs, Metrics, Traces) | 15–25 | OpenTelemetry-Setup |
| Tests + CI/CD + IaC + Pre-Prod | 40–60 | Pflicht für Zertifizierung |
| **Summe Minimum** | **~600 PT** | |
| **Summe Plausibel** | **~890 PT** | |

Realistisch verfügbar bei 4 Monaten × 4,5 FTE (Mittel von 3–5) × 16 produktiven Arbeitstagen/Monat = **288 Netto-PT**.

**Deckungslücke: ~50 %** im Best-Case, ~65 % im Plausibel-Case. Das ist nicht knapp, das ist strukturell unmöglich.

### Aufwands-Treiber (Top 5)

1. **Wallet/Ledger korrekt** — double-entry, idempotente Übergänge, Rake-Aufteilung, Refund-/Chargeback-Pfade, eCOGRA-prüfbare Bilanz. Dieses Modul allein verbraucht oft mehr Zeit als geschätzt — und Fehler hier sind existenzbedrohend.
2. **Dispute-Workflow** — der wichtigste UX-Pfad in P2P-Skill-Gaming. SLA-Timer, Evidence-Pipeline, Moderator-Tooling, Audit-Trail je Entscheidung. Wird im PDF mit "Stufe 3" abgetan.
3. **Admin-Backoffice** — fast immer unterschätzt. Ohne Backoffice ist die Plattform nicht betreibbar (KYC-Reviews, Auszahlungen freigeben, Bans, Refunds, Audit-Antworten an MGA).
4. **API-Adapter (Riot/Steam) mit Edge-Case-Handling** — Polling-Strategien, Match-ID-Disambiguation, Token-Refresh, Rate-Limit-Backoff, Cache-Invalidation. Aussagen "Sekunden, €0" sind nur die Happy-Path-Werte.
5. **Compliance-Reporting** — MGA verlangt regelmäßige Reports (Player Activity, Suspicious Transactions, Self-Exclusion-Register). Das ist Code, kein Excel.

### Realistischer Zeitplan

Für die im PDF skizzierte Plattform mit 3–5 Devs:
- **MVP-Soft-Launch (geschlossener Beta, keine Echtgeld-Auszahlungen):** 6–8 Monate
- **MVP mit MGA-Lizenz und Echtgeld:** 12–15 Monate (inkl. Lizenzierungs-Wartezeit, die parallel läuft aber nicht entfällt)

**4 Monate sind ~3× zu kurz.**

---

## 2. Tech-Stack-Heterogenität — Anti-Pattern oder gerechtfertigt?

**Verdikt: Klares Anti-Pattern für die Teamgröße. Konfidenz 97 %.**

Vier Sprachen (Node/Go, Rust/Go, Java/Kotlin, Python) plus Frontend (vermutlich TypeScript) bei 3–5 Devs:

- Jede Sprache hat eigene Toolchain (Build, Lint, Test, Deps, CI-Lane, Security-Scanning, Runtime-Images, SBOM).
- Jede Sprache braucht **mindestens 2 Personen mit Hands-on-Erfahrung**, sonst hat man Bus-Faktor 1.
- Bei 5 Devs × 5 Sprachen = jeder Dev müsste in 2–3 Sprachen produktiv sein, sofort.
- Ramp-up auf Rust: 3–6 Monate für eine Mid-Senior-Person, die aus Java/C# kommt. Das passt nicht in einen 4-Monats-MVP.

**Versteckte Botschaft:** Der Stack liest sich wie ein "Tools-of-the-Trade"-Showroom statt einer Engineering-Entscheidung — Rust für die Betting-Engine wirkt motiviert durch "muss schnell sein", nicht durch ein Profiling-Ergebnis. Bei den erwarteten Lastniveaus (5–80k MAU) ist Node, Go oder Kotlin für die Betting-Engine völlig ausreichend, und die Latenz-Vorteile von Rust werden vom Postgres-Commit dominiert.

### Empfohlener Stack für 3–5 Devs

**Eine Server-Sprache + ein Frontend-Stack:**
- Variante A: **Kotlin/Java (Spring Boot)** Backend + TypeScript-Frontend. Vorteil: stabilstes Ökosystem für regulierte Finanz-/Payment-Domänen, JDBC/JPA mit Transaktionen, gutes HSM-Tooling, sehr gute Auditierbarkeit. Nachteil: höhere Startup-Latenz, mehr Memory.
- Variante B: **TypeScript End-to-End** (Node/NestJS + React/Next). Vorteil: ein Skill-Set, schnellste Iteration. Nachteil: schwächer in CPU-bound Tasks, aber für diese Plattform irrelevant.
- Python **nur** als zweite Sprache für KYC/ML-Adapter, **nicht** als eigener Service.

**FTE-Realismus für den Briefing-Stack (heterogen):** 8–12 FTE über 4 Monate, davon mindestens ein Senior pro Sprache. Mit 3–5 Devs ist es eine garantierte Tech-Debt-Fabrik.

---

## 3. eCOGRA-Zertifizierung Realismus

**Verdikt: Im PDF unterspezifiziert und zeitlich nicht eingeplant. Konfidenz 80 %** (eCOGRA-Scoping ist case-by-case, daher nicht 95 %).

### Was eCOGRA bei einer Skill-P2P-Wager-Plattform prüft

- **RNG-Zertifizierung:** Bei reinem P2P-Skill-Wager ohne House-Outcomes ist RNG-Zertifizierung **nicht der Hauptpfad**. Aber sobald die Plattform Matchmaking, Bracket-Generierung, oder Tie-Breaker zufällig durchführt, gibt es RNG-Touchpoints.
- **Mathematische Integrität:** Rake-Berechnung, Pot-Verteilung, Refund-Logik. Quellcode-Review + Reproduzierbare Test-Vektoren.
- **Wallet-Isolation:** Player Funds Segregation (Trust-Account-Modell), getrennt von Operating Funds. **Banking-Setup-Vorbedingung**, nicht reine Software.
- **Match-Validation-Integrität:** Wie wird ein Ergebnis manipulationssicher festgestellt? Dies ist bei Skill-P2P die zentrale Audit-Frage, und hier ist das 3-Stufen-Modell ein Schwachpunkt (siehe §4).
- **Responsible Gaming:** Limit-Setting, Self-Exclusion, Reality-Checks, GAMSTOP-Äquivalent. Pflichtfunktionen, im PDF nicht erwähnt.
- **Sicherheits-/Pen-Test-Anforderungen:** ISO 27001-nah, oft separater Pen-Test erforderlich.

### Zeit & Kosten (Marktwerte 2025)

- **Pre-Audit-Vorbereitung:** 2–3 Monate (Dokumentation, Test-Vektoren, Architektur-Beschreibung, Change-Management-Prozess)
- **Audit-Durchführung:** 3–6 Monate (initial), oft länger bei P2P-Spezifika weil weniger Vorlagen existieren
- **Kosten:** €40k–€120k für die Erstzertifizierung (gestaffelt: Scope, Sprachen, Iterations-Findings, Re-Audit-Runden), plus jährliche Re-Zertifizierung
- **Technische Vorbedingungen, die VOR Audit-Start stehen müssen:**
  - Komplette Source-Control mit auditbarem Branching-Modell
  - Reproducible Builds (gleicher Commit → gleicher Artifact-Hash)
  - Append-only Audit-Log (✓ S3 Object Lock erfüllt das)
  - Vollständige Test-Coverage für Geldfluss-Pfade
  - Separation of Duties zwischen Dev und Prod-Deployment
  - HSM für signing keys und Wallet-Schlüssel
  - Dokumentierte Incident-Response- und Change-Management-Prozesse
  - **MGA-Lizenz oder mindestens MGA-Process aktiv** — eCOGRA zertifiziert nicht im Vakuum

**Realistischer Gesamtzeitrahmen Plattform-MVP fertig → eCOGRA-Sign-off:** 9–15 Monate **nach** Code-Fertigstellung. In der PDF-Timeline ist eCOGRA ein Bullet-Point ohne Phase — das ist ein **kritischer Plan-Fehler**.

---

## 4. Match-Validation 3-Stufen-System — Produktion-Risiko

**Verdikt: Stufe 1 ist fragil-stabil, Stufe 2 ist tickende Bombe, Stufe 3 ist unterbudgetiert. Konfidenz 92 %.**

### Stufe 1 — Steam/Riot API

- **Vorteil:** Konkret, deterministisch, fälschungssicher solange die API selbst integer ist.
- **Risiko:** Single Point of Failure (siehe §5). Kein dokumentierter Fallback.
- **Operative Realität:** Match-IDs auf Riot/Steam sind nicht immer 1:1 mappbar zu User-Eingaben (Lobby-Codes existieren oft nicht öffentlich, Custom-Games sind teils nicht via öffentlicher Match-History sichtbar). Heißt: selbst Stufe 1 hat Edge-Cases die Code brauchen.

### Stufe 2 — Screenshot + OCR + Gegner-Bestätigung

Das ist **der schwächste Punkt der gesamten Architektur**.

- **Manipulationsanfälligkeit:** Photoshop, gefälschte In-Game-Overlays, Browser-DevTools-Edit, gerenderte Fake-Screenshots aus Replay-Tools. Es gibt keine OCR-Engine die das zuverlässig erkennt. Tesseract: bricht bei Anti-Aliasing-Schriften. AWS Textract / Google Vision / Azure Form Recognizer: liest den Text korrekt, prüft aber nicht ob das Bild echt ist.
- **Image-Forensik:** ELA (Error Level Analysis), Metadata-Check, Perceptual Hashing gegen bekannte Templates — ist machbar, kommt aber im PDF nicht vor und ist ein eigenes Subsystem mit ML.
- **Gegner-Bestätigung als Sicherheits-Layer:** funktioniert nur, wenn die Gegner nicht kollaborieren. Bei Match-Fixing oder Smurf-Schemen ist genau das gegeben.
- **DSGVO bei Screenshots:**
  - In-Game-Names (oft Klarnamen oder identifizierbare Aliase) sind personenbezogene Daten.
  - Hintergrund-Inhalte (offene Discord-Fenster, andere Spieler-Namen, Streamer-Overlays mit Gesichtern) erfordern Datenminimierung.
  - Pflicht: automatisches Cropping/Redaction auf den relevanten Score-Bereich vor OCR, Aufbewahrungsfrist max. 30 Tage post-Dispute, Recht-auf-Vergessenwerden umsetzbar.
  - OCR-Anbieter-Auswahl mit DPA: AWS Textract (EU-Region möglich), Azure Form Recognizer (EU-Region) — ja. Google Vision (US-zentriert, EU-Daten-Pfad komplexer).
- **Empfehlung Engine:** **Azure AI Document Intelligence (vormals Form Recognizer)** oder **AWS Textract** — beide bieten EU-Hosting, DPA, und ausreichende Genauigkeit für strukturierte In-Game-Scoreboards. **Nicht** Google Vision wegen Datentransfer-Komplexität, **nicht** Tesseract wegen Qualität.

### Stufe 3 — Moderator-Review

**Skalierungs-Realität:**
- Bei 80.000 MAU und realistischen 5–15 % Disputes/Edge-Cases (PDF-Annahme 10–20 % ist eher hoch, aber bei P2P realistisch im Hoch-Risiko-Bereich): **4.000–12.000 Disputes/Monat**.
- €1–3 pro Dispute ist **deutlich zu niedrig kalkuliert**. Eine seriöse manuelle Review (Evidence lesen, Chat-History, Game-Replay, ggf. beide Parteien anhören, dokumentieren, ggf. eskalieren) braucht 10–30 Minuten. Bei Tier-1-Outsourcing (Philippinen, Osteuropa) €4–8 pro Review brutto. Bei DACH-Inhouse €15–40.
- Realistische Kosten bei 8.000 Disputes/Monat × €5 = **€40.000/Monat**. Bei DACH-Staff × €20 = **€160.000/Monat**.
- Bei dem im PDF skizzierten Revenue-Modell frisst das die Marge auf.
- **4-Stunden-SLA bei 8.000 Disputes/Monat:** verlangt mindestens 3–5 FTE Moderator:innen rund-um-die-Uhr.

---

## 5. Drittanbieter-API-Abhängigkeiten (Riot, Steam) als Single-Point-of-Failure

**Verdikt: Existenzielles Geschäfts-Risiko. Konfidenz 96 %.**

### Riot Games

- **Riot Developer ToS** verbieten explizit "use of the Riot API in connection with gambling, betting, or wagering". Stand bekannt aus früheren Versionen, geprüft öffentlich verfügbar bis 2024/2025.
- **Wahrscheinlichkeit Cease-and-Desist:** Sehr hoch, sobald die Plattform sichtbar wird und Marketing schaltet. Riot hat in der Vergangenheit aktiv Skin-Gambling-Sites verfolgt.
- **Konsequenz:** API-Key-Sperrung, ggf. Production-Key-Antrag schon im Onboarding rejected. Phase 1 (LoL) ist damit **strukturell gefährdet**.

### Steam

- Steam Web API ist offener, aber GSLT/Match-History-Endpoints können rate-limitiert oder deprecated werden. Steam hat in der Vergangenheit ohne Vorwarnung Endpoints abgeschaltet (siehe CS:GO Inventory History).
- CS2 Match-Data über offizielle API ist begrenzt; viele Stats kommen über 3rd-party Aggregatoren (FACEIT, Leetify), was eine zusätzliche Abhängigkeitsebene einzieht.

### Architektur-Konsequenz

Stufe 1 ist nicht 100 % deterministisch verfügbar. **Es muss zwingend einen Fallback geben** auf Stufe 2/3, der aber wiederum die OCR-/Moderator-Probleme erbt. Im PDF ist kein API-Ausfall-Szenario adressiert.

**Empfehlung:**
- Erste Spieltitel-Auswahl auf die mit den **kommerziell freundlichsten APIs** begrenzen (FACEIT API hat kommerzielle Tarife, Battlefy, Toornament).
- Riot/Valve-Direktintegration nicht als Single-Source-of-Truth designen, sondern als one-of-many Evidence-Provider.
- Schriftliche kommerzielle Zustimmung von Riot **vor** Investitionsentscheidung einholen. Ohne diese Zusage ist Phase 1 ein Glücksspiel.

---

## 6. Screenshot-OCR DSGVO + Skalierungs-Realismus

Bereits in §4 detailliert. Zusammenfassung:

- **DSGVO-Pflichten:**
  - DPIA (Datenschutz-Folgenabschätzung) Pflicht, weil systematische Verarbeitung von User-Content mit potenziell personenbezogenen Daten.
  - Auftragsverarbeitungsvertrag (AVV/DPA) mit OCR-Provider.
  - EU-Region für Verarbeitung.
  - Automatisches Redaction von Hintergrund-Inhalten vor Persistierung.
  - Löschfristen klar definiert (max. 30 Tage post-Resolution, gesetzliche Aufbewahrungsfrist für Audit überlagert das ggf.).
- **Skalierung:**
  - OCR-API-Kosten: AWS Textract ca. $1.50 per 1.000 pages, Azure ca. $1.00 per 1.000. Bei 8.000 Disputes/Monat = €10–15 pro Monat OCR-API-Kosten. Vernachlässigbar.
  - **Der teure Teil sind die Menschen dahinter**, nicht die OCR-API.
- **Latenz:** OCR selbst <2s, aber End-to-End Dispute-Lifecycle ist Stunden, nicht Sekunden. Das passt zur 4h-SLA, aber nicht zu User-Erwartung "schnelle Auszahlung".

---

## 7. Kafka / HSM / S3 Object Lock — Overkill oder Pflicht?

### Apache Kafka

**Verdikt: Überdimensioniert für MVP. Konfidenz 94 %.**

- Kafka braucht: ZooKeeper oder KRaft, mind. 3 Broker für HA, Schema Registry, Connect, ggf. Streams/ksqlDB. Operative Mindest-Komplexität für eine Person mit Kafka-Erfahrung: 0,3–0,5 FTE Dauer-Pflege.
- Bei 3–5 Devs ohne dedizierten Platform-Engineer: **operatives Risiko hoch**.
- **Alternativen für MVP:**
  - **Postgres + LISTEN/NOTIFY + Outbox-Pattern** — reicht bis 100k Events/Stunde locker, ist ACID, kein zusätzliches System.
  - **Redis/Valkey Streams** — leichtgewichtig, aber kein Replay/Compaction wie Kafka.
  - **NATS JetStream** — gutes Mittelfeld, deutlich einfacher als Kafka.
  - **AWS SQS/SNS oder Azure Service Bus** — managed, kein Ops-Aufwand.
- **Empfehlung:** Postgres-Outbox + NATS oder Managed Cloud Queue für MVP. Kafka frühestens bei Series A, wenn ein Platform-Team da ist.

### HSM

**Verdikt: Cloud-HSM reicht für eCOGRA. Konfidenz 80 %** (eCOGRA-Vorgaben können je nach Audit-Vertrag dediziertes HSM verlangen).

- **AWS CloudHSM** (~$1.45/h pro HSM = ~€1.000/Monat pro HSM, plus 2. HSM für HA = ~€2.000/Monat) oder **Azure Dedicated HSM** (höher: ~€3–4k/Monat). Beide sind FIPS 140-2 Level 3.
- **Azure Key Vault Premium** (managed HSM-backed) ist die kosteneffiziente Variante (~€800/Monat für moderate Nutzung) und ist in der Regel ausreichend für iGaming-Plattformen, die keine PCI-DSS-Level-1-Card-Storage betreiben (denn das outsourct man an den PSP).
- Dediziertes Hardware-HSM on-prem (Thales, Utimaco): €30k+ CAPEX + Maintenance. **Nicht nötig** wenn der Audit das nicht explizit verlangt — und für eine Cloud-First-Plattform ist das auch architektonisch deplatziert.
- **Bestätigung mit eCOGRA vor Architektur-Fix einholen.**

### AWS S3 Object Lock

**Verdikt: Architektonisch korrekt, MGA-konform, kostenseitig harmlos. Konfidenz 90 %.**

- WORM-Storage via Object Lock + Compliance Mode + Legal Hold + Versioning erfüllt die Append-only / Tamper-Evident-Anforderung von MGA und eCOGRA.
- **Aber:** S3 Object Lock allein ist kein vollständiger Audit-Trail. Es fehlt:
  - Hash-Chain oder Merkle-Tree-Signatur über die Log-Einträge (gegen "ich habe einen Eintrag nie geschrieben")
  - Signierung mit HSM-Key
  - Regelmäßige Replikation in Off-Region für Disaster Recovery
- **Latenz:** S3 PUT mit Object Lock ist ~50–200ms. Kein Realtime-Pfad. Korrekt asynchron via Outbox/Queue.
- **Kosten:** bei 80k MAU und ~1 KB pro Audit-Event × 100 Events/User/Monat = 8 GB/Monat. S3 ~€0.20/Monat. **Skaliert problemlos.** PUT-Requests sind der Hauptkostentreiber (~€5/Monat/Mio. Requests).

---

## 8. Anti-Collusion / Anti-Smurf-Detection technisch

**Verdikt: Fundamental ungelöst in der Branche. Konfidenz 95 %.**

- **Match-Fixing zwischen befreundeten Spielern** ist in P2P-Skill-Gaming **das** Strukturproblem. Lösung erfordert:
  - Soziales Graph-Modeling (wie oft spielen User A und B gegeneinander, wie hoch sind die Stakes, wie symmetrisch sind die Outcomes über Zeit)
  - Bayesian-Anomaly-Detection auf Win-Rate-Diskrepanzen vs. Skill-Rating
  - Manuelle Investigations-Pfade
  - Restriktionen: keine Wiederholungs-Matches gegen denselben Gegner innerhalb Zeitfenster, Cooldowns, Stake-Cap pro Paar
- **Smurf-Detection:**
  - Device-Fingerprinting (FingerprintJS Pro adressiert das, aber mit signifikanter False-Positive-Rate bei legitimen Multi-User-Haushalten und Privacy-Browsern)
  - Behavioral Biometrics (Mausbewegungen, Tipprhythmus)
  - In-Game-Skill-Indikatoren via API (LoL Rank, CS Premier Rating) als Cross-Check
- **VPN-Detection** trifft 10–20 % legitime User (Privacy-bewusste, Reisende, Firmen-Netze). Blanket-Blocking ist nicht möglich. Risiko-basiertes Adaptive-Gating ist nötig.

**Operative Realität:** Das ist ein eigenes Sub-Produkt. **Für MVP nicht baubar.** Auch große, etablierte Skin-Trading-/Skill-Plattformen kämpfen kontinuierlich damit (FACEIT, Challengermode, Battlefy).

**Empfehlung MVP:**
- Sehr enge Stake-Limits (z.B. max. €25/Match)
- Manuelle Review aller Auszahlungen >€100 in der Beta-Phase
- Soft-Launch in einer kleinen Community, in der Reputation existiert
- Volle Anti-Collusion-Pipeline erst Phase 2/3

---

## 9. CTO-Lücke + Hire-Realismus

**Verdikt: Der größte Personalrisiko-Punkt im gesamten Konzept. Konfidenz 97 %.**

- **Ohne CTO ist die Tech-Stack-Auswahl bereits getroffen worden** — das ist genau die Entscheidung, die ein CTO normalerweise nach Team-Constraints kalibriert. Der präsentierte Stack reflektiert das (siehe §2).
- **DACH-Gehälter 2026 (realistisch, brutto inkl. AG-Anteil):**
  - Mid-Senior Backend Engineer (5–8 Jahre): €85k–€115k/Jahr = €7k–€10k/Monat
  - Senior Backend (8+ Jahre): €110k–€150k/Jahr = €9k–€12k/Monat
  - Staff/Principal (FinTech/iGaming-Erfahrung, regulierte Domäne): €140k–€190k/Jahr = €12k–€16k/Monat
  - CTO (mit Lizenzierungs-Erfahrung): €150k–€220k Base + Equity = €13k–€18k/Monat
  - Junior (1–3 Jahre): €55k–€75k/Jahr = €4,5k–€6,5k/Monat
- **PDF-Annahme "€5–10k/Monat"** ist Junior bis Lower-Mid. Damit baut man **keine** regulierte Geld-Plattform.
- **Realistische Personalkosten 4 Monate, 4 Devs (1 Lead/Senior + 2 Mid + 1 Junior):**
  - Lead Senior: 4 × €11k = €44k
  - 2 × Mid: 4 × €8k × 2 = €64k
  - 1 × Junior: 4 × €6k = €24k
  - **Summe: €132k Personal allein** — bereits 2,4× über dem €55k-Budget
- Plus CTO oder externer Tech-Lead/Architekt für die ersten 3 Monate: weitere €30k–€60k.

---

## 10. Tech-Budget-Realismus

**€55k für 4 Monate Tech-MVP einer regulierten iGaming-Plattform ist nicht knapp, es ist eine Größenordnung daneben. Konfidenz 96 %.**

### Realistische Tech-Kosten 4 Monate

| Kostenposten | Untergrenze | Plausibel | Bemerkung |
|---|---|---|---|
| Personal (4 Devs Mid-Mix, 4 Mon.) | €120k | €160k | siehe §9 |
| CTO/Tech-Lead extern (4 Mon., 50 %) | €40k | €70k | Pflicht ohne festen CTO |
| Cloud-Infrastruktur (dev+staging+prod) | €4k | €10k | inkl. RDS, S3, Cloud-HSM |
| HSM (CloudHSM × 2 für HA) | €4k | €8k | siehe §7 |
| OCR-API-Verbrauch | €0.5k | €1.5k | gering |
| KYC/AML-Provider (Sumsub/Veriff) | €4k | €10k | min. Setup + Volumen |
| PSP-Setup + Onboarding | €5k | €15k | je nach PSP |
| Pen-Test (Pflicht für MGA-Submission) | €15k | €35k | unabhängiger Anbieter |
| Sec-Audit / Source-Code-Review | €10k | €25k | inkl. Findings-Loop |
| eCOGRA Pre-Assessment + Audit-Start | €20k | €60k | nur Anfangskosten |
| Tooling (GitHub Enterprise, Datadog, Linear, etc.) | €4k | €8k | für 5 Devs |
| Legal/Compliance-Beratung Tech-bezogen | €10k | €25k | DPIA, ToS, AGB, AVV |
| Lizenzkosten (MGA-Application separat) | €0k | €0k | nicht Tech-Budget |
| **Summe** | **€236k** | **€427k** | |

**Realistischer Tech-MVP-Aufwand bis Soft-Launch: €250k–€430k.** Der präsentierte Budget-Posten ist um den Faktor **5–8** zu niedrig.

---

## 11. Top-3 technische Killer-Risiken

### Risiko 1 — Riot/Valve ToS-Sperre für Phase 1

**Wahrscheinlichkeit: hoch (>60 %).**
**Impact: existenzgefährdend** — Phase-1-Spieltitel sind die gesamte Launch-Strategie.
**Mitigation:** Schriftliche kommerzielle Zustimmung vor Investition. Wenn nicht erhältlich: Pivot auf FACEIT-API-Partnership oder Tournament-Aggregatoren-API.

### Risiko 2 — Match-Validation-Manipulation (Stufe 2 + Collusion)

**Wahrscheinlichkeit: sehr hoch (>80 %) — passiert in der Branche routinemäßig.**
**Impact: laufende Liquiditätsabflüsse + Reputationsverlust + Lizenz-Risiko.**
**Mitigation:** Stufe 2 für MVP entweder weglassen (nur Spiele mit API) oder massive manuelle Review-Quote akzeptieren. Anti-Collusion-Pipeline gehört in den Kern, nicht in eine Spätphase.

### Risiko 3 — Budget/Timeline-Mismatch bricht das Team

**Wahrscheinlichkeit: nahezu sicher bei den präsentierten Parametern.**
**Impact: Tech-Debt-Spirale, Burnout, Compliance-Lücken, MGA-Audit-Findings, Re-Build nötig nach 12 Monaten.**
**Mitigation:** Realistisches Re-Budgeting (Faktor 5–8 auf Tech), Realistische Timeline (Faktor 3), oder Scope-Reduktion auf einen einzelnen Spieltitel + ein einziges Land + Hard-Limits auf Stakes.

---

## 12. Empfehlung: GO / GO mit Conditions / NO-GO

### NO-GO in der aktuellen Form. Konfidenz 92 %.

In den aktuellen Parametern (€55k Tech-Budget, 4 Monate, 3–5 Devs, 4-Sprachen-Stack, kein CTO, Phase-1-Spieltitel mit ToS-Risiko, Stufe-2-Validation als Produktiv-Pfad, Apache Kafka aus dem Stand) ist das Projekt nicht auslieferbar.

### Bedingter GO möglich, wenn ALLE folgenden Conditions erfüllt sind:

1. **CTO-Hire vor weiterer Investition** mit Erfahrung in regulierten Echtgeld-Plattformen.
2. **Tech-Budget realistisch auf €250k–€430k angehoben** für den Tech-MVP-Pfad, oder Scope drastisch reduziert (siehe 6).
3. **Timeline auf 9–12 Monate** bis Soft-Launch und 12–15 Monate bis MGA-Lizenz-Echtgeld.
4. **Tech-Stack konsolidiert auf 1 Backend-Sprache + TypeScript-Frontend.** Kein Rust/Java/Python-Mix.
5. **Schriftliche kommerzielle API-Zustimmung von Riot und Valve** liegt vor Investitionsentscheidung vor — oder Phase 1 wird auf FACEIT/Tournament-API gepivotiert.
6. **MVP-Scope reduziert auf:** 1 Spieltitel mit stabiler API, 1 Land (Malta-Lizenz-Land oder DACH-skill-game-konform), max. €25 Stake pro Match, manuelle Auszahlungs-Reviews >€100.
7. **Kafka durch Postgres-Outbox + NATS/Managed Queue ersetzt.**
8. **Stufe-2-Screenshot-Validation aus Phase 1 entfernt.** Erst Phase 2 nach proven Operations.
9. **Anti-Collusion-Minimal-Pipeline ist Pflicht-Modul** im MVP (Velocity-Limits, Pair-Cooldowns, manuelle Auszahlungs-Reviews), nicht "spätere Phase".
10. **eCOGRA Pre-Engagement-Gespräch vor Architektur-Freeze** zur Scope-Klärung.

### Sonst NO-GO. Wenn die Conditions nicht akzeptiert werden, wird das Projekt entweder
(a) nie auslieferbar,
(b) als unsichere/unlizenzierbare Plattform launchen und durch Regulator-Action oder Match-Fixing-Verluste sterben, oder
(c) das Team in der ersten Welle abbrennen und ein teurer Re-Build wird in 12 Monaten beauftragt.

---

## 13. Folgefragen

Falls Investment-Komitee weiter prüfen will, vor nächster Tranche zu klären:

1. **Riot/Valve schriftliche kommerzielle Lizenz vorhanden?** Wenn nein: Plan B mit FACEIT/Tournament-API durchkalkuliert?
2. **CTO-Hire-Pipeline:** wer ist im Anflug, welche regulierten-iGaming-Refs?
3. **eCOGRA-Pre-Assessment-Termin:** ist gebucht? Ergebnis vorhanden? Scope-Brief?
4. **MGA-Lizenzantrag-Stand:** eingereicht? Welche Klasse (B2C / Type 2 für Wetten)?
5. **PSP-Provider final entschieden?** Onboarding-Status, KYC-Tier-Architektur, Auszahlungs-Limits, Chargeback-Reservierung?
6. **Trust-Account für Player-Funds:** welche Bank, welches Land, welcher Vertragsstand?
7. **Anti-Collusion-Konzept** mehr als ein Bullet-Point? Wer modelliert das?
8. **Disputes-Operations-Plan:** wie viele Moderator:innen ab Launch, in welchem Land, mit welchen Tools, welche Eskalations-Pfade?
9. **Cloud-Provider entschieden** (AWS / Azure / GCP) und Region-Strategie inklusive Daten-Souveränität?
10. **Reproducible Builds + Audit-fähiger CI/CD-Pfad** bereits Setup oder noch zu bauen?
11. **DPIA und Datenschutz-Konzept-Stand?** Wer ist DSB (intern/extern)?
12. **Backup/Disaster-Recovery-RPO/RTO-Zielwerte** definiert?
13. **Versicherung (Cyber/Pro-Indemnity)** budgetiert? Üblich für iGaming-Plattformen.
14. **Bug-Bounty oder externes Pen-Test-Programm** geplant ab Launch?
15. **Source-Code-Escrow** für MGA-Audit-Anforderung?

---

**Schlussbemerkung:**
Die Architektur-Wahl "Modular Monolith" ist die einzige Stelle, an der dieses Konzept Engineering-Reife zeigt. Alles andere — Stack-Heterogenität, Budget, Timeline, Match-Validation-Realismus, API-Abhängigkeiten, fehlender CTO — zeichnet das Bild einer Konzeption, die **nicht von einem operativ erfahrenen Tech-Lead validiert wurde**. Das macht die wichtigste Empfehlung gleichzeitig zur einfachsten: **vor jeder weiteren Tranche ein CTO-Hire**, und dann das Konzept gemeinsam mit dieser Person neu kalibrieren. Alles andere ist Capital-at-Risk ohne Pfad zur Auslieferung.
