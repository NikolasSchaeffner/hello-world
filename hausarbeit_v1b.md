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

Drei Studienbriefe, zwei laufende Module, ein voller Kalender – und kein Gefühl dafür, ob man eigentlich vorankommt. Wer im Fernstudium steht, kennt diesen Zustand. Es gibt keinen Hörsaal, der den Takt vorgibt, keine Kommilitonen, an denen man sich orientieren könnte. Ich erinnere mich noch genau an ein Semester, in dem ich drei Module parallel belegt hatte und irgendwann schlicht den Überblick verlor – was ich gelernt hatte, was noch fehlte, welche Fristen liefen ab. Abgebrochen habe ich nicht, aber nah dran war es.

Das ist kein Einzelfall. Das Deutsche Zentrum für Hochschul- und Wissenschaftsforschung beziffert die Abbruchquote im Bachelorstudium auf rund 28 Prozent. Der Grund liegt selten an der Intelligenz; er liegt an der Struktur. Genau da setzt die zentrale Frage dieser Arbeit an: Wie lässt sich Struktur digital nachbilden, sodass sie Studierenden nicht bloß als Liste auf dem Smartphone sitzt, sondern als aktiver Begleiter funktioniert?

Parallel wächst der Markt für digitale Lernhilfen rasant. Statista prognostiziert dem weltweiten E-Learning-Plattformmarkt bis 2028 ein Volumen von rund 63 Milliarden Euro. Aus dieser Schnittmenge – echtem Bedarf auf der einen Seite, wachsendem Markt auf der anderen – entstand die Idee eines virtuellen Lerntrainers. Nicht ein neuer Kurs, nicht noch ein Learning-Management-System, sondern ein gezieltes Werkzeug, das den Studienverlauf strukturiert begleitet.

Diese Perspektive bringe ich nicht nur als Studierender mit. Von 2001 bis 2003 erlernte ich die Grundlagen der Informations- und Kommunikationstechnik an meinem schulischen Berufskolleg; anschließend folgte zwischen 2004 und 2007 eine Ausbildung zum IT-Systemelektroniker bei einem mittelständischen IT-Dienstleister in Mannheim. Dort arbeitete ich in First- und Second-Level-Support, in Rollout-Projekten für öffentliche Einrichtungen sowie in Industrieunternehmen. Von 2015 bis 2020 koordinierte ich bei einem IT-Consulting-Unternehmen im Raum Ludwigshafen Consultants, akquirierte Aufträge und wurde mit Modellierungswerkzeugen wie Enterprise Architect und Innovator vertraut. 

Aus dieser Praxis kenne ich die zentrale Einsicht: Software-Projekte scheitern nicht an der Technik. Sie scheitern an unklaren Anforderungen und fehlender Struktur am Anfang. Der CHAOS-Report der Standish Group, der seit 1994 internationale IT-Projekte auswertet, bestätigt das. Eine klare Aussage von Anforderungen – das ist einer der drei wichtigsten Erfolgsfaktoren überhaupt. Genau hier setzt das Modul Software-Engineering I an. Und genau hier setzt diese Arbeit an.

### 1.2 Zielsetzung der Arbeit

Ziel ist die softwaretechnische Modellierung eines virtuellen Lerntrainers gemäß Alternative A der Aufgabenstellung. Im Mittelpunkt stehen vier aufeinander aufbauende UML-Modelle: ein Use-Case-Diagramm für die Funktionssicht, ein Klassendiagramm als Business Object Model für die Datenstruktur, ein Aktivitätsdiagramm für einen ausgewählten Anwendungsfall und ein Sequenzdiagramm für die Erstellung einer Mentoren-Auswertung. 

Die Aufgabe verlangt ausdrücklich nicht nur die formal korrekte Notation. Sie verlangt eine nachvollziehbare Herleitung und Begründung jedes einzelnen Modellartefakts. Diesem Anspruch folgt diese Arbeit konsequent.

Konkret werden drei Teilziele verfolgt. Erstens wird das theoretische Fundament von UML und modellbasierter Entwicklung so dargestellt, dass die späteren Modellierungsentscheidungen aus ihm ableitbar sind – nicht umgekehrt. Zweitens entstehen die vier Diagramme nicht aus dem Nichts, sondern werden dokumentiert und in jeder substanziellen Entscheidung begründet, einschließlich der Alternativen, die ich verworfen habe. Drittens wird das Ergebnis kritisch gewürdigt und in einen Praxiskontext gestellt, der über reine Modulanforderungen hinausweist.

### 1.3 Aufbau und Vorgehensweise

Die Arbeit gliedert sich in vier Hauptkapitel. Kapitel 2 legt das theoretische Fundament: Software-Engineering und modellbasierte Entwicklung, die UML als Standard, die vier verwendeten Diagrammtypen sowie ihre Beziehungselemente. Ein eigener Abschnitt widmet sich der Anforderungsanalyse als Brücke zwischen fachlichen Anforderungen und später Modellierung.

Kapitel 3 bildet den Schwerpunkt. Hier entstehen die vier UML-Modelle Schritt für Schritt: erst das Use-Case-Diagramm mit seinen Akteuren und Beziehungen, dann das Klassendiagramm mit Vererbung und Aggregations-/Kompositionsentscheidungen, anschließend das Aktivitätsdiagramm zum Use Case „Lernunit eingeben" und schließlich das Sequenzdiagramm zur Erstellung der Mentoren-Auswertung. Bei jedem Modell wird die Entscheidung dargestellt, begründet und – wo sinnvoll – mit verworfenen Alternativen kontrastiert. Kapitel 4 würdigt die Ergebnisse kritisch und schließt mit Fazit und Ausblick.

---

## 2 Theoretische Grundlagen

### 2.1 Software-Engineering und modellbasierte Entwicklung

Was bedeutet es, Software „ingenieurmäßig" zu entwickeln? Balzert versteht darunter die systematische, planbare Herstellung, den Betrieb und die Pflege von Software. Das Gegenteil: Drauflosprogrammieren. Dieses Gegensatzpaar wurde zwingend notwendig nach der sogenannten Software-Krise der späten 1960er-Jahre, als Projekte reihenweise an Budget, Terminen und Qualität zerbrachen. Was danach entstand, war eine Disziplin – und diese Disziplin stellt heute den Rahmen für jede strukturierte Softwareentwicklung dar.

Doch hat diese Disziplin das Problem gelöst? Ein Blick in die historischen CHAOS-Daten zeigt: Nein. Nur etwa ein Drittel aller IT-Projekte gilt dort als uneingeschränkt erfolgreich. Allerdings gibt es hier einen wichtigen Vorbehalt. Eveleens und Verhoef weisen in einer vielzitierten Analyse nach, dass die Standish-Definitionen methodisch angreifbar sind – sie machen Erfolg allein an der Schätzgenauigkeit von Kosten, Zeit und Funktionsumfang fest und erzeugen dadurch verzerrte Erfolgsquoten. Für diese Arbeit folgt daraus eine Unterscheidung: Die grobe Tendenz – viele Projekte geraten in Schwierigkeiten – ist breit belegt. Die konkreten Prozentwerte sollte man nicht überstrapazieren.

Im Zentrum des Software-Engineerings steht das Modell. Ein Modell ist eine zweckgerichtete Abstraktion: Es blendet aus, was nicht zählt, und hebt hervor, worauf es ankommt. Balzert beschreibt das nüchtern als Reduktion auf das Wesentliche. Mich fiel beim Modellieren des Lerntrainers jedoch etwas anderes auf: Genau diese Reduktion ist der schwierigste Teil. Was wesentlich ist und was nicht – darüber gibt es keine Lehrbuchantwort. Das muss man selbst entscheiden, oft mehrmals.

Brandt-Pook und Kollmeier zerlegen Softwareentwicklung in drei zusammenwirkende Elemente: Prozess, Methoden und Projektgeschehen. Die UML, mit der diese Arbeit operiert, ordnen sie eindeutig den Methoden zu. Der Lerntrainer ist dabei kein simples Programm – er ist ein Softwaresystem im eigentlichen Sinne: ein Verbund interagierender Komponenten, in dem Benutzer, Mentor, Administrator und das System selbst zusammenspielen. Daraus folgt unmittelbar eine Konsequenz: Ein einzelnes Diagramm wird die Vielschichtigkeit eines Systems nie einfangen. Deshalb braucht es vier verschiedene Diagrammtypen.

### 2.2 Die Unified Modeling Language als Standard

Die UML ist heute die Lingua franca der Modellierung. Ihre Geschichte ist überraschend lebendig: In den 1990er-Jahren konkurrierten mehrere objektorientierte Notationen wild durcheinander, bis Booch, Rumbaugh und Jacobson – die „drei Amigos", wie sie in der Literatur genannt werden – ihre Ansätze zusammenführten. Die Object Management Group erhob das Ergebnis 1997 zum Standard. Das ist also nicht die Erfindung am Reißbrett, sondern das Resultat eines handfesten Methodenstreits.

Heute verbindlich ist UML 2.5.1, an der ich mich bei der Notation orientiere. Vierzehn Diagrammtypen umfasst die Sprache insgesamt, grob geteilt in Struktur- und Verhaltensdiagramme. Strukturdiagramme zeigen den statischen Aufbau. Verhaltensdiagramme zeigen das dynamische Verhalten. Für den Lerntrainer brauche ich aus beiden Lagern: ein Strukturdiagramm für die Daten, drei Verhaltensdiagramme für Funktionen und Abläufe.

Oestereich und Scheithauer erinnern an den eigentlichen Nutzen der UML. Nicht in hübschen Kästchen, sondern darin, dass Fachseite und Entwicklung endlich dieselbe Sprache sprechen. In meiner Zeit im IT-Consulting habe ich genau diesen Effekt mehrfach beobachtet: Sobald ein Modell auf dem Tisch lag, sprachen alle plötzlich konkret über dieselben Dinge. Vorher redeten sie aneinander vorbei.

### 2.3 Struktur- und Verhaltensdiagramme im Überblick

Die vierzehn Diagrammtypen der UML zerfallen in zwei große Familien. Strukturdiagramme – allen voran das Klassendiagramm – halten den statischen Aufbau fest: Bausteine und deren dauerhafte Beziehungen. Verhaltensdiagramme zeigen, was im System geschieht: wer es benutzt, wie ein Vorgang abläuft, wer wann mit wem kommuniziert. 

Für den Lerntrainer ziehe ich aus beiden Familien: ein Strukturdiagramm für die Daten, drei Verhaltensdiagramme für Funktionen, Abläufe und Interaktion. Die folgenden vier Unterkapitel beschreiben jeden Typ nach demselben Muster – Zweck, zentrale Notationselemente, Grenzen –, um die Modellierungsentscheidungen später ableitbar zu machen.

#### 2.3.1 Use-Case-Diagramm

Das Use-Case-Diagramm beantwortet zwei Fragen: Wer nutzt das System? Was kann es tun? Das Verfahren geht zurück auf Jacobson, der die Methode bereits Anfang der 1990er-Jahre etabliert hat. Eine zentrale Idee treibt sein Ansatz an: das System von außen denken, vom Nutzen her, nicht von der Technik. Oestereich und Scheithauer beschreiben es als Einstieg jeder Anforderungsanalyse.

Die Notation ist bewusst sparsam. Ein Akteur erscheint als Strichmännchen – eine Rolle außerhalb des Systems, ein Mensch oder ein anderes System. Der Anwendungsfall selbst: eine Ellipse. Die Systemgrenze: ein Rechteck, das alle Anwendungsfälle umschließt und das Innen vom Außen trennt. Eine einfache Linie verbindet Akteur und Anwendungsfall. Gerade diese Sparsamkeit ist die Stärke: Das Diagramm bleibt lesbar auch für Fachvertreter ohne Informatikhintergrund. Das ist zugleich seine Grenze – über das Wie eines Ablaufs sagt es nichts aus. Dafür sind Aktivitäts- oder Sequenzdiagramme zuständig.

Zwischen Anwendungsfällen lassen sich drei Beziehungen modellieren, die ich später gezielt nutze: «include» für eine zwingend enthaltene Teilfunktion, «extend» für eine nur unter Bedingungen auftretende Erweiterung und die Generalisierung für eine Spezialisierung. Diese drei auseinanderzuhalten ist erfahrungsgemäß die eigentliche Hürde – und sie entscheidet darüber, ob ein Diagramm etwas aussagt oder bloß dekoriert.

#### 2.3.2 Klassendiagramm

Das Klassendiagramm ist das wichtigste Strukturdiagramm der UML. In der Analysephase wird es Business Object Model genannt, weil es fachliche Gegenstände abbildet und technische Details noch außen vor lässt. Eine Klasse erscheint als Rechteck mit drei Feldern: Name, Attribute, Methoden. Jedes Attribut trägt einen Datentyp, jede Operation eine Signatur; Sichtbarkeiten (öffentlich, privat, geschützt) regeln den Zugriff. Für ein reines Analysemodell wie das BOM treten Sichtbarkeiten allerdings in den Hintergrund – hier zählt zunächst die fachliche Struktur.

Den Kern bilden die Beziehungen. Die Assoziation verbindet zwei Klassen als gleichberechtigte Partner; ihre Multiplizitäten legen fest, wie viele Objekte der einen Seite mit wie vielen der anderen in Beziehung stehen. Hier liegt eine Hürde. Kleuker warnt nicht ohne Grund davor, diese Kardinalitäten zu unterschätzen: Ein Fehler hier pflanzt sich bis in die Datenbank fort. Für Teil-Ganzes-Beziehungen kennt die UML zwei Sonderformen: die schwache Aggregation, bei der das Teil eigenständig fortbesteht, und die starke Komposition, bei der das Teil mit dem Ganzen verschwindet. Die Vererbung schließlich verbindet eine Unterklasse mit einer allgemeineren Oberklasse. Bei solchen Entscheidungen zeigt sich die Modellierung nicht als technisches Zeichnen, sondern als konzeptionelle Arbeit.

#### 2.3.3 Aktivitätsdiagramm

Das Aktivitätsdiagramm bildet Abläufe ab und ähnelt auf den ersten Blick einem Flussdiagramm – kann aber deutlich mehr. Eine Aktion erscheint als abgerundetes Rechteck, der Kontrollfluss als Pfeil. Ein ausgefüllter Kreis markiert den Startknoten, ein umrandeter den Endknoten. Ein Entscheidungsknoten – eine Raute – verzweigt den Fluss anhand einer Bedingung; ein passender Zusammenführungsknoten führt die Zweige wieder zusammen. Für echte Parallelität sorgen Fork und Join, die mehrere Flüsse gleichzeitig starten und später synchronisieren.

Besonders nützlich sind Schwimmbahnen, die jede Aktion einer verantwortlichen Rolle zuordnen. So zeigt sich auf einen Blick, wer was tut. Für den Lerntrainer eignet sich das Diagramm ideal, um den Eingabe-Workflow einer Lernunit samt Fehlerfällen abzubilden. Seine Grenze: Es zeigt den Ablauf, nicht den zeitlichen Nachrichtenaustausch zwischen konkreten Objekten. Dafür ist das Sequenzdiagramm zuständig.

#### 2.3.4 Sequenzdiagramm

Das Sequenzdiagramm gehört zu den Interaktionsdiagrammen. Es stellt dar, wer wann welche Nachricht an wen schickt. Jedes beteiligte Objekt besitzt eine Lebenslinie – eine senkrechte gestrichelte Linie –, auf der ein Aktivierungsbalken markiert, wann das Objekt gerade aktiv ist. Entscheidend ist die Unterscheidung der Nachrichtentypen: Eine synchrone Nachricht (gefüllte Pfeilspitze) lässt den Sender warten, bis eine Antwort zurückkommt. Eine asynchrone Nachricht (offene Pfeilspitze) erlaubt dem Sender, sofort weiterzuarbeiten. Diesen Unterschied unterschätzte ich anfangs; erst beim Modellieren wurde mir klar, wie sehr er das Verhalten des Systems prägt.

