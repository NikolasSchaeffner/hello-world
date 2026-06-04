# Hausarbeit: Softwaremodellierung – Virtueller Lerntrainer

## Inhaltsverzeichnis
1. Einleitung
   - 1.1 Problemstellung und Relevanz
   - 1.2 Zielsetzung der Arbeit
   - 1.3 Aufbau und Vorgehensweise
2. Theoretische Grundlagen
   - 2.1 Software-Engineering und modellbasierte Entwicklung
   - 2.2 Die Unified Modeling Language als Standard
   - 2.3 Struktur- und Verhaltensdiagramme im Überblick
     - 2.3.1 Use-Case-Diagramm
     - 2.3.2 Klassendiagramm
     - 2.3.3 Aktivitätsdiagramm
     - 2.3.4 Sequenzdiagramm
   - 2.4 Funktionale und nichtfunktionale Anforderungen
   - 2.5 Anforderungsanalyse als Brücke zur Modellierung
   - 2.6 Zwischenfazit
3. Anwendungsteil: Modellierung des Lerntrainers
   - 3.1 Einordnung und methodisches Vorgehen
   - 3.2 Aufgabe A1 – Use-Case-Diagramm
     - 3.2.1 Akteure und Use Cases
     - 3.2.2 Beziehungen und ihre Begründung
     - 3.2.3 Textuelle Ausarbeitung eines zentralen Use Cases
   - 3.3 Aufgabe A2 – Klassendiagramm (BOM)
     - 3.3.1 Klassen und die abstrakte Oberklasse Person
     - 3.3.2 Komposition oder Aggregation – eine bewusste Abwägung
     - 3.3.3 Fachliche und technische Sicht – eine bewusste Grenze
   - 3.4 Aufgabe A3 – Aktivitätsdiagramm
   - 3.5 Aufgabe A4 – Sequenzdiagramm
4. Diskussion
   - 4.1 Kritische Würdigung der Ergebnisse
   - 4.2 Modellierungswerkzeuge – eine Einordnung aus der Praxis
   - 4.3 Fazit und Ausblick

---

## 1 Einleitung

### 1.1 Problemstellung und Relevanz

Drei Studienbriefe, zwei laufende Module, ein voller Kalender — und kein Gefühl dafür, ob man eigentlich vorankommt. Wer im Fernstudium steht, kennt das. Keinen Hörsaal, der den Takt vorgibt. Keine Kommilitonen am Nebentisch, an denen man sich orientieren könnte. Man organisiert alles selbst. Ich erinnere mich an ein Semester, in dem ich drei Module parallel belegt hatte und irgendwann schlicht nicht mehr wusste, was ich wann gelernt hatte und was noch fehlte. Abgebrochen habe ich nicht — aber nahe dran war ich.

Das ist kein Einzelfall. Das Deutsche Zentrum für Hochschul- und Wissenschaftsforschung beziffert die Abbruchquote im Bachelorstudium auf rund 28 Prozent; als einer der Hauptgründe gilt die mangelnde Passung zwischen den Voraussetzungen der Studierenden und den Anforderungen des Studiums. Auf der anderen Seite wächst der Markt für digitale Lernhilfen: Statista prognostiziert dem weltweiten E-Learning-Plattformmarkt bis 2028 ein Volumen von rund 63 Milliarden Euro bei einem jährlichen Wachstum von gut vier Prozent. Aus dieser Schnittmenge — realer Bedarf hier, wachsender Markt dort — entstand die Idee, einen virtuellen Lerntrainer zu modellieren, der den Studienverlauf aktiv begleitet.

Diese Perspektive bringe ich nicht nur als Studierender mit. Von 2001 bis 2003 erlernte ich am schulischen Berufskolleg die Grundlagen der Informations- und Kommunikationstechnik; zwischen 2004 und 2007 folgte eine Ausbildung zum IT-Systemelektroniker bei einem mittelständischen IT-Dienstleister in Mannheim, mit Einsätzen im First- und Second-Level-Support, in Rollout-Projekten für öffentliche Einrichtungen und in Industrieunternehmen. Von 2015 bis 2020 arbeitete ich dann bei einem IT-Consulting-Unternehmen im Raum Ludwigshafen: Consultants koordinieren, Aufträge akquirieren, und mit Modellierungswerkzeugen wie Enterprise Architect und Innovator umgehen. Aus dieser Praxis weiß ich ziemlich genau: Software-Projekte scheitern selten an der Technik. Sie scheitern an unklaren Anforderungen am Anfang.

Der CHAOS-Report der Standish Group, der seit 1994 IT-Projekte international auswertet, benennt präzise Anforderungen als einen der drei wichtigsten Erfolgsfaktoren überhaupt — und bestätigt damit genau das, was mir in der Praxis wiederholt begegnet ist. Genau dort setzt das Modul Software-Engineering I an, und genau dort setzt diese Arbeit an.

### 1.2 Zielsetzung der Arbeit

Ziel dieser Hausarbeit ist die softwaretechnische Modellierung eines virtuellen Lerntrainers gemäß Alternative A der Aufgabenstellung. Vier aufeinander aufbauende UML-Modelle stehen dabei im Mittelpunkt: ein Use-Case-Diagramm für die Funktionssicht, ein Klassendiagramm als Business Object Model für die Datenstruktur, ein Aktivitätsdiagramm für einen ausgewählten Anwendungsfall und ein Sequenzdiagramm für die Erstellung einer Mentoren-Auswertung. Die Aufgabe verlangt ausdrücklich nicht nur formal korrekte Notation, sondern eine nachvollziehbare Herleitung und Begründung jedes Modellartefakts. Diesem Anspruch folgt die vorliegende Arbeit.

Drei Teilziele: Erstens soll das theoretische Fundament von UML und modellbasierter Entwicklung so aufgebaut werden, dass die späteren Modellierungsentscheidungen daraus ableitbar sind — nicht als dekoratives Vorwissen, sondern als inhaltliche Begründungsgrundlage. Zweitens werden die vier Diagramme entworfen, dokumentiert und in jeder substanziellen Entscheidung begründet, einschließlich der Alternativen, die ich im Arbeitsprozess verworfen habe. Drittens wird das Ergebnis kritisch eingeordnet und in einen Praxiskontext gestellt, der über die reine Modulanforderung hinausweist.

### 1.3 Aufbau und Vorgehensweise

Die Arbeit gliedert sich in vier Hauptkapitel. Kapitel 2 legt das theoretische Fundament: Software-Engineering und modellbasierte Entwicklung, die UML als Standard, die vier verwendeten Diagrammtypen mit ihren Beziehungselementen und schließlich die Anforderungsanalyse, die als Scharnier zwischen fachlichen Anforderungen und Modellierung funktioniert. Ein Zwischenfazit schließt den theoretischen Teil ab.

Kapitel 3 bildet den Schwerpunkt. Hier entstehen die vier UML-Modelle Schritt für Schritt — mit ihren Akteuren, Vererbungsentscheidungen, Aggregations- und Kompositionsabwägungen, Ablauflogiken und Interaktionsszenarien. Bei jedem Modell steht neben dem Ergebnis auch der Weg dorthin, einschließlich der Sackgassen. Kapitel 4 würdigt die Ergebnisse kritisch und schließt mit Fazit und Ausblick.

---

## 2 Theoretische Grundlagen

### 2.1 Software-Engineering und modellbasierte Entwicklung

Was bedeutet es, Software „ingenieurmäßig" zu entwickeln? Balzert beschreibt das als systematische, planbare Herstellung, den Betrieb und die Pflege von Software — das Gegenteil von Drauflosprogrammieren. Dass dieser Anspruch nötig wurde, lehrte die sogenannte Software-Krise der späten 1960er-Jahre, in der Projekte reihenweise an Budget, Terminen und Qualität zerbrachen. Die Folgekonferenzen schufen die Disziplin, die bis heute den Rahmen strukturierter Softwareentwicklung bildet.

Gelöst ist das Problem damit aber nicht. Wer die historischen CHAOS-Daten der Standish Group liest, stellt fest: Nur etwa ein Drittel aller IT-Projekte gilt dort als uneingeschränkt erfolgreich. Diese Zahlen sind allerdings mit Vorsicht zu behandeln. Eveleens und Verhoef weisen in einer vielzitierten Analyse nach, dass die Standish-Definitionen methodisch angreifbar sind — Erfolg wird dort allein an der Schätzgenauigkeit von Kosten, Zeit und Funktionsumfang festgemacht, was die Quoten systematisch verzerrt. Was bleibt: Die grobe Tendenz ist breit belegt. Viele Projekte geraten in Schwierigkeiten. Die konkreten Prozentwerte sollte man nicht überstrapazieren; das Muster dahinter — unklare Anforderungen als Hauptursache — ist es, was zählt. Und genau das deckt sich mit dem, was mir aus der Berufspraxis vertraut ist.

Im Zentrum des Software-Engineerings steht das Modell. Ein Modell ist eine zweckgerichtete Abstraktion: Es blendet aus, was nicht zählt, und hebt hervor, worauf es ankommt. Balzert beschreibt das als Reduktion auf das Wesentliche. Was dabei nüchtern klingt, ist in der Praxis die eigentliche Herausforderung — denn was wesentlich ist, steht nirgends geschrieben. Das muss man selbst entscheiden, und meistens mehrmals.

Brandt-Pook und Kollmeier zerlegen die Softwareentwicklung in drei zusammenwirkende Sichten: Prozess, Methoden und Projektgeschehen. Die UML, mit der diese Arbeit operiert, ordnen sie eindeutig den Methoden zu. Der Lerntrainer ist dabei kein simples Programm, sondern ein Softwaresystem im eigentlichen Sinne — ein Verbund interagierender Komponenten, in dem Benutzer, Mentor, Administrator und das System selbst zusammenspielen. Warum dann vier verschiedene Diagrammtypen nötig sind, ergibt sich daraus direkt: Kein einzelnes Diagramm wäre in der Lage, diese Vielschichtigkeit einzufangen.

### 2.2 Die Unified Modeling Language als Standard

Die UML ist heute die Lingua franca der Modellierung — aber sie ist keine Erfindung am Reißbrett. In den 1990er-Jahren konkurrierten mehrere objektorientierte Notationen; bis Booch, Rumbaugh und Jacobson — die „drei Amigos", wie sie in der Literatur genannt werden — ihre Ansätze zusammenführten und die Object Management Group das Ergebnis 1997 zum Standard erhob. Eine Versöhnungsgeschichte aus einem handfesten Methodenstreit heraus. Verbindlich ist heute Version 2.5.1, an der ich mich bei der Notation orientiere.

Vierzehn Diagrammtypen umfasst die UML, grob aufgeteilt in Struktur- und Verhaltensdiagramme. Erstere zeigen den statischen Aufbau, letztere das dynamische Verhalten. Oestereich und Scheithauer erinnern daran, was der eigentliche Nutzen ist — nicht hübsche Kästchen, sondern die Möglichkeit, dass Fachseite und Entwicklung dieselbe Sprache sprechen. In meiner Zeit im IT-Consulting habe ich diesen Effekt mehrfach erlebt: Sobald ein Modell auf dem Tisch lag, sprachen alle plötzlich konkret über dieselben Dinge, statt aneinander vorbeizureden.

### 2.3 Struktur- und Verhaltensdiagramme im Überblick

Die vierzehn Diagrammtypen der UML zerfallen in zwei große Familien. Strukturdiagramme — allen voran das Klassendiagramm — halten den statischen Aufbau fest: Bausteine und ihre dauerhaften Beziehungen. Verhaltensdiagramme zeigen, was im System geschieht. Für den Lerntrainer ziehe ich aus beiden Familien: ein Strukturdiagramm für die Daten, drei Verhaltensdiagramme für Funktionen, Abläufe und Interaktion. Die folgenden Unterkapitel beschreiben jeden verwendeten Typ nach demselben Muster — Zweck, zentrale Notationselemente, Grenzen — damit die Modellierungsentscheidungen in Kapitel 3 daraus ableitbar sind.

#### 2.3.1 Use-Case-Diagramm

Das Use-Case-Diagramm beantwortet zwei Fragen: Wer nutzt das System? Und was kann es? Es geht zurück auf Jacobson, der die Methode Anfang der 1990er-Jahre etabliert hat und den Anwendungsfall bewusst an den Anfang jeder Analyse stellt — das System wird von außen gedacht, vom Nutzen her, nicht von der Technik. Oestereich und Scheithauer beschreiben es entsprechend als Einstieg jeder Anforderungsanalyse.

Die Notation ist bewusst sparsam: Akteur als Strichmännchen, Anwendungsfall als Ellipse, Systemgrenze als umschließendes Rechteck, Assoziation als schlichte Linie. Gerade diese Sparsamkeit ist seine Stärke — das Diagramm ist auch für Fachvertreter ohne Informatikhintergrund lesbar. Seine Grenze liegt genau dort: Über das Wie eines Ablaufs sagt es nichts. Dafür braucht es das Aktivitäts- oder Sequenzdiagramm.

