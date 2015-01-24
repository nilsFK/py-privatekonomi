Mappers fungerar som ett klister mellan formatteraren och databasen.

Det går att märka upp subformatters med mappers, exempelvis:

```python
    @AccountMapper("Account", "name")
    def format_account_name(self, content, subformatter):
        """ Konto: namn """
        return content.strip()
```

Notera att AccountMapper används som decorator på subformatterare enligt formatet:
`@AccountMapper(model_name, model_col)`

där `model_name` är namnet på modellen och `model_col` är den kolumn som värdet mappas till.

En mapper definierar även upp en uppsättning av modeller som den känner till och kan nås via den statiska metoden `getModelNames`, exempelvis:

```python
AccountMapper.getModelnames()
```

Inbyggda mappers finns sparade i core/mappers/, medan användardefinierade mappers finns i /mappers/.