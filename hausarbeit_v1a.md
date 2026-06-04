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

Drei Studienbriefe, zwei laufende Module, ein voller Kalender. Und kein Gefühl dafür, ob man eigentlich vorankommt. Wer im Fernstudium steht, kennt das. Kein Hörsaal gibt den Takt vor, keine Kommilitonen sitzen am Nebentisch, an denen man sich messen könnte. Ich erinnere mich noch genau an ein Semester mit drei parallelen Modulen, in dem ich irgendwann schlicht den Überblick verlor: was ich gelernt hatte, was noch fehlte, welche Fristen längst abgelaufen waren. Abgebrochen habe ich nicht. Aber nah dran war es.

Das ist kein Einzelfall. Das Deutsche Zentrum für Hochschul- und Wissenschaftsforschung beziffert die Abbruchquote im Bachelorstudium auf rund 28 Prozent. Der Grund liegt selten am Stoff. Er liegt an der Struktur. Und genau hier hakt die Frage ein, die diese Arbeit antreibt: Wie lässt sich Struktur digital nachbilden, sodass sie Studierenden nicht bloß als tote Liste auf dem Smartphone liegt, sondern als aktiver Begleiter funktioniert?

Parallel wächst der Markt für digitale Lernhilfen rasant. Statista taxiert das weltweite Volumen für E-Learning-Plattformen bis 2028 auf etwa 63 Milliarden Euro. Aus dieser Schnittmenge, echtem Bedarf hier und wachsendem Markt dort, entstand die Idee eines virtuellen Lerntrainers. Kein neuer Kurs, kein weiteres Learning-Management-System, sondern ein schmales Werkzeug, das den Studienverlauf strukturiert begleitet.

Diese Perspektive bringe ich nicht nur als Studierender mit. Von 2001 bis 2003 erlernte ich die Grundlagen der Informations- und Kommunikationstechnik an einem schulischen Berufskolleg, anschließend folgte zwischen 2004 und 2007 eine Ausbildung zum IT-Systemelektroniker bei einem mittelständischen IT-Dienstleister in Mannheim. Dort arbeitete ich im First- und Second-Level-Support, in Rollout-Projekten für öffentliche Einrichtungen und in Industrieunternehmen. Von 2015 bis 2020 koordinierte ich bei einem IT-Consulting-Unternehmen im Raum Ludwigshafen Consultants, akquirierte Aufträge und wurde mit Modellierungswerkzeugen wie Enterprise Architect und Innovator vertraut.

Aus dieser Praxis kenne ich eine Einsicht, die sich mir eingebrannt hat: Software-Projekte scheitern nicht an der Technik. Sie scheitern an unklaren Anforderungen und an fehlender Struktur ganz am Anfang. Der CHAOS-Report der Standish Group, der seit 1994 internationale IT-Projekte auswertet, deckt das. Eine klare Formulierung von Anforderungen zählt dort zu den drei wichtigsten Erfolgsfaktoren überhaupt. Hier setzt das Modul Software-Engineering I an. Und hier setzt diese Arbeit an.

### 1.2 Zielsetzung der Arbeit

Ziel ist die softwaretechnische Modellierung eines virtuellen Lerntrainers gemäß Alternative A der Aufgabenstellung. Vier UML-Modelle bauen dabei aufeinander auf: ein Use-Case-Diagramm für die Funktionssicht, ein Klassendiagramm als Business Object Model für die Datenstruktur, ein Aktivitätsdiagramm für einen ausgewählten Anwendungsfall und ein Sequenzdiagramm für die Erstellung einer Mentoren-Auswertung.

Die Aufgabe verlangt ausdrücklich mehr als formal korrekte Notation. Sie verlangt eine nachvollziehbare Herleitung und eine Begründung für jedes einzelne Modellartefakt. Diesem Anspruch versuche ich gerecht zu werden.

Drei Dinge will ich erreichen. Das theoretische Fundament von UML und modellbasierter Entwicklung soll so dastehen, dass sich die späteren Modellierungsentscheidungen daraus ableiten lassen, nicht umgekehrt. Die vier Diagramme sollen nicht aus dem Nichts auftauchen, sondern dokumentiert und in jeder substanziellen Entscheidung begründet werden, einschließlich der Sackgassen, die ich unterwegs wieder verlassen habe. Und am Ende soll das Ergebnis kritisch gewürdigt und in einen Praxiskontext gestellt werden, der über die reine Modulanforderung hinausreicht.

### 1.3 Aufbau und Vorgehensweise

Vier Hauptkapitel. Kapitel 2 legt das theoretische Fundament: Software-Engineering und modellbasierte Entwicklung, die UML als Standard, die vier verwendeten Diagrammtypen samt ihren wichtigsten Beziehungselementen. Ein eigener Abschnitt gilt der Anforderungsanalyse, jener Brücke zwischen den fachlichen Anforderungen und der späteren Modellierung.

Kapitel 3 ist der Schwerpunkt. Hier wachsen die vier UML-Modelle Schritt für Schritt: erst das Use-Case-Diagramm mit Akteuren und Beziehungen, dann das Klassendiagramm mit Vererbung und der heiklen Frage Aggregation oder Komposition, danach das Aktivitätsdiagramm zum Use Case „Lernunit eingeben" und schließlich das Sequenzdiagramm zur Mentoren-Auswertung. Jede Entscheidung wird dargestellt, begründet und, wo es etwas bringt, gegen die verworfene Alternative gehalten. Kapitel 4 würdigt die Ergebnisse kritisch und schließt mit Fazit und Ausblick.

---

## 2 Theoretische Grundlagen

