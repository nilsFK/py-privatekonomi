import privatekonomi as pe
from core import config

# Config
institution = "swedbank"
source = "samples/swedbank/sample2"
persist = True

# Config app
app = pe.App()
app.setFormatter(institution)
app.setParser(institution)
app.setSource(source)
db_config = config.readConfig("db", "Database")
app.persistWith(db_config)
default_config = pe.get_default_config()
default_config['use_logging'] = True
default_config['log_to_file'] = False
default_config['insert_rows'] = 100
app.config(default_config)
print(repr(app))
# Build and run app
app.build()
data = app.run()

print(data)