Zwischen Anwendungsfällen lassen sich drei Beziehungen modellieren, die ich später gezielt einsetze: «include» für eine zwingend enthaltene Teilfunktion, «extend» für eine nur unter Bedingungen auftretende Erweiterung, Generalisierung für Spezialisierung. Diese drei auseinanderzuhalten ist erfahrungsgemäß die eigentliche Hürde — und sie entscheidet darüber, ob ein Diagramm etwas aussagt oder nur dekoriert.

#### 2.3.2 Klassendiagramm

Das Klassendiagramm ist das wichtigste Strukturdiagramm der UML. In der Analysephase heißt es Business Object Model, weil es die fachlichen Gegenstände abbildet und technische Details noch draußen lässt. Eine Klasse erscheint als Rechteck mit drei Feldern: Name, Attribute, Methoden. Für ein reines Analysemodell wie das BOM treten Sichtbarkeiten in den Hintergrund — hier zählt zunächst die fachliche Struktur.

Den Kern bilden die Beziehungen. Die Assoziation verbindet zwei Klassen als gleichberechtigte Partner; ihre Multiplizitäten legen fest, wie viele Objekte der einen Seite mit wie vielen der anderen in Beziehung stehen. Kleuker warnt in seinem Grundkurs Datenbankentwicklung nicht ohne Grund davor, Kardinalitäten zu unterschätzen: Ein Fehler hier pflanzt sich bis in die Datenbank fort, weil das Datenmodell direkt aus dem Klassendiagramm folgt. Für Teil-Ganzes-Beziehungen kennt die UML zwei Sonderformen: schwache Aggregation, bei der das Teil eigenständig fortbesteht, und starke Komposition, bei der das Teil mit dem Ganzen verschwindet. Die Vererbung verbindet Unterklasse mit allgemeinerer Oberklasse. Beim Lerntrainer entscheidet die Frage, ob ein Studienplan einen oder mehrere Lernpläne bündelt, über die gesamte Datenstruktur — eine Unterscheidung, die mir in Kapitel 3 noch Kopfzerbrechen bereiten wird.

#### 2.3.3 Aktivitätsdiagramm

Das Aktivitätsdiagramm bildet Abläufe ab und ähnelt auf den ersten Blick einem Flussdiagramm — kann aber deutlich mehr. Aktion als abgerundetes Rechteck, Kontrollfluss als Pfeil, Startknoten als ausgefüllter Kreis, Endknoten als umrandeter Kreis. Ein Entscheidungsknoten verzweigt den Fluss; ein passender Zusammenführungsknoten führt die Zweige wieder zusammen. Für echte Parallelität sorgen Fork und Join.

Besonders nützlich sind Schwimmbahnen, die jede Aktion einer verantwortlichen Rolle zuordnen und auf einen Blick zeigen, wer was tut. Für den Lerntrainer eignet sich das Diagramm ideal, um den Eingabe-Workflow einer Lernunit samt Fehlerfällen abzubilden. Seine Grenze: Der zeitliche Nachrichtenaustausch zwischen konkreten Objekten lässt sich damit nicht zeigen — dafür ist das Sequenzdiagramm zuständig.

#### 2.3.4 Sequenzdiagramm

Das Sequenzdiagramm stellt dar, wer wann welche Nachricht an wen schickt. Jedes beteiligte Objekt hat eine Lebenslinie — senkrechte gestrichelte Linie — auf der ein Aktivierungsbalken markiert, wann es gerade aktiv ist. Entscheidend ist die Unterscheidung der Nachrichtentypen: Eine synchrone Nachricht (gefüllte Pfeilspitze) lässt den Sender warten; eine asynchrone Nachricht (offene Pfeilspitze) erlaubt ihm, sofort weiterzuarbeiten. Diesen Unterschied habe ich anfangs unterschätzt — erst beim Modellieren wurde mir klar, wie sehr er das Systemverhalten prägt.

Seit UML 2 lassen sich mit kombinierten Fragmenten ganze Kontrollstrukturen abbilden: alt für sich gegenseitig ausschließende Alternativen, opt für einen optionalen Abschnitt, loop für Wiederholungen. Genau diese Fragmente brauche ich für die Mentoren-Auswertung — etwa um die Benachrichtigung wahlweise per SMS oder E-Mail abzubilden. Die Stärke des Diagramms liegt in der präzisen zeitlichen Reihenfolge; bei vielen Objekten wird es schnell unleserlich.

### 2.4 Funktionale und nichtfunktionale Anforderungen

Bevor Anwendungsfälle und Klassen entstehen, lohnt ein Blick auf die Natur der Anforderungen selbst. Funktionale Anforderungen beschreiben, was ein System leisten soll. Für den Lerntrainer ist „Das System ermittelt nach jeder eingegebenen Lernunit den Tages- und Wochensoll-Status" ein typisches Beispiel — diese Anforderung schlägt sich später unmittelbar in einem Anwendungsfall und einer «include»-Beziehung nieder. Nichtfunktionale Anforderungen beschreiben dagegen, wie gut das System seine Aufgaben erfüllt — Qualitätsmerkmale wie Leistung, Sicherheit, Benutzbarkeit, Wartbarkeit. Gerade sie werden in studentischen Arbeiten gern übersehen, obwohl sie über Erfolg oder Misserfolg eines Systems oft stärker entscheiden als die reine Funktionalität.

Für den Lerntrainer ergeben sich aus dem Kontext drei nichtfunktionale Anforderungen, die ich direkt begründe. Datenschutz: Lerndaten sind personenbezogen, weshalb der Administrator in meinem Modell bewusst keinen Zugriff auf individuelle Lernverläufe erhält — das schlägt sich in der Rollentrennung des Use-Case-Diagramms nieder. Antwortzeit: Die Soll-Berechnung läuft nach jeder Eingabe. Als Richtwert setze ich unter einer Sekunde an — gestützt auf Erkenntnisse zur Nutzerwahrnehmung: Wartezeiten über einer Sekunde stören den Interaktionsfluss spürbar, und bei einem Alltagswerkzeug, das mehrmals täglich genutzt wird, wird daraus schnell eine Abnutzungserscheinung. Eine App, die nach jeder Lerneingabe halbe Sekunden denkt, nervt — und wird irgendwann nicht mehr geöffnet. Benutzbarkeit: Die Zielgruppe sind nebenberuflich Studierende, die das Werkzeug zwischen Job und Lernen einsetzen und keine Einarbeitungszeit haben.