Seit UML 2 lassen sich mit kombinierten Fragmenten ganze Kontrollstrukturen abbilden: alt für sich gegenseitig ausschließende Alternativen, opt für einen optionalen Abschnitt, loop für Wiederholungen. Genau diese Fragmente brauche ich für die Mentoren-Auswertung. Die Stärke des Diagramms liegt in der präzisen zeitlichen Reihenfolge. Seine Grenze ist die Übersichtlichkeit – bei vielen Objekten wird es schnell unleserlich.

### 2.4 Funktionale und nichtfunktionale Anforderungen

Bevor Anwendungsfälle und Klassen entstehen, lohnt sich ein Blick auf die Natur der Anforderungen selbst. Die Literatur trennt funktionale von nichtfunktionalen Anforderungen. Funktionale Anforderungen beschreiben, was ein System leisten soll – welche Funktionen es bereitstellt und wie es auf Eingaben reagiert. Nichtfunktionale Anforderungen beschreiben, wie gut es seine Aufgaben erfüllt – Qualitätsmerkmale wie Leistung, Sicherheit, Benutzbarkeit oder Wartbarkeit.

Für den Lerntrainer ist „Das System ermittelt nach jeder eingegebenen Lernunit den Tages- und Wochensoll-Status" eine typische funktionale Anforderung; sie schlägt sich später unmittelbar in einem Anwendungsfall nieder. Gerade nichtfunktionale Anforderungen werden in studentischen Arbeiten gern übersehen – dabei entscheiden sie über Erfolg oder Misserfolg oft stärker als die reine Funktionalität. Aus meiner Praxis fallen mir für den Lerntrainer sofort drei ein. 

Erstens: Datenschutz. Lerndaten sind personenbezogen, weshalb der Administrator bewusst keinen Zugriff auf individuelle Lernverläufe erhält. Zweitens: Antwortzeit. Die Soll-Berechnung läuft nach jeder Eingabe und muss nahezu verzögerungsfrei erfolgen – sonst nervt die App im Alltag. Drittens: Benutzbarkeit. Die Zielgruppe sind nebenberuflich Studierende, die das Werkzeug zwischen Beruf und Lernen einsetzen und keine Einarbeitungszeit haben.

Diese Trennung ist kein Selbstzweck. Sie erklärt, warum manche Anforderungen direkt als Anwendungsfall sichtbar werden, während andere – etwa der Datenschutz – sich eher in Strukturentscheidungen des Klassendiagramms niederschlagen.

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

Bevor das erste Diagramm entsteht, müssen Anforderungen erhoben, strukturiert und verstanden werden. Das International Requirements Engineering Board (IREB) definiert in seinem Lehrplan diese Tätigkeit als systematische Vorgehensweise zur Ermittlung, Dokumentation, Prüfung und Verwaltung von Anforderungen. Pohl und Rupp bezeichnen die Anforderungsanalyse zu Recht als eine der anspruchsvollsten Tätigkeiten der Softwareentwicklung überhaupt. Meine Berufspraxis bestätigt das: Wo Anforderungen unscharf bleiben, multiplizieren sich Missverständnisse durch jede Projektphase – mit messbaren Folgen.

Die Standish Group berichtet seit Jahrzehnten, dass unklare Anforderungen einer der Hauptgründe für Projektabbrüche sind. Eine konsequente Anforderungsanalyse ist deshalb keine bürokratische Pflichtübung. Sie ist eine Investition, die sich in jeder folgenden Phase auszahlt. Genau aus diesem Grund nimmt sich diese Arbeit Zeit, jeden Modellschritt aus den Anforderungen der Aufgabenstellung herzuleiten, statt direkt mit dem Zeichnen zu beginnen.

### 2.6 Zwischenfazit

Die theoretischen Grundlagen verdichten sich auf drei Kernpunkte. Erstens: Software-Engineering ist ein strukturiertes Vorgehen, dessen Wirksamkeit empirisch belegt ist – und dessen Vernachlässigung sich in den CHAOS-Daten ablesen lässt. Zweitens: Die UML ist der etablierte Standard für diese Strukturarbeit, nicht weil sie hübsch aussieht, sondern weil sie eine gemeinsame Sprache zwischen Fachlichkeit und Technik schafft. Drittens: Eine sorgfältige Anforderungsanalyse ist die Brücke zwischen Idee und Modell; sie entscheidet, ob die Modellierung trägt oder nicht.

Diese Erkenntnisse führen direkt ins nächste Kapitel: Wenn die Anforderungen das Fundament bilden, dann muss die Modellierung deren Logik sichtbar machen. Das ist die Aufgabe der vier Diagramme im Anwendungsteil.

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

Bevor das erste Diagramm entstand, war zu klären, was der Lerntrainer leisten soll und in welchem Umfeld er steht. Er unterstützt Studierende beim Planen und Protokollieren ihres Lernfortschritts. Ein Lernplan bildet den Fortschritt eines Moduls ab, ihm sind Lernunits zugeordnet, und ein übergreifender Studienplan bündelt alles. 

Simpel klingt das. Ist es aber nicht, sobald man die Details ernst nimmt. Pohl und Rupp nennen die Anforderungsanalyse zu Recht eine der anspruchsvollsten Tätigkeiten überhaupt – was sich im Verlauf dieser Arbeit bestätigt hat.

