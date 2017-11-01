#!/usr/bin/python

import latex_table
import json

def storeJSON(table, file_string):
    with open(file_string, 'w') as fp:
        json.dump(table.getEntries(), fp, indent=4)