### 2.1 Software-Engineering und modellbasierte Entwicklung

Was heißt es, Software „ingenieurmäßig" zu entwickeln? Balzert versteht darunter die systematische, planbare Herstellung, den Betrieb und die Pflege von Software. Das Gegenteil von Drauflosprogrammieren. Zwingend nötig wurde dieser Anspruch nach der sogenannten Software-Krise der späten 1960er-Jahre, als Projekte reihenweise an Budget, Terminen und Qualität zerbrachen. Aus den Folgekonferenzen entstand die Disziplin, die heute den Rahmen für jede strukturierte Softwareentwicklung bildet.

Hat diese Disziplin das Problem gelöst? Ein Blick in die historischen CHAOS-Daten sagt: nein. Nur etwa ein Drittel aller IT-Projekte gilt dort als uneingeschränkt erfolgreich. Mit einem wichtigen Vorbehalt allerdings. Eveleens und Verhoef weisen in einer vielzitierten Analyse nach, dass die Standish-Definitionen methodisch angreifbar sind. Sie machen Erfolg allein an der Schätzgenauigkeit von Kosten, Zeit und Funktionsumfang fest und erzeugen dadurch verzerrte Erfolgsquoten. Für diese Arbeit folgt daraus eine Unterscheidung: Die grobe Tendenz, viele Projekte geraten in Schwierigkeiten, ist breit belegt. Die exakten Prozentwerte sollte man nicht überstrapazieren.

Im Zentrum des Software-Engineerings steht das Modell. Ein Modell ist eine zweckgerichtete Abstraktion: Es blendet aus, was nicht zählt, und hebt hervor, worauf es ankommt. Balzert beschreibt das nüchtern als Reduktion auf das Wesentliche. Mir fiel beim Modellieren des Lerntrainers allerdings etwas anderes auf. Genau diese Reduktion ist der schwierigste Teil. Was wesentlich ist und was nicht, dazu gibt es keine Lehrbuchantwort. Das muss man selbst entscheiden. Oft mehrmals.

Brandt-Pook und Kollmeier zerlegen die Softwareentwicklung in drei zusammenwirkende Sichten: Prozess, Methoden und Projektgeschehen. Die UML, mit der diese Arbeit operiert, ordnen sie eindeutig den Methoden zu. Der Lerntrainer ist dabei kein simples Programm. Er ist ein Softwaresystem im eigentlichen Sinne, ein Verbund interagierender Komponenten, in dem Benutzer, Mentor, Administrator und das System selbst zusammenspielen. Und damit ist auch schon klar, warum es vier verschiedene Diagrammtypen braucht. Ein einzelnes Diagramm fängt die Vielschichtigkeit eines Systems nie ein.

### 2.2 Die Unified Modeling Language als Standard

Die UML ist heute die Verkehrssprache der Modellierung. Ihre Geschichte ist überraschend lebendig. In den 1990er-Jahren rangen mehrere objektorientierte Notationen wild durcheinander, bis Booch, Rumbaugh und Jacobson, in der Literatur gern die „drei Amigos" genannt, ihre Ansätze zusammenführten. Die Object Management Group erhob das Ergebnis 1997 zum Standard. Das ist also keine Erfindung am Reißbrett, sondern das Resultat eines handfesten Methodenstreits.

Heute verbindlich ist UML 2.5.1, an ihr orientiere ich mich bei der Notation. Vierzehn Diagrammtypen umfasst die Sprache, grob geteilt in Struktur- und Verhaltensdiagramme. Strukturdiagramme zeigen den statischen Aufbau. Verhaltensdiagramme zeigen das dynamische Verhalten. Für den Lerntrainer brauche ich aus beiden Lagern: ein Strukturdiagramm für die Daten, drei Verhaltensdiagramme für Funktionen und Abläufe.

Oestereich und Scheithauer erinnern an den eigentlichen Nutzen der UML. Der liegt nicht in hübschen Kästchen, sondern darin, dass Fachseite und Entwicklung endlich dieselbe Sprache sprechen. In meiner Zeit im IT-Consulting habe ich diesen Effekt mehrfach erlebt. Sobald ein Modell auf dem Tisch lag, redeten plötzlich alle konkret über dieselbe Sache. Vorher redeten sie aneinander vorbei.

### 2.3 Struktur- und Verhaltensdiagramme im Überblick

Die vierzehn Diagrammtypen der UML zerfallen in zwei große Familien. Strukturdiagramme, allen voran das Klassendiagramm, halten den statischen Aufbau fest: die Bausteine eines Systems und ihre dauerhaften Beziehungen. Verhaltensdiagramme zeigen, was geschieht: wer das System benutzt, wie ein Vorgang abläuft, wer wann mit wem kommuniziert.

Für den Lerntrainer ziehe ich aus beiden Familien: ein Strukturdiagramm für die Daten, drei Verhaltensdiagramme für Funktionen, Abläufe und Interaktion. Die folgenden vier Unterkapitel beschreiben jeden Typ nach demselben Muster: Zweck, zentrale Notationselemente, Grenzen. So lassen sich die Modellierungsentscheidungen später daraus ableiten.

#### 2.3.1 Use-Case-Diagramm

Das Use-Case-Diagramm beantwortet zwei Fragen. Wer nutzt das System? Was kann es? Das Verfahren geht auf Jacobson zurück, der die Methode bereits Anfang der 1990er-Jahre etabliert hat. Eine Idee treibt seinen Ansatz an: das System von außen denken, vom Nutzen her, nicht von der Technik. Oestereich und Scheithauer beschreiben es als Einstieg jeder Anforderungsanalyse.

