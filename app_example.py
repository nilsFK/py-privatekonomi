import privatekonomi as pe

# Config
institution = "swedbank"
source = "samples/swedbank/sample1"
persist = True

# Config app
app = pe.App()
app.setFormatter(institution)
app.setParser(institution)
app.setSource(source)
app.setPersist(persist)

# Build and run app
app.build()
data = app.run()

print data
