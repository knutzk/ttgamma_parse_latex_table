#!/usr/bin/python

# This class holds a table in form of a dictionary. Columns are
# registered first, then rows can be added (which should have the same
# number of entries as columns are registered).
class Table():
    _dictionary = {}
    _rows = []
    _columns = []

    # Register a new column.
    def registerColumn(self, name):
        self._columns.append(name)

    # Add a row to the table.
    def addRow(self, entries = []):
        row_name = entries.pop(0)
        # Make sure that #entries fits #registered columns
        if not len(entries) == len(self._columns):
            print "Trying to add a row with too many entries"
            return
        # Add entries to dictionary
        self._rows.append(row_name)
        self._dictionary[row_name] = dict()
        for (i, e) in enumerate(entries):
            self._dictionary[row_name][self._columns[i]] = e

    # Give me the list of rows.
    def getRows(self):
        return self._rows

    # Give me the list of columns.
    def getColumns(self):
        return self._columns

    # Give me the whole dictionary.
    def getEntries(self):
        return self._dictionary



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
