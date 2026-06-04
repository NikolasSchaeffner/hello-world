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

Drei Studienbriefe, zwei laufende Module, ein Kalender, der schon platzt. Und kein Gefühl dafür, ob man eigentlich vorankommt. Wer im Fernstudium steht, kennt das. Kein Hörsaal gibt den Takt vor. Keine Kommilitonen am Nebentisch, an denen man sich messen könnte. Man organisiert alles selbst, jeden Abend neu. Und genau hier scheitern viele. Nicht am Stoff. An der Struktur. Ich hatte einmal ein Semester mit drei Modulen parallel, und irgendwann wusste ich schlicht nicht mehr, was ich wann gelernt hatte und was noch fehlte. Abgebrochen habe ich nicht. Aber gefehlt hat nicht viel.

Ein Einzelfall ist das nicht. Das Deutsche Zentrum für Hochschul- und Wissenschaftsforschung beziffert die Abbruchquote im Bachelorstudium auf rund 28 Prozent, und ein Hauptgrund ist immer derselbe: Die Voraussetzungen der Studierenden passen nicht zu dem, was das Studium verlangt. Während die Leute abspringen, wächst der Markt für digitale Lernhilfen weiter. Statista rechnet dem weltweiten E-Learning-Plattformmarkt bis 2028 ein Volumen von rund 63 Milliarden Euro vor, bei gut vier Prozent jährlichem Wachstum. Realer Bedarf auf der einen Seite, ein Markt im Aufwind auf der anderen. Aus dieser Lücke heraus entstand die Idee zu einem virtuellen Lerntrainer, der den Studienverlauf nicht ersetzt, aber strukturiert begleitet.

Diese Sicht bringe ich nicht nur als Studierender mit. Am Berufskolleg habe ich von 2001 bis 2003 die Grundlagen der Informations- und Kommunikationstechnik gelernt, danach folgte zwischen 2004 und 2007 die Ausbildung zum IT-Systemelektroniker bei einem mittelständischen IT-Dienstleister in Mannheim. First- und Second-Level-Support, Rollout-Projekte für öffentliche Einrichtungen, Einsätze in der Industrie. Von 2015 bis 2020 kam dann das IT-Consulting im Raum Ludwigshafen: Consultants koordinieren, Aufträge akquirieren, und nebenbei wuchs ich in Werkzeuge wie Enterprise Architect und Innovator hinein. Eine Lehre aus all dem hat sich eingebrannt. Software-Projekte scheitern selten an der Technik. Sie scheitern an unklaren Anforderungen und fehlender Struktur, ganz am Anfang, lange bevor jemand eine Zeile Code schreibt.

Zahlen stützen das. Der CHAOS-Report der Standish Group wertet seit 1994 IT-Projekte international aus und zählt eine klare Aussage der Anforderungen zu den drei wichtigsten Erfolgsfaktoren überhaupt. Hier setzt das Modul Software-Engineering I an. Und hier setzt diese Arbeit an.

### 1.2 Zielsetzung der Arbeit

Diese Hausarbeit modelliert einen virtuellen Lerntrainer softwaretechnisch, gemäß Alternative A der Aufgabenstellung. Vier UML-Modelle bauen dabei aufeinander auf: ein Use-Case-Diagramm für die Funktionssicht, ein Klassendiagramm als Business Object Model für die Datenstruktur, ein Aktivitätsdiagramm für einen ausgewählten Anwendungsfall, ein Sequenzdiagramm für die Erstellung einer Mentoren-Auswertung. Verlangt ist dabei mehr als saubere Notation. Verlangt ist, dass man jeden Modellschritt herleitet und begründet. Genau das versuche ich durchzuhalten.

Drei Teilziele stecken dahinter. Das theoretische Fundament zu UML und modellbasierter Entwicklung soll so liegen, dass sich die späteren Entscheidungen daraus ableiten lassen, nicht aus dem Bauch. Dann die vier Diagramme selbst: entworfen, dokumentiert, in jeder ernsthaften Frage begründet, samt der Wege, die ich unterwegs wieder verworfen habe. Und am Ende eine kritische Würdigung, die das Ergebnis in einen Praxiskontext stellt, der über die reine Modulanforderung hinausgeht.

### 1.3 Aufbau und Vorgehensweise

Vier Hauptkapitel, klar getrennt. Kapitel 2 legt das Fundament. Es klärt, was Software-Engineering und modellbasierte Entwicklung meinen, ordnet die UML als Standard ein und stellt die vier Diagrammtypen mitsamt ihren wichtigsten Beziehungselementen vor. Ein eigener Abschnitt gehört der Anforderungsanalyse, jener Brücke zwischen den fachlichen Anforderungen und dem, was später daraus an Modellen entsteht. Ein Zwischenfazit zurrt die Kernaussagen fest.

Den Schwerpunkt trägt Kapitel 3. Dort entstehen die vier Modelle, eines nach dem anderen: erst das Use-Case-Diagramm mit Akteuren und Beziehungen, dann das Klassendiagramm mit Vererbung und der Frage Aggregation oder Komposition, danach das Aktivitätsdiagramm zum Use Case „Lernunit eingeben", zuletzt das Sequenzdiagramm zur Mentoren-Auswertung. Jede Entscheidung wird dargestellt, begründet und, wo es etwas bringt, gegen die verworfene Alternative gehalten. Kapitel 4 würdigt das Ganze kritisch und endet mit Fazit und Ausblick.

---

## 2 Theoretische Grundlagen

### 2.1 Software-Engineering und modellbasierte Entwicklung

Software „ingenieurmäßig" entwickeln, was heißt das eigentlich? Balzert fasst es nüchtern: systematisch herstellen, betreiben, pflegen. Also das Gegenteil von Drauflosprogrammieren. Dass dieser Anspruch überhaupt nötig wurde, lehrte die Software-Krise der späten 1960er-Jahre, als Projekte reihenweise an Budget, Terminen und Qualität zerbrachen. Aus den Folgekonferenzen wuchs die Disziplin, die heute jeder strukturierten Softwareentwicklung den Rahmen gibt. Gelöst ist das Problem damit nicht. Wer die historischen CHAOS-Daten anschaut, sieht es schwarz auf weiß: Nur etwa ein Drittel aller IT-Projekte gilt dort als uneingeschränkt erfolgreich. Diese Zahlen muss man vorsichtig lesen. Eveleens und Verhoef zeigen in einer vielzitierten Analyse, dass die Standish-Definitionen methodisch wackeln, weil sie Erfolg allein an der Schätzgenauigkeit von Kosten, Zeit und Funktionsumfang messen und so verzerrte Quoten produzieren. Ich ziehe daraus zwei Schlüsse. Die Tendenz stimmt, viele Projekte geraten in Schwierigkeiten, das ist breit belegt. Die genauen Prozentwerte aber sollte man nicht zu fest anziehen.

Im Zentrum steht das Modell. Ein Modell ist eine zweckgerichtete Abstraktion. Es blendet aus, was nicht zählt, und hebt heraus, worauf es ankommt. Balzert nennt das schlicht Reduktion auf das Wesentliche. Beim Modellieren des Lerntrainers ist mir aufgegangen, dass genau diese Reduktion der härteste Teil ist. Was wesentlich ist und was nicht, steht eben nirgends. Das entscheidet man selbst. Oft mehr als einmal.

Brandt-Pook und Kollmeier zerlegen die Softwareentwicklung in drei zusammenwirkende Sichten: Prozess, Methoden, Projektgeschehen. Die UML, mit der diese Arbeit hantiert, gehört eindeutig zu den Methoden. Und der Lerntrainer ist kein simples Programm, sondern ein Softwaresystem im eigentlichen Sinn, ein Verbund interagierender Komponenten, in dem Benutzer, Mentor, Administrator und das System selbst zusammenspielen. Daraus folgt schon, warum ein einziges Diagramm nie reicht. Eine Skizze fängt eine solche Vielschichtigkeit nicht ein. Vier müssen es sein.

### 2.2 Die Unified Modeling Language als Standard

Die UML ist die Lingua franca der Modellierung. Ihre Geschichte ist eine Versöhnungsgeschichte. In den 1990ern stritten mehrere objektorientierte Notationen um die Vorherrschaft, bis Booch, Rumbaugh und Jacobson, in der Literatur die „drei Amigos", ihre Ansätze zusammenwarfen und die Object Management Group das Ergebnis 1997 zum Standard erklärte. Überrascht hat mich beim Einlesen vor allem eines: UML ist keine Reißbrett-Erfindung. Sie ist aus einem handfesten Methodenstreit hervorgegangen. Verbindlich ist heute Version 2.5.1, an der ich mich bei der Notation halte.

Vierzehn Diagrammtypen umfasst die UML, grob geteilt in Struktur und Verhalten. Erstere zeigen den statischen Aufbau, letztere das dynamische Geschehen. Für den Lerntrainer borge ich aus beiden Lagern: ein Strukturdiagramm für die Daten, drei Verhaltensdiagramme für Funktionen und Abläufe. Oestereich und Scheithauer erinnern an den eigentlichen Nutzen der UML. Er liegt nicht in hübschen Kästchen, sondern darin, dass Fachseite und Entwicklung endlich dieselbe Sprache sprechen. Diesen Effekt habe ich im Consulting mehr als einmal erlebt. Sobald ein Modell auf dem Tisch lag, ein Modell zum Anfassen, redeten plötzlich alle über dieselbe Sache. Vorher hatten sie aneinander vorbeigeredet, ohne es zu merken.

### 2.3 Struktur- und Verhaltensdiagramme im Überblick

Die vierzehn Typen zerfallen in zwei Familien. Strukturdiagramme, allen voran das Klassendiagramm, halten fest, woraus ein System besteht und welche dauerhaften Beziehungen seine Bausteine verbinden. Verhaltensdiagramme zeigen, was geschieht: wer das System benutzt, wie ein Vorgang abläuft, wer wann mit wem spricht. Aus beiden Familien greife ich. Ein Strukturdiagramm für die Daten, drei Verhaltensdiagramme für Funktionen, Abläufe und Interaktion. Die nächsten vier Abschnitte gehen jeden Typ nach demselben Raster durch: Zweck, zentrale Notation, Grenzen. So lässt sich Kapitel 3 daraus ableiten.

#### 2.3.1 Use-Case-Diagramm

