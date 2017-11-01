#!/usr/bin/python

import latex_table
import json

def storeJSON(table, file_string):
    with open(file_string, 'w') as fp:
        json.dump(table.getEntries(), fp, indent=4)

def storeTEX(table, file_string):
    with open(file_string, 'w') as fp:

        fp.write("\\begin{tabular}\n")
        fp.write("\\end{tabular}\n")