Die Notation ist mit Absicht karg. Ein Akteur erscheint als Strichmännchen, eine Rolle außerhalb des Systems, ein Mensch oder ein anderes System. Der Anwendungsfall selbst: eine Ellipse. Die Systemgrenze: ein Rechteck, das alle Anwendungsfälle umschließt und das Innen vom Außen trennt. Eine schlichte Linie verbindet Akteur und Anwendungsfall zur Assoziation. Gerade diese Kargheit ist die Stärke, denn das Diagramm bleibt auch für Fachvertreter ohne Informatikhintergrund lesbar. Sie ist zugleich seine Grenze. Über das Wie eines Ablaufs sagt es nichts. Dafür sind Aktivitäts- oder Sequenzdiagramm da.

Zwischen Anwendungsfällen lassen sich drei Beziehungen modellieren, die ich später gezielt nutze: «include» für eine zwingend enthaltene Teilfunktion, «extend» für eine nur unter Bedingungen auftretende Erweiterung und die Generalisierung für eine Spezialisierung. Diese drei auseinanderzuhalten ist erfahrungsgemäß die eigentliche Hürde, und sie entscheidet darüber, ob ein Diagramm etwas aussagt oder bloß dekoriert. Ein verbreiteter Stolperstein dabei ist die Pfeilrichtung: Bei «include» zeigt der Pfeil vom Basisfall zum eingebundenen Anwendungsfall, bei «extend» läuft er genau umgekehrt, vom erweiternden Fall zurück zum Basisfall. Wer das verwechselt, dreht die Aussage um.

#### 2.3.2 Klassendiagramm

Das Klassendiagramm ist das wichtigste Strukturdiagramm der UML. In der Analysephase wird es Business Object Model genannt, weil es die fachlichen Gegenstände eines Systems abbildet und technische Details noch außen vor lässt. Eine Klasse erscheint als Rechteck mit drei Feldern: Name, Attribute, Operationen. Jedes Attribut trägt einen Datentyp, jede Operation eine Signatur; Sichtbarkeiten (öffentlich, privat, geschützt) regeln den Zugriff. Für ein reines Analysemodell wie das BOM treten die Sichtbarkeiten allerdings in den Hintergrund. Hier zählt zunächst die fachliche Struktur, noch nicht die Kapselung.

Den Kern bilden die Beziehungen. Die Assoziation verbindet zwei Klassen als gleichberechtigte Partner; ihre Multiplizitäten legen fest, wie viele Objekte der einen Seite mit wie vielen der anderen in Beziehung stehen. Hier lauert eine Hürde. Kleuker warnt nicht ohne Grund davor, diese Multiplizitäten zu unterschätzen: Ein Fehler hier pflanzt sich bis in die Datenbank fort. Für Teil-Ganzes-Beziehungen kennt die UML zwei Sonderformen der Assoziation. Die schwache Aggregation, bei der das Teil eigenständig fortbesteht. Und die starke Komposition, bei der das Teil mit dem Ganzen verschwindet und obendrein zu höchstens einem Ganzen gehören darf. Die Vererbung schließlich verbindet eine Unterklasse mit einer allgemeineren Oberklasse. Bei genau solchen Entscheidungen entpuppt sich Modellierung nicht als technisches Zeichnen, sondern als konzeptionelle Arbeit.

#### 2.3.3 Aktivitätsdiagramm

Das Aktivitätsdiagramm bildet Abläufe ab und ähnelt auf den ersten Blick einem Flussdiagramm, kann aber deutlich mehr. Eine Aktion erscheint als abgerundetes Rechteck, der Kontrollfluss als Pfeil. Ein ausgefüllter Kreis markiert den Startknoten, ein umrandeter Kreis mit Punkt den Endknoten. Ein Entscheidungsknoten, eine Raute, verzweigt den Fluss anhand einer Bedingung; ein passender Zusammenführungsknoten, ebenfalls eine Raute, führt die Zweige wieder zusammen. Für echte Parallelität sorgen Fork und Join, die mehrere Flüsse gleichzeitig starten und später synchronisieren.

Besonders nützlich sind die Schwimmbahnen. Sie ordnen jede Aktion einer verantwortlichen Rolle zu, und so wird auf einen Blick sichtbar, wer was tut. Für den Lerntrainer eignet sich das Diagramm ideal, um den Eingabe-Workflow einer Lernunit samt Fehlerfällen abzubilden. Seine Grenze: Es zeigt den Ablauf, nicht aber den zeitlich geordneten Nachrichtenaustausch zwischen konkreten Objekten. Dafür ist das Sequenzdiagramm zuständig.

#### 2.3.4 Sequenzdiagramm

Das Sequenzdiagramm gehört zu den Interaktionsdiagrammen. Es stellt dar, wer wann welche Nachricht an wen schickt. Jedes beteiligte Objekt besitzt eine Lebenslinie, eine senkrechte gestrichelte Linie, auf der ein Aktivierungsbalken markiert, wann das Objekt gerade aktiv ist. Entscheidend ist die Unterscheidung der Nachrichtentypen. Eine synchrone Nachricht (gefüllte Pfeilspitze) lässt den Sender warten, bis eine Antwort zurückkommt. Eine asynchrone Nachricht (offene Pfeilspitze) erlaubt dem Sender, sofort weiterzuarbeiten. Diesen Unterschied unterschätzte ich anfangs. Erst beim Modellieren wurde mir klar, wie sehr er das Verhalten des Systems prägt.

