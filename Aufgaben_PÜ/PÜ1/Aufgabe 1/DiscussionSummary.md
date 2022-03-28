## Project background

### Purpose of project

Eine Software zur Überprüfung und Darstellung Patienabhängiger Leistungsdaten. Die Analyse wird anhand eines Leistungstests am Ergometer durchgeführt. 

### Scope of project

Die Software ist auf jedes Fitnesslevel der Probanden anwendbar und dient zur Überprüfung der Vitalparameter unter Anstrengung. Die Vitalparameter werden mit passenden Messgeräten aufgezeichnet. Die Schwierigkeitsstufe wird dabei auf den jeweiligen Probanden individuell eingestellt.
### Other background information

Das System soll eine korrekte Datenverarbeitung gewährleisten.

## Perspectives
### Who will use the system?

Das System kann von Diagnostikern, Therapeuten oder Ärzten sowohl für Rehabilitations- als auch für Trainingszwecke für ihre Patienten verwendet werden.

### Who can provide input about the system?

Personen, die mit der Auswertung der dargestellten Daten arbeiten oder mit der Auswertung beschäftigt sind. Erfahrungen während der Nutzung können zur Verbesserung der Software beitragen. 


## Project Objectives
### Known business rules

t.b.d

### System information and/or diagrams

Beispiel von aufgezeichneten EKG Daten

![](ekg_example.png)

Aus diesem muss die Herzrate bestimmt werden.

### Assumptions and dependencies

Ein auf den Patienten angepasster Schwierigkeitsgrad muss verwendet werden, um die Durchführbarkeit der Tests zu gewährleisten. Eine richtige Anwendung der Messinstrumente ist erforderlich. 

Analyse der Daten:
Zum einen werden Daten wie, Name, Geburtsjahr, das Leistungslevel in Watt und die Testdauer in Sekunden von der Testperson aufgenommen. Der Test dauert bei jeder Person 180 Sekunden. Sekündlich werden die getretenen Watt am Fahrradergometer gemessen und Visuell in einem Graph dargestellt. Die csv Datei beinhaltet zwei Spalten mit Daten. Wobei die EKG-Daten in millisekunden aufgelöst sind. Dabei ist in der ersten Spalte der Zeitstempel (in 180 Sekunden werden 180 000 Messpunkte erfasst)

### Design and implementation constraints

Ein einfach zu bedienendes Benutzer-Interface.

## Risks

Bei nicht korrekt angepasstem Schwierigkeitsgrad kann es zu einer Überanstrengung des Patienten führen.

## Known future enhancements

t.b.d

## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues

...
