#!/usr/bin/python

import json

def storeJSON(dict, file_string):
    with open(file_string, 'w') as fp:
        json.dump(dict, fp, indent=4)

def storeTEX(dict, file_string):
    with open(file_string, 'w') as fp:
        fp.write("\\begin{tabular}\n")
        fp.write("  \\hline\n")
        fp.write("  ")
        # First we need to write out the headers
        for row in dict:
            for column in dict[row]:
                fp.write("& %s " % (column))
            fp.write("\\\\\n")
            break
        fp.write("  \\hline\n")

        # Now read all rows and output them as well
        for row in dict:
            fp.write("  %s " % (row))
            for column in dict[row]:
                fp.write("& %s " % dict[row][column])
            fp.write("\\\\\n")
        fp.write("  \\hline\n")
        fp.write("\\end{tabular}\n")