Zwei Fragen beantwortet das Use-Case-Diagramm. Wer nutzt das System? Und was kann es? Die Methode geht auf Jacobson zurück, der den Anwendungsfall schon Anfang der 1990er bewusst an den Anfang jeder Analyse stellte. Das System wird von außen gedacht, vom Nutzen her, nicht von der Technik. Oestereich und Scheithauer beschreiben es daher als Einstieg jeder Anforderungsanalyse.

Die Notation ist absichtlich karg. Ein Akteur, gezeichnet als Strichmännchen, steht für eine Rolle außerhalb des Systems, ein Mensch oder ein anderes System. Der Anwendungsfall ist eine Ellipse. Die Systemgrenze ein Rechteck, das alle Anwendungsfälle umschließt und Innen von Außen trennt. Eine schlichte Linie verbindet Akteur und Anwendungsfall zur Assoziation. Und gerade diese Kargheit ist die Stärke. Auch Fachleute ohne Informatikhintergrund lesen das Diagramm mühelos. Genau darin liegt aber auch die Grenze. Über das Wie eines Ablaufs schweigt es. Dafür braucht es das Aktivitäts- oder das Sequenzdiagramm.

Zwischen Anwendungsfällen lassen sich drei Beziehungen ziehen, die ich später gezielt verwende. «include» für eine Teilfunktion, die zwingend dazugehört. «extend» für eine Erweiterung, die nur unter Bedingungen auftaucht. Und die Generalisierung für eine Spezialisierung. Diese drei sauber auseinanderzuhalten, das ist die eigentliche Hürde. Und sie entscheidet, ob ein Diagramm etwas sagt oder bloß schmückt.

#### 2.3.2 Klassendiagramm

Das Klassendiagramm ist das wichtigste Strukturdiagramm der UML. In der Analysephase heißt es Business Object Model, weil es die fachlichen Gegenstände eines Systems abbildet und technische Details noch beiseitelässt. Eine Klasse erscheint als Rechteck mit drei Feldern: Name, Attribute, Methoden. Jedes Attribut trägt einen Datentyp, jede Operation eine Signatur, und Sichtbarkeiten regeln, wer worauf zugreifen darf. Bei einem reinen Analysemodell wie dem BOM rücken diese Sichtbarkeiten in den Hintergrund. Hier zählt zuerst die fachliche Struktur.

Der Kern sind die Beziehungen. Die Assoziation verbindet zwei Klassen als gleichberechtigte Partner, und ihre Multiplizitäten sagen, wie viele Objekte der einen Seite mit wie vielen der anderen verbunden sind. Heikel sind genau diese Kardinalitäten. Kleuker warnt in seinem „Grundkurs Datenbankentwicklung" davor, sie zu unterschätzen, und er hat recht: Ein Fehler an dieser Stelle pflanzt sich bis in die Datenbank fort. Für Teil-Ganzes-Beziehungen kennt die UML zwei Sonderformen. Die schwache Aggregation, bei der das Teil eigenständig weiterlebt. Und die starke Komposition, bei der das Teil mit dem Ganzen verschwindet. Die Vererbung schließlich hängt eine Unterklasse an eine allgemeinere Oberklasse. Beim Lerntrainer entscheidet schon die Frage, ob ein Studienplan einen oder mehrere Lernpläne bündelt, über die gesamte Datenstruktur. Eine Frage, die mir in Kapitel 3 noch Kopfzerbrechen machen wird.

#### 2.3.3 Aktivitätsdiagramm

Das Aktivitätsdiagramm zeigt Abläufe. Auf den ersten Blick wirkt es wie ein Flussdiagramm, kann aber mehr. Eine Aktion ist ein abgerundetes Rechteck, der Kontrollfluss ein Pfeil. Ein ausgefüllter Kreis markiert den Start, ein umrandeter das Ende. Der Entscheidungsknoten, gezeichnet als Raute, verzweigt den Fluss nach einer Bedingung, und ein Zusammenführungsknoten holt die Zweige wieder zusammen. Echte Parallelität liefern Fork und Join: mehrere Flüsse gleichzeitig starten, später synchronisieren.

Besonders praktisch sind die Schwimmbahnen. Sie weisen jede Aktion einer verantwortlichen Rolle zu, sodass man auf einen Blick sieht, wer was tut. Für den Eingabe-Workflow einer Lernunit samt Fehlerfällen ist dieses Diagramm wie gemacht. Eine Grenze hat es trotzdem. Den zeitlichen Nachrichtenaustausch zwischen konkreten Objekten zeigt es nicht. Das ist Sache des Sequenzdiagramms.

#### 2.3.4 Sequenzdiagramm

Das Sequenzdiagramm gehört zu den Interaktionsdiagrammen und hält fest, wer wann welche Nachricht an wen schickt. Jedes beteiligte Objekt hat eine Lebenslinie, eine senkrechte gestrichelte Linie, auf der ein Aktivierungsbalken zeigt, wann das Objekt gerade arbeitet. Entscheidend ist der Unterschied der Nachrichtentypen. Eine synchrone Nachricht, gefüllte Pfeilspitze, lässt den Sender warten, bis Antwort kommt. Eine asynchrone, offene Pfeilspitze, erlaubt dem Sender, sofort weiterzumachen. Diesen Unterschied habe ich anfangs unterschätzt. Erst beim Modellieren ging mir auf, wie stark er das Verhalten des Systems prägt.

