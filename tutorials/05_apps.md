Katalogen apps/ innehåller färdiga implementationer som kan köras.

Ett standardexempel ingår i form av main.py som helt enkelt skapar en parser och en formaterare med möjlighet att spara undan resultatet till databasen. Denna app används som default när vi kör privatekonomi.py på kommandoraden. Se README.md för ytterligare exempel.

Vid implementation av en app måste man implementera åtminstone en metod med signaturen:
```python
execute(source, parser, formatter)
```

om man skickar med --persist=true behöver man även en metod med signaturen:
```python
persist(output)
```
