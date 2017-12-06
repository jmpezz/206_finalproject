##Name: Julia Pezzullo

import itertools
import json
import sqlite3
import datetime
from urllib.request import urlopen

access_token = "25880197.9d22fc1.264658484e9142b190635083bfd474aa"

#time, caption length, likes, hashtags, comments, type, location, user tags
#
with urlopen('https://api.instagram.com/v1/users/self/media/recent/?access_token=25880197.9d22fc1.264658484e9142b190635083bfd474aa') as response:
	str_response = response.read().decode('utf-8')
	obj = json.loads(str_response)

	for ob in obj['data']:
		print (ob)

CACHE_FNAME = "206_FinalProject_cache.json"

try:
	cache_file = open(CACHE_FNAME, 'r') #attempting to read data from file
	cache_data = cache_file.read() #if data there, get into string
	cache_file.close() #close the file, data is now in dictionary
	CACHE_DICTION = json.loads(cache_data) #load data into dictionary
except:
	CACHE_DICTION = {}


conn = sqlite3.connect('206_FinalProject.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS InstagramDB')
cur.execute('CREATE TABLE InstagramDB (date_time DATETIME, caption_length INTEGER, likes INTEGER, tags TEXT, comments INTEGER, type TEXT, location TEXT, tagged_users TEXT)')

for info in obj['data']:
	date_posted = datetime.datetime.fromtimestamp(int(str(info['created_time'])))
	caption_len = len(info['caption']['text'])
	likes = info['likes']['count']
	hashtags = info['tags']
	comments = info['comments']['count']
	type_post = info['type']
	try:
		location = info['location']['name']
	except:
		location = 'No Named Location'
	if len(info['users_in_photo']) == 0:
		tagged_users = "No tagged users"

	else:
		for user in info['users_in_photo']:
			tagged_users= []
			tagged_users.append(user['user']['full_name'])


			#tagged_users.append(user['user']['full_name'])
	print (tagged_users)






