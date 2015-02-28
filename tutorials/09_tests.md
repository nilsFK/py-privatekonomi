Katalogen tests/ innehåller enhetstester och försäkrar om att koden är fullt fungerande. Exempel:

```bash
export PYTHONPATH=.
python tests/test_swedbank.py
```

för att köra igenom hela testsviten:

```bash
python -m unittest discover tests
```