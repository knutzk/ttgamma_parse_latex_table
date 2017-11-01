#!/usr/bin/python

import json

# A simple class to read in a JSON file that holds list of systematic
# groups. This class reads in the JSON file, and inverts the
# dictionary to look up groups for systematics.
class SystDictionary():
    _groups = []       #List of all groups
    _systematics = []  #List of all systematics
    _inv_dict = {}     #Reverse dictionary to look up groups

    def __init__(self, file_string):
        with open(file_string, 'r') as data_file:
            data = json.load(data_file)
        for g in data:
            self._groups.append((g))
            for s in data[g]:
                self._inv_dict[s] = g
                self._systematics.append(s)

    def getGroup(self, syst):
        return self._inv_dict[syst]

    def getSystematics(self):
        return self._systematics
