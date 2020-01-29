#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
test_data = [
    {
        "Transaction" : {
            "accounting_date" : "2016-03-02",
            "transaction_date" : "2016-03-02",
            "security_amount" : 34.0,
            "security_rate" : 123.1,
            "amount" : -4224.0
        },
        "TransactionData" : {
            "identifier" : "306246150",
            "liquidity_date" : "2016-03-04",
            "type" : "Aktie",
            "ISIN" : "SE0006993986",
            "interest" : 0,
            "fee" : 39.0,
            "purchase_value" : 4224.0,
            "results" : 0.0,
            "total_amount" : 34.0,
            "exchange_rate" : 1.0,
            "transaction_text" : None,
            "cancellation_date" : None,
            "verification_no" : "532740700"
        },
        "Account" : {
            "current_balance" : 102.0
        },
        "Currency" : {
            "code" : "SEK"
        },
        "TransactionType" : {
            "name" : "KÖPT"
        },
        "SecurityProvider" : {
            "name" : "BETS B"
        }
    },
    {
        "Transaction" : {
            "accounting_date" : "2016-02-29",
            "transaction_date" : "2016-02-29",
            "security_amount" : 0,
            "security_rate" : 0,
            "amount" : 4326.0
        },
        "TransactionData" : {
            "identifier" : "305477335",
            "liquidity_date" : "2016-02-29",
            "type" : None,
            "ISIN" : None,
            "interest" : 0,
            "fee" : 0.0,
            "purchase_value" : 0.0,
            "results" : 0.0,
            "total_amount" : 0.0,
            "exchange_rate" : 1.0,
            "transaction_text" : "SPARA",
            "cancellation_date" : None,
            "verification_no" : "213067130"
        },
        "Account" : {
            "current_balance" : 4326.0
        },
        "Currency" : {
            "code" : "SEK"
        },
        "TransactionType" : {
            "name" : "INSÄTTNING"
        },
        "SecurityProvider" : {
            "name" : ""
        }
    }
]