Seit UML 2 lassen sich mit kombinierten Fragmenten ganze Kontrollstrukturen abbilden: alt für sich gegenseitig ausschließende Alternativen, opt für einen optionalen Abschnitt, loop für Wiederholungen. Genau diese Fragmente brauche ich für die Mentoren-Auswertung. Die Stärke des Diagramms liegt in der präzisen zeitlichen Reihenfolge. Seine Grenze ist die Übersichtlichkeit. Bei vielen Objekten wird es schnell unleserlich.

### 2.4 Funktionale und nichtfunktionale Anforderungen

Bevor Anwendungsfälle und Klassen entstehen, lohnt sich ein Blick auf die Natur der Anforderungen selbst. Die Literatur trennt funktionale von nichtfunktionalen Anforderungen. Funktionale Anforderungen beschreiben, was ein System leisten soll, welche Funktionen es bereitstellt und wie es auf Eingaben reagiert. Nichtfunktionale Anforderungen beschreiben, wie gut es seine Aufgaben erfüllt, also Qualitätsmerkmale wie Leistung, Sicherheit, Benutzbarkeit oder Wartbarkeit.

„Das System ermittelt nach jeder eingegebenen Lernunit den Tages- und Wochensoll-Status" ist eine typische funktionale Anforderung; sie schlägt sich später unmittelbar in einem Anwendungsfall und einer «include»-Beziehung nieder. Gerade nichtfunktionale Anforderungen gehen in studentischen Arbeiten gern unter. Dabei entscheiden sie über Erfolg oder Misserfolg oft stärker als die reine Funktionalität. Aus meiner Praxis fallen mir für den Lerntrainer sofort drei ein.

Erstens der Datenschutz. Lerndaten sind personenbezogen, deshalb bekommt der Administrator bewusst keinen Zugriff auf individuelle Lernverläufe. Zweitens die Antwortzeit. Die Soll-Berechnung läuft nach jeder Eingabe und muss nahezu verzögerungsfrei erfolgen, sonst nervt die App im Alltag. Drittens die Benutzbarkeit. Die Zielgruppe sind nebenberuflich Studierende, die das Werkzeug zwischen Beruf und Lernen quetschen und keine Einarbeitungszeit haben.

Diese Trennung ist kein Selbstzweck. Sie erklärt, warum manche Anforderungen direkt als Anwendungsfall sichtbar werden, während andere, der Datenschutz etwa, sich eher in Strukturentscheidungen des Klassendiagramms verstecken.

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

Bevor das erste Diagramm entsteht, müssen Anforderungen erhoben, strukturiert und verstanden werden. Das International Requirements Engineering Board (IREB) definiert diese Tätigkeit in seinem Lehrplan als systematische Vorgehensweise zur Ermittlung, Dokumentation, Prüfung und Verwaltung von Anforderungen. Pohl und Rupp bezeichnen die Anforderungsanalyse zu Recht als eine der anspruchsvollsten Tätigkeiten der Softwareentwicklung überhaupt. Meine Berufspraxis bestätigt das. Wo Anforderungen unscharf bleiben, vervielfältigen sich Missverständnisse durch jede Projektphase. Mit messbaren Folgen.

Die Standish Group berichtet seit Jahrzehnten, dass unklare Anforderungen zu den Hauptgründen für Projektabbrüche zählen. Eine konsequente Anforderungsanalyse ist deshalb keine bürokratische Pflichtübung. Sie ist eine Investition, die sich in jeder folgenden Phase auszahlt. Genau darum nimmt sich diese Arbeit die Zeit, jeden Modellschritt aus den Anforderungen der Aufgabenstellung herzuleiten, statt direkt mit dem Zeichnen loszulegen.

### 2.6 Zwischenfazit

Die theoretischen Grundlagen verdichten sich auf drei Kernpunkte. Software-Engineering ist ein strukturiertes Vorgehen, dessen Wirksamkeit empirisch gestützt ist und dessen Vernachlässigung sich in den CHAOS-Daten der vergangenen drei Jahrzehnte ablesen lässt. Die UML ist der etablierte Standard für diese Strukturarbeit, nicht weil sie hübsch aussieht, sondern weil sie eine gemeinsame Sprache zwischen Fachlichkeit und Technik schafft. Und eine sorgfältige Anforderungsanalyse ist die Brücke zwischen Idee und Modell; sie entscheidet, ob die Modellierung trägt oder einbricht.

Damit ist auch der Übergang ins nächste Kapitel gesetzt. Bilden die Anforderungen das Fundament, dann muss die Modellierung deren Logik sichtbar machen. Das ist die Aufgabe der vier Diagramme im Anwendungsteil.

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

Simpel klingt das. Ist es aber nicht, sobald man die Details ernst nimmt. Pohl und Rupp nennen die Anforderungsanalyse nicht umsonst eine der anspruchsvollsten Tätigkeiten überhaupt, und im Verlauf dieser Arbeit hat sich das bestätigt.

Um den Rahmen abzustecken, zeigt Abbildung 1 zunächst den Domänenkontext: drei menschliche Akteure, das zu modellierende System, einen technischen Benachrichtigungsdienst als Umsystem. Diese Kontextsicht steht bewusst vor der detaillierten Modellierung, weil sie die Systemgrenze klärt, also die Frage, was zum Lerntrainer gehört und was draußen liegt. Der Benachrichtigungsdienst etwa ist ein technisches Umsystem. Der Lerntrainer nutzt ihn, aber er gehört nicht zur fachlichen Domäne und taucht deshalb später im Business Object Model nicht auf.

