# LaTeX Table Parser

Parse a LaTeX table of systematics, group them and output them in a nice format. Execute with:
```
python table_parser.py [input_file]
```
where _input_file_ is a tex file that contains _tabular_ environments. The script searches for these environment and parses the first (1) tabular enviornment found in the file. Information is then stored in a dictionary.

To get some help, execute:
```
python table_parser.py --help
```

The parsed info can be outputted in two data formats:
- tex: this basically redoes a _tabular_ environment and outputs the dictionary into it
- json: dump the dictionary into a json-formatted file

Grouping of systematics is not yet implemented...