Um den Rahmen abzustecken, zeigt Abbildung 1 den Domänenkontext: drei menschliche Akteure, das zu modellierende System, ein technischer Benachrichtigungsdienst als Umsystem. Diese Kontextsicht ist bewusst der detaillierten Modellierung vorangestellt, weil sie die Systemgrenze klärt – was zum Lerntrainer gehört und was außerhalb liegt. Der Benachrichtigungsdienst etwa ist ein technisches Umsystem; er wird vom Lerntrainer genutzt, gehört aber nicht zur fachlichen Domäne und taucht deshalb später im Business Object Model nicht auf.

Mein Vorgehen folgte der inneren Logik der vier Modelle. Erst das Use-Case-Diagramm für die Funktionssicht, dann das Klassendiagramm für die Datenstruktur, anschließend das Aktivitätsdiagramm für einen Ablauf und zuletzt das Sequenzdiagramm für ein Interaktionsszenario. Die vier müssen zusammenpassen – ein Akteur im Use-Case-Diagramm, der im Sequenzdiagramm fehlt, wäre ein Bruch. Wichtiger als das fertige Bild war mir dabei stets die Begründung: Warum diese Lösung und nicht eine der Alternativen?

### 3.2 Aufgabe A1 – Use-Case-Diagramm

#### 3.2.1 Akteure und Use Cases

Der Einstieg über Use Cases ist kein Zufall. Jacobson stellt den Anwendungsfall bewusst an den Anfang – das System wird von außen gedacht. Ich bin derselben Logik gefolgt. Vier Akteure ließen sich aus den Anforderungen herauslesen.

Der Benutzer ist die Hauptfigur: Er legt Pläne an, erfasst Lernunits und ruft Auswertungen ab. Der Administrator pflegt nur systemweite Vorlagen und bekommt bewusst keinen Einblick in persönliche Lerndaten – eine Trennung, die mir aus Datenschutzgründen wichtig war. Der Mentor unterstützt einzelne Studierende und handelt in deren Namen. Und das System selbst? Es tritt als Akteur auf, sobald es ohne menschliches Zutun reagiert – etwa wenn nach jeder Eingabe automatisch der Soll-Status berechnet wird.

Zuerst sah das Diagramm aus wie ein Spinnennetz. Jeder Akteur war mit fast jedem Use Case verbunden, die Linien kreuzten sich, und das Bild verlor seine Aussagekraft. Erst die Sortierung der Use Cases in fünf Gruppen – Planverwaltung, Lernunit-Verwaltung, die systemgesteuerte Fortschrittskontrolle mit Zwischenbericht, Lob, Bonus und Warnung, dann Auswertungen und schließlich Administration – brachte Ordnung hinein. Diese Gruppierung stand in keiner Vorgabe; sie entstand aus der Notwendigkeit, das Diagramm lesbar zu halten. Das ist eine praktische Erkenntnis: Sobald ein Modell unübersichtlich wird, fehlt ihm meist eine Strukturierungsebene.

#### 3.2.2 Beziehungen und ihre Begründung

An den Beziehungen entscheidet sich, ob ein Use-Case-Diagramm etwas aussagt oder nur dekoriert. Der Use Case „Lernunit eingeben" bindet „Zwischenbericht ermitteln" über «include» ein. Denn das System berechnet nach jeder Eingabe zwingend den Soll-Status – das ist kein Sonderfall, sondern Kernlogik. Lob, Bonus und Überarbeitungswarnung dagegen hängen an «extend», weil sie nur unter Bedingungen feuern.

Hier lag übrigens meine erste Sackgasse. Zunächst hatte ich auch diese drei als «include» modelliert. Der Gedanke: Sie gehören ja „dazu". Beim zweiten Hinsehen merkte ich, dass das falsch ist – ein Lob erscheint eben nicht immer, sondern nur bei erreichtem Tagessoll. Rupp et al. bestätigen die Faustregel: Bedingte Erweiterungen sind der Lehrbuchfall für «extend». 

Zwischen „Lernunit erstellen" und ihren beiden Varianten besteht eine Generalisierung – eine Spezialisierung. Den Mentor schließlich modellierte ich als spezialisierten Benutzer, der dessen Use Cases erbt und um eigene Rechte ergänzt.

**Beziehungstypen im Use-Case-Diagramm (Tab. 3):**

| Beziehung | Wann angemessen | Beispiel im Lerntrainer |
|---|---|---|
| «include» | Teilfunktion zwingend enthalten | „Lernunit eingeben" ➜ „Zwischenbericht ermitteln" |
| «extend» | Erweiterung nur unter Bedingung | „Zwischenbericht ermitteln" ➜ „Lob anzeigen" bei Tagessoll |
| Generalisierung | Spezialfall mit gemeinsamer Wurzel | „Lernunit erstellen" – individuell vs. aus Vorlage |
| Akteur-Vererbung | Rolle erbt Funktionen einer anderen | Mentor erbt vom Benutzer und ergänzt eigene Rechte |

#### 3.2.3 Textuelle Ausarbeitung eines zentralen Use Cases

Ein Use-Case-Diagramm zeigt das Was, nicht das Wie. Um einen Anwendungsfall wirklich zu durchdringen, empfiehlt die Literatur ein zusätzliches Werkzeug: die textuelle Use-Case-Schablone. Ein strukturierter Steckbrief mit Vorbedingung, Standardablauf, Alternativabläufen und Nachbedingung. Pohl und Rupp betonen, dass erst diese Ausformulierung die im Diagramm verdichteten Beziehungen überprüfbar macht. 

