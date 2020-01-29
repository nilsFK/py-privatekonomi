#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import py_privatekonomi.core.parser
import csv
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from py_privatekonomi.utilities import common
import sys
class CsvParser(py_privatekonomi.core.parser.Parser):
    def __init__(self):
        pass

    def parse(self, contents, dialect = 'excel', opts = {}):
        rows = []
        for content in contents:
            content = common.decode(content)
            c = StringIO(content)
            options = {
                'delimiter' : str(','),
                'quoting' : csv.QUOTE_ALL
            }
            options.update(opts)

            if sys.version < '3':
                reader = self.unicode_csv_reader(c, dialect=dialect, **options)
            else:
                reader = self.csv_reader(c, dialect=dialect, **options)

            for row in reader:
                if self.is_empty_row(row):
                    # empty rows are usually rows that have been deleted from within Excel
                    # but still remains in the file as empty strings, ignore these for now
                    continue
                rows.append(row)
        return rows

    def csv_reader(self, data, dialect, **kwargs):
        reader = csv.reader(data, dialect=dialect, **kwargs)
        for row in reader:
            yield [cell for cell in row]

    def unicode_csv_reader(self, unicode_csv_data, dialect=csv.excel, **kwargs):
        # csv module doesn't do Unicode; encode temporarily as UTF-8:
        csv_reader = csv.reader(self.utf_8_encoder(unicode_csv_data),
                                dialect=dialect, **kwargs)
        for row in csv_reader:
            # decode UTF-8 back to Unicode, cell by cell:
            yield [unicode(cell, 'utf-8') for cell in row]

    def utf_8_encoder(self, unicode_csv_data):
        for line in unicode_csv_data:
            yield line.encode('utf-8')

    def is_empty_row(self, row):
        for col in row:
            if len(col) > 0:
                return False
        return True