Mein Vorgehen folgte der inneren Logik der vier Modelle. Erst das Use-Case-Diagramm für die Funktionssicht, dann das Klassendiagramm für die Datenstruktur, anschließend das Aktivitätsdiagramm für einen Ablauf, zuletzt das Sequenzdiagramm für ein Interaktionsszenario. Die vier müssen zusammenpassen. Ein Akteur, der im Use-Case-Diagramm auftaucht, im Sequenzdiagramm aber fehlt, wäre ein Bruch. Wichtiger als das fertige Bild war mir dabei stets die Begründung. Warum diese Lösung und nicht eine der Alternativen?

### 3.2 Aufgabe A1 – Use-Case-Diagramm

#### 3.2.1 Akteure und Use Cases

Der Einstieg über Use Cases ist kein Zufall. Jacobson stellt den Anwendungsfall bewusst an den Anfang, das System wird von außen gedacht. Derselben Logik bin ich gefolgt. Vier Akteure ließen sich aus den Anforderungen herauslesen.

Der Benutzer ist die Hauptfigur. Er legt Pläne an, erfasst Lernunits, ruft Auswertungen ab. Der Administrator pflegt nur die systemweiten Vorlagen und bekommt bewusst keinen Einblick in persönliche Lerndaten, eine Trennung, die mir aus Datenschutzgründen wichtig war. Der Mentor unterstützt einzelne Studierende und handelt in deren Namen. Und das System selbst? Es tritt als Akteur auf, sobald es ohne menschliches Zutun reagiert, etwa wenn nach jeder Eingabe automatisch der Soll-Status berechnet wird.

Zuerst sah das Diagramm aus wie ein Spinnennetz. Fast jeder Akteur war mit fast jedem Use Case verbunden, die Linien kreuzten sich kreuz und quer, und das Bild sagte am Ende nichts mehr. Erst die Sortierung der Use Cases in fünf Gruppen brachte Ordnung hinein: Planverwaltung, Lernunit-Verwaltung, die systemgesteuerte Fortschrittskontrolle mit Zwischenbericht, Lob, Bonus und Warnung, dann die Auswertungen und schließlich die Administration. Diese Gruppierung stand in keiner Vorgabe. Sie entstand aus der Not, das Diagramm lesbar zu halten. Eine praktische Erkenntnis: Wird ein Modell unübersichtlich, fehlt ihm meist eine Strukturierungsebene.

#### 3.2.2 Beziehungen und ihre Begründung

An den Beziehungen entscheidet sich, ob ein Use-Case-Diagramm etwas aussagt oder nur dekoriert. Der Use Case „Lernunit eingeben" bindet „Zwischenbericht ermitteln" über «include» ein, denn das System berechnet nach jeder Eingabe zwingend den Soll-Status. Kein Sonderfall, sondern Kernlogik. Lob, Bonus und Überarbeitungswarnung dagegen hängen an «extend», weil sie nur unter Bedingungen feuern.

Hier lag übrigens meine erste Sackgasse. Zunächst hatte ich auch diese drei als «include» modelliert. Der Gedanke: Sie gehören ja „dazu". Beim zweiten Hinsehen merkte ich, dass das falsch ist. Ein Lob erscheint eben nicht immer, sondern nur bei erreichtem Tagessoll. Aus meiner Zeit im IT-Support kenne ich solche bedingten Abläufe gut: Eine automatische Eskalation wird auch nur ausgelöst, wenn ein Ticket eine Frist reißt, nicht bei jedem Ticket. Rupp et al. bestätigen die Faustregel, dass bedingte Erweiterungen der Lehrbuchfall für «extend» sind. Wichtig dabei: Basisfall ist „Zwischenbericht ermitteln", und die drei Erweiterungen docken an klar benannten Erweiterungspunkten an, etwa „Tagessoll geprüft".

Zwischen „Lernunit erstellen" und ihren beiden Varianten, individuell und aus Vorlage, besteht eine Generalisierung. Den Mentor schließlich modellierte ich als spezialisierten Benutzer, der dessen Use Cases erbt und um eigene Rechte ergänzt.

**Beziehungstypen im Use-Case-Diagramm (Tab. 3):**

| Beziehung | Wann angemessen | Beispiel im Lerntrainer |
|---|---|---|
| «include» | Teilfunktion zwingend enthalten | „Lernunit eingeben" ➜ „Zwischenbericht ermitteln" |
| «extend» | Erweiterung nur unter Bedingung | „Lob anzeigen" ➜ „Zwischenbericht ermitteln" bei Tagessoll |
| Generalisierung | Spezialfall mit gemeinsamer Wurzel | „Lernunit erstellen" – individuell vs. aus Vorlage |
| Akteur-Vererbung | Rolle erbt Funktionen einer anderen | Mentor erbt vom Benutzer und ergänzt eigene Rechte |

#### 3.2.3 Textuelle Ausarbeitung eines zentralen Use Cases

Ein Use-Case-Diagramm zeigt das Was, nicht das Wie. Um einen Anwendungsfall wirklich zu durchdringen, empfiehlt die Literatur ein zusätzliches Werkzeug: die textuelle Use-Case-Schablone. Ein strukturierter Steckbrief mit Vorbedingung, Standardablauf, Alternativabläufen und Nachbedingung. Pohl und Rupp betonen, dass erst diese Ausformulierung die im Diagramm verdichteten Beziehungen überprüfbar macht.

Ich habe das für „Lernunit eingeben" getan, den zentralen und am häufigsten ausgeführten Anwendungsfall. Die Schablone in Tabelle 4 schlägt zugleich die Brücke zum Aktivitätsdiagramm in Abschnitt 3.4, das denselben Ablauf grafisch aufgreift.

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