Ich habe das für „Lernunit eingeben" getan – den zentralen und am häufigsten ausgeführten Anwendungsfall. Die Schablone in Tabelle 4 bildet zugleich die Brücke zum Aktivitätsdiagramm in Abschnitt 3.4, das denselben Ablauf grafisch aufgreift.

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

Beim Klassendiagramm bin ich an einer Stelle länger hängengeblieben: bei der Frage, wie Studierende und Mentoren zusammenhängen. Mein erster Reflex war, den Mentor von der Klasse Studierender erben zu lassen – schließlich ist ein Mentor ja auch irgendwie an der Hochschule tätig. Je länger ich darüber nachdachte, desto schiefer kam mir das vor. Ein Mentor ist kein besonderer Studierender, und ein Studierender ist kein angehender Mentor. Die beiden teilen Eigenschaften, aber keiner ist dem anderen untergeordnet. 

Also verwarfen ich diesen ersten Entwurf und führten stattdessen eine abstrakte Oberklasse Person ein, von der beide erben. Person trägt das Attribut name, ist aber selbst nicht instanziierbar – ein Objekt im laufenden System ist immer konkret das eine oder das andere. Diese Lösung fühlt sich nicht nur sauberer an, sie ist es auch: Sie bündelt das Gemeinsame an einer Stelle, ohne eine falsche Hierarchie zu behaupten.

Der Rest ergab sich daraus. Studierender bekommt studienstart und studiengang sowie Referenzen auf genau einen Studienplan und beliebig viele Mentoren. Mentor ergänzt eintrittsdatum und fachrichtung. Der Studienplan bündelt die Lernpläne; der Lernplan trägt modulname, semester, ects und das Tages- sowie Wochensoll in Minuten. Eine bewusste Entscheidung war, das Soll in Minuten statt in Stunden zu speichern. Wer mit Zeiterfassungssystemen gearbeitet hat, kennt die Tücke: Rundungsfehler pflanzen sich fort und machen irgendwann alle Auswertungen wertlos.

Knifflig wurde es bei der Lernunit: Sie beschreibt das Lehrmaterial, dokumentiert aber nicht das eigentliche Lernen. Dafür führte ich eine eigene Klasse Lernvorgang ein – denn wer sich an einem Tag dreimal hinsetzt, erzeugt drei Lernvorgänge, nicht einen. Die Lehrmaterialarten lagerte ich als Enumeration LehrmaterialTyp aus, wie die Aufgabenstellung verlangt.

#### 3.3.2 Komposition oder Aggregation – eine bewusste Abwägung

An keiner anderen Stelle des Modells habe ich so lange gegrübelt wie hier. Die Aufgabe verlangt mindestens eine Aggregation oder Komposition. Klingt nach einer Formalie, ist aber eine echte Entscheidung – und ich brauchte zwei Abende, bis ich sie für mich sauber begründen konnte.

Fangen wir mit dem klaren Fall an: Studienplan und Lernplan. Ein Lernplan ohne seinen Studienplan – ergibt das Sinn? Nein. Wird der Studienplan gelöscht, müssen die Lernpläne mit verschwinden. Das ist eine Komposition im Lehrbuchsinn, und die ausgefüllte Raute bringt diese enge Bindung auf den Punkt.

Schwieriger war die Auswertung. Mein erster Entwurf hatte auch sie als Komposition am Mentor hängen. Die Logik dahinter: Der Mentor erstellt die Auswertung, also gehört sie ihm. Plausibel? Ja. Falsch? Auch ja. Denn eine Komposition würde bedeuten: Verlässt ein Mentor die Hochschule und sein Datensatz wird gelöscht, reißt er sämtliche Auswertungen mit sich. Das wäre fatal. Eine Auswertung dokumentiert den Lernfortschritt eines Studierenden – sie muss erhalten bleiben, ganz gleich, ob der Mentor noch da ist oder nicht.

Am ersten Abend übersah ich das einfach. Erst am zweiten, als ich gedanklich durchspielte, was beim Löschen eines Mentors passiert, fiel der Groschen. Das war der Knackpunkt.

Also umgebaut: Aggregation, hohle Raute. Das Teil überlebt das Ganze. Eine kurz erwogene Zwischenlösung – die Auswertung beim Löschen dem „Sammel-Account" zuzuordnen – verwarfen ich, weil sie das Modell unnötig verkompliziert hätte. Diese Variante erscheint mir am saubersten; ich halte sie für tragfähig.

Bleibt die dritte Beziehung: Lernplan zu Lernunit. Komposition? Aggregation? Tatsächlich weder noch. Eine Lernunit-Definition lässt sich auch für sich betrachten, ohne dass sie an einem einzelnen Lernplan klebt – eine schlichte Assoziation reicht völlig. Hätte ich hier eine Komposition gesetzt, hätte ich das Modell überspezifiziert. Erst als ich die drei Fälle nebeneinander legte – feste Komposition, lose Aggregation, neutrale Assoziation –, hat es bei mir wirklich klick gemacht.

#### 3.3.3 Fachliche und technische Sicht – eine bewusste Grenze

