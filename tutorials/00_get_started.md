Transaktionsloggar
==================
Transaktionsloggar kan sparas var som helst i filsystemet och laddas in av py-privatekonomi. Om det fattas stöd för formatering och parsning av en viss typ av transaktionslogg kan man enkelt lägga till stöd för dessa genom att bygga ut py-privatekonomi med ytterligare formaterare och parsers.

Swedbank
--------
För att hämta transaktionsloggar, följ dessa steg:

1. Logga in på Swedbank
2. Gå in på ditt konto
3. Till höger har du Sök transaktioner på kontot. Välj intervall för bokföringsdatum och klicka på Sök
4. Klicka därefter på Exportera
5. På nästa sida: välj Oformaterad text och klicka på Exportera
6. Notera var på filsystemet filen finns och kör privatekonomi.py enligt:
```bash
python privatekonomi.py sökväg/till/transaktionslogg -p swedbank -f swedbank -a py_privatekonomi.core.apps.example1
```

Avanza
------
För att hämta transaktionsloggar från Avanza, följ dessa steg:

1. Logga in på Avanza
2. Gå till ditt konto
3. Välj fliken Transaktioner
4. Välj datumintervall
5. Klicka på Exportera transaktioner till Excel
6. Notera var på filsystemet filen finns och kör privatekonomi.py enligt:
```bash
python privatekonomi.py sökväg/till/transaktionslogg -p avanza -f avanza -a py_privatekonomi.core.apps.example1
```

ini-filer
=========
Istället för att skicka in en direkt sökväg till transaktionsfilen kan man skicka in en sökväg där py-privatekonomi letar upp alla filer som matchar de villkor som anges i ini-filen. ini-filen kan innehålla följande:

```
[Source]
dir=/sökväg/till/transaktionsloggar
suffix=.txt
prefix=sample
filename_like=sample
exact_match=/sökväg/till/transaktionsloggar/sample.txt
```

där:

* dir = sökvägen till var transaktionsloggarna finns
* suffix = matchar alla filer med ett visst suffix
* prefix = matchar alla filer med ett visst prefix
* filename_like = matchar alla filer som innehåller ett visst ord
* exact_match = matchar exakt på en viss fil

Notera att exact_match har företräde över övriga alternativ, vilket medför att den endast kan användas exklusivt.

För att använda ini-filer, gör följande:

1. Skapa en ny fil configs/, t.ex my_source.ini
2. Konfigurera my_source.ini med ovanstående alternativ
3.  Kör följande:
```bash
python py-privatekonomi.py my_source.ini -p swedbank -f swedbank -a py_privatekonomi.core.apps.example1
```

