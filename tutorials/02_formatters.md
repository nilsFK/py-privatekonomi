Formatters (formaterare) tar datastrukturer som har semantisk betydelse men som saknar korrekt formatering. Formaterarens indata är den parsade råa texten samt en uppsättning av semantiska namn. Dess utdata är den formaterade indatan.

Exempel:

```
parsed_text, formatters = parser.parse(rawtext)
```

där `parsed_text` är den parsade råa texten och `formatters` är den semantiska uppsättningen av namn.

En implementation av en formaterare utövar formatering på den parsade texten i en viss bestämd ordning. Denna ordning bestäms av den uppsättning av semantiska namn som vi talade om tidigare.