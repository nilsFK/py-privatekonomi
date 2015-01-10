Parsers är den huvudsakliga konstruktionen i py-privatekonomi. De ansvarar för att transformera rå text till en datastruktur som är grunden för att formateras vidare. Parsern ger alltså den råa texten semantik genom att mappa ett meningsfullt namn till data.

För att parsningen skall genomföras behöver vi veta vad det är vi parsar. Denna omfattning av olika uppbyggnader av rå text ger upphov till olika parsers som parsar på olika sätt.

Inbygda parsers finns i katalogen parsers/, däribland regex_parser och swedbank_parser. T.ex. så är swedbank_parser specialiserad på att parsa rå text som är tillgänglig från swedbank, medan regex_parser har som fundamental uppgift att omvandla rå text till användarbart innehåll genom att applicera reguljära uttryck.

Vissa parsers är mer grundläggande än andra. T.ex. så är regex_parser mer grundläggande än swedbank_parser, då swedbank_parser använder sig utav regex_parser för att parsa den råa texten.