Beim Klassendiagramm bin ich an einer Stelle länger hängengeblieben: bei der Frage, wie Studierende und Mentoren zusammenhängen. Mein erster Reflex war, den Mentor von der Klasse Studierender erben zu lassen. Ein Mentor ist ja irgendwie auch an der Hochschule tätig. Je länger ich darüber nachdachte, desto schiefer kam mir das vor. Ein Mentor ist kein besonderer Studierender, und ein Studierender ist kein angehender Mentor. Die beiden teilen Eigenschaften, aber keiner ist dem anderen untergeordnet. Vererbung verlangt aber genau das, eine „ist-ein"-Beziehung, und die ist hier schlicht nicht gegeben.

Also verwarf ich diesen ersten Entwurf und führte stattdessen eine abstrakte Oberklasse Person ein, von der beide erben. Person trägt das gemeinsame Attribut name, ist aber selbst nicht instanziierbar. Ein Objekt im laufenden System ist immer konkret das eine oder das andere. Diese Lösung fühlt sich nicht nur sauberer an, sie ist es auch. Sie bündelt das Gemeinsame an einer Stelle, ohne eine falsche Hierarchie zu behaupten.

Der Rest ergab sich daraus. Studierender bekommt studienstart und studiengang sowie Referenzen auf genau einen Studienplan und beliebig viele Mentoren. Mentor ergänzt eintrittsdatum und fachrichtung. Der Studienplan bündelt die Lernpläne; der Lernplan trägt modulname, semester, ects und das Tages- sowie Wochensoll in Minuten. Eine bewusste Entscheidung war, das Soll in Minuten statt in Stunden zu speichern. Wer mit Zeiterfassung gearbeitet hat, kennt die Tücke: Rundungsfehler pflanzen sich fort und machen irgendwann die schönsten Auswertungen wertlos.

Knifflig wurde es bei der Lernunit. Sie beschreibt das Lehrmaterial, dokumentiert aber nicht das eigentliche Lernen. Dafür führte ich eine eigene Klasse Lernvorgang ein, denn wer sich an einem Tag dreimal hinsetzt, erzeugt drei Lernvorgänge, nicht einen. Die Lehrmaterialarten lagerte ich als Enumeration LehrmaterialTyp aus, wie die Aufgabenstellung verlangt.

#### 3.3.2 Komposition oder Aggregation – eine bewusste Abwägung

An keiner anderen Stelle des Modells habe ich so lange gegrübelt wie hier. Die Aufgabe verlangt mindestens eine Aggregation oder Komposition. Klingt nach einer Formalie, ist aber eine echte Entscheidung, und ich brauchte zwei Abende, bis ich sie für mich sauber begründen konnte.

Fangen wir mit dem klaren Fall an: Studienplan und Lernplan. Ein Lernplan ohne seinen Studienplan, ergibt das Sinn? Nein. Wird der Studienplan gelöscht, müssen die Lernpläne mit verschwinden. Hinzu kommt, dass ein Lernplan immer zu genau einem Studienplan gehört, nicht zu mehreren. Existenzielle Abhängigkeit plus exklusive Zugehörigkeit, das ist die Komposition im Lehrbuchsinn, und die ausgefüllte Raute am Studienplan bringt diese enge Bindung auf den Punkt.

Schwieriger war die Auswertung. Mein erster Entwurf hatte auch sie als Komposition am Mentor hängen. Die Logik dahinter: Der Mentor erstellt die Auswertung, also gehört sie ihm. Plausibel? Ja. Falsch? Auch ja. Denn eine Komposition würde bedeuten: Verlässt ein Mentor die Hochschule und sein Datensatz wird gelöscht, reißt er sämtliche Auswertungen mit sich. Das wäre fatal. Eine Auswertung dokumentiert den Lernfortschritt eines Studierenden. Sie muss erhalten bleiben, ganz gleich, ob der Mentor noch da ist oder nicht.

Am ersten Abend übersah ich das einfach. Erst am zweiten, als ich gedanklich durchspielte, was beim Löschen eines Mentors passiert, fiel der Groschen. Das war der Knackpunkt.

Also umgebaut: Aggregation, hohle Raute. Das Teil überlebt das Ganze. Eine kurz erwogene Zwischenlösung, die Auswertung beim Löschen einem „Sammel-Account" zuzuschlagen, verwarf ich, weil sie das Modell unnötig verkompliziert hätte. Die Aggregation erscheint mir am saubersten; ich halte sie für tragfähig.

Bleibt die dritte Beziehung: Lernplan zu Lernunit. Komposition? Aggregation? Tatsächlich weder noch. Eine Lernunit beschreibt Lehrmaterial, das sich auch für sich betrachten lässt, ohne an einem einzelnen Lernplan zu kleben, und durchaus in mehreren Plänen referenziert werden kann. Eine schlichte Assoziation reicht völlig. Hätte ich hier eine Komposition gesetzt, hätte ich das Modell überspezifiziert und mir eine Exklusivität eingehandelt, die fachlich gar nicht stimmt. Erst als ich die drei Fälle nebeneinanderlegte, feste Komposition, lose Aggregation, neutrale Assoziation, hat es bei mir wirklich klick gemacht.

#### 3.3.3 Fachliche und technische Sicht – eine bewusste Grenze

Ein Punkt verdient eine Klarstellung, weil er im Sequenzdiagramm später noch wichtig wird. Das Klassendiagramm liegt hier als Business Object Model vor. Es bildet bewusst nur die fachliche Domäne ab, also jene Gegenstände, über die auch ein Studierender oder ein Mentor sprechen würde: Lernplan, Lernunit, Auswertung. Oestereich und Scheithauer betonen, dass das Analysemodell von technischen Realisierungsdetails frei bleiben soll, weil diese erst in der Designphase hinzukommen.