Diese Trennung ist kein Selbstzweck. Sie erklärt, warum manche Anforderungen direkt als Anwendungsfall sichtbar werden, während andere — etwa der Datenschutz — sich eher in Strukturentscheidungen des Klassendiagramms niederschlagen.

**Anforderungskatalog (Tab. 1):**

| ID | Art / Kategorie | Anforderung | Bezug im Modell |
|---|---|---|---|
| F1 | funktional | Der Benutzer kann Studien- und Lernpläne sowie Lernunits anlegen und bearbeiten. | Use Cases, Klassen Studienplan/Lernplan/Lernunit |
| F2 | funktional | Das System ermittelt nach jeder Eingabe den Tages- und Wochensoll-Status. | «include» Zwischenbericht; Aktivitätsdiagramm |
| F3 | funktional | Das System gibt bei erreichtem Soll ein Lob, bei Übererfüllung einen Bonus und bei über 40 h/Woche eine Warnung aus. | «extend»-Beziehungen |
| F4 | funktional | Der Mentor erstellt Auswertungen und wird über neue Anfragen benachrichtigt. | Sequenzdiagramm; Klasse Auswertung |
| NF1 | nichtfunktional – Sicherheit | Persönliche Lerndaten sind vor unbefugtem Zugriff geschützt; der Administrator erhält keinen Einblick. | Rollentrennung im Use-Case-Diagramm |
| NF2 | nichtfunktional – Leistung | Die Soll-Berechnung erfolgt nahezu verzögerungsfrei (Richtwert unter einer Sekunde). | Synchrone Nachricht im Sequenzdiagramm |
| NF3 | nichtfunktional – Benutzbarkeit | Die Bedienung ist ohne Einarbeitung für nebenberuflich Studierende verständlich. | Schlanke Use-Case-Struktur |
| NF4 | nichtfunktional – Wartbarkeit | Technische Dienste (z. B. Benachrichtigung) sind von der Fachdomäne getrennt. | Trennung BOM / NotificationService |

### 2.5 Anforderungsanalyse als Brücke zur Modellierung

Bevor das erste Diagramm entsteht, müssen Anforderungen erhoben, strukturiert und verstanden werden. Das IREB definiert diese Tätigkeit in seinem Lehrplan als systematische Vorgehensweise zur Ermittlung, Dokumentation, Prüfung und Verwaltung von Anforderungen. Pohl und Rupp bezeichnen sie als eine der anspruchsvollsten Tätigkeiten der Softwareentwicklung überhaupt — und begründen das damit, dass Anforderungen typischerweise implizit, widersprüchlich und volatil sind: Sie ändern sich, bevor das erste Modell fertig ist. Aus meiner Berufspraxis kann ich das bestätigen. Wo Anforderungen unscharf bleiben, multiplizieren sich Missverständnisse durch jede Projektphase — weil jede Entwicklerin, jeder Tester die Lücken anders füllt, und am Ende wundert sich jeder über alle anderen.

Die Standish Group berichtet seit Jahrzehnten, dass unklare Anforderungen einer der Hauptgründe für Projektabbrüche sind. Eine konsequente Anforderungsanalyse ist also keine bürokratische Pflichtübung, sondern eine Investition, die sich in jeder folgenden Phase rechnet. Genau deshalb nimmt diese Arbeit sich die Zeit, jeden Modellschritt aus den Anforderungen der Aufgabenstellung herzuleiten — statt direkt mit dem Zeichnen anzufangen.

### 2.6 Zwischenfazit

Drei Punkte tragen die spätere Modellierung.

Software-Engineering hat seinen Ursprung in einer konkreten Krise und eine empirisch belegbare Wirkung — auch wenn die konkreten CHAOS-Zahlen methodisch zu hinterfragen sind (Eveleens/Verhoef), bleibt das Muster: strukturloses Vorgehen kostet. Die UML ist der etablierte Standard, um diese Strukturarbeit zu visualisieren — nicht weil sie hübsch aussieht, sondern weil sie eine gemeinsame Sprache schafft, in der Fachlichkeit und Technik tatsächlich miteinander reden können (Oestereich/Scheithauer). Und die Anforderungsanalyse ist das Scharnier zwischen Idee und Modell: Wer sie überspringt, modelliert ins Blaue.

**Gegenüberstellung der vier UML-Diagrammtypen (Tab. 2):**

| Diagrammtyp | Sicht / Kategorie | Beantwortet die Frage… | Einsatz im Lerntrainer |
|---|---|---|---|
| Use-Case | Verhalten | Wer nutzt das System wofür? | Funktionsübersicht (A1) |
| Klassen | Struktur | Wie sind die Daten organisiert? | Datenmodell als BOM (A2) |
| Aktivität | Verhalten | Wie läuft ein Vorgang ab? | Use Case „Lernunit eingeben" (A3) |
| Sequenz | Interaktion | Wer kommuniziert wann mit wem? | Mentoren-Auswertung (A4) |

---

## 3 Anwendungsteil: Modellierung des Lerntrainers

### 3.1 Einordnung und methodisches Vorgehen

Bevor das erste Diagramm entstand, war zu klären, was der Lerntrainer leisten soll und in welchem Umfeld er steht. Er unterstützt Studierende beim Planen und Protokollieren des Lernfortschritts. Ein Lernplan bildet den Fortschritt eines Moduls ab, ihm sind Lernunits zugeordnet, und ein übergreifender Studienplan bündelt alles. Klingt simpel — ist es aber nicht, sobald man die Details ernst nimmt. Pohl und Rupp bezeichnen die Anforderungsanalyse zu Recht als eine der anspruchsvollsten Tätigkeiten überhaupt, weil implizite Anforderungen so lange unsichtbar bleiben, bis man anfängt zu modellieren und sie einem plötzlich entgegenpringen. Das hat sich hier bestätigt.

Um den Rahmen des Systems abzustecken, zeigt Abbildung 1 zunächst den Domänenkontext: die drei menschlichen Akteure, das zu modellierende System und den technischen Benachrichtigungsdienst als Umsystem. Diese Kontextsicht ist bewusst der detaillierten Modellierung vorangestellt, weil sie die Systemgrenze klärt — was gehört zum Lerntrainer, was liegt außerhalb? Der Benachrichtigungsdienst ist ein technisches Umsystem; er wird vom Lerntrainer genutzt, gehört aber nicht zur fachlichen Domäne und taucht deshalb im Business Object Model nicht auf.