Ein Punkt verdient eine Klarstellung, weil er im Sequenzdiagramm später noch wichtig wird. Das Klassendiagramm liegt hier als Business Object Model vor – es bildet bewusst nur die fachliche Domäne ab. Also jene Gegenstände, über die auch ein Studierender oder ein Mentor sprechen würde: Lernplan, Lernunit, Auswertung. Oestereich und Scheithauer betonen, dass das Analysemodell von technischen Realisierungsdetails frei bleiben soll, weil diese erst in der Designphase hinzukommen.

Diese Trennung ist kein formaler Selbstzweck. Sie erklärt, warum ein technischer Hilfsdienst wie der Versand von Benachrichtigungen im BOM nichts zu suchen hat – er ist kein fachliches Geschäftsobjekt, sondern ein Mittel zum Zweck. Im Sequenzdiagramm in Abschnitt 3.5 taucht ein solcher Dienst dennoch auf, weil dort der technische Ablauf gezeigt wird. Im fachlichen Datenmodell bleibt er bewusst außen vor. Vermischt man diese beiden Sichten, entsteht ein Modell, das weder die Fachseite noch die Technik sauber bedient – ein Fehler, den ich in echten Projekten mehr als einmal gesehen habe.

### 3.4 Aufgabe A3 – Aktivitätsdiagramm

Für das Aktivitätsdiagramm hatte ich die freie Wahl des Use Cases und entschied mich für „Lernunit eingeben". Warum? Weil er der Use Case ist, den ein Nutzer am häufigsten ausführt – oft mehrmals täglich. Außerdem steckt in ihm mit den drei Soll-Prüfungen genug Entscheidungslogik, um ein Diagramm zu rechtfertigen, das mehr zeigt als eine simple Kette. Zwei Schwimmbahnen – Benutzer und System – trennen sauber, wer was tut.

Der Ablauf startet mit der Auswahl oder Neuanlage einer Lernunit. Der Nutzer erfasst die Lerndauer. Hier wollte die Aufgabe einen Fehlerfall sehen. Der naheliegendste: Was, wenn jemand versehentlich null Minuten oder einen negativen Wert eingibt? Ein Entscheidungsknoten fängt das ab, zeigt eine Fehlermeldung und schickt den Nutzer zurück zur Eingabe. Erst eine gültige Dauer führt hinüber in die System-Bahn.

Anders als zunächst gedacht, habe ich die drei Soll-Prüfungen nicht in einen einzigen Sammel-Knoten gepackt. Mein erster Entwurf tat das – ein Knoten, der „alle Ziele erreicht?" fragt. Das war mir zu grob. Tages-, Wochensoll und das 40-Stunden-Limit sind drei eigenständige Bedingungen mit drei eigenen Reaktionen (Lob, Bonus, Warnung), und genau das sollte das Diagramm zeigen. Also: drei getrennte Entscheidungsknoten, nacheinander. Dort entsteht ein Lernvorgang, dann wird der Zwischenbericht ermittelt, am Ende laufen alle Zweige in einem Endknoten zusammen.

### 3.5 Aufgabe A4 – Sequenzdiagramm

Das vierte Diagramm bildet die Mentoren-Auswertung ab – ein vorgegebener Ablauf. Vier Lebenslinien sind beteiligt: :Studierender, :System, :Mentor und ein :NotificationService, den das System erst im Verlauf erzeugt. 

Der Studierende bestellt synchron eine Auswertung – er wartet kurz auf die Bestätigung. Anschließend benachrichtigt das System den Mentor asynchron. Das war mir wichtig. Würde das System hier synchron warten, bliebe der Studierende blockiert, bis der Mentor reagiert – was Stunden dauern kann. Asynchron darf er weiterarbeiten.

Der Mentor lädt synchron die Lernvorgangsdaten, schreibt sein Feedback und speichert es. Daraufhin erzeugt das System den NotificationService. Diese Kopplung ist bewusst so gewählt: Der NotificationService ist kein fachliches Geschäftsobjekt wie Lernplan oder Auswertung. Er ist ein rein technischer Dienst für den Versand. Deshalb taucht er im Business Object Model nicht auf – das BOM bildet absichtlich nur die fachliche Domäne ab. Im Sequenzdiagramm hingegen, das den technischen Ablauf zeigt, muss der Dienst sichtbar werden – und mit «create» wird klar dokumentiert, dass das System ihn instanziiert.

Für die Benachrichtigung verlangte die Aufgabe „SMS oder E-Mail". Mein erster Gedanke war, das mit zwei separaten Nachrichten zu lösen – doch das hätte suggeriert, beide würden gesendet. Hier hakte ich kurz: Ein alt-Fragment ist genau das Richtige, weil es genau eine der beiden Alternativen wählt. Den Timeout-Fall – der Mentor reagiert nicht rechtzeitig – packte ich in ein opt-Fragment mit erneuter Erinnerung. Zum Schluss ruft der Studierende die fertige Auswertung synchron ab.

---

## 4 Diskussion

### 4.1 Kritische Würdigung der Ergebnisse

Am Anfang stand eine textuelle Beschreibung, am Ende ein konsistentes UML-Modell aus vier Diagrammen. Jedes beleuchtet eine andere Seite des Lerntrainers, und doch greifen sie ineinander: Was das Use-Case-Diagramm an Funktionen verspricht, lösen Klassen-, Aktivitäts- und Sequenzdiagramm strukturell und dynamisch ein.

In der Praxis war der Weg holpriger, als diese Aufzählung vermuten lässt. Rückblickend waren es weniger die Diagramme selbst als die Entscheidungen dahinter, die mich etwas gelehrt haben. Im Use-Case-Diagramm lag der Schlüssel in der sauberen Rollentrennung und der bewussten Wahl zwischen «include», «extend» und Generalisierung. Im Klassendiagramm waren es die abstrakte Oberklasse Person und vor allem die Abwägung zwischen Komposition und Aggregation. Ich hätte zu Beginn nicht gedacht, dass mich eine einzelne Raute so lange beschäftigen würde. Das Aktivitätsdiagramm zwang mich, einen realistischen Fehlerfall mitzudenken. Das Sequenzdiagramm machte mir den Unterschied zwischen synchroner und asynchroner Kommunikation greifbarer, als es jede Definition gekonnt hätte.

Allerdings: Meine Modellierung beruht allein auf einer schriftlichen Vorgabe. In einem echten Projekt würde ich mit künftigen Nutzern sprechen, Prototypen zeigen, nachjustieren. Aus meiner Berufspraxis kenne ich, wie viel sich an einem Modell ändert, sobald drei Fachexperten in einem Workshop draufschauen. Das ersetzt keine Modulhausarbeit – es sollte aber als Hinweis stehen. Außerdem bleibt mein Modell auf der fachlichen Analyseebene. Die spannenden Architekturfragen – welches Entwurfsmuster sich für die Benachrichtigungslogik eignet – habe ich bewusst ausgeklammert. Sie wären der logische nächste Schritt.

### 4.2 Modellierungswerkzeuge – eine Einordnung aus der Praxis

Ein Aspekt, der in der reinen Aufgabenstellung nicht vorkommt, in der Praxis aber über Erfolg und Frust entscheidet, ist die Wahl des Modellierungswerkzeugs. In meiner Zeit im IT-Consulting arbeitete ich mit professionellen Werkzeugen wie Enterprise Architect und Innovator. Beide sind mächtig: Sie halten ein gemeinsames Repository, prüfen die Konsistenz zwischen Diagrammen und erlauben es, ein Modellelement einmal anzulegen und in mehreren Diagrammen wiederzuverwenden. Diese Konsistenzprüfung ist Gold wert, sobald ein Modell über wenige Diagramme hinauswächst – das deckt sich mit der Forderung der Literatur nach werkzeuggestützter Sicherung der Modellqualität.

Für eine Arbeit in diesem Umfang wäre ein solches Schwergewicht jedoch überdimensioniert. Leichtgewichtige Werkzeuge erstellen Diagramme entweder grafisch oder – textbasiert – aus einer Beschreibungssprache, was Versionsverwaltung und schnelle Änderungen erleichtert. Der Preis: die fehlende semantische Konsistenzprüfung. Ein grafisches Werkzeug zeichnet bereitwillig auch eine fachlich falsche Beziehung. Diese Erkenntnis prägte mein Vorgehen – ich sicherte die Konsistenz zwischen den vier Diagrammen manuell, also genau jene Arbeit von Hand, die ein professionelles Werkzeug automatisiert. Für eine größere, nächste Iteration des Lerntrainers wäre der Umstieg auf ein Repository-basiertes Werkzeug der logische Schritt.

### 4.3 Fazit und Ausblick

Diese Hausarbeit startete mit einer einfachen Frage: Wie entsteht Struktur im Fernstudium? Sie führte über UML-Modellierung hin zu einer anderen Einsicht – nämlich dass gute Struktur vor allem sauberes Denken erfordert. Die vier Diagramme sind das Endprodukt; aber der eigentliche Wert liegt in den Überlegungen, die dahinter stecken. Mit jedem Modell, das ich verwarf, wurde mein Verständnis klarer. Mit jeder Alternative, die ich durchspielte, wurde die endgültige Entscheidung tragfähiger.

Was käme nach dieser Modellierung? Mir schweben eine gamifizierte Fortschrittsanzeige vor und eine datengestützte Empfehlung, welche Lernunit als Nächstes dran wäre. Die Idee kommt nicht von ungefähr: Eine Metaanalyse von Sailer und Homner über zahlreiche Einzelstudien weist Gamification einen kleinen, aber stabilen positiven Effekt auf kognitive Lernergebnisse nach. Die Selbstbestimmungstheorie von Deci und Ryan erklärt, warum: Belohnungsmechaniken wirken nur, wenn sie die Grundbedürfnisse nach Kompetenz und Autonomie bedienen. Das im Lerntrainer modellierte Lob bei erreichtem Tagessoll ist schon ein erster, kleiner Schritt in diese Richtung.

Der CHAOS-Report der Standish Group zeigt seit Jahrzehnten: Die meisten Software-Projekte scheitern nicht an Technik. Sie scheitern an unklaren Anforderungen und fehlender Struktur. Meine Berufserfahrung unterstreicht das. Eine Hausarbeit lässt sich dazu nicht abschließend in Beziehung setzen – sie ist kein echtes Projekt. Aber die Methode lässt sich übertragen: Erst die Funktionen klären, dann die Daten, dann die Abläufe, dann die Interaktionen. Wer diese Reihenfolge beherzigt, hat eine deutlich bessere Ausgangslage.

Eines nehme ich aus dieser Arbeit auf jeden Fall mit: Modelle sind keine bloße Formalität, die man abhakt. Sie zwingen einen, Widersprüche zu sehen, bevor sie teuer werden. Und dafür hat sich die Mühe gelohnt – die zwei Abende mit der Raute eingeschlossen.

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
