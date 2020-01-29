from __future__ import absolute_import
from __future__ import unicode_literals
try:
    # 2.x.x
    from ConfigParser import SafeConfigParser as config_parser
except:
    # 3.x.x
    from configparser import ConfigParser as config_parser

def readConfig(name, section):
    config = config_parser()
    configs = config.read("configs/" + name + ".ini")
    if hasattr(config, 'items'):
        return dict(config.items(section))
    else:
        return dict(config[section])
