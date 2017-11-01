#!/usr/bin/python

import sys
import latex_table
import table_to_file

if __name__ == "__main__":
    # Parse arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="the LaTeX input file to be parsed")

    # Add two mutually exclusive arguments: grouped/ungrouped
    parser_grouped = parser.add_mutually_exclusive_group()
    parser_grouped.add_argument("--grouped", help="group systematics", action="store_true")
    parser_grouped.add_argument("--ungrouped", help="do *not* group systematics", action="store_false")

    # Add optional arguments for file output
    parser.add_argument("--json", dest="json_file", help="output a JSON file")
    parser.add_argument("--tex", dest="tex_file", help="output a LaTeX file")

    args = parser.parse_args()

    if args.grouped:
        print "Grouping systematics is not yet implemented"
        sys.exit(1)

    table = latex_table.readFromLatex(args.input)

    rows = table.getRows()
    columns = table.getColumns()
    dict = table.getEntries()

    if args.json_file:
        table_to_file.storeJSON(table, args.json_file)
    if args.tex_file:
        table_to_file.storeTEX(table, args.tex_file)

    for row in rows:
        for column in columns:
            print "%s %s %s" % (row, column, dict[row][column])
