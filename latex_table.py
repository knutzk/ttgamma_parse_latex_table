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


# Internal function to find a tabular environment. This removes all
# lines before and after it (including the begin/end commands).
def _find_tabulars(lines):
    beginning = [i for (i, string) in enumerate(lines) if "\\begin{tabular}" in string]
    del lines[:beginning[0]+1]
    end = [i for (i, string) in enumerate(lines) if "\\end{tabular}" in string]
    del lines[end[0]:]
    return lines


# This function reads a LaTeX document, parses the first (!) occurence
# of a 'tabular' object and returns it as a Table object.
def readFromLatex(tex_file_string):
    with open(tex_file_string, 'r') as tex_file:
        lines = tex_file.readlines()
        # Remove everything but the tabular
        lines = _find_tabulars(lines)
        # Remove lines with '\hline'
        lines = [l for l in lines if l.find("\\hline")]
        # Remove end-of-line commands and the ' \\'
        lines = [l.strip()[:-3] for l in lines]

        # Remove the first line which contains the headers, remove all
        # its whitespace, split it at '&' and save this nicely.
        headers = lines.pop(0)
        headers = [h.strip() for h in headers.split('&')]
        del headers[0]

        lines = [l.split(" & ") for l in lines]

        # Now save everything in a table object
        table = Table()
        for h in headers:
            table.registerColumn(h)
        for l in lines:
            table.addRow(l)
        return table

# end of file
