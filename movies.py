import requests
import json
import sqlite3
import pprint

url = 'https://test.biografklubdanmark.dk/api/v1/apps/movies'

r = requests.get(url)

data =r.json()
#movies = json.dumps(data, indent=2)
#pprint.pprint(data)

print(type(data))





