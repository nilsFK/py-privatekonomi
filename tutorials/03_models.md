Models (eller modeller) är den huvudsakliga konstruktionen för att spara undan rå text som har blivit parsad och formaterad.

Katalogen py_privatekonomi/core/models/ innehåller alla implementationer av en viss Model.

Notera att första gången en model används (d.v.s. instantieras) kommer den generera motsvarande tabeller. Vissa tabeller har beroenden till andra tabeller (via foreign keys), så ordningen modeller skapas är viktig.
