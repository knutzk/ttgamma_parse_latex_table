#!/usr/bin/python

import sys
import latex_table

if __name__ == "__main__":
    # Parse arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="the LaTeX input file to be parsed")

    # Add two mutually exclusive arguments: grouped/ungrouped
    parser_grouped = parser.add_mutually_exclusive_group()
    parser_grouped.add_argument("--grouped", help="group systematics", action="store_true")
    parser_grouped.add_argument("--ungrouped", help="do *not* group systematics", action="store_false")

    args = parser.parse_args()

    if args.grouped:
        print "Grouping systematics is not yet implemented"
        sys.exit(1)

    table = latex_table.readFromLatex(args.input)

    rows = table.getRows()
    columns = table.getColumns()
    dict = table.getEntries()

    for row in rows:
        for column in columns:
            print "%s %s %s" % (row, column, dict[row][column])
