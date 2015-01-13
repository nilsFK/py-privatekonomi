Formatters (formaterare) tar datastrukturer som har semantisk betydelse men som saknar korrekt formatering. Formaterarens indata är den parsade råa texten samt en uppsättning av semantiska namn (så kallade *subformatters*). Dess utdata är den formaterade indatan.

Exempel:

```python
parsed_text, subformatters = parser.parse(raw_text)
formatted_data = formatter.format(parsed_text, subformatters)
```

där `parsed_text` är den parsade råa texten och `subformatters` är den semantiska uppsättningen av namn.

En implementation av en formaterare utövar formatering på den parsade texten i en viss bestämd ordning. Denna ordning bestäms av den uppsättning av semantiska namn som vi talade om tidigare, d.v.s. `subformatters`.

Formaterare som ingår som en del av kärnan finns sparade i katalogen core/formatters/. Användardefinierade formaterare skaps i root-katalogen /formatters/.
