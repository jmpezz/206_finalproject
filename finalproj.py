##Name: Julia Pezzullo

import itertools
import json
import sqlite3

access_token = e02e6ffe7f3f4170b916faeff4f98d19


CACHE_FNAME = "206_FinalProject_cache.json"
# Put the rest of your caching setup here:
try:
	cache_file = open(CACHE_FNAME, 'r') #attempting to read data from file
	cache_data = cache_file.read() #if data there, get into string
	cache_file.close() #close the file, data is now in dictionary
	CACHE_DICTION = json.loads(cache_data) #load data into dictionary
except:
	CACHE_DICTION = {}


