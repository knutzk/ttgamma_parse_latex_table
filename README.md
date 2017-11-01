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

The grouping of systematics is entirely based on the file [syst_dictionary.json]. This file contains JSON-formatted groups of systematics, which are used as a look-up table by the table parser. The following options are available:
- grouped: perform the grouping as defined in the dictionary file
- ungrouped: do _not_ perform grouping; this parses the input, but doesn't manipulate it. Good for writing into different formats.
