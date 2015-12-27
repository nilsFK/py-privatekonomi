py-privatekonomi
================
py-privatekonomi håller reda på din privatekonomi genom att läsa in transaktionsloggar från din bank, konvertera detta till ett strukturerat format och, om du vill, sparar ner resultatet i en databas.

Installation
------------
> pip install -r requirements.txt

eller

> python -m pip install -r requirements.txt

Om resultatet skall sparas till databas kör följande:

> pip install -r persist_requirements.txt

eller

> python -m pip install persist_requirements.txt

För att persista data, skapa en fil med namnet db.ini i katalogen configs med innehållet:

```
[Database]
engine = engine
username = username
password = password
host = host
port = port
database = database
prefix = ekonomi
```

engine utgörs av dialect+driver.
Se följande länk för exempel på dialect+driver:
    http://docs.sqlalchemy.org/en/rel_0_9/dialects/index.html

Notera även att till skillnad från övriga konfigurationer är `prefix` valfri och utgör endast ett prefix till tabellerna.

Användning
----------
> python privatekonomi.py [-h] source -f FORMATTER -p PARSER -a APP [--persist]

där
* **source**: obligatorisk. sökvägen till filen som innehåller transaktionerna.
* **FORMATTER**: obligatorisk. formaterar innehållet från source
* **PARSER**: obligatorisk. parsar det formaterade innehållet från source
* **APP**: obligatorisk. den app som används för att ta emot det parsade och formatterade innehållet.
* **persist**: valfri. sparar undan resultatet i databas; förutsätter att db.ini är korrekt konfigurerad.

För ytterligare instruktioner, kör:

> python privatekonomi.py -h

Exempel
-------
> python privatekonomi.py samples/swedbank/sample1 -f swedbank -p swedbank -a py_privatekonomi.core.apps.example1

Projektstatus
-------------
* Stöd för Swedbank (ordinarie textexporter)
* Stöd för Avanza (ordinarie csv-filer, excel-filer)

Stöd
----
Testas regelbundet för Python 2.7.x och 3.3.x