Mein Vorgehen folgte der inneren Logik der vier Modelle: Zuerst das Use-Case-Diagramm für die Funktionssicht, dann das Klassendiagramm für die Datenstruktur, dann das Aktivitätsdiagramm für einen Ablauf, zuletzt das Sequenzdiagramm für ein Interaktionsszenario. Die vier müssen zusammenpassen — ein Akteur, der im Use-Case-Diagramm auftaucht, aber im Sequenzdiagramm fehlt, wäre ein Bruch. Wichtiger als das fertige Bild war mir stets die Begründung: Warum diese Lösung, und warum nicht eine andere?

### 3.2 Aufgabe A1 – Use-Case-Diagramm

#### 3.2.1 Akteure und Use Cases

Der Einstieg über Use Cases ist kein Zufall. Jacobson hat die Methode geprägt und stellt den Anwendungsfall bewusst an den Anfang — das System wird vom Nutzen her gedacht, nicht von der Technik. Genau so bin ich vorgegangen. Vier Akteure ließen sich aus den Anforderungen herauslesen.

Der Benutzer ist die Hauptfigur: Er legt Pläne an, erfasst Lernunits und ruft Auswertungen ab. Der Administrator pflegt nur systemweite Vorlagen und bekommt bewusst keinen Einblick in persönliche Lerndaten — eine Rollentrennung aus Datenschutzgründen, die sich später in NF1 niederschlägt. Der Mentor unterstützt einzelne Studierende und handelt in deren Namen. Und das System tritt selbst als Akteur auf, sobald es ohne menschliches Zutun reagiert — zum Beispiel wenn nach jeder Eingabe automatisch der Soll-Status berechnet wird.

Zuerst sah das Diagramm aus wie ein Spinnennetz. Jeder Akteur war mit fast jedem Use Case verbunden, Linien kreuzten sich, das Bild verlor seine Aussagekraft. Erst die Gruppierung der Use Cases in fünf Blöcke — Planverwaltung, Lernunit-Verwaltung, systemgesteuerte Fortschrittskontrolle mit Zwischenbericht/Lob/Bonus/Warnung, Auswertungen, Administration — brachte Ordnung. Diese Gruppierung stand in keiner Vorgabe; sie entstand aus der Notwendigkeit, das Diagramm lesbar zu halten. Der Effekt ist aus der Praxis bekannt: Sobald ein Modell unübersichtlich wird, fehlt ihm eine Strukturierungsebene.

#### 3.2.2 Beziehungen und ihre Begründung

An den Beziehungen entscheidet sich, ob ein Use-Case-Diagramm etwas aussagt oder nur dekoriert. Der Use Case „Lernunit eingeben" bindet „Zwischenbericht ermitteln" über «include» ein — das System berechnet nach jeder Eingabe zwingend den Soll-Status, das ist kein Sonderfall, sondern Kernlogik. Lob, Bonus und Überarbeitungswarnung dagegen hängen an «extend», weil sie nur unter Bedingungen auftreten.

Hier lag meine erste Sackgasse. Zunächst hatte ich auch diese drei als «include» modelliert, weil sie ja „dazugehören". Beim zweiten Hinsehen war das falsch — ein Lob erscheint nicht immer, sondern nur bei erreichtem Tagessoll. Aus meiner Zeit im IT-Support kenne ich solche bedingten Abläufe: Eine automatische Eskalation feuert nur dann, wenn ein Ticket eine Frist reißt, nicht bei jedem Ticket. Rupp et al. bestätigen die Faustregel: Bedingte Erweiterungen sind der Lehrbuchfall für «extend» — die Entscheidung, einen Anwendungsfall zu erweitern, liegt beim erweiternden, nicht beim Basis-Use-Case. Zwischen „Lernunit erstellen" und ihren beiden Varianten besteht eine Generalisierung, und den Mentor habe ich als spezialisierten Benutzer modelliert, der dessen Use Cases erbt und um eigene Rechte ergänzt.

**Beziehungstypen im Use-Case-Diagramm (Tab. 3):**

| Beziehung | Wann angemessen | Beispiel im Lerntrainer |
|---|---|---|
| «include» | Teilfunktion zwingend enthalten | „Lernunit eingeben" ➜ „Zwischenbericht ermitteln" |
| «extend» | Erweiterung nur unter Bedingung | „Zwischenbericht ermitteln" ➜ „Lob anzeigen" bei Tagessoll |
| Generalisierung | Spezialfall mit gemeinsamer Wurzel | „Lernunit erstellen" – individuell vs. aus Vorlage |
| Akteur-Vererbung | Rolle erbt Funktionen einer anderen | Mentor erbt vom Benutzer und ergänzt eigene Rechte |

#### 3.2.3 Textuelle Ausarbeitung eines zentralen Use Cases

Ein Use-Case-Diagramm zeigt das Was, nicht das Wie. Um einen Anwendungsfall wirklich zu durchdringen, empfiehlt die Literatur die textuelle Use-Case-Schablone — einen strukturierten Steckbrief mit Vorbedingung, Standardablauf, Alternativabläufen und Nachbedingung. Pohl und Rupp betonen, dass erst diese Ausformulierung die im Diagramm verdichteten Beziehungen überprüfbar macht: Was als «include»-Kante eingezeichnet ist, muss sich im Standardablauf wiederfinden; was als «extend» gilt, erscheint im Alternativablauf. Diesen Konsistenzcheck habe ich für den Use Case „Lernunit eingeben" gemacht — er ist der am häufigsten ausgeführte Anwendungsfall und bildet zugleich die Brücke zum Aktivitätsdiagramm in Abschnitt 3.4.

**Use-Case-Schablone „Lernunit eingeben" (Tab. 4):**

| Feld | Inhalt |
|---|---|
| Use Case | Lernunit eingeben |
| Ziel | Der Benutzer erfasst eine geleistete Lernsitzung; das System aktualisiert den Lernfortschritt und prüft die Soll-Vorgaben. |
| Primärakteur | Benutzer (Studierender) |
| Vorbedingung | Der Benutzer ist angemeldet und hat mindestens einen Lernplan angelegt. |
| Auslöser | Der Benutzer wählt „Lernunit eingeben". |
| Standardablauf | 1. Benutzer wählt eine bestehende Lernunit oder legt eine neue an. 2. Benutzer erfasst die Lerndauer der Sitzung. 3. System legt einen Lernvorgang an. 4. System ermittelt den Zwischenbericht (Tages-/Wochensoll). 5. System zeigt das Ergebnis an. |
| Alternativ-/Fehlerablauf | 2a. Dauer ≤ 0: System zeigt eine Fehlermeldung und kehrt zu Schritt 2 zurück. 4a. Tagessoll erreicht: System zeigt ein Lob. 4b. Wochensoll erreicht: System gewährt einen Bonus. 4c. Mehr als 40 h/Woche: System gibt eine Überarbeitungswarnung aus. |
| Nachbedingung | Der Lernvorgang ist gespeichert, der Lernfortschritt ist aktualisiert, der Benutzer hat eine Rückmeldung erhalten. |

