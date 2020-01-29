#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
test_data = [
    {
        "Transaction" : {
            "transaction_date" : "2015-12-23",
            "amount" : 9000.0,
            "security_amount" : None,
            "security_rate" : None
        },
        "Account" : {
            "name" : "Sparkonto"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "dec-jan"
        },
        "TransactionType" : {
            "name" : "Insättning"
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2015-12-23",
            "amount" : 1337.0,
            "security_amount" : None,
            "security_rate" : None
        },
        "Account" : {
            "name" : "ISK"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "dec-jan"
        },
        "TransactionType" : {
            "name" : "Insättning"
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2015-12-21",
            "amount" : None,
            "security_amount" : 75.0,
            "security_rate" : 69.82
        },
        "Account" : {
            "name" : "ISK"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Privatekonomi software group AB"
        },
        "TransactionType" : {
            "name" : "Split"
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2015-12-21",
            "amount" : None,
            "security_amount" : -15.0,
            "security_rate" : 349.1
        },
        "Account" : {
            "name" : "ISK"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Privatekonomi software group AB"
        },
        "TransactionType" : {
            "name" : "Split"
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2015-12-14",
            "amount" : -1234.0,
            "security_amount" : 15.0,
            "security_rate" : 346.5
        },
        "Account" : {
            "name" : "ISK"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Privatekonomi software group AB"
        },
        "TransactionType" : {
            "name" : "Köp"
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2015-11-30",
            "amount" : -123.0,
            "security_amount" : None,
            "security_rate" : None
        },
        "Account" : {
            "name" : "Sparkonto"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Preliminär skatt, ränta"
        },
        "TransactionType" : {
            "name" : "Räntor"
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2015-11-30",
            "amount" : 1.23,
            "security_amount" : None,
            "security_rate" : None
        },
        "Account" : {
            "name" : "Sparkonto"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "Intjänad ränta"
        },
        "TransactionType" : {
            "name" : "Räntor"
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2015-11-30",
            "amount" : 1500,
            "security_amount" : None,
            "security_rate" : None
        },
        "Account" : {
            "name" : "Sparkonto"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "nov-dec"
        },
        "TransactionType" : {
            "name" : "Insättning"
        }
    },
    {
        "Transaction" : {
            "transaction_date" : "2015-11-30",
            "amount" : 3000,
            "security_amount" : None,
            "security_rate" : None
        },
        "Account" : {
            "name" : "ISK"
        },
        "Currency" : {
            "code" : "SEK"
        },
        "SecurityProvider" : {
            "name" : "nov-dec"
        },
        "TransactionType" : {
            "name" : "Insättning"
        }
    }
]