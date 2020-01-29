#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
test_data = [
    {
        "Transaction" : {
            "transaction_date" : "2015-01-08",
            "amount" : -1286.75,
            "security_amount" : 4.0726,
            "security_rate" : 413.68
        },
        "Account" : {
            "name" : "Spar Aktie"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Aktiefond #1"
        },
        "TransactionType" : {
            "name" : "Sälj"
        },
        "TransactionData" : {
            "ISIN" : "SE0000000001",
            "courtage" : 10.50
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2015-01-07",
            "amount" : -1329.5,
            "security_amount" : 15.1663,
            "security_rate" : 222.17
        },
        "Account" : {
            "name" : "Spar Aktie"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Aktiefond #2"
        },
        "TransactionType" : {
            "name" : "Köp"
        },
        "TransactionData" : {
            "ISIN" : "SE0000000002",
            "courtage" : 20
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2015-01-07",
            "amount" : -682.61,
            "security_amount" : 0.8534,
            "security_rate" : 1974
        },
        "Account" : {
            "name" : "Spar Aktie"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Aktiefond #3"
        },
        "TransactionType" : {
            "name" : "Köp"
        },
        "TransactionData" : {
            "ISIN" : "SE0000000003",
            "courtage" : 30.50
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2015-01-05",
            "amount" : 2728.8,
            "security_amount" : None,
            "security_rate" : None
        },
        "Account" : {
            "name" : "Spar Aktie"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Insättning Januari"
        },
        "TransactionType" : {
            "name" : "Insättning"
        },
        "TransactionData" : {
            "ISIN" : "SE0000000004",
            "courtage" : 40
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2014-12-08",
            "amount" : -1144.98,
            "security_amount" : 5.1423,
            "security_rate" : 222.66
        },
        "Account" : {
            "name" : "Spar Aktie"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Aktiefond #2"
        },
        "TransactionType" : {
            "name" : "Köp"
        },
        "TransactionData" : {
            "ISIN" : "SE0000000005",
            "courtage" : 50.50
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2014-11-26",
            "amount" : 2145.42,
            "security_amount" : None,
            "security_rate" : None
        },
        "Account" : {
            "name" : "Spar Aktie"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Insättning November"
        },
        "TransactionType" : {
            "name" : "Insättning"
        },
        "TransactionData" : {
            "ISIN" : "SE0000000006",
            "courtage" : 60
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2014-10-29",
            "amount" : -863.81,
            "security_amount" : 16.2254,
            "security_rate" : 114.87
        },
        "Account" : {
            "name" : "Spar Aktie"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Aktiefond #3"
        },
        "TransactionType" : {
            "name" : "Köp"
        },
        "TransactionData" : {
            "ISIN" : "SE0000000007",
            "courtage" : 70.50
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2014-10-28",
            "amount" : -862.99,
            "security_amount" : 8.7321,
            "security_rate" : 213.35
        },
        "Account" : {
            "name" : "Spar Aktie"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Aktiefond #2"
        },
        "TransactionType" : {
            "name" : "Köp"
        },
        "TransactionData" : {
            "ISIN" : "SE0000000008",
            "courtage" : 80
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2014-10-27",
            "amount" : 2826.80,
            "security_amount" : None,
            "security_rate" : None
        },
        "Account" : {
            "name" : "Spar Aktie"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Insättning Oktober"
        },
        "TransactionType" : {
            "name" : "Insättning"
        },
        "TransactionData" : {
            "ISIN" : "SE0000000009",
            "courtage" : 90.50
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2014-10-02",
            "amount" : -10218.04,
            "security_amount" : 149.8263,
            "security_rate" : 114.92
        },
        "Account" : {
            "name" : "Spar Aktie"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Aktiefond #1"
        },
        "TransactionType" : {
            "name" : "Köp"
        },
        "TransactionData" : {
            "ISIN" : "SE00000000010",
            "courtage" : 100
        }
    },
]