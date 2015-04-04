#!/usr/bin/env python
# -*- coding: utf-8 -*-
test_data = [
    {
        "Transaction" : {
            "accounting_date" : "2015-01-05",
            "transaction_date" : "2015-01-03",
            "reference" : u"PATREON.COM",
            "amount" : -8.02
        },
        "Currency" : {
            "code" : "USD"
        },
        "Account" : {
            "name" : "Mitt vanliga konto",
            "account_code" : "12345",
            "account_number" : "1234567890"
        },
        "TransactionType" : {
            "name" : u"Kortköp/uttag"
        }
    },
    {
        "Transaction" : {
            "accounting_date" : "2015-01-02",
            "transaction_date" : "2015-01-02",
            "reference" : u"PATREON.COM",
            "amount" : -7.96
        },
        "Currency" : {
            "code" : "SEK"
        },
        "Account" : {
            "name" : "Mitt vanliga konto",
            "account_code" : "12345",
            "account_number" : "1234567890"
        },
        "TransactionType" : {
            "name" : u"Kortköp/uttag"
        }
    },
    {
        "Transaction" : {
            "accounting_date" : "2015-01-02",
            "transaction_date" : "2015-01-02",
            "reference" : u"ICA SUPERMARKET",
            "amount" : -93.97
        },
        "Currency" : {
            "code" : "SEK"
        },
        "Account" : {
            "name" : "Mitt vanliga konto",
            "account_code" : "12345",
            "account_number" : "1234567890"
        },
        "TransactionType" : {
            "name" : u"Kortköp/uttag"
        }
    },
    {
        "Transaction" : {
            "accounting_date" : "2015-01-02",
            "transaction_date" : "2015-01-01",
            "reference" : u"ICA SUPERMARKET",
            "amount" : -88.6
        },
        "Currency" : {
            "code" : "SEK"
        },
        "Account" : {
            "name" : "Mitt vanliga konto",
            "account_code" : "12345",
            "account_number" : "1234567890"
        },
        "TransactionType" : {
            "name" : u"Bankomatuttag"
        }
    },
    {
        "Transaction" : {
            "accounting_date" : "2015-01-02",
            "transaction_date" : "2014-12-31",
            "reference" : u"ICA SUPERMARKET",
            "amount" : -315.29
        },
        "Currency" : {
            "code" : "SEK"
        },
        "Account" : {
            "name" : "Mitt andra konto",
            "account_code" : "23456",
            "account_number" : "2345678901"
        },
        "TransactionType" : {
            "name" : u"Kortköp/uttag"
        }
    },
    {
        "Transaction" : {
            "accounting_date" : "2014-12-29",
            "transaction_date" : "2014-12-27",
            "reference" : u"SPOTIFY Spotify",
            "amount" : -49.0
        },
        "Currency" : {
            "code" : "USD"
        },
        "Account" : {
            "name" : "Mitt andra konto",
            "account_code" : "23456",
            "account_number" : "2345678901"
        },
        "TransactionType" : {
            "name" : u"Kortköp/uttag"
        }
    },
    {
        "Transaction" : {
            "accounting_date" : "2014-12-29",
            "transaction_date" : "2014-12-24",
            "reference" : u"ELGIGANTEN STOC",
            "amount" : -1490.0
        },
        "Currency" : {
            "code" : "SEK"
        },
        "Account" : {
            "name" : "Mitt andra konto",
            "account_code" : "23456",
            "account_number" : "2345678901"
        },
        "TransactionType" : {
            "name" : u"Kortköp/uttag"
        }
    },
    {
        "Transaction" : {
            "accounting_date" : "2014-12-23",
            "transaction_date" : "2014-12-23",
            "reference" : u"HBONORDIC.COM",
            "amount" : -79.0
        },
        "Currency" : {
            "code" : "SEK"
        },
        "Account" : {
            "name" : "Mitt andra konto",
            "account_code" : "23456",
            "account_number" : "2345678901"
        },
        "TransactionType" : {
            "name" : u"Kortköp/uttag"
        }
    },
    {
        "Transaction" : {
            "accounting_date" : "2014-12-23",
            "transaction_date" : "2014-12-23",
            "reference" : u"BAR BQ BAR & GRI",
            "amount" : -72.0
        },
        "Currency" : {
            "code" : "SEK"
        },
        "Account" : {
            "name" : "Mitt andra konto",
            "account_code" : "23456",
            "account_number" : "2345678901"
        },
        "TransactionType" : {
            "name" : u"Kortköp/uttag"
        }
    },
    {
        "Transaction" : {
            "accounting_date" : "2014-12-23",
            "transaction_date" : "2014-12-23",
            "reference" : u"COOP KONSUM",
            "amount" : -103.94
        },
        "Currency" : {
            "code" : "SEK"
        },
        "Account" : {
            "name" : "Mitt andra konto",
            "account_code" : "23456",
            "account_number" : "2345678901"
        },
        "TransactionType" : {
            "name" : u"Bankomatuttag"
        }
    },
    {
        "Transaction" : {
            "accounting_date" : "2014-12-22",
            "transaction_date" : "2014-12-22",
            "reference" : u"",
            "amount" : -1000.0
        },
        "Currency" : {
            "code" : "USD"
        },
        "Account" : {
            "name" : "Mitt tredje konto",
            "account_code" : "34567",
            "account_number" : "3456789012"
        },
        "TransactionType" : {
            "name" : u"Bankomatuttag"
        }
    },
]