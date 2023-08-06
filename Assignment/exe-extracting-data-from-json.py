# Importing necessary libraries/modules
from urllib.request import urlopen
import urllib.parse, urllib.error
import json

# Requesting user input for a URL
url = input("Enter location: ")

# Setting a default URL for testing/debugging if user input is empty
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1856260.json"

# Printing a message to indicate that data retrieval is in progress
print(f"Retrieving: {url}")

# Opening the URL, reading its contents, and converting it from bytes to a string
jsn = urlopen(url).read().decode()

# Printing the number of characters retrieved
print(f"Retrieved {len(jsn)} characters")

# Parsing the retrieved string data as JSON objects and storing it in the 'data' variable
data = json.loads(jsn)

# Initializing variables to count and sum the 'count' values from the 'comments' list
total = 0
count = 0

# Looping through each 'comment' in the 'comments' list and counting the total number of comments and summing up their 'count' values
for comment in data['comments']:
    count += 1
    total += int(comment['count'])

# Printing the count of comments and their total sum
print(f"Count: {count}\nSum: {total}")