Seit UML 2 lassen sich mit kombinierten Fragmenten ganze Kontrollstrukturen zeichnen. alt für einander ausschließende Alternativen. opt für einen optionalen Abschnitt. loop für Wiederholungen. Genau die brauche ich für die Mentoren-Auswertung, etwa um die Benachrichtigung wahlweise per SMS oder E-Mail darzustellen. Die Stärke des Diagramms liegt in der präzisen zeitlichen Reihenfolge. Seine Schwäche auch: Bei vielen Objekten wird es schnell unleserlich.

### 2.4 Funktionale und nichtfunktionale Anforderungen

Bevor Anwendungsfälle und Klassen entstehen, lohnt ein Blick auf die Anforderungen selbst. Die Literatur trennt funktionale von nichtfunktionalen. Funktionale Anforderungen sagen, was ein System leisten soll, welche Funktionen es bietet, wie es auf Eingaben reagiert. Beim Lerntrainer ist „Das System ermittelt nach jeder eingegebenen Lernunit den Tages- und Wochensoll-Status" so eine funktionale Anforderung. Sie schlägt sich später unmittelbar in einem Anwendungsfall und einer «include»-Beziehung nieder.

Nichtfunktionale Anforderungen sagen, wie gut das System seine Aufgaben erfüllt. Leistung, Sicherheit, Benutzbarkeit, Wartbarkeit. In studentischen Arbeiten gehen sie gern unter, obwohl sie oft stärker über Erfolg oder Scheitern entscheiden als die Funktionalität selbst. Für den Lerntrainer fallen mir aus der Praxis sofort welche ein. Da ist der Datenschutz: Lerndaten sind personenbezogen, also bekommt der Administrator in meinem Modell bewusst keinen Zugriff auf individuelle Lernverläufe. Da ist die Antwortzeit. Die Soll-Berechnung läuft nach jeder Eingabe, sie muss also fast verzögerungsfrei kommen, sonst nervt die App im Alltag und fliegt vom Handy. Und da ist die Benutzbarkeit. Die Zielgruppe sind nebenberuflich Studierende, gequetscht zwischen Job und Lernen. Einarbeitungszeit haben sie keine.

Diese Trennung ist kein Selbstzweck. Sie erklärt, warum manche Anforderungen direkt als Anwendungsfall sichtbar werden, andere dagegen, der Datenschutz etwa, eher in Strukturentscheidungen des Klassendiagramms verschwinden.

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

Bevor das erste Diagramm entsteht, müssen Anforderungen erhoben, sortiert und verstanden werden. Das International Requirements Engineering Board definiert diese Arbeit in seinem Lehrplan als systematisches Vorgehen zur Ermittlung, Dokumentation, Prüfung und Verwaltung von Anforderungen. Pohl und Rupp nennen die Anforderungsanalyse eine der anspruchsvollsten Tätigkeiten der Softwareentwicklung überhaupt. Wer im Beruf damit zu tun hatte, widerspricht dem nicht. Bleiben Anforderungen unscharf, vermehren sich die Missverständnisse durch jede Projektphase, und am Ende sind sie messbar teuer.

Die Standish Group meldet seit Jahrzehnten dasselbe: Unklare Anforderungen gehören zu den Hauptgründen für Projektabbrüche. Eine ordentliche Analyse ist deshalb keine bürokratische Pflichtübung, sondern eine Investition, die sich später auszahlt. Darum nimmt sich diese Arbeit die Zeit, jeden Modellschritt aus den Anforderungen herzuleiten, statt gleich zum Zeichnen zu greifen.

### 2.6 Zwischenfazit

Drei Dinge bleiben hängen. Software-Engineering ist strukturiertes Vorgehen, seine Wirksamkeit ist belegt, und was passiert, wenn man es vernachlässigt, lässt sich an drei Jahrzehnten CHAOS-Daten ablesen. Die UML ist der etablierte Standard, um diese Strukturarbeit sichtbar zu machen. Nicht weil sie hübsch ist, sondern weil sie eine gemeinsame Sprache zwischen Fachlichkeit und Technik schafft. Und die Anforderungsanalyse? Sie ist die Brücke zwischen Idee und Modell. Trägt sie nicht, trägt später auch das Modell nicht.

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

Vor dem ersten Diagramm stand eine schlichte Frage: Was soll der Lerntrainer überhaupt leisten, und in welchem Umfeld steht er? Er unterstützt Studierende beim Planen und Protokollieren ihres Lernfortschritts. Ein Lernplan bildet den Fortschritt eines Moduls ab, ihm sind Lernunits zugeordnet, und ein übergreifender Studienplan hält das Ganze zusammen. Klingt simpel. Ist es nicht, sobald man die Details ernst nimmt. Pohl und Rupp nennen die Anforderungsanalyse eine der anspruchsvollsten Tätigkeiten überhaupt, und diese Arbeit hat das bestätigt.

Um den Rahmen abzustecken, zeigt Abbildung 1 zuerst den Domänenkontext: die drei menschlichen Akteure, das zu modellierende System, den technischen Benachrichtigungsdienst als Umsystem. Diese Kontextsicht steht bewusst vor der detaillierten Modellierung, weil sie die Systemgrenze klärt. Was gehört zum Lerntrainer, was liegt draußen? Der Benachrichtigungsdienst etwa ist ein technisches Umsystem. Der Lerntrainer nutzt ihn, fachlich gehört er nicht dazu, und deshalb taucht er im Business Object Model später nicht auf.

