#!/usr/bin/python

import latex_table

if __name__ == "__main__":
    # Parse arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="the LaTeX input file to be parsed")
    args = parser.parse_args()

    table = latex_table.readFromLatex(args.input)

    rows = table.getRows()
    columns = table.getColumns()
    dict = table.getEntries()

    for row in rows:
        for column in columns:
            print "%s %s %s" % (row, column, dict[row][column])
