py-privatekonomi
================
Parsar, formatterar och sparar undan transaktionsloggar från diverse källor, däribland Swedbank. Ytterligare stöd kan tillkomma.

Installation
------------
> pip install -r requirements.txt

För att persista data, skapa en fil med namnet db.ini i katalogen configs med innehållet:

[Database]
    engine = engine
    username = username
    password = password
    host = host
    port = port
    database = database

engine utgörs av dialect+driver.
Se följande länk för exempel på dialect+driver:
    http://docs.sqlalchemy.org/en/rel_0_9/dialects/index.html
Notera att dessa kan installeras via **requirements.txt**

Användning
----------
> privatekonomi.py source -f formatter -p parser

där
* source: sökvägen till filen som innehåller transaktionerna.
* formatter: formaterar innehållet från source
* parser: parsar det formaterade innehållet från source

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