Mein Vorgehen folgte der inneren Logik der vier Modelle. Erst das Use-Case-Diagramm für die Funktionssicht. Dann das Klassendiagramm für die Daten. Danach das Aktivitätsdiagramm für einen Ablauf. Zuletzt das Sequenzdiagramm für ein Interaktionsszenario. Die vier müssen zusammenpassen. Ein Akteur, der im Use-Case-Diagramm auftaucht, im Sequenzdiagramm aber fehlt, wäre ein Bruch, und solche Brüche fallen einem irgendwann auf die Füße. Wichtiger als das fertige Bild war mir immer die Begründung. Warum diese Lösung und nicht die andere?

### 3.2 Aufgabe A1 – Use-Case-Diagramm

#### 3.2.1 Akteure und Use Cases

Der Einstieg über Use Cases ist kein Zufall. Jacobson, der die Methode geprägt hat, setzt den Anwendungsfall bewusst an den Anfang. So bin ich vorgegangen. Aus den Anforderungen ließen sich vier Akteure herauslesen.

Der Benutzer ist die Hauptfigur. Er legt Pläne an, erfasst Lernunits, ruft Auswertungen ab. Der Administrator pflegt nur die systemweiten Vorlagen und bekommt bewusst keinen Blick in persönliche Lerndaten, eine Trennung, auf der ich aus Datenschutzgründen bestanden habe. Der Mentor unterstützt einzelne Studierende und handelt in deren Namen. Und das System? Das tritt selbst als Akteur auf, sobald es ohne menschliches Zutun reagiert, etwa wenn nach jeder Eingabe automatisch der Soll-Status berechnet wird.

Der erste Entwurf sah aus wie ein Spinnennetz. Jeder Akteur war mit fast jedem Use Case verbunden, die Linien kreuzten sich kreuz und quer, und das Bild sagte am Ende gar nichts mehr. Erst eine Sortierung brachte Luft hinein. Fünf Gruppen: Planverwaltung, Lernunit-Verwaltung, die systemgesteuerte Fortschrittskontrolle mit Zwischenbericht, Lob, Bonus und Warnung, dann die Auswertungen, schließlich die Administration. Diese Gruppierung stand in keiner Vorgabe. Sie entstand allein aus der Not, das Diagramm lesbar zu halten. Den Effekt kenne ich aus der Praxis: Wird ein Modell unübersichtlich, fehlt ihm meistens eine Strukturierungsebene.

#### 3.2.2 Beziehungen und ihre Begründung

An den Beziehungen entscheidet sich alles. Der Use Case „Lernunit eingeben" bindet „Zwischenbericht ermitteln" über «include» ein, denn nach jeder Eingabe berechnet das System zwingend den Soll-Status. Das ist kein Sonderfall. Das ist Kernlogik. Lob, Bonus und Überarbeitungswarnung dagegen hängen an «extend», weil sie nur unter Bedingungen feuern.

Hier lag meine erste Sackgasse. Anfangs hatte ich auch diese drei als «include» modelliert, weil sie ja „dazugehören". Beim zweiten Hinsehen merkte ich, dass das schlicht falsch ist. Ein Lob erscheint eben nicht immer. Nur bei erreichtem Tagessoll. Solche bedingten Abläufe kenne ich aus dem IT-Support gut: Eine automatische Eskalation läuft auch nur dann an, wenn ein Ticket eine Frist reißt, nicht bei jedem Ticket. Rupp et al. bestätigen die Faustregel, bedingte Erweiterungen sind der Lehrbuchfall für «extend». Zwischen „Lernunit erstellen" und ihren beiden Varianten besteht eine Generalisierung, und den Mentor habe ich als spezialisierten Benutzer angelegt, der dessen Use Cases erbt und um eigene Rechte ergänzt.

**Beziehungstypen im Use-Case-Diagramm (Tab. 3):**

| Beziehung | Wann angemessen | Beispiel im Lerntrainer |
|---|---|---|
| «include» | Teilfunktion zwingend enthalten | „Lernunit eingeben" ➜ „Zwischenbericht ermitteln" |
| «extend» | Erweiterung nur unter Bedingung | „Zwischenbericht ermitteln" ➜ „Lob anzeigen" bei Tagessoll |
| Generalisierung | Spezialfall mit gemeinsamer Wurzel | „Lernunit erstellen" – individuell vs. aus Vorlage |
| Akteur-Vererbung | Rolle erbt Funktionen einer anderen | Mentor erbt vom Benutzer und ergänzt eigene Rechte |

#### 3.2.3 Textuelle Ausarbeitung eines zentralen Use Cases

Ein Use-Case-Diagramm zeigt das Was, nicht das Wie. Um einen Anwendungsfall wirklich zu durchdringen, empfiehlt die Literatur die textuelle Use-Case-Schablone, einen strukturierten Steckbrief mit Vorbedingung, Standardablauf, Alternativabläufen, Nachbedingung. Pohl und Rupp betonen, dass erst diese Ausformulierung die im Diagramm verdichteten Beziehungen prüfbar macht. Ich habe das für den zentralen und am häufigsten ausgeführten Anwendungsfall „Lernunit eingeben" gemacht. Die Schablone in Tabelle 4 schlägt zugleich die Brücke zum Aktivitätsdiagramm in Abschnitt 3.4, das denselben Ablauf grafisch aufgreift.

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

