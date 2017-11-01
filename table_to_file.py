#!/usr/bin/python

import latex_table
import json

def storeJSON(table, file_string):
    with open(file_string, 'w') as fp:
        json.dump(table.getEntries(), fp, indent=4)

def storeTEX(table, file_string):
    with open(file_string, 'w') as fp:
        fp.write("\\begin{tabular}\n")
        fp.write("  \\hline\n")
        fp.write("  ")
        # First we need to write out the headers
        for row in table.getEntries():
            for column in table.getEntries()[row]:
                fp.write("& %s " % (column))
            fp.write("\\\\\n")
            break
        fp.write("  \\hline\n")
        fp.write("\\end{tabular}\n")
