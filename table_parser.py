#!/usr/bin/python

from latex_table import Table

table = Table()
table.registerColumn('had-fakes')
table.registerColumn('e-fakes')
table.addRow(["btagSF", 3, 16])
table.addRow(["muonSF", 5, 3])

rows = table.getRows()
columns = table.getColumns()
dict = table.getEntries()

for row in rows:
    for column in columns:
        print "%s %s %s" % (row, column, dict[row][column])