Beim Klassendiagramm bin ich an einer Stelle länger hängengeblieben. Wie hängen Studierende und Mentoren zusammen? Mein erster Reflex: Lass den Mentor von Studierender erben, ist ja auch irgendwie an der Hochschule. Je länger ich darüber nachdachte, desto schiefer kam mir das vor. Ein Mentor ist kein besonderer Studierender. Und ein Studierender ist kein angehender Mentor. Die beiden teilen Eigenschaften, aber keiner steht über dem anderen. Also habe ich den Entwurf zerrissen und eine abstrakte Oberklasse Person eingeführt, von der beide erben. Person trägt das Attribut name, ist aber nicht instanziierbar. Ein Objekt im laufenden System ist immer konkret das eine oder das andere, nie ein abstraktes Dazwischen. Diese Lösung fühlt sich nicht nur sauberer an, sie ist es: Sie bündelt das Gemeinsame an einer Stelle, ohne eine falsche Hierarchie zu behaupten.

Der Rest folgte fast von allein. Studierender bekommt studienstart und studiengang, dazu Referenzen auf genau einen Studienplan und beliebig viele Mentoren. Mentor ergänzt eintrittsdatum und fachrichtung. Der Studienplan bündelt die Lernpläne, der Lernplan trägt modulname, semester, ects sowie das Tages- und Wochensoll, in Minuten. Das Soll in Minuten zu speichern statt in Stunden war eine bewusste Wahl, sie vermeidet Rundungsfehler bei der Fortschrittsberechnung. Wer einmal mit Zeiterfassung gearbeitet hat, weiß, warum das zählt. Stimmt die Datenbasis nicht, sind auch die schönsten Auswertungen wertlos.

Knifflig wurde die Lernunit. Sie beschreibt das Lehrmaterial, dokumentiert aber nicht das Lernen selbst. Dafür kam eine eigene Klasse Lernvorgang dazu. Wer sich an einem Tag dreimal hinsetzt, erzeugt drei Lernvorgänge, nicht einen. Die Lehrmaterialarten habe ich als Enumeration LehrmaterialTyp ausgelagert, so wie es die Aufgabenstellung verlangt.

#### 3.3.2 Komposition oder Aggregation – eine bewusste Abwägung

Nirgends im Modell habe ich so lange gegrübelt wie hier. Die Aufgabe verlangt mindestens eine Aggregation oder Komposition. Klingt nach Formalie. Ist eine echte Entscheidung, und ich habe zwei Abende gebraucht, bis ich sie für mich sauber begründen konnte. Fangen wir beim klaren Fall an, Studienplan und Lernplan. Ein Lernplan ohne seinen Studienplan? Ergibt keinen Sinn. Verschwindet der Studienplan, müssen die Lernpläne mit. Lehrbuch-Komposition, und die ausgefüllte Raute bringt diese enge Bindung auf den Punkt.

Schwieriger wurde die Auswertung. Sie war der Grund für die zwei Abende. Mein erster Entwurf hängte sie als Komposition an den Mentor. Die Logik dahinter klingt zwingend: Der Mentor erstellt die Auswertung, also gehört sie ihm. Falsch. Eine Komposition würde nämlich bedeuten: Verlässt ein Mentor die Hochschule und sein Datensatz wird gelöscht, reißt er sämtliche Auswertungen mit in den Abgrund. Das wäre fatal. Eine Auswertung dokumentiert den Lernfortschritt eines Studierenden. Sie muss bleiben. Ganz gleich, ob der Mentor noch da ist oder längst weg.

Am ersten Abend habe ich das schlicht übersehen. Erst am zweiten, als ich gedanklich durchspielte, was beim Löschen eines Mentors passiert, fiel der Groschen. Das war der Knackpunkt.

Also habe ich umgebaut. Aggregation, hohle Raute. Das Teil überlebt das Ganze. Eine Zwischenlösung hatte ich kurz erwogen, die Auswertung beim Löschen des Mentors einem „Sammel-Account" zuzuschlagen, aber das verkompliziert das Modell ohne Not, also weg damit. Die Aggregation ist die sauberste Variante, die ich sehe. Tragfähig, auch wenn man über Detailfragen sicher streiten könnte.

Bleibt die dritte Beziehung, Lernplan zu Lernunit. Komposition? Aggregation? Weder noch. Eine Lernunit-Definition steht auch für sich, ohne an einem einzelnen Lernplan zu kleben, eine schlichte Assoziation reicht völlig. Eine Komposition hätte das Modell hier überspezifiziert. Erst als ich die drei Fälle nebeneinanderlegte, feste Komposition, lose Aggregation, neutrale Assoziation, hat es bei mir wirklich klick gemacht.

#### 3.3.3 Fachliche und technische Sicht – eine bewusste Grenze

