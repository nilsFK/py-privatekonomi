py-privatekonomi
================
Parsar, formatterar och sparar undan transaktionsloggar från diverse källor, däribland Swedbank. Ytterligare stöd kan tillkomma.

Installation
------------
**TODO**

Användning
----------
> privatekonomi.py source

där source är sökvägen till filen som innehåller transaktionerna. Transaktionerna kopieras helt enkelt in i en fil som vi därefter läser in via source.

För ytterligare instruktioner, kör:

> privatekonomi.py -h

Exempel
-------
> privatekonomi.py samples/sample1 -f swedbank -p whitespace

Status
------
* Total refaktorisering kommer genomföras.
* För närvarande endast stöd för Swedbank.
* Lägg till stöd för exporterade Swedbankfiler (kontohistorik).
* Modeller
* Annat gott och blandat!

Att göra
--------
* Total refaktorisering

Stöd
----
Siktar på stöd för Python 2.7.x+
