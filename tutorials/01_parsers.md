Parsers är den huvudsakliga konstruktionen i py-privatekonomi. De ansvarar för att transformera rå text till en datastruktur som är grunden för att formateras vidare. Parsern ger alltså den råa texten semantik genom att mappa ett meningsfullt namn till data.

För att parsningen skall genomföras behöver vi veta vad det är vi parsar. Denna omfattning av olika uppbyggnader av rå text ger upphov till olika parsers som parsar på olika sätt.

Inbygda parsers finns i katalogen /core/parsers/, däribland `regex_parser` och `swedbank_parser`. T.ex. så är `swedbank_parser` specialiserad på att parsa rå text som är tillgänglig från swedbank, medan `regex_parser` har som fundamental uppgift att omvandla rå text till användarbart innehåll genom att applicera reguljära uttryck.

Användardefinierade parsers sparas i katalogen /parsers/.

Vissa parsers är mer grundläggande än andra. T.ex. så är `regex_parser` mer grundläggande än `swedbank_parser`, då `swedbank_parser` använder sig utav `regex_parser` för att parsa den råa texten.

Parsern returnerar dels den parsade råa texten, samt även en uppsättning av semantiska namn, så kallade subformatterare. Dessa appliceras i tur och ordning, så det är väsentligt i vilken ordning de specificeras i.

Exempel:

subformatters = [
    "transaction_amount",
    "transaction_reference",
    None, # skicka None för data som inte används vid formatering
    "account_current_balance"
]

Eftersom subformatteraren är en ordnad datastruktur så är den i praktiken en array med namn/textsträngar. Dessa namn är välkända och används av formatteraren för att formatera den parsade datan, se nästa del för ytterligare information.