Ein Punkt braucht hier eine Klarstellung, weil er im Sequenzdiagramm noch wichtig wird. Das Klassendiagramm ist als Business Object Model angelegt. Es bildet bewusst nur die fachliche Domäne ab, also die Gegenstände, über die auch ein Studierender oder ein Mentor reden würde: Lernplan, Lernunit, Auswertung. Oestereich und Scheithauer betonen, dass das Analysemodell frei von technischen Realisierungsdetails bleiben soll, denn die kommen erst in der Designphase dazu.

Diese Trennung ist kein formaler Selbstzweck. Sie erklärt, warum ein technischer Hilfsdienst wie der Versand von Benachrichtigungen im BOM nichts verloren hat. Er ist kein fachliches Geschäftsobjekt, sondern Mittel zum Zweck. Im Sequenzdiagramm in Abschnitt 3.5 taucht so ein Dienst trotzdem auf, weil dort der technische Ablauf gezeigt wird. Im fachlichen Datenmodell bleibt er draußen. Wer beide Sichten vermischt, bekommt ein Modell, das weder die Fachseite noch die Technik sauber bedient. Diesen Fehler habe ich in Projekten mehr als einmal gesehen.

### 3.4 Aufgabe A3 – Aktivitätsdiagramm

Beim Aktivitätsdiagramm hatte ich freie Wahl des Use Cases und nahm „Lernunit eingeben". Warum gerade den? Weil ihn ein Nutzer am häufigsten ausführt, oft mehrmals am Tag. Und weil in ihm mit den drei Soll-Prüfungen genug Entscheidungslogik steckt, um ein Diagramm zu rechtfertigen, das mehr zeigt als eine simple Kette. Zwei Schwimmbahnen, Benutzer und System, trennen sauber, wer was tut.

Der Ablauf startet mit Auswahl oder Neuanlage einer Lernunit. Dann erfasst der Nutzer die Lerndauer. An dieser Stelle wollte die Aufgabe einen Fehlerfall sehen, und mir fiel sofort der naheliegendste ein: Was, wenn jemand versehentlich null Minuten eintippt oder einen negativen Wert? Ein Entscheidungsknoten fängt das ab, wirft eine Fehlermeldung, schickt den Nutzer zurück zur Eingabe. Erst eine gültige Dauer führt hinüber in die System-Bahn.

Die drei Soll-Prüfungen habe ich nicht in einen Sammel-Knoten gepackt, anders als zuerst geplant. Mein erster Entwurf hatte genau das: ein Knoten, der „alle Ziele erreicht?" fragt. Zu grob. Tages-, Wochensoll und das 40-Stunden-Limit sind drei eigenständige Bedingungen mit drei eigenen Reaktionen, Lob, Bonus, Warnung. Und genau das sollte das Diagramm zeigen. Also drei getrennte Entscheidungsknoten, nacheinander. Zuerst entsteht ein Lernvorgang, dann wird der Zwischenbericht ermittelt, am Ende laufen alle Zweige in einem Endknoten zusammen.

### 3.5 Aufgabe A4 – Sequenzdiagramm

Das vierte Diagramm bildet den vorgegebenen Ablauf der Mentoren-Auswertung ab. Vier Lebenslinien sind beteiligt: :Studierender, :System, :Mentor und ein :NotificationService, den das System erst im Verlauf erzeugt. Der Studierende bestellt synchron eine Auswertung, er wartet kurz auf Bestätigung. Dann benachrichtigt das System den Mentor asynchron. Das war mir wichtig. Würde das System hier synchron warten, bliebe der Studierende blockiert, bis der Mentor reagiert. Das kann Stunden dauern. Asynchron darf er weiterarbeiten.

Der Mentor lädt synchron die Lernvorgangsdaten, schreibt sein Feedback, speichert es. Daraufhin erzeugt das System den NotificationService. Diese Kopplung ist Absicht. Der NotificationService ist kein fachliches Geschäftsobjekt wie Lernplan oder Auswertung, sondern ein rein technischer Dienst für den Versand. Deshalb fehlt er im Business Object Model, das absichtlich nur die Fachdomäne zeigt. Im Sequenzdiagramm dagegen, das den technischen Ablauf abbildet, muss er sichtbar werden. Mit «create» wird klar dokumentiert, dass das System ihn instanziiert und damit für seinen Lebenszyklus geradesteht.

Für die Benachrichtigung verlangte die Aufgabe „SMS oder E-Mail". Mein erster Gedanke war, das mit zwei separaten Nachrichten zu lösen. Aber das hätte suggeriert, beide würden gesendet. Hier hakte ich kurz. Erst ein Blick in die OMG-Spezifikation machte klar, dass ein alt-Fragment genau passt, weil es genau eine der beiden Alternativen wählt. Den Timeout-Fall, der Mentor reagiert nicht rechtzeitig, habe ich in ein opt-Fragment mit erneuter Erinnerung gesteckt. Zum Schluss ruft der Studierende die fertige Auswertung synchron ab.

---

## 4 Diskussion

### 4.1 Kritische Würdigung der Ergebnisse

Am Anfang stand eine textuelle Beschreibung, am Ende ein konsistentes UML-Modell aus vier Diagrammen. Jedes beleuchtet eine andere Seite des Lerntrainers, und trotzdem greifen sie ineinander. Was das Use-Case-Diagramm an Funktionen verspricht, lösen Klassen-, Aktivitäts- und Sequenzdiagramm strukturell und dynamisch ein. So weit die Theorie. In Wahrheit war der Weg dorthin holpriger, als diese saubere Aufzählung glauben macht.

