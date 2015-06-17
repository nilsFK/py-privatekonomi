En app i Privatekonomi.py tar emot resultatet av parsningen/formateringen samt har även möjlighet att spara resultatet till databas.

Standardexempel finns att tillgå i katalogen py_privatekonomi/core/apps.
Ett standardexempel ingår i form av example1.py som helt enkelt skapar en parser och en formaterare. Detta exempel kräver inte att man har SQLAlchemy installerat.

För att köra standardexempel #1 (example1), skriv in:

```
python privatekonomi.py samples/swedbank/sample1 -p swedbank -f swedbank -a py_privatekonomi.core.apps.example1
```

Notera att för att köra standardexempel så måste vi ange prefix `py_privatekonomi.core.apps.`

Vid implementation av en app måste man implementera åtminstone en metod med signaturen:
```python
execute(sources, parser, formatter, configs)
```

om man skickar med --persist behöver man även en metod med signaturen:
```python
persist(output, configs)
```

Det går även att skapa fristående appar. Se app_example.py för hur sådana fungerar.