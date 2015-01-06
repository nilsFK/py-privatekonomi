py-privatekonomi
================
Parsar, formatterar och sparar undan transaktionsloggar från diverse källor, däribland Swedbank. Ytterligare stöd kan tillkomma.

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
> privatekonomi.py source -f formatter -p parser --persist=true|false

där
* source: obligatorisk. sökvägen till filen som innehåller transaktionerna.
* formatter: obligatorisk. formaterar innehållet från source
* parser: obligatorisk. parsar det formaterade innehållet från source
* persist: valfri. sparar undan resultatet i databas, förutsätter att db.ini är konfigurerad

För ytterligare instruktioner, kör:

> privatekonomi.py -h

Exempel
-------
> privatekonomi.py samples/swedbank/sample1 -f swedbank -p whitespace

Projektstatus
-------------
* Total refaktorisering kommer genomföras.
* För närvarande endast stöd för Swedbank.

Stöd
----
Siktar på stöd för Python 2.7.x+. Ordentligt stöd för Python 3.x.x kommer senare, är för närvarande att betraktas som otestat.
