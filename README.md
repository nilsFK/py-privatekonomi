py-privatekonomi
================
Parsar, formatterar och sparar undan transaktionsloggar från diverse källor, däribland Swedbank.

Installation
------------
> pip install -r requirements.txt

För att persista data, skapa en fil med namnet db.ini i katalogen configs med innehållet:

```
[Database]
engine = engine
username = username
password = password
host = host
port = port
database = database
```

engine utgörs av dialect+driver.
Se följande länk för exempel på dialect+driver:
    http://docs.sqlalchemy.org/en/rel_0_9/dialects/index.html

Notera att dessa kan installeras via **requirements.txt**

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
> python privatekonomi.py samples/swedbank/sample1 -f swedbank -p swedbank -a main --persist

Projektstatus
-------------
* Total refaktorisering kommer genomföras.
* För närvarande endast stöd för Swedbank.

Stöd
----
Siktar på stöd för Python 2.7.x+. Ordentligt stöd för Python 3.x.x kommer senare, är för närvarande att betraktas som otestat.
