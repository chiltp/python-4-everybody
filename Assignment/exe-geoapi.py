# Importing necessary libraries/modules
from urllib.request import urlopen
from urllib.parse import urlencode
import urllib.error
import json

# Initializing a dictionary with a 'key' parameter
param = {'key': 42}

# Requesting user input for an address
url = input("Enter location: ")

# Initializing the first half of the URL for the web service
serviceurl = "http://py4e-data.dr-chuck.net/json?"

# Adding the 'address' parameter to the dictionary
param['address'] = url

# Setting a default address if user input is empty
if len(url) < 1:
    param['address'] = "University of Malaya"

# Combining the two halves of the URL to create the complete URL
url = serviceurl + urlencode(param)

# Printing a message to indicate that data retrieval is in progress
print(f"Retrieving {url}")

# Opening the URL, reading its contents, and converting it to a string
jsn = urlopen(url).read().decode()

# Printing a message to indicate that data retrieval is complete and showing the length of the retrieved data
print(f"Retrieved {len(jsn)} characters")

# Loading the string data into a JSON format
data = json.loads(jsn)

# Uncomment the line below to see the JSON data structure
# print(json.dumps(data, indent=2))

# Locating the 'place_id' key in the JSON data and storing its value
placeID = data["results"][0]["place_id"]

# Printing the place ID retrieved from the JSON data
print(f"Place id {placeID}")