### 3.3 Aufgabe A2 – Klassendiagramm (BOM)

#### 3.3.1 Klassen und die abstrakte Oberklasse Person

Beim Klassendiagramm bin ich an einer Stelle länger hängengeblieben: der Frage, wie Studierende und Mentoren zusammenhängen. Mein erster Reflex war, den Mentor von der Klasse Studierender erben zu lassen — schließlich ist ein Mentor ja auch irgendwie an der Hochschule. Doch je länger ich darüber nachdachte, desto schiefer wurde das. Ein Mentor ist kein besonderer Studierender. Ein Studierender ist kein angehender Mentor. Die beiden teilen Eigenschaften — Name, Kontaktdaten, Zugehörigkeit —, aber keiner ist dem anderen untergeordnet. Also habe ich diesen ersten Entwurf verworfen und stattdessen eine abstrakte Oberklasse Person eingeführt, von der beide erben. Person trägt das Attribut name, ist aber selbst nicht instanziierbar — ein Objekt im laufenden System ist immer konkret das eine oder das andere. Diese Lösung bündelt das Gemeinsame an einer Stelle, ohne eine falsche Hierarchie zu behaupten.

Der Rest ergab sich daraus. Studierender bekommt studienstart und studiengang sowie Referenzen auf genau einen Studienplan und beliebig viele Mentoren; Mentor ergänzt eintrittsdatum und fachrichtung. Der Studienplan bündelt die Lernpläne, der Lernplan trägt modulname, semester, ects und das Tages- sowie Wochensoll in Minuten. Soll in Minuten statt Stunden zu speichern, ist eine bewusste Entscheidung gegen Rundungsfehler bei der Fortschrittsberechnung — wer mit Zeiterfassungssystemen gearbeitet hat, weiß: Stimmt die Datenbasis nicht, sind auch die Auswertungen wertlos.

Knifflig wurde es bei der Lernunit: Sie beschreibt das Lehrmaterial, dokumentiert aber nicht das eigentliche Lernen. Dafür habe ich eine eigene Klasse Lernvorgang eingeführt — denn wer sich an einem Tag dreimal hinsetzt, erzeugt drei Lernvorgänge, nicht einen. Die Lehrmaterialarten sind als Enumeration LehrmaterialTyp ausgelagert, wie es die Aufgabenstellung verlangt.

#### 3.3.2 Komposition oder Aggregation – eine bewusste Abwägung

An keiner anderen Stelle des Modells habe ich so lange gegrübelt. Die Aufgabe verlangt mindestens eine Aggregation oder Komposition. Klingt nach Formalie — ist aber eine echte Entscheidung, und ich habe zwei Abende gebraucht, bis ich sie sauber begründen konnte.

Fangen wir mit dem klaren Fall an: Studienplan und Lernplan. Ein Lernplan ohne seinen Studienplan ergibt keinen Sinn. Wird der Studienplan gelöscht, müssen die Lernpläne mit verschwinden. Das ist Komposition im Lehrbuchsinn, und die ausgefüllte Raute bringt diese enge Bindung auf den Punkt.

Schwieriger — und ehrlich gesagt der Grund für die zwei Abende — war die Auswertung. Mein erster Entwurf hatte auch sie als Komposition am Mentor hängen. Logik: Der Mentor erstellt die Auswertung, also gehört sie ihm. Klingt plausibel. Ist aber falsch. Eine Komposition würde bedeuten: Verlässt ein Mentor die Hochschule und sein Datensatz wird gelöscht, reißt er sämtliche Auswertungen mit sich. Eine Auswertung dokumentiert den Lernfortschritt eines Studierenden — sie muss erhalten bleiben, unabhängig davon, ob der Mentor noch da ist oder nicht.

Am ersten Abend habe ich das schlicht übersehen. Erst am zweiten, als ich gedanklich durchspielte, was beim Löschen eines Mentors passiert, fiel der Groschen. Also Aggregation, hohle Raute. Das Teil überlebt das Ganze. Eine kurz erwogene Zwischenlösung — die Auswertung beim Löschen des Mentors einem Sammel-Account zuzuordnen — habe ich verworfen, weil sie das Modell unnötig verkompliziert hätte.

Bleibt die dritte Beziehung: Lernplan zu Lernunit. Komposition? Aggregation? Tatsächlich weder noch. Eine Lernunit-Definition lässt sich auch für sich betrachten, ohne an einem einzelnen Lernplan zu kleben — eine schlichte Assoziation reicht. Hätte ich hier eine Komposition gesetzt, hätte ich das Modell überspezifiziert. Erst als ich die drei Fälle nebeneinanderlegte — feste Komposition, lose Aggregation, neutrale Assoziation — hat es wirklich geklickt.

#### 3.3.3 Fachliche und technische Sicht – eine bewusste Grenze

Das Klassendiagramm ist hier als Business Object Model angelegt — es bildet bewusst nur die fachliche Domäne ab, also jene Gegenstände, über die auch ein Studierender oder Mentor sprechen würde: Lernplan, Lernunit, Auswertung. Oestereich und Scheithauer betonen, dass das Analysemodell von technischen Realisierungsdetails frei bleiben soll, weil diese erst in der Designphase hinzukommen. Das BOM ist kein Vorentwurf der Architektur, sondern ein Verständigungsinstrument zwischen Fachseite und Entwicklung — und für diese Funktion muss es verständlich bleiben.

Diese Trennung erklärt, warum ein technischer Hilfsdienst wie der Benachrichtigungsversand im BOM nichts zu suchen hat. Er ist kein fachliches Geschäftsobjekt, sondern ein Mittel zum Zweck. Im Sequenzdiagramm in Abschnitt 3.5 taucht er dennoch auf, weil dort der technische Ablauf gezeigt wird — im fachlichen Datenmodell bleibt er draußen. Wer beide Sichten vermischt, erhält ein Modell, das weder die Fachseite noch die Technik sauber bedient. Das ist ein Fehler, den ich in Projekten der Praxis mehr als einmal gesehen habe.

### 3.4 Aufgabe A3 – Aktivitätsdiagramm

