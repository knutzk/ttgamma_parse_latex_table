#!/usr/bin/python

import sys
import latex_table
from syst_calculator import SystDictionary
import dict_to_file


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
        dict = SystDictionary("syst_dictionary.json")
        systs = dict.getSystematics()
        sys.exit(1)

    # ======================================================
    # Start the main execution here
    # ======================================================
    table = latex_table.readFromLatex(args.input)


    if args.json_file:
        dict_to_file.storeJSON(table.getEntries(), args.json_file)
    if args.tex_file:
        dict_to_file.storeTEX(table.getEntries(), args.tex_file)

    rows = table.getRows()
    columns = table.getColumns()
    dict = table.getEntries()

    for row in rows:
        for column in columns:
            print "%s %s %s" % (row, column, dict[row][column])
