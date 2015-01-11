En app i Privatekonomi.py tar emot resultatet av parsningen/formatteringen samt har även möjlighet att spara resultatet till databas.

Standardexempel finns att tillgå i katalogen core/apps.
Ett standardexempel ingår i form av example1.py som helt enkelt skapar en parser och en formaterare. Detta exempel kräver inte att man har SQLAlchemy installerat.

För att köra standardexempel #1 (example1), skriv in:

```
python privatekonomi.py samples/swedbank/sample1 -p swedbank -f swedbank -a core.apps.example1
```

Notera att för att köra standardexempel så måste vi ange prefix `core.apps.`

Vid implementation av en app måste man implementera åtminstone en metod med signaturen:
```python
execute(source, parser, formatter)
```

om man skickar med --persist behöver man även en metod med signaturen:
```python
persist(output)
```

Egna appar skapas direkt i katalogen apps/. T.ex. så kan man skapa en modul med namnet myapp.py, vilket kan köras med:

```
python privatekonomi.py samples/swedbank/sample1 -p swedbank -f swedbank -a myapp
```