Für das Aktivitätsdiagramm hatte ich die freie Wahl des Use Cases — und entschied mich für „Lernunit eingeben". Der am häufigsten ausgeführte Anwendungsfall, oft mehrmals täglich. Außerdem steckt in ihm mit den drei Soll-Prüfungen genug Entscheidungslogik, um ein Diagramm zu rechtfertigen, das mehr zeigt als eine schlichte Kette. Zwei Schwimmbahnen — Benutzer und System — trennen sauber, wer was tut.

Der Ablauf startet mit der Auswahl oder Neuanlage einer Lernunit. Dann erfasst der Nutzer die Lerndauer. Hier wollte die Aufgabe einen Fehlerfall — und der naheliegendste ist der offensichtlichste: Was, wenn jemand versehentlich null Minuten oder einen negativen Wert eingibt? Ein Entscheidungsknoten fängt das ab, zeigt eine Fehlermeldung und schickt den Nutzer zur Eingabe zurück. Erst eine gültige Dauer führt hinüber in die System-Bahn.

Die drei Soll-Prüfungen habe ich nicht in einen einzigen Sammel-Knoten gepackt. Mein erster Entwurf hatte das — ein Knoten, der „alle Ziele erreicht?" fragt. Zu grob. Tages-, Wochensoll und das 40-Stunden-Limit sind drei eigenständige Bedingungen mit drei eigenen Reaktionen — Lob, Bonus, Warnung — und genau das zeigt das Diagramm auch: drei getrennte Entscheidungsknoten, nacheinander. Zuerst entsteht ein Lernvorgang, dann wird der Zwischenbericht ermittelt, am Ende laufen alle Zweige in einem Endknoten zusammen.

### 3.5 Aufgabe A4 – Sequenzdiagramm

Das vierte Diagramm bildet den vorgegebenen Ablauf der Mentoren-Auswertung ab. Vier Lebenslinien: :Studierender, :System, :Mentor und ein :NotificationService, den das System erst im Verlauf erzeugt. Der Studierende bestellt synchron eine Auswertung — er wartet kurz auf die Bestätigung. Anschließend benachrichtigt das System den Mentor asynchron. Das war mir wichtig: Würde das System hier synchron warten, bliebe der Studierende blockiert, bis der Mentor reagiert — was Stunden dauern kann. Asynchron darf er weiterarbeiten.

Der Mentor lädt synchron die Lernvorgangsdaten, schreibt sein Feedback und speichert es; daraufhin erzeugt das System den NotificationService. Diese Kopplung ist bewusst so gewählt. Der NotificationService ist kein fachliches Geschäftsobjekt wie Lernplan oder Auswertung, sondern ein rein technischer Dienst für den Versand. Er taucht deshalb im BOM nicht auf — das BOM bildet absichtlich nur die fachliche Domäne ab. Im Sequenzdiagramm hingegen, das den technischen Ablauf zeigt, muss der Dienst sichtbar werden, und mit «create» ist klar dokumentiert, dass das System ihn instanziiert und damit für seinen Lebenszyklus verantwortlich ist.

Für die Benachrichtigung verlangte die Aufgabe „SMS oder E-Mail". Mein erster Gedanke war, das mit zwei separaten Nachrichten zu lösen — doch das hätte suggeriert, beide würden gesendet. Erst ein Blick in die OMG-Spezifikation klärte, dass ein alt-Fragment genau das Richtige ist, weil es genau eine der beiden Alternativen wählt. Den Timeout-Fall — der Mentor reagiert nicht rechtzeitig — habe ich in ein opt-Fragment mit erneuter Erinnerung gepackt. Zum Schluss ruft der Studierende die fertige Auswertung synchron ab.

---

## 4 Diskussion

### 4.1 Kritische Würdigung der Ergebnisse

Am Anfang stand eine textuelle Beschreibung, am Ende ein konsistentes UML-Modell aus vier Diagrammen. Jedes beleuchtet eine andere Seite des Lerntrainers, und doch greifen sie ineinander: Was das Use-Case-Diagramm an Funktionen verspricht, lösen Klassen-, Aktivitäts- und Sequenzdiagramm strukturell und dynamisch ein. Soweit das Ergebnis. Der Weg dorthin war holpriger, als diese Darstellung vermuten lässt.

Rückblickend war das Lehrreichste nicht das korrekte Zeichnen von Kästchen und Pfeilen, sondern die Entscheidungen dahinter — und was diese Entscheidungen über die Modellierungspraxis verraten. Im Use-Case-Diagramm war der Schlüssel die saubere Rollentrennung und die bewusste Wahl zwischen «include», «extend» und Generalisierung. Die Konsequenz dieser Unterscheidung ist nicht akademisch: Wer «include» und «extend» verwechselt, baut ein Diagramm, das Kernlogik von optionalem Verhalten nicht trennt — und dann entstehen downstream Architekturentscheidungen auf falscher Grundlage. Im Klassendiagramm war es die abstrakte Oberklasse Person und die Abwägung zwischen Komposition und Aggregation. Ehrlich gesagt hätte ich zu Beginn nicht gedacht, dass mich eine einzelne Raute so lange beschäftigen würde. Das Aktivitätsdiagramm zwang mich, einen realistischen Fehlerfall mitzudenken — nicht als Fußnote, sondern als gleichwertigen Zweig im Ablauf. Das Sequenzdiagramm schließlich machte mir den Unterschied zwischen synchroner und asynchroner Kommunikation greifbarer, als es jede Definition gekonnt hätte.

Was die eigentliche Erkenntnis aus alldem ist: Modellierung ist kein Abbildungsvorgang, bei dem man eine bekannte Realität in Kästchen überträgt. Sie ist ein Denkprozess, der Widersprüche sichtbar macht — oft zum ersten Mal. Der Mentor-Auswertung-Fall ist das beste Beispiel: Erst das Durchspielen des Lösch-Szenarios hat die falsche Kompositionsbeziehung aufgedeckt. Im Programmiercode hätte dieser Fehler lange verborgen bleiben können. Genau das ist der Wert früher Modellierung — nicht Vollständigkeit, sondern die Erzwingung von Präzision in einem Moment, in dem Korrekturen noch nichts kosten.

Eine ehrliche Einschränkung gehört dazu. Meine Modellierung beruht allein auf einer schriftlichen Vorgabe — in einem echten Projekt hätte ich mit künftigen Nutzern gesprochen, Prototypen gezeigt, nachjustiert. Aus der Berufspraxis weiß ich, wie viel sich an einem Modell ändert, sobald drei Fachexperten in einem Workshop draufschauen. Außerdem bleibt das Modell auf der fachlichen Analyseebene stehen. Die spannenden Architekturfragen — welches Entwurfsmuster sich für die Benachrichtigungslogik eignet, ob Observer oder Strategy, wie Goll et al. das für ähnliche Szenarien beschreiben — habe ich bewusst ausgeklammert; sie wären der logische nächste Schritt.

