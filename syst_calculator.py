#!/usr/bin/python

import json

# A simple class to read in a JSON file that holds list of systematic
# groups. This class reads in the JSON file, and inverts the
# dictionary to look up groups for systematics.
class SystDictionary():
    _groups = []       #List of all groups
    _systematics = []  #List of all systematics
    _dict = {}         #Normal dictionary to look up systematics of a group
    _inv_dict = {}     #Reverse dictionary to look up group of a systematic

    def __init__(self, file_string):
        with open(file_string, 'r') as data_file:
            self._dict = json.load(data_file)
        for g in self._dict:
            self._groups.append((g))
            for s in self._dict[g]:
                self._inv_dict[s] = g
                self._systematics.append(s)

    # Look up a systematic in the inverse dictionary.
    def lookupSystematic(self, syst):
        return self._inv_dict[syst]

    # Look up a group in the dictionary.
    def lookupGroup(self, group):
        return self._dict[group]

    # Return a list of all systematics.
    def getSystematics(self):
        return self._systematics
