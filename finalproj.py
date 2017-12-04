##Name: Julia Pezzullo

import itertools
import json
import sqlite3
from urllib.request import urlopen

access_token = "25880197.9d22fc1.264658484e9142b190635083bfd474aa"

#time, caption length, likes, filter, hashtags, comments, type, location, user tags
#
with urlopen('https://api.instagram.com/v1/users/self/media/recent/?access_token=25880197.9d22fc1.264658484e9142b190635083bfd474aa') as response:
	str_response = response.read().decode('utf-8')
	obj = json.loads(str_response)

	for ob in obj['data']:
		print (ob)

CACHE_FNAME = "206_FinalProject_cache.json"
# Put the rest of your caching setup here:
try:
	cache_file = open(CACHE_FNAME, 'r') #attempting to read data from file
	cache_data = cache_file.read() #if data there, get into string
	cache_file.close() #close the file, data is now in dictionary
	CACHE_DICTION = json.loads(cache_data) #load data into dictionary
except:
	CACHE_DICTION = {}


