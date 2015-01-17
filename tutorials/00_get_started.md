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
6. Notera var på filsystemet filen finns och kör py-privatekonomi.py enligt:

