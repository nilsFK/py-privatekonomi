#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
try:
    import xlrd
except:
    raise Exception("xlrd is required for excel files and is not installed, please run pip install -r requirements.txt")
def get_content(fname, sheet_num):
    book = xlrd.open_workbook(fname)
    sh = book.sheet_by_index(sheet_num)
    content = []
    for rowx in range(sh.nrows):
        content.append([])
        for colx in range(sh.ncols):
            cell_value = sh.cell(rowx, colx).value
            if sh.cell_type(rowx, colx) == xlrd.XL_CELL_DATE:
                try:
                    year, month, day, hour, minute, second = xlrd.xldate_as_tuple(cell_value, book.datemode)
                    cell_value = datetime.datetime(year, month, day, hour, minute, second)
                except xlrd.XLDateError as e:
                    return False
            content[rowx].append(cell_value)
    return content