Diese Trennung ist kein formaler Selbstzweck. Sie erklärt, warum ein technischer Hilfsdienst wie der Versand von Benachrichtigungen im BOM nichts zu suchen hat. Er ist kein fachliches Geschäftsobjekt, sondern ein Mittel zum Zweck. Im Sequenzdiagramm in Abschnitt 3.5 taucht ein solcher Dienst dennoch auf, weil dort der technische Ablauf gezeigt wird. Im fachlichen Datenmodell bleibt er bewusst draußen. Wer beide Sichten vermischt, bekommt ein Modell, das weder die Fachseite noch die Technik sauber bedient. Ein Fehler, den ich in echten Projekten mehr als einmal gesehen habe.

### 3.4 Aufgabe A3 – Aktivitätsdiagramm

Für das Aktivitätsdiagramm hatte ich die freie Wahl des Use Cases und entschied mich für „Lernunit eingeben". Warum gerade den? Weil ihn ein Nutzer am häufigsten ausführt, oft mehrmals täglich. Außerdem steckt in ihm mit den drei Soll-Prüfungen genug Entscheidungslogik, um ein Diagramm zu rechtfertigen, das mehr zeigt als eine simple Kette. Zwei Schwimmbahnen, Benutzer und System, trennen sauber, wer was tut.

Der Ablauf startet mit der Auswahl oder Neuanlage einer Lernunit. Der Nutzer erfasst die Lerndauer. Hier wollte die Aufgabe einen Fehlerfall sehen, und der naheliegendste fiel mir sofort ein: Was, wenn jemand versehentlich null Minuten oder einen negativen Wert eingibt? Ein Entscheidungsknoten fängt das ab, zeigt eine Fehlermeldung und schickt den Nutzer zurück zur Eingabe. Erst eine gültige Dauer führt hinüber in die System-Bahn.

Anders als zunächst gedacht, habe ich die drei Soll-Prüfungen nicht in einen einzigen Sammelknoten gepackt. Mein erster Entwurf tat genau das, ein Knoten, der „alle Ziele erreicht?" fragt. Zu grob. Tages-, Wochensoll und das 40-Stunden-Limit sind drei eigenständige Bedingungen mit drei eigenen Reaktionen (Lob, Bonus, Warnung), und genau das sollte das Diagramm zeigen. Also drei getrennte Entscheidungsknoten, nacheinander. In der System-Bahn entsteht zuerst der Lernvorgang, dann wird der Zwischenbericht ermittelt, und am Ende laufen alle Zweige über passende Zusammenführungsknoten in einem einzigen Endknoten zusammen.

### 3.5 Aufgabe A4 – Sequenzdiagramm

Das vierte Diagramm bildet den vorgegebenen Ablauf der Mentoren-Auswertung ab. Vier Lebenslinien sind beteiligt: :Studierender, :System, :Mentor und ein :NotificationService, den das System erst im Verlauf erzeugt.

Der Studierende bestellt synchron eine Auswertung, er wartet kurz auf die Bestätigung. Anschließend benachrichtigt das System den Mentor asynchron. Das war mir wichtig. Würde das System hier synchron warten, bliebe der Studierende blockiert, bis der Mentor reagiert, und das kann Stunden dauern. Asynchron darf er weiterarbeiten.

Der Mentor lädt synchron die Lernvorgangsdaten, schreibt sein Feedback und speichert es. Daraufhin erzeugt das System den NotificationService. Diese Kopplung ist bewusst so gewählt. Der NotificationService ist kein fachliches Geschäftsobjekt wie Lernplan oder Auswertung. Er ist ein rein technischer Dienst für den Versand. Deshalb taucht er im Business Object Model nicht auf, das BOM bildet absichtlich nur die fachliche Domäne ab. Im Sequenzdiagramm hingegen, das den technischen Ablauf zeigt, muss der Dienst sichtbar werden, und mit der «create»-Nachricht ist klar dokumentiert, dass das System ihn instanziiert und damit Verantwortung für seinen Lebenszyklus übernimmt.

Für die Benachrichtigung verlangte die Aufgabe „SMS oder E-Mail". Mein erster Gedanke war, das mit zwei separaten Nachrichten zu lösen, doch das hätte suggeriert, beide würden gesendet. Hier hakte ich kurz. Ein alt-Fragment ist genau das Richtige, weil es abhängig von einer Guard-Bedingung, etwa der hinterlegten Benachrichtigungspräferenz, genau eine der beiden Alternativen wählt. Den Timeout-Fall, der Mentor reagiert nicht rechtzeitig, packte ich in ein opt-Fragment mit erneuter Erinnerung. Zum Schluss ruft der Studierende die fertige Auswertung synchron ab.

---

## 4 Diskussion

### 4.1 Kritische Würdigung der Ergebnisse

Am Anfang stand eine textuelle Beschreibung, am Ende ein konsistentes UML-Modell aus vier Diagrammen. Jedes beleuchtet eine andere Seite des Lerntrainers, und doch greifen sie ineinander: Was das Use-Case-Diagramm an Funktionen verspricht, lösen Klassen-, Aktivitäts- und Sequenzdiagramm strukturell und dynamisch ein.

In der Praxis war der Weg holpriger, als diese Aufzählung vermuten lässt. Rückblickend waren es weniger die Diagramme selbst als die Entscheidungen dahinter, die mir etwas beigebracht haben. Im Use-Case-Diagramm lag der Schlüssel in der sauberen Rollentrennung und der bewussten Wahl zwischen «include», «extend» und Generalisierung. Im Klassendiagramm waren es die abstrakte Oberklasse Person und vor allem die Abwägung zwischen Komposition und Aggregation. Dass mich eine einzelne Raute so lange beschäftigen würde, hätte ich zu Beginn nicht gedacht. Das Aktivitätsdiagramm zwang mich, einen realistischen Fehlerfall mitzudenken. Das Sequenzdiagramm machte mir den Unterschied zwischen synchroner und asynchroner Kommunikation greifbarer, als es jede Definition gekonnt hätte.

Eine ehrliche Einschränkung gehört dazu. Meine Modellierung beruht allein auf einer schriftlichen Vorgabe. In einem echten Projekt würde ich mit künftigen Nutzern sprechen, Prototypen zeigen, nachjustieren. Aus der Berufspraxis weiß ich, wie viel sich an einem Modell verschiebt, sobald drei Fachexperten in einem Workshop draufschauen. Das ersetzt keine Modulhausarbeit, sollte aber als Hinweis stehen. Außerdem bleibt mein Modell auf der fachlichen Analyseebene. Die spannenden Architekturfragen, etwa welches Entwurfsmuster sich für die Benachrichtigungslogik anbietet (ein Observer drängt sich auf), habe ich bewusst ausgeklammert. Sie wären der logische nächste Schritt.

### 4.2 Modellierungswerkzeuge – eine Einordnung aus der Praxis

Ein Aspekt fehlt in der reinen Aufgabenstellung, entscheidet in der Praxis aber über Erfolg und Frust: die Wahl des Modellierungswerkzeugs. In meiner Zeit im IT-Consulting arbeitete ich mit professionellen Werkzeugen wie Enterprise Architect und Innovator. Beide sind mächtig. Sie halten ein gemeinsames Repository, prüfen die Konsistenz zwischen Diagrammen und erlauben es, ein Modellelement einmal anzulegen und in mehreren Diagrammen wiederzuverwenden. Diese Konsistenzprüfung ist Gold wert, sobald ein Modell über wenige Diagramme hinauswächst. Das deckt sich mit der Forderung der Literatur nach werkzeuggestützter Sicherung der Modellqualität.

Für eine Arbeit in diesem Umfang wäre so ein Schwergewicht jedoch überdimensioniert. Leichtgewichtige Werkzeuge erstellen Diagramme entweder grafisch oder, textbasiert, aus einer Beschreibungssprache, was Versionsverwaltung und schnelle Änderungen erleichtert. Der Preis: keine semantische Konsistenzprüfung. Ein grafisches Werkzeug zeichnet bereitwillig auch eine fachlich falsche Beziehung. Diese Erkenntnis prägte mein Vorgehen. Die Konsistenz zwischen den vier Diagrammen sicherte ich manuell, also genau jene Arbeit von Hand, die ein professionelles Werkzeug automatisiert. Für eine größere, nächste Iteration des Lerntrainers wäre der Umstieg auf ein Repository-basiertes Werkzeug der logische Schritt.

### 4.3 Fazit und Ausblick

Diese Hausarbeit startete mit einer einfachen Frage: Wie entsteht Struktur im Fernstudium? Über die UML-Modellierung landete ich bei einer anderen Einsicht. Gute Struktur erfordert vor allem sauberes Denken. Die vier Diagramme sind das Endprodukt, aber der eigentliche Wert steckt in den Überlegungen dahinter. Mit jedem Modell, das ich verwarf, wurde mein Verständnis klarer. Mit jeder Alternative, die ich durchspielte, wurde die endgültige Entscheidung tragfähiger.

Was käme nach dieser Modellierung? Mir schweben eine gamifizierte Fortschrittsanzeige vor und eine datengestützte Empfehlung, welche Lernunit als Nächstes dran wäre. Die Idee kommt nicht von ungefähr. Eine Metaanalyse von Sailer und Homner über zahlreiche Einzelstudien weist Gamification einen kleinen, aber stabilen positiven Effekt auf kognitive Lernergebnisse nach. Warum das funktioniert, erklärt die Selbstbestimmungstheorie von Deci und Ryan: Belohnungsmechaniken wirken nur, wenn sie die Grundbedürfnisse nach Kompetenz und Autonomie bedienen, statt sie zu untergraben. Das im Lerntrainer modellierte Lob bei erreichtem Tagessoll ist schon ein erster, kleiner Schritt in diese Richtung.

Der CHAOS-Report der Standish Group zeigt seit Jahrzehnten: Die wenigsten Software-Projekte scheitern an der Technik. Sie scheitern an unklaren Anforderungen und an fehlender Struktur. Meine Berufserfahrung unterstreicht das. Eine Hausarbeit lässt sich dazu nicht abschließend in Beziehung setzen, sie ist kein echtes Projekt. Aber die Methode überträgt sich: erst die Funktionen klären, dann die Daten, dann die Abläufe, dann die Interaktionen. Wer diese Reihenfolge beherzigt, hat eine deutlich bessere Ausgangslage als jemand, der gleich zu programmieren beginnt.

Eines nehme ich aus dieser Arbeit auf jeden Fall mit. Modelle sind keine bloße Formalität, die man abhakt, um endlich zum Programmieren zu kommen. Sie zwingen einen, Widersprüche zu sehen, bevor sie teuer werden. Und allein dafür hat sich die Mühe gelohnt. Die zwei Abende mit der Raute eingeschlossen.

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
