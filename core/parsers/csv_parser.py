#!/usr/bin/env python
# -*- coding: utf-8 -*-
import core.parser
import csv
import StringIO
from utilities import common

class CsvParser(core.parser.Parser):
    def __init__(self):
        pass

    def parse(self, contents, dialect = 'excel', opts = {}):
        rows = []
        for content in contents:
            content = common.decode(content)
            c = StringIO.StringIO(content)
            options = {
                'delimiter' : ',',
                'quoting' : csv.QUOTE_ALL
            }
            options.update(opts)
            try:
                reader = self.unicode_csv_reader(c, dialect=dialect, **options)
            except:
                reader = csv.reader(c, dialect=dialect, **options)
            for r in reader:
                rows.append(r)
        return rows

    def unicode_csv_reader(self, unicode_csv_data, dialect=csv.excel, **kwargs):
        # csv.py doesn't do Unicode; encode temporarily as UTF-8:
        csv_reader = csv.reader(self.utf_8_encoder(unicode_csv_data),
                                dialect=dialect, **kwargs)
        for row in csv_reader:
            # decode UTF-8 back to Unicode, cell by cell:
            yield [unicode(cell, 'utf-8') for cell in row]

    def utf_8_encoder(self, unicode_csv_data):
        for line in unicode_csv_data:
            yield line.encode('utf-8')
