#!/usr/bin/python

import latex_table

if __name__ == "__main__":
    table = latex_table.readFromLatex("table.tex")

    rows = table.getRows()
    columns = table.getColumns()
    dict = table.getEntries()

    for row in rows:
        for column in columns:
            print "%s %s %s" % (row, column, dict[row][column])
