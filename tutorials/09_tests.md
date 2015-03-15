Katalogen tests/ innehåller enhetstester och försäkrar om att koden är fullt fungerande. Exempel:

```bash
export PYTHONPATH=.
python tests/test_swedbank.py
```

för att köra igenom hela testsviten:

```bash
python -m unittest discover tests
```

Som default kör den inte igenom tester som är beroende av databasen, dessa skrivs istället ut som "Skipping ...". För att testa mot databas behöver man i första hand lägga till en fil med namnet "db_test.ini" i katalogen configs. Denna skall bestå av samma innehåll som db.ini, fast peka ut den databas som används för tester.

Notera att när databastesterna körs så kommer samtliga tabeller tas bort och byggas upp igen. Var därför noggrann med att inte peka ut en produktionsdatabas.