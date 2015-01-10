from factories.account_formatter_factory import AccountFormatterFactory
from factories.account_parser_factory import AccountParserFactory

def get_parser(acc_type):
    return AccountParserFactory().createAccountParser(acc_type)

def get_formatter(acc_type, formatters):
    return AccountFormatterFactory().createAccountFormatter(acc_type, formatters)