Rückblickend haben mich weniger die Diagramme etwas gelehrt als die Entscheidungen dahinter. Im Use-Case-Diagramm lag der Schlüssel in der Rollentrennung und der bewussten Wahl zwischen «include», «extend» und Generalisierung. Im Klassendiagramm waren es die abstrakte Oberklasse Person und vor allem die Abwägung Komposition gegen Aggregation, die ich nicht aus dem Lehrbuch abgeschrieben, sondern am konkreten Fall durchgerungen habe. Dass mich eine einzelne Raute so lange beschäftigen würde, hätte ich am Anfang nicht gedacht. Das Aktivitätsdiagramm zwang mich, einen echten Fehlerfall mitzudenken. Und das Sequenzdiagramm machte mir den Unterschied zwischen synchroner und asynchroner Kommunikation greifbarer, als es jede Definition gekonnt hätte.

Eine ehrliche Einschränkung gehört dazu. Mein Modell beruht allein auf einer schriftlichen Vorgabe. In einem echten Projekt hätte ich mit künftigen Nutzern gesprochen, Prototypen gezeigt, nachjustiert. Aus dem Beruf weiß ich, wie viel sich an einem Modell verschiebt, sobald drei Fachexperten in einem Workshop draufschauen. Eine Modulhausarbeit ersetzt das nicht. Trotzdem sollte es hier stehen. Außerdem bleibt mein Modell auf der fachlichen Analyseebene. Die spannenden Architekturfragen, etwa welches Entwurfsmuster zur Benachrichtigungslogik passt, habe ich bewusst ausgeklammert, sie hätten den Rahmen gesprengt. Sie wären der logische nächste Schritt.

### 4.2 Modellierungswerkzeuge – eine Einordnung aus der Praxis

Ein Punkt fehlt in der Aufgabenstellung ganz, entscheidet im Berufsalltag aber über Erfolg und Frust: die Wahl des Modellierungswerkzeugs. Im Consulting habe ich mit Schwergewichten wie Enterprise Architect und Innovator gearbeitet. Beide können viel. Sie halten ein gemeinsames Repository, prüfen die Konsistenz zwischen Diagrammen und erlauben es, ein Modellelement einmal anzulegen und es in mehreren Diagrammen wiederzuverwenden. Genau diese Konsistenzprüfung ist Gold wert, sobald ein Modell über wenige Diagramme hinauswächst. Die Literatur fordert nicht umsonst eine werkzeuggestützte Sicherung der Modellqualität.

Für eine Arbeit in diesem Umfang wäre so ein Schwergewicht überdimensioniert. Leichtgewichtige Werkzeuge zeichnen entweder direkt grafisch oder erzeugen die Diagramme, wie textbasierte Ansätze, aus einer Beschreibungssprache, was Versionsverwaltung und schnelle Änderungen erleichtert. Der Preis: keine semantische Konsistenzprüfung. Ein grafisches Werkzeug malt eine fachlich falsche Beziehung genauso bereitwillig wie eine richtige. Diese Erfahrung hat mein Vorgehen geprägt. Ich habe die Konsistenz zwischen den vier Diagrammen hier von Hand sichergestellt, also genau die Arbeit selbst erledigt, die ein professionelles Werkzeug automatisiert. Für die nächste, größere Iteration des Lerntrainers wäre der Umstieg auf ein Repository-basiertes Werkzeug der nächste Schritt.

### 4.3 Fazit und Ausblick

Was käme nach dieser Modellierung? Mir schwebt eine gamifizierte Fortschrittsanzeige vor und eine datengestützte Empfehlung, welche Lernunit als Nächstes dran ist. Die Idee kommt nicht aus der Luft. Eine Metaanalyse von Sailer und Homner über viele Einzelstudien weist Gamification einen kleinen, aber stabilen positiven Effekt auf kognitive Lernergebnisse nach. Warum das wirkt, erklärt die Selbstbestimmungstheorie von Deci und Ryan: Belohnungsmechaniken greifen nur, wenn sie die Grundbedürfnisse nach Kompetenz und Autonomie bedienen, statt sie zu untergraben. Das Lob bei erreichtem Tagessoll, das im Lerntrainer schon steckt, ist rückblickend ein erster kleiner Schritt in diese Richtung.

Der CHAOS-Report der Standish Group zeigt seit Jahrzehnten dasselbe. Die wenigsten Software-Projekte scheitern an Technik. Sie scheitern an unklaren Anforderungen und fehlender Struktur. Meine eigene Berufserfahrung unterschreibt das. Eine Hausarbeit lässt sich damit nicht abschließend vergleichen, sie ist kein echtes Projekt, aber das methodische Vorgehen überträgt sich: erst die Funktionen klären, dann die Daten, dann die Abläufe, dann die Interaktionen. Wer diese Reihenfolge ernst nimmt, startet besser als jemand, der gleich zu programmieren anfängt.

Eines nehme ich auf jeden Fall mit. Modelle sind keine Formalität, die man abhakt, um endlich zum Code zu kommen. Sie zwingen einen, Widersprüche zu sehen, bevor sie teuer werden. Allein dafür hat sich die Mühe gelohnt. Die zwei Abende mit der Raute eingeschlossen.

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
