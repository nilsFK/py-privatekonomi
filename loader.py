import importlib
from utilities import common
def load_app(app, source, parser, formatter, persist = False):
    safe_module = common.path_leaf(app)
    if not safe_module.startswith("core.apps"):
        safe_module.replace(".", "")
        safe_module = "apps.%s" % safe_module
    app = importlib.import_module("%s" % safe_module)
    output = getattr(app, 'execute')(source, parser, formatter)
    if persist:
        getattr(app, 'persist')(output)