### 4.2 Modellierungswerkzeuge – eine Einordnung aus der Praxis

Ein Aspekt, der in der reinen Aufgabenstellung nicht vorkommt, in der Praxis aber über Erfolg und Frust entscheidet, ist die Wahl des Modellierungswerkzeugs. In meiner Zeit im IT-Consulting habe ich mit professionellen Werkzeugen wie Enterprise Architect und Innovator gearbeitet. Beide sind mächtig: Sie halten ein gemeinsames Repository, prüfen die Konsistenz zwischen Diagrammen und erlauben es, ein Modellelement einmal anzulegen und in mehreren Diagrammen wiederzuverwenden. Diese Konsistenzprüfung ist Gold wert, sobald ein Modell über wenige Diagramme hinauswächst — und deckt sich mit dem, was die Literatur zur Modellqualitätssicherung fordert.

Für eine Arbeit in diesem Umfang wäre ein solches Schwergewicht überdimensioniert. Leichtgewichtige Werkzeuge erstellen Diagramme entweder direkt grafisch oder — wie textbasierte Ansätze — aus einer Beschreibungssprache, was Versionsverwaltung und schnelle Änderungen erleichtert. Aber: Ein grafisches Werkzeug zeichnet bereitwillig auch eine fachlich falsche Beziehung. Die Konsistenz zwischen den vier Diagrammen habe ich hier manuell sichergestellt — genau die Arbeit, die ein professionelles Repository-Werkzeug automatisiert. Für eine nächste, größere Iteration des Lerntrainers wäre dieser Umstieg der logische Schritt.

### 4.3 Fazit und Ausblick

Was käme nach dieser Modellierung? Mir schweben eine gamifizierte Fortschrittsanzeige vor und eine datengestützte Empfehlung, welche Lernunit als Nächstes dran wäre. Sailer und Homner weisen in einer Metaanalyse einen kleinen, aber stabilen positiven Effekt von Gamification auf kognitive Lernergebnisse nach. Aber — und das ist entscheidend — nicht jede Belohnungslogik wirkt gleich. Die Selbstbestimmungstheorie von Deci und Ryan erklärt, warum: Belohnungsmechaniken wirken nur dann, wenn sie die Grundbedürfnisse nach Kompetenz und Autonomie bedienen, statt sie zu untergraben. Das Lob bei erreichtem Tagessoll, das ich bereits modelliert habe, funktioniert genau in diesem Rahmen — es signalisiert Kompetenz, ohne Druck zu erzeugen.

Der CHAOS-Report zeigt seit Jahrzehnten, dass die wenigsten Software-Projekte an Technik scheitern, sondern an unklaren Anforderungen. Eine Hausarbeit ist kein echtes Projekt — aber das methodische Vorgehen lässt sich übertragen: Erst Funktionen klären, dann Daten, dann Abläufe, dann Interaktionen. Wer diese Reihenfolge beherzigt, hat eine deutlich bessere Ausgangslage als jemand, der mit dem Programmieren beginnt.

Eines nehme ich auf jeden Fall mit: Modelle sind keine Formalität, die man abhakt, um endlich zum Programmieren zu kommen. Sie zwingen einen, Widersprüche zu sehen, bevor sie teuer werden. Allein dafür hat sich die Mühe gelohnt — die zwei Abende mit der Raute eingeschlossen.

---

## Literaturverzeichnis

Balzert, H. (2009): Lehrbuch der Softwaretechnik. Basiskonzepte und Requirements Engineering, 3. Auflage, Heidelberg.

Brandt-Pook, H./ Kollmeier, R. (2020): Softwareentwicklung kompakt und verständlich. Wie Softwaresysteme entstehen, 3. Auflage, Wiesbaden.

Deci, E. L./ Ryan, R. M. (1993): Die Selbstbestimmungstheorie der Motivation und ihre Bedeutung für die Pädagogik, in: Zeitschrift für Pädagogik, Band 39, Nr. 2, S. 223–238.

Eveleens, J. L./ Verhoef, C. (2010): The Rise and Fall of the Chaos Report Figures, in: IEEE Software, Band 27, Nr. 1, S. 30–36. DOI 10.1109/MS.2009.154.

Goll, J. et al. (2023): Architektur- und Entwurfsmuster der Softwaretechnik. Mit lauffähigen Beispielen in Java, 3. Auflage, Wiesbaden.

Heublein, U. et al. (2022): Die Entwicklung der Studienabbruchquoten in Deutschland (DZHW Brief 05|2022), Deutsches Zentrum für Hochschul- und Wissenschaftsforschung, Hannover. DOI 10.34878/2022.05.dzhw_brief.

IREB (2026): Lehrplan IREB Certified Professional for Requirements Engineering – Foundation Level, Version 3.3.

Jacobson, I. et al. (1992): Object-Oriented Software Engineering. A Use Case Driven Approach, Wokingham.

Kecher, C. et al. (2017): UML 2.5. Das umfassende Handbuch, 6. Auflage, Bonn.

Kleuker, S. (2016): Grundkurs Datenbankentwicklung. Von der Anforderungsanalyse zur komplexen Datenbankanfrage, 4. Auflage, Wiesbaden.

Kleuker, S. (2017): Grundkurs Software-Engineering mit UML. Der pragmatische Weg zu erfolgreichen Softwareprojekten, 4. Auflage, Wiesbaden.

Object Management Group (2017): OMG Unified Modeling Language (OMG UML), Version 2.5.1.

Oestereich, B./ Scheithauer, A. (2013): Analyse und Design mit der UML 2.5. Objektorientierte Softwareentwicklung, 11. Auflage, München.

Pohl, K./ Rupp, C. (2021): Basiswissen Requirements Engineering, 5. Auflage, Heidelberg.

Rumbaugh, J. et al. (2005): The Unified Modeling Language Reference Manual, 2. Auflage, Boston.

Rupp, C. et al. (2012): UML 2 glasklar. Praxiswissen für die UML-Modellierung, 4. Auflage, München.

Sailer, M./ Homner, L. (2020): The Gamification of Learning. A Meta-Analysis, in: Educational Psychology Review, Band 32, Nr. 1, S. 77–112.

Standish Group (1994): The CHAOS Report.

Statista (2024): E-Learning Plattform – Weltweit. Statista Marktprognose.

Winniewski, P. (2024): Grundlagenwissen der Software-Entwicklung. IT-Konzepte und Fachbegriffe für das Projektmanagement, Wiesbaden.
