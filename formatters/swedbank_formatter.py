#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Formats input to a data structure according to the
# input acquired from Swedbank transactions
import sys, time
from collections import deque
import gen_formatter
class SwedbankFormatter(gen_formatter.GenFormatter):
    def __init__(self):
        self.formatters = [
            "accounting_date",
            "transaction_date",
            "account_event",
            "amount",
            "balance"
        ]

    def format(self, input):
        output = []
        for i in input:
            deq = deque(self.formatters)
            items = {}
            for token in i:
                if token == ' ':
                    continue
                meth = deq.popleft()
                formatted_token = getattr(self, "format_%s" % meth)(token)
                items[meth]= formatted_token
            output.append(items)
        return output

    def format_accounting_date(self, content):
        ret_content = content
        print "format_accounting_date %s" % repr(content)
        ret_content = ret_content.strip()
        ret_content = time.strptime(ret_content, "%y-%m-%d")
        return ret_content

    def format_transaction_date(self, content):
        ret_content = content
        print "format_transaction_date %s" % repr(content)
        ret_content = ret_content.strip()
        ret_content = time.strptime(ret_content, "%y-%m-%d")
        return ret_content

    def format_account_event(self, content):
        ret_content = content
        print "format_account_event %s" % repr(content)
        ret_content = ret_content.strip()
        return ret_content

    def format_amount(self, content):
        ret_content = content
        print "format_amount %s" % repr(content)
        return super(SwedbankFormatter, self).format_currency(ret_content)

    def format_balance(self, content):
        ret_content = content
        print "format_balance %s" % repr(content)
        return super(SwedbankFormatter, self).format_currency(ret_content)
