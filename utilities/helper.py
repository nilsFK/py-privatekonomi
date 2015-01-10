import factories.account_formatter_factory
import factories.account_parser_factory

def get_parser(acc_type):
    return factories.account_parser_factory.AccountParserFactory().createAccountParser(acc_type)

def get_formatter(acc_type):
    return factories.account_formatter_factory.AccountFormatterFactory().createAccountFormatter(acc_type)