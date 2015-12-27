#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
            "name" : u"Insättning"
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
            "name" : u"Insättning"
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
            "name" : u"Split"
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
            "name" : u"Privatekonomi software group AB"
        },
        "TransactionType" : {
            "name" : u"Split"
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
            "name" : u"Köp"
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
            "name" : u"Preliminär skatt, ränta"
        },
        "TransactionType" : {
            "name" : u"Räntor"
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
            "name" : u"Intjänad ränta"
        },
        "TransactionType" : {
            "name" : u"Räntor"
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
            "name" : u"nov-dec"
        },
        "TransactionType" : {
            "name" : u"Insättning"
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
            "name" : u"nov-dec"
        },
        "TransactionType" : {
            "name" : u"Insättning"
        }
    }
]