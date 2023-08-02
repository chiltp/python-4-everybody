# required libraries/modules
from urllib.request import urlopen
import urllib.parse, urllib.error
import json

# request for URL
url = input("Enter location: ")

# default URL for testing/debugging
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1856260.json"

# print 'Receiving' message to match sample execution
print(f"Retrieving: {url}")

# open URL. Read it in and convert it from byte to string type
jsn = urlopen(url).read().decode()

# counting total number of characters read
print(f"Retrieving {len(jsn)} characters")

# prime 'data' to parse string as json objects
data = json.loads(jsn)

# looping through list of 'comments' and count+summing all 'count' values
total = 0
count = 0
for comment in data['comments']:
    count += 1
    total += int(comment['count'])

# formatted output to match sample execution
print(f"Count: {count}\nSum: